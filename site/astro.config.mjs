// @ts-check
import { defineConfig, fontProviders } from 'astro/config';
import { unified } from '@astrojs/markdown-remark';
import tailwindcss from '@tailwindcss/vite';
import sitemap from '@astrojs/sitemap';
import { stripGuiaComments } from './src/lib/remark-strip-guia.mjs';

// https://astro.build/config
export default defineConfig({
  site: 'https://eynes.github.io',
  base: '/website',
  output: 'static',
  trailingSlash: 'never',
  redirects: {
    '/verticales': '/sectores',
    '/verticales/[slug]': '/sectores/[slug]',
    '/verticales/distribucion-y-mayoristas': '/sectores/repuestos-y-autopartes',
    '/verticales/servicios-consultoria-it': '/sectores/tecnologia-ti',
    '/verticales/materiales-electricos-y-ferreterias': '/sectores/mayorista-de-ferreteria-y-buloneria',
    '/casos/clinica-ima': '/casos/clinica-ima-s-a',
  },
  integrations: [
    sitemap({
      filter: (page) => !page.includes('/legal/') && !page.includes('/verticales'),
    }),
  ],
  vite: {
    plugins: [tailwindcss()],
  },
  markdown: {
    processor: unified({ remarkPlugins: [stripGuiaComments] }),
  },
  fonts: [
    {
      provider: fontProviders.google(),
      name: 'Inter',
      cssVariable: '--font-inter',
      weights: [400, 500, 600, 700],
      subsets: ['latin'],
    },
    {
      provider: fontProviders.google(),
      name: 'IBM Plex Mono',
      cssVariable: '--font-plex-mono',
      weights: [400, 500, 600],
      subsets: ['latin'],
    },
  ],
});
