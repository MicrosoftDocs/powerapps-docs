---
title: Important upcoming changes and deprecations in Power Apps portals
description: Learn about the important changes including deprecation coming soon to Power Apps portals.
author: sandhangitmsft

ms.topic: conceptual
ms.custom: 
ms.date: 09/14/2021
ms.subservice: portals
ms.author: sandhan
ms.reviewer: ndoelman
contributors:
    - nickdoelman
    - sandhangitmsft
    - dileepsinghmicrosoft
    - nageshbhat-msft
---

# Important upcoming changes and deprecations in Power Apps portals

The announcements for changes, and deprecations described in this article apply to Power Apps portals.

Makers, developers, and IT professionals can use this information to prepare for future releases.

> [!IMPORTANT]
> "Deprecated" means we intend to remove the feature or capability from a future major release. The feature or capability will continue to work and is fully supported until it is officially removed. This deprecation notification can span a few months or years. After removal, the feature or capability no longer work. This notice is to allow you sufficient time to plan and update your code before the feature or capability is removed.

## CDN for US Government

Starting January 2022, Power Apps portals for US Government will begin using [Azure Content Delivery Network (CDN)](/azure/cdn/cdn-overview) for [default JavaScript and CSS files](faq.yml#do-portals-use-any-static-content-from-cdns--content-delivery-network--that-i-need-to-allow-list-). Depending on the US Government deployment, configure the allow-list for the following CDN URLs:

| Power Apps portals version | CDN URL |
| - | - |
| Government Community Cloud (GCC) | `https://gov.content.powerapps.us` |
| GCC High | `https://high.content.powerapps.us` |
| Power Apps Department of Defense (DoD) | `https://content.appsplatform.us` |

## Table permission changes for forms and lists on new portals

Starting with release [9.3.7.x](/power-platform/released-versions/portals/portalupdate1), newly created portals will have table permissions enforced for all [forms](configure/entity-forms.md#secure-your-forms) and [lists](configure/entity-lists.md#securing-lists) irrespective of the **Enable Table Permissions** setting.

Also, with the same release, lists on all portals (new or existing) that have [OData feeds](configure/entity-lists.md#list-odata-feeds) enabled will require appropriate [table permissions](configure/entity-permissions-studio.md) setup for the feed on these lists to work.

> [!NOTE]
> The changes described above also apply to portals [converted](admin/convert-portal.md) from trial to production.

To configure anonymous access explicitly, use proper [table permissions](configure/entity-permissions-studio.md), and web role setup instead.

## SameSite mode changes

Starting with portals version [9.3.6.x](versions/version-9.3.6.x.md), makers can mark **SameSite** mode as **Strict** for all portal cookies where applicable.  

With this change, we're adding a new website setting to control the **SameSite** mode for all cookies, configurable at specific cookie level.

| Site Setting Name | Scope | Possible value |
| - | - | - |
| HTTP/SameSite/Default | Global, for all cookies. | None <br> Lax <br> Strict |
| HTTP/SameSite/{CookieName} | Specific cookie. | None <br> Lax <br> Strict |

Default value for all existing and newly provisioned portals is **None**.

> [!IMPORTANT]
> Starting October 2021, all newly provisioned portals will have **Strict** as the Default value instead of **None**.

To learn how to configure site settings for portals, go to [Configure site settings for portals](configure/configure-site-settings.md)

## Tracking for web page, web file, and login

Starting with portals version [9.3.4.x](versions/version-9.3.4.x.md), the following functionality has been retired:

- [Web page tracking](admin/portal-checker-analysis.md#web-page-tracking-enabled)
- [Web file tracking](admin/portal-checker-analysis.md#web-file-tracking-enabled)
- [Login tracking](admin/portal-checker-analysis.md#login-tracking-enabled)

### See also

[Important changes (deprecations) coming in Power Apps, Power Automate, and customer engagement apps](/power-platform/important-changes-coming)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]