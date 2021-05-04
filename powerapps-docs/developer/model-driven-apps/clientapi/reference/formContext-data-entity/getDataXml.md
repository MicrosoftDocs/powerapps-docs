---
title: "getDataXml (Client API reference) in model-driven apps| MicrosoftDocs"
description: Returns a string representing the XML that will be sent to the server when the record is saved.
ms.date: 10/31/2018
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 1a66f93d-a47c-4316-91f1-dcf5d09f9d19
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
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