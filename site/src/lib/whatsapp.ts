/** Builds a wa.me deep link — no backend required. */
export function buildWhatsAppLink(rawPhone: string, message: string): string {
  const digits = rawPhone.replace(/[^\d]/g, '');
  return `https://wa.me/${digits}?text=${encodeURIComponent(message)}`;
}
