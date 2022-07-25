---
title: "Customize the editable grid control (Preview)| Microsoft Docs"
description: "Learn how you can customize the editable grid control."
keywords: "Component Framework, code components, Power Apps controls"
ms.author: jasongre
author: jasongre
ms.date: 07/22/2022
ms.reviewer: jdaly
ms.topic: article
ms.subservice: pcf
contributors:
 - JimDaly
 - aliry
---

# Customize the editable grid control (Preview)

[This article is pre-release documentation and is subject to change.]

The  [Power Apps grid control (preview)](../../maker/model-driven-apps/the-power-apps-grid-control.md) uses modern Microsoft Fluent controls to allow users to see and edit values in grid cells. Scenarios may exist, however, that have special needs requiring modification of the out-of-the-box visuals and user interactions. To faciltate this, the Power Apps grid control provides extensibility APIs that allow the grid interface to be customized. Using these APIs, makers can implement a grid customizer control (code component) to provide custom cell renderer and editor components to the grid.

:::image type="content" source="../../maker/model-driven-apps/media/power-apps-grid-custom-renderers.png" alt-text="Custom cell renderers for the Power Apps grid control" lightbox="../../maker/model-driven-apps/media/power-apps-grid-custom-renderers.png":::

## Grid customizer control

A grid customizer is a PCF control implementing the Power Apps grid control customizer interface. This interface allows you to define the React element that will be rendered when a grid cell is in read-only mode (the cell renderer) or in edit mode (the cell editor). Multiple grid customizer controls can exist in an environment, but each grid can only have a single grid customizer control assigned. You may decide that a separate customizer control is needed for each grid you want to modify, or you may choose to reuse the same customizer control for multiple grids.

### Implementing a grid customizer control

To implement a grid customizer control, you first need to be familiar with the steps to [Create and build a code component](create-custom-controls-using-pcf.md) and you must have access to the template control.

The template control is included in the [PowerApps-Samples](https://github.com/microsoft/PowerApps-Samples) GitHub repository. You will need to clone or download the repo to access the files located here: [PowerApps-Samples/component-framework/resources/GridCustomizerControlTemplate](https://github.com/microsoft/PowerApps-Samples/tree/master/component-framework/resources/GridCustomizerControlTemplate)

1. Open the `GridCustomizerControlTemplate` folder using Visual Studio Code.
1. In a terminal window, run `npm install`.
1. Create your custom cell renderers and editors.

   The customization code is in the **customizers** folder.
   - `CellRendererOverrides.tsx` includes cell renderer customizers per data type.
   - `CellEditorOverrides.tsx` includes cell editor customizers per data type.

   Modify these files to add react elements to be rendered when a cell is in read-only (cell renderer) or in edit (cell editor) mode.

   Each file exports an object mapping the column data type to a function returning a react element to be rendered inside the cells for that column type.


   ```typescript
   /**
    * Provide cell renderer overrides per column data type.
   */
    export interface CellRendererOverrides {
      [dataType: string]: (props: CellRendererProps, rendererParams: GetRendererParams)
      => React.ReactElement | null | undefined; 
   };

   /**
    * Provide cell editor overrides per column data type.
   */
    export interface CellEditorOverrides {
      [dataType: string]: (defaultProps: CellEditorProps, rendererParams: GetEditorParams)
      => React.ReactElement | null | undefined; 
   };
   ```

   > [!NOTE]
   > If the function returns null or undefined, then the grid will use the internal renderer/editor for the targeted cells.
    
1. After defining your custom cell renderers and editors, **package** the grid customizer control and **import** it to your Power Apps environment. Alternatively, you can use the `pac pcf push` command. More information: [PCF command](/power-platform/developer/cli/reference/pcf-command)
1. After publishing the grid customizer control, open the **Customize the system** panel from the **Settings > Customizations** menu.

   :::image type="content" source="media/customize-editable-grid-settings-customize-system.png" alt-text="Open the Customize the system panel from the Settings > Customizations menu":::

1. From the entities node, select an entity that your customizer control will target (e.g. Account).  
1. From the right panel, select the **Controls** tab.

   :::image type="content" source="media/customize-editable-grid-control-tab.png" alt-text="The grid control tab":::

1. From the **Controls** list, add the **(Preview) Power Apps grid control**.

   :::image type="content" source="media/customize-editable-grid-add-power-apps-grid-control.png" alt-text="Adding the (Preview) Power Apps grid control" lightbox="media/customize-editable-grid-add-power-apps-grid-control-full.png":::

1. In the Properties panel, set the **Customizer control** property to the full logical name of your grid customizer code component.

   Full logical name = `{publisher prefix}_{namespace}.{control name}`

   :::image type="content" source="../../maker/model-driven-apps/media/power-apps-grid-assign-customizer-control.png" alt-text="Assign a value to the customizer control property of the Power Apps grid control" lightbox="../../maker/model-driven-apps/media/power-apps-grid-assign-customizer-control-full.png":::
 
1. **Save and publish** your customizations for this entity.
1. Test your customizer by opening the main grid for the customized entity.
1. Repeat steps 6-11 for any other entities whose grid needs a grid customizer control.

## Example

You can find an example of a customized editable grid control here: [Customized Editable Grid Control](sample-controls/customized-editable-grid-control.md).

### See also

[Power Apps component framework overview](overview.md)<br/>
[Create your first code component](implementing-controls-using-typescript.md)<br/>
[Learn Power Apps component framework](/learn/paths/use-power-apps-component-framework)


[!INCLUDE [footer-banner](../../includes/footer-banner.md)]