# CT-30 Professional Lab 02 — Archive Integrity, Checksums and Restore Drill

- Level: Master / Professional Practice
- Estimated time: 4–6 hours
- Environment: Archive storage, checksum utility, media/project applications and restore destination
- Lab status: Authored procedure; no enterprise archive platform is certified

## Brief
Create a production archive with a manifest and checksums, store redundant copies, simulate one missing/corrupt asset and restore a usable project from a verified copy.

## Procedure
1. Define archive scope, retention, access and deletion rules.
2. Freeze approved project/version and inventory all dependencies.
3. Create a manifest with paths, sizes, file types, versions and checksums where available.
4. Copy package to two independent storage locations under the approved policy.
5. Recalculate checksums and compare with source manifest.
6. Simulate a missing file in a test copy and identify it through manifest reconciliation.
7. Simulate a corrupt file and verify checksum mismatch detection.
8. Restore from a verified redundant copy to a clean location.
9. Reopen project and relink media; verify fonts/plugins/LUTs/caches as applicable.
10. Play final master and inspect metadata.
11. Record restore duration, missing dependencies and recovery decisions.
12. Update archive manifest and schedule periodic restore tests.

## Validation
All required files reconcile; checksums match; restore opens project; media and output play; access/retention policy is documented.

## Deliverables
Archive package, manifest, checksum report, simulated defect logs, restore report, project-open evidence and retention schedule.

## Assessment — 100 points
Archive scope 10; manifest quality 15; checksum verification 20; redundancy 10; restore procedure 20; dependency recovery 15; governance/handoff 10. Pass 80/100.
