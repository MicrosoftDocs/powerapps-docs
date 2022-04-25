---
title: How to enable the enhanced email template  in Power Apps
description:Enable the enhancd email template option in Power Apps
author: mgandham
manager: shujoshi

ms.component: pa-user
ms.topic: conceptual
ms.date: 6/30/2021
ms.subservice: end-user
ms.author: gandhamm
ms.custom: ""
ms.reviewer: ""
ms.assetid: 
search.audienceType: 
  - enduser
search.app: 
  - PowerApps
  - D365CE
---

# Enable the enhanced email template editor page
 
You can configure and enable the enhanced email template editor for apps across the organization. You can disable the enhanced email template page for a specific app. The app displays the default email template editor page if you disable this option.

## Enable the enhanced email template editor across all apps

To configure the enhanced email template for apps across the organization, perform the following steps:

1. Go to **Power Apps** instance and select the environment in which you you want to configure the template.
2. Select **Solutions**.
3. On the **Solutions** page, select the solution in which you want to configure the template.
   > [!NOTE]
   > Don't select the default solution to configure the template.
4. Select **Add Existing** > **More** > **Setting**.
5. On the **Add existing Setting Definition** pane, select the **Enable the New Email Template Editor** option and then select **Next**.
6. Select **Add** on the **Selected Setting Definition**. The **Enable the New Email Template Editor** option is added to your solution. 
7. Select the **Enable the New Email Template Editor** option. The **Edit Enable the New Email Template Editor** pane appears.
8. Set the **Setting environment value** option to **Yes** on the **Edit Enable the New Email Template Editor** pane.
9. Select **Publish All Customizations**.

## Disable the enhanced email template for an app

For an app to display the default email template editor page, you must disable the enhanced email template selection option. To disable the option for a specific app, you must add the app to the Solution in which you've added the the email template editor selection option. Perform the following steps:

1. Go to **Power Apps** instance.
2. Select **Solutions**.
1. On the **Solutions** page, select the Solution in which you've added the the email template selection option.
1. Go to **Add Existing** > **App** > **Model-driven app**> **Add existing model-driven apps** pane. Select the app for which you want to disable the enhanced insert email template selection page. The app is added to the solution. 
1. Select the **Enable the New Email Template Editor** option in the solution.
1. On the **Edit Enable the New Email Template Editor**, in the **Setting app value** section, the selected app is displayed. 
2. Select **New app value** for the app, and select **No** for the specified app. 
4. Select **Save** and **Publish All Customizations**.

### Example

To disable the enhanced email template editor page in the Customer Service Workspace app, perform the following steps:

1. Select the Solution where you've enabled the **Enable the New Email Template Editor** option.
2.  Add the Customer Service Workspace app to the Solution. Go to **Add Existing** > **App** > **Model-driven app**>**Add existing model-driven apps** and select the Customer Service Workspace app.
3.  Select the **Enable the New Email Template Editor** option. 
4.  On the **EEnable the New Email Template Editor** pane, the Customer Service Workspace option is displayed. 
5.  Select **New app value** and then select **No**. 
Once you publish the customizations, the Customer Service Workspace app displays the default email template editor page.


### See also

[How to create an email template  in model-driven apps](email-template-create.md)  
[Customize an email template using the template editor](cs-template-options.md)


[!INCLUDE[footer-include](../includes/footer-banner.md)]
