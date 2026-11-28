# CT-03 Lesson 03 — Vertical Reframing, Captions and Safe Composition

- **Course:** CT-03 — Short-Form & Social Video Editing
- **Level:** Intermediate
- **Estimated time:** 210–270 minutes, including transcript correction, reframing practice, device review and revision
- **Prerequisites:** Lessons 01–02; basic timeline navigation; an authorized source clip containing a moving subject and a short spoken passage
- **Tools/environment:** Any editor with crop/transform and timeline controls; optional keyframe/tracking tools; text or subtitle editor; headphones; phone-sized preview. A spreadsheet or paper log is sufficient for planning.
- **Version/review date:** Revision 2.0 — 2026-11-18. Platform interface overlays, caption upload rules and editor menus change; verify current official guidance for the actual destination and installed version.

## Learning outcomes

By the end, learners can:
1. Explain the difference between a crop, reframing, pan-and-scan, tracking and a designed vertical composition.
2. Calculate a crop window and identify when a source cannot support the desired framing without unacceptable enlargement.
3. Reframe static and moving subjects while preserving action, spatial relationships and continuity.
4. Choose between keyframing, tracking, alternate shots, split composition, background extension or a new source take.
5. Distinguish captions, subtitles, transcripts, burned-in text and sidecar timed-text files.
6. Correct an automatically generated transcript against the original audio and preserve speaker meaning.
7. Segment and synchronize captions using phrase boundaries, reading conditions and relevant non-speech audio.
8. Design text hierarchy, contrast, line breaks and screen placement for small-screen viewing.
9. Test composition against destination interface obstructions without assuming a universal safe-zone measurement.
10. Conduct silent, audio-only, full-speed and device-sized quality reviews.
11. Record source, rights, translation, version and approval evidence for a captioned vertical deliverable.

## Key definitions and terminology

| Term | Definition | Context/example |
|---|---|---|
| Aspect ratio | Proportional relationship between frame width and height. | 9:16 is taller than it is wide. |
| Crop | Selecting a smaller visible region from a larger image. | A central 9:16 crop from a landscape frame. |
| Reframing | Deliberately changing the visible area and subject placement for a new composition. | Moving the crop window to keep a speaker visible. |
| Pan-and-scan | Moving a crop window across a larger source image over time. | Following a person moving across a landscape shot. |
| Letterboxing / pillarboxing | Adding bars to fit a different aspect ratio without cropping. | Side bars around a landscape image in a vertical canvas. |
| Scale factor | Amount an image is enlarged or reduced. | A 1.5× enlargement increases displayed size but may reveal softness. |
| Pixel dimensions | Number of horizontal and vertical pixels in an image or video frame. | 1920 × 1080 source dimensions. |
| Keyframe | A stored parameter value at a specific timeline time; the editor interpolates values between keyframes. | Position at 00:00 and 00:04. |
| Interpolation / easing | Method used to calculate motion between keyframes. | Linear movement versus a gradual ease-in/ease-out. |
| Tracking | Estimating a subject or feature's movement so a crop, graphic or effect can follow it. | Tracking a face or product in a shot. |
| Safe composition area | A project-defined region that avoids critical content being obscured or cut off in the intended viewing context. | Keeping a CTA clear of a known app overlay. |
| UI overlay | Interface element displayed above content by a platform or player. | Profile, caption, share or navigation controls. |
| Caption | Timed text conveying speech and relevant non-speech audio information for accessibility or comprehension. | Dialogue plus “[door closes]” when relevant. |
| Subtitle | Timed text primarily representing dialogue, often translated or intended for viewers who do not understand the spoken language. Conventions vary by region and use. | English translation of spoken Thai. |
| Transcript | Text record of spoken content, generally not necessarily timed to playback. | Corrected interview transcript. |
| SDH | Subtitles for the Deaf and Hard of Hearing; a convention that includes speaker identification and meaningful sound information. | “(MAYA) The motor is running.” |
| Burned-in / open captions | Text permanently rendered into the video image. | Captions visible in every compatible player. |
| Sidecar / closed captions | Timed text delivered separately and displayed by a compatible player or platform. | SRT or WebVTT file, subject to platform support. |
| Cue | A timed text unit with a start/end time and text. | One phrase appearing from 00:00:02.100 to 00:00:04.000. |
| Reading speed | Rate at which viewers must read displayed text, often estimated in characters per second or words per minute. | A long cue shown briefly may be difficult to read. |
| Speaker label | Text identifying who is speaking when identity is not obvious or distinction matters. | “HOST:” or a verified speaker name. |
| Sound cue | A text description of meaningful non-speech audio. | “[alarm sounds]” when it affects understanding. |
| Text hierarchy | Visual ordering that communicates what to read first, second and third. | Dialogue caption first; optional speaker label secondary. |
| Contrast ratio | Relative luminance contrast between foreground and background, measured under a defined method. | White text against a dark translucent panel. |
| Localization | Adapting language and cultural references for a target audience while preserving meaning. | Translating idioms rather than word-for-word substitution. |
| Caption drift | Progressive timing mismatch between text and actual speech. | Captions increasingly appear late after a frame-rate or edit change. |

