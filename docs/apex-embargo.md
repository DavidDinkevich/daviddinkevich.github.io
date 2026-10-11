# APEX embargo

The tracked `.apex-embargo` marker controls what GitHub Pages publishes from this repository.

The project page is public. The paper PDF and research code are not.

While the marker exists:

- `/APEX/` contains only the Coming Soon page.
- `/apex/` redirects to `/APEX/`.
- Files below `/APEX/`, including the paper PDF, are not deployed.
- The homepage keeps its APEX card, but its Paper action reads “Paper — Coming Soon.”
- The deployed sitemap omits `/APEX/`.

`DavidDinkevich/APEX` stays private. GitHub Pages cannot be enabled on that private repository, so the published project page is the copy under `APEX/` in this repository.

Without the marker:

- `/APEX/` serves the project page from `APEX/`.
- `/apex/` redirects to `/APEX/`.
- The homepage Paper action stays “Paper — Coming Soon” until `apex-paper-url.txt` exists.
- The PDF is not in the deployed tree.

## Link the paper after arXiv

After the arXiv page is public:

1. Point the APEX project-page arXiv action at the public abs URL and, if the PDF should be hosted here, add it then.
2. Record the public paper URL and keep the embargo marker absent:

   ```bash
   printf '%s\n' 'https://arxiv.org/abs/ARXIV_ID' > apex-paper-url.txt
   git add apex-paper-url.txt
   git commit -m "Website: Link APEX arXiv paper" -m "Send the homepage Paper action to the public abs page."
   git push origin main
   ```

Wait for the Pages build, then verify:

- `https://daviddinkevich.github.io/APEX/`
- `https://daviddinkevich.github.io/apex/`
- `https://daviddinkevich.github.io/sitemap.xml`

Confirm the project page’s PDF, arXiv, and Code actions; confirm the personal homepage Paper action points to arXiv.

If the `/APEX/` prefix was temporarily hidden through Google Search Console, cancel that removal. Inspect the canonical APEX URL and request indexing once.

## Re-enable the Coming Soon page

Restore the marker, then commit and push:

```bash
printf '%s\n' 'Remove this file to publish the complete APEX project page.' > .apex-embargo
git add .apex-embargo
git commit -m "Website: Re-enable APEX embargo" -m "Return the project URL to the Coming Soon deployment."
git push origin main
```
