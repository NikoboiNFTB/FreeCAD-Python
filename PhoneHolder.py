import FreeCAD as App   # type: ignore
import Part             # type: ignore

# New document
doc = App.newDocument("PhoneHolderFinalFinal")

# Add the first box
box = doc.addObject("Part::Box", "Block")
box.Length = 73
box.Width = 48
box.Height = 31.5
doc.recompute()

# First cut
main_block = doc.Objects[-1]
cut_box = Part.makeBox(61.5, 48, 15.5, App.Vector(12.5, 0, 8))
cut_shape = main_block.Shape.cut(cut_box)
cut_block = doc.addObject("Part::Feature", "Wall_Cut1")
cut_block.Shape = cut_shape
main_block.ViewObject.Visibility = False
doc.recompute()

# Second cut
main_block = doc.Objects[-1]
cut_box = Part.makeBox(48, 15.5, 8, App.Vector(25, 16.25, 0))
cut_shape = main_block.Shape.cut(cut_box)
cut_block = doc.addObject("Part::Feature", "Wall_Cut2")
cut_block.Shape = cut_shape
main_block.ViewObject.Visibility = False
doc.recompute()



# Create Cylinder
main_block = doc.Objects[-1]

base_point = App.Vector(49, 24, 31.5)
cyl1 = Part.makeCylinder(23, 28, base_point, App.Vector(0, 0, 1))
cyl1_obj = doc.addObject("Part::Feature", "LargeCylinder")
cyl1_obj.Shape = cyl1
doc.recompute()

fused_shape = main_block.Shape.fuse(cyl1)
fused_obj = doc.addObject("Part::Feature", "Block_With_Cylinder")
fused_obj.Shape = fused_shape
main_block.ViewObject.Visibility = False
cyl1_obj.ViewObject.Visibility = False
doc.recompute()

cyl2 = Part.makeCylinder(11, 28, base_point, App.Vector(0, 0, 1))
cyl2_obj = doc.addObject("Part::Feature", "CutCylinder")
cyl2_obj.Shape = cyl2
doc.recompute()

final_shape = fused_obj.Shape.cut(cyl2)
final_obj = doc.addObject("Part::Feature", "FinalPart")
final_obj.Shape = final_shape
fused_obj.ViewObject.Visibility = False
cyl2_obj.ViewObject.Visibility = False
doc.recompute()



# Create a new block to fuse
new_block = Part.makeBox(2, 24, 22, App.Vector(48, 12, 31.5))
new_block_obj = doc.addObject("Part::Feature", "NewBlock")
new_block_obj.Shape = new_block
doc.recompute()

previous_shape = doc.Objects[-2].Shape
fused_shape = previous_shape.fuse(new_block)

fused_obj = doc.addObject("Part::Feature", "FusedBlock")
fused_obj.Shape = fused_shape

doc.Objects[-3].ViewObject.Visibility = False
doc.Objects[-1].ViewObject.Visibility = True
doc.recompute()

new_block = Part.makeBox(24, 2, 22, App.Vector(37, 23, 31.5))
new_block_obj = doc.addObject("Part::Feature", "NewBlock")
new_block_obj.Shape = new_block
doc.recompute()

previous_shape = doc.Objects[-2].Shape
fused_shape = previous_shape.fuse(new_block)

fused_obj = doc.addObject("Part::Feature", "FusedBlock")
fused_obj.Shape = fused_shape

doc.Objects[-3].ViewObject.Visibility = False
doc.Objects[-1].ViewObject.Visibility = True
doc.recompute()



# Charger Holder
new_block = Part.makeBox(25, 15.5, 25, App.Vector(0, 16.25, -25))
new_block_obj = doc.addObject("Part::Feature", "NewBlock")
new_block_obj.Shape = new_block
doc.recompute()

previous_shape = doc.Objects[-2].Shape
fused_shape = previous_shape.fuse(new_block)

fused_obj = doc.addObject("Part::Feature", "FusedBlock")
fused_obj.Shape = fused_shape

