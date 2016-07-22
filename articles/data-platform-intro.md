<properties
	pageTitle="Understand entities | Microsoft Common Data Model"
	description="Introduction to entities, fields, relationships, and databases."
	services="powerapps"
	documentationCenter="na"
	authors="guangyang, karthikb"
	manager="darshand"
	editor=""
	tags=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="07/21/2016"
   ms.author="karthikb"/>

# Understand entities in Microsoft Common Data Model
You can store organizational data in one or more custom entities. Entities offer several benefits over external data sources such as Microsoft Excel and Salesforce:

* If you already have a set of data in another format, you can import it into a custom entity
* You can use a custom entity to compile a set of data from scratch.
* You can easily incorporate custom entities into an app that you're developing, just as you do with data in other sources.
* You can use generic data, such as a list of countries/regions from around the world, from standard entities that are built into Microsoft Common Data Model.

Each entity contains a set of records that users can create, read, update, and delete. Each record has information in various fields, and each field contains data of a specific type. You can create relationships between entities so that you can look up information in one entity based on a record in another entity. For example, you could create a product entity that contains a record for each product and fields that contain the name, the price, and an image of each product. You would set the price field to the **currency** data type, and you could create a lookup relationship between that entity and a customer entity to identify which products each customer bought.

## Why entities?
If you're not sure whether entities are your best option, consider these benefits:

* Rich metadata: Entities provide rich metadata that describe the schema of your data and that is used in the apps that you build. You can easily define entities, and fields work nicely with PowerApps.
* Easy to manage: Both the metadata and data are stored in the cloud. You don't need to worry about the details of how they're stored.
* Easy to share: You can easily share data with your colleagues because PowerApps manages the permissions.
* Secure: Data is stored securely so that users can see it only if you grant them access.

## Standard and custom entities
When you develop an app, you can use standard entities, custom entities, or both:

- Microsoft Common Data Model provides standard entities by default. These are designed, in accordance with best practices, to capture the most common concepts for an organization, such as Contacts, Accounts, and Products. For the full list, see [Standard entities and enumeration types](data-platform-standard-entities.md).
- You can extend the functionality of standard entities by creating one or more custom entities to store information that's unique to your organization. For more information, see [how to create a custom entity](data-platform-create-entities.md).

If a standard entity can serve a particular purpose in your app, you should use it rather than developing a custom entity that does the same thing. If a standard entity would serve a purpose with a few changes, you can add fields to suit your needs. However, you can't make changes that break the entity (such as deleting a standard field) or that restrict its information (such as adding a required field). These requirements ensure that standard entities remain consistent across all organizations.

## Fields
Each field has a name, a display name, a data type (such as **text** or **number**), and some simple validation (for example, to check whether the field is required or to verify uniqueness). Every field falls into one of three categories: system field, standard field, or custom field.

### System fields
All entities, whether standard or custom, are created with a set of read-only fields that you can't change, delete, or set to a value. For more information, see [System and record title fields](). These are the most important system fields:

- **CreatedOnDateTime**: The date and time when a record was created.
- **LastModifiedDateTime**: The date and time when a record was modified most recently.
- **LastModifiedByUser**: User who modified the record most recently.

### Standard fields
Each standard entity contains a set of default fields that you can't change or delete. For more information, see [the full list of standard entities and their default fields]().

### Custom fields
You can create custom fields in either a standard entity or a custom entity. You must specify the name, display name, and data type of a custom field. PowerApps supports these data types:

- **Boolean**: True or false.
- **Currency**: A numeric value that represents money.
- **DateTime**: A date and time.
- **Date**: A date.
- **Email**: A text value that represents an email address.
- **Enumeration**: One value from a list of values.
- **Image**: An image.
- **Integer**: A positive or negative value.
- **Lookup**: A lookup field into another entity's title field.
- **Multi line text**: Multiple lines of text.
- **Number**: A number.
- **Number Sequence**: A sequence number that's read-only and generated automatically. Usually used as the record's unique ID.
- **Phone**: A text value that represents a phone number.
- **Text**: Text of length upto 128 characters.
- **URL**: A text value that represents a URL.

For more information, see the [Manage fields in an entity]().

## Lookup relationships
You can navigate between records in entities if they have a relationship that's defined as a field of the **lookup** data type. To create a lookup relationship, add a field of data type **lookup** in one entity, and point to the entity in which you want to look up information. For more information, see [Entity relationships via lookup field]().

## Databases
You create an entity in your own database so that other users can't see it unless you share it with them. In addition, other users can create entities that have the same name without conflicting with your entity. Every database contains a copy of the standard entities.

## Get started ##
Try it out by [creating an entity](data-platform-create-entity.md) and then [creating an app that uses that entity](data-platform-create-app.md).
