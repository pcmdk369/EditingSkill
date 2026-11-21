# CT-24 Lesson 02 — Prompted Inpainting, Masks and Region Control

- Course: CT-24 — AI-Assisted Image Editing
- Level: Beginner / Intermediate
- Estimated time: 120–180 minutes
- Prerequisites: Previous CT-24 lessons and authorized image assets
- Tools/environment: AI image editor/provider and conventional raster editor; record provider/model/version, OS and terms review date
- Version/review date: Tool-neutral; provider terms change and must be checked before use

## Learning outcomes
Use masks and bounded prompts to modify selected image regions while protecting untouched content and checking edge integration.

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
Inpainting generates content within a selected region using surrounding context and prompt guidance. Mask boundaries influence results. Large masks can alter more of the image than intended. Iterate on copies, compare variants and inspect seams, geometry, text and reflections.

## Tools, requirements and alternatives
Use only services whose terms, data handling and rights are acceptable for the project. Preserve originals and work non-destructively. For sensitive/confidential images, use approved local processing or do not process externally. A conventional raster editor remains necessary for precise corrections and final QA.

## Procedure
1. Duplicate source. 2. Define exact region and purpose. 3. Create tight mask with suitable feather. 4. Write concise prompt describing only required change. 5. Generate multiple drafts if permitted. 6. Compare against source. 7. Inspect edges and nearby details. 8. Keep approved result on separate layer and log changes.

## Worked example
Remove a temporary background object from a personal photo while leaving subject pixels unchanged.

## Dry run
Mask overlaps product label and generated text changes. Restore original label from source or approved asset; do not accept invented text.

## Guided practice
Perform two bounded inpainting edits on learner-created images.

## Independent assignment
Apply the workflow to a second image set with different content. Submit originals, editable project, final exports, provenance and review evidence.

## Common errors and recovery
| Symptom | Likely cause | Diagnosis | Recovery |
|---|---|---|---|
| Submit original, masks, variants, final layers and prompt/change log. | AI image workflow issue | Compare with original, terms and factual reference | Reject or correct and document |

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
