# CT-19 Professional Lab 02 — Data-Driven Motion, Localization and Template QC

- Course: CT-19 — Motion Graphics & Kinetic Typography
- Level: Expert / Professional
- Estimated time: 4–5 hours
- Environment: Motion-graphics application, data source (CSV/JSON or equivalent), render and text QA tools
- Lab status: Authored procedure; no specific application expressions or runtime are certified

## Brief
Build a reusable animated title/lower-third system driven by a small data table. Deliver three language variants and two aspect ratios while preserving text accuracy, readability and brand consistency.

## Learning objectives
Build reusable controls, validate data mapping, adapt typography to localization, protect safe areas and test template outputs.

## Procedure
1. Define approved fields: speaker name, role, organization and language.
2. Create a source-of-truth data sheet with unique IDs and verified spelling.
3. Build a template with separate controls for text, color, position, timing and animation.
4. Use named controls and document supported character limits.
5. Create one reference render and obtain design approval.
6. Import data through the application's supported method; do not assume a particular scripting API.
7. Generate all variants and inspect missing/duplicate records.
8. Adapt layout for longer translations; do not shrink text below the agreed readable size automatically.
9. Create vertical and landscape compositions with independent safe-area checks.
10. Test accents, non-Latin scripts, punctuation, line breaks and font fallback.
11. Verify animation timing does not truncate names or titles.
12. Render a proof batch, review every output and correct mapping/layout defects.
13. Export final files and package template, fonts/assets (where licensing permits), data version and manifest.

## Validation
| Test | Method | Pass condition |
|---|---|---|
| Data mapping | Compare rendered output to source row | Exact match |
| Unique IDs | Audit output count | No missing/duplicate variants |
| Localization | Review every language | Correct script and line breaks |
| Readability | Playback at intended size | Text readable for required duration |
| Safe area | Inspect each aspect ratio | No important text obscured |
| Template portability | Open on clean system | Dependencies documented |
| Batch render | Reconcile job list and outputs | All expected files exist |

## Troubleshooting
- Missing glyph: use a properly licensed font with script coverage.
- Text overflow: revise hierarchy or layout; avoid arbitrary tiny type.
- Wrong name on render: audit row IDs and data binding.
- Vertical UI collision: recompose for the destination's safe area.
- Expression failure: document software/version and provide a static fallback.

## Deliverables
Template project, source data, three language variants, two aspect-ratio sets, font/license notes, render log, QC report and manifest.

## Assessment — 100 points
Template architecture 20; data integrity 20; localization 15; responsive layout 15; motion/readability 10; portability 10; documentation 10. Pass 80/100.

## Completion checklist
- [ ] Data source and version documented.
- [ ] Template controls named and explained.
- [ ] All records rendered exactly once.
- [ ] Language scripts and fonts validated.
- [ ] Safe areas checked in both ratios.
- [ ] Playback and timing reviewed.
- [ ] Package and manifest complete.
