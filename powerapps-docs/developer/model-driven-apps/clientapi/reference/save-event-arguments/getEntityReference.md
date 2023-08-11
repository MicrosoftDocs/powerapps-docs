---
title: EventArgs.getEntityReference (Client API reference)
description: Includes description and supported parameters for the EventArgs.getEntityReference method.
author: HemantGaur
ms.author: hemantg
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# EventArgs.getEntityReference (Client API reference)

Use this method to know information about a table being saved/updated. It returns table ID, and table name if success.

[!INCLUDE [online-only-api-note](../../includes/online-only-api-note.md)]

## Syntax

`executionContext.getEventArgs().getEntityReference();`

## Related articles

[PostSave](../events/postsave.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
