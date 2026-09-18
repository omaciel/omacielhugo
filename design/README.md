# Site redesign mockups

Static HTML mockups for replacing the current `gokarna` theme. Open
`design/index.html` in a browser to compare them. Each direction has a home
page (`index.html`) and an article page (`post.html`) built from real site
content. Shared images are in `assets/`.

**Azulejo was chosen** and is built as the site's Hugo theme in
`themes/azulejo/`. The other two mockups are kept here for reference.

## 1. Rough Draft (`rough-draft/`)

Named after the Substack newsletter, *Life in Rough Draft*.

- **Idea:** the whole site is a legal pad. Every line of text sits on a ruled
  line (a 32px baseline grid), dates go in the red margin, and the headline
  shows a revision: “~~aspiring~~ award-winning novelist.”
- **Color:** pad `#fbf3c9`, rules `#b7cbe3`, margin `#de6b6b`, ballpoint ink
  `#1d2b4f`, red pencil `#c2272d`, binding `#6e1f2a`.
- **Type:** Newsreader for all text; Caveat for margin notes and red-pencil marks.
- **Motion:** the strike-through and the handwritten correction draw in once on
  page load.

## 2. Azulejo (`azulejo/`)

Brazilian modernism, after Athos Bulcão’s tile walls in Brasília.

- **Idea:** the animated avatar sits beside a bold cobalt headline with the
  same red-pencil revision as Rough Draft (“~~aspiring~~ award-winning
  novelist”). Tile motifs appear further down the page.
- **Color:** white `#ffffff`, grout `#e8ecf4`, cobalt `#1f47a8`, ink `#0f1d3a`.
  Yellow `#f2b705` and green `#0f7a4f` appear only to mark series.
- **Type:** Bricolage Grotesque (condensed, heavy) for headings; Source Serif 4
  for reading.
- **Structure:** a tile chip beside each post shows its series (The Mill,
  Murder Hornet, Ikigai, or a standalone essay).

## 3. TK90X (`tk90x/`)

Based on the Brazilian ZX Spectrum clone Og learned BASIC on, typing programs
out of *Input* magazine.

- **Idea:** a black case with the four-color diagonal stripe. The hero screen
  plays a Spectrum loading border, then types out a BASIC listing about Og and
  ends with `0 OK, 50:1`.
- **Color:** case `#1c1c1f`, paper `#ffffff`, stripes red `#e0262d`, yellow
  `#f6c20f`, green `#2ea44f`, cyan `#00a0d6`.
- **Type:** Atkinson Hyperlegible Next for everything readable; Press Start 2P
  only on the hero screen and in pull quotes.
- **Structure:** stripe colors map to the kind of writing (fiction, engineering
  and leadership, life, reading), and the post list has filters for each.

All three respect `prefers-reduced-motion`, show visible keyboard focus, and
work at phone width.
