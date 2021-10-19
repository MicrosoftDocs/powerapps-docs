---
title: Migrate Microsoft Access data to Microsoft Dataverse | Microsoft Docs
description: You can migrate your Microsoft Access data to Microsoft Dataverse or Microsoft Dataverse for Teams
author: NHelgren
ms.service: powerapps
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
# Migrate Microsoft Access data to Microsoft Dataverse

Microsoft Access users can now choose to migrate their data into Dataverse or Dataverse for Teams to make use of Azure Cloud security and Power Platform functionality. Migrating Access data to Dataverse provides many new opportunities for interaction and management of data.  

Migration is handled in Access using the export feature, and the migration tool that streamlines the process.

Once migrated, Access users are able to continue using their existing desktop client to manage their data. They're also able to use the Power Platform to manage their data and:

- Create applications for desktop, laptop, phone, and tablet.
- Create automated processes based on the data and services in Dataverse or Dataverse for Teams.
- Create AI driven virtual assistants based from the data.
- Perform deep analysis on the stored data using business intelligence.

Before you migrate, there are a few key factors to consider. Currently, Dataverse and Dataverse for Teams don't support every data type that is in Access. Additionally, some data types in Dataverse and Dataverse for Teams may have different data limits.  

Dataverse and Dataverse for Teams offer differing features that you can use to best meet your needs. Dataverse for Teams is targeted at users who want to have Power Platform functionality within the Microsoft Teams application. Dataverse is included with licenses of Dynamics 365, Power Apps, Power Automate, Power BI, or Power Virtual Agent. Organizations that have a Dataverse for Teams environment can choose later to upgrade to Dataverse.


|Dataverse  |Dataverse for Teams  |
|---------|---------|
| All available data types supported.   |  Relational data, image, and file data support, built on the core of Dataverse.     |
|Dataverse enterprise-grade capabilities, including advanced Role-Based Access Control, highly extensible business logic, sophisticated reporting, and robust offline      | Use apps, chatbots, and automations backed by Dataverse embedded in Teams on any platform.         |
|Existing premium connectors to enterprise systems such as SAP, Oracle, and so on.    |  Some data types are not supported or have minimal functionality (Currency, Date Only, Customer)        |
|Standalone premium apps, bots, and automations outside of Teams      |  Not all controls are available such as, bar code scanner, interface tools, and formulas        |

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

For more information, go to [How are Dataverse for Teams and Dataverse different?](../../teams/data-platform-compare.md).

### See also

[Data types and sizes for Access data migration to Dataverse](migrate-access-datatypes.md)