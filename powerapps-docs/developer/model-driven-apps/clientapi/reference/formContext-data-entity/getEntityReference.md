---
title: "getEntityReference (Client API reference) in model-driven apps| MicrosoftDocs"
description: Returns a lookup value that references a record.
ms.date: 04/15/2021
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
# getEntityReference (Client API reference)

[!INCLUDE[./includes/getEntityReference-description.md](./includes/getEntityReference-description.md)]

## Syntax

`formContext.data.entity.getEntityReference();`

[!INCLUDE[cc-terminology](../../../../data-platform/includes/cc-terminology.md)]

## Return Value

**Type**: Lookup object.

**Description**: The returned object has following three parameters:

- **entityType**: String. Logical name of the table record. For example, "account".
- **id**: String. GUID value of the table record.
- **name**: (Optional) String. Name of the table record. 





[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]