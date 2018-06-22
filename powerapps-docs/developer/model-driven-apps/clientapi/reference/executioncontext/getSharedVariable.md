---
title: "getSharedVariable (Client API reference) in Dynamics 365 Customer Engagement| MicrosoftDocs" 
ms.date: 10/31/2017
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 702a13c1-f4ae-4de2-9e8b-95360ad9240c
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
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





