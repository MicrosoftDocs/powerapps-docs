---
title: "How to create and edit fields for Common Data Service for Apps| MicrosoftDocs"
ms.custom: ""
ms.date: 05/18/2018
ms.reviewer: ""
ms.service: "crm-online"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "PowerApps"
ms.assetid: d88677fa-2caf-47b0-aec6-10a25a7ec9c3
caps.latest.revision: 55
ms.author: "matp"
manager: "brycho"
search.audienceType: 
  - maker
search.app: 
  - "PowerApps"
  - D365CE
---
# How to create and edit fields

In Common Data Service for Apps fields define the individual data items that can be used to store data in an entity. Fields are sometimes called *attributes* by developers. 
  
Before you create a custom field, evaluate whether using an existing field would meet your requirements. More information: [Create new metadata or use existing metadata?](create-edit-metadata.md#create-new-metadata-or-use-existing-metadata)

There are two designers you can use to create or edit fields:

|Designer| Description|
|--|--|
|[PowerApps portal](https://web.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc)|Provides an easy streamlined experience, but some special settings are not available.<br />More information: [Create and edit fields for Common Data Service for Apps using PowerApps portal](create-edit-field-portal.md)|
|Solution explorer|Not as easy, but provides for more flexibility for less common requirements.<br />More information: [Create and edit fields for Common Data Service for Apps using PowerApps solution explorer](create-edit-field-solution-explorer.md) |

> [!NOTE]
> You can also create fields in your environment using the following:
> - In model-driven apps, select **New Field** from the form editor.
> - Import a solution that contains the definition of the fields.
> - Use Power Query to create new entities and fill them with data.<br />More information: [Add data to an entity in the Common Data Service by using Power Query](/powerapps/maker/common-data-service/data-platform-cds-newentity-pq).
> - A developer can use [Metadata services](/powerapps/developer/common-data-service/use-web-services#metadata-services) to write a program to create and update fields.

Information in this topic will help you choose which designer you can use. 

You should use the PowerApps portal to Create and edit fields for Common Data Service for Appsunless you need to address any of the following requirements:

- Create a Customer Lookup field
- Create a field in a solution other than the CDS Default solution
- Define status reason transitions
- Edit multiple fields at once
- Enable Auditing
- Enable Field Level Security
- Select whether the field appears in global filter in interactive experience
- Select whether the field is sortable in interactive experience dashboards
- Set a field Requirement Level as Business Recommended
- Set managed properties for a field

> [!NOTE]
> You can create a Lookup field in the PowerApps portal or in solution explorer by creating a One-to-many relationship on the entity. But only solution explorer offers the option to create this relationship while creating a field.

## Community tools

**[Attribute Manager](https://www.xrmtoolbox.com/plugins/DLaB.Xrm.AttributeManager/)** is a tool that XrmToolbox community developed for CDS for Apps. Please see the [Developer Tools](https://docs.microsoft.com/dynamics365/customer-engagement/developer/developer-tools) topic for more community developed tools.

> [!NOTE]
> The community tools are not a product of Microsoft and does not extend support to the community tools. 
> If you have questions pertaining to the tool, please contact the publisher. More Information: [XrmToolBox](https://www.xrmtoolbox.com).

### See also  
[Create and edit fields for Common Data Service for Apps using PowerApps portal](create-edit-field-portal.md)<br />
[Create and edit fields for Common Data Service for Apps using PowerApps solution explorer](create-edit-field-solution-explorer.md)<br />
[Types of fields and field data types](types-of-fields.md)<br />
[Developer Documentation: Work with attribute metadata](/dynamics365/customer-engagement/developer/org-service/work-attribute-metadata)
 