doc.Objects[-3].ViewObject.Visibility = False
doc.Objects[-1].ViewObject.Visibility = True
doc.recompute()



import FreeCAD as App       # type: ignore
import Part                 # type: ignore
from FreeCAD import Vector  # type: ignore

doc = App.ActiveDocument

# Cut Cable - cylinder cut through the holder to simulate cable slot
cyl_radius = 2
cyl_height = 15.5

# Create cylinder and rotate it to align with Y-axis (green)
cyl = Part.makeCylinder(cyl_radius, cyl_height)
rotation = App.Rotation(Vector(1, 0, 0), 90)  # Rotate 90° around X to point along Y-axis
placement = App.Placement(Vector(12.5, 31.75, -12.5), rotation)
cyl.Placement = placement

# Perform the cut
main_block = doc.Objects[-1]
cut_shape = main_block.Shape.cut(cyl)

cut_obj = doc.addObject("Part::Feature", "Cable_Cut")
cut_obj.Shape = cut_shape

main_block.ViewObject.Visibility = False
doc.recompute()



# Cut
main_block = doc.Objects[-1]
cut_box = Part.makeBox(12.5, 15.5, 4, App.Vector(0, 16.25, -14.5))
cut_shape = main_block.Shape.cut(cut_box)
cut_block = doc.addObject("Part::Feature", "Wall_Cut1")
cut_block.Shape = cut_shape
main_block.ViewObject.Visibility = False
doc.recompute()



# Cut
main_block = doc.Objects[-1]
cut_box = Part.makeBox(2, 15.5, 2, App.Vector(0, 16.25, -10.5))
cut_shape = main_block.Shape.cut(cut_box)
cut_block = doc.addObject("Part::Feature", "Wall_Cut1")
cut_block.Shape = cut_shape
main_block.ViewObject.Visibility = False
doc.recompute()

# Cut
main_block = doc.Objects[-1]
cut_box = Part.makeBox(2, 15.5, 2, App.Vector(0, 16.25, -16.5))
cut_shape = main_block.Shape.cut(cut_box)
cut_block = doc.addObject("Part::Feature", "Wall_Cut1")
cut_block.Shape = cut_shape
main_block.ViewObject.Visibility = False
doc.recompute()

# Cut
main_block = doc.Objects[-1]
cut_box = Part.makeBox(2, 15.5, 2, App.Vector(0, 16.25, -25))
cut_shape = main_block.Shape.cut(cut_box)
cut_block = doc.addObject("Part::Feature", "Wall_Cut1")
cut_block.Shape = cut_shape
main_block.ViewObject.Visibility = False
doc.recompute()



# Add Cylinder from (2, 31.75, -8.5) to (2, 16.25, -8.5) with radius 2mm

from FreeCAD import Vector  # type: ignore
import Part                 # type: ignore

# Compute direction and height
start_point = Vector(2, 16.25, -8.5)
end_point = Vector(2, 31.75, -8.5)
direction = end_point.sub(start_point)
height = direction.Length
axis = direction.normalize()

# Create cylinder with placement along the computed direction
cyl = Part.makeCylinder(2, height)
cyl.Placement = App.Placement(
    start_point,
    App.Rotation(Vector(0, 0, 1), axis)  # This aligns Z with your axis
)

# Fuse it to the previous shape
main_block = doc.Objects[-1]
fused_shape = main_block.Shape.fuse(cyl)

fused_obj = doc.addObject("Part::Feature", "Final_With_Added_Cylinder")
fused_obj.Shape = fused_shape

# Hide previous object
main_block.ViewObject.Visibility = False
doc.recompute()



# Add Cylinder from (2, 31.75, -16.5) to (2, 16.25, -16.5) with radius 2mm

from FreeCAD import Vector  # type: ignore
import Part                 # type: ignore

