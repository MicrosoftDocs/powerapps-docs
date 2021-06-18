---
title: "Understanding the information returned from performance insights in Power Apps | MicrosoftDocs"
description: Understand the information returned with performance insights. 
ms.custom: ""
ms.date: 06/15/2021
ms.reviewer: ""
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "overview"
applies_to: 
  - "powerapps"
author: "Mattp123"
ms.author: "matp"
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Understanding insights

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

Performance insights distributes insights into the following categories: 
- [Overall performance](#overall-performance)
- [Client environment](#client-environment)
- [Usage pattern](#usage-pattern)
- [Page performance](#page-performance)
- [Customization](#customization)
- [Configuration](#configuration)
- [Network](#network)

## Overall performance

This insight summarizes the overall performance of your app as an executive summary under the Insight ID Perf.Summary.Overview. 

In this insight, you can see the overall performance of your app based on the severity. 
- **Critical**: Indicates poor performance.
- **Warning**: Indicates performance could be improved.
- **Informational**: Indicates good performance.

### How to improve

When it comes time to optimize the app, you can look at the detailed insights from the client, network, customization categories as well as plugins, savedQeury, and settings. Some actionable items can be derived by reviewing those insights. 

## Client environment

When users experience a Power Apps app on their devices, several factors can affect performance such as browser type, browser version, and specification of hardware. In this section, you can see what insights check client environments.  

### Browser type 

Insight ID: Perf.Environment.Client.Browser.Type 

#### Description 

Certain web browser types can impact the performance of your app. Using unsupported or non-modern browsers can lead to slow performance. This insight provides the performance implications of different browsers, especially non-recommended browsers. For example, [Power Apps has deprecated it's support of Internet Explorer](/power-platform/important-changes-coming#internet-explorer-11-support-for-dynamics-365-and-microsoft-power-platform-is-deprecated). 

#### How to improve 

If you have users on old browsers such as Internet Explorer, switch to a modern Chromium based browser. We recommend that users run a modern browser, such as [Microsoft Edge](https://www.microsoft.com/edge?form=MY01BL&OCID=MY01BL&r=1) or Google Chrome.

> [!NOTE]
> Some legacy applications leveraging NPAPI will only work on Internet Explorer. 

### Browser version 

Insight ID: Perf.Environment.Client.Browser.Version 

#### Description 

This insight checks how many users are using your app from an old version of a browser. Even if users are on modern browsers, and not on non-recommended browser types like Internet Explorer, older versions of browsers perform slower.

#### How to improve 

Users should regularly update the browser to the latest version. Enterprise customers can apply a group policy to be on a specific version. As Unified Service Desk (USD) also uses the default browser setting of the machine, it also requires checking the default browser type and version. 

### Minimum system requirements 

Insight ID: Perf.Environment.Device.MimimumRequirements 

#### Description 

This insight checks whether the user’s environment meets minimum system requirements. You can check the [web application requirements](/en-us/power-platform/admin/web-application-requirements) to see what are the minimum system requirements depending on the app type.  

In general, some activities like rendering, scripting, and downloading contents happen on the client side. Meeting the minimum system requirements is necessary for such activities.  

#### How to improve 

Users should use the hardware that meets or exceeds the minimum system requirements for Power Apps.  

### HTTP protocol

Insight ID: Perf.Environment.Client.Browser.HttpProtocol 
 
#### Description 

Power Apps platform supports HTTP/2. However, if your app is using the HTTP/1.1 protocol for XHR requests onto Power Apps, it might cause slow performance due to the concurrent limitation of requests with the HTTP/1.1 protocol. 

#### How to improve

If this insight identified some users who are using the HTTP/1.1 protocol, we strongly recommend that these user’s client should support the HTTP/2 protocol.  

Several configurations and network infrastructure can block the HTTP/2 protocol, such as a VPN network, proxy server, or device internet option settings.  

Users can simply check out what protocol has been used from a dev tool of a browser. As you can see the figure below, network calls happened over HTTP/2


## Usage pattern


## Page performance

## Customization

## Configuration

## Network

