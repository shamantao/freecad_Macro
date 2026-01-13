# FreeCAD Macros for AI-Assisted Development

This repository contains FreeCAD macros developed with GitHub Copilot to help share and analyze FreeCAD projects using AI assistance.

## Macros

### 1. ExportProjectToPython.FCMacro

Exports your entire FreeCAD project to a Python script that can recreate the project from scratch. This is useful for:
- Creating forks of projects
- Version control of parametric models
- Sharing projects as code
- Learning FreeCAD's Python API
- Collaborative development

**Features:**
- Exports all objects with their properties
- Preserves object hierarchy and relationships
- Generates executable Python code
- Includes placement and transformation data
- Handles multiple object types (Part, PartDesign, Sketcher, etc.)

### 2. GenerateProjectSummary.FCMacro

Generates a comprehensive text summary of your FreeCAD project optimized for AI analysis. The summary includes:
- Complete project structure and hierarchy
- Object types and counts
- Detailed properties for each object
- Sketch geometry and constraints
- Object relationships and dependencies
- Analysis guidelines for AI assistants

**Use this summary to get AI suggestions on:**
- Design corrections and improvements
- Optimization opportunities
- Best practices compliance
- Potential issues and fixes
- Alternative modeling approaches

## Installation

### Method 1: Manual Installation

1. Download the `.FCMacro` files from this repository
2. In FreeCAD, go to `Macro > Macros...` 
3. Click the `User macros location` button to open your macros folder
4. Copy the `.FCMacro` files to this folder
5. Restart FreeCAD or refresh the macro list

### Method 2: Direct Download

1. In FreeCAD, go to `Tools > Addon Manager`
2. Navigate to your macros folder (shown in `Macro > Macros...`)
3. Save the macro files directly there

## Usage

### Using ExportProjectToPython.FCMacro

1. Open your FreeCAD document
2. Go to `Macro > Macros...`
3. Select `ExportProjectToPython.FCMacro`
4. Click `Execute`
5. Choose a location to save the generated `.py` file
6. The macro will export all objects and their properties

**Generated Python file can be executed to recreate the project:**
```bash
python your_project_export.py
```

Or run it within FreeCAD's Python console.

### Using GenerateProjectSummary.FCMacro

1. Open your FreeCAD document
2. Go to `Macro > Macros...`
3. Select `GenerateProjectSummary.FCMacro`
4. Click `Execute`
5. Choose a location to save the generated `.txt` file
6. Share the text file with AI assistants (ChatGPT, Claude, Copilot, etc.)

**Example prompt for AI:**
```
I have a FreeCAD project. Here is a complete summary of the project structure 
and all objects. Please analyze it and suggest improvements, identify potential 
issues, and recommend best practices.

[Paste the generated summary here]
```

## Examples

### Example Output: ExportProjectToPython.FCMacro

The macro generates a Python script like this:

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
FreeCAD Project Export: MyProject
Generated on: 2026-01-13 12:00:00
...
"""

import FreeCAD as App
import Part

# Create new document
doc = App.newDocument('MyProject')

# Creating object: Box (Type: Part::Box)
Box = doc.addObject('Part::Box', 'Box')
Box.Length = 10.0
Box.Width = 10.0
Box.Height = 10.0
...

doc.recompute()
```

### Example Output: GenerateProjectSummary.FCMacro

The macro generates a detailed text summary:

```
================================================================================
FREECAD PROJECT SUMMARY FOR AI ANALYSIS
================================================================================

Generated: 2026-01-13 12:00:00

--------------------------------------------------------------------------------
DOCUMENT INFORMATION
--------------------------------------------------------------------------------
Name: MyProject
Label: MyProject
Object Count: 5

--------------------------------------------------------------------------------
OBJECT TYPE STATISTICS
--------------------------------------------------------------------------------
  Part::Box: 2
  Part::Cylinder: 1
  Sketcher::SketchObject: 2

...
```

## Requirements

- FreeCAD 0.19 or later
- Python 3 (included with FreeCAD)
- PySide (included with FreeCAD)

## Supported Object Types

- Part primitives (Box, Cylinder, Sphere, Cone, Torus)
- PartDesign features (Body, Pad, Pocket, etc.)
- Sketcher objects with geometry and constraints
- Groups and assemblies
- Generic FreeCAD objects

## Limitations

- Complex sketch geometry is simplified in exports
- Some advanced features may need manual adjustment
- Very large projects may generate large files
- Expressions and formulas are partially supported

## Contributing

Contributions are welcome! If you'd like to improve these macros:

1. Fork this repository
2. Make your changes
3. Test with various FreeCAD projects
4. Submit a pull request

## Use Cases

### For Developers
- Generate code examples for FreeCAD API learning
- Create reproducible test cases
- Share parametric designs as code
- Build automated design workflows

### For AI-Assisted Design
- Get expert suggestions on your designs
- Identify optimization opportunities
- Learn best practices from AI analysis
- Troubleshoot complex projects

### For Collaboration
- Share projects without large binary files
- Review changes in version control
- Document design decisions
- Create project templates

## License

GNU General Public License v3.0 (GPL-3.0)

See the [LICENSE](LICENSE) file for details.

## Author

These macros were developed with GitHub Copilot assistance.

## Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Check FreeCAD documentation: https://wiki.freecad.org/
- Visit FreeCAD forum: https://forum.freecad.org/
