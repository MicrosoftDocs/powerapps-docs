---
title: "Configure the enhanced insert email template selection window | MicrosoftDocs"
description: "Configure the email template selection window at the org level or app."
ms.custom: ""
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
# Enable the enhanced insert email template selection dialog
 
You can configure and enable the enhanced email template for apps across the organization. For a specific app, you can disable this option to display the default email template selection window. 

## Enable the enhanced email template across all apps

To configure the enhanced email template for apps across the organization, perform the following steps:

1. Go to [Power Apps](https://make.preview.powerapps.com/) instance and select the environment in which you you want to configure the template.
2. Select **Solutions**.
3. On the **Solutions** page, select the solution in which you want to configure the template.
   > [!NOTE]
   > Don't select the default solution to configure the template.
4. Select **Add Existing** > **More** > **Setting**.
   > ![Add a setting to a solution](media/email_template_dialog_add.png)
1. On the **Add existing Setting Definition**, select the **Enable the New Insert Template Dialog** option and then select **Next**.
   > ![Add the email template dialog option](media/new_email_template_option.png)
1. Select **Add** on the **Selected Setting Definition**. The **Enable the New Insert Template Dialog** option is added to your solution. Select **Edit**.
1. Set the **Setting environment value** option to **Yes** on the **Edit Enable the New Insert Template Dialog**.
   > ![Set the option to yes across the apps ](media/new_email_template_envvar.png)
1. Select **Publish All Customizations**.

## Disable the enhanced email template for an app

To disable the enhanced email template selection window and display the default email template for an app, perform the following steps:

1. Go to Power Apps instance.
2. Select **Solutions**.
1. Select the solution created for the email template selection option.
1. Go to **Add Existing** > **App** > **Model-driven app** and select the app.
   > ![Add a model driven app](media/new_email_template_addcsw.png)
1. Select the **Enable the new Insert Template Dialog** option.
1. On the **Edit Enable the New Insert Template Dialog**, in the **Setting app value** section, specify **No** for the specified app.
   > ![Set the environment variable to No for an app](media/new_email_template_deloptn.png)
1. Select **Save** and **Publish All Customizations**.

### See also

[Set up enhanced email](/power-platform/admin/system-settings-dialog-box-email-tab)<br>
[Understand the email experience](view-create-email.md)                                                    

[!INCLUDE[footer-include](../includes/footer-banner.md)]
