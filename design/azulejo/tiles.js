// Bulcão-style tile motifs, drawn on a 100×100 tile.
const MOTIFS = [
  '<path d="M0 0H100A100 100 0 0 1 0 100Z"/>',
  '<path d="M0 0H100L0 100Z"/><circle cx="74" cy="74" r="12"/>',
  '<path d="M0 100A50 50 0 0 1 100 100Z"/><rect width="100" height="18"/>',
  '<path d="M0 0H50A50 50 0 0 1 0 50Z M100 100H50A50 50 0 0 1 100 50Z"/>',
];
const COLORS = { cobalt: '#1f47a8', sun: '#f2b705', leaf: '#0f7a4f', ink: '#0f1d3a' };

function tileSVG(motif, color, turn = 0) {
  return `<svg viewBox="0 0 100 100" aria-hidden="true" style="transform:rotate(${turn * 90}deg)"><g fill="${COLORS[color] || color}">${MOTIFS[motif]}</g></svg>`;
}

// Static tiles: <span data-tile="motif,color,turn">
document.querySelectorAll('[data-tile]').forEach(el => {
  const [m, c, t] = el.dataset.tile.split(',');
  el.innerHTML = tileSVG(+m, c, +(t || 0));
});

// A repeating tile band as a background image.
document.querySelectorAll('.band').forEach(el => {
  const svg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 100"><rect width="200" height="100" fill="#fff"/><g fill="#1f47a8">${MOTIFS[3]}<g transform="translate(100 0)">${MOTIFS[0]}</g></g></svg>`;
  el.style.backgroundImage = `url("data:image/svg+xml,${encodeURIComponent(svg)}")`;
  el.style.backgroundSize = '72px 36px';
});
