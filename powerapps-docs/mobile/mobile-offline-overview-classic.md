---
title: Mobile offline overview (classic)
ms.custom: Configure mobile offline synchronization
description: Set up mobile offline for Power Apps
ms.date: 10/13/2022
ms.reviewer: sericks

ms.suite: 
ms.tgt_pltfrm: 
ms.topic: article
applies_to: Dynamics 365 apps
ms.assetid: 7f992860-8c7b-48ba-806a-63a3634d209d
caps.latest.revision: 1
ms.author: trdehove
author: trdehove
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Mobile offline overview (classic)

Set up mobile offline synchronization to allow users to work in offline mode on their mobile device. Mobile offline allows users to use Power Apps in offline mode and interact with their data without an internet connection.

The mobile app provides a rich offline experience that helps users stay productive. You can use basic commands such as create, read, update, and delete when you're offline. Once you're back online, the changes that you made on the mobile app are automatically synchronized with Microsoft Dataverse.
  
The offline experience uses [!INCLUDE[pn_Windows_Azure](../includes/pn-windows-azure.md)] services to periodically synchronize tables with the mobile app so that synchronized rows are available when a user's mobile devices is disconnected from the internet. 

Before you set-up the mobile app in offline mode, be sure to review [Mobile offline capabilities and limitations](offline-capabilities.md).

> [!IMPORTANT]
> - To use this feature, an administrator must set up mobile offline for their organization. The set up and configuration process for mobile offline is the same for [Power Apps mobile](/powerapps/mobile/run-powerapps-on-mobile) and Dynamics 365 for phones and tablets app. To enable mobile offline synchronization for Power Apps mobile or Dynamics 365 mobile, follow the steps in [Set up mobile offline (classic)](setup-mobile-offline-classic.md).
> - There is a new mobile offline experience for model-driven apps. For more information, see [Mobile offline overview (preview)](/powerapps/mobile/work-in-offline-mode).

