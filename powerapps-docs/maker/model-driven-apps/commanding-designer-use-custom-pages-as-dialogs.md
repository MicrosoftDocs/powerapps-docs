---
title: "Use commands with custom pages and cloud flows| MicrosoftDocs"
description: "Use the command designer to customize the command bar."
Keywords: command bar, command designer, commanding, modern, dialog, flow
author: caburk
ms.author: caburk
ms.reviewer: matp
manager: kvivek
ms.date: 07/26/2021
ms.service: powerapps
ms.topic: conceptual
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---
# Open custom pages as dialogs and use cloud flows (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

This sample demonstrates how you can build simple custom pages that open as dialogs when a command is clicked. You may also call a cloud flow from the custom page dialog. 

## Prerequisites
- [Add a custom page to your model-driven app](add-page-to-model-app.md)
- Optionally [trigger a cloud flow from the custom page](../../maker/canvas-apps/using-logic-flows.md)

## Create a command

First, you'll need to determine the table and command bar location to place the command.

1. Open the app designer, and then add the desired table to your model-driven app. More information: [Create a model-driven app that has an account table page](create-a-model-driven-app.md)
1. Publish the app.
1. Select the desired table from the **Pages** area in the app designer.
1. Select **...** (ellipsis), and then select **Edit command bar (preview)**.
    > [!div class="mx-imgBorder"]
    > ![App Designer entry point](media/commanddesigner-app-designer-entry-point.png "App Designer entry point")
 
1. Select the location of the command bar you want, and then select **Edit**.
    > [!div class="mx-imgBorder"]
    > ![Select location](media/commanddesigner-command-bar-location-selection.png "Select location")
1. [Open the command designer to edit a command bar](#open-the-command-designer-to-edit-a-command-bar), and then select **+ New** on the command designer command bar.
   :::image type="content" source="media/commanddesigner-new.png" alt-text="Create a new command":::

## Create a JavaScript web resource

> [!NOTE]
> This commanding customization is currently only supported using JavaScript. Currently, Power Fx isn't supported.

1. For the **action**, select **JavaScript**.
1. Select **+ Add library**
1. Select **New** to create a new JavaScript web resource
1. Enter a **Name** and optionally a **Display** name and **Description**.
1. For **Type**, select **Script (JScript)**.
1. Open the **Text editor**.
1. Depending on the type of dialog you wish to use, copy and paste an example from [the Navigate API reference](../../developer/model-driven-apps/clientapi/navigate-to-custom-page-examples.md) .
1. **Save**, and then **publish** the web resource.

## Call the JavaScript from your command

1. Select the library you created in the previous steps.
1. Enter the name of the JavaScript **function**.
    > [!div class="mx-imgBorder"]
    > ![New model-driven app name prompt](/media/CommandDesigner-open-dialog.png "Enter name of JavaScript function")
1. Optionally, add visibility logic.
1. **Save and publish**.

### See also

[Design a custom page for your model-driven app](design-page-for-model-app.md)

[Navigating to and from a custom page using client API](../../developer/model-driven-apps/clientapi/navigate-to-custom-page-examples.md)

[Using PowerFx in custom page](page-powerfx-in-model-app.md)
