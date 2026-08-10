---
title: "Reference Dataverse Schema Definitions by Name or MetadataId"
description: "Learn how to reference Microsoft Dataverse schema definitions by name or MetadataId with the Web API to retrieve table, column, relationship, and choice metadata."
ms.date: 08/07/2026
author: MsSQLGirl
ms.author: jukoesma
ms.reviewer: jdaly
search.audienceType: 
  - developer
contributors: 
  - JimDaly
---
# Reference Dataverse schema definitions by name or MetadataId

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

Learn how to reference Microsoft Dataverse schema definitions by name or MetadataId through the Web API. These queries help applications retrieve metadata and adapt to table and column configuration changes.

> [!NOTE]
> This article demonstrates retrieving schema definitions by name. You can also use the names when performing other operations to create, update, and delete schema entities.

<a name="bkmk_byName"></a>

## Retrieve schema definitions by name
  
All retrievable definition items have a `MetadataId` primary key that you can use to retrieve individual items. For definitions that have an alternate key, you can retrieve them by name.
  
Retrieving definition items by name is easier because you probably already have some reference to the item name in your code. The following table lists the alternate key properties for retrieving such items by name.
  
|Definition item|Alternate Key|Example|  
|-------------------|-------------------|-------------|  
|Entity|LogicalName|`GET /api/data/v9.2/EntityDefinitions(LogicalName='account')`|  
|Attribute|LogicalName|`GET /api/data/v9.2/EntityDefinitions(LogicalName='account')/Attributes(LogicalName='emailaddress1')`|  
|Relationship|SchemaName|`GET /api/data/v9.2/RelationshipDefinitions(SchemaName='Account_Tasks')`|  
|Global Option Set|Name|`GET /api/data/v9.2/GlobalOptionSetDefinitions(Name='metric_goaltype')`|  
  
<a name="bkmk_exampleByName"></a>

### Example: Retrieve schema definitions by name

A common definition item that people want to retrieve is the options configured for a particular attribute. The following example shows how to retrieve the `OptionSet` and `GlobalOptionSet` properties of a <xref href="Microsoft.Dynamics.CRM.PicklistAttributeMetadata?text=PicklistAttributeMetadata EntityType" />.  
  
> [!NOTE]
>  You don't need to expand both the `OptionSet` and `GlobalOptionSet` single-valued navigation properties of <xref href="Microsoft.Dynamics.CRM.PicklistAttributeMetadata?text=PicklistAttributeMetadata EntityType" />. You can get the option definition from either property regardless of whether the attribute is configured to use global option sets or the local option set within the entity.
  
 **Request:**  

```http  
GET [Organization URI]/api/data/v9.2/EntityDefinitions(LogicalName='account')/Attributes(LogicalName='accountcategorycode')/Microsoft.Dynamics.CRM.PicklistAttributeMetadata?$select=LogicalName&$expand=OptionSet($select=Options),GlobalOptionSet($select=Options) HTTP/1.1  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
Accept: application/json  
Content-Type: application/json; charset=utf-8  
```  
  
 **Response:**  

