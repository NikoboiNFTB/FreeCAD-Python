import FreeCAD as App   # type: ignore
import Part             # type: ignore

# New document
doc = App.newDocument("CapHolder")

# Add the base box
main_block = doc.addObject("Part::Box", "Base")
main_block.Length = 31.5
main_block.Width = 127.5
main_block.Height = 31.5
doc.recompute()

# First cut
cut_box = Part.makeBox(31.5, 8, 15.5, App.Vector(0, 0, 16))
cut_shape = main_block.Shape.cut(cut_box)
cut1 = doc.addObject("Part::Feature", "Cut1")
cut1.Shape = cut_shape
doc.removeObject(main_block.Name)
doc.recompute()

# Second cut
cut_box = Part.makeBox(31.5, 31.5, 23.5, App.Vector(0, 8, 8))
cut_shape = cut1.Shape.cut(cut_box)
cut2 = doc.addObject("Part::Feature", "Cut2")
cut2.Shape = cut_shape
doc.removeObject(cut1.Name)
doc.recompute()

# Third cut
cut_box = Part.makeBox(31.5, 80, 15.5, App.Vector(0, 47.5, 8))
cut_shape = cut2.Shape.cut(cut_box)
cut3 = doc.addObject("Part::Feature", "Cut3")
cut3.Shape = cut_shape
doc.removeObject(cut2.Name)
doc.recompute()

# Fourth cut
cut_box = Part.makeBox(15.5, 80, 31.5, App.Vector(8, 47.5, 0))
cut_shape = cut3.Shape.cut(cut_box)
cut4 = doc.addObject("Part::Feature", "Cut4")
cut4.Shape = cut_shape
doc.removeObject(cut3.Name)
doc.recompute()

# Fifth cut
cut_box = Part.makeBox(8, 74, 8, App.Vector(23.5, 53.5, 23.5))
cut_shape = cut4.Shape.cut(cut_box)
cut5 = doc.addObject("Part::Feature", "Cut5")
cut5.Shape = cut_shape
doc.removeObject(cut4.Name)
doc.recompute()


# Cut Along 1
cut_box = Part.makeBox(1, 80, 1, App.Vector(7, 47.5, 23.5))
cut_shape = cut5.Shape.cut(cut_box)
cut_along1 = doc.addObject("Part::Feature", "Along1")
cut_along1.Shape = cut_shape
doc.removeObject(cut5.Name)
doc.recompute()

# Cut Along 2
cut_box = Part.makeBox(1, 80, 1, App.Vector(7, 47.5, 7))
cut_shape = cut_along1.Shape.cut(cut_box)
cut_along2 = doc.addObject("Part::Feature", "Along2")
cut_along2.Shape = cut_shape
doc.removeObject(cut_along1.Name)
doc.recompute()

# Cut Along 3
cut_box = Part.makeBox(1, 80, 1, App.Vector(23.5, 47.5, 7))
cut_shape = cut_along2.Shape.cut(cut_box)
cut_along3 = doc.addObject("Part::Feature", "Along3")
cut_along3.Shape = cut_shape
doc.removeObject(cut_along2.Name)
doc.recompute()

# Cut Along 4
cut_box = Part.makeBox(1, 6, 1, App.Vector(23.5, 47.5, 23.5))
cut_shape = cut_along3.Shape.cut(cut_box)
cut_along4 = doc.addObject("Part::Feature", "Along4")
cut_along4.Shape = cut_shape
doc.removeObject(cut_along3.Name)
doc.recompute()


# Cut Across 1
cut_box = Part.makeBox(1, 1, 8, App.Vector(7, 126.5, 23.5))
cut_shape = cut_along4.Shape.cut(cut_box)
cut_across1 = doc.addObject("Part::Feature", "Across1")
cut_across1.Shape = cut_shape
doc.removeObject(cut_along4.Name)
doc.recompute()

# Cut Across 2
cut_box = Part.makeBox(1, 1, 8, App.Vector(7, 126.5, 0))
cut_shape = cut_across1.Shape.cut(cut_box)
cut_across2 = doc.addObject("Part::Feature", "Across2")
cut_across2.Shape = cut_shape
doc.removeObject(cut_across1.Name)
doc.recompute()

# Cut Across 3
cut_box = Part.makeBox(1, 1, 8, App.Vector(23.5, 52.5, 23.5))
cut_shape = cut_across2.Shape.cut(cut_box)
cut_across3 = doc.addObject("Part::Feature", "Across3")
cut_across3.Shape = cut_shape
doc.removeObject(cut_across2.Name)
doc.recompute()

