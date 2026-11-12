---
title: Enable the modern, refreshed look for model-driven apps on mobile (preview)
description: Learn how to enable the modern, refreshed look and dynamic font scaling for model-driven apps in Power Apps mobile.
author: yogeshgupta698
ai-usage: ai-generated
ms.service: powerapps
ms.topic: how-to
ms.custom: mobile
ms.date: 11/12/2026
ms.subservice: mobile
ms.author: yogupt
ms.reviewer: smurkute
search.audienceType:
  - admin
  - maker
---

# Enable the modern, refreshed look for model-driven apps on mobile (preview)

[This article is prerelease documentation and is subject to change.]

Power Apps mobile supports the modern, refreshed look for model-driven apps. This experience brings fluent-based styling to supported forms, views, dashboards, dialogs, controls, and commands in model-driven apps on mobile devices.

> [!IMPORTANT]
>
> - This is a preview feature.
> - Preview features aren't meant for production use and might have restricted functionality. These features are subject to [supplemental terms of use](https://go.microsoft.com/fwlink/?linkid=2189520). They're available before an official release so that customers can get early access and provide feedback.

An administrator can enable the experience for all eligible model-driven apps in an environment or for individual apps by configuring the **Mobile modern experience** solution setting.

> [!IMPORTANT]
> **Mobile modern experience** is different from **New look for model-driven apps**. The New Look is mandatory for model-driven apps in a web browser as of 2026 release wave 1. To use the refreshed look in Power Apps mobile during preview, an administrator must also configure **Mobile modern experience**.

## App settings

The mobile experience has two related but independent app settings.

| Setting | Purpose | Required for the mobile new look |
|---|---|---|
| **Mobile modern experience** | Enables the modern, refreshed look in Power Apps mobile. Set the value to `2` to turn it on. | Yes |
| **Enable mobile dynamic font** | Scales text based on the text-size setting on the user's iOS or Android device. | No |

Turning on **Mobile modern experience** doesn't automatically turn on dynamic font scaling. Configure **Enable mobile dynamic font** separately when you want the app to respond to the device's text-size setting.

## Prerequisites

- A model-driven app that users can run in Power Apps mobile.
- Permission to work with solutions and publish app customizations.
- The app's **Primary mobile player** setting set to **Power Apps mobile**. Learn more in [Manage model-driven app settings in the app designer](../maker/model-driven-apps/app-properties.md).
- The latest available version of Power Apps mobile on each test device.

## Enable the new look for an environment

Use an environment value to enable the modern, refreshed look for eligible model-driven apps in the environment.

