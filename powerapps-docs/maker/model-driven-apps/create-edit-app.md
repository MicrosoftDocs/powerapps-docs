---
title: "Create or edit a model-driven app using the app designer in PowerApps | MicrosoftDocs"
description: "Learn how to create or edit apps using the app designer"
keywords: ""
ms.date: 05/23/2018
ms.service: crm-online
ms.custom: 
ms.topic: article
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "powerapps"
author: "Mattp123"
ms.assetid: 2a44229e-44f0-4c4e-ba21-a476210d0a12
ms.author: "matp"
manager: "kvivek"
ms.reviewer: 
ms.suite: 
ms.tgt_pltfrm: 
caps.latest.revision: 19
topic-status: Drafting
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---

# Tutorial: Create a model-driven app by using the app designer

In this tutorial you learn the basics of how to create and edit a model-driven app by using the tile-based app designer.

## Prerequisites
Verify the following prerequisites before you start creating an app:
- A PowerApps environment. More information: [Create an environment](https://docs.microsoft.com/powerapps/administrator/create-environment)
- System administrator or system customizer security role. More information: [About predefined security roles](https://docs.microsoft.com/powerapps/maker/model-driven-apps/share-model-driven-app#about-predefined-security-roles)
 
<a name="createApp"></a>   
## Create an app  

1.  On the [PowerApps](https://web.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) site, select **Model-driven** (lower left of the navigation pane).  

    ![Model-driven design mode](media/model-driven-switch.png)

    > [!IMPORTANT]
    > “If the **Model-driven** design mode isn't available, you may need to [Create an environment](https://docs.microsoft.com/powerapps/administrator/create-environment). 

2. Select **Apps**, and then select **Create an app**.

3. On the **Create a New App** page, enter the following details: 

    - **Name**: Enter a name for the app.  
  
    - **Unique Name**: The unique name is automatically populated based on the app name that you specify. It is prefixed with a publisher prefix. You can change the part of the unique name that's editable. The unique name can only contain English characters and numbers.  
  
        > [!NOTE]
        >  The publisher prefix is the text that's added to any entity or field created for a solution that has this publisher.   
  
    - **Description**: Type a short description of what the app is or does.  
  
    - **Icon**: By default, the **Use Default App** thumbnail check box is checked. To select a different web resource as an icon for the app, clear the check box, and then select an icon from the drop-down list. This icon will be displayed on the preview tile of the app.  
  
    - Select the client type that the app will be used for.  
  
        - **Unified Interface**: This is the newer responsive web browser client that has a similar interface across PC and mobile devices.  

        - **Web**: This is the classic Dynamics 365 customer engagement web browser client.  
    
    - **App URL Suffix**: The app URL is automatically populated based on the app name that you specify. You'll see a preview of how the complete URL looks. The app URL must be unique.  
  
         For example: https://\<org>.crm#.dynamics.com/Apps/\<App URL>

         For on-premises: http://\<server>/\<org name>/Apps/\<App URL> 
  
      > [!NOTE]
      >  If you clear the **App URL Suffix** field and then save the app, the app URL will be automatically generated with the app ID.  
  
    - **Use existing solution to create the App**: Select this option to create the app from a list of installed solutions. When you select this option, **Done** switches to **Next** on the header. If you select **Next**, the **Create app from existing solution** page opens. From the **Select Solution** drop-down list, select a solution from which you want to create the app. If any site map is available for the selected solution, the **Select Sitemap** drop-down list will appear. Select the site map, and then select **Done**.

      > [!NOTE]
      > By selecting **Default Solution** when you add a site map, the components that are associated with that site map are automatically added to the app.  

      ![Use existing solution to create the app page](media/use-existing-solution-to-create-the-app.png "Use an existing solution to create the app") 

    - **Choose a welcome page**: This option allows you to select from the web resources available in your organization. The welcome pages you create can contain information that's useful to users, such as links to videos, upgrade instructions, or getting started information. The welcome page is displayed when an app is opened. Users can select **Do not show this Welcome Screen next time** on the welcome page to disable the page so it doesn’t appear the next time the app starts. More information about how to create a web resource, such as an HTML file that you can use as a welcome page: [Create and edit web resources to extend the web application](create-edit-web-resources.md)  
      
    To edit app properties later, go to the **Properties** tab in the app designer. More information: [Manage app properties](manage-app-properties.md)  
  
     > [!NOTE]
     >  You can't change the unique name and app URL suffix on the **Properties** tab.  
  
4. Select **Done** or&mdash;if you selected **Use an existing solution to create the App**&mdash;select **Next** to select from the available solutions that were imported in the organization.  
  
    A new app is created and is shown in Draft status. You'll see the app designer canvas for the new app. From there you can add components, such as entities, views, and dashboards to make your app useful. More information: [Add or edit app components](add-edit-app-components.md)  
   
<a name="editApp"></a>   
## Edit an app  
  
1.  On the [PowerApps](https://web.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) site, select **Model-driven** (lower left of the navigation pane).  

> [!IMPORTANT]
> “If the **Model-driven** design mode isn't available, you may need to [Create an environment](https://docs.microsoft.com/powerapps/administrator/create-environment). 

2. On the left navigation pane select **Apps**, select an app, and then on the toolbar select **Edit**.   

3. In the app designer add or edit components to the app, as required. More information: [Add or edit app components](add-edit-app-components.md)  
 
  
### Next steps  
 [Add or edit app components](add-edit-app-components.md)   


