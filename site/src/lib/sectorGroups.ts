/**
 * Fixed color rotation for sector groups (agrupador), shared by the home
 * industry grid, /sectores index, and the nav mega-menu — so a given
 * group always reads the same color everywhere, regardless of how many
 * of its items are shown on a given page.
 */
const ORDERED_GROUPS = [
  'AGROINDUSTRIA Y MANUFACTURA',
  'ALIMENTOS Y GASTRONOMÍA',
  'AUTOMOTRIZ Y VEHÍCULOS',
  'COMERCIO MAYORISTA Y MINORISTA',
  'CONSTRUCCIÓN E INFRAESTRUCTURA',
  'ENERGÍA Y SECTORES PESADOS',
  'SALUD, CIENCIA Y CUIDADO ANIMAL',
  'SERVICIOS E INSUMOS INDUSTRIALES',
  'SERVICIOS EMPRESARIALES',
  'TECNOLOGÍA E INNOVACIÓN',
] as const;

const COLOR_CLASSES = ['text-teal', 'text-purple', 'text-silver', 'text-purple-light'] as const;

export function groupColorClass(agrupador: string): string {
  const index = ORDERED_GROUPS.indexOf(agrupador as (typeof ORDERED_GROUPS)[number]);
  return COLOR_CLASSES[(index === -1 ? 0 : index) % COLOR_CLASSES.length];
}

/** Sorts group names into the same fixed order everywhere they're listed. */
export function sortGroups<T extends { nombre: string }>(groups: T[]): T[] {
  return [...groups].sort((a, b) => {
    const ia = ORDERED_GROUPS.indexOf(a.nombre as (typeof ORDERED_GROUPS)[number]);
    const ib = ORDERED_GROUPS.indexOf(b.nombre as (typeof ORDERED_GROUPS)[number]);
    return (ia === -1 ? 999 : ia) - (ib === -1 ? 999 : ib);
  });
}