1. Sign in to [Power Apps](https://make.powerapps.com), and then select the environment that contains your apps.
1. In the navigation pane, select **Solutions**, and then open an unmanaged solution. You can also create a solution for the setting.
1. On the command bar, select **Add existing** > **More** > **Setting**.
1. Search for and select **Mobile modern experience**.
1. Select **Next**, select **Include setting definition**, and then select **Add**.
1. In the solution, select the added **Mobile modern experience**.
1. In the **Edit setting value** pane, under **Setting environment value**, select **New value**.
1. Enter `2`, and then select **Save**.

The environment value applies to eligible apps that don't have an app-specific value.

## Enable or override the new look for one app

Use an app value to enable the experience for one model-driven app or to override the environment value.

1. Add the model-driven app and the **Mobile modern experience** setting to the same unmanaged solution.
1. In the solution, select **Mobile modern experience**.
1. In the **Edit setting value** pane, under **Setting app values**, find the model-driven app.
1. Enter `2`, and then select **Save**.
1. Republish the model-driven app.

Power Apps determines the effective value in the following order:

1. Setting app value.
1. Setting environment value.
1. Default value in the setting definition.

## Enable dynamic font scaling

Dynamic font scaling is optional and isn't a prerequisite for the mobile new look. When you enable it, text in supported areas responds to the text-size setting on the user's iOS or Android device.

1. Open the model-driven app in the app designer.
1. On the command bar, select **Settings**, and then select **Features**.
1. Turn on **Enable mobile dynamic font**.
1. Select **Save**, and then publish the app.

### Supported text sizes

> [!IMPORTANT]
> In this preview, dynamic font scaling supports text sizes up to **135% of the default text size** (1.35 times the default) on both Android and iOS. Larger text sizes aren't supported. They can cause content to overlap or appear truncated and make controls difficult to use. This limit is a Power Apps mobile support limit, not an operating-system maximum or an automatic cap on the size the app renders.

Both operating systems offer text sizes beyond this supported range, including accessibility settings. On iOS, **Larger Accessibility Sizes** provides additional sizes beyond the standard text-size slider. Android's available sizes depend on the device and operating-system version. For device settings, see [Change the font size on your iPhone, iPad, and iPod touch](https://support.apple.com/en-us/102453) and [Android font scaling](https://developer.android.com/about/versions/14/features#non-linear-font-scaling).

Dynamic font scaling changes text size; it isn't a browser zoom or device display-zoom setting. Test the app at the default text size and at larger sizes within the supported range on both iOS and Android. Pay particular attention to grids, quick-create forms, dialogs, commands, and custom components. Don't assume that the device's largest available text size is supported by this preview.

## Review grid configuration

To use dynamic font scaling in mobile grids, configure the **Power Apps grid control**. Migrate legacy read-only and editable grids where font scaling is required. Turning on **Mobile modern experience** or **Enable mobile dynamic font** doesn't automatically replace all grid configurations in the app.

1. Review the table views, form subgrids, and dashboard grids used by the app on phones and tablets.
1. For table views that use a legacy grid, add and configure the Power Apps grid control for the table. Table-level configuration applies to the table's views, review form subgrids and dashboard grids separately.
1. For each form subgrid that needs font scaling, add and configure the Power Apps grid control on the form. Verify that the mobile clients you support use the configured control.
1. Review **Reflow behavior**. **Reflow** switches between a table and a list based on the available width; **List only** always displays a list. Test the selected layout and the configured **Number of columns for list view** at larger supported text sizes.
1. Save and publish the affected table and form customizations, and publish the app after changing its settings.

For table and subgrid setup steps, see [Power Apps grid control](../maker/model-driven-apps/the-power-apps-grid-control.md). Grid migration can change behavior as well as appearance. For example, sorting, **Select all**, and **Clear all** aren't available in the card list view. Review [Limitations with card form lists](../maker/model-driven-apps/the-power-apps-grid-control.md#limitations-with-card-form-lists) before changing an existing grid.

Test selecting, editing, and opening rows, available sorting and filtering actions, and the space used by empty and populated subgrids in Power Apps mobile. Enabling font scaling doesn't remove the grid control's existing limitations.

## Verify the mobile experience

1. Open Power Apps mobile on a test device.
1. Refresh the app list, and then open the model-driven app.
1. Verify the refreshed styling on the app's primary forms, views, dashboards, dialogs, and controls.
1. Test navigation, commands, grids, quick-create forms, and custom components.
1. If you enabled dynamic font scaling, change the device text size within the [supported range](#supported-text-sizes) and verify that supported text scales without overlapping or hiding controls.
1. If the app is available offline, also test its primary scenarios while the device is offline.

The settings change the presentation of the app. They don't change its Dataverse data, forms, views, or security model.

## Known limitations

- This mobile experience is a preview feature.
- Dynamic font scaling has a [supported text-size limit](#supported-text-sizes) on both Android and iOS, even when the device offers larger accessibility sizes.
- Grids require [separate configuration](#review-grid-configuration) to use the Power Apps grid control for font scaling. The app settings don't migrate legacy grids.
- Dark mode and switching themes aren't supported.
- Classic theme customizations aren't honored by the modern, refreshed look.
- Only SVG custom icons are supported. Other image formats might display a default icon.
- Custom pages don't currently inherit the modern theme.
- **Header and navigation refresh** is a separate preview experience. Mobile support for that preview isn't currently documented.

## See also

- [Modern, refreshed look for model-driven apps](../user/modern-fluent-design.md)
- [Use model-driven apps in the Power Apps mobile app](use-custom-model-driven-app-on-mobile.md)
- [Use settings to provide customized app experiences](../maker/data-platform/create-edit-configure-settings.md)
- [Manage model-driven app settings in the app designer](../maker/model-driven-apps/app-properties.md)