## Purpose and professional relevance

A vertical adaptation is a new composition with a different visual field. The editor must protect the story's evidence and the subject's action while deciding what the viewer should see first. A technically centered crop can be editorially wrong if it cuts off a hand demonstrating a feature, removes a second participant, changes a person's apparent gaze direction or hides the context that makes a statement understandable.

Captions are not decorative stickers. They carry meaning, support access for Deaf and hard-of-hearing viewers, help viewers in sound-sensitive environments and can support comprehension across languages. Incorrect captions can create factual, reputational, safety and legal risk. Auto-transcription is a draft, not an authoritative source.

Professional delivery therefore requires two independent forms of review:
- **Picture composition:** subject/action visibility, continuity, crop quality, overlays and small-screen legibility.
- **Text/audio integrity:** transcript accuracy, speaker attribution, cue timing, meaningful sound information, translation quality and text accessibility.

Do not assume that a single crop, font size, caption position or safe-zone percentage works for every platform, device, interface state, language or accessibility need.

## Theory and decision principles

### 1. Understand the crop geometry

For a source frame of width (W_s) and height (H_s), the source aspect ratio is (W_s/H_s). For a target aspect ratio (r_t), a crop that fills the target without empty bars can be planned in either direction:

- If the target is narrower than the source, retain the full source height and calculate crop width (W_c = H_s 	imes r_t).
- If the target is wider than the source, retain the full source width and calculate crop height (H_c = W_s/r_t).

The crop window can then move within the source boundaries. These equations describe geometry only; they do not decide the best artistic composition or guarantee sufficient resolution.

**Example:** A 1920 × 1080 source has ratio 16:9 (approximately 1.778). A 9:16 target has ratio 0.5625. Keeping the full 1080-pixel height gives a crop width of 607.5 pixels. In practice, the editor chooses integer pixel bounds and positions the window around the action. A centered crop may not include the subject.

If the source is enlarged beyond its native detail, image quality may soften or show artifacts. Upscaling algorithms can create plausible detail but cannot guarantee recovery of information never captured. If the crop is too tight, consider an alternate shot, split layout, blurred/extended background, letterboxing, a wider re-shoot or a deliberate graphic explanation. Disclose or avoid any treatment that changes the apparent evidence.

### 2. Prioritize action and meaning, not only faces

Before positioning the crop, identify:
- primary subject (person, object or graphic);
- essential action (hand movement, product mechanism, gesture, text or spatial relation);
- context needed to interpret the action;
- gaze and movement direction;
- headroom and lead room;
- other people or objects that must remain visible;
- caption and interface obstruction risk.

A face detector may find a face but cannot decide which hand, product feature, subtitle or second participant is narratively essential. Human review remains necessary.

### 3. Select a reframing method

| Method | Appropriate when | Advantages | Risks / checks |
|---|---|---|---|
| Static crop | Subject remains in one useful region | Stable, simple, low distraction | May exclude later movement |
| Manual keyframed pan-and-scan | Subject moves predictably or emphasis changes | Editorial control | Jerky motion, late correction, excessive movement |
| Automated tracking | A supported tool follows a clear subject | Can speed repetitive positioning | Drift, occlusion, wrong subject, version/tool limitations |
| Cut to alternate angle | Another shot preserves the action | Natural editorial solution | Continuity and timing must match |
| Vertical split / stacked layout | Two regions are simultaneously essential | Preserves both contexts | Small images, visual competition, accessibility |
| Background extension / blurred fill | Full source composition should remain visible | Avoids aggressive crop | Decorative fill can distract; disclose generative extension where relevant |
| Letterbox / pillarbox | Original composition must remain intact | Honest preservation | Smaller displayed picture |
| Re-shoot / request vertical source | Crop cannot preserve required information | Best source quality | Requires production time and permission |

