---
title: "Transistion your legacy web client app to unified interface | MicrosoftDocs"
description: "Learn how to transistion your web client app to unified interface"
ms.custom: ""
ms.date: 07/08/2019
ms.reviewer: ""
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "powerapps"
author: "Mattp123"
ms.assetid: 14c4c18c-927c-4ea2-ba66-0531285a99a7
caps.latest.revision: 25
ms.author: "matp"
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---
# Transistion your legacy web client app to unified interface

This topic explains how to transition your legacy web client app to unified interface. The Unified interface framework uses responsive web design principles to provide an optimal viewing and interaction experience for any screen size, device, or orientation. 

## Prerequisites
- A legacy web client app. 
- Although not required, we recommend a non-production environment to test your app and ensure it does not impact your current deployment or development cycles. More information: [Manage sandbox instances](/dynamics365/customer-engagement/admin/manage-sandbox-instances)

## Create the environment
First, create a new sandbox environment and enable **Unified Interface Only** mode, which will use Unified Interface for all model-driven apps in the environment. This also includes any Dynamics 365 for Customer Engagement application modules originally configured for the web client.

1. Go to the [Power Platform Admin center](https://admin.powerplatform.microsoft.com/), select **Environments**, and then select an environment. 
2. Go to **Settings** > **Behavior** > **Interface settings** and then select **Use Unified Interface only**.

> [!NOTE]
> If you need to switch the environment back to its original state you can toggle the unified interface setting to revert to the original interface. More information: [Enable Unified Interface Only](/dynamics365/customer-engagement/admin/enable-unified-interface-only)


## Review your app in the Unified Interface
Run your app that was originally legacy web client. Notice that, after you turn on **Unified Interface Only**, all available apps in the environment will use Unified Interface even if an app is configured for Unified Interface or legacy web client.


