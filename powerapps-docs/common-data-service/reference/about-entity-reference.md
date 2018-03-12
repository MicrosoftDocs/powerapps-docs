---
title: "About Entity Reference (Common Data Service for Apps)| MicrosoftDocs"
description: "Use this reference to understand the available operations that can be performed for specific entities, the default attributes attributes of each entity and the relationships between entities."

services: ''
suite: powerapps
documentationcenter: na
author: JimDaly
manager: faisalmo
editor: ''
tags: ''

ms.service: powerapps
ms.devlang: na
ms.topic: reference
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 03/12/2018
ms.author: jdaly
---
# About the Entity Reference

Use this reference to understand the available operations that can be performed for specific entities, the default attributes attributes of each entity and the relationships between entities.

> [!NOTE]
> This reference includes only entities where:
>
> -  **IsPrivate** equals `false`
>    - This excludes entities where no external use cases exist.
> - **IsIntersect** equals `false`
>    - This excludes entities used to define Many-to-many relationships.
> - The entity supports some kind of operation.
>    - This excludes entities which you can't use. 
>
> To see all entity metadata information for your environment, see [Dynamics 365 Developers Guide : Browse the metadata for your organization](/dynamics365/customer-engagement/developer/browse-your-metadata).


## Entity Properties

This section includes selected entity properties rather than all of them. Only those properties expected to be most useful for developers are included. Some entity properties can be changed.

## Attributes
Attributes are listed in two separate sections: **Writable attributes** and **Read-only attributes**. The purpose of this separation is to focus on the attributes a developer can set when creating or updating an entity instance. Understanding these attributes helps a developer understand what they can do with the entity beyond simply retrieving the values. 

The attributes in the **Writable attributes** section return true for *either*  the **IsValidForCreate** or **IsValidForUpdate** properties, (usually both). If either of these properties return false, this is indicated.

**Read-only attributes** are always return false for the **IsValidForCreate** *and* **IsValidForUpdate** properties.

## Relationships

The <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata> class includes three properties to represent relationships:

|Property| Type  |Description  |
|---------|---------|---------|
|<xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.OneToManyRelationships>|<xref:Microsoft.Xrm.Sdk.Metadata.OneToManyRelationshipMetadata>[]|Gets the array of one-to-many relationships for the entity.|
|<xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.ManyToOneRelationships>|<xref:Microsoft.Xrm.Sdk.Metadata.OneToManyRelationshipMetadata>[]|Gets the array of many-to-one relationships for the entity.|
|<xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.ManyToManyRelationships>|<xref:Microsoft.Xrm.Sdk.Metadata.ManyToManyRelationshipMetadata>[]|Gets the array of many-to-many relationships for the entity.|

> [!NOTE]
> It is important to keep in mind that while each entity lists those relationships which apply to it, each relationship is shared by both related entities. The relationships exist *between* entities. While One-To-Many relationships exist, *Many-to-One* relationships are simply a view of a One-To-Many relationship from the referencing entity.

### One-to-Many relationships
In order to represent that there are no actual *Many-to-One* relationships with a minimum of confusion, the details of each relationship are only documented once. Each One-to-Many relationship is listed with the referenced entity and includes selected relationship details and a link to the corresponding *Many-to-One* relationship. Each *Many-to-One* relationship listed includes only a link to the corresponding One-to-Many relationship.

### Many-to-Many relationships
Each Many-to-Many relationship includes <xref:Microsoft.Xrm.Sdk.Metadata.ManyToManyRelationshipMetadata.Entity1LogicalName> and <xref:Microsoft.Xrm.Sdk.Metadata.ManyToManyRelationshipMetadata.Entity2LogicalName>. For this documentation relationship details are only included in the topic for *Entity1*. Each Many-to-Many relationship where the entity is *Entity2* includes only a link to the details found in the topic for *Entity1*.

## Messages

The messages in this list are applicable for the entity. For example, user-owned entities support the `Assign`, `GrantAccess`, `ModifyAccess`, and `RevokeAccess` messages while organization-owned entities do not. Other entities will have specialized messages, such as `DeleteAuditData` which applies only to the [Audit Entity](entities/audit.md).

### Organization service
When using the Organization service, you can usually invoke the corresponding request class which will belong to either the <xref:Microsoft.Crm.Sdk.Messages> or <xref:Microsoft.Xrm.Sdk.Messages> namespaces. These classes have names that include the `Request` prefix added to the message name.

### Web API
When using the Web API, you can usually invoke the corresponding Function or Action with the same name as the message. Not every message that can be invoked using the SDK assemblies have a corresponding Web API function or action. For example, the `SetState` message is deprecated and was not implemented for the Web API.
