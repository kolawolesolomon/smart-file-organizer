import tempfile
import unittest
from pathlib import Path
from organizer import organize

class OrganizerTests(unittest.TestCase):
    def test_preview_and_apply(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "photo.JPG"
            source.write_text("sample")
            self.assertEqual(len(organize(root)), 1)
            self.assertTrue(source.exists())
            organize(root, apply=True)
            self.assertFalse(source.exists())
            self.assertEqual((root / "Images/photo.JPG").read_text(), "sample")

    def test_collision(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "Documents").mkdir()
            (root / "Documents/a.txt").write_text("old")
            (root / "a.txt").write_text("new")
            organize(root, apply=True)
            self.assertEqual((root / "Documents/a.txt").read_text(), "old")
            self.assertEqual((root / "Documents/a_1.txt").read_text(), "new")

    def test_missing_folder(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(ValueError):
                organize(Path(tmp) / "missing")

    def test_categories_and_skipped_entries(self):
        files = {
            "photo.png": "Images", "report.pdf": "Documents",
            "movie.MP4": "Videos", "sound.WAV": "Audio",
            "backup.7z": "Archives", "LICENSE": "Other",
        }
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for name in [*files, ".secret.txt"]:
                (root / name).write_text(name)
            (root / "nested").mkdir()
            self.assertEqual(len(organize(root, apply=True)), len(files))
            for name, category in files.items():
                self.assertEqual((root / category / name).read_text(), name)
            self.assertTrue((root / ".secret.txt").is_file())
            self.assertTrue((root / "nested").is_dir())

    def test_symlink_source_is_skipped_and_symlink_destination_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "photo.png"
            source.write_text("original")
            outside = root / "outside"
            outside.mkdir()
            try:
                (root / "alias.png").symlink_to(source)
                (root / "Images").symlink_to(outside, target_is_directory=True)
            except (OSError, NotImplementedError) as error:
                self.skipTest(f"Cannot create symbolic links: {error}")
            with self.assertRaisesRegex(ValueError, "Unsafe destination"):
                organize(root, apply=True)
            self.assertEqual(source.read_text(), "original")
            self.assertEqual(list(outside.iterdir()), [])
            (root / "Images").unlink()
            self.assertEqual(len(organize(root, apply=True)), 1)
            self.assertTrue((root / "alias.png").is_symlink())

    def test_failed_hard_link_retains_source(self):
        from unittest.mock import patch

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "photo.png"
            source.write_text("original")
            with patch("organizer.os.link", side_effect=OSError("link failed")):
                with self.assertRaisesRegex(OSError, "link failed"):
                    organize(root, apply=True)
            self.assertEqual(source.read_text(), "original")
            self.assertFalse((root / "Images/photo.png").exists())

if __name__ == "__main__":
    unittest.main()
