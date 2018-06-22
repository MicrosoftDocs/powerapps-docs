---
title: "getEntityReference (Client API reference) in Dynamics 365 Customer Engagement| MicrosoftDocs"
ms.date: 10/31/2017
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 1a66f93d-a47c-4316-91f1-dcf5d09f9d19
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
---
# getEntityReference (Client API reference)



[!INCLUDE[./includes/getEntityReference-description.md](./includes/getEntityReference-description.md)]

## Syntax

`formContext.data.entity.getEntityReference();`

## Return Value

**Type**: Lookup object.

**Description**: The returned object has following three attributes:

- **entityType**: String. Logical name of the entity record. For example, "account".
- **id**: String. GUID value of the entity record.
- **name**: (Optional) String. Name of the entity record. 



