---
title: RequestHide function in Power Apps
description: Reference information including syntax and examples for the RequestHide function in Power Apps.
author: emcoope-msft
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 06/18/2020
ms.subservice: canvas-maker
ms.author: emcoope
search.audienceType: 
  - maker
search.app: 
  - PowerApps
contributors:
  - gregli-msft
  - tapanm-msft
---

# RequestHide function in Power Apps

Hides the [SharePoint form](../sharepoint-form-integration.md#understand-the-sharepointintegration-control).

>[!NOTE]
> Only works with [SharePoint forms](../sharepoint-form-integration.md).

## Description

Use the **RequestHide** function to hide the SharePoint form. By default, RequestHide() is used for the *OnSuccess* property of a SharePoint form being customized.

![RequestHide example.](media/function-requesthide/requesthide-fuction.png)

This function is not required for the **SharePointIntegration** control's **OnCancel** event as SharePoint by default hides the form when a user selects **Cancel**, and the function only reacts to a SharePoint form.

## Syntax

**RequestHide** ( )

* No parameters.

## Examples

| Formula | Description |
| --- | --- |
| **RequestHide()** | Hides the form. |


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]