---
title: "Create and edit global choices (picklists) overview for Microsoft Dataverse | MicrosoftDocs"
ms.custom: ""
ms.date: 05/26/2018
ms.reviewer: ""
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "overview"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "PowerApps"
ms.assetid: f06b8941-8dca-4601-b965-341cfb6fc3b2
caps.latest.revision: 11
ms.author: "matp"
manager: "kvivek"
author: "Mattp123"
search.audienceType: 
  - maker
search.app: 
  - "PowerApps"
  - D365CE
---
# Create and edit global choices overview 

[!INCLUDE[cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

A choice (picklist) is a type of column that can be included in a table. It defines a set of options. When a choice is displayed in a form it uses a drop-down list control. When displayed in **Advanced Find** it uses a *picklist control*. Sometimes choices are called picklists by developers.  
  
You can define a choice  to use a set of options defined within itself (locally) or it can use a set of options defined elsewhere (globally) which can be used by other choice  columns. 

Global choices are useful when you have a standard set of categories that can apply to more than one column. Maintaining two separate choices with the same values is difficult and if they are not synchronized you can see errors, especially if you are mapping table columns in a one-to-many table relationship. More information:  [Mapping table columns](map-entity-fields.md)

> [!NOTE]
> If you define every choice as a global choice your list of global choices will grow and could be difficult to manage. If you know that the set of options will only be used in one place, use a local choice.

There are two designers you can use to create or edit global choices:

|Designer| Description|
|--|--|
|[Power Apps portal](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc)|Provides an easy streamlined experience, but some special settings are not available.<br />More information: [Create a choice ](custom-picklists.md) |
|Solution explorer|Not as easy, but provides for more flexibility for less common requirements. <br />More information: [Create and edit global choices for Microsoft Dataverse using solution explorer](create-edit-global-option-sets-solution-explorer.md) |

> [!NOTE]
> You can also create global choices in your environment using the following:
> - Import a solution that contains the definition of the global choices.
> - A developer can write a program to create them. <br />More information: [Developer documentation: Customize global choices](/dynamics365/customer-engagement/developer/org-service/customize-global-option-sets).

Information in this topic will help you choose which designer you can use. 

You should use the [Power Apps portal](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) to work with global choices unless you need to address any of the following requirements:

- Assign colors to options
- Change the order of options
- Create a global choice in a solution other than the Common Data Service Default Solution
- Set managed properties
- Set properties used for virtual tables
- View dependencies

## See also

[Create a choice ](custom-picklists.md)<br />
[Create and edit global choices for Dataverse using solution explorer](create-edit-global-option-sets-solution-explorer.md)<br />
[Developer documentation: Customize global choices](/dynamics365/customer-engagement/developer/org-service/customize-global-option-sets)
  

 


[!INCLUDE[footer-include](../../includes/footer-banner.md)]