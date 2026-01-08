import FreeCAD as App   # type: ignore
import Part             # type: ignore

doc = App.newDocument("CrossCylinder")

# --- Outer Cylinder ---
outer_radius = 23.00
outer_height = 28.00
outer_cylinder = Part.makeCylinder(outer_radius, outer_height)

# --- Inner Cylinder (to subtract) ---
inner_radius = 11.00
inner_height = 28.00
inner_cylinder = Part.makeCylinder(inner_radius, inner_height)

# Subtract inner cylinder from outer
main_body = outer_cylinder.cut(inner_cylinder)

# --- Cross Blocks ---
# Block 1: Vertical in Y direction
block1 = Part.makeBox(2, 44, 22)  # Width (X), Length (Y), Height (Z)
block1.translate(App.Vector(-1, -22, 0))  # Centered on X=0

# Block 2: Horizontal in X direction
block2 = Part.makeBox(44, 2, 22)  # Width (X), Length (Y), Height (Z)
block2.translate(App.Vector(-22, -1, 0))  # Centered on Y=0

# Union both blocks
cross_blocks = block1.fuse(block2)

# Add cross blocks to main body
final_part = main_body.fuse(cross_blocks)

# --- Show Result in FreeCAD ---
part_obj = doc.addObject("Part::Feature", "CrossCylinder")
part_obj.Shape = final_part

doc.recompute()



