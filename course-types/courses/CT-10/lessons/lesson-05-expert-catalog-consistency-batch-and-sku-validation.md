# CT-10 Lesson 05 — Catalog Consistency, Batch Processing and SKU Validation

- Course: CT-10 — Product & E-commerce Image Editing
- Level: Expert
- Estimated time: 120–180 minutes
- Prerequisites: Previous CT-10 lessons and authorized product imagery
- Tools/environment: Raster editor, RAW processor and catalog spreadsheet; record OS/app/version and output specification
- Version/review date: Tool-neutral; verify current marketplace/client requirements

## Learning outcomes
Process product catalogs consistently while validating SKU, variant, dimensions, color and file naming across all outputs.

## Key definitions
- **SKU:** Stock keeping unit identifying a product/variant.
- **Hero image:** Primary image used to represent a product.
- **Variant:** Specific color, size, finish or configuration.
- **Alpha channel:** Transparency information in an image.
- **Contact shadow:** Shadow directly beneath an object grounding it to a surface.
- **Preflight:** Review of assets and output requirements before delivery.
- **Provenance:** Record of asset origin and transformations.

## Purpose and theory
Catalog automation should be driven by a verified SKU-to-source map. A wrong image can create customer dissatisfaction and returns. Batch operations must be tested on a small sample and include exception handling for unusual products, colors and aspect ratios.

## Tools, requirements and alternatives
Use a raster editor with masks/layers, a RAW processor where needed and a structured SKU manifest. Record versions and marketplace/client specifications. Use original or authorized product images; preserve source files and physical product references.

## Procedure
1. Validate SKU/source mapping with client data. 2. Group products by setup and material. 3. Establish master crop and lighting rules. 4. Apply baseline corrections in batches. 5. Review each SKU and variant individually. 6. Route exceptions for manual treatment. 7. Export with deterministic naming. 8. Compare output inventory to input manifest and resolve missing/duplicate files.

## Worked example
A 100-item catalog uses automated naming and baseline resizing. Transparent packaging and metallic variants are manually reviewed.

## Dry run
A batch renames two variants to the same SKU suffix. Stop export, reconcile source data and regenerate names before delivery.

## Guided practice
Process a 12-SKU sample catalog with one manual exception.

## Independent assignment
Apply the same process to a second product family with different materials or variants. Submit editable project, final exports, SKU mapping, rights log and QC evidence.

## Common errors and recovery
| Symptom | Likely cause | Diagnosis | Recovery |
|---|---|---|---|
| Submit SKU map, batch settings, exception log, exports and reconciliation report. | Catalog workflow issue | Inspect physical/reference product, source and manifest | Correct and rerun validation |

## Knowledge check
1. Why is SKU/variant mapping a critical editorial step?
2. What does an alpha channel provide?
3. Why must product color be checked against a reliable reference?
4. What can make a product composite misleading?
5. What should a catalog manifest record?

## Answer guidance
1. It ensures each image represents the correct product and variant.
2. Transparency information.
3. Lighting, profile and displays can alter apparent color.
4. False scale, invented features, wrong reflections or omitted limitations.
5. SKU, variant, view, filename, dimensions, version, rights and approval.

## Assessment rubric — 20 points
| Criterion | Points | Evidence |
|---|---:|---|
| Product brief/SKU accuracy | 5 | Source map and variant check |
| Selection/edge quality | 4 | Masked project |
| Color and material fidelity | 4 | Reference comparison |
| Export and naming | 4 | Manifest and metadata |
| Rights and handoff | 3 | License and QC record |

Pass: 16/20. Wrong product/variant representation or unauthorized use requires correction.

## Quality-control checklist
- [ ] SKU and variant match physical/reference product.
- [ ] Product details and included accessories are accurate.
- [ ] Color/material remain faithful.
- [ ] Background and shadow are realistic.
- [ ] Dimensions and format match destination.
- [ ] File names and manifest reconcile.
- [ ] Rights and final approvals are recorded.

## Further study
- [Adobe — Image editing and color management](https://helpx.adobe.com/photoshop/using/color.html)
- Use current official seller documentation for the target marketplace.
- Confirm client-specific product representation rules.

## Version and change notes
Tool-neutral course. Marketplace image rules change; verify requirements at production time. This course does not authorize deceptive product representation.
