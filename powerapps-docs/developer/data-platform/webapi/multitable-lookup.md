---
title: "Use multi-table lookup columns"
description: "Learn how to use a single lookup type column to refer to data in multiple other tables."
ms.date: 07/07/2021
ms.reviewer: jdaly
ms.topic: article
author: NHelgren
ms.author: nhelgren
search.audienceType: 
  - developer
contributors:
 - JimDaly
---

# Multi-table lookups

Multi-table lookup type columns allow a user to use a specific table that has
multiple one-to-many (1:N) relationships to other tables in the environment. A single lookup
type column can refer to multiple other tables. A lookup value submitted to the
multi-table type column is matched to a record in any of the related
tables. Multi-table lookups can be created with both local tables and virtual tables as referenced tables.

Multi-table types are currently built into Microsoft Dataverse as static types like
Customer, which connects to Account and Contact. This new feature gives users the
power to define any other multi-table lookups they might need.

> [!NOTE]
> At this time users can create and modify custom multi-table lookups via the SDK or Web APIs.
> Interactive user interface support will be coming in a future release.

## Examples

Let's say you're hosting media for users in a library. You have many different
MediaObjects, many of them have the same name but are in different formats like
Books, Audio, and Video. Creating a multi-table lookup called `new_Media`
that has 1:N relationships to `new_Books`, `new_Audio`, and `new_Video` 
results in a `new_Media` lookup table that provides quick identifications of
records stored in specific tables.

### new_Media lookup table

| **PrimaryID** | **PrimaryName**  | **RelatedID** | **Related Name** |
|---------------|------------------|---------------|------------------|
| \<media1\>    | `MediaObjectOne`   | \<books1\>    | `Content1`         |
| \<media2\>    | `MediaObjectTwo`   | \<audio1\>    | `Content1`         |
| \<media3\>    | `MediaObjectThree` | \<video1\>    | `Content3`         |
| \<media4\>    | `MediaObjectFour`  | \<audio2\>    | `Content3`         |

### new_Books table

| **PrimaryID** | **PrimaryName** | **CallNumber** |
|---------------|-----------------|----------------|
| \<books1\>    | `Content1`        | 1ww-3452       |
| \<books2\>    | `Content2`        | a4e-87hw       |

### new_Audio table

| **PrimaryID** | **PrimaryName** | **AudioFormat** |
|---------------|-----------------|-----------------|
| \<audio1\>    | `Content1`        | mp4             |
| \<audio2\>    | `Content3`        | wma             |

### new_Video table

| **PrimaryID** | **PrimaryName** | **VideoFormat** |
|---------------|-----------------|-----------------|
| \<video1\>    | `Content3`        | wmv             |
| \<video2\>    | `Content2`        | avi             |

The Media lookup can return records across all the tables in the polymorphic
lookup.

- A lookup on Media with the name `Content1` would retrieve records for
    \<books1\> and \<audio1\>

- A lookup on Media of `Content3` would retrieve records for \<audio2\> and
    \<video1\>

### Web API example

The following HTTP `POST` request creates a polymorphic lookup attribute.

**Request**

```http
POST [Organization URI]/api/data/v9.2/CreatePolymorphicLookupAttribute HTTP/1.1 

Accept: application/json 
Content-Type: application/json; charset=utf-8 
OData-MaxVersion: 4.0 
OData-Version: 4.0 

{
 "OneToManyRelationships": [
   {
     "SchemaName": "new_media_new_book",
     "ReferencedEntity": "new_book",
     "ReferencingEntity": "new_media"
   },
   {
     "SchemaName": "new_media_new_video",
     "ReferencedEntity": "new_video",
     "ReferencingEntity": "new_media"
   },
   {
     "SchemaName": "new_media_new_audio",
     "ReferencedEntity": "new_audio",
     "ReferencingEntity": "new_media",
     "CascadeConfiguration": {  
        "Assign": "NoCascade",  
        "Delete": "RemoveLink",  
        "Merge": "NoCascade",  
        "Reparent": "NoCascade",  
        "Share": "NoCascade",  
        "Unshare": "NoCascade"  
     }
   }
 ],

 "Lookup": {
   "AttributeType": "Lookup",
   "AttributeTypeName": {
     "Value": "LookupType"
   },

   "Description": {
     "@odata.type": "Microsoft.Dynamics.CRM.Label",
     "LocalizedLabels": [
       {
         "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
         "Label": "Media Polymorphic Lookup",
         "LanguageCode": 1033
       }
     ],

     "UserLocalizedLabel": {
       "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
       "Label": " Media Polymorphic Lookup Attribute",
       "LanguageCode": 1033
     }
   },

   "DisplayName": {
     "@odata.type": "Microsoft.Dynamics.CRM.Label",
     "LocalizedLabels": [
       {
         "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
         "Label": "MediaPolymorphicLookup",
         "LanguageCode": 1033
       }
     ],

     "UserLocalizedLabel": {
       "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
       "Label": "MediaPolymorphicLookup",
       "LanguageCode": 1033
     }
   },

   "SchemaName": "new_mediaPolymporphicLookup",
   "@odata.type": "Microsoft.Dynamics.CRM.ComplexLookupAttributeMetadata"
 }
}
```

