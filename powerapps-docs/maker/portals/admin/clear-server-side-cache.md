---
title: "Clear the server-side cache for a portal | MicrosoftDocs"
description: "Instructions to force the portal to refresh its cache immediately."
author: tapanm-msft
manager: kvivek
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 04/23/2020
ms.author: tapanm
ms.reviewer:
---

# Clear the server-side cache for a portal

As a portal administrator, you can clear the server-side cache for the entire portal so that updated data from Common Data Service is immediately reflected on the portal. Updates from Common Data Service  are communicated to the portal in asynchronous mode, so there might be a lag between the time data is updated in Common Data Service and the time that updated data appears on the portal. To eliminate this delay&mdash;for example, when it interferes with portal configuration&mdash;you can force the portal to refresh its cache immediately.

> [!NOTE]
> The SLA for cache refresh (data transfer between Common Data Service and portal) is 15 minutes.

## Steps to clear portal server-side cache

> [!IMPORTANT]
> Clearing the portal server-side cache causes temporary performance degradation of the portal while data gets reloaded from Common Data Service.

To clear the server-side cache:

1. Sign in to the portal as an administrator.

1. Navigate to the URL as follows: `<portal_path>/_services/about`.

1. Select **Clear Cache**.

The server-side cache is deleted, and data is reloaded from Common Data Service. 

![Clear the portal cache](media/clear-server-side-cache/clear-portal-cache.png)

## Configuration entity caching portals with capacity-based licenses

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
