---
title: "getSharedVariable (Client API reference) in model-driven apps| MicrosoftDocs"
description: "Describes the getSharedVariable function used with the client api in model-driven apps."
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
# getSharedVariable (Client API reference)



Retrieves a variable set using the [setSharedVariable](setSharedVariable.md) method.

## Syntax

`ExecutionContextObj.getSharedVariable(key)`

## Parameters

**key**

   **Type**: String

   **Description**: The name of the variable.

## Return value

**Type**: Object

**Description**: The specific type depends on what the value object is.

### Related topics
[setSharedVariable](setSharedVariable.md)

[Execution context](../execution-context.md)







[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]