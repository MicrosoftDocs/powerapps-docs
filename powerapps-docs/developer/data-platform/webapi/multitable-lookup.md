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

By using multi-table lookup type columns, sometimes called *polymorphic lookups*, you can use a specific table that has
multiple one-to-many (1:N) relationships to other tables in the environment. A single lookup
type column can refer to multiple other tables. A lookup value submitted to the
multi-table type column matches a record in any of the related
tables. You can create multi-table lookups with both local tables and virtual tables as referenced tables.

Microsoft Dataverse currently includes multi-table types as static types, such as
Customer, which connects to [Account](../reference/entities/account.md) and [Contact](../reference/entities/contact.md) tables. By using multi-table lookups, you can define any other multi-table lookups you need.

> [!NOTE]
> You can create and modify custom multi-table lookups through the SDK for .NET or Dataverse Web API.
> Interactive user interface support will be available in a future release.
> 
> [Sample: Web API multi-table lookup sample (PowerShell)](samples/multi-table-lookup-powershell.md) contains the sample code that demonstrates the [Example](#example) presented in this article.

## Retrieve data about related tables

To retrieve information about related tables with a lookup column, including multi-table lookups, use one of the following methods: retrieve the lookup property or expand the single-valued navigation property.


### Retrieve the lookup property

Each lookup column has a corresponding [lookup property](web-api-navigation-properties.md#lookup-properties) that you can retrieve by using the `$select` query option. These properties follow the naming convention: `_<name>_value`. `<name>` is the logical name of the lookup column. The value of the lookup property is the unique identifier for the related record, if any.

For a multi-table lookup, the unique ID isn't valuable unless you know which table it applies to. When you retrieve data from any lookup column, you can apply the following OData annotation preferences. These preference options are especially useful with a multi-table lookup because they provide more data from the related record and information about which table the data comes from.

| Annotation | Description |
|---------|---------|
| `OData.Community.Display.V1.FormattedValue` | Returns the primary name column value for the record currently set in this column. |
| `Microsoft.Dynamics.CRM.associatednavigationproperty` | Returns the name of the single-valued navigation property that supports the record currently set in this column. |
| `Microsoft.Dynamics.CRM.lookuplogicalname` | Returns the logical name of the table for the record currently set in this column. |

> [!NOTE]
> Use lookup properties to retrieve the formatted value and supporting metadata needed to expand the single-valued navigation property to get more information.

[Learn more about retrieving lookup property data](query/select-columns.md#lookup-property-data).

### Expand the single-valued navigation property

When you create a multi-table lookup, each table requires a separate one-to-many relationship. Each relationship adds a distinct single-valued navigation property.

The name of this single-valued navigation property is stored in the [OneToManyRelationshipMetadata.ReferencingEntityNavigationPropertyName](xref:Microsoft.Xrm.Sdk.Metadata.OneToManyRelationshipMetadata.ReferencingEntityNavigationPropertyName) property. A common error is when people try to guess the value of this case-sensitive property. There are three ways to definitively determine the correct name of this navigation property:

- Retrieve the relationship metadata. [Learn more about options to retrieve Dataverse schema definitions](../query-schema-definitions.md#evaluate-other-options-to-retrieve-schema-definitions).
- Download and review the CSDL $metadata document. [Learn how to identify these single-value navigation properties in the $metadata service document](web-api-navigation-properties.md#multi-table-lookups).
- [Retrieve the lookup property](#retrieve-the-lookup-property) and include the `Microsoft.Dynamics.CRM.associatednavigationproperty` OData annotation preferences.

When you query the table, use the `$expand` query option with the single-valued navigation property to include the related table. [Learn more about joining related tables using OData `$expand` query option](query/join-tables.md).

## Example

Suppose you're hosting media for users in a library. You have many different
media objects. Many of them have the same name but are in different formats like
books, audio, and video.

In this example, three tables support each specific kind of media:

- `sample_Book` includes `sample_name` and `sample_callnumber` columns.
- `sample_Audio` includes `sample_name` and `sample_audioformat` columns.
- `sample_Video` includes `sample_name` and `sample_videoformat` columns.

The `sample_Media` table has a multi-table lookup with the schema name `sample_MediaPolymorphicLookup`. You can set the lookup column to refer to records in any of the three specific media tables.


### `sample_Book` table

The `sample_Book` table is the first of the three related tables. This simple query retrieves the two records found in this table.

```http
GET [Organization URI]/api/data/v9.2/sample_books?$select=sample_name,sample_callnumber
Content-Type: application/json; charset=utf-8
OData-MaxVersion: 4.0
OData-Version: 4.0
Accept: application/json
```
This example shows the JSON body of the response:

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

The `sample_Audio` table is the second of the three related tables. This simple query retrieves the two records in this table.

```http
GET [Organization URI]/api/data/v9.2/sample_audios?$select=sample_name,sample_audioformat
Content-Type: application/json; charset=utf-8
OData-MaxVersion: 4.0
OData-Version: 4.0
Accept: application/json
```

This example shows the JSON body of the response:

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

The `sample_Video` table is the third of the three related tables. This simple query retrieves the two records in this table.

```http
GET [Organization URI]/api/data/v9.2/sample_videos?$select=sample_name,sample_videoformat
Content-Type: application/json; charset=utf-8
OData-MaxVersion: 4.0
OData-Version: 4.0
Accept: application/json
```

This example shows the JSON body of the response:

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

- Selects the `_sample_mediapolymorphiclookup_value` lookup property in the `$select` query option for the `sample_mediapolymorphiclookup` lookup column. By using the `OData.Community.Display.V1.FormattedValue`, `Microsoft.Dynamics.CRM.associatednavigationproperty`, and `Microsoft.Dynamics.CRM.lookuplogicalname` `odata.include-annotations` preferences, you get these values with each record.
- Expands three single-valued navigation properties, one for each related table. For each expanded navigation property, the primary name column (`sample_name`) is selected as well as the respective custom column value: `sample_callnumber`, `sample_audioformat`, `sample_videoformat`.

> [!NOTE]
> Only one of the three expanded single-valued navigation might have data. All three will be null if the lookup column isn't set.

These operations demonstrate how the table records are related through the `sample_MediaPolymorphicLookup` lookup column.

**Request**

```http
GET [Organization URI]
/api/data/v9.2/sample_medias
?$select=sample_name,_sample_mediapolymorphiclookup_value
&$expand=sample_MediaPolymorphicLookup_sample_book(
    $select=sample_name,sample_callnumber),
sample_MediaPolymorphicLookup_sample_audio(
    $select=sample_name,sample_audioformat),
sample_MediaPolymorphicLookup_sample_video(
    $select=sample_name,sample_videoformat)
Content-Type: application/json; charset=utf-8
OData-MaxVersion: 4.0
OData-Version: 4.0
Accept: application/json
Prefer: odata.include-annotations="OData.Community.Display.V1.FormattedValue,Microsoft.Dynamics.CRM.associatednavigationproperty,Microsoft.Dynamics.CRM.lookuplogicalname"
```

> [!NOTE]
> For readability, the URL is shown across multiple lines. When making the request, remove all line breaks and whitespace so the URL is a single continuous string.

**Response**

When you set these query options and preference headers, the body of the response contains the following JSON:

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
            "sample_name": "Content1",
            "sample_callnumber": "ww-3452"
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
            "sample_name": "Content1",
            "sample_audioformat": "mp4"
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
            "sample_videoid": "00000000-0000-0000-0000-000000000003",
            "sample_name": "Content3",
            "sample_videoformat": "wmv"
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
            "sample_name": "Content3",
            "sample_audioformat": "wma"
         },
         "sample_MediaPolymorphicLookup_sample_video": null
      }
   ]
}
```

## Setting a multi-table lookup column

Updating a record to set a polymorphic lookup column is exactly as described in [Associate with a single-valued navigation property](associate-disassociate-entities-using-web-api.md#associate-with-a-single-valued-navigation-property). Use the correct single-valued navigation property name. These names are case sensitive.

This example shows [updating a value](update-delete-entities-using-web-api.md#basic-update) using `PATCH`.

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
```


## Create a multi-table lookup column

> [!NOTE]
> The following example shows how to use the Dataverse Web API. You can also use the SDK for .NET with the <xref:Microsoft.Crm.Sdk.Messages.CreatePolymorphicLookupAttributeRequest> and <xref:Microsoft.Crm.Sdk.Messages.CreatePolymorphicLookupAttributeResponse> classes.

Use the [CreatePolymorphicLookupAttribute action](xref:Microsoft.Dynamics.CRM.CreatePolymorphicLookupAttribute) to create a multi-table lookup. This example creates the column as part of a solution with the unique name `polymorphiclookupexamplesolution` by using the [MSCRM.SolutionUniqueName optional parameter](../optional-parameters.md#associate-a-solution-component-with-a-solution).

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


## Add relationship to existing multi-table lookup column

Adding a relationship to an existing multi-table lookup column by using the Web API is similar to creating any new one-to-many relationship. [Learn how to create a one-to-many relationship using the Web API](create-update-entity-relationships-using-web-api.md#create-a-one-to-many-relationship). The difference is that the [OneToManyRelationshipMetadata](/power-apps/developer/data-platform/webapi/reference/onetomanyrelationshipmetadata)`.Lookup` property must have a `SchemaName` value that matches the existing polymorphic lookup column.


## Remove a relationship from an existing multi-table lookup column

Removing a relationship from an existing multi-table lookup column by using the Web API is the same as deleting any one-to-many relationship. Send a `DELETE` request to the `RelationshipDefinitions` endpoint by using the value of the [OneToManyRelationshipMetadata](/power-apps/developer/data-platform/webapi/reference/onetomanyrelationshipmetadata)`.MetadataId` property as the key.


### See also

[Sample: Web API multi-table lookup sample (PowerShell)](samples/multi-table-lookup-powershell.md)   
[Use the Web API with table definitions](use-web-api-metadata.md)  
[Create and update table relationships](create-update-entity-relationships-using-web-api.md)  
[Query table definitions using the Web API](query-metadata-web-api.md)  
[Retrieve table definitions by name or MetadataId](retrieve-metadata-name-metadataid.md)  
[Model tables and columns using the Web API](create-update-entity-definitions-using-web-api.md)  
[Web API table schema operations sample](web-api-metadata-operations-sample.md)  
[Web API table schema operations sample (C#)](samples/webapiservice-metadata-operations.md)
