import FreeCAD as App   # type: ignore
import Part             # type: ignore

# New document
doc = App.newDocument("ChargerHolderFinal")

# Add the first box
box = doc.addObject("Part::Box", "Block")
box.Length = 12
box.Width = 28
box.Height = 12
doc.recompute()

# First cut
main_block = doc.Objects[-1]
cut_box = Part.makeBox(8, 20, 4, App.Vector(4, 4, 0))
cut_shape = main_block.Shape.cut(cut_box)
cut_block = doc.addObject("Part::Feature", "Wall_Cut1")
cut_block.Shape = cut_shape
main_block.ViewObject.Visibility = False
doc.recompute()

# Second cut
main_block = doc.Objects[-1]
cut_box = Part.makeBox(4, 20, 4, App.Vector(4, 4, 4))
cut_shape = main_block.Shape.cut(cut_box)
cut_block = doc.addObject("Part::Feature", "Wall_Cut1")
cut_block.Shape = cut_shape
main_block.ViewObject.Visibility = False
doc.recompute()
