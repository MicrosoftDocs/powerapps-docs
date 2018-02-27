---
title: Understand entities | Microsoft Docs
description: Introduction to entities, fields, relationships, and databases.
services: powerapps
documentationcenter: na
author: clwesene
manager: kfend
editor: ''
tags: ''

ms.service: powerapps
ms.devlang: na
ms.topic: article
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 10/20/2017
ms.author: kfend

---
# Understand entities in the Common Data Service

The Common Data Service allows you to securely store and manage data within a set of standard and custom entities. An entity is a set of fields used to store data similarly to a table within a database. After your data is stored you can use Microsoft PowerApps to build rich applications using your data:

* Import data into standard or custom entities.
* Create custom entities to support your scenario and application.
* Add custom fields to standard entities where additional information is needed.
* Incorporate standard and custom entities into an app that you're developing as easily as you would with data in other sources.
* Leverage the productivity add-ins to access your data from Microsoft Excel and Outlook.
* Secure your data within your organization using role-based security against standard and custom entities.
* Include picklists of predefined data, such as Country, Salutation, or Currency.
* Provide global support for your data and applications by leveraging translation of entity and field names.

Each entity contains a set of records that users can create, read, update, and delete. You can create relationships between entities so that you can look up information in one entity based on a record in another entity. For example, you could create a custom entity to track events which a customer had attended. By adding the Customer to your custom entity as a lookup field, you establish a relationship between the two entities which can be leveraged in your app and in reporting.

For information on purchasing a plan for using the Common Data Service, see [Pricing info](pricing-billing-skus.md).

## Why use entities?
Entities within the Common Data Service, both standard and custom, allow a secure and cloud-based storage option for your data. Entities allow you to create a business-focused definition of your data for use within your apps. If you're not sure if entities are your best option, consider these benefits:

* **Easy to manage** - Both the metadata and data are stored in the cloud. You don't need to worry about the details of how they're stored.
* **Easy to share** - You can easily share data with your colleagues because PowerApps manages the permissions.
* **Easy to secure** - Data is securely stored so that users can see it only if you grant them access. Role-based security allows you to control access to entities for different users within your organization.
* **Rich metadata** - Data types and relationships are leveraged directly within PowerApps. For example, defining a field type URL will present your data as a hyperlink within your app.
* **Productivity tools** - Entities are available within the add-ins for Microsoft Excel and Outlook to increase productivity, and ensure your data is accessible.
* **Picklists** - Include picklists from a rich set of standard picklists to provide quick drop downs within your entities and apps.

## Standard and custom entities
When you develop an app, you can use standard entities, custom entities, or both. If a standard entity can serve a particular purpose in your app, you should use it rather than developing a custom entity that does the same thing. If a standard entity would serve a purpose with a few changes, you can add fields to suit your needs.

* The Common Data Service provides standard entities by default. These are designed, in accordance with best practices, to capture the most common concepts for an organization, such as Contacts, Accounts, and Products. For a full list of entities, see [Standard entities](data-platform-intro.md#standard-entities).
* You can extend the functionality of standard entities by creating one or more custom entities to store information that's unique to your organization. For more information, see [How to create a custom entity](data-platform-create-entity.md).

> [!NOTE]
> If possible, use standard entities (with custom fields added, if required). This will ensure that you can benefit from new features or apps that leverage these entities in the future.


## Fields
Each field has a name, display name, data type, and some simple validation. Data types include, for example, **text**, **date**, or **number**. Validation ensures that required fields contain data and records are unique if the entity requires them to be. Every field falls into one of three categories: system fields, standard fields, or custom fields.

### System fields
All entities, whether standard or custom, are created with a set of read-only fields that you can't change, delete, or set to a value. For more information, see [System and record title fields](data-platform-create-entity.md#system-fields-and-the-record-title-field). These are the most important system fields:

* **Created Record Date** - The date and time when a record was created.
* **Created By** - The user who created the record.
* **Modified Record Date** - The date and time when a record was most recently modified.
* **Last Modified By** - The user who most recently modified the record.

### Standard fields
Each standard entity contains a set of default fields that you can't change or delete. For a list of the entities and their fields, and a list of the picklists, see [Standard entities](https://docs.microsoft.com/common-data-service/entity-reference/standard-entities).

### Custom fields
You can create custom fields in either a standard entity or a custom entity. You must specify the name, display name, and data type of each custom field. For a complete list of supported types, see [Entity field data types](https://docs.microsoft.com/common-data-service/entity-reference/field-data-types).

## Lookup relationships
You can navigate between records in entities if they have a relationship that's defined as a field of the **Lookup** data type. To create a lookup relationship, add a field of data type **Lookup** in one entity, and point to the entity in which you want to look up information. For more information, see [Entity relationships via lookup field](data-platform-entity-lookup.md).

## Standard entities
For a list of the entities and their fields, and a list of the enumerations, see [Standard entities](https://docs.microsoft.com/common-data-service/entity-reference/standard-entities).

| Functional group | Description |
| --- | --- |
| Customer Service |The Customer Service entities manage issues from your customers, including tracking, escalation, and documentation. |
| Foundation |The Foundation entities contain information that is relevant to nearly every other entity group. This group contains entities such as Address and Currency. |
| People, Organizations, and Groups |These entities encompass a rich set of people and organizations that you might interact with, including employees, contractors, donors, volunteers, fans, alumni, and families. |
| Purchasing |The Purchasing entities let you create purchasing solutions. |
| Sales |The Sales entities let you create end-to-end sales solutions, from tracking leads and opportunities, to following through with contacts, accepting and delivering orders, and sending invoices. |

## Get started
Try it out by creating an app using a standard entity or [create a custom entity](data-platform-create-entity.md), and then [create an app that uses that entity](maker/data-platform-create-app.md).

<!--TODO - Add Link for Standard entity app - Template? -->

## Privacy notice
With the Microsoft PowerApps common data model we collect and store custom entity and field names in our diagnostic systems.  We use this knowledge to improve the common data model for our customers. The entity and field names that Creators create help us understand scenarios that are common across the Microsoft PowerApps community and ascertain gaps in the service’s standard entity coverage, such as schemas related to organizations. The data in the database tables associated with these entities is not accessed or used by Microsoft or replicated outside of the region in which the database is provisioned. Note, however, the custom entity and field names may be replicated across regions and are deleted in accordance with our data retention policies. Microsoft is committed to your privacy as described further in our [Trust Center](https://www.microsoft.com/trustcenter/Privacy/default.aspx).

