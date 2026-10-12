# APEX embargo

The tracked `.apex-embargo` marker controls what GitHub Pages publishes from this repository.

The project page and paper are public. The research code is not.

While the marker exists:

- `/APEX/` contains only the Coming Soon page.
- `/apex/` redirects to `/APEX/`.
- Files below `/APEX/`, including the paper PDF, are not deployed.
- The homepage keeps its APEX card, but its Paper action reads “Paper — Coming Soon.”
- The deployed sitemap omits `/APEX/`.

`DavidDinkevich/APEX` stays private. GitHub Pages cannot be enabled on that private repository, so the published project page is the copy under `APEX/` in this repository.

Without the marker:

- `/APEX/` serves the project page from `APEX/`, including the paper PDF.
- `/apex/` redirects to `/APEX/`.
- The homepage Paper action links to the arXiv abs URL in `apex-paper-url.txt`.
- Code stays “Coming Soon” until the APEX repository is public.

## Re-enable the Coming Soon page

Restore the marker, then commit and push:

```bash
printf '%s\n' 'Remove this file to publish the complete APEX project page.' > .apex-embargo
git add .apex-embargo
git commit -m "Website: Re-enable APEX embargo" -m "Return the project URL to the Coming Soon deployment."
git push origin main
```
