---
name: editskill-subtitles
description: Specialist agent for accurate, accessible captions, subtitles, transcription, synchronization, translation and localization.
---

# Subtitles and Captions — EditSkill Specialist Module

## 1. Scope and non-goals

Create, synchronize, format, translate and validate timed text for video, film, social media, streaming, education and accessibility. Distinguish subtitles that translate or represent dialogue from captions that may also describe meaningful non-speech audio. Follow the user's delivery brief and applicable accessibility requirements.

This module does not certify legal compliance, guarantee translation quality or treat automated speech recognition as authoritative.

## 2. Activation and intake

Activate when the task requests captions, subtitles, transcription, translation, localization, speaker labels, SRT/VTT files or caption quality review.

Collect:
- source media/audio and exact version;
- spoken language(s), target language(s), locale and script;
- verbatim, edited-for-reading or translated style;
- speaker identification requirements;
- caption format: burned-in, sidecar or both;
- destination platform, accessibility specification and reading conventions;
- names, technical vocabulary, brand terms and approved glossary;
- privacy/consent and retention restrictions for speech-processing services.

Do not send confidential audio to external transcription services without approval and an acceptable data-handling basis.

## 3. Key terminology

- **Cue:** one timed text event.
- **Timecode:** position in the media timeline.
- **SRT:** SubRip timed-text format.
- **WebVTT:** web video text track format.
- **Burned-in caption:** text rendered into the video image.
- **Sidecar caption:** separate timed-text file.
- **Reading speed:** text quantity relative to display duration, commonly expressed in characters per second or words per minute depending on the standard.
- **Localization:** adapting language, references, measurements and context for a target audience.
- **SDH captioning:** subtitles for the deaf and hard of hearing, including relevant non-speech audio information.

## 4. Production workflow

1. Confirm the exact source file and create a transcript draft.
2. Transcribe speech with timestamps where possible.
3. Human-check every line against the audio; pay special attention to names, numbers, negation, technical words and overlapping speech.
4. Establish speaker labels and non-speech audio conventions from the brief.
5. Segment text into natural phrases; avoid breaking names, articles or closely connected phrases awkwardly.
6. Time cues to speech and meaningful sound events.
7. Check reading speed and display duration against the target specification; use the governing platform/accessibility standard rather than assuming one universal limit.
8. Use line breaks that support natural reading and avoid covering faces, demonstrations or important graphics.
9. Translate only after the source transcript is verified. Preserve meaning, tone, names and uncertainty.
10. Have a competent human reviewer check localized text and cultural context.
11. Export the requested format and encoding.
12. Reopen the exported subtitle file and validate parsing, cue order, timestamps and overlaps.
13. Play the final video with captions enabled and review synchronization from beginning to end.

## 5. SRT example

```srt
1
00:00:01,200 --> 00:00:03,400
Welcome to today's editing lesson.

2
00:00:03,500 --> 00:00:05,800
We will build the sequence step by step.
```

SRT uses numbered cues and comma-separated milliseconds. This is a minimal example, not a complete style guide. Confirm the receiving platform's accepted syntax and encoding.

## 6. Timing and segmentation rules

- Cue start must not precede the relevant speech in a way that reveals information prematurely, unless the format intentionally uses anticipatory text.
- Cue end should allow reading while avoiding unnecessary persistence over unrelated shots.
- Avoid overlapping cues unless the target format and intended presentation explicitly support them.
- Keep speaker changes clear.
- Preserve meaningful pauses and non-speech audio when required.
- Do not silently “correct” a speaker's factual statement; caption what was said and flag a suspected factual error separately.
- Do not invent inaudible words. Mark uncertainty using the project's convention and escalate when meaning is material.

## 7. Quality-control checklist

- Accuracy: every caption matches source audio.
- Completeness: all required speech and meaningful sounds are represented.
- Timing: cues align with speech and do not drift.
- Segmentation: phrases and line breaks are readable.
- Readability: contrast, placement and duration are suitable.
- Language: spelling, punctuation, locale and terminology are consistent.
- Speakers: labels and identities are correct and appropriately consented.
- Technical: encoding, timestamps, cue order and format parse correctly.
- Integration: final export displays the intended captions on the target device/platform.

## 8. Troubleshooting

| Issue | Cause | Recovery |
|---|---|---|
| Captions drift later | inaccurate timing or media version mismatch | retime against the exact final master |
| Garbled characters | encoding mismatch | export in the required Unicode encoding and reopen |
| Cues overlap | rushed segmentation or poor timecodes | retime and validate sequential order |
| Wrong names/numbers | ASR misrecognition | compare with source and approved glossary |
| Translation feels unnatural | literal translation or locale mismatch | revise with a fluent reviewer |
| Captions obscure action | fixed placement | reposition or adjust shot/caption design |

## 9. Privacy, rights and human review

Treat voice recordings and transcripts as potentially personal information. Use only authorized source media. Confirm consent and service terms before external processing. Do not infer identity, age, health or other sensitive traits from voice. Obtain human review for translations, names, legal/medical/financial terminology and factual content.

## 10. Handoff record

Deliver the source version, transcript, caption files, language/locale, format, software/tool version, review status, known uncertainties and final synchronization evidence. Clearly distinguish machine-generated draft from human-reviewed captions.

## 11. Learning references

- [CT-03 Short-Form & Social Video](../../../course-types/courses/CT-03-short-form-social-video.md)
- [Professional Academic Standard](../../../standards/PCMDK369-PROFESSIONAL-ACADEMIC-STANDARD.md)
- [Shared course standard](../references/course-standard.md)


## 12. Course-specific learning route

For short-form vertical composition, caption accuracy and phone-preview practice, use [CT-03 Lesson 03 — Vertical Reframing, Captions and Safe Composition](../../../course-types/courses/CT-03/lesson-03-vertical-reframing-captions-and-safe-composition.md). The broader course sequence is [CT-03 Short-Form & Social Video Editing](../../../course-types/courses/CT-03-short-form-social-video.md). Follow the lesson's source-audio verification and accessibility checks; do not treat automatic transcription or platform-generated captions as approved without human review.
