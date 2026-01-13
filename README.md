# FreeCAD Macros — Project Inspection & Reconstruction

**Date:** 2026-01-13  \
**Author:** shamantao  \
**AI-assisted:** GitHub Copilot (plus optional Gemini 3 Pro during drafting)

This repository contains two practical FreeCAD macros designed to help you:

- **Inspect** an active document and generate a human-readable report (object list, placement, visuals, basic geometry).
- **Serialize** a model into a standalone Python rebuild script, useful for sharing parametric intent or “cleaning” a file by reconstructing it.

## What’s included

### 1) `dashboardQA_Inspect_Project.FCMacro`
Generates a text report next to your `.FCStd` file (or in your home folder if the document is unsaved).

The report includes, for each object:

- Name / Label and `TypeId`
- Placement: position and rotation (axis + angle)
- Visual properties (visibility, shape color, transparency)
- Basic geometry status + bounding box (when a valid `Shape` is available)
- Group/Part hierarchy traversal (children are inspected recursively)

**Typical use cases**

- Quick “project audit” before refactoring
- Debugging visibility/placement issues
- Creating a lightweight artifact to share in issues or reviews

### 2) `dashboardQA_Serialize_To_Macro.FCMacro`
Analyzes the active FreeCAD document and writes a Python script named `rebuild_<doc>.py` that attempts to recreate the project.

Currently focuses on:

- `PartDesign::Body` (with placement + view properties)
- Sketches inside bodies (basic geometry export: lines and circles)
- Basic features inside bodies (Pads and Pockets: profile + length, plus some flags)
- `App::Part` groups with basic primitives (e.g. cylinders) where found

**Notes / limitations**

- Sketch constraints are listed but currently commented out (intended as a starting point).
- Not all geometry types are supported yet (e.g. arcs, splines, external geometry, complex constraints).

## Requirements

- FreeCAD (tested target in the generator header: **FreeCAD 1.0.2+**)
- A currently active document (`App.ActiveDocument`)

## How to use

1. Open your `.FCStd` in FreeCAD.
2. Run the macro:
	- **Inspect:** run `dashboardQA_Inspect_Project.FCMacro`
	- **Serialize:** run `dashboardQA_Serialize_To_Macro.FCMacro`

### Outputs

- Inspection macro writes: `<YourFileName>_inspection.txt` next to the `.FCStd`.
- Serialize macro writes: `rebuild_<DocumentName>.py` next to the `.FCStd`.

## Ideas / next improvements (optional)

- Add support for more sketch geometry: `ArcOfCircle`, ellipses, splines.
- Emit (and validate) sketch constraints rather than commenting them out.
- Rebuild more PartDesign features (fillet, chamfer, revolve, loft, pattern, etc.).
- Add a small GUI panel to select export scope (whole doc vs selection).
- Include a deterministic export mode (stable ordering, stable formatting) for diff-friendly outputs.
- Add sample outputs under a `samples/` folder so people can see what they get.

## License

GPL-3.0 — see `LICENSE`.

## Safety

These macros generate files and may create/close documents during reconstruction. Review generated scripts before running them on important work, and keep backups.
