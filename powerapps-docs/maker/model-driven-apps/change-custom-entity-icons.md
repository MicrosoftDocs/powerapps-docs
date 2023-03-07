---
title: "Change model-driven app custom table icons in Power Apps | MicrosoftDocs"
description: "Learn how to change the icon for a custom table"
ms.custom: ""
ms.date: 07/20/2022
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "how-to"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "powerapps"
author: "Mattp123"
ms.assetid: 477f9792-8207-49ef-8968-45274b5355a8
caps.latest.revision: 19
ms.subservice: mda-maker
ms.author: "matp"
manager: "kvivek"
tags: 
  - "Links to topic not migrated"
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---
# Change model-driven app custom table icons

When a custom table is created, it is automatically assigned a default icon. All custom tables use the same icon by default. Use custom icons to differentiate how your custom tables look. It is not possible to modify the icons assigned to system tables.

In the example here, the accounts table has an icon already assigned to it as it is a system table, however the other tables have the default icon.

:::image type="content" source="media/icons-start.png" alt-text="Model-driven apps without icons set":::
  
Icons can be used for the following purposes with model-driven apps.

|Icon Type  |Description  |
|---------|---------|
|**Table icon**|A .svg, .gif, .png, or .jpg format image, 16x16 pixels in size. This article describes how to edit the table icon. |
|**Icon for table forms**|A .svg, .gif, .png, or .jpg format image, 32x32 pixels in size. More information: [ Enable or disable table options](../data-platform/edit-entities.md#enable-or-disable-table-options) |
|**App icon**|Must be a scalable vector graphic (.svg) icon. More information: [Manage model-driven app settings in the app designer](app-properties.md) |

> [!NOTE]
>
> - All image files must be no more than 10 kilobytes in size.
>
> - Setting the icon in the app designer overrides the table definition icon setting. When the table icon in app designer is set to the default icon, the icon specified in the table definition is displayed in the app.
>
> - When a scalable vector graphic (.svg) image is used as the app icon or icon for table forms, it must have the default size set. Since SVG is an XML document, the [svg](https://developer.mozilla.org/docs/Web/SVG/Element/svg) element [width](https://developer.mozilla.org/docs/Web/SVG/Attribute/width) and [height](https://developer.mozilla.org/docs/Web/SVG/Attribute/height) values can be edited with a text editor to define the default size for the image.

Each type of icon is stored as a web resource. Create a web resource first and then set the icons to use them. Alternatively, you can add the icon by creating a new web resource when you define the table properties.

## Set the icons for a custom table from the table definition

1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).  

1. Select **Solutions**, and then open the solution you want or create a new one. Then open the custom table from the solution. To use the default solution, expand **Data**, select **Tables**, and then open the table you want.

1. Select **Properties**. In the right **Edit table** pane, expand **Advanced options**.

1. Under **Choose table image**, select from the following options:
   - Select the dropdown to choose an existing web resource.
   - Select **New image web resource** to create a web resource to add the icon. More information: [Create or edit web resources to extend an app](create-edit-web-resources.md) 
   :::image type="content" source="media/select-table-icon.png" alt-text="Select the table icon you want or create a new one":::

1. Select **Save**.

## Set the icon for a custom table in app designer

1. On the app designer left pane, select the table.
1. In the right table properties pane, under **Icon**, select **Use web resource** > **Select icon**.
1. Select from the list of existing image web resources or select New to create a new one.
1. Select **Select**, and then select **Publish** to make the changes available in your app. 

## Review changes to your model-driven app icons

Once the updates have taken effect the changes can be reviewed by playing the app.  In this case, the *Courses* table has been updated and the icon has changed.  

:::image type="content" source="media/icons-end.png" alt-text="Model-driven apps with updated icon set":::

### Set the icons for a custom table (classic)

1. From the Power Apps portal, select **Solutions**.
2. Open the unmanaged solution with the tables where icons need to be set.
3. Select **Switch to classic** from within the solution command bar (you may need to select **...** first). This opens the solution in the classic solution explorer.

4. Once in the classic solution explorer, expand **Entities** (tables).

5. Select the custom table, which requires an updated icon.

#### Set table icons

1. On the command bar, select **Update Icons**.  
  
2. In the **Select New Icons** dialog, on the **Web Client** tab, under **Icon in Web application** or **Icon for Entity Forms**, to the right of **New Icon**, select the **Browse** button ![Lookup button.](media/lookup-button-4.gif).
3. Select or create the appropriate web resource, and then select **OK**.
4. In the **Unified Interface** tab, do the same for the **New Icon** column.
5. Select **OK** to close the **Select New Icons** dialog.
6. On the command bar, on the **File** menu, select **Save**.  
7. When your changes are complete, publish them. Select **Publish** in the command bar while the table is selected in solution explorer.

## Community tools

**[Iconator](https://www.xrmtoolbox.com/plugins/MscrmTools.Iconator/)** is a tool that XrmToolbox community developed for Power Apps. This allows a designer to **update** the icons associated with a table in addition to introducing **new icons**.

See the [Developer tools for Microsoft Dataverse](../../developer/data-platform/developer-tools.md) article for community developed tools.

> [!NOTE]
> The community tools are not a product of Microsoft and Microsoft doesn't provide support for the community tools.
> If there are questions relating to the tool, please contact the publisher. More Information: [XrmToolBox](https://www.xrmtoolbox.com).

## Next steps

[Create a table](/powerapps/maker/model-driven-apps/data-platform-create-entity)<br />
[Edit a table](../data-platform/edit-entities.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]