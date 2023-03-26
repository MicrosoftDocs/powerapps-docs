---
title: "Multi-level $expand with collection-valued navigation properties (Microsoft Dataverse)| Microsoft Docs"
description: "Learn how to expand collection-valued navigation properties more than a single level of depth."
ms.date: 03/25/2022
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

# Multi-level $expand with collection-valued navigation properties

You can retrieve results with deeper hierarchy by including multi-level nested `$expand` system query option with your query. Using these with single-valued navigation properties is relatively straightforward. More information: 

Collection-valued navigation properties represent a 1:N or N:N relationship. Use `$expand` to add related rows to the results of your query.

You can use a single level `$expand`: `systemusers?$select=fullname&$expand=user_accounts($select=name)`

Or you can use a nested `$expand`: `systemusers?$select=fullname&$expand=user_accounts($select=name;$expand=Account_Tasks($select=subject))`

## Limited options

`$orderby` and `$top` not supported


## Differences in paging behaviors

When you use multi-level `$expand` with a collection-valued navigation property, the shape of the results is different than when you use only a single `$expand`.

Depending on your data and your query, expanding collection-valued navigation properties can significantly increase the amount of data returned. With multi-level expansions of collection-valued navigation properties, it is important that you apply bounds to the results returned, and this is typically done using paging with the `Prefer: odata.maxpagesize` request header.

It is important to note that `odata.maxpagesize` is a preference. Dataverse will attempt to apply the preference but may return a different number of pages or interpret as needed.

When you use paging on a query with more than one level of `$expand`, the `odata.maxpagesize` preference is applied to each collection that is returned. Any `@odata.nextLink` URLs returned with these expanded collections include paging data to skip the records already returned.

When you use only one level of expand, paging only applies to the base entityset resource returned by the query. No paging is applied to expanded collections. Each expanded collection can return up to 5000 records.  Any `@odata.nextLink` URLs returned with these expanded collections return the entire collection, without skipping those records already returned.

The following examples all use the same data, which can be represented this way:

```
systemuser(4026be43-6b69-e111-8f65-78e7d1620f5e): FirstName LastName
    - user_accounts:
        - account: Litware, Inc.
            - Account_Tasks:
                - task: Task 1 for Litware
                - task: Task 2 for Litware
                - task: Task 3 for Litware
        - account: Adventure Works
        - account: Fabrikam, Inc.
```

- Each of the three account records have the single-valued navigation property `ownerid` set to the user **FirstName LastName**.
  
  The partner collection-valued navigation property is `user_accounts`.
  
- The three task records have the single-valued navigation property `regardingobjectid` set to the account **Litware, Inc.**.
   
   The partner collection-valued navigation property is `Account_Tasks`.

Compare the following queries which:

- Use the `Prefer: odata.maxpagesize=2` request header
- Return only accounts where **FirstName LastName** is set using `ownerid`

> [!NOTE]
> You must scroll the samples horizontally to see the URLs in the **Response** that contain paging data.


## [Single $expand accounts](#tab/single-account)

This query returns accounts filtered by the `_ownerid_value` that represents the **FirstName LastName** user and expands the related tasks.

**Request**

```http
GET [Organization Uri]/api/data/v9.2/accounts?$filter=_ownerid_value eq 4026be43-6b69-e111-8f65-78e7d1620f5e
&$select=name
&$expand=Account_Tasks($select=subject) HTTP/1.1
Prefer: odata.maxpagesize=2
If-None-Match: null
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
```

**Response**

