# CT-23 Lesson 03 — Subtitle Formats: SRT, WebVTT and Technical Validation

- Course: CT-23 — Subtitles, Captions & Localization
- Level: Intermediate
- Estimated time: 120–180 minutes
- Prerequisites: Previous CT-23 lessons and authorized media/transcripts
- Tools/environment: Subtitle editor, text editor and target media player; record OS/app/version and locale
- Version/review date: Tool-neutral; verify current platform/accessibility specifications

## Learning outcomes
Create and validate common timed-text files, understand encoding and verify cue order/timestamps.

## Key definitions
- **Caption:** Timed text representing speech and, where required, meaningful non-speech audio.
- **Subtitle:** Timed text representing dialogue, often translated or adapted.
- **Cue:** One timed text event.
- **Reading speed:** Text amount relative to display duration.
- **SDH:** Subtitles for the deaf and hard of hearing.
- **Locale:** Language and regional conventions.
- **Glossary:** Approved terminology list.
- **Sidecar file:** Separate subtitle/caption file accompanying video.

## Purpose and theory
SRT and WebVTT use different syntax and metadata conventions. Timecode formatting, cue numbering, encoding and overlap handling matter. A file may look correct in a text editor but fail in a target player. Validate by reopening and testing in the intended playback environment.

## Tools, requirements and alternatives
Use a current subtitle editor and target playback tool. Record source master version, language/locale, file format and encoding. Use authorized media and protect sensitive recordings. Confirm destination requirements rather than assuming one universal reading-speed rule.

## Procedure
1. Choose format from delivery brief. 2. Export UTF-8 text. 3. Validate cue numbering and time syntax. 4. Check start/end order and overlaps. 5. Verify special characters and punctuation. 6. Open in target player/editor. 7. Play with captions enabled. 8. Record format/version and validation evidence.

## Worked example
A simple SRT cue includes index, start/end time and text; WebVTT begins with its required header and uses its own timestamp syntax.

## Dry run
Garbled accented characters indicate encoding mismatch. Re-export UTF-8 and test in target player.

## Guided practice
Convert a reviewed transcript into SRT and WebVTT and compare.

## Independent assignment
Apply the workflow to a second clip or target locale. Submit source transcript, subtitle file, reviewer notes and validation evidence.

## Common errors and recovery
| Symptom | Likely cause | Diagnosis | Recovery |
|---|---|---|---|
| Submit both files and parser/player test notes. | Subtitle issue | Compare with source media and target player | Correct and retest |

## Knowledge check
1. Why should captions be checked against audio?
2. What affects reading speed and cue segmentation?
3. How do SRT and WebVTT differ?
4. Why is localization more than literal translation?
5. What can automated QA not reliably verify?

## Answer guidance
1. ASR can mishear names, numbers, negation and speakers.
2. Text length, complexity, duration, language and audience.
3. They use different syntax/metadata conventions.
4. It adapts locale, idiom, culture, units and meaning.
5. Semantic accuracy, cultural nuance and accessibility context.

## Assessment rubric — 20 points
| Criterion | Points | Evidence |
|---|---:|---|
| Transcript accuracy | 4 | Source comparison |
| Timing/segmentation | 4 | Cue review |
| Format/encoding | 4 | Parser/player test |
| Translation/accessibility | 4 | Glossary/reviewer notes |
| Versioning/handoff | 4 | Manifest and QA log |

Pass: 16/20. Misleading translation, missing negation or unauthorized processing requires remediation.

## Quality-control checklist
- [ ] Exact source master identified.
- [ ] Transcript verified against audio.
- [ ] Cue timing and reading speed checked.
- [ ] Text segmentation and line breaks reviewed.
- [ ] Translation reviewed by competent human.
- [ ] Encoding/syntax tested in target player.
- [ ] Language/version and delivery manifest complete.

## Further study
- [W3C — WebVTT](https://www.w3.org/TR/webvtt1/)
- [W3C — Web Content Accessibility Guidelines](https://www.w3.org/WAI/standards-guidelines/wcag/)
- Confirm current platform caption/subtitle guidance.

## Version and change notes
Tool-neutral. Reading-speed limits and caption conventions vary by audience, platform and jurisdiction; follow the project specification.
