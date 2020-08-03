---
title: Dataflex tables - Overview | Microsoft Docs
description: Provides an overview of creating apps in Microsoft Teams.
author: NHelgren
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 08/17/2020
ms.author: nhelgren
ms.reviewer: matp
---
# Dataflex tables: Overview

Tables provide the ability to create, populate, and query data within Dataflex. Tables represent different types of entities important to an organization, such as a table to store products or another to store orders.  

Each of these tables contains columns that contain data about the subject of the table. For example, a table named Product could have columns that contain a product name, product identifier, manufacturer identifier, and price. Each of these columns may contain different types of data – identifiers could be numbers, a price represents a cost in a specific currency, etc. 

A solution will often have multiple tables that are used together in an application. For example, an Order table may reference multiple other tables (Customer, Product, Country, etc.)  These tables are “related” to one another and Tables provides the way to create those relationships. 

> [!NOTE]
> All the capabilities found in tables are powered by Dataflex. While this will satisfy many scenarios, there are some where an organization may want to have additional capacity, capabilities, or control for their solution.  In these scenarios, Dataflex environments can be upgraded to Dataflex Pro (formerly Common Data Service). The upgrade process, referred to as “promotion”, has several considerations discussed later in this document. 

The next several sections will cover information about tables in Dataflex, how to create and manage them, defining what data columns are in your table, and more. 

### See also
