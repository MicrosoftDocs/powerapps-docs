---
title: "How to create and edit columns for Microsoft Dataverse | MicrosoftDocs"
description: Learn how to create and edit columns
ms.custom: ""
ms.date: 08/12/2025
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "how-to"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "PowerApps"
ms.assetid: d88677fa-2caf-47b0-aec6-10a25a7ec9c3
caps.latest.revision: 55
ms.subservice: dataverse-maker
ms.author: "matp"
author: "Mattp123"
search.audienceType: 
  - maker
---
# How to create and edit columns

In Microsoft Dataverse columns, define the individual data items that can be used to store data in a table. Columns are sometimes called *attributes* by developers. 

Watch this video for a quick overview about columns:
> [!VIDEO https://learn-video.azurefd.net/vod/player?id=3379c026-1830-4265-86fc-c7d16a0b6b49]
  
Before you create a custom column, evaluate whether using an existing column would meet your requirements. More information: [Create new metadata or use existing metadata?](create-edit-metadata.md#create-new-metadata-or-use-existing-metadata)

> [!NOTE]
> You can also create columns in your environment using these methods:
>
> - For model-driven apps, select **New table column** in the form editor.
> - Import a solution that contains the definition of the columns.
> - Use Power Query to create new tables and fill them with data. [Learn how to add data to a table in the Dataverse by using Power Query](/power-query/dataflows/add-data-power-query).
> - A developer can use [Metadata services](../../developer/data-platform/metadata-services.md) to write a program to retrieve information about, create, and update columns.

> [!NOTE]
> You can create a Lookup column in Power Apps by creating a one-to-many relationship on the table. 

For more information about how to create a table column, go to [Create and edit columns for Dataverse using Power Apps portal](create-edit-field-portal.md).

## Community tools

**[Attribute Manager](https://www.xrmtoolbox.com/plugins/DLaB.Xrm.AttributeManager/)** is a tool that XrmToolbox community developed for Dataverse. Go to the [Developer tools and resources](../../developer/data-platform/developer-tools.md) article for more community developed tools.

> [!NOTE]
> The community tools aren't a product of Microsoft and Microsoft doesn't offer support for the community tools.
> If you have questions pertaining to the tool, contact the publisher. More Information: [XrmToolBox](https://www.xrmtoolbox.com)

### Related articles

[Types of columns and column data types](types-of-fields.md)

[Developer Documentation: Column definitions](../../developer/data-platform/entity-attribute-metadata.md)   
 
[!INCLUDE[footer-include](../../includes/footer-banner.md)]
