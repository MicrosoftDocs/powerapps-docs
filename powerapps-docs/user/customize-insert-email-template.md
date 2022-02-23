---
title: "Configure the enhanced insert email template selection window | MicrosoftDocs"
description: "Configure the email template selection window at the org level or app."
ms.custom: ""
author: gandhamm
manager: shujoshi

ms.topic: task
ms.date: 06/30/2021
ms.subservice: end-user
ms.author: mgandham
search.audienceType: 
  - enduser
search.app: 
  - PowerApps
  - D365CE
---
# Configure the new insert email template

The new email template selection window enables users to:

 - filter templates based on standard and customized attributes
 - switch between list, tile, and grid views
 - search for out-of-the-box and custom templates by title, subject, description, or content of the template
 - zoom in to view templates in a new window. You can also navigate between templates.
 - Modify the content for a selected template
 
You can configure and enable the new email template for apps across the organization.  For a specific app, you can disable this option to display the default email template selection window. 

## Enable the new email template across all apps

To configure the new email template for apps across the organization, perform the following steps:

1. Navigate to **Power Apps** > **Solutions**.

1. Create a new solution. See [Understand the email experience](../maker/data-platform/create-solution.md)

1. On the **Solutions** page, go to the solution you created.

1. Select **Add Existing > More dropdown > Setting**.
 
1. On the Add existing Setting Definition page, select the **Enable the New Insert Template Dialog** option and select **Next**.

1. Select **Add** on the Selected Setting Definition page. The **Enable the new Insert Template Dialog** option is added to your solution. Click **Edit**.

1. Set the **Setting environment value** option to Yes on the The Edit Enable the New Insert Template Dialog page.

1. Select **Publish All Customizations**.

## Disable the new email template for an app

To disable the new email template selection window and display the default window, perform the following options:

1. Navigate to **Power Apps** > **Solutions**.
1. 
1. Select the solution created for the email template selection option.
1. 
1. Select **App > Model-driven app**.
1. 
1. Select the app to disable the option.
1. 
1. Select **Enable the new Insert Template Dialog** option.
1. 
1. On the Edit Enable the New Insert Template Dialog page, select the New app value option for the specified app.
1. 
1. Specify No and click Save.
1.  
1. Select **Publish All Customizations**.
