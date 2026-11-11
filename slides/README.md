# Python and Git 101: the slide deck

The course slides, written in [Slidev](https://sli.dev) with the Dataminded theme.

## Layout

| Path | What it is |
| --- | --- |
| `slides.md` | Entry file: headmatter, cover slide, and one `src:` include per part |
| `parts/` | One file per section of the deck. Speaker notes live in the HTML comments. |
| `style.css` | Deck-wide CSS helpers |
| `theme/` | Vendored copy of `slidev-theme-dataminded`, linked from `package.json` |
| `public/` | Static assets, served from `/` |

## Working on the deck

```bash
cd slides
npm install        # once
npm run dev        # live preview on localhost:3030, press "p" for presenter mode
npm run export     # writes python-and-git-101.pdf
npm run build      # static site in dist/
```

If you add or rename a file under `parts/`, restart the dev server: Slidev resolves
`src:` includes at startup. The same goes for `style.css`.

## Conventions

- Headings are two-tone: wrap the accent word in `<span class="dm-accent">...</span>`.
- Content slides use `layout: default` with a `label:` for the top-right tag. The label
  is the section name (`3 · Language fundamentals`) and stays constant between section
  dividers.
- Dividers use `layout: section`, exercise pointers use `layout: statement` and name the
  exercise folder.
- Components (`DmColumns`, `DmComparison`, `DmSteps`, `DmProcess`, `DmIconBadge`) come
  from the theme.
- Icons are UnoCSS classes such as `i-mdi-console` (any [Material Design Icon](https://pictogrammers.com/library/mdi/)),
  passed as `icon="i-mdi-..."` to `DmIconBadge`, `DmInfoCard` and `DmBanner`.
- `style.css` has the layout helpers `grid-2`, `grid-3`, `split` (code left, picture right) and `note`
  (a one-line takeaway under a table or diagram).
- `setup/mermaid.ts` gives every Mermaid diagram the brand palette, git graphs included.
- Commands are PowerShell: participants work on managed Windows laptops.
- No emdashes, and bold marks a single term rather than a whole claim.
- `slidev export` flattens `v-click` builds to their final state, so keep the last state
  complete.
- Slides render at 980x552 CSS pixels. Anything taller silently overflows the page in
  the PDF export, so check the export after adding a long code block.
