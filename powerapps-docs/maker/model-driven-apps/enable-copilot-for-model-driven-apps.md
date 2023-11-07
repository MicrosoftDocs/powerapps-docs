---
title: Enable Copilot for app users in model driven apps
description: Learn how to enable Power Apps Copilot in model driven apps for end users
Keywords: Power Apps, model driven apps, Copilot
author: makolomi
applies_to: 
  - "Dynamics 365 (online)"
  - "powerapps"
  - "Copilot"
ms.subservice: mda-maker
ms.author: makolomi
ms.reviewer: 
ms.date: 06/11/2023
ms.topic: how-to
ms.assetid: 
search.audienceType: 
  - maker
---
[This topic is pre-release documentation and is subject to change.]

Copilot for app users in model-driven apps is a next-generation AI assistant that provides data insights on Dataverse tables through natural language conversation. Copilot helps app users boost productivity through AI-powered insights and intuitive app navigation. More information:[Copilot for app users in model-driven apps](https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/add-ai-copilot).

# Enable Copilot for end users in model driven apps
Makers who are Environmental Administators can enable Copilot in model-driven apps for all the users in their environments in [Power Platform admin center](https://admin.powerplatform.microsoft.com).

1. Sign in to the Power Platform admin center at https://admin.powerplatform.microsoft.com.

2. In the navigation pane, go to **Environments** and select the enviornment where you want to enable Copilot for app users in model-driven apps in. Click on "**Settinngs** for this environment in the top menu.

  > [!div class="mx-imgBorder"]
  > ![Select environment Settings.](media/Environment_settings.png)
 
3. In **Settings** for the seleceted environment, navigate to **Product** section and select **Features** option.

  > [!div class="mx-imgBorder"]
  > ![Select Copilot feature for the environment.](media/Environment_features.png)

4. In **Features** section, set the value for **Allow users to analyze data using an AI-powered chat experience in canvas and model-driven apps** to **On** in the dropdown control.
   
  > [!div class="mx-imgBorder"]
  > ![Set Copilot feature ON for the envrironment](media/Copilot_for_apps_users_ON.png)

 
5. Go back to **Product** section and select **Behavior** option.  Set **Release channel** for model-driven apps to **Monthly channel** in the dropdown control. More information: [Behavior settings](/power-platform/admin/settings-behavior#settings) and [Changing release channels for model-driven apps](channel-change.md).
   
  > [!div class="mx-imgBorder"]
  > ![Set Release channel to Monthly channel for model driven apps](media/Behavior_release_channel.png)
   
6. Configure Dataverse tables that you want Copilot to use for the reponses. You must select both the tables and the columns of importance for Copilot to search accross to produce quality data inisghts. More information: [Configure tables to use Copilot](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/table-settings-for-copilot)

- Go to  table **Properties > Advanced options** and enable **Track Changes** and **Appear in search results** settings for Dataverse tables to be used by Copilot. Note that most standard Dataverse tables have these settings enabled by default, but custom tables require them to be set manually. More information: [Enable table indexing](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/table-settings-for-copilot#enable-indexing)
- Select which columns from these tables  to be


## See also

[FAQ for Copilot in model-driven apps](../common/faqs-copilot-model-driven-app.md) <br />
[Responsible AI FAQs for Power Apps](../common/responsible-ai-overview.md) <br />
[Add Copilot control to a canvas app (preview)](../canvas-apps/add-ai-copilot.md)