### 4. Keyframe motion should be intentional

A basic pan-and-scan uses position and possibly scale keyframes. Place a start keyframe, a keyframe before the subject reaches the edge, and an end keyframe. Preview the entire interval, not just the keyframe locations. Linear interpolation moves at a constant parameter rate; eased interpolation accelerates/decelerates. The visual result depends on source motion and crop movement together.

Avoid:
- keyframes placed only after the subject is already clipped;
- sudden position jumps at cuts;
- overshooting the subject and correcting repeatedly;
- tracking jitter that attracts more attention than the subject;
- unnecessary scale changes that reduce detail;
- automated tracking without inspecting occlusions and shot boundaries.

### 5. Captions and subtitles have different jobs

Use the brief to decide whether the deliverable needs:
- verbatim or edited captions;
- SDH sound and speaker information;
- translated subtitles;
- a transcript;
- open captions, sidecar text, or both.

A captioning specification should state the convention, language, speaker-label policy, treatment of non-speech sounds, punctuation policy, reading-speed target and delivery format. Do not silently rewrite a speaker's meaning to improve style. If a transcript is edited for readability, preserve intent and mark material omissions when required by the project.

### 6. Transcription requires human correction

Automatic speech recognition can fail on:
- names, brands and technical terms;
- accents, dialects, code-switching and overlapping speech;
- quiet speech, music, noise and reverberation;
- numbers, units, negation and punctuation;
- words that sound alike but change the meaning.

The correction process is: listen to the full context, compare the transcript, replay uncertain spans, verify names against an authorized source, check numbers and negation carefully, and record unresolved uncertainty. Do not guess a name or technical claim.

### 7. Segment captions for comprehension

A cue should represent a meaningful phrase or speaker turn. Break at natural syntactic boundaries; avoid separating an article from its noun, a preposition from its object or a name from its title. Avoid displaying a full paragraph at once. Use enough display time for the intended audience and complexity. Reading-speed calculations are diagnostics, not a universal guarantee.

If using characters per second (CPS), define what is counted (spaces and punctuation included or excluded) and apply the same convention consistently. If using words per minute (WPM), explain the language and counting method. Languages differ in word boundaries, script density and reading behaviour; do not apply an English threshold uncritically to every language.

### 8. Design for legibility and accessibility

- Use a readable typeface and sufficient size at the actual output resolution.
- Maintain strong foreground/background contrast across bright and dark footage.
- Use an outline, shadow or opaque/semi-opaque panel only when it improves contrast without obscuring important content.
- Do not rely on color alone to identify speakers or distinguish meaning.
- Keep line lengths and line breaks natural; avoid covering faces, hands, product details or critical visual evidence.
- Provide speaker identification and meaningful sound descriptions when required by the caption convention.
- Avoid rapid flashing, distracting animated text and unnecessary motion.
- Review at normal speed and on a small screen, not only while zoomed into an editing monitor.
- Provide sidecar captions where supported and appropriate; burned-in captions alone may not satisfy every accessibility or localization need.
- For translated text, use a competent human reviewer familiar with the language and context.

WCAG is a web-content standard, not a universal social-video export specification. Its contrast and media-accessibility principles are useful reference points, but determine which legal, contractual and platform requirements apply to the actual distribution context.

### 9. Safe composition is destination-specific

Platforms may overlay account names, descriptions, buttons, progress indicators, captions, navigation and controls. Their positions can vary by application version, device, placement, user settings, ad format and interface state. Do not hardcode a supposedly universal safe-zone percentage.

Use this method:
1. Identify the exact destination and placement.
2. Consult current official creative specifications or a current preview tool if available.
3. Record the date and source of the guidance.
4. Create a project overlay guide as a temporary review aid.
5. Keep essential text and action away from observed obstruction areas.
6. Preview the actual export in the target app/device where possible.
7. If direct preview is unavailable, record that the check is simulated and not platform-verified.

## Tools, requirements and alternatives

