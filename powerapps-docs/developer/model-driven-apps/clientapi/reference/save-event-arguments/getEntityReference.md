---
title: EventArgs.getEntityReference (Client API reference)
description: Includes description and supported parameters for the EventArgs.getEntityReference method.
author: adrianorth
ms.author: aorth
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors:
  - JimDaly
---
# EventArgs.getEntityReference (Client API reference)

Use this method to know information about a table being saved/updated. It returns table ID, and table name if success.

## Syntax

`executionContext.getEventArgs().getEntityReference();`

## Related articles

[PostSave](../events/postsave.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]