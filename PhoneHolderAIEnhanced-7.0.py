import FreeCAD as App       # type: ignore
import Part                 # type: ignore
from FreeCAD import Vector  # type: ignore

doc = App.newDocument("PhoneHolderAIEnhanced")

# Main block
main_block = Part.makeBox(50, 50, 31)
current_shape = main_block

# Cut 1
cut1 = Part.makeBox(42.25, 50, 15.5, Vector(7.75, 0, 7.75))
current_shape = current_shape.cut(cut1)

# Cut 2
cut2 = Part.makeBox(25, 15.5, 7.75, Vector(25, 17.25, 0))
current_shape = current_shape.cut(cut2)

# Large cylinder and subtract smaller cylinder
large_cyl = Part.makeCylinder(23, 20.25, Vector(25, 25, 31))
small_cyl = Part.makeCylinder(11, 28, Vector(25, 25, 23.25))

current_shape = current_shape.fuse(large_cyl)
current_shape = current_shape.cut(small_cyl)

# Additional blocks
new_blocks = [
    (2, 25, 22, Vector(24, 12.5, 23.25)),
    (25, 2, 22, Vector(12.5, 24, 23.25)),
    (25, 15.5, 12, Vector(0, 17.25, -12)),
]

for length, width, height, pos in new_blocks:
    blk = Part.makeBox(length, width, height, pos)
    current_shape = current_shape.fuse(blk)

# Cable cut
cable_cut = Part.makeCylinder(2, 15.5)
cable_cut.Placement = App.Placement(Vector(19, 32.75, -6), App.Rotation(Vector(1, 0, 0), 90))
current_shape = current_shape.cut(cable_cut)

# Additional Cuts

cut_boxes = [
    # --- Charger Holder ---
    (19, 15.5, 4, Vector(0, 17.25, -8)),        # Charger crevice
    (2, 15.5, 10, Vector(0, 17.25, -12)),       # Charger Insert Guides

    # --- Front Edge Smoothing ---
    (2, 17.25, 2, Vector(0, 0, 0)),             # Charger-side, top
    (2, 17.25, 2, Vector(0, 32.75, 0)),         # Charger-side, bottom
    (2, 50, 2, Vector(0, 0, 29)),               # Phone-side

    # --- Shelf Wall Slide ---
    (2, 50, 19.5, Vector(48, 0, 5.75)),         # Shelf Wall Insert Guides

    # --- Shelf Slide ---
    (2, 19.5, 7.75, Vector(48, 15.25, 0)),      # Shelf Slide Guide

    # --- Transition ---
    (25, 19.5, 2, Vector(25, 15.25, 5.75)),     # Shelf slide clearance (horizontal)

    # --- Bolt and fastener access ---
    (9, 4, 7.75, Vector(41, 32.75, 0)),         # Bolt head access pocket
    (2, 2, 7.75, Vector(39, 32.75, 0)),         # Bolt shaft slot
    (2, 2, 2, Vector(39, 34.75, 5.75)),         # Bolt head clearance cube

    # --- Upper fastener alignment ---
    (2, 2, 7.75, Vector(48, 36.75, 0)),         # Upper bolt shaft slot
    (9, 2, 2, Vector(39, 36.75, 5.75)),         # Upper bolt head clearance
]

for length, width, height, pos in cut_boxes:
    box = Part.makeBox(length, width, height, pos)
    current_shape = current_shape.cut(box)

# Rounding Edges

cyl_positions = [
    # --- Charger Holder ---
    ((2, 17.25, -2), (2, 32.75, -2)),          # Charger Insert Guide
    ((2, 17.25, -10), (2, 32.75, -10)),        # Charger Insert Guide

    # --- Front vertical reinforcement ---
    ((2, 0, 2), (2, 17.25, 2)),                # Front-left vertical support
    ((2, 32.75, 2), (2, 50, 2)),               # Front-right vertical support
    ((2, 0, 29), (2, 50, 29)),                 # Top front reinforcement

    # --- Wall Mounting Threads ---
    ((48, 0, 25.25), (48, 50, 25.25)),         # Wall Insert Guide - Long
    ((48, 0, 5.75), (48, 15.25, 5.75)),        # Wall Insert Guide - Top
    ((48, 38.75, 5.75), (48, 50, 5.75)),       # Wall Insert Guide - Bottom

    # --- Shelf support threads ---
    ((25, 15.25, 5.75), (48, 15.25, 5.75)),    # Shelf horizontal support
    ((25, 34.75, 5.75), (39, 34.75, 5.75)),    # Shelf rear brace

    # --- Vertical fastener risers ---
    ((48, 15.25, 0), (48, 15.25, 5.75)),       # Wall fastener riser (lower)
    ((39, 34.75, 0), (39, 34.75, 5.75)),       # Shelf fastener riser

    # --- Upper fastener bridges ---
    ((39, 34.75, 5.75), (39, 38.75, 5.75)),    # Vertical connector
    ((48, 38.75, 0), (48, 38.75, 5.75)),       # Wall fastener riser (upper)
    ((48, 38.75, 5.75), (39, 38.75, 5.75)),    # Upper horizontal connector
]


for start, end in cyl_positions:
    start_v = Vector(*start)
    end_v = Vector(*end)
    direction = end_v - start_v
    height = direction.Length
    axis = direction.normalize()
    rotation = App.Rotation(Vector(0, 0, 1), direction)
    cyl = Part.makeCylinder(2, height)
    cyl.Placement = App.Placement(start_v, rotation)
    current_shape = current_shape.fuse(cyl)

# Add spheres
sphere_pos = [
    Vector(48, 15.25, 5.75),
    Vector(39, 34.75, 5.75),
    Vector(48, 38.75, 5.75),
]

spheres = [Part.makeSphere(2, pos) for pos in sphere_pos]

for s in spheres:
    current_shape = current_shape.fuse(s)

# Create final object in document
final_obj = doc.addObject("Part::Feature", "Final_Model")
final_obj.Shape = current_shape
doc.recompute()
