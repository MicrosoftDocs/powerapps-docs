---
title: "Retrieve table definitions by name or MetadataId (Microsoft Dataverse) | Microsoft Docs"
description: "Microsoft Dataverse uses a metadata-driven architecture to provide the flexibility to create custom tables and additional system table columns."
ms.custom: ""
ms.date: 04/22/2021
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
ms.assetid: 80bcdd8e-7c4f-4fd5-8708-00345f5d0408
caps.latest.revision: 8
author: "JimDaly" # GitHub ID
ms.author: "jdaly"
ms.reviewer: "pehecke"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Retrieve table definitions by name or MetadataId

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

Your applications can adapt to configuration changes by querying the table and column definitions (metadata). When you know one of the key properties of a definition item, you can retrieve definitions using the Web API.

<a name="bkmk_byName"></a>

## Retrieve definition items by name
  
All retrievable definition items have a `MetadataId` primary key that can be used to retrieve individual items. For those types of definition which have a defined alternate key, you can retrieve them by name.  
  
Retrieving definition items by name is generally easier because you probably already have some reference to the item name in your code. The following table lists the alternate key properties for retrieving such items by name.
  
|Definition item|Alternate Key|Example|  
|-------------------|-------------------|-------------|  
|Entity|LogicalName|`GET /api/data/v9.0/EntityDefinitions(LogicalName='account')`|  
|Attribute|LogicalName|`GET /api/data/v9.0/EntityDefinitions(LogicalName='account')/Attributes(LogicalName='emailaddress1')`|  
|Relationship|SchemaName|`GET /api/data/v9.0/RelationshipDefinitions(SchemaName='Account_Tasks')`|  
|Global Option Set|Name|`GET /api/data/v9.0/GlobalOptionSetDefinitions(Name='metric_goaltype')`|  
  
<a name="bkmk_exampleByName"></a>

### Example: Retrieve definition items by name

A common definition item that people want to retrieve are the options configured for a particular  attribute. The following example shows how to retrieve the `OptionSet` and `GlobalOptionSet` properties of a  <xref href="Microsoft.Dynamics.CRM.PicklistAttributeMetadata?text=PicklistAttributeMetadata EntityType" />.  
  
> [!NOTE]
>  Expanding both the `OptionSet` and `GlobalOptionSet` single-valued navigation properties of   <xref href="Microsoft.Dynamics.CRM.PicklistAttributeMetadata?text=PicklistAttributeMetadata EntityType" /> allows you to get the option definition whether the attribute is configured to use global option sets or the 'local' option set within the entity. If it is a 'local' option set, the  `GlobalOptionSet` property will be null as shown below.  
>   
>  If the attribute used a global option set, the `GlobalOptionSet` property would contain the defined options and the `OptionSet` property would be null.  
  
 **Request**  

```http  
GET [Organization URI]/api/data/v9.0/EntityDefinitions(LogicalName='account')/Attributes(LogicalName='accountcategorycode')/Microsoft.Dynamics.CRM.PicklistAttributeMetadata?$select=LogicalName&$expand=OptionSet($select=Options),GlobalOptionSet($select=Options) HTTP/1.1  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
Accept: application/json  
Content-Type: application/json; charset=utf-8  
```  
  
 **Response**  

