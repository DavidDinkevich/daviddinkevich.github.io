# APEX embargo

The tracked `.apex-embargo` marker controls what GitHub Pages publishes.

While the marker exists:

- `/APEX/` contains only the Coming Soon page.
- `/apex/` redirects to `/APEX/`.
- Files below `/APEX/`, including the paper PDF, are not deployed.
- The homepage keeps its APEX card, but its Paper action reads “Paper — Coming Soon.”
- The deployed sitemap omits `/APEX/`.

The complete APEX page source remains in this public repository. The paper PDF does not; private standalone packages inject a local copy with `scripts/package_apex.py`.

## Publish after arXiv

Record the public arXiv URL, remove the marker, commit, and push:

```bash
printf '%s\n' 'https://arxiv.org/abs/ARXIV_ID' > apex-paper-url.txt
git rm .apex-embargo
git add apex-paper-url.txt
git commit -m "Website: Publish APEX project page" -m "Restore the complete project page and link its paper after the arXiv release."
git push origin main
```

Wait for the `Deploy site` workflow and GitHub Pages build to succeed, then verify:

- `https://daviddinkevich.github.io/APEX/`
- `https://daviddinkevich.github.io/apex/`
- `https://daviddinkevich.github.io/sitemap.xml`

Confirm that both Paper actions point to arXiv and that `https://daviddinkevich.github.io/APEX/static/pdfs/apex_paper.pdf` still returns 404.

If the `/APEX/` prefix was temporarily hidden through Google Search Console, cancel that removal. Inspect the canonical APEX URL and request indexing once.

## Re-enable the embargo

Restore the marker with the same content, commit, and push:

```bash
printf '%s\n' 'Remove this file to publish the complete APEX project page.' > .apex-embargo
git add .apex-embargo
git commit -m "Website: Re-enable APEX embargo" -m "Return the project URL to the Coming Soon deployment."
git push origin main
```
