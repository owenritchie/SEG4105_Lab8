# Development Methodology

## 1. Software Development Lifecycle (SDLC)
- Framework: Agile Scrum with 2-week sprints, timed against the project milestones (requirements by Dec 18, 2026, software and ML model by Mar 26, 2027, 20-hive pilot by Apr 16, 2027, go-live by Apr 30, 2027).
- Planning & Tracking: Work items are logged as GitHub Issues and prioritized in Project Boards. Each sprint ends with a review of the dashboard with the grower and a retrospective.

## 2. Version Control & Branching Strategy
- Workflow: GitHub Flow.
- main: Always contains production-ready, tested code.
- feature/* | fix/* | docs/*: Short-lived branches created from main for isolated changes (e.g. `feature/add-documentation`, `docs/architecture-and-methodology`).
- Commit Convention: Conventional Commits style prefixes (feat:, fix:, docs:, refactor:, test:), e.g. `Docs: add initial README`.

## 3. Code Review & Definition of Done (DoD)
1. Code compiles/runs locally without errors or regressions.
2. Unit and integration tests pass.
3. Relevant documentation (README and /docs) is updated.
4. Changes are submitted via Pull Request and reviewed prior to merging into main.

## 4. Testing & Quality Assurance Strategy
- Unit Testing: Python `unittest` (`python -m unittest discover -s tests`), covering the strength estimate and status bands in `src/core`. Target: 80% line coverage of `src/core` and `src/data`.
- Integration / System Testing: Build the Docker image and run it, then check `/health`, `/api/hives` and the dashboard end to end. During the 20-hive pilot, compare the estimated frames against manual inspections to confirm the ±0.5 frame accuracy target on at least 95% of hives.
