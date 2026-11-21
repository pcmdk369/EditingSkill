# CT-20 Professional Lab 01 — Screen Keying, Tracking and Compositing

- Level: Advanced / Professional
- Estimated time: 5–7 hours
- Environment: Compositing application; record OS/app/version, source color space and alpha convention
- Lab status: Authored procedure; not executed in this session

## Brief
Composite a 5-second green-screen subject into a background plate. Create a clean matte, suppress spill, match perspective and validate temporal stability.

## Prerequisites
Complete CT-20 Lessons 01–05. Use authorized source footage and background plate with matching frame rate/resolution where possible.

## Procedure
1. Inventory plate and background metadata.
2. Confirm color space and alpha interpretation.
3. Build a comp with source, matte, edge and color stages.
4. Create garbage/holdout mattes.
5. Key screen and refine matte density/softness.
6. Clean holes and edge noise.
7. Suppress spill without shifting subject color.
8. Track subject or background if required.
9. Match scale, perspective, light and shadow.
10. Add grain/motion blur consistent with plate.
11. Review full shot on light/dark backgrounds.
12. Render proof and inspect representative frames.
13. Export final and package project/dependencies.

## Expected artifacts
Keyed matte, final composite, tracking data, node graph, source inventory, project package and QC report.

## Validation
| Test | Method | Expected result |
|---|---|---|
| Matte | Alpha view | No major holes/chatter |
| Edge | Light/dark background | No visible fringe |
| Spill | Subject color review | Natural color retained |
| Track | Full shot playback | No drift |
| Integration | Compare perspective/light/grain | Believable composite |
| Export | Frame count/playback | No missing frames |

## Troubleshooting
Uneven screen: multiple keys/masks. Green fringe: refine spill/edge. Track drift: retrack or manual correction. Color mismatch: inspect transforms. Missing frame: reconcile range and rerender.

## Assessment — 100 points
Matte quality 20; edge/spill 15; tracking 15; integration 20; color/alpha pipeline 10; temporal QC 10; rights/handoff 10. Pass 80/100.

## Handoff
Submit comp, matte, tracking data, source plate, dependency manifest, final render and QC report.
