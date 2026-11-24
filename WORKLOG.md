# Developer Portfolio Work Log

Development journal for my seven-project portfolio. I direct the project scope and technical goals, using AI-assisted development tools.

## 24 November 2026 — Smart File Organizer

My objective was to build a lightweight Python utility for organizing cluttered folders. I prioritized a preview-first interface, minimal dependencies and protection against filename conflicts.

The implementation categorizes files by extension, skips hidden files and symlinks, and preserves existing filenames. Three regression tests cover preview and apply behavior, duplicate names and invalid folders.

An initial publishing attempt did not produce a confirmed commit. The publishing process was restored by validating a README update and retrying file creation. The original cause remains unknown.

The repository includes GitHub Actions for Windows, macOS and Linux with Python 3.10 and 3.13. Hosted test results remain unverified. Apply mode requires filesystem hard-link support.

## 24 November 2026 — Gravity Lab

My goal was to create an interactive educational physics sandbox using Python and Pygame. The design separates physics from rendering, with adjustable gravity, mouse launching, trajectory trails and boundary bounces.

Four regression tests cover acceleration, zero gravity and boundary collisions. The test suite and cross-platform GitHub Actions workflow are published. Execution results and graphical interaction still need independent verification. Particle-to-particle collisions are outside the current scope.

## 24 November 2026 — Maze Escape

My third project explores procedural generation and browser-based game development. I selected a dependency-free JavaScript approach using randomized depth-first search and Canvas rendering.

The published implementation includes keyboard and touch controls, a move counter, a victory condition and maze regeneration. Automated tests check connectivity, boundary integrity, reciprocal walls, absence of cycles and invalid dimensions. The README and Node.js GitHub Actions workflow are published. Test execution and browser verification remain pending.

## 24 November 2026 — Expense Tracker

My objective was a lightweight C# console journal with local JSON storage, category totals and input validation. The implementation, README and automated build and smoke-test workflow are published. Build and execution remain unverified.

## Habit Tracker

My goal was to explore Flutter and Dart through a daily habit checklist with local persistence. The application source, setup instructions and static analysis workflow are published. Platform scaffolding must be generated before running; device testing remains pending.

## Pixel Studio

My goal was a browser-based creative tool using TypeScript and Canvas. The implementation supports a 16×16 grid, color selection, clearing and PNG export. Build automation and documentation are published; build and browser checks remain pending.

## URL Shortener

My objective was to explore Go HTTP services, concurrency-safe storage and redirect handling. The implementation, tests, workflow and README are published. Storage is in memory and the service is localhost-only. Build and test execution remain unverified.
