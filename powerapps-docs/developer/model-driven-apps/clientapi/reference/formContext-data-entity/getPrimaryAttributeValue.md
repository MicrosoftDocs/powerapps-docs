---
title: "getPrimaryAttributeValue (Client API reference) in model-driven apps| MicrosoftDocs"
ms.date: 10/31/2018
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 1a66f93d-a47c-4316-91f1-dcf5d09f9d19
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
---
# getPrimaryAttributeValue (Client API reference)



[!INCLUDE[./includes/getPrimaryAttributeValue-description.md](./includes/getPrimaryAttributeValue-description.md)]

## Syntax

`formContext.data.entity.getPrimaryAttributeValue();`

## Return Value

**Type**: String.

**Description**: The name of the entity.

## Remarks

Each entity has one string attribute that is designated as the <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.PrimaryNameAttribute>. The value for this attribute is used when links to the record are displayed.