# Cut Across 4
cut_box = Part.makeBox(1, 1, 8, App.Vector(23.5, 126.5, 0))
cut_shape = cut_across3.Shape.cut(cut_box)
cut_across4 = doc.addObject("Part::Feature", "Across4")
cut_across4.Shape = cut_shape
doc.removeObject(cut_across3.Name)
doc.recompute()


# Cut Across 5
cut_box = Part.makeBox(8, 1, 1, App.Vector(0, 126.5, 23.5))
cut_shape = cut_across4.Shape.cut(cut_box)
cut_across5 = doc.addObject("Part::Feature", "Across5")
cut_across5.Shape = cut_shape
doc.removeObject(cut_across4.Name)
doc.recompute()

# Cut Across 6
cut_box = Part.makeBox(8, 1, 1, App.Vector(0, 126.5, 7))
cut_shape = cut_across5.Shape.cut(cut_box)
cut_across6 = doc.addObject("Part::Feature", "Across6")
cut_across6.Shape = cut_shape
doc.removeObject(cut_across5.Name)
doc.recompute()

# Cut Across 7
cut_box = Part.makeBox(8, 1, 1, App.Vector(23.5, 52.5, 23.5))
cut_shape = cut_across6.Shape.cut(cut_box)
cut_across7 = doc.addObject("Part::Feature", "Across7")
cut_across7.Shape = cut_shape
doc.removeObject(cut_across6.Name)
doc.recompute()

# Cut Across 8
cut_box = Part.makeBox(8, 1, 1, App.Vector(23.5, 126.5, 7))
cut_shape = cut_across7.Shape.cut(cut_box)
cut_across8 = doc.addObject("Part::Feature", "Across8")
cut_across8.Shape = cut_shape
doc.removeObject(cut_across7.Name)
doc.recompute()



# Cut Across 9
cut_box = Part.makeBox(31.5, 1, 1, App.Vector(0, 39.5, 30.5))
cut_shape = cut_across8.Shape.cut(cut_box)
cut_across9 = doc.addObject("Part::Feature", "Across8")
cut_across9.Shape = cut_shape
doc.removeObject(cut_across8.Name)
doc.recompute()

# Cut Across 10
cut_box = Part.makeBox(31.5, 1, 1, App.Vector(0, 7, 15))
cut_shape = cut_across9.Shape.cut(cut_box)
cut_across10 = doc.addObject("Part::Feature", "Across9")
cut_across10.Shape = cut_shape
doc.removeObject(cut_across9.Name)
doc.recompute()

# Cut Across 11
cut_box = Part.makeBox(31.5, 1, 1, App.Vector(0, 0, 15))
cut_shape = cut_across10.Shape.cut(cut_box)
cut_across11 = doc.addObject("Part::Feature", "Across10")
cut_across11.Shape = cut_shape
doc.removeObject(cut_across10.Name)
doc.recompute()



def add_cylinder_between_points(p1, p2, radius=1.0, name="Cylinder"):
    import math
    from FreeCAD import Vector  # type: ignore

    # Calculate direction and length
    direction = p2.sub(p1)
    height = direction.Length

    # Default cylinder is aligned along Z-axis; compute rotation
    z_axis = Vector(0, 0, 1)
    axis = z_axis.cross(direction)
    angle = math.degrees(z_axis.getAngle(direction))

    # Create the cylinder
    cyl = Part.makeCylinder(radius, height)
    cyl_vector = App.Vector(0, 0, 0)
    cyl.translate(cyl_vector)

    # Apply rotation and translation
    if axis.Length > 0:  # Avoid rotating if direction is already aligned
        cyl.rotate(Vector(0, 0, 0), axis, angle)

    cyl.translate(p1)

    # Add to document
    obj = doc.addObject("Part::Feature", name)
    obj.Shape = cyl
    doc.recompute()
    return obj


# Cylinder 1
p1 = App.Vector(7, 47.5, 24.5)
p2 = App.Vector(7, 126.5, 24.5)
add_cylinder_between_points(p1, p2, radius=1.0, name="Cyl1")

# Cylinder 2
p1 = App.Vector(7, 47.5, 7)
p2 = App.Vector(7, 126.5, 7)
add_cylinder_between_points(p1, p2, radius=1.0, name="Cyl2")

# Cylinder 3
p1 = App.Vector(24.5, 47.5, 7)
p2 = App.Vector(24.5, 126.5, 7)
add_cylinder_between_points(p1, p2, radius=1.0, name="Cyl3")

