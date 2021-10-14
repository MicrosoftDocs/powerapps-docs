---
title: "Create a model-driven app site map in Power Apps | MicrosoftDocs"
description: "Learn how to create a site map for your app"
keywords: ""
ms.date: 05/29/2018
ms.service: powerapps
ms.custom: 
ms.topic: tutorial
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "powerapps"
author: "Mattp123"
ms.assetid: 2461bd71-6cb4-46b7-8d1f-6a0aa3dca809
ms.subservice: mda-maker
ms.author: "matp"
manager: kvivek
ms.reviewer: 
ms.suite: 
ms.tgt_pltfrm: 
caps.latest.revision: 18
topic-status: Drafting
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---

# Create a model-driven app site map using the site map designer

[!INCLUDE [cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

In this tutorial you perform several site map tasks such as creating a new site map, and adding an area, group, and subarea.

Site maps define the navigation for your app. Create a site map for your app with ease by using the tile-based site map designer. Use the designer to drag components onto the design canvas, preview your work, and instantly publish the site map. System customizers or any user with the required privileges can quickly create site maps for apps.  
  
The site map designer also lets you define the area, subarea, or group titles in the languages supported by the environment.  
  
A default site map is available. You can edit this site map or configure site maps for new apps by using the site map designer. The site map designer is integrated with the app designer.  

## Prerequisites
Make sure that you have the System Administrator or System Customizer security role or equivalent permissions.  Specifically, any user with the following privileges can also create apps:  
-   Create, Read, and Write privileges for the App table  
-   Read and Write privileges for the Customizations table  
-   Read privileges for the Solution table

You can view or set these privileges on the **Customization** tab of a security role.
  
## Create a site map for an app  
  
1. On the app designer canvas, in the **Site Map** area, select the pencil icon![Open Site Map Designer button.](media/dynamics365-open-designer.PNG "Open Site Map Designer button")next to **Site Map** to **Open the Site Map Designer** .  

   ![Open the site map designer.](media/app-designer-sitemap-location.png "Open the site map designer")
  
    The site map designer opens a canvas that is prepopulated with one area, one group, and one subarea. Select the area, group, or subarea tile to change its properties.
 
    > [!NOTE]
    >  Selecting **Open the Site Map Designer** ![Open Site Map Designer button.](media/dynamics365-open-designer.PNG "Open Site Map Designer button") from the app designer canvas automatically creates a new site map (if there's no existing site map), and gives the new site map the same name as the app name and the same unique name as the app unique name. 

2.  [Add an area to the site map](create-site-map-app.md#bkmk_AddArea).  
  
3.  [Add a group to the site map](create-site-map-app.md#bkmk_AddGroup).  
  
4.  [Add a subarea to a group in the site map](create-site-map-app.md#bkmk_AddSubarea).  
  
5.  Select **Save**.  
  
    > [!NOTE]
    >  The new site map is associated with the app when you go back to the app designer and select **Save**. When a site map is configured, **Configured** appears on the site map tile; otherwise **Not Configured** appears on the tile.  If you open the site map designer from the app designer and configure a new site map, but close the browser before associating the site map with the app, the site map will be automatically associated with the app the next time you open the app designer, based on the app unique name.  
  
6.  Select **Publish**.  
  
## Edit the default site map 

 Your environment comes with a default site map.  
  
1. Open solution explorer.  
  
2. In the solution window, under **Components**, select **Client Extensions**.  

3. On the component toolbar, select **Add Existing** > **Site Map**.

4. In the list of solution components, select the site map named **Site Map**, and then select **OK**.
  
5.  Double-click to select the site map you added that has the display name **Site Map** and is in a **Managed** state. You can also select the site map, and then on the toolbar, select **Edit**.  
  
     The site map opens in the site map designer.  
  
6.  [Add an area to the site map](create-site-map-app.md#bkmk_AddArea).  
  
7.  [Add a group to the site map](create-site-map-app.md#bkmk_AddGroup).  
  
8.  [Add a subarea to a group in the site map](create-site-map-app.md#bkmk_AddSubarea).  
  
9. Select **Save**.  
  
10. Select **Publish**.  
  
<a name="bkmk_AddArea"></a>   
## Add an area to the site map  
  
1.  Select **Add** ![Add button on the designer.](media/dynamics365-designer-addbutton.PNG "Add button on the designer") on the site map designer canvas, and then select **Area**.  
  
     or  
  
     From the **Components** tab, drag the **Area** tile to the empty box on the canvas. You'll see the empty box when you move the tile to the correct place on the canvas.  
  
2.  Select the area you just added. You'll see the **Properties** tab highlighted in the pane to the right of the canvas.  
  
3.  Add or edit the area properties.  
  
     Under **General**, do the following:  
  
    - **Title**: Enter the title for the area in the base language of the organization.  
  
    - **Icon**: A default application icon is selected. Select a different icon for the area from the list of web resources available in the solution.  
  
    - **ID**: A unique ID is automatically generated, but you can enter a different one if you want. We recommend that you use the provided ID because if the ID you enter is not unique, users might get an error when they're using the app, or you might get an error when you import a solution that contains this site map.  
  
    - **Show Groups**: Select this check box to show groups of subareas in the navigation pane.  
  
     Under **Advanced**, do the following:  
  
    - **More Titles**: If your organization uses multiple languages, select a language (Locale) for the title, enter the title, and then select **Add** ![Add button in the site map designer.](media/add-icon-sitemap-designer.png "Add button in the site map designer"). You can create, edit, or delete titles for as many languages as your organization uses. However, you can have only one title per language.  
  
    - **More Description**: If your organization uses multiple languages, select a language for the description, enter the description, and then select **Add** ![Add button in the site map designer.](media/add-icon-sitemap-designer.png "Add button in the site map designer"). You can create, edit, or delete descriptions for as many languages as your organization uses. However, you can have only one description per language.  
  
    - **URL**: Enter the URL to render for the Dynamics 365 for Outlook folder that represents the area.  
  
<a name="bkmk_AddGroup"></a>   
## Add a group to the site map  
  
1.  On the site map designer canvas, select the area you want to add the group to.  
2.  Select **Add** ![Add button on the designer.](media/dynamics365-designer-addbutton.PNG "Add button on the designer"), and then select **Group**.  
  
     or  
  
     From the **Components** tab, drag the **Group** tile to an empty box under the **Area** in the canvas. You'll see the empty box when you move the tile to the correct place in the canvas.  
  
3.  Select the group you just added.  
  
4.  On the **Properties** tab, add or edit the group properties:  
  
     Under **General**, do the following:  
  
    - **Title**: Enter the title for the group in the base language of the organization.  
  
    - **ID**: A unique ID is automatically generated. Enter a different one if necessary. We recommend using the automatic ID because if the ID you enter is not unique, you might get an error when you import a solution containing this site map.  
  
     Under **Advanced**, do the following:  
  
    - **More Titles**: If your organization uses multiple languages, select a language (Locale) for the title, enter the title for the group, and then select **Add** ![Add button in the site map designer.](media/add-icon-sitemap-designer.png "Add button in the site map designer"). You can create, edit, or delete titles for as many languages as your organization uses. However, you can have only one title per language.  
  
    - **More Descriptions**: If your organization uses multiple languages, select a language for the description, enter the description for the group, and then select **Add** ![Add button in the site map designer.](media/add-icon-sitemap-designer.png "Add button in the site map designer"). You can create, edit, or delete descriptions for as many languages as your organization uses. However, you can have only one description per language.  
  
    - **URL**: Enter the URL to render for the Dynamics 365 for Outlook folder that represents the group.  

    - **Set as Profile**: Select this check box to indicate whether this group represents a user-selectable profile for the workplace. The group set as a user-selectable profile is made available as options in your personal options. This only applies for groups within the **Workplace** area.  
  
<a name="bkmk_AddSubarea"></a>   
## Add a subarea to a group in the site map  
  
1.  Select **Add** ![Add button on the designer.](media/dynamics365-designer-addbutton.PNG "Add button on the designer") on the site map designer canvas, and then select **Subarea**.  
  
     or  
  
     From the **Components** tab, drag the **Subarea** tile to an empty box under the **Group** section in the canvas. You'll see the empty box when you move the tile to the correct place in the canvas.  
  
2.  Select the subarea you just added.  
  
3.  On the **Properties** tab, add or edit the subarea properties:  
  
     Under **General**, do the following:  
  
    - **Type**: Select whether the subarea you are adding is a dashboard, table, web resource, or URL.  
  
    - **Entity**: Select the table that the subarea is for. This column is disabled if the subarea type is other than **Entity** in the **Type** drop-down list.  
  
    - **URL**: Specify a URL to a web page. The URL text displays from this subarea and, when selected, a new browser window opens that displays the page. This column is disabled if you've selected **Entity** in the **Type** drop-down list.  
 
      > [!IMPORTANT]
      > Site map subarea URLs that link to an .aspx page aren’t supported.
 
    - **Default Dashboard**: Select the default dashboard to be displayed for this subarea. This column is disabled if you haven't selected **Dashboard** in the **Type** drop-down list.  
  
    - **Title**: Enter the title for the subarea in the base language of the organization.  
  
    - **Icon**: A default application icon is selected. Select a different icon for the subarea from the list of web resources available in the solution.  
  
    - **ID**. A unique ID is automatically generated. Enter a different unique ID if necessary.  
  
    - **Parameter Passing**. Select this check box to pass information about the organization and language context to the URL. This check box is checked only when the subarea type is a web resource or a URL-based subarea.  
  
     Under **Advanced**, do the following:  
 
    - **Privileges**: This defines whether a subarea is displayed based on privileges available in any security roles that are assigned to the user. Select the name of the table to check privileges for, and then select the check boxes to assign privileges. 
  
    - **More Titles**: If your organization uses multiple languages, select a language for the title, enter the title for the subarea, and then select **Add**. You can create, edit, or delete titles for as many languages as your organization uses. However, you can have only one title per language.  
  
    - **More Descriptions**: If your organization uses multiple languages, select a language for the description, enter the description for the subarea, and then select **Add**. You can create, edit, or delete descriptions for as many languages as your organization uses. However, you can have only one description per language.  
  
    - **SKUs**: Select the versions of Dynamics 365 that display this subarea.  
  
    - **Client**: Select the type of client that displays this subarea.  
  
    - **Outlook Shortcut**: Select the icon to display in Dynamics 365 for Outlook.  
  
    - **Offline Availability**: Select this check box to make this subarea available to users when they are offline in Dynamics 365 for Outlook.  
  
## Organize areas, groups, and subareas  
 You can organize your areas, groups, and subareas by dragging them to new positions. A container box appears where you can drop the tiles. Here are some things you can do:  
  
-   Move a subarea to a new position within the same group or a different group under the same area.  
  
-   Move a subarea to a new position within a group under a different area.  
  
-   Move a group to a new position within the same area.  
  
-   Move a group to a new position in a different area.  
  
-   Move an area to a new position.  
  
## Clone a component in a site map  
 To make a copy of an existing component, select the component, and then on the toolbar, select **Clone**.  All details of the cloned component are same as the base component except the ID and title. The ID is generated randomly. 
  
 When you clone an area, the cloned area is added to the right of the currently selected area. When you clone a group, the cloned group is added to the right of the currently selected group. When you clone a subarea, the cloned subarea is added below the currently selected subarea.  
  
## Delete an area, group, or subarea from a site map  
 To delete a site map component, select the component tile, and then on the toolbar, select **Delete**. When you delete an area, all groups and subareas in the area are also deleted. Similarly, when you delete a group, the group and subareas in it are deleted.  
  
## Clients supported  
 The following table explains the clients supported for different site maps.  
 
|Site Maps|Supported Clients|  
|---------------|-----------------------|  
|New apps| Unified Interface |  
|Site map for the Dynamics 365 - custom app | Legacy web app and Dynamics 365 for Outlook |  
|Model-driven apps (Sales, Sales Hub, Customer Service, Customer Service Hub, Field Service, Project Service Automation)| Legacy web app and Unified Interface|  
 
  
### Next steps  
 [Create or edit an app](create-edit-app.md)   
 [Add or edit app components](add-edit-app-components.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]