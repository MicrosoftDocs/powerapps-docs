---
title: Repeat for every property in cards for Power Apps
description: Learn about the repeat for every property in cards for Power Apps.
author: anuitz
ms.topic: reference
ms.custom: 
ms.reviewer: mkaur
ms.date: 03/01/2023
ms.author: anuitz
search.audienceType:
  - maker
search.app:
  - PowerApps
contributors:
  - mduelae
  - anuitz
---

# Repeat for every property in cards

Repeat for every is used to display a control multiple times based on a data source. The repeat for every property is set to a collection or data source, then the relevant property can use `ThisItem` to reference specific items within the collection or data source.

## Example

Using the Dataverse Accounts table and a text label's **Repeat for every** property, a maker can create a card that displays the account name of every account within the Accounts table.

1. Add the Accounts table using the [Dataverse connection](../make-a-card/connectors/connector-intro.md).
1. Add a text label control.
1. Set the text label **Repeat for every** property to `Accounts`.
1. Set the text label **Text** property to `ThisItem.'Account Name'`.
1. Play the card, which will show a list of text labels the length of the Accounts table, each one displaying an account name.
