---
title: "disableAsyncTimeout  (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the disableAsyncTimeout method.
author: MitiJ
ms.author: mijosh
ms.date: 01/16/2024
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# disableAsyncTimeout (Client API reference)

[!INCLUDE[./includes/disableAsyncTimeout-description.md](./includes/disableAsyncTimeout-description.md)]

## Syntax

`executionContext.getEventArgs().disableAsyncTimeout()`

## Example

```javascript
async function myHandler(context) {  
     context.getEventArgs().disableAsyncTimeout();
     // The 10000ms time out will not be disabled if the above line does not come before all async awaits
     await Xrm.Navigation.openConfirmDialog({ text: "Are you sure you want to save?" });
 }
```


### Related articles

[getSaveMode](getSaveMode.md)  
[isDefaultPrevented](isDefaultPrevented.md)   
[preventDefault](preventDefault.md)   
[preventDefaultOnError](preventDefaultOnError.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
