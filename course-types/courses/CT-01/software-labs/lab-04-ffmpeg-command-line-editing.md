# CT-01 Software Lab 04 — FFmpeg: Command-Line Editing and Validation

**Track:** Cross-platform command-line media processing  
**Reference baseline:** Official FFmpeg documentation checked 16 November 2026. Commands depend on the FFmpeg build, codecs and shell.  
**Practice time:** 2–3 hours  
**Prerequisites:** Basic file/folder navigation; CT-01 Lessons 01–04  
**Safety:** Work on copies. Commands below write new output files; inspect paths before execution.

## Outcomes
Inspect media, trim a clip, create a vertical derivative, concatenate compatible clips, and validate output metadata and playback.

## Key terms
- FFmpeg: multimedia framework with command-line tools and libraries.
- ffprobe: companion utility for inspecting media streams and container metadata.
- Codec: method for encoding/decoding media.
- Container: file format that holds one or more streams.
- Filter: operation applied to audio/video streams.
- Stream: video, audio, subtitle or data track inside a media file.
- Transcode: decode and encode media into a new representation.
- Concat demuxer: reads a list of compatible media files as one input.
- Filter graph: connected chain of audio/video operations.

## Lab A — Confirm installation and inspect media
1. Open Terminal, PowerShell or the shell used by your system.
2. Run `ffmpeg -version` and `ffprobe -version`.
3. Create a working folder and copy practice assets into it.
4. Inspect a file:
   ```bash
   ffprobe -v error -show_entries format=duration,format_name:stream=index,codec_type,codec_name,width,height,r_frame_rate,sample_rate,channels -of json "input.mp4"
   ```
5. Record duration, codecs, dimensions, frame rate and audio streams. Do not infer frame rate from filenames.

## Lab B — Create a review trim
Use a short excerpt from a source file:
```bash
ffmpeg -i "input.mp4" -ss 00:00:05 -t 00:00:10 -c:v libx264 -crf 20 -preset medium -c:a aac -b:a 192k "trim-review.mp4"
```
This decodes and re-encodes the selected interval. CRF is a quality-oriented control for x264, not a universal bitrate guarantee. Exact output quality and speed depend on source, encoder build and settings. For frame-accurate editing, validate the actual start/end and use a suitable workflow rather than assuming every seek mode is frame-exact.

## Lab C — Scale and pad to vertical
Create a 1080×1920 canvas while preserving the full image inside it:
```bash
ffmpeg -i "input.mp4" -vf "scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2" -c:v libx264 -crf 20 -preset medium -c:a aac -b:a 192k "vertical-padded.mp4"
```
This fits the whole frame and adds padding; it does not perform intelligent subject-aware reframing. Check whether the output should instead be cropped/reframed, and inspect dimensions and orientation.

## Lab D — Concatenate compatible files
The concat demuxer is appropriate when inputs have compatible streams, codecs, time bases and parameters. Create a UTF-8 text file named `list.txt`:
```text
file 'part-01.mp4'
file 'part-02.mp4'
```
Then:
```bash
ffmpeg -f concat -safe 0 -i "list.txt" -c copy "joined.mp4"
```
Use only trusted local filenames in the list. Stream copy avoids re-encoding but does not normalize incompatible media. If files differ in resolution, codec, frame rate or stream layout, use the concat filter and re-encode after deliberately normalizing each input. Read FFmpeg's concat documentation before using complex filter graphs.

## Lab E — Validate the output
1. Run ffprobe on every output.
2. Confirm duration, dimensions, frame rate and expected audio streams.
3. Play each file from beginning to end.
4. Inspect the first/last frame, sync and any transition points.
5. Compare the output to the written delivery requirements.

## Worked assignment
Create a 20–30 second montage from three self-recorded clips. Probe all inputs, trim useful sections, join compatible segments, create a vertical padded preview and validate all output metadata.

## Common errors and recovery
- `command not found`: install FFmpeg from a trusted source and ensure its executable is on PATH.
- Unknown encoder: inspect `ffmpeg -encoders`; available encoders depend on build configuration.
- Concat fails: inspect stream parameters; use a filter-based normalization/re-encode workflow for incompatible inputs.
- Audio missing: inspect input streams and explicitly map/select streams when necessary.
- Wrong orientation: inspect rotation metadata and display dimensions; normalize orientation deliberately.
- Output corrupt: test a short file, check disk space and permissions, then rerun with a simpler filter chain.

## Knowledge check
1. What is ffprobe used for?
2. What is the difference between stream copy and transcoding?
3. Why can concat demuxer fail on mismatched clips?
4. Does scale-and-pad automatically reframe a person?
5. Why inspect output metadata and playback?

### Answer key
1. Inspect container and stream properties.
2. Stream copy remuxes/copies encoded streams without decoding/re-encoding; transcoding decodes and encodes again.
3. The demuxer expects compatible stream parameters for seamless joining.
4. No; it preserves the full frame and adds padding.
5. A successful command does not guarantee correct framing, sync or delivery compliance.

## Submission and rubric — 30 points
Installation/environment report 3; accurate probing 5; trim 5; vertical conversion 5; compatible join 5; output validation and explanation 7. Pass 24/30; corrupt output or unverified stream properties must be corrected.

## Quality-control checklist
- [ ] Original files untouched.
- [ ] FFmpeg/ffprobe versions recorded.
- [ ] Input metadata logged.
- [ ] Commands and output paths documented.
- [ ] No unintended missing streams.
- [ ] Outputs play from beginning to end.
- [ ] Output properties match the intended brief.

## Official references
- FFmpeg, [Documentation index](https://ffmpeg.org/documentation.html)
- FFmpeg, [Filters documentation](https://www.ffmpeg.org/ffmpeg-filters.html)
- FFmpeg, [FAQ — concatenation](https://ffmpeg.org/faq.html#How-can-I-concatenate-video-files_003f)

## Version note
FFmpeg is actively developed and builds differ in enabled codecs/encoders. Run `ffmpeg -version` and `ffmpeg -encoders` locally. Treat this lab's commands as examples to test against the installed build, not guaranteed presets for every system.
