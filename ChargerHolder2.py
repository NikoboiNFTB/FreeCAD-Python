# Measures:
# Holder 32mm * 48mm  >  48mm * 64mm
# Distance to shelf: 26mm  >  42mm
# Cable thiccness: 5mm
# USB-C thiccness: 10mm



import FreeCAD as App   # type: ignore
import Part             # type: ignore



# New document
doc = App.newDocument("ChargerHolderFinal")



# Add the first box

box = doc.addObject("Part::Box", "Block")
box.Length = 48
box.Width = 26
box.Height = 64

doc.recompute()



# Cut Holder

doc = App.getDocument(App.listDocuments().keys()[-1])

main_block = doc.Objects[-1]

cut_box = Part.makeBox(32, 26, 48, App.Vector(8, 0, 8))

cut_shape = main_block.Shape.cut(cut_box)

cut_block = doc.addObject("Part::Feature", "Holder_Cut")
cut_block.Shape = cut_shape

main_block.ViewObject.Visibility = False

doc.recompute()



# Cut Shelf

doc = App.getDocument(App.listDocuments().keys()[-1])

main_block = doc.Objects[-1]

cut_box = Part.makeBox(16, 13, 64, App.Vector(16, 13, 0))

cut_shape = main_block.Shape.cut(cut_box)

cut_block = doc.addObject("Part::Feature", "Shelf_Cut")
cut_block.Shape = cut_shape

main_block.ViewObject.Visibility = False

doc.recompute()



# Add Cable Holder and Fuse

from FreeCAD import Vector # type: ignore

cable_holder = Part.makeBox(16, 13, 16)
cable_holder.translate(Vector(48, 13, 24))

main_block = doc.Objects[-1]
fused_shape = main_block.Shape.fuse(cable_holder)

fused_obj = doc.addObject("Part::Feature", "With_Cable_Holder")
fused_obj.Shape = fused_shape

main_block.ViewObject.Visibility = False
doc.recompute()



# Cut Cable

doc = App.ActiveDocument

main_block = doc.Objects[-1]

cyl_radius = 2.5
cyl_height = 16

cyl = Part.makeCylinder(cyl_radius, cyl_height)

cyl.translate(App.Vector(56, 19.5, 24))

cut_shape = main_block.Shape.cut(cyl)

cut_obj = doc.addObject("Part::Feature", "Cable_Cut")
cut_obj.Shape = cut_shape

main_block.ViewObject.Visibility = False

doc.recompute()



# Cut Shaft

doc = App.getDocument(App.listDocuments().keys()[-1])

main_block = doc.Objects[-1]

cut_box = Part.makeBox(16, 4, 16, App.Vector(48, 17.5, 24))

cut_shape = main_block.Shape.cut(cut_box)

cut_block = doc.addObject("Part::Feature", "Insert_Cut")
cut_block.Shape = cut_shape

main_block.ViewObject.Visibility = False

doc.recompute()



# Cut Corner 1

doc = App.getDocument(App.listDocuments().keys()[-1])

main_block = doc.Objects[-1]

cut_box = Part.makeBox(2, 2, 16, App.Vector(62, 21.5, 24))

cut_shape = main_block.Shape.cut(cut_box)

cut_block = doc.addObject("Part::Feature", "Cut_Corner_1")
cut_block.Shape = cut_shape

main_block.ViewObject.Visibility = False

doc.recompute()



# Cut Corner 2

doc = App.getDocument(App.listDocuments().keys()[-1])

main_block = doc.Objects[-1]

cut_box = Part.makeBox(2, 2, 16, App.Vector(62, 15.5, 24))

cut_shape = main_block.Shape.cut(cut_box)

cut_block = doc.addObject("Part::Feature", "Cut_Corner_2")
cut_block.Shape = cut_shape

main_block.ViewObject.Visibility = False

doc.recompute()



# Cut Corner 3

doc = App.getDocument(App.listDocuments().keys()[-1])

main_block = doc.Objects[-1]

cut_box = Part.makeBox(2, 2, 16, App.Vector(62, 13, 24))

cut_shape = main_block.Shape.cut(cut_box)

cut_block = doc.addObject("Part::Feature", "Cut_Corner_3")
cut_block.Shape = cut_shape

main_block.ViewObject.Visibility = False

doc.recompute()



# Add Cylinder 1 and Fuse

cyl_radius = 2
cyl_height = 16
cyl_position = Vector(62, 23.5, 24)

cylinder = Part.makeCylinder(cyl_radius, cyl_height)
cylinder.translate(cyl_position)

main_block = doc.Objects[-1]
fused_shape = main_block.Shape.fuse(cylinder)

fused_obj = doc.addObject("Part::Feature", "Cylinder_1")
fused_obj.Shape = fused_shape

main_block.ViewObject.Visibility = False
doc.recompute()



# Add Cylinder 2 and Fuse

cyl_radius = 2
cyl_height = 16
cyl_position = Vector(62, 15.5, 24)

cylinder = Part.makeCylinder(cyl_radius, cyl_height)
cylinder.translate(cyl_position)

main_block = doc.Objects[-1]
fused_shape = main_block.Shape.fuse(cylinder)

fused_obj = doc.addObject("Part::Feature", "Cylinder_2")
fused_obj.Shape = fused_shape

main_block.ViewObject.Visibility = False
doc.recompute()



# Add Cylinder 3 and Fuse

cyl_radius = 2
cyl_height = 16
cyl_position = Vector(62, 15, 24)

cylinder = Part.makeCylinder(cyl_radius, cyl_height)
cylinder.translate(cyl_position)

main_block = doc.Objects[-1]
fused_shape = main_block.Shape.fuse(cylinder)

fused_obj = doc.addObject("Part::Feature", "Cylinder_3")
fused_obj.Shape = fused_shape

main_block.ViewObject.Visibility = False
doc.recompute()



