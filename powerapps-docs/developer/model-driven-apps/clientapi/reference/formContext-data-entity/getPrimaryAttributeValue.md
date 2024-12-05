---
title: "entity.getPrimaryAttributeValue (Client API reference) in model-driven apps"
description: Gets a string for the value of the primary column of the table.
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
# entity.getPrimaryAttributeValue (Client API reference)



[!INCLUDE[./includes/getPrimaryAttributeValue-description.md](./includes/getPrimaryAttributeValue-description.md)]

## Syntax

`formContext.data.entity.getPrimaryAttributeValue();`

[!INCLUDE[cc-terminology](../../../../data-platform/includes/cc-terminology.md)]

## Return Value

**Type**: String.

**Description**: The name of the table.

## Remarks

Each table has one string column that is designated as the <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.PrimaryNameAttribute>. The value for this column is used when links to the record are displayed.

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