```http   
HTTP/1.1 200 OK  
Content-Type: application/json; odata.metadata=minimal  
OData-Version: 4.0  
  
{
  "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#EntityDefinitions('account')/Attributes/Microsoft.Dynamics.CRM.PicklistAttributeMetadata(LogicalName,OptionSet(Options),GlobalOptionSet(Options))/$entity",
  "MetadataId": "118771ca-6fb9-4f60-8fd4-99b6124b63ad",
  "LogicalName": "accountcategorycode",
  "OptionSet": {
    "MetadataId": "b994cdd8-5ce9-4ab9-bdd3-8888ebdb0407",
    "Options": [
      {
        "Value": 1,
        "Color": null,
        "IsManaged": true,
        "ExternalValue": null,
        "ParentValues": [],
        "Tag": null,
        "IsHidden": false,
        "MetadataId": null,
        "HasChanged": null,
        "Label": {
          "LocalizedLabels": [
            {
              "Label": "Preferred Customer",
              "LanguageCode": 1033,
              "IsManaged": true,
              "MetadataId": "0bd8a218-2341-db11-898a-0007e9e17ebd",
              "HasChanged": null
            }
          ],
          "UserLocalizedLabel": {
            "Label": "Preferred Customer",
            "LanguageCode": 1033,
            "IsManaged": true,
            "MetadataId": "0bd8a218-2341-db11-898a-0007e9e17ebd",
            "HasChanged": null
          }
        },
        "Description": {
          "LocalizedLabels": [],
          "UserLocalizedLabel": null
        }
      },
      {
        "Value": 2,
        "Color": null,
        "IsManaged": true,
        "ExternalValue": null,
        "ParentValues": [],
        "Tag": null,
        "IsHidden": false,
        "MetadataId": null,
        "HasChanged": null,
        "Label": {
          "LocalizedLabels": [
            {
              "Label": "Standard",
              "LanguageCode": 1033,
              "IsManaged": true,
              "MetadataId": "0dd8a218-2341-db11-898a-0007e9e17ebd",
              "HasChanged": null
            }
          ],
          "UserLocalizedLabel": {
            "Label": "Standard",
            "LanguageCode": 1033,
            "IsManaged": true,
            "MetadataId": "0dd8a218-2341-db11-898a-0007e9e17ebd",
            "HasChanged": null
          }
        },
        "Description": {
          "LocalizedLabels": [],
          "UserLocalizedLabel": null
        }
      }
    ]
  },
  "GlobalOptionSet": {
    "MetadataId": "b994cdd8-5ce9-4ab9-bdd3-8888ebdb0407",
    "Options": [
      {
        "Value": 1,
        "Color": null,
        "IsManaged": true,
        "ExternalValue": null,
        "ParentValues": [],
        "Tag": null,
        "IsHidden": false,
        "MetadataId": null,
        "HasChanged": null,
        "Label": {
          "LocalizedLabels": [
            {
              "Label": "Preferred Customer",
              "LanguageCode": 1033,
              "IsManaged": true,
              "MetadataId": "0bd8a218-2341-db11-898a-0007e9e17ebd",
              "HasChanged": null
            }
          ],
          "UserLocalizedLabel": {
            "Label": "Preferred Customer",
            "LanguageCode": 1033,
            "IsManaged": true,
            "MetadataId": "0bd8a218-2341-db11-898a-0007e9e17ebd",
            "HasChanged": null
          }
        },
        "Description": {
          "LocalizedLabels": [],
          "UserLocalizedLabel": null
        }
      },
      {
        "Value": 2,
        "Color": null,
        "IsManaged": true,
        "ExternalValue": null,
        "ParentValues": [],
        "Tag": null,
        "IsHidden": false,
        "MetadataId": null,
        "HasChanged": null,
        "Label": {
          "LocalizedLabels": [
            {
              "Label": "Standard",
              "LanguageCode": 1033,
              "IsManaged": true,
              "MetadataId": "0dd8a218-2341-db11-898a-0007e9e17ebd",
              "HasChanged": null
            }
          ],
          "UserLocalizedLabel": {
            "Label": "Standard",
            "LanguageCode": 1033,
            "IsManaged": true,
            "MetadataId": "0dd8a218-2341-db11-898a-0007e9e17ebd",
            "HasChanged": null
          }
        },
        "Description": {
          "LocalizedLabels": [],
          "UserLocalizedLabel": null
        }
      }
    ]
  }
}
```  
  
<a name="bkmk_byMetadataId"></a>
   
## Retrieve schema definitions by MetadataId

Because the `MetadataId` is the primary key for definition items, retrieving individual items follows the same pattern used to retrieve business data tables.  
  
