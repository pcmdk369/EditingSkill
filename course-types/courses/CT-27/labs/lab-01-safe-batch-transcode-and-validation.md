# CT-27 Professional Lab 01 — Safe Batch Transcode and Validation

- Level: Advanced / Professional
- Estimated time: 4–6 hours
- Environment: FFmpeg/FFprobe or equivalent; record version/build and OS
- Lab status: Authored procedure; commands must be tested against the learner's installed build

## Brief
Create a safe batch pipeline that probes authorized source videos, transcodes to a specified review format, validates each output and writes a CSV manifest. Never overwrite originals.

## Procedure
1. Create source, working, output, logs and quarantine folders.
2. Record FFmpeg/FFprobe versions and available encoders.
3. Generate an input manifest before processing.
4. Validate each input with FFprobe and reject corrupt/unreadable files.
5. Define an explicit target specification from the brief.
6. Run a dry-run to display planned commands and output paths.
7. Detect filename collisions and fail rather than overwrite.
8. Process one sample file and inspect quality, audio and metadata.
9. Run the batch with per-file logs and controlled concurrency.
10. Validate exit status, output existence, nonzero size, streams, duration and metadata.
11. Play each output or apply a representative playback sampling policy approved by the brief.
12. Write success/failure and error details to manifest.
13. Quarantine failures; do not silently skip.
14. Compare input/output counts and archive commands, logs and manifest.

## Example inspection command
```bash
ffprobe -v error -show_entries format=duration,size:stream=codec_type,codec_name,width,height,r_frame_rate,sample_rate,channels -of json "input.mp4"
```
This is read-only metadata inspection. Verify options against the installed FFprobe version.

## Validation
Input count equals processed plus rejected; every success has a playable output; every failure has a log and reason; no source file was modified; manifest paths resolve.

## Assessment — 100 points
Safe path handling 15; probe/inventory 15; target settings 15; dry-run/collision handling 15; batch reliability 15; output validation 15; logs/manifest 10. Pass 80/100. Overwriting source media is a critical failure.