| Need | Options | Tool-independent alternative |
|---|---|---|
| Crop and transform | NLE crop/position/scale controls | Calculate crop bounds on paper or a still-frame image |
| Motion reframing | Position/scale keyframes | Manual edit decision list with time-coded crop positions |
| Subject tracking | Built-in tracker or supported third-party tool | Manual keyframes; always inspect tracking output |
| Transcript | Human transcription, speech-recognition draft | Listen and transcribe manually |
| Caption authoring | NLE caption track, subtitle editor | Plain-text cue table with start/end times |
| Timed-text formats | SRT, WebVTT or destination-supported format | Keep a structured cue table; validate syntax before delivery |
| Contrast check | Accessibility contrast analyzer | Inspect foreground/background values and test actual playback; visual judgment alone is not a numeric measurement |
| Device preview | Actual phone/tablet and destination app | Device-sized preview in player; label as simulated |
| Localization | Qualified human translator/reviewer | Do not publish a translation that cannot be competently checked |

SRT and WebVTT are common text-based timed-text formats, but syntax, styling support, line limits, encoding and accepted upload options vary by platform and player. Confirm the destination's current specification. Do not assume every editor exports valid sidecar files or that every platform accepts every format.

Application menus and tracking/caption features are version-dependent. Use the installed application's official manual for exact steps. No particular NLE, transcription service, font or platform is required for the core exercise.

## Procedure A — Plan and create a vertical reframe

1. **Confirm the destination specification.** Reuse Lesson 01's brief. Record target dimensions, frame rate, codec/container, placement and any current official safe-area guidance.
2. **Preserve the source.** Duplicate the project/sequence or create a new vertical sequence. Keep the original master unchanged.
3. **Inspect the whole source.** Watch at normal speed and mark the subject, essential action, gaze, movement, other participants and contextual objects.
4. **Choose the crop strategy.** Calculate an initial crop window. Decide whether a static crop is sufficient or movement requires keyframes/tracking.
5. **Check resolution.** Estimate enlargement and inspect fine detail. If quality is inadequate, select another method instead of hiding the defect with sharpening.
6. **Set the first crop.** Position the focal subject while keeping essential action and context visible. Do not automatically center every face.
7. **Create movement only when necessary.** Place keyframes before the subject reaches the crop boundary. Preview between and beyond keyframes.
8. **Inspect tracking.** If automated tracking is used, review start, middle, end, occlusion, motion blur and shot transitions. Correct drift manually.
9. **Review adjacent shots.** Check eyeline, screen direction, subject scale, headroom and continuity across cuts.
10. **Resolve impossible compositions.** Use an alternate shot, split layout, letterboxing, background extension or re-shoot when one crop cannot preserve the story.
11. **Add temporary guides.** Use current destination guidance where available. Mark guides as review overlays and remove them from the final export unless the brief explicitly requires them.
12. **Preview at target size.** Confirm subject visibility, image detail, text clearance and no unintended clipping.
13. **Record decisions.** Save source ID, crop method, keyframe ranges, unresolved compromises and reviewer approval.

## Procedure B — Create accurate, accessible captions

1. **Confirm the text convention.** Determine caption/subtitle language, verbatim/editing policy, SDH needs, speaker labels and output format.
2. **Create a transcript draft.** Use a human transcription or authorized speech-recognition draft. Do not upload confidential audio to an external service without approval and privacy review.
3. **Correct against the source.** Listen from before to after each uncertain phrase. Check names, numbers, technical terms, negation, speaker changes and overlapping speech.
4. **Mark uncertainty.** Use an approved uncertainty notation in the working transcript and seek clarification; never invent words.
5. **Segment into cues.** Break at natural phrase boundaries and speaker turns. Preserve punctuation and avoid awkward grammatical splits.
6. **Set timing.** Align cue start/end to actual speech and meaningful sound. Use waveform as a visual aid, not a replacement for listening.
7. **Check reading conditions.** Review cue duration, line length, language, reading speed and complexity at normal playback speed.
8. **Add relevant sound information.** Include meaningful non-speech sounds and speaker labels when required by the selected convention.
9. **Style for legibility.** Apply consistent typography, contrast, position and hierarchy. Avoid faces, hands, products and important motion.
10. **Review muted.** Confirm that text communicates the spoken information and relevant audio cues.
11. **Review audio with captions hidden.** Confirm the picture and sound still make sense and that no visual edit changes the dialogue meaning.
12. **Review full playback.** Watch the entire sequence at normal speed; do not inspect only isolated cues.
13. **Export the required forms.** Produce burned-in text, sidecar timed text or both according to the brief. Validate file encoding and syntax.
14. **Localize with human review.** Verify meaning, names, idioms, line breaks, timing and cultural context.
15. **Save evidence.** Keep transcript, cue file, source version, reviewer notes and final export version together.

