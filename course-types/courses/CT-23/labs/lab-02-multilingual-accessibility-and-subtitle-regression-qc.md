# CT-23 Professional Lab 02 — Multilingual Accessibility and Subtitle Regression QC

- Course: CT-23 — Subtitles, Captions & Localization
- Level: Expert / Professional
- Estimated time: 4–6 hours
- Environment: Subtitle editor, media player, transcript/source audio and QA spreadsheet
- Lab status: Authored procedure; no platform-specific compliance certification is claimed

## Brief
Deliver captions and localized subtitles for a short video in two target languages. Validate transcript accuracy, cue timing, reading speed, speaker identification, accessibility and file compatibility.

## Procedure
1. Freeze the exact picture/audio master and record its version/duration.
2. Confirm source language, target locales, style guide and delivery format.
3. Create a source transcript with speaker/timecode information.
4. Human-check transcript against audio before translation.
5. Create localized drafts with an approved glossary and terminology list.
6. Have a competent fluent reviewer check meaning, tone, names, numbers and cultural references.
7. Segment cues around natural phrase boundaries.
8. Check reading speed and display duration against the client/platform standard; record the metric and threshold used.
9. Check speaker labels, sound descriptions and non-speech cues according to the requested caption type.
10. Validate SRT/VTT syntax, encoding, cue order, timestamps and overlaps.
11. Preview captions on target devices/aspect ratios and ensure text does not obscure essential visual information.
12. Run a regression check after every picture or transcript revision.
13. Deliver sidecar files and burned-in versions only where requested.
14. Create a language/version manifest and unresolved-issue list.

## Validation
| Test | Method | Pass condition |
|---|---|---|
| Transcript | Full audio comparison | Speech represented accurately |
| Translation | Fluent human review | Meaning and terminology preserved |
| Timing | Playback at normal speed | Cues align with speech |
| Reading speed | Calculate per selected standard | Within specified limits |
| Format | Parse/reopen file | Valid syntax/encoding |
| Accessibility | Visual/audio review | Required speakers/sound cues included |
| Regression | Compare with final master | No stale timecodes |
| Device | Preview target playback | Readable and unobstructed |

## Troubleshooting
- Subtitle drift after picture edit: regenerate/re-time against final master.
- Line overflow: resegment or rewrite for reading, preserving meaning.
- Font/script fallback: use licensed font with required glyph coverage.
- Ambiguous idiom: escalate to fluent locale reviewer.
- Cue overlaps: revise timing and validate sequentially.
- Incorrect speaker attribution: compare source and approved speaker map.

## Deliverables
Source transcript, two localized subtitle files, style/glossary sheet, QA report, timing/readability metrics, regression record and delivery manifest.

## Assessment — 100 points
Transcript accuracy 20; localization 20; timing/segmentation 15; accessibility 15; format validation 10; regression control 10; handoff 10. Pass 80/100. Material mistranslation or misattribution is a mandatory failure.

## Completion checklist
- [ ] Exact master version identified.
- [ ] Source transcript human-checked.
- [ ] Glossary and locale reviewed.
- [ ] Timing and reading speed measured.
- [ ] Format/encoding validated.
- [ ] Accessibility preview completed.
- [ ] Regression test and manifest complete.
