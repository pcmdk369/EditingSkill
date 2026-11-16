# CT-13 Lesson 03 — Noise Cleanup, EQ and Dynamics

- Course: CT-13 — Audio Editing
- Level: Intermediate
- Estimated time: 120–180 minutes
- Prerequisites: Previous CT-13 lessons and authorized audio assets
- Tools/environment: DAW/audio editor, headphones/speakers and media inspector; record OS/app/version and audio interface
- Version/review date: Tool-neutral; delivery standards depend on client/platform

## Learning outcomes
Apply noise reduction, equalization and compression conservatively to improve clarity without introducing artifacts or pumping.

## Key definitions
- **Sample rate:** Number of audio samples per second.
- **Bit depth:** Number of bits used to represent each sample.
- **Waveform:** Visual representation of signal amplitude over time.
- **Crossfade:** Overlap of two clips with complementary fades.
- **EQ:** Equalization; frequency-dependent level adjustment.
- **Compression:** Dynamic-range control based on level and time behavior.
- **Integrated loudness:** Measurement of perceived loudness over a defined program.
- **True peak:** Estimate of peak level including inter-sample reconstruction.

## Purpose and theory
Noise reduction trades noise floor against artifacts. EQ changes frequency balance; compression reduces dynamic range above a threshold. Processing should solve an audible problem, not follow a fixed preset. Keep an unprocessed reference and use bypass comparison at matched loudness.

## Tools, requirements and alternatives
Use a current DAW/audio editor. Record sample rate, bit depth, channel mapping, monitoring and software version. Use original or licensed media and preserve untouched source recordings. Verify client loudness and delivery specifications.

## Procedure
1. Identify noise type and whether it can be removed at source. 2. Capture room tone where appropriate. 3. Apply light noise reduction and listen for artifacts. 4. Use high-pass filtering only when low-frequency content is unwanted. 5. Apply EQ for intelligibility and tonal balance. 6. Use compression with appropriate attack/release. 7. Compare processed/unprocessed at matched loudness. 8. Save processing settings and export a test.

## Worked example
Dialogue contains steady HVAC noise. A modest reduction lowers the noise while preserving consonants and room character.

## Dry run
Aggressive denoise creates watery artifacts. Reduce amount, use narrower selection or accept some noise rather than damaging speech.

## Guided practice
Clean one noisy dialogue clip and compare three processing levels.

## Independent assignment
Apply the workflow to a second source with different noise, dynamics or channel structure. Submit session, export, settings and QC evidence.

## Common errors and recovery
| Symptom | Likely cause | Diagnosis | Recovery |
|---|---|---|---|
| Submit processed/unprocessed examples, settings and artifact notes. | Audio workflow issue | Inspect waveform, routing and rendered file | Correct and remeasure |

## Knowledge check
1. How do sample rate and bit depth differ?
2. Why do fades prevent clicks?
3. What is the risk of aggressive noise reduction?
4. How do peak and loudness differ?
5. Why must the rendered file be measured and played back?

## Answer guidance
1. Sample rate is samples per second; bit depth relates sample quantization resolution.
2. They smooth abrupt waveform discontinuities.
3. It can introduce artifacts and damage speech/music.
4. Peak is instantaneous maximum; loudness estimates perceived program level.
5. Export can differ from session due to encoding, routing and processing.

## Assessment rubric — 20 points
| Criterion | Points | Evidence |
|---|---:|---|
| Session organization/source handling | 4 | Session and inventory |
| Editing/cleanup quality | 5 | Playback and comparison |
| Routing/sync | 3 | Routing and sync evidence |
| Loudness/export compliance | 4 | Meter report and metadata |
| Rights and handoff | 4 | Asset log and manifest |

Pass: 16/20. Unauthorized voice use or missing source integrity requires remediation.

## Quality-control checklist
- [ ] Original audio preserved.
- [ ] Session rate/channel layout documented.
- [ ] Cuts/fades are free of clicks.
- [ ] Processing artifacts checked.
- [ ] Dialogue intelligibility maintained.
- [ ] Delivery target measured on final render.
- [ ] Rights, dependencies and stems documented.

## Further study
- [EBU — Audio loudness recommendation R 128](https://tech.ebu.ch/publications/r128)
- [AES Standards](https://www.aes.org/standards/)
- Selected DAW's official current documentation.

## Version and change notes
Tool-neutral. Loudness and delivery targets must come from the actual brief; no universal platform target is assumed.