## Worked example

**Brief/input:** A fictional maker demonstrates a reusable bottle lid in a 16:9 interview/demo recording. The speaker appears on the left; the lid and hands are on the right. The speaker says: “Press the tab until it clicks. Then lift the ring to release it.” The intended output is a vertical 9:16 clip for a destination whose current interface overlay positions must be checked separately.

**Editorial problem:** A centered vertical crop includes the speaker's face but excludes the hands and locking tab. A crop around the object loses the speaker's explanation.

**Decision process:**
1. Mark the two essential regions: speaker face and tab/hands.
2. Check whether the source has enough detail for a short pan-and-scan between the speaker and the mechanism.
3. If the explanation and demonstration happen at different times, use a cut from speaker to object close-up with a consistent audio bridge.
4. If both must be visible simultaneously, test a vertical stacked/split composition with adequate image size.
5. Avoid a fast crop move that makes the viewer chase the subject.
6. Caption the exact sentence and synchronize the word “clicks” with the audible/visible event only if the source confirms it.
7. Keep the caption away from the hand action and the destination's observed controls.
8. Do not add a “leakproof” or “secure under pressure” claim; the source only demonstrates the tab operation.

**Expected output:** A 9:16 edit, an editable project, corrected transcript/cue file, a crop-decision record and a device-preview/QC report. This is a fictional teaching scenario; no product footage or performance test is supplied.

## Dry run / annotated walkthrough

### A. Crop-window calculation

**Source:** 1920 × 1080 (16:9).  
**Target:** 9:16.  
**Retain full source height:** 1080 pixels.

[
W_c = 1080 	imes rac{9}{16} = 607.5 	ext{ pixels}
]

A practical crop uses integer boundaries, for example approximately 608 × 1080 pixels. This crop retains only about 31.7% of the source width. A center crop begins near the middle of the source and may exclude subjects placed at the sides.

**Dry-run decisions:**
- Inspect source coordinates for the face and hands.
- Choose a crop window that includes the currently essential action.
- If the subject moves beyond the crop window, decide whether to pan, cut or use a split layout.
- Check whether scaling the crop to the target output introduces unacceptable softness.
- Record crop coordinates and the reason for the selected composition.

The calculation is geometric. It does not prove that the crop is aesthetically appropriate or that the source has enough resolution for every delivery profile.

### B. Keyframe trace

| Timeline time | Subject position in source | Crop decision | Verification |
|---|---|---|---|
| 00:00 | Speaker introduces the lid | Crop on speaker | Face and opening context visible |
| 00:02 | Hands move toward the tab | Begin gradual move toward mechanism | No abrupt crop jump |
| 00:03 | Tab is pressed | Hold crop on hands/tab | Contact point remains visible |
| 00:05 | Speaker looks toward object | Keep object visible; use audio bridge | Gaze/action remains understandable |
| 00:07 | Ring is lifted | Hold crop on ring | Release action visible |
| 00:09 | Demonstration ends | Cut to a wider/alternate shot if available | No false continuity |

This is a planning trace, not measured footage or a tested tracker output.

### C. Caption cue dry run

**Source speech:** “Press the tab until it clicks. Then lift the ring to release it.”

| Cue | Draft timing | Text | Review question |
|---|---|---|---|
| 1 | 00:00:00.500–00:00:02.100 | Press the tab until it clicks. | Does “clicks” match the actual word and audible event? |
| 2 | 00:00:02.200–00:00:04.000 | Then lift the ring to release it. | Is the full phrase readable and synchronized? |

These times are illustrative only. In a real edit, derive timings from the source audio and verify by playback. If the phrase is difficult to read, split at a natural boundary or adjust the edit; do not arbitrarily shorten the cue.

### D. Transcript correction trace

| Recognition draft | Source check | Final decision |
|---|---|---|
| “press the tap” | Listen to the phrase; visible mechanism and authorized product terminology say “tab” | Correct to “tab” |
| “until it clicks” | Replay the phrase and inspect source | Retain only if clearly spoken |
| “lift the ring” | Confirm the speaker's words and visible object | Retain if supported |
| “to release it” | Check the full phrase and negation/context | Preserve exact meaning |

The fictional table demonstrates verification logic. It must not be used to override real source audio or a verified glossary.

