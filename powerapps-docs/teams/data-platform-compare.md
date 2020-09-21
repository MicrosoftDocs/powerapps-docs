---
title: Project Oakdale vs. Common Data Service | Microsoft Docs
description: Explains the differences between Project Oakdale and Common Data Service.
author: NHelgren
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 09/11/2020
ms.author: nhelgren
ms.reviewer: matp
---

# How are Project Oakdale and Common Data Service different?

[!INCLUDE [cc-beta-prerelease-disclaimer.md](../includes/cc-beta-prerelease-disclaimer.md)]

Applications within a team in Microsoft Teams have access to a Project Oakdale environment. Project Oakdale is a common platform that allows all these interfaces to have a unified understanding of how the data is modeled and consumed. Project Oakdale delivers a targeted set of the features commonly needed for creating apps, flows, and more within Teams. If your organization requires additional capabilities, such as more granular control for security and governance, or capacity beyond the approximately 1 million rows a Project Oakdale environment can contain, Project Oakdale can be promoted to Common Data Service.

## Key terminology changes

Some terminology has changed between Common Data Service and Project Oakdale to make it easier for a broader audience. The table below provides a mapping between Common Data Service and Project Oakdale terms.

|Project Oakdale  |Common Data Service  |
|---------|---------|
|Table, tables     | Entity, entities        |
|Column, columns     |  Field, fields <br /> attribute, attributes       |

Most of the processes for creating and managing tables in Project Oakdale are the same as creating and managing entities in Common Data Service. Where applicable, these articles about Project Oakdale link you to Common Data Service articles that provide more detail.

## Entity features

This table describes the differences between a Project Oakdale table and Common Data Service entity features.

|Feature  |Project Oakdale  |Common Data Service  |
|---------|---------|---------|
|Basic data types     |  Yes       |  Yes       |
|Advanced data types​ (customer, multiple transaction currencies)      |  No       |  Yes       |
|Common Data Model    |  Coming Soon       |  Yes       |
|Relational storage      | Yes       |  Yes       |
|Non-relational​ storage (logs)   |  No       |  Yes       |
|Managed data lake​      |  No       | Yes        |
|File and image support     | Yes        |  Yes       |
|Find, filter, sort     |   Yes      |  Yes       |
|Advanced and relevance search​      |   No      | Yes        |
|Mobile offline     |  No       |  Yes       |

Note that most of the standard tables that are provided with a Common Data Service environment won't be present as part of Project Oakdale.

## Business intelligence and professional developer features

This table describes the differences between Project Oakdale and Common Data Service business intelligence and professional developer features.


|Area  |Feature  |Project Oakdale  |Common Data Service  |
|---------|---------|---------|---------|
|Business intelligence     |  Data visualization   |  Yes    |  Yes   |
|      |   Paginated reports (SQL Server Reporting Services)   |  No    |  Yes     |
|Professional developer     | API access       |  No     |  Yes     |
|      |  Plugins       |   No      |  Yes       |

## Environments

In Project Oakdale and Common Data Service, data is stored within an environment. Project Oakdale creates a single environment for each team in Teams where you create data, apps, chatbots, and workflows. Environments support backups, point-in-time restore, and disaster recovery. With Project Oakdale, capacity is measured with relational, image, and file data. The 2-GB capacity provided to a team can typically store up to 1 million rows of data.

To make management easier, the lifecycle of the Project Oakdale environment is connected to that of the associated team. For example, when a team is deleted, the associated environment is also deleted.

Whereas Project Oakdale focuses on one environment per team for up to 500 teams, the Common Data Service supports unlimited environments in addition to capabilities that are relevant for multiple environments, such as copy and reset.


|Environment lifecycle  |Project Oakdale  |Common Data Service  |
|---------|---------|---------|
|Environments   | 1 per Team     | Unlimited        |
|Maximum size     |   1 million rows or 2 GB      |  4 TB or more     |
|Promote to Common Data Service or Dynamics 365   |  Yes    |  Yes    |

## Security

Because collaboration in Teams happens with people inside and outside your organization, the security model needed to support this is easy to use. In Project Oakdale, access is preconfigured with a security role based on membership type such as owners, members, or guests.

Both Project Oakdale and Common Data Service include support for activity logging. For example, activity logging identifies who created a record. However, Common Data Service provides additional capabilities for auditing.

Because Common Data Service isn't specific to the Teams environment, it delivers more options for admin and user roles. It also includes a number of additional security capabilities such as customer-managed keys, field-level security, hierarchical security, sharing, and support for legacy authentication.

> [!NOTE]
> Because Project Oakdale environments are specific to a team, they only contain one business unit.


|Security feature  |Project Oakdale  |Common Data Service  |
|---------|---------|---------|
|Admin roles     |  System Administrator and System Customizer       |  System Administrator and System Customizer and additional service admin roles. More information: [Use service admin roles to manage your tenant](/power-platform/admin/use-service-admin-role-manage-tenant)      |
|User roles    | Team owners, members, and guests        |  Several standard security roles and custom roles can also be created. More information: [Security roles and privileges](/power-platform/admin/security-roles-privileges)       |
|Activity logging     |  Yes       |  Yes       |
|Business units     |   One      |  Unlimited      |
|Auditing     |  No       |  Yes       |
|Customer-managed environment encryption key     |   No      |  Yes       |
|Field-level security     |   No      |  Yes       |
|Hierarchical security     |  No       |  Yes       |
|Record sharing     |  No       |  Yes       |

## Integration

Integration with Project Oakdale is delivered primarily through connectors. Support for both standard connectors and the ability to use the Common Data Service connector to connect to a Project Oakdale for a Teams environment is included. Users with Premium licenses have access to the full set of over 350 standard and premium connectors available. This provides the ability to bring data into or retrieve data from tables in Project Oakdale, execute workflows when data in those tables change, and also use data from tables in workflow logic.

Common Data Service can also use connectors. Additionally, Common Data Service includes other built-in integration capabilities that can export data to a data lake or publish events to an event hub, service bus, or by using webhooks. Common Data Service also supports the TDS protocol, which provides integration with SQL Server.<!--note from editor: Edit okay?-->

Common Data Service can also be used with server-side sync to synchronize with Exchange or POP3, and with Data Export Service, which synchronizes data to Azure SQL Database.


|Integration feature  |Project Oakdale  |Common Data Service  |
|---------|---------|---------|
|Power Automate     |   Yes      |  Yes       |
|Export to Azure data lake    |   No      |  Yes       |
|Data Export Service     |   No      |  Yes       |
|Events to Azure Event Hubs     |   No      |  Yes       |
|Events to Azure Service Bus     |   No      |  Yes       |
|Webhooks     |   No      |  Yes       |
|Server-side sync     |   No      |  Yes       |
|SQL Server Management Studio     |   No      |   Yes      |

  

### See also

[Create a table](create-table.md)
