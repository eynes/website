// Pure JSON-LD builder functions — one per schema.org type in
// content/06-seo/schema-org-referencia.md's mapping table. Each returns a
// plain object (no "@context"; BaseLayout adds that once per script tag).

import { withBase } from './url';

export interface Crumb {
  name: string;
  url: string;
}

export interface Faq {
  pregunta: string;
  respuesta: string;
}

const ORG_ID = 'https://eynes.com.ar/#organization';

export function organizationSchema(site: {
  razon_social: string;
  nombre_comercial: string;
  dominio: string;
  redes: { linkedin: string; instagram: string };
}) {
  return {
    '@type': 'Organization',
    '@id': ORG_ID,
    name: site.razon_social,
    alternateName: site.nombre_comercial,
    url: `https://${site.dominio}`,
    sameAs: [site.redes.linkedin, site.redes.instagram].filter(Boolean),
  };
}

export function websiteSchema(site: { nombre_comercial: string; dominio: string }) {
  return {
    '@type': 'WebSite',
    name: site.nombre_comercial,
    url: `https://${site.dominio}`,
  };
}

export function localBusinessSchema(office: {
  ciudad: string;
  pais: string;
  direccion: string;
  telefono: string;
  email: string;
}) {
  return {
    '@type': 'LocalBusiness',
    name: `Eynes – ${office.ciudad}`,
    address: office.direccion,
    telephone: office.telefono,
    email: office.email,
    areaServed: office.pais,
    parentOrganization: { '@id': ORG_ID },
  };
}

export function aboutPageSchema() {
  return { '@type': 'AboutPage' };
}

export function contactPageSchema() {
  return { '@type': 'ContactPage' };
}

export function collectionPageSchema(name: string, description: string, itemUrls: string[]) {
  return {
    '@type': 'CollectionPage',
    name,
    description,
    mainEntity: {
      '@type': 'ItemList',
      itemListElement: itemUrls.map((url, i) => ({
        '@type': 'ListItem',
        position: i + 1,
        url,
      })),
    },
  };
}

export function serviceSchema({
  name,
  description,
  url,
}: {
  name: string;
  description: string;
  url: string;
}) {
  return {
    '@type': 'Service',
    name,
    description,
    url,
    provider: { '@id': ORG_ID },
  };
}

export function productSchema({
  name,
  description,
  url,
}: {
  name: string;
  description: string;
  url: string;
}) {
  return { '@type': 'Product', name, description, url };
}

/** Returns null (never emitted) when there are no real FAQs on the page. */
export function faqPageSchema(faqs: Faq[]) {
  if (!faqs || faqs.length === 0) return null;
  return {
    '@type': 'FAQPage',
    mainEntity: faqs.map((f) => ({
      '@type': 'Question',
      name: f.pregunta,
      acceptedAnswer: { '@type': 'Answer', text: f.respuesta },
    })),
  };
}

export function articleSchema({
  headline,
  description,
  url,
  datePublished,
  dateModified,
  author,
  image,
}: {
  headline: string;
  description?: string;
  url: string;
  datePublished?: string;
  dateModified?: string;
  author?: string;
  image?: string;
}) {
  return {
    '@type': 'Article',
    headline,
    description,
    url,
    ...(datePublished ? { datePublished } : {}),
    ...(dateModified ? { dateModified } : {}),
    ...(author ? { author: { '@type': 'Person', name: author } } : {}),
    ...(image ? { image } : {}),
  };
}

export function breadcrumbListSchema(crumbs: Crumb[]) {
  return {
    '@type': 'BreadcrumbList',
    itemListElement: crumbs.map((c, i) => ({
      '@type': 'ListItem',
      position: i + 1,
      name: c.name,
      item: withBase(c.url),
    })),
  };
}

export function blogSchema() {
  return { '@type': 'Blog' };
}

/** True-ish ISO date check — real content still often has "[COMPLETAR ...]" placeholders. */
export function isRealDate(value?: string | null): boolean {
  return !!value && /^\d{4}-\d{2}-\d{2}/.test(value);
}
