# CT-10 Professional Lab 02 — SKU-to-Image Reconciliation and Catalog Release Audit

- Course: CT-10 — Product & E-commerce Image Editing
- Level: Expert / Professional
- Estimated time: 4–5 hours
- Environment: Raster editor, product data sheet, spreadsheet or catalog system, metadata inspector
- Lab status: Authored procedure; no marketplace acceptance or integration test is claimed

## 1. Scenario
A catalog contains multiple products with color/size variants. Images have inconsistent filenames, mixed backgrounds and two incorrect variant photos. Build a controlled reconciliation workflow that prevents the wrong image from being assigned to a sellable SKU.

## 2. Learning objectives
- define a source-of-truth product/variant table;
- reconcile images against SKU, color, size and product attributes;
- validate image count, naming, dimensions and output profile;
- identify edits that misrepresent product appearance;
- create a release gate and correction audit trail.

## 3. Inputs
Use a fictional catalog or authorized client data. Required columns: product ID, SKU, variant ID, color name/code, size, source filename, approved reference, output filename, rights status and approval state. Never infer a product feature from an image alone.

## 4. Reconciliation workflow
1. Freeze the source data sheet and record its version/date.
2. Create a unique row for every sellable SKU/variant.
3. Inventory source images and record filename, dimensions and metadata.
4. Match each image to a SKU using authoritative product records, not filename guesswork alone.
5. Compare visible color/material/details with approved product references.
6. Flag ambiguous images, missing views and conflicting product data.
7. Perform background isolation and retouching on copies; preserve product geometry, labels and included accessories.
8. Apply a documented filename convention based on product ID, variant and view.
9. Export to the supplied marketplace/client specification.
10. Re-import or reopen all outputs and compare them to the SKU table.
11. Create a contact sheet grouped by product and variant.
12. Run a second-person review of every high-risk or ambiguous match.
13. Block any row with unknown SKU, mismatched color, missing rights or pending approval.
14. Generate release manifest with exact source/output mapping and approval status.

## 5. Mandatory integrity checks
- Product dimensions and proportions are not altered to imply a different model.
- Color correction does not shift a variant into another advertised color.
- Labels, ports, buttons, ingredients, accessories and included contents are not fabricated.
- Shadows/reflections do not hide defects or imply a feature not present.
- AI-generated product imagery is checked against physical product references and approved.
- Any image with an unresolved SKU match is excluded from release.

## 6. Validation matrix
| Test | Method | Pass condition |
|---|---|---|
| SKU uniqueness | Check product table | No duplicate or missing key |
| Image mapping | Compare image to approved reference | Correct variant |
| Color/material | Compare under consistent viewing conditions | No misleading mismatch |
| Output spec | Inspect dimensions/profile/format | Matches brief |
| Naming | Compare file path to SKU/view | Exact match |
| Rights | Inspect source/license record | Authorized |
| Completeness | Compare required views per SKU | All required images present |
| Approval | Review release state | No pending row exported as approved |

## 7. Defect classification
- **Critical:** wrong SKU/variant, fabricated product feature, unauthorized image or materially false representation.
- **Major:** missing required view, wrong output dimensions/profile, color mismatch.
- **Minor:** filename inconsistency that does not create SKU ambiguity, small non-material cleanup issue.
- **Observation:** optional composition improvement.

## 8. Deliverables
Product/variant source table, source inventory, image mapping, edited outputs, contact sheet, defect log, approval record, release manifest and archive package.

## 9. Assessment — 100 points
SKU mapping 20; product fidelity 20; batch/export correctness 15; visual quality 10; defect detection 15; rights/provenance 10; release controls/handoff 10. Pass 80/100. Any wrong-SKU image or false product claim is a critical failure.

## 10. Completion checklist
- [ ] Source-of-truth table version recorded.
- [ ] Every image mapped to an authoritative SKU.
- [ ] Variant color/details independently checked.
- [ ] Product truth and rights gates passed.
- [ ] Filenames and output metadata reconciled.
- [ ] Contact sheet reviewed.
- [ ] Critical/major defects closed.
- [ ] Release manifest and archive complete.
