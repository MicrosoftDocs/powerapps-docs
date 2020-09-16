---
title: Project Oakdale overview | Microsoft Docs
description: Provides an overview of Project Oakdale.
author: NHelgren
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 08/17/2020
ms.author: nhelgren
ms.reviewer: matp
---
# Overview of Project Oakdale

[!INCLUDE [cc-beta-prerelease-disclaimer.md](../includes/cc-beta-prerelease-disclaimer.md)]

Project Oakdale delivers a built-in, low-code data platform for Teams. It provides relational data storage, rich data types, enterprise grade governance, and one-click solution deployment. Project Oakdale enables everyone to easily build and deploy apps.

:::image type="content" source="media/tables-in-teams.png" alt-text="Project Oakdale table in Teams":::

Some of the benefits of Project Oakdale include:

- Support to build low-code and no-code apps, flows, and chatbots for and within Teams

- Core data capabilities from the same platform behind Microsoft Power Platform and Dynamics 365

- Storage, rich data types with enterprise capabilities, and one-click solution deployment

- A new table designer that makes it even easier to define and populate data

- Enterprise security that is easy to use and aligned with Teams approach

- Inclusion in most existing Teams licenses

- With 2 GB storage per team, can support up to 1 million rows

- Support for up to 500 teams

- Can be promoted to full Common Data Service

## Tables in Project Oakdale

Project Oakdale tables provide the ability to create, populate, and query data within Project Oakdale. Tables represent different types of entities important to an organization, such as a table to store products or another to store orders.  

Each of these tables contains columns that contain data about the subject of the table. For example, a table named *Product* could have columns that contain a product name, product identifier, manufacturer identifier, and price. Each of these columns may contain different types of data. For example, identifiers could be numbers, a price represents a cost in a specific currency, and so on.

A solution will often have multiple tables that are used together in an application. For example, an Order table may reference multiple other tables (Customer, Product, Country, etc.)  These tables are “related” to one another and tables provide the way to create those relationships.

You can create and populate these tables with a new table designer that makes it even easier to work with these tables.

> [!NOTE]
> All the capabilities found in tables are powered by Project Oakdale. While this will satisfy many situations, there are situations where an organization may want to have additional capacity, capabilities, or control over their solution. In these scenarios, Project Oakdale environments can be upgraded to Common Data Service. The upgrade process, referred to as *promotion*, has several considerations discussed in [Promotion process](/power-platform/admin/about-teams-environment?branch=teams-preview#promotion-process) in the Power Platform admin guide.

## Security in Project Oakdale

These tables and the applications that use them are secured with enterprise-grade security that is easy to understand and use for low-code and no-code developers. Security in Project Oakdale aligns to how security is handled in Teams, with a focus on Owners, Members, and Guests. 

### See also
[How are Project Oakdale and Common Data Service different?](data-platform-compare.md) <br />
[Work with table relationships](relationships-table.md)
