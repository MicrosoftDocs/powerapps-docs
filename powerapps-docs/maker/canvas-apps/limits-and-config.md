---
title: Canvas app system requirements and limits
description: Learn about device platform and web browser requirements, limits, and configuration values for canvas apps built in Power Apps.
author: lancedMicrosoft
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 10/27/2021
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
  - wimcoor
---
# System requirements, limits, and configuration values for canvas apps
This article contains information on supported device platforms, web browser requirements, limits, and configuration values for canvas apps. 

## Supported platforms for running canvas apps using the Power Apps mobile app

| **Minimum required** | **Recommended** |
| --- | --- |
| iOS 13 or later |iOS 13 or later|
| Android 7 or later |Android 7 or later |
| Windows 8.1 or later (PC only) |Windows 10 Fall Creators Update with at least 8 GB of RAM)|

> [!NOTE]
> - As of October 16, 2020, we no longer support iOS 12. Only iOS 13 or later is supported. 
> - We currently don't support new features on Windows platform for [Power Apps mobile app](/powerapps/maker/canvas-apps/run-canvas-and-model-apps-on-mobile). Features such as the Improved Microsoft Dataverse option and guest access are not available on this platform. We recommend using a web player on Windows to leverage the full set of capabilities. Updates to the Power Apps mobile app for Windows platform will be announced in future.
> - Canvas apps running on Windows platform must use the legacy Microsoft Dataverse connector. A [warning is displayed](use-native-cds-connector.md) for apps that still use the legacy connector, but using it for Windows platform is supported.

## Supported browsers for running canvas apps

| **Browser** | **Supported Versions** |
| --- | --- |
| Google Chrome|Latest three major releases|
| Microsoft Edge|Latest three major releases|
| *Microsoft Internet Explorer|11 (with Compatibility View off)|
| Mozilla Firefox (latest version)|Latest three major releases|
| Apple Safari|13 and later|

*Microsoft Internet Explorer 11 support for Power Apps is deprecated. We recommend that you use Microsoft Edge. More information: [Deprecation announcement](/power-platform/important-changes-coming#internet-explorer-11-support-for-dynamics-365-and-microsoft-power-platform-is-deprecated)

### Supported platforms for browsers running canvas apps

| **Operating System** | **Supported Versions** |
| --- | --- |
| Windows |Windows 8.1 or later|
| macOS|10.13 or later|
| iOS |iOS 13 or later|
| Android |10 or later |

*Microsoft Internet Explorer 11 support for Power Apps is deprecated. We recommend that you use Microsoft Edge. More information: [Deprecation announcement](/power-platform/important-changes-coming#internet-explorer-11-support-for-dynamics-365-and-microsoft-power-platform-is-deprecated)

## Supported browsers for Power Apps Studio

| **Browser** | **Supported Versions** |
| --- | --- |
| Google Chrome|Latest three major releases|
| Microsoft Edge|Latest three major releases|
| *Microsoft Internet Explorer|11 (with Compatibility View off)|

*Microsoft Internet Explorer 11 support for Power Apps is deprecated. We recommend that you use Microsoft Edge. More information: [Deprecation announcement](/power-platform/important-changes-coming#internet-explorer-11-support-for-dynamics-365-and-microsoft-power-platform-is-deprecated)

### Supported platforms for browsers running Power Apps Studio

| **Operating Systems** | **Supported Versions** |
| --- | --- |
| Windows |Windows 8.1 or later|
| macOS|10.13 or later|

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

Calls made from an API connected through an app (for example, the SQL API or the SharePoint API) come from these [IP addresses](/connectors/common/outbound-ip-addresses#power-platform).

## Required services
This list identifies all services to which Power Apps Studio talks and their usages. Your network must **not** block these services.

| Domain(s) | Protocols | Uses |
| --- | --- | --- |
| api.bap.microsoft.com<br/>api.businessappdiscovery.microsoft.com | https | Environment permissions management|
| management.azure.com |https |RP |
| msmanaged-na.azure-apim.net |https |Runtime of Connectors/Apis |
| login.microsoft.com<br>login.windows.net<br>login.microsoftonline.com<br>secure.aadcdn.microsoftonline-p.com |https |Microsoft Authentication Library |
| graph.microsoft.com<br>graph.windows.net |https |Azure Graph - For getting user info (for example, profile photo) |
| gallery.azure.com |https |Sample and Template apps |
| \*.azure-apim.net |https |Api Hubs - Different subdomains for each locale |
| \*.powerapps.com |https | create.powerapps.com, content.powerapps.com, apps.powerapps.com, and make.powerapps.com |
| \*.azureedge.net |https | create.powerapps.com, content.powerapps.com, and make.powerapps.com |
| \*.blob.core.windows.net |https | Blob storage |
| \*.flow.microsoft.com | https | create.powerapps.com, content.powerapps.com, and make.powerapps.com |
| \*.dynamics.com | https | Microsoft Dataverse |
| vortex.data.microsoft.com |https |Telemetry |
| localhost | https | Power Apps Mobile|
| 127.0.0.1 | http | Power Apps Mobile|

> [!NOTE]
> If you're using a VPN, it must be configured to exclude localhost from tunneling for Power Apps Mobile.

## Embedding limits for canvas apps

Power Apps doesn't support the nested embedding of canvas apps in native desktop, mobile, or other non-browser clients.

The following table shows some of the examples where embedding a canvas app isn't supported:

| Canvas apps embedded to | Unsupported client |
| - | - |
| A SharePoint page that is added as a tab in a Microsoft Teams channel | <ul> <li> Teams desktop </li> <li> Teams mobile </li> </ul> |
| A Power BI report that is added to a Teams team, or a SharePoint site | <ul> <li> Teams desktop </li> <li> Teams mobile </li> <li> SharePoint mobile </li> </ul> |
| A model-driven form that is added to Teams | <ul> <li> Teams desktop </li> <li> Teams mobile </li> </ul> |

## Size limits

You can find information about size limits on text, hyperlinks, images, and media in [Data types](functions/data-types.md#text-hyperlink-image-and-media).

## Power Apps per app plan

Information is now available in the [Power Apps per app plan](/power-platform/admin/signup-for-powerapps-admin#power-apps-per-app-plan) section in the Power Platform admin guide.


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
