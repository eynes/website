import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const CONTENT = (path: string) => new URL(`../../content/${path}`, import.meta.url);

const estado = z.enum(['borrador', 'revision', 'publicado']);
const faq = z.object({ pregunta: z.string(), respuesta: z.string() });

// Fields present on every "real page" content type. Kept permissive
// (plain optional strings) because content still in `estado: "borrador"`
// commonly has literal "[COMPLETAR]" placeholder text in these fields —
// strict validation (e.g. z.string().url()) would break the dev build.
// Enforcing "no [COMPLETAR] left" only happens for estado:publicado
// content, via scripts/check-published-content.mjs, not here.
const pageMeta = {
  title: z.string(),
  seo_title: z.string(),
  meta_description: z.string(),
  slug: z.string(),
  url: z.string().optional(),
  estado,
  og_image: z.string().optional().default(''),
};

const hubMeta = {
  title: z.string(),
  seo_title: z.string(),
  meta_description: z.string(),
  slug: z.string(),
  url: z.string().optional(),
  estado,
};

// ---- 02-verticales ----
const verticales = defineCollection({
  loader: glob({ pattern: '[!_]*.md', base: CONTENT('02-verticales') }),
  schema: z.object({
    ...pageMeta,
    schema_type: z.literal('Service'),
    faqs: z.array(faq).default([]),
    modulos_relevantes: z.array(z.string()).default([]),
    casos_relacionados: z.array(z.string()).default([]),
    integraciones_destacadas: z.array(z.string()).default([]),
  }),
});

// ---- 03-modulos ----
const modulos = defineCollection({
  loader: glob({ pattern: '[!_]*.md', base: CONTENT('03-modulos') }),
  schema: z.object({
    ...pageMeta,
    schema_type: z.literal('Product'),
    faqs: z.array(faq).default([]),
    modulos_integrados: z.array(z.string()).default([]),
    caso_relacionado: z
      .object({ slug: z.string().optional(), resultado: z.string().optional() })
      .optional(),
  }),
});

// ---- 04-casos-de-exito ----
const casosDeExito = defineCollection({
  loader: glob({ pattern: '[!_]*.md', base: CONTENT('04-casos-de-exito') }),
  schema: z.object({
    ...pageMeta,
    schema_type: z.literal('Article'),
    cliente: z.string(),
    logo: z.string().optional().default(''),
    rubro: z.string(),
    pais: z.string(),
    usuarios: z.union([z.number(), z.string()]),
    modulos_implementados: z.array(z.string()).default([]),
    resultado_clave: z.string(),
  }),
});

// ---- 05-blog/posts ----
const blog = defineCollection({
  loader: glob({ pattern: '**/*.md', base: CONTENT('05-blog/posts') }),
  schema: z.object({
    ...pageMeta,
    schema_type: z.literal('Article'),
    categoria: z.enum(['localizacion-ar', 'comparativas', 'por-rubro', 'guias-de-uso']),
    autor: z.string(),
    fecha_publicacion: z.string(),
    fecha_actualizacion: z.string(),
    tiempo_lectura_min: z.union([z.number(), z.string()]),
    og_image_alt: z.string().optional().default(''),
    origen_linkedin: z.string().nullable().optional(),
    relacionados: z.array(z.string()).default([]),
    enlaces_internos_sugeridos: z.array(z.string()).default([]),
    indice: z.array(z.string()).default([]),
    faqs: z.array(faq).default([]),
  }),
});

// ---- 01-paginas-unicas (home, nosotros, contacto/demo, localizacion) ----
const paginasUnicas = defineCollection({
  loader: glob({ pattern: '*.md', base: CONTENT('01-paginas-unicas') }),
  schema: z.object({
    ...pageMeta,
    schema_type: z.enum(['Organization', 'AboutPage', 'ContactPage', 'Service']),
    faqs: z.array(faq).default([]),
    relacionados: z.array(z.string()).default([]),
  }),
});

// ---- hub (listing) pages: one singleton collection per hub file ----
const verticalesHub = defineCollection({
  loader: glob({ pattern: '_hub.md', base: CONTENT('02-verticales') }),
  schema: z.object({ ...hubMeta, schema_type: z.literal('CollectionPage') }),
});
const modulosHub = defineCollection({
  loader: glob({ pattern: '_hub.md', base: CONTENT('03-modulos') }),
  schema: z.object({ ...hubMeta, schema_type: z.literal('CollectionPage') }),
});
const casosHub = defineCollection({
  loader: glob({ pattern: '_hub.md', base: CONTENT('04-casos-de-exito') }),
  schema: z.object({ ...hubMeta, schema_type: z.literal('CollectionPage') }),
});
const blogHub = defineCollection({
  loader: glob({ pattern: '_hub.md', base: CONTENT('05-blog') }),
  schema: z.object({
    ...hubMeta,
    schema_type: z.literal('Blog'),
    categorias: z.array(
      z.object({ slug: z.string(), nombre: z.string(), descripcion: z.string() })
    ),
  }),
});

// ---- 00-config: only site.md + navegacion.md are consumed by the build ----
const siteConfig = defineCollection({
  loader: glob({ pattern: 'site.md', base: CONTENT('00-config') }),
  schema: z.object({
    razon_social: z.string(),
    nombre_comercial: z.string(),
    tagline_corto: z.string(),
    dominio: z.string(),
    badge_partner: z.object({
      texto: z.string(),
      icono: z.string(),
      link_verificacion: z.string(),
    }),
    antiguedad: z.object({
      anio_fundacion: z.string(),
      anios_operando: z.string(),
    }),
    paises_operacion: z.array(z.string()),
    prueba_social_home: z.object({
      empresas_clientes: z.string(),
      anios_experiencia: z.string(),
      paises: z.string(),
      logos_clientes_destacados: z.array(z.string()),
    }),
    // Real physical offices only — these get LocalBusiness schema /
    // Google Business Profile treatment. Today: Buenos Aires only.
    oficinas: z.array(
      z.object({
        ciudad: z.string(),
        pais: z.string(),
        direccion: z.string(),
        telefono: z.string(),
        email: z.string(),
        es_sede_principal: z.boolean(),
      })
    ),
    // Phone/email coverage areas with no physical office — shown as
    // plain info on Nosotros/Contacto, never given LocalBusiness schema.
    zonas_de_cobertura: z.array(
      z.object({
        ciudad: z.string(),
        pais: z.string(),
        telefono: z.string(),
        email: z.string(),
      })
    ),
    contacto_general: z.object({
      email_comercial: z.string(),
      email_soporte: z.string(),
      whatsapp_comercial: z.string(),
    }),
    redes: z.object({
      linkedin: z.string(),
      instagram: z.string(),
    }),
    legal: z.object({
      politica_privacidad_url: z.string(),
      terminos_url: z.string(),
    }),
  }),
});

const navConfig = defineCollection({
  loader: glob({ pattern: 'navegacion.md', base: CONTENT('00-config') }),
  schema: z.object({
    nav_principal: z.array(z.object({ etiqueta: z.string(), url: z.string() })),
    cta_nav: z.object({ etiqueta: z.string(), url: z.string() }),
    footer_columnas: z.array(
      z.object({
        titulo: z.string(),
        tipo: z.enum(['dinamico_oficinas', 'dinamico_redes']).optional(),
        links: z.array(z.object({ etiqueta: z.string(), url: z.string() })).optional(),
      })
    ),
  }),
});

export const collections = {
  verticales,
  modulos,
  casosDeExito,
  blog,
  paginasUnicas,
  verticalesHub,
  modulosHub,
  casosHub,
  blogHub,
  siteConfig,
  navConfig,
};
