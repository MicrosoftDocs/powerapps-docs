---
title: Project Oakdale overview | Microsoft Docs
description: Provides an overview of Project Oakdale.
author: NHelgren
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 09/16/2020
ms.author: nhelgren
ms.reviewer: matp
---
# Overview of Project Oakdale

[!INCLUDE [cc-beta-prerelease-disclaimer.md](../includes/cc-beta-prerelease-disclaimer.md)]

Project Oakdale delivers a built-in, low-code data platform for Microsoft Teams. It provides relational data storage, rich data types, enterprise-grade governance, and one-click solution deployment. Project Oakdale enables everyone to easily build and deploy apps.

:::image type="content" source="media/tables-in-teams.png" alt-text="Project Oakdale table in Teams":::

Some of the benefits of Project Oakdale include:

- Support to build low-code and no-code apps, flows, and chatbots for and within Teams.

- Core data capabilities from the same platform behind Microsoft Power Platform and Dynamics 365.

- Storage, rich data types with enterprise capabilities, and one-click solution deployment.

- A new table designer that makes it even easier to define and populate data.

- Enterprise security that's easy to use and aligned with the approach used in Teams.

- Inclusion in most existing Teams licenses.

- Storage of 2 GB per team, and support for up to 1 million rows.

- Support for up to 500 teams.

- The capability to be promoted to full Common Data Service.

## Tables in Project Oakdale

Project Oakdale tables provide the ability to create, populate, and query data within Project Oakdale. Tables represent different types of entities important to an organization, such as a table to store products or another to store orders.  

Each of these tables includes columns that contain data about the subject of the table. For example, a table named *Product* might have columns that contain a product name, product identifier, manufacturer identifier, and price. Each of these columns can contain different types of data. For example, identifiers could be numbers, a price represents a cost in a specific currency, and so on.

A solution often has multiple tables that are used together in an application. For example, an Order table might reference multiple other tables (Customer, Product, and Country). These tables are "related" to one another, and tables provide the way to create those relationships.

You can create and populate these tables with a new table designer that makes it even easier to work with these tables.

> [!NOTE]
> All the capabilities found in tables are powered by Project Oakdale. Although this will satisfy many situations, in some situations an organization might want to have additional capacity, capabilities, or control over their solution. In these scenarios, Project Oakdale environments can be upgraded to Common Data Service. The upgrade process, referred to as *promotion*, has several considerations discussed in [Promotion process](/power-platform/admin/about-teams-environment?branch=teams-preview#promotion-process) in the Microsoft Power Platform admin guide.

## Security in Project Oakdale

These tables and the applications that use them are secured with enterprise-grade security that's easy to understand and use for low-code and no-code developers. Security in Project Oakdale aligns to how security is handled in Teams, with a focus on Owners, Members, and Guests.

### See also

[How are Project Oakdale and Common Data Service different?](data-platform-compare.md) <br />
[Create tables](create-table.md)<br/>
[Work with table relationships](relationships-table.md)
