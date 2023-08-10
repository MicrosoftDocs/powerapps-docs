---
title: Query schema definitions
description: Write a query to retrieve definitions of tables, columns, relationships, and labels for a Dataverse organization. Optionally, track changes to these definitions over time.
ms.date: 08/05/2023
ms.topic: how-to
author: NHelgren
ms.subservice: dataverse-developer
ms.author: nhelgren
ms.reviewer: jdaly
search.audienceType: 
  - developer
contributors:
 - JimDaly
---

# Query schema definitions

Applications built using Dataverse need to be able to adapt to changes to schema definitions. New tables, columns, relationships, and labels can be added or changed via configuration or by importing a solution. Because applications need to be able to respond to these changes, they frequently depend on retrieving schema definitions when they start. However, the total amount of data describing the schema of a Dataverse organization can be very large. You need to be able to know how to get just the data you need.

The `RetrieveMetadataChanges` message provides two capabilities:

1. **Query**: Compose a single query to retrieve just the schema data you need. This article focuses on composing queries.
1. **Cache Management**: If you cache the schema definition data with your app, you can use `RetrieveMetadataChanges` to efficiently retrieve only the changes since your last query. Use the information about these changes to add or remove items in your cache. Caching may result in a significant improvement time for your application to start. Cache management is covered in [Cache Schema data](cache-schema-data.md).


## Evaluate other options to retrieve schema definitions

When composing a query to retrieve schema definitions, `RetrieveMetadataChanges` message provides an advantage to define a single request that can span multiple table definitions and return details for derived types and manage a cache over time.

The following table summarizes other ways you can retrieve schema definitions, but none of them provide capabilities to manage a cache over time.

#### [SDK for .NET](#tab/sdk)


