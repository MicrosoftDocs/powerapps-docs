---
title: How to run a model-driven app | MicrosoftDocs
description: "How to run a Power Apps model-driven app"
ms.custom: ""
ms.date: 10/04/2022
ms.reviewer: "matp"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "how-to"
author: "Mattp123"
ms.subservice: mda-maker
ms.author: "matp"
manager: "kvivek"
tags: 
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---
# How to run a model-driven app

## Run an app in a browser

To run a model-driven app in a web browser, the user must have a [security role](../model-driven-apps/model-driven-app-glossary.md#security-role) assigned in addition to having the URL for the app.

Learn how to create a [security role from a copy](../model-driven-apps/share-model-driven-app.md#copy-a-security-role-to-create-a-new-one)

To get the direct link to an app:

1. Go to make.powerapps.com.
1. Select  the **Environment** where the app is located.
1. On the left navigation pane, select **Apps**, or select **Solutions** and open the solution where the app is located.
1. Select the **...** next to the model-driven app, and then select **Edit**. The classic app designer opens.
1. Select the **Properties** tab, and then scroll down to **Unified Interface URL**. Copy the **Unified Interface URL**.

   !["Acquiring the link for a model-driven app"](media/unified-interface-url.png "Acquiring the link for a model-driven app")
1. Paste the app URL in a location so that your users can access it, such as by posting it on a SharePoint site or send via email.

To play the app, enter the URL in a web browser.

## Authentication prompts while running a model-driven app

You may notice authentication prompts during your model-driven app session. These prompts are expected and are required for certain features. Below highlights a list of features that trigger these prompts. This list is subject to change as new features are released: 

- [Custom pages](model-app-page-overview.md).
- [Power Fx](commanding-use-powerfx.md) expressions.
- Opening the Office apps launcher located on the upper left of the app header.
- Selecting the **Add to Teams** button.
- [Collaboration feature](../../user/collaboration.md).

Additionally, some organizational or browser settings may increase the frequency of these prompts. We recommend reviewing your settings to help reduce authentication prompts during sessions.

- **Third party cookies blocked in browser.** This will cause an authentication prompt to trigger each time you open a model-driven app. Note that opening the app in incognito mode or in the Safari web browser via ITP settings will usually block third-party cookies by default. [Enable third party cookies](../../troubleshooting-startup-issues.md) to reduce these prompts.
- **Azure Active Directory conditional access or multi-factor authentication policies**. Policies specifically on Power Apps or Microsoft Graph will trigger additional authentication prompts. Contact your admin to review  your organization's conditional access or MFA policies.

## Run an app on a tablet or phone

Use the app URL described in the earlier section to run a model-driven app on a tablet's web browser. For phones, users download the Power Apps mobile app from the relevant app store. Then, sign into the app, and select the specific app. More information: [Get started with Power Apps mobile](../../mobile/run-powerapps-on-mobile.md)

### See also

[Create and edit columns for Microsoft Dataverse using Power Apps portal](../data-platform/create-edit-field-portal.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