```http
HTTP/1.1 200 OK
OData-Version: 4.0
Preference-Applied: odata.maxpagesize=2

{
    "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#accounts(name,Account_Tasks(subject))",
    "value": [
        {
            "@odata.etag": "W/\"80649578\"",
            "name": "Litware, Inc.",
            "accountid": "78914942-34cb-ed11-b596-0022481d68cd",
            "Account_Tasks": [
                {
                    "@odata.etag": "W/\"80649460\"",
                    "subject": "Task 1 for Litware",
                    "_regardingobjectid_value": "78914942-34cb-ed11-b596-0022481d68cd",
                    "activityid": "f68393c1-34cb-ed11-b597-000d3a993550"
                },
                {
                    "@odata.etag": "W/\"80649469\"",
                    "subject": "Task 2 for Litware",
                    "_regardingobjectid_value": "78914942-34cb-ed11-b596-0022481d68cd",
                    "activityid": "75f142ce-34cb-ed11-b597-000d3a993550"
                },
                {
                    "@odata.etag": "W/\"80649662\"",
                    "subject": "Task 3 for Litware",
                    "_regardingobjectid_value": "78914942-34cb-ed11-b596-0022481d68cd",
                    "activityid": "f22427ce-51cb-ed11-b597-000d3a993550"
                }
            ],
            "Account_Tasks@odata.nextLink": "[Organization Uri]/api/data/v9.2/accounts(78914942-34cb-ed11-b596-0022481d68cd)/Account_Tasks?$select=subject"
        },
        {
            "@odata.etag": "W/\"80649580\"",
            "name": "Adventure Works",
            "accountid": "7a914942-34cb-ed11-b596-0022481d68cd",
            "Account_Tasks": [],
            "Account_Tasks@odata.nextLink": "[Organization Uri]/api/data/v9.2/accounts(7a914942-34cb-ed11-b596-0022481d68cd)/Account_Tasks?$select=subject"
        }
    ],
    "@odata.nextLink": "[Organization Uri]/api/data/v9.2/accounts?$filter=_ownerid_value%20eq%204026be43-6b69-e111-8f65-78e7d1620f5e&$select=name&$expand=Account_Tasks($select=subject)&$skiptoken=%3Ccookie%20pagenumber=%222%22%20pagingcookie=%22%253ccookie%2520page%253d%25221%2522%253e%253caccountid%2520last%253d%2522%257b7A914942-34CB-ED11-B596-0022481D68CD%257d%2522%2520first%253d%2522%257b78914942-34CB-ED11-B596-0022481D68CD%257d%2522%2520%252f%253e%253c%252fcookie%253e%22%20istracking=%22False%22%20/%3E"
}
```

Only the `@odata.nextLink` URL contains paging data.

Because this query uses a single `$expand`, the `Account_Tasks@odata.nextLink` URLs don't include paging data. These URLs provide an alternate URL to retrieve the values currently returned. These URLs are returned even when there are no task records in the `Account_Tasks` collection.

The `odata.maxpagesize=2` preference is applied to the accounts entity set resource. Only 2 account records are returned.


## [Single $expand systemuser](#tab/single-systemuser)

This query returns a collection of account records but uses the `systemuser.user_accounts` collection-valued navigation property to filter the results to only those accounts associated to the user **FirstName LastName**.

**Request**

```http
GET [Organization Uri]/api/data/v9.2/systemusers(4026be43-6b69-e111-8f65-78e7d1620f5e)/user_accounts?$select=name
&$expand=Account_Tasks($select=subject) HTTP/1.1
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
OData-Version: 4.0
Preference-Applied: odata.maxpagesize=2

{
    "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#accounts(name,Account_Tasks(subject))",
    "value": [
        {
            "@odata.etag": "W/\"80649578\"",
            "name": "Litware, Inc.",
            "accountid": "78914942-34cb-ed11-b596-0022481d68cd",
            "Account_Tasks": [
                {
                    "@odata.etag": "W/\"80649460\"",
                    "subject": "Task 1 for Litware",
                    "_regardingobjectid_value": "78914942-34cb-ed11-b596-0022481d68cd",
                    "activityid": "f68393c1-34cb-ed11-b597-000d3a993550"
                },
                {
                    "@odata.etag": "W/\"80649469\"",
                    "subject": "Task 2 for Litware",
                    "_regardingobjectid_value": "78914942-34cb-ed11-b596-0022481d68cd",
                    "activityid": "75f142ce-34cb-ed11-b597-000d3a993550"
                },
                {
                    "@odata.etag": "W/\"80649662\"",
                    "subject": "Task 3 for Litware",
                    "_regardingobjectid_value": "78914942-34cb-ed11-b596-0022481d68cd",
                    "activityid": "f22427ce-51cb-ed11-b597-000d3a993550"
                }
            ]
        },
        {
            "@odata.etag": "W/\"80649580\"",
            "name": "Adventure Works",
            "accountid": "7a914942-34cb-ed11-b596-0022481d68cd",
            "Account_Tasks": []
        }
    ],
    "@odata.nextLink": "[Organization Uri]/api/data/v9.2/systemusers(4026be43-6b69-e111-8f65-78e7d1620f5e)/user_accounts?$select=name&$expand=Account_Tasks($select=subject)&$skiptoken=%3Ccookie%20pagenumber=%222%22%20pagingcookie=%22%253ccookie%2520page%253d%25221%2522%2520parentEntityId%253d%25224026be43-6b69-e111-8f65-78e7d1620f5e%2522%2520parentAttributeName%253d%2522owninguser%2522%2520parentEntityObjectTypeCode%253d%25228%2522%253e%253caccountid%2520last%253d%2522%257b7A914942-34CB-ED11-B596-0022481D68CD%257d%2522%2520first%253d%2522%257b78914942-34CB-ED11-B596-0022481D68CD%257d%2522%2520%252f%253e%253c%252fcookie%253e%22%20istracking=%22False%22%20/%3E"
}
```

