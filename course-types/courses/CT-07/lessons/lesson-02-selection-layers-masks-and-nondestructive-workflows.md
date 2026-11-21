# CT-07 Lesson 02 — Selections, Layers, Masks and Non-Destructive Workflows

- Course: CT-07 — Photo & Image Editing
- Level: Beginner / Intermediate
- Estimated time: 120–180 minutes
- Prerequisites: Previous CT-07 lessons and authorized image assets
- Tools/environment: Any capable raster editor or RAW processor; record app/version, OS and color-management setup
- Version/review date: Tool-neutral; output specifications depend on print/web/client destination

## Learning outcomes
Use selections, layers and masks to isolate and edit image regions while retaining reversible control.

## Key definitions
- **Raster image:** Pixel-based image representation.
- **Resolution/dimensions:** Pixel count across width and height; print resolution also relates pixels to physical size.
- **Color profile:** Data describing how color values should be interpreted.
- **Layer:** Independent editable image/content element.
- **Mask:** Non-destructive control over layer visibility.
- **RAW:** Camera capture data requiring interpretation and processing.
- **Histogram:** Graph of tonal value distribution.
- **Provenance:** Record of image origin and transformations.

## Purpose and theory
A selection defines an active region; a layer holds image or graphic content; a mask controls visibility without deleting underlying pixels. Non-destructive editing makes revisions safer and supports professional handoff. Feathering and edge refinement must match subject and output scale.

## Tools, requirements and alternatives
Use a suitable raster editor and, where needed, a RAW processor. Record exact versions and color-profile assumptions. Keep original images, use backups and work non-destructively. Only edit images you own or are authorized to use.

## Procedure
1. Duplicate the base layer. 2. Select the subject using a suitable tool. 3. Inspect edge quality at multiple zoom levels. 4. Refine hair, transparent and high-contrast edges separately. 5. Add a mask rather than erasing pixels. 6. Place corrections on separate layers. 7. Name and group layers by function. 8. Toggle layers to compare before/after and check halos.

## Worked example
A portrait background is darkened using a masked adjustment layer. The subject remains untouched and the mask can be refined later.

## Dry run
A bright halo appears around the subject. Inspect mask edge, feather and contrast; refine locally rather than applying excessive global feather.

## Guided practice
Create a clean subject mask and three separate adjustment layers.

## Independent assignment
Repeat the workflow on a second image set with a different lighting or delivery condition. Submit source inventory, editable project, exports and a short rationale for key decisions.

## Common errors and recovery
| Symptom | Likely cause | Diagnosis | Recovery |
|---|---|---|---|
| Submit layered project, mask screenshots and export. | Workflow issue | Inspect source, settings and target requirements | Correct and retest |

## Knowledge check
1. Why preserve original image files?
2. How do layers and masks support non-destructive editing?
3. What can a histogram tell you, and what can it not tell you?
4. Why do batch presets require individual review?
5. What determines the correct delivery format?

## Answer guidance
1. They preserve source quality and allow recovery/revision.
2. They keep edits reversible and independently adjustable.
3. It shows tonal distribution but does not determine aesthetic correctness.
4. Source conditions and subject matter may vary.
5. Destination requirements, transparency, compression, profile and downstream workflow.

## Assessment rubric — 20 points
| Criterion | Points | Evidence |
|---|---:|---|
| Source integrity and organization | 4 | Original preservation and inventory |
| Technical image quality | 5 | Correct dimensions/profile and clean output |
| Non-destructive workflow | 4 | Layered editable project |
| Visual judgment and accuracy | 4 | Before/after and rationale |
| Rights, metadata and handoff | 3 | Asset log and delivery manifest |

Pass: 16/20. Unauthorized image use or deceptive factual alteration requires remediation.

## Quality-control checklist
- [ ] Original preserved.
- [ ] Project is editable and organized.
- [ ] Color/profile and dimensions match brief.
- [ ] Artifacts and edges inspected at output size.
- [ ] Rights and consent recorded.
- [ ] Metadata/privacy considered.
- [ ] Delivery package verified.

## Further study
- [Adobe — Digital Imaging Fundamentals](https://helpx.adobe.com/photoshop/using/color.html)
- [International Color Consortium](https://www.color.org/)
- Check official documentation for the selected editor and current version.

## Version and change notes
Tool-neutral instruction. Exact color-management and export steps must be verified in the selected application/version.
