# CT-01 — Professional Practice: Professional Delivery, Quality Control and Archive

**Course:** Video Editing  
**Pathway stage:** Professional Practice

## Learning outcomes
Translate a delivery specification into export settings; create masters and derivatives; inspect video/audio/captions; package editable projects; verify archives and prepare a handoff.

## Prerequisites
Lessons 01–13 and an approved picture-locked project.

## Key definitions
- Delivery specification: agreed technical and packaging requirements.
- Master: approved high-quality output intended as a source for distribution derivatives.
- Mezzanine codec: high-quality intermediate codec used for post-production or exchange.
- Distribution encode: compressed output intended for a specific platform or audience.
- Bitrate: amount of data encoded per unit of time.
- Container: file wrapper containing video, audio and other streams.
- QC: quality control, systematic inspection against requirements.
- Checksum: value used to verify file integrity.
- Archive: preserved project and media package intended for future retrieval.
- Manifest: list of files, versions and properties included in a delivery or archive.

## Why it matters
An export that looks correct in the editor may still have missing audio, wrong frame rate, incorrect captions, black frames or broken packaging. Professional delivery verifies the actual rendered files and the ability to reopen the project.

## Theory
Separate the master from platform derivatives. Use the client's specification rather than guessing a codec or bitrate. A high-bitrate file is not automatically better if the source is poor or the platform re-encodes it. Keep a high-quality master where required and generate derivatives from that controlled source or the approved project.

QC should include technical inspection and full playback. Check file integrity, dimensions, frame rate, duration, audio channels, loudness/peaks as specified, captions, spelling, black frames, sync, color and ending. Archive testing must include a restore test, not merely successful copying.

## Tools and alternatives
NLE export panel, media information utility, caption validator/player, checksum tool and storage with backup. Use a manual checklist if automated QC is unavailable.

## Procedure
1. Obtain the delivery specification and identify every required file.
2. Confirm sequence settings and picture lock.
3. Select a master format and codec according to the specification.
4. Confirm frame size, frame rate, scan type, pixel aspect, audio sample rate/channels and color tagging where required.
5. Export a short test and inspect playback before the full render when risk is high.
6. Render the master and verify that the file opens and plays.
7. Inspect the beginning, middle, end and every known problem area; for critical delivery, watch the full programme.
8. Check duration, dimensions, frame rate, audio channels, sync, peaks/loudness and caption timing.
9. Generate platform derivatives from the master or controlled project; adapt framing and captions per format.
10. Use descriptive filenames with project, version, format and date.
11. Package project file, required media, fonts/graphics where licensed, captions, manifests, approval and version notes.
12. Create checksums when appropriate and copy the archive to the required storage.
13. Restore a sample or full project copy to a separate location and confirm that it opens.
14. Deliver a manifest and note any known limitations.

## Worked example
A client requests a landscape master, vertical social version and separate SRT captions. Create the master according to the written spec. Build the vertical version as a deliberate reframing pass, not an automatic crop. Check captions independently in the SRT and burned-in version if both are requested.

## Dry run
Create a 10-second test export. Compare the file's actual dimensions, frame rate and audio channels to the specification. Open it in a separate player and verify that playback matches the timeline.

## Guided exercise
Export a short test, inspect metadata, check audio and captions, then correct one deliberately introduced issue such as a wrong filename or missing caption.

## Independent assignment
Deliver a complete package for a 60–90 second video: master, vertical derivative, captions, editable project, media manifest, QC report, version log and verified archive copy.

## Common errors and recovery
- Wrong export preset: compare actual file properties with the written spec and re-export.
- Audio missing or wrong channel layout: inspect routing and export audio settings.
- Captions out of sync: verify frame rate/timebase and retime against the final master.
- Vertical crop cuts off subject: reframe shot by shot and reposition graphics.
- Project opens offline: include required media or document relink paths; restore and retest.
- Archive copy corrupt: recopy, verify checksums and test restore before delivery.

## Knowledge check
1. Why distinguish a master from a distribution encode?
2. What is a delivery specification?
3. Name five QC checks.
4. Why must captions be checked against the final master?
5. What proves an archive is usable?

## Answer key
1. The master preserves a controlled high-quality source; distribution encodes are tailored to delivery platforms.
2. Written requirements for files, formats, dimensions, frame rate, audio, captions and packaging.
3. Any five: dimensions, frame rate, duration, sync, audio channels, loudness/peaks, captions, black frames, spelling, color.
4. Picture edits or frame-rate changes can alter timing.
5. A successful restore test and project-open check.

## Assessment rubric — 30 points
Specification interpretation 5; export correctness 6; playback and metadata QC 8; captions/audio 4; packaging and manifest 4; restore test 3. Pass 24/30.

## Quality-control checklist
- [ ] Delivery specification confirmed.
- [ ] Master and derivatives named correctly.
- [ ] Metadata matches specification.
- [ ] Video watched and audio listened to.
- [ ] Captions and spelling verified.
- [ ] Project and media package open correctly.
- [ ] Archive restore test succeeds.
- [ ] Handoff manifest and limitations included.

## Further study
Study broadcast delivery specifications, IMF/AS-11 where relevant, platform encodes, checksums, LTO/cloud archive strategy and media asset management.
