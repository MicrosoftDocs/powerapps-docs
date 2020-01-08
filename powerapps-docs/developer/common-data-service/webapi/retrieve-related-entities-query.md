---
title: "Retrieve related entity records with a query (Common Data Service)| Microsoft Docs"
description: "ead how you can retrieve related entity records by expanding the navigation properties."
ms.custom: ""
ms.date: 01/08/2020
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
ms.assetid: 3D8FB9AF-3663-437A-988E-CBAE9579F167
caps.latest.revision: 78
author: "susikka"
ms.author: "susikka"
manager: "shujoshi"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Retrieve related entity records with a query

Use the `$expand` system query option in the navigation properties to control what data from related entities is returned. There are two types of navigation properties:  
  
- *Single-valued* navigation properties correspond to Lookup attributes that support many-to-one relationships and allow setting a reference to another entity.  
  
- *Collection-valued* navigation properties correspond to one-to-many or many-to-many relationships.  
  
If you include only the name of the navigation property, you’ll receive all the properties for related records. You can limit the properties returned for related records using the `$select` system query option in parentheses after the navigation property name. Use this for both single-valued and collection-valued navigation properties.  

> [!NOTE]
>  - To retrieve related entities for an entity instance, see [Retrieve related entities for an entity by expanding navigation properties](retrieve-entity-using-web-api.md#bkmk_expandRelated). 
> - Queries which expand collection-valued navigation properties may return cached data for those properties that doesn’t reflect recent changes. It is recommended to use `If-None-Match` header with value `null` to override browser caching. See [HTTP Headers](compose-http-requests-handle-errors.md#bkmk_headers) for more details.
> 

<a bkmk="bkmk_retrieverelatedentityexpandsinglenavprop"></a>

## Retrieve related entity records by expanding single-valued navigation properties

The following example demonstrates how to retrieve the contact for all the account records. For the related contact records, we are only retrieving the contactid and fullname.  
  
**Request**  

```http 
GET [Organization URI]/api/data/v9.1/accounts?$select=name&$expand=primarycontactid($select=contactid,fullname) HTTP/1.1  
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
```  
  
**Response** 
 
```http 
HTTP/1.1 200 OK  
Content-Type: application/json; odata.metadata=minimal  
OData-Version: 4.0  
  
{  
   "@odata.context":"[Organization URI]/api/data/v9.1/$metadata#accounts(name,primarycontactid,primarycontactid(contactid,fullname))",
   "value":[  
      {  
         "@odata.etag":"W/\"513475\"",
         "name":"Fourth Coffee (sample)",
         "accountid":"36dbf27c-8efb-e511-80d2-00155db07c77",
         "primarycontactid":{  
            "contactid":"9cdbf27c-8efb-e511-80d2-00155db07c77",
            "fullname":"Yvonne McKay (sample)"
         }
      },
      {  
         "@odata.etag":"W/\"513477\"",
         "name":"Litware, Inc. (sample)",
         "accountid":"38dbf27c-8efb-e511-80d2-00155db07c77",
         "primarycontactid":{  
            "contactid":"9edbf27c-8efb-e511-80d2-00155db07c77",
            "fullname":"Susanna Stubberod (sample)"
         }
      },
      {  
         "@odata.etag":"W/\"513479\"",
         "name":"Adventure Works (sample)",
         "accountid":"3adbf27c-8efb-e511-80d2-00155db07c77",
         "primarycontactid":{  
            "contactid":"a0dbf27c-8efb-e511-80d2-00155db07c77",
            "fullname":"Nancy Anderson (sample)"
         }
      },
      {  
         "@odata.etag":"W/\"513481\"",
         "name":"Fabrikam, Inc. (sample)",
         "accountid":"3cdbf27c-8efb-e511-80d2-00155db07c77",
         "primarycontactid":{  
            "contactid":"a2dbf27c-8efb-e511-80d2-00155db07c77",
            "fullname":"Maria Campbell (sample)"
         }
      },
      {  
         "@odata.etag":"W/\"514057\"",
         "name":"Blue Yonder Airlines (sample)",
         "accountid":"3edbf27c-8efb-e511-80d2-00155db07c77",
         "primarycontactid":{  
            "contactid":"a0dbf27c-8efb-e511-80d2-00155db07c77",
            "fullname":"Nancy Anderson (sample)"
         }
      },
      {  
         "@odata.etag":"W/\"513485\"",
         "name":"City Power & Light (sample)",
         "accountid":"40dbf27c-8efb-e511-80d2-00155db07c77",
         "primarycontactid":{  
            "contactid":"a6dbf27c-8efb-e511-80d2-00155db07c77",
            "fullname":"Scott Konersmann (sample)"
         }
      },
      {  
         "@odata.etag":"W/\"513487\"",
         "name":"Contoso Pharmaceuticals (sample)",
         "accountid":"42dbf27c-8efb-e511-80d2-00155db07c77",
         "primarycontactid":{  
            "contactid":"a8dbf27c-8efb-e511-80d2-00155db07c77",
            "fullname":"Robert Lyon (sample)"
         }
      },
      {  
         "@odata.etag":"W/\"513489\"",
         "name":"Alpine Ski House (sample)",
         "accountid":"44dbf27c-8efb-e511-80d2-00155db07c77",
         "primarycontactid":{  
            "contactid":"aadbf27c-8efb-e511-80d2-00155db07c77",
            "fullname":"Paul Cannon (sample)"
         }
      },
      {  
         "@odata.etag":"W/\"513491\"",
         "name":"A. Datum Corporation (sample)",
         "accountid":"46dbf27c-8efb-e511-80d2-00155db07c77",
         "primarycontactid":{  
            "contactid":"acdbf27c-8efb-e511-80d2-00155db07c77",
            "fullname":"Rene Valdes (sample)"
         }
      },
      {  
         "@odata.etag":"W/\"513493\"",
         "name":"Coho Winery (sample)",
         "accountid":"48dbf27c-8efb-e511-80d2-00155db07c77",
         "primarycontactid":{  
            "contactid":"aedbf27c-8efb-e511-80d2-00155db07c77",
            "fullname":"Jim Glynn (sample)"
         }
      }
   ]
}    
```  

Instead of returning the related entities for entity sets, you can also return references (links) to the related entities by expanding the single-valued navigation property with the `$ref` option. The following example returns links to the contact records for all the accounts.  
  
 **Request**

```http  
GET [Organization URI]/api/data/v9.1/accounts?$select=name&$expand=primarycontactid/$ref HTTP/1.1  
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
```  
  
 **Response**
 
```http 
HTTP/1.1 200 OK  
Content-Type: application/json; odata.metadata=minimal  
OData-Version: 4.0  
  
{  
   "@odata.context":"[Organization URI]/api/data/v9.1/$metadata#accounts(name,primarycontactid)",
   "value":[  
      {  
         "@odata.etag":"W/\"513475\"",
         "name":"Fourth Coffee (sample)",
         "_primarycontactid_value":"9cdbf27c-8efb-e511-80d2-00155db07c77",
         "accountid":"36dbf27c-8efb-e511-80d2-00155db07c77",
         "primarycontactid":{  
            "@odata.id":"[Organization URI]/api/data/v9.1/contacts(9cdbf27c-8efb-e511-80d2-00155db07c77)"
         }
      },
      {  
         "@odata.etag":"W/\"513477\"",
         "name":"Litware, Inc. (sample)",
         "_primarycontactid_value":"9edbf27c-8efb-e511-80d2-00155db07c77",
         "accountid":"38dbf27c-8efb-e511-80d2-00155db07c77",
         "primarycontactid":{  
            "@odata.id":"[Organization URI]/api/data/v9.1/contacts(9edbf27c-8efb-e511-80d2-00155db07c77)"
         }
      },
      {  
         "@odata.etag":"W/\"513479\"",
         "name":"Adventure Works (sample)",
         "_primarycontactid_value":"a0dbf27c-8efb-e511-80d2-00155db07c77",
         "accountid":"3adbf27c-8efb-e511-80d2-00155db07c77",
         "primarycontactid":{  
            "@odata.id":"[Organization URI]/api/data/v9.1/contacts(a0dbf27c-8efb-e511-80d2-00155db07c77)"
         }
      },
      {  
         "@odata.etag":"W/\"513481\"",
         "name":"Fabrikam, Inc. (sample)",
         "_primarycontactid_value":"a2dbf27c-8efb-e511-80d2-00155db07c77",
         "accountid":"3cdbf27c-8efb-e511-80d2-00155db07c77",
         "primarycontactid":{  
            "@odata.id":"[Organization URI]/api/data/v9.1/contacts(a2dbf27c-8efb-e511-80d2-00155db07c77)"
         }
      },
      {  
         "@odata.etag":"W/\"514057\"",
         "name":"Blue Yonder Airlines (sample)",
         "_primarycontactid_value":"a0dbf27c-8efb-e511-80d2-00155db07c77",
         "accountid":"3edbf27c-8efb-e511-80d2-00155db07c77",
         "primarycontactid":{  
            "@odata.id":"[Organization URI]/api/data/v9.1/contacts(a0dbf27c-8efb-e511-80d2-00155db07c77)"
         }
      },
      {  
         "@odata.etag":"W/\"513485\"",
         "name":"City Power & Light (sample)",
         "_primarycontactid_value":"a6dbf27c-8efb-e511-80d2-00155db07c77",
         "accountid":"40dbf27c-8efb-e511-80d2-00155db07c77",
         "primarycontactid":{  
            "@odata.id":"[Organization URI]/api/data/v9.1/contacts(a6dbf27c-8efb-e511-80d2-00155db07c77)"
         }
      },
      {  
         "@odata.etag":"W/\"513487\"",
         "name":"Contoso Pharmaceuticals (sample)",
         "_primarycontactid_value":"a8dbf27c-8efb-e511-80d2-00155db07c77",
         "accountid":"42dbf27c-8efb-e511-80d2-00155db07c77",
         "primarycontactid":{  
            "@odata.id":"[Organization URI]/api/data/v9.1/contacts(a8dbf27c-8efb-e511-80d2-00155db07c77)"
         }
      },
      {  
         "@odata.etag":"W/\"513489\"",
         "name":"Alpine Ski House (sample)",
         "_primarycontactid_value":"aadbf27c-8efb-e511-80d2-00155db07c77",
         "accountid":"44dbf27c-8efb-e511-80d2-00155db07c77",
         "primarycontactid":{  
            "@odata.id":"[Organization URI]/api/data/v9.1/contacts(aadbf27c-8efb-e511-80d2-00155db07c77)"
         }
      },
      {  
         "@odata.etag":"W/\"513491\"",
         "name":"A. Datum Corporation (sample)",
         "_primarycontactid_value":"acdbf27c-8efb-e511-80d2-00155db07c77",
         "accountid":"46dbf27c-8efb-e511-80d2-00155db07c77",
         "primarycontactid":{  
            "@odata.id":"[Organization URI]/api/data/v9.1/contacts(acdbf27c-8efb-e511-80d2-00155db07c77)"
         }
      },
      {  
         "@odata.etag":"W/\"513493\"",
         "name":"Coho Winery (sample)",
         "_primarycontactid_value":"aedbf27c-8efb-e511-80d2-00155db07c77",
         "accountid":"48dbf27c-8efb-e511-80d2-00155db07c77",
         "primarycontactid":{  
            "@odata.id":"[Organization URI]/api/data/v9.1/contacts(aedbf27c-8efb-e511-80d2-00155db07c77)"
         }
      }
   ]
}  
```  

<a bkmk="bkmk_retrieverelatedentityexpandcollectionnavprop"></a>

## Retrieve related entities by expanding collection-valued navigation properties

If you expand on collection-valued navigation parameters to retrieve related entities for entity sets, an `@odata.nextLink` property will be returned for the related entities. You should use the value of the `@odata.nextLink` property with a new `GET` request to return the required data.  

The following example retrieves the tasks assigned to the top 5 account records.  
  
**Request**

```http 
GET [Organization URI]/api/data/v9.1/accounts?$top=5&$select=name&$expand=Account_Tasks($select%20=%20subject,%20scheduledstart) HTTP/1.1  
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
```  
  
**Response** 
 
```http 
HTTP/1.1 200 OK  
Content-Type: application/json; odata.metadata=minimal  
OData-Version: 4.0  
  
{  
   "@odata.context":"[Organization URI]/api/data/v9.1/$metadata#accounts(name,Account_Tasks,Account_Tasks(subject,scheduledstart))",
   "value":[  
      {  
         "@odata.etag":"W/\"513475\"",
         "name":"Fourth Coffee (sample)",
         "accountid":"36dbf27c-8efb-e511-80d2-00155db07c77",
         "Account_Tasks":[  

         ],
         "Account_Tasks@odata.nextLink":"[Organization URI]/api/data/v9.1/accounts(36dbf27c-8efb-e511-80d2-00155db07c77)/Account_Tasks?$select%20=%20subject,%20scheduledstart"
      },
      {  
         "@odata.etag":"W/\"513477\"",
         "name":"Litware, Inc. (sample)",
         "accountid":"38dbf27c-8efb-e511-80d2-00155db07c77",
         "Account_Tasks":[  

         ],
         "Account_Tasks@odata.nextLink":"[Organization URI]/api/data/v9.1/accounts(38dbf27c-8efb-e511-80d2-00155db07c77)/Account_Tasks?$select%20=%20subject,%20scheduledstart"
      },
      {  
         "@odata.etag":"W/\"514074\"",
         "name":"Adventure Works (sample)",
         "accountid":"3adbf27c-8efb-e511-80d2-00155db07c77",
         "Account_Tasks":[  

         ],
         "Account_Tasks@odata.nextLink":"[Organization URI]/api/data/v9.1/accounts(3adbf27c-8efb-e511-80d2-00155db07c77)/Account_Tasks?$select%20=%20subject,%20scheduledstart"
      },
      {  
         "@odata.etag":"W/\"513481\"",
         "name":"Fabrikam, Inc. (sample)",
         "accountid":"3cdbf27c-8efb-e511-80d2-00155db07c77",
         "Account_Tasks":[  

         ],
         "Account_Tasks@odata.nextLink":"[Organization URI]/api/data/v9.1/accounts(3cdbf27c-8efb-e511-80d2-00155db07c77)/Account_Tasks?$select%20=%20subject,%20scheduledstart"
      },
      {  
         "@odata.etag":"W/\"514057\"",
         "name":"Blue Yonder Airlines (sample)",
         "accountid":"3edbf27c-8efb-e511-80d2-00155db07c77",
         "Account_Tasks":[  

         ],
         "Account_Tasks@odata.nextLink":"[Organization URI]/api/data/v9.1/accounts(3edbf27c-8efb-e511-80d2-00155db07c77)/Account_Tasks?$select%20=%20subject,%20scheduledstart"
          }
       ]
    }
 
```  

<a bkmk="bkmk_retrieverelatedentitysingleandcollectionnavprop"></a>
  
## Retrieve related entities by expanding both single-valued and collection-valued navigation properties

The following example demonstrates how you can expand related entities for entity sets using both single- and collection-valued navigation properties. As explained earlier, expanding on collection-valued navigation properties to retrieve related entities for entity sets returns an `@odata.nextLink` property for the related entities. You should use the value of the `@odata.nextLink` property with a new `GET` request to return the required data.  
  
In this example, we are retrieving the contact and tasks assigned to the top 3 accounts.  
  
**Request**

```http 
GET [Organization URI]/api/data/v9.1/accounts?$top=3&$select=name&$expand=primarycontactid($select=contactid,fullname),Account_Tasks($select=subject,scheduledstart)  HTTP/1.1  
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
```  
  
**Response**  

```http 
HTTP/1.1 200 OK  
Content-Type: application/json; odata.metadata=minimal  
OData-Version: 4.0  
  
{  
   "@odata.context":"[Organization URI]/api/data/v9.1/$metadata#accounts(name,primarycontactid,Account_Tasks,primarycontactid(contactid,fullname),Account_Tasks(subject,scheduledstart))",
   "value":[  
      {  
         "@odata.etag":"W/\"550614\"",
         "name":"Fourth Coffee (sample)",
         "accountid":"5b9648c3-68f7-e511-80d3-00155db53318",
         "primarycontactid":{  
            "contactid":"c19648c3-68f7-e511-80d3-00155db53318",
            "fullname":"Yvonne McKay (sample)"
         },
         "Account_Tasks":[  

         ],
         "Account_Tasks@odata.nextLink":"[Organization URI]/api/data/v9.1/accounts(5b9648c3-68f7-e511-80d3-00155db53318)/Account_Tasks?$select=subject,scheduledstart"
      },
      {  
         "@odata.etag":"W/\"550615\"",
         "name":"Litware, Inc. (sample)",
         "accountid":"5d9648c3-68f7-e511-80d3-00155db53318",
         "primarycontactid":{  
            "contactid":"c39648c3-68f7-e511-80d3-00155db53318",
            "fullname":"Susanna Stubberod (sample)"
         },
         "Account_Tasks":[  

         ],
         "Account_Tasks@odata.nextLink":"[Organization URI]/api/data/v9.1/accounts(5d9648c3-68f7-e511-80d3-00155db53318)/Account_Tasks?$select=subject,scheduledstart"
      },
      {  
         "@odata.etag":"W/\"550616\"",
         "name":"Adventure Works (sample)",
         "accountid":"5f9648c3-68f7-e511-80d3-00155db53318",
         "primarycontactid":{  
            "contactid":"c59648c3-68f7-e511-80d3-00155db53318",
            "fullname":"Nancy Anderson (sample)"
         },
         "Account_Tasks":[  

         ],
         "Account_Tasks@odata.nextLink":"[Organization URI]/api/data/v9.1/accounts(5f9648c3-68f7-e511-80d3-00155db53318)/Account_Tasks?$select=subject,scheduledstart"
      }
   ]
}
  
```
## Filter collection values based on data in related entities

The Web API allows you to use two lambda operators, which are `any` and `all` to evaluate a Boolean expression on a collection. More information: [Use Lambda operators](query-data-web-api.md#bkmk_LambdaOperators).

## See also

[Query data using Web API](query-data-web-api.md)<br />
[Perform operations using the Web API](perform-operations-web-api.md)<br />
[Compose Http requests and handle errors](compose-http-requests-handle-errors.md)<br />
[Create an entity using the Web API](create-entity-web-api.md)<br />
[Retrieve an entity using the Web API](retrieve-entity-using-web-api.md)<br />
[Update and delete entities using the Web API](update-delete-entities-using-web-api.md)<br />
[Associate and disassociate entities using the Web API](associate-disassociate-entities-using-web-api.md)
