---
title: "Change model-driven app custom table icons in Power Apps | MicrosoftDocs"
description: "Learn how to change the icon for a custom table"
ms.custom: ""
ms.date: 05/04/2020
ms.reviewer: ""
ms.service: powerapps
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

[!INCLUDE [cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

When a custom table is created, it is automatically assigned a default icon. All custom tables use the same icon by default. Use custom icons to differentiate how your custom tables look. It is not possible to modify the icons assigned to system tables.

In the example show we see that the accounts table has an icon already assigned to it as it is a system table, however the other tables have the default icon.

:::image type="content" source="media/icons-start.png" alt-text="Model-driven apps without icons set":::
  
 Three types of table icons for each custom table can be uploaded. 

|Icon Type  |Description  |
|---------|---------|
|**Unified Interface Icon**|Must be a scalable vector graphic (.svg) icon |
|**Icon in Web application**|An .svg, .gif, .png, or .jpg format image, 16x16 pixels in size.|
|**Icon for table forms**|An .svg, .gif, .png, or .jpg format image, 32x32 pixels in size.|

> [!NOTE]
> All image files must be no more than 10 kilobytes in size.
>
> When a scalable vector graphic (.svg) image is used as the **Icon in Web application** or **Icon for table forms**, it must have the default size set. Since SVG is an XML document, the [svg](https://developer.mozilla.org/docs/Web/SVG/Element/svg) element [width](https://developer.mozilla.org/docs/Web/SVG/Attribute/width) and [height](https://developer.mozilla.org/docs/Web/SVG/Attribute/height) values can be edited with a text editor to define the default size for the image.

Each type of icon is stored as a Web Resource. The web resources can be created first and then set the icons to use them, or this can be created when creating the new web resource within the **Lookup Row** dialog by selecting **New** while setting the value. More information: [Create or edit web resources to extend an app](create-edit-web-resources.md)

## Set the icons for a custom table

### Navigate to the table within the solution explorer

The solution explorer is the only approved method of setting table icons.

1. From the Power Apps portal select **Solutions**.
2. Navigate to the unmanaged solution with the tables where icons need to be set.
3. Select **Switch to classic** from within the solution.  The 3 dots in the menu may need to be selected first.  This will navigate a designer to the classic solution explorer.

4. Once in the classic solution explorer expand the entities (tables) node.

5. Select the custom table which requires an updated icon.

### Set table icons

1. On the command bar, select **Update Icons**.  
  
2. In the **Select New Icons** dialog box, in the **Web Client** tab, under **Icon in Web application** or **Icon for Entity Forms**, to the right of **New Icon**, select the **Browse** button ![Lookup button.](media/lookup-button-4.gif).
3. Select or create the appropriate web resource, and then select **OK**. 
4. In the **Unified Interface** tab, do the same for the **New Icon** column.
5. Select **OK** to close the **Select New Icons** dialog
6. On the command bar, on the **File** menu, select **Save**.  
7. When your changes are complete, publish them. Select **Publish** in the command bar while the table is selected in solution explorer.

## Review changes to your model-driven app icons

Once the updates have taken effect the changes can be reviewed by playing the app.  In this case the Courses entity/table has been updated and the icon has changed.  

:::image type="content" source="media/icons-end.png" alt-text="Model-driven apps without icons set":::

## Community tools

**[Iconator](https://www.xrmtoolbox.com/plugins/MscrmTools.Iconator/)** is a tool that XrmToolbox community developed for Power Apps. This allows a designer to **update** the icons associated with a table in addition to introducing **new icons**.

See the [Developer tools for Microsoft Dataverse](../../developer/data-platform/developer-tools.md) topic for community developed tools.

> [!NOTE]
> The community tools are not a product of Microsoft and does not extend support to the community tools.
> If there are questions relating to the tool, please contact the publisher. More Information: [XrmToolBox](https://www.xrmtoolbox.com).

## Next steps

[Create a table](/powerapps/maker/model-driven-apps/data-platform-create-entity)<br />
[Edit a table](../data-platform/edit-entities.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]