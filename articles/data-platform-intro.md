<properties
	pageTitle="Understanding tables"
	description="Introduction to tables, fields, relationships and workspaces."
	services="powerapps"
	documentationCenter="na"
	authors="guangyang"
	manager="dwrede"
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

# Understanding Tables

PowerApps provides a powerful data platform with many capabilities that make it easier to create applications. In this platform, data is stored in tables. Each table has a set of fields of a particular data type. Information is stored as records of the table. Tables can be related to other tables via lookup. Applications can create, read, update and delete records in a table.

## Why Tables?

PowerApps support both storing data in the platform as well connecting to your organization's existing data both in the cloud and on-premises. Having said that, tables offering the following benefits:

- Rich metadata: It provides rich metadata describing the schema of your data, which will be used in the applications you build. You can easily define tables and fields work nice with PowerApps.
- Easy to manage: Both the metadata and data are stored in the cloud. You don't need to worry about the details of how they are stored.
- Easy to share: It's easy to share data with your colleagues. PowerApps will figure out the permission.
- Secure: Data is stored securely that only people who you granted access can see them.

If you are building applications storing some new data, tables is a great option for you. Or if you have some existing data in some ad-hoc data source (like Excel files), importing them into tables is also recommended.

## Standard and Custom Tables

There are two types of tables:

- **Standard tables**: These are tables provided by PowerApps out-of-box, like [Contact](), [Account]() and [Product](), etc. They are designed to capture the most common concepts for an organization with best practices. For a full list of standard tables, please go [here]().
- **Custom tables**: These are new tables you create to store information unique to your organization. They are designed to extend the functionality that standard tables provide.

It is always a good idea to leverage standard tables whenever they fit your organization's needs. You can add new fields to a standard table to customize it without creating a whole new custom table. When you do such kind of customization on standard tables, keep in mind that you cannot make any breaking changes (like deleting a standard field) or any changes that restrict the information stored in the standard tables (like adding a new required field). This guarantees the same baseline of standard tables for all organizations.

To learn how to create a table, please go [here]().

## Fields

Each table contains a set of fields. Each field has both name and display name, data type, like text or number, and some simple validation like required or uniqueness. There are three types of fields.

### System Fields

All tables, standard and custom have a set of read-only fields provided by the system. These fields cannot be changed or deleted. The value will also be assigned by the system automatically. Following is a list of the most important system fields:

- CreatedDateTime: the date and time when a record was created.
- ModifiedDateTime: the date and time when a record was last modified.

For a full list of system fields, please go [here]().

### Standard Fields

These are fields in the standard tables provided by the system. These fields cannot be changed or deleted. For a full list of standard tables and corresponding standard fields, please go [here]().

### Custom Fields

These are fields created by you. You can create custom fields in both standard and custom tables. In addition to the name and display name, all fields must be defined as a particular data type. Following is a list of the most important data types PowerApps supports today.

- Number Sequence: a system generated read-only sequence number. Usually used as the record unique ID.
- Text: text of various lengths.
- Number: number.
- Boolean: true or false.
- DateTime: date and time.
- Enumeration: one value from a list of values.
- Currency: numeric value representing money.
- Email: text value representing email.
- Phone: text value representing phone number.
- URL: text value representing URL.
- Location: location by latitude and longitude.

For a full list of supported data types, please go [here](). To learn how to manage fields in a table, please go [here]().

## Relationships

Tables can have relationships between each other. Such relationships are defined as fields of data type lookup, which allow you to navigate from records of one table to the corresponding records in another table. Creating a relationship is as simple as adding a field of data type lookup and pointing to the table you want to look up to.

To learn how to create relationships in details, please go [here]().

## Workspace

A workspace is a set of tables sharing the same scope and security boundary. By default, every user who has permission to manage tables has his/her own workspace and they'll have their own copy of the standard tables in their own workspaces.

Workspace provides a separation of tables so that within an organization, different individuals or groups can create tables with the same name. You can also share your workspace with others so that multiple people within an organization can collaborate on the same set of tables.

## Get Started

Want to try it out? Please go through the following articles:

1. [Create a table]().
2. [Create a PowerApps using tables]().