---
title: System requirements, limits, and configuration values | Microsoft Docs
description: System requirements, limits, and configuration values for PowerApps
services: ''
suite: PowerApps
documentationcenter: na
author: skjerland
manager: kfile
editor: ''
tags: ''

ms.service: PowerApps
ms.devlang: na
ms.topic: article
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 03/07/2018
ms.author: sharik

---
# System requirements, limits, and configuration values
This topic contains device platform and browser requirements, as well as current limits and configuration values for PowerApps.

## Supported device platforms
* iOS 9.3 or later (recommended: iOS 10 or later with at least 2GB of RAM)
* Android 5 or later (recommended: Android 7 or later with at least 4GB of RAM)
* Windows 7 SP1 or later (recommended: Windows 10 Fall Creators Update with at least 8 GB of RAM)

## Supported web browsers
| **Browser** | **Operating system** |
| --- | --- |
| Google Chrome (latest version)<br>(recommended) |Windows 7 SP1, 8.1, and 10 <br>macOS <br>iOS 8 or later<br>Android |
| Microsoft Edge (latest version)<br>(recommended) |Windows 10 |
| Microsoft Internet Explorer 11 (with Compatibility View off) |Windows 7 SP1, 8.1, and 10 |
| Mozilla Firefox (latest version) |Windows 7 SP1, 8.1, and 10 <br> Android <br>macOS |
| Apple Safari (latest version) |macOS <br> iOS 8 or later |

## Request limits
These limits apply to each single outgoing request:

| Name | Limit |
| --- | --- |
| Timeout |180 Seconds |
| Retry attempts |4 |

> [!NOTE]
> The retry value may vary. For certain error conditions, it doesn't make sense to retry.

## IP addresses
Requests from PowerApps use IP addresses that depend on the region of the [environment](../administrator/environments-overview.md) that the app is in. We don't publish fully qualified domain names available for PowerApps scenarios.

Calls made from an API connected through an app (for example, the SQL API or the SharePoint API) come from the IP address specified later in this topic.

You should use these addresses if, for example, you must whitelist IP addresses for an Azure SQL database.

| Region | Outbound IP |
| --- | --- |
| Asia |52.163.91.227, 52.163.89.40, 52.163.89.65, 52.163.95.29, 13.75.89.9, 13.75.91.198, 13.75.92.202, 13.75.92.124 |
| Australia |13.77.7.172, 13.70.191.49, 13.70.189.7, 13.70.187.251, 13.70.82.210, 13.73.203.158, 13.73.207.42, 13.73.205.35 |
| Canada |52.233.30.222, 52.233.30.148, 52.233.30.199, 52.233.29.254, 52.232.130.205, 52.229.126.118, 52.229.126.28, 52.229.123.56 |
| Europe |52.166.241.149, 52.166.244.232, 52.166.245.173, 52.166.243.169, 40.69.45.126, 40.69.45.11, 40.69.45.93, 40.69.42.254 |
| India |52.172.54.172, 52.172.55.107, 52.172.55.84, 52.172.51.70, 52.172.158.185, 52.172.159.100, 52.172.158.2, 52.172.155.245 |
| Japan |104.214.137.186, 104.214.139.29, 104.214.140.23, 104.214.138.174, 13.78.85.193, 13.78.84.73, 13.78.85.200, 13.78.86.229 |
| United States |104.43.232.28, 104.43.232.242, 104.43.235.249, 104.43.234.211, 52.160.93.247, 52.160.91.66, 52.160.92.131, 52.160.95.100, 40.117.101.91, 40.117.98.246, 40.117.101.120, 40.117.100.191 |
| United States (Early Access) |52.161.26.191, 52.161.27.42, 52.161.29.40, 52.161.26.33, 13.66.213.240, 13.66.214.51, 13.66.210.166, 13.66.213.29 |

## Required services
This list identifies all services to which PowerApps Studio talks and their usages. Your network must **not** block these services.

| Domain(s) | Protocols | Uses |
| --- | --- | --- |
| management.azure.com |https |RP |
| msmanaged-na.azure-apim.net |https |Runtime of Connectors/Apis |
| login.microsoft.com<br>login.windows.net<br>login.microsoftonline.com<br>secure.aadcdn.microsoftonline-p.com |https |ADAL |
| graph.microsoft.com<br>graph.windows.net |https |Azure Graph - For getting user info (e.g. profile photo) |
| gallery.azure.com |https |Sample and Template apps |
| *.azure-apim.net |https |Api Hubs - Different sub-domains for each locale |
| *.powerapps.com |https |WebAuth + Portal |
| *.azureedge.net |https |WebAuth |
| *.blob.core.windows.net |https |Blob storage |
| vortex.data.microsoft.com |https |Telemetry |
