---
title: "getDataXml (Client API reference) in model-driven apps"
description: Returns a string representing the XML that will be sent to the server when the record is saved.
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
# getDataXml (Client API reference)



[!INCLUDE[./includes/getDataXml-description.md](./includes/getDataXml-description.md)]

## Syntax

`formContext.data.entity.getDataXml();`

[!INCLUDE[cc-terminology](../../../../data-platform/includes/cc-terminology.md)]

## Return Value

**Type**: String.

**Description**: In this example, the following three columns for an account record were updated: name, accountnumber, telephone2.

```"<account><name>Contoso</name><accountnumber>55555</accountnumber><telephone2>425 555-1234</telephone2></account>"```

## Remarks

This method does not work with Microsoft Dynamics 365 for tablets.





[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
