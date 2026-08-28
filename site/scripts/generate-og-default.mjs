// One-off: renders a simple branded 1200x630 placeholder OG image so
// social shares never point at a broken image while real screenshots are
// still pending. Run manually if the design needs to change; not part of
// the build.
import sharp from 'sharp';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const outPath = path.resolve(__dirname, '..', 'public', 'og-default.png');

const svg = `
<svg width="1200" height="630" viewBox="0 0 1200 630" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#101a3d" />
      <stop offset="100%" stop-color="#2a3a7c" />
    </linearGradient>
  </defs>
  <rect width="1200" height="630" fill="url(#bg)" />
  <text x="90" y="300" font-family="Arial, sans-serif" font-size="88" font-weight="700" fill="#ffffff">Eynes</text>
  <text x="90" y="360" font-family="Arial, sans-serif" font-size="34" fill="#c7cef0">Tu empresa, conectada para crecer.</text>
  <rect x="90" y="410" width="330" height="50" rx="25" fill="rgba(255,255,255,0.12)" />
  <text x="112" y="443" font-family="Arial, sans-serif" font-size="24" fill="#ffffff">Silver Partner Oficial de Odoo</text>
</svg>
`;

await sharp(Buffer.from(svg)).png().toFile(outPath);
console.log(`Wrote ${outPath}`);
