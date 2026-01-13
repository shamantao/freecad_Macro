# Examples

This directory contains example outputs from the FreeCAD macros.

## Example Project

For demonstration purposes, let's consider a simple FreeCAD project with:
- 1 Box (10x10x10 mm)
- 1 Cylinder (radius 5mm, height 20mm)
- 1 Sphere (radius 7.5mm)

## ExportProjectToPython Output

See `example_export.py` for a sample Python export of a simple project.

## GenerateProjectSummary Output

See `example_summary.txt` for a sample AI-readable summary of the same project.

## How to Test

1. Create a new FreeCAD document
2. Add a few simple objects (Box, Cylinder, Sphere)
3. Run `ExportProjectToPython.FCMacro` - you should get a Python file
4. Run `GenerateProjectSummary.FCMacro` - you should get a text summary
5. Compare your outputs with these examples
