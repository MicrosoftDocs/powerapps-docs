---
title: How to run a model-driven app | MicrosoftDocs
description: "How to run a Power Apps model-driven app"
ms.custom: ""
ms.date: 12/07/2021
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

## Run an app on a tablet or phone

Use the app URL described in the earlier section to run a model-driven app on a tablet's web browser. For phones, users download the Power Apps mobile app from the relevant app store. Then, sign into the app, and select the specific app. More information: [Get started with Power Apps mobile](../../mobile/run-powerapps-on-mobile.md)

### See also

[Create and edit columns for Microsoft Dataverse using Power Apps portal](../data-platform/create-edit-field-portal.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
