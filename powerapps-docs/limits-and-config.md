---
title: Power Apps system requirements and limits
description: Learn about device platform and web browser requirements, limits, and configuration values for Power Apps.
author: lancedMicrosoft
ms.topic: article
ms.custom: canvas
ms.reviewer: mkaur
ms.date: 09/8/2025
ms.update-cycle: 180-days
ms.subservice: canvas-maker
ms.author: gregli
search.audienceType: 
  - maker
contributors:
  - mduelae
  - lancedmicrosoft
  - alaug
  - amchern
ms.contributors:
- arijitba
- norliu
ms.collection: 
    - bap-ai-copilot
---
# System requirements, limits, and configuration values for Power Apps

This article contains information on supported device platforms, web browser requirements, limits, and configuration values for Power Apps. 

## Supported platforms for running apps using the Power Apps mobile app

> [!NOTE]
> - To ensure optimal user experience, we recommend that you test your app on the specific devices intended for production deployment. 
> - Performance testing and results may vary between device types such as mobile, desktop, and laptops due to processing power, memory capacity, network connectivity, app complexity and other apps running in parallel in a device. Make sure the test results meet your business requirements before you roll out the solutions in production.

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
| \*.azure-apim.net |https |API Hubs - Different subdomains for each locale |
| \*.azure-apihub.net |https |API Hubs - Different subdomains for each locale |
| \*.powerapps.com |https | create.powerapps.com, content.powerapps.com, apps.powerapps.com, make.powerapps.com, \*gateway.prod.island.powerapps.com, \*gateway.prod.cm.powerapps.com, \*harvest.preview.powerapps.com, and \*harvest.powerapps.com |
| \*.gateway.prod.island.powerapps.com<br>\*.harvest.preview.powerapps.com<br>\*.harvest.powerapps.com| WSS | Required for communication with and startup of canvas apps and real-time updates with Coding Agent. |
| \*.azureedge.net |https | create.powerapps.com, content.powerapps.com, and make.powerapps.com <br>(Optional) We highly recommend that you use the wildcard listed under Domain(s). You can [download](https://go.microsoft.com/fwlink/?linkid=2225562) the complete list if you want to allow specific domain names instead of using *.azureedge.net. However, this list is subject to change.</br> |
| \*.azurefd.net |https | create.powerapps.com, content.powerapps.com, and make.powerapps.com |
| \*.ces.microsoftcloud.com<br/>config.centro.core.microsoft<br/>admin.microsoft.com<br/>petrol.office.microsoft.com<br/>oness.microsoft.com  | https  | Access to net promoter score (NPS) and surveys. |
| \*.blob.core.windows.net |https | Blob storage <br>(Optional) We highly recommend that you use the wildcard listed under Domain(s). You can [download](https://go.microsoft.com/fwlink/?linkid=2225562) the complete list if you want to allow specific domain names instead of using *.blob.core.windows.net. However, this list is subject to change.</br> |
| \*.flow.microsoft.com<br/>\*.powerautomate.com | https | create.powerapps.com, content.powerapps.com, and make.powerapps.com |
| http://\*.crm#.dynamics.com and https://\*.crm#.dynamics.com | https | Required for environments access. Includes integration and static Content Delivery Network (CDN) content endpoints. <br /><br />Replace # in http://\*.crm#.dynamics.com and https://\*.crm#.dynamics.com with your region's number: <ul><li>Asia/Pacific: 5</li><li>Canada: 3 </li><li>Europe, Africa, and Middle East: 15 and 4</li><li>France: 12</li><li>Germany: 16</li><li>India: 8</li><li>Japan: 7</li><li>North America: no number</li><li>Oceania: 6</li><li>Singapore: 20</li><li>South Africa: 14</li><li>South America: 2</li><li>Switzerland: 17</li><li>UAE: 15</li><li>United Kingdom: 11</li><li>Dynamics 365 US Government: 9</li> |
| browser.pipe.aria.microsoft.com | https | Rest of the World telemetry endpoint for model-driven apps |
| *.events.data.microsoft.com | https | Telemetry endpoint for Power Apps|
| localhost | http | Power Apps Mobile|
| 127.0.0.1 | http <br><br>You might need to explicitly list the port (5040 and up) for localhost/127.0.0.1.| Power Apps Mobile|
| ecs.office.com | https | Retrieve feature flags for Power Apps |
| augloop.svc.cloud.microsoft<br>\*.augloop.svc.cloud.microsoft | WSS | Power Apps Studio Copilot |
| config.edge.skype.com | https | Retrieve feature flags for Power Apps (backup)|
| api.powerplatform.com<br>\*.powerplatform.com <br> *.api.powerplatformusercontent.com <br> *.powerplatformusercontent.com| https | Required for Power Platform API connectivity used internally by Microsoft products, and Power Platform [programmability and extensibility](/power-platform/admin/programmability-extensibility-overview).|
| *.sharepointonline.com| https | Retrieve assets for presenting the header that appears at the top of app playing experiences |
| ris.api.iris.microsoft.com<br>eudb.ris.api.iris.microsoft.com | https | Record user action in response to Power Apps in-app campaigns |
| arc.msn.com<br>arc-emea.msn.com | https | Record user viewing of Power Apps in-app campaigns |
| *.hubblecontent.osi.office.net<br>hubble.officeapps.live.com<br>res.cdn.office.net |https |Provides stock images to use in your app |
| dc.services.visualstudio.com | https | [Application Insights](/azure/azure-monitor/app/app-insights-overview) endpoint used for [custom telemetry in canvas app](maker/canvas-apps/application-insights.md) |
| *.ocv.microsoft.com | https | Allows users to provide Copilot feedback data in Power Apps |
| js.monitor.azure.com | https | This is used by the office header for reporting telemetry |

<sup>1</sup> Replaces domain name `gov.content.powerapps.us` used before July 2022. <br>
<sup>2</sup> Replaces domain name `high.content.powerapps.us` used before July 2022. <br>
<sup>3</sup> Replaces domain name `content.appsplatform.us` used before July 2022.

> [!IMPORTANT]
> - If you're using a VPN, it must be configured to exclude localhost from tunneling for Power Apps Mobile.
> - If you are a US Government customer or a customer in China, there are additional service URLs that must be unblocked. More information:<br/>**US Government**: [Power Apps US Government service URLs](/power-platform/admin/powerapps-us-government#power-apps-us-government-service-urls), [Power Automate US Government service URLs](/power-automate/us-govt#power-automate-us-government-service-urls)<br/>**China**: [Power Platform and Dynamics 365 apps - operated by 21Vianet in China](/power-platform/admin/about-microsoft-cloud-china).

## Deprecated endpoints

This section lists endpoints that we no longer support. Instead, use the new endpoints listed below. We recommend updating any bookmarks you might have that use the deprecated endpoint to the new endpoint.

| Deprecated endpoint | New endpoint |
| --- | --- |
| web.powerapps.com/apps/{yourAppGuid} | apps.powerapps.com/play/{yourAppGuid}
| web.powerapps.com/apps/{yourAppGuid}/open | apps.powerapps.com/play/{yourAppGuid}

## Embedding limits for Power Apps

### Canvas app embedding

Power Apps doesn't support the nested embedding of canvas apps in native desktop, mobile, or other non-browser clients.

The following table shows some of the examples where embedding a canvas app is and isn't supported:
  
| Power Apps embedding scenario                                                                   | Supported clients                                 | Unsupported clients                            |
|-------------------------------------------------------------------------------------------------|---------------------------------------------------|------------------------------------------------|
| A canvas app embedded in a SharePoint page.                                                     | Web, for example,   Sharepoint.com                        | <ul> <li> Teams desktop </li> <li> Teams mobile </li> </ul>                    |
| A canvas app embedded in a SharePoint page that is added as a tab in a Microsoft Teams channel. | Web, for example.   <ul><li>Sharepoint.com</li>  <li>Teams.microsoft.com</li></ul> | <ul> <li> Teams desktop </li> <li> Teams mobile </li> </ul>                    |
| A canvas app used as a custom form in the SharePoint page.                                      | Web, for example,   Sharepoint.com                        | <ul> <li> Teams desktop </li> <li> Teams mobile </li> </ul> |
| A canvas app used as a custom form in the SharePoint page that is added to a Teams team.        | Web, for example.   <ul><li>Sharepoint.com</li>  <li>Teams.microsoft.com</li></ul> | <ul> <li> Teams desktop </li> <li> Teams mobile </li> <li>SharePoint mobile</li> </ul> |
| A Power BI report that is added to Teams, or a SharePoint site.                                 | Web, for example, Teams.microsoft.com                     | <ul> <li> Teams desktop </li> <li> Teams mobile </li> <li>SharePoint mobile</li> |
| A canvas app is embedded in a third party client.                                                 | Third party websites in a browser         | Third party native applications            |
|A canvas app in [Unified Service Desk](/dynamics365/unified-service-desk/admin/overview-unified-service-desk) |None|Unified Service Desk Desktop app|
| A canvas app embedded in Power BI | Web, for example, app.powerbi.com | Power BI Desktop Client |

### Model-driven app embedding

Power Apps doesn't support embedding a model-driven app or page within an IFrame in another application.

## Proxies

Power Apps doesn't support running with a proxy enabled. This can cause unpredictable behavior. If you encounter issues, disable the proxy and then try again.

- Some proxies (such as Zscaler, Blue Coat) modify Power Apps requests by removing headers (CORS or authentication headers). Power Apps relies on these headers to load the app.
- Some proxies (such as Microsoft Defender for Cloud Apps, McAfee) might intercept and change the URL of an app or embedded app. For example, if there's a Dynamics 365 app that is running under domain **org.crm.dynamics.com** or a canvas app that is running under domain **apps.powerapps.com**, the platform doesn't support a proxy that changes these domains to a custom domain such as **mycustomdomain.com**. This can cause unpredictable behavior when the platform tries to retrieve tokens that are necessary to run the app.

## Local Network Access and Permission Issues

In 2025, many browsers introduced additional security controls to prevent cross-origin attacks and unauthorized access to [private network resources.](https://developer.chrome.com/blog/local-network-access) These changes went into effect for Edge with their [December 4, 2025 release](/deployedge/microsoft-edge-relnote-stable-channel#version-1430365066-december-4-2025).

Some proxies are configured by default to host resources in a manner that appears to the end-user's browser as a local network resource, which now results in those requests being blocked. This may appear to end-users as unexpected permission prompts, silent failures, or generic messages such as "This app stopped working. Try refreshing your browser".

> [!NOTE]
> Microsoft Support cannot resolve these networking issues.
> Enterprise admins may be able mitigate this by updating browser policies such as LocalNetworkAccessAllowedForUrls for [Microsoft Edge](/deployedge/microsoft-edge-browser-policies/localnetworkaccessallowedforurls) and [Google Chrome](https://chromeenterprise.google/policies/#LocalNetworkAccessAllowedForUrls) or by updating proxy configurations according to their vendor's guidelines.

## Data types size limits

For canvas app data type limits, you can find information about size limits on text, hyperlinks, images, and media in [Data types in Power Apps](/power-platform/power-fx/data-types#text-hyperlink-image-and-media).

For Microsoft Dataverse data type size limits, you can find information on column types, such as text and image columns, in [Types of columns](maker/data-platform/types-of-fields.md).

## Power Apps per app plan

Information is now available in the [Power Apps per app plan](/power-platform/admin/signup-for-powerapps-admin#power-apps-per-app-plan) section in the Power Platform admin guide.

  
## See also

[System requirements, limits, and configuration values for Power Pages](/power-pages/system-requirements)
