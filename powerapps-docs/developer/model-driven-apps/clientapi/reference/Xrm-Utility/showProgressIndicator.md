---
title: "showProgressIndicator (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the showProgressIndicator method.
author: sriharibs-msft
ms.author: srihas
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# showProgressIndicator (Client API reference)



[!INCLUDE[./includes/showProgressIndicator-description.md](./includes/showProgressIndicator-description.md)]

Any subsequent call to this method will update the displayed message in the existing progress dialog with the message specified in the latest method call.

>[!NOTE]
>Although the showProgressIndicator function is synchronous, the UI updates asynchronously. This means that any code synchronously executed immediately after calling showProgressIndicator may execute before the progress indicator is shown in the UI.

>[!WARNING]
>The progress dialog blocks the UI until it is closed using the [closeProgressIndicator](closeProgressIndicator.md) method. So, you must use this method with caution.

## Syntax

`Xrm.Utility.showProgressIndicator(message)`

## Parameters 

|Name |Type |Required |Description |
|---|---|---|---|
|`message`|String|Yes|The message to be displayed in the progress dialog.|



### Related articles

[closeProgressIndicator](closeProgressIndicator.md)

[Xrm.Utility](../xrm-utility.md)  





[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
