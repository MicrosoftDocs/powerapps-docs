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

If you have users on old browsers such as Internet Explorer, switch to a modern Chromium based browser, such as and therefore, we recommend that users run a modern browser, such as Microsoft Edge or Google Chrome.

## Usage pattern

## Page performance

## Customization

## Configuration

## Network

