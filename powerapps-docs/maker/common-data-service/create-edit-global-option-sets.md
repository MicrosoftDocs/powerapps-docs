---
title: "Create and edit global option sets (picklists) overview for Common Data Service for Apps | MicrosoftDocs"
ms.custom: ""
ms.date: 05/26/2018
ms.reviewer: ""
ms.service: "crm-online"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "PowerApps"
ms.assetid: f06b8941-8dca-4601-b965-341cfb6fc3b2
caps.latest.revision: 11
ms.author: "matp"
manager: "brycho"
---
# Create and edit global option sets overview 

An option set (picklist) is a type of field that can be included in an entity. It defines a set of options. When an option set is displayed in a form it uses a drop-down list control. When displayed in **Advanced Find** it uses a *picklist control*. Sometimes option sets are called picklists by developers.  
  
You can define an option set to use a set of options defined within itself (locally) or it can use a set of options defined elsewhere (globally) which can be used by other option set fields. 

Global option sets are useful when you have a standard set of categories that can apply to more than one field. Maintaining two separate option sets with the same values is difficult and if they are not synchronized you can see errors, especially if you are mapping entity fields in a one-to-many entity relationship. More information:  [Mapping entity fields](map-entity-fields.md)

> [!NOTE]
> If you define every option set as a global option set your list of global option sets will grow and could be difficult to manage. If you know that the set of options will only be used in one place, use a local option set.

There are two designers you can use to create or edit global option sets:

|Designer| Description|
|--|--|
|[PowerApps portal](https://web.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc)|Provides an easy streamlined experience, but some special settings are not available.<br />More information: [Create an option set](custom-picklists.md) |
|Solution explorer|Not as easy, but provides for more flexibility for less common requirements. <br />More information: [Create and edit global option sets for Common Data Service for Apps using solution explorer](create-edit-global-option-sets-solution-explorer.md) |

> [!NOTE]
> You can also create global option sets in your environment using the following:
> - Import a solution that contains the definition of the global option sets.
> - A developer can write a program to create them. <br />More information: [Developer documentation: Customize global option sets](/dynamics365/customer-engagement/developer/org-service/customize-global-option-sets).

Information in this topic will help you choose which designer you can use. 

You should use the [PowerApps portal](https://web.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) to work with global option sets unless you need to address any of the following requirements:

- Assign colors to options
- Change the order of options
- Create a global option set in a solution other than the CDS Default solution
- Set managed properties
- Set properties used for virtual entities
- View dependencies

## See also

[Create an option set](custom-picklists.md)<br />
[Create and edit global option sets for Common Data Service for Apps using solution explorer](create-edit-global-option-sets-solution-explorer.md)<br />
[Developer documentation: Customize global option sets](/dynamics365/customer-engagement/developer/org-service/customize-global-option-sets)
  

 
