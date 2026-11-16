# CT-22 — 3D Modeling, Materials & Rendering Assessment

**Total:** 50 points | **Suggested time:** 45–60 minutes

## Part A — Multiple choice (10 × 2 = 20)

1. A polygon mesh contains: A. Vertices/edges/faces B. Audio samples C. Captions D. LUTs.
2. Topology affects: A. Deformation/shading B. Copyright C. Loudness D. File name.
3. Bevel creates: A. Chamfer/rounded edge B. Audio fade C. UV channel D. Camera movement.
4. UV mapping: A. Maps 3D surface to 2D texture coordinates B. Changes frame rate C. Adds sound D. Creates keyframes.
5. Texel density describes: A. Texture pixel density B. Mesh weight C. Camera focal length D. Sample rate.
6. Metallic/roughness are: A. Material properties B. Audio effects C. File permissions D. Motion curves.
7. Procedural modeling uses: A. Parameters/rules B. Only manual sculpting C. Captions D. Video proxies.
8. Render optimization should start with: A. Measuring bottlenecks B. Randomly lowering quality C. Deleting source D. Changing logo.
9. AI-generated meshes may contain: A. Non-manifold geometry B. Guaranteed clean topology C. License clearance D. Perfect UVs.
10. Interchange delivery should be: A. Reimported/tested B. Assumed correct C. Only screenshot D. Unnamed.

## Part B — Short answer (5 × 3 = 15)

11. Why are quads/edge loops useful?
12. What do UV seams do?
13. Explain the difference between color and data textures.
14. Name three factors affecting render time.
15. What should a 3D asset manifest include?

## Part C — Applied case (15)

16. An exported model has wrong scale, missing textures and flipped normals. Explain a safe diagnostic workflow. (8)
17. A procedural asset is slow to render. How do you optimize without degrading the deliverable blindly? (7)

## Answer key
1 A; 2 A; 3 A; 4 A; 5 A; 6 A; 7 A; 8 A; 9 A; 10 A.
11. They support controlled deformation/subdivision and predictable edge flow. (3)
12. They define where the surface is cut and laid out in 2D. (3)
13. Color textures describe appearance; data textures encode values and should not be color transformed. (3)
14. Geometry, texture memory, shader complexity, lighting, sampling, hardware. (3)
15. Scale/axis, geometry, UVs, textures, materials, licenses, versions and test renders. (3)
16. Check unit/axis export settings, recalculate/inspect normals, package textures, reimport into target app and test again. (8)
17. Profile scene, identify bottleneck, test one change at a time, use instances/LOD/texture optimization, compare quality and retain rollback. (7)

## Performance bands
45–50 exemplary; 40–44 competent; 35–39 developing; below 35 remediation. Interchange and rights issues require correction.
