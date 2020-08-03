---
title: Dataflex tables - Overview | Microsoft Docs
description: Provides an overview of tables in Microsoft Teams.
author: NHelgren
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 08/17/2020
ms.author: nhelgren
ms.reviewer: matp
---
# Dataflex tables: Overview

Tables provide the ability to create, populate, and query data within Microsoft Dataflex. Tables represent different types of entities important to an organization, such as a table to store products or another to store orders.  

Each of these tables contains columns that contain data about the subject of the table. For example, a table named Product could have columns that contain a product name, product identifier, manufacturer identifier, and price. Each of these columns may contain different types of data. For example, identifiers could be numbers, a price represents a cost in a specific currency, and so on.

A solution will often have multiple tables that are used together in an application. For example, an Order table may reference multiple other tables (Customer, Product, Country, etc.)  These tables are “related” to one another and tables provide the way to create those relationships.

> [!NOTE]
> All the capabilities found in tables are powered by Dataflex. While this will satisfy many situations, there are situations where an organization may want to have additional capacity, capabilities, or control over their solution. In these scenarios, Dataflex environments can be upgraded to Dataflex Pro (formerly Common Data Service). The upgrade process, referred to as *promotion*, has several considerations discussed later. 

The next several topics cover information about tables in Dataflex, how to create and manage them, define what data columns are in your table, and more. 

### See also
[Dataflex vs Dataflex Pro](data-platform-compare.md)