# Compute direction and height
start_point = Vector(2, 16.25, -16.5)
end_point = Vector(2, 31.75, -16.5)
direction = end_point.sub(start_point)
height = direction.Length
axis = direction.normalize()

# Create cylinder with placement along the computed direction
cyl = Part.makeCylinder(2, height)
cyl.Placement = App.Placement(
    start_point,
    App.Rotation(Vector(0, 0, 1), axis)  # This aligns Z with your axis
)

# Fuse it to the previous shape
main_block = doc.Objects[-1]
fused_shape = main_block.Shape.fuse(cyl)

fused_obj = doc.addObject("Part::Feature", "Final_With_Added_Cylinder")
fused_obj.Shape = fused_shape

# Hide previous object
main_block.ViewObject.Visibility = False
doc.recompute()



# Add Cylinder from (2, 31.75, -23) to (2, 16.25, -23) with radius 2mm

from FreeCAD import Vector  # type: ignore
import Part                 # type: ignore

# Compute direction and height
start_point = Vector(2, 16.25, -23)
end_point = Vector(2, 31.75, -23)
direction = end_point.sub(start_point)
height = direction.Length
axis = direction.normalize()

# Create cylinder with placement along the computed direction
cyl = Part.makeCylinder(2, height)
cyl.Placement = App.Placement(
    start_point,
    App.Rotation(Vector(0, 0, 1), axis)  # This aligns Z with your axis
)

# Fuse it to the previous shape
main_block = doc.Objects[-1]
fused_shape = main_block.Shape.fuse(cyl)

fused_obj = doc.addObject("Part::Feature", "Final_With_Added_Cylinder")
fused_obj.Shape = fused_shape

# Hide previous object
main_block.ViewObject.Visibility = False
doc.recompute()



# Cut
main_block = doc.Objects[-1]
cut_box = Part.makeBox(2, 48, 2, App.Vector(71, 0, 23.5))
cut_shape = main_block.Shape.cut(cut_box)
cut_block = doc.addObject("Part::Feature", "Wall_Cut1")
cut_block.Shape = cut_shape
main_block.ViewObject.Visibility = False
doc.recompute()

# Cut
main_block = doc.Objects[-1]
cut_box = Part.makeBox(2, 48, 2, App.Vector(71, 0, 6))
cut_shape = main_block.Shape.cut(cut_box)
cut_block = doc.addObject("Part::Feature", "Wall_Cut1")
cut_block.Shape = cut_shape
main_block.ViewObject.Visibility = False
doc.recompute()



# Cut
main_block = doc.Objects[-1]
cut_box = Part.makeBox(2, 2, 8, App.Vector(71, 14.25, 0))
cut_shape = main_block.Shape.cut(cut_box)
cut_block = doc.addObject("Part::Feature", "Wall_Cut1")
cut_block.Shape = cut_shape
main_block.ViewObject.Visibility = False
doc.recompute()

# Cut
main_block = doc.Objects[-1]
cut_box = Part.makeBox(2, 2, 8, App.Vector(71, 31.75, 0))
cut_shape = main_block.Shape.cut(cut_box)
cut_block = doc.addObject("Part::Feature", "Wall_Cut1")
cut_block.Shape = cut_shape
main_block.ViewObject.Visibility = False
doc.recompute()

# Cut
main_block = doc.Objects[-1]
cut_box = Part.makeBox(46, 2, 2, App.Vector(25, 14.25, 6))
cut_shape = main_block.Shape.cut(cut_box)
cut_block = doc.addObject("Part::Feature", "Wall_Cut1")
cut_block.Shape = cut_shape
main_block.ViewObject.Visibility = False
doc.recompute()

# Cut
main_block = doc.Objects[-1]
cut_box = Part.makeBox(46, 2, 2, App.Vector(25, 31.75, 6))
cut_shape = main_block.Shape.cut(cut_box)
cut_block = doc.addObject("Part::Feature", "Wall_Cut1")
cut_block.Shape = cut_shape
main_block.ViewObject.Visibility = False
doc.recompute()



