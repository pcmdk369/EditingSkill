# CT-10 Professional Lab 01 — Product Variant Catalog and QC

- Level: Advanced / Professional
- Estimated time: 4–6 hours
- Environment: Raster editor/RAW processor and spreadsheet; record OS/app/version
- Lab status: Authored procedure; not executed in this session

## Brief
Prepare a 12-SKU sample catalog with hero and detail images. Each output must match the correct product variant, preserve product truth and comply with the client's image specification.

## Prerequisites and inputs
Complete CT-10 Lessons 01–05. Use authorized product images, physical/reference samples or approved color references. Obtain current marketplace/client specifications and SKU master data.

## Structure
```text
ct10-catalog-lab/
  source/
  sku-master/
  references/
  project/
  exports/
  rights/
  qc/
  delivery/
```

## Procedure
1. Import SKU master and validate variant identifiers.
2. Inventory all source images and map each to one SKU/variant/view.
3. Record source dimensions, profile and rights.
4. Select a reference product image for each lighting/material group.
5. Remove backgrounds using masks and preserve required transparent details.
6. Correct product color against approved references.
7. Create hero and detail views with consistent crop and scale.
8. Review each product for missing accessories, altered labels or invented features.
9. Apply batch resize/naming to a small test subset.
10. Inspect outputs and correct exceptions manually.
11. Compare export inventory to SKU master; detect missing/duplicate files.
12. Package source, exports, manifest and QC report.

## Expected artifacts
12-SKU source map, editable project, hero/detail exports, color/edge notes, rights log, manifest and reconciliation report.

## Validation
| Test | Method | Expected result |
|---|---|---|
| SKU mapping | Compare file manifest to master data | Every output mapped correctly |
| Variant fidelity | Compare with physical/reference product | Correct color/size/finish |
| Edges | Inspect against light/dark backgrounds | No halos/missing details |
| Product truth | Check labels/accessories/features | No invented or omitted facts |
| Export | Inspect dimensions/profile/format | Meets brief |
| Completeness | Compare expected/actual files | No missing or duplicate outputs |

## Troubleshooting
Wrong variant: stop and reconcile source mapping. Color shift: verify reference/profile. Transparent edge: refine mask. Duplicate filename: halt batch and correct naming rule. Missing export: rerun only failed SKU after diagnosis.

## Assessment — 100 points
SKU mapping 20; product accuracy 20; selection/edge quality 15; color/material fidelity 15; batch process 10; QC 10; rights/handoff 10. Pass 80/100; variant accuracy and rights are mandatory gates.

## Handoff
Submit editable project, all exports, SKU manifest, rights log, QC report and exception record.
