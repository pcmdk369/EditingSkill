# CT-24 Lesson 04 — Generative Extension, Compositing and Consistency

- Course: CT-24 — AI-Assisted Image Editing
- Level: Advanced
- Estimated time: 120–180 minutes
- Prerequisites: Previous CT-24 lessons and authorized image assets
- Tools/environment: AI image editor/provider and conventional raster editor; record provider/model/version, OS and terms review date
- Version/review date: Tool-neutral; provider terms change and must be checked before use

## Learning outcomes
Extend canvases and composite generated regions while maintaining perspective, lighting, material and visual continuity.

## Key definitions
- **Inpainting:** Generating content inside a selected image region.
- **Outpainting:** Extending image content beyond original boundaries.
- **Generative fill:** Model-assisted creation/replacement of pixels in a region.
- **Upscaling:** Increasing pixel dimensions; AI methods may synthesize detail.
- **Provenance:** Record of source and transformation history.
- **Prompt:** Instruction supplied to a generative model.
- **Human-in-the-loop:** Human review/approval before consequential use.
- **Disclosure:** Clear communication that content was generated or materially altered where required.

## Purpose and theory
Outpainting extends image boundaries and must match camera perspective, light direction, grain, depth and scene geometry. Generative content may create inconsistent objects or impossible structures. Keep generated regions identifiable in layers and verify visual continuity.

## Tools, requirements and alternatives
Use only services whose terms, data handling and rights are acceptable for the project. Preserve originals and work non-destructively. For sensitive/confidential images, use approved local processing or do not process externally. A conventional raster editor remains necessary for precise corrections and final QA.

## Procedure
1. Define new canvas and crop. 2. Preserve original image region. 3. Extend background in small sections. 4. Compare generated geometry/perspective. 5. Match light, shadow and color. 6. Inspect repeating patterns and object continuity. 7. Blend seams on separate layers. 8. Document generated areas and approval.

## Worked example
A landscape image is extended to a wider banner. Background architecture is checked for perspective and repeated windows.

## Dry run
Outpainted arm or product component changes shape. Restore from original or use manual compositing rather than accepting inconsistent anatomy/product form.

## Guided practice
Extend one image to two aspect ratios and compare continuity.

## Independent assignment
Apply the workflow to a second image set with different content. Submit originals, editable project, final exports, provenance and review evidence.

## Common errors and recovery
| Symptom | Likely cause | Diagnosis | Recovery |
|---|---|---|---|
| Submit original, generated layers, composites and consistency notes. | AI image workflow issue | Compare with original, terms and factual reference | Reject or correct and document |

## Knowledge check
1. How does inpainting differ from outpainting?
2. Why is AI upscaling not proof of recovered detail?
3. What should be checked before external upload?
4. Why preserve original and generated layers?
5. What belongs in an AI image provenance record?

## Answer guidance
1. Inpainting changes selected regions; outpainting extends beyond original canvas.
2. Models can synthesize plausible but unsupported detail.
3. Rights, consent, privacy, retention, training and commercial terms.
4. It supports reversibility, review and traceability.
5. Source, tool/model/version, task/prompt, settings, changes, reviewer and approvals.

## Assessment rubric — 20 points
| Criterion | Points | Evidence |
|---|---:|---|
| Task/rights selection | 4 | Brief and risk assessment |
| Masking and image craft | 4 | Layered project |
| Factual/identity accuracy | 4 | Source comparison |
| Provenance and disclosure | 4 | Tool/model/change log |
| QC and handoff | 4 | Exports and manifest |

Pass: 16/20. Unauthorized processing, misleading factual alteration or unapproved likeness use requires remediation.

## Quality-control checklist
- [ ] Source rights and consent verified.
- [ ] Provider terms and data handling reviewed.
- [ ] Original preserved.
- [ ] Generated regions inspected for artifacts/factual errors.
- [ ] Identity/product/text accuracy checked.
- [ ] Provenance and disclosure documented.
- [ ] Final outputs and approvals archived.

## Further study
- [NIST — AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- Review current provider terms and applicable privacy/copyright guidance.
- Selected image editor's official documentation.

## Version and change notes
Tool-neutral. AI service terms and legal treatment vary by provider and jurisdiction. This course is educational, not legal advice.
