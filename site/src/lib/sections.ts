import { unified } from 'unified';
import remarkParse from 'remark-parse';
import remarkGfm from 'remark-gfm';
import remarkRehype from 'remark-rehype';
import rehypeStringify from 'rehype-stringify';
import { stripGuiaComments } from './remark-strip-guia.mjs';

export interface Section {
  title: string;
  body: string;
}

const HEADING_RE = /^##\s+(\d{2}[a-z]?)\s+—\s+(.*)$/gm;

/**
 * Splits a content entry's raw Markdown body into numbered sections
 * (e.g. "## 02b — Comparador directo") keyed by their number, matching
 * the section-slotted structure used by verticales/modulos/casos content.
 */
export function splitSections(body: string): Record<string, Section> {
  const sections: Record<string, Section> = {};
  const matches = [...body.matchAll(HEADING_RE)];
  for (let i = 0; i < matches.length; i++) {
    const match = matches[i];
    const key = match[1];
    const title = match[2].trim();
    const start = match.index! + match[0].length;
    const end = i + 1 < matches.length ? matches[i + 1].index! : body.length;
    sections[key] = { title, body: body.slice(start, end).trim() };
  }
  return sections;
}

const pipeline = unified()
  .use(remarkParse)
  .use(remarkGfm)
  .use(stripGuiaComments)
  .use(remarkRehype)
  .use(rehypeStringify);

export async function renderFragment(markdown: string | undefined): Promise<string> {
  if (!markdown) return '';
  const file = await pipeline.process(markdown);
  return String(file);
}

export async function renderSection(
  sections: Record<string, Section>,
  key: string
): Promise<string> {
  return renderFragment(sections[key]?.body);
}

/** Extracts a `**Label:** value` line's value from a section's raw body. */
export function extractLabeled(body: string | undefined, label: string): string {
  if (!body) return '';
  const re = new RegExp(`\\*\\*${label}:\\*\\*\\s*(.+)`);
  return body.match(re)?.[1]?.trim() ?? '';
}

/** Removes a `**Label:** value` line from a section's raw body (e.g. once it's been extracted separately). */
export function stripLabeledLine(body: string | undefined, label: string): string {
  if (!body) return '';
  const re = new RegExp(`^\\*\\*${label}:\\*\\*.*$`, 'm');
  return body.replace(re, '').trim();
}
