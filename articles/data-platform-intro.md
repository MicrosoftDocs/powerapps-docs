<properties
	pageTitle="Understand tables | Microsoft PowerApps"
	description="Introduction to tables, fields, relationships, and workspaces."
	services="powerapps"
	documentationCenter="na"
	authors="guangyang"
	manager="erikre"
	editor=""
	tags=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="04/07/2016"
   ms.author="guayan"/>

# Understand tables in Microsoft PowerApps
You can store organizational data in one or more custom tables. Tables offer several benefits over external data sources such as Microsoft Excel and Salesforce:
* If you already have a set of data in another format, you can import it into a custom table
* You can use a custom table to compile a set of data from scratch.
* You can easily incorporate custom tables into an app that you're developing, just as you do with data in other sources.
* You can use generic data, such as a list of countries/regions from around the world, from standard tables that are built into Microsoft PowerApps.

Each table contains a set of records that users can create, read, update, and delete. Each record has information in various fields, and each field contains data of a specific type. You can create relationships between tables so that you can look up information in one table based on a record in another table. For example, you could create a product table that contains a record for each product and fields that contain the name, the price, and an image of each product. You would set the price field to the **currency** data type, and you could create a lookup relationship between that table and a customer table to identify which products each customer bought.

## Why tables?
If you're not sure whether tables are your best option, consider these benefits:

* Rich metadata: Tables provide rich metadata that describe the schema of your data and that is used in the apps that you build. You can easily define tables, and fields work nicely with PowerApps.
* Easy to manage: Both the metadata and data are stored in the cloud. You don't need to worry about the details of how they're stored.
* Easy to share: You can easily share data with your colleagues because PowerApps manages the permissions.
* Secure: Data is stored securely so that users can see it only if you grant them access.

## Standard and custom tables
When you develop an app, you can use standard tables, custom tables, or both:

- PowerApps provides standard tables by default. These are designed, in accordance with best practices, to capture the most common concepts for an organization, such as Contacts, Accounts, and Products. For the full list, see [Standard tables and enumeration types](data-platform-standard-tables.md).
- You can extend the functionality of standard tables by creating one or more custom tables to store information that's unique to your organization. For more information, see [how to create a custom table](data-platform-create-table.md).

If a standard table can serve a particular purpose in your app, you should use it rather than developing a custom table that does the same thing. If a standard table would serve a purpose with a few changes, you can add fields to suit your needs. However, you can't make changes that break the table (such as deleting a standard field) or that restrict its information (such as adding a required field). These requirements ensure that standard tables remain consistent across all organizations.

## Fields
Each field has a name, a display name, a data type (such as **text** or **number**), and some simple validation (for example, to check whether the field is required or to verify uniqueness). Every field falls into one of three categories: system field, standard field, or custom field.

### System fields
All tables, whether standard or custom, are created with a set of read-only fields, that you can't change, delete, or set to a value. For more information, see [System and record title fields](). These are the most important system fields:

- **CreatedDateTime**: The date and time when a record was created.
- **ModifiedDateTime**: The date and time when a record was modified most recently.

### Standard fields
Each standard table contains a set of default fields that you can't change or delete. For more information, see [the full list of standard tables and their default fields]().

### Custom fields
You can create custom fields in either a standard table or a custom table. You must specify the name, display name, and data type of a custom field. PowerApps supports these data types:

- Number Sequence: A sequence number that's read-only and generated automatically. Usually used as the record's unique ID.
- **Text**: Text of various lengths.
- **Number**: A number.
- **Boolean**: True or false.
- **DateTime**: A date and time.
- **Enumeration**: One value from a list of values.
- **Currency**: A numeric value that represents money.
- **Email**: A text value that represents an email address.
- **Phone**: A text value that represents a phone number.
- **URL**: A text value that represents a URL.
- **Location**: A location, as defined by its latitude and longitude.

For more information, see the [Manage fields in a table]().

## Lookup relationships
You can navigate between records in tables if they have a relationship that's defined as a field of the **lookup** data type. To create a lookup relationship, add a field of data type **lookup** in one table, and point to the table in which you want to look up information. For more information, see [Table relationships via lookup field]().

## Workspaces
You create a table in your own workspace so that other users can't see it unless you share it with them. In addition, other users can create tables that have the same name without conflicting with your table. Every workspace contains a copy of the standard tables.

## Get started ##
Try it out by [creating a table](data-platform-create-table.md) and then [creating an app that uses a table]().
