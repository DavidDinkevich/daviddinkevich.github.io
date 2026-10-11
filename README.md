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

The APEX paper is deliberately not stored in this public repository. Build a private, standalone copy of the complete project page by supplying the local paper:

```bash
python3 scripts/package_apex.py \
  --paper /path/to/apex_paper.pdf \
  --output "$HOME/Desktop/APEX-project-site.zip"
```

Extract the ZIP and open `index.html`, or run `python3 -m http.server 8000` inside the extracted directory.

Format source files with `npm run format`.
