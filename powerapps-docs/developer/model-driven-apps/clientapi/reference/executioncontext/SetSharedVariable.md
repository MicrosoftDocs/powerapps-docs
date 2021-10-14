---
title: "setSharedVariable (Client API reference) in model-driven apps| MicrosoftDocs"
description: "Learn about the getEventSource method that returns a reference to the form or an item on the form depending on where the method was called." 
ms.date: 10/31/2018
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 702a13c1-f4ae-4de2-9e8b-95360ad9240c
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# setSharedVariable (Client API reference)



Sets the value of a variable to be used by a handler after the current handler completes.

## Syntax

`ExecutionContextObj.setSharedVariable(key, value)`

## Parameters

- **key**: String: The name of the variable
- **Value**: Object. The values to set



## Return value

**Type**: Object

**Description**: The specific type depends on what the value object is.

### Related topics
[getSharedVariable](getSharedVariable.md)

[Execution context](../execution-context.md)







[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]