```http   
HTTP/1.1 200 OK  
Content-Type: application/json; odata.metadata=minimal  
OData-Version: 4.0  
  
{  
    "@odata.context": "[Organization URI]/api/data/v9.0/$metadata#EntityDefinitions('account')/Attributes/Microsoft.Dynamics.CRM.PicklistAttributeMetadata(LogicalName,OptionSet,GlobalOptionSet,OptionSet(Options),GlobalOptionSet(Options))/$entity",  
    "LogicalName": "accountcategorycode",  
    "MetadataId": "118771ca-6fb9-4f60-8fd4-99b6124b63ad",  
    "OptionSet@odata.context": "[Organization URI]/api/data/v9.0/$metadata#EntityDefinitions('account')/Attributes(118771ca-6fb9-4f60-8fd4-99b6124b63ad)/Microsoft.Dynamics.CRM.PicklistAttributeMetadata/OptionSet(Options)/$entity",  
    "OptionSet": {  
        "Options": [{  
            "Value": 1,  
            "Label": {  
                "LocalizedLabels": [{  
                    "Label": "Preferred Customer",  
                    "LanguageCode": 1033,  
                    "IsManaged": true,  
                    "MetadataId": "0bd8a218-2341-db11-898a-0007e9e17ebd",  
                    "HasChanged": null  
                }],  
                "UserLocalizedLabel": {  
                    "Label": "Preferred Customer",  
                    "LanguageCode": 1033,  
                    "IsManaged": true,  
                    "MetadataId": "0bd8a218-2341-db11-898a-0007e9e17ebd",  
                    "HasChanged": null  
                }  
            },  
            "Description": {  
                "LocalizedLabels": [  
  
                ],  
                "UserLocalizedLabel": null  
            },  
            "Color": null,  
            "IsManaged": true,  
            "MetadataId": null,  
            "HasChanged": null  
        }, {  
            "Value": 2,  
            "Label": {  
                "LocalizedLabels": [{  
                    "Label": "Standard",  
                    "LanguageCode": 1033,  
                    "IsManaged": true,  
                    "MetadataId": "0dd8a218-2341-db11-898a-0007e9e17ebd",  
                    "HasChanged": null  
                }],  
                "UserLocalizedLabel": {  
                    "Label": "Standard",  
                    "LanguageCode": 1033,  
                    "IsManaged": true,  
                    "MetadataId": "0dd8a218-2341-db11-898a-0007e9e17ebd",  
                    "HasChanged": null  
                }  
            },  
            "Description": {  
                "LocalizedLabels": [  
  
                ],  
                "UserLocalizedLabel": null  
            },  
            "Color": null,  
            "IsManaged": true,  
            "MetadataId": null,  
            "HasChanged": null  
        }],  
        "MetadataId": "b994cdd8-5ce9-4ab9-bdd3-8888ebdb0407"  
    },  
    "GlobalOptionSet": null  
}  
```  
  
<a name="bkmk_byMetadataId"></a>
   
## Retrieve definition items by MetadataId

Because the `MetadataId` is the primary key for definition items, retrieving individual items follows the same pattern used to retrieve business data tables.  
  
|Definition item|Example|  
|-------------------|-------------|  
|Entity|`GET /api/data/v9.0/EntityDefinitions(<Entity MetadataId>)`|  
|Attribute|`GET /api/data/v9.0/EntityDefinitions(<Entity MetadataId>)/Attributes(<Attribute MetadataId>)`|  
|Relationship|`GET /api/data/v9.0/RelationshipDefinitions(<Relationship MetadataId>)`|  
|Global Option Set|`GET /api/data/v9.0/GlobalOptionSetDefinitions(<OptionSet MetadataId>)`|  
  
### Example: Retrieve definition items by MetadataId  