## Guided practice

**Task:** Reframe and caption a 15–20 second segment from authorized learner-created footage.

1. Choose one landscape clip with a moving subject and one short spoken instruction.
2. Record source dimensions and target delivery dimensions.
3. Calculate an initial vertical crop.
4. Create a static crop and a second version using keyframes or another appropriate layout.
5. Compare subject/action visibility, motion smoothness and image detail.
6. Create a transcript and correct it while listening to the source.
7. Add timed captions and any relevant sound/speaker information.
8. Preview at a phone-sized display and check against current destination guidance if available.
9. Ask a peer to identify the demonstrated action and read the captions at normal speed.
10. Revise and document the changes.

**Success criteria:** The action remains visible, crop motion is intentional, text matches the source, captions can be read at normal speed, no essential information is hidden, and any simulated safe-zone check is clearly labeled.

## Independent assignment

Create a 20–30 second vertical edit from a source that includes:
- at least one moving subject or changing point of visual emphasis;
- a spoken passage of at least two sentences;
- at least one important object/action that could be lost in a careless crop.

**Deliverables:**
1. Original source inventory and rights/consent record.
2. Crop geometry note with source/target dimensions and crop method.
3. Vertical editable project or reproducible edit decision list.
4. A static-crop version and a considered moving/alternate-composition version.
5. Corrected transcript and timed cue file.
6. Final captioned review export.
7. Device-sized preview or an explicitly labeled simulated preview.
8. Caption/reframing QC report with at least three defects considered, even if no defects remain.
9. Version/change log and a 200–300 word reflection explaining trade-offs.

**Constraints:** Use only learner-created or appropriately licensed material. Do not upload confidential audio to unapproved transcription services. Do not fabricate dialogue, speaker identity, sound cues or product claims. Preserve the original master.

## Common errors and recovery

| Symptom | Likely cause | Diagnosis | Recovery |
|---|---|---|---|
| Face visible but demonstration is missing | Crop centered on face rather than action | Review source and identify essential action region | Reframe, cut to detail or use a split layout |
| Subject exits vertical frame | Static crop used for moving subject | Watch the full shot and inspect boundaries | Add earlier keyframes, track with review or choose alternate shot |
| Crop motion feels nervous | Too many keyframes or abrupt interpolation | Preview motion at normal speed | Simplify keyframes, smooth movement or use a cut |
| Image becomes soft | Excessive enlargement or low-resolution source | Compare crop detail with source | Reduce zoom, use another shot or request a higher-resolution source |
| Tracking jumps to wrong object | Occlusion, similar objects or tracker failure | Inspect tracking points across the full shot | Correct manually or abandon tracking |
| Speaker and object cannot both fit | Composition requires two focal regions | Compare crop limits with source layout | Cut between views, split/stack layout or preserve bars |
| Caption words are wrong | ASR misrecognition, accent, noise or terminology | Replay source with surrounding context | Correct manually and verify names/numbers |
| Caption appears before speech | Timing copied from rough transcript or shifted edit | Compare cue boundaries with waveform and listening | Retime and recheck full sequence |
| Caption drift increases over time | Edit duration/frame-rate change or timing offset | Compare early, middle and late cues | Re-time from the final locked picture/audio |
| Text is unreadable over changing footage | Insufficient contrast or unstable background | Preview over brightest/darkest frames | Add a consistent panel/outline and retest |
| Captions cover hands or product | Caption placement not checked against action | Review the shot with text visible | Reposition, use another line placement or adjust crop |
| Translated caption sounds unnatural | Literal translation or missing context | Human bilingual review | Rewrite for meaning and re-time |
| Speaker label is wrong | Unverified identity assumption | Check production records/approved identification | Use neutral label or omit label if permitted |
| Sidecar file rejected | Unsupported syntax, encoding or format | Validate file structure and destination requirements | Correct syntax/encoding or deliver supported alternative |
| UI overlay hides CTA | Safe area based on outdated or generic guide | Preview exact placement/device | Reposition and record current spec/date |
| Muted video is confusing | Essential context only exists in audio | Review visual sequence without sound | Add meaningful visual context without duplicating everything |
| AI-generated background changes evidence | Generative extension alters factual scene | Compare with original and review disclosure/permission | Restore original, use neutral fill or disclose authorized alteration |

## Knowledge check

