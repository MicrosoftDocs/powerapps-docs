---
title: "Create 1:N (one-to-many) or N:1 (many-to-one) table relationships in Power Apps overview | MicrosoftDocs"
description: "Learn how to create one-to-many or many-to-one table relationships"
ms.custom: ""
ms.date: 10/04/2021
ms.reviewer: ""
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "overview"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "powerapps"
author: "Mattp123"
ms.assetid: 52c00707-b2bc-4950-abec-89baefd94f6e
caps.latest.revision: 33
ms.subservice: dataverse-maker
ms.author: "matp"
manager: "kvivek"
tags: 
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---
# Create one-to-many or many-to-one table relationships overview

[!INCLUDE[cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

In Microsoft Dataverse 1:N (one-to-many) or N:1 (many-to-one) relationships define how two tables are related to each other.
  
Before you create a custom table relationship, evaluate whether using an existing table relationship would meet your requirements. More information: [Create new metadata or use existing metadata?](create-edit-metadata.md#create-new-metadata-or-use-existing-metadata)

Watch this video for a quick overview about how to create a table, a table relationship, and columns:
> [!VIDEO https://www.microsoft.com/en-us/videoplayer/embed/RWLPQb]

There are two designers you can use to create and edit 1:N (one-to-many) or N:1 (many-to-one) relationships:

|Designer| Description|
|--|--|
|[Power Apps portal](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc)|Provides an easy streamlined experience, but some special settings are not available.<br />More information: [Create and edit 1:N (one-to-many) or N:1 (many-to-one) table relationships in Power Apps portal](create-edit-1n-relationships-portal.md)|
|Solution explorer|Not as easy, but provides for more flexibility for less common requirements. <br />More information: [Create and edit 1:N (one-to-many) or N:1 (many-to-one) table relationships using solution explorer](create-edit-1n-relationships-solution-explorer.md) |

> [!NOTE]
> You can also create new table relationship in your environment using the following:
> - In model-driven apps, select **New Column** from the form editor and create a *Lookup* column. <br />More information: [Add, configure, move, or delete columns on a form](../model-driven-apps/add-move-or-delete-fields-on-form.md)
> - Create a new Lookup column for the related table. <br />More information: [Create and edit columns](create-edit-fields.md)
> - Import a solution that contains the definition of the table relationship. <br />More information: [Import, update, and export solutions](import-update-export-solutions.md)
> - Use Power Query to create new tables and fill them with data. <br />More information: [Add data to a table in Dataverse by using Power Query](add-data-power-query.md).
> - A developer can use [Metadata services](../../developer/data-platform/metadata-services.md) to write a program to create and update table relationships. <br />More information: [Customize table relationship metadata](/dynamics365/customer-engagement/developer/customize-table-relationship-metadata)

Information in this topic will help you choose which designer you can use. 

You should use the Power Apps portal to create and edit 1:N (one-to-many) or N:1 (many-to-one) table relationships unless you need to address any of the following requirements:

- Configure column mappings
- Configure navigation pane options for model-driven app
- Configure relationship behaviors
- Define whether the relationship is hidden in advanced find.
- Make a Hierarchical relationship


## Community tools

**[table Relation Diagram Creator](https://www.xrmtoolbox.com/plugins/JourneyIntoCRM.XrmToolbox.ERDPlugin/)** is a tool that XrmToolbox community developed for Dataverse. Please see the [Developer tools for Dataverse](/dynamics365/customer-engagement/developer/developer-tools) topic for more community developed tools.

> [!NOTE]
> The community tools are not a product of Microsoft and does not extend support to the community tools. 
> If you have questions pertaining to the tool, please contact the publisher. More Information: [XrmToolBox](https://www.xrmtoolbox.com).

### See also

[Create and edit relationships between tables](create-edit-entity-relationships.md)<br />
[Create and edit 1:N (one-to-many) or N:1 (many-to-one) table relationships in Power Apps portal](create-edit-1n-relationships-portal.md)<br />
[Create and edit 1:N (one-to-many) or N:1 (many-to-one) table relationships using solution explorer](create-edit-1n-relationships-solution-explorer.md)<br />
[Developer documentation: Customize table relationship metadata](/dynamics365/customer-engagement/developer/customize-entity-relationship-metadata)<br />
[Developer documentation: table relationship eligibility](/dynamics365/customer-engagement/developer/entity-relationship-eligibility)




[!INCLUDE[footer-include](../../includes/footer-banner.md)]