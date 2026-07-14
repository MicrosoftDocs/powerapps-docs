---
title: How to run a model-driven app | MicrosoftDocs
description: "How to run a Power Apps model-driven app"
ms.custom: ""
ms.date: 05/06/2025
ms.reviewer: "matp"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "how-to"
author: "Mattp123"
ms.subservice: mda-maker
ms.author: "matp"
contributors: asheehi
tags: 
search.audienceType: 
  - maker
---
# How to run a model-driven app

## Run an app in a browser

To run a model-driven app in a web browser, the user must have a [security role](../model-driven-apps/model-driven-app-glossary.md#security-role) assigned in addition to having the URL for the app.

Learn how to create a [security role from a copy](/power-platform/admin/copy-security-role)

To get the direct link to an app:

1. Go to make.powerapps.com.
1. Select  the **Environment** where the app is located.
1. On the left navigation pane, select **Apps**, or select **Solutions** and open the solution where the app is located. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]
1. Select the **...** next to the model-driven app, and then select **Edit**. The classic app designer opens.
1. Select the **Properties** tab, and then scroll down to **Unified Interface URL**. Copy the **Unified Interface URL**.

   !["Acquiring the link for a model-driven app"](media/unified-interface-url.png "Acquiring the link for a model-driven app")
1. Paste the app URL in a location so that your users can access it, such as by posting it on a SharePoint site or send via email.

To play the app, enter the URL in a web browser.

## Authentication prompts while running a model-driven app

You may notice authentication prompts during your model-driven app session. These prompts are expected and are required for certain features. Below highlights a list of features that trigger these prompts. This list is subject to change as new features are released: 

- [Custom pages](model-app-page-overview.md).
- [Power Fx](commanding-use-powerfx.md) expressions with commands.
- Opening the Office apps launcher located on the upper left of the app header.
- [Collaboration feature](../../user/collaboration.md).

Additionally, some organizational or browser settings may increase the frequency of these prompts. We recommend reviewing your settings to help reduce authentication prompts during sessions.

- **Third party cookies blocked in browser.** This will cause an authentication prompt to trigger each time you open a model-driven app. Note that opening the app in incognito mode or in the Safari web browser via ITP settings will usually block third-party cookies by default. [Enable third party cookies](../../troubleshooting-startup-issues.md) to reduce these prompts.
- **Microsoft Entra conditional access or multi-factor authentication policies**. Policies specifically on Power Apps or Microsoft Graph will trigger additional authentication prompts. Contact your admin to review  your organization's conditional access or MFA policies.

## Run an app on a tablet or phone

Use the app URL described in the earlier section to run a model-driven app on a tablet's web browser. For phones, users download the Power Apps mobile app from the relevant app store. Then, sign into the app, and select the specific app. More information: [Get started with Power Apps mobile](../../mobile/run-powerapps-on-mobile.md)

## View the app description in the browser experience

When a user hovers over the app name at the top of the web browser, the app's description is shown.

:::image type="content" source="media/app-description-browser.png" alt-text="hovering over the app name shows the app description":::

If the app's description was [generated using AI](build-first-model-driven-app.md#create-an-app-description-with-copilot), a disclaimer is shown. Selecting the app name opens the app switcher where the user can play another app that they have access to.

### See also

[Create and edit columns for Microsoft Dataverse using Power Apps portal](../data-platform/create-edit-field-portal.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
