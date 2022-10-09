---
title: "Query Schema Definitions (Microsoft Dataverse) | Microsoft Docs"
description: "Write a query to retrieve definitions of tables, columns, relationships, and labels for a Dataverse organization. Optionally, track changes to these definitions over time."
ms.date: 10/12/2022
ms.topic: article
author: NHelgren
ms.subservice: dataverse-developer
ms.author: nhelgren
ms.reviewer: jdaly
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors:
 - JimDaly
---

# Query Schema Definitions

Applications built using Dataverse need to be able to adapt to changes to schema definitions. New tables, columns, relationships, and labels can be added or changed via configuration or by importing a solution. Because applications need to be able to respond to these changes, they frequently depend on retrieving schema definitions when they start. However, the total amount of data describing the schema of a Dataverse organization can be very large. You need to be able to know how to get just the data you need.

The `RetrieveMetadataChanges` message provides two capabilities:

1. **Query**: Compose a single query to retrieve just the schema data you need. This is the focus of this topic.
1. **Cache Management**: If you cache the schema definition data with your app, you can use `RetrieveMetadataChanges` to efficiently retrieve only the changes since your last query. Use the information about these changes to add or remove items in your cache. This may result in a significant improvement time for your application to start. Cache management is covered in [Cache Schema data](cache-schema-data.md).


## Evaluate other options to retrieve schema definitions

When composing a query to retrieve schema definitions, `RetrieveMetadataChanges` message provides an advantage to define a single request that can span multiple table definitions and return details for derived types as well as manage a cache over time.

The following table summarizes other ways you can retrieve schema definitions, but none of them provide capabilities to manage a cache over time.

#### [SDK for .NET](#tab/sdk)


|Message|Description|
|---------|---------|
|`RetrieveAllEntities`|Retrieves data for all tables, including all columns, privileges, and relationships if you wish.<br />While it does provide for filtering out parts you don’t need, it is a very expensive operation.<br />See: <xref:Microsoft.Xrm.Sdk.Messages.RetrieveAllEntitiesRequest?text=RetrieveAllEntitiesRequest> and <xref:Microsoft.Xrm.Sdk.Messages.RetrieveAllEntitiesResponse?text=RetrieveAllEntitiesResponse> classes.|
|`RetrieveEntity`|You can retrieve definition of any single table including all columns, privileges, and relationships if you wish. You can’t select which specific properties you want.<br />See: [Retrieve and update a table](org-service/metadata-retrieve-update-delete-entities.md#retrieve-and-update-a-table)|
|`RetrieveAttribute`|You can retrieve the complete definition of any single attribute, but you can’t select which specific properties you want.<br />See: [Retrieve a column](org-service/metadata-attributemetadata.md#retrieve-a-column)|
|`RetrieveRelationship`|You can retrieve the complete definition of any single relationship, but you can’t select which specific properties you want.<br />See: [Retrieve table row relationships](org-service/metadata-relationshipmetadata.md#retrieve-table-row-relationships)|
|`RetrieveAllOptionSets`|You can retrieve information about all the global choices defined in the organization, but this doesn’t include choices that are only defined locally within a column.<br />See: [Insert, update, delete, and order global choices](org-service/metadata-global-option-set-options.md)|
|`RetrieveEntityKey`|You can retrieve the definition for any alternate keys for a specific table. <br />See:[Retrieve and delete alternate keys](define-alternate-keys-entity.md#retrieve-and-delete-alternate-keys)|


#### [Web API](#tab/webapi)

|Method|Description|
|---------|---------|
|<xref:Microsoft.Dynamics.CRM.RetrieveAllEntities?text=RetrieveAllEntities Function>|Retrieves data for all tables, including all columns, privileges, and relationships if you wish.<br />While it does provide for filtering out parts you don’t need, it is a very expensive operation.|
|<xref:Microsoft.Dynamics.CRM.RetrieveEntity?text=RetrieveEntity Function>|You can retrieve definition of any single table including all columns, privileges, and relationships if you wish.<br />While it does provide for filtering out parts you don’t need, it is still an expensive operation.|
|`EntityDefinitions` EntitySet|Enables a query for multiple table definitions using OData syntax to filter and select the properties you want to return.  Expand the `Attributes`,`Keys`,`ManyToManyRelationships`,`ManyToOneRelationships`, and `OneToManyRelationships` collection-valued navigation properties to get information about relationships, alternate keys and columns.<br/>Cannot return properties specific to column entity types that are derived from <xref:Microsoft.Dynamics.CRM.AttributeMetadata?text=AttributeMetadata EntityType> without casting. Each query that expands `Attributes` can only cast to a single derived column type, so multiple requests may be required. For example, you can't get the `OptionSet` definitions for both a <xref:Microsoft.Dynamics.CRM.BooleanAttributeMetadata> column and a <xref:Microsoft.Dynamics.CRM.PicklistAttributeMetadata> column in the same query.<br/>If you don't need to manage a cache, and you don't need details about derived column entity types in a single request or you don't mind sending multiple requests, this may be all you need. <br/>See [Query table definitions using the Web API](webapi/query-metadata-web-api.md)|
|`RelationshipDefinitions` EntitySet|Enables a query for multiple relationship definitions using OData syntax to filter and select the properties you want to return. <br />Contains data for both <xref:Microsoft.Dynamics.CRM.OneToManyRelationshipMetadata> and <xref:Microsoft.Dynamics.CRM.ManyToManyRelationshipMetadata> EntityTypes. You must cast your query to either of those types to select or filter based on properties they possess, otherwise you are limited to the shared properties from the base <xref:Microsoft.Dynamics.CRM.RelationshipMetadataBase?text=RelationshipMetadataBase EntityType> that those entity types are derived from. If you need to select or filter on specific properties from either derived types, you will need to send two separate requests. More information: [Use the Web API with table definitions](webapi/use-web-api-metadata.md) |
|`GlobalOptionSetDefinitions` EntitySet|Enables a query for multiple global choice definitions using OData syntax to filter and select the properties you want to return.<br />Contains data for both <xref:Microsoft.Dynamics.CRM.BooleanOptionSetMetadata> and <xref:Microsoft.Dynamics.CRM.OptionSetMetadata> EntityTypes. You must cast your query to either of those types to select or filter based on properties they possess, otherwise you are limited to the shared properties from the base <xref:Microsoft.Dynamics.CRM.OptionSetMetadataBase?text=OptionSetMetadataBase EntityType> that those entity types are derived from. For example, `OptionSetMetadataBase` doesn't include the `Options`property. If you need to select or filter on specific properties from either derived types, you will need to send two separate requests. More information: [Use the Web API with table definitions](webapi/use-web-api-metadata.md)|

---


## Basic RetrieveMetadataChanges example

## Create a query using EntityQueryExpression

## Limit data returned using MetadataFilterExpression

## Process data returned

### See also

[Cache Schema data](cache-schema-data.md)<br />
[Organization Service: Table definitions in Microsoft Dataverse](entity-metadata.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]