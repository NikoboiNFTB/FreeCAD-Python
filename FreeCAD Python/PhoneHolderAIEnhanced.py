import FreeCAD as App
import Part
from FreeCAD import Vector

doc = App.newDocument("PhoneHolderOptimized")

def fuse_all(base, shapes):
    for s in shapes:
        base = base.fuse(s)
    return base

def cut_all(base, shapes):
    for s in shapes:
        base = base.cut(s)
    return base

# --- Base block and initial cuts ---
main = Part.makeBox(73, 48, 31.5)
cuts = [
    Part.makeBox(61.5, 48, 15.5, Vector(12.5, 0, 8)),
    Part.makeBox(48, 15.5, 8, Vector(25, 16.25, 0)),
]
main = cut_all(main, cuts)

# --- Cylindrical top (main hole + outer shape) ---
base_point = Vector(49, 24, 31.5)
outer_cyl = Part.makeCylinder(23, 28, base_point)
inner_cyl = Part.makeCylinder(11, 28, base_point)
main = main.fuse(outer_cyl).cut(inner_cyl)

# --- Side block fusions ---
fuse_blocks = [
    Part.makeBox(2, 24, 22, Vector(48, 12, 31.5)),
    Part.makeBox(24, 2, 22, Vector(37, 23, 31.5)),
    Part.makeBox(25, 15.5, 25, Vector(0, 16.25, -25)),
]
main = fuse_all(main, fuse_blocks)

# --- Cable hole (rotated cylinder along Y) ---
cable_cyl = Part.makeCylinder(2, 15.5)
rot = App.Rotation(Vector(1, 0, 0), 90)
cable_cyl.Placement = App.Placement(Vector(12.5, 31.75, -12.5), rot)
main = main.cut(cable_cyl)

# --- Cable wall cuts ---
cuts = [
    Part.makeBox(12.5, 15.5, 4, Vector(0, 16.25, -14.5)),
    Part.makeBox(2, 15.5, 2, Vector(0, 16.25, -10.5)),
    Part.makeBox(2, 15.5, 2, Vector(0, 16.25, -16.5)),
    Part.makeBox(2, 15.5, 2, Vector(0, 16.25, -25)),
]
main = cut_all(main, cuts)

# --- Function for connecting cylinders ---
def make_cyl(p1, p2, r):
    d = p2.sub(p1)
    h = d.Length
    if h == 0: return None
    a = d.normalize()
    if abs(a.z - 1) < 1e-6:
        rot = App.Rotation()
    elif abs(a.z + 1) < 1e-6:
        rot = App.Rotation(Vector(1,0,0),180)
    else:
        rot = App.Rotation(Vector(0,0,1), a)
    cyl = Part.makeCylinder(r, h)
    cyl.Placement = App.Placement(p1, rot)
    return cyl

# --- Rounded edges (every cylinder present) ---
edges = [
    (Vector(2, 16.25, -8.5), Vector(2, 31.75, -8.5)),
    (Vector(2, 16.25, -16.5), Vector(2, 31.75, -16.5)),
    (Vector(2, 16.25, -23), Vector(2, 31.75, -23)),
    (Vector(71, 0, 6), Vector(71, 14.25, 6)),
    (Vector(71, 33.75, 6), Vector(71, 48, 6)),
    (Vector(71, 14.25, 0), Vector(71, 14.25, 6)),
    (Vector(71, 33.75, 0), Vector(71, 33.75, 6)),
    (Vector(25, 14.25, 6), Vector(71, 14.25, 6)),
    (Vector(25, 33.75, 6), Vector(71, 33.75, 6)),
    (Vector(71, 0, 25.5), Vector(71, 48, 25.5)),
    (Vector(2, 0, 29.5), Vector(2, 48, 29.5)),
    (Vector(2, 0, 2), Vector(2, 16.25, 2)),
    (Vector(2, 31.75, 2), Vector(2, 48, 2)),
]
main = fuse_all(main, [make_cyl(a, b, 2) for a, b in edges if make_cyl(a, b, 2)])

# --- Spheres ---
spheres = [Part.makeSphere(2, Vector(71, 14.25, 6)), Part.makeSphere(2, Vector(71, 33.75, 6))]
main = fuse_all(main, spheres)

# --- Cuts ---
cuts = [
    Part.makeBox(2, 48, 2, Vector(71, 0, 23.5)),
    Part.makeBox(2, 48, 2, Vector(71, 0, 6)),
    Part.makeBox(2, 2, 8, Vector(71, 14.25, 0)),
    Part.makeBox(2, 2, 8, Vector(71, 31.75, 0)),
    Part.makeBox(46, 2, 2, Vector(25, 14.25, 6)),
    Part.makeBox(46, 2, 2, Vector(25, 31.75, 6)),
    Part.makeBox(2, 48, 2, Vector(0, 0, 29.5)),
    Part.makeBox(2, 16.25, 2, Vector(0, 0, 0)),
    Part.makeBox(2, 16.25, 2, Vector(0, 31.75, 0)),
]
main = cut_all(main, cuts)

# --- Done ---
final_obj = doc.addObject("Part::Feature", "PhoneHolder_Optimized")
final_obj.Shape = main
doc.recompute()
