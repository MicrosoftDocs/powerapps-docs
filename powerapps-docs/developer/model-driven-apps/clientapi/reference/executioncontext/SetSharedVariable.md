---
title: "setSharedVariable (Client API reference) in model-driven apps| MicrosoftDocs"
description: "Learn about the getEventSource method that returns a reference to the form or an item on the form depending on where the method was called." 
ms.author: jdaly
author: adrianorth
manager: kvivek
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors:
  - JimDaly
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