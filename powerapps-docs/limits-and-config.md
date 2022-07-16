---
title: Power Apps system requirements and limits
description: Learn about device platform and web browser requirements, limits, and configuration values for Power Apps.
author: lancedMicrosoft
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 07/21/2022
ms.subservice: canvas-maker
ms.author: gregli
search.audienceType: 
  - maker
search.app: 
  - PowerApps
contributors:
  - tapanm-msft
  - lancedmicrosoft
  - alaug
  - amchern
---
# System requirements, limits, and configuration values for Power Apps

This article contains information on supported device platforms, web browser requirements, limits, and configuration values for Power Apps. 

## Supported platforms for running apps using the Power Apps mobile app

| **Platform** | **Version**
| --- | --- |
| iOS |The latest version of iOS is always the recommended version to run Power Apps mobile. The previous version is the minimum required.|
| Android |The latest version of Android is always the recommended version to run Power Apps mobile. The previous three versions are the minimum required to run Power Apps mobile. 
| Windows | Windows 10 version 17763.0 or later to run [Power Apps for Windows (preview)](mobile/windows-app-install.md).

> [!NOTE]
> New major versions of iOS and Android are released each year. When a new version is released, if you're using the oldest previously supported version, you'll have 60 days to update your device to at least the new minimum supported version to continue to run Power Apps mobile.

## Supported browsers for running Power Apps

| **Browser** | **Supported versions** |  **App type** |
| --- | --- | --- |
| Google Chrome|Latest three major releases| Model-driven apps, canvas apps, Power Apps portals, app and component designers<sup>1</sup>.  |
| Microsoft Edge|Latest three major releases| Model-driven apps, canvas apps, Power Apps portals, app and component designers<sup>1</sup>.  |
| Mozilla Firefox |Latest three major releases| Model-driven apps, canvas apps, Power Apps portals.  |
| Apple Safari|13 and later| Model-driven apps, canvas apps, Power Apps portals.  |

<sup>1</sup>App and component designers include Power Apps studio, Power Apps portals Studio, model-driven app designer, and model-driven custom page designer.

## Supported operating systems for browsers running Power Apps

| **Operating system** | **Supported versions** |  **App type**  |
| --- | --- | ---|
| Windows |Windows 10 or later| Model-driven apps, canvas apps, Power Apps portals, app and component designers<sup>1</sup>.   |
| macOS|10.13 or later| Model-driven apps, canvas apps, Power Apps portals, app and component designers<sup>1</sup>.   |
| iOS |iOS 13 or later| Model-driven apps<sup>2</sup>, canvas apps, Power Apps portals.  |
| Android |10 or later | Model-driven apps<sup>2</sup>, canvas apps, Power Apps portals.  |

<sup>1</sup>App and component designers include Power Apps studio, Power Apps portals Studio, model-driven app designer, and model-driven custom page designer.

<sup>2</sup>Using the web browser on a phone to run a model-driven app isn't supported; use the [Power Apps mobile app](mobile/run-powerapps-on-mobile.md).

For classic web application system requirements, go to [Web application requirements](/power-platform/admin/web-application-requirements).

> [!NOTE]
> Canvas apps running on Windows platform must use the legacy Microsoft Dataverse connector. A [warning is displayed](maker/canvas-apps/use-native-cds-connector.md) for apps that still use the legacy connector, but using it for Windows platform is supported.

## Request limits

These limits apply to each single outgoing request:

| Name | Limit |
| --- | --- |
| Timeout |180 Seconds |
| Retry attempts |4 |

> [!NOTE]
> The retry value may vary. For certain error conditions, it's not necessary to retry.

## IP addresses

Requests from Power Apps use IP addresses that depend on the region of the [environment](/power-platform/admin/environments-overview) that the app is in. We don't publish fully qualified domain names available for Power Apps scenarios.

