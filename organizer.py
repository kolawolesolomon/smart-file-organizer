"""Sort top-level files by extension, previewing changes by default."""
import argparse
import os
from pathlib import Path

CATEGORIES = {
    "Images": "jpg jpeg png gif webp svg",
    "Documents": "pdf doc docx txt csv xlsx pptx md",
    "Videos": "mp4 mov mkv avi",
    "Audio": "mp3 wav flac m4a",
    "Archives": "zip tar gz 7z",
}

def organize(folder, apply=False):
    folder = Path(folder)
    if not folder.is_dir():
        raise ValueError("Folder does not exist")
    moves = []
    reserved = set()
    for source in sorted(folder.iterdir()):
        if source.is_symlink() or not source.is_file() or source.name.startswith("."):
            continue
        ext = source.suffix.lower().lstrip(".")
        category = next((k for k, v in CATEGORIES.items() if ext in v.split()), "Other")
        directory = folder / category
        if directory.is_symlink() or (directory.exists() and not directory.is_dir()):
            raise ValueError(f"Unsafe destination: {directory}")
        target = directory / source.name
        index = 1
        while target.exists() or target.is_symlink() or target in reserved:
            target = directory / f"{source.stem}_{index}{source.suffix}"
            index += 1
        reserved.add(target)
        moves.append((source, target))
    if apply:
        for source, target in moves:
            target.parent.mkdir(exist_ok=True)
            os.link(source, target)
            source.unlink()
    return moves

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("folder", type=Path)
    parser.add_argument("--apply", action="store_true", help="Move files instead of previewing")
    args = parser.parse_args()
    try:
        moves = organize(args.folder, args.apply)
    except (OSError, ValueError) as exc:
        parser.exit(1, f"Error: {exc}\n")
    for source, target in moves:
        print(f"{source.name} -> {target.parent.name}/{target.name}")
    print(f"{len(moves)} files {'moved' if args.apply else 'planned (preview only)'}.")

if __name__ == "__main__":
    main()
