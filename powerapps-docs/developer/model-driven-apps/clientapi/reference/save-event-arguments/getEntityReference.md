---
title: "getEntityReference (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the getEntityReference method.
ms.date: 04/21/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 03e970ee-7ed3-4df2-9670-222d76a479fd
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

Use this method to know information about a table being saved/updated. It returns table ID, and table name if success.

## Syntax

`executionContext.getEventArgs().getEntityReference();`

## Related articles

[PostSave](../events/postsave.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]