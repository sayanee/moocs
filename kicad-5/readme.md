# KiCad 5.0

## Adding new footprint libraries

This allows another user on another computer to access the library within the project specific directory.

1. Open the KiCad project folder outside the KiCad program
1. Create a folder called `library` in the project
1. Copy and paste `*.pretty` folder from another location
1. Go to `Preferences` > `Manage footprint libraries` > `Project specific libraries` tab
1. Choose the `*.pretty` folder from the `library` directory

## [A faster way to update your layout](https://www.youtube.com/watch?v=FO7sArFLOdk)

### Before

1. Edit schematic
1. Annotate schematic
1. Generate Netlist
1. Import Netlist in footprint layout

### After

1. Ensure footprint components are locked down!
1. Edit schematic
1. Go to `Tools` > `Update PCB from Schematic...`
1. Check again to ensure footprint layout is not broken

## ⁉️ [Grid origin, Drill and place offset and layer alignment targets](https://www.youtube.com/watch?v=lWyEiKdQi4k)



1. Footprint layout sidebar > `Set origin point for the grid`
1. Plot GERBER format
1. Check `Use auxiliary axis as origin`

## [Drawing and modifying planes](https://www.youtube.com/watch?v=jEDCzisf0Rk)

1. Check the zone in `Layers`
2. Check grid size as required
3.  Select the first `Arrow` tool
4. Select the zone
5. See the tiny square and circle anchor points
6. Drag the anchor points according to the shape
7. Create a new Anchor Point on the zone linke with  `Right Click` > `Create Corner`

![](images/create-corner.jpg)



## [Copying symbols from one library to another](https://www.youtube.com/watch?v=Dd7KLLg59O0)

1. Go to the Schematic
2. Go to the Symbol Editor with the icon at the top menubar `Create, Delete, Edit Symbols`
3. Select the symbol to copy
4. `Right click` > `Copy symbol`
5. Go to another symbol group to paste the symbol with `Right Click` > `Paste Symbol`
6. Remove the symbol with `Right Click` > `Remove Symbol`

![](images/copy-paste-remove-symbol.jpg)

## [Modern Toolset (Push & Shove Router)](https://www.youtube.com/watch?v=wkL0WoKleYU)

1. Go to the foot print layout
2. Select the `Route Track` symbol
3. Start drawing the track
4. Change route settings with `Right Click`> `Interactive Router Settings` > `Mode` > `Shove`

## [Switching from 2 layer to 4 layer](https://www.youtube.com/watch?v=OBY1GuCmgPY)

Go to `Setup` in the menubar > `Layers Setup` > Section `Preset Layer Groupings` dropdown > Choose `Four layers, parts on front and back`

## [Pad Mask Clearance](https://www.youtube.com/watch?v=qrlE_UGiBuU)

1. **(Global) For all footprints:** Go to footprint layout > `Setup` > `Pad to Mask clearance`
2. **(Component) For specific footprint:** Highlight the component pads > Hit `e` for edit > View `Footprint properties` > `Local settings` section
3. **(Pad) For specific pad:**

## [Flipping your view in PCBnew](https://www.youtube.com/watch?v=OwOlJv5TwrA)

How to vertically flip the board especially for the back layer so that it appears exactly as real life?

Go to `View` > `Flip board view`

## [3D Viewer](https://www.youtube.com/watch?v=lu41QO-K7GQ)

- `z` and `shift + z` to view the board on the Z-axis
- `y` and `shift + y` to view the board on the Y-axis
- `x` and `shift + x` to view the board on the X-axis
- Click `Settings` to turn on and off components and layers in view
- Change Silkscreen color with `Preferences` > `Choose Colors` > `Silkscreen color`

## [Blind and Buried Vias](https://www.youtube.com/watch?v=H8tPb9ekhLw)

1. Go to footprint layout
2. Go to `Setup` > `Design Rules` > `Design Rules Editor` > `Global Design Rules`> Check `Allow blind/buried vias`
3. Open the `3D Viewer` > Settings > Uncheck `Show board body`> View the through, buries and blind vias


## [Custom pad shapes](https://www.youtube.com/watch?v=pSS_IRM5KIY)

1. Open Footprint Editor
1. Select the pad to edit
1. Hit `e` to edit
1. `Pad Properties` popup > `General` tab > Choose `Pad Type` > Choose `Shape` > `Custom (Rect. Anchor)`
1. Select tab `Custom Shape Primitives` > `Add Primitive` > `Polygon` > Edit values

## [Interactive BOM](https://www.youtube.com/watch?v=H9WsmhtoH8E)

Download [plugin](https://github.com/openscopeproject/InteractiveHtmlBom) ✅

## [Importing External 3D Models](https://www.youtube.com/watch?v=M1plXo8oLrQ)

1. Open footprint layout
1. Select the component to edit the new 3D model
1. Hit `e` to edit
1. `Footprint Properties` popup > `3D Settings` Popup > Add the path for the new 3D model

Use [grabcad](https://grabcad.com) to download and search for newer 3D models

## [Rounding PCB Corners](https://www.youtube.com/watch?v=FtdAiXc_dNY)

1. Go to footprint layout
1. Select the Edge Cuts layer
1. Make a rectangular Edge Cuts lines with `Add graphic lines`
1. Select `Add graphc arc` tool
1. Create arcs on the 4 edges counter-clockwise
1. Delete the rectangular edges
1. Rejoin the arcs with straight lines with `Add graphic lines`

## [Minimum Soldermask Thickness](https://www.youtube.com/watch?v=8TZBeHTQNiE)

⁉️

### Measure using a ruler

1. Go to footprint layout
1. Select `Set units to millimetres`
1. Select `Measure distance` or `Cmd + Shift + m`

## [Courtyards and how to use them](https://www.youtube.com/watch?v=ZCwvLosXLpk)

1. Edit footprint for the selected component
1. Create a bounding box in the `F.CrtYd` or `B.CrtYd` courtyard layers
1. Come back to the footprint layout
1. Select `Perform design rules check`
1. Check `Check footprint courtyard overlap` or `Check courtyard missing in footprints`
