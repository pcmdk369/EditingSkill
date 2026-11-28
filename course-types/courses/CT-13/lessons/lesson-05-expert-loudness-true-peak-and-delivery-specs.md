# CT-13 Lesson 05 — Loudness, True Peak and Delivery Specifications

- Course: CT-13 — Audio Editing
- Level: Expert
- Estimated time: 120–180 minutes
- Prerequisites: Previous CT-13 lessons and authorized audio assets
- Tools/environment: DAW/audio editor, headphones/speakers and media inspector; record OS/app/version and audio interface
- Version/review date: Tool-neutral; delivery standards depend on client/platform

## Learning outcomes
Measure loudness and peak behavior, interpret delivery targets from the brief and export correct channel/format specifications.

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
Peak level measures instantaneous sample or reconstructed peak; loudness estimates perceived level over time. Integrated loudness and true peak are different metrics. Standards vary by platform, broadcaster and client. Never invent one universal target; use the written delivery spec and measure the final file.

## Tools, requirements and alternatives
Use a current DAW/audio editor. Record sample rate, bit depth, channel mapping, monitoring and software version. Use original or licensed media and preserve untouched source recordings. Verify client loudness and delivery specifications.

## Procedure
1. Obtain target loudness/peak/channel specification. 2. Confirm meter standard and measurement mode. 3. Mix dialogue/music/effects for clarity. 4. Measure integrated loudness and true peak. 5. Adjust gain/dynamics rather than blindly normalizing. 6. Verify channel layout and sample rate/bit depth. 7. Export a test and measure the rendered file. 8. Record final measurements.

## Worked example
A podcast deliverable specifies a particular integrated loudness and true-peak ceiling. The engineer measures the final export and records actual results.

## Dry run
Timeline meter passes but exported file clips after encoding. Measure the rendered file and adjust ceiling/encoding settings.

## Guided practice
Prepare a 60-second mix against a supplied target specification and document measurements.

## Independent assignment
Apply the workflow to a second source with different noise, dynamics or channel structure. Submit session, export, settings and QC evidence.

## Common errors and recovery
| Symptom | Likely cause | Diagnosis | Recovery |
|---|---|---|---|
| Submit master, meter report and export settings. | Audio workflow issue | Inspect waveform, routing and rendered file | Correct and remeasure |

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
