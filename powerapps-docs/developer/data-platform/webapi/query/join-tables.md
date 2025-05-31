---
title: Join tables using OData
description: Learn how to use OData to join tables when you retrieve data from Microsoft Dataverse Web API.
ms.date: 10/30/2024
ms.topic: how-to
author: MsSQLGirl
ms.author: jukoesma
ms.reviewer: jdaly
ms.subservice: dataverse-developer
search.audienceType: 
  - developer
contributors: 
  - JimDaly
  - JosinaJoy
  - legunter
---
# Join tables using OData

To control what data is returned from related table records, use the `$expand` [query option](overview.md#odata-query-options) with navigation properties.

- You can include up to 15 `$expand` options in a query. Each `$expand` option creates a join that can affect performance.
- Queries which expand collection-valued navigation properties might return cached data for those properties that doesn't reflect recent changes. It's recommended to use `If-None-Match` header with value `null` to override browser caching. [Learn more about using HTTP Headers](../compose-http-requests-handle-errors.md#bkmk_headers) for more details.

The following table describes the [query options](overview.md#odata-query-options) you can apply in certain `$expand` options:


|Option|Description|More information|
|---------|---------|---------|
|`$select`|Select which properties are returned.|[Select columns](select-columns.md)|
|`$filter`|For collection-valued navigation properties, limit the records returned. |[Filter rows](filter-rows.md)|
|`$orderby`|For collection-valued navigation properties, control the order of records returned. Not supported with nested `$expand`. |[Nested $expand on collection-valued navigation properties](#nested-expand-on-collection-valued-navigation-properties)|
|`$top`|For collection-valued navigation properties, limit the number of records returned. Not supported with nested `$expand`. |[Nested $expand on collection-valued navigation properties](#nested-expand-on-collection-valued-navigation-properties)|
|`$expand`|Expand navigation properties in the related entity set. Using `$expand` in an `$expand` is called a *nested `$expand`*. |[Nested expand of single-valued navigation properties](#nested-expand-of-single-valued-navigation-properties) and [Nested $expand on collection-valued navigation properties](#nested-expand-on-collection-valued-navigation-properties)|

These options are a subset of the query options described in [OData Version 4.0 Part 1: Protocol Plus Errata 02 11.2.4.2.1 Expand Options](https://docs.oasis-open.org/odata/odata/v4.0/errata02/os/complete/part1-protocol/odata-v4.0-errata02-os-part1-protocol-complete.html#_Toc406398299). The options `$skip`, `$count`, `$search`, and `$levels` aren't supported for the Dataverse Web API.

Use these options with `$expand` by adding them in parentheses after the name of the navigation property. Separate each option with a semicolon (;).

For example, the following query:

- Requests the `account.name` property
- Joins the `AccountTasks` collection-valued navigation property requesting:

  - The `task.subject` property
  - Where the `task.subject` contains the string "`Task`"
  - Ordered by the `task.createdon` date, descending

```http
/accounts?$select=name&$expand=Account_Tasks($select=subject;$filter=contains(subject,'Task');$orderby=createdon desc)
```

## Limit columns with $select

As with any query, always limit the columns returned using `$select` when you use `$expand`. For example, the following request returns the `contact.fullname` and `task.subject` values in the expanded results from the `account` entity type:

**Request:**

```http
GET [Organization URI]/api/data/v9.2/accounts?$select=name
&$expand=primarycontactid($select=fullname),Account_Tasks($select=subject)
Prefer: odata.maxpagesize=1
If-None-Match: null
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
```

**Response:**

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

It's important to remember there are two types of navigation properties. [Learn more about Web API Navigation Properties](../web-api-navigation-properties.md)  
  
- *Single-valued* navigation properties correspond to lookup attributes that support many-to-one relationships and allow setting a reference to another record.  
  
- *Collection-valued* navigation properties correspond to one-to-many or many-to-many relationships.

Expanding a collection-valued navigation property can make the size of the response large in ways it's difficult to anticipate. It's important that you include limits to control how much data is returned. You can limit the number of records by using paging. [Learn more about paging results](page-results.md)

There's a significant difference in how paging is applied to nested $expand options applied to collection valued navigation properties. [Learn more about expanding collection-valued navigation properties](#expand-collection-valued-navigation-properties)

## Expand single-valued navigation properties

The following example demonstrates how to retrieve contact records including the primary contact and the user who created the records.
  
**Request:**  

```http 
GET [Organization URI]/api/data/v9.2/accounts?$select=name
&$expand=primarycontactid($select=contactid,fullname),createdby($select=fullname)  
Prefer: odata.maxpagesize=2
If-None-Match: null
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0
```  
  
**Response:** 
 
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

The `createdby` single-valued navigation property returns an instance of the [systemuser EntityType](xref:Microsoft.Dynamics.CRM.systemuser). Both `systemuserid` and `ownerid` properties are returned. This is because `systemuser` inherits from [principal EntityType](xref:Microsoft.Dynamics.CRM.principal) and shares the `ownerid` primary key with [team EntityType](xref:Microsoft.Dynamics.CRM.team) through this inheritance.

However, the [User (SystemUser) table](../../reference/entities/systemuser.md) has the primary key of [SystemUserId](../../reference/entities/systemuser.md#BKMK_SystemUserId). Both `systemuserid` and `ownerid` properties have the same value. [Learn more about EntityType inheritance](../web-api-entitytypes.md#entitytype-inheritance)

### Return references

Instead of returning data, you can also return references, or links, to the related records by expanding the single-valued navigation property with the `/$ref` option. The following example returns JSON objects with an `@odata.id` property that has a URL for each primary contact.
  
 **Request:**

```http  
GET [Organization URI]/api/data/v9.2/accounts?$select=name
&$expand=primarycontactid/$ref  
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
```  
  
 **Response:**
 
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

You can expand single-valued navigation properties to multiple levels by nesting an `$expand` option in another `$expand` option.

The following query returns `task` records and expands the related `contact`, the `account` related to the `contact`, and the `systemuser` who created the`account` record:

**Request:**

```http
GET [Organization URI]/api/data/v9.2/tasks?$select=subject
&$expand=regardingobjectid_contact_task($select=fullname;
 $expand=parentcustomerid_account($select=name;
  $expand=createdby($select=fullname)))  
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
Prefer: odata.maxpagesize=2
```

**Response:**

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
|**Paging**|Paging on expanded rows.|Paging only on [EntitySet resource](overview.md#entityset-resources). `<property name>@odata.nextLink` URLs for expanded rows don't include paging information.|
|**`$top` or `$orderby` supported**|No|Yes|
|**N:N Relationships supported**|No. See [Nested $expand with N:N relationships](#nested-expand-with-nn-relationships)|Yes|

### Single $expand on collection-valued navigation properties

If you use only single-level `$expand`, no paging is applied to the expanded rows. If you include the `Prefer: odata.maxpagesize` request header, paging is only applied to the EntitySet resource of the query.

Each expanded collection-valued navigation property returns a `<property>@odata.nextLink` URL that includes no paging information. It's a URL that represents the [filtered collection](overview.md#filtered-collections) for the relationship with your query options appended. You can use that URL to send a separate `GET` request and it returns the same rows that were returned in your original request. You can apply paging to that request.

Because no paging is applied to the expanded records, up to 5,000 related table records can be returned for each expanded collection-valued navigation property. Depending on your data and the query, it could be a lot of data. Returning that much data could affect performance and possibly cause your request to time out. Be cautious about the queries you compose. You can use `$top`, `$filter`, and `$orderby` options to control the total number of records returned.

The following example includes a single expand of the `Account_Tasks` and `contact_customer_accounts` while retrieving account records. The `Prefer: odata.maxpagesize=1` request header ensures that only one account record is returned in the first page.

**Request:**

```http
GET [Organization URI]/api/data/v9.2/accounts?$select=name,accountid
&$expand=Account_Tasks($select=subject),contact_customer_accounts($select=fullname)
Prefer: odata.maxpagesize=1
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
```

**Response:**

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

Compare this response with the following example, which includes a nested `$expand`. Scroll the example response horizontally to see that only the `@odata.nextLink` URL for the account result contains paging information.


### Nested $expand on collection-valued navigation properties

If you use a nested `$expand` anywhere in your query, and you include the `Prefer: odata.maxpagesize` request header, paging is applied to each of the expanded collections.

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

The following example is based on the previous example and uses the same data. The only difference is the addition in the URL of this nested `$expand` on a single-valued navigation property to return the owning user of the contact: `;$expand=owninguser($select=fullname)`.

**Request:**

```http
GET [Organization URI]/api/data/v9.2/accounts?$select=name,accountid
&$expand=Account_Tasks($select=subject),contact_customer_accounts($select=fullname;
$expand=owninguser($select=fullname))
Prefer: odata.maxpagesize=1
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
```

**Response:**

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

Compare this response with the previous example, which doesn't use a nested `$expand`. In this response:

- The `Prefer: odata.maxpagesize=1` request header is applied to the `task` records returned with `Account_Tasks`. 
- Only one task is returned instead of three.
- The `Account_Tasks@odata.nextLink` URL returns the next two tasks. 
- Scroll the example response horizontally to see that `Account_Tasks@odata.nextLink`, `contact_customer_accounts@odata.nextLink`, and`@odata.nextLink` URLs contain paging information.

### Nested $expand with N:N relationships

When a collection-valued navigation property represents an N:N relationship, you'll get the following error when you use nested `$expand` statements:

```json
{
   "error": {
      "code": "0x80060888",
      "message": "The navigation property '<NAME>' cannot be expanded. Only many-to-one relationships are supported for nested expansion."
   }
}
```

For example, using the Dynamics Lead table, which has a `contactleads_association` N:N relationship with the [contact table](../../reference/entities/contact.md), the following query returns the error because it includes `;$expand=createdby`.

```http
GET [Organization URI]/contacts?$select=fullname$expand=contactleads_association($select=fullname;$expand=createdby)
```

To avoid this error, you can construct the query [using FetchXml](../../fetchxml/join-tables.md). For example:

```xml
<fetch>
  <entity name='contact'>
    <attribute name='fullname' />
    <link-entity name='contactleads' 
      from='contactid' 
      to='contactid' 
      alias='cl'>
      <link-entity name='lead' 
         from='leadid' 
         to='leadid' 
         alias='lead'>
        <attribute name='fullname' />
        <link-entity name='systemuser' 
           from='systemuserid' 
           to='createdby' 
           alias='systemuser'>
          <attribute name='fullname' />
        </link-entity>
      </link-entity>
    </link-entity>
  </entity>
</fetch>
```

[Learn more about joining tables using many-to-many relationships with FetchXml](../../fetchxml/join-tables.md#many-to-many-relationships)

## Next steps

Learn how to order rows.

> [!div class="nextstepaction"]
> [Order rows](order-rows.md)

[!INCLUDE [footer-banner](../../../../includes/footer-banner.md)]
