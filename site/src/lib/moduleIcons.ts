// Official Odoo app icon per módulo, plus one accent hex picked from that
// same icon's own fill colors (never an arbitrary color) — used to give
// each module card its own tinted halo/glow instead of one flat brand color
// repeated on every card.
export const MODULE_ICONS: Record<string, { file: string; accent: string }> = {
  'ventas-y-crm': { file: 'crm', accent: '#1AD3BB' },
  compras: { file: 'purchase', accent: '#005E7A' },
  inventario: { file: 'stock', accent: '#FBB945' },
  'contabilidad-y-finanzas': { file: 'account_accountant', accent: '#953B24' },
  rrhh: { file: 'hr', accent: '#985184' },
  'comercio-exterior': { file: 'dropshipping', accent: '#088BF5' },
  importaciones: { file: '3pl_logistic_company', accent: '#F78613' },
  'punto-de-venta': { file: 'point_of_sale', accent: '#712258' },
};

export const DEFAULT_MODULE_ICON = { file: 'base', accent: '#714b67' };

export function getModuleIcon(slug: string) {
  return MODULE_ICONS[slug] ?? DEFAULT_MODULE_ICON;
}
