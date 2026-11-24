# Smart File Organizer

A lightweight Python CLI that sorts top-level files by extension into Images, Documents, Videos, Audio, Archives and Other.

## Usage

Requires Python 3.8+; no third-party dependencies.

```sh
python organizer.py /path/to/folder
python organizer.py /path/to/folder --apply
```

The first command previews changes. The second moves files, preserving existing names by adding numeric suffixes when necessary. Hidden files, symlinks and subfolders are skipped. Moves use hard links to avoid overwriting files; the filesystem must support hard links. A failure can leave earlier moves completed. Preview and back up important files first.

## Tests

```sh
python -m unittest -v
```

Initial implementation; automated tests are included.