Calls made from an API connected through an app (for example, the SQL API or the SharePoint API) come from these [IP addresses](/power-platform/admin/online-requirements#ip-addresses-required).

## Required services

This list identifies all services to which Power Apps communicates and their usages. Your network must **not** block these services.

| Domain(s) | Protocols | Uses |
| --- | --- | --- |
| api.bap.microsoft.com<br/>api.businessappdiscovery.microsoft.com | https | Environment permissions management|
| management.azure.com |https |Power Apps Management Service |
| msmanaged-na.azure-apim.net |https |Runtime of Connectors/Apis |
| login.microsoft.com<br>login.windows.net<br>login.microsoftonline.com<br>secure.aadcdn.microsoftonline-p.com |https |Microsoft Authentication Library |
| graph.microsoft.com<br>graph.windows.net |https |Azure Graph - For getting user info (for example, profile photo) |
| gallery.azure.com |https |Sample and Template apps |
| \*.azure-apim.net |https |Api Hubs - Different subdomains for each locale |
| \*.powerapps.com |https | create.powerapps.com, content.powerapps.com, apps.powerapps.com, make.powerapps.com, \*gateway.prod.island.powerapps.com, and \*gateway.prod.cm.powerapps.com |
| \*.azureedge.net |https | create.powerapps.com, content.powerapps.com, and make.powerapps.com |
| \*.blob.core.windows.net |https | Blob storage |
| \*.flow.microsoft.com | https | create.powerapps.com, content.powerapps.com, and make.powerapps.com |
| \*.dynamics.com | https | Microsoft Dataverse |
| vortex.data.microsoft.com |https |Telemetry |
| localhost | https | Power Apps Mobile|
| 127.0.0.1 | http | Power Apps Mobile|
| ecs.office.com | https | Retrieve feature flags for Power Apps |
| config.edge.skype.com | https | Retrieve feature flags for Power Apps (backup)|
| \*.api.powerplatform.com | https | Required for Power Platform API connectivity used internally by Microsoft products, and Power Platform [programmability and extensibility](/power-platform/admin/programmability-extensibility-overview).|
| *.powerapps.us | https | Required for Power Apps portals for Government Community Cloud (GCC).<sup>1</sup>  |
| *.powerapps.us | https | Required for Power Apps portals for Government Community Cloud (GCC High).<sup>2</sup> |
| *.appsplatform.us | https | Required for Power Apps portals for Power Apps Department of Defense (DoD).<sup>3</sup> |

<sup>1</sup> Replaces domain name `gov.content.powerapps.us` used prior to July 2022. <br>
<sup>2</sup> Replaces domain name `high.content.powerapps.us` used prior to July 2022. <br>
<sup>3</sup> Replaces domain name `content.appsplatform.us` used prior to July 2022.

> [!NOTE]
> If you're using a VPN, it must be configured to exclude localhost from tunneling for Power Apps Mobile.

## Deprecated endpoints

This section lists endpoints that we no longer support. Instead, use the new endpoints listed below. We recommend updating any bookmarks you might have that use the deprecated endpoint to the new endpoint.

| Deprecated endpoint | New endpoint |
| --- | --- |
| web.powerapps.com/apps/{yourAppGuid} | apps.powerapps.com/play/{yourAppGuid}
| web.powerapps.com/apps/{yourAppGuid}/open | apps.powerapps.com/play/{yourAppGuid}

## Embedding limits for canvas apps

Power Apps doesn't support the nested embedding of canvas apps in native desktop, mobile, or other non-browser clients.

The following table shows some of the examples where embedding a canvas app isn't supported:

| Canvas apps embedded to | Unsupported client |
| - | - |
| A SharePoint page that is added as a tab in a Microsoft Teams channel | <ul> <li> Teams desktop </li> <li> Teams mobile </li> </ul> |
| A Power BI report that is added to a Teams team, or a SharePoint site | <ul> <li> Teams desktop </li> <li> Teams mobile </li> <li> SharePoint mobile </li> </ul> |
| A model-driven form that is added to Teams | <ul> <li> Teams desktop </li> <li> Teams mobile </li> </ul> |

## Proxies

Power Apps does not support running with a proxy enabled. Some proxies (such as Zscaler, Blue Coat) modify Power Apps requests by removing headers (CORS or authentication headers). Power Apps relies on these headers to load the app. Hence, if your app has any problems while loading when proxy is enabled, disable the proxy and then try again.

## Data types size limits

For canvas app data type limits, you can find information about size limits on text, hyperlinks, images, and media in [Data types in Power Apps](maker/canvas-apps/functions/data-types.md#text-hyperlink-image-and-media).

For Microsoft Dataverse data type size limits, you can find information on column types, such as text and image columns, in [Types of columns](maker/data-platform/types-of-fields.md).

## Power Apps per app plan

Information is now available in the [Power Apps per app plan](/power-platform/admin/signup-for-powerapps-admin#power-apps-per-app-plan) section in the Power Platform admin guide.
