---
title: "addOnChange (Client API reference) in model-driven apps| MicrosoftDocs"
description: "Learn about the attribute addOnchange method to set a function to be called when the attribute value is changed." 
ms.date: 10/31/2017
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 9f3b2fed-fde5-46e4-8c59-43aa51aa82df
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
---
# addOnChange (Client API reference)



Sets a function to be called when the **OnChange** event occurs.

## Attribute types supported

All

## Syntax

`formContext.getAttribute(arg).addOnChange(myFunction)`

## Parameters

| Parameter Name| Type| Description  |
| --------|-----------| -----|
|myFunction| Function reference| Specifies the function to be executed on the attribute **OnChange** event. The [execution context](../../clientapi-execution-context.md) is automatically passed as the first parameter to this function.|


### Related topics

[removeOnChange](removeOnChange.md)

[Attribute OnChange Event](../events/attribute-onchange.md)





