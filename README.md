# David Dinkevich

Source for [daviddinkevich.github.io](https://daviddinkevich.github.io/).

The homepage is a dependency-free static site:

- `index.html` contains the page content and metadata.
- `static/css/index.css` contains the visual system and responsive styles.
- `static/js/index.js` contains abstract and preview interactions.
- `APEX/` is the standalone APEX project page.
- `apex/` redirects lowercase links to the canonical APEX page.

Run a local preview from the repository root:

```bash
python3 -m http.server 8000
```

Format source files with `npm run format`.
