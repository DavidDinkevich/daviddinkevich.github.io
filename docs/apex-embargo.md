# APEX embargo

The tracked `.apex-embargo` marker controls what GitHub Pages publishes.

While the marker exists:

- `/APEX/` contains only the Coming Soon page.
- `/apex/` redirects to `/APEX/`.
- Files below `/APEX/`, including the paper PDF, are not deployed.
- The homepage keeps its APEX card, but its Paper action reads “Paper — Coming Soon.”
- The deployed sitemap omits `/APEX/`.

The complete project page, paper, and research code live in the private `DavidDinkevich/APEX` repository. Its `gh-pages` branch is staged but GitHub Pages remains disabled.

## Publish after arXiv

After the arXiv page is public:

1. Update the APEX `gh-pages` branch so its arXiv and Code actions point to the public resources.
2. Push both APEX branches while the repository is private.
3. Make `DavidDinkevich/APEX` public and enable GitHub Pages from the `gh-pages` branch at `/`.
4. Verify `https://daviddinkevich.github.io/APEX/` serves the complete project page.
5. In this repository, record the public paper URL and remove the embargo:

   ```bash
   printf '%s\n' 'https://arxiv.org/abs/ARXIV_ID' > apex-paper-url.txt
   git rm .apex-embargo
   git add apex-paper-url.txt
   git commit -m "Website: Publish APEX project page" -m "Hand the project route to its public repository and link the arXiv paper."
   git push origin main
   ```

Wait for both Pages builds to succeed, then verify:

- `https://daviddinkevich.github.io/APEX/`
- `https://daviddinkevich.github.io/apex/`
- `https://daviddinkevich.github.io/sitemap.xml`

Confirm the project page’s PDF, arXiv, and Code actions; confirm the personal homepage Paper action points to arXiv.

If the `/APEX/` prefix was temporarily hidden through Google Search Console, cancel that removal. Inspect the canonical APEX URL and request indexing once.

## Re-enable the embargo

Before publication, keep the APEX repository private with Pages disabled. Restore the marker in this repository if needed, then commit and push:

```bash
printf '%s\n' 'Remove this file to publish the complete APEX project page.' > .apex-embargo
git add .apex-embargo
git commit -m "Website: Re-enable APEX embargo" -m "Return the project URL to the Coming Soon deployment."
git push origin main
```
