# CT-23 Lesson 07 — AI-Assisted Transcription, Translation and Human Review

- Course: CT-23 — Subtitles, Captions & Localization
- Level: AI & Automation
- Estimated time: 120–180 minutes
- Prerequisites: Previous CT-23 lessons and authorized media/transcripts
- Tools/environment: Subtitle editor, text editor and target media player; record OS/app/version and locale
- Version/review date: Tool-neutral; verify current platform/accessibility specifications

## Learning outcomes
Use speech recognition and machine translation responsibly with consent, privacy, terminology control and frame-accurate human QA.

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
AI can accelerate draft transcription and translation but may hallucinate words, omit negation, misidentify speakers and mistranslate names. Voice/video may contain personal data. Review provider terms and obtain authorization before external processing. Human review remains necessary for meaning, accessibility and cultural accuracy.

## Tools, requirements and alternatives
Use a current subtitle editor and target playback tool. Record source master version, language/locale, file format and encoding. Use authorized media and protect sensitive recordings. Confirm destination requirements rather than assuming one universal reading-speed rule.

## Procedure
1. Classify source sensitivity and consent. 2. Check provider retention/training/commercial terms. 3. Preserve original media. 4. Generate transcript/translation draft. 5. Compare with audio and approved glossary. 6. Correct all cues and timing. 7. Log tool/model/version and reviewer. 8. Obtain approval and disclose use where required.

## Worked example
ASR drafts a transcript; a human corrects a technical term and speaker attribution before translation.

## Dry run
AI drops “not” from a sentence. Compare source and correct immediately; audit related cues for meaning reversal.

## Guided practice
Compare manual and AI transcripts, then produce a human-reviewed subtitle file.

## Independent assignment
Apply the workflow to a second clip or target locale. Submit source transcript, subtitle file, reviewer notes and validation evidence.

## Common errors and recovery
| Symptom | Likely cause | Diagnosis | Recovery |
|---|---|---|---|
| Submit original, AI draft, corrected transcript, target subtitles and provenance log. | Subtitle issue | Compare with source media and target player | Correct and retest |

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
