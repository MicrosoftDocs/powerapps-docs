---
title: Manage your mobile app with Microsoft Intune| Microsoft Docs
description: Manage mobile app with Microsoft Intune.
author: trdehove
ms.component: pa-user
ms.topic: quickstart
ms.date: 10/11/2024
ms.subservice: mobile
ms.author: trdehove
ms.custom: ""
ms.reviewer: smurkute
ms.assetid: 
search.audienceType: 
  - enduser
searchScope:
  - "Power Apps"
---

# Manage your mobile app with Microsoft Intune

Mobile application management software enables IT administrators to apply and enforce corporate policies on mobile apps. One mobile application management option for IT administrators is Microsoft Intune, which offers a suite of features that lets you publish, push, configure, secure, monitor, and update mobile apps - including Power Apps mobile, [Dynamics 365 Sales Mobile](/dynamics365/sales/sales-mobile/dynamics-365-sales-mobile-app), and [Field Service Mobile](/dynamics365/field-service/field-service-mobile-app-user-guide).
Mobile application management is essential to organizations whose users use mobile app primarily because:

1. Users frequently travel to multiple locations, and protecting sensitive company data is critical.
2. Many organizations have a bring-your-own-device policy, which means that the mobile app needs management among many devices and apps for personal use.

With an Intune-enabled mobile app, IT administrators can:

- Add and assign the mobile app to user groups and devices, including users in specific groups, devices in particular groups, and more.
- See reports and track app usage.
- Limit sharing of corporate data among apps by restricting data leakage through cut, copy, paste, and save-as.
- Provide encryption at rest.

Intune is a separate Microsoft product that is not included with Power Apps mobile. Refer to the documentation on [What is Microsoft Intune app management?](/mem/intune/apps/app-management) and [Assign apps to groups with Microsoft Intune](/mem/intune/apps/apps-deploy) to get started.

A configuration can be set up through the [Device Management portal](https://devicemanagement.microsoft.com/). Each supported platform (iOS, Android, and Windows) requires a separate configuration.

## Enhanced security support in Intune

Intune advanced app settings aren't currently supported with Power Apps Mobile. However, organization admins and makers have complete control over authentication, user access, managing sensitive data access, configuring notifications, setting data sync policies across sources, and defining access to organizational data and documents, through combination of Power Platform environment settings and Azure conditional access policies.
