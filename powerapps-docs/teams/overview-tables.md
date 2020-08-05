---
title: ***REMOVED*** tables - Overview | Microsoft Docs
description: Provides an overview of tables in Microsoft Teams.
author: NHelgren
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 08/17/2020
ms.author: nhelgren
ms.reviewer: matp
---
# ***REMOVED*** tables: Overview
Microsoft ***REMOVED*** delivers a built-in, low-code data platform for Teams. It provides relational data storage, rich data types, enterprise grade governance, and one-click solution deployment. ***REMOVED*** enables everyone to easily build and deploy apps. 

***REMOVED*** tables provide the ability to create, populate, and query data within ***REMOVED***. Tables represent different types of entities important to an organization, such as a table to store products or another to store orders.  

Each of these tables contains columns that contain data about the subject of the table. For example, a table named *Product* could have columns that contain a product name, product identifier, manufacturer identifier, and price. Each of these columns may contain different types of data. For example, identifiers could be numbers, a price represents a cost in a specific currency, and so on.

A solution will often have multiple tables that are used together in an application. For example, an Order table may reference multiple other tables (Customer, Product, Country, etc.)  These tables are “related” to one another and tables provide the way to create those relationships.

> [!NOTE]
> All the capabilities found in tables are powered by ***REMOVED***. While this will satisfy many situations, there are situations where an organization may want to have additional capacity, capabilities, or control over their solution. In these scenarios, ***REMOVED*** environments can be upgraded to ***REMOVED*** Pro (formerly Common Data Service). The upgrade process, referred to as *promotion*, has several considerations discussed in [Promotion process](/power-platform/admin/about-teams-environment?branch=teams-preview#promotion-process). 

### See also
[How are ***REMOVED*** and ***REMOVED*** Pro different?](data-platform-compare.md) <br />
[Work with table relationships](relationships-table.md)
