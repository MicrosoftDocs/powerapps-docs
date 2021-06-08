---
title: Important changes coming in Power Apps portals
description: Learn about the important changes including deprecation coming soon to Power Apps portals.
author: sandhangitmsft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 06/08/2021
ms.author: sandhan
ms.reviewer: tapanm
contributors:
    - tapanm-msft
    - sandhangitmsft
---

# Important changes coming in Power Apps portals

The announcements for changes, and deprecations described in this article apply to Power Apps portals.

Makers, developers and IT professionals can use this information to prepare for future releases.

> [!IMPORTANT]
> "Deprecated" means we intend to remove the feature or capability from a future major release. The feature or capability will continue to work and is fully supported until it is officially removed. This deprecation notification can span a few months or years. After removal, the feature or capability no longer work. This notice is to allow you sufficient time to plan and update your code before the feature or capability is removed.

## SameSite mode changes

Makers can mark **SameSite** mode as **Strict** for all portal cookies where applicable.  

With this change, we're adding a new website setting to control the **SameSite** mode for all cookies, configurable at specific cookie level.

| Site Setting Name | Scope | Possible value |
| - | - | - |
| HTTP/SameSite/Default | Global, for all cookies. | None <br> Lax <br> Strict |
| HTTP/SameSite/{CookieName} | Specific cookie. | None <br> Lax <br> Strict |

All newly provisioned portals will have **SameSite** default to the value of **Strict**. Existing portals will default to **None**.

To learn how to configure site settings for portals, go to [Configure site settings for portals](configure/configure-site-settings.md)

### See also

[Important changes (deprecations) coming in Power Apps, Power Automate, and customer engagement apps](/power-platform/important-changes-coming)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]