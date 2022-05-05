---
title: How to enable the enhanced email template in Power Apps
description: Turn on the enhanced email template option in Power Apps.
author: gandhamm
manager: shujoshi
ms.topic: task
ms.date: 05/06/2022
ms.subservice: end-user
ms.author: mgandham
search.audienceType: 
  - enduser
search.app: 
  - PowerApps
  - D365CE
---

# Enable the enhanced email template editor page

Turn on the enhanced email template editing experience in apps across your organization. If you need to, you can turn off the enhanced email template page for a specific app. Users of that app see the default email template editor page.

## Enable the enhanced email template editor across all apps

1. In [Power Apps](https://make.preview.powerapps.com/) select the environment the environment that contains your solution.
2. Select **Solutions**, and then select the solution in which you want to turn on the enhanced template editing experience.
   > [!NOTE]
   > Don't select the default solution to configure the template.
4. Select **Add Existing** > **More** > **Setting**.

   > ![Add a setting to a solution](media/usr_soln_setting.png)
1. On the **Add existing Setting Definition** pane, select the **Enable the New Email Template Editor** option and then select **Next**.
   > ![Add the enable email template editor option](media/usr_soln_email_setting.png)
1. Select **Add** on the **Selected Setting Definition** to add the **Enable the New Email Template Editor** option to your solution. 
1. Select the **Enable the New Email Template Editor** option. The **Edit Enable the New Email Template Editor** pane appears.
1. Set the **Setting environment value** option to **Yes** on the **Edit Enable the New Email Template Editor** pane.
   > ![Set the variable to yes](media/enable-email-template-option.png)
1. Select **Publish All Customizations**.

## Disable the enhanced email template for an app


To force app to display the default email template editor page, turn off the enhanced template editing experience in that app. First, you'll need to add the app to the solution to which you've added the enhanced email template editing experience.

1. In [Power Apps](https://make.preview.powerapps.com/), select **Solutions**, and then select the solution to which you've added the enhanced email template editing experience.
2. Select **Solutions**.
1. On the **Solutions** page, select the Solution in which you've added the the email template selection option.
1. Go to **Add Existing** > **App** > **Model-driven app**> **Add existing model-driven apps** pane. Select the app for which you want to disable the enhanced insert email template selection page. The app is added to the solution. 
   > ![Add an app to an existing solution](media/disable-add-app.png)
1. Select the **Enable the New Email Template Editor** option in the solution.
1. On the **Edit Enable the New Email Template Editor**, in the **Setting app value** section, the selected app is displayed. 
1. Select **New app value** for the app, and select **No** for the specified app.
   > ![Disable the variable](media/enh_disable_app.png)
1. Select **Save** and **Publish All Customizations**.

After you publish the customizations, the app uses the default email template editor.

### See also

[How to create an email template  in model-driven apps](email-template-create.md)  
[Customize an email template using the template editor](cs-template-options.md)

[!INCLUDE[footer-include](../includes/footer-banner.md)]
