---
title: "Use multi-table lookup columns (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn how to use a single lookup type column to refer to data in multiple other tables." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 07/06/2021
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "NHelgren" # GitHub ID
ms.author: "nhelgren" # MSFT alias of Microsoft employees only
manager: "mayadumesh" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Multi-table Lookups

Multi-table lookup type columns allow a user to use a specific table that has
multiple one-to-many (1:M) relationships to other tables in the environment. A single lookup
type column can refer to multiple other tables. A lookup value submitted to the
multi-table type column will be matched to a record in any of the related
tables.

Multi-table types are currently built into Microsoft Dataverse as static types like
Customer, which connects to Account and Contact. This new feature gives users the
power to define any other multi-table lookups they may need.

> [!NOTE]
> At this time users can create and modify custom multi-table lookups via the SDK or Web APIs.
> Interactive user interface support will be coming in a future release.

## Examples

Let's say you are hosting media for users in a library. You have many different
MediaObjects, many of them have the same name but are in different formats like
“Books”, “Audio”, and “Video”. Creating a multi-table lookup called “new_Media”
that has 1:M relationships to “new_Books”, “new_Audio”, and “new_Video” will
result in a “new_Media” lookup table that provides quick identifications of
records stored in specific tables.

### new_Media lookup table

| **PrimaryID** | **PrimaryName**  | **RelatedID** | **Related Name** |
|---------------|------------------|---------------|------------------|
| \<media1\>    | MediaObjectOne   | \<books1\>    | Content1         |
| \<media2\>    | MediaObjectTwo   | \<audio1\>    | Content1         |
| \<media3\>    | MediaObjectThree | \<video1\>    | Content3         |
| \<media4\>    | MediaObjectFour  | \<audio2\>    | Content3         |

### new_Books table

| **PrimaryID** | **PrimaryName** | **CallNumber** |
|---------------|-----------------|----------------|
| \<books1\>    | Content1        | 1ww-3452       |
| \<books2\>    | Content2        | a4e-87hw       |

### new_Audio table

| **PrimaryID** | **PrimaryName** | **AudioFormat** |
|---------------|-----------------|-----------------|
| \<audio1\>    | Content1        | mp4             |
| \<audio2\>    | Content3        | wma             |

### new_Video table

| **PrimaryID** | **PrimaryName** | **VideoFormat** |
|---------------|-----------------|-----------------|
| \<video1\>    | Content3        | wmv             |
| \<video2\>    | Content2        | avi             |

The Media look up can return records across all the tables in the polymorphic
lookup.

- A lookup on Media with the name Content1 would retrieve records for
    \<books1\> and \<audio1\>

- A lookup on Media of Content3 would retrieve records for \<audio2\> and
    \<video1\>

### Web API example

Shown below is an HTTP post for a polymorphic lookup attribute. 

```http
POST [Organization URI]/api/data/v9.0/CreatePolymorphicLookupAttribute HTTP/1.1 

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
         "\@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
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

The response from the HTTP post is shown below containing the ID of the polymorphic attribute and all the relationships created.

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
```

### See Also

[Create and update entity relationships](create-update-entity-relationships-using-web-api.md)
