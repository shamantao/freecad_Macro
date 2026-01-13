#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
FreeCAD Project Export: SimpleExample
Generated on: 2026-01-13 12:00:00
Original file: /path/to/SimpleExample.FCStd

This script recreates the FreeCAD project programmatically.
"""

import FreeCAD as App
import Part
import PartDesign
import Sketcher

# Create new document
doc = App.newDocument('SimpleExample')

# Document properties
doc.Label = 'SimpleExample'
doc.Comment = '''A simple example project with basic shapes'''

# Create objects

# Creating object: Box (Type: Part::Box)
Box = doc.addObject('Part::Box', 'Box')
Box.Length = 10.0
Box.Width = 10.0
Box.Height = 10.0
Box.Placement = App.Placement(
    App.Vector(0.0, 0.0, 0.0),
    App.Rotation(0.0, 0.0, 0.0, 1.0)
)
Box.ViewObject.Visibility = True

# Creating object: Cylinder (Type: Part::Cylinder)
Cylinder = doc.addObject('Part::Cylinder', 'Cylinder')
Cylinder.Radius = 5.0
Cylinder.Height = 20.0
Cylinder.Placement = App.Placement(
    App.Vector(20.0, 0.0, 0.0),
    App.Rotation(0.0, 0.0, 0.0, 1.0)
)
Cylinder.ViewObject.Visibility = True

# Creating object: Sphere (Type: Part::Sphere)
Sphere = doc.addObject('Part::Sphere', 'Sphere')
Sphere.Radius = 7.5
Sphere.Placement = App.Placement(
    App.Vector(40.0, 0.0, 0.0),
    App.Rotation(0.0, 0.0, 0.0, 1.0)
)
Sphere.ViewObject.Visibility = True

# Recompute document
doc.recompute()

# Save document (optional)
# doc.saveAs('path/to/save/document.FCStd')

print('Project recreated successfully!')
