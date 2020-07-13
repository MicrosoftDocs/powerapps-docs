---
title: "Retrieve related entity records with a query (Common Data Service)| Microsoft Docs"
description: "ead how you can retrieve related entity records by expanding the navigation properties."
ms.custom: ""
ms.date: 06/27/2020
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
ms.assetid: 3D8FB9AF-3663-437A-988E-CBAE9579F167
caps.latest.revision: 78
author: "JimDaly"
ms.author: "phecke"
manager: "ryjones"
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
>  - You are limited to no more than 10 `$expand` options in a query. This is to protect performance. Each `$expand` options creates a join that can impact performance. 
>  - To retrieve related entities for an entity instance, see [Retrieve related entities for an entity by expanding navigation properties](retrieve-entity-using-web-api.md#bkmk_expandRelated). 
> - Queries which expand collection-valued navigation properties may return cached data for those properties that doesn’t reflect recent changes. It is recommended to use `If-None-Match` header with value `null` to override browser caching. See [HTTP Headers](compose-http-requests-handle-errors.md#bkmk_headers) for more details.
> 

<a bkmk="bkmk_retrieverelatedentityexpandsinglenavprop"></a>

## Retrieve related entity records by expanding single-valued navigation properties

The following example demonstrates how to retrieve the contact for all the account records. For the related contact records, we are only retrieving the contactid and fullname.  
  
**Request**  

```http 
GET [Organization URI]/api/data/v9.1/accounts?$select=name
&$expand=primarycontactid($select=contactid,fullname) HTTP/1.1  
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
      }
   ]
}
```  

Instead of returning the related entities for entity sets, you can also return references (links) to the related entities by expanding the single-valued navigation property with the `$ref` option. The following example returns links to the contact records for all the accounts.  
  
 **Request**

```http  
GET [Organization URI]/api/data/v9.1/accounts?$select=name
&$expand=primarycontactid/$ref HTTP/1.1  
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
      }
   ]
}  
```

## Multi-level expand of single-valued navigation properties

You can expand single-valued navigation properties to multiple levels by nesting an `$expand` option within another `$expand` option.

> [!NOTE]
> There is no limit on the depth of nested `$expand` options, but the combined limit of 10 total `$expand` options in a query still applies.


The following query returns `task` records and expands the related `contact`, the `account` related to the `contact`, and finally to the `systemuser` who created the  `account` record.

**Request**

```http
GET [Organization URI]/api/data/v9.1/tasks?$select=subject
&$expand=regardingobjectid_contact_task($select=fullname;
 $expand=parentcustomerid_account($select=name;
  $expand=createdby($select=fullname))) HTTP/1.1  
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
    "@odata.context": "[Organization URI]/api/data/v9.1/$metadata#tasks(subject,regardingobjectid_contact_task(fullname,parentcustomerid_account(name,createdby(fullname))))",
    "value":
  [
     {
        "@odata.etag": "W/\"28876997\"",
        "subject": "Task 1 for Susanna Stubberod",
        "activityid": "834814f9-b0b8-ea11-a812-000d3a122b89",
        "regardingobjectid_contact_task": {
            "fullname": "Susanna Stubberod (sample)",
            "contactid": "824814f9-b0b8-ea11-a812-000d3a122b89",
            "parentcustomerid_account": {
                "name": "Contoso, Ltd. (sample)",
                "accountid": "7a4814f9-b0b8-ea11-a812-000d3a122b89",
                "createdby": {
                    "fullname": "Nancy Anderson",
                    "systemuserid": "4026be43-6b69-e111-8f65-78e7d1620f5e",
                    "ownerid": "4026be43-6b69-e111-8f65-78e7d1620f5e"
                }
            }
        }
    },
    {
        "@odata.etag": "W/\"28877001\"",
        "subject": "Task 2 for Susanna Stubberod",
        "activityid": "844814f9-b0b8-ea11-a812-000d3a122b89",
        "regardingobjectid_contact_task": {
            "fullname": "Susanna Stubberod (sample)",
            "contactid": "824814f9-b0b8-ea11-a812-000d3a122b89",
            "parentcustomerid_account": {
                "name": "Contoso, Ltd. (sample)",
                "accountid": "7a4814f9-b0b8-ea11-a812-000d3a122b89",
                "createdby": {
                    "fullname": "Nancy Anderson",
                    "systemuserid": "4026be43-6b69-e111-8f65-78e7d1620f5e",
                    "ownerid": "4026be43-6b69-e111-8f65-78e7d1620f5e"
                }
            }
        }
     }
  ]
}
```

<a bkmk="bkmk_retrieverelatedentityexpandcollectionnavprop"></a>

## Retrieve related entities by expanding collection-valued navigation properties

If you expand on collection-valued navigation parameters to retrieve related entities for entity sets, an `@odata.nextLink` property will be returned for the related entities. You should use the value of the `@odata.nextLink` property with a new `GET` request to return the required data.  

The following example retrieves the tasks assigned to the top 2 account records.  
  
**Request**

```http 
GET [Organization URI]/api/data/v9.1/accounts?$top=2
&$select=name
&$expand=Account_Tasks($select=subject,scheduledstart) HTTP/1.1  
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
         "Account_Tasks":[],
         "Account_Tasks@odata.nextLink":"[Organization URI]/api/data/v9.1/accounts(36dbf27c-8efb-e511-80d2-00155db07c77)/Account_Tasks?$select%20=%20subject,%20scheduledstart"
      },
      {  
         "@odata.etag":"W/\"513477\"",
         "name":"Litware, Inc. (sample)",
         "accountid":"38dbf27c-8efb-e511-80d2-00155db07c77",
         "Account_Tasks":[],
         "Account_Tasks@odata.nextLink":"[Organization URI]/api/data/v9.1/accounts(38dbf27c-8efb-e511-80d2-00155db07c77)/Account_Tasks?$select%20=%20subject,%20scheduledstart"
      }
   ]
}
 
```  

<a bkmk="bkmk_retrieverelatedentitysingleandcollectionnavprop"></a>
  
## Retrieve related entities by expanding both single-valued and collection-valued navigation properties

The following example demonstrates how you can expand related entities for entity sets using both single- and collection-valued navigation properties. As explained earlier, expanding on collection-valued navigation properties to retrieve related entities for entity sets returns an `@odata.nextLink` property for the related entities. You should use the value of the `@odata.nextLink` property with a new `GET` request to return the required data.  
  
In this example, we are retrieving the contact and tasks assigned to the top 2 accounts.  
  
**Request**

```http 
GET [Organization URI]/api/data/v9.1/accounts?$top=2
&$select=name
&$expand=primarycontactid($select=contactid,fullname),
Account_Tasks($select=subject,scheduledstart)  HTTP/1.1  
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
   "value":
   [  
      {  
         "@odata.etag":"W/\"550614\"",
         "name":"Fourth Coffee (sample)",
         "accountid":"5b9648c3-68f7-e511-80d3-00155db53318",
         "primarycontactid":{  
            "contactid":"c19648c3-68f7-e511-80d3-00155db53318",
            "fullname":"Yvonne McKay (sample)"
         },
         "Account_Tasks":[],
         "Account_Tasks@odata.nextLink":"[Organization URI]/api/data/v9.1/accounts(5b9648c3-68f7-e511-80d3-00155db53318)/Account_Tasks?$select%20=%20subject,%20scheduledstart"
      },
      {  
         "@odata.etag":"W/\"550615\"",
         "name":"Litware, Inc. (sample)",
         "accountid":"5d9648c3-68f7-e511-80d3-00155db53318",
         "primarycontactid":{  
            "contactid":"c39648c3-68f7-e511-80d3-00155db53318",
            "fullname":"Susanna Stubberod (sample)"
         },
         "Account_Tasks":[],
         "Account_Tasks@odata.nextLink":"[Organization URI]/api/data/v9.1/accounts(5d9648c3-68f7-e511-80d3-00155db53318)/Account_Tasks?$select%20=%20subject,%20scheduledstart"
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
