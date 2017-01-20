# Create schematic

## Things to do

1. Add components, wires, labels, power, edit components
- Annotate schematic
- Perform electrical rules check
- Generate net list
- Associate component with footprint
- Generate PCB layout
- Check design rules
- Fill zones
- Connecting vias
- Creating Silk Screen

## Editing schematic

### 1. Add components

1. Open schematic editor

  ![](img/symbol-worksheet-layout-editor.png)
- Press `a` to `add component`

  ![](img/find-component.png)
- Press `w` to add wires for joining components

  ![](img/place-wire.png)
- Press `l` to add labels

  ![](img/add-labels.png)
- Press `p` to add power

  ![](img/place-power.png)
- Press `v` to edit values of components

  ![](img/edit-value.png)

### 2. Annotate

1. Click `annotate` to annotate the schematic
- Choose the annotation options

  ![](img/annotate-schematic-options.png)

### 3. Perform electrical rules check

1. Click `Perform electrical rules checks`

  ![](img/electrical-rules-check-menu.png)
- Add options for electrical checks

  ![](img/electrical-checks.png)

### 4. Generate net list

1. Click `generate net list` in the menu

  ![](img/netlist-menu.png)
- Save net list in the project folder as `*.net`

  ![](img/netlist-dialog.png)

### 5. Associate component with footprint

1. Click `run CvPCB to associate components and footprint`

  ![](img/associate-components-footprint.png)
- Associate each component with footprint

  ![](img/associate-components-dialog.png)
- Re-generate the net list
- Layout PCB

  ![](img/layout-pcb.png)
- Read netlist in layout PCB

  ![](img/read-netlist.png)

### 6. Generate PCB

1. Generate PCB

  ![](img/read-current-netlist.png)

  ![](img/generated-pcb.png)
- Select footprint mode

  ![](img/select-footprint-mode.png)
- Spread out all footprints

  ![](img/spread-footprint.png)
- Press `m` to move components
- Press `f` to flip to the backside of the PCB
- Right click to select bigger grid

  ![](img/select-grid.png)
- Press `space` to set the `(0,0)` point on the PCB

  ![](img/zero-zero.png)
- Change to edge cuts layer

  ![](img/edge-cuts.png)
- Select graphic line tool

  ![](img/graphic-line-tool.png)

### 7. Check design rules

1. Check design rules

  ![](img/design-rules.png)
  ![](img/net-class-editor.png)
  ![](img/global-design-rules.png)
- Ensure track and via sizes

  ![](img/track-via-sizes.png)

### 8. Add tracks and vias

1. Add track by choosing the upper copper layer

  ![](img/front-copper.png)
- Choose `Add tracks and vias`

  ![](img/add-tracks-vias.png)

### 9. Fill zones

1. Click `fill zones`

  ![](img/add-fill-zones.png)
- Click and add **front copper fill**

  ![](img/fcu-fill.png)
- OR Click and add **back copper fill**

  ![](img/bcu-fill.png)
- Right click to `Fill or Refill zones`

  ![](img/fill-or-refill-zones.png)


### 10. Connecting via

1. Click `v` to drop a via
- Double click to finish
- Hit `b` to redraw

### 11. Creating Silk Screen

1. Choose silk screen layer

  ![](img/silk-screen-layer.png)
- Choose Text editing

  ![](img/choose-text.png)
- Add in text manually

  ![](img/add-text-manually.png)
