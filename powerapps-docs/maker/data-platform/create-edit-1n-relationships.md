---
title: "Create 1:N (one-to-many) or N:1 (many-to-one) table relationships in Power Apps overview"
description: "Learn how to create one-to-many or many-to-one table relationships in Microsoft Dataverse"
ms.custom: ""
ms.date: 09/18/2024
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: overview
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "powerapps"
author: "Mattp123"
ms.assetid: 52c00707-b2bc-4950-abec-89baefd94f6e
caps.latest.revision: 33
ms.subservice: dataverse-maker
ms.author: "matp"
tags: 
search.audienceType: 
  - maker
---
# Create one-to-many or many-to-one table relationships in Microsoft Dataverse overview

In Microsoft Dataverse a one-to-many (1:N) or many-to-one (N:1) relationship defines how two tables are related to each other.
  
Before you create a custom table relationship, evaluate whether using an existing table relationship would meet your requirements. More information: [Create new metadata or use existing metadata?](create-edit-metadata.md#create-new-metadata-or-use-existing-metadata)

Watch this video for a quick overview about how to create a table, a table relationship, and columns:
> [!VIDEO https://learn-video.azurefd.net/vod/player?id=19b21a48-4a49-4163-8506-7fb79f3290ef]

You create and edit table relationships, including one-to-many and many-to-one relationships, in Power Apps.

You can also create new table relationship in your environment using any of the following experiences:

- In model-driven apps, select **New Column** from the form editor and create a *Lookup* column. More information: [Add, configure, move, or delete columns on a form](../model-driven-apps/add-move-or-delete-fields-on-form.md)
- Create a new Lookup column for the related table.More information: [Create and edit columns](create-edit-fields.md)
- Import a solution that contains the definition of the table relationship. More information: [Import, update, and export solutions](import-update-export-solutions.md)
- Use Power Query to create new tables and fill them with data. More information: [Add data to a table in Dataverse by using Power Query](/power-query/dataflows/add-data-power-query).
- A developer can use [Metadata services](../../developer/data-platform/metadata-services.md) to write a program to create and update table relationships. More information: [Table relationship definitions](/powerapps/developer/data-platform/entity-relationship-metadata)

Information in this article helps you choose which designer you can use.

## Create a one-to-many or many-to-one relationship

[Create and edit one-to-many or many-to-one table relationships in Power Apps](create-edit-1n-relationships-portal.md)<br />

## Community tools

**[table Relation Diagram Creator](https://www.xrmtoolbox.com/plugins/JourneyIntoCRM.XrmToolbox.ERDPlugin/)** is a tool that XrmToolbox community developed for Dataverse. Please see the [Developer tools for Dataverse](/dynamics365/customer-engagement/developer/developer-tools) topic for more community developed tools.

> [!NOTE]
> The community tools are not a product of Microsoft and does not extend support to the community tools. 
> If you have questions pertaining to the tool, please contact the publisher. More Information: [XrmToolBox](https://www.xrmtoolbox.com).

### See also

[Create and edit relationships between tables](create-edit-entity-relationships.md)<br />

[Create and edit 1:N (one-to-many) or N:1 (many-to-one) table relationships using solution explorer](create-edit-1n-relationships-solution-explorer.md)<br />
[Developer documentation: Customize table relationship metadata](/dynamics365/customer-engagement/developer/customize-entity-relationship-metadata)<br />
[Developer documentation: table relationship eligibility](/dynamics365/customer-engagement/developer/entity-relationship-eligibility)




[!INCLUDE[footer-include](../../includes/footer-banner.md)]
