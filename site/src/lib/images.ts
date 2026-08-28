import type { ImageMetadata } from 'astro';

// Real binaries (once available) live under src/assets/content/, mirroring
// the content/ folder structure. Frontmatter gives plain string paths, so
// they're resolved dynamically via import.meta.glob (Astro's documented
// pattern for this), not static ESM imports.
const images = import.meta.glob<{ default: ImageMetadata }>(
  '/src/assets/content/**/*.{jpg,jpeg,png,webp,svg}'
);

/**
 * Resolves a content frontmatter image path to optimizable image metadata.
 * Returns undefined for anything not yet available (most fields are still
 * literally "[COMPLETAR]" while content is in borrador state) — every
 * image-consuming component must have a placeholder fallback branch.
 */
export async function resolveImage(path?: string | null): Promise<ImageMetadata | undefined> {
  if (!path || path.includes('[COMPLETAR') || path.trim() === '') return undefined;
  const key = `/src/assets/content/${path}`;
  const loader = images[key];
  if (!loader) return undefined;
  const mod = await loader();
  return mod.default;
}