> [!NOTE]
> In this case, there are no `Account_Tasks@odata.nextLink` urls. This is because [TODO: Need explanation here].


## [Multi-level $expand systemuser](#tab/multi-systemuser)

This query returns only the **FirstName LastName** systemuser record with multiple `$expand` system query options to include the accounts and related tasks.

**Request**

```http
GET [Organization Uri]/api/data/v9.2/systemusers?$filter=systemuserid eq 4026be43-6b69-e111-8f65-78e7d1620f5e
&$select=fullname
&$expand=user_accounts($select=name;
 $expand=Account_Tasks($select=subject)) HTTP/1.1
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
OData-Version: 4.0
Preference-Applied: odata.maxpagesize=2

{
    "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#systemusers(fullname,user_accounts(name,Account_Tasks(subject)))",
    "value": [
        {
            "@odata.etag": "W/\"61658658\"",
            "fullname": "FirstName LastName",
            "systemuserid": "4026be43-6b69-e111-8f65-78e7d1620f5e",
            "ownerid": "4026be43-6b69-e111-8f65-78e7d1620f5e",
            "user_accounts": [
                {
                    "name": "Litware, Inc.",
                    "accountid": "78914942-34cb-ed11-b596-0022481d68cd",
                    "Account_Tasks": [
                        {
                            "subject": "Task 1 for Litware",
                            "activityid": "f68393c1-34cb-ed11-b597-000d3a993550"
                        },
                        {
                            "subject": "Task 2 for Litware",
                            "activityid": "75f142ce-34cb-ed11-b597-000d3a993550"
                        }
                    ],
                    "Account_Tasks@odata.nextLink": "[Organization Uri]/api/data/v9.2/accounts(78914942-34cb-ed11-b596-0022481d68cd)/Account_Tasks?$select=subject&$skiptoken=%3Ccookie%20pagenumber=%222%22%20pagingcookie=%22%253ccookie%2520page%253d%25221%2522%2520countOfRecords%253d%25222%2522%253e%253cactivityid%2520last%253d%2522%257b75f142ce-34cb-ed11-b597-000d3a993550%257d%2522%2520first%253d%2522%257bf68393c1-34cb-ed11-b597-000d3a993550%257d%2522%2520%252f%253e%253c%252fcookie%253e%22%20istracking=%22False%22%20/%3E"
                }
            ],
            "user_accounts@odata.nextLink": "[Organization Uri]/api/data/v9.2/systemusers(4026be43-6b69-e111-8f65-78e7d1620f5e)/user_accounts?$select=name&$expand=Account_Tasks($select=subject)&$skiptoken=%3Ccookie%20pagenumber=%222%22%20pagingcookie=%22%253ccookie%2520page%253d%25221%2522%2520countOfRecords%253d%25221%2522%253e%253caccountid%2520last%253d%2522%257b78914942-34cb-ed11-b596-0022481d68cd%257d%2522%2520first%253d%2522%257b78914942-34cb-ed11-b596-0022481d68cd%257d%2522%2520%252f%253e%253c%252fcookie%253e%22%20istracking=%22False%22%20/%3E"
        }
    ],
    "@odata.nextLink": "[Organization Uri]/api/data/v9.2/systemusers?$filter=systemuserid%20eq%204026be43-6b69-e111-8f65-78e7d1620f5e&$select=fullname&$expand=user_accounts($select=name;$expand=Account_Tasks($select=subject))&$skiptoken=%3Ccookie%20pagenumber=%222%22%20pagingcookie=%22%253ccookie%2520page%253d%25221%2522%2520countOfRecords%253d%25221%2522%253e%253csystemuserid%2520last%253d%2522%257b4026be43-6b69-e111-8f65-78e7d1620f5e%257d%2522%2520first%253d%2522%257b4026be43-6b69-e111-8f65-78e7d1620f5e%257d%2522%2520%252f%253e%253c%252fcookie%253e%22%20istracking=%22False%22%20/%3E"
}
```

