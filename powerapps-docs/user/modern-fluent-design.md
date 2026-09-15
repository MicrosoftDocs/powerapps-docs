---
title: Modern, refreshed look for model-driven apps
description: Learn about the updated user interface that makes model-driven apps easier to use.
author: sriharibs-msft
ms.topic: overview
ms.date: 07/31/2026
ms.service: powerapps
ms.subservice: end-user
ms.author: srihas
ms.custom: bap-template
ms.reviewer: smurkute
ms.assetid: 
search.audienceType: 
  - enduser
contributors:
  - HemantGaur
  - adrianorth
  - jasongre
  - geniaalbre
---

# Modern, refreshed look for model-driven apps

Model-driven apps are modernized in waves. Each wave updates styling, layout, and behavior to align with the latest [Microsoft Fluent design system](https://react.fluentui.dev/?path=/docs/concepts-introduction--page) — making apps easier to use so people can accomplish their goals more quickly. The Fluent design system provides consistency, quality, and Microsoft-wide platform coherence. It also provides a solid foundation for extensibility and future capabilities like dark mode.

> [!IMPORTANT]
> With the **2026 Wave 1** release, all users must use the **New Look** (wave 1 of the modernization arc). Makers can't switch a model-driven app back to the classic look. This requirement doesn't include the **header and navigation refresh (wave 2)**.

## Modernization waves at a glance

| Wave | What it includes | Availability |
|------|------------------|--------------|
| **Wave 1 — The New Look** | Updated styling in forms, views, dashboards, dialogs, and controls; the floating command bar; the Power Apps grid; new field control styling | Generally available. Mandatory as of 2026 Wave 1. |
| **Wave 2 - Header and navigation refresh** | Modern app header, streamlined sitemap, more working space on forms with a sticky condensed header, tightened spacing, updated command bar behavior | Generally available. Opt-in today. |

Future waves continue to build on this foundation.

## Wave 1: The New Look

Here's what you can expect in the New Look experience:

- Updated styling in form, view, and dashboard pages, which includes the use of drop shadows and brighter background colors to create an elevated or _floating_ appearance. The floating appearance helps to visually separate sections and focuses attention on primary content.
- New Fluent-based controls in forms, business process flows, and dialogs. Dialogs now resize height automatically based on the content.
- A new Power Apps grid in place of the read-only grid in view and standard, dashboard pages.
- A new mechanism for customizing the app header colors to match your personal or organizational branding. To learn more, see [Use modern themes](../maker/model-driven-apps/modern-theme-overrides.md).

### Command bar

The _floating_ command bar aligns with the Microsoft 365 experience, with consistent spacing, rounded corners, and elevation. In the following example, the command bar is in a separate section at the top of the page.

:::image type="content" source="media/modern-command-bar.png" alt-text="Floating command bar":::

### View pages

View pages use the new command bar and updated grid areas that take advantage of the elevation changes to help draw the user's attention.

The most significant change on view pages is the switch from the read-only grid to the [Power Apps grid control](../maker/model-driven-apps/the-power-apps-grid-control.md), which features infinite scrolling for a modern, data browsing experience. This grid also appears in subgrids and associated grids in main forms and dashboards. The Power Apps grid control also supports inline editing by using the **Enable filtering** property. Makers can manually configure their editable grids to use the Power Apps grid control.

The following example shows a view page with the modern, refreshed look.

:::image type="content" source="media/modern-view-page.png" alt-text="A view page with the modern, refreshed look.":::

### Form pages

Form pages use the new command bar with refreshed headers, tabs, sections, and business process flows. Quick views, card forms, headers, sitemaps, and timeline controls also feature updated styling.

The following example shows a form page with the modern, refreshed look.

:::image type="content" source="media/modern-form-page.png" alt-text="A form page with the modern, refreshed look.":::

### Field controls

Field controls such as text input, action input, lookup, and check box controls are built and designed by using Fluent components. Future updates will modernize more field controls by using Fluent design.

Field sections, which are containers for the fields on a form, have a more streamlined design. Icons are now on the right side of field labels. Some redundant icons were removed for a cleaner layout. Input and error message styling is also refreshed based on Fluent design.

The following example shows a set of fields with the modern, refreshed look.

:::image type="content" source="media/ModernFields2024April.png" alt-text="Fields in a model-driven app that has the modern, refreshed look.":::

### Dashboard page

The system dashboard page, with independent subgrids and charts, uses the new command bar and has styling similar to the sections in form and view pages. When you turn on the modern experience, or when you use the [monthly channel](../maker/model-driven-apps/channel-overview.md), the system dashboard grids use the new [Power Apps grid control](../maker/model-driven-apps/the-power-apps-grid-control.md). The new grid isn't turned on by default.

:::image type="content" source="media/modern-system-dashboard.png" alt-text="System dashboard page with the modern, refreshed look.":::

### Chart controls

The chart controls on view pages and dashboards are updated to a new color palette for the modern, refreshed look.

If you customize the chart colors, the new look overrides your custom colors. To keep your custom colors, add the **CustomColorOverride** property in the chart .xml file.

```xml
<Chart CustomColorOverride="true">
```

## Wave 2: Header and navigation refresh

The header and navigation refresh (wave 2) builds on the New Look (wave 1) with a redesigned app header, streamlined sitemap, and reworked form layout that gives users more space to focus on their work.

The following image shows the app header and sitemap with the header and navigation refresh enabled.

:::image type="content" source="media/new-header-nav-look-highlight.png" alt-text="Screenshot that shows new look with header and navigation refresh." lightbox="media/new-header-nav-look-highlight.png":::

The following image shows the form header with the header and navigation refresh enabled.

:::image type="content" source="media/modern-fluent-design/form-header.png" alt-text="Screenshot that shows the new form header with the header and navigation refresh." lightbox="media/modern-fluent-design/form-header.png":::

### What's new in the header and navigation refresh

- **Full-width command bar**: The command bar returns to a full-width container at the top of both view and form pages, giving users enough room to surface the most important commands without pushing them into the overflow menu. This behavior replaces the "compact commands" behavior that appeared in earlier previews of this feature.
- **New command ordering**: System commands like **Show As** and **Show Chart** now appear in the third position, after **New** and **Delete**.
- **More working space on forms**: The command bar is now the only element fixed at the top of the page. The summary area and form header scroll off with the rest of the form, giving users more room to work. When the form header scrolls out of view, a **condensed sticky header** attaches below the command bar so the record is always identifiable.
- **More responsive form header**: The form header adapts to different window sizes and content densities.
- **Tighter spacing and margins**: Targeted adjustments across the app improve consistency, readability, and overall page density.

> [!NOTE]
> If you used the preview version of this feature, **compact commands** are no longer available. The command bar is now full-width across both views and forms.

### Enable the header and navigation refresh for an existing app

The header and navigation refresh automatically applies to all apps generated by the [Plan designer](/power-apps/maker/plan-designer/plan-designer). For other existing apps, opt in by following these steps:

1. In the app designer, select **Settings** on the command bar.
2. Select **Features**, and then enable **Header and navigation refresh**.

:::image type="content" source="media/header-refresh-maker.png" alt-text="Screenshot that shows how to enable header and navigation refresh in app designer." lightbox="media/header-refresh-maker.png":::

### Building on the header and navigation refresh (wave 2)

The header and navigation refresh introduces appearance settings that help users customize their experience. For example, users can control the [display density (preview)](appearance-settings.md#display-density) to make the app more compact or more spacious for their workflow. Additional appearance capabilities are planned and documented in [Appearance settings for model-driven apps (preview)](appearance-settings.md).

## Known limitations

The modern, refreshed look for model-driven apps has some limitations:

### Modern, refreshed look outside of browser

The mail app supports the modern, refreshed look. It's on by default for environments on the [monthly channel](../maker/model-driven-apps/channel-overview.md) as part of the February 2026 release, and will be enabled on the semi-annual channel with the October 2026 update.

The mobile app also supports the modern, refreshed look. Admins can enable it by adding the **Mobile modern experience** setting to a solution and updating the value for the environment or for individual apps (2 = on). For step-by-step guidance, see [Enable the modern, refreshed look for model-driven apps on mobile (preview)](../mobile/mobile-new-look.md). To learn more about app settings, see [Manage model-driven app settings in the app designer](../maker/model-driven-apps/app-properties.md).

### Switching themes or enabling dark mode

Switching themes or enabling dark mode isn't supported at this time.

### Honoring classic theming

With the modern, refreshed look, Power Apps no longer honors [classic theme customizations](../maker/model-driven-apps/create-themes-organization-branding.md). You can, however, override the colors for the app header to match your organization branding with the modern, refreshed look. Learn more in [Change the color of the app header](#3-can-i-change-the-color-of-the-app-header). Other theme customization options for the modern, refreshed look aren't available yet.

### Custom icons

Only SVG icons are supported. If you use other formats such as PNG, the navigation doesn't display them and a default icon appears instead.

## Frequently asked questions (FAQs)

### 1. Can I use the modern, refreshed look in the Power Apps component framework or in custom code components?

The modern theme in use is passed to [Power Apps component framework](../developer/component-framework/overview.md) components, so you can [style your components with modern theming](../developer/component-framework/fluent-modern-theming.md).

### 2. Can I use the modern, refreshed look in custom pages?

You can use modern controls with custom pages and the modern, refreshed look. Currently, custom pages don't use the modern theme.

### 3. Can I change the color of the app header?

You can change the color of the app header to match your organization while using the modern, refreshed look. To learn more, see [Use modern themes](../maker/model-driven-apps/modern-theme-overrides.md). Other theme customization options for the modern, refreshed look aren't available yet.

### 4. FAQ for the header and navigation refresh (wave 2)

#### Can I turn on the header and navigation refresh without turning on the New Look?

No. The header and navigation refresh (wave 2) builds on the New Look (Wave 1), so you must enable the New Look to see the header and navigation refresh experience.

#### How do I enable the header and navigation refresh for existing apps?

The header and navigation refresh is an opt-in capability for existing apps. Enable it through the app settings. See [Enable the header and navigation refresh for an existing app](#enable-the-header-and-navigation-refresh-for-an-existing-app).

#### Why don't I see the Help icon in the global command bar in the app header?

The **Settings** pane includes the Help link to documentation.

#### Where is the side pane rail next to the Copilot chat pane?

The side pane switcher becomes available only when there are two or more side panes in the app. When Copilot chat is the only side pane, the switcher is hidden.

#### Why does the sitemap of an app generated by the [Plan designer](/power-apps/maker/plan-designer/plan-designer) look different from existing apps' sitemap?

Apps generated by the [Plan designer](/power-apps/maker/plan-designer/plan-designer) have a streamlined sitemap. Home, Recent, Pinned, and sitemap groups are turned off by default for a simplified flat list of navigation options in the sitemap.

## Revert to the classic look

> [!NOTE]
> Starting with the **2026 Wave 1** release, the **New Look** is mandatory for all users. Makers can no longer switch a model-driven app to the classic look.

Admins can turn off the New Look for all users by updating the **New look for model driven apps** app setting.

1. Open <https://make.powerapps.com/>.
1. Under **Solutions**, open an existing solution with one or more model-driven apps.
1. Select **Add Existing** > **More** > **Setting**.
1. Search for **New look**.
1. Select **New look for model driven apps**.
1. Select **Add** to add it to the solution.
1. Select **New look for model driven apps** from the solution explorer.
1. Update **Setting Environment Value** to **No**.
1. Add the **apps to the solution** for which you want to turn off new look.
1. Update the **value of the apps** to **No**.
1. Select **Save**.
1. Publish all customizations.

To learn more about this and other app settings, see [Manage model-driven app settings in the app designer](../maker/model-driven-apps/app-properties.md).
