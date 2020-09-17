---
title: System requirements, limits, and configuration values for canvas apps | Microsoft Docs
description: System requirements, limits, and configuration values for canvas apps built in Power Apps
author: lancedMicrosoft
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 09/14/2020
ms.author: gregli
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# System requirements, limits, and configuration values for canvas apps
This topic contains device platform and web browser requirements, as well as limits and configuration values for canvas apps.

## Supported platforms for running canvas apps using the Power Apps mobile app

| **Minimum required** | **Recommended** |
| --- | --- |
| iOS 12 or later |iOS 12 or later|
| Android 7 or later |Android 7 or later |
| Windows 8.1 or later (PC only) |Windows 10 Fall Creators Update with at least 8 GB of RAM)|

> [!NOTE]
> - After October 16, 2020 we will no longer support iOS 12. After October 16, 2020 iOS 13 or later will be supported. 
> - We currently don't support new features on Windows platform for [Power Apps mobile app](/powerapps/user/run-app-client). Features such as the Improved Common Data Service option and guest access are not available on this platform. We recommend using a web player on Windows to leverage the full set of capabilities. Updates to the Power Apps mobile app for Windows platform will be announced in future.

## Supported browsers for running canvas apps

| **Browser** | **Operating system** |
| --- | --- |
| Google Chrome (latest version)<br>(recommended) |Windows 7 SP1, 8.1, and 10 <br>Android 5 or later <br>iOS 8 or later<br>macOS |
| Microsoft Edge (latest version)<br>(recommended) |Windows 10 |
| Microsoft Internet Explorer 11 (with Compatibility View off) |Windows 7 SP1, 8.1, and 10 |
| Mozilla Firefox (latest version) |Windows 7 SP1, 8.1, and 10 <br> Android 5 or later <br>iOS 8 or later <br>macOS |
| Apple Safari (latest version) |iOS 8 or later <br>macOS |

## Supported browsers for Power Apps Studio

| **Browser** | **Operating system** |
| --- | --- |
| Google Chrome (latest version)<br>(recommended) |Windows 7 SP1, 8.1, and 10 <br>macOS |
| Microsoft Edge (latest version)<br>(recommended) |Windows 10 |
| Microsoft Internet Explorer 11 (with Compatibility View off) |Windows 7 SP1, 8.1, and 10 |

## Request limits
These limits apply to each single outgoing request:

| Name | Limit |
| --- | --- |
| Timeout |180 Seconds |
| Retry attempts |4 |

> [!NOTE]
> The retry value may vary. For certain error conditions, it's not necessary to retry.

## IP addresses
Requests from Power Apps use IP addresses that depend on the region of the [environment](../../administrator/environments-overview.md) that the app is in. We don't publish fully qualified domain names available for Power Apps scenarios.

Calls made from an API connected through an app (for example, the SQL API or the SharePoint API) come from the IP address specified later in this topic.

You should use these addresses if, for example, you must allow IP addresses for an Azure SQL database.

> [!IMPORTANT]
> If you have existing configurations, please update them as soon as possible before September 30, 2018 so they include and match the IP addresses in this list for the regions where your Power Apps apps exist.

