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

if __name__ == "__main__":
    unittest.main()
