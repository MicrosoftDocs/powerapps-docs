---
title: "Customize the editable grid control | Microsoft Docs"
description: "Learn how you can customize the editable grid control."
keywords: "Component Framework, code components, Power Apps controls"
author: clromano
ms.author: clromano
ms.date: 07/25/2022
ms.reviewer: jdaly
ms.topic: how-to
ms.subservice: pcf
contributors:
 - JimDaly
 - aliry
---

# Customize the editable grid control

The  [Power Apps grid control](../../maker/model-driven-apps/the-power-apps-grid-control.md) uses modern Microsoft Fluent controls to allow users to see and edit values in grid cells. Scenarios might exist that have special requirements requiring modification of the out-of-the-box visuals and user interactions. To facilitate these scenarios, the Power Apps grid control provides extensibility APIs that allow the grid interface to be customized. Makers can use these APIs to implement a grid customizer control (code component) to provide custom cell renderer and editor components to the grid.

:::image type="content" source="../../maker/model-driven-apps/media/power-apps-grid-custom-renderers.png" alt-text="Custom cell renderers for the Power Apps grid control" lightbox="../../maker/model-driven-apps/media/power-apps-grid-custom-renderers.png":::

## Grid customizer control

A grid customizer is a PCF control implementing the Power Apps grid control customizer interface. This interface allows you to define the React element that is rendered when a grid cell is in read-only mode (the cell renderer) or in edit mode (the cell editor). Multiple grid customizer controls can exist in an environment, but each grid can only have a single grid customizer control assigned. You might decide that a separate customizer control is needed for each grid you want to modify, or you might choose to reuse the same customizer control for multiple grids.

### Implementing a grid customizer control

To implement a grid customizer control, you first need to be familiar with the steps to [Create and build a code component](create-custom-controls-using-pcf.md) and you must have access to the template control.

The template control is included in the [PowerApps-Samples](https://github.com/microsoft/PowerApps-Samples) GitHub repository. You need to clone or download the repo to access the files located here: [PowerApps-Samples/component-framework/resources/GridCustomizerControlTemplate](https://github.com/microsoft/PowerApps-Samples/tree/master/component-framework/resources/GridCustomizerControlTemplate)

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
   > If the function returns null or undefined, then the grid uses the internal renderer/editor for the targeted cells.
    
1. After defining your custom cell renderers and editors, **package** the grid customizer control and **import** it to your Power Apps environment. Alternatively, you can use the [pac pcf push](/power-platform/developer/cli/reference/pcf#pac-pcf-push) command.
1. After publishing the grid customizer control, open the **Customize the system** panel from the **Settings > Customizations** menu.

   :::image type="content" source="media/customize-editable-grid-settings-customize-system.png" alt-text="Open the Customize the system panel from the Settings > Customizations menu":::

1. From the entities node, select an entity that your customizer control targets (for example, Account).  
1. From the right panel, select the **Controls** tab.

   :::image type="content" source="media/customize-editable-grid-control-tab.png" alt-text="The grid control tab":::

1. From the **Controls** list, add the **Power Apps grid control**.

   :::image type="content" source="media/customize-editable-grid-add-power-apps-grid-control.png" alt-text="Adding the Power Apps grid control" lightbox="media/customize-editable-grid-add-power-apps-grid-control-full.png":::

1. In the **Properties** panel, set the **Customizer control** property to the full logical name of your grid customizer code component.

   Full logical name = `{publisher prefix}_{namespace}.{control name}`

   :::image type="content" source="../../maker/model-driven-apps/media/power-apps-grid-assign-customizer-control.png" alt-text="Assign a value to the customizer control property of the Power Apps grid control" lightbox="media/power-apps-grid-assign-customizer-control-full.png":::
 
1. **Save and publish** your customizations for this entity.
1. Test your customizer by opening the main grid for the customized entity.
1. Repeat steps 6-11 for any other entities whose grid needs a grid customizer control.

## Best practices

- Cell renderers and editors are user interface components. Don't use them to mutate data or metadata of the grid.
- The customizer controls should be lightweight and fast so as to not affect overall grid performance.
- To maintain the design consistency, follow [Fluent design principles](https://www.microsoft.com/design/fluent/#/) and use [Fluent controls](https://developer.microsoft.com/en-us/fluentui#/controls/web) in your customizers.
- Make sure your custom renderer or editor is accessible.
- The customizer function should be pure since the grid calls it multiple times to get customized elements and expects the return value to be consistent.
- The grid might dispose a customizer element at any time and call to get a new one at any time. Make sure to dispose of any internal state on unmount to prevent memory leaks.
- Don't use renderers to override the values in the grid since the server doesn't use the new values to do filtering or sorting.

## Example

You can find an example of a customized editable grid control here: [Customized editable grid](sample-controls/customized-editable-grid-control.md).

### See also

[Power Apps component framework overview](overview.md)<br/>
[Create your first code component](implementing-controls-using-typescript.md)<br/>
[Learn Power Apps component framework](/training/paths/use-power-apps-component-framework)


[!INCLUDE [footer-banner](../../includes/footer-banner.md)]
