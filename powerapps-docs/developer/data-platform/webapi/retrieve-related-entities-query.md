---
title: "Retrieve related table records with a query (Microsoft Dataverse)| Microsoft Docs"
description: "Read how you can retrieve related table records by expanding the navigation properties."
ms.custom: ""
ms.date: 04/29/2021
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
ms.assetid: 3D8FB9AF-3663-437A-988E-CBAE9579F167
caps.latest.revision: 78
author: "JimDaly"
ms.author: "pehecke"
manager: "ryjones"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Retrieve related table records with a query

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

Use the `$expand` system query option in the navigation properties to control what data from related entities is returned. There are two types of navigation properties:  
  
- *Single-valued* navigation properties correspond to Lookup attributes that support many-to-one relationships and allow setting a reference to another entity.  
  
- *Collection-valued* navigation properties correspond to one-to-many or many-to-many relationships.  
  
If you include only the name of the navigation property, you’ll receive all the properties for related records. You can limit the properties returned for related records using the `$select` system query option in parentheses after the navigation property name. Use this for both single-valued and collection-valued navigation properties.  

> [!NOTE]
>  - You are limited to no more than 10 `$expand` options in a query. This is to protect performance. Each `$expand` options creates a join that can impact performance. 
>  - To retrieve related entities for an entity instance, see [Retrieve related tables for a table by expanding navigation properties](retrieve-entity-using-web-api.md#bkmk_expandRelated). 
> - Queries which expand collection-valued navigation properties may return cached data for those properties that doesn’t reflect recent changes. It is recommended to use `If-None-Match` header with value `null` to override browser caching. See [HTTP Headers](compose-http-requests-handle-errors.md#bkmk_headers) for more details.
> 

<a bkmk="bkmk_retrieverelatedentityexpandsinglenavprop"></a>

## Retrieve related table records by expanding single-valued navigation properties

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

## Retrieve related tables by expanding collection-valued navigation properties

If you expand on collection-valued navigation parameters to retrieve related entities for entity sets, only one level of depth is returned if there is data. Otherwise the collection will return an empty array.

In either case an `@odata.nextLink` property will be returned for the related entities. If you want to retrieve the collection separately, you can use the value of the `@odata.nextLink` property with a new `GET` request to return the required data.  

The following example retrieves the tasks assigned to the top 2 account records.  One has related tasks, the other does not.
  
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
    "@odata.context": "[Organization URI]/api/data/v9.1/$metadata#accounts(name,Account_Tasks(subject,scheduledstart))",
    "value": [
        {
            "@odata.etag": "W/\"37867294\"",
            "name": "Contoso, Ltd. (sample)",
            "accountid": "7a4814f9-b0b8-ea11-a812-000d3a122b89",
            "Account_Tasks": [
                {
                    "@odata.etag": "W/\"28876919\"",
                    "subject": "Task 1 for Contoso, Ltd.",
                    "scheduledstart": null,
                    "_regardingobjectid_value": "7a4814f9-b0b8-ea11-a812-000d3a122b89",
                    "activityid": "7b4814f9-b0b8-ea11-a812-000d3a122b89"
                },
                {
                    "@odata.etag": "W/\"28876923\"",
                    "subject": "Task 2 for Contoso, Ltd.",
                    "scheduledstart": null,
                    "_regardingobjectid_value": "7a4814f9-b0b8-ea11-a812-000d3a122b89",
                    "activityid": "7c4814f9-b0b8-ea11-a812-000d3a122b89"
                },
                {
                    "@odata.etag": "W/\"28876927\"",
                    "subject": "Task 3 for Contoso, Ltd.",
                    "scheduledstart": null,
                    "_regardingobjectid_value": "7a4814f9-b0b8-ea11-a812-000d3a122b89",
                    "activityid": "7d4814f9-b0b8-ea11-a812-000d3a122b89"
                }
            ],
            "Account_Tasks@odata.nextLink": "[Organization URI]/api/data/v9.1/accounts(7a4814f9-b0b8-ea11-a812-000d3a122b89)/Account_Tasks?$select=subject,scheduledstart"
        },
        {
            "@odata.etag": "W/\"37526208\"",
            "name": "Fourth Coffee",
            "accountid": "ccd685f9-cddd-ea11-a813-000d3a122b89",
            "Account_Tasks": [],
            "Account_Tasks@odata.nextLink": "[Organization URI]/api/data/v9.1/accounts(ccd685f9-cddd-ea11-a813-000d3a122b89)/Account_Tasks?$select=subject,scheduledstart"
        }
    ]
}
 
```  

<a bkmk="bkmk_retrieverelatedentitysingleandcollectionnavprop"></a>
  
## Retrieve related tables by expanding both single-valued and collection-valued navigation properties

The following example demonstrates how you can expand related entities for entity sets using both single and collection-valued navigation properties. As explained earlier, expanding on collection-valued navigation properties to retrieve related entities for entity sets returns one level of depth and an `@odata.nextLink` property for the related entities.  
  
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
    "@odata.context": "[Organization URI]/api/data/v9.1/$metadata#accounts(name,primarycontactid(contactid,fullname),Account_Tasks(subject,scheduledstart))",
    "value": [
        {
            "@odata.etag": "W/\"37867294\"",
            "name": "Contoso, Ltd. (sample)",
            "accountid": "7a4814f9-b0b8-ea11-a812-000d3a122b89",
            "primarycontactid": {
                "contactid": "7e4814f9-b0b8-ea11-a812-000d3a122b89",
                "fullname": "Yvonne McKay (sample)"
            },
            "Account_Tasks": [
                {
                    "@odata.etag": "W/\"28876919\"",
                    "subject": "Task 1 for Contoso, Ltd.",
                    "scheduledstart": null,
                    "_regardingobjectid_value": "7a4814f9-b0b8-ea11-a812-000d3a122b89",
                    "activityid": "7b4814f9-b0b8-ea11-a812-000d3a122b89"
                },
                {
                    "@odata.etag": "W/\"28876923\"",
                    "subject": "Task 2 for Contoso, Ltd.",
                    "scheduledstart": null,
                    "_regardingobjectid_value": "7a4814f9-b0b8-ea11-a812-000d3a122b89",
                    "activityid": "7c4814f9-b0b8-ea11-a812-000d3a122b89"
                },
                {
                    "@odata.etag": "W/\"28876927\"",
                    "subject": "Task 3 for Contoso, Ltd.",
                    "scheduledstart": null,
                    "_regardingobjectid_value": "7a4814f9-b0b8-ea11-a812-000d3a122b89",
                    "activityid": "7d4814f9-b0b8-ea11-a812-000d3a122b89"
                }
            ],
            "Account_Tasks@odata.nextLink": "[Organization URI]/api/data/v9.1/accounts(7a4814f9-b0b8-ea11-a812-000d3a122b89)/Account_Tasks?$select=subject,scheduledstart"
        },
        {
            "@odata.etag": "W/\"37526208\"",
            "name": "Fourth Coffee",
            "accountid": "ccd685f9-cddd-ea11-a813-000d3a122b89",
            "primarycontactid": {
                "contactid": "384d0f84-7de6-ea11-a817-000d3a122b89",
                "fullname": "Charlie Brown"
            },
            "Account_Tasks": [],
            "Account_Tasks@odata.nextLink": "[Organization URI]/api/data/v9.1/accounts(ccd685f9-cddd-ea11-a813-000d3a122b89)/Account_Tasks?$select=subject,scheduledstart"
        }
    ]
}
```

## Filter collection values based on data in related tables

The Web API allows you to use two lambda operators, which are `any` and `all` to evaluate a Boolean expression on a collection. More information: [Use Lambda operators](query-data-web-api.md#bkmk_LambdaOperators).

## See also

[Search across table data using relevance search](relevance-search.md)  
[Query data using Web API](query-data-web-api.md)<br />
[Perform operations using the Web API](perform-operations-web-api.md)<br />
[Compose Http requests and handle errors](compose-http-requests-handle-errors.md)<br />
[Create a table using the Web API](create-entity-web-api.md)<br />
[Retrieve a table using the Web API](retrieve-entity-using-web-api.md)<br />
[Update and delete tables using the Web API](update-delete-entities-using-web-api.md)<br />
[Associate and disassociate tables using the Web API](associate-disassociate-entities-using-web-api.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]