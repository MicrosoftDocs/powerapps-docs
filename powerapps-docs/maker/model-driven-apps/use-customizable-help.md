---
title: "Enable and use customizable help for model-driven apps"
description: "Learn how to enable and use customizable help with model-driven apps"
keywords: 
ms.date: 03/02/2026
ms.topic: how-to
author: Mattp123
ms.subservice: mda-maker
ms.author: matp
topic-status: Drafting
search.audienceType: 
  - customizer
---
# Enable and use customizable help

Customizable help lets you provide your own contextual information to model-driven app users filling in forms.

> [!NOTE]
> Instead of creating and maintaining your own Help system, custom help panes and guided tasks are available that you can use to author Help that gives your Unified Interface application a custom in-product help experience that is tailored to your organization. More information: [Create guided help for your Unified Interface app](../data-platform/create-custom-help-pages.md)

With model-driven apps, you can replace the default Help with the custom Help of your choice, at the global (environment) level or table level. Custom Help makes the content exposed through the Help links more relevant for your custom or customizable tables. With a single, global URL you can override the out-of-the-box Help links for all customizable tables. Per-table URLs override the out-of-the-box Help links on grids and forms for a specific customizable table. You can include additional parameters in the URL, such as language code and table name. These parameters allow a developer to add functionality to redirect the user to a page that’s relevant to their language or the table context within the application. The table level custom Help settings are solution aware, therefore you can package them as a part of a solution and transport them between environments or distribute them in solutions.

## Set up customizable Help

Customizable Help can be set at the global and table levels.

> [!IMPORTANT]
> You can't use both custom help panes with customizable help at the same time. Enabling one disables the other.

### Set customizable Help at the global level

People with the system administrator security role can use the settings to override default Help at the global level.

1. Sign in the [Power Platform admin center](https://admin.preview.powerplatform.microsoft.com/home). Select Manage, open the environment you want, and then select  **Settings** on the command bar.
1. Expand **Product**, and then select **Features**.
1. Under **Help features**, turn **Custom help for customizable entitites** to **On**.
1. Under **Set custom Help URL**, enter the **Global custom Help URL** to your custom Help.
   - **Append Parameters to URL**. Select **Yes** to allow for parameters such as language code or table name to be appended to the **Help URL** that you specify in the table definition. More information: [Append parameters to URL](#append-parameters-to-url)  

1. Select **Save**.

### Set customizable Help for a specific table

After you enable custom Help at the global level, system customizers can override the global Help URL for a table in the table definition.

1. Sign in to [Power Apps](https://make.powerapps.com).
1. Go to **Tables**, and then open the table you want.
1. Select **Properties**, and expand **Advanced options**.
1. In the **For this table** area, in the **Help URL** box enter the URL of your custom Help page.

#### Append parameters to URL

As described previously, to allow for the appending of parameters to the **Help URL** for the table definition, set **Append Parameters to URL** in the **System Settings** > **General** tab to **Yes**.

Examples of the parameters that can be appended to the URL:

- User Language Code: userlcid
- Table Name: table
- Entry Point: hierarchy chart or form
- Form ID: formid

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