|Definition item|Example|  
|-------------------|-------------|  
|Entity|`GET /api/data/v9.2/EntityDefinitions(<Entity MetadataId>)`|  
|Attribute|`GET /api/data/v9.2/EntityDefinitions(<Entity MetadataId>)/Attributes(<Attribute MetadataId>)`|  
|Relationship|`GET /api/data/v9.2/RelationshipDefinitions(<Relationship MetadataId>)`|  
|Global Option Set|`GET /api/data/v9.2/GlobalOptionSetDefinitions(<OptionSet MetadataId>)`|  
  
### Example: retrieve schema definitions by MetadataId  

To get the same result as [Example: Retrieve definition items by name](#bkmk_exampleByName), perform a series of query operations to get the `MetadataId` by filtering by the entity `LogicalName` and then by the attribute `LogicalName`.  
  
 **Request:**

```http  
GET [Organization URI]/api/data/v9.2/EntityDefinitions?$filter=LogicalName%20eq%20'account'&$select=MetadataId HTTP/1.1  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
Accept: application/json  
Content-Type: application/json; charset=utf-8  
```  
  
 **Response:**

```http  
HTTP/1.1 200 OK  
Content-Type: application/json; odata.metadata=minimal  
OData-Version: 4.0  
  
{  
  "@odata.context":"[Organization URI]/api/data/v9.2/$metadata#EntityDefinitions(MetadataId)","value":[  
    {  
      "MetadataId":"70816501-edb9-4740-a16c-6a5efbc05d84"  
    }  
  ]  
}  
```  
  
 **Request:**

```http  
GET [Organization URI]/api/data/v9.2/EntityDefinitions(70816501-edb9-4740-a16c-6a5efbc05d84)/Attributes?$filter=LogicalName%20eq%20'accountcategorycode'&$select=MetadataId HTTP/1.1  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
Accept: application/json  
Content-Type: application/json; charset=utf-8  
```  
  
 **Response:**

```http  
HTTP/1.1 200 OK  
Content-Type: application/json; odata.metadata=minimal  
OData-Version: 4.0  
  
{  
    "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#EntityDefinitions(70816501-edb9-4740-a16c-6a5efbc05d84)/Attributes(MetadataId)","value":[  
    {  
        "@odata.type": "#Microsoft.Dynamics.CRM.PicklistAttributeMetadata",  
        "MetadataId": "118771ca-6fb9-4f60-8fd4-99b6124b63ad"  
    }  
    ]  
}  
```  
  
 **Request:**

```http  
GET [Organization URI]/api/data/v9.2/EntityDefinitions(70816501-edb9-4740-a16c-6a5efbc05d84)/Attributes(118771ca-6fb9-4f60-8fd4-99b6124b63ad)/Microsoft.Dynamics.CRM.PicklistAttributeMetadata?$select=LogicalName&$expand=OptionSet($select=Options),GlobalOptionSet($select=Options) HTTP/1.1  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
Accept: application/json  
Content-Type: application/json; charset=utf-8  
```  
  
 **Response:**

```http
HTTP/1.1 200 OK  
Content-Type: application/json; odata.metadata=minimal  
OData-Version: 4.0  
  
{
  "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#EntityDefinitions('account')/Attributes/Microsoft.Dynamics.CRM.PicklistAttributeMetadata(LogicalName,OptionSet(Options),GlobalOptionSet(Options))/$entity",
  "MetadataId": "118771ca-6fb9-4f60-8fd4-99b6124b63ad",
  "LogicalName": "accountcategorycode",
  "OptionSet": {
    "MetadataId": "b994cdd8-5ce9-4ab9-bdd3-8888ebdb0407",
    "Options": [
      {
        "Value": 1,
        "Color": null,
        "IsManaged": true,
        "ExternalValue": null,
        "ParentValues": [],
        "Tag": null,
        "IsHidden": false,
        "MetadataId": null,
        "HasChanged": null,
        "Label": {
          "LocalizedLabels": [
            {
              "Label": "Preferred Customer",
              "LanguageCode": 1033,
              "IsManaged": true,
              "MetadataId": "0bd8a218-2341-db11-898a-0007e9e17ebd",
              "HasChanged": null
            }
          ],
          "UserLocalizedLabel": {
            "Label": "Preferred Customer",
            "LanguageCode": 1033,
            "IsManaged": true,
            "MetadataId": "0bd8a218-2341-db11-898a-0007e9e17ebd",
            "HasChanged": null
          }
        },
        "Description": {
          "LocalizedLabels": [],
          "UserLocalizedLabel": null
        }
      },
      {
        "Value": 2,
        "Color": null,
        "IsManaged": true,
        "ExternalValue": null,
        "ParentValues": [],
        "Tag": null,
        "IsHidden": false,
        "MetadataId": null,
        "HasChanged": null,
        "Label": {
          "LocalizedLabels": [
            {
              "Label": "Standard",
              "LanguageCode": 1033,
              "IsManaged": true,
              "MetadataId": "0dd8a218-2341-db11-898a-0007e9e17ebd",
              "HasChanged": null
            }
          ],
          "UserLocalizedLabel": {
            "Label": "Standard",
            "LanguageCode": 1033,
            "IsManaged": true,
            "MetadataId": "0dd8a218-2341-db11-898a-0007e9e17ebd",
            "HasChanged": null
          }
        },
        "Description": {
          "LocalizedLabels": [],
          "UserLocalizedLabel": null
        }
      }
    ]
  },
  "GlobalOptionSet": {
    "MetadataId": "b994cdd8-5ce9-4ab9-bdd3-8888ebdb0407",
    "Options": [
      {
        "Value": 1,
        "Color": null,
        "IsManaged": true,
        "ExternalValue": null,
        "ParentValues": [],
        "Tag": null,
        "IsHidden": false,
        "MetadataId": null,
        "HasChanged": null,
        "Label": {
          "LocalizedLabels": [
            {
              "Label": "Preferred Customer",
              "LanguageCode": 1033,
              "IsManaged": true,
              "MetadataId": "0bd8a218-2341-db11-898a-0007e9e17ebd",
              "HasChanged": null
            }
          ],
          "UserLocalizedLabel": {
            "Label": "Preferred Customer",
            "LanguageCode": 1033,
            "IsManaged": true,
            "MetadataId": "0bd8a218-2341-db11-898a-0007e9e17ebd",
            "HasChanged": null
          }
        },
        "Description": {
          "LocalizedLabels": [],
          "UserLocalizedLabel": null
        }
      },
      {
        "Value": 2,
        "Color": null,
        "IsManaged": true,
        "ExternalValue": null,
        "ParentValues": [],
        "Tag": null,
        "IsHidden": false,
        "MetadataId": null,
        "HasChanged": null,
        "Label": {
          "LocalizedLabels": [
            {
              "Label": "Standard",
              "LanguageCode": 1033,
              "IsManaged": true,
              "MetadataId": "0dd8a218-2341-db11-898a-0007e9e17ebd",
              "HasChanged": null
            }
          ],
          "UserLocalizedLabel": {
            "Label": "Standard",
            "LanguageCode": 1033,
            "IsManaged": true,
            "MetadataId": "0dd8a218-2341-db11-898a-0007e9e17ebd",
            "HasChanged": null
          }
        },
        "Description": {
          "LocalizedLabels": [],
          "UserLocalizedLabel": null
        }
      }
    ]
  }
}
```  
  
### See also

[Use the Web API with table definitions](use-web-api-metadata.md)  
[Query table definitions using the Web API](query-metadata-web-api.md)  
[Create and update table definitions using the Web API](create-update-entity-definitions-using-web-api.md)  
[Create and update table relationships using the Web API](create-update-entity-relationships-using-web-api.md)  
[Web API table schema operations sample](web-api-metadata-operations-sample.md)  
[Web API table schema operations sample (C#)](samples/webapiservice-metadata-operations.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
