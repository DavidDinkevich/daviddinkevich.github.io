# David Dinkevich

Source for [daviddinkevich.github.io](https://daviddinkevich.github.io/).

The homepage is a dependency-free static site:

- `index.html` contains the page content and metadata.
- `static/css/index.css` contains the visual system and responsive styles.
- `static/js/index.js` contains abstract and preview interactions.
- `embargo/` contains the Coming Soon placeholder and lowercase redirect.
- `APEX/` contains the published project page, including the paper PDF.

The research code stays in the private `DavidDinkevich/APEX` repository. This site serves `https://daviddinkevich.github.io/APEX/` because GitHub Pages cannot be enabled on that private repository.

Run a local preview from the repository root:

```bash
python3 -m http.server 8000
```

Format source files with `npm run format`.