The following JSON is the body of the response from the HTTP `POST` request containing the ID of the polymorphic attribute and all the relationships created.

```json
{
    "@odata.context":
      "http://<organization URL>/api/data/v9.1/$metadata#Microsoft.Dynamics.CRM.CreatePolymorphicLookupAttributeResponse",

    "RelationshipIds":[
        "77d4c6e9-0397-eb11-a81c-000d3a6cfaba",
        "7ed4c6e9-0397-eb11-a81c-000d3a6cfaba",
        "85d4c6e9-0397-eb11-a81c-000d3a6cfaba"
    ],

    "AttributeId":"d378dd3e-42f4-4bd7-95c7-0ee546c7de40"
}
```

## Use the multi-table lookup APIs

The following table lists the operations relevant for table and attribute definitions.

| Operation<br/>(method) | Description | URL format |
| --- | --- | --- |
| Create<br/>(POST) | New API | [OrganizationUrl]/api/data/v9.2<br/>/CreatePolymorphicLookupAttribute |
| Retrieve attribute<br/>(GET) | Existing API | [OrganizationUrl]/api/data/v9.2<br/>/EntityDefinitions(\<EntityId\>)/Attributes(\<AttributeId\>) |
| Retrieve relationship<br/>(GET) | Existing API | [OrganizationUrl]/api/data/v9.2<br/>/RelationshipDefinitions(\<RelationshipId\>) |
| Add relationship<br/>(POST) | Adds a relationship<br/>to an existing<br/>polymorphic lookup<br/>attribute | [OrganizationUrl]/api/data/v9.2<br/>/RelationshipDefinitions |
| Remove relationship<br/>(DELETE) | Existing API | [OrganizationUrl]/api/data/v9.2<br/>/RelationshipDefinitions(\<RelationshipId\>) |
| Remove attribute<br/>(DELETE) | Existing API | [OrganizationUrl]/api/data/v9.2<br/>/EntityDefinitions(\<EntityId\>)/Attributes(\<AttributeId\>) |

The following table lists the operations relevant for table and attribute data.

| Operation<br/>(method) | Description | URL format |
| --- | --- | --- |
| Create<br/>(POST) | See the following `new_checkouts` example | [OrganizationUrl]/api/data/v9.2<br/>/\<entitysetName\> |
| Retrieve<br/>(GET) | Add the following header to get annotations:<p/>Content-Type: application/json<br/>Prefer: odata.include-annotations="*" | [OrganizationUrl]/api/data/v9.2<br/>/\<entitysetName\>(\<recordId\>) |

The following example request that creates a new record with two rows.   

```http
POST [OrganizationUrl]/api/data/v9.1/new_checkouts
```

```http
{
  "new_name": "c1",
  new_CheckedoutItem_new_book@odata.bind: "/new_books(387a2c9b-ecc6-ea11-a81e-000d3af68bd7)"
}

{
  "new_name": "c2",
  new_CheckedoutItem_new_device@odata.bind: "/new_devices(6472e7ba-ecc6-ea11-a81e-000d3af68bd7)"
}
```

### Create polymorphic lookup (example payload)

```http
POST [OrganizationUrl]/api/data/v9.2/CreatePolymorphicLookupAttribute
```