# Cylinder 4
p1 = App.Vector(24.5, 47.5, 24.5)
p2 = App.Vector(24.5, 52.5, 24.5)
add_cylinder_between_points(p1, p2, radius=1.0, name="Cyl4")



# Cylinder 5
p1 = App.Vector(0, 126.5, 24.5)
p2 = App.Vector(7, 126.5, 24.5)
add_cylinder_between_points(p1, p2, radius=1.0, name="Cyl5")

# Cylinder 6
p1 = App.Vector(0, 126.5, 7)
p2 = App.Vector(7, 126.5, 7)
add_cylinder_between_points(p1, p2, radius=1.0, name="Cyl6")

# Cylinder 7
p1 = App.Vector(24.5, 126.5, 7)
p2 = App.Vector(31.5, 126.5, 7)
add_cylinder_between_points(p1, p2, radius=1.0, name="Cyl7")

# Cylinder 8
p1 = App.Vector(24.5, 52.5, 24.5)
p2 = App.Vector(31.5, 52.5, 24.5)
add_cylinder_between_points(p1, p2, radius=1.0, name="Cyl8")



# Cylinder 9
p1 = App.Vector(7, 126.5, 24.5)
p2 = App.Vector(7, 126.5, 31.5)
add_cylinder_between_points(p1, p2, radius=1.0, name="Cyl9")

# Cylinder 10
p1 = App.Vector(7, 126.5, 0)
p2 = App.Vector(7, 126.5, 7)
add_cylinder_between_points(p1, p2, radius=1.0, name="Cyl10")

# Cylinder 11
p1 = App.Vector(24.5, 126.5, 0)
p2 = App.Vector(24.5, 126.5, 7)
add_cylinder_between_points(p1, p2, radius=1.0, name="Cyl11")

# Cylinder 12
p1 = App.Vector(24.5, 52.5, 24.5)
p2 = App.Vector(24.5, 52.5, 31.5)
add_cylinder_between_points(p1, p2, radius=1.0, name="Cyl12")



# Cylinder 13
p1 = App.Vector(0, 40.5, 30.5)
p2 = App.Vector(31.5, 40.5, 30.5)
add_cylinder_between_points(p1, p2, radius=1.0, name="Cyl12")

# Cylinder 14
p1 = App.Vector(0, 7, 15)
p2 = App.Vector(31.5, 7, 15)
add_cylinder_between_points(p1, p2, radius=1.0, name="Cyl12")

# Cylinder 15
p1 = App.Vector(0, 1, 15)
p2 = App.Vector(31.5, 1, 15)
add_cylinder_between_points(p1, p2, radius=1.0, name="Cyl12")





def add_sphere_at_point(p, radius=1.0, name="Sphere"):
    from FreeCAD import Vector  # type: ignore

    sphere = Part.makeSphere(radius)
    sphere.translate(p)

    obj = doc.addObject("Part::Feature", name)
    obj.Shape = sphere
    doc.recompute()
    return obj


# Sphere 1
point = App.Vector(7, 126.5, 24.5)
add_sphere_at_point(point, radius=1.0, name="Sphere1")

# Sphere 2
point = App.Vector(7, 126.5, 7)
add_sphere_at_point(point, radius=1.0, name="Sphere2")

# Sphere 3
point = App.Vector(24.5, 126.5, 7)
add_sphere_at_point(point, radius=1.0, name="Sphere3")

# Sphere 4
point = App.Vector(24.5, 52.5, 24.5)
add_sphere_at_point(point, radius=1.0, name="Sphere4")





import Part # type: ignore

# Collect all visible Part::Feature objects with a Shape
objects_to_fuse = [obj for obj in doc.Objects if hasattr(obj, "Shape") and obj.TypeId == "Part::Feature"]

if len(objects_to_fuse) < 2:
    print("Not enough objects to fuse.")
else:
    # Start with the shape of the first object
    fused_shape = objects_to_fuse[0].Shape

    # Fuse it with each subsequent shape
    for obj in objects_to_fuse[1:]:
        fused_shape = fused_shape.fuse(obj.Shape)

    # Add the fused object to the document
    fused_obj = doc.addObject("Part::Feature", "Fused")
    fused_obj.Shape = fused_shape

    # Hide original objects
    for obj in objects_to_fuse:
        obj.ViewObject.Visibility = False

    doc.recompute()
    print("Fusion complete.")



