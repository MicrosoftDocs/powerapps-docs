---
title: "Create and edit choices (picklists) overview for Microsoft Dataverse | MicrosoftDocs"
description: Provides an overview about choice columns in Dataverse.
ms.custom: ""
ms.date: 08/05/2022
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: overview
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "PowerApps"
ms.assetid: f06b8941-8dca-4601-b965-341cfb6fc3b2
caps.latest.revision: 11
ms.subservice: dataverse-maker
ms.author: "matp"
author: "Mattp123"
search.audienceType: 
  - maker
---
# Create and edit choice columns overview

A choice (picklist) is a type of column that can be included in a table. It defines a set of options. When a choice is displayed in a form it uses a drop-down list control. When displayed in **Advanced Find** it uses a *picklist control*. Sometimes choices are called picklists by developers.  
  
You can define a choice  to use a set of options defined within itself (locally) or it can use a set of options defined elsewhere (globally) which can be used by other choice  columns.

Global choice columns are useful when you have a standard set of categories that can apply to more than one column. Maintaining two separate choice options with the same values is difficult and if they aren't synchronized you can see errors, especially if you are mapping table columns in a one-to-many table relationship. More information:  [Mapping table columns](map-entity-fields.md)

> [!NOTE]
> If you define every choice as a global choice your list of global choice columns will grow and could be difficult to manage. If you know that the set of options will only be used in one place, use a local choice.

Choice columns can be configured as either single select (choice) or multi-select (choices).

> [!NOTE]
> You can also create global choices in your environment using the following:
> - Import a solution that contains the definition of the global choices.
> - A developer can write a program to create them. <br />More information: [Developer documentation: Choices columns](/power-apps/developer/data-platform/multi-select-picklist).

## See also

[Create a choice ](custom-picklists.md)<br />

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
