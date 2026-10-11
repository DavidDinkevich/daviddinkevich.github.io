#!/usr/bin/env python3

import argparse
import shutil
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
EMBARGO_MARKER = REPOSITORY_ROOT / ".apex-embargo"
PAPER_LINK = (
    '<a class="action-link" href="/APEX/static/pdfs/apex_paper.pdf" '
    'aria-label="APEX paper PDF, 39 megabytes">Paper</a>'
)
PAPER_COMING_SOON = '<span class="action-link action-link--disabled" aria-disabled="true">Paper — Coming Soon</span>'


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=("auto", "embargo", "full"), default="auto")
    parser.add_argument("--output", type=Path, default=Path("_site"))
    return parser.parse_args()


def copy_file(source: Path, destination: Path) -> None:
    assert source.is_file(), source
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)


def copy_directory(source: Path, destination: Path) -> None:
    assert source.is_dir(), source
    shutil.copytree(source, destination)


def assemble_site(mode: str, output: Path) -> None:
    assert mode in {"embargo", "full"}, mode
    assert not output.exists(), f"Output already exists: {output}"
    output.mkdir(parents=True)

    for filename in ("404.html", "robots.txt"):
        copy_file(REPOSITORY_ROOT / filename, output / filename)
    for directory in ("static", "publications"):
        copy_directory(REPOSITORY_ROOT / directory, output / directory)

    if mode == "embargo":
        homepage = (REPOSITORY_ROOT / "index.html").read_text()
        assert homepage.count(PAPER_LINK) == 1
        (output / "index.html").write_text(homepage.replace(PAPER_LINK, PAPER_COMING_SOON))
        copy_file(REPOSITORY_ROOT / "embargo/sitemap.xml", output / "sitemap.xml")
        copy_file(REPOSITORY_ROOT / "embargo/apex-coming-soon.html", output / "APEX/index.html")
        lowercase_alias = output / "apex"
        if lowercase_alias.exists():
            assert lowercase_alias.samefile(output / "APEX")
        else:
            copy_file(REPOSITORY_ROOT / "embargo/apex-alias.html", lowercase_alias / "index.html")
        apex_files = sorted(
            path.relative_to(output / "APEX") for path in (output / "APEX").rglob("*") if path.is_file()
        )
        assert apex_files == [Path("index.html")], apex_files
        assert not (output / "APEX/static/pdfs/apex_paper.pdf").exists()
    else:
        copy_file(REPOSITORY_ROOT / "index.html", output / "index.html")
        copy_file(REPOSITORY_ROOT / "sitemap.xml", output / "sitemap.xml")
        copy_directory(REPOSITORY_ROOT / "APEX", output / "APEX")
        copy_directory(REPOSITORY_ROOT / "apex", output / "apex")
        assert (output / "APEX/static/pdfs/apex_paper.pdf").is_file()

    (output / ".nojekyll").touch()


def main() -> None:
    args = parse_args()
    if args.mode == "auto":
        mode = "embargo" if EMBARGO_MARKER.exists() else "full"
    else:
        mode = args.mode
    output = args.output if args.output.is_absolute() else REPOSITORY_ROOT / args.output
    assemble_site(mode, output)
    print(f"Assembled {mode} site at {output}")


if __name__ == "__main__":
    main()
