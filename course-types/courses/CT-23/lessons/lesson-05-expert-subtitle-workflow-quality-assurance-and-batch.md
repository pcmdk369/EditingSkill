# CT-23 Lesson 05 — Subtitle Workflow, Quality Assurance and Batch Production

- Course: CT-23 — Subtitles, Captions & Localization
- Level: Expert
- Estimated time: 120–180 minutes
- Prerequisites: Previous CT-23 lessons and authorized media/transcripts
- Tools/environment: Subtitle editor, text editor and target media player; record OS/app/version and locale
- Version/review date: Tool-neutral; verify current platform/accessibility specifications

## Learning outcomes
Manage multi-language subtitle projects with glossary, versioning, automated checks and human review.

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
Large subtitle projects require source/version control, locale tracking, style consistency and QA. Automated checks can find overlaps, duration, line length and missing cues, but cannot reliably judge meaning or cultural accuracy. Maintain language-specific reviewer signoff.

## Tools, requirements and alternatives
Use a current subtitle editor and target playback tool. Record source master version, language/locale, file format and encoding. Use authorized media and protect sensitive recordings. Confirm destination requirements rather than assuming one universal reading-speed rule.

## Procedure
1. Build source/target language matrix. 2. Lock source video version. 3. Maintain glossary and style guide. 4. Generate/translate drafts. 5. Run syntax/timing checks. 6. Assign fluent review per language. 7. Track corrections and versions. 8. Validate each file against exact master.

## Worked example
A series has five languages; each file is linked to a master version, glossary version and reviewer.

## Dry run
One language file is timed against an older edit. Reconcile master version and retime affected cues.

## Guided practice
Create a two-language subtitle package with automated and human QA logs.

## Independent assignment
Apply the workflow to a second clip or target locale. Submit source transcript, subtitle file, reviewer notes and validation evidence.

## Common errors and recovery
| Symptom | Likely cause | Diagnosis | Recovery |
|---|---|---|---|
| Submit language matrix, files, glossary, QA report and approvals. | Subtitle issue | Compare with source media and target player | Correct and retest |

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