To achieve the same result as shown in [Example: Retrieve definition items by name](#bkmk_exampleByName), you will need to perform a series of query operations to get the `MetadataId` by filtering by the entity `LogicalName` and then by the attribute `LogicalName`.  
  
 **Request**

```http  
GET [Organization URI]/api/data/v9.0/EntityDefinitions?$filter=LogicalName%20eq%20'account'&$select=MetadataId HTTP/1.1  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
Accept: application/json  
Content-Type: application/json; charset=utf-8  
```  
  
 **Response**

```http  
HTTP/1.1 200 OK  
Content-Type: application/json; odata.metadata=minimal  
OData-Version: 4.0  
  
{  
  "@odata.context":"[Organization URI]/api/data/v9.0/$metadata#EntityDefinitions(MetadataId)","value":[  
    {  
      "MetadataId":"70816501-edb9-4740-a16c-6a5efbc05d84"  
    }  
  ]  
}  
```  
  
 **Request**

```http  
GET [Organization URI]/api/data/v9.0/EntityDefinitions(70816501-edb9-4740-a16c-6a5efbc05d84)/Attributes?$filter=LogicalName%20eq%20'accountcategorycode'&$select=MetadataId HTTP/1.1  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
Accept: application/json  
Content-Type: application/json; charset=utf-8  
```  
  
 **Response**

```http  
HTTP/1.1 200 OK  
Content-Type: application/json; odata.metadata=minimal  
OData-Version: 4.0  
  
{  
    "@odata.context": "[Organization URI]/api/data/v9.0/$metadata#EntityDefinitions(70816501-edb9-4740-a16c-6a5efbc05d84)/Attributes(MetadataId)","value":[  
    {  
        "@odata.type": "#Microsoft.Dynamics.CRM.PicklistAttributeMetadata",  
        "MetadataId": "118771ca-6fb9-4f60-8fd4-99b6124b63ad"  
    }  
    ]  
}  
```  
  
 **Request**

```http  
GET [Organization URI]/api/data/v9.0/EntityDefinitions(70816501-edb9-4740-a16c-6a5efbc05d84)/Attributes(118771ca-6fb9-4f60-8fd4-99b6124b63ad)/Microsoft.Dynamics.CRM.PicklistAttributeMetadata?$select=LogicalName&$expand=OptionSet($select=Options),GlobalOptionSet($select=Options) HTTP/1.1  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
Accept: application/json  
Content-Type: application/json; charset=utf-8  
```  
  
 **Response**

```http
HTTP/1.1 200 OK  
Content-Type: application/json; odata.metadata=minimal  
OData-Version: 4.0  
  
{  
    "@odata.context": "[Organization URI]/api/data/v9.0/$metadata#EntityDefinitions(70816501-edb9-4740-a16c-6a5efbc05d84)/Attributes/Microsoft.Dynamics.CRM.PicklistAttributeMetadata(LogicalName,OptionSet,GlobalOptionSet,OptionSet(Options),GlobalOptionSet(Options))/$entity",  
    "LogicalName": "accountcategorycode",  
    "MetadataId": "118771ca-6fb9-4f60-8fd4-99b6124b63ad",  
    "OptionSet@odata.context": "[Organization URI]/api/data/v9.0/$metadata#EntityDefinitions(70816501-edb9-4740-a16c-6a5efbc05d84)/Attributes(118771ca-6fb9-4f60-8fd4-99b6124b63ad)/Microsoft.Dynamics.CRM.PicklistAttributeMetadata/OptionSet(Options)/$entity",  
    "OptionSet": {  
        "Options": [{  
            "Value": 1,  
            "Label": {  
                "LocalizedLabels": [{  
                    "Label": "Preferred Customer",  
                    "LanguageCode": 1033,  
                    "IsManaged": true,  
                    "MetadataId": "0bd8a218-2341-db11-898a-0007e9e17ebd",  
                    "HasChanged": null  
                }],  
                "UserLocalizedLabel": {  
                    "Label": "Preferred Customer",  
                    "LanguageCode": 1033,  
                    "IsManaged": true,  
                    "MetadataId": "0bd8a218-2341-db11-898a-0007e9e17ebd",  
                    "HasChanged": null  
                }  
            },  
            "Description": {  
                "LocalizedLabels": [  
  
                ],  
                "UserLocalizedLabel": null  
            },  
            "Color": null,  
            "IsManaged": true,  
            "MetadataId": null,  
            "HasChanged": null  
        }, {  
            "Value": 2,  
            "Label": {  
                "LocalizedLabels": [{  
                    "Label": "Standard",  
                    "LanguageCode": 1033,  
                    "IsManaged": true,  
                    "MetadataId": "0dd8a218-2341-db11-898a-0007e9e17ebd",  
                    "HasChanged": null  
                }],  
                "UserLocalizedLabel": {  
                    "Label": "Standard",  
                    "LanguageCode": 1033,  
                    "IsManaged": true,  
                    "MetadataId": "0dd8a218-2341-db11-898a-0007e9e17ebd",  
                    "HasChanged": null  
                }  
            },  
            "Description": {  
                "LocalizedLabels": [  
  
                ],  
                "UserLocalizedLabel": null  
            },  
            "Color": null,  
            "IsManaged": true,  
            "MetadataId": null,  
            "HasChanged": null  
        }],  
        "MetadataId": "b994cdd8-5ce9-4ab9-bdd3-8888ebdb0407"  
    },  
    "GlobalOptionSet": null  
}  
```  
  
### See also

[Use the Web API with table definitions](use-web-api-metadata.md)<br />
[Query table definitions using the Web API](query-metadata-web-api.md)<br />
[Create and update table definitions using the Web API](create-update-entity-definitions-using-web-api.md)<br /> 
[Create and update table relationships using the Web API](create-update-entity-relationships-using-web-api.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]