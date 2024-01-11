---
title: Web API query data sample
description: Use this sample code to learn how to query data using the Dataverse Web API. These samples use C# and client-side JavaScript.
ms.date: 04/14/2023
ms.topic: sample
author: divkamath
ms.author: dikamath
ms.reviewer: jdaly
search.audienceType: 
  - developer
contributors: 
  - JimDaly
---

# Web API query data sample

Use this group of sample code to learn how to query data using the Microsoft Dataverse Web API. This sample is implemented as a separate project for the following languages:

- [Query Data Sample (C#)](samples/webapiservice-query-data.md)
- [Web API Query Data Sample (Client-side JavaScript)](samples/query-data-client-side-javascript.md)

This topic describes a common set of operations implemented by each sample in this group. This topic describes the HTTP requests and responses and text output that each sample in this group will perform without the language specific details. See the language specific descriptions and the individual samples for details about how this operations are performed.

## Demonstrates

This sample is divided into the following principal sections, containing Web API query data operations which are discussed in greater detail in the associated conceptual topics.

|Topic section|Associated topic(s)|
|-------------------|---------------------------|
|[Section 1: Select specific properties](#section-1-select-specific-properties)|[Retrieve specific properties](retrieve-entity-using-web-api.md#bkmk_requestProperties)<br /> [Formatted values](query-data-web-api.md#formatted-values)|
|[Section 2: Use query functions](#section-2-use-query-functions)|[Filter rows](query-data-web-api.md#filter-rows)<br />[Use OData query functions](query-data-web-api.md#use-odata-query-functions)<br />[Compose a query with functions](use-web-api-functions.md#bkmk_composeQueryWithFunctions)<br /> <xref:Microsoft.Dynamics.CRM.QueryFunctionIndex>|
|[Section 3: Ordering and aliases](#section-3-ordering-and-aliases)|[Order rows](query-data-web-api.md#order-rows)<br /> [Filter rows](query-data-web-api.md#filter-rows)<br />|
|[Section 4: Limit and count results](#section-4-limit-and-count-results)|[Use the $top query option](query-data-web-api.md#use-the-top-query-option)<br />[Count number of rows](query-data-web-api.md#count-number-of-rows)|
|[Section 5: Pagination](#section-5-pagination)|[Page results](query-data-web-api.md#page-results)|
|[Section 6: Expand results](#section-6-expand-results)|[Join tables](query-data-web-api.md#join-tables)|
|[Section 7: Aggregate results](#section-7-aggregate-results)|[Aggregate data](query-data-web-api.md#aggregate-data)|
|[Section 8: FetchXML queries](#section-8-fetchxml-queries)|[FetchXML schema](../fetchxml-schema.md)<br /> [Use FetchXml with Web API](use-fetchxml-web-api.md)|
|[Section 9: Use predefined queries](#section-9-use-predefined-queries)|[Retrieve and execute predefined queries](retrieve-and-execute-predefined-queries.md)<br /> <xref:Microsoft.Dynamics.CRM.userquery?text=userquery EntityType><br /> <xref:Microsoft.Dynamics.CRM.savedquery?text=savedquery EntityType>|
|[Section 10: Delete sample records](#section-10-delete-sample-records)|[Basic delete](update-delete-entities-using-web-api.md#basic-delete)<br />[Execute batch operations using the Web API](execute-batch-operations-using-web-api.md)|

The following sections contain a brief discussion of the Dataverse Web API operations performed, along with the corresponding HTTP messages and associated console output.

<a name="bkmk_sampleData"></a>

## Section 0: Create records to query

The sample code creates a set of sample rows to query. The code deletes the data at the end unless you choose to keep it. You may get different results depending on existing data in your environment.
  
The data is added using *deep insert* in a single `POST` request and matches the following structure:  
  
```json  
{
  "name": "Contoso, Ltd. (sample)",
  "Account_Tasks": [
    {
      "subject": "Task 1 for Contoso, Ltd.",
      "description": "Task 1 for Contoso, Ltd. description",
      "actualdurationminutes": 10
    },
    {
      "subject": "Task 2 for Contoso, Ltd.",
      "description": "Task 2 for Contoso, Ltd. description",
      "actualdurationminutes": 10
    },
    {
      "subject": "Task 3 for Contoso, Ltd.",
      "description": "Task 3 for Contoso, Ltd. description",
      "actualdurationminutes": 10
    }
  ],
  "primarycontactid": {
    "firstname": "Yvonne",
    "lastname": "McKay (sample)",
    "jobtitle": "Coffee Master",
    "annualincome": 45000,
    "Contact_Tasks": [
      {
        "subject": "Task 1 for Yvonne McKay",
        "description": "Task 1 for Yvonne McKay description",
        "actualdurationminutes": 5
      },
      {
        "subject": "Task 2 for Yvonne McKay",
        "description": "Task 2 for Yvonne McKay description",
        "actualdurationminutes": 5
      },
      {
        "subject": "Task 3 for Yvonne McKay",
        "description": "Task 3 for Yvonne McKay description",
        "actualdurationminutes": 5
      }
    ]
  },
  "contact_customer_accounts": [
    {
      "firstname": "Susanna",
      "lastname": "Stubberod (sample)",
      "jobtitle": "Senior Purchaser",
      "annualincome": 52000,
      "Contact_Tasks": [
        {
          "subject": "Task 1 for Susanna Stubberod",
          "description": "Task 1 for Susanna Stubberod description",
          "actualdurationminutes": 3
        },
        {
          "subject": "Task 2 for Susanna Stubberod",
          "description": "Task 2 for Susanna Stubberod description",
          "actualdurationminutes": 3
        },
        {
          "subject": "Task 3 for Susanna Stubberod",
          "description": "Task 3 for Susanna Stubberod description",
          "actualdurationminutes": 3
        }
      ]
    },
    {
      "firstname": "Nancy",
      "lastname": "Anderson (sample)",
      "jobtitle": "Activities Manager",
      "annualincome": 55500,
      "Contact_Tasks": [
        {
          "subject": "Task 1 for Nancy Anderson",
          "description": "Task 1 for Nancy Anderson description",
          "actualdurationminutes": 4
        },
        {
          "subject": "Task 2 for Nancy Anderson",
          "description": "Task 2 for Nancy Anderson description",
          "actualdurationminutes": 4
        },
        {
          "subject": "Task 3 for Nancy Anderson",
          "description": "Task 3 for Nancy Anderson description",
          "actualdurationminutes": 4
        }
      ]
    },
    {
      "firstname": "Maria",
      "lastname": "Cambell (sample)",
      "jobtitle": "Accounts Manager",
      "annualincome": 31000,
      "Contact_Tasks": [
        {
          "subject": "Task 1 for Maria Cambell",
          "description": "Task 1 for Maria Cambell description",
          "actualdurationminutes": 5
        },
        {
          "subject": "Task 2 for Maria Cambell",
          "description": "Task 2 for Maria Cambell description",
          "actualdurationminutes": 5
        },
        {
          "subject": "Task 3 for Maria Cambell",
          "description": "Task 3 for Maria Cambell description",
          "actualdurationminutes": 5
        }
      ]
    },
    {
      "firstname": "Scott",
      "lastname": "Konersmann (sample)",
      "jobtitle": "Accounts Manager",
      "annualincome": 38000,
      "Contact_Tasks": [
        {
          "subject": "Task 1 for Scott Konersmann",
          "description": "Task 1 for Scott Konersmann description",
          "actualdurationminutes": 6
        },
        {
          "subject": "Task 2 for Scott Konersmann",
          "description": "Task 2 for Scott Konersmann description",
          "actualdurationminutes": 6
        },
        {
          "subject": "Task 3 for Scott Konersmann",
          "description": "Task 3 for Scott Konersmann description",
          "actualdurationminutes": 6
        }
      ]
    },
    {
      "firstname": "Robert",
      "lastname": "Lyon (sample)",
      "jobtitle": "Senior Technician",
      "annualincome": 78000,
      "Contact_Tasks": [
        {
          "subject": "Task 1 for Robert Lyon",
          "description": "Task 1 for Robert Lyon description",
          "actualdurationminutes": 7
        },
        {
          "subject": "Task 2 for Robert Lyon",
          "description": "Task 2 for Robert Lyon description",
          "actualdurationminutes": 7
        },
        {
          "subject": "Task 3 for Robert Lyon",
          "description": "Task 3 for Robert Lyon description",
          "actualdurationminutes": 7
        }
      ]
    },
    {
      "firstname": "Paul",
      "lastname": "Cannon (sample)",
      "jobtitle": "Ski Instructor",
      "annualincome": 68500,
      "Contact_Tasks": [
        {
          "subject": "Task 1 for Paul Cannon",
          "description": "Task 1 for Paul Cannon description",
          "actualdurationminutes": 8
        },
        {
          "subject": "Task 2 for Paul Cannon",
          "description": "Task 2 for Paul Cannon description",
          "actualdurationminutes": 8
        },
        {
          "subject": "Task 3 for Paul Cannon",
          "description": "Task 3 for Paul Cannon description",
          "actualdurationminutes": 8
        }
      ]
    },
    {
      "firstname": "Rene",
      "lastname": "Valdes (sample)",
      "jobtitle": "Data Analyst III",
      "annualincome": 86000,
      "Contact_Tasks": [
        {
          "subject": "Task 1 for Rene Valdes",
          "description": "Task 1 for Rene Valdes description",
          "actualdurationminutes": 9
        },
        {
          "subject": "Task 2 for Rene Valdes",
          "description": "Task 2 for Rene Valdes description",
          "actualdurationminutes": 9
        },
        {
          "subject": "Task 3 for Rene Valdes",
          "description": "Task 3 for Rene Valdes description",
          "actualdurationminutes": 9
        }
      ]
    },
    {
      "firstname": "Jim",
      "lastname": "Glynn (sample)",
      "jobtitle": "Senior International Sales Manager",
      "annualincome": 81400,
      "Contact_Tasks": [
        {
          "subject": "Task 1 for Jim Glynn",
          "description": "Task 1 for Jim Glynn description",
          "actualdurationminutes": 10
        },
        {
          "subject": "Task 2 for Jim Glynn",
          "description": "Task 2 for Jim Glynn description",
          "actualdurationminutes": 10
        },
        {
          "subject": "Task 3 for Jim Glynn",
          "description": "Task 3 for Jim Glynn description",
          "actualdurationminutes": 10
        }
      ]
    }
  ]
}  
```  
  
<a name="bkmk_selectproperties"></a>

## Section 1: Select specific properties

Always include the `$select` query option in your queries. If you don't, the server returns all properties of each table row, which reduces performance. [Learn how to select columns](query-data-web-api.md#select-columns).

This example demonstrates how to construct a basic query by selecting three properties of a [contact EntityType](xref:Microsoft.Dynamics.CRM.contact). The properties are `fullname`, `jobtitle`, `annualincome`. The section also illustrates the differences between [formatted](query-data-web-api.md#formatted-values) and unformatted values as seen in the results of the contact's `annualincome` property.
  
In this example, we are requesting for a specific contact. In this case, it's the primary contact of the account, `Yvonne McKay (sample)`.  
  
**Request:**

```http
GET [Organization Uri]/api/data/v9.2/contacts(81716234-9628-ed11-9db1-000d3a320482)?$select=fullname,jobtitle,annualincome HTTP/1.1
Prefer: odata.include-annotations="*"
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
```

**Response:**

```http
HTTP/1.1 200 OK
ETag: W/"1146626"
OData-Version: 4.0
Preference-Applied: odata.include-annotations="*"

{
  "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#contacts(fullname,jobtitle,annualincome)/$entity",
  "@odata.etag": "W/\"1146626\"",
  "fullname": "Yvonne McKay (sample)",
  "jobtitle": "Coffee Master",
  "annualincome@OData.Community.Display.V1.FormattedValue": "$45,000.00",
  "annualincome": 45000.0,
  "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
  "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
  "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
  "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
  "contactid": "81716234-9628-ed11-9db1-000d3a320482"
}
```
  
**Console output:**  
  
```text
Contact basic info:
        Fullname: Yvonne McKay (sample)
        Jobtitle: Coffee Master
        Annualincome (unformatted): 45000
        Annualincome (formatted): $45,000.00  
```  
  
<a name="bkmk_queryfunctions"></a>
  
## Section 2: Use query functions
 
Use filter options to set criteria for the results you want. You can  build simple to complex filters using a combination of query functions, comparison operators, and logical operators. More information: [Filter rows](query-data-web-api.md#filter-rows)  
  
Query functions are functions you can use as a filter criteria in a query. These functions accept parameters and return a `Boolean` value.There are standard query functions and Dataverse specific query functions.  This sample illustrates how to create a query for each type.  
  
### Standard query functions

Dataverse supports a subset of OData built-in query functions, specifically: `contains`, `endswith`, and `startswith`. For example, the `contains` standard query function allows you to filter for properties that match a string.  More information: [Use OData query functions](query-data-web-api.md#use-odata-query-functions)

In this operation, we are querying for all contacts with `fullname` containing the string `(sample)`.
  
**Request:**

```http
GET [Organization Uri]/api/data/v9.2/contacts?$select=fullname,jobtitle,annualincome&$filter=contains(fullname,'(sample)') and _parentcustomerid_value eq 7d716234-9628-ed11-9db1-000d3a320482 HTTP/1.1
Prefer: odata.include-annotations="*"
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
```

**Response:**

```http
HTTP/1.1 200 OK
OData-Version: 4.0
Preference-Applied: odata.include-annotations="*"

{
  "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#contacts(fullname,jobtitle,annualincome)",
  "@Microsoft.Dynamics.CRM.totalrecordcount": -1,
  "@Microsoft.Dynamics.CRM.totalrecordcountlimitexceeded": false,
  "@Microsoft.Dynamics.CRM.globalmetadataversion": "1144249",
  "value": [
    {
      "@odata.etag": "W/\"1146759\"",
      "fullname": "Susanna Stubberod (sample)",
      "jobtitle": "Senior Purchaser",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$52,000.00",
      "annualincome": 52000.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
      "contactid": "85716234-9628-ed11-9db1-000d3a320482"
    },
    {
      "@odata.etag": "W/\"1146761\"",
      "fullname": "Nancy Anderson (sample)",
      "jobtitle": "Activities Manager",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$55,500.00",
      "annualincome": 55500.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
      "contactid": "89716234-9628-ed11-9db1-000d3a320482"
    },
    {
      "@odata.etag": "W/\"1146763\"",
      "fullname": "Maria Cambell (sample)",
      "jobtitle": "Accounts Manager",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$31,000.00",
      "annualincome": 31000.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
      "contactid": "8d716234-9628-ed11-9db1-000d3a320482"
    },
    {
      "@odata.etag": "W/\"1146765\"",
      "fullname": "Scott Konersmann (sample)",
      "jobtitle": "Accounts Manager",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$38,000.00",
      "annualincome": 38000.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
      "contactid": "91716234-9628-ed11-9db1-000d3a320482"
    },
    {
      "@odata.etag": "W/\"1146767\"",
      "fullname": "Robert Lyon (sample)",
      "jobtitle": "Senior Technician",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$78,000.00",
      "annualincome": 78000.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
      "contactid": "95716234-9628-ed11-9db1-000d3a320482"
    },
    {
      "@odata.etag": "W/\"1146769\"",
      "fullname": "Paul Cannon (sample)",
      "jobtitle": "Ski Instructor",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$68,500.00",
      "annualincome": 68500.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
      "contactid": "99716234-9628-ed11-9db1-000d3a320482"
    },
    {
      "@odata.etag": "W/\"1146771\"",
      "fullname": "Rene Valdes (sample)",
      "jobtitle": "Data Analyst III",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$86,000.00",
      "annualincome": 86000.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
      "contactid": "9d716234-9628-ed11-9db1-000d3a320482"
    },
    {
      "@odata.etag": "W/\"1146773\"",
      "fullname": "Jim Glynn (sample)",
      "jobtitle": "Senior International Sales Manager",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$81,400.00",
      "annualincome": 81400.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
      "contactid": "a1716234-9628-ed11-9db1-000d3a320482"
    }
  ]
}
```

**Console output:**  
  
```text
Contacts filtered by fullname containing '(sample)':
        |Full Name                  |Job Title                          |Annual Income
        |---------------------------|-----------------------------------|---------------
        |Susanna Stubberod (sample) |Senior Purchaser                   |$52,000.00
        |Nancy Anderson (sample)    |Activities Manager                 |$55,500.00
        |Maria Cambell (sample)     |Accounts Manager                   |$31,000.00
        |Scott Konersmann (sample)  |Accounts Manager                   |$38,000.00
        |Robert Lyon (sample)       |Senior Technician                  |$78,000.00
        |Paul Cannon (sample)       |Ski Instructor                     |$68,500.00
        |Rene Valdes (sample)       |Data Analyst III                   |$86,000.00
        |Jim Glynn (sample)         |Senior International Sales Manager |$81,400.00
```  
  
### Dataverse query functions

Dataverse query functions provide a number of options to build queries that are relevant for Dataverse. For a complete list of these functions, refer to the <xref:Microsoft.Dynamics.CRM.QueryFunctionIndex>. More information: [Compose a query with functions](use-web-api-functions.md#bkmk_composeQueryWithFunctions)  
  
YDataverse query functions are similar to the standard query functions. The main difference is that when you use Dataverse query functions, you must provide the full name of the function, including the parameter name(s). For example, to get a list of contacts created in the last hour, you can build a query using the [LastXHours function](xref:Microsoft.Dynamics.CRM.LastXHours).  
  
**Request:**

```http
GET [Organization Uri]/api/data/v9.2/contacts?$select=fullname,jobtitle,annualincome&$filter=Microsoft.Dynamics.CRM.LastXHours(PropertyName=@p1,PropertyValue=@p2) and _parentcustomerid_value eq 7d716234-9628-ed11-9db1-000d3a320482&@p1='createdon'&@p2='1' HTTP/1.1
Prefer: odata.include-annotations="*"
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
```

**Response:**

```http
HTTP/1.1 200 OK
OData-Version: 4.0
Preference-Applied: odata.include-annotations="*"

{
  "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#contacts(fullname,jobtitle,annualincome)",
  "@Microsoft.Dynamics.CRM.totalrecordcount": -1,
  "@Microsoft.Dynamics.CRM.totalrecordcountlimitexceeded": false,
  "@Microsoft.Dynamics.CRM.globalmetadataversion": "1144249",
  "value": [
    {
      "@odata.etag": "W/\"1146759\"",
      "fullname": "Susanna Stubberod (sample)",
      "jobtitle": "Senior Purchaser",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$52,000.00",
      "annualincome": 52000.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
      "contactid": "85716234-9628-ed11-9db1-000d3a320482"
    },
    {
      "@odata.etag": "W/\"1146761\"",
      "fullname": "Nancy Anderson (sample)",
      "jobtitle": "Activities Manager",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$55,500.00",
      "annualincome": 55500.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
      "contactid": "89716234-9628-ed11-9db1-000d3a320482"
    },
    {
      "@odata.etag": "W/\"1146763\"",
      "fullname": "Maria Cambell (sample)",
      "jobtitle": "Accounts Manager",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$31,000.00",
      "annualincome": 31000.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
      "contactid": "8d716234-9628-ed11-9db1-000d3a320482"
    },
    {
      "@odata.etag": "W/\"1146765\"",
      "fullname": "Scott Konersmann (sample)",
      "jobtitle": "Accounts Manager",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$38,000.00",
      "annualincome": 38000.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
      "contactid": "91716234-9628-ed11-9db1-000d3a320482"
    },
    {
      "@odata.etag": "W/\"1146767\"",
      "fullname": "Robert Lyon (sample)",
      "jobtitle": "Senior Technician",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$78,000.00",
      "annualincome": 78000.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
      "contactid": "95716234-9628-ed11-9db1-000d3a320482"
    },
    {
      "@odata.etag": "W/\"1146769\"",
      "fullname": "Paul Cannon (sample)",
      "jobtitle": "Ski Instructor",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$68,500.00",
      "annualincome": 68500.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
      "contactid": "99716234-9628-ed11-9db1-000d3a320482"
    },
    {
      "@odata.etag": "W/\"1146771\"",
      "fullname": "Rene Valdes (sample)",
      "jobtitle": "Data Analyst III",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$86,000.00",
      "annualincome": 86000.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
      "contactid": "9d716234-9628-ed11-9db1-000d3a320482"
    },
    {
      "@odata.etag": "W/\"1146773\"",
      "fullname": "Jim Glynn (sample)",
      "jobtitle": "Senior International Sales Manager",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$81,400.00",
      "annualincome": 81400.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
      "contactid": "a1716234-9628-ed11-9db1-000d3a320482"
    }
  ]
}
```  
  
**Console output:**  
  
```text
Contacts that were created within the last 1hr:
        |Full Name                  |Job Title                          |Annual Income
        |---------------------------|-----------------------------------|---------------
        |Susanna Stubberod (sample) |Senior Purchaser                   |$52,000.00
        |Nancy Anderson (sample)    |Activities Manager                 |$55,500.00
        |Maria Cambell (sample)     |Accounts Manager                   |$31,000.00
        |Scott Konersmann (sample)  |Accounts Manager                   |$38,000.00
        |Robert Lyon (sample)       |Senior Technician                  |$78,000.00
        |Paul Cannon (sample)       |Ski Instructor                     |$68,500.00
        |Rene Valdes (sample)       |Data Analyst III                   |$86,000.00
        |Jim Glynn (sample)         |Senior International Sales Manager |$81,400.00
```  
  
<a name="bkmk_operators"></a>

### Use operators

Use [comparison operators](query-data-web-api.md#comparison-operators) and [logical operators](query-data-web-api.md#logical-operators) (`eq`,`ne`,`gt`,`ge`,`lt`,`le`,`and`,`or`,`not`)  to further refine your results. In this example, we're requesting a list of all contacts where `fullname` contains `(sample)` and the annual income is greater than `55000`.  
  
**Request:**

```http
GET [Organization Uri]/api/data/v9.2/contacts?$select=fullname,jobtitle,annualincome&$filter=contains(fullname,'(sample)') and annualincome gt 55000 and _parentcustomerid_value eq 7d716234-9628-ed11-9db1-000d3a320482 HTTP/1.1
Prefer: odata.include-annotations="*"
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
```

**Response:**

```http
HTTP/1.1 200 OK
OData-Version: 4.0
Preference-Applied: odata.include-annotations="*"

{
  "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#contacts(fullname,jobtitle,annualincome)",
  "@Microsoft.Dynamics.CRM.totalrecordcount": -1,
  "@Microsoft.Dynamics.CRM.totalrecordcountlimitexceeded": false,
  "@Microsoft.Dynamics.CRM.globalmetadataversion": "1144249",
  "value": [
    {
      "@odata.etag": "W/\"1146761\"",
      "fullname": "Nancy Anderson (sample)",
      "jobtitle": "Activities Manager",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$55,500.00",
      "annualincome": 55500.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
      "contactid": "89716234-9628-ed11-9db1-000d3a320482"
    },
    {
      "@odata.etag": "W/\"1146767\"",
      "fullname": "Robert Lyon (sample)",
      "jobtitle": "Senior Technician",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$78,000.00",
      "annualincome": 78000.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
      "contactid": "95716234-9628-ed11-9db1-000d3a320482"
    },
    {
      "@odata.etag": "W/\"1146769\"",
      "fullname": "Paul Cannon (sample)",
      "jobtitle": "Ski Instructor",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$68,500.00",
      "annualincome": 68500.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
      "contactid": "99716234-9628-ed11-9db1-000d3a320482"
    },
    {
      "@odata.etag": "W/\"1146771\"",
      "fullname": "Rene Valdes (sample)",
      "jobtitle": "Data Analyst III",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$86,000.00",
      "annualincome": 86000.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
      "contactid": "9d716234-9628-ed11-9db1-000d3a320482"
    },
    {
      "@odata.etag": "W/\"1146773\"",
      "fullname": "Jim Glynn (sample)",
      "jobtitle": "Senior International Sales Manager",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$81,400.00",
      "annualincome": 81400.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
      "contactid": "a1716234-9628-ed11-9db1-000d3a320482"
    }
  ]
}
```  
  
**Console output:**
  
```text
Contacts with '(sample)' in name and income above $55,000:
        |Full Name                  |Job Title                          |Annual Income
        |---------------------------|-----------------------------------|---------------
        |Nancy Anderson (sample)    |Activities Manager                 |$55,500.00
        |Robert Lyon (sample)       |Senior Technician                  |$78,000.00
        |Paul Cannon (sample)       |Ski Instructor                     |$68,500.00
        |Rene Valdes (sample)       |Data Analyst III                   |$86,000.00
        |Jim Glynn (sample)         |Senior International Sales Manager |$81,400.00
```  
  
<a name="bkmk_prededence"></a>
   
### Set precedence
 
Since all operators have the same precedence, use parentheses to establish the order in which query conditions are evaluated. Filters are applied from left to right. The order in which statements appear in the filter can affect the results.
  
In this example, we're requesting a list of all contacts where `fullname` contains `(sample)`, `jobtitle` contains either `senior` or `manager`, and `annualincome` is greater than `55000`. To get the results we want, we must use parentheses to group the `jobtitle` filters. If we don't, the `or` operator has the same precedence as the `and` operators. The query in this example looks like this: `$filter=contains(fullname,'(sample)') and (contains(jobtitle,'senior') or contains(jobtitle,'manager')) and annualincome gt 55000`.
  
**Request:**

```http
GET [Organization Uri]/api/data/v9.2/contacts?$select=fullname,jobtitle,annualincome&$filter=contains(fullname,'(sample)') and (contains(jobtitle, 'senior') or contains(jobtitle,'manager')) and annualincome gt 55000 and _parentcustomerid_value eq 7d716234-9628-ed11-9db1-000d3a320482 HTTP/1.1
Prefer: odata.include-annotations="*"
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
```

**Response:**

```http
HTTP/1.1 200 OK
OData-Version: 4.0
Preference-Applied: odata.include-annotations="*"

{
  "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#contacts(fullname,jobtitle,annualincome)",
  "@Microsoft.Dynamics.CRM.totalrecordcount": -1,
  "@Microsoft.Dynamics.CRM.totalrecordcountlimitexceeded": false,
  "@Microsoft.Dynamics.CRM.globalmetadataversion": "1144249",
  "value": [
    {
      "@odata.etag": "W/\"1146761\"",
      "fullname": "Nancy Anderson (sample)",
      "jobtitle": "Activities Manager",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$55,500.00",
      "annualincome": 55500.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
      "contactid": "89716234-9628-ed11-9db1-000d3a320482"
    },
    {
      "@odata.etag": "W/\"1146767\"",
      "fullname": "Robert Lyon (sample)",
      "jobtitle": "Senior Technician",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$78,000.00",
      "annualincome": 78000.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
      "contactid": "95716234-9628-ed11-9db1-000d3a320482"
    },
    {
      "@odata.etag": "W/\"1146773\"",
      "fullname": "Jim Glynn (sample)",
      "jobtitle": "Senior International Sales Manager",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$81,400.00",
      "annualincome": 81400.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
      "contactid": "a1716234-9628-ed11-9db1-000d3a320482"
    }
  ]
}
```
  
**Console output:**  
  
```text
Contacts with '(sample)' in name senior jobtitle or high income:
        |Full Name                  |Job Title                          |Annual Income
        |---------------------------|-----------------------------------|---------------
        |Nancy Anderson (sample)    |Activities Manager                 |$55,500.00
        |Robert Lyon (sample)       |Senior Technician                  |$78,000.00
        |Jim Glynn (sample)         |Senior International Sales Manager |$81,400.00
```  


## Section 3: Ordering and aliases

<a name="bkmk_orderresults"></a>

### Order results

To sort results in ascending or descending order, use the `$orderby` filter option . In this example, we will query for all contacts with `fullname` containing `(sample)` and request the data in ascending order based on the `jobtitle` property value and then in  descending order based on the `annualincome` property value using this syntax: `$orderby=jobtitle asc, annualincome desc`. More information: [Order rows](query-data-web-api.md#order-rows)  
  
**Request:**

```http
GET [Organization Uri]/api/data/v9.2/contacts?$select=fullname,jobtitle,annualincome&$filter=contains(fullname,'(sample)') and _parentcustomerid_value eq 7d716234-9628-ed11-9db1-000d3a320482&$orderby=jobtitle asc, annualincome desc HTTP/1.1
Prefer: odata.include-annotations="*"
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
```

**Response:**

```http
HTTP/1.1 200 OK
OData-Version: 4.0
Preference-Applied: odata.include-annotations="*"

{
  "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#contacts(fullname,jobtitle,annualincome)",
  "@Microsoft.Dynamics.CRM.totalrecordcount": -1,
  "@Microsoft.Dynamics.CRM.totalrecordcountlimitexceeded": false,
  "@Microsoft.Dynamics.CRM.globalmetadataversion": "1144249",
  "value": [
    {
      "@odata.etag": "W/\"1146765\"",
      "fullname": "Scott Konersmann (sample)",
      "jobtitle": "Accounts Manager",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$38,000.00",
      "annualincome": 38000.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
      "contactid": "91716234-9628-ed11-9db1-000d3a320482"
    },
    {
      "@odata.etag": "W/\"1146763\"",
      "fullname": "Maria Cambell (sample)",
      "jobtitle": "Accounts Manager",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$31,000.00",
      "annualincome": 31000.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
      "contactid": "8d716234-9628-ed11-9db1-000d3a320482"
    },
    {
      "@odata.etag": "W/\"1146761\"",
      "fullname": "Nancy Anderson (sample)",
      "jobtitle": "Activities Manager",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$55,500.00",
      "annualincome": 55500.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
      "contactid": "89716234-9628-ed11-9db1-000d3a320482"
    },
    {
      "@odata.etag": "W/\"1146771\"",
      "fullname": "Rene Valdes (sample)",
      "jobtitle": "Data Analyst III",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$86,000.00",
      "annualincome": 86000.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
      "contactid": "9d716234-9628-ed11-9db1-000d3a320482"
    },
    {
      "@odata.etag": "W/\"1146773\"",
      "fullname": "Jim Glynn (sample)",
      "jobtitle": "Senior International Sales Manager",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$81,400.00",
      "annualincome": 81400.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
      "contactid": "a1716234-9628-ed11-9db1-000d3a320482"
    },
    {
      "@odata.etag": "W/\"1146759\"",
      "fullname": "Susanna Stubberod (sample)",
      "jobtitle": "Senior Purchaser",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$52,000.00",
      "annualincome": 52000.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
      "contactid": "85716234-9628-ed11-9db1-000d3a320482"
    },
    {
      "@odata.etag": "W/\"1146767\"",
      "fullname": "Robert Lyon (sample)",
      "jobtitle": "Senior Technician",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$78,000.00",
      "annualincome": 78000.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
      "contactid": "95716234-9628-ed11-9db1-000d3a320482"
    },
    {
      "@odata.etag": "W/\"1146769\"",
      "fullname": "Paul Cannon (sample)",
      "jobtitle": "Ski Instructor",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$68,500.00",
      "annualincome": 68500.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
      "contactid": "99716234-9628-ed11-9db1-000d3a320482"
    }
  ]
}
```
  
**Console output:**  
  
```text
Contacts ordered by jobtitle (Ascending) and annualincome (descending)
        |Full Name                  |Job Title                          |Annual Income
        |---------------------------|-----------------------------------|---------------
        |Scott Konersmann (sample)  |Accounts Manager                   |$38,000.00
        |Maria Cambell (sample)     |Accounts Manager                   |$31,000.00
        |Nancy Anderson (sample)    |Activities Manager                 |$55,500.00
        |Rene Valdes (sample)       |Data Analyst III                   |$86,000.00
        |Jim Glynn (sample)         |Senior International Sales Manager |$81,400.00
        |Susanna Stubberod (sample) |Senior Purchaser                   |$52,000.00
        |Robert Lyon (sample)       |Senior Technician                  |$78,000.00
        |Paul Cannon (sample)       |Ski Instructor                     |$68,500.00
```  
  
<a name="bkmk_parameteralias"></a>

### Parameter alias

Use [parameter aliases](query-data-web-api.md#use-parameter-aliases-with-query-options) to more easily reuse parameters in your filters. You can use aliases in `$filter` and `$orderby` options. If the alias isn't assigned a value, it's assumed to be null.

You can also use parameter aliases when you [call functions](use-web-api-functions.md). For example, we can rewrite the query in the previous order results operation to use parameters and get the same output.
  
**Request:**

```http
GET [Organization Uri]/api/data/v9.2/contacts?$select=fullname,jobtitle,annualincome&$filter=contains(@p1,'(sample)') and @p2 eq @p3&$orderby=@p4 asc, @p5 desc&@p1=fullname&@p2=_parentcustomerid_value&@p3=7d716234-9628-ed11-9db1-000d3a320482&@p4=jobtitle&@p5=annualincome HTTP/1.1
Prefer: odata.include-annotations="*"
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
```

**Response:**

```http
HTTP/1.1 200 OK
OData-Version: 4.0
Preference-Applied: odata.include-annotations="*"

{
  "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#contacts(fullname,jobtitle,annualincome)",
  "@Microsoft.Dynamics.CRM.totalrecordcount": -1,
  "@Microsoft.Dynamics.CRM.totalrecordcountlimitexceeded": false,
  "@Microsoft.Dynamics.CRM.globalmetadataversion": "1144249",
  "value": [
    {
      "@odata.etag": "W/\"1146765\"",
      "fullname": "Scott Konersmann (sample)",
      "jobtitle": "Accounts Manager",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$38,000.00",
      "annualincome": 38000.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
      "contactid": "91716234-9628-ed11-9db1-000d3a320482"
    },
    {
      "@odata.etag": "W/\"1146763\"",
      "fullname": "Maria Cambell (sample)",
      "jobtitle": "Accounts Manager",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$31,000.00",
      "annualincome": 31000.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
      "contactid": "8d716234-9628-ed11-9db1-000d3a320482"
    },
    {
      "@odata.etag": "W/\"1146761\"",
      "fullname": "Nancy Anderson (sample)",
      "jobtitle": "Activities Manager",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$55,500.00",
      "annualincome": 55500.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
      "contactid": "89716234-9628-ed11-9db1-000d3a320482"
    },
    {
      "@odata.etag": "W/\"1146771\"",
      "fullname": "Rene Valdes (sample)",
      "jobtitle": "Data Analyst III",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$86,000.00",
      "annualincome": 86000.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
      "contactid": "9d716234-9628-ed11-9db1-000d3a320482"
    },
    {
      "@odata.etag": "W/\"1146773\"",
      "fullname": "Jim Glynn (sample)",
      "jobtitle": "Senior International Sales Manager",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$81,400.00",
      "annualincome": 81400.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
      "contactid": "a1716234-9628-ed11-9db1-000d3a320482"
    },
    {
      "@odata.etag": "W/\"1146759\"",
      "fullname": "Susanna Stubberod (sample)",
      "jobtitle": "Senior Purchaser",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$52,000.00",
      "annualincome": 52000.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
      "contactid": "85716234-9628-ed11-9db1-000d3a320482"
    },
    {
      "@odata.etag": "W/\"1146767\"",
      "fullname": "Robert Lyon (sample)",
      "jobtitle": "Senior Technician",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$78,000.00",
      "annualincome": 78000.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
      "contactid": "95716234-9628-ed11-9db1-000d3a320482"
    },
    {
      "@odata.etag": "W/\"1146769\"",
      "fullname": "Paul Cannon (sample)",
      "jobtitle": "Ski Instructor",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$68,500.00",
      "annualincome": 68500.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
      "contactid": "99716234-9628-ed11-9db1-000d3a320482"
    }
  ]
}
```  
  
**Console output:**  
  
```text
Contacts ordered by jobtitle (Ascending) and annualincome (descending)
        |Full Name                  |Job Title                          |Annual Income
        |---------------------------|-----------------------------------|---------------
        |Scott Konersmann (sample)  |Accounts Manager                   |$38,000.00
        |Maria Cambell (sample)     |Accounts Manager                   |$31,000.00
        |Nancy Anderson (sample)    |Activities Manager                 |$55,500.00
        |Rene Valdes (sample)       |Data Analyst III                   |$86,000.00
        |Jim Glynn (sample)         |Senior International Sales Manager |$81,400.00
        |Susanna Stubberod (sample) |Senior Purchaser                   |$52,000.00
        |Robert Lyon (sample)       |Senior Technician                  |$78,000.00
        |Paul Cannon (sample)       |Ski Instructor                     |$68,500.00
```  
  
<a name="bkmk_limitresults"></a>

## Section 4: Limit and count results

As a best practice, don't return more data than you need. To protect performance, the server returns a maximum of 5,000 table rows per request.

To limit the number of results returned, [use the `$top` query option](query-data-web-api.md#use-the-top-query-option) or add [`odata.maxpagesize`](#bkmk_filterPagination) in the request header. The `$top` query option returns the top number of rows from the result set and ignores the rest. The `odata.maxpagesize` request header specifies the number of rows to return per page with an `@odata.nextLink` property to get the results of the next page. [Learn more about page results](query-data-web-api.md#page-results).
  
<a name="bkmk_topResults"></a>
 
### Top results

We can apply the `$top` query option to limit the basic query operation to the first five contacts with `fullname` containing `(sample)`. In this case, the request actually produces at least 10 results, but only the first 5 entries are returned in the response.  
  
**Request:**

```http
GET [Organization Uri]/api/data/v9.2/contacts?$select=fullname,jobtitle,annualincome&$filter=contains(fullname,'(sample)') and _parentcustomerid_value eq 7d716234-9628-ed11-9db1-000d3a320482&$top=5 HTTP/1.1
Prefer: odata.include-annotations="*"
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
```

**Response:**

```http
HTTP/1.1 200 OK
OData-Version: 4.0
Preference-Applied: odata.include-annotations="*"

{
  "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#contacts(fullname,jobtitle,annualincome)",
  "@Microsoft.Dynamics.CRM.totalrecordcount": -1,
  "@Microsoft.Dynamics.CRM.totalrecordcountlimitexceeded": false,
  "@Microsoft.Dynamics.CRM.globalmetadataversion": "1144249",
  "value": [
    {
      "@odata.etag": "W/\"1146759\"",
      "fullname": "Susanna Stubberod (sample)",
      "jobtitle": "Senior Purchaser",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$52,000.00",
      "annualincome": 52000.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
      "contactid": "85716234-9628-ed11-9db1-000d3a320482"
    },
    {
      "@odata.etag": "W/\"1146761\"",
      "fullname": "Nancy Anderson (sample)",
      "jobtitle": "Activities Manager",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$55,500.00",
      "annualincome": 55500.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
      "contactid": "89716234-9628-ed11-9db1-000d3a320482"
    },
    {
      "@odata.etag": "W/\"1146763\"",
      "fullname": "Maria Cambell (sample)",
      "jobtitle": "Accounts Manager",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$31,000.00",
      "annualincome": 31000.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
      "contactid": "8d716234-9628-ed11-9db1-000d3a320482"
    },
    {
      "@odata.etag": "W/\"1146765\"",
      "fullname": "Scott Konersmann (sample)",
      "jobtitle": "Accounts Manager",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$38,000.00",
      "annualincome": 38000.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
      "contactid": "91716234-9628-ed11-9db1-000d3a320482"
    },
    {
      "@odata.etag": "W/\"1146767\"",
      "fullname": "Robert Lyon (sample)",
      "jobtitle": "Senior Technician",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$78,000.00",
      "annualincome": 78000.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
      "contactid": "95716234-9628-ed11-9db1-000d3a320482"
    }
  ]
}
```
  
**Console output:**  
  
```text
Contacts top 5 results:
        |Full Name                  |Job Title                          |Annual Income
        |---------------------------|-----------------------------------|---------------
        |Susanna Stubberod (sample) |Senior Purchaser                   |$52,000.00
        |Nancy Anderson (sample)    |Activities Manager                 |$55,500.00
        |Maria Cambell (sample)     |Accounts Manager                   |$31,000.00
        |Scott Konersmann (sample)  |Accounts Manager                   |$38,000.00
        |Robert Lyon (sample)       |Senior Technician                  |$78,000.00
``` 

### Collection count

If you just want the number of records in a collection, append `/$count` to the collection URL. The maximum value is 5,000.

**Request:**

```http
GET [Organization Uri]/api/data/v9.2/contacts/$count HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
```

**Response:**

```http
HTTP/1.1 200 OK
OData-Version: 4.0

9
```

**Console output:**  
  
```text
The contacts collection has 9 contacts.
```  
  
<a name="bkmk_resultCount"></a>

### Result count

You can get [the count of rows](query-data-web-api.md#count-number-of-rows) from a collection-valued property or a count of matched table rows in a filter. The count tells you the number of possible rows in your result. However, Dataverse returns 5,000 as the maximum count even if the result may have more.

In this example, we build a filter where `jobtitle` contains either `Senior` or `Manager` and we also request a `$count` of the result. The response contains the count in the `@odata.count` property along with the results of the query.
  
**Request:**

```http
GET [Organization Uri]/api/data/v9.2/contacts?$select=fullname,jobtitle,annualincome&$filter=(contains(jobtitle,'senior') or contains(jobtitle, 'manager')) and _parentcustomerid_value eq 7d716234-9628-ed11-9db1-000d3a320482&$count=true HTTP/1.1
Prefer: odata.include-annotations="*"
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
```

**Response:**

```http
HTTP/1.1 200 OK
OData-Version: 4.0
Preference-Applied: odata.include-annotations="*"

{
  "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#contacts(fullname,jobtitle,annualincome)",
  "@odata.count": 6,
  "@Microsoft.Dynamics.CRM.totalrecordcount": 6,
  "@Microsoft.Dynamics.CRM.totalrecordcountlimitexceeded": false,
  "@Microsoft.Dynamics.CRM.globalmetadataversion": "1144249",
  "value": [
    {
      "@odata.etag": "W/\"1146759\"",
      "fullname": "Susanna Stubberod (sample)",
      "jobtitle": "Senior Purchaser",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$52,000.00",
      "annualincome": 52000.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
      "contactid": "85716234-9628-ed11-9db1-000d3a320482"
    },
    {
      "@odata.etag": "W/\"1146761\"",
      "fullname": "Nancy Anderson (sample)",
      "jobtitle": "Activities Manager",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$55,500.00",
      "annualincome": 55500.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
      "contactid": "89716234-9628-ed11-9db1-000d3a320482"
    },
    {
      "@odata.etag": "W/\"1146763\"",
      "fullname": "Maria Cambell (sample)",
      "jobtitle": "Accounts Manager",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$31,000.00",
      "annualincome": 31000.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
      "contactid": "8d716234-9628-ed11-9db1-000d3a320482"
    },
    {
      "@odata.etag": "W/\"1146765\"",
      "fullname": "Scott Konersmann (sample)",
      "jobtitle": "Accounts Manager",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$38,000.00",
      "annualincome": 38000.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
      "contactid": "91716234-9628-ed11-9db1-000d3a320482"
    },
    {
      "@odata.etag": "W/\"1146767\"",
      "fullname": "Robert Lyon (sample)",
      "jobtitle": "Senior Technician",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$78,000.00",
      "annualincome": 78000.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
      "contactid": "95716234-9628-ed11-9db1-000d3a320482"
    },
    {
      "@odata.etag": "W/\"1146773\"",
      "fullname": "Jim Glynn (sample)",
      "jobtitle": "Senior International Sales Manager",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$81,400.00",
      "annualincome": 81400.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
      "contactid": "a1716234-9628-ed11-9db1-000d3a320482"
    }
  ]
}
```  
  
**Console output:**  
  
```text
6 Contacts with 'senior' or 'manager' in job title:
        |Full Name                  |Job Title                          |Annual Income
        |---------------------------|-----------------------------------|---------------
        |Susanna Stubberod (sample) |Senior Purchaser                   |$52,000.00
        |Nancy Anderson (sample)    |Activities Manager                 |$55,500.00
        |Maria Cambell (sample)     |Accounts Manager                   |$31,000.00
        |Scott Konersmann (sample)  |Accounts Manager                   |$38,000.00
        |Robert Lyon (sample)       |Senior Technician                  |$78,000.00
        |Jim Glynn (sample)         |Senior International Sales Manager |$81,400.00
```  
  
<a name="bkmk_filterPagination"></a>

## Section 5: Pagination

Some queries return a large number of rows, and it's easier to view them one page at a time. To [retrieve paginated results](query-data-web-api.md#page-results), use the `odata.maxpagesize` option instead of `$top`.
  
In this example, we ask for a `$count` and set the `odata.maxpagesize` to `4`. This filter matches 10 contacts, but we're only retrieving 4 at a time. We also use the count and the max page size to figure out how many pages there are. The result of the first page is returned in this request.
  
**Request:**

```http
GET [Organization Uri]/api/data/v9.2/contacts?$select=fullname,jobtitle,annualincome&$filter=contains(fullname,'(sample)')&$count=true HTTP/1.1
Prefer: odata.maxpagesize=4; odata.include-annotations="*"
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
```

**Response:**

```http
HTTP/1.1 200 OK
OData-Version: 4.0
Preference-Applied: odata.include-annotations="*"; odata.maxpagesize=4

{
  "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#contacts(fullname,jobtitle,annualincome)",
  "@odata.count": 9,
  "@Microsoft.Dynamics.CRM.totalrecordcount": 9,
  "@Microsoft.Dynamics.CRM.totalrecordcountlimitexceeded": false,
  "@Microsoft.Dynamics.CRM.globalmetadataversion": "1144249",
  "value": [
    {
      "@odata.etag": "W/\"1146626\"",
      "fullname": "Yvonne McKay (sample)",
      "jobtitle": "Coffee Master",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$45,000.00",
      "annualincome": 45000.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
      "contactid": "81716234-9628-ed11-9db1-000d3a320482"
    },
    {
      "@odata.etag": "W/\"1146759\"",
      "fullname": "Susanna Stubberod (sample)",
      "jobtitle": "Senior Purchaser",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$52,000.00",
      "annualincome": 52000.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
      "contactid": "85716234-9628-ed11-9db1-000d3a320482"
    },
    {
      "@odata.etag": "W/\"1146761\"",
      "fullname": "Nancy Anderson (sample)",
      "jobtitle": "Activities Manager",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$55,500.00",
      "annualincome": 55500.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
      "contactid": "89716234-9628-ed11-9db1-000d3a320482"
    },
    {
      "@odata.etag": "W/\"1146763\"",
      "fullname": "Maria Cambell (sample)",
      "jobtitle": "Accounts Manager",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$31,000.00",
      "annualincome": 31000.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
      "contactid": "8d716234-9628-ed11-9db1-000d3a320482"
    }
  ],
  "@odata.nextLink": "[Organization Uri]/api/data/v9.2/contacts?$select=fullname,jobtitle,annualincome&$filter=contains(fullname,'(sample)')&$count=true&$skiptoken=%3Ccookie%20pagenumber=%222%22%20pagingcookie=%22%253ccookie%2520page%253d%25221%2522%253e%253ccontactid%2520last%253d%2522%257b8D716234-9628-ED11-9DB1-000D3A320482%257d%2522%2520first%253d%2522%257b81716234-9628-ED11-9DB1-000D3A320482%257d%2522%2520%252f%253e%253c%252fcookie%253e%22%20istracking=%22False%22%20/%3E"
}
```
  
**Console output:**  
  
```text
Contacts total: 9    Contacts per page: 4.
Page 1 of 3:
        |Full Name                  |Job Title                          |Annual Income
        |---------------------------|-----------------------------------|---------------
        |Yvonne McKay (sample)      |Coffee Master                      |$45,000.00
        |Susanna Stubberod (sample) |Senior Purchaser                   |$52,000.00
        |Nancy Anderson (sample)    |Activities Manager                 |$55,500.00
        |Maria Cambell (sample)     |Accounts Manager                   |$31,000.00
```  
  
To retrieve page 2, use a `GET` request with the value of the  `@odata.nextLink` property.  
  
**Request:**

```http
GET [Organization Uri]/api/data/v9.2/contacts?$select=fullname,jobtitle,annualincome&$filter=contains(fullname,'(sample)')&$count=true&$skiptoken=<cookie pagenumber="2" pagingcookie="%3ccookie%20page%3d%221%22%3e%3ccontactid%20last%3d%22%7b8D716234-9628-ED11-9DB1-000D3A320482%7d%22%20first%3d%22%7b81716234-9628-ED11-9DB1-000D3A320482%7d%22%20%2f%3e%3c%2fcookie%3e" istracking="False" /> HTTP/1.1
Prefer: odata.maxpagesize=4; odata.include-annotations="*"
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
```

**Response:**

```http
HTTP/1.1 200 OK
OData-Version: 4.0
Preference-Applied: odata.include-annotations="*"; odata.maxpagesize=4

{
  "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#contacts(fullname,jobtitle,annualincome)",
  "@odata.count": 9,
  "@Microsoft.Dynamics.CRM.totalrecordcount": 9,
  "@Microsoft.Dynamics.CRM.totalrecordcountlimitexceeded": false,
  "@Microsoft.Dynamics.CRM.globalmetadataversion": "1144249",
  "value": [
    {
      "@odata.etag": "W/\"1146765\"",
      "fullname": "Scott Konersmann (sample)",
      "jobtitle": "Accounts Manager",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$38,000.00",
      "annualincome": 38000.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
      "contactid": "91716234-9628-ed11-9db1-000d3a320482"
    },
    {
      "@odata.etag": "W/\"1146767\"",
      "fullname": "Robert Lyon (sample)",
      "jobtitle": "Senior Technician",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$78,000.00",
      "annualincome": 78000.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
      "contactid": "95716234-9628-ed11-9db1-000d3a320482"
    },
    {
      "@odata.etag": "W/\"1146769\"",
      "fullname": "Paul Cannon (sample)",
      "jobtitle": "Ski Instructor",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$68,500.00",
      "annualincome": 68500.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
      "contactid": "99716234-9628-ed11-9db1-000d3a320482"
    },
    {
      "@odata.etag": "W/\"1146771\"",
      "fullname": "Rene Valdes (sample)",
      "jobtitle": "Data Analyst III",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$86,000.00",
      "annualincome": 86000.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
      "contactid": "9d716234-9628-ed11-9db1-000d3a320482"
    }
  ],
  "@odata.nextLink": "[Organization Uri]/api/data/v9.2/contacts?$select=fullname,jobtitle,annualincome&$filter=contains(fullname,'(sample)')&$count=true&$skiptoken=%3Ccookie%20pagenumber=%223%22%20pagingcookie=%22%253ccookie%2520page%253d%25222%2522%253e%253ccontactid%2520last%253d%2522%257b9D716234-9628-ED11-9DB1-000D3A320482%257d%2522%2520first%253d%2522%257b91716234-9628-ED11-9DB1-000D3A320482%257d%2522%2520%252f%253e%253c%252fcookie%253e%22%20istracking=%22False%22%20/%3E"
}
```  
  
   **Console output:**
  
```text
Page 2 of 3:
        |Full Name                  |Job Title                          |Annual Income
        |---------------------------|-----------------------------------|---------------
        |Scott Konersmann (sample)  |Accounts Manager                   |$38,000.00
        |Robert Lyon (sample)       |Senior Technician                  |$78,000.00
        |Paul Cannon (sample)       |Ski Instructor                     |$68,500.00
        |Rene Valdes (sample)       |Data Analyst III                   |$86,000.00
```  
  
<a name="bkmk_expandresults"></a>

## Section 6: Expand results

To retrieve information on associated table rows, use the `$expand` query option on navigation properties. More information: [Join Tables](query-data-web-api.md#join-tables)
  
### Expand on single-valued navigation property

A single-valued navigation property represents a many-to-one relationship. In our sample data, the account has a relationship with a contact through the `primarycontactid` column, or attribute. In this relationship, the account can have only one primary contact. Using the [account EntityType](xref:Microsoft.Dynamics.CRM.account), we can create a query to get information about the account and expanded information about its primary contact.
  
**Request:**

```http
GET [Organization Uri]/api/data/v9.2/accounts(7d716234-9628-ed11-9db1-000d3a320482)?$select=name&$expand=primarycontactid($select=fullname,jobtitle,annualincome) HTTP/1.1
Prefer: odata.include-annotations="*"
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
```

**Response:**

```http
HTTP/1.1 200 OK
ETag: W/"1146751"
OData-Version: 4.0
Preference-Applied: odata.include-annotations="*"

{
  "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#accounts(name,primarycontactid(fullname,jobtitle,annualincome))/$entity",
  "@odata.etag": "W/\"1146751\"",
  "name": "Contoso, Ltd. (sample)",
  "accountid": "7d716234-9628-ed11-9db1-000d3a320482",
  "primarycontactid": {
    "@odata.etag": "W/\"1146626\"",
    "fullname": "Yvonne McKay (sample)",
    "jobtitle": "Coffee Master",
    "annualincome@OData.Community.Display.V1.FormattedValue": "$45,000.00",
    "annualincome": 45000.0,
    "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
    "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
    "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
    "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
    "contactid": "81716234-9628-ed11-9db1-000d3a320482"
  }
}
```
  
**Console output:**  
  
```text
Account Contoso, Ltd. (sample) has the following primary contact person:
        Fullname: Yvonne McKay (sample)
        Jobtitle: Coffee Master
        Annualincome: 45000 
```  
  
### Expand on partner property

Each navigation property has a corresponding "partner" property. After an association is made, we can retrieve information through it. Which column we use depends on the base table we query.

For example, in the previous operation, we created a query against the [account entity type](xref:Microsoft.Dynamics.CRM.account). We wanted to get more information about its primary contact, so we used the `primarycontactid` column, or attribute. If we look up the [account entity type](xref:Microsoft.Dynamics.CRM.account), in the [single-valued navigation properties](/power-apps/developer/data-platform/webapi/reference/account#single-valued-navigation-properties) section we find that the partner property of `primarycontactid` is the `account_primary_contact` collection-valued navigation property, which is found in the [contact entity type](xref:Microsoft.Dynamics.CRM.contact).

If you build a query against a contact, you can expand on the `account_primary_contact` column to get information about accounts where the contact is the primary contact. In the sample data, `Yvonne McKay (sample)` is the primary contact person for only one account. However, Yvonne can potentially be assigned to other accounts as the primary contact. Because the `account_primary_contact` property has a many-to-one relationship, the result is returned as an array of account rows.
  
**Request:**

```http
GET [Organization Uri]/api/data/v9.2/contacts(81716234-9628-ed11-9db1-000d3a320482)?$select=fullname,jobtitle,annualincome&$expand=account_primary_contact($select=name) HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
```

**Response:**

```http
HTTP/1.1 200 OK
ETag: W/"1146626"
OData-Version: 4.0

{
  "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#contacts(fullname,jobtitle,annualincome,account_primary_contact(name))/$entity",
  "@odata.etag": "W/\"1146626\"",
  "fullname": "Yvonne McKay (sample)",
  "jobtitle": "Coffee Master",
  "annualincome": 45000.0,
  "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
  "contactid": "81716234-9628-ed11-9db1-000d3a320482",
  "account_primary_contact": [
    {
      "@odata.etag": "W/\"1146751\"",
      "name": "Contoso, Ltd. (sample)",
      "accountid": "7d716234-9628-ed11-9db1-000d3a320482"
    }
  ]
}
```
  
**Console output:**  
  
```text
Contact 'Yvonne McKay (sample)' is the primary contact for the following accounts:
        Contoso, Ltd. (sample)
```  
  
### Expand on collection-valued navigation property

Collection-valued navigation properties support one-to-many or many-to-many relationships. For example, in our sample data, the account has a relationship with many contacts through the `contact_customer_accounts` column, or attribute.

We can use the [account entity type](xref:Microsoft.Dynamics.CRM.account) in a query to get information about the account and expand information about its contacts. In this case, the `Contoso, Ltd. (sample)` is associated with nine other contacts through the `contact_customer_accounts` collection-valued navigation property.
  
**Request:**

```http
GET [Organization Uri]/api/data/v9.2/accounts(7d716234-9628-ed11-9db1-000d3a320482)?$select=name&$expand=contact_customer_accounts($select=fullname,jobtitle,annualincome) HTTP/1.1
Prefer: odata.include-annotations="*"
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
```

**Response:**

```http
HTTP/1.1 200 OK
ETag: W/"1146751"
OData-Version: 4.0
Preference-Applied: odata.include-annotations="*"

{
  "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#accounts(name,contact_customer_accounts(fullname,jobtitle,annualincome))/$entity",
  "@odata.etag": "W/\"1146751\"",
  "name": "Contoso, Ltd. (sample)",
  "accountid": "7d716234-9628-ed11-9db1-000d3a320482",
  "contact_customer_accounts": [
    {
      "@odata.etag": "W/\"1146759\"",
      "fullname": "Susanna Stubberod (sample)",
      "jobtitle": "Senior Purchaser",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$52,000.00",
      "annualincome": 52000.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
      "contactid": "85716234-9628-ed11-9db1-000d3a320482"
    },
    {
      "@odata.etag": "W/\"1146761\"",
      "fullname": "Nancy Anderson (sample)",
      "jobtitle": "Activities Manager",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$55,500.00",
      "annualincome": 55500.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
      "contactid": "89716234-9628-ed11-9db1-000d3a320482"
    },
    {
      "@odata.etag": "W/\"1146763\"",
      "fullname": "Maria Cambell (sample)",
      "jobtitle": "Accounts Manager",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$31,000.00",
      "annualincome": 31000.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
      "contactid": "8d716234-9628-ed11-9db1-000d3a320482"
    },
    {
      "@odata.etag": "W/\"1146765\"",
      "fullname": "Scott Konersmann (sample)",
      "jobtitle": "Accounts Manager",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$38,000.00",
      "annualincome": 38000.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
      "contactid": "91716234-9628-ed11-9db1-000d3a320482"
    },
    {
      "@odata.etag": "W/\"1146767\"",
      "fullname": "Robert Lyon (sample)",
      "jobtitle": "Senior Technician",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$78,000.00",
      "annualincome": 78000.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
      "contactid": "95716234-9628-ed11-9db1-000d3a320482"
    },
    {
      "@odata.etag": "W/\"1146769\"",
      "fullname": "Paul Cannon (sample)",
      "jobtitle": "Ski Instructor",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$68,500.00",
      "annualincome": 68500.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
      "contactid": "99716234-9628-ed11-9db1-000d3a320482"
    },
    {
      "@odata.etag": "W/\"1146771\"",
      "fullname": "Rene Valdes (sample)",
      "jobtitle": "Data Analyst III",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$86,000.00",
      "annualincome": 86000.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
      "contactid": "9d716234-9628-ed11-9db1-000d3a320482"
    },
    {
      "@odata.etag": "W/\"1146773\"",
      "fullname": "Jim Glynn (sample)",
      "jobtitle": "Senior International Sales Manager",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$81,400.00",
      "annualincome": 81400.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
      "contactid": "a1716234-9628-ed11-9db1-000d3a320482"
    }
  ]
}
```
  
   **Console output:**
  
```text
Account 'Contoso, Ltd. (sample)' has the following contact customers:
        |Full Name                  |Job Title                          |Annual Income
        |---------------------------|-----------------------------------|---------------
        |Susanna Stubberod (sample) |Senior Purchaser                   |$52,000.00
        |Nancy Anderson (sample)    |Activities Manager                 |$55,500.00
        |Maria Cambell (sample)     |Accounts Manager                   |$31,000.00
        |Scott Konersmann (sample)  |Accounts Manager                   |$38,000.00
        |Robert Lyon (sample)       |Senior Technician                  |$78,000.00
        |Paul Cannon (sample)       |Ski Instructor                     |$68,500.00
        |Rene Valdes (sample)       |Data Analyst III                   |$86,000.00
        |Jim Glynn (sample)         |Senior International Sales Manager |$81,400.00
```  
  
### Expand on multiple navigation properties

You can expand on as many navigation properties as the query requires. However, the `$expand` option can only go one level deep.

This example expands the `primarycontactid`, `contact_customer_accounts`, and `Account_Tasks` navigation properties of the [account entity type](xref:Microsoft.Dynamics.CRM.account). The query returns a response that contains information about the account and two collections, a contacts collection and a tasks collection. The sample code processes the collections separately.
  
**Request:**

```http
GET [Organization Uri]/api/data/v9.2/accounts(7d716234-9628-ed11-9db1-000d3a320482)?$select=name&$expand=primarycontactid($select=fullname,jobtitle,annualincome),contact_customer_accounts($select=fullname,jobtitle,annualincome),Account_Tasks($select=subject,description) HTTP/1.1
Prefer: odata.include-annotations="*"
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
```

**Response:**

```http
HTTP/1.1 200 OK
ETag: W/"1146751"
OData-Version: 4.0
Preference-Applied: odata.include-annotations="*"

{
  "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#accounts(name,primarycontactid(fullname,jobtitle,annualincome),contact_customer_accounts(fullname,jobtitle,annualincome),Account_Tasks(subject,description))/$entity",
  "@odata.etag": "W/\"1146751\"",
  "name": "Contoso, Ltd. (sample)",
  "accountid": "7d716234-9628-ed11-9db1-000d3a320482",
  "primarycontactid": {
    "@odata.etag": "W/\"1146626\"",
    "fullname": "Yvonne McKay (sample)",
    "jobtitle": "Coffee Master",
    "annualincome@OData.Community.Display.V1.FormattedValue": "$45,000.00",
    "annualincome": 45000.0,
    "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
    "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
    "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
    "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
    "contactid": "81716234-9628-ed11-9db1-000d3a320482"
  },
  "contact_customer_accounts": [
    {
      "@odata.etag": "W/\"1146759\"",
      "fullname": "Susanna Stubberod (sample)",
      "jobtitle": "Senior Purchaser",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$52,000.00",
      "annualincome": 52000.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
      "contactid": "85716234-9628-ed11-9db1-000d3a320482"
    },
    {
      "@odata.etag": "W/\"1146761\"",
      "fullname": "Nancy Anderson (sample)",
      "jobtitle": "Activities Manager",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$55,500.00",
      "annualincome": 55500.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
      "contactid": "89716234-9628-ed11-9db1-000d3a320482"
    },
    {
      "@odata.etag": "W/\"1146763\"",
      "fullname": "Maria Cambell (sample)",
      "jobtitle": "Accounts Manager",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$31,000.00",
      "annualincome": 31000.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
      "contactid": "8d716234-9628-ed11-9db1-000d3a320482"
    },
    {
      "@odata.etag": "W/\"1146765\"",
      "fullname": "Scott Konersmann (sample)",
      "jobtitle": "Accounts Manager",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$38,000.00",
      "annualincome": 38000.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
      "contactid": "91716234-9628-ed11-9db1-000d3a320482"
    },
    {
      "@odata.etag": "W/\"1146767\"",
      "fullname": "Robert Lyon (sample)",
      "jobtitle": "Senior Technician",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$78,000.00",
      "annualincome": 78000.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
      "contactid": "95716234-9628-ed11-9db1-000d3a320482"
    },
    {
      "@odata.etag": "W/\"1146769\"",
      "fullname": "Paul Cannon (sample)",
      "jobtitle": "Ski Instructor",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$68,500.00",
      "annualincome": 68500.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
      "contactid": "99716234-9628-ed11-9db1-000d3a320482"
    },
    {
      "@odata.etag": "W/\"1146771\"",
      "fullname": "Rene Valdes (sample)",
      "jobtitle": "Data Analyst III",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$86,000.00",
      "annualincome": 86000.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
      "contactid": "9d716234-9628-ed11-9db1-000d3a320482"
    },
    {
      "@odata.etag": "W/\"1146773\"",
      "fullname": "Jim Glynn (sample)",
      "jobtitle": "Senior International Sales Manager",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$81,400.00",
      "annualincome": 81400.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
      "contactid": "a1716234-9628-ed11-9db1-000d3a320482"
    }
  ],
  "Account_Tasks": [
    {
      "@odata.etag": "W/\"1146746\"",
      "subject": "Task 1 for Contoso, Ltd.",
      "description": "Task 1 for Contoso, Ltd. description",
      "activityid": "7e716234-9628-ed11-9db1-000d3a320482"
    },
    {
      "@odata.etag": "W/\"1146748\"",
      "subject": "Task 2 for Contoso, Ltd.",
      "description": "Task 2 for Contoso, Ltd. description",
      "activityid": "7f716234-9628-ed11-9db1-000d3a320482"
    },
    {
      "@odata.etag": "W/\"1146750\"",
      "subject": "Task 3 for Contoso, Ltd.",
      "description": "Task 3 for Contoso, Ltd. description",
      "activityid": "80716234-9628-ed11-9db1-000d3a320482"
    }
  ]
}
```
  
**Console output:**  
  
```text
-- Expanding multiple property types in one request --

Account Contoso, Ltd. (sample) has the following primary contact person:
        Fullname: Yvonne McKay (sample)
        Jobtitle: Coffee Master
        Annualincome: 45000

Account 'Contoso, Ltd. (sample)' has the following contact customers:
        |Full Name                  |Job Title                          |Annual Income
        |---------------------------|-----------------------------------|---------------
        |Susanna Stubberod (sample) |Senior Purchaser                   |$52,000.00
        |Nancy Anderson (sample)    |Activities Manager                 |$55,500.00
        |Maria Cambell (sample)     |Accounts Manager                   |$31,000.00
        |Scott Konersmann (sample)  |Accounts Manager                   |$38,000.00
        |Robert Lyon (sample)       |Senior Technician                  |$78,000.00
        |Paul Cannon (sample)       |Ski Instructor                     |$68,500.00
        |Rene Valdes (sample)       |Data Analyst III                   |$86,000.00
        |Jim Glynn (sample)         |Senior International Sales Manager |$81,400.00

Account 'Contoso, Ltd. (sample)' has the following tasks:
        Task 1 for Contoso, Ltd.
        Task 2 for Contoso, Ltd.
        Task 3 for Contoso, Ltd.
```

### Multi-level expands

With single-valued navigation properties, you can use `$expand` to continue up multiple levels using only single-valued navigation properties. This query starts with `task` records and expands data from the `contact`, `account`, and `systemuser` tables using only single-valued navigation properties.

**Request:**

```http
GET [Organization Uri]/api/data/v9.2/tasks?$select=subject&$filter=regardingobjectid_contact_task/_accountid_value eq 7d716234-9628-ed11-9db1-000d3a320482&$expand=regardingobjectid_contact_task($select=fullname;$expand=parentcustomerid_account($select=name;$expand=createdby($select=fullname))) HTTP/1.1
Prefer: odata.include-annotations="*"
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
```

**Response:**

```http
HTTP/1.1 200 OK
OData-Version: 4.0
Preference-Applied: odata.include-annotations="*"

{
  "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#tasks(subject,regardingobjectid_contact_task(fullname,parentcustomerid_account(name,createdby(fullname))))",
  "@Microsoft.Dynamics.CRM.totalrecordcount": -1,
  "@Microsoft.Dynamics.CRM.totalrecordcountlimitexceeded": false,
  "@Microsoft.Dynamics.CRM.globalmetadataversion": "1144249",
  "value": [
    {
      "@odata.etag": "W/\"1146775\"",
      "subject": "Task 1 for Susanna Stubberod",
      "activityid": "86716234-9628-ed11-9db1-000d3a320482",
      "regardingobjectid_contact_task": {
        "fullname": "Susanna Stubberod (sample)",
        "contactid": "85716234-9628-ed11-9db1-000d3a320482",
        "parentcustomerid_account": {
          "name": "Contoso, Ltd. (sample)",
          "accountid": "7d716234-9628-ed11-9db1-000d3a320482",
          "createdby": {
            "fullname": "FirstName Lastname",
            "systemuserid": "ce939f72-a724-ed11-b83e-00224804438a",
            "ownerid": "ce939f72-a724-ed11-b83e-00224804438a"
          }
        }
      }
    },
    {
      "@odata.etag": "W/\"1146777\"",
      "subject": "Task 2 for Susanna Stubberod",
      "activityid": "87716234-9628-ed11-9db1-000d3a320482",
      "regardingobjectid_contact_task": {
        "fullname": "Susanna Stubberod (sample)",
        "contactid": "85716234-9628-ed11-9db1-000d3a320482",
        "parentcustomerid_account": {
          "name": "Contoso, Ltd. (sample)",
          "accountid": "7d716234-9628-ed11-9db1-000d3a320482",
          "createdby": {
            "fullname": "FirstName Lastname",
            "systemuserid": "ce939f72-a724-ed11-b83e-00224804438a",
            "ownerid": "ce939f72-a724-ed11-b83e-00224804438a"
          }
        }
      }
    },
    {
      "@odata.etag": "W/\"1146779\"",
      "subject": "Task 3 for Susanna Stubberod",
      "activityid": "88716234-9628-ed11-9db1-000d3a320482",
      "regardingobjectid_contact_task": {
        "fullname": "Susanna Stubberod (sample)",
        "contactid": "85716234-9628-ed11-9db1-000d3a320482",
        "parentcustomerid_account": {
          "name": "Contoso, Ltd. (sample)",
          "accountid": "7d716234-9628-ed11-9db1-000d3a320482",
          "createdby": {
            "fullname": "FirstName Lastname",
            "systemuserid": "ce939f72-a724-ed11-b83e-00224804438a",
            "ownerid": "ce939f72-a724-ed11-b83e-00224804438a"
          }
        }
      }
    },
    {
      "@odata.etag": "W/\"1146781\"",
      "subject": "Task 1 for Nancy Anderson",
      "activityid": "8a716234-9628-ed11-9db1-000d3a320482",
      "regardingobjectid_contact_task": {
        "fullname": "Nancy Anderson (sample)",
        "contactid": "89716234-9628-ed11-9db1-000d3a320482",
        "parentcustomerid_account": {
          "name": "Contoso, Ltd. (sample)",
          "accountid": "7d716234-9628-ed11-9db1-000d3a320482",
          "createdby": {
            "fullname": "FirstName Lastname",
            "systemuserid": "ce939f72-a724-ed11-b83e-00224804438a",
            "ownerid": "ce939f72-a724-ed11-b83e-00224804438a"
          }
        }
      }
    },
    {
      "@odata.etag": "W/\"1146783\"",
      "subject": "Task 2 for Nancy Anderson",
      "activityid": "8b716234-9628-ed11-9db1-000d3a320482",
      "regardingobjectid_contact_task": {
        "fullname": "Nancy Anderson (sample)",
        "contactid": "89716234-9628-ed11-9db1-000d3a320482",
        "parentcustomerid_account": {
          "name": "Contoso, Ltd. (sample)",
          "accountid": "7d716234-9628-ed11-9db1-000d3a320482",
          "createdby": {
            "fullname": "FirstName Lastname",
            "systemuserid": "ce939f72-a724-ed11-b83e-00224804438a",
            "ownerid": "ce939f72-a724-ed11-b83e-00224804438a"
          }
        }
      }
    },
    {
      "@odata.etag": "W/\"1146785\"",
      "subject": "Task 3 for Nancy Anderson",
      "activityid": "8c716234-9628-ed11-9db1-000d3a320482",
      "regardingobjectid_contact_task": {
        "fullname": "Nancy Anderson (sample)",
        "contactid": "89716234-9628-ed11-9db1-000d3a320482",
        "parentcustomerid_account": {
          "name": "Contoso, Ltd. (sample)",
          "accountid": "7d716234-9628-ed11-9db1-000d3a320482",
          "createdby": {
            "fullname": "FirstName Lastname",
            "systemuserid": "ce939f72-a724-ed11-b83e-00224804438a",
            "ownerid": "ce939f72-a724-ed11-b83e-00224804438a"
          }
        }
      }
    },
    {
      "@odata.etag": "W/\"1146787\"",
      "subject": "Task 1 for Maria Cambell",
      "activityid": "8e716234-9628-ed11-9db1-000d3a320482",
      "regardingobjectid_contact_task": {
        "fullname": "Maria Cambell (sample)",
        "contactid": "8d716234-9628-ed11-9db1-000d3a320482",
        "parentcustomerid_account": {
          "name": "Contoso, Ltd. (sample)",
          "accountid": "7d716234-9628-ed11-9db1-000d3a320482",
          "createdby": {
            "fullname": "FirstName Lastname",
            "systemuserid": "ce939f72-a724-ed11-b83e-00224804438a",
            "ownerid": "ce939f72-a724-ed11-b83e-00224804438a"
          }
        }
      }
    },
    {
      "@odata.etag": "W/\"1146789\"",
      "subject": "Task 2 for Maria Cambell",
      "activityid": "8f716234-9628-ed11-9db1-000d3a320482",
      "regardingobjectid_contact_task": {
        "fullname": "Maria Cambell (sample)",
        "contactid": "8d716234-9628-ed11-9db1-000d3a320482",
        "parentcustomerid_account": {
          "name": "Contoso, Ltd. (sample)",
          "accountid": "7d716234-9628-ed11-9db1-000d3a320482",
          "createdby": {
            "fullname": "FirstName Lastname",
            "systemuserid": "ce939f72-a724-ed11-b83e-00224804438a",
            "ownerid": "ce939f72-a724-ed11-b83e-00224804438a"
          }
        }
      }
    },
    {
      "@odata.etag": "W/\"1146791\"",
      "subject": "Task 3 for Maria Cambell",
      "activityid": "90716234-9628-ed11-9db1-000d3a320482",
      "regardingobjectid_contact_task": {
        "fullname": "Maria Cambell (sample)",
        "contactid": "8d716234-9628-ed11-9db1-000d3a320482",
        "parentcustomerid_account": {
          "name": "Contoso, Ltd. (sample)",
          "accountid": "7d716234-9628-ed11-9db1-000d3a320482",
          "createdby": {
            "fullname": "FirstName Lastname",
            "systemuserid": "ce939f72-a724-ed11-b83e-00224804438a",
            "ownerid": "ce939f72-a724-ed11-b83e-00224804438a"
          }
        }
      }
    },
    {
      "@odata.etag": "W/\"1146793\"",
      "subject": "Task 1 for Scott Konersmann",
      "activityid": "92716234-9628-ed11-9db1-000d3a320482",
      "regardingobjectid_contact_task": {
        "fullname": "Scott Konersmann (sample)",
        "contactid": "91716234-9628-ed11-9db1-000d3a320482",
        "parentcustomerid_account": {
          "name": "Contoso, Ltd. (sample)",
          "accountid": "7d716234-9628-ed11-9db1-000d3a320482",
          "createdby": {
            "fullname": "FirstName Lastname",
            "systemuserid": "ce939f72-a724-ed11-b83e-00224804438a",
            "ownerid": "ce939f72-a724-ed11-b83e-00224804438a"
          }
        }
      }
    },
    {
      "@odata.etag": "W/\"1146795\"",
      "subject": "Task 2 for Scott Konersmann",
      "activityid": "93716234-9628-ed11-9db1-000d3a320482",
      "regardingobjectid_contact_task": {
        "fullname": "Scott Konersmann (sample)",
        "contactid": "91716234-9628-ed11-9db1-000d3a320482",
        "parentcustomerid_account": {
          "name": "Contoso, Ltd. (sample)",
          "accountid": "7d716234-9628-ed11-9db1-000d3a320482",
          "createdby": {
            "fullname": "FirstName Lastname",
            "systemuserid": "ce939f72-a724-ed11-b83e-00224804438a",
            "ownerid": "ce939f72-a724-ed11-b83e-00224804438a"
          }
        }
      }
    },
    {
      "@odata.etag": "W/\"1146797\"",
      "subject": "Task 3 for Scott Konersmann",
      "activityid": "94716234-9628-ed11-9db1-000d3a320482",
      "regardingobjectid_contact_task": {
        "fullname": "Scott Konersmann (sample)",
        "contactid": "91716234-9628-ed11-9db1-000d3a320482",
        "parentcustomerid_account": {
          "name": "Contoso, Ltd. (sample)",
          "accountid": "7d716234-9628-ed11-9db1-000d3a320482",
          "createdby": {
            "fullname": "FirstName Lastname",
            "systemuserid": "ce939f72-a724-ed11-b83e-00224804438a",
            "ownerid": "ce939f72-a724-ed11-b83e-00224804438a"
          }
        }
      }
    },
    {
      "@odata.etag": "W/\"1146799\"",
      "subject": "Task 1 for Robert Lyon",
      "activityid": "96716234-9628-ed11-9db1-000d3a320482",
      "regardingobjectid_contact_task": {
        "fullname": "Robert Lyon (sample)",
        "contactid": "95716234-9628-ed11-9db1-000d3a320482",
        "parentcustomerid_account": {
          "name": "Contoso, Ltd. (sample)",
          "accountid": "7d716234-9628-ed11-9db1-000d3a320482",
          "createdby": {
            "fullname": "FirstName Lastname",
            "systemuserid": "ce939f72-a724-ed11-b83e-00224804438a",
            "ownerid": "ce939f72-a724-ed11-b83e-00224804438a"
          }
        }
      }
    },
    {
      "@odata.etag": "W/\"1146801\"",
      "subject": "Task 2 for Robert Lyon",
      "activityid": "97716234-9628-ed11-9db1-000d3a320482",
      "regardingobjectid_contact_task": {
        "fullname": "Robert Lyon (sample)",
        "contactid": "95716234-9628-ed11-9db1-000d3a320482",
        "parentcustomerid_account": {
          "name": "Contoso, Ltd. (sample)",
          "accountid": "7d716234-9628-ed11-9db1-000d3a320482",
          "createdby": {
            "fullname": "FirstName Lastname",
            "systemuserid": "ce939f72-a724-ed11-b83e-00224804438a",
            "ownerid": "ce939f72-a724-ed11-b83e-00224804438a"
          }
        }
      }
    },
    {
      "@odata.etag": "W/\"1146803\"",
      "subject": "Task 3 for Robert Lyon",
      "activityid": "98716234-9628-ed11-9db1-000d3a320482",
      "regardingobjectid_contact_task": {
        "fullname": "Robert Lyon (sample)",
        "contactid": "95716234-9628-ed11-9db1-000d3a320482",
        "parentcustomerid_account": {
          "name": "Contoso, Ltd. (sample)",
          "accountid": "7d716234-9628-ed11-9db1-000d3a320482",
          "createdby": {
            "fullname": "FirstName Lastname",
            "systemuserid": "ce939f72-a724-ed11-b83e-00224804438a",
            "ownerid": "ce939f72-a724-ed11-b83e-00224804438a"
          }
        }
      }
    },
    {
      "@odata.etag": "W/\"1146806\"",
      "subject": "Task 1 for Paul Cannon",
      "activityid": "9a716234-9628-ed11-9db1-000d3a320482",
      "regardingobjectid_contact_task": {
        "fullname": "Paul Cannon (sample)",
        "contactid": "99716234-9628-ed11-9db1-000d3a320482",
        "parentcustomerid_account": {
          "name": "Contoso, Ltd. (sample)",
          "accountid": "7d716234-9628-ed11-9db1-000d3a320482",
          "createdby": {
            "fullname": "FirstName Lastname",
            "systemuserid": "ce939f72-a724-ed11-b83e-00224804438a",
            "ownerid": "ce939f72-a724-ed11-b83e-00224804438a"
          }
        }
      }
    },
    {
      "@odata.etag": "W/\"1146808\"",
      "subject": "Task 2 for Paul Cannon",
      "activityid": "9b716234-9628-ed11-9db1-000d3a320482",
      "regardingobjectid_contact_task": {
        "fullname": "Paul Cannon (sample)",
        "contactid": "99716234-9628-ed11-9db1-000d3a320482",
        "parentcustomerid_account": {
          "name": "Contoso, Ltd. (sample)",
          "accountid": "7d716234-9628-ed11-9db1-000d3a320482",
          "createdby": {
            "fullname": "FirstName Lastname",
            "systemuserid": "ce939f72-a724-ed11-b83e-00224804438a",
            "ownerid": "ce939f72-a724-ed11-b83e-00224804438a"
          }
        }
      }
    },
    {
      "@odata.etag": "W/\"1146810\"",
      "subject": "Task 3 for Paul Cannon",
      "activityid": "9c716234-9628-ed11-9db1-000d3a320482",
      "regardingobjectid_contact_task": {
        "fullname": "Paul Cannon (sample)",
        "contactid": "99716234-9628-ed11-9db1-000d3a320482",
        "parentcustomerid_account": {
          "name": "Contoso, Ltd. (sample)",
          "accountid": "7d716234-9628-ed11-9db1-000d3a320482",
          "createdby": {
            "fullname": "FirstName Lastname",
            "systemuserid": "ce939f72-a724-ed11-b83e-00224804438a",
            "ownerid": "ce939f72-a724-ed11-b83e-00224804438a"
          }
        }
      }
    },
    {
      "@odata.etag": "W/\"1146812\"",
      "subject": "Task 1 for Rene Valdes",
      "activityid": "9e716234-9628-ed11-9db1-000d3a320482",
      "regardingobjectid_contact_task": {
        "fullname": "Rene Valdes (sample)",
        "contactid": "9d716234-9628-ed11-9db1-000d3a320482",
        "parentcustomerid_account": {
          "name": "Contoso, Ltd. (sample)",
          "accountid": "7d716234-9628-ed11-9db1-000d3a320482",
          "createdby": {
            "fullname": "FirstName Lastname",
            "systemuserid": "ce939f72-a724-ed11-b83e-00224804438a",
            "ownerid": "ce939f72-a724-ed11-b83e-00224804438a"
          }
        }
      }
    },
    {
      "@odata.etag": "W/\"1146814\"",
      "subject": "Task 2 for Rene Valdes",
      "activityid": "9f716234-9628-ed11-9db1-000d3a320482",
      "regardingobjectid_contact_task": {
        "fullname": "Rene Valdes (sample)",
        "contactid": "9d716234-9628-ed11-9db1-000d3a320482",
        "parentcustomerid_account": {
          "name": "Contoso, Ltd. (sample)",
          "accountid": "7d716234-9628-ed11-9db1-000d3a320482",
          "createdby": {
            "fullname": "FirstName Lastname",
            "systemuserid": "ce939f72-a724-ed11-b83e-00224804438a",
            "ownerid": "ce939f72-a724-ed11-b83e-00224804438a"
          }
        }
      }
    },
    {
      "@odata.etag": "W/\"1146816\"",
      "subject": "Task 3 for Rene Valdes",
      "activityid": "a0716234-9628-ed11-9db1-000d3a320482",
      "regardingobjectid_contact_task": {
        "fullname": "Rene Valdes (sample)",
        "contactid": "9d716234-9628-ed11-9db1-000d3a320482",
        "parentcustomerid_account": {
          "name": "Contoso, Ltd. (sample)",
          "accountid": "7d716234-9628-ed11-9db1-000d3a320482",
          "createdby": {
            "fullname": "FirstName Lastname",
            "systemuserid": "ce939f72-a724-ed11-b83e-00224804438a",
            "ownerid": "ce939f72-a724-ed11-b83e-00224804438a"
          }
        }
      }
    },
    {
      "@odata.etag": "W/\"1146820\"",
      "subject": "Task 1 for Jim Glynn",
      "activityid": "a2716234-9628-ed11-9db1-000d3a320482",
      "regardingobjectid_contact_task": {
        "fullname": "Jim Glynn (sample)",
        "contactid": "a1716234-9628-ed11-9db1-000d3a320482",
        "parentcustomerid_account": {
          "name": "Contoso, Ltd. (sample)",
          "accountid": "7d716234-9628-ed11-9db1-000d3a320482",
          "createdby": {
            "fullname": "FirstName Lastname",
            "systemuserid": "ce939f72-a724-ed11-b83e-00224804438a",
            "ownerid": "ce939f72-a724-ed11-b83e-00224804438a"
          }
        }
      }
    },
    {
      "@odata.etag": "W/\"1146822\"",
      "subject": "Task 2 for Jim Glynn",
      "activityid": "a3716234-9628-ed11-9db1-000d3a320482",
      "regardingobjectid_contact_task": {
        "fullname": "Jim Glynn (sample)",
        "contactid": "a1716234-9628-ed11-9db1-000d3a320482",
        "parentcustomerid_account": {
          "name": "Contoso, Ltd. (sample)",
          "accountid": "7d716234-9628-ed11-9db1-000d3a320482",
          "createdby": {
            "fullname": "FirstName Lastname",
            "systemuserid": "ce939f72-a724-ed11-b83e-00224804438a",
            "ownerid": "ce939f72-a724-ed11-b83e-00224804438a"
          }
        }
      }
    },
    {
      "@odata.etag": "W/\"1146827\"",
      "subject": "Task 3 for Jim Glynn",
      "activityid": "a4716234-9628-ed11-9db1-000d3a320482",
      "regardingobjectid_contact_task": {
        "fullname": "Jim Glynn (sample)",
        "contactid": "a1716234-9628-ed11-9db1-000d3a320482",
        "parentcustomerid_account": {
          "name": "Contoso, Ltd. (sample)",
          "accountid": "7d716234-9628-ed11-9db1-000d3a320482",
          "createdby": {
            "fullname": "FirstName Lastname",
            "systemuserid": "ce939f72-a724-ed11-b83e-00224804438a",
            "ownerid": "ce939f72-a724-ed11-b83e-00224804438a"
          }
        }
      }
    }
  ]
}
```



   **Console output:**

```
Expanded values from Task:
        |Subject                       |Contact                       |Account                  |Account CreatedBy
        |------------------------------|------------------------------|-------------------------|--------------------
        |Task 1 for Susanna Stubberod  |Susanna Stubberod (sample)    |Contoso, Ltd. (sample)   |FirstName Lastname
        |Task 2 for Susanna Stubberod  |Susanna Stubberod (sample)    |Contoso, Ltd. (sample)   |FirstName Lastname
        |Task 3 for Susanna Stubberod  |Susanna Stubberod (sample)    |Contoso, Ltd. (sample)   |FirstName Lastname
        |Task 1 for Nancy Anderson     |Nancy Anderson (sample)       |Contoso, Ltd. (sample)   |FirstName Lastname
        |Task 2 for Nancy Anderson     |Nancy Anderson (sample)       |Contoso, Ltd. (sample)   |FirstName Lastname
        |Task 3 for Nancy Anderson     |Nancy Anderson (sample)       |Contoso, Ltd. (sample)   |FirstName Lastname
        |Task 1 for Maria Cambell      |Maria Cambell (sample)        |Contoso, Ltd. (sample)   |FirstName Lastname
        |Task 2 for Maria Cambell      |Maria Cambell (sample)        |Contoso, Ltd. (sample)   |FirstName Lastname
        |Task 3 for Maria Cambell      |Maria Cambell (sample)        |Contoso, Ltd. (sample)   |FirstName Lastname
        |Task 1 for Scott Konersmann   |Scott Konersmann (sample)     |Contoso, Ltd. (sample)   |FirstName Lastname
        |Task 2 for Scott Konersmann   |Scott Konersmann (sample)     |Contoso, Ltd. (sample)   |FirstName Lastname
        |Task 3 for Scott Konersmann   |Scott Konersmann (sample)     |Contoso, Ltd. (sample)   |FirstName Lastname
        |Task 1 for Robert Lyon        |Robert Lyon (sample)          |Contoso, Ltd. (sample)   |FirstName Lastname
        |Task 2 for Robert Lyon        |Robert Lyon (sample)          |Contoso, Ltd. (sample)   |FirstName Lastname
        |Task 3 for Robert Lyon        |Robert Lyon (sample)          |Contoso, Ltd. (sample)   |FirstName Lastname
        |Task 1 for Paul Cannon        |Paul Cannon (sample)          |Contoso, Ltd. (sample)   |FirstName Lastname
        |Task 2 for Paul Cannon        |Paul Cannon (sample)          |Contoso, Ltd. (sample)   |FirstName Lastname
        |Task 3 for Paul Cannon        |Paul Cannon (sample)          |Contoso, Ltd. (sample)   |FirstName Lastname
        |Task 1 for Rene Valdes        |Rene Valdes (sample)          |Contoso, Ltd. (sample)   |FirstName Lastname
        |Task 2 for Rene Valdes        |Rene Valdes (sample)          |Contoso, Ltd. (sample)   |FirstName Lastname
        |Task 3 for Rene Valdes        |Rene Valdes (sample)          |Contoso, Ltd. (sample)   |FirstName Lastname
        |Task 1 for Jim Glynn          |Jim Glynn (sample)            |Contoso, Ltd. (sample)   |FirstName Lastname
        |Task 2 for Jim Glynn          |Jim Glynn (sample)            |Contoso, Ltd. (sample)   |FirstName Lastname
        |Task 3 for Jim Glynn          |Jim Glynn (sample)            |Contoso, Ltd. (sample)   |FirstName Lastname
```

## Section 7: Aggregate results

To return aggregated values, use the `$apply` option. This example applies `average`, `sum`, `min`, and `max` to annual income values.

**Request:**

```http
GET [Organization Uri]/api/data/v9.2/accounts(7d716234-9628-ed11-9db1-000d3a320482)/contact_customer_accounts?$apply=aggregate(annualincome with average as average, annualincome with sum as total, annualincome with min as minimum, annualincome with max as maximum) HTTP/1.1
Prefer: odata.include-annotations="*"
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
```

**Response:**

```http
HTTP/1.1 200 OK
OData-Version: 4.0
Preference-Applied: odata.include-annotations="*"

{
  "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#contacts",
  "@Microsoft.Dynamics.CRM.totalrecordcount": -1,
  "@Microsoft.Dynamics.CRM.totalrecordcountlimitexceeded": false,
  "value": [
    {
      "telephone3": null,
      "address1_shippingmethodcode": null,
      "familystatuscode": null,
      "haschildrencode": null,
      "nickname": null,
      "address1_freighttermscode": null,
      "address3_upszone": null,
      "_ownerid_value": null,
      "annualincome_base": null,
      "anniversary": null,
      "address1_upszone": null,
      "fullname": null,
      "merged": null,
      "websiteurl": null,
      "address2_city": null,
      "_slainvokedid_value": null,
      "address1_postofficebox": null,
      "importsequencenumber": null,
      "address3_longitude": null,
      "preferredappointmentdaycode": null,
      "customertypecode": null,
      "utcconversiontimezonecode": null,
      "overriddencreatedon": null,
      "aging90": null,
      "stageid": null,
      "address3_primarycontactname": null,
      "address1_utcoffset": null,
      "address1_latitude": null,
      "home2": null,
      "yomifirstname": null,
      "isbackofficecustomer": null,
      "_masterid_value": null,
      "address3_shippingmethodcode": null,
      "lastonholdtime": null,
      "address2_fax": null,
      "address3_stateorprovince": null,
      "address3_telephone3": null,
      "address3_telephone2": null,
      "address3_telephone1": null,
      "_transactioncurrencyid_value": null,
      "governmentid": null,
      "yomifullname": null,
      "participatesinworkflow": null,
      "address2_line1": null,
      "followemail": null,
      "address1_telephone3": null,
      "educationcode": null,
      "address1_telephone2": null,
      "address1_telephone1": null,
      "address2_postofficebox": null,
      "_owninguser_value": null,
      "emailaddress1": null,
      "ftpsiteurl": null,
      "emailaddress2": null,
      "address2_latitude": null,
      "processid": null,
      "emailaddress3": null,
      "address2_shippingmethodcode": null,
      "address2_composite": null,
      "creditonhold": null,
      "traversedpath": null,
      "address1_city": null,
      "spousesname": null,
      "address3_addressid": null,
      "address3_name": null,
      "address3_postofficebox": null,
      "address2_line2": null,
      "aging30_base": null,
      "address1_addressid": null,
      "address1_addresstypecode": null,
      "donotphone": null,
      "managerphone": null,
      "contactid": null,
      "address2_stateorprovince": null,
      "_createdby_value": null,
      "donotemail": null,
      "address2_postalcode": null,
      "donotsendmm": null,
      "entityimage_url": null,
      "firstname": null,
      "address1_composite": null,
      "leadsourcecode": null,
      "aging60": null,
      "managername": null,
      "_modifiedby_value": null,
      "address3_postalcode": null,
      "marketingonly": null,
      "jobtitle": null,
      "timezoneruleversionnumber": null,
      "address3_utcoffset": null,
      "address2_telephone3": null,
      "address2_telephone2": null,
      "address2_telephone1": null,
      "numberofchildren": null,
      "address1_postalcode": null,
      "address2_upszone": null,
      "_owningteam_value": null,
      "address2_line3": null,
      "timespentbymeonemailandmeetings": null,
      "territorycode": null,
      "department": null,
      "address1_country": null,
      "address2_longitude": null,
      "suffix": null,
      "_modifiedonbehalfby_value": null,
      "creditlimit": null,
      "address1_line2": null,
      "paymenttermscode": null,
      "address1_county": null,
      "donotpostalmail": null,
      "_preferredsystemuserid_value": null,
      "accountrolecode": null,
      "preferredappointmenttimecode": null,
      "assistantname": null,
      "address1_fax": null,
      "_owningbusinessunit_value": null,
      "_parentcustomerid_value": null,
      "_createdonbehalfby_value": null,
      "annualincome": null,
      "_accountid_value": null,
      "modifiedon": null,
      "address2_name": null,
      "creditlimit_base": null,
      "_modifiedbyexternalparty_value": null,
      "address2_utcoffset": null,
      "business2": null,
      "statuscode": null,
      "address3_composite": null,
      "_slaid_value": null,
      "fax": null,
      "address1_line1": null,
      "shippingmethodcode": null,
      "donotbulkemail": null,
      "childrensnames": null,
      "address2_county": null,
      "lastname": null,
      "versionnumber": null,
      "address3_city": null,
      "address2_freighttermscode": null,
      "aging30": null,
      "externaluseridentifier": null,
      "address1_line3": null,
      "_parentcontactid_value": null,
      "assistantphone": null,
      "statecode": null,
      "address1_stateorprovince": null,
      "birthdate": null,
      "customersizecode": null,
      "address3_addresstypecode": null,
      "onholdtime": null,
      "_createdbyexternalparty_value": null,
      "entityimage_timestamp": null,
      "mobilephone": null,
      "address3_county": null,
      "employeeid": null,
      "exchangerate": null,
      "subscriptionid": null,
      "entityimageid": null,
      "company": null,
      "donotbulkpostalmail": null,
      "gendercode": null,
      "callback": null,
      "lastusedincampaign": null,
      "address3_line3": null,
      "donotfax": null,
      "telephone2": null,
      "address3_freighttermscode": null,
      "yomilastname": null,
      "address3_fax": null,
      "description": null,
      "address3_line1": null,
      "address3_line2": null,
      "address2_addresstypecode": null,
      "createdon": null,
      "yomimiddlename": null,
      "aging90_base": null,
      "address1_name": null,
      "telephone1": null,
      "address1_primarycontactname": null,
      "address1_longitude": null,
      "middlename": null,
      "address2_primarycontactname": null,
      "entityimage": null,
      "address2_addressid": null,
      "preferredcontactmethodcode": null,
      "address3_latitude": null,
      "salutation": null,
      "aging60_base": null,
      "pager": null,
      "address2_country": null,
      "address3_country": null,
      "average@OData.Community.Display.V1.AttributeName": "annualincome",
      "average@OData.Community.Display.V1.FormattedValue": "$61,300.00",
      "average": 61300.0,
      "total@OData.Community.Display.V1.AttributeName": "annualincome",
      "total@OData.Community.Display.V1.FormattedValue": "$490,400.00",
      "total": 490400.0,
      "minimum@OData.Community.Display.V1.AttributeName": "annualincome",
      "minimum@OData.Community.Display.V1.FormattedValue": "$31,000.00",
      "minimum": 31000.0,
      "maximum@OData.Community.Display.V1.AttributeName": "annualincome",
      "maximum@OData.Community.Display.V1.FormattedValue": "$86,000.00",
      "maximum": 86000.0
    }
  ]
}
```

   **Console output:**

```
Aggregated Annual Income information for Contoso contacts:
        Average income: $61,300.00
        Total income: $490,400.00
        Minium income: $31,000.00
        Maximum income: $86,000.00
```


<a name="bkmk_fetchxml"></a>

## Section 8: FetchXML queries

Besides query filter operations, the Web API also supports [FetchXML queries](../use-fetchxml-construct-query.md). FetchXML provides an alternative way to define queries and more options for aggregation. All the query options we would normally define, such as `$select`, `$filter`, and `$orderby`, are defined in the XML.

To use FetchXML, compose a string that represents the query. Make sure the query string conforms to the [FetchXML schema](../fetchxml-schema.md). Before you include the string in the URL, you must URL-encode it.

In this example, we query for all contacts where `fullname` matches `(sample)`, and return the results in descending order by `fullname`.

This is the XML for the query:
  
```xml  
<fetch mapping="logical" output-format="xml-platform" version="1.0" distinct="false">  
  <entity name="contact">  
    <attribute name="fullname" />  
    <attribute name="jobtitle" />  
    <attribute name="annualincome" />  
    <order descending="true"  
           attribute="fullname" />  
    <filter type="and">  
      <condition value="%(sample)%"  
                 attribute="fullname"  
                 operator="like" />
      <condition value="7d716234-9628-ed11-9db1-000d3a320482"
                 attribute="parentcustomerid"
                 operator="eq" /> 
    </filter>  
  </entity>  
</fetch>  
```

In this example, the query is sent using a `$batch` request. FetchXML queries can be long, so they can reach the limits for URLs that can be sent using `GET`. With a `$batch` operation, the URL is sent in the body of the request, where the limits are higher.
  
**Request:**

```http
POST [Organization Uri]/api/data/v9.2/$batch HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json

--batch_7118cb08-27c1-44c0-be91-c2442fe9d454
Content-Type: application/http
Content-Transfer-Encoding: binary
Content-Length: 881

GET /api/data/v9.2/contacts?fetchXml=%3Cfetch+mapping%3D%22logical%22+output-format%3D%22xml-platform%22+version%3D%221.0%22+distinct%3D%22false%22%3E%0D%0A++%3Centity+name%3D%22contact%22%3E%0D%0A++++%3Cattribute+name%3D%22fullname%22+%2F%3E%0D%0A++++%3Cattribute+name%3D%22jobtitle%22+%2F%3E%0D%0A++++%3Cattribute+name%3D%22annualincome%22+%2F%3E%0D%0A++++%3Corder+descending%3D%22true%22+attribute%3D%22fullname%22+%2F%3E%0D%0A++++%3Cfilter+type%3D%22and%22%3E%0D%0A++++++%3Ccondition+value%3D%22%25(sample)%25%22+attribute%3D%22fullname%22+operator%3D%22like%22+%2F%3E%0D%0A++++++%3Ccondition+value%3D%227d716234-9628-ed11-9db1-000d3a320482%22+attribute%3D%22parentcustomerid%22+operator%3D%22eq%22+%2F%3E%0D%0A++++%3C%2Ffilter%3E%0D%0A++%3C%2Fentity%3E%0D%0A%3C%2Ffetch%3E&$count=true HTTP/1.1
Prefer: odata.include-annotations="*"


--batch_7118cb08-27c1-44c0-be91-c2442fe9d454--

```

**Response:**

```http
HTTP/1.1 200 OK
OData-Version: 4.0

--batchresponse_ed1a482b-c942-4da4-8257-adaa53acc8e0
Content-Type: application/http
Content-Transfer-Encoding: binary

HTTP/1.1 200 OK
Content-Type: application/json; odata.metadata=minimal; odata.streaming=true
OData-Version: 4.0
Preference-Applied: odata.include-annotations="*"

{
  "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#contacts(fullname,jobtitle,annualincome,_transactioncurrencyid_value,transactioncurrencyid,contactid,transactioncurrencyid())",
  "@odata.count": 8,
  "@Microsoft.Dynamics.CRM.totalrecordcount": 8,
  "@Microsoft.Dynamics.CRM.totalrecordcountlimitexceeded": false,
  "@Microsoft.Dynamics.CRM.globalmetadataversion": "1144249",
  "value": [
    {
      "@odata.etag": "W/\"1146759\"",
      "fullname": "Susanna Stubberod (sample)",
      "jobtitle": "Senior Purchaser",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$52,000.00",
      "annualincome": 52000.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
      "contactid": "85716234-9628-ed11-9db1-000d3a320482"
    },
    {
      "@odata.etag": "W/\"1146765\"",
      "fullname": "Scott Konersmann (sample)",
      "jobtitle": "Accounts Manager",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$38,000.00",
      "annualincome": 38000.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
      "contactid": "91716234-9628-ed11-9db1-000d3a320482"
    },
    {
      "@odata.etag": "W/\"1146767\"",
      "fullname": "Robert Lyon (sample)",
      "jobtitle": "Senior Technician",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$78,000.00",
      "annualincome": 78000.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
      "contactid": "95716234-9628-ed11-9db1-000d3a320482"
    },
    {
      "@odata.etag": "W/\"1146771\"",
      "fullname": "Rene Valdes (sample)",
      "jobtitle": "Data Analyst III",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$86,000.00",
      "annualincome": 86000.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
      "contactid": "9d716234-9628-ed11-9db1-000d3a320482"
    },
    {
      "@odata.etag": "W/\"1146769\"",
      "fullname": "Paul Cannon (sample)",
      "jobtitle": "Ski Instructor",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$68,500.00",
      "annualincome": 68500.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
      "contactid": "99716234-9628-ed11-9db1-000d3a320482"
    },
    {
      "@odata.etag": "W/\"1146761\"",
      "fullname": "Nancy Anderson (sample)",
      "jobtitle": "Activities Manager",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$55,500.00",
      "annualincome": 55500.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
      "contactid": "89716234-9628-ed11-9db1-000d3a320482"
    },
    {
      "@odata.etag": "W/\"1146763\"",
      "fullname": "Maria Cambell (sample)",
      "jobtitle": "Accounts Manager",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$31,000.00",
      "annualincome": 31000.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
      "contactid": "8d716234-9628-ed11-9db1-000d3a320482"
    },
    {
      "@odata.etag": "W/\"1146773\"",
      "fullname": "Jim Glynn (sample)",
      "jobtitle": "Senior International Sales Manager",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$81,400.00",
      "annualincome": 81400.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
      "contactid": "a1716234-9628-ed11-9db1-000d3a320482"
    }
  ]
}
--batchresponse_ed1a482b-c942-4da4-8257-adaa53acc8e0--

```
  
   **Console output:**
  
```text
Contacts Fetched by fullname containing '(sample)':
        |Full Name                  |Job Title                          |Annual Income
        |---------------------------|-----------------------------------|---------------
        |Susanna Stubberod (sample) |Senior Purchaser                   |$52,000.00
        |Scott Konersmann (sample)  |Accounts Manager                   |$38,000.00
        |Robert Lyon (sample)       |Senior Technician                  |$78,000.00
        |Rene Valdes (sample)       |Data Analyst III                   |$86,000.00
        |Paul Cannon (sample)       |Ski Instructor                     |$68,500.00
        |Nancy Anderson (sample)    |Activities Manager                 |$55,500.00
        |Maria Cambell (sample)     |Accounts Manager                   |$31,000.00
        |Jim Glynn (sample)         |Senior International Sales Manager |$81,400.00
```  
  
### FetchXML pagination

The way FetchXML handles paging is different from how a query filter handles it. In FetchXML, you can specify a `count` column that indicates how many results to return per page. In the same request, use the `page` column to specify the page number to return.

The following operation requests page 2 from the previous FetchXML sample. Based on our sample data, we should have eight contacts in our result. Breaking down each page to four contacts per page, we should have two pages. Page 2 should contain only four contacts. If we then ask for page 3, the system returns zero results.
  
```xml  
<fetch mapping="logical" 
        output-format="xml-platform" 
        version="1.0" 
        distinct="false"
        page="2"  
        count="4">  
  <entity name="contact">  
    <attribute name="fullname" />  
    <attribute name="jobtitle" />  
    <attribute name="annualincome" />  
    <order descending="true"  
           attribute="fullname" />  
    <filter type="and">  
      <condition value="%(sample)%"  
                 attribute="fullname"  
                 operator="like" />
      <condition value="7d716234-9628-ed11-9db1-000d3a320482"
                 attribute="parentcustomerid"
                 operator="eq" /> 
    </filter>  
  </entity>  
</fetch>  
```  
  
**Request:**

```http
GET [Organization Uri]/api/data/v9.2/contacts?fetchXml=%3Cfetch+mapping%3D%22logical%22+output-format%3D%22xml-platform%22+version%3D%221.0%22+distinct%3D%22false%22+count%3D%224%22+page%3D%222%22%3E%0D%0A++%3Centity+name%3D%22contact%22%3E%0D%0A++++%3Cattribute+name%3D%22fullname%22+%2F%3E%0D%0A++++%3Cattribute+name%3D%22jobtitle%22+%2F%3E%0D%0A++++%3Cattribute+name%3D%22annualincome%22+%2F%3E%0D%0A++++%3Corder+descending%3D%22true%22+attribute%3D%22fullname%22+%2F%3E%0D%0A++++%3Cfilter+type%3D%22and%22%3E%0D%0A++++++%3Ccondition+value%3D%22%25(sample)%25%22+attribute%3D%22fullname%22+operator%3D%22like%22+%2F%3E%0D%0A++++++%3Ccondition+value%3D%227d716234-9628-ed11-9db1-000d3a320482%22+attribute%3D%22parentcustomerid%22+operator%3D%22eq%22+%2F%3E%0D%0A++++%3C%2Ffilter%3E%0D%0A++%3C%2Fentity%3E%0D%0A%3C%2Ffetch%3E&$count=true HTTP/1.1
Prefer: odata.include-annotations="*"
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
```

**Response:**

```http
HTTP/1.1 200 OK
OData-Version: 4.0
Preference-Applied: odata.include-annotations="*"

{
  "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#contacts(fullname,jobtitle,annualincome,_transactioncurrencyid_value,transactioncurrencyid,contactid,transactioncurrencyid())",
  "@odata.count": 8,
  "@Microsoft.Dynamics.CRM.totalrecordcount": 8,
  "@Microsoft.Dynamics.CRM.totalrecordcountlimitexceeded": false,
  "@Microsoft.Dynamics.CRM.globalmetadataversion": "1144249",
  "value": [
    {
      "@odata.etag": "W/\"1147963\"",
      "fullname": "Paul Cannon (sample)",
      "jobtitle": "Ski Instructor",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$68,500.00",
      "annualincome": 68500.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
      "contactid": "99716234-9628-ed11-9db1-000d3a320482"
    },
    {
      "@odata.etag": "W/\"1147945\"",
      "fullname": "Nancy Anderson (sample)",
      "jobtitle": "Activities Manager",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$55,500.00",
      "annualincome": 55500.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
      "contactid": "89716234-9628-ed11-9db1-000d3a320482"
    },
    {
      "@odata.etag": "W/\"1147948\"",
      "fullname": "Maria Cambell (sample)",
      "jobtitle": "Accounts Manager",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$31,000.00",
      "annualincome": 31000.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
      "contactid": "8d716234-9628-ed11-9db1-000d3a320482"
    },
    {
      "@odata.etag": "W/\"1147979\"",
      "fullname": "Jim Glynn (sample)",
      "jobtitle": "Senior International Sales Manager",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$81,400.00",
      "annualincome": 81400.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac",
      "contactid": "a1716234-9628-ed11-9db1-000d3a320482"
    }
  ]
}
```
  
**Console output:**  
  
```text
Contacts Fetched by fullname containing '(sample)' - Page 2:
        |Full Name                  |Job Title                          |Annual Income
        |---------------------------|-----------------------------------|---------------
        |Paul Cannon (sample)       |Ski Instructor                     |$68,500.00
        |Nancy Anderson (sample)    |Activities Manager                 |$55,500.00
        |Maria Cambell (sample)     |Accounts Manager                   |$31,000.00
        |Jim Glynn (sample)         |Senior International Sales Manager |$81,400.00
```  
  
<a name="bkmk_predefinedqueries"></a>
 
## Section 9: Use predefined queries

You can use the Web API to [retrieve and execute predefined queries](retrieve-and-execute-predefined-queries.md).
  
### Saved query

In this operation, we request the `savedqueryid` GUID of the saved query named **Active Accounts**. Then we use the GUID and the `savedQuery` parameter to query for a list of active accounts.

First, we get the saved query's GUID.
  
**Request:**

```http
GET [Organization Uri]/api/data/v9.2/savedqueries?$select=name,savedqueryid&$filter=name eq 'Active Accounts' HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
```

**Response:**

```http
HTTP/1.1 200 OK
OData-Version: 4.0

{
  "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#savedqueries(name,savedqueryid)",
  "value": [
    {
      "@odata.etag": "W/\"966435\"",
      "name": "Active Accounts",
      "savedqueryid": "00000000-0000-0000-00aa-000010001002"
    }
  ]
}
```
  
Next, we use the `savedQuery` parameter to get the saved query's content.
  
**Request:**

```http
GET [Organization Uri]/api/data/v9.2/accounts?savedQuery=00000000-0000-0000-00aa-000010001002 HTTP/1.1
Prefer: odata.maxpagesize=3; odata.include-annotations="*"
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
```

**Response:**

```http
HTTP/1.1 200 OK
OData-Version: 4.0
Preference-Applied: odata.include-annotations="*"; odata.maxpagesize=3

{
  "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#accounts(name,_primarycontactid_value,primarycontactid,accountid,address1_city,telephone1,primarycontactid())",
  "@Microsoft.Dynamics.CRM.totalrecordcount": -1,
  "@Microsoft.Dynamics.CRM.totalrecordcountlimitexceeded": false,
  "@Microsoft.Dynamics.CRM.globalmetadataversion": "1144249",
  "@accountprimarycontactidcontactcontactid.OData.Community.Display.V1.CurrentEntityField": "primarycontactid",
  "value": [
    {
      "@odata.etag": "W/\"1147935\"",
      "name": "Contoso, Ltd. (sample)",
      "_primarycontactid_value@OData.Community.Display.V1.FormattedValue": "Yvonne McKay (sample)",
      "_primarycontactid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "primarycontactid",
      "_primarycontactid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "contact",
      "_primarycontactid_value": "d36e86e2-a228-ed11-9db1-000d3a320482",
      "accountid": "cf6e86e2-a228-ed11-9db1-000d3a320482"
    }
  ]
}
```
  
**Console output:**  
  
```text
-- Saved Query --

Active Accounts
        1) Contoso, Ltd. (sample), Yvonne McKay (sample), NULL
```  
  
### User query

This sample creates a user query, executes it, then deletes it from the system.

**Request:**

```http
POST [Organization Uri]/api/data/v9.2/userqueries HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json

{
  "name": "My User Query",
  "description": "User query to display contact info.",
  "querytype": 0,
  "returnedtypecode": "contact",
  "fetchxml": "<fetch mapping='logical' output-format='xml-platform' version='1.0' distinct='false'>
    <entity name ='contact'>
      <attribute name ='fullname' />
      <attribute name ='contactid' />
      <attribute name ='jobtitle' />
      <attribute name ='annualincome' />
      <order descending ='false' attribute='fullname' />
      <filter type ='and'>
         <condition value ='%(sample)%' attribute='fullname' operator='like' />
         <condition value ='%Manager%' attribute='jobtitle' operator='like' />
         <condition value ='55000' attribute='annualincome' operator='gt' />
      </filter>
    </entity>
</fetch>"
}
```

**Response:**

```http
HTTP/1.1 204 NoContent
OData-Version: 4.0
OData-EntityId: [Organization Uri]/api/data/v9.2/userqueries(f76e86e2-a228-ed11-9db1-000d3a320482)
```

This user query asks for any contacts where `fullname` contains `(sample)`, `jobtitle` contains `manager`, and `annualincome` is greater than `55000`. Our sample data has two contacts that match the query.

In the sample code, the `userqueryid` value is returned with the request that creates it. Normally, you'd need to query the system to retrieve it using a query like the following one:
  
**Request:**
  
```http
GET https://[Organization URI]/api/data/v9.0/userqueries?$select=name,userqueryid,&$filter=name%20eq%20'My%20User%20Query' HTTP/1.1  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
Content-Type: application/json; charset=utf-8  
  
```  
  
**Response:**
  
```http
HTTP/1.1 200 OK
Content-Type: application/json; odata.metadata=minimal  
OData-Version: 4.0  
Content-Length: 246  
  
{   
   "@odata.context":"https://[Organization URI]/api/data/v9.0/$metadata#userqueries(name,userqueryid)",  
   "value":[   
      {   
         "@odata.etag":"W/\"621698\"",  
         "name":"My User Query",  
         "userqueryid":"f76e86e2-a228-ed11-9db1-000d3a320482"  
      }  
   ]  
}  
```  
  
This example passes the GUID value with the `userQuery` parameter to get the user query's content.
  
**Request:**

```http
GET [Organization Uri]/api/data/v9.2/contacts?userQuery=f76e86e2-a228-ed11-9db1-000d3a320482 HTTP/1.1
Prefer: odata.maxpagesize=3; odata.include-annotations="*"
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
```

**Response:**

```http
HTTP/1.1 200 OK
OData-Version: 4.0
Preference-Applied: odata.include-annotations="*"; odata.maxpagesize=3

{
  "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#contacts(fullname,contactid,jobtitle,annualincome,_transactioncurrencyid_value,transactioncurrencyid,transactioncurrencyid())",
  "@Microsoft.Dynamics.CRM.totalrecordcount": -1,
  "@Microsoft.Dynamics.CRM.totalrecordcountlimitexceeded": false,
  "@Microsoft.Dynamics.CRM.globalmetadataversion": "1144249",
  "value": [
    {
      "@odata.etag": "W/\"1147979\"",
      "fullname": "Jim Glynn (sample)",
      "contactid": "f36e86e2-a228-ed11-9db1-000d3a320482",
      "jobtitle": "Senior International Sales Manager",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$81,400.00",
      "annualincome": 81400.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac"
    },
    {
      "@odata.etag": "W/\"1147945\"",
      "fullname": "Nancy Anderson (sample)",
      "contactid": "db6e86e2-a228-ed11-9db1-000d3a320482",
      "jobtitle": "Activities Manager",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$55,500.00",
      "annualincome": 55500.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "daf76074-6820-ed11-b83b-00224802b2ac"
    }
  ]
}
```
  
**Console output:**  
  
```text
-- User Query --

Contacts Fetched by My User Query:
        |Full Name                  |Job Title                          |Annual Income
        |---------------------------|-----------------------------------|---------------
        |Jim Glynn (sample)         |Senior International Sales Manager |$81,400.00
        |Nancy Anderson (sample)    |Activities Manager                 |$55,500.00
```  

## Section 10: Delete sample records

Use a `$batch` operation to delete all the records created in [Section 0: Create records to query](#section-0-create-records-to-query).

**Request:**

```http
POST [Organization Uri]/api/data/v9.2/$batch HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json

--batch_23ea682f-a60a-412a-b37d-7df10a976508
Content-Type: application/http
Content-Transfer-Encoding: binary
Content-Length: 121

DELETE /api/data/v9.2/contacts(f36e86e2-a228-ed11-9db1-000d3a320482) HTTP/1.1


--batch_23ea682f-a60a-412a-b37d-7df10a976508
Content-Type: application/http
Content-Transfer-Encoding: binary
Content-Length: 121

DELETE /api/data/v9.2/contacts(ef6e86e2-a228-ed11-9db1-000d3a320482) HTTP/1.1


--batch_23ea682f-a60a-412a-b37d-7df10a976508
Content-Type: application/http
Content-Transfer-Encoding: binary
Content-Length: 121

DELETE /api/data/v9.2/contacts(eb6e86e2-a228-ed11-9db1-000d3a320482) HTTP/1.1


--batch_23ea682f-a60a-412a-b37d-7df10a976508
Content-Type: application/http
Content-Transfer-Encoding: binary
Content-Length: 121

DELETE /api/data/v9.2/contacts(e76e86e2-a228-ed11-9db1-000d3a320482) HTTP/1.1


--batch_23ea682f-a60a-412a-b37d-7df10a976508
Content-Type: application/http
Content-Transfer-Encoding: binary
Content-Length: 121

DELETE /api/data/v9.2/contacts(e36e86e2-a228-ed11-9db1-000d3a320482) HTTP/1.1


--batch_23ea682f-a60a-412a-b37d-7df10a976508
Content-Type: application/http
Content-Transfer-Encoding: binary
Content-Length: 121

DELETE /api/data/v9.2/contacts(df6e86e2-a228-ed11-9db1-000d3a320482) HTTP/1.1


--batch_23ea682f-a60a-412a-b37d-7df10a976508
Content-Type: application/http
Content-Transfer-Encoding: binary
Content-Length: 121

DELETE /api/data/v9.2/contacts(db6e86e2-a228-ed11-9db1-000d3a320482) HTTP/1.1


--batch_23ea682f-a60a-412a-b37d-7df10a976508
Content-Type: application/http
Content-Transfer-Encoding: binary
Content-Length: 121

DELETE /api/data/v9.2/contacts(d76e86e2-a228-ed11-9db1-000d3a320482) HTTP/1.1


--batch_23ea682f-a60a-412a-b37d-7df10a976508
Content-Type: application/http
Content-Transfer-Encoding: binary
Content-Length: 121

DELETE /api/data/v9.2/accounts(cf6e86e2-a228-ed11-9db1-000d3a320482) HTTP/1.1


--batch_23ea682f-a60a-412a-b37d-7df10a976508
Content-Type: application/http
Content-Transfer-Encoding: binary
Content-Length: 121

DELETE /api/data/v9.2/contacts(d36e86e2-a228-ed11-9db1-000d3a320482) HTTP/1.1


--batch_23ea682f-a60a-412a-b37d-7df10a976508
Content-Type: application/http
Content-Transfer-Encoding: binary
Content-Length: 124

DELETE /api/data/v9.2/userqueries(f76e86e2-a228-ed11-9db1-000d3a320482) HTTP/1.1


--batch_23ea682f-a60a-412a-b37d-7df10a976508--

```

**Response:**

```http
HTTP/1.1 200 OK
OData-Version: 4.0

--batchresponse_1e45a745-8b68-401f-a1c0-0081ec083cdc
Content-Type: application/http
Content-Transfer-Encoding: binary

HTTP/1.1 204 No Content
OData-Version: 4.0


--batchresponse_1e45a745-8b68-401f-a1c0-0081ec083cdc
Content-Type: application/http
Content-Transfer-Encoding: binary

HTTP/1.1 204 No Content
OData-Version: 4.0


--batchresponse_1e45a745-8b68-401f-a1c0-0081ec083cdc
Content-Type: application/http
Content-Transfer-Encoding: binary

HTTP/1.1 204 No Content
OData-Version: 4.0


--batchresponse_1e45a745-8b68-401f-a1c0-0081ec083cdc
Content-Type: application/http
Content-Transfer-Encoding: binary

HTTP/1.1 204 No Content
OData-Version: 4.0


--batchresponse_1e45a745-8b68-401f-a1c0-0081ec083cdc
Content-Type: application/http
Content-Transfer-Encoding: binary

HTTP/1.1 204 No Content
OData-Version: 4.0


--batchresponse_1e45a745-8b68-401f-a1c0-0081ec083cdc
Content-Type: application/http
Content-Transfer-Encoding: binary

HTTP/1.1 204 No Content
OData-Version: 4.0


--batchresponse_1e45a745-8b68-401f-a1c0-0081ec083cdc
Content-Type: application/http
Content-Transfer-Encoding: binary

HTTP/1.1 204 No Content
OData-Version: 4.0


--batchresponse_1e45a745-8b68-401f-a1c0-0081ec083cdc
Content-Type: application/http
Content-Transfer-Encoding: binary

HTTP/1.1 204 No Content
OData-Version: 4.0


--batchresponse_1e45a745-8b68-401f-a1c0-0081ec083cdc
Content-Type: application/http
Content-Transfer-Encoding: binary

HTTP/1.1 204 No Content
OData-Version: 4.0


--batchresponse_1e45a745-8b68-401f-a1c0-0081ec083cdc
Content-Type: application/http
Content-Transfer-Encoding: binary

HTTP/1.1 204 No Content
OData-Version: 4.0


--batchresponse_1e45a745-8b68-401f-a1c0-0081ec083cdc
Content-Type: application/http
Content-Transfer-Encoding: binary

HTTP/1.1 204 No Content
OData-Version: 4.0


--batchresponse_1e45a745-8b68-401f-a1c0-0081ec083cdc--

```


  
### See also

[Use the Dataverse Web API](overview.md)   
[Query Data using the Web API](query-data-web-api.md)   
[Retrieve and execute predefined queries](retrieve-and-execute-predefined-queries.md)   
[Web API Query Data Sample (C#)](samples/webapiservice-query-data.md)   
[Web API Query Data Sample (Client-side JavaScript)](samples/query-data-client-side-javascript.md)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
