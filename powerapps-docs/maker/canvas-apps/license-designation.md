---
title: License designation for an app | Microsoft Docs
description: Explains how to check license designation for the selected app
author: tapanm-msft
manager: kvivek
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: 
ms.date: 03/24/2020
ms.author: alaug
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---

# How to check license designation for an app

Starting October 2019, several connectors are reclassified from Standard to Premium.

[Power Apps licensing FAQ](https://docs.microsoft.com/power-platform/admin/powerapps-flow-licensing-faq#office-365) outlines
reclassified connectors. Apps using these connectors before the
reclassification have been granted an extended timeframe allowing users
without a premium license to access these apps.

The following table outlines the designations and which license an end user must have to access an app.

| **Designation​** | **Definition**
|-|-|
| Standard​ | An app that only uses standard connectors. An end user must have a Power Apps for Office 365 plan, per app plan, or a per user plan to access this app.
| Extended​ | An app allowed to use connectors promoted to premium on October 1, 2019.​ An end user must have a Power Apps for Office 365 plan, per app plan or per user plan. [Power Apps licensing FAQ](https://docs.microsoft.com/power-platform/admin/powerapps-flow-licensing-faq#office-365) outlines which connectors were promoted to premium on October 1, 2019.
| Premium​ | An app that uses at least one premium connector, a custom connector or an on-premise gateway. An end user must have a per app plan or per user plan to access.

## Check app license designation from app settings

1. Sign in to [Power Apps](https://make.powerapps.com).

1. Select **Apps** from left side.

1. Select an app from the list of app. You can use the **Settings** option from top or, use the **More Commands** (**...**) and then **Settings** from the drop-down menu:

    ![Settings option](media/license-designation/app-settings.png)

1. Select **Settings** to see the license designation information:

    ![License designation from settings](media/license-designation/settings-license-designation.png)

## Check app license designation from app details

1. Sign in to [Power Apps](https://make.powerapps.com).

1. Select **Apps** from left side.

1. Select an app from the list of app. You can use the **Details** option from top or, use the **More Commands** (**...**) and then **Details** from the drop-down menu:

    ![App details](media/license-designation/app-details.png)

1. Select **Details**:

    ![App designation in details](media/license-designation/app-details-page.png)

## Pass assignment

For information about Pass assignment, read [Power Apps per app
plans](https://docs.microsoft.com/power-platform/admin/about-powerapps-perapp#step-three-set-up-apps-to-use-per-app-plans).

## Next steps

- [Power Apps licensing FAQ](https://docs.microsoft.com/power-platform/admin/powerapps-flow-licensing-faq)

### See also

- [Edit an app](edit-app.md)
- [Delete an app](delete-app.md)
