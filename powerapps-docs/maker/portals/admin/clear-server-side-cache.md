---
title: "Clear the server-side cache for a portal"
description: "Instructions to force the portal to refresh its cache immediately."
author: neerajnandwana-msft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 07/21/2020
ms.author: nenandw
ms.reviewer: tapanm
---

# Clear the server-side cache for a portal

As a portal administrator, you can clear the server-side cache for the entire portal so that updated data from Common Data Service is immediately reflected on the portal. Updates from Common Data Service  are communicated to the portal in asynchronous mode, so there might be a lag between the time data is updated in Common Data Service and the time that updated data appears on the portal. To eliminate this delay&mdash;for example, when it interferes with portal configuration&mdash;you can force the portal to refresh its cache immediately.

> [!IMPORTANT]
> - Clearing the [portal server-side cache](#steps-to-clear-portal-server-side-cache) or the [configuration entities cache](#configuration-entity-caching-portals-with-capacity-based-licenses) causes temporary performance degradation of the portal while data gets reloaded from Common Data Service.
> - Changes to the [configuration entities](#list-of-configuration-entities-refreshed-when-you-clear-config), or [business data entities (standard or custom)](../../common-data-service/entity-overview.md) such as when [publishing changes](../../common-data-service/create-solution.md#publish-changes) should be performed during non-peak hours. Frequent or too many entity changes may adversely affect portal performance.
> - The SLA for cache refresh (data transfer between Common Data Service and portal) is 15 minutes.
> - Power Apps portals with version 9.2.6.x or later have improved caching. For more information, go to [Caching changes for portals with version 9.2.6.x or later](#caching-changes-for-portals-with-version-926x-or-later).

## Steps to clear portal server-side cache

To clear the server-side cache:

1. Sign in to the portal as an administrator.

1. Navigate to the URL as follows: `<portal_path>/_services/about`.

1. Select **Clear Cache**.

The server-side cache is deleted, and data is reloaded from Common Data Service. 

![Clear the portal cache](media/clear-server-side-cache/clear-portal-cache.png)

## Configuration entity caching in portals with capacity-based licenses<a name = "configuration-entity-caching-portals-with-capacity-based-licenses"></a>

[Capacity based](https://docs.microsoft.com/power-platform/admin/powerapps-flow-licensing-faq#portals) portals have more options on `<portal_path>/_services/about`:

![Clear portal cache with capacity-based license](media/clear-server-side-cache/clear-config-capacity-license.png)

To learn more about the differences between Power Apps portals and portal add-ons, read [Power Apps portal FAQ](../faq.md#what-is-the-difference-between-power-apps-portals-dynamics-365-portals-and-add-on-portals).

Portal metadata is stored in entities called *configuration entities*. If you change configuration entities using the *Unified Interface application*, you **must** select **Clear config** to clear the configuration cache for changes to reflect in your Portal.  

### List of configuration entities refreshed when you clear config

Clearing the server-side configuration cache for a portal includes refreshing the data from the following *configuration entities*:

| Configuration entities:| | |
|-------------------------------------------|---------------------------|--------------------------------------|
| adx_contentaccesslevel                    | adx_redirect              | adx_webpage_tag                      |
| adx_contentsnippet                        | adx_setting               | adx_webpageaccesscontrolrule         |
| adx_entityform                            | adx_shortcut              | adx_webpageaccesscontrolrule_webrole |
| adx_entityformmetadata                    | adx_sitemarker            | adx_webpagehistory                   |
| adx_entitylist                            | adx_sitesetting           | adx_webpagelog                       |
| adx_entitypermission_webrole              | adx_webfile               | adx_webrole_systemuser               |
| adx_externalidentity                      | adx_webfilelog            | adx_website                          |
| adx_pagealert                             | adx_webform               | adx_website_list                     |
| adx_pagenotification                      | adx_webformmetadata       | adx_website_sponsor                  |
| adx_pagetag                               | adx_webformsession        | adx_websiteaccess                    |
| adx_pagetag_webpage                       | adx_webformstep           | adx_websiteaccess_webrole            |
| adx_pagetemplate                          | adx_weblink               | adx_websitebinding                   |
| adx_portallanguage                        | adx_weblinkset            | adx_websitelanguage                  |
| adx_publishingstate                       | adx_webnotificationentity | adx_webtemplate                      |
| adx_publishingstatetransitionrule         | adx_webnotificationurl    | adx_urlhistory                       |
| adx_publishingstatetransitionrule_webrole | adx_webpage               | adx_entitypermission                 |

## Caching changes for portals with version 9.2.6.x or later

Power Apps portals with version 9.2.6.x or later benefit from improved caching functionality to increase consistency and reliability as follows.

- [Capacity-based portals and add-on portals](../faq.md#what-is-the-difference-between-power-apps-portals-dynamics-365-portals-and-add-on-portals) will use the same caching functionality.
- Capacity-based portals don't have to manually [clear the configuration entity cache](#configuration-entity-caching-portals-with-capacity-based-licenses).
- Add-on portals with high load will have improved performance and a reliable data cache refresh.

> [!IMPORTANT]
> - No change to SLA for cache refresh (data transfer between Common Data Service and portal) mentioned earlier in this article.
> - Data changes done using portals will reflect immediately in Common Data Service and portals.
> - No change to [clear server-side cache functionality](#steps-to-clear-portal-server-side-cache). You can continue to use this functionality to clear server cache immediately.
 
### FAQs
 
**1. Can I change the cache refresh duration from 15 minutes to a lesser duration?** <br>
No. SLA for cache refresh remains 15 minutes. Any changes from Common Data Service will reflect on portals within 15 minutes.

**2. I'm using plugins or workflows to update data in other entities and need these data changes to reflect immediately on my portal.** <br>
This design approach isn't recommended. Except the primary record where the create or update action is triggered, data reflection from Common data Service to portals is never guaranteed to be immediate.

**3. Is there any difference in caching between capacity-based portals and add-on portals?** <br>
No.

**4. How long does it take for changes to reflect from portals to Common Data Service?** <br>
Immediately, as long as the update changes a primary record and isn't based on indirect changes to data using plugins or workflows.
