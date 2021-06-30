---
title: System requirements, limits, and configuration values for canvas apps
description: Learn about system requirements, limits, and configuration values for canvas apps built in Power Apps.
author: lancedMicrosoft
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 06/22/2021
ms.author: gregli
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# System requirements, limits, and configuration values for canvas apps
This article contains device platform and web browser requirements, limits, and configuration values for canvas apps.

## Supported platforms for running canvas apps using the Power Apps mobile app

| **Minimum required** | **Recommended** |
| --- | --- |
| iOS 12 or later |iOS 12 or later|
| Android 7 or later |Android 7 or later |
| Windows 8.1 or later (PC only) |Windows 10 Fall Creators Update with at least 8 GB of RAM)|

> [!NOTE]
> - On October 16, 2020 we will no longer support iOS 12. After October 16, 2020 iOS 13 or later will be supported. 
> - We currently don't support new features on Windows platform for [Power Apps mobile app](/powerapps/maker/canvas-apps/run-canvas-and-model-apps-on-mobile). Features such as the Improved Microsoft Dataverse option, and guest access are not available on this platform. We recommend using a web player on Windows to leverage the full set of capabilities. Updates to the Power Apps mobile app for Windows platform will be announced in future.
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

Calls made from an API connected through an app (for example, the SQL API or the SharePoint API) come from the IP address specified later in this article.

For example, use these addresses when you must allow IP addresses for an Azure SQL database.

| Region | Outbound IP |
| --- | --- |
| Asia | 13.75.113.224, 52.187.147.27, 52.175.23.169, 52.187.68.19, 13.75.36.64 - 13.75.36.79, 104.214.164.0 - 104.214.164.31, 13.67.8.240 - 13.67.8.255, 13.67.15.32 - 13.67.15.63 |
| Australia  | 13.75.139.0, 13.77.45.34, 13.72.243.10, 13.70.136.174, 13.70.72.192 - 13.70.72.207, 13.70.78.224 - 13.70.78.255, 13.77.50.240 - 13.77.50.255, 13.77.55.160 - 13.77.55.191 |
| Brazil | 191.234.180.112, 104.214.107.148, 104.41.59.51, 191.233.203.192 - 191.233.203.207, 191.233.207.160 - 191.233.207.191 |
| Canada | 52.242.36.40, 40.85.206.95, 52.237.24.126, 52.242.35.152, 40.69.106.240 - 40.69.106.255, 40.69.111.0 - 40.69.111.31, 13.71.170.208 - 13.71.170.223, 13.71.175.160 - 13.71.175.191 |
| Europe |  52.169.216.196, 40.89.131.3, 52.174.180.160, 52.178.150.68, 94.245.91.93, 52.174.88.118, 40.91.208.65, 137.117.161.181, 13.69.171.0, 13.69.227.208 - 13.69.227.223, 13.69.231.192 - 13.69.231.223, 13.69.64.208 - 13.69.64.223, 13.69.71.192 - 13.69.71.223 |
| France | 40.89.155.59, 40.89.135.2, 52.136.133.184, 40.79.130.208 - 40.79.130.223, 40.79.148.96 - 40.79.148.127, 40.79.178.240 - 40.79.178.255, 40.79.180.224 - 40.79.180.255 |
| Germany | 51.116.211.212, 51.116.236.78, 51.116.155.80 - 51.116.155.95, 51.116.158.96 - 51.116.158.127, 51.116.59.16 - 51.116.59.31, 51.116.60.192 - 51.116.60.223 |
| India | 13.71.127.169, 13.71.30.211, 52.172.211.12, 13.71.125.22, 104.211.189.218, 20.192.184.32 - 20.192.184.63, 40.78.194.240 - 40.78.194.255, 20.38.128.224 - 20.38.128.255, 104.211.146.224 - 104.211.146.239, 20.43.123.0 - 20.43.123.31, 104.211.81.192 - 104.211.81.207 |
| Japan | 104.215.28.128, 13.71.128.159, 13.71.153.19, 104.215.61.248, 40.74.100.224 - 40.74.100.239, 40.80.180.64 - 40.80.180.95, 13.78.108.0 - 13.78.108.15, 40.79.189.64 - 40.79.189.95 |
| Switzerland | 51.103.143.163, 51.107.86.217, 51.107.231.190, 51.107.59.16 - 51.107.59.31, 51.107.60.224 - 51.107.60.255, 51.107.155.16 - 51.107.155.31, 51.107.156.224 - 51.107.156.255 |
| United Arab Emirates | 20.45.67.36, 20.45.67.28, 20.37.74.192 - 20.37.74.207, 40.119.162.44, 40.120.8.0 - 40.120.8.31 |
| United Kingdom | 51.140.77.227, 51.140.245.29, 51.140.80.51, 51.140.61.124, 51.141.47.105, 51.141.124.13, 51.105.77.96 - 51.105.77.127, 51.140.148.0 - 51.140.148.15, 51.140.211.0 - 51.140.211.15, 51.140.212.224 - 51.140.212.255 |
| United States (Early Access)  | 13.78.178.187, 52.151.42.172, 52.161.102.22, 13.78.132.82, 52.183.78.157, 13.71.195.32 - 13.71.195.47, 13.71.199.192 - 13.71.199.223, 13.66.140.128 - 13.66.140.143, 13.66.145.96 - 13.66.145.127 |
| United States | 104.41.132.180, 13.91.93.63, 52.173.245.164, 40.71.249.205, 40.114.40.132, 52.232.188.154, 104.209.247.23, 52.162.242.161, 104.42.122.49, 40.112.195.87, 13.91.97.196, 40.71.193.203, 104.210.14.156, 13.66.130.243, 65.52.197.64, 40.113.242.246, 40.71.11.80 - 40.71.11.95, 40.71.15.160 - 40.71.15.191, 52.162.107.160 - 52.162.107.175, 52.162.111.192 - 52.162.111.223, 13.89.171.80 - 13.89.171.95, 13.89.178.64 - 13.89.178.95, 40.70.146.208 - 40.70.146.223, 40.70.151.96 - 40.70.151.127, 13.86.223.32 - 13.86.223.63, 40.112.243.160 - 40.112.243.175 |
| United States Government (GCC) | 20.140.137.128 - 20.140.137.159, 52.127.5.224 - 52.127.5.255, 127.0.0.1 |
| Department of Defense (DoD) in Azure Government | 52.127.61.192 - 52.127.61.223, 127.0.0.1 |

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


> [!NOTE]
> If you're using a VPN, it must be configured to exclude localhost from tunneling for Power Apps Mobile.

## Size limits

You can find information about size limits on text, hyperlinks, images, and media in [Data types](functions/data-types.md#text-hyperlink-image-and-media).

## Power Apps per app plan

The information is now available in [Power Apps per app plan](/power-platform/admin/signup-for-powerapps-admin#power-apps-per-app-plan) section in the Power Platform admin guide.


[!INCLUDE[footer-include](../../includes/footer-banner.md)]