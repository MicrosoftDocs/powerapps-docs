---
title: "addOnChange (Client API reference) in model-driven apps"
description: "Learn about the column addOnchange method to set a function to be called when the column value is changed." 
author: clromano
ms.author: clromano
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
ms.subservice: mda-developer
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# addOnChange (Client API reference)


Sets a function to be called when the **OnChange** event occurs.

> [!NOTE]
> If the `addOnChange` method is used on the form `OnLoad` event handler, you should ensure that it's called when necessary. You can use the [getEventArgs](../executioncontext/getEventArgs.md) to conditionally call the `addOnChange` method based on the data load state.

## Column types supported

All

## Syntax

`formContext.getAttribute(arg).addOnChange(myFunction)`

## Parameters

| Parameter Name| Type| Description  |
| --------|-----------| -----|
|`myFunction`| Function reference| Specifies the function to be executed on the column **OnChange** event. The [execution context](../../clientapi-execution-context.md) is automatically passed as the first parameter to this function.|


### Related articles

[removeOnChange](removeOnChange.md)   
[Column OnChange Event](../events/attribute-onchange.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
