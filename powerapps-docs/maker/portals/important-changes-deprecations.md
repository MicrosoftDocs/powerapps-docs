---
title: Important upcoming changes and deprecations in Power Apps portals
description: Learn about the important changes, including deprecations, coming soon to Power Apps portals.
author: sandhangitmsft
ms.topic: conceptual
ms.custom: 
ms.date: 09/21/2022
ms.subservice: portals
ms.author: sandhan
ms.reviewer: ndoelman
contributors:
    - nickdoelman
    - sandhangitmsft
    - dileepsinghmicrosoft
    - nageshbhat-msft
    - ProfessorKendrick
---

# Important upcoming changes and deprecations in Power Apps portals


[!INCLUDE[cc-pages-ga-banner](../../includes/cc-pages-ga-banner.md)]

The announcements for changes and deprecations described in this article apply to Power Apps portals.

Makers, developers, and IT pros can use this information to prepare for future releases.

> [!IMPORTANT]
> *Deprecated* means that we intend to remove the feature or capability from a future major release. The feature or capability will continue to work and is fully supported until it's officially removed. This deprecation notification can span a few months or years. After it's removal, the feature or capability no longer work. This notice is to allow you sufficient time to plan and update your code before the feature or capability is removed.

## Controlling site visibility changes in Power Pages

Starting October 2022 with website version 9.4.9.xx, any new site created in Power Pages or Power Apps portals will be private by default. Only makers or people in the organization granted permission by makers will have website access, making Power Pages sites secure. This feature will provide another layer of security using Azure Active Directory authentication to prevent accidental leaks of partially developed website data and design. When a website is ready to go-live, the site visibility can be changed to public making it accessible to everyone over the internet anonymously or secured with identity providers.  

At launch, users with the system administrator role along with [service admins](/power-platform/admin/use-service-admin-role-manage-tenant) will by default have privilege to change site visibility status (private to public or vice versa). 

> [!Note] 
> All system administrators being able to change the site visibility will only be for a certain duration after which service admins will need to explicitly specify whether all system administrators are allowed to change site visibility. However, admins can grant or revoke the privilege of changing site visibility status for system administrators at tenant level by running a PowerShell script. Additionally, to provide granular control on who can change the site visibility status, admins can delegate the permissions to specific System administrators in certain Azure Directory security groups. 

## OAuth 2.0 implicit grant flow within your portal 

The [authorize endpoint](oauth-implicit-grant-flow.md#authorize-endpoint-details), [token endpoint](oauth-implicit-grant-flow.md#token-endpoint-details) using GET request, and using the default certificate for OAuth 2.0 implicit grant flow is deprecated. No action is needed for newly created portals or for existing portals that don't use this feature. If you're already using this feature, you need to use the token endpoint POST request to get a secure access token to authorize the external APIs.

> [!NOTE]
> - All existing customers who are using this deprecated feature need to migrate to the supported method by October 2022.
> - For more information on using a custom certificate, go to [Using a custom certificate](oauth-implicit-grant-flow.md#custom-certificates).
> - For sample code on using POST calls on the Token endpoint, go to [Token endpoint sample](oauth-implicit-grant-flow.md#token-endpoint-sample).

## List OData feed 

Starting June 2022, using [OData feeds](configure/list-odata-feeds.md) to interact with data via RESTful web services will be deprecated. We recommend that you migrate to the portal [Web API](web-api-overview.md) by April 2023. 

> [!NOTE] 
> Starting October 2022, newly provisioned portals won't able to use list OData features. 

## Portal content editor

Starting June 2022, the portal content editor tool to design your website is deprecated. We recommend using Power Apps portals Studio to edit the portal.

> [!NOTE]
> This feature will be removed by April 2023.

## Portals search using Lucene.NET search 

Starting with website version 9.4.4.xx, portal search uses Dataverse search as a default search provider for all new portals. Lucene.NET search is deprecated; however, existing portals that use Lucene.NET search won't be affected. We recommend that users migrate to Dataverse search. Enable Dataverse search for existing portal by setting the Search/EnableDataverseSearch site setting to true.

> [!NOTE]
> All existing customers who use Lucene.NET search must migrate to Dataverse search by October 2023.

## Content Delivery Network for US Government

Starting January 2022, Power Apps portals for US Government will begin using [Azure Content Delivery Network](/azure/cdn/cdn-overview) for [default JavaScript and CSS files](faq.yml#do-portals-use-any-static-content-from-cdns--content-delivery-network--that-i-need-to-allow-list-). Depending on the US Government deployment, configure the allowlist for the following Content Delivery Network URLs as follows.

| Power Apps portals version | Content Delivery Network URL |
| - | - |
| Government Community Cloud (GCC) | `https://gov.content.powerapps.us` |
| GCC High | `https://high.content.powerapps.us` |
| Power Apps Department of Defense | `https://content.appsplatform.us` |

## Table permission changes for forms and lists on new portals

Starting with release [9.3.7.x](/power-platform/released-versions/portals/portalupdate1), newly created portals will have table permissions enforced for all [forms](configure/entity-forms.md#secure-your-forms) and [lists](configure/securing-lists.md), irrespective of the **Enable Table Permissions** setting.

Also, with the same release, lists on all portals (new or existing) that have [list OData feeds](configure/list-odata-feeds.md) enabled will require that the appropriate [table permissions](configure/entity-permissions-studio.md) be set up for the feed on these lists to work.

> [!NOTE]
> The changes described above also apply to portals [converted](admin/convert-portal.md) from trial to production.

To configure anonymous access explicitly, use proper [table permissions](configure/entity-permissions-studio.md) and web role set up instead.

## SameSite mode changes

Starting with portals version [9.3.6.x](versions/version-9.3.6.x.md), makers can mark **SameSite** mode as **Strict** for all portal cookies where applicable.  

With this change, we're adding a new website setting to control the **SameSite** mode for all cookies, configurable to the level of specific cookies.

| Site setting name | Scope | Possible value |
| - | - | - |
| HTTP/SameSite/Default | Global, for all cookies. | None <br /> Lax <br /> Strict |
| HTTP/SameSite/{CookieName} | Specific cookie. | None <br /> Lax <br /> Strict |

The default value for all existing and newly provisioned portals is **None**.

To learn how to configure site settings for portals, go to [Configure site settings for portals](configure/configure-site-settings.md).

## Tracking for webpage, web file, and login

Starting with portals version [9.3.4.x](versions/version-9.3.4.x.md), the following functionality has been retired:

- [Webpage tracking](admin/portal-checker-analysis.md#web-page-tracking-enabled)
- [Web file tracking](admin/portal-checker-analysis.md#web-file-tracking-enabled)
- [Login tracking](admin/portal-checker-analysis.md#login-tracking-enabled)

### See also

[Important changes (deprecations) coming in Power Apps, Power Automate, and customer engagement apps](/power-platform/important-changes-coming)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
