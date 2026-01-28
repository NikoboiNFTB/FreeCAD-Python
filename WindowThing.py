import FreeCAD as App   # type: ignore
import Part             # type: ignore



# New document
doc = App.newDocument("FinalProduct")



# Add Block

box = doc.addObject("Part::Box", "Block")
box.Length = 13
box.Width = 20
box.Height = 20

doc.recompute()



# Cut Box

doc = App.getDocument(App.listDocuments().keys()[-1])

main_block = doc.Objects[-1]

cut_box = Part.makeBox(13, 12, 16, App.Vector(0, 8, 4))

cut_shape = main_block.Shape.cut(cut_box)

cut_block = doc.addObject("Part::Feature", "Box_Cut")
cut_block.Shape = cut_shape

main_block.ViewObject.Visibility = False

doc.recompute()



# Cut Wedge

doc = App.getDocument(App.listDocuments().keys()[-1])

main_block = doc.Objects[-1]

p1 = App.Vector(0, 8, 4)
p2 = App.Vector(0, 4, 20)
p3 = App.Vector(0, 8, 20)

triangle_wire = Part.makePolygon([p1, p2, p3, p1])
triangle_face = Part.Face(triangle_wire)

extrusion_length = 13
tri_prism = triangle_face.extrude(App.Vector(extrusion_length, 0, 0))

cut_shape = main_block.Shape.cut(tri_prism)

cut_tri_block = doc.addObject("Part::Feature", "Wedge_Cut")
cut_tri_block.Shape = cut_shape

main_block.ViewObject.Visibility = False

doc.recompute()



# Cut Pad

doc = App.ActiveDocument

main_block = doc.Objects[-1]

cyl_radius = 3.2
cyl_height = 4

cyl = Part.makeCylinder(cyl_radius, cyl_height)

import math
cyl.rotate(App.Vector(0,0,0), App.Vector(1,0,0), 90)

cyl.translate(App.Vector(6.5, 8, 12))

cut_shape = main_block.Shape.cut(cyl)

cut_obj = doc.addObject("Part::Feature", "Pad_Cut")
cut_obj.Shape = cut_shape

main_block.ViewObject.Visibility = False

doc.recompute()



# Cut Screw

doc = App.ActiveDocument

main_block = doc.Objects[-1]

cyl_radius = 1.6
cyl_height = 8

cyl = Part.makeCylinder(cyl_radius, cyl_height)

import math
cyl.rotate(App.Vector(0,0,0), App.Vector(1,0,0), 90)

cyl.translate(App.Vector(6.5, 8, 12))

cut_shape = main_block.Shape.cut(cyl)

cut_obj = doc.addObject("Part::Feature", "Screw_Cut")
cut_obj.Shape = cut_shape

main_block.ViewObject.Visibility = False

doc.recompute()



# Cut Insert

doc = App.getDocument(App.listDocuments().keys()[-1])

main_block = doc.Objects[-1]

cut_box = Part.makeBox(4, 16, 4, App.Vector(4.5, 16, 0))

cut_shape = main_block.Shape.cut(cut_box)

cut_block = doc.addObject("Part::Feature", "Insert_Cut")
cut_block.Shape = cut_shape

main_block.ViewObject.Visibility = False

doc.recompute()



# Cut Cable

doc = App.ActiveDocument

main_block = doc.Objects[-1]

cyl_radius = 2.5
cyl_height = 4

cyl = Part.makeCylinder(cyl_radius, cyl_height)

cyl.translate(App.Vector(6.5, 16, 0))

cut_shape = main_block.Shape.cut(cyl)

cut_obj = doc.addObject("Part::Feature", "Cable_Cut")
cut_obj.Shape = cut_shape

main_block.ViewObject.Visibility = False

doc.recompute()




# Cut Shaft

doc = App.getDocument(App.listDocuments().keys()[-1])

main_block = doc.Objects[-1]

cut_box = Part.makeBox(1, 12, 4, App.Vector(6, 8, 0))

cut_shape = main_block.Shape.cut(cut_box)

cut_block = doc.addObject("Part::Feature", "Shaft_Cut")
cut_block.Shape = cut_shape

main_block.ViewObject.Visibility = False

doc.recompute()



