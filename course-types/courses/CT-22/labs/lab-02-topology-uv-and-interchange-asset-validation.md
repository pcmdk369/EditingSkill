# CT-22 Professional Lab 02 — Topology, UV and Interchange Asset Validation

- Course: CT-22 — 3D Modeling, Materials & Rendering
- Level: Expert / Professional
- Estimated time: 5–7 hours
- Environment: 3D modeling application, UV tools, material preview and interchange viewer
- Lab status: Authored procedure; no specific DCC version or downstream engine is certified

## Brief
Create a production-ready hard-surface prop with clean topology, UVs, materials and two interchange exports. Validate that the asset opens correctly in a clean scene and retains scale, orientation, textures and material intent.

## Procedure
1. Record units, axis convention, target polygon/triangle budget and downstream use.
2. Build a blockout and confirm silhouette/scale before detail.
3. Establish clean edge flow and appropriate support loops/bevels.
4. Inspect non-manifold geometry, normals, duplicate vertices and intersecting components.
5. Apply transforms according to the target pipeline; record unapplied transforms if intentional.
6. Create UVs with suitable texel density and minimal unintended stretching.
7. Pack UV islands with padding appropriate to texture resolution and mipmapping.
8. Build materials using documented texture maps and color-space interpretation.
9. Test lighting and render a neutral inspection turntable.
10. Export to two agreed interchange formats, recording version/options.
11. Import into a clean scene or target application; verify units, axes, normals, UVs and textures.
12. Compare material appearance and note shader features that do not translate.
13. Check polygon count, texture memory and file size against brief.
14. Package native source, interchange exports, textures, preview renders and manifest.

## Validation matrix
| Test | Method | Pass condition |
|---|---|---|
| Topology | Mesh inspection | No unintended non-manifold or broken normals |
| Scale/axis | Import into clean scene | Matches documented convention |
| UV | Checker texture | No critical stretching/overlap |
| Texture | Reopen exported asset | Maps resolve and color space documented |
| Material | Preview in target app | Differences documented |
| Geometry budget | Inspect statistics | Within target |
| Portability | Clean import | No missing dependencies |
| Archive | Manifest comparison | All files and versions listed |

## Troubleshooting
- Dark shading: inspect normals, smoothing and topology.
- UV seams: adjust island layout and padding.
- Missing textures: package relative paths and verify import settings.
- Scale mismatch: apply/record units and axis conversion.
- Material changes: document unsupported shader nodes and provide texture-baked fallback if required.

## Deliverables
Native project, two interchange exports, UV layout, texture set, mesh statistics, preview renders, import test report and manifest.

## Assessment — 100 points
Topology 20; UV quality 15; materials 10; scale/axis correctness 15; interchange portability 20; optimization 10; documentation 10. Pass 80/100.

## Completion checklist
- [ ] Units and target budget documented.
- [ ] Topology and normals inspected.
- [ ] UVs and texel density checked.
- [ ] Texture/color-space mapping recorded.
- [ ] Interchange exports reopened in clean scene.
- [ ] Material differences documented.
- [ ] Package and manifest complete.
