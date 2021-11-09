---
title: Change authoring version for Power Apps Studio
description: Learn about how to change the authoring version for Power Apps Studio.
author: emcoope-msft
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 11/10/2021
ms.subservice: canvas-maker
ms.author: emcoope
search.audienceType: 
  - maker
search.app: 
  - PowerApps
contributors:
  - tapanm-msft
  - emcoope-msft
---

# Change authoring version for Power Apps Studio

The default version of Power Apps Studio session is determined based on your environment's location, [refresh cadence](/power-platform/admin/create-environment#setting-an-environment-refresh-cadence). This default version of Studio changes when an update is released for your environment based on configured refresh cadence.

You can now change the authoring version of your current Studio session to earlier or later versions as available for your environment instead of using the version loaded by default.

> [!IMPORTANT]
> Change the authoring version of current Power Apps Studio session only when needed, such as a workaround for an issue.

## Check and change Studio authoring version

When you find any issue, and if you're instructed by a support team member, you can temporarily change the Studio version you're using.

Depending on how you begin, you can check and change authoring version of your current Studio while having an app already open, or not.

### Check Studio version for open app

1. Open an [existing](edit-app.md) or a [new app](data-platform-create-app.md) in Power Apps Studio.

1. Select **Settings**.

    :::image type="content" source="media/studio-versions/select-settings.png" alt-text="Select Settings from the top-menu.":::

1. Select **Support** and review your existing Studio version for the current session.

    :::image type="content" source="media/studio-versions/authoring-version-edit.png" alt-text="Check authoring version, and choose Edit to change.":::

### Check Studio version when no apps open

1. Go to create.powerapps.com.

1. Select **Account** from the left-pane, and review your existing Studio version for the current session.

    :::image type="content" source="media/studio-versions/create-power-apps.png" alt-text="Check version using create.powerapps.com, and change authoring version.":::

### Change Studio version

1. If you're instructed to change the version of your current Studio session, select [Edit](#check-studio-version-for-open-app) or [Change authoring version](#check-studio-version-when-no-apps-open) depending on whether you already have an app open in Studio or not.

1. From the list of available authoring versions, choose the version you want, and then select **Reload + apply version**.

    :::image type="content" source="media/studio-versions/change-version-reload.png" alt-text="Change authoring version, and reload Studio session.":::

    > [!TIP]
    > The default version for your environment will have **(recommended)** next to the authoring version number.

1. (Optional) Save the app when you're prompted to save the changes if you had an app already open that wasn't saved.

1. Select **Open**, or **New** to work with app inside Studio using the version you selected.

You're now editing the app in the Studio version you've selected. When you exit the current Studio session, to work with apps again, repeat the above steps since the authoring version change only persists for the current Studio session.

## Known limitations and workarounds

- Selecting **Reload + apply version** only changes the current authoring session to the version you choose. This change doesn't persist for future sessions. New Studio sessions always start with the default Studio version for your environment.
- To update the app with the Studio version you selected, you must save the app with the chosen Studio version.
- If you save an app using a version newer than the default for your environment, you may not be able to open that app using the default version of Studio. In that case, you'll see the following dialog.

    :::image type="content" source="media/studio-versions/saved-new-version.png" alt-text="Open in new version, or restore previous version.":::

    - Select **Open in new version** to open your app for editing until your environment’s default
    version gets updated to the app’s current version.

    - Select **Restore previous version** to open the app’s [versions](restore-an-app.md) and revert to an older version of the app saved with the default Studio version associated to your environment.

        > [!NOTE]
        > If you choose to restore the app to a previous version, you'll lose any changes made between your latest and previous app versions.

### See also

- [Setting an environment refresh cadence](/power-platform/admin/create-environment#setting-an-environment-refresh-cadence)
- [Restore a canvas app to a previous version](restore-an-app.md)

