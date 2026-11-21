# CT-03 Professional Lab 01 — Build and Validate a Vertical Social Edit

- **Course:** CT-03 Short-Form & Social Video Editing
- **Level:** Intermediate implementation
- **Estimated time:** 3–4 hours
- **Environment:** Desktop or mobile editor capable of custom sequence dimensions, trimming, text and export
- **Software/version:** Record the exact application, version, OS and edition used by the learner. This lab intentionally avoids unverified menu labels.
- **Source assets:** Learner-recorded footage or properly licensed media. Do not use copyrighted music or footage without permission.

## 1. Lab brief

Create a 20–30 second vertical video that communicates one clear idea, uses a truthful opening, demonstrates evidence, includes readable captions where speech is present, and ends with an appropriate next step.

## 2. Required inputs

Prepare:
- 6–12 video clips or one recording with multiple usable moments;
- optional original or licensed music and sound effects;
- transcript for spoken content;
- a one-sentence audience/message brief;
- destination platform and current export requirements.

Create a project folder:

```text
ct03-vertical-project/
  01-source/
  02-audio/
  03-project/
  04-graphics/
  05-exports/
  06-delivery/
  notes/
```

Copy source files into the project; keep originals backed up. Never rename or overwrite the only copy.

## 3. Deliverable specification

Record the approved aspect ratio, pixel dimensions, frame rate, duration, audio format, caption method and file-size/codec constraints. A common vertical working target is 9:16; confirm exact delivery settings with the brief and current destination documentation.

## 4. Implementation steps

1. Create the folder structure and copy the authorized assets.
2. Inspect each clip and record duration, orientation, resolution and frame rate where available.
3. Create a new project and sequence using the approved specification.
4. Review footage and build a selects list with source filenames and timecodes.
5. Write the central message and select a truthful hook.
6. Assemble the opening, evidence/process and payoff.
7. Remove repetition while preserving context and necessary action.
8. Reframe each shot individually; keyframe moving subjects when necessary.
9. Add captions from a corrected transcript. Review timing and spelling against the source.
10. Add music only when licensed or original; keep dialogue intelligible.
11. Add a concise CTA if required by the brief.
12. Review the full timeline at normal speed, then inspect frame-by-frame around cuts and text.
13. Export a review file using the approved specification.
14. Watch the exported file from beginning to end; do not validate only the timeline preview.
15. Correct defects, export a final version and record the settings.

## 5. Optional command-line inspection

If FFmpeg is installed, use the following non-destructive command to inspect a media file:

```bash
ffprobe -v error -show_entries format=duration:stream=codec_type,codec_name,width,height,r_frame_rate,sample_rate,channels -of json "input.mp4"
```

Expected result: JSON metadata describing the file's streams and duration. Replace the filename with an actual path. This command reads the file; it does not edit or export it.

## 6. Validation tests

| Test | Pass condition | Evidence |
|---|---|---|
| Aspect ratio | Matches approved vertical specification | Export metadata or editor settings |
| Duration | Within brief tolerance | Export metadata |
| Picture | No accidental black frames, missing media or unintended crop | Full playback review |
| Reframing | Subject/action remains visible | Shot-by-shot review |
| Captions | Accurate, synchronized and readable | Muted playback + transcript |
| Audio | No clipping; dialogue understandable | Headphone/speaker review |
| Rights | Every source and audio asset has a lawful basis | Asset log |
| Delivery | Final file and editable project are organized | Folder manifest |

## 7. Troubleshooting

- **Black bars:** verify sequence dimensions and clip scaling; do not stretch footage to fill.
- **Soft image:** check source resolution and avoid excessive scaling.
- **Jerky motion:** inspect frame-rate mismatch and keyframe interpolation.
- **Caption mismatch:** compare transcript and waveform/audio; correct manually.
- **Audio distortion:** reduce gain and re-export; do not normalize a clipped source and assume distortion is repaired.
- **Unexpected export:** verify codec, dimensions, frame rate and audio settings against the specification.

## 8. Submission manifest

Submit:
- final MP4 (or requested format);
- editable project and linked assets or a clearly documented package;
- specification sheet;
- selects log;
- transcript/caption file where applicable;
- rights/asset log;
- brief QC report listing checks, issues and fixes.

## 9. Rubric — 100 points

| Criterion | Points |
|---|---:|
| Message and hook | 15 |
| Story structure and pacing | 15 |
| Vertical composition and reframing | 15 |
| Caption accuracy and readability | 15 |
| Audio quality and intelligibility | 10 |
| Technical export compliance | 10 |
| Rights, accessibility and ethical accuracy | 10 |
| Project organization and handoff | 10 |
| **Total** | **100** |

Suggested pass: 80/100, with no critical failure in rights, source integrity or technical playback. A failed critical criterion requires correction regardless of total score.

## 10. Completion evidence

The lab is authored as an instructional procedure. It is not evidence that a learner has executed it. Record the learner's submitted artifacts and reviewer feedback before marking the practical task validated.