1. Define aspect ratio and calculate the width of a 9:16 crop that retains the full 1080-pixel height of a 1920 × 1080 source.
2. Why is a center crop not automatically the correct vertical composition?
3. Explain the difference between static crop, pan-and-scan and subject tracking.
4. Name three alternatives when a single vertical crop cannot preserve both the speaker and an essential object.
5. What should be checked between keyframes, not only at keyframe positions?
6. Distinguish captions, subtitles and transcripts.
7. Why is automatic speech recognition not a final authority?
8. Name four transcript details that deserve special verification.
9. What is caption drift, and when can it appear?
10. Why should reading speed be treated as a diagnostic rather than a universal pass/fail number?
11. Give two examples of meaningful non-speech sound information.
12. Why should the editor check captions against both the source audio and the final locked edit?
13. Why is there no universal safe-zone percentage for all social platforms?
14. What is the difference between burned-in and sidecar timed text?
15. What should the editor do if an external transcription service has not been approved for confidential audio?
16. Why can a high-contrast caption panel still be inaccessible or poorly designed?

## Answer key / instructor guidance

1. Aspect ratio is width divided by height. (1080 	imes 9/16 = 607.5) pixels, approximately 608 pixels before choosing integer crop boundaries.
2. It may exclude off-center subjects, hands, products, other participants or contextual evidence.
3. Static crop holds a fixed window; pan-and-scan moves the crop window over time; tracking estimates subject movement to guide the window or effect and can fail.
4. Cut to another angle, use a split/stacked composition, letterbox/pillarbox, extend the background, request a wider/vertical take or use a deliberate alternate shot.
5. Motion smoothness, clipping, subject visibility, overshoot, tracking drift and continuity.
6. Captions represent speech and relevant audio information; subtitles primarily render dialogue, often translated; a transcript is a text record that need not be timed.
7. It can mishear accents, names, numbers, negation, technical terms, overlapping speech and noisy audio.
8. Names, numbers/units, negation, technical terms, speaker identity, overlapping speech and punctuation/context.
9. Caption timing increasingly diverges from speech, sometimes after edits, speed changes, frame-rate conversions or offsets.
10. Languages and viewers differ; cue complexity, line breaks, reading context and the defined counting method matter. Use playback and audience testing.
11. “[alarm sounds]” when relevant; “[glass breaks]”; “[applause]”; “[door slams]”. Include only meaningful cues, not every incidental noise.
12. The source confirms words; the final edit confirms timing and sync after trims, retimes or picture changes.
13. UI overlays and placements vary by platform, app version, device, ad format and user interface state.
14. Burned-in text is part of the image; sidecar timed text is separate and requires compatible playback support.
15. Do not upload it. Use an approved local/human workflow or obtain authorization and review privacy/terms first.
16. Contrast alone does not fix poor timing, small type, excessive text, bad line breaks, covered content, missing speaker/sound information or language inaccuracies.

## Assessment rubric

**Total: 100 points. Suggested pass: 80/100.** Mandatory source integrity, rights/privacy and transcript accuracy gates must pass regardless of total score.

| Criterion | Points | Evidence |
|---|---:|---|
| Crop geometry and source analysis | 10 | Dimension/crop note and source inspection |
| Subject/action visibility | 15 | Full-shot review and crop decisions |
| Motion continuity and reframing method | 15 | Static/moving comparison and keyframe/tracking evidence |
| Transcript and caption accuracy | 15 | Corrected transcript checked against source |
| Cue timing and reading comprehension | 10 | Cue file and normal-speed review |
| Typography, contrast and safe composition | 10 | Phone-sized preview and overlay review |
| Accessibility and localization | 10 | Sound/speaker, language and human-review checks |
| Rights, privacy and professional documentation | 5 | Asset/consent/AI processing records |
| Project organization and QC report | 10 | Editable project, versions, defect log and final checks |

**Mandatory gates:** A fabricated quotation, unapproved disclosure of confidential audio, unauthorized asset, materially incorrect caption or misleading visual reframe blocks release until corrected. If the source cannot support the required composition, the learner must document the limitation and choose a safe alternative.

## Quality-control checklist

