import FreeCAD as App   # type: ignore
import Part             # type: ignore

# New document
doc = App.newDocument("ChargerHolderFinal")

# Add the first box
box = doc.addObject("Part::Box", "Block")
box.Length = 23
box.Width = 4
box.Height = 8
doc.recompute()

# First cut
main_block = doc.Objects[-1]
cut_box = Part.makeBox(15, 4, 8, App.Vector(4, 0, 4))
cut_shape = main_block.Shape.cut(cut_box)
cut_block = doc.addObject("Part::Feature", "Wall_Cut1")
cut_block.Shape = cut_shape
main_block.ViewObject.Visibility = False
doc.recompute()
