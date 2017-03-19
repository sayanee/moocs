# Create schematic

## Things to do

1. Add components, wires, labels, power, edit components
1. Annotate schematic
1. Perform electrical rules check
1. Generate net list
1. Associate component with footprint
1. Generate PCB layout
1. Check design rules
1. Fill zones
1. Connecting vias
1. Creating Silk Screen

## Editing schematic

### 1. Add components

1. Open schematic editor

    ![](img/symbol-schematic-editor.png)
1. Press `a` to `add component`

    ![](img/find-component.png)
1. Press `w` to add wires for joining components

    ![](img/place-wire.png)
1. Press `l` to add labels

    ![](img/add-labels.png)
1. Press `p` to add power

    ![](img/place-power.png)
1. Press `v` to edit values of components

    ![](img/edit-value.png)

### 2. Annotate

1. Click `annotate` to annotate the schematic
1. Choose the annotation options

    ![](img/annotate-schematic-options.png)

### 3. Perform electrical rules check

1. Click `Perform electrical rules checks`

    ![](img/electrical-rules-check-menu.png)
1. Add options for electrical checks

    ![](img/electrical-checks.png)

### 4. Generate net list

1. Click `generate net list` in the menu

    ![](img/netlist-menu.png)
1. Save net list in the project folder as `*.net`

    ![](img/netlist-dialog.png)

### 5. Associate component with footprint

1. Click `run CvPCB to associate components and footprint`

    ![](img/associate-components-footprint.png)
1. Associate each component with footprint

    ![](img/associate-components-dialog.png)
1. Re-generate the net list
1. Layout PCB

    ![](img/layout-pcb.png)
1. Read netlist in layout PCB

    ![](img/read-netlist.png)

### 6. Generate PCB

1. Generate PCB

    ![](img/read-current-netlist.png)

    ![](img/generated-pcb.png)
1. Select footprint mode

    ![](img/select-footprint-mode.png)
1. Spread out all footprints

    ![](img/spread-footprint.png)
1. Press `m` to move components
1. Press `f` to flip to the backside of the PCB
1. Right click to select bigger grid

    ![](img/select-grid.png)
1. Press `space` to set the `(0,0)` point on the PCB

    ![](img/zero-zero.png)
1. Change to edge cuts layer

    ![](img/edge-cuts.png)
1. Select graphic line tool

    ![](img/graphic-line-tool.png)

### 7. Check design rules

1. Check design rules

    ![](img/design-rules.png)
    ![](img/net-class-editor.png)
    ![](img/global-design-rules.png)
1. Ensure track and via sizes

    ![](img/track-via-sizes.png)

### 8. Add tracks and vias

1. Add track by choosing the upper copper layer

    ![](img/front-copper.png)
1. Choose `Add tracks and vias`

    ![](img/add-tracks-vias.png)

### 9. Fill zones

1. Click `fill zones`

    ![](img/add-fill-zones.png)
1. Click and add **front copper fill**

    ![](img/fcu-fill.png)
1. OR Click and add **back copper fill**

    ![](img/bcu-fill.png)
1. Right click to `Fill or Refill zones`

    ![](img/fill-or-refill-zones.png)


### 10. Connecting via

1. Click `v` to drop a via
1. Double click to finish
1. Hit `b` to redraw

### 11. Creating Silk Screen

1. Choose silk screen layer

    ![](img/silk-screen-layer.png)
1. Choose Text editing

    ![](img/choose-text.png)
1. Add in text manually

    ![](img/add-text-manually.png)
