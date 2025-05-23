---
title: "preventDefault (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the preventDefault method.
author: MitiJ
ms.author: mijosh
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# preventDefault (Client API reference)

[!INCLUDE[./includes/preventDefault-description.md](./includes/preventDefault-description.md)]

## Syntax

`executionContext.getEventArgs().preventDefault();`

> [!IMPORTANT]
> When you use `preventDefault` on a form with business process flows, the stage navigation may throw this error: **Unable to save form data due to web resource registered onSave invoking preventDefault**. Use [`OnPreStageChange`](../events/onprestagechange.md) to prevent this error. 

### Related articles

[getSaveMode](getSaveMode.md)   
[isDefaultPrevented](isDefaultPrevented.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
