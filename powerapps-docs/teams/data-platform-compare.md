---
title: Dataverse for Teams vs. Dataverse | Microsoft Docs
description: Explains the differences between Dataverse for Teams and Dataverse.
author: mmercuri
ms.service: powerapps
ms.topic: conceptual
ms.custom: intro-internal
ms.date: 03/19/2021
ms.subservice: teams
ms.author: mmercuri
ms.reviewer: matp
---
# How are Dataverse for Teams and Dataverse different?

[!INCLUDE[cc-data-platform-banner](../includes/cc-data-platform-banner.md)]

Applications within a team in Microsoft Teams have access to a Dataverse for Teams environment. Dataverse for Teams is a common platform that allows all these interfaces to have a unified understanding of how the data is modeled and consumed. Dataverse for Teams delivers a targeted set of the features commonly needed for creating apps, flows, and more within Teams. If your organization requires additional capabilities, such as more granular control for security and governance, or capacity beyond the approximately 1 million rows a Dataverse for Teams environment can contain, Dataverse for Teams can be [upgraded](/power-platform/admin/about-teams-environment#upgrade-process) to Dataverse.

## Table features

Following are the differences between a Dataverse for Teams and Dataverse table features.

|Feature  |Dataverse for Teams  |Dataverse  |
|---------|---------|---------|
|Basic data types     |  Yes       |  Yes       |
|Advanced data types​ (customer, multiple transaction currencies)      |  No       |  Yes       |
|Common Data Model    |  Yes       |  Yes       |
|Relational storage      | Yes       |  Yes       |
|Non-relational storage (logs)   |  No       |  Yes       |
|Managed data lake      |  No       | Yes        |
|File and image support     | Yes        |  Yes       |
|Find, filter, sort     |   Yes      |  Yes       |
|Advanced and relevance search      |   No      | Yes        |
|Mobile offline     |  No       |  Yes       |

Note that most of the standard tables that are provided with a Dataverse environment won't be present as part of Dataverse for Teams.

## Business intelligence and professional developer features

This table describes the differences between Dataverse for Teams and Dataverse business intelligence and professional developer features.


|Area  |Feature  |Dataverse for Teams  |Dataverse  |
|---------|---------|---------|---------|
|Business intelligence     |  Data visualization   |  Yes    |  Yes   |
|      |   Paginated reports (SQL Server Reporting Services)   |  No    |  Yes     |
|Professional developer     | API access       |  No     |  Yes     |
|      |  Plug-ins       |   No      |  Yes       |

## Environments

In Dataverse for Teams and Dataverse, data is stored within an environment. Dataverse for Teams creates a single environment for each team in Teams where you create data, apps, chatbots, and workflows. Environments support backups, point-in-time restore, and disaster recovery. With Dataverse for Teams, capacity is measured with relational, image, and file data. The 2-GB capacity provided to a team can typically store up to 1 million rows of data.

To make management easier, the lifecycle of the Dataverse for Teams environment is connected to that of the associated team. For example, when a team is deleted, the associated environment is also deleted.

Whereas Dataverse for Teams focuses on one environment per team for up to 10,000 teams, Dataverse supports unlimited environments in addition to capabilities that are relevant for multiple environments, such as copy and reset.


|Environment lifecycle  |Dataverse for Teams  |Dataverse  |
|---------|---------|---------|
|Environments   | 1 per Team     | Unlimited        |
|Maximum size     |   1 million rows or 2 GB      |  4 TB or more     |
|Upgrade to Dataverse   |  Yes    |  N/A    |

## Security

Because collaboration in Teams happens with people inside and outside your organization, the security model needed to support this is easy to use. In Dataverse for Teams, access is preconfigured with a security role based on membership type such as owners, members, or guests.

Because Dataverse isn't specific to the Teams environment, it delivers more options for admin and user roles. It also includes a number of additional security capabilities such as customer-managed keys, field-level security, hierarchical security, sharing, and support for legacy authentication.

> [!NOTE]
> Because Dataverse for Teams environments are specific to a team, they only contain one business unit.


|Security feature  |Dataverse for Teams  |Dataverse  |
|---------|---------|---------|
|Admin roles     |  System Administrator and System Customizer       |  System Administrator and System Customizer and additional service admin roles. More information: [Use service admin roles to manage your tenant](/power-platform/admin/use-service-admin-role-manage-tenant)      |
|User roles    | Team owners, members, and guests        |  Several standard security roles and custom roles can also be created. More information: [Security roles and privileges](/power-platform/admin/security-roles-privileges)       |
|Activity logging     |  No       |  Yes       |
|Auditing     |  No       |  Yes       |
|Business units     |   One      |  Unlimited      |
|Customer-managed environment encryption key     |   No      |  Yes       |
|Field-level security     |   No      |  Yes       |
|Hierarchical security     |  No       |  Yes       |
|Record sharing     |  No       |  Yes       |

## Integration

Integration with Dataverse for Teams is delivered primarily through connectors. Support for both standard connectors and the ability to use the Dataverse connector to connect to a Dataverse for Teams for a Teams environment is included. Users with Premium licenses have access to the full set of over 350 standard and premium connectors available. This provides the ability to bring data into or retrieve data from tables in Dataverse for Teams, execute workflows when data in those tables change, and also use data from tables in workflow logic.

Dataverse can also use connectors. Additionally, Dataverse includes other built-in integration capabilities that can export data to a data lake or publish events to an event hub, service bus, or by using webhooks. Dataverse also supports the TDS protocol, which provides integration with SQL Server.

Dataverse can also be used with server-side sync to synchronize with Exchange or POP3, and with Data Export Service, which synchronizes data to Azure SQL Database.


|Integration feature  |Dataverse for Teams  |Dataverse  |
|---------|---------|---------|
|Power Automate     |   Yes      |  Yes       |
|Azure Synapse Link for Dataverse    |   No      |  Yes       |
|Data Export Service     |   No      |  Yes       |
|Events to Azure Event Hubs     |   No      |  Yes       |
|Events to Azure Service Bus     |   No      |  Yes       |
|Webhooks     |   No      |  Yes       |
|Server-side sync     |   No      |  Yes       |
|SQL Server Management Studio     |   No      |   Yes      |

  

### See also

[Create a table](create-table.md)


[!INCLUDE[footer-include](../includes/footer-banner.md)]
