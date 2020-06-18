---
title: RequestHide function | Microsoft Docs
description: Reference information, including syntax and examples, for the RequestHide function in Power Apps
author: emcoope-msft
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 06/18/2020
ms.author: emcoope
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---

# RequestHide function in Power Apps

Hides the [SharePoint form](../sharepoint-form-integration.md#understand-the-sharepointintegration-control).

>[!NOTE]
> Only works with [SharePoint forms](../sharepoint-form-integration.md).

## Description

Use the **RequestHide** function to hide the SharePoint form. By default, RequestHide() is used for the *OnSuccess* property of a SharePoint form being customized.

![RequestHide example](media/function-requesthide/requesthide-fuction.png)

### Considerations

- Not required when using **SharePointIntegration** control actions such as **OnCancel** as SharePoint by default hides the form when a user selects **Cancel**, and the function only reacts to a SharePoint form.
- When using **RequestHide()** outside the context of a **SharePointIntegration** control, such as **OnSelect** for a button, won't return a formula error and the button **OnSelect** won't have any effect.

## Syntax

**RequestHide** ( )

* No parameters.

## Examples

| Formula | Description |
| --- | --- |
| **RequestHide()** | Hides the form. |
