/** Prefixes a root-relative path with Astro's configured `base` (e.g. "/website").
 * Leaves absolute URLs, mailto:/tel: links and bare "#anchor" hrefs untouched. */
export function withBase(path: string): string {
  if (/^([a-z][a-z0-9+.-]*:|#)/i.test(path)) return path;
  const base = import.meta.env.BASE_URL;
  const trimmedBase = base.endsWith('/') ? base.slice(0, -1) : base;
  return `${trimmedBase}${path.startsWith('/') ? path : `/${path}`}`;
}
