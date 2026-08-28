import { getCollection, type CollectionKey, type CollectionEntry } from 'astro:content';

/**
 * Production builds only ever emit `estado: "publicado"` routes for
 * repeatable collections (verticales/modulos/casosDeExito/blog) — a page
 * "not being ready" should mean the URL doesn't exist yet. Local dev
 * previews everything regardless of estado. Singleton pages (home,
 * nosotros, demo, localizacion-argentina) are NOT filtered this way —
 * see their pages for why.
 */
export async function getPublished<C extends CollectionKey>(
  collection: C
): Promise<CollectionEntry<C>[]> {
  return getCollection(collection, (entry: CollectionEntry<C>) =>
    import.meta.env.PROD ? (entry.data as { estado: string }).estado === 'publicado' : true
  );
}
