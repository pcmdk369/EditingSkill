# CT-01 — Advanced: Color Correction, Shot Matching and Look Development

**Course:** Video Editing  
**Pathway stage:** Advanced

## Learning outcomes
Distinguish correction from grading; evaluate exposure and white balance; use waveform, vectorscope and RGB parade; match shots; create a restrained look; manage color pipeline assumptions.

## Prerequisites
Intermediate editing workflow, a sequence with multiple shots and a display suitable for visual review.

## Key definitions
- Color correction: technical adjustment to make footage balanced and consistent.
- Color grading: creative shaping of color and contrast for mood or style.
- White balance: adjustment that makes neutral objects appear neutral under a given light source.
- Waveform: scope displaying signal level across image position.
- RGB parade: separate red, green and blue channel waveform display.
- Vectorscope: scope showing color hue and saturation distribution.
- Color space: defined range and behavior of colors a system can represent.
- Gamma/transfer function: relationship between encoded signal values and displayed brightness.
- LUT: lookup table mapping input color values to output values; it is not automatically a complete color-management solution.
- Shot matching: making shots within a scene feel consistent.

## Why it matters
A stylish grade cannot repair every exposure or color problem. Technical consistency gives the audience a coherent scene and makes creative choices repeatable.

## Theory
Correct in a stable order: confirm interpretation/color management; balance exposure; neutralize unwanted color casts where appropriate; match shots; then create a look. Do not force every scene to be neutral—mixed lighting and intentional color are sometimes part of the story.

Scopes complement visual judgment. A waveform helps inspect luminance distribution; RGB parade helps reveal channel imbalance; vectorscope helps inspect hue and saturation. Scopes do not decide the artistic intent.

LUTs may assume a particular camera log profile, gamut or transform. Applying the wrong LUT can produce clipped highlights, crushed shadows or oversaturation. Know the input and output assumptions.

## Tools and alternatives
NLE color page or grading application; calibrated/reference display where available; scopes; camera metadata and manufacturer transform documentation. For limited systems, use a consistent display and compare shots side by side, noting the limitation.

## Procedure
1. Duplicate the sequence or create a grading version.
2. Identify source color spaces, transfer functions and any camera log/gamut metadata.
3. Confirm the project color-management interpretation before applying transforms.
4. Review each shot with waveform, RGB parade and vectorscope.
5. Correct exposure and contrast while preserving important highlight and shadow detail.
6. Adjust white balance or tint only where it supports the scene's intended lighting.
7. Choose a representative reference shot.
8. Match neighboring shots for exposure, contrast, saturation and skin-tone consistency where relevant.
9. Apply a creative look after matching; keep it reversible and documented.
10. Check transitions between shots, not just isolated still frames.
11. Review on a second display when possible and record monitor limitations.
12. Export a short test and confirm the rendered result matches the timeline reasonably.

## Worked example
Three shots from one interview use different camera angles. First identify the camera profiles and correct input transforms. Match exposure and white balance to the reference angle. Only then apply a subtle warm look to the scene. Compare all angles in sequence and check skin and neutral objects.

## Dry run
Create a split-screen before/after still for three shots. Record observed exposure, color-cast and saturation differences. Make corrections, then view the shots in sequence to detect mismatch that is not obvious in still comparison.

## Guided exercise
Match three clips recorded under similar lighting. Capture scope screenshots before and after and explain one correction per shot.

## Independent assignment
Grade a 60-second scene with at least five shots. Submit a node/layer or adjustment map, source interpretation notes, reference stills, scope captures and a short look rationale.

## Common errors and recovery
- Wrong LUT: verify camera log/gamut input and transform order; remove the LUT if assumptions are unknown.
- Skin becomes oversaturated: reduce saturation selectively and compare to reference.
- Highlights clip: revisit exposure and transform; do not judge only from a compressed preview.
- Shots match as stills but not in motion: review cuts and moving highlights in sequence.
- Different displays disagree: use a known reference display and document limitations; avoid chasing every uncalibrated screen.

## Knowledge check
1. Correction versus grading?
2. What does an RGB parade help reveal?
3. Why must LUT assumptions be known?
4. Why match shots before a creative look?
5. What are two limits of scopes?

## Answer key
1. Correction creates technical balance/consistency; grading shapes creative mood/style.
2. Channel imbalance and relative RGB signal levels.
3. Wrong input assumptions can create severe contrast/color errors.
4. A look should be applied consistently to already balanced material.
5. Scopes do not determine artistic intent and cannot replace visual/contextual judgment.

## Assessment rubric — 30 points
Source interpretation 5; exposure and balance 7; shot matching 8; creative look 4; scope use and documentation 4; export review 2. Pass 24/30.

## Quality-control checklist
- [ ] Source color interpretation documented.
- [ ] No unintended clipped highlights or crushed shadows.
- [ ] Neighboring shots match appropriately.
- [ ] Creative look supports the story.
- [ ] Scopes and visual review both used.
- [ ] Export inspected on a known display.

## Further study
Study camera log profiles, scene-referred/display-referred workflows, HDR/SDR, color management and display calibration.
