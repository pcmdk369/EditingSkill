# CT-20 Professional Lab 02 — Multipass, Alpha and Compositing Conform QC

- Course: CT-20 — Visual Effects & Compositing
- Level: Expert / Professional
- Estimated time: 5–7 hours
- Environment: Compositing application, 3D render passes, image-sequence tools and color-management configuration
- Lab status: Authored procedure; no EXR renderer or application version is tested here

## Brief
Integrate a rendered CG element into live-action footage using separate render passes and alpha. Deliver a comp script/project and final shot with documented color/alpha interpretation.

## Learning objectives
Interpret premultiplied/unpremultiplied alpha, combine passes, match color and grain, validate temporal stability and package a reproducible comp.

## Inputs
Authorized plate, CG beauty and available utility passes (diffuse/specular/shadow/depth or equivalent), camera data, reference frame and output specification. Record frame range, frame rate, resolution, color space and render version.

## Procedure
1. Inventory plate and render passes; verify matching frame ranges and dimensions.
2. Confirm alpha convention, channel names, bit depth and color encoding from render documentation.
3. Inspect a single frame before building the full composite.
4. Verify premultiplication/unpremultiplication at the correct stage; avoid double premultiplication.
5. Reconstruct or adjust the beauty using available passes only where appropriate.
6. Match exposure, white balance, contrast and black levels to the plate.
7. Integrate shadows/reflections and contact cues without inventing unsupported interaction.
8. Match depth of field, motion blur, grain/noise and lens characteristics.
9. Check edges over light, dark and saturated backgrounds.
10. Review the full frame range for flicker, matte chatter, tracking drift and temporal mismatch.
11. Render a low-resolution proof and compare with approved reference.
12. Export using specified codec/container, color space, alpha and naming.
13. Reopen the output and inspect metadata and full playback.
14. Package project, scripts, LUTs, assets, caches and dependency manifest.

## Technical concepts
- Premultiplied alpha: RGB values are multiplied by alpha.
- Straight/unassociated alpha: RGB values are stored independently of alpha.
- Render pass: separate contribution or data channel from a renderer.
- Linear workflow: compositing operations performed in a linear-light representation.
- Conform: preparing a shot/project to match editorial and delivery specifications.

## Validation
| Test | Method | Pass condition |
|---|---|---|
| Frame alignment | Compare all pass metadata | Same range and dimensions |
| Alpha | Composite over multiple backgrounds | No dark/bright fringe |
| Color | Inspect transforms and reference | No double transform |
| Integration | Compare contact/shadow/DOF | Element belongs in plate |
| Temporal | Watch full sequence | No flicker or drift |
| Export | Reopen and inspect | Correct codec/color/alpha |
| Portability | Reopen project package | Dependencies resolved |

## Troubleshooting
- Dark fringe: check premultiplication order and matte edge.
- Washed-out CG: verify linear/display transforms and pass color space.
- Flicker: inspect animated noise, sampling and temporal effects.
- Missing frames: compare sequence numbering and render queue.
- Broken relink: use packaged relative paths and verify from clean location.

## Deliverables
Comp project, final shot, render-pass inventory, alpha/color pipeline notes, frame-range report, QC contact sheet, render settings and package manifest.

## Assessment — 100 points
Pass inventory 10; alpha handling 20; color pipeline 15; integration 15; temporal QC 15; output conformity 10; portability/documentation 15. Pass 80/100.

## Completion checklist
- [ ] Plate and passes inventoried.
- [ ] Alpha convention verified.
- [ ] Color transforms documented.
- [ ] Edges checked over multiple backgrounds.
- [ ] Temporal review complete.
- [ ] Export metadata verified.
- [ ] Project reopens from package.
