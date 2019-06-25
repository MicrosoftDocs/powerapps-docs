---
title: "Migrating embedded canvas apps on model-driven forms from public preview release to latest | MicrosoftDocs"
ms.custom: ""
ms.date: 06/19/2019
ms.reviewer: ""
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "get-started-article"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "PowerApps"
author: "Aneesmsft"
ms.author: "matp"
manager: "kvivek"
tags: 
  - "PowerApps maker portal impact"
search.audienceType: 
  - maker
search.app: 
  - "PowerApps"
  - D365CE
---

# Migrating embedded canvas apps on model-driven forms from public preview release to latest
This topic explains how to migrate embedded canvas apps on model-driven forms from the public preview release to the latest.

> [!IMPORTANT]
> With the latest release, embedded canvas apps on model-driven forms are generally available. Any embedded canvas apps on model-driven forms created using the public preview release should be migrated to new embedded canvas apps created using the latest release.
> Support for embedded canvas apps on model-driven forms from the public preview release will soon be deprecated. 

1. Sign in to [PowerApps](https://web.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).
2. Open the embedded canvas app from public preview release for editing in PowerApps Studio. For steps on editing a canvas app see: [Edit a canvas app](../canvas-apps/edit-app.md).
3. In a new browser tab, follow the steps to [create a new embedded canvas app for a model-driven form](embedded-canvas-app-create.md) using the latest release.
4. Copy the controls from the embedded canvas app from public preview release to the new embedded canvas app, one screen at a time using the steps below.
    1. Select the browser tab from Step 2, that has the embedded canvas app from public preview release open in PowerApps Studio.
    2. Select a screen to copy controls from.
    3. Use **Ctrl + A** to select all controls on the screen.
    4. Use **Ctrl + C** to copy all selected controls.
    5. Select the browser tab from Step 3, that has the new embedded canvas app created using the latest release.
    6. Select a screen or add a new one.
    7. Use **Ctrl + V** to paste the controls.
    8. Repeat the steps to copy each screen.
5. When you are done copying all the screens, select the browser tab from Step 3, that has the new embedded canvas app created using the latest release.
6. Add any missing datasources in the new embedded canvas app.
7. Update all missing references in the new embedded canvas app. 
8. When you are done making changes,  Select the **File** tab, and then select **Save**.
9. To make your changes available to end-users select **Publish** and then select **Publish this version**.

## See also
[Embed a canvas app on a model-driven form](embed-canvas-app-in-form.md) <br />
[Perform predefined actions on the host form from within an embedded canvas app](embedded-canvas-app-actions.md) <br />
[Share an embedded canvas app](share-embedded-canvas-app.md) <br />
[Guidelines on working with embedded canvas apps](embedded-canvas-app-guidelines.md)