```rest
{
  "OneToManyRelationships": [
    {
      "SchemaName": "new_checkout_poly_new_book",
      "ReferencedEntity": "new_book",
      "ReferencingEntity": "new_checkout"
    },
    {
      "SchemaName": "new_checkout_poly_new_device",
      "ReferencedEntity": "new_device",
      "ReferencingEntity": "new_checkout"
    },
    {
      "SchemaName": "new_checkout_poly_new_dvd",
      "ReferencedEntity": "new_dvd",
      "ReferencingEntity": "new_checkout",
      "CascadeConfiguration": {
        "Assign": "NoCascade",
        "Delete": "RemoveLink",
        "Merge": "NoCascade",
        "Reparent": "NoCascade",
        "Share": "NoCascade",
        "Unshare": "NoCascade"
      }
    }
  ],
  "Lookup": {
    "AttributeType": "Lookup",
    "AttributeTypeName": {
      "Value": "LookupType"
    },
    "Description": {
      "@odata.type": "Microsoft.Dynamics.CRM.Label",
      "LocalizedLabels": [
        {
          "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
          "Label": "Checkouted item Polymorphic Lookup Attribute",
          "LanguageCode": 1033
        }
      ],
      "UserLocalizedLabel": {
        "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
        "Label": "Checkedout item Polymorphic Lookup Attribute",
        "LanguageCode": 1033
      }
    },
    "DisplayName": {
      "@odata.type": "Microsoft.Dynamics.CRM.Label",
      "LocalizedLabels": [
        {
          "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
          "Label": "Checkedout item",
          "LanguageCode": 1033
        }
      ],
      "UserLocalizedLabel": {
        "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
        "Label": "Checkedout item",
        "LanguageCode": 1033
      }
    },
    "SchemaName": "new_CheckedoutItem",
    "@odata.type": "Microsoft.Dynamics.CRM.ComplexLookupAttributeMetadata"
  }
}
```

### Add relationship to existing polymorphic lookup (example payload)

```http
POST [OrganizationUrl]/api/data/v9.2/RelationshipDefinitions
```

```rest
{
  "SchemaName": "new_checkout_poly_new_researchresource",
  "@odata.type": "Microsoft.Dynamics.CRM.OneToManyRelationshipMetadata",
  "CascadeConfiguration": {
    "Assign": "NoCascade",
    "Delete": "RemoveLink",
    "Merge": "NoCascade",
    "Reparent": "NoCascade",
    "Share": "NoCascade",
    "Unshare": "NoCascade"
  },
  "ReferencedEntity": "new_researchresource",
  "ReferencingEntity": "new_checkout",
  "Lookup": {
    "AttributeType": "Lookup",
    "AttributeTypeName": { "Value": "LookupType" },
    "Description": {
      "@odata.type": "Microsoft.Dynamics.CRM.Label",
      "LocalizedLabels": [
        {
          "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
          "Label": "Checkout Polymorphic Lookup Attribute",
          "LanguageCode": 1033
        }
      ],
      "UserLocalizedLabel": {
        "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
        "Label": "Checkout Polymorphic Lookup Attribute",
        "LanguageCode": 1033
      }
    },
    "DisplayName": {
      "@odata.type": "Microsoft.Dynamics.CRM.Label",
      "LocalizedLabels": [
        {
          "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
          "Label": "Checkout item",
          "LanguageCode": 1033
        }
      ],
      "UserLocalizedLabel": {
        "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
        "Label": "Checkout item",
        "LanguageCode": 1033
      }
    },
    "SchemaName": "new_CheckedoutItem",
    "@odata.type": "Microsoft.Dynamics.CRM.LookupAttributeMetadata"
  }
}
```

### See Also

[Use the Web API with table definitions](use-web-api-metadata.md)  
[Create and update table relationships](create-update-entity-relationships-using-web-api.md)  
[Query table definitions using the Web API](query-metadata-web-api.md)  
[Retrieve table definitions by name or MetadataId](retrieve-metadata-name-metadataid.md)  
[Model tables and columns using the Web API](create-update-entity-definitions-using-web-api.md)  
[Web API table schema operations sample](web-api-metadata-operations-sample.md)  
[Web API table schema operations sample (C#)](samples/webapiservice-metadata-operations.md)
