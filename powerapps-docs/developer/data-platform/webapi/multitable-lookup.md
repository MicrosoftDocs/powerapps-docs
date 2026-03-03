---
title: "Use multi-table lookup columns"
description: "Learn how to use a single lookup type column to refer to data in multiple other tables. This type of column is sometimes called a polymorphic lookup."
ms.date: 03/02/2026
ms.reviewer: jdaly
ms.topic: how-to
author: MsSQLGirl
ms.author: jukoesma
search.audienceType: 
  - developer
contributors:
 - JimDaly
---

# Multi-table lookups

Multi-table lookup type columns, sometimes called *polymorphic lookups*, allow a user to use a specific table that has
multiple one-to-many (1:N) relationships to other tables in the environment. A single lookup
type column can refer to multiple other tables. A lookup value submitted to the
multi-table type column is matched to a record in any of the related
tables. Multi-table lookups can be created with both local tables and virtual tables as referenced tables.

Multi-table types are currently built into Microsoft Dataverse as static types like
Customer, which connects to [Account](../reference/entities/account.md) and [Contact](../reference/entities/contact.md) tables. Multi-table lookups gives users the power to define any other multi-table lookups they might need.

> [!NOTE]
> At this time users can create and modify custom multi-table lookups via the SDK or Web APIs.
> Interactive user interface support will be coming in a future release.

## Retrieving data about related tables

There are two ways to retrieve information related tables with a lookup column, including multi-table lookups: expand the single-valued navigation property, or retrieve the lookup property.

### Expand the single-valued navigation property

When you create a multi-table lookup, each table requires a separate one-to-many relationship. Each relationship adds a distinct single-valued navigation property.

