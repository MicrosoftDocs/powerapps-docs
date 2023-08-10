---
title: Power Apps system requirements and limits
description: Learn about device platform and web browser requirements, limits, and configuration values for Power Apps.
author: lancedMicrosoft
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: mkaur
ms.date: 08/04/2023
ms.subservice: canvas-maker
ms.author: gregli
search.audienceType: 
  - maker
contributors:
  - mduelae
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
| Windows | Windows 10 version 17763.0 or later to run [Power Apps for Windows](mobile/windows-app-install.md).

> [!NOTE]
> New major versions of iOS and Android are released each year. When a new version is released, if you're using the oldest previously supported version, you'll have 60 days to update your device to at least the new minimum supported version to continue to run Power Apps mobile.

## Supported browsers for running Power Apps

| **Browser** | **Supported versions** |  **App type** |
| --- | --- | --- |
| Google Chrome|Latest three major releases| Model-driven apps, canvas apps, app and component designers<sup>1</sup>.  |
| Microsoft Edge|Latest three major releases| Model-driven apps, canvas apps, app and component designers<sup>1</sup>.  |
| Mozilla Firefox |Latest three major releases| Model-driven apps and canvas apps. |
| Apple Safari|13 and later| Model-driven apps and canvas apps.  |

<sup>1</sup>App and component designers include Power Apps studio, model-driven app designer, and model-driven custom page designer.

## Supported operating systems for browsers running Power Apps

| **Operating system** | **Supported versions** |  **App type**  |
| --- | --- | ---|
| Windows |Windows 10 or later| Model-driven apps, canvas apps, app and component designers<sup>1</sup>.   |
| macOS|10.13 or later| Model-driven apps, canvas apps, app and component designers<sup>1</sup>.   |
| iOS |iOS 13 or later| Model-driven apps<sup>2</sup> and canvas apps. |
| Android |10 or later | Model-driven apps<sup>2</sup> and canvas apps.  |

