# CT-01 Software Lab 01 — DaVinci Resolve 20: Project, Edit, Color and Deliver

**Track:** Desktop NLE  
**Reference baseline:** DaVinci Resolve 20 documentation. Resolve 21.1 documentation is also available; page names and features may change between releases and editions. Confirm the installed version before following UI labels.  
**Practice time:** 2–3 hours  
**Prerequisites:** CT-01 Lessons 01–09  
**Practice assets:** 5–8 self-recorded or properly licensed clips, one voice recording, one music track, one still image. Do not use unlicensed commercial music or stock footage.

## Outcomes
Create a project, organize media, assemble and refine a sequence, perform a basic grade, balance sound and export a verified review file.

## Important version and edition note
Resolve's page-based workflow commonly includes Media, Cut, Edit, Fusion, Color, Fairlight and Deliver. Available tools can differ by version, operating system and Free/Studio edition. This lab teaches stable workflow concepts; do not assume every effect or codec is available in every edition. Blackmagic's official Resolve 20 Beginner's Guide and current Reference Manual are the authority for current UI details.

## Key terms
- Project library: location/database that stores Resolve project records.
- Media Pool: project bin area for imported media.
- Timeline: ordered video and audio tracks.
- Inspector: controls for selected clip properties; exact controls depend on selection and page.
- Node: modular processing step used in color and compositing workflows.
- Deliver: page/workspace for configuring and rendering output.

## Lab A — Project and ingest
1. Launch Resolve and open the Project Manager.
2. Create a new project named CT01_Resolve_Lab01.
3. Save a copy/backup of source assets in a stable folder before importing.
4. In the Media page or Media Pool, navigate to the practice folder and import the clips.
5. Create bins named Video, Audio, Stills and Exports (or equivalent folders/bins).
6. Review clip properties and note mixed frame rates, orientation and audio.
7. Before editing, confirm intended timeline resolution and frame rate from the brief. In Resolve, project settings are available through the Project Settings control; current reference manuals describe timeline format and related settings there.
8. Create a timeline using the confirmed settings. Do not change frame rate casually after editing has begun.

## Lab B — Assembly and refinement
1. Open the Edit page (or the equivalent timeline editing workspace in the installed version).
2. Place a strong opening image, then assemble setup, process and payoff.
3. Use source viewer and timeline viewer to distinguish source selection from sequence playback.
4. Trim clip heads/tails; use ripple operations carefully and check downstream sync.
5. Add a second audio track for voice and another for music.
6. Create J/L cuts by allowing audio and picture boundaries to differ where the story benefits.
7. Add only purposeful transitions. Keep straight cuts as the default.
8. Add a simple title using built-in title tools; verify spelling and phone-size readability.
9. Save a new project version before color and audio finishing.

## Lab C — Basic color and audio
1. Open the Color page and select a representative shot.
2. Review image with scopes where available; balance exposure and white balance conservatively.
3. Match neighboring shots before applying a creative look.
4. Avoid applying a LUT unless its camera/input transform assumptions are known.
5. Open Fairlight or the available audio mixer workspace.
6. Balance dialogue first, then music. Use fades at edits and check for clicks.
7. Review the whole sequence with sound; do not judge only by meters.

## Lab D — Export and verify
1. Open Deliver.
2. Choose a preset only if it matches the written delivery brief; otherwise set dimensions, frame rate, codec/container and audio deliberately.
3. Set a clear filename and output path in the Exports folder.
4. Add the job to the render queue and render.
5. Open the rendered file in a separate media player.
6. Check duration, dimensions, frame rate, audio presence, sync, first/last frame and all known edit points.
7. Reopen the project and confirm source media remains online.

## Worked assignment
Create a 45–60 second craft/process story in 16:9. Make a second 9:16 timeline by reframing shots individually; do not assume a center crop keeps every subject visible.

## Common problems
- Media offline: restore original folder path or relink to the stable source folder.
- Timeline frame rate wrong: inspect project/timeline settings before editing; create a correctly configured timeline if required.
- Color looks extreme: verify input color interpretation and remove unknown LUTs.
- Render fails: check disk space, output permissions, unsupported effects/codecs and system load; test a short range.
- Export differs from viewer: inspect the actual file and verify output scaling, color tags and render settings.

## Knowledge check
1. What does the Project Manager store?
2. Why confirm timeline settings before detailed editing?
3. What is the purpose of matching shots before a look?
4. Why inspect the rendered file outside Resolve?
5. Why create a separately reframed vertical version?

### Answer key
1. Project records in the selected project library.
2. Changing core timing/format settings late can complicate conform and playback.
3. To create a consistent base before creative styling.
4. The export—not the timeline preview—is the delivered artifact.
5. Subject placement, titles, captions and composition differ by aspect ratio.

## Submission and rubric — 30 points
Project setup/media organization 5; story assembly 6; trim/continuity 5; color/sound 5; export specification 4; independent playback and reopen test 5. Pass 24/30; any missing-media or corrupt-export failure must be corrected.

## Quality checklist
- [ ] Source originals preserved and backup exists.
- [ ] Project name and media bins are clear.
- [ ] Timeline matches the brief.
- [ ] Dialogue is intelligible and music does not mask it.
- [ ] Shots are consistent and titles readable.
- [ ] Export metadata matches the brief.
- [ ] Rendered file played independently.
- [ ] Project reopens with media online.

## Official references
- Blackmagic Design, [DaVinci Resolve 20 Beginner's Guide](https://documents.blackmagicdesign.com/UserManuals/DaVinci-Resolve-20-Beginners-Guide.pdf)
- Blackmagic Design, [DaVinci Resolve Reference Manual](https://documents.blackmagicdesign.com/UserManuals/DaVinciResolveReferenceManual.pdf)

## Version note
This lab is written against the Resolve 20 learning guide and current reference-manual concepts. Resolve 21.1 documentation is also published. Recheck the installed release's manual for changed controls, supported codecs and edition-specific features before teaching a precise click path.
