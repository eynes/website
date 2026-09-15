import { getCollection, type CollectionKey, type CollectionEntry } from 'astro:content';

/**
 * Production builds only ever emit `estado: "publicado"` routes for
 * repeatable collections (verticales/modulos/casosDeExito) — a page
 * "not being ready" should mean the URL doesn't exist yet. Local dev
 * previews everything regardless of estado. Singleton pages (home,
 * nosotros, demo, localizacion-argentina) are NOT filtered this way —
 * see their pages for why.
 */
export async function getPublished<C extends CollectionKey>(
  collection: C
): Promise<CollectionEntry<C>[]> {
  return getCollection(collection, (entry: CollectionEntry<C>) =>
    (import.meta.env.PROD ||
      collection === 'verticales' ||
      collection === 'casosDeExito' ||
      collection === 'localizacionArgentina')
      ? (entry.data as { estado: string }).estado === 'publicado'
      : true
  );
}

/** Puts entries whose slug is in `destacados` first (in that order), then the rest unchanged. */
export function sortDestacadosFirst<T extends { data: { slug: string } }>(
  entries: T[],
  destacados: string[]
): T[] {
  const destacadosSet = new Set(destacados);
  const destacadosOrdenados = destacados
    .map((slug) => entries.find((e) => e.data.slug === slug))
    .filter((e): e is T => Boolean(e));
  const resto = entries.filter((e) => !destacadosSet.has(e.data.slug));
  return [...destacadosOrdenados, ...resto];
}
