# Developer Portfolio Work Log

## 24 November 2026 — Smart File Organizer

I set out to build a lightweight Python utility to organize cluttered folders. I chose a preview-first command-line interface and the Python standard library to minimize dependencies and reduce the risk of accidental file changes.

Working with AI assistance, I established the project scope, created a public GitHub repository, and published the implementation, documentation and three automated regression tests. The implementation categorizes files by extension, skips hidden files and symlinks, and protects existing filenames with numeric suffixes.

An initial GitHub file creation attempt did not produce a confirmed commit. I resolved the publishing blocker by validating an existing README update before retrying file creation successfully. The exact original failure cause remains unknown.

I configured GitHub Actions to test Python 3.10 and 3.13 on Windows, macOS and Linux. The workflow is committed; its first results have not yet been verified. Hard-link support is required for apply mode.

## Next milestone — Gravity Lab

I created the public repository for a planned Python/Pygame physics sandbox. Implementation and testing are pending.

## 24 November 2026 — Gravity Lab implementation

With AI assistance, I implemented a Pygame projectile sandbox with adjustable keyboard-controlled gravity, mouse launching, trajectory trails and boundary bounces. I separated simulation logic from rendering and added four regression tests. All four corresponding physics checks passed in an isolated Python environment using the retrieved implementation. I published a GitHub Actions workflow targeting Windows, macOS and Linux with Python 3.12. Hosted CI results and graphical interaction remain unverified; Pygame was not installed in the local test environment. The simulation does not model particle-to-particle collisions.