Because there is more than 1 `$expand` system query option in the query, the behavior is different.

Note that a total of four records are returned:

- One user record
- One expanded account record
- Two expanded task records

The `odata.maxpagesize=2` preference was applied to limit the total number of records returned, but didn't limit it strictly to just two records. With this query, the `@odata.nextLink` URL values for each collection contain paging data and you can use them to get the next set of records if they exist.

- `Account_Tasks@odata.nextLink` returns the third task record associated to account **Litware**
- `user_accounts@odata.nextLink` returns the 2 accounts: **Adventure Works** and **Fabrikam, Inc.**
- `@odata.nextLink` returns no records because the query used the primary key for the `systemuser` entityset: <br />`$filter=systemuserid eq 4026be43-6b69-e111-8f65-78e7d1620f5e`.
   
   In this case, Dataverse is anticipating that there could be more records and provides a paging URL. When you perform an `GET` request using that `URL`, it will contain no records and there will be no `@odata.nextLink`. Then you will know that there are no more records that meet the criteria.


## [Multi-level $expand systemuser bug](#tab/multi-systemuser-bug)

> [!IMPORTANT]
> I'm just including this here so you can see it in the review.
> 
> I wanted to use this query as an example, but it only shows that the second `$expand` included in the query is completely ignored: `;$expand=Account_Tasks($select=subject)`.
> 
> We know that **Litware** has associated tasks, but these results show: `"Account_Tasks": []`.

**Request**

```http
GET [Organization Uri]/api/data/v9.2/systemusers(4026be43-6b69-e111-8f65-78e7d1620f5e)?$select=fullname
&$expand=user_accounts($select=name;
$expand=Account_Tasks($select=subject)) HTTP/1.1
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
OData-Version: 4.0
Preference-Applied: odata.maxpagesize=2

{
    "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#systemusers(fullname,user_accounts(name,Account_Tasks(subject)))/$entity",
    "@odata.etag": "W/\"61658658\"",
    "fullname": "FirstName LastName",
    "systemuserid": "4026be43-6b69-e111-8f65-78e7d1620f5e",
    "ownerid": "4026be43-6b69-e111-8f65-78e7d1620f5e",
    "user_accounts": [
        {
            "@odata.etag": "W/\"80649578\"",
            "name": "Litware, Inc.",
            "accountid": "78914942-34cb-ed11-b596-0022481d68cd",
            "Account_Tasks": []
        },
        {
            "@odata.etag": "W/\"80649580\"",
            "name": "Adventure Works",
            "accountid": "7a914942-34cb-ed11-b596-0022481d68cd",
            "Account_Tasks": []
        }
    ],
    "user_accounts@odata.nextLink": "[Organization Uri]/api/data/v9.2/systemusers(4026be43-6b69-e111-8f65-78e7d1620f5e)/user_accounts?$select=name&$expand=Account_Tasks($select=subject)&$skiptoken=%3Ccookie%20pagenumber=%222%22%20pagingcookie=%22%253ccookie%2520page%253d%25221%2522%2520parentEntityId%253d%25224026be43-6b69-e111-8f65-78e7d1620f5e%2522%2520parentAttributeName%253d%2522owninguser%2522%2520parentEntityObjectTypeCode%253d%25228%2522%253e%253caccountid%2520last%253d%2522%257b7A914942-34CB-ED11-B596-0022481D68CD%257d%2522%2520first%253d%2522%257b78914942-34CB-ED11-B596-0022481D68CD%257d%2522%2520%252f%253e%253c%252fcookie%253e%22%20istracking=%22False%22%20/%3E"
}
```

---