---
title: "Customizing the Power Apps grid control | MicrosoftDocs"
description: "A control for use with Power Apps that lets users view, open, and edit records from a view or subgrid"
ms.custom: ""
ms.date: 06/20/2022
ms.reviewer: "matp"

ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "overview"
applies_to: 
  - "powerapps"
author: "Mattp123"
ms.subservice: mda-maker
ms.author: "matp"
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Customizing the Power Apps grid control

The [Power Apps grid control](./the-power-apps-grid-control.md) uses modern Microsoft Fluent controls to allow users to see and edit values in grid cells. Scenarios may exist, however, that have special needs requiring modification of the out-of-the-box visuals and user interactions. To faciltate this, the Power Apps grid control provides extensibility APIs that allow the grid interface to be customized. Using these APIs, makers can implement a grid customizer control (code component) to provide custom cell renderer and editor components to the grid. 

:::image type="content" source="media/power-apps-grid-custom-renderers.png" alt-text="Custom cell renderers for the Power Apps grid control":::

## Grid customizer control
A grid customizer is a PCF control implementing the Power Apps grid control customizer interface, which allows you to define the React element that will be rendered when a grid cell is in read-only mode (the cell renderer) or in edit mode (the cell editor). Multiple grid customizer controls can exist in an environment, but each grid can only have a single grid customizer control assigned. You may decide thta a separate customizer control is needed for each grid you want to modify, or you may choose to reuse the same customizer control for multiple grids.

### Implementing a grid customizer control
To implement a grid customizer control, you first need to be familiar with [creating and building code components](https://docs.microsoft.com/en-us/power-apps/developer/component-framework/create-custom-controls-using-pcf) and then follow the steps below: 

1.  Download the template control [here]().
1.  Unzip and navigate to the control template directory.
1.  Run `npm install`.
1.  Create your custom cell renderers and editors. 

    The customization code is in the **customizers** folder.
    -  `CellRendererOverrides.tsx` includes cell renderer customizers per data type.
    -  `CellEditorOverrides.tsx` includes cell editor customizers per data type.

    You will modify these files to add React elements used for cell renderers or cell editors. Each file exports an object that maps the column data type to a function returning a React element to be rendered inside the cells for that column type.
    
        export interface CellRendererOverrides {
          [dataType: string]: (props: CellRendererProps, rendererParams: GetRendererParams)
            => React.ReactElement | null | undefined; 
        }
        
        export interface CellEditorOverrides {
          [dataType: string]: (defaultProps: CellEditorProps, rendererParams: GetEditorParams)
            => React.ReactElement | null | undefined; 
        }
 
    Note: If the function returns null or undefined, then the grid will use the internal renderer/editor for the targeted cells.
    
1.  After defining your custom cell renderers and editors, **package** the grid customizer control and **import** it to your Power Apps environment. Alternatively, you can use the `pac pcf push` command.
1.  After publishing the grid customizer control, open the **Customize the system** panel from the **Settings > Customiztaion** menu.
1.  From the entities node, select an entity that your customizer control will target (e.g. Account).  
1.  From the right panel, select the **Controls** tab.
1.  From the Controls list, add the **(Preview) Power Apps grid control**.
1.  In the Properties panel, set the **Customizer control** property to the full logical name of your grid customizer code component.
    
        Full logical name = {publisher prefix}_{namespace}.{control name}

    :::image type="content" source="media/power-apps-grid-assign-customizer-control.png" alt-text="Assign a value to the customizer control property of the Power Apps grid control":::
 
1.  **Save and publish** your customizations for this entity.
1.  Test your customizer by opening the main grid for the customized entity. 
1.  Repeat steps 7-12 for any other entities whose grid needs a grid customizer control.
