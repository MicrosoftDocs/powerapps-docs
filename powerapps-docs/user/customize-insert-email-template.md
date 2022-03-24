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
# Configure the enhanced insert email template
 
You can configure and enable the enhanced email template for apps across the organization. For a specific app, you can disable this option to display the default email template selection window. 

## Enable the enhanced email template across all apps

To configure the enhanced email template for apps across the organization, perform the following steps:

1. Navigate to **Power Apps** > **Solutions**.
1. Create a new solution. More information: [Understand the email experience](../maker/data-platform/create-solution.md)
1. On the **Solutions** page, go to the solution you created.
1. Select **Add Existing** > **More** > **Setting**.
1. On the Add existing Setting Definition page, select the **Enable the New Insert Template Dialog** option and then select **Next**.
1. Select **Add** on the Selected Setting Definition page. The **Enable the new Insert Template Dialog** option is added to your solution. Select **Edit**.
1. Set the **Setting environment value** option to **Yes** on the Edit Enable the New Insert Template Dialog page.
1. Select **Publish All Customizations**.

## Disable the enhanced email template for an app

To disable the enhanced email template selection window and display the default window for an app, perform the following steps:

1. Navigate to **Power Apps** > **Solutions**.
1. Select the solution created for the email template selection option.
1. Go to **App** > **Model-driven app** and select the app.
1. Select the **Enable the new Insert Template Dialog** option.
1. On the Edit Enable the New Insert Template Dialog page, select the **New app value** option and specify **No** for the specified app.
1. Select **Save** and **Publish All Customizations**.
