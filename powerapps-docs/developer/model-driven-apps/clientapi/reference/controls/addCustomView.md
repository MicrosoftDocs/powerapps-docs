---
title: "addCustomView (Client API reference) in model-driven apps"
description: Adds a new view for the lookup dialog box.
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
# addCustomView (Client API reference)

Adds a new view for the lookup dialog box. 

## Control types supported

Lookup

## Syntax

`formContext.getControl(arg).addCustomView(viewId, entityName, viewDisplayName, fetchXml, layoutXml, isDefault)`

## Parameters

- **viewId**: String. The string representation of a GUID for a view.
    > [!NOTE]
    > This value is never saved and only needs to be unique among the other available views for the lookup. A string for a non-valid GUID will work, for example "00000000-0000-0000-0000-000000000001". It's recommended that you use a tool like **guidgen.exe** to generate a valid GUID.  

- **entityName**: String. The name of the table.
- **viewDisplayName**: String. The name of the view.
- **fetchXml**: String. The fetchXml query for the view.
- **layoutXml**: String. The XML that defines the layout of the view.
- **isDefault**: Boolean: Indicates whether the view should be the default view.

[!INCLUDE[cc-terminology](../../../../data-platform/includes/cc-terminology.md)]

## Remarks

This method doesn't work with **Owner** lookups. Owner lookups are used to assign user-owned records.


[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
