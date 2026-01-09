---
title: Important upcoming changes (deprecations) in canvas apps
description: Learn about the important changes including deprecation coming soon to canvas apps.
author: mduelae

ms.topic: article
ms.custom: 
ms.date: 01/07/2026
ms.subservice: canvas-maker
ms.author: tapanm
ms.reviewer: mkaur-msft
contributors:
    - mduelae
    - shwetamurkute
---

# Important upcoming changes (deprecations) in canvas apps

The announcements for changes (deprecations) described in this article apply to canvas apps.

Makers, developers, and IT professionals can use this information to prepare for future releases.

> [!IMPORTANT]
> "Deprecated" means we intend to remove the feature or capability from a future major release. The feature or capability will continue to work and is fully supported until it is officially removed. This deprecation notification can span a few months or years. After removal, the feature or capability no longer work. This notice is to allow you sufficient time to plan and update your code before the feature or capability is removed.

## Enhanced deep link creation requirement

Starting May 1, 2026, for canvas apps, all deep links for Power Apps mobile must include the environment ID as a required parameter. Existing deep links without these parameters will stop working after the deprecation date. You also need to create new shortcuts. Update your links now to avoid disruptions. Old links have slower performance until support ends. Learn more in [Use deep links with the Power Apps mobile app](/power-apps/mobile/mobile-deep-links).

## Deprecated endpoints

For information about deprecated endpoints, see [Deprecated endpoints](../../limits-and-config.md#deprecated-endpoints)

## New addition for restrictive firewall rules to filter subdomains

Effective February 14, 2022, if you’re using restrictive firewall rules to filter subdomains instead of `*.powerapps.com`, you’ll also need to allow access to `*gateway.prod.island.powerapps.com` for a continued Power Apps authoring and runtime experience. To see the complete list of the subdomains, go to [Required services](limits-and-config.md#required-services).

## Rules feature in canvas apps is deprecated

Effective October 14, 2019, the [rules](working-with-rules.md) feature in canvas apps in Power Apps is deprecated. Few people have made use of rules in their canvas apps. From feedback collected through research and discussions with makers of Power Apps, the rules feature was confusing, and expressions were easier to learn, use, and debug. For more information about the rules feature deprecation, see [Blog: Canvas Rules feature deprecation](https://powerapps.microsoft.com/blog/canvas-rules-feature-deprecation/).

## Map component fields using dropdown option

The capability to map component fields using dropdown option available through the **Advanced** tab for the selected component that's added to an app has been deprecated. To learn more about mapping component fields, alternatives, and this deprecation, go to [Map input fields of a component](map-component-input-fields.md).

### See also

[Important changes (deprecations) coming in Power Apps, Power Automate, and customer engagement apps](/power-platform/important-changes-coming)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
