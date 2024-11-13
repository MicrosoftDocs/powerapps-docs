---
title: Modern, refreshed look for model-driven apps
description: Learn about the updated, user interface that makes model-driven apps easier to use.
author: adrianorth
ms.topic: overview
ms.date: 10/10/2024
ms.service: powerapps
ms.subservice: end-user
ms.author: aorth
ms.custom: bap-template
ms.reviewer: smurkute
ms.assetid: 
search.audienceType: 
  - enduser
contributors:
  - HemantGaur
  - adrianorth
  - jasongre
---

# Modern, refreshed look for model-driven apps

Model-driven apps have a modern, refreshed look when the **New look** toggle is turned on. The new look provides updated styling including fonts, colors, borders, shadows, and more that align to the latest [Microsoft Fluent design system](https://react.fluentui.dev/?path=/docs/concepts-introduction--page). The updated look makes model-driven apps easier to use so that users can accomplish their goals quickly and efficiently. The Fluent design system provides consistency, quality, and Microsoft-wide platform coherence. It also provides a solid foundation for extensibility and allows support for dark mode in the future.

> [!IMPORTANT]
> With the [October monthly channel release](/power-platform/released-versions/common-data-service/monthly-2410), the **New Look** toggle as been removed and users will have it be always on. Learn more at [Managing always on rollout](#managing-always-on-rollout). This change was shared in [2024 wave 2 release note](/power-platform/release-plan/2024wave2/power-apps/use-modern-refreshed-look-model-driven-apps) and [October 2024 monthly release note](/power-platform/released-versions/common-data-service/monthly-2410#new-look-always-on).

## What's included with the modern, refreshed look

Here's what you can expect in the modern, refreshed experience:

- Updated styling in form, view, and dashboard pages, which includes the use of drop shadows and brighter background colors to create an elevated or _floating_ appearance. The floating appearance helps to visually separate sections and focuses attention on primary content.
- New Fluent-based controls in forms, business process flows, and dialogs. Dialogs now resize height automatically based on the content.
- A new Power Apps grid in place of the read-only grid in view and standard, dashboard pages.
- A new mechanism for customizing the app header colors to match your personal or organizational branding. More information: [Use modern themes](../maker/model-driven-apps/modern-theme-overrides.md)
- An end user setting called **Try the new look** that turns on the modern, refreshed experience.

:::image type="content" source="media/modern-try-toggle-off.png" alt-text="The 'Try the new look' setting.":::

### Command bar

The _floating_ command bar aligns with the Microsoft 365 experience, with consistent spacing, rounded corners, and elevation. Notice how the command bar is in a separate section at the top of the page in the following example.

:::image type="content" source="media/modern-command-bar.png" alt-text="Floating command bar":::

### View pages

View pages use the new command bar and have updated grid areas that take advantage of the elevation changes to help draw the user's attention.

The most significant change on view pages is the switch from the read-only grid to the [Power Apps grid control](../maker/model-driven-apps/the-power-apps-grid-control.md), which features infinite scrolling for a modern, data browsing experience. This grid also appears in subgrids and associated grids in main forms and dashboards. The Power Apps grid control also supports inline editing using the **Enable filtering** property. Makers can manually configure their editable grids to use the Power Apps grid control.

The following example shows a view page with the modern, refreshed look.

:::image type="content" source="media/modern-view-page.png" alt-text="A view page with the modern, refreshed look.":::

### Form pages

Form pages use the new command bar and have refreshed headers, tabs, sections, and business process flows. Quick views, card forms, headers, sitemaps, and timeline controls also feature updating styling.

The following example shows a form page with the modern, refreshed look.

:::image type="content" source="media/modern-form-page.png" alt-text="A form page with the modern, refreshed look.":::

### Field controls

Field controls such as text input, action input, lookup, and check box controls are built and designed using Fluent components. More field controls are planned to be modernized using Fluent design in future updates.

Field sections, which are containers for the fields on a form, have a more streamlined design. Icons are now on the right side of field labels. Some redundant icons have been removed for a cleaner layout. Input and error message styling is also refreshed based on Fluent design.

The following example shows a set of fields with the modern, refreshed look.

:::image type="content" source="media/ModernFields2024April.png" alt-text="Fields in a model-driven app that has the modern, refreshed look.":::

### Dashboard page

The system dashboard page, with independent subgrids and charts, has been updated to use the new [command bar](#command-bar) and has styling similar to the sections in form and view pages. When the modern experience is turned on, or when using the [monthly channel](../maker/model-driven-apps/channel-overview.md), the system dashboard grids use the new [Power Apps grid control](../maker/model-driven-apps/the-power-apps-grid-control.md). The new grid isn't turned on by default.

:::image type="content" source="media/modern-system-dashboard.png" alt-text="System dashboard page with the modern, refreshed look.":::

### Chart controls

The chart controls on view pages and dashboards have been updated to a new color palette for the modern, refreshed look.

If the chart colors have been customized, the new look overrides the custom colors. The maker can keep the custom colors by adding the **CustomColorOverride** property in the chart .xml file.

```xml
<Chart CustomColorOverride="true">
```

## Known limitations

The modern, refreshed look for model-driven apps has some limitations:

### Modern, refreshed look outside of browser

The mobile app and mail app don't support the modern, refreshed look, and aren't part of the preview or general availability.

### Switching themes or enabling dark mode

Switching themes or enabling dark mode isn't supported at this time.

### Honoring classic theming

With the modern, refreshed look, Power Apps is no longer honoring [classic theme customizations](../maker/model-driven-apps/create-themes-organization-branding.md). You can, however, override the colors for the app header to match your organization branding with the modern, refreshed look. Leaern more in [Change the color of the app header](#can-i-change-the-color-of-the-app-header).  Other theme customization options for the modern, refreshed look aren't available yet.  

### Custom icons

Only SVG icons are supported. If you use other formats such as PNG, the navigation doesn't display them and a default icon appears instead.

## Frequently asked questions (FAQs)

### Can I use the modern, refreshed look in the Power Apps component framework or in custom code components?

The modern theme in use is passed to [Power Apps component framework](../developer/component-framework/overview.md) components allowing you to [style your components with modern theming](../developer/component-framework/fluent-modern-theming.md).

### Can I use the modern, refreshed look in custom pages?

Modern controls can be used with custom pages and the modern, refreshed look. The modern theme isn't currently inherited by custom pages.

### Can I change the color of the app header?

It's possible to change the color of the app header to match your organization while in the modern, refreshed look. See [Use modern themes](../maker/model-driven-apps/modern-theme-overrides.md) for more details. Other theme customization options for the modern, refreshed look aren't available yet.

## Working with the modern, refreshed look

### Provide feedback on the modern, refreshed look

After using the modern, refreshed look in your model-driven apps, tell us what you think about it in the [Power Apps community forum](https://go.microsoft.com/fwlink/?linkid=2221574).

### Managing always on rollout

With the October 2024 monthly release, monthly channel users will no longer see the **New look** toggle in the app header. Those users will have the new look always on. Makers and admins can force users to have the classic look by turning the app setting **New look for model driven apps** to **false**. Learn more at [Revert to the classic look](#revert-to-the-old-ui).

### Revert to the old UI

End users in the semi-annual channel can switch back to the old UI by turning off the **New look** toggle. Makers can also turn off the new look by updating the app setting.

Learn more about turning off the modern, refreshed look, in [Manage model-driven app settings in the app designer](../maker/model-driven-apps/app-properties.md).

Admins can turn off the **New look** setting across all apps in an organization by using the solution explorer to set the **New look for model driven apps** value to **No**. This hides the **New look** toggle and prevents the modern, refreshed look from taking effect.

1. Open <https://make.powerapps.com/>
1. Under Solutions open an existing solution with one or more model-driven apps:
1. Select **Add Existing** > **More** > **Setting**.
1. Search for **New look**.
1. Select **New look for model driven apps**.
1. Select **Add** to add it to the solution.
1. Select **New look for model driven apps** from the solution explorer.
1. Update **Setting Environment Value** to **No**.
1. Select **Save**.
1. Publish all customizations.

    > [!NOTE]
    > If you are using 2023 release wave 2 and want to turn off the new look, update the **Try the new look** setting.

### Enabling the modern look for my app and removing the toggle

In scenarios where makers and admins want to turn on an "Always on" modern experience, they can activate this by setting the **New look always on** app setting. This turns on the modern, refreshed look for all users of the app and remove the header switch ability for end users to turn off **New look**.

Admins can turn on the **New look always on** setting across all apps in an organization by using the solution explorer to set the **New look always on** value to **Yes**. This hides the **New look** toggle and turns on the modern, refreshed look for all users.

1. Open <https://make.powerapps.com/>
1. Under Solutions open an existing solution with one or more model-driven apps:
1. Select **Add Existing** > **More** > **Setting**.
1. Search for **New look always on**.
1. Select **New look always on**.
1. Select **Add** to add it to the solution.
1. Select **New look always on** from the solution explorer.
1. Update **Setting Environment Value** to **Yes**.
1. Select **Save**.
1. Publish all customizations.
