---
title: Enable the modern, refreshed look for model-driven apps on mobile (preview)
description: Learn how to enable the modern, refreshed look and dynamic font scaling for model-driven apps in Power Apps mobile.
author: yogeshgupta698
ms.service: powerapps
ms.topic: how-to
ms.custom: mobile
ms.date: 08/10/2026
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

Test the app with the supported text-size and display-scaling options on both iOS and Android. Pay particular attention to grids, quick-create forms, dialogs, commands, and custom components at larger accessibility sizes.

## Review grid configuration

The modern, refreshed look uses the Power Apps grid on supported view pages. If the app has manually configured editable grids or dashboard grids, review those configurations and use the Power Apps grid where you want the modern grid experience. Enabling **Mobile modern experience** doesn't replace every grid configuration in the app.

Test sorting, filtering, selecting, editing, and opening rows in Power Apps mobile. For configuration details and supported capabilities, see [Power Apps grid control](../maker/model-driven-apps/the-power-apps-grid-control.md).

## Verify the mobile experience

1. Open Power Apps mobile on a test device.
1. Refresh the app list, and then open the model-driven app.
1. Verify the refreshed styling on the app's primary forms, views, dashboards, dialogs, and controls.
1. Test navigation, commands, grids, quick-create forms, and custom components.
1. If you enabled dynamic font scaling, change the device text size and verify that supported text scales without overlapping or hiding controls.
1. If the app is available offline, also test its primary scenarios while the device is offline.

The settings change the presentation of the app. They don't change its Dataverse data, forms, views, or security model.

## Known limitations

- This mobile experience is a preview feature.
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