# Add Cylinder from (71, 0, 6) to (71, 14.25, 6) with radius 2mm

from FreeCAD import Vector  # type: ignore
import Part                 # type: ignore

# Compute direction and height
start_point = Vector(71, 0, 6)
end_point = Vector(71, 14.25, 6)
direction = end_point.sub(start_point)
height = direction.Length
axis = direction.normalize()

# Create cylinder with placement along the computed direction
cyl = Part.makeCylinder(2, height)
cyl.Placement = App.Placement(
    start_point,
    App.Rotation(Vector(0, 0, 1), axis)  # This aligns Z with your axis
)

# Fuse it to the previous shape
main_block = doc.Objects[-1]
fused_shape = main_block.Shape.fuse(cyl)

fused_obj = doc.addObject("Part::Feature", "Final_With_Added_Cylinder")
fused_obj.Shape = fused_shape

# Hide previous object
main_block.ViewObject.Visibility = False
doc.recompute()

# Add Cylinder from (71, 33.75, 6) to (71, 48, 6) with radius 2mm

from FreeCAD import Vector  # type: ignore
import Part                 # type: ignore

# Compute direction and height
start_point = Vector(71, 33.75, 6)
end_point = Vector(71, 48, 6)
direction = end_point.sub(start_point)
height = direction.Length
axis = direction.normalize()

# Create cylinder with placement along the computed direction
cyl = Part.makeCylinder(2, height)
cyl.Placement = App.Placement(
    start_point,
    App.Rotation(Vector(0, 0, 1), axis)  # This aligns Z with your axis
)

# Fuse it to the previous shape
main_block = doc.Objects[-1]
fused_shape = main_block.Shape.fuse(cyl)

fused_obj = doc.addObject("Part::Feature", "Final_With_Added_Cylinder")
fused_obj.Shape = fused_shape

# Hide previous object
main_block.ViewObject.Visibility = False
doc.recompute()



# Add Cylinder from (71, 14.25, 0) to (71, 14.25, 6) with radius 2mm

from FreeCAD import Vector  # type: ignore
import Part                 # type: ignore

# Compute direction and height
start_point = Vector(71, 14.25, 0)
end_point = Vector(71, 14.25, 6)
direction = end_point.sub(start_point)
height = direction.Length
axis = direction.normalize()

# Create cylinder with placement along the computed direction
cyl = Part.makeCylinder(2, height)
cyl.Placement = App.Placement(
    start_point,
    App.Rotation(Vector(0, 0, 1), axis)  # This aligns Z with your axis
)

# Fuse it to the previous shape
main_block = doc.Objects[-1]
fused_shape = main_block.Shape.fuse(cyl)

fused_obj = doc.addObject("Part::Feature", "Final_With_Added_Cylinder")
fused_obj.Shape = fused_shape

# Hide previous object
main_block.ViewObject.Visibility = False
doc.recompute()



# Add Cylinder from (71, 33.75, 0) to (71, 33.75, 6) with radius 2mm

from FreeCAD import Vector  # type: ignore
import Part                 # type: ignore

# Compute direction and height
start_point = Vector(71, 33.75, 0)
end_point = Vector(71, 33.75, 6)
direction = end_point.sub(start_point)
height = direction.Length
axis = direction.normalize()

# Create cylinder with placement along the computed direction
cyl = Part.makeCylinder(2, height)
cyl.Placement = App.Placement(
    start_point,
    App.Rotation(Vector(0, 0, 1), axis)  # This aligns Z with your axis
)

# Fuse it to the previous shape
main_block = doc.Objects[-1]
fused_shape = main_block.Shape.fuse(cyl)

fused_obj = doc.addObject("Part::Feature", "Final_With_Added_Cylinder")
fused_obj.Shape = fused_shape

# Hide previous object
main_block.ViewObject.Visibility = False
doc.recompute()




# Add Cylinder from (25, 14.25, 6) to (71, 14.25, 6) with radius 2mm

