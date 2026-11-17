# CT-07 Professional Lab 02 — Color-Managed Batch Delivery and Image-Integrity Audit

- Course: CT-07 — Photo & Image Editing
- Level: Advanced / Expert / Professional
- Estimated time: 4–5 hours
- Environment: RAW processor/raster editor, color-managed display where available, metadata inspector and spreadsheet
- Lab status: Authored procedure; no display calibration or export has been performed in this session

## 1. Scenario
Prepare a six-image series for two destinations: web publication and print proof. The set contains mixed camera sources, different white balances and one image intended for factual editorial use. Produce consistent outputs while preserving the distinction between routine correction and content-altering manipulation.

## 2. Learning objectives
- define a color-management workflow and record assumptions;
- normalize a series without flattening intentional lighting differences;
- prepare destination-specific exports;
- audit image alterations according to use context;
- maintain source, edit and export provenance.

## 3. Inputs and prerequisites
Six authorized RAW/JPEG images, destination specifications, a visual reference, rights/consent records and an approved image-use classification. Preserve originals and work on copies.

## 4. Image-use classification
| Use | Permitted approach | Escalation |
|---|---|---|
| Documentary/news | Basic tonal/color correction and technical cleanup consistent with policy | Any content removal/addition or misleading reconstruction |
| Commercial/product | Approved retouching that does not misrepresent product characteristics | Material changes to size, features, performance or condition |
| Portrait/beauty | Agreed retouching within client/subject expectations | Identity-sensitive or deceptive transformation |
| Creative/composite | Broad transformation if rights and audience context allow | Misleading presentation as an unaltered factual record |

The commissioning organization or applicable editorial standard controls final policy. This table is a learning framework, not a universal legal rule.

## 5. Procedure
1. Inventory sources and record file ID, dimensions, camera metadata and rights status.
2. Confirm destination color spaces, bit depth, file types, physical dimensions and compression requirements.
3. Record display environment and whether it is calibrated; do not claim color-critical accuracy on an unverified display.
4. Select a reference frame and define neutral, exposure and contrast targets.
5. Correct white balance and exposure on working copies; avoid clipping important highlight/shadow detail.
6. Apply local adjustments with layers/masks or equivalent non-destructive tools.
7. Match the series while preserving genuine scene differences.
8. Audit the editorial image for prohibited content removal/addition or misleading reconstruction.
9. Export a web proof with specified profile and dimensions.
10. Export a print proof using the printer/client's supplied profile and requirements; if none is supplied, record the assumption and request confirmation.
11. Reopen every export and inspect metadata, color appearance, edge artifacts, sharpening and compression.
12. Compare project and output manifest; record source-to-output mapping and edit history.

## 6. Color-management concepts
- **Working space:** Color space used during editing.
- **Embedded profile:** Metadata that describes how pixel values should be interpreted.
- **Conversion:** Transforming pixel values from one profile to another to preserve appearance.
- **Assignment:** Changing the profile interpretation without recalculating pixel values; can change appearance.
- **Soft proof:** Preview of how an output condition may reproduce, subject to display accuracy and profile quality.

Never assign a new profile merely to make an image “look right” without understanding the source and destination. Verify export behavior in the chosen application.

## 7. Validation matrix
| Test | Method | Pass condition |
|---|---|---|
| Source preservation | Compare originals/backups | Unchanged |
| Series consistency | Contact sheet and reference comparison | Coherent without forced sameness |
| Profile | Inspect exported metadata | Correct destination profile |
| Dimensions | Metadata inspection | Match web/print specification |
| Image integrity | Compare source and edit history | No prohibited content manipulation |
| Artifacts | Inspect 100% and output size | No distracting halos/banding |
| Reopen test | Open all exported files | Correctly rendered and readable |
| Provenance | Audit manifest | Every output traces to a source |

## 8. Troubleshooting
- Unexpected color shift: inspect embedded profile and conversion settings.
- Washed-out export: verify profile handling and viewer color management.
- Banding: inspect bit depth, gradient processing and compression.
- Inconsistent skin/product color: compare under consistent viewing conditions and source lighting.
- Print mismatch: request printer profile/proofing requirements; do not promise exact reproduction from an uncalibrated display.

## 9. Deliverables
Six-image web set, six-image print proofs, editable projects, source inventory, color-management record, image-use classification, rights log, provenance manifest and QC report.

## 10. Assessment — 100 points
Color-management reasoning 20; batch consistency 15; destination exports 15; image-integrity decisions 20; source/provenance 10; artifact QC 10; handoff 10. Pass 80/100. Misrepresentation of factual editorial imagery or unauthorized asset use is mandatory remediation.

## 11. Completion checklist
- [ ] Source images backed up and inventoried.
- [ ] Destination specifications confirmed.
- [ ] Display/color assumptions documented.
- [ ] Working and output profiles recorded.
- [ ] Series consistency checked.
- [ ] Editorial integrity classification applied.
- [ ] Web and print outputs reopened and inspected.
- [ ] Provenance and QC manifest complete.
