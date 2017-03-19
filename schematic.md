# Create schematic

## Things to do

1. Add components, wires, labels, power, edit components
1. Annotate schematic
1. Perform electrical rules check
1. Generate net list
1. Associate component with footprint


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
1. Click `Generate`

    ![](img/generate-netlist.jpg)
1. Save NetList

    ![](img/save-netlist.png)
1. Run PCB New

    ![](img/run-pcbnew.png)
