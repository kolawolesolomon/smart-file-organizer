# Smart File Organizer

[![Tests](https://github.com/kolawolesolomon/smart-file-organizer/actions/workflows/tests.yml/badge.svg)](https://github.com/kolawolesolomon/smart-file-organizer/actions/workflows/tests.yml)

Sort a cluttered folder from the command line with a preview-first Python tool. It categorizes top-level files by extension into Images, Documents, Videos, Audio, Archives and Other.

## Setup and use

Requires Python 3.8+ and the standard library. From the repository root, run the first command to review the plan and the second to apply it.

```sh
python organizer.py /path/to/folder
python organizer.py /path/to/folder --apply
```

Existing destination names receive numeric suffixes. Dot-prefixed files, symbolic links and subdirectories are skipped.

## Tests

```sh
python -m unittest -v
```

Tests use temporary directories and cover preview, moves, categories, collisions, skipped entries, invalid folders and link failures. GitHub Actions runs the suite on Linux, macOS and Windows. The symbolic-link test skips on hosts where the process cannot create links.

## Limitations

Apply mode needs hard-link support and source and destination on the same filesystem. The organizer creates the destination link before removing the original entry. If a move fails, earlier moves may already be complete. Avoid simultaneous edits to the target folder during apply mode.