| Region | Outbound IP |
| --- | --- |
| Asia | 13.75.36.64 - 13.75.36.79, 13.67.8.240 - 13.67.8.255, 52.175.23.169, 52.187.68.19, 104.214.164.0 - 104.214.164.31, 13.67.15.32 - 13.67.15.63, 20.44.29.64 - 20.44.29.95, 40.79.189.64 - 40.79.189.95, 40.80.180.64 - 40.80.180.95, 52.231.148.224 - 52.231.148.255, 127.0.0.1 |
| Australia  | 13.70.72.192 - 13.70.72.207, 13.72.243.10, 13.77.50.240 - 13.77.50.255, 13.70.136.174, 13.70.78.224 - 13.70.78.255, 13.77.55.160 - 13.77.55.191, 127.0.0.1 |
| Brazil | 191.233.203.192 - 191.233.203.207, 104.214.19.48 - 104.214.19.63, 13.65.86.57, 104.41.59.51, 191.233.207.160 - 191.233.207.191, 127.0.0.1 |
| Canada | 13.71.170.208 - 13.71.170.223, 13.71.170.224 - 13.71.170.239, 52.237.24.126, 40.69.106.240 - 40.69.106.255, 52.242.35.152, 13.71.175.160 - 13.71.175.191, 13.71.170.224 - 13.71.170.239, 40.69.111.0 - 40.69.111.31, 127.0.0.1|
| Europe | 13.69.227.208 - 13.69.227.223, 52.178.150.68, 13.69.64.208 - 13.69.64.223, 52.174.88.118, 137.117.161.181, 13.69.231.192 - 13.69.231.223, 13.69.71.192 - 13.69.71.223, 40.79.148.96 - 40.79.148.127, 40.79.180.224 - 40.79.180.255, 51.107.59.16 - 51.107.59.31, 51.107.60.224 - 51.107.60.255, 51.107.86.217, 127.0.0.1|
| India  | 104.211.81.192 - 104.211.81.207, 52.172.211.12, 40.78.194.240 - 40.78.194.255, 13.71.125.22, 104.211.146.224 - 104.211.146.239, 104.211.189.218, 20.38.128.224 - 20.38.128.255, 20.43.123.0 - 20.43.123.31, 127.0.0.1 |
| Japan | 13.78.108.0 - 13.78.108.15, 13.71.153.19, 40.74.100.224 - 40.74.100.239, 104.215.61.248, 127.0.0.1 |
| South America | 191.233.203.192 - 191.233.203.207, 104.214.19.48 - 104.214.19.63, 13.65.86.57, 104.41.59.51, 127.0.0.1 |
| United Arab Emirates | 20.45.67.28, 127.0.0.1 |
| United Kingdom | 51.140.148.0 - 51.140.148.15, 51.140.80.51, 51.140.211.0 - 51.140.211.15, 51.141.47.105, 51.105.77.96 - 51.105.77.127, 51.140.212.224 - 51.140.212.255, 127.0.0.1 |
| United States | 13.89.171.80 - 13.89.171.95, 52.173.245.164, 40.71.11.80 - 40.71.11.95, 40.71.249.205, 40.70.146.208 - 40.70.146.223, 52.232.188.154, 52.162.107.160 - 52.162.107.175, 52.162.242.161, 40.112.243.160 - 40.112.243.175, 104.42.122.49, 13.66.145.96 - 13.66.145.127, 13.71.199.192 - 13.71.199.223, 13.73.244.224 - 13.73.244.255, 13.86.223.32 - 13.86.223.63, 13.89.178.64 - 13.89.178.95, 40.70.151.96 - 40.70.151.127, 40.71.15.160 - 40.71.15.191, 52.162.111.192 - 52.162.111.223, 127.0.0.1 |
| United States (Early Access)  | 13.71.195.32 - 13.71.195.47, 52.161.102.22, 13.66.140.128 - 13.66.140.143, 52.183.78.157, 127.0.0.1 |
| United States Government (GCC) | 20.140.137.128 - 20.140.137.159, 52.127.5.224 - 52.127.5.255, 127.0.0.1 |
| Department of Defense (DoD) in Azure Government | 52.127.61.192 - 52.127.61.223, 127.0.0.1  |

## Required services
This list identifies all services to which Power Apps Studio talks and their usages. Your network must **not** block these services.

| Domain(s) | Protocols | Uses |
| --- | --- | --- |
| api.bap.microsoft.com<br/>api.businessappdiscovery.microsoft.com | https | Environment permissions management|
| management.azure.com |https |RP |
| msmanaged-na.azure-apim.net |https |Runtime of Connectors/Apis |
| login.microsoft.com<br>login.windows.net<br>login.microsoftonline.com<br>secure.aadcdn.microsoftonline-p.com |https |ADAL |
| graph.microsoft.com<br>graph.windows.net |https |Azure Graph - For getting user info (e.g., profile photo) |
| gallery.azure.com |https |Sample and Template apps |
| \*.azure-apim.net |https |Api Hubs - Different sub-domains for each locale |
| \*.powerapps.com |https | create.powerapps.com, make.powerapps.com, content.powerapps.com,apps.powerapps.com, and make.powerapps.com |
| \*.azureedge.net |https | create.powerapps.com, make.powerapps.com, content.powerapps.com, and make.powerapps.com |
| \*.blob.core.windows.net |https | Blob storage |
| \*.flow.microsoft.com | https | create.powerapps.com, make.powerapps.com, content.powerapps.com, and make.powerapps.com |
| \*.dynamics.com | https | Common Data Service |
| vortex.data.microsoft.com |https |Telemetry |
| localhost | https | Power Apps Mobile|


> [!NOTE]
> If you're using a VPN, it must be configured to exclude localhost from tunneling for Power Apps Mobile.

## Size limits

You can find information about size limits on text, hyperlinks, images, and media in [Data types](functions/data-types.md#text-hyperlink-image-and-media).

## Power Apps per app plan

The information is now available in [Power Apps per app plan](/power-platform/admin/signup-for-powerapps-admin#power-apps-per-app-plan) section in the Power Platform admin guide.
