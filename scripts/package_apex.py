#!/usr/bin/env python3

import argparse
import io
import subprocess
import tarfile
from pathlib import Path, PurePosixPath
from zipfile import ZIP_DEFLATED, ZipFile


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
ARCHIVE_ROOT = PurePosixPath("APEX-project-site")
PAPER_PATH = PurePosixPath("static/pdfs/apex_paper.pdf")
LOCAL_README = """APEX project site

Open index.html directly, or serve this directory locally:

    python3 -m http.server 8000

Then open http://localhost:8000/.
"""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Package the complete APEX site with a private local paper PDF.")
    parser.add_argument("--paper", required=True, type=Path, help="Private apex_paper.pdf outside this repository")
    parser.add_argument("--output", required=True, type=Path, help="Destination .zip path outside this repository")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    paper = args.paper.expanduser().resolve()
    output = args.output.expanduser().resolve()

    assert paper.is_file(), paper
    assert paper.suffix == ".pdf", paper
    with paper.open("rb") as paper_file:
        assert paper_file.read(5) == b"%PDF-"
    assert output.suffix == ".zip", output
    assert output.parent.is_dir(), output.parent
    assert not output.exists(), output

    git_archive = subprocess.run(
        ["git", "archive", "--format=tar", "HEAD:APEX"],
        cwd=REPOSITORY_ROOT,
        check=True,
        stdout=subprocess.PIPE,
    ).stdout

    archived_paths: set[PurePosixPath] = set()
    with tarfile.open(fileobj=io.BytesIO(git_archive)) as source, ZipFile(output, "x", ZIP_DEFLATED) as destination:
        for member in source.getmembers():
            if member.isdir():
                continue
            assert member.isfile(), member
            path = PurePosixPath(member.name)
            assert not path.is_absolute(), path
            assert ".." not in path.parts, path
            archived_paths.add(path)
            if path == PAPER_PATH:
                continue
            source_file = source.extractfile(member)
            assert source_file is not None, member
            destination.writestr(str(ARCHIVE_ROOT / path), source_file.read())

        assert PurePosixPath("index.html") in archived_paths
        destination.write(paper, str(ARCHIVE_ROOT / PAPER_PATH))
        destination.writestr(str(ARCHIVE_ROOT / "README.txt"), LOCAL_README)

    print(f"Created private APEX site archive: {output}")


if __name__ == "__main__":
    main()
