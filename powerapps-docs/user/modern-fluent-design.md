---
title: Modern, refreshed look for model-driven apps
description: Learn about the updated, user interface that makes model-driven apps easier to use.
author: chmoncay
ms.topic: overview
ms.date: 02/07/2024
ms.service: powerapps
ms.subservice: end-user
ms.author: chmoncay
ms.custom: bap-template
ms.reviewer: sericks
ms.assetid: 
search.audienceType: 
  - enduser
contributors:
  - HemantGaur
  - adrianorth
  - jasongre

---

# Modern, refreshed look for model-driven apps

Model-driven apps have a modern, refreshed look when the **Try the new look** feature is [turned on by end users](modern-fluent-design.md#turn-on-the-modern-refreshed-look). The new look provides updated styling including fonts, colors, borders, shadows, and more that align to the latest [Microsoft Fluent design system](https://react.fluentui.dev/?path=/docs/concepts-introduction--page). The updated look makes model-driven apps easier to use so that users can accomplish their goals quickly and efficiently. The Fluent design system provides consistency, quality, and Microsoft-wide platform coherence. It also provides a solid foundation for extensibility and allows support for dark mode in the future.

The modern, refreshed look feature that's now on by default will roll out on a slower schedule than other features. More information: [Managing on by default general availability rollout](modern-fluent-design.md#managing-on-by-default-general-availability-rollout).

## What's included with the modern, refreshed look

Here's what you can expect in the modern, refreshed experience:

- Updated styling in form, view, and dashboard pages, which includes the use of drop shadows and brighter background colors to create an elevated or _floating_ appearance. The floating appearance helps to visually separate sections and focuses attention on primary content.
- New Fluent-based controls in forms, business process flows, and dialogs. Dialogs now resize height automatically based on the content.
- A new Power Apps grid in place of the read-only grid in view and standard, dashboard pages.
- A new mechanism for customizing the app header colors to match your personal or organizational branding. More information: [Use modern themes](../maker/model-driven-apps/modern-theme-overrides.md)
- An end user setting called **Try the new look** that enables the modern, refreshed experience.

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

Field controls such as text input, action input, lookup, and check box controls are built and designed using Fluent components. More field controls will be modernized using Fluent design in future updates.

Field sections, which are containers for the fields on a form, have a more streamlined design. Icons are now on the right side of field labels. Some redundant icons have been removed for a cleaner layout. For example, the recommended icons are removed for simplicity. Input and error message styling is also refreshed based on Fluent design.

The following example shows a set of fields with the modern, refreshed look.

:::image type="content" source="media/modern-fields.png" alt-text="Fields in a model-driven app that has the modern, refreshed look.":::

### Dashboard page

The system dashboard page, with independent subgrids and charts, has been updated to use the new [command bar](#command-bar) and has styling similar to the sections in form and view pages. When the modern experience is enabled, or when using the [monthly channel](../maker/model-driven-apps/channel-overview.md), the system dashboard grids use the new [Power Apps grid control](../maker/model-driven-apps/the-power-apps-grid-control.md). The new grid isn't enabled by default.

:::image type="content" source="media/modern-system-dashboard.png" alt-text="System dashboard page with the modern, refreshed look.":::

## Known limitations

The modern, refreshed look for model-driven apps has some limitations:

### Modern, refreshed look outside of browser

The mobile app and mail app don't support the modern, refreshed look and aren't part of the preview or general availability.

### Switching themes or enabling dark mode

Switching themes or enabling dark mode isn't supported at this time.

### Honoring classic theming

With the modern, refreshed look, Power Apps is no longer honoring [classic theme customizations](../maker/model-driven-apps/create-themes-organization-branding.md). You can, however, override the colors for the app header to match your organization branding with the modern, refreshed look. See [change the color of the app header](#change-the-color-of-the-app-header) for more details.  Other theme customization options for the modern, refreshed look aren't available yet.  

### Custom icons

Only SVG icons are supported. If you use other formats such as PNG, the navigation won't display them and a default icon will appear instead.

## Frequently asked questions (FAQs)

### Using the modern, refreshed look in Power Apps Component Framework / custom code components

The modern theme in use is passed to [Power Apps component framework](../developer/component-framework/overview.md) components allowing you to [style your components with modern theming](../developer/component-framework/fluent-modern-theming.md).

### Using the modern, refreshed look in custom pages

Modern controls can be used with custom pages and the modern, refreshed look. The modern theme isn't currently inherited by custom pages.

### Change the color of the app header

It's possible to change the color of the app header to match your organization while in the modern, refreshed look. See [Use modern themes](../maker/model-driven-apps/modern-theme-overrides.md) for more details. Other theme customization options for the modern, refreshed look aren't available yet.

## Working with the modern, refreshed look

### Provide feedback on the modern, refreshed look

After using the modern, refreshed look in your model-driven apps, tell us what you think about it in the [Power Apps community forum](https://go.microsoft.com/fwlink/?linkid=2221574).

### Managing opt-in general availability rollout

The modern, refreshed look for model-driven apps is generally available in the following release channels:

- Monthly channel in August 2023
- Semi-annual Channel as of 2023 Release Wave 2

Once generally available, end users will see the **Try the new look** setting to enable the modern, refreshed experience. Users can switch back to the old user interface (UI) at any time.

### Turn on the modern, refreshed look

End users can enable the modern, refreshed look for their model-driven apps in the app by enabling the **Try the new look** setting in the header of their app. They can switch back at [anytime](modern-fluent-design.md#revert-to-the-old-ui).

### Revert to the old UI

Yes, end users can switch back to the old UI by turning off the **New look** toggle. Makers can also disable the new look by updating the app setting.

For more information about disabling the modern, refreshed look, see [Manage model-driven app settings in the app designer](../maker/model-driven-apps/app-properties.md).

Admins can disable the **New look** setting across all apps in an organization by using the solution explorer to set the **New look for model driven apps** value to **No**. This hides the **New look** toggle and prevents the modern, refreshed look from taking effect.

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

### Managing on by default general availability rollout

Starting with 2024 Release Wave 1, the modern, refreshed look for model-driven apps is on by default. Once generally available, end users will see the **New look** setting enabled by default showing the modern, refreshed experience. Users can switch back to the old user interface (UI) at any time. The rollout will happen slowly over many weeks starting in April. Makers and admins should expect delays in seeing this feature rollout to their apps.

### Enabling the modern look for my app and removing the toggle

In scenarios where makers and admins want to turn on an "Always on" modern experience they can enable this by setting the **New look always on** app setting. This enables the modern, refreshed look for all users of the app and remove the header switch ability for end users to turn off **New look**.

Admins can enable the **New look always on** setting across all apps in an organization by using the solution explorer to set the **New look always on** value to **Yes**. This hides the **New look** toggle and enables the modern, refreshed look for all users.

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
