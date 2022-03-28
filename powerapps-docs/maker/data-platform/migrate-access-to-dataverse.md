---
title: Migrate Microsoft Access data to Microsoft Dataverse (contains video) | Microsoft Docs
description: You can migrate your Microsoft Access data to Microsoft Dataverse or Microsoft Dataverse for Teams
author: NHelgren

ms.topic: overview
ms.custom: 
  - model
  - intro-internal
ms.reviewer: matp
ms.date: 10/18/2021
ms.subservice: dataverse-maker
ms.author: NHelgren
search.audienceType: 
  - maker
search.app: 
  - PowerApps
contributors:
---
# Migrate Microsoft Access data to Microsoft Dataverse (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

Microsoft Access users can now choose to migrate their data into Dataverse or Dataverse for Teams to make use of Azure cloud security and Microsoft Power Platform functionality. Migrating Access data to Dataverse provides many new opportunities for interaction and management of data.  

Watch this short video about migrating Access data to Dataverse.
> [!VIDEO https://www.microsoft.com/en-us/videoplayer/embed/RWO6T0]

Migration is handled in Access using the export feature, and the migration tool that streamlines the process.

> [!NOTE]
> [Join the Microsoft Access beta to start your migration](https://aka.ms/AccessAndPowerPlatform)

Once migrated, Access users can continue using their existing desktop client to manage their data. They're also able to use Power Platform to manage their data. Plus, they can:

- Create applications for desktop, laptop, phone, and tablet.
- Create automated processes based on the data and services in Dataverse or Dataverse for Teams.
- Create AI-driven virtual assistants based on the data.
- Perform deep analysis on the stored data using business intelligence.

Before you migrate, there are a few key factors to consider. Currently, Dataverse and Dataverse for Teams don't support every data type that is in Access. Additionally, some data types in Dataverse and Dataverse for Teams may have different data limits. More information: [Data types and sizes for Access data migration to Dataverse](migrate-access-datatypes.md) 

Dataverse and Dataverse for Teams offer differing features that you can use to best meet your needs. Dataverse for Teams is targeted at users who want to have Power Platform functionality within the Microsoft Teams application. Dataverse is included with licenses of Dynamics 365 or Power Apps. Organizations that have a Dataverse for Teams environment can choose later to upgrade to Dataverse.

|Dataverse  |Dataverse for Teams  |
|---------|---------|
| All available data types supported.   |  Relational data, image, and file data support, built on the core of Dataverse.     |
|Dataverse enterprise-grade capabilities, including advanced Role-Based Access Control, highly extensible business logic, sophisticated reporting, and robust offline.      | Use apps, chatbots, and automations backed by Dataverse embedded in Teams on any platform.         |
|Existing premium connectors to enterprise systems such as SAP, Oracle, and so on.    |  Some data types are not supported or have minimal functionality (Currency, Date Only, Customer).        |
|Standalone premium apps, bots, and automations outside of Teams.      |  Not all controls are available, such as bar code scanner, interface tools, and formulas.        |

Total storage capacity is also different. Dataverse and Dataverse for Teams have a heterogenous data storage platform, which allows for storing different types of data in ways that help improve performance and lower cost of maintenance.  

:::row:::
   :::column span="":::
      **Access**
   :::column-end:::
   :::column span="":::
      **Dataverse**<sup>1</sup>
   :::column-end:::
   :::column span="":::
      **Dataverse for Teams**
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      2-GB storage on local machine
   :::column-end:::
   :::column span="":::
      - 10-GB relational database 
      - 20-GB file and image blob storage
      - 2-GB log storage in non-relational storage
      - You can purchase additional capacity as needed in any of the store types
   :::column-end:::
   :::column span="":::
      - 2-GB storage (up to 1 million records) per Team
      - Images, files, and logs stored separately in blob storage (counts towards 2-GB limit)
   :::column-end:::
:::row-end:::

<sup>1</sup> Single base license

For more information, go to [How are Dataverse for Teams and Dataverse different?](../../teams/data-platform-compare.md)

## Comparison of Access and Dataverse Terminology

Users integrating Access with Dataverse or Dataverse for Teams may find some differences in names for general features and functions. This section provides a guide to understand naming differences.

Unlike Access, Dataverse and Dataverse for Teams are data sources. The user interface layer will depend on what Power Platform feature you are using: Power Apps, Power Automate, Power BI, or Power Virtual Agents. The lists below encompass naming differences and similarities at the database layer only.

|Access  |Dataverse and Dataverse for Teams  |Comments  |
|---------|---------|---------|
|Primary Key  | Primary Key   | The usage is the same but the key contents are different    |
|Calculated Field   | Calculated Column (property)   |  Dataverse does not have a calculated column data type but rather allows calculations to be created on individual data types like whole number, decimal, or text       |
|Row    | Row  or record   |  Sometimes referred to as a record in Dataverse and Dataverse for Teams    |
|Short Text  |  Text    |  Supported for migration       |
|Long Text  |  Multiline Text    |  Supported for migration       |
|Number: Single   | Float        |  Currently not supported for migration - [workaround available](migrate-access-datatypes.md#migrate-numbersingle-and-numberdouble-columns-to-dataverse)           |
|Number: Double     |  Float       | Currently not supported for migration - [workaround available](migrate-access-datatypes.md#migrate-numbersingle-and-numberdouble-columns-to-dataverse)            |
|Large Number      |  Big Integer (BigInt)       | Supported for migration, usable through Dataverse API, Power Apps UI does not currently support this       |
|Number: Decimal      | Decimal         | Supported for migration         |
|Yes/No      | Yes/No         |  Supported for migration        |
|Int      | Whole Number         |  Supported for migration       |
|Multi-Select Options      | Choices        | Supported for migration         |
|GUID      | Unique Identifier           |   In Dataverse and Dataverse for Teams, this is currently only used as a key        |
|  Hyperlink         |  URL       | Supported for migration         |
|Unique Index      |  Alternate Key        | Not supported for migration      |
|Multi-Value Lookup      | Choice        | Supported for migration         |

### See also

[Data types and sizes for Access data migration to Dataverse](migrate-access-datatypes.md)