|Message|Description and limitations|
|---------|---------|
|`RetrieveAllEntities`|Retrieves data for all tables, including all columns, privileges, and relationships if you wish.<br />See: <xref:Microsoft.Xrm.Sdk.Messages.RetrieveAllEntitiesRequest?text=RetrieveAllEntitiesRequest> and <xref:Microsoft.Xrm.Sdk.Messages.RetrieveAllEntitiesResponse?text=RetrieveAllEntitiesResponse> classes.<br /><br />**Limitations**: While you can use the `EntityFilters` parameter to exclude some parts, it's a very expensive operation.|
|`RetrieveEntity`|You can retrieve definition of any single table including all columns, privileges, and relationships if you wish.<br />See: [Retrieve and update a table](org-service/metadata-retrieve-update-delete-entities.md#retrieve-and-update-a-table)<br /><br />**Limitations**:  While you can use the `EntityFilters` parameter to exclude some data, you can't select which specific properties you want, it's still an expensive operation.|
|`RetrieveAttribute`|You can retrieve the complete definition of any single attribute.<br />See: [Retrieve a column](org-service/metadata-attributemetadata.md#retrieve-a-column)<br /><br />**Limitations**: You can't select which specific properties you want.|
|`RetrieveRelationship`|You can retrieve the complete definition of any single relationship.<br />See: [Retrieve table row relationships](org-service/metadata-relationshipmetadata.md#retrieve-table-row-relationships)<br /><br />**Limitations**: You can't select which specific properties you want.|
|`RetrieveAllOptionSets`|You can retrieve information about all the global choices defined in the organization.<br />See: [Insert, update, delete, and order global choices](org-service/metadata-global-option-set-options.md)<br /><br />**Limitations**: Choices that are only defined locally within a column aren't included.|
|`RetrieveEntityKey`|You can retrieve the definition for any alternate keys for a specific table. <br />See:[Retrieve and delete alternate keys](define-alternate-keys-entity.md#retrieve-and-delete-alternate-keys)|


#### [Web API](#tab/webapi)

|Method|Description and limitations|
|---------|---------|
|<xref:Microsoft.Dynamics.CRM.RetrieveAllEntities?text=RetrieveAllEntities Function>|Retrieves data for all tables, including all columns, privileges, and relationships if you wish.<br /><br />**Limitations**: While you can use the `EntityFilters` parameter to exclude some parts, it's a very expensive operation.|
|<xref:Microsoft.Dynamics.CRM.RetrieveEntity?text=RetrieveEntity Function>|You can retrieve definition of any single table including all columns, privileges, and relationships if you wish.<br /><br />**Limitations**: While you can use the `EntityFilters` parameter to exclude some data, you can't select which specific properties you want, it's still an expensive operation.|
|`EntityDefinitions` EntitySet|Enables a query for multiple table definitions using OData syntax to filter and select the properties you want to return. <br />Expand the `Attributes`,`Keys`,`ManyToManyRelationships`,`ManyToOneRelationships`, and `OneToManyRelationships` collection-valued navigation properties to get information about columns, alternate keys, and relationships.<br/>See [Query table definitions using the Web API](webapi/query-metadata-web-api.md)<br /><br />**Limitations**: Can't return properties specific to column entity types that are derived from <xref:Microsoft.Dynamics.CRM.AttributeMetadata?text=AttributeMetadata EntityType> without casting. Each query that expands `Attributes` can only cast to a single derived column type, so multiple requests may be required. For example, you can't get the `OptionSet` definitions for both a <xref:Microsoft.Dynamics.CRM.BooleanAttributeMetadata> column and a <xref:Microsoft.Dynamics.CRM.PicklistAttributeMetadata> column in the same request.<br/><br/>If you don't need to manage a cache, and you don't need details about derived column entity types in a single request, or you don't mind sending multiple requests, this approach may be all you need. |
|`RelationshipDefinitions` EntitySet|Enables a query for multiple relationship definitions using OData syntax to filter and select the properties you want to return. <br />Contains data for both <xref:Microsoft.Dynamics.CRM.OneToManyRelationshipMetadata> and <xref:Microsoft.Dynamics.CRM.ManyToManyRelationshipMetadata> EntityTypes.<br /> More information: [Use the Web API with table definitions](webapi/use-web-api-metadata.md)  <br /><br />**Limitations**: You must cast your query to either of those types to select or filter based on properties they possess, otherwise you're limited to the shared properties from the base <xref:Microsoft.Dynamics.CRM.RelationshipMetadataBase?text=RelationshipMetadataBase EntityType> that those entity types are derived from. If you need to select or filter on specific properties from either derived types, you need to send two separate requests.|
|`GlobalOptionSetDefinitions` EntitySet|Enables a query for multiple *global* choice definitions using OData syntax to filter and select the properties you want to return.<br /> More information: [Use the Web API with table definitions](webapi/use-web-api-metadata.md)<br /><br />**Limitations**:<br /> - Doesn't include choices that are only defined locally within a column.<br /> - Contains data for both <xref:Microsoft.Dynamics.CRM.BooleanOptionSetMetadata> and <xref:Microsoft.Dynamics.CRM.OptionSetMetadata> entity types. You must cast your query to either of those types to select or filter based on properties they possess, otherwise you're limited to the shared properties from the base <xref:Microsoft.Dynamics.CRM.OptionSetMetadataBase?text=OptionSetMetadataBase EntityType> that those entity types are derived from. For example, `OptionSetMetadataBase` doesn't include the `Options` property. If you need to select or filter on specific properties from either derived types, you need to send two separate requests.|

---


## Basic RetrieveMetadataChanges example

For a simple example of what you can do with `RetrieveMetadataChanges`, compare what you can do with Web API and the `EntityDefinitions` entity set.

Using Web API you can compose a query like this:

```http
GET [Organization URI]/api/data/v9.2/EntityDefinitions?$select=SchemaName&$filter=LogicalName eq 'account' or LogicalName eq 'contact'&$expand=Attributes($select=LogicalName;$filter=IsValidForCreate eq true)
```

This query returns data from both the account and contact table definitions, and expand all the column definitions where `IsValidForCreate` is true.

The following examples show how to compose the same query using `RetrieveMetadataChanges`.

#### [SDK for .NET](#tab/sdk)

```csharp
/// <summary>
/// Get the SchemaName for the account and contact tables together with
/// the LogicalName of any attributes which are valid for create
/// </summary>
/// <param name="service"></param>
static void SimpleRetrieveMetadataChangesExample(IOrganizationService service) {

    var query = new EntityQueryExpression
    {
        Properties = new MetadataPropertiesExpression("SchemaName", "Attributes"),
        Criteria = new MetadataFilterExpression(filterOperator: LogicalOperator.Or)
        {
            Conditions = {
                {
                    new MetadataConditionExpression(
                        propertyName:"LogicalName",
                        conditionOperator: MetadataConditionOperator.Equals,
                        value:"account")
                },
                {
                    new MetadataConditionExpression(
                        propertyName:"LogicalName",
                        conditionOperator: MetadataConditionOperator.Equals,
                        value:"contact")
                }
            }, 
        },
        AttributeQuery = new AttributeQueryExpression
        {
            Properties = new MetadataPropertiesExpression("LogicalName"),
            Criteria = new MetadataFilterExpression(filterOperator: LogicalOperator.And)
            {
                Conditions = {
                    {
                        new MetadataConditionExpression(
                        propertyName:"IsValidForCreate",
                        conditionOperator: MetadataConditionOperator.Equals,
                        value:true)
                    }
                }
            }            
        },
        LabelQuery = new LabelQueryExpression { 
             FilterLanguages = {
                { 1033 }
            } 
        }
        
    };

    var request = new RetrieveMetadataChangesRequest
    {
        Query = query
    };

    var response = (RetrieveMetadataChangesResponse)service.Execute(request);

    response.EntityMetadata.ToList().ForEach(em => {

        Console.WriteLine($"Entity SchemaName:{em.SchemaName}");
        em.Attributes.ToList().ForEach(a => {
            Console.WriteLine($"\tAttribute LogicalName:{a.LogicalName}");
        });
    });
}
```

**Output:**

```text
Entity SchemaName:Account
        Attribute LogicalName:emailaddress3
        Attribute LogicalName:emailaddress1
        Attribute LogicalName:address1_city
    <List truncated for brevity>
Entity SchemaName:Contact
        Attribute LogicalName:contactid
        Attribute LogicalName:emailaddress3
        Attribute LogicalName:emailaddress2
    <List truncated for brevity>
```

#### [Web API](#tab/webapi)

The [RetrieveMetadataChanges function](xref:Microsoft.Dynamics.CRM.RetrieveMetadataChanges) `Query` parameter requires a URL encoded string representing the JSON value of the query, which is an [EntityQueryExpression complex type](xref:Microsoft.Dynamics.CRM.EntityQueryExpression).
The following JSON is the query.

```json
{
   "Properties": {
      "AllProperties": false,
      "PropertyNames": ["SchemaName","Attributes"]
   },
   "Criteria": {
      "FilterOperator": "Or",
      "Conditions": [
         {
            "ConditionOperator": "Equals",
            "PropertyName": "LogicalName",
            "Value": {
               "Type": "System.String",
               "Value": "account"
            }
         },
         {
            "ConditionOperator": "Equals",
            "PropertyName": "LogicalName",
            "Value": {
               "Type": "System.String",
               "Value": "contact"
            }
         }
      ]
   },
   "AttributeQuery": {
      "Properties": {
         "AllProperties": false,
         "PropertyNames": ["LogicalName"]
      },
      "Criteria": {
         "FilterOperator": "And",
         "Conditions": [
            {
               "ConditionOperator": "Equals",
               "PropertyName": "IsValidForCreate",
               "Value": {
                  "Type": "System.Boolean",
                  "Value": "True"
               }
            }
         ]
      }
   },
   "LabelQuery": {
      "FilterLanguages": [1033],
      "MissingLabelBehavior": 0
   }
}
```

**Request:**

```http
GET [Organization URI]/api/data/v9.2/RetrieveMetadataChanges(Query=@p1)?@p1=%7B%22AttributeQuery%22:%7B%22Criteria%22:%7B%22Conditions%22:[%7B%22ConditionOperator%22:%22Equals%22,%22PropertyName%22:%22IsValidForCreate%22,%22Value%22:%7B%22Type%22:%22System.Boolean%22,%22Value%22:%22True%22%7D%7D],%22FilterOperator%22:%22And%22%7D,%22Properties%22:%7B%22AllProperties%22:false,%22PropertyNames%22:[%22LogicalName%22]%7D%7D,%22Criteria%22:%7B%22Conditions%22:[%7B%22ConditionOperator%22:%22Equals%22,%22PropertyName%22:%22LogicalName%22,%22Value%22:%7B%22Type%22:%22System.String%22,%22Value%22:%22account%22%7D%7D,%7B%22ConditionOperator%22:%22Equals%22,%22PropertyName%22:%22LogicalName%22,%22Value%22:%7B%22Type%22:%22System.String%22,%22Value%22:%22contact%22%7D%7D],%22FilterOperator%22:%22Or%22%7D,%22LabelQuery%22:%7B%22FilterLanguages%22:[1033],%22MissingLabelBehavior%22:0%7D,%22Properties%22:%7B%22AllProperties%22:false,%22PropertyNames%22:[%22SchemaName%22,%22Attributes%22]%7D%7D HTTP/1.1

OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
```

**Response:**

```http
HTTP/1.1 200 OK
Content-Type: application/json; odata.metadata=minimal
OData-Version: 4.0

{
   "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.RetrieveMetadataChangesResponse",
   "ServerVersionStamp": "74812162!10/09/2022 22:10:22",
   "DeletedMetadata": {
      "Count": 0,
      "IsReadOnly": false,
      "Keys": [],
      "Values": []
   },
   "EntityMetadata": [
        {
            "LogicalName": "account",
            "SchemaName": "Account",
            "MetadataId": "70816501-edb9-4740-a16c-6a5efbc05d84",
            "HasChanged": null,
            "Attributes": [
                {
                    "@odata.type": "#Microsoft.Dynamics.CRM.ComplexStringAttributeMetadata",
                    "LogicalName": "emailaddress3",
                    "MetadataId": "97fb4aae-ea5d-427f-9b2b-9a6b9754286e",
                    "HasChanged": null
                },
                {
                    "@odata.type": "#Microsoft.Dynamics.CRM.ComplexStringAttributeMetadata",
                    "LogicalName": "emailaddress1",
                    "MetadataId": "b254ab69-de5a-4edb-8059-bdeb6863c544",
                    "HasChanged": null
                },
                {
                    "@odata.type": "#Microsoft.Dynamics.CRM.ComplexStringAttributeMetadata",
                    "LogicalName": "address1_city",
                    "MetadataId": "ca8d0a94-8569-4154-b511-718e11635449",
                    "HasChanged": null
                },
            <Remaining attributes truncated for brevity>
            ]
        },
        {
            "LogicalName": "contact",
            "SchemaName": "Contact",
            "MetadataId": "608861bc-50a4-4c5f-a02c-21fe1943e2cf",
            "HasChanged": null,
            "Attributes": [
                {
                  "LogicalName": "contactid",
                  "MetadataId": "2ae700b3-97d2-4d99-96f2-8e4aa6368fc2",
                  "HasChanged": null,
                },
                {
                  "@odata.type": "#Microsoft.Dynamics.CRM.ComplexStringAttributeMetadata",
                  "LogicalName": "emailaddress3",
                  "MetadataId": "2a7f7ad8-9d2a-4e1e-8769-88d7b3affabb",
                  "HasChanged": null,
                },
                {
                  "@odata.type": "#Microsoft.Dynamics.CRM.ComplexStringAttributeMetadata",
                  "LogicalName": "emailaddress2",
                  "MetadataId": "edd802ac-72ae-4e29-b2de-9dfe57c898f1",
                  "HasChanged": null,
                },
            <Remaining attributes truncated for brevity>
            ]
        }
    ]
}

```

> [!NOTE]
> The response example has been edited to remove properties with null values. All properties are returned with the `EntityMetadata`. Properties other than the `MetadataId` that are not requested will have null values. These were removed from the example response for brevity. The actual response payload is much larger.


---

## Create a query using EntityQueryExpression

Use `EntityQueryExpression` to set the `RetrieveMetadataChanges` `Query` property.

#### [SDK for .NET](#tab/sdk)

[EntityQueryExpression](xref:Microsoft.Xrm.Sdk.Metadata.Query.EntityQueryExpression) has the following properties:

|Property|Type|Description|
|---------|---------|---------|
|`Properties`|[MetadataPropertiesExpression](xref:Microsoft.Xrm.Sdk.Metadata.Query.MetadataPropertiesExpression)|Set the `PropertyNames` to a list of property names to return. Or you can set `AllProperties` to true to return all the properties. For items that have them, you don't need to add the `MetadataId`, `LogicalName`, or `HasChanged` property names. These properties are always be included.|
|`Criteria`|[MetadataFilterExpression](xref:Microsoft.Xrm.Sdk.Metadata.Query.MetadataPropertiesExpression)|See [Limit data returned using MetadataFilterExpression](#limit-data-returned-using-metadatafilterexpression)|
|`AttributeQuery`|[AttributeQueryExpression](xref:Microsoft.Xrm.Sdk.Metadata.Query.AttributeQueryExpression)|Follows the same pattern as `EntityQueryExpression`. `AttributeQueryExpression` also has `Properties` and `Criteria` to control which column definitions to return.<br /><br />**Note**: When you use `AttributeQuery`, `Attributes` must be one of the `Properties` requested for the `EntityQueryExpression`.|
|`RelationshipQuery`|[RelationshipQueryExpression](xref:Microsoft.Xrm.Sdk.Metadata.Query.RelationshipQueryExpression)|Follows the same pattern as `EntityQueryExpression`. `RelationshipQueryExpression` also has `Properties` and `Criteria` to control which relationship definitions to return.<br/><br />**Note**: When you use `RelationshipQuery`, `OneToManyRelationships`, `ManyToOneRelationships`, or `ManyToManyRelationships` they must be one of the `Properties` requested for the `EntityQueryExpression`.|
|`KeyQuery`|[EntityKeyQueryExpression](xref:Microsoft.Xrm.Sdk.Metadata.Query.EntityKeyQueryExpression)|Follows the same pattern as `EntityQueryExpression`. `EntityKeyQueryExpression` also has `Properties` and `Criteria` to control which alternate key definitions to return.<br /><br />**Note**: When you use `KeyQuery`, `Keys` must be one of the `Properties` requested for the `EntityQueryExpression`.|
|`LabelQuery`|[LabelQueryExpression](xref:Microsoft.Xrm.Sdk.Metadata.Query.LabelQueryExpression)|Use the`FilterLanguages` property to limit the languages that are returned. If an organization has many languages provisioned, you receive labels for all languages that could add considerably to the data returned. If your app is for an individual user, you should include the user's preferred [LCID language code](/openspecs/office_standards/ms-oe376/6c085406-a698-4e12-9d4d-c3b0ee3dbc4a). See [Retrieve the user's preferred language code](#retrieve-the-users-preferred-language-code)|


#### [Web API](#tab/webapi)

[EntityQueryExpression](xref:Microsoft.Dynamics.CRM.EntityQueryExpression) has the following properties:

|Property|Type|Description|
|---------|---------|---------|
|`Properties`|[MetadataPropertiesExpression](xref:Microsoft.Dynamics.CRM.MetadataPropertiesExpression)|Set the `PropertyNames` to a list of property names to return. Or you can set `AllProperties` to true to return all the properties. For items that have them, you don't need to add the `MetadataId`, `LogicalName`, or `HasChanged` property names. These properties are always included.|
|`Criteria`|[MetadataFilterExpression](xref:Microsoft.Dynamics.CRM.MetadataFilterExpression)|See [Limit data returned using MetadataFilterExpression](#limit-data-returned-using-metadatafilterexpression)|
|`AttributeQuery`|[AttributeQueryExpression](xref:Microsoft.Dynamics.CRM.AttributeQueryExpression)|Follows the same pattern as `EntityQueryExpression`. `AttributeQueryExpression` also has `Properties` and `Criteria` to control which column definitions to return.<br /><br />**Note**: When you use `AttributeQuery`, `Attributes` must be one of the `Properties` requested for the `EntityQueryExpression`.|
|`RelationshipQuery`|[RelationshipQueryExpression](xref:Microsoft.Dynamics.CRM.RelationshipQueryExpression)|Follows the same pattern as `EntityQueryExpression`. `RelationshipQueryExpression` also has `Properties` and `Criteria` to control which relationship definitions to return.<br/><br />**Note**: When you use `RelationshipQuery`, `OneToManyRelationships`, `ManyToOneRelationships`, or `ManyToManyRelationships`, they must be one of the `Properties` requested for the `EntityQueryExpression`.|
|`KeyQuery`|[EntityKeyQueryExpression](xref:Microsoft.Dynamics.CRM.EntityKeyQueryExpression)|Follows the same pattern as `EntityQueryExpression`. `EntityKeyQueryExpression` also has `Properties` and `Criteria` to control which alternate key definitions to return.<br /><br />**Note**: When you use `KeyQuery`, `Keys` must be one of the `Properties` requested for the `EntityQueryExpression`.|
|`LabelQuery`|[LabelQueryExpression](xref:Microsoft.Dynamics.CRM.LabelQueryExpression)|Use the`FilterLanguages` property to limit the languages that are returned. If an organization has many languages provisioned, you receive labels for all languages that could add considerably to the data returned. If your app is for an individual user, you should include the user's preferred [LCID language code](/openspecs/office_standards/ms-oe376/6c085406-a698-4e12-9d4d-c3b0ee3dbc4a). See [Retrieve the user's preferred language code](#retrieve-the-users-preferred-language-code)|

---

> [!NOTE]
> The `Query` parameter is optional, so you can use `RetrieveMetadataChanges` without any filters, but this is equivalent to using `RetrieveAllEntities`, a very expensive operation.

## Limit data returned using MetadataFilterExpression

#### [SDK for .NET](#tab/sdk)

Use [MetadataFilterExpression](xref:Microsoft.Xrm.Sdk.Metadata.Query.MetadataFilterExpression) for the `Criteria` property for [EntityQueryExpression](xref:Microsoft.Xrm.Sdk.Metadata.Query.EntityQueryExpression), [AttributeQueryExpression](xref:Microsoft.Xrm.Sdk.Metadata.Query.AttributeQueryExpression), [RelationshipQueryExpression](xref:Microsoft.Xrm.Sdk.Metadata.Query.RelationshipQueryExpression), and [EntityKeyQueryExpression](xref:Microsoft.Xrm.Sdk.Metadata.Query.EntityKeyQueryExpression).

`MetadataFilterExpression` has the following properties:

|Property|Type|Description|
|---------|---------|---------|
|`FilterOperator`|[LogicalOperator](xref:Microsoft.Xrm.Sdk.Query.LogicalOperator)|Controls how the `Conditions` are evaluated, either `And` or `Or`. |
|`Conditions`|[DataCollection](xref:Microsoft.Xrm.Sdk.DataCollection`1)\<[MetadataConditionExpression](xref:Microsoft.Dynamics.CRM.MetadataConditionExpression)\>|A collection of conditions to evaluate. See [Set conditions using MetadataConditionExpression](#set-conditions-using-metadataconditionexpression) |
|`Filters`|[DataCollection](xref:Microsoft.Xrm.Sdk.DataCollection`1)\<[MetadataFilterExpression](xref:Microsoft.Xrm.Sdk.Metadata.Query.MetadataFilterExpression)\>|More filters to apply for a more complex query.|

#### [Web API](#tab/webapi)

Use [MetadataFilterExpression](xref:Microsoft.Dynamics.CRM.MetadataFilterExpression) for the `Criteria` property for [EntityQueryExpression](xref:Microsoft.Dynamics.CRM.EntityQueryExpression), [AttributeQueryExpression](xref:Microsoft.Dynamics.CRM.AttributeQueryExpression), [RelationshipQueryExpression](xref:Microsoft.Dynamics.CRM.RelationshipQueryExpression), and [EntityKeyQueryExpression](xref:Microsoft.Dynamics.CRM.EntityKeyQueryExpression).

`MetadataFilterExpression` has the following properties:

|Property|Type|Description|
|---------|---------|---------|
|`FilterOperator`|[LogicalOperator](xref:Microsoft.Dynamics.CRM.LogicalOperator)|Controls how the `Conditions` are evaluated, either `And` or `Or`. |
|`Conditions`|Collection([MetadataConditionExpression](xref:Microsoft.Dynamics.CRM.MetadataConditionExpression))|A collection of conditions to evaluate. See [Set conditions using MetadataConditionExpression](#set-conditions-using-metadataconditionexpression) |
|`Filters`|Collection([MetadataFilterExpression](xref:Microsoft.Dynamics.CRM.MetadataFilterExpression))|More filters to apply for a more complex query.|

---

## Set conditions using MetadataConditionExpression

#### [SDK for .NET](#tab/sdk)

Use [MetadataConditionExpression](xref:Microsoft.Xrm.Sdk.Metadata.Query.MetadataConditionExpression) for the [MetadataFilterExpression](xref:Microsoft.Xrm.Sdk.Metadata.Query.MetadataFilterExpression) `Conditions` property.

`MetadataConditionExpression` has the following properties:

|Property|Type|Description|
|---------|---------|---------|
|`ConditionOperator`|[MetadataConditionOperator](xref:Microsoft.Xrm.Sdk.Metadata.Query.MetadataConditionOperator)| Describes the type of comparison to apply to the `Value` property.|
|`PropertyName`|string|The name of the property to evaluate|
|`Value`|object|The value (or values) to compare.|

Generally, you can only use properties that represent simple data types, enumerations, [BooleanManagedProperty](xref:Microsoft.Xrm.Sdk.BooleanManagedProperty), or [AttributeRequiredLevelManagedProperty](xref:Microsoft.Xrm.Sdk.Metadata.AttributeRequiredLevelManagedProperty) in a `MetadataFilterExpression`. You can't set conditions on any properties that are collections or labels. When a `BooleanManagedProperty` or `AttributeRequiredLevelManagedProperty` is specified, only the `Value` property is evaluated. Filtering on [AttributeMetadata.SourceType property](xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.SourceType) isn't supported.

#### [Web API](#tab/webapi)

Use [MetadataConditionExpression](xref:Microsoft.Dynamics.CRM.MetadataConditionExpression) for the [MetadataFilterExpression](xref:Microsoft.Dynamics.CRM.MetadataFilterExpression) `Conditions` property.

`MetadataConditionExpression` has the following properties:

|Property|Type|Description|
|---------|---------|---------|
|`ConditionOperator`|[MetadataConditionOperator](xref:Microsoft.Dynamics.CRM.MetadataConditionOperator)| Describes the type of comparison to apply to the `Value` property.|
|`PropertyName`|string|The name of the property to evaluate|
|`Value`|[Object ComplexType](xref:Microsoft.Dynamics.CRM.Object)|The value (or values) to compare. |


Generally, you can only use properties that represent simple data types, enumerations, [BooleanManagedProperty](xref:Microsoft.Dynamics.CRM.BooleanManagedProperty), or [AttributeRequiredLevelManagedProperty](xref:Microsoft.Dynamics.CRM.AttributeRequiredLevelManagedProperty) in a `MetadataFilterExpression`. You can't set conditions on any properties that are collections or labels. When a `BooleanManagedProperty` or `AttributeRequiredLevelManagedProperty` is specified, only the `Value` property is evaluated. Filtering on [AttributeMetadata](xref:Microsoft.Dynamics.CRM.AttributeMetadata).SourceType property isn't supported.

The [Object ComplexType](xref:Microsoft.Dynamics.CRM.Object) has two string properties: `Type` and `Value`. To set the `Type`, you must match the .NET type for the values that you're comparing. The following table shows the `Type` values to use.


|Type|Type value  |
|---------|---------|
|[AttributeRequiredLevel](xref:Microsoft.Dynamics.CRM.AttributeRequiredLevel)|`"Microsoft.Xrm.Sdk.Metadata.AttributeRequiredLevel"`|
|[AttributeTypeCode](xref:Microsoft.Dynamics.CRM.AttributeTypeCode)|`"Microsoft.Xrm.Sdk.Metadata.AttributeTypeCode"`|
|[AttributeTypeDisplayName](xref:Microsoft.Dynamics.CRM.AttributeTypeDisplayName)|`"Microsoft.Xrm.Sdk.Metadata.AttributeTypeDisplayName"`|
|[DateTimeOffset](xref:System.DateTimeOffset)|`"System.DateTime"`|
|[Guid](xref:System.Guid)|`"System.Guid"`|
|[OwnershipTypes](xref:Microsoft.Dynamics.CRM.OwnershipTypes)|`"Microsoft.Xrm.Sdk.Metadata.OwnershipTypes"`|
|[RelationshipType](xref:Microsoft.Dynamics.CRM.RelationshipType)|`"Microsoft.Xrm.Sdk.Metadata.RelationshipType"`|
|`Collection(string)`|`"System.String[]"`|
|`bool`<br />[BooleanManagedProperty](xref:Microsoft.Dynamics.CRM.BooleanManagedProperty)|`"System.Boolean"`|
|`int`|`"System.Int32"`|
|`string`|`"System.String"`|


---

### MetadataConditionOperator Enum values

The `MetadataConditionOperator` Enum has the following members:

|Field|Description|
|---------|---------|
|`Equals`|The values are compared for equality.|
|`NotEquals`|The two values aren't equal.|
|`In`|The value exists in a list of values.|
|`NotIn`|The given value isn't matched to a value in a list.|
|`GreaterThan`| The value is greater than the compared value.|
|`LessThan`|The value is less than the compared value.|


## Process data returned

#### [SDK for .NET](#tab/sdk)

The [RetrieveMetadataChangesResponse](xref:Microsoft.Xrm.Sdk.Messages.RetrieveMetadataChangesResponse) has the following properties:

|Property|Type|Description|
|---------|---------|---------|
|`EntityMetadata`|[EntityMetadataCollection](xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadataCollection)|The table definitions requested. When you're querying data, or when initializing a cache, this value can be treated the same as the response from the `RetrieveAllEntities` message. If you want to access a specific column, relationship, or alternate key definition, you must return the table definition that contains them.|
|`ServerVersionStamp`|`string`|A timestamp identifier for the metadata retrieved. When you manage a cache of schema definitions, use this value as the `ClientVersionStamp` property in subsequent requests so that only the changes since the previous request is returned.|
|`DeletedMetadata`|[DeletedMetadataCollection](xref:Microsoft.Xrm.Sdk.Metadata.Query.DeletedMetadataCollection)|Data for the items deleted since the previous request. This value only contains data when `RetrieveMetadataChanges` is sent with the `ClientVersionStamp` and `DeletedMetadataFilters` parameters. For more information, see [Cache Schema data](cache-schema-data.md)|


#### [Web API](#tab/webapi)

The [RetrieveMetadataChangesResponse](xref:Microsoft.Dynamics.CRM.RetrieveMetadataChangesResponse) has the following properties:

|Property|Type|Description|
|---------|---------|---------|
|`EntityMetadata`|Collection(<xref:Microsoft.Dynamics.CRM.ComplexEntityMetadata>)|The table definitions requested. When you're querying data, or when initializing a cache, this value can be treated the same as the response from the `RetrieveAllEntities` message. If you want to access a specific column, relationship, or alternate key definition, you must return the table definition that contains them.|
|`ServerVersionStamp`|`string`|A timestamp identifier for the metadata retrieved. When you manage a cache of schema definitions, use this value as the `ClientVersionStamp` property in subsequent requests so that only the changes since the previous request is returned.|
|`DeletedMetadata`|[DeletedMetadataCollection](xref:Microsoft.Dynamics.CRM.DeletedMetadataCollection)|Data for the items deleted since the previous request. This value only contains data when `RetrieveMetadataChanges` is sent with the `ClientVersionStamp` and `DeletedMetadataFilters` parameters. For more information, see [Cache Schema data](cache-schema-data.md)|

The `EntityMetadata` property returns a collection of [ComplexEntityMetadata complex type](xref:Microsoft.Dynamics.CRM.ComplexEntityMetadata). This type is different than the [EntityMetadata entity type](xref:Microsoft.Dynamics.CRM.EntityMetadata) used with the `EntityDefinitions` entity set used to create and update entity tables.

All the types returned with `RetrieveMetadataChangesResponse.EntityMetadata`, [RetrieveAllEntitiesResponse.EntityMetadata](xref:Microsoft.Dynamics.CRM.RetrieveAllEntitiesResponse), and [RetrieveEntityResponse.EntityMetadata](xref:Microsoft.Dynamics.CRM.RetrieveEntityResponse) return these complex types that have corresponding entity types used when creating or updated schema definitions.

---


## Retrieve the user's preferred language code

The following examples show how you can retrieve the user's preferred [LCID language code](/openspecs/office_standards/ms-oe376/6c085406-a698-4e12-9d4d-c3b0ee3dbc4a).

#### [SDK for .NET](#tab/sdk)

You can retrieve the user's preferred language from the [UserSettings.UILanguageId](reference/entities/usersettings.md#BKMK_UILanguageId) column.

```csharp
static int? RetrieveUserUILanguageCode(IOrganizationService service)
{
   // To get the current user's systemuserid
   var whoIAm = (WhoAmIResponse)service.Execute(new WhoAmIRequest());

   var query = new QueryExpression("usersettings")
   {
         ColumnSet = new ColumnSet("uilanguageid", "systemuserid"),
         Criteria = new FilterExpression
         {
            Conditions = {
                  {
                     new ConditionExpression(
                        attributeName:"systemuserid",
                        conditionOperator:ConditionOperator.Equal,
                        value: whoIAm.UserId)
                  }
            }
         },
         TopCount = 1
   };

   EntityCollection userSettings = service.RetrieveMultiple(query: query);
   if (userSettings.Entities.Count > 0)
   {
         return (int)userSettings.Entities[0]["uilanguageid"];
   }
   return null;
}
```

#### [Web API](#tab/webapi)

First get the `UserId` using the [WhoAmI function](xref:Microsoft.Dynamics.CRM.WhoAmI)

**Request:**

```http
GET [Organization URI]/api/data/v9.2/WhoAmI HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
```

**Response:**

```http
HTTP/1.1 200 OK
Content-Type: application/json; odata.metadata=minimal
OData-Version: 4.0

{
  "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.WhoAmIResponse",
  "BusinessUnitId": "38e0dbe4-131b-e111-ba3e-78e7d1620f5e",
  "UserId": "4026be43-6b69-e111-8f65-78e7d1620f5e",
  "OrganizationId": "883278f5-03af-45eb-a0bc-3fea67caa544"
}
```

Then use the `UserId` value to filter the records using the `systemuserid` from the [usersettings entity type](xref:Microsoft.Dynamics.CRM.usersettings) to return the `uilanguageid` value.

**Request:**

```http
GET [Organization URI]/api/data/v9.2/usersettingscollection?$select=uilanguageid&$filter=systemuserid eq 4026be43-6b69-e111-8f65-78e7d1620f5e&$top=1&$count=true HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null

```

**Response:**

```http
HTTP/1.1 200 OK
Content-Type: application/json; odata.metadata=minimal
OData-Version: 4.0

{
  "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#usersettingscollection(uilanguageid)",
  "@odata.count": 1,
  "value": [
    {
      "@odata.etag": "W/\"47652882\"",
      "uilanguageid": 1033,
      "systemuserid": "4026be43-6b69-e111-8f65-78e7d1620f5e"
    }
  ]
}
```

---

### See also

[Cache Schema data](cache-schema-data.md)   
[Web API Query schema definitions and detect changes Sample (C#)](webapi/samples/retrievemetadatachanges.md)   
[SDK for .NET Query schema definitions and detect changes Sample (C#)](org-service/samples/query-metadata-changes.md)   
[Organization Service: Table definitions in Microsoft Dataverse](entity-metadata.md)   
[Query table definitions using the Web API](webapi/query-metadata-web-api.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
