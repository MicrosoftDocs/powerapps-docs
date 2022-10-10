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
|`RetrieveAllEntities`|Retrieves data for all tables, including all columns, privileges, and relationships if you wish.<br />While you can use the `EntityFilters` parameter to exclude some parts, it is a very expensive operation.<br />See: <xref:Microsoft.Xrm.Sdk.Messages.RetrieveAllEntitiesRequest?text=RetrieveAllEntitiesRequest> and <xref:Microsoft.Xrm.Sdk.Messages.RetrieveAllEntitiesResponse?text=RetrieveAllEntitiesResponse> classes.|
|`RetrieveEntity`|You can retrieve definition of any single table including all columns, privileges, and relationships if you wish. While you can use the `EntityFilters` parameter to exclude some data, you can’t select which specific properties you want.<br />See: [Retrieve and update a table](org-service/metadata-retrieve-update-delete-entities.md#retrieve-and-update-a-table)|
|`RetrieveAttribute`|You can retrieve the complete definition of any single attribute, but you can’t select which specific properties you want.<br />See: [Retrieve a column](org-service/metadata-attributemetadata.md#retrieve-a-column)|
|`RetrieveRelationship`|You can retrieve the complete definition of any single relationship, but you can’t select which specific properties you want.<br />See: [Retrieve table row relationships](org-service/metadata-relationshipmetadata.md#retrieve-table-row-relationships)|
|`RetrieveAllOptionSets`|You can retrieve information about all the global choices defined in the organization, but this doesn’t include choices that are only defined locally within a column.<br />See: [Insert, update, delete, and order global choices](org-service/metadata-global-option-set-options.md)|
|`RetrieveEntityKey`|You can retrieve the definition for any alternate keys for a specific table. <br />See:[Retrieve and delete alternate keys](define-alternate-keys-entity.md#retrieve-and-delete-alternate-keys)|


#### [Web API](#tab/webapi)

|Method|Description|
|---------|---------|
|<xref:Microsoft.Dynamics.CRM.RetrieveAllEntities?text=RetrieveAllEntities Function>|Retrieves data for all tables, including all columns, privileges, and relationships if you wish.<br />While you can use the `EntityFilters` parameter to exclude some parts, it is a very expensive operation.|
|<xref:Microsoft.Dynamics.CRM.RetrieveEntity?text=RetrieveEntity Function>|You can retrieve definition of any single table including all columns, privileges, and relationships if you wish.<br />While you can use the `EntityFilters` parameter to exclude some data, you can’t select which specific properties you want, it is still an expensive operation.|
|`EntityDefinitions` EntitySet|Enables a query for multiple table definitions using OData syntax to filter and select the properties you want to return. <br />Expand the `Attributes`,`Keys`,`ManyToManyRelationships`,`ManyToOneRelationships`, and `OneToManyRelationships` collection-valued navigation properties to get information about relationships, alternate keys and columns.<br/>Cannot return properties specific to column entity types that are derived from <xref:Microsoft.Dynamics.CRM.AttributeMetadata?text=AttributeMetadata EntityType> without casting. Each query that expands `Attributes` can only cast to a single derived column type, so multiple requests may be required. For example, you can't get the `OptionSet` definitions for both a <xref:Microsoft.Dynamics.CRM.BooleanAttributeMetadata> column and a <xref:Microsoft.Dynamics.CRM.PicklistAttributeMetadata> column in the same request.<br/>If you don't need to manage a cache, and you don't need details about derived column entity types in a single request or you don't mind sending multiple requests, this may be all you need. <br/>See [Query table definitions using the Web API](webapi/query-metadata-web-api.md)|
|`RelationshipDefinitions` EntitySet|Enables a query for multiple relationship definitions using OData syntax to filter and select the properties you want to return. <br />Contains data for both <xref:Microsoft.Dynamics.CRM.OneToManyRelationshipMetadata> and <xref:Microsoft.Dynamics.CRM.ManyToManyRelationshipMetadata> EntityTypes. You must cast your query to either of those types to select or filter based on properties they possess, otherwise you are limited to the shared properties from the base <xref:Microsoft.Dynamics.CRM.RelationshipMetadataBase?text=RelationshipMetadataBase EntityType> that those entity types are derived from. If you need to select or filter on specific properties from either derived types, you will need to send two separate requests. More information: [Use the Web API with table definitions](webapi/use-web-api-metadata.md) |
|`GlobalOptionSetDefinitions` EntitySet|Enables a query for multiple *global* choice definitions using OData syntax to filter and select the properties you want to return.<br /> Doesn’t include choices that are only defined locally within a column.<br />Contains data for both <xref:Microsoft.Dynamics.CRM.BooleanOptionSetMetadata> and <xref:Microsoft.Dynamics.CRM.OptionSetMetadata> entity types. You must cast your query to either of those types to select or filter based on properties they possess, otherwise you are limited to the shared properties from the base <xref:Microsoft.Dynamics.CRM.OptionSetMetadataBase?text=OptionSetMetadataBase EntityType> that those entity types are derived from. For example, `OptionSetMetadataBase` doesn't include the `Options` property. If you need to select or filter on specific properties from either derived types, you will need to send two separate requests. More information: [Use the Web API with table definitions](webapi/use-web-api-metadata.md)|

---


## Basic RetrieveMetadataChanges example

For a simple example of what you can do with `RetrieveMetadataChanges`, compare what you can do with Web API and the `EntityDefinitions` entity set.

Using Web API you can compose a query like this:

```http
GET [Organization URI]/api/data/v9.2/EntityDefinitions?$select=SchemaName&$filter=LogicalName eq 'account' or LogicalName eq 'contact'&$expand=Attributes($select=LogicalName;$filter=IsValidForCreate eq true)
```

This will return data from both the account and contact definitions, and expand all the column definitions where `IsValidForCreate` is true.

You can compose the same query using `RetrieveMetadataChanges` using the examples below:

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

The <xref:Microsoft.Dynamics.CRM.RetrieveMetadataChanges?text=RetrieveMetadataChanges Function> `Query` parameter requires a URL encoded string representing the JSON value of the query, which is an <xref:Microsoft.Dynamics.CRM.EntityQueryExpression?text=EntityQueryExpression ComplexType>.

This is the query as JSON:

```json
{
   "Properties": {
      "AllProperties": false,
      "PropertyNames": [
         "SchemaName",
         "Attributes"
      ]
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
         "PropertyNames": [
            "LogicalName"
         ]
      },
      "Criteria": {
         "Conditions": [
            {
               "ConditionOperator": "Equals",
               "PropertyName": "IsValidForCreate",
               "Value": {
                  "Type": "System.Boolean",
                  "Value": "True"
               }
            }
         ],
         "FilterOperator": "And"
      }
   },
   "LabelQuery": {
      "FilterLanguages": [
         1033
      ],
      "MissingLabelBehavior": 0
   }
}
```

**Request**

```http
GET [Organization URI]/api/data/v9.2/RetrieveMetadataChanges(Query=@p1)?@p1=%7B%22AttributeQuery%22:%7B%22Criteria%22:%7B%22Conditions%22:[%7B%22ConditionOperator%22:%22Equals%22,%22PropertyName%22:%22IsValidForCreate%22,%22Value%22:%7B%22Type%22:%22System.Boolean%22,%22Value%22:%22True%22%7D%7D],%22FilterOperator%22:%22And%22%7D,%22Properties%22:%7B%22AllProperties%22:false,%22PropertyNames%22:[%22LogicalName%22]%7D%7D,%22Criteria%22:%7B%22Conditions%22:[%7B%22ConditionOperator%22:%22Equals%22,%22PropertyName%22:%22LogicalName%22,%22Value%22:%7B%22Type%22:%22System.String%22,%22Value%22:%22account%22%7D%7D,%7B%22ConditionOperator%22:%22Equals%22,%22PropertyName%22:%22LogicalName%22,%22Value%22:%7B%22Type%22:%22System.String%22,%22Value%22:%22contact%22%7D%7D],%22FilterOperator%22:%22Or%22%7D,%22LabelQuery%22:%7B%22FilterLanguages%22:[1033],%22MissingLabelBehavior%22:0%7D,%22Properties%22:%7B%22AllProperties%22:false,%22PropertyNames%22:[%22SchemaName%22,%22Attributes%22]%7D%7D HTTP/1.1

OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
```

**Response**

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
> The response above has been edited to remove properties with null values. All properties are returned with the EntityMetadata. Properties other than the `MetadataId` that are not requested will have null values. These were removed from the example response above for brevity.


---

## Create a query using EntityQueryExpression

## Limit data returned using MetadataFilterExpression

## Process data returned

### See also

[Cache Schema data](cache-schema-data.md)<br />
[Organization Service: Table definitions in Microsoft Dataverse](entity-metadata.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]