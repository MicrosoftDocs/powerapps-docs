---
title: "Edit a canvas app embedded on a model-driven form | MicrosoftDocs"
description: Learn how to edit an embedded canvas app
ms.custom: ""
ms.date: 06/25/2019
ms.reviewer: ""
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "how-to"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "PowerApps"
author: "Aneesmsft"
ms.author: "matp"
manager: "kvivek"
tags: 
  - "Power Apps maker portal impact"
search.audienceType: 
  - maker
search.app: 
  - "PowerApps"
  - D365CE
---

# Edit a canvas app embedded on a model-driven form

[!INCLUDE [cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

This topic explains how to edit a canvas app embedded on a model-driven form.

## Edit the canvas app directly
You can edit a canvas app embedded on a model-driven form just like any other canvas app. For steps on editing a canvas app see: [Edit a canvas app](../canvas-apps/edit-app.md)

## Edit the canvas app via the host model-driven form
An alternate option is to edit the embedded canvas app via the host model-driven form.

Imagine that you want to edit a canvas app embedded on a form named Account Main Form for the Accounts table. To do this, follow these steps: 

1.	Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).
2.  [Edit the form](create-and-edit-forms.md) named Account Main Form for the Accounts table. 
3.  In the command bar, select **Switch to classic** to open the form in the classic form designer.
4.	In the classic form designer, select the column that is customized to display the embedded canvas app.
5.	With the column selected, on the **Home** tab in the **Edit** group, select **Change Properties**.
6.	On the **Column Properties** dialog box, select the **Controls** tab.
7.	In the **Column Properties** dialog box, in the list of controls select **Canvas app**.
8.	In the section below the controls list, select **Customize** to edit the canvas app. This opens the canvas app for editing, in Power Apps Studio, in a new tab.
	   > [!NOTE]
       > If opening Power Apps Studio is blocked due to a web browser pop-up blocker you must enable the make.powerapps.com site or temporarily disable the pop-up blocker and then select **Customize** again.
9. When you are done making changes, select the **File** tab, and then select **Save**.
10. To make your changes available to end-users select **Publish** and then select **Publish this version**.

## See also
[Embed a canvas app on a model-driven form](embed-canvas-app-in-form.md) <br />
[Add an embedded canvas app on a model-driven form](embedded-canvas-app-add-classic-designer.md) <br />
[Customize the screen size and orientation of a canvas app embedded on a model-driven form](embedded-canvas-app-customize-screen.md) <br />
[Perform predefined actions on the host form from within an embedded canvas app](embedded-canvas-app-actions.md) <br />
[ModelDrivenFormIntegration control's properties and actions](embedded-canvas-app-properties-actions.md) <br />
[Share an embedded canvas app](share-embedded-canvas-app.md) <br />
[Guidelines on working with embedded canvas apps](embedded-canvas-app-guidelines.md) <br />
[Migrating embedded canvas apps on model-driven forms created using the public preview release to latest](embedded-canvas-app-migrate-from-preview.md) <br />


[!INCLUDE[footer-include](../../includes/footer-banner.md)]