### Picture and composition
- [ ] Original source/master remains unchanged.
- [ ] Target dimensions and frame rate match the approved brief.
- [ ] Crop geometry and enlargement are documented.
- [ ] Every shot has an intentional crop; no default crop is blindly reused.
- [ ] Faces, hands, objects and essential action remain visible.
- [ ] Moving subjects stay within frame without distracting motion.
- [ ] Tracking has been inspected through occlusion and shot changes.
- [ ] Adjacent shots preserve screen direction, eyeline and continuity.
- [ ] Important image detail is not unacceptably softened.
- [ ] Temporary safe-zone guides are removed from the final export.

### Captions and audio
- [ ] Transcript is corrected against the source audio.
- [ ] Names, numbers, technical terms and negation are verified.
- [ ] Speaker attribution is authorized and accurate.
- [ ] Meaningful sound information is included when required.
- [ ] Cue boundaries follow natural phrase/speaker boundaries.
- [ ] Start/end times are checked against the final locked edit.
- [ ] Captions remain synchronized at the beginning, middle and end.
- [ ] Reading time, line breaks and language conventions are reviewed.
- [ ] Contrast, size and placement are readable on a small screen.
- [ ] Text does not obscure faces, hands or essential evidence.
- [ ] Translation receives competent human review.

### Rights, privacy and delivery
- [ ] Source, music, font and graphic rights are recorded.
- [ ] Identifiable people have appropriate permission/release.
- [ ] External AI/transcription processing is approved where used.
- [ ] Platform safe-area guidance is current and its date/source recorded.
- [ ] Actual device/platform preview is completed or explicitly labeled simulated.
- [ ] Sidecar syntax/encoding is validated where delivered.
- [ ] Full export playback and file integrity are checked.
- [ ] Project, transcript, cue file, review notes and versions are organized.

## Capstone integration

For the CT-03 three-format campaign capstone, create a vertical master that preserves the story promise from Lesson 02. Record crop decisions for every shot that changes from landscape or square sources. Keep a transcript master separate from each timed-text adaptation; if line breaks or timing differ across formats, record the reason. Provide a vertical captioned export and, where required by the brief, a sidecar subtitle/caption file. Compare vertical, square and landscape versions for subject visibility, caption placement, interface obstructions and reading conditions. A safe-area check must identify the actual platform placement and verification date or state clearly that the preview is simulated.

## Further study and references

- [W3C WAI — Making Audio and Video Media Accessible](https://www.w3.org/WAI/media/av/): captions, transcripts, audio description and accessible media planning.
- [W3C — Web Content Accessibility Guidelines (WCAG) 2.2](https://www.w3.org/TR/WCAG22/): contrast, text presentation and media-related accessibility principles; applicability depends on delivery context.
- [W3C — WebVTT: The Web Video Text Tracks Format](https://www.w3.org/TR/webvtt1/): timed-text format specification; platform support and profile requirements still need verification.
- [Library of Congress — Recommended Formats Statement](https://www.loc.gov/preservation/resources/rfs/): preservation-oriented format considerations, not a social-platform export preset.
- [YouTube Help — Add subtitles and captions](https://support.google.com/youtube/answer/2734796): platform-specific caption workflows; verify current instructions before delivery.
- [YouTube Help — Shorts](https://support.google.com/youtube/answer/10059070): destination-specific format context; interface and requirements can change.
- [Related Lesson 01 — Audience, Platform and Format Design](lesson-01-audience-platform-and-format-design.md).
- [Related Lesson 02 — Hooks, Story Compression and Retention](lesson-02-hooks-story-compression-and-retention.md).
- [Workbook Section 03 — Vertical Reframing and Caption QC](workbook/section-03-vertical-reframing-and-caption-qc.md).

## Version and change notes

- **Revision 2.0 — 2026-11-18:** Replaced the short outline with the shared academic lesson structure. Added crop geometry, reframing decision matrix, keyframe/tracking theory, caption/subtitle/transcript distinctions, transcript verification, cue segmentation, accessibility, destination-specific safe composition, two procedures, worked example, crop/keyframe/caption dry runs, guided and independent practice, troubleshooting, 16 answer-guided checks, 100-point rubric, mandatory release gates, QC and capstone integration.
- Tool instructions remain application-neutral. Exact menus, tracking capabilities, caption styling and export options depend on the installed editor and version.
- Platform overlays and specifications change; verify current official guidance and record the check date. A simulated device preview is not a verified platform upload.
- Practice scenario is fictional and text-only. Learners must supply their own recordings or authorized media; no unlicensed copyrighted clips or audio are included.
- No NLE, tracker, transcription service, mobile device, platform upload or caption validator was executed for this lesson.
