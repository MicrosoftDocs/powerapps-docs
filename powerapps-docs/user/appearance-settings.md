---
title: Appearance settings for model-driven apps (preview)
description: Learn how to customize the display density of a model-driven app to fit your workflow.
author: jasongre
ms.topic: how-to
ms.date: 09/10/2026
ms.author: jasongre
ms.custom: bap-template
ms.reviewer: smurkute
contributors:
- jasongre
- geniaalbre
---

# Appearance settings for model-driven apps (preview)

[This article is prerelease documentation and is subject to change.]

Model-driven apps include a set of appearance settings that you can use to tailor how the app looks to your workflow. These settings complement the modernization introduced with the [modern, refreshed look](modern-fluent-design.md).

> [!IMPORTANT]
>
> - This feature is in preview.
> - Preview features aren't meant for production use and might have restricted functionality. These features are subject to [supplemental terms of use](https://go.microsoft.com/fwlink/?linkid=2189520). They're available before an official release so that customers can get early access and provide feedback.

You can find appearance settings in the **Appearance** tab of the **Personal settings** panel.

> [!NOTE]
> Appearance settings require the [header and navigation refresh (wave 2)](modern-fluent-design.md#wave-2-header-and-navigation-refresh) to be enabled on the app. If the header and navigation refresh isn't turned on, the **Appearance** tab isn't shown and the app renders at the default appearance.


## Display density

Display density controls how compact or spacious the model-driven app appears. If you process large volumes of data, such as in high-velocity data-entry, field service, or manufacturing scenarios, choose a denser display to see more information on screen at once. If you prefer more breathing room, stay on the default.

### Density levels

Three density levels are available:

| Level | Description |
|------|-------------|
| **Comfortable** | The default spacing that matches the modern, refreshed look. Recommended for most users. |
| **Cozy** | A moderate reduction in vertical and horizontal spacing across the app shell, grids, forms, and controls. |
| **Compact** | The tightest spacing, designed for users who need to maximize the amount of data on screen. |

Density adjusts only the spacing between elements. It doesn't reduce the size of interactive controls, so all density levels continue to meet accessibility requirements for target sizes.

### Set your personal density

Any user can set their own density preference. This preference applies to every model-driven app that has the header and navigation refresh (wave 2) enabled.

1. In a model-driven app, open the **Settings** menu on the app header.
1. Select **Personal settings**.
1. Select the **Appearance** tab.
1. Under **Display density**, select one of the following options:
   - **Auto** uses the default density configured for the app.
   - **Comfortable**, **Cozy**, or **Compact** overrides the app default with your preferred density.

Your preference is saved immediately and applies across your model-driven apps.

### Set a default density for an app or environment

Admins and makers can set a default density so an app or environment matches its intended usage pattern. Unless display density is turned off for an app, users can override the default with their personal preference.

- **Environment default**: An admin sets a default density value that applies to all model-driven apps in the environment.
- **App default**: A maker can override the environment default for a specific app.
- **Personal preference**: A user's explicit density choice overrides the app and environment defaults. If the user selects **Auto**, the app default is used.

The default value for the **Display density** setting is **Comfortable**.

Makers can configure **Display density** in the **Settings** dialog in the app designer. They can also add the **Display density** setting to a solution and edit its value directly for the environment or for individual apps. To learn more about app settings, see [Manage model-driven app settings in the app designer](../maker/model-driven-apps/app-properties.md).

Makers can suppress display density for an app by setting **Display density** to **Off** (enum value `0`). When display density is off:

- The app uses **Comfortable** density.
- The display density options are hidden from users.
- Any stored display density preference for the user is ignored.

### Behavior in controls that don't use spacing tokens

Density is applied to controls that use Fluent spacing tokens. During the rollout of display density, some first-party and third-party controls might not yet use the tokens and will continue to render at their current spacing. This behavior is expected. As more controls use spacing tokens over time, density coverage will expand across the app.


## Related information

- [Modern, refreshed look for model-driven apps](modern-fluent-design.md)
- [Header and navigation refresh (wave 2)](modern-fluent-design.md#wave-2-header-and-navigation-refresh)