from FreeCAD import Vector  # type: ignore
import Part                 # type: ignore

# Compute direction and height
start_point = Vector(25, 14.25, 6)
end_point = Vector(71, 14.25, 6)
direction = end_point.sub(start_point)
height = direction.Length
axis = direction.normalize()

# Create cylinder with placement along the computed direction
cyl = Part.makeCylinder(2, height)
cyl.Placement = App.Placement(
    start_point,
    App.Rotation(Vector(0, 0, 1), axis)  # This aligns Z with your axis
)

# Fuse it to the previous shape
main_block = doc.Objects[-1]
fused_shape = main_block.Shape.fuse(cyl)

fused_obj = doc.addObject("Part::Feature", "Final_With_Added_Cylinder")
fused_obj.Shape = fused_shape

# Hide previous object
main_block.ViewObject.Visibility = False
doc.recompute()


# Add Cylinder from (25, 33.75, 6) to (71, 33.75, 6) with radius 2mm

from FreeCAD import Vector  # type: ignore
import Part                 # type: ignore

# Compute direction and height
start_point = Vector(25, 33.75, 6)
end_point = Vector(71, 33.75, 6)
direction = end_point.sub(start_point)
height = direction.Length
axis = direction.normalize()

# Create cylinder with placement along the computed direction
cyl = Part.makeCylinder(2, height)
cyl.Placement = App.Placement(
    start_point,
    App.Rotation(Vector(0, 0, 1), axis)  # This aligns Z with your axis
)

# Fuse it to the previous shape
main_block = doc.Objects[-1]
fused_shape = main_block.Shape.fuse(cyl)

fused_obj = doc.addObject("Part::Feature", "Final_With_Added_Cylinder")
fused_obj.Shape = fused_shape

# Hide previous object
main_block.ViewObject.Visibility = False
doc.recompute()



import FreeCAD as App       # type: ignore
import Part                 # type: ignore
from FreeCAD import Vector  # type: ignore

doc = App.ActiveDocument

# Define sphere parameters
radius = 2
positions = [Vector(71, 14.25, 6), Vector(71, 33.75, 6)]

# Create the spheres
spheres = [Part.makeSphere(radius, pos) for pos in positions]

# Fuse the two spheres together
fused_spheres = spheres[0].fuse(spheres[1])

# Get the last object (the one to fuse with)
main_block = doc.Objects[-1]

# Fuse the combined spheres with the main object
final_shape = main_block.Shape.fuse(fused_spheres)

# Create new fused object
final_obj = doc.addObject("Part::Feature", "Final_With_Spheres")
final_obj.Shape = final_shape

# Hide the previous object
main_block.ViewObject.Visibility = False
doc.recompute()



# Add Cylinder from (71, 0, 25.5) to (71, 48, 25.5) with radius 2mm

from FreeCAD import Vector  # type: ignore
import Part                 # type: ignore

# Compute direction and height
start_point = Vector(71, 0, 25.5)
end_point = Vector(71, 48, 25.5)
direction = end_point.sub(start_point)
height = direction.Length
axis = direction.normalize()

# Create cylinder with placement along the computed direction
cyl = Part.makeCylinder(2, height)
cyl.Placement = App.Placement(
    start_point,
    App.Rotation(Vector(0, 0, 1), axis)  # This aligns Z with your axis
)

# Fuse it to the previous shape
main_block = doc.Objects[-1]
fused_shape = main_block.Shape.fuse(cyl)

fused_obj = doc.addObject("Part::Feature", "Final_With_Added_Cylinder")
fused_obj.Shape = fused_shape

# Hide previous object
main_block.ViewObject.Visibility = False
doc.recompute()



# Cut
main_block = doc.Objects[-1]
cut_box = Part.makeBox(2, 48, 2, App.Vector(0, 0, 29.5))
cut_shape = main_block.Shape.cut(cut_box)
cut_block = doc.addObject("Part::Feature", "Wall_Cut1")
cut_block.Shape = cut_shape
main_block.ViewObject.Visibility = False
doc.recompute()