> [!IMPORTANT]
> The name of this single-valued navigation property is stored in the [OneToManyRelationshipMetadata.ReferencingEntityNavigationPropertyName](xref:Microsoft.Xrm.Sdk.Metadata.OneToManyRelationshipMetadata.ReferencingEntityNavigationPropertyName) property.  You can also discover this name by downloading and reviewing the CSDL $metadata document. [Learn how to identify these single-value navigation properties in the $metadata service document](web-api-navigation-properties.md#multi-table-lookups).

When you query the table, use the `$expand` query option to include the related table. [Learn more about joining related tables using OData `$expand` query option](query/join-tables.md).


### Retrieve the lookup property

Each lookup column has a corresponding [lookup property](web-api-navigation-properties.md#lookup-properties) that you can retrieve with the `$select` query option. These properties follow the naming convention `_<name>_value` where `<name>` is the logical name of the lookup column. The value of the lookup property is the unique identifier for the related record, if any.

For a multi-table lookup, the unique ID isn't valuable unless you know which table it applies to. When you retrieve data from any lookup column, you can apply certain OData annotation preferences. These are especially useful with a multi-table lookup because they provide more data from the related record and information about which table the data comes from.

|Annotation  |Description  |
|---------|---------|
|`OData.Community.Display.V1.FormattedValue`|Returns the primary name column value for the related record.|
|`Microsoft.Dynamics.CRM.associatednavigationproperty`|Returns the name of the single-valued navigation property that supports this relationship.|
|`Microsoft.Dynamics.CRM.lookuplogicalname`|Returns the logical name of the related table|

[Learn more about retrieving lookup property data](query/select-columns.md#lookup-property-data)



## Examples

Let's say you're hosting media for users in a library. You have many different
media objects. Many of them have the same name but are in different formats like
Books, Audio, and Video. Creating a multi-table lookup with the schema name `sample_MediaPolymorphicLookup`
that has 1:N relationships to `sample_Book`, `sample_Audio`, and `sample_Video` 
support a `sample_Media` table that provides quick identifications of
records stored in specific tables.

### `sample_Book` table

`sample_Book` is the first of the three related tables. This simple query retrieves the two records found here.

```http
GET [Organization URI]/api/data/v9.2/sample_books?$select=sample_name,sample_callnumber
Content-Type: application/json; charset=utf-8
OData-MaxVersion: 4.0
OData-Version: 4.0
Accept: application/json
```
This is the JSON body of the response:

```json
{
   "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#sample_books(sample_name,sample_callnumber)",
   "value": [
      {
         "@odata.etag": "W/\"171704230\"",
         "sample_callnumber": "ww-3452 ",
         "sample_bookid": "00000000-0000-0000-0000-000000000001",
         "sample_name": "Content1"
      },
      {
         "@odata.etag": "W/\"171704235\"",
         "sample_callnumber": "a4e-87hw",
         "sample_bookid": "00000000-0000-0000-0000-000000000005",
         "sample_name": "Content2"
      }
   ]
}
```

### `sample_Audio` table

`sample_Audio` is the second of the three related tables. This simple query retrieves the two records found here.

```http
GET [Organization URI]/api/data/v9.2/sample_audios?$select=sample_name,sample_audioformat
Content-Type: application/json; charset=utf-8
OData-MaxVersion: 4.0
OData-Version: 4.0
Accept: application/json
```

This is the JSON body of the response:

```json
{
   "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#sample_audios(sample_name,sample_audioformat)",
   "value": [
      {
         "@odata.etag": "W/\"171704242\"",
         "sample_audioid": "00000000-0000-0000-0000-000000000002",
         "sample_audioformat": "mp4",
         "sample_name": "Content1"
      },
      {
         "@odata.etag": "W/\"171704246\"",
         "sample_audioid": "00000000-0000-0000-0000-000000000004",
         "sample_audioformat": "wma",
         "sample_name": "Content3"
      }
   ]
}
```

### `sample_Video` table

`sample_Video` is the third of the three related tables. This simple query retrieves the two records found here.

```http
GET [Organization URI]/api/data/v9.2/sample_videos?$select=sample_name,sample_videoformat
Content-Type: application/json; charset=utf-8
OData-MaxVersion: 4.0
OData-Version: 4.0
Accept: application/json
```

This is the JSON body of the response:

```json
{
   "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#sample_videos(sample_name,sample_videoformat)",
   "value": [
      {
         "@odata.etag": "W/\"171704254\"",
         "sample_name": "Content2",
         "sample_videoformat": "avi",
         "sample_videoid": "00000000-0000-0000-0000-000000000006"
      },
      {
         "@odata.etag": "W/\"171704250\"",
         "sample_name": "Content3",
         "sample_videoformat": "wmv",
         "sample_videoid": "00000000-0000-0000-0000-000000000003"
      }
   ]
}
```

### `sample_Media` table

This table has the multi-table lookup column with schema name `sample_MediaPolymorphicLookup` and logical name `sample_mediapolymorphiclookup`.

For the purpose of this demonstration, this table contains only four records that are related to supporting records:

|`sample_name`|`sample_mediapolymorphiclookup` value|`sample_mediapolymorphiclookup` type|
|---------|---------|---------|
|Media Object One|00000000-0000-0000-0000-000000000001|`sample_book`|
|Media Object Two|00000000-0000-0000-0000-000000000002|`sample_audio`|
|Media Object Three|00000000-0000-0000-0000-000000000003|`sample_video`|
|Media Object Four|00000000-0000-0000-0000-000000000004|`sample_audio`|

### Retrieving related data

Using the `sample_Media` table, this example query:

- Selects the `_sample_mediapolymorphiclookup_value` lookup property in the `$select` query option for the `sample_mediapolymorphiclookup` lookup column. With the `OData.Community.Display.V1.FormattedValue`, `Microsoft.Dynamics.CRM.associatednavigationproperty`, and `Microsoft.Dynamics.CRM.lookuplogicalname` `odata.include-annotations` preferences applied, these values are returned with each record.
- Expands three single-valued navigation properties, one for each related table. For each expanded navigation property, the primary name column (`sample_name`) is selected as well as the respective custom column value: `sample_callnumber`, `sample_audioformat`, `sample_videoformat`.

These operations demonstrate how the table records are related via the `sample_MediaPolymorphicLookup` lookup column.

**Request**

```http
GET [Organization URI]/api/data/v9.2/sample_medias?$select=sample_name,_sample_mediapolymorphiclookup_value&
$expand=sample_MediaPolymorphicLookup_sample_book($select=sample_name,sample_callnumber),sample_MediaPolymorphicLookup_sample_audio($select=sample_name,sample_audioformat),sample_MediaPolymorphicLookup_sample_video($select=sample_name,sample_videoformat)
Content-Type: application/json; charset=utf-8
OData-MaxVersion: 4.0
OData-Version: 4.0
Accept: application/json
Prefer: odata.include-annotations="OData.Community.Display.V1.FormattedValue,Microsoft.Dynamics.CRM.associatednavigationproperty,Microsoft.Dynamics.CRM.lookuplogicalname"
```

**Response**

With these query options and preference headers set, the body of the response contains the following JSON:

```json
{
   "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#sample_medias(sample_name,_sample_mediapolymorphiclookup_value,sample_MediaPolymorphicLookup_sample_book(sample_name),sample_MediaPolymorphicLookup_sample_audio(sample_name,sample_audioformat),sample_MediaPolymorphicLookup_sample_video(sample_name))",
   "value": [
      {
         "@odata.etag": "W/\"171704264\"",
         "sample_mediaid": "00000000-0000-0000-0000-000000000007",
         "sample_name": "Media Object One",
         "_sample_mediapolymorphiclookup_value@OData.Community.Display.V1.FormattedValue": "Content1",
         "_sample_mediapolymorphiclookup_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "sample_MediaPolymorphicLookup_sample_book",
         "_sample_mediapolymorphiclookup_value@Microsoft.Dynamics.CRM.lookuplogicalname": "sample_book",
         "_sample_mediapolymorphiclookup_value": "00000000-0000-0000-0000-000000000001",
         "sample_MediaPolymorphicLookup_sample_book": {
            "sample_bookid": "00000000-0000-0000-0000-000000000001",
            "sample_name": "Content1"
         },
         "sample_MediaPolymorphicLookup_sample_audio": null,
         "sample_MediaPolymorphicLookup_sample_video": null
      },
      {
         "@odata.etag": "W/\"171704268\"",
         "sample_mediaid": "00000000-0000-0000-0000-000000000008",
         "sample_name": "Media Object Two",
         "_sample_mediapolymorphiclookup_value@OData.Community.Display.V1.FormattedValue": "Content1",
         "_sample_mediapolymorphiclookup_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "sample_MediaPolymorphicLookup_sample_audio",
         "_sample_mediapolymorphiclookup_value@Microsoft.Dynamics.CRM.lookuplogicalname": "sample_audio",
         "_sample_mediapolymorphiclookup_value": "00000000-0000-0000-0000-000000000002",
         "sample_MediaPolymorphicLookup_sample_book": null,
         "sample_MediaPolymorphicLookup_sample_audio": {
            "sample_audioid": "00000000-0000-0000-0000-000000000002",
            "sample_audioformat": "mp4",
            "sample_name": "Content1"
         },
         "sample_MediaPolymorphicLookup_sample_video": null
      },
      {
         "@odata.etag": "W/\"171704273\"",
         "sample_mediaid": "00000000-0000-0000-0000-000000000009",
         "sample_name": "Media Object Three",
         "_sample_mediapolymorphiclookup_value@OData.Community.Display.V1.FormattedValue": "Content3",
         "_sample_mediapolymorphiclookup_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "sample_MediaPolymorphicLookup_sample_video",
         "_sample_mediapolymorphiclookup_value@Microsoft.Dynamics.CRM.lookuplogicalname": "sample_video",
         "_sample_mediapolymorphiclookup_value": "00000000-0000-0000-0000-000000000003",
         "sample_MediaPolymorphicLookup_sample_book": null,
         "sample_MediaPolymorphicLookup_sample_audio": null,
         "sample_MediaPolymorphicLookup_sample_video": {
            "sample_name": "Content3",
            "sample_videoid": "00000000-0000-0000-0000-000000000003"
         }
      },
      {
         "@odata.etag": "W/\"171704279\"",
         "sample_mediaid": "00000000-0000-0000-0000-000000000010",
         "sample_name": "Media Object Four",
         "_sample_mediapolymorphiclookup_value@OData.Community.Display.V1.FormattedValue": "Content3",
         "_sample_mediapolymorphiclookup_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "sample_MediaPolymorphicLookup_sample_audio",
         "_sample_mediapolymorphiclookup_value@Microsoft.Dynamics.CRM.lookuplogicalname": "sample_audio",
         "_sample_mediapolymorphiclookup_value": "00000000-0000-0000-0000-000000000004",
         "sample_MediaPolymorphicLookup_sample_book": null,
         "sample_MediaPolymorphicLookup_sample_audio": {
            "sample_audioid": "00000000-0000-0000-0000-000000000004",
            "sample_audioformat": "wma",
            "sample_name": "Content3"
         },
         "sample_MediaPolymorphicLookup_sample_video": null
      }
   ]
}
```

### Setting a multi-table lookup column

Updating a record to set a polymorphic lookup column is exactly as described in [Associate with a single-valued navigation property](associate-disassociate-entities-using-web-api.md#associate-with-a-single-valued-navigation-property). You need to pay special attention to use the correct single-valued navigation property name. These names are case sensitive.

**Request**

```http
PATCH [Organization Uri]/api/data/v9.2/sample_medias(00000000-0000-0000-0000-000000000007) HTTP/1.1
If-Match: *
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json

{
  "sample_MediaPolymorphicLookup_sample_book@odata.bind": "sample_books(00000000-0000-0000-0000-000000000001)"
}
```


**Response**

```http
HTTP/1.1 204 NoContent
OData-Version: 4.0
OData-EntityId: [Organization Uri]/api/data/v9.2/sample_medias(00000000-0000-0000-0000-000000000007)
```


### Create a multi-table lookup column

> [!NOTE]
> While this example shows how to use the Dataverse Web API, you can also use the SDK for .NET with the <xref:Microsoft.Crm.Sdk.Messages.CreatePolymorphicLookupAttributeRequest> and <xref:Microsoft.Crm.Sdk.Messages.CreatePolymorphicLookupAttributeResponse> classes.

Use the [CreatePolymorphicLookupAttribute action](xref:Microsoft.Dynamics.CRM.CreatePolymorphicLookupAttribute) to create a multi-table lookup. This example creates the column as part of a solution with the unique name `polymorphiclookupexamplesolution` using the [MSCRM.SolutionUniqueName optional parameter](../optional-parameters.md#associate-a-solution-component-with-a-solution).

**Request**

```http
POST [Organization URI]/api/data/v9.2/CreatePolymorphicLookupAttribute HTTP/1.1
Consistency: Strong
Accept: application/json
OData-MaxVersion: 4.0
Authorization: Bearer [REDACTED]
MSCRM.SolutionUniqueName: polymorphiclookupexamplesolution
OData-Version: 4.0

{
  "OneToManyRelationships": [
    {
      "ReferencedEntity": "sample_book",
      "SchemaName": "sample_media_sample_book",
      "ReferencingEntity": "sample_media"
    },
    {
      "ReferencedEntity": "sample_audio",
      "SchemaName": "sample_media_sample_audio",
      "ReferencingEntity": "sample_media",
      "CascadeConfiguration": {
        "Assign": "NoCascade",
        "Share": "NoCascade",
        "Delete": "RemoveLink",
        "Merge": "NoCascade",
        "Reparent": "NoCascade",
        "Unshare": "NoCascade"
      }
    },
    {
      "ReferencedEntity": "sample_video",
      "SchemaName": "sample_media_sample_video",
      "ReferencingEntity": "sample_media",
      "CascadeConfiguration": {
        "Assign": "NoCascade",
        "Share": "NoCascade",
        "Delete": "RemoveLink",
        "Merge": "NoCascade",
        "Reparent": "NoCascade",
        "Unshare": "NoCascade"
      }
    }
  ],
  "Lookup": {
    "AttributeTypeName": {
      "Value": "LookupType"
    },
    "SchemaName": "sample_MediaPolymorphicLookup",
    "Description": {
      "LocalizedLabels": [
        {
          "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
          "Label": "Polymorphic lookup that can reference a Book, Audio, or Video record",
          "LanguageCode": 1033
        }
      ],
      "@odata.type": "Microsoft.Dynamics.CRM.Label"
    },
    "AttributeType": "Lookup",
    "DisplayName": {
      "LocalizedLabels": [
        {
          "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
          "Label": "Media",
          "LanguageCode": 1033
        }
      ],
      "@odata.type": "Microsoft.Dynamics.CRM.Label"
    },
    "@odata.type": "Microsoft.Dynamics.CRM.ComplexLookupAttributeMetadata"
  }
}
```

The following JSON is an example of the [CreatePolymorphicLookupAttributeResponse ComplexType](xref:Microsoft.Dynamics.CRM.CreatePolymorphicLookupAttributeResponse). It contains the ID of the polymorphic attribute and all the relationships created.

```json
{
    "@odata.context":
      "http://<organization URL>/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.CreatePolymorphicLookupAttributeResponse",

    "RelationshipIds":[
        "77d4c6e9-0397-eb11-a81c-000d3a6cfaba",
        "7ed4c6e9-0397-eb11-a81c-000d3a6cfaba",
        "85d4c6e9-0397-eb11-a81c-000d3a6cfaba"
    ],

    "AttributeId":"d378dd3e-42f4-4bd7-95c7-0ee546c7de40"
}
```


### Add relationship to existing polymorphic lookup

Adding a relationship to an existing multi-table lookup column with the Web API is similar to creating any new one-to-many relationship. [Learn how to create a one-to-many relationship using the Web API](create-update-entity-relationships-using-web-api.md#create-a-one-to-many-relationship). The difference is that the [OneToManyRelationshipMetadata](/power-apps/developer/data-platform/webapi/reference/onetomanyrelationshipmetadata)`.Lookup` property must have a `SchemaName` value that matches the polymorphic lookup column.


### Remove a relationship from an existing polymorphic lookup

Removing a relationship to an existing multi-table lookup column with the Web API is the same as deleting any one-to-many relationship. Send a `DELETE` request to the `RelationshipDefinitions` using the value of the [OneToManyRelationshipMetadata](/power-apps/developer/data-platform/webapi/reference/onetomanyrelationshipmetadata)`.MetadataId` property as the key.


### See Also

[Use the Web API with table definitions](use-web-api-metadata.md)  
[Create and update table relationships](create-update-entity-relationships-using-web-api.md)  
[Query table definitions using the Web API](query-metadata-web-api.md)  
[Retrieve table definitions by name or MetadataId](retrieve-metadata-name-metadataid.md)  
[Model tables and columns using the Web API](create-update-entity-definitions-using-web-api.md)  
[Web API table schema operations sample](web-api-metadata-operations-sample.md)  
[Web API table schema operations sample (C#)](samples/webapiservice-metadata-operations.md)
