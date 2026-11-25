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

## 25 November 2026 — Portfolio verification

I checked the latest workflow for each repository against its main-branch commit before making changes. Six workflows were green. Habit Tracker had failed at static analysis, and Pixel Studio's workflow only compiled TypeScript even though its package manifest advertised a test command.

### Smart File Organizer

My local Python 3.9 run exposed a mismatch between the documented Python 3.8 minimum and the use of `Path.hardlink_to`, which arrived in Python 3.10. I switched to `os.link` and kept the link-before-unlink order. I verified preview, apply and invalid directory handling through the CLI with temporary files. Six regression tests cover classification, name collisions, skipped entries, unsafe symlink destinations and source retention when hard-link creation fails. I moved the Python 3.8 compatibility job to Ubuntu 22.04 after the default Ubuntu 26.04 runner could not install that version. The revised seven-job matrix passed on Linux, macOS and Windows. Symbolic-link cases can skip when a runner lacks permission to create links. Apply mode still requires hard-link support on the same filesystem, and an interrupted batch can leave earlier moves complete.

### Gravity Lab

I ran the four independent physics regressions for acceleration, zero gravity and boundary bounces and verified Python bytecode compilation. I added a Pygame smoke check with an SDL dummy display and scripted input. It starts the app, adjusts gravity down to zero and back up, launches a projectile, draws a trail, captures a rendered frame and clears the scene before exiting. The cross-platform physics jobs and Linux graphical smoke check passed. Physical pointer input in a desktop window remains unverified.

### Maze Escape

I kept the procedural generator and checked connectivity, reciprocal walls, bounded edges and lack of cycles with two Node tests. I fixed the canvas width relative to its content area and verified a narrow Chrome viewport. The browser test solved a generated maze using keyboard and emulated touch, checked move counts and victory, and verified the New maze control reset the game. The test captured a screenshot from the running page.

### Expense Tracker

I turned the CI command sequence into a reproducible Bash smoke test. Separate .NET CLI processes used a temporary JSON file containing only synthetic transactions. The build and smoke test passed, including case-insensitive category totals, the overall total, rejection of zero, negative and malformed amounts, preservation of the JSON after invalid input and Git ignore coverage for the default data files. The app remains a single-process local journal. A custom data path inside the repository needs an ignore rule.

### Pixel Studio

I restored the test file referenced by `npm test` and updated CI to execute it. TypeScript compilation and both Canvas and DOM test-double cases passed. Chrome verified real canvas colors after mouse and emulated touch input, clearing, narrow-screen layout and export of a 320×320 PNG. The browser test captured a running-editor screenshot.

### URL Shortener

I expanded the Go HTTP handler tests to cover invalid requests, unknown codes and 32 concurrent shorten-and-redirect operations with unique paths. The Go 1.22 build and all three test cases with race detection passed. The server retains its localhost binding and in-memory storage.

### Habit Tracker

The original GitHub Actions log showed that Flutter 3.50.1 resolved dependencies successfully and then exited during analysis. The diagnostic identified the `package:flutter/material.dart` import, which had been deprecated when Material widgets moved to a standalone package. I migrated to `material_ui` and kept analysis enabled. I preserved the SharedPreferences JSON format and added an injectable clock for the widget tests. Completion refreshes while the app is open and when it resumes.

I checked in Android and web scaffolding. The first fixed run passed analysis, all three widget tests and the web build, then stopped at Android assembly because the scaffold's Android Gradle Plugin was below Flutter 3.50.1's minimum. I aligned Gradle, the Android Gradle Plugin and Kotlin with the pinned Flutter release's templates. Android debug compilation then passed. The Android build verifies the APK. Running it on a physical Android device is a separate check.

The final Flutter run passed dependency resolution, clean static analysis, three widget tests, web compilation, Android debug compilation and a Chrome startup check. It uploaded the debug APK and a screenshot of the running web build. The widget tests cover creation, duplicate and blank input, completion, deletion, reloading and date rollover.

### Portfolio milestone

I updated the seven READMEs with setup, usage, verification commands, limitations and build badges. The workflows for the four graphical projects capture screenshots from the running applications. Chrome touch input was emulated for Maze Escape and Pixel Studio. Habit Tracker browser verification covered startup, and its feature checks ran as widget tests. Physical Android, touchscreen and desktop input remain useful follow-up checks.

These passing runs record the verification described above.

- [habit-tracker](https://github.com/kolawolesolomon/habit-tracker/actions/runs/45572020868)
- [smart-file-organizer](https://github.com/kolawolesolomon/smart-file-organizer/actions/runs/45572098900)
- [gravity-lab](https://github.com/kolawolesolomon/gravity-lab/actions/runs/45572345647)
- [maze-escape](https://github.com/kolawolesolomon/maze-escape/actions/runs/45572343133)
- [expense-tracker](https://github.com/kolawolesolomon/expense-tracker/actions/runs/45571892194)
- [pixel-studio](https://github.com/kolawolesolomon/pixel-studio/actions/runs/45572342869)
- [url-shortener](https://github.com/kolawolesolomon/url-shortener/actions/runs/45571899099)
