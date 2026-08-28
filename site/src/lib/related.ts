import { getEntry, type CollectionKey, type CollectionEntry } from 'astro:content';

/**
 * Cross-links in content (e.g. a caso's `rubro`, a vertical's
 * `casos_relacionados`) are plain slug strings, not Astro `reference()`s,
 * because real mismatches exist today (rubros/módulos referenced by name
 * that don't have a page yet). Resolve defensively: render plain text
 * instead of a broken link when nothing matches.
 */
export async function resolveRelated<C extends CollectionKey>(
  collection: C,
  slug: string | undefined | null
): Promise<CollectionEntry<C> | null> {
  if (!slug) return null;
  try {
    const entry = await getEntry(collection, slug);
    return (entry as CollectionEntry<C> | undefined) ?? null;
  } catch {
    return null;
  }
}

/**
 * Like resolveRelated, but also refuses to hand back an entry whose own
 * route won't exist in a production build (estado !== "publicado") — so a
 * cross-link never points at a page that 404s.
 */
export async function resolvePublishedRelated<C extends CollectionKey>(
  collection: C,
  slug: string | undefined | null
): Promise<CollectionEntry<C> | null> {
  const entry = await resolveRelated(collection, slug);
  if (!entry) return null;
  if (import.meta.env.PROD && (entry.data as { estado?: string }).estado !== 'publicado') {
    return null;
  }
  return entry;
}
