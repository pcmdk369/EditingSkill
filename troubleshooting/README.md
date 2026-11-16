# Troubleshooting Guide

## General diagnostic method
1. Describe the symptom and expected behavior.
2. Record application, version, operating system and hardware.
3. Identify when the problem began and whether it is reproducible.
4. Preserve project and source files before changing settings.
5. Isolate one variable at a time.
6. Prefer reversible fixes.
7. Retest the exact failing workflow.
8. Record root cause, fix and remaining limitations.

## Common issue categories
- Missing media: verify path, filename, drive availability and relink.
- Choppy playback: inspect codec, storage speed, resolution, cache and proxies.
- Export failure: inspect disk space, permissions, codec support, render range and logs.
- Audio sync: compare source frame rate, sample rate, timecode and drift.
- Color shift: inspect color management, display transforms, tags and player behavior.
- Caption mismatch: verify transcript, timing basis, frame rate and encoding.
- AI artifacts: reduce transformation strength, use better references, mask/rework, or choose another method.
- Corrupt output: verify render completion, file size, metadata and full playback; rerender if needed.
