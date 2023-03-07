---
title: "isOnPremises (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the isOnPremises method.
author: adrianorth
ms.author: aorth
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors:
  - JimDaly
---
# isOnPremises (Client API reference)



Returns a boolean value indicating if the model-driven apps instance is hosted on-premises or online. 

## Syntax

```JavaScript
var globalContext = Xrm.Utility.getGlobalContext();
globalContext.isOnPremises();
```

## Return Value

**Type**: Boolean

**Description**: **true** if the model-driven apps instance is on-premises; **false** otherwise.

### Related topics

[Xrm.Utility.getGlobalContext](../getGlobalContext.md)





[!INCLUDE[footer-include](../../../../../../includes/footer-banner.md)]
