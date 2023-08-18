---
title: Query data using the Web API
description: Learn how to use the Web API to query Microsoft Dataverse tables and the query options you can apply.
ms.topic: how-to
ms.date: 04/13/2023
author: divkamath
ms.author: dikamath
ms.reviewer: jdaly
search.audienceType: 
  - developer
contributors: 
  - JimDaly
ms.custom: bap-template
---
# Query data using the Web API

When you use the Web API to create a query against a Dataverse table, you need to make the following decisions:

|Decision|Description|
|---------|---------|
|[Select columns](#select-columns)|Which columns of data to return|
|[Join tables](#join-tables)|Which related tables to include in the results|
|[Order rows](#order-rows)|What order to return the results|
|[Filter rows](#filter-rows)|Which rows of data to return|
|[Page results](#page-results)|How many rows of data to return|
|[Aggregate data](#aggregate-data)|How to group and aggregate the data returned|
|[Count number of rows](#count-number-of-rows)|How to count the number of rows|

This article is about querying data found in tables. You can also use Web API to query data about *table definitions*, or *entity metadata*. The structure of the data is different, so many of the capabilities described here do not apply. More information: [Query table definitions using the Web API](query-metadata-web-api.md) and [Query schema definitions](../query-schema-definitions.md)

## Entity collections

Every query begins with a collection of entities. Entity collections can be:

- [EntitySet resources](#entityset-resources): One of the Web API EntitySet collections.
- [Filtered collections](#filtered-collections): A set of entities returned by a [collection-valued navigation property](web-api-navigation-properties.md#collection-valued-navigation-properties) for a specific record.
- An expanded collection-valued navigation property. More information: [Expand collection-valued navigation properties](#expand-collection-valued-navigation-properties)

### EntitySet resources

To find all the EntitySet resources available in your environment, send a `GET` request to the Web API [service document](web-api-service-documents.md#service-document):

**Request:**

```http
GET [Organization URI]/api/data/v9.2/
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0
```

**Response:**

```http
HTTP/1.1 200 OK  
Content-Type: application/json; odata.metadata=minimal  
OData-Version: 4.0  

{
    "@odata.context": "[Organization URI]/api/data/v9.2/$metadata",
    "value": [
        {
            "name": "aadusers",
            "kind": "EntitySet",
            "url": "aadusers"
        },
        {
            "name": "accountleadscollection",
            "kind": "EntitySet",
            "url": "accountleadscollection"
        },
        {
            "name": "accounts",
            "kind": "EntitySet",
            "url": "accounts"
        },
      ... <Truncated for brevity>
   [
}
```

> [!TIP]
> These values are usually the plural name of the table, but they can be different. Use this query to confirm you're using the correct EntitySet resource name.

To retrieve data from the [account EntityType](xref:Microsoft.Dynamics.CRM.account), you start with the `accounts` EntitySet resource.

```http
GET [Organization URI]/api/data/v9.2/accounts?$select=name
```

### Filtered collections

You can query any collection of entities represented by a collection-valued navigation property of a specified record.

If you want to retrieve data from the [account EntityType](xref:Microsoft.Dynamics.CRM.account), where a specific user is the [OwningUser](../reference/entities/account.md#BKMK_OwningUser), you can use the `user_accounts` collection-valued navigation property from the specified [systemuser](xref:Microsoft.Dynamics.CRM.systemuser) record.

```http
GET [Organization URI]/api/data/v9.2/systemusers(<systemuserid value>)/user_accounts?$select=name
```

To locate the name of the collection-valued navigation property:

- For any Dataverse tables and relationships, you can check the <xref:Microsoft.Dynamics.CRM.EntityTypeIndex?displayProperty=fullName>
- For any custom tables or relationships, look for the [collection-valued navigation properties](web-api-navigation-properties.md#collection-valued-navigation-properties) within the [$metadata service document](web-api-service-documents.md#csdl-metadata-document)


## OData query options

The following table describes the OData query options the Dataverse Web API supports.


|Option|Use to|More information|
|---------|---------|---------|
|`$select`|Request a specific set of properties for each entity or complex type.|[Select columns](#select-columns)|
|`$expand`|Specify the related resources to be included in line with retrieved resources. |[Join tables](#join-tables)|
|`$filter `|Filter a collection of resources. |[Filter rows](#filter-rows)|
|`$orderby`|Request resources in a particular order. |[Order rows](#order-rows)|
|`$apply`|Aggregate and group your data. |[Aggregate data](#aggregate-data)|
|`$top`|Specify the number of items in the queried collection to be included in the result. Don't use `$top` when you retrieve pages of data. |[Use the $top query option](#use-the-top-query-option)|
|`$count`|Request a count of the matching resources included with the resources in the response. |[Count number of rows](#count-number-of-rows)|

You can apply multiple options to a query. Separate query options from the resource path with a question mark (?). Separate each option after the first with an ampersand (&). Option names are case-sensitive.

The Dataverse Web API doesn't support these [OData query options](https://docs.oasis-open.org/odata/odata/v4.0/errata03/os/complete/part2-url-conventions/odata-v4.0-errata03-os-part2-url-conventions-complete.html#_Toc453752356): `$skip`,`$search`,`$format`.

### Use parameter aliases with query options

You can use parameter aliases for `$filter` and `$orderby` query options, but not inside the `$expand` option. Parameter aliases allow you to use the same value multiple times in a request. If the alias isn't assigned a value, it's assumed to be null.

Without parameter aliases:

```http
GET [Organization URI]/api/data/v9.2/accounts?$select=name,revenue
&$orderby=revenue asc,name desc
&$filter=revenue ne null
```

With parameter aliases:

```http
GET [Organization URI]/api/data/v9.2/accounts?$select=name,revenue
&$orderby=@p1 asc,@p2 desc
&$filter=@p1 ne @p3&@p1=revenue&@p2=name
```

You can also use parameter aliases when using functions. More information: [Use Web API functions](use-web-api-functions.md)


## Select columns

> [!IMPORTANT]
> When you query data, it's important to limit the amount of data returned to optimize performance. Only select the columns with data that you need.

Use the `$select` [query option](#odata-query-options) to choose which columns to return with your query. In OData, every column is represented as a [*property*](web-api-properties.md). If you don't include a `$select` query option, all properties are returned.

The following example requests the `name` and `revenue` properties from one row of the `accounts` EntitySet resource:

**Request:**

```http
GET [Organization URI]/api/data/v9.2/accounts?$select=name,revenue&$top=1
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
```

**Response:**

```http
HTTP/1.1 200 OK  
Content-Type: application/json; odata.metadata=minimal  
OData-Version: 4.0  

{
    "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#accounts(name,revenue)",
    "value": [
        {
            "@odata.etag": "W/\"81052965\"",
            "name": "Litware, Inc. (sample)",
            "revenue": 20000.0000,
            "_transactioncurrencyid_value": "228f42f8-e646-e111-8eb7-78e7d162ced1",
            "accountid": "4624eff7-53d3-ed11-a7c7-000d3a993550"
        }
    ]
}
```

The primary key property is always returned so you don't need to include it in your `$select`. In this example, `accountid` is the primary key.

Other property values may also be included. In this case, the `_transactioncurrencyid_value` [lookup property](web-api-properties.md#lookup-properties) for the related [Currency (TransactionCurrency)  table/entity reference](../reference/entities/transactioncurrency.md) is included because `revenue` is a currency property.

### Which properties are available?

All the available properties for an entity are found in the [$metadata service document](web-api-service-documents.md#csdl-metadata-document). More information: [Web API Properties](web-api-properties.md)

The entity types included with Dataverse are described in the <xref:Microsoft.Dynamics.CRM.EntityTypeIndex>.

> [!TIP]
> The easiest way to quickly discover which properties are available is to send a request using the `$top` query option with a value of `1` without using `$select`.

### Formatted values

Formatted values are string values generated on the server that you can use in your application. Formatted values include:

- The localized labels for choice, choices, yes/no, status, and status reason columns
- The primary name value for lookup and owner properties
- Currency values with currency symbols
- Formatted date values in the user's time zone

To include formatted values in your results, use this request header:

```
Prefer: odata.include-annotations="OData.Community.Display.V1.FormattedValue"
```

Formatted values are one of several annotations you can request. Use `Prefer: odata.include-annotations="*"` to include all annotations. More information: [Request annotations](compose-http-requests-handle-errors.md#request-annotations)

The formatted value is returned with the record with an annotation that follows this convention:

```
<property name>@OData.Community.Display.V1.FormattedValue
```

For example:



**Request:**

```http
GET [Organization URI]/api/data/v9.2/accounts?$select=name,revenue,_primarycontactid_value,customertypecode,modifiedon
&$top=1
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0
Prefer: odata.include-annotations="OData.Community.Display.V1.FormattedValue"
```

The following table describes the values and formatted values that are returned for the requested properties.

|Property|Value|Formatted value|
|---------|---------|---------|
|`name`|`Litware, Inc. (sample)`|None|
|`revenue`|`20000.0000`|`$20,000.00`|
|`_primarycontactid_value`|`70bf4d48-34cb-ed11-b596-0022481d68cd`|`Susanna Stubberod (sample)`|
|`customertypecode`|`1`|`Competitor`|
|`modifiedon`|`2023-04-07T21:59:01Z`|`4/7/2023 2:59 PM`|
|`_transactioncurrencyid_value`|`228f42f8-e646-e111-8eb7-78e7d162ced1`|`US Dollar`|
|`accountid`|`78914942-34cb-ed11-b596-0022481d68cd`|None|

**Response:**

```http
HTTP/1.1 200 OK  
Content-Type: application/json; odata.metadata=minimal  
OData-Version: 4.0
Preference-Applied: odata.include-annotations="OData.Community.Display.V1.FormattedValue"

{
    "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#accounts(name,revenue)",
    "value": [
{
            "@odata.etag": "W/\"81359849\"",
            "name": "Litware, Inc. (sample)",
            "revenue@OData.Community.Display.V1.FormattedValue": "$20,000.00",
            "revenue": 20000.0000,
            "_primarycontactid_value@OData.Community.Display.V1.FormattedValue": "Susanna Stubberod (sample)",
            "_primarycontactid_value": "70bf4d48-34cb-ed11-b596-0022481d68cd",
            "customertypecode@OData.Community.Display.V1.FormattedValue": "Competitor",
            "customertypecode": 1,
            "modifiedon@OData.Community.Display.V1.FormattedValue": "4/7/2023 2:59 PM",
            "modifiedon": "2023-04-07T21:59:01Z",
            "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
            "_transactioncurrencyid_value": "228f42f8-e646-e111-8eb7-78e7d162ced1",
            "accountid": "78914942-34cb-ed11-b596-0022481d68cd"
        }
    ]
}
```

### Lookup property data

When a [lookup property](web-api-properties.md#lookup-properties) represents a multi-table, or polymorphic, relationship, you need to request specific annotations to determine which table contains the related data.

For example, many tables have records that users or teams may own. Ownership data is stored in a lookup column named `ownerid`. This column is a single-valued navigation property in OData. You could use `$expand` to create a join to get this value, but you can't use `$select`. However, you can use the corresponding `_ownerid_value` lookup property with `$select`.

When you include the `_ownerid_value` lookup property with your `$select`, it returns a GUID value. This value doesn't tell you whether the owner of the record is a user or a team. You need to request annotations to get this data.

To include these annotations in your results, use this request header:

```
Prefer: odata.include-annotations="Microsoft.Dynamics.CRM.associatednavigationproperty,Microsoft.Dynamics.CRM.lookuplogicalname"
```

> [!TIP]
> Or you can use `Prefer: odata.include-annotations="*"` to include all annotations. More information: [Request annotations](compose-http-requests-handle-errors.md#request-annotations)


**Request:**

```http
GET [Organization URI]/api/data/v9.2/accounts?$select=name,_ownerid_value&$top=2
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0
Prefer: odata.include-annotations="Microsoft.Dynamics.CRM.associatednavigationproperty,Microsoft.Dynamics.CRM.lookuplogicalname"
```

The following response returns two different account records. A `team` owns the first one, and a `systemuser` owns the second one. The `_ownerid_value@Microsoft.Dynamics.CRM.lookuplogicalname` annotation provides this information.

**Response:**

```http
HTTP/1.1 200 OK  
Content-Type: application/json; odata.metadata=minimal  
OData-Version: 4.0
Preference-Applied: odata.include-annotations="Microsoft.Dynamics.CRM.associatednavigationproperty,Microsoft.Dynamics.CRM.lookuplogicalname"

{
    "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#accounts(name,_ownerid_value)",
    "value": [
        {
            "@odata.etag": "W/\"81550512\"",
            "name": "Adventure Works (sample)",
            "_ownerid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "ownerid",
            "_ownerid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "team",
            "_ownerid_value": "39e0dbe4-131b-e111-ba7e-78e7d1620f5e",
            "accountid": "1adef0b8-54d3-ed11-a7c7-000d3a993550"
        },
        {
            "@odata.etag": "W/\"81359849\"",
            "name": "Litware, Inc. (sample)",
            "_ownerid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "ownerid",
            "_ownerid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "systemuser",
            "_ownerid_value": "4026be43-6b69-e111-8f65-78e7d1620f5e",
            "accountid": "78914942-34cb-ed11-b596-0022481d68cd"
        }
    ]
}
```

- `<lookup property name>@Microsoft.Dynamics.CRM.lookuplogicalname` is the logical name of the related table.
- `<lookup property name>@Microsoft.Dynamics.CRM.associatednavigationproperty` is the name of the corresponding single-valued navigation property. You can use `$expand` using this value in another request to get more data from the related record.


## Join tables


To control what data is returned from related table records, use the `$expand` [query option](#odata-query-options) with navigation properties.

- You can include up to 15 `$expand` options in a query. Each `$expand` option creates a join that can affect performance.
- Queries which expand collection-valued navigation properties may return cached data for those properties that doesn't reflect recent changes. It is recommended to use `If-None-Match` header with value `null` to override browser caching. More information: [HTTP Headers](compose-http-requests-handle-errors.md#bkmk_headers) for more details.

The following table describes the [query options](#odata-query-options) you can apply in certain `$expand` options:


|Option|Description|
|---------|---------|
|`$select`|Select which properties are returned. More information: [Select columns](#select-columns)|
|`$filter`|For collection-valued navigation properties, limit the records returned. More information: [Filter rows](#filter-rows)|
|`$orderby`|For collection-valued navigation properties, control the order of records returned. Not supported with nested `$expand`. More information: [Nested $expand on collection-valued navigation properties](#nested-expand-on-collection-valued-navigation-properties)|
|`$top`|For collection-valued navigation properties, limit the number of records returned. Not supported with nested `$expand`. More information: [Nested $expand on collection-valued navigation properties](#nested-expand-on-collection-valued-navigation-properties)|
|`$expand`|Expand navigation properties in the related entity set. Using `$expand` in an `$expand` is called a *nested `$expand`*. More information: [Nested expand of single-valued navigation properties](#nested-expand-of-single-valued-navigation-properties) & [Nested $expand on collection-valued navigation properties](#nested-expand-on-collection-valued-navigation-properties)|

These options are a subset of the query options described in the **11.2.4.2.1 Expand Options** section of [OData Version 4.0 Part 1: Protocol Plus Errata 02](https://docs.oasis-open.org/odata/odata/v4.0/errata02/os/complete/part1-protocol/odata-v4.0-errata02-os-part1-protocol-complete.html#_Toc406398299). The options `$skip`, `$count`, `$search`, and `$levels` aren't supported for the Dataverse Web API.

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

### Limit columns with $select

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

### Navigation property type differences

It's important to remember there are two types of navigation properties. More information: [Web API Navigation Properties](web-api-navigation-properties.md)  
  
- *Single-valued* navigation properties correspond to lookup attributes that support many-to-one relationships and allow setting a reference to another record.  
  
- *Collection-valued* navigation properties correspond to one-to-many or many-to-many relationships.

Expanding a collection-valued navigation property can make the size of the response large in ways it's difficult to anticipate. It's important that you include limits to control how much data is returned. You can limit the number of records by using paging. More information: [Page results](#page-results)

There is a significant difference in how paging is applied to nested $expand options applied to collection valued navigation properties. More information: [Expand collection-valued navigation properties](#expand-collection-valued-navigation-properties)

### Expand single-valued navigation properties

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

However, the [User (SystemUser) table](../reference/entities/systemuser.md) has the primary key of [SystemUserId](../reference/entities/systemuser.md#BKMK_SystemUserId). Both `systemuserid` and `ownerid` properties have the same value. More information: [EntityType inheritance](web-api-entitytypes.md#entitytype-inheritance)

#### Return references

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

### Nested expand of single-valued navigation properties

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

### Expand collection-valued navigation properties

There are some important differences in the response that depend on whether you use nested `$expand` with a collection-valued navigation property anywhere in your query.

||Nested $expand|Single $expand|
|---------|---------|---------|
|**Paging**|Paging on expanded rows.|Paging only on [EntitySet resource](#entityset-resources). `<property name>@odata.nextLink` URLs for expanded rows don't include paging information.|
|**`$top` or `$orderby` supported**|No|Yes|

#### Single $expand on collection-valued navigation properties

If you use only single-level `$expand`, no paging is applied applied to the expanded rows. If you include the `Prefer: odata.maxpagesize` request header, paging is only applied to the EntitySet resource of the query.

Each expanded collection-valued navigation property returns a `<property>@odata.nextLink` URL that includes no paging information. It's a URL that represents the [filtered collection](#filtered-collections) for the relationship with your query options appended. You can use that URL to send a separate `GET` request and it returns the same rows that were returned in your original request. You can apply paging to that request.

Because no paging is applied to the expanded records, up to 5,000 related records can be returned for each expanded collection-valued navigation property. Depending on your data and the query, it could be a lot of data. Returning that much data could affect performance and possibly cause your request to time out. Be cautious about the queries you compose. You can use `$top`, `$filter`, and `$orderby` options to control the total number of records returned.

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


#### Nested $expand on collection-valued navigation properties

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

Compare this response with the previous example, which doesn't use a nested `$expand`. In this response, the `Prefer: odata.maxpagesize=1` request header is applied to the `task` records returned with `Account_Tasks`. Only one task is returned instead of three. The `Account_Tasks@odata.nextLink` URL returns the next two tasks. Scroll the example response horizontally to see that `Account_Tasks@odata.nextLink`, `contact_customer_accounts@odata.nextLink`, and`@odata.nextLink` URLs contain paging information.

## Order rows

Use the `$orderby` [query option](#odata-query-options) to specify the order in which items are returned. Use the `asc` or `desc` suffix to specify ascending or descending order, respectively. The default is ascending. The following example retrieves the `name` and `revenue` properties of accounts, ordered by ascending `revenue` and descending `name`:

```http
GET [Organization URI]/api/data/v9.2/accounts?$select=name,revenue
&$orderby=revenue asc,name desc
&$filter=revenue ne null
```

## Filter rows

Use the `$filter` [query option](#odata-query-options) to filter a collection of resources.

Dataverse evaluates each resource in the collection using the expression set for `$filter`. Only records where the expression evaluates to `true` are returned in the response. Records aren't returned if the expression evaluates to `false` or `null`, or if the user doesn't have read access to the record.

The following table describes the operators and functions you can use in `$filter` expressions.


| |Description| More information|
|---------|---------|---------|
|**Comparison operators**|Use the `eq`,`ne`,`gt`,`ge`,`lt`, and `le` operators to compare a property and a value.|[ Comparison operators](#comparison-operators)|
|**Logical operators**|Use `and`, `or`, and `not` to create more complex expressions. |[Logical operators](#logical-operators)|
|**Grouping operators**|Use parentheses: (), to specify the precedence to evaluate a complex expression. |[Grouping operators](#grouping-operators)|
|**OData query functions**|Evaluate string values using `contains`, `endswith`, and `startswith` functions. |[Use OData query functions](#use-odata-query-functions)|
|**Dataverse query functions**|Use more than 60 specialized functions designed for business applications. |[Dataverse query functions](#dataverse-query-functions)|
|**Lambda expressions**|Create expressions based on values of related collections. |[Filter using values of related collections](#filter-using-values-of-related-collections)|

If you're using a [lookup property](web-api-properties.md#lookup-properties) in a `$filter`, you can also use a [filtered collection](#filtered-collections) with the corresponding collection-valued navigation property. For example, these two queries return the same results:

`accounts?$filter=_owninguser_value eq '<systemuserid value>'&$select=name`

`systemusers(<systemuserid value>)/user_accounts?$select=name`

### Comparison operators

The following table describes the operators you can use to compare a property and a value.

|Operator|Description|Example|  
|--------------|-----------------|-------------|
|`eq`|Equal|`$filter=revenue eq 100000`|  
|`ne`|Not Equal|`$filter=revenue ne 100000`|  
|`gt`|Greater than|`$filter=revenue gt 100000`|  
|`ge`|Greater than or equal|`$filter=revenue ge 100000`|  
|`lt`|Less than|`$filter=revenue lt 100000`|  
|`le`|Less than or equal|`$filter=revenue le 100000`|  

#### Column comparison

You can use comparison operators to compare property values in the same row; that is, to [compare columns](../column-comparison.md). Only comparison operators can be used to compare values in the same row, and the column types must match. For example, the following query returns any contacts where `firstname` equals `lastname`:

```http
GET [Organization URI]/api/data/v9.2/contacts?$select=fullname&$filter=firstname eq lastname
```

### Logical operators

The following table describes the logical operators you can use to create more complex expressions.

|Operator|Description|Example|  
|--------------|-----------------|-------------|
|`and`|Logical and|`$filter=revenue lt 100000 and revenue gt 2000`|  
|`or`|Logical or|`$filter=contains(name,'(sample)') or contains(name,'test')`|  
|`not`|Logical negation|`$filter=not contains(name,'sample')`|  

### Grouping operators

Use parentheses () with logical operators to specify the precedence to evaluate a complex expression; for example:

`$filter=(contains(name,'sample') or contains(name,'test')) and revenue gt 5000`

### Dataverse query functions

Use more than 60 specialized functions designed for business applications. These functions provide special capabilities, as described in the following table.

|Group|Functions|
|---------|---------|
|**Dates** |<xref:Microsoft.Dynamics.CRM.InFiscalPeriod>, <xref:Microsoft.Dynamics.CRM.InFiscalPeriodAndYear>, <xref:Microsoft.Dynamics.CRM.InFiscalYear>, <xref:Microsoft.Dynamics.CRM.InOrAfterFiscalPeriodAndYear>, <xref:Microsoft.Dynamics.CRM.InOrBeforeFiscalPeriodAndYear>,<br /><xref:Microsoft.Dynamics.CRM.Last7Days>, <xref:Microsoft.Dynamics.CRM.LastFiscalPeriod>, <xref:Microsoft.Dynamics.CRM.LastFiscalYear>, <xref:Microsoft.Dynamics.CRM.LastMonth>, <xref:Microsoft.Dynamics.CRM.LastWeek>, <xref:Microsoft.Dynamics.CRM.LastXDays>, <xref:Microsoft.Dynamics.CRM.LastXFiscalPeriods>, <xref:Microsoft.Dynamics.CRM.LastXFiscalYears>,<br /><xref:Microsoft.Dynamics.CRM.LastXHours>, <xref:Microsoft.Dynamics.CRM.LastXMonths>, <xref:Microsoft.Dynamics.CRM.LastXWeeks>, <xref:Microsoft.Dynamics.CRM.LastXYears>, <xref:Microsoft.Dynamics.CRM.LastYear>, <xref:Microsoft.Dynamics.CRM.Next7Days>, <xref:Microsoft.Dynamics.CRM.NextFiscalPeriod>, <xref:Microsoft.Dynamics.CRM.NextFiscalYear>,<br /><xref:Microsoft.Dynamics.CRM.NextMonth>, <xref:Microsoft.Dynamics.CRM.NextWeek>, <xref:Microsoft.Dynamics.CRM.NextXDays>, <xref:Microsoft.Dynamics.CRM.NextXFiscalPeriods>, <xref:Microsoft.Dynamics.CRM.NextXFiscalYears>, <xref:Microsoft.Dynamics.CRM.NextXHours>, <xref:Microsoft.Dynamics.CRM.NextXMonths>,<br /><xref:Microsoft.Dynamics.CRM.NextXWeeks>, <xref:Microsoft.Dynamics.CRM.NextXYears>, <xref:Microsoft.Dynamics.CRM.NextYear>, <xref:Microsoft.Dynamics.CRM.OlderThanXDays>, <xref:Microsoft.Dynamics.CRM.OlderThanXHours>, <xref:Microsoft.Dynamics.CRM.OlderThanXMinutes>, <xref:Microsoft.Dynamics.CRM.OlderThanXMonths>,<br /><xref:Microsoft.Dynamics.CRM.OlderThanXWeeks>, <xref:Microsoft.Dynamics.CRM.OlderThanXYears>, <xref:Microsoft.Dynamics.CRM.On>, <xref:Microsoft.Dynamics.CRM.OnOrAfter>, <xref:Microsoft.Dynamics.CRM.OnOrBefore>, <xref:Microsoft.Dynamics.CRM.ThisFiscalPeriod>, <xref:Microsoft.Dynamics.CRM.ThisFiscalYear>, <xref:Microsoft.Dynamics.CRM.ThisMonth>, <xref:Microsoft.Dynamics.CRM.ThisWeek>, <xref:Microsoft.Dynamics.CRM.ThisYear>, <xref:Microsoft.Dynamics.CRM.Today>, <xref:Microsoft.Dynamics.CRM.Tomorrow>, <xref:Microsoft.Dynamics.CRM.Yesterday>|
|**Id Values**|<xref:Microsoft.Dynamics.CRM.EqualBusinessId>, <xref:Microsoft.Dynamics.CRM.EqualUserId>, <xref:Microsoft.Dynamics.CRM.NotEqualBusinessId>, <xref:Microsoft.Dynamics.CRM.NotEqualUserId>|
|**Hierarchy**|<xref:Microsoft.Dynamics.CRM.Above>, <xref:Microsoft.Dynamics.CRM.AboveOrEqual>, <xref:Microsoft.Dynamics.CRM.EqualUserOrUserHierarchy>, <xref:Microsoft.Dynamics.CRM.EqualUserOrUserHierarchyAndTeams>, <xref:Microsoft.Dynamics.CRM.EqualUserOrUserTeams>, <br /><xref:Microsoft.Dynamics.CRM.EqualUserTeams>, <xref:Microsoft.Dynamics.CRM.NotUnder>, <xref:Microsoft.Dynamics.CRM.Under>, <xref:Microsoft.Dynamics.CRM.UnderOrEqual><br />More information: [Query hierarchical data](../query-hierarchical-data.md)|
|**Choices columns**|<xref:Microsoft.Dynamics.CRM.ContainValues>, <xref:Microsoft.Dynamics.CRM.DoesNotContainValues><br />More information: [Query data from choices](../multi-select-picklist.md#query-data-from-choices)|
|**Between**|<xref:Microsoft.Dynamics.CRM.Between>, <xref:Microsoft.Dynamics.CRM.NotBetween>|
|**In**|<xref:Microsoft.Dynamics.CRM.In>, <xref:Microsoft.Dynamics.CRM.NotIn>|
|**Language**|<xref:Microsoft.Dynamics.CRM.EqualUserLanguage>|

> [!NOTE]
> The [Contains function](xref:Microsoft.Dynamics.CRM.Contains) is for use with columns that have full-text indexing. Only the Dynamics 365 KBArticle (article) table has columns that have full-text indexing. Use the OData `contains` function instead.

The <xref:Microsoft.Dynamics.CRM.QueryFunctionIndex?displayProperty=fullName> has the complete list. Each article provides a syntax example you can copy.

You must use the function's *fully qualified name* and append the [Service namespace](web-api-service-documents.md#service-namespace) (`Microsoft.Dynamics.CRM`) to the name of the function.

Each function has a `PropertyName` parameter that specifies the property to be evaluated. The function may have more parameters, such as `PropertyValue`, `PropertyValues`, or `PropertyValue1` and `PropertyValue2`. When these parameters exist, you must supply a value, or values, to compare to the `PropertyName` parameter.

The following example shows uses the [Between function](xref:Microsoft.Dynamics.CRM.Between) to search for accounts with between 5 and 2,000 employees.  
  
```http 
GET [Organization URI]/api/data/v9.2/accounts?$select=name,numberofemployees
&$filter=Microsoft.Dynamics.CRM.Between(PropertyName='numberofemployees',PropertyValues=["5","2000"])  
```  

### Filter using string values

Keep the following points in mind when you filter on string values:

- All filters using string values are case insensitive.
- You must URL encode special characters in filter criteria. More information: [URL encode special characters](#url-encode-special-characters)
- You may use wildcard characters, but avoid trailing wildcards. More information: [Use wildcard characters](#use-wildcard-characters)
- You can use OData query functions: `contains`, `startswith`, and `endswith`. More information: [Use OData query functions](#use-odata-query-functions)
- You must manage single quotes when you use filters that accept an array of string values. More information: [Manage single quotes](#manage-single-quotes)

#### URL encode special characters

If the string you are using as a value in a filter function includes a special character, you need to URL encode it. For example, if you use this function: `contains(name,'+123')`, it will not work because `+` is a character that can't be included in a URL. If you URL encode the string, it will become `contains(name,'%2B123')` and you will get results where the column value contains `+123`.

The following table shows the URL encoded values for common special characters.

|Special<br />character|URL encoded<br />character|
|---|---|
|`$`|`%24`|
|`&`|`%26`|
|`+`|`%2B`|
|`,`|`%2C`|
|`/`|`%2F`|
|`:`|`%3A`|
|`;`|`%3B`|
|`=`|`%3D`|
|`?`|`%3F`|
|`@`|`%40`|


#### Use wildcard characters

When composing filters using strings, you can apply the following wildcard characters:

|Characters  |Description  |T-SQL documentation and examples  |
|---------|---------|---------|
|`% ` |Matches any string of zero or more characters. This wildcard character can be used as either a prefix or a suffix.|[Percent character (Wildcard - Character(s) to Match) (Transact-SQL)](/sql/t-sql/language-elements/percent-character-wildcard-character-s-to-match-transact-sql)|
|`_`  |Use the underscore character to match any single character in a string comparison operation that involves pattern matching.|[_ (Wildcard - Match One Character) (Transact-SQL)](/sql/t-sql/language-elements/wildcard-match-one-character-transact-sql)|
|`[]` |Matches any single character within the specified range or set that is specified between brackets.|[[ ] (Wildcard - Character(s) to Match) (Transact-SQL)](/sql/t-sql/language-elements/wildcard-character-s-to-match-transact-sql)|
|`[^]`|Matches any single character that isn't within the range or set specified between the square brackets.|[[^] (Wildcard - Character(s) Not to Match) (Transact-SQL)](/sql/t-sql/language-elements/wildcard-character-s-not-to-match-transact-sql)|

More information: [Use wildcard characters in conditions for string values](../wildcard-characters.md)

##### Trailing wildcards not supported

It's important not to use trailing wild cards because they aren't supported. Queries that use these anti-patterns introduce performance problems because the queries can't be optimized. Here are some examples of trailing wildcards:

```
startswith(name,'%value')
endswith(name,'value%')
```

#### Use OData query functions

The following table describes the OData query functions you can use to filter on string values:

|Function|Example|  
|--------------|-------------|  
|`contains`|`$filter=contains(name,'(sample)')`|  
|`endswith`|`$filter=endswith(name,'Inc.')`|  
|`startswith`|`$filter=startswith(name,'a')`|

You can use these functions with the logical operator `not` to negate the result.

#### Manage single quotes

Some filters accept an array of string values, such as the [In Query function](xref:Microsoft.Dynamics.CRM.In). When you specify values in these filters that contain single quote, or apostrophe, characters, such as `O'Brian` or `Men's clothes`, you must use double quotes around the values; for example:

```http
GET [Organization URI]/api/data/v9.2/contacts?$select=fullname
&$filter=Microsoft.Dynamics.CRM.In(PropertyName=@p1,PropertyValues=@p2)
&@p1='lastname'
&@p2=["OBrian","OBryan","O'Brian","O'Bryan"]
```

If you don't, you get the following error: `Invalid JSON. A comma character ',' was expected in scope 'Array'. Every two elements in an array and properties of an object must be separated by commas.`

If the filter is for a single value, replace the single quote character with two consecutive single quote characters; for example:

```http
GET [Organization URI]/api/data/v9.2/contacts?$select=fullname
&$filter=lastname eq 'O''Bryan'
```

If you don't, you get an error like this: `There is an unterminated literal at position 21 in 'lastname eq 'O'Bryan''.`

### Filter based on related data values

You can filter rows returned based on values in related tables. How you filter depends on the type of relationship.

#### Filter using lookup column property values

You can filter based on values in single-valued navigation properties that represent lookup columns. Use this pattern:

`<single-valued navigation property>/<property name>`

The following example returns account records based on the value of the `primarycontactid/fullname` column:

**Request:**

```http
GET [Organization URI]/api/data/v9.2/accounts?$filter=primarycontactid/fullname eq 'Susanna Stubberod (sample)'
&$select=name,_primarycontactid_value
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0
Prefer: odata.include-annotations="OData.Community.Display.V1.FormattedValue"
```

**Response:**

```http
HTTP/1.1 200 OK
Content-Type: application/json; odata.metadata=minimal
OData-Version: 4.0
Preference-Applied: odata.include-annotations="OData.Community.Display.V1.FormattedValue"

{
    "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#accounts(name,_primarycontactid_value)",
    "value": [
        {
            "@odata.etag": "W/\"81359849\"",
            "name": "Litware, Inc. (sample)",
            "_primarycontactid_value@OData.Community.Display.V1.FormattedValue": "Susanna Stubberod (sample)",
            "_primarycontactid_value": "70bf4d48-34cb-ed11-b596-0022481d68cd",
            "accountid": "78914942-34cb-ed11-b596-0022481d68cd"
        }
    ]
}
```

You can also compare values further up the hierarchy of single-valued navigation properties.

The following example returns the first account where the contact record represents the `primarycontactid`, where 'System Administrator' created the record, using `primarycontactid/createdby/fullname` in the `$filter`.

**Request:**

```http
GET [Organization URI]/api/data/v9.2/accounts?$filter=primarycontactid/createdby/fullname eq 'System Administrator'
&$select=name,_primarycontactid_value
&$expand=primarycontactid(
$select=fullname,_createdby_value;
$expand=createdby($select=fullname))
&$top=1
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0
Prefer: odata.include-annotations="OData.Community.Display.V1.FormattedValue"

```

**Response:**

```http
HTTP/1.1 200 OK
Content-Type: application/json; odata.metadata=minimal
OData-Version: 4.0
Preference-Applied: odata.include-annotations="OData.Community.Display.V1.FormattedValue"

{
    "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#accounts(name,_primarycontactid_value,primarycontactid(fullname,_createdby_value,createdby(fullname)))",
    "value": [
        {
            "@odata.etag": "W/\"81359849\"",
            "name": "Litware, Inc. (sample)",
            "_primarycontactid_value@OData.Community.Display.V1.FormattedValue": "Susanna Stubberod (sample)",
            "_primarycontactid_value": "70bf4d48-34cb-ed11-b596-0022481d68cd",
            "accountid": "78914942-34cb-ed11-b596-0022481d68cd",
            "primarycontactid": {
                "fullname": "Susanna Stubberod (sample)",
                "_createdby_value@OData.Community.Display.V1.FormattedValue": "System Administrator",
                "_createdby_value": "4026be43-6b69-e111-8f65-78e7d1620f5e",
                "contactid": "70bf4d48-34cb-ed11-b596-0022481d68cd",
                "createdby": {
                    "fullname": "System Administrator",
                    "systemuserid": "4026be43-6b69-e111-8f65-78e7d1620f5e",
                    "ownerid": "4026be43-6b69-e111-8f65-78e7d1620f5e"
                }
            }
        }
    ]
}
```

#### Filter using values of related collections

Use the *Lambda operators* `any` and `all` to evaluate values in a collection to filter the results.

- `any`: Returns `true` if the expression applied is true for any member of the collection; otherwise, it returns false. The `any` operator without an argument returns `true` if the collection isn't empty.
- `all`: Returns true if the expression applied is true for all members of the collection; otherwise, it returns false.

The syntax looks like this:

`<collection>/[any | all](o:<expression to evaluate>)`

In this case, `o` is the variable that represents items in the collection. The convention is to use the first letter of the type.
In the expression, use `o/<property or collection name>` to refer to a property or collection of a given item.

You can include conditions on multiple collection-valued navigation properties and nested collections. You can't include conditions on collection-valued navigation properties that are nested in a lookup navigation property. For example, `$filter=primarycontactid/new_contact_account/any(a:a/accountid eq '{GUID}')` isn't supported.

More information: [Lambda Operators at odata.org](https://www.odata.org/getting-started/basic-tutorial/#lambda)

##### Lambda operator examples

The following example retrieves all account entity records that have at least one email with "sometext" in the subject:

```http
GET [Organization URI]/api/data/v9.2/accounts?$select=name
&$filter=Account_Emails/any(e:contains(e/subject,'sometext'))
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0
```

The following example retrieves all account entity records that have all associated tasks closed:

```http
GET [Organization URI]/api/data/v9.2/accounts?$select=name
&$filter=Account_Tasks/all(t:t/statecode eq 1)
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0
```

The following example retrieves all account entity records that have at least one email with "sometext" in the subject and whose state code is active:

```http
GET [Organization URI]/api/data/v9.2/accounts?$select=name
&$filter=Account_Emails/any(e:contains(e/subject,'sometext') and 
e/statecode eq 0)
Accept: application/json
OData-MaxVersion: 4.0
OData-Version: 4.0
```

The following example creates a nested query using `any` and `all` operators:

```http
GET [Organization URI]/api/data/v9.2/accounts?$select=name
&$filter=(contact_customer_accounts/any(c:c/jobtitle eq 'jobtitle' and 
c/opportunity_customer_contacts/any(o:o/description ne 'N/A'))) and 
endswith(name,'Inc.')
Accept: application/json
OData-MaxVersion: 4.0
OData-Version: 4.0
```

## Page results

Use the `Prefer: odata.maxpagesize` request header to control the number of records returned. If you don't specify a number, up to 5,000 records may be returned for each request. You can't request a page size larger than 5,000.

> [!NOTE]
> Dataverse doesn't support the `$skip` query option, so you can't use the the combination of `$top` and `$skip` for paging. More information: [Use the $top query option](#use-the-top-query-option)

The following example returns just the first two contact records:

**Request:**

```http
GET [Organization URI]/api/data/v9.2/contacts?$select=fullname
Accept: application/json
OData-MaxVersion: 4.0
OData-Version: 4.0
Prefer: odata.maxpagesize=2
```

**Response:**

```http
HTTP/1.1 200 OK
OData-Version: 4.0
Preference-Applied: odata.maxpagesize=2

{
    "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#contacts(fullname)",
    "value": [
        {
            "@odata.etag": "W/\"72201545\"",
            "fullname": "Yvonne McKay (sample)",
            "contactid": "49b0be2e-d01c-ed11-b83e-000d3a572421"
        },
        {
            "@odata.etag": "W/\"80648695\"",
            "fullname": "Susanna Stubberod (sample)",
            "contactid": "70bf4d48-34cb-ed11-b596-0022481d68cd"
        }
    ],
    "@odata.nextLink": "[Organization URI]/api/data/v9.2/contacts?$select=fullname&$skiptoken=%3Ccookie%20pagenumber=%222%22%20pagingcookie=%22%253ccookie%2520page%253d%25221%2522%253e%253ccontactid%2520last%253d%2522%257bD5026A4D-D01C-ED11-B83E-000D3A572421%257d%2522%2520first%253d%2522%257b49B0BE2E-D01C-ED11-B83E-000D3A572421%257d%2522%2520%252f%253e%253c%252fcookie%253e%22%20istracking=%22False%22%20/%3E"
}
```

When there are more records than requested, the `@odata.nextLink` annotation provides a URL you can use with `GET` to return the next page of data, as shown in the following example:

**Request:**

```http
GET [Organization URI]/api/data/v9.2/contacts?$select=fullname&$skiptoken=%3Ccookie%20pagenumber=%222%22%20pagingcookie=%22%253ccookie%2520page%253d%25221%2522%253e%253ccontactid%2520last%253d%2522%257bD5026A4D-D01C-ED11-B83E-000D3A572421%257d%2522%2520first%253d%2522%257b49B0BE2E-D01C-ED11-B83E-000D3A572421%257d%2522%2520%252f%253e%253c%252fcookie%253e%22%20istracking=%22False%22%20/%3E
Accept: application/json
OData-MaxVersion: 4.0
OData-Version: 4.0
Prefer: odata.maxpagesize=2
```

**Response:**

```http
HTTP/1.1 200 OK
OData-Version: 4.0
Preference-Applied: odata.maxpagesize=2

{
    "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#contacts(fullname)",
    "value": [
        {
            "@odata.etag": "W/\"80648710\"",
            "fullname": "Nancy Anderson (sample)",
            "contactid": "72bf4d48-34cb-ed11-b596-0022481d68cd"
        },
        {
            "@odata.etag": "W/\"80648724\"",
            "fullname": "Maria Campbell (sample)",
            "contactid": "74bf4d48-34cb-ed11-b596-0022481d68cd"
        }
    ],
    "@odata.nextLink": "[Organization URI]/api/data/v9.2/contacts?$select=fullname&$skiptoken=%3Ccookie%20pagenumber=%223%22%20pagingcookie=%22%253ccookie%2520page%253d%25222%2522%253e%253ccontactid%2520last%253d%2522%257bF2318099-171F-ED11-B83E-000D3A572421%257d%2522%2520first%253d%2522%257bBB55F942-161F-ED11-B83E-000D3A572421%257d%2522%2520%252f%253e%253c%252fcookie%253e%22%20istracking=%22False%22%20/%3E"
}
```

You should cache the results returned, or the `@odata.nextLink` URL value, and use it to return to previous pages.

Don't change the `@odata.nextLink` URL value or append any query options to it. For every subsequent request for more pages, you should use the same `odata.maxpagesize` preference value used in the original request. You can continue paging through the data until no `@odata.nextLink` annotation is included in the results.

In the earlier examples, encoded information was set as the value of the `$skiptoken` parameter in the `@odata.nextLink` URL value. The server sets this encoded information to control paging. You shouldn't modify the encoded information or encode it further. Use the URL value provided to retrieve the next page.

### Use the $top query option

Use the `$top` query option to limit the number of results returned. Don't use `$top` with the `Prefer: odata.maxpagesize` request header. If you include both, `$top` is ignored.

The following example returns just the first three account rows:

```http
GET [Organization URI]/api/data/v9.2/accounts?$select=name,revenue&$top=3
```

## Aggregate data

Use the `$apply` option to aggregate and group your data dynamically.

The aggregate functions are limited to a collection of 50,000 records.  Further information around using aggregate functionality with Dataverse can be found here: [Use FetchXML aggregation](../use-fetchxml-aggregation.md).

You can find more information about OData data aggregation here: [OData extension for data aggregation version 4.0](https://docs.oasis-open.org/odata/odata-data-aggregation-ext/v4.0/cs01/odata-data-aggregation-ext-v4.0-cs01.html). Dataverse supports only a subset of these aggregate methods.

Following are some examples:

- [List of unique statuses in the query](#list-of-unique-statuses-in-the-query)
- [Count by status values](#count-by-status-values)
- [Aggregate sum of revenue](#aggregate-sum-of-revenue)
- [Average revenue based on status](#average-revenue-based-on-status)
- [Sum of revenue based on status](#sum-of-revenue-based-on-status)
- [Total account revenue by primary contact name](#total-account-revenue-by-primary-contact-name)
- [Primary contact names for accounts in 'WA'](#primary-contact-names-for-accounts-in-wa)
- [Last created record date and time](#last-created-record-date-and-time)
- [First created record date and time](#first-created-record-date-and-time)

These samples don't show the complete request and response for brevity.

### List of unique statuses in the query

```http
GET accounts?$apply=groupby((statuscode))
Prefer: odata.include-annotations="OData.Community.Display.V1.FormattedValue"
```

**Response body**

```json
{
    "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#accounts",
    "value": [
        {
            "statuscode@OData.Community.Display.V1.FormattedValue": "Active",
            "statuscode": 1
        },
        {
            "statuscode@OData.Community.Display.V1.FormattedValue": "Inactive",
            "statuscode": 2
        }
    ]
}
```

### Count by status values

```http
GET accounts?$apply=groupby((statuscode),aggregate($count as count))
Prefer: odata.include-annotations="OData.Community.Display.V1.FormattedValue"
```

**Response body**

```json
{
    "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#accounts",
    "value": [
        {
            "statuscode@OData.Community.Display.V1.FormattedValue": "Active",
            "statuscode": 1,
            "count@OData.Community.Display.V1.FormattedValue": "8",
            "count": 8
        },
        {
            "statuscode@OData.Community.Display.V1.FormattedValue": "Inactive",
            "statuscode": 2,
            "count@OData.Community.Display.V1.FormattedValue": "1",
            "count": 1
        }
    ]
}
```

### Aggregate sum of revenue

```http
GET accounts?$apply=aggregate(revenue with sum as total)
Prefer: odata.include-annotations="OData.Community.Display.V1.FormattedValue"
```

**Response body**

```json
{
    "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#accounts",
    "value": [
        {
            "total@OData.Community.Display.V1.FormattedValue": "$440,000.00",
            "total": 440000.000000000
        }
    ]
}
```

### Average revenue based on status

```http
GET accounts?$apply=groupby((statuscode),aggregate(revenue with average as averagevalue))
Prefer: odata.include-annotations="OData.Community.Display.V1.FormattedValue"
```

**Response body**

```json
{
    "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#accounts",
    "value": [
        {
            "statuscode@OData.Community.Display.V1.FormattedValue": "Active",
            "statuscode": 1,
            "averagevalue@OData.Community.Display.V1.FormattedValue": "$53,750.00",
            "averagevalue": 53750.000000000
        },
        {
            "statuscode@OData.Community.Display.V1.FormattedValue": "Inactive",
            "statuscode": 2,
            "averagevalue@OData.Community.Display.V1.FormattedValue": "$10,000.00",
            "averagevalue": 10000.000000000
        }
    ]
}
```

### Sum of revenue based on status

```http
GET accounts?$apply=groupby((statuscode),aggregate(revenue with sum as total))
Prefer: odata.include-annotations="OData.Community.Display.V1.FormattedValue"
```

**Response body**

```json
{
    "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#accounts",
    "value": [
        {
            "statuscode@OData.Community.Display.V1.FormattedValue": "Active",
            "statuscode": 1,
            "total@OData.Community.Display.V1.FormattedValue": "$430,000.00",
            "total": 430000.000000000
        },
        {
            "statuscode@OData.Community.Display.V1.FormattedValue": "Inactive",
            "statuscode": 2,
            "total@OData.Community.Display.V1.FormattedValue": "$10,000.00",
            "total": 10000.000000000
        }
    ]
}
```

### Total account revenue by primary contact name

```http
GET accounts?$apply=groupby((primarycontactid/fullname),aggregate(revenue with sum as total))
Prefer: odata.include-annotations="OData.Community.Display.V1.FormattedValue"
```

**Response body**

```json
{
    "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#accounts",
    "value": [
        {
            "total@OData.Community.Display.V1.FormattedValue": "$10,000.00",
            "total": 10000.000000000,
            "contact_fullname": "Jim Glynn (sample)"
        },
        {
            "total@OData.Community.Display.V1.FormattedValue": "$80,000.00",
            "total": 80000.000000000,
            "contact_fullname": "Maria Campbell (sample)"
        },
      ... <truncated for brevity>
      
    ]
}
```

### Primary contact names for accounts in 'WA'

```http
GET accounts?$apply=filter(address1_stateorprovince eq 'WA')/groupby((primarycontactid/fullname))
```

**Response body**

```json
{
    "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#accounts",
    "value": [
        {
            "contact_fullname": "Rene Valdes (sample)"
        },
        {
            "contact_fullname": "Robert Lyon (sample)"
        },
        {
            "contact_fullname": "Scott Konersmann (sample)"
        }
    ]
}
```

### Last created record date and time

```http
GET accounts??$apply=aggregate(createdon with max as lastCreate)
Prefer: odata.include-annotations="OData.Community.Display.V1.FormattedValue"
```

**Response body**

```json
{
    "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#accounts",
    "value": [
        {
            "lastCreate@OData.Community.Display.V1.FormattedValue": "3/25/2023 10:42 AM",
            "lastCreate": "2023-03-25T17:42:47Z"
        }
    ]
}
```

### First created record date and time

```http
GET accounts?$apply=aggregate(createdon with min as firstCreate)
Prefer: odata.include-annotations="OData.Community.Display.V1.FormattedValue"
```

**Response body**

```json
{
    "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#accounts",
    "value": [
        {
            "firstCreate@OData.Community.Display.V1.FormattedValue": "3/25/2023 10:42 AM",
            "firstCreate": "2023-03-25T17:42:46Z"
        }
    ]
}
```

## Count number of rows

Use the `$count=true` query option to include a count of entities that match the filter criteria, up to 5,000.  

**Request:**

```http
GET [Organization URI]/api/data/v9.2/accounts?$select=accountid&$count=true
Accept: application/json
OData-MaxVersion: 4.0
OData-Version: 4.0
```

**Response:**

```http
HTTP/1.1 200 OK
OData-Version: 4.0

{
    "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#accounts(accountid)",
    "@odata.count": 9,
    "value": [
        {
            "@odata.etag": "W/\"81359849\"",
            "accountid": "78914942-34cb-ed11-b596-0022481d68cd"
        },
        ... <Truncated for brevity>
    ]
}
```

The response `@odata.count` annotation contains the number of rows, up to 5,000, that matches the filter criteria irrespective of the page size requested.
  
> [!NOTE]
> If you want to retrieve a snapshot within the past 24 hours of the total number of rows for a table beyond 5,000, use the [RetrieveTotalRecordCount function](xref:Microsoft.Dynamics.CRM.RetrieveTotalRecordCount). 
  

If the count value is 5,000 and you want to know whether the count is exactly 5,000 or greater than 5,000, you can add the following header:

```
Prefer: odata.include-annotations="Microsoft.Dynamics.CRM.totalrecordcount,Microsoft.Dynamics.CRM.totalrecordcountlimitexceeded"
```

This header adds the following annotations to the result:

- `@Microsoft.Dynamics.CRM.totalrecordcount`
- `@Microsoft.Dynamics.CRM.totalrecordcountlimitexceeded`


When used with the `$count=true` query option and there are more than 5,000 records, the following values are returned:

```
"@odata.count": 5000,
"@Microsoft.Dynamics.CRM.totalrecordcount": 5000,
"@Microsoft.Dynamics.CRM.totalrecordcountlimitexceeded": true,
```

If there are fewer than 5000 records, the actual count is returned.

```
"@odata.count": 58,
"@Microsoft.Dynamics.CRM.totalrecordcount": 58,
"@Microsoft.Dynamics.CRM.totalrecordcountlimitexceeded": false,
```

If you don't include the `$count=true` query option, the total `@Microsoft.Dynamics.CRM.totalrecordcount` value is `-1`.

The following example shows that there are 10 accounts that match the `$filter`, but only the first three accounts are returned:
  
 **Request:**

```http
GET [Organization URI]/api/data/v9.2/accounts?$select=name?
&$filter=contains(name,'sample')
&$count=true  
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
Prefer: odata.maxpagesize=3
Prefer: odata.include-annotations="Microsoft.Dynamics.CRM.*"
```  
  
 **Response:** 
 
```http
HTTP/1.1 200 OK  
Content-Type: application/json; odata.metadata=minimal  
OData-Version: 4.0  
Preference-Applied: odata.maxpagesize=3
Preference-Applied: odata.include-annotations="Microsoft.Dynamics.CRM.*"
  
{  
   "@odata.context":"[Organization URI]/api/data/v9.2/$metadata#accounts(name)",
   "@odata.count":10,
   "@Microsoft.Dynamics.CRM.totalrecordcount": 5000,
   "@Microsoft.Dynamics.CRM.totalrecordcountlimitexceeded": true,
   "value":[  
      {  
         "@odata.etag":"W/\"502482\"",
         "name":"Fourth Coffee (sample)",
         "accountid":"655eaf89-f083-e511-80d3-00155d2a68d3"
      },
      {  
         "@odata.etag":"W/\"502483\"",
         "name":"Litware, Inc. (sample)",
         "accountid":"675eaf89-f083-e511-80d3-00155d2a68d3"
      },
      {  
         "@odata.etag":"W/\"502484\"",
         "name":"Adventure Works (sample)",
         "accountid":"695eaf89-f083-e511-80d3-00155d2a68d3"
      }
   ],
   "@odata.nextLink":"[Organization URI]/api/data/v9.2/accounts?$select=name&$filter=contains(name,'sample')&$skiptoken=%3Ccookie%20pagenumber=%222%22%20pagingcookie=%22%253ccookie%2520page%253d%25221%2522%253e%253caccountid%2520last%253d%2522%257b695EAF89-F083-E511-80D3-00155D2A68D3%257d%2522%2520first%253d%2522%257b655EAF89-F083-E511-80D3-00155D2A68D3%257d%2522%2520%252f%253e%253c%252fcookie%253e%22%20istracking=%22False%22%20/%3E"
}

```  
  
To get just a number that represents the count of a collection, append `/$count`, as in the following example:
  
 **Request:**  

```http
GET [Organization URI]/api/data/v9.2/accounts/$count  
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
```  
  
 **Response:**

```http
HTTP/1.1 200 OK  
Content-Type: text/plain  
OData-Version: 4.0  
  
10  
```
### See also

[Search across table data using Dataverse search](relevance-search.md)  
[Work with Quick Find's search item limit](../quick-find-limit.md)  
[Web API query data sample (C#)](samples/webapiservice-query-data.md)<br />
[Web API query data sample (client-side JavaScript)](samples/query-data-client-side-javascript.md)<br />
[Perform operations using the Web API](perform-operations-web-api.md)<br />
[Compose HTTP requests and handle errors](compose-http-requests-handle-errors.md)<br />
