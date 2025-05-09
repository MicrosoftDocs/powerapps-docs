---
title: "Add relationships in a model-driven app form in Power Apps | MicrosoftDocs"
description: "Learn how to change the navigation within a form"
ms.custom: ""
ms.date: 09/13/2022
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: how-to
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "powerapps"
author: "Mattp123"
ms.assetid: 4c379202-9f0e-4003-a49c-efff53e7f79f
caps.latest.revision: 63
ms.subservice: mda-maker
ms.author: "matp"
search.audienceType: 
  - maker
---
# Add table relationships to a form

Creating a table relationship adds the navigation within a form that allows app users to view a list of related records from the **Related** tab in a model-driven app.

:::image type="content" source="media/related-tab.png" alt-text="Related tab in a model-driven app":::

Each table relationship has properties to control the relationship behavior. More information: [Table relationship behavior](../data-platform/create-edit-entity-relationships.md#table-relationship-behavior)
  
Table relationships that are configured to be displayed can be hidden using the form designer.

## Add, edit, or create a related table in form designer (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

> [!IMPORTANT]
> This is a preview feature.

1. Sign into [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc)
1. Select **Solutions** on the left navigation pane, open the solution that has the table you want, and then open the table. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]
1. Select **Forms**, and then open the main form where you want to add a related table.
1. Select the **Related** tab. The **Related** menu appears:
   - Add and edit an existing relationship. Select a table in the list to display the table properties in the right pane. Select **Edit relationship** to make changes to the relationship. More information: [Add advanced relationship behavior](../data-platform/data-platform-entity-lookup.md#add-advanced-relationship-behavior)
   - Add a new relationship. Select **+** to **Search** for another relationship or select **New relationship** to create either a **One-to-many relationship** or **Many-to-many** relationship. More information: [Add a One-to-many relationship](../data-platform/data-platform-entity-lookup.md#add-a-one-to-many-relationship) and [Add a Many-to-many relationship](../data-platform/data-platform-entity-lookup.md#add-a-many-to-many-relationship)

     :::image type="content" source="media/add-relationship-form-designer.png" alt-text="Add a related table":::
1. **Save** and **Publish** the change.

### Hide a relationship

1. In form designer, select the **Related** tab, and then select the table where you want to hide a relationship.
1. On the right properties pane, under **Display options** select **Hide**.
1. **Save and Publish** the change.

### Relationship management limitations in form designer

- You can edit display options for system relationships but you can’t remove the relationship from the related menu. However, you can hide the relationship. More information: [Hide a relationship](#hide-a-relationship)
- You can’t edit or remove self many-to-many relationships.
- You can't add or edit related web resources or external URLs.

## Create navigation using the legacy experience

To enable editing navigation first select **Navigation** from the **Select** group on the **Home** tab of the form designer.  

> [!div class="mx-imgBorder"] 
> ![Navigation command.](media/navigation-command.png)
 
In the right pane, from **Relationship Explorer** you can filter by 1:N (one-to-many) or N:N (many-to-many) relationships, or view all available relationships. The **Only show unused relationships checkbox** is disabled and selected. Relationships are added one at a time. 
 
> [!div class="mx-imgBorder"] 
> ![Relationship explorer.](media/relationship-explorer.png)

To add a relationship from the **Relationship Explorer** just double-click the relationship and it will be added below the currently selected relationship in the navigation area. Double-click a relationship in the navigation area and you can change the label on the **Display** tab. On the **Name** tab you can see information about the relationship. Use the **Edit** button to open the definition of the table.  
  
There are five groups in the navigation area. You can drag them to reposition them and double-click them to change the label, but you can’t remove them. These groups will only display when there is something in them. So if you don’t want a group to appear, just don’t add anything to it.  
  
Use the **Navigation Link** button in the **Control** group of the **Insert** tab to add a link to a web resource or external URL.  
 
![Navigation link.](media/navigation-link.png)
 
<a name="BKMK_NavigationLinkProperties"></a>   

### Navigation link properties

 Navigation links have the following properties:  
  
|Property|Description|  
|--------------|-----------------|  
|Name|**Required**: Text to display as a label.|  
|Icon|Use a 32x32 pixel web resource. Use a PNG image with a transparent background is recommended.|  
|Web Resource|Specify a web resource to display in the main pane of the form.|  
|External URL|Specify the URL of a page to display in the main pane of the form.|  

<a name="BKMK_PrivacyNotices"></a>   

## Privacy notices

 [!INCLUDE[cc_privacy_crm_website_preview_control](../../includes/cc-privacy-crm-website-preview-control.md)]    
  
 [!INCLUDE[cc_privacy_multimedia_control](../../includes/cc-privacy-multimedia-control.md)]  

## See also

[Create and edit table relationships for Microsoft Dataverse](../data-platform/create-edit-entity-relationships.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
