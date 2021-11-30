---
title: Change authoring version for Power Apps Studio
description: Learn about how to change the authoring version for Power Apps Studio.
author: emcoope-msft
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 11/15/2021
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

The default version of a Power Apps Studio session is determined by your environment's location and [refresh cadence](/power-platform/admin/create-environment#setting-an-environment-refresh-cadence). This default version of Power Apps Studio changes when an update is released for your environment based on configured refresh cadence.

You can now change the authoring version of your current Power Apps Studio session from the version loaded by default, to an earlier or later version as available for your environment.

> [!IMPORTANT]
> Change the authoring version of a current Power Apps Studio session only when needed, such as to work around an issue as instructed by Microsoft support.

How you check and change the authoring version of your current Power Apps Studio depends on whether you have an app already open, or not.

## Check Power Apps Studio version when an app is open

1. Open an [existing](edit-app.md) or a [new app](data-platform-create-app.md) in Power Apps Studio.

1. Select **Settings**.

    :::image type="content" source="media/studio-versions/select-settings.png" alt-text="Select Settings from the top menu.":::

1. Select **Support** and review your existing Power Apps Studio version for the current session.

    :::image type="content" source="media/studio-versions/authoring-version-edit.png" alt-text="Check authoring version, and choose Edit to change.":::

## Check Power Apps Studio version when an app isn't open

1. Go to create.powerapps.com.

1. Select **Account** from the left pane, and review your existing Power Apps Studio version for the current session.

    :::image type="content" source="media/studio-versions/create-power-apps.png" alt-text="Check version using create.powerapps.com.":::

## Change Power Apps Studio version

1. If you're instructed to change the version of your current Power Apps Studio session, select [Edit](#check-power-apps-studio-version-when-an-app-is-open) or [Change authoring version](#check-power-apps-studio-version-when-an-app-isnt-open), depending on whether you already have an app open in Power Apps Studio, or not.

1. From the list of available authoring versions, choose the version you want, and then select **Reload + apply version**.

    :::image type="content" source="media/studio-versions/change-version-reload.png" alt-text="Change authoring version, and reload Power Apps Studio session.":::

    > [!TIP]
    > The default version for your environment will have **(recommended)** next to the authoring version number.

1. (Optional) Save the app when you're prompted to save the changes if you had an app already open that wasn't saved.

1. Select **Open** or **New** to work with the app inside Power Apps Studio using the version you selected.

You're now editing the app in the Power Apps Studio version you've selected. Since the authoring version change only persists for the current Power Apps Studio session, repeat the above steps when you want to work with the same app again.

## Known limitations and workarounds

- Selecting **Reload + apply version** only changes the current authoring session to the version you choose. This change doesn't persist for future sessions. New Power Apps Studio sessions always start with the default Power Apps Studio version for your environment.
- To update the app with the Power Apps Studio version you selected, you must [save the app](save-publish-app.md#save-changes-to-an-app) with the chosen Power Apps Studio version.
- If you save an app using a version newer than the default for your environment, you might not be able to open that app using the default version of Power Apps Studio. In that case, you'll see the following dialog:

    :::image type="content" source="media/studio-versions/saved-new-version.png" alt-text="Open in new version, or restore previous version.":::

    - Select **Open in new version** to open your app for editing until your environment’s default version gets updated to the app’s current version.

    - Select **Restore previous version** to see all [versions](restore-an-app.md) for the app, and revert to an older version saved with the default Power Apps Studio version associated with your environment.

        > [!NOTE]
        > If you choose to restore the app to a previous version, you'll lose any changes made between your latest and previous app versions.

### See also

- [Setting an environment refresh cadence](/power-platform/admin/create-environment#setting-an-environment-refresh-cadence)
- [Restore a canvas app to a previous version](restore-an-app.md)
- [Get session and app ID details](get-sessionid.md)
