---
title: "How to create and edit columns for Microsoft Dataverse| MicrosoftDocs"
description: Learn how to create and edit columns
ms.custom: ""
ms.date: 02/08/2019
ms.reviewer: ""
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "how-to"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "PowerApps"
ms.assetid: d88677fa-2caf-47b0-aec6-10a25a7ec9c3
caps.latest.revision: 55
ms.author: "matp"
manager: "kvivek"
author: "Mattp123"
search.audienceType: 
  - maker
search.app: 
  - "PowerApps"
  - D365CE
---
# How to create and edit columns

[!INCLUDE[cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

In Microsoft Dataverse columns define the individual data items that can be used to store data in a table. Columns are sometimes called *attributes* by developers. 

Watch this video for a quick overview about columns:
> [!VIDEO https://www.microsoft.com/en-us/videoplayer/embed/RWEC1G]
  
Before you create a custom column, evaluate whether using an existing column would meet your requirements. More information: [Create new metadata or use existing metadata?](create-edit-metadata.md#create-new-metadata-or-use-existing-metadata)

There are two designers you can use to create or edit columns:

|Designer| Description|
|--|--|
|[Power Apps portal](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc)|Provides an easy streamlined experience, but some special settings are not available.<br />More information: [Create and edit columns for Dataverse using Power Apps portal](create-edit-field-portal.md)|
|Solution explorer|Not as easy, but provides for more flexibility for less common requirements.<br />More information: [Create and edit columns for Dataverse using Power Apps solution explorer](create-edit-field-solution-explorer.md) |

> [!NOTE]
> You can also create columns in your environment using the following:
> - In model-driven apps, select **New Column** from the form editor.
> - Import a solution that contains the definition of the columns.
> - Use Power Query to create new tables and fill them with data.<br />More information: [Add data to a table in the Dataverse by using Power Query](./add-data-power-query.md).
> - A developer can use [Metadata services](/powerapps/developer/data-platform/use-web-services#metadata-services) to write a program to create and update columns.

Information in this topic will help you choose which designer you can use. 

You should use the Power Apps portal to create and edit columns for Dataverse unless you need to address any of the following requirements:

- Create a Customer Lookup column. 
   - More information: [Different types of lookups](types-of-fields.md#different-types-of-lookups)
- Create a column in a solution other than the Common Data Service Default Solution. 
   - More information: [Solutions overview](solutions-overview.md)
- Define status reason transitions. 
   - More information: [Define status reason transitions for the Case or custom tables](define-status-reason-transitions.md)
- Edit multiple columns at once.
- Enable Auditing. 
   - More information: [Auditing overview](../../developer/data-platform/auditing-overview.md)
- Enable Column Level Security. 
   - More information: [Column security tables](../../developer/data-platform/field-security-entities.md)
- Select whether the column appears in global filter in interactive experience. 
   - More information: [Configure model-driven app interactive experience dashboards](../model-driven-apps/configure-interactive-experience-dashboards.md)
- Select whether the column is sortable in interactive experience dashboards. 
   - More information: [Configure model-driven app interactive experience dashboards](../model-driven-apps/configure-interactive-experience-dashboards.md)
- Set a column Requirement Level as Business Recommended. 
   - More information: [Create business rules and recommendations to apply logic in a model-driven app form](../model-driven-apps/create-business-rules-recommendations-apply-logic-form.md)
- Set managed properties for a column. 
   - More information: [Set managed properties for columns](set-managed-properties-for-field.md)

> [!NOTE]
> You can create a Lookup column in the Power Apps portal or in solution explorer by creating a One-to-many relationship on the table. But only solution explorer offers the option to create this relationship while creating a column.

## Community tools

**[Attribute Manager](https://www.xrmtoolbox.com/plugins/DLaB.Xrm.AttributeManager/)** is a tool that XrmToolbox community developed for Dataverse. Please see the [Developer Tools](/dynamics365/customer-engagement/developer/developer-tools) topic for more community developed tools.

> [!NOTE]
> The community tools are not a product of Microsoft and does not extend support to the community tools. 
> If you have questions pertaining to the tool, please contact the publisher. More Information: [XrmToolBox](https://www.xrmtoolbox.com).

### See also  
[Create and edit columns for Dataverse using Power Apps portal](create-edit-field-portal.md)<br />
[Create and edit columns for Dataverse using Power Apps solution explorer](create-edit-field-solution-explorer.md)<br />
[Types of columns and column data types](types-of-fields.md)<br />
[Developer Documentation: Work with attribute metadata](/dynamics365/customer-engagement/developer/org-service/work-attribute-metadata)
 


[!INCLUDE[footer-include](../../includes/footer-banner.md)]