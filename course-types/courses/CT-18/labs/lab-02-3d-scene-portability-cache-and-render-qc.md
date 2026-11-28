# CT-18 Professional Lab 02 — 3D Scene Portability, Cache Integrity and Render QC

- Course: CT-18 — 3D Animation
- Level: Expert / Professional
- Estimated time: 5–7 hours
- Environment: 3D application, renderer, cache system and target playback/comp environment
- Lab status: Authored procedure; no renderer or farm compatibility is certified here

## Brief
Prepare a 3D animated shot for transfer to another workstation or render environment. Package assets, textures, fonts, caches, simulation data and render settings so the scene can be reproduced.

## Learning objectives
- identify all external dependencies;
- define scene units, frame range and color/render settings;
- validate caches and deterministic frame output;
- package a portable scene;
- compare render outputs and document hardware/software differences.

## Procedure
1. Save a versioned copy and record application, plugins and renderer versions.
2. Record scene units, frame rate, frame range, resolution, color management and render engine.
3. Inventory models, rigs, textures, fonts, linked libraries, scripts and external references.
4. Identify simulation caches, baked animation, particles, cloth, hair and geometry dependencies.
5. Bake or package required caches using the application's documented method.
6. Use relative paths or a supported asset-collection mechanism.
7. Reopen the package from a clean location or second workstation where available.
8. Render a low-resolution frame range including first, middle and final frames.
9. Compare lighting, textures, motion, simulation and color against the source environment.
10. Render a representative full-quality frame and inspect noise, sampling, motion blur and alpha.
11. Test a small frame chunk for missing assets or cache discontinuity.
12. If distributed rendering is used, record worker environment and frame assignment; verify no overlapping or missing frames.
13. Assemble the image sequence and inspect frame count/order.
14. Encode a review movie and compare timing with the source timeline.
15. Deliver scene, caches, dependencies, render settings, frame sequence, review movie and manifest.

## Validation matrix
| Test | Method | Pass condition |
|---|---|---|
| Dependency audit | Open package on clean location | No missing assets |
| Cache integrity | Compare cached playback/render | No unexplained discontinuity |
| Scene settings | Inspect metadata | Match brief |
| Frame coverage | Compare expected vs actual frames | Complete range |
| Render consistency | Compare test frames | No unintended setting differences |
| Color/alpha | Inspect in target comp/viewer | Correct interpretation |
| Reopen test | Load delivered scene | Reproducible setup |
| Manifest | Audit paths and versions | All dependencies identified |

## Troubleshooting
- Missing textures: repath to packaged asset and retest.
- Simulation changes between machines: verify cache path/version and bake settings.
- Flicker: inspect sampling, temporal effects and cache determinism.
- Different color: compare OCIO/color-management configuration and display transform.
- Missing frames: reconcile render chunks and regenerate only verified gaps.

## Deliverables
Portable scene package, dependency manifest, cache records, render settings, frame sequence, review movie, test-frame comparisons and QC report.

## Assessment — 100 points
Dependency completeness 20; cache integrity 15; scene settings 15; render consistency 20; frame sequence 10; color/alpha 10; handoff/reproducibility 10. Pass 80/100. Missing critical dependencies or unverified frame ranges require remediation.

## Completion checklist
- [ ] Software/plugin versions recorded.
- [ ] All assets and caches inventoried.
- [ ] Package reopened from clean location.
- [ ] Test renders checked across frame range.
- [ ] Render settings and color configuration documented.
- [ ] Sequence coverage and alpha verified.
- [ ] Handoff manifest complete.
