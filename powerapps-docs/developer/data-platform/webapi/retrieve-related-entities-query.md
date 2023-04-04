---
title: "Retrieve related table records with a query (Microsoft Dataverse)| Microsoft Docs"
description: "Learn how you can retrieve related table records by expanding the navigation properties using the Web API."
ms.date: 03/30/2023
author: divkamath
ms.author: dikamath
ms.reviewer: jdaly
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors: 
  - JimDaly
---

# Retrieve related table records with a query

Use the `$expand` system query option with navigation properties to control what data is returned from related table records.

> [!NOTE]
>  - You are limited to no more than 15 `$expand` options in a query. This is to protect performance. Each `$expand` options creates a join that can impact performance. 
> - Queries which expand collection-valued navigation properties may return cached data for those properties that doesn't reflect recent changes. It is recommended to use `If-None-Match` header with value `null` to override browser caching. More information: [HTTP Headers](compose-http-requests-handle-errors.md#bkmk_headers) for more details.

You can apply the following system query options within certain `$expand` options:


|Option|Description|
|---------|---------|
|`$select`|Select which properties are returned. More information: [Limit columns with $select](#limit-columns-with-select)|
|`$filter`|For collection-valued navigation properties, limit the records returned. More information: [Filter results](query-data-web-api.md#filter-results)|
|`$orderby`|For collection-valued navigation properties, control the order of records returned. Not supported with nested `$expand`. More information: [Nested $expand on collection-valued navigation properties](#nested-expand-on-collection-valued-navigation-properties)|
|`$top`|For collection-valued navigation properties, limit the number of records returned. Not supported with nested `$expand`. More information: [Nested $expand on collection-valued navigation properties](#nested-expand-on-collection-valued-navigation-properties)|
|`$expand`|Expand navigation properties in the related entity set. Using `$expand` within an `$expand` is called a *nested `$expand`*. More information: [Nested expand of single-valued navigation properties](#nested-expand-of-single-valued-navigation-properties) & [Nested $expand on collection-valued navigation properties](#nested-expand-on-collection-valued-navigation-properties)|

These options are a subset of the system query options described in the **11.2.4.2.1 Expand Options** section of [OData Version 4.0 Part 1: Protocol Plus Errata 02](https://docs.oasis-open.org/odata/odata/v4.0/errata02/os/complete/part1-protocol/odata-v4.0-errata02-os-part1-protocol-complete.html#_Toc406398299). The options `$skip`, `$count`, `$search`, and `$levels` aren't supported for the Dataverse Web API.

Use these options with `$expand` by adding them in parentheses after the name of the navigation property. Separate each option with a semicolon. For example:

```http
/accounts?$select=name&$expand=Account_Tasks($select=subject;$filter=contains(subject,'Task');$orderby=createdon desc)
```
## Limit columns with $select

Always limit the columns returned using `$select` when you use `$expand`. For example, the following request returns the `contact.fullname` and `task.subject` values in the expanded results from the `account` entity type.

**Request**

```http
GET [Organization URI]/api/data/v9.2/accounts?$select=name
&$expand=primarycontactid($select=fullname),Account_Tasks($select=subject) HTTP/1.1
Prefer: odata.maxpagesize=1
If-None-Match: null
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
```

**Response**

```http
HTTP/1.1 200 OK
OData-Version: 4.0
Preference-Applied: odata.maxpagesize=1

{
    "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#accounts(name,primarycontactid(fullname),Account_Tasks(subject))",
    "value": [
        {
            "@odata.etag": "W/\"80649578\"",
            "name": "Litware, Inc. (sample)",
            "accountid": "78914942-34cb-ed11-b596-0022481d68cd",
            "primarycontactid": {
                "fullname": "Susanna Stubberod (sample)",
                "contactid": "70bf4d48-34cb-ed11-b596-0022481d68cd"
            },
            "Account_Tasks": [
                {
                    "@odata.etag": "W/\"80649460\"",
                    "subject": "Task 1 for Litware",
                    "_regardingobjectid_value": "78914942-34cb-ed11-b596-0022481d68cd",
                    "activityid": "f68393c1-34cb-ed11-b597-000d3a993550"
                }
            ],
            "Account_Tasks@odata.nextLink": "[Organization URI]/api/data/v9.2/accounts(78914942-34cb-ed11-b596-0022481d68cd)/Account_Tasks?$select=subject"
        }
    ],
    "@odata.nextLink": "[Organization URI]/api/data/v9.2/accounts?$select=name&$expand=primarycontactid($select=fullname),Account_Tasks($select=subject)&$skiptoken=%3Ccookie%20pagenumber=%222%22%20pagingcookie=%22%253ccookie%2520page%253d%25221%2522%253e%253caccountid%2520last%253d%2522%257b78914942-34CB-ED11-B596-0022481D68CD%257d%2522%2520first%253d%2522%257b78914942-34CB-ED11-B596-0022481D68CD%257d%2522%2520%252f%253e%253c%252fcookie%253e%22%20istracking=%22False%22%20/%3E"
}
```

## Navigation property type differences

It's important to remember there are two types of navigation properties. More information: [Web API Navigation Properties](web-api-navigation-properties.md)  
  
- *Single-valued* navigation properties correspond to lookup attributes that support many-to-one relationships and allow setting a reference to another record.  
  
- *Collection-valued* navigation properties correspond to one-to-many or many-to-many relationships.

Expanding a collection-valued navigation property can make the size of the response large in ways it is difficult to anticipate. It's important that you include limits to control how much data is returned. The `Prefer: odata.maxpagesize` request header is the most common way to limit the number of records returned, although you can also use `$top`. More information: [Specify the number of rows to return in a page](query-data-web-api.md#specify-the-number-of-rows-to-return-in-a-page)

> [!NOTE]
> There is a significant difference in how paging is applied to nested $expand options applied to collection valued navigation properties. More information: [Expand collection-valued navigation properties](#expand-collection-valued-navigation-properties)

## Expand single-valued navigation properties

The following example demonstrates how to retrieve contact records including the primary contact and the user who created the records.
  
**Request**  

```http 
GET [Organization URI]/api/data/v9.2/accounts?$select=name
&$expand=primarycontactid($select=contactid,fullname),createdby($select=fullname) HTTP/1.1  
Prefer: odata.maxpagesize=2
If-None-Match: null
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0
```  
  
**Response** 
 
```http 
HTTP/1.1 200 OK  
Content-Type: application/json; odata.metadata=minimal
Preference-Applied: odata.maxpagesize=2
OData-Version: 4.0  
  
{
    "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#accounts(name,primarycontactid(contactid,fullname),createdby(fullname))",
    "value": [
        {
            "@odata.etag": "W/\"80649578\"",
            "name": "Litware, Inc. (sample)",
            "accountid": "78914942-34cb-ed11-b596-0022481d68cd",
            "primarycontactid": {
                "contactid": "70bf4d48-34cb-ed11-b596-0022481d68cd",
                "fullname": "Susanna Stubberod (sample)"
            },
            "createdby": {
                "fullname": "System Administrator",
                "systemuserid": "4026be43-6b69-e111-8f65-78e7d1620f5e",
                "ownerid": "4026be43-6b69-e111-8f65-78e7d1620f5e"
            }
        },
        {
            "@odata.etag": "W/\"80649580\"",
            "name": "Adventure Works (sample)",
            "accountid": "7a914942-34cb-ed11-b596-0022481d68cd",
            "primarycontactid": {
                "contactid": "72bf4d48-34cb-ed11-b596-0022481d68cd",
                "fullname": "Nancy Anderson (sample)"
            },
            "createdby": {
                "fullname": "System Administrator",
                "systemuserid": "4026be43-6b69-e111-8f65-78e7d1620f5e",
                "ownerid": "4026be43-6b69-e111-8f65-78e7d1620f5e"
            }
        }
    ],
    "@odata.nextLink": "[Organization URI]/api/data/v9.2/accounts?$select=name%0A&$expand=primarycontactid($select=contactid,fullname),createdby($select=fullname)&$skiptoken=%3Ccookie%20pagenumber=%222%22%20pagingcookie=%22%253ccookie%2520page%253d%25221%2522%253e%253caccountid%2520last%253d%2522%257b7A914942-34CB-ED11-B596-0022481D68CD%257d%2522%2520first%253d%2522%257b78914942-34CB-ED11-B596-0022481D68CD%257d%2522%2520%252f%253e%253c%252fcookie%253e%22%20istracking=%22False%22%20/%3E"
}
```  

### Return references

Instead of returning data, you can also return references (links) to the related records by expanding the single-valued navigation property with the `/$ref` option. The following example returns JSON objects with an `@odata.id` property that has a URL for each primary contact.
  
 **Request**

```http  
GET [Organization URI]/api/data/v9.2/accounts?$select=name
&$expand=primarycontactid/$ref HTTP/1.1  
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
```  
  
 **Response**
 
```http 
HTTP/1.1 200 OK  
Content-Type: application/json; odata.metadata=minimal
Preference-Applied: odata.maxpagesize=2
OData-Version: 4.0  
  
{
    "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#accounts(name,primarycontactid,primarycontactid/$ref())",
    "value": [
        {
            "@odata.etag": "W/\"80649578\"",
            "name": "Litware, Inc. (sample)",
            "_primarycontactid_value": "70bf4d48-34cb-ed11-b596-0022481d68cd",
            "accountid": "78914942-34cb-ed11-b596-0022481d68cd",
            "primarycontactid": {
                "@odata.id": "[Organization URI]/api/data/v9.2/contacts(70bf4d48-34cb-ed11-b596-0022481d68cd)"
            }
        },
        {
            "@odata.etag": "W/\"80649580\"",
            "name": "Adventure Works (sample)",
            "_primarycontactid_value": "72bf4d48-34cb-ed11-b596-0022481d68cd",
            "accountid": "7a914942-34cb-ed11-b596-0022481d68cd",
            "primarycontactid": {
                "@odata.id": "[Organization URI]/api/data/v9.2/contacts(72bf4d48-34cb-ed11-b596-0022481d68cd)"
            }
        }
    ],
    "@odata.nextLink": "[Organization URI]/api/data/v9.2/accounts?$select=name%0A&$expand=primarycontactid/$ref&$skiptoken=%3Ccookie%20pagenumber=%222%22%20pagingcookie=%22%253ccookie%2520page%253d%25221%2522%253e%253caccountid%2520last%253d%2522%257b7A914942-34CB-ED11-B596-0022481D68CD%257d%2522%2520first%253d%2522%257b78914942-34CB-ED11-B596-0022481D68CD%257d%2522%2520%252f%253e%253c%252fcookie%253e%22%20istracking=%22False%22%20/%3E"
}
```

You can only use the `/$ref` option with single-valued navigation properties. If you use it with a collection-valued navigation property, you get the following error:

```json
{
    "error": {
        "code": "0x80060888",
        "message": "Expand with $ref is only supported on lookup type navigation property."
    }
}
```

## Nested expand of single-valued navigation properties

You can expand single-valued navigation properties to multiple levels by nesting an `$expand` option within another `$expand` option.

The following query returns `task` records and expands the related `contact`, the `account` related to the `contact`, and finally to the `systemuser` who created the  `account` record.

**Request**

```http
GET [Organization URI]/api/data/v9.2/tasks?$select=subject
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
Preference-Applied: odata.maxpagesize=2
OData-Version: 4.0 

{
    "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#tasks(subject,regardingobjectid_contact_task(fullname,parentcustomerid_account(name,createdby(fullname))))",
    "value": [
        {
            "@odata.etag": "W/\"80730855\"",
            "subject": "Task 1 for Susanna Stubberod",
            "activityid": "e9a8c72c-dbcc-ed11-b597-000d3a993550",
            "regardingobjectid_contact_task": {
                "fullname": "Susanna Stubberod (sample)",
                "contactid": "70bf4d48-34cb-ed11-b596-0022481d68cd",
                "parentcustomerid_account": {
                    "name": "Litware, Inc. (sample)",
                    "accountid": "78914942-34cb-ed11-b596-0022481d68cd",
                    "createdby": {
                        "fullname": "System Administrator",
                        "systemuserid": "4026be43-6b69-e111-8f65-78e7d1620f5e",
                        "ownerid": "4026be43-6b69-e111-8f65-78e7d1620f5e"
                    }
                }
            }
        },
        {
            "@odata.etag": "W/\"80730861\"",
            "subject": "Task 2 for Susanna Stubberod",
            "activityid": "c206f534-dbcc-ed11-b597-000d3a993550",
            "regardingobjectid_contact_task": {
                "fullname": "Susanna Stubberod (sample)",
                "contactid": "70bf4d48-34cb-ed11-b596-0022481d68cd",
                "parentcustomerid_account": {
                    "name": "Litware, Inc. (sample)",
                    "accountid": "78914942-34cb-ed11-b596-0022481d68cd",
                    "createdby": {
                        "fullname": "System Administrator",
                        "systemuserid": "4026be43-6b69-e111-8f65-78e7d1620f5e",
                        "ownerid": "4026be43-6b69-e111-8f65-78e7d1620f5e"
                    }
                }
            }
        }
    ],
    "@odata.nextLink": "[Organization URI]/api/data/v9.2/tasks?$select=subject&$expand=regardingobjectid_contact_task($select=fullname;$expand=parentcustomerid_account($select=name;$expand=createdby($select=fullname)))&$skiptoken=%3Ccookie%20pagenumber=%222%22%20pagingcookie=%22%253ccookie%2520page%253d%25221%2522%253e%253cactivityid%2520last%253d%2522%257bC206F534-DBCC-ED11-B597-000D3A993550%257d%2522%2520first%253d%2522%257bE9A8C72C-DBCC-ED11-B597-000D3A993550%257d%2522%2520%252f%253e%253c%252fcookie%253e%22%20istracking=%22False%22%20/%3E"
}
```

## Expand collection-valued navigation properties

There are some important differences in the response that depend on whether you use nested `$expand` with a collection-valued navigation property anywhere in your query.

||Nested $expand|Single $expand|
|---------|---------|---------|
|**Paging**|Paging on expanded rows.|Paging only on resource entityset. `<property name>@odata.nextLink` URLs for expanded rows don't include paging information.|
|**`$top` or `$orderby` supported**|No|Yes|

### Single $expand on collection-valued navigation properties

If you use only single `$expand`, there's no paging applied to the expanded rows. If you include the `Prefer: odata.maxpagesize` request header, paging is only applied to the entityset resource of the query.

Each expanded collection-valued navigation property returns a `<property>@odata.nextLink` URL that includes no paging information. It's a URL that takes you to the collection filtered by the relationship. You can use that URL to send a separate `GET` request and it returns the same rows that were returned in your original request. You can apply paging to that request.

Because no paging is applied to the expanded records, up to 5000 related records can be returned. You can use `$top`, `$filter`, and `$orderby` options to control the total number of records returned.

The following example includes single expand of the `Account_Tasks` and `contact_customer_accounts` while retrieving account records. The `Prefer: odata.maxpagesize=1` request header ensures that only one account record is returned in with the first page.

**Request**

```http
GET [Organization URI]/api/data/v9.2/accounts?$select=name,accountid
&$expand=Account_Tasks($select=subject),contact_customer_accounts($select=fullname) HTTP/1.1
Prefer: odata.maxpagesize=1
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
```

**Response**

```http
HTTP/1.1 200 OK  
Content-Type: application/json; odata.metadata=minimal
Preference-Applied: odata.maxpagesize=1
OData-Version: 4.0 

{
    "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#accounts(name,accountid,Account_Tasks(subject),contact_customer_accounts(fullname))",
    "value": [
        {
            "@odata.etag": "W/\"80649578\"",
            "name": "Litware, Inc. (sample)",
            "accountid": "78914942-34cb-ed11-b596-0022481d68cd",
            "Account_Tasks": [
                {
                    "@odata.etag": "W/\"80730894\"",
                    "subject": "Task 1 for Litware",
                    "_regardingobjectid_value": "78914942-34cb-ed11-b596-0022481d68cd",
                    "activityid": "be9f6557-e2cc-ed11-b597-000d3a993550"
                },
                {
                    "@odata.etag": "W/\"80730903\"",
                    "subject": "Task 2 for Litware",
                    "_regardingobjectid_value": "78914942-34cb-ed11-b596-0022481d68cd",
                    "activityid": "605dbd65-e2cc-ed11-b597-000d3a993550"
                },
                {
                    "@odata.etag": "W/\"80730909\"",
                    "subject": "Task 3 for Litware",
                    "_regardingobjectid_value": "78914942-34cb-ed11-b596-0022481d68cd",
                    "activityid": "a718856c-e2cc-ed11-b597-000d3a993550"
                }
            ],
            "Account_Tasks@odata.nextLink": "[Organization URI]/api/data/v9.2/accounts(78914942-34cb-ed11-b596-0022481d68cd)/Account_Tasks?$select=subject",
            "contact_customer_accounts": [
                {
                    "@odata.etag": "W/\"80648695\"",
                    "fullname": "Susanna Stubberod (sample)",
                    "_parentcustomerid_value": "78914942-34cb-ed11-b596-0022481d68cd",
                    "contactid": "70bf4d48-34cb-ed11-b596-0022481d68cd"
                }
            ],
            "contact_customer_accounts@odata.nextLink": "[Organization URI]/api/data/v9.2/accounts(78914942-34cb-ed11-b596-0022481d68cd)/contact_customer_accounts?$select=fullname"
        }
    ],
    "@odata.nextLink": "[Organization URI]/api/data/v9.2/accounts?$select=name,accountid&$expand=Account_Tasks($select=subject),contact_customer_accounts($select=fullname)&$skiptoken=%3Ccookie%20pagenumber=%222%22%20pagingcookie=%22%253ccookie%2520page%253d%25221%2522%253e%253caccountid%2520last%253d%2522%257b7A914942-34CB-ED11-B596-0022481D68CD%257d%2522%2520first%253d%2522%257b78914942-34CB-ED11-B596-0022481D68CD%257d%2522%2520%252f%253e%253c%252fcookie%253e%22%20istracking=%22False%22%20/%3E"
}
```

> [!NOTE]
> Compare this response to the following example that includes a nested `$expand`.
> 
> You need to scroll the example response horizontally to see that only the `@odata.nextLink` URL for the account result contains paging information.


### Nested $expand on collection-valued navigation properties

If you use a nested `$expand` anywhere in your query, and you've included the `Prefer: odata.maxpagesize` request header, paging is applied to each of the expanded collections.

Each expanded collection-valued navigation property returns a `<property>@odata.nextLink` URL that includes paging information. You can use that URL to send a separate `GET` request and it will return the next set of records that weren't included in your original request.

You can't use `$top` or `$orderby` options to limit the total number of records returned with a nested `$expand`. The following error is returned if you use these options:

```json
{
    "error": {
        "code": "0x80060888",
        "message": "Only $select and $filter clause can be provided while doing $expand on many-to-one relationship or nested one-to-many relationship."
    }
}
```

This example is based on the previous example and uses the same data. The only difference in the URL is the addition of this nested `$expand` on a single-valued navigation property to return the owning user of the contact: `;$expand=owninguser($select=fullname)`.

**Request**

```http
GET [Organization URI]/api/data/v9.2/accounts?$select=name,accountid
&$expand=Account_Tasks($select=subject),contact_customer_accounts($select=fullname;
$expand=owninguser($select=fullname)) HTTP/1.1
Prefer: odata.maxpagesize=1
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
```

**Response**

```http
HTTP/1.1 200 OK  
Content-Type: application/json; odata.metadata=minimal
Preference-Applied: odata.maxpagesize=1
OData-Version: 4.0 

{
    "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#accounts(name,accountid,Account_Tasks(subject),contact_customer_accounts(fullname,owninguser(fullname)))",
    "value": [
        {
            "@odata.etag": "W/\"80649578\"",
            "name": "Litware, Inc. (sample)",
            "accountid": "78914942-34cb-ed11-b596-0022481d68cd",
            "Account_Tasks": [
                {
                    "subject": "Task 1 for Litware",
                    "activityid": "be9f6557-e2cc-ed11-b597-000d3a993550"
                }
            ],
            "Account_Tasks@odata.nextLink": "[Organization URI]/api/data/v9.2/accounts(78914942-34cb-ed11-b596-0022481d68cd)/Account_Tasks?$select=subject,description&$skiptoken=%3Ccookie%20pagenumber=%222%22%20pagingcookie=%22%253ccookie%2520page%253d%25221%2522%2520countOfRecords%253d%25221%2522%253e%253cactivityid%2520last%253d%2522%257bbe9f6557-e2cc-ed11-b597-000d3a993550%257d%2522%2520first%253d%2522%257bbe9f6557-e2cc-ed11-b597-000d3a993550%257d%2522%2520%252f%253e%253c%252fcookie%253e%22%20istracking=%22False%22%20/%3E",
            "contact_customer_accounts": [
                {
                    "fullname": "Susanna Stubberod (sample)",
                    "contactid": "70bf4d48-34cb-ed11-b596-0022481d68cd",
                    "owninguser": {
                        "fullname": "System Administrator",
                        "systemuserid": "4026be43-6b69-e111-8f65-78e7d1620f5e",
                        "ownerid": "4026be43-6b69-e111-8f65-78e7d1620f5e"
                    }
                }
            ],
            "contact_customer_accounts@odata.nextLink": "[Organization URI]/api/data/v9.2/accounts(78914942-34cb-ed11-b596-0022481d68cd)/contact_customer_accounts?$select=fullname&$expand=owninguser($select=fullname)&$skiptoken=%3Ccookie%20pagenumber=%222%22%20pagingcookie=%22%253ccookie%2520page%253d%25221%2522%2520countOfRecords%253d%25221%2522%253e%253ccontactid%2520last%253d%2522%257b70bf4d48-34cb-ed11-b596-0022481d68cd%257d%2522%2520first%253d%2522%257b70bf4d48-34cb-ed11-b596-0022481d68cd%257d%2522%2520%252f%253e%253c%252fcookie%253e%22%20istracking=%22False%22%20/%3E"
        }
    ],
    "@odata.nextLink": "[Organization URI]/api/data/v9.2/accounts?$select=name,accountid&$expand=Account_Tasks($select=subject,description),contact_customer_accounts($select=fullname;$expand=owninguser($select=fullname))&$skiptoken=%3Ccookie%20pagenumber=%222%22%20pagingcookie=%22%253ccookie%2520page%253d%25221%2522%2520countOfRecords%253d%25221%2522%253e%253caccountid%2520last%253d%2522%257b78914942-34cb-ed11-b596-0022481d68cd%257d%2522%2520first%253d%2522%257b78914942-34cb-ed11-b596-0022481d68cd%257d%2522%2520%252f%253e%253c%252fcookie%253e%22%20istracking=%22False%22%20/%3E"
}
```

> [!NOTE]
> Compare this response to the previous example that doesn't use nested `$expand`.
> 
> In this response, the `Prefer: odata.maxpagesize=1` request header is applied to the `task` records returned with `Account_Tasks`. Only one task is returned instead of three. The `Account_Tasks@odata.nextLink` URL will return the next two tasks.
>
> You need to scroll the example response horizontally to see that `Account_Tasks@odata.nextLink`, `contact_customer_accounts@odata.nextLink`, and  `@odata.nextLink` URLs contain paging information.


## See also

[Query data using Web API](query-data-web-api.md)<br />
[Retrieve a table row using the Web API](retrieve-entity-using-web-api.md)<br />
[Web API Query Data sample (C#)](samples/webapiservice-query-data.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]