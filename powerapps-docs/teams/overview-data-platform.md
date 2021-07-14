---
title: Microsoft Dataverse for Teams overview | Microsoft Docs
description: Provides the benefits of Dataverse for Teams.
author: NHelgren
ms.service: powerapps
ms.topic: conceptual
ms.custom: intro-internal
ms.date: 09/22/2020
ms.subservice: teams
ms.author: nhelgren
ms.reviewer: matp
---
# Overview of Microsoft Dataverse for Teams

Microsoft Dataverse for Teams delivers a built-in, low-code data platform for Microsoft Teams. It provides relational data storage, rich data types, enterprise-grade governance, and one-click solution deployment. Dataverse for Teams enables everyone to easily build and deploy apps.

:::image type="content" source="media/tables-in-teams.png" alt-text="Dataverse for Teams table in Teams.":::

Some of the benefits of Dataverse for Teams include:

- Support to build low-code and no-code apps, flows, and chatbots for and within Teams.

- Core data capabilities from the same platform behind Microsoft Power Platform and Dynamics 365.

- Storage, rich data types with enterprise capabilities, and one-click solution deployment.

- A new visual editor that makes it even easier to define and populate table data.

- Enterprise security that's easy to use and aligned with the approach used in Teams.

- Inclusion in most existing Teams licenses.

- Storage of 2 GB per team, and support for up to 1 million rows.

- Support for up to 500 teams.

- The capability to be upgraded to Dataverse.

See also: [Dataverse for Teams FAQs](data-platform-faqs.md)

## Tables in Dataverse for Teams

Dataverse for Teams tables provide the ability to create, populate, and query data within Dataverse for Teams. Tables represent different types of entities important to an organization, such as a table to store products or another to store orders.  

Each of these tables includes columns that contain data about the subject of the table. For example, a table named *Product* might have columns that contain a product name, product identifier, manufacturer identifier, and price. Each of these columns can contain different types of data. For example, the type of data for a product name is text, identifiers could be numbers, and so on.

A solution often has multiple tables that are used together in an application. For example, an Order table might reference multiple other tables, such as Customer, Product, and Country. These tables are "related" to one another, and tables provide the way to create those relationships.

You can create and populate these tables with a new visual editor that makes it even easier to work with these tables.

> [!NOTE]
> All the capabilities found in tables are powered by Dataverse for Teams. Although this will satisfy many situations, in some situations an organization might want to have additional capacity, capabilities, or control over their solution. In these scenarios, Dataverse for Teams environments can be upgraded to Microsoft Dataverse. The upgrade process has several considerations discussed in [Upgrade process](/power-platform/admin/about-teams-environment#upgrade-process) in the Microsoft Power Platform admin guide.

## Security in Dataverse for Teams

These tables and the applications that use them are secured with enterprise-grade security that's easy to understand and use for low-code and no-code developers. Security in Dataverse for Teams aligns to how security is handled in Teams, with a focus on Owners, Members, and Guests.

## Administer Dataverse for Teams environment

You can administer and manage Dataverse for Teams environment using the Power Platform admin center. More information: [About the Dataverse for Teams environment](/power-platform/admin/about-teams-environment) in the Power Platform admin guide.

### See also

[How are Dataverse for Teams and Dataverse different?](data-platform-compare.md) <br />
[Create tables](create-table.md)<br/>
[Work with table relationships](relationships-table.md)<br/>
[Dataverse for Teams FAQs](data-platform-faqs.md)


[!INCLUDE[footer-include](../includes/footer-banner.md)]