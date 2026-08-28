// Fails the build if any content file that will actually render in
// production still contains a "[COMPLETAR]" placeholder.
//
// Two different rendering rules apply (see src/content.config.ts /
// src/lib/content.ts for the full rationale):
//   - Singletons that always render regardless of `estado` — the 4
//     01-paginas-unicas/*.md files, every `_hub.md`, and the always-loaded
//     00-config/{site,navegacion}.md — are checked unconditionally.
//   - Repeatable collection items (verticales/modulos/casosDeExito/blog
//     posts) only ever render once `estado: "publicado"`, so those are
//     only checked in that state.
// `_PLANTILLA*.md` files and the editorial-only 00-config docs
// (ctas-reutilizables.md, voz-y-tono.md) are never loaded by the build at
// all, so they're excluded entirely.
//
// Runs standalone (not through astro:content) so it can execute before
// Astro even starts, as the package.json "prebuild" step.
import fg from 'fast-glob';
import matter from 'gray-matter';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const contentRoot = path.resolve(__dirname, '..', '..', 'content');

const NEVER_LOADED = new Set(['00-config/ctas-reutilizables.md', '00-config/voz-y-tono.md']);

function alwaysRenders(relativePath) {
  return (
    relativePath.startsWith('01-paginas-unicas/') ||
    relativePath.endsWith('/_hub.md') ||
    relativePath === '00-config/site.md' ||
    relativePath === '00-config/navegacion.md'
  );
}

const files = await fg('**/*.md', {
  cwd: contentRoot,
  ignore: ['**/_PLANTILLA*.md'],
});

const failures = [];

for (const relativePath of files) {
  if (NEVER_LOADED.has(relativePath)) continue;

  const fullPath = path.join(contentRoot, relativePath);
  const raw = fs.readFileSync(fullPath, 'utf-8');
  const { data } = matter(raw);

  const mustCheck = alwaysRenders(relativePath) || data.estado === 'publicado';
  if (mustCheck && raw.includes('[COMPLETAR')) {
    failures.push({ relativePath, alwaysRenders: alwaysRenders(relativePath) });
  }
}

if (failures.length > 0) {
  console.error('\n❌ [COMPLETAR] placeholder found in file(s) that render in production:\n');
  for (const f of failures) {
    const reason = f.alwaysRenders ? 'always renders (singleton/hub/config)' : 'estado: "publicado"';
    console.error(`   - content/${f.relativePath}  [${reason}]`);
  }
  console.error('\nFinish the content, or (for gated content) set estado back to "borrador"/"revision".\n');
  process.exit(1);
}

console.log(`✅ Content QA passed (${files.length} files checked).`);