# Add Cylinder from (2, 0, 29.5) to (2, 48, 29.5) with radius 2mm

from FreeCAD import Vector  # type: ignore
import Part                 # type: ignore

# Compute direction and height
start_point = Vector(2, 0, 29.5)
end_point = Vector(2, 48, 29.5)
direction = end_point.sub(start_point)
height = direction.Length
axis = direction.normalize()

# Create cylinder with placement along the computed direction
cyl = Part.makeCylinder(2, height)
cyl.Placement = App.Placement(
    start_point,
    App.Rotation(Vector(0, 0, 1), axis)  # This aligns Z with your axis
)

# Fuse it to the previous shape
main_block = doc.Objects[-1]
fused_shape = main_block.Shape.fuse(cyl)

fused_obj = doc.addObject("Part::Feature", "Final_With_Added_Cylinder")
fused_obj.Shape = fused_shape

# Hide previous object
main_block.ViewObject.Visibility = False
doc.recompute()



# Cut
main_block = doc.Objects[-1]
cut_box = Part.makeBox(2, 16.25, 2, App.Vector(0, 0, 0))
cut_shape = main_block.Shape.cut(cut_box)
cut_block = doc.addObject("Part::Feature", "Wall_Cut1")
cut_block.Shape = cut_shape
main_block.ViewObject.Visibility = False
doc.recompute()

# Cut
main_block = doc.Objects[-1]
cut_box = Part.makeBox(2, 16.25, 2, App.Vector(0, 31.75, 0))
cut_shape = main_block.Shape.cut(cut_box)
cut_block = doc.addObject("Part::Feature", "Wall_Cut1")
cut_block.Shape = cut_shape
main_block.ViewObject.Visibility = False
doc.recompute()



# Add Cylinder from (2, 0, 2) to (2, 16.25, 2) with radius 2mm

from FreeCAD import Vector  # type: ignore
import Part                 # type: ignore

# Compute direction and height
start_point = Vector(2, 0, 2)
end_point = Vector(2, 16.25, 2)
direction = end_point.sub(start_point)
height = direction.Length
axis = direction.normalize()

# Create cylinder with placement along the computed direction
cyl = Part.makeCylinder(2, height)
cyl.Placement = App.Placement(
    start_point,
    App.Rotation(Vector(0, 0, 1), axis)  # This aligns Z with your axis
)

# Fuse it to the previous shape
main_block = doc.Objects[-1]
fused_shape = main_block.Shape.fuse(cyl)

fused_obj = doc.addObject("Part::Feature", "Final_With_Added_Cylinder")
fused_obj.Shape = fused_shape

# Hide previous object
main_block.ViewObject.Visibility = False
doc.recompute()



# Add Cylinder from (2, 31.75, 2) to (2, 48, 2) with radius 2mm

from FreeCAD import Vector  # type: ignore
import Part                 # type: ignore

# Compute direction and height
start_point = Vector(2, 31.75, 2)
end_point = Vector(2, 48, 2)
direction = end_point.sub(start_point)
height = direction.Length
axis = direction.normalize()

# Create cylinder with placement along the computed direction
cyl = Part.makeCylinder(2, height)
cyl.Placement = App.Placement(
    start_point,
    App.Rotation(Vector(0, 0, 1), axis)  # This aligns Z with your axis
)

# Fuse it to the previous shape
main_block = doc.Objects[-1]
fused_shape = main_block.Shape.fuse(cyl)

fused_obj = doc.addObject("Part::Feature", "Final_With_Added_Cylinder")
fused_obj.Shape = fused_shape

# Hide previous object
main_block.ViewObject.Visibility = False
doc.recompute()




# Hide specific objects by name
for name in ["NewBlock", "NewBlock001", "NewBlock002"]:
    obj = doc.getObject(name)
    if obj:
        obj.ViewObject.Visibility = False




