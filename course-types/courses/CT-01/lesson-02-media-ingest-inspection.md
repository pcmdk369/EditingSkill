# CT-01 Lesson 02 — Media Ingest, Inspection and Organization

- Stage: Beginner
- Practice time: 75–100 minutes
- Prerequisites: Lesson 01
- Tools: File manager, NLE media browser, media player and optional FFprobe
- Assets: 5–10 legally usable video, audio and image files

## Learning outcomes
Safely copy source media; inspect technical properties; organize assets; identify common media problems; prepare a source inventory.

## Key definitions
- Ingest: controlled transfer and preparation of source media.
- Metadata: information about a file, such as date, dimensions, codec and duration.
- Container: a wrapper holding media streams and metadata, for example MP4 or MOV.
- Codec: method used to encode and decode a media stream, for example H.264 or ProRes.
- Proxy: an easier-to-edit copy used to improve playback performance.
- Relink: reconnect a project to media after its path changes.
- Checksum: calculated value used to help verify that a copied file matches its source.

## Why this matters
Ingest errors can later appear as missing clips, silent footage, poor playback or incorrect exports. Inspection catches these problems before editing.

## Theory
A filename extension does not fully describe a file. Two MP4 files can use different codecs, frame rates, dimensions and audio formats. Inspect the actual media properties when compatibility or delivery matters.

Use a consistent naming pattern such as Project_Topic_Take_Date. Preserve original camera names in an inventory when renaming working copies. Keep proxies clearly identified so they are not mistaken for camera originals.

## Tools and alternatives
Use the NLE media browser and operating system file manager. For detailed inspection, use a trusted media-information utility or FFprobe. Avoid unknown codec packs and untrusted converter downloads.

## Procedure
1. Confirm that assets are authorized for the project.
2. Copy files from cards or devices into the project source folders; do not edit camera originals in place.
3. Compare file counts and sizes. Where available, verify checksums.
4. Inspect duration, dimensions, frame rate, orientation, codec and audio channels.
5. Play the beginning, middle and end of long clips to detect corruption or gaps.
6. Listen with headphones at a safe volume; check for clipping, hum, wind and missing channels.
7. Import media into the NLE and organize bins by type or purpose.
8. Label proxies and generated media distinctly from originals.
9. Record each asset's filename, type, duration, properties, rights/source and issues.
10. Save the inventory with the project documentation.

## Worked example
A source clip is 3840×2160 at 29.97 fps with stereo audio. The brief asks for a 1920×1080, 29.97 fps web master. The 4K source can be edited in a 1080 sequence and scaled by the editor. Keep the original file and record its properties.

## Dry run: sample inventory
| Asset | Type | Duration | Properties | Audio | Notes |
|---|---|---:|---|---|---|
| VID_0042.MP4 | Video | 18 s | 3840×2160, 29.97 fps | Stereo | Clean |
| VO_Intro.wav | Audio | 24 s | WAV | Mono | Clear voice |
| Logo.png | Image | — | 2000×1000 | — | Transparent |

## Guided practice
Ingest five files, create bins by media type, inspect each asset and complete an inventory. Include a note for every file, even if no issue is observed.

## Independent assignment
Submit an ingest report containing filenames, media properties, rights/source, backup verification method and compatibility risks.

## Common errors and recovery
- Assuming extension identifies codec: inspect stream properties.
- Editing from a removable card: copy and verify first.
- Renaming originals: preserve original names and document any working-copy mapping.
- Missing audio: test source playback and channel mapping.
- Proxy mistaken for master: label clearly and verify export uses high-quality source media.

## Knowledge check
1. Define ingest.
2. Why is MP4 insufficient to identify a codec?
3. What problem does a proxy solve?
4. Name four video properties to record.
5. What does a checksum help verify?

## Answer key
1. Controlled transfer and preparation of media for a project.
2. MP4 is a container and can hold streams encoded with different codecs/settings.
3. It improves editing performance by using easier-to-decode media.
4. Any four: duration, dimensions, frame rate, codec, orientation, audio channels.
5. That a copied file matches its source, subject to a reliable checksum process.

## Assessment rubric — 20 points
Safe copy and backup 5; accurate inspection 5; organization 4; inventory and rights notes 4; problem identification 2. Pass: 16/20.

## Quality-control checklist
- [ ] Assets copied and verified.
- [ ] Originals preserved.
- [ ] Properties recorded.
- [ ] Audio and video spot-checked.
- [ ] Bins and folders are clear.
- [ ] Proxy/original distinction is clear.

## Further study
Study bitrate, timecode, codecs and proxy workflows. FFprobe options and NLE labels can vary by installed version.