<sup>1</sup>App and component designers include Power Apps studio, model-driven app designer, and model-driven custom page designer.

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
| api.bap.microsoft.com<br>\*.api.bap.microsoft.com | https | Environment permissions management |
| management.azure.com |https |Power Apps Management Service |
| msmanaged-na.azure-apim.net |https |Runtime of Connectors/Apis |
| login.microsoft.com<br>login.windows.net<br>login.microsoftonline.com<br>secure.aadcdn.microsoftonline-p.com<br>*.odc.officeapps.live.com |https |Microsoft Authentication Library |
| graph.microsoft.com<br>graph.windows.net |https |Azure Graph - For getting user info (for example, profile photo) |
| \*.azure-apim.net |https |Api Hubs - Different subdomains for each locale |
| \*.powerapps.com |https | create.powerapps.com, content.powerapps.com, apps.powerapps.com, make.powerapps.com, \*gateway.prod.island.powerapps.com, and \*gateway.prod.cm.powerapps.com |
| \*.azureedge.net |https | create.powerapps.com, content.powerapps.com, and make.powerapps.com <br>(Optional) We highly recommend that you use the wildcard listed under Domain(s). You may [download](https://go.microsoft.com/fwlink/?linkid=2225562) the complete list if you want to allow specific domain names instead of using *.azureedge.net. However, this list is subject to change.</br> |
| \*.ces.microsoftcloud.com  | https  | Access to net promoter score (NPS) and surveys. |
| \*.blob.core.windows.net |https | Blob storage <br>(Optional) We highly recommend that you use the wildcard listed under Domain(s). You may [download](https://go.microsoft.com/fwlink/?linkid=2225562) the complete list if you want to allow specific domain names instead of using *.blob.core.windows.net. However, this list is subject to change.</br> |
| \*.flow.microsoft.com<br/>\*.powerautomate.com | https | create.powerapps.com, content.powerapps.com, and make.powerapps.com |
| http://\*.crm#.dynamics.com and https://\*.crm#.dynamics.com | http and https | Required for environments access. Includes integration and static Content Delivery Network (CDN) content endpoints. <br /><br />Replace # in http://\*.crm#.dynamics.com and https://\*.crm#.dynamics.com with your region's number: <ul><li>Asia/Pacific: 5</li><li>Canada: 3 </li><li>Europe, Africa, and Middle East: 15 and 4</li><li>France: 12</li><li>Germany: 16</li><li>India: 8</li><li>Japan: 7</li><li>North America: no number</li><li>Oceania: 6</li><li>Singapore: 20</li><li>South Africa: 14</li><li>South America: 2</li><li>Switzerland: 17</li><li>UAE: 15</li><li>United Kingdom: 11</li><li>Dynamics 365 US Government: 9</li> |
| vortex.data.microsoft.com |https |Telemetry |
| localhost | https | Power Apps Mobile|
| 127.0.0.1 | http | Power Apps Mobile|
| ecs.office.com | https | Retrieve feature flags for Power Apps |
| config.edge.skype.com | https | Retrieve feature flags for Power Apps (backup)|
| api.powerplatform.com<br>\*.api.powerplatform.com | https | Required for Power Platform API connectivity used internally by Microsoft products, and Power Platform [programmability and extensibility](/power-platform/admin/programmability-extensibility-overview).|
| *.sharepointonline.com| https | Retrieve assets for presenting the header that appears at the top of app playing experiences |
| ris.api.iris.microsoft.com<br>eudb.ris.api.iris.microsoft.com | https | Record user action in response to Power Apps in-app campaigns |
| arc.msn.com<br>arc-emea.msn.com | https | Record user viewing of Power Apps in-app campaigns |

<sup>1</sup> Replaces domain name `gov.content.powerapps.us` used prior to July 2022. <br>
<sup>2</sup> Replaces domain name `high.content.powerapps.us` used prior to July 2022. <br>
<sup>3</sup> Replaces domain name `content.appsplatform.us` used prior to July 2022.

> [!IMPORTANT]
> - If you're using a VPN, it must be configured to exclude localhost from tunneling for Power Apps Mobile.
> - If you are a US Government customer or a customer in China, there are additional service URLs that must be unblocked. More information:<br/>**US Government**: [Power Apps US Government service URLs](/power-platform/admin/powerapps-us-government#power-apps-us-government-service-urls), [Power Automate US Government service URLs](/power-automate/us-govt#power-automate-us-government-service-urls)<br/>**China**: [Power Platform and Dynamics 365 apps - operated by 21Vianet in China](/power-platform/admin/about-microsoft-cloud-china).  

## Deprecated endpoints

This section lists endpoints that we no longer support. Instead, use the new endpoints listed below. We recommend updating any bookmarks you might have that use the deprecated endpoint to the new endpoint.

| Deprecated endpoint | New endpoint |
| --- | --- |
| web.powerapps.com/apps/{yourAppGuid} | apps.powerapps.com/play/{yourAppGuid}
| web.powerapps.com/apps/{yourAppGuid}/open | apps.powerapps.com/play/{yourAppGuid}

## Embedding limits for canvas apps

Power Apps doesn't support the nested embedding of canvas apps in native desktop, mobile, or other non-browser clients.

The following table shows some of the examples where embedding a canvas app is and isn't supported:
  
| Power Apps embedding scenario                                                                   | Supported clients                                 | Unsupported clients                            |
|-------------------------------------------------------------------------------------------------|---------------------------------------------------|------------------------------------------------|
| A canvas app embedded in a SharePoint page.                                                     | Web, e.g.   Sharepoint.com                        | <ul> <li> Teams desktop </li> <li> Teams mobile </li> </ul>                    |
| A canvas app embedded in a SharePoint page that is added as a tab in a Microsoft Teams channel. | Web, e.g.   <ul><li>Sharepoint.com</li>  <li>Teams.microsoft.com</li></ul> | <ul> <li> Teams desktop </li> <li> Teams mobile </li> </ul>                    |
| A canvas app used as a custom form in the SharePoint page.                                      | Web, e.g.   Sharepoint.com                        | <ul> <li> Teams desktop </li> <li> Teams mobile </li> </ul> |
| A canvas app used as a custom form in the SharePoint page that is added to a Teams team.        | Web, e.g.   <ul><li>Sharepoint.com</li>  <li>Teams.microsoft.com</li></ul> | <ul> <li> Teams desktop </li> <li> Teams mobile </li> <li>SharePoint mobile</li> </ul> |
| A Power BI report that is added to Teams, or a SharePoint site.                                 | Web, e.g. Teams.microsoft.com                     | <ul> <li> Teams desktop </li> <li> Teams mobile </li> <li>SharePoint mobile</li> |
| A model-driven form that is added to Teams.                                                     | Web, e.g. Teams.microsoft.com                     | <ul> <li> Teams desktop </li> <li> Teams mobile </li> </ul>                    |
| A canvas app is embedded in a 3rd party client.                                                 | 3rd party web client that iframe's an app         | 3rd party native client via WebView            |
|A canvas app in [Unified Service Desk](/dynamics365/unified-service-desk/admin/overview-unified-service-desk) |None|Unified Service Desk Desktop app|
## Proxies
Power Apps does not support running with a proxy enabled. This can cause unpredictable behavior. If you encounter issues, disable the proxy and then try again.

- Some proxies (such as Zscaler, Blue Coat) modify Power Apps requests by removing headers (CORS or authentication headers). Power Apps relies on these headers to load the app.
- Some proxies (such as Microsoft Defender for Cloud Apps, McAfee) may intercept and change the URL of an app or embedded app. For example, if there is a Dynamics 365 app that is running under domain **org.crm.dynamics.com** or a canvas app that is running under domain **apps.powerapps.com**, the platform will not support a proxy that change these domains to a custom domain such as **mycustomdomain.com**. This can cause unpredictable behavior when the platform tries to retrieve tokens that are necessary to run the app.

## Data types size limits

For canvas app data type limits, you can find information about size limits on text, hyperlinks, images, and media in [Data types in Power Apps](/power-platform/power-fx/data-types#text-hyperlink-image-and-media).

For Microsoft Dataverse data type size limits, you can find information on column types, such as text and image columns, in [Types of columns](maker/data-platform/types-of-fields.md).

## Power Apps per app plan

Information is now available in the [Power Apps per app plan](/power-platform/admin/signup-for-powerapps-admin#power-apps-per-app-plan) section in the Power Platform admin guide.

  
## See also

[System requirements, limits, and configuration values for Power Pages](/power-pages/system-requirements)
