---
title: "Web API Query Data Sample (Microsoft Dataverse)| Microsoft Docs"
description: "These code samples shows how to query data using the Web API. These samples are implemented using client-side JavaScript and C#."
ms.custom: ""
ms.date: 06/15/2021
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
ms.assetid: 9457ce4f-0ef6-4085-8346-fe3134ec7106
caps.latest.revision: 18
author: "JimDaly" # GitHub ID
ms.author: "jdaly"
ms.reviewer: "pehecke"
manager: "annbe"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Web API Query Data Sample

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

This group of  samples demonstrate how to query data using the Microsoft Dataverse Web API. This sample is implemented as a separate project for the following languages:

- [Web API Query Data Sample (Client-side JavaScript)](samples/query-data-client-side-javascript.md)

- [Query Data Sample (C#)](samples/cdswebapiservice-query-data.md)

This topic describes a common set of operations implemented by each sample in this group. This topic describes the HTTP requests and responses and text output that each sample in this group will perform without the language specific details. See the language specific descriptions and the individual samples for details about how this operations are performed.

## Demonstrates

This sample is divided into the following principal sections, containing Web API query data operations which are discussed in greater detail in the associated conceptual topics.

|Topic section|Associated topic(s)|
|-------------------|---------------------------|
|[Selecting specific properties](#bkmk_selectproperties)|[Retrieve specific properties](retrieve-entity-using-web-api.md#bkmk_requestProperties)<br /><br /> [Include formatted values](query-data-web-api.md#bkmk_includeFormattedValues)|
|[Using query functions](#bkmk_queryfunctions)|[Filter results](query-data-web-api.md#bkmk_filter)<br /><br /> [Standard query functions](query-data-web-api.md#bkmk_buildInQueryFunctions)<br /><br /> [Compose a query with functions](use-web-api-functions.md#bkmk_composeQueryWithFunctions)<br /><br /> <xref:Microsoft.Dynamics.CRM.QueryFunctionIndex>|
|[Using operators](#bkmk_operators)|[Standard filter operators](query-data-web-api.md#bkmk_buildInFilterOperators)|
|[Setting precedence](#bkmk_prededence)|[Standard filter operators](query-data-web-api.md#bkmk_buildInFilterOperators)|
|[Ordering results](#bkmk_orderresults)|[Order results](query-data-web-api.md#bkmk_order)<br /><br /> [Filter results](query-data-web-api.md#bkmk_filter)|
|[Parameter alias](#bkmk_parameteralias)|[Use parameter aliases with system query options](query-data-web-api.md#bkmk_useParameterAliases)|
|[Limit results](#bkmk_limitresults)|[Limit results](query-data-web-api.md#bkmk_limitResults)<br /><br /> [Limits on number of rows returned](query-data-web-api.md#bkmk_limits)|
|[Expanding results](#bkmk_expandresults)|[Retrieve related rows by expanding navigation properties](query-data-web-api.md#bkmk_expandRelated)|
|[Predefined queries](#bkmk_predefinedqueries)|[Retrieve and execute predefined queries](retrieve-and-execute-predefined-queries.md)<br /><br /> <xref:Microsoft.Dynamics.CRM.userquery?text=userquery EntityType/><br /><br /> <xref:Microsoft.Dynamics.CRM.savedquery?text=savedquery EntityType/>|
<!-- TODO:
|[FetchXML queries](#bkmk_fetchxml)|[FetchXML schema](../org-service/fetchxml-schema.md)<br /><br /> [Page large result sets with FetchXML](../org-service/page-large-result-sets-with-fetchxml.md)<br /><br /> [Use custom FetchXML](retrieve-and-execute-predefined-queries.md#bkmk_useFetchXML)| -->

The following sections contain a brief discussion of the Dataverse Web API operations performed, along with the corresponding HTTP messages and associated console output.

<a name="bkmk_sampleData"></a>

## Sample data

To ensure the queries in this sample work properly, a standard set of sample rows is created by this sample. These sample rows will be deleted unless the user chooses to not delete them. This is the data the sample will be querying. You may get different results depending on any existing data in your environment.  
  
The data is added using *deep insert* in a single `POST` request and matches the following structure:  
  
```json  
  
 {  
        "name": "Contoso, Ltd. (sample)",  
        "primarycontactid": {  
            "firstname": "Yvonne", "lastname": "McKay (sample)", "jobtitle": "Coffee Master",  
            "annualincome": 45000, "Contact_Tasks": [  
            { "subject": "Task 1", "description": "Task 1 description" },  
            { "subject": "Task 2", "description": "Task 2 description" },  
            { "subject": "Task 3", "description": "Task 3 description" }  
            ]  
        },   
							"Account_Tasks": [  
        { "subject": "Task 1", "description": "Task 1 description" },  
        { "subject": "Task 2", "description": "Task 2 description" },  
        { "subject": "Task 3", "description": "Task 3 description" }  
        ],  
        "contact_customer_accounts": [  
            {  
                "firstname": "Susanna", "lastname": "Stubberod (sample)", "jobtitle": "Senior Purchaser",  
                "annualincome": 52000, "Contact_Tasks": [  
            { "subject": "Task 1", "description": "Task 1 description" },  
            { "subject": "Task 2", "description": "Task 2 description" },  
            { "subject": "Task 3", "description": "Task 3 description" }  
                ]  
            },  
            {  
                "firstname": "Nancy", "lastname": "Anderson (sample)", "jobtitle": "Activities Manager",  
                "annualincome": 55500, "Contact_Tasks": [  
                { "subject": "Task 1", "description": "Task 1 description" },  
                { "subject": "Task 2", "description": "Task 2 description" },  
                { "subject": "Task 3", "description": "Task 3 description" }  
                ]  
            },  
            {  
                "firstname": "Maria", "lastname": "Cambell (sample)", "jobtitle": "Accounts Manager",  
                "annualincome": 31000, "Contact_Tasks": [  
                { "subject": "Task 1", "description": "Task 1 description" },  
                { "subject": "Task 2", "description": "Task 2 description" },  
                { "subject": "Task 3", "description": "Task 3 description" }  
                ]  
            },  
            {  
                "firstname": "Nancy", "lastname": "Anderson (sample)", "jobtitle": "Logistics Specialist",  
                "annualincome": 63500, "Contact_Tasks": [  
                { "subject": "Task 1", "description": "Task 1 description" },  
                { "subject": "Task 2", "description": "Task 2 description" },  
                { "subject": "Task 3", "description": "Task 3 description" }  
                ]  
            },  
            {  
                "firstname": "Scott", "lastname": "Konersmann (sample)", "jobtitle": "Accounts Manager",  
                "annualincome": 38000, "Contact_Tasks": [  
                { "subject": "Task 1", "description": "Task 1 description" },  
                { "subject": "Task 2", "description": "Task 2 description" },  
                { "subject": "Task 3", "description": "Task 3 description" }  
                ]  
            },  
            {  
                "firstname": "Robert", "lastname": "Lyon (sample)", "jobtitle": "Senior Technician",  
                "annualincome": 78000, "Contact_Tasks": [  
                { "subject": "Task 1", "description": "Task 1 description" },  
                { "subject": "Task 2", "description": "Task 2 description" },  
                { "subject": "Task 3", "description": "Task 3 description" }  
                ]  
            },  
            {  
                "firstname": "Paul", "lastname": "Cannon (sample)", "jobtitle": "Ski Instructor",  
                "annualincome": 68500, "Contact_Tasks": [  
                { "subject": "Task 1", "description": "Task 1 description" },  
                { "subject": "Task 2", "description": "Task 2 description" },  
                { "subject": "Task 3", "description": "Task 3 description" }  
                ]  
            },  
            {  
                "firstname": "Rene", "lastname": "Valdes (sample)", "jobtitle": "Data Analyst III",  
                "annualincome": 86000, "Contact_Tasks": [  
                { "subject": "Task 1", "description": "Task 1 description" },  
                { "subject": "Task 2", "description": "Task 2 description" },  
                { "subject": "Task 3", "description": "Task 3 description" }  
                ]  
            },  
            {  
                "firstname": "Jim", "lastname": "Glynn (sample)", "jobtitle": "Senior International Sales Manager",  
                "annualincome": 81400, "Contact_Tasks": [  
                { "subject": "Task 1", "description": "Task 1 description" },  
                { "subject": "Task 2", "description": "Task 2 description" },  
                { "subject": "Task 3", "description": "Task 3 description" }  
                ]  
            }  
        ]  
    }  
```  
  
<a name="bkmk_selectproperties"></a>

## Selecting specific properties
  
Always construct  queries using the `$select` query option, otherwise the server will return all properties of each table row which reduces performance. This example demonstrates how to construct a basic query by selecting three properties of a <xref href="Microsoft.Dynamics.CRM.contact?text=contact EntityType" />. The properties are `fullname`, `jobtitle`, `annualincome`. The section also illustrates the differences between formatted and unformatted values as seen in the results of the contact's `annualincome` property. More information:[Request specific properties](query-data-web-api.md#bkmk_requestProperties), [Include formatted values](query-data-web-api.md#bkmk_includeFormattedValues).  
  
In this example, we are requesting for a specific contact. In this case, it's the primary contact of the account, `Yvonne McKay (sample)`.  
  
 **HTTP Request**  
  
```  
GET https://[Organization URI]/api/data/v9.0/contacts(b848fdee-c143-e611-80d5-00155da84802)?$select=fullname,jobtitle,annualincome HTTP/1.1  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
Content-Type: application/json; charset=utf-8  
Prefer: odata.maxpagesize=10, odata.include-annotations=OData.Community.Display.V1.FormattedValue  
```  
  
 **HTTP Response**  
  
```  
HTTP/1.1 200 OK  
Content-Type: application/json; odata.metadata=minimal  
OData-Version: 4.0  
Preference-Applied: odata.include-annotations="OData.Community.Display.V1.FormattedValue"  
Preference-Applied: odata.maxpagesize=10  
Content-Length: 517  
  
{  
   "@odata.context":"https://[Organization URI]/api/data/v9.0/$metadata#contacts(fullname,jobtitle,annualincome)/$entity",  
   "@odata.etag":"W/\"619718\"",  
   "fullname":"Yvonne McKay (sample)",  
   "jobtitle":"Coffee Master",  
   "annualincome@OData.Community.Display.V1.FormattedValue":"$45,000.00",  
   "annualincome":45000.0000,  
   "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
   "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
   "contactid":"15c364b2-bf43-e611-80d5-00155da84802"  
}  
```  
  
 **Console output**  
  
```  
Contact basic info:  
	Fullname: 'Yvonne McKay (sample)'  
	Jobtitle: 'Coffee Master'  
	Annualincome: '45000' (unformatted)  
	Annualincome: $45,000.00 (formatted)  
  
```  
  
<a name="bkmk_queryfunctions"></a>
  
## Using query functions
 
Use filter options to set criteria for the results you want. You can  build simple to complex filters using a combination of query functions, comparison operators, and logical operators. More information:[Filter results](query-data-web-api.md#bkmk_filter).  
  
Query functions are functions that can be used as a filter criteria in a query. There are standard query functions and Dataverse specific query functions. These functions accept parameters and return a `Boolean` value. This sample illustrates how to create a query for each type.  
  
### Standard query functions

Dataverse supports a small subset of OData built-in query functions, specifically: `contains`, `endswith`, and `startswith`. For example, the `contains` standard query function allows us to filter for properties matching a string. In this operation, we are querying for all contacts with `fullname` containing the string `(sample)`. More information:[Standard query functions](query-data-web-api.md#bkmk_buildInQueryFunctions).  
  
 **HTTP Request**  
  
```  
GET https://[Organization URI]/api/data/v9.0/contacts?$select=fullname,jobtitle,annualincome&$filter=contains(fullname,'(sample)') HTTP/1.1  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
Content-Type: application/json; charset=utf-8  
Prefer: odata.maxpagesize=10, odata.include-annotations=OData.Community.Display.V1.FormattedValue  
```  
  
 **HTTP Response**  
  
```  
HTTP/1.1 200 OK  
Content-Type: application/json; odata.metadata=minimal  
OData-Version: 4.0  
Preference-Applied: odata.include-annotations="OData.Community.Display.V1.FormattedValue"  
Preference-Applied: odata.maxpagesize=10  
Content-Length: 4284  
  
{  
   "@odata.context":"https://[Organization URI]/api/data/v9.0/$metadata#contacts(fullname,jobtitle,annualincome)",  
   "value":[  
      {  
         "@odata.etag":"W/\"619718\"",  
         "fullname":"Yvonne McKay (sample)",  
         "jobtitle":"Coffee Master",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$45,000.00",  
         "annualincome":45000.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"15c364b2-bf43-e611-80d5-00155da84802"  
      },  
      {  
         "@odata.etag":"W/\"619839\"",  
         "fullname":"Susanna Stubberod (sample)",  
         "jobtitle":"Senior Purchaser",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$52,000.00",  
         "annualincome":52000.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"1cc364b2-bf43-e611-80d5-00155da84802"  
      },  
      {  
         "@odata.etag":"W/\"619841\"",  
         "fullname":"Nancy Anderson (sample)",  
         "jobtitle":"Activities Manager",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$55,500.00",  
         "annualincome":55500.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"20c364b2-bf43-e611-80d5-00155da84802"  
      },  
      {  
         "@odata.etag":"W/\"619843\"",  
         "fullname":"Maria Cambell (sample)",  
         "jobtitle":"Accounts Manager",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$31,000.00",  
         "annualincome":31000.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"24c364b2-bf43-e611-80d5-00155da84802"  
      },  
      {  
         "@odata.etag":"W/\"619845\"",  
         "fullname":"Nancy Anderson (sample)",  
         "jobtitle":"Logistics Specialist",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$63,500.00",  
         "annualincome":63500.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"28c364b2-bf43-e611-80d5-00155da84802"  
      },  
      {  
         "@odata.etag":"W/\"619847\"",  
         "fullname":"Scott Konersmann (sample)",  
         "jobtitle":"Accounts Manager",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$38,000.00",  
         "annualincome":38000.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"2cc364b2-bf43-e611-80d5-00155da84802"  
      },  
      {  
         "@odata.etag":"W/\"619849\"",  
         "fullname":"Robert Lyon (sample)",  
         "jobtitle":"Senior Technician",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$78,000.00",  
         "annualincome":78000.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"30c364b2-bf43-e611-80d5-00155da84802"  
      },  
      {  
         "@odata.etag":"W/\"619851\"",  
         "fullname":"Paul Cannon (sample)",  
         "jobtitle":"Ski Instructor",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$68,500.00",  
         "annualincome":68500.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"34c364b2-bf43-e611-80d5-00155da84802"  
      },  
      {  
         "@odata.etag":"W/\"619853\"",  
         "fullname":"Rene Valdes (sample)",  
         "jobtitle":"Data Analyst III",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$86,000.00",  
         "annualincome":86000.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"38c364b2-bf43-e611-80d5-00155da84802"  
      },  
      {  
         "@odata.etag":"W/\"619855\"",  
         "fullname":"Jim Glynn (sample)",  
         "jobtitle":"Senior International Sales Manager",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$81,400.00",  
         "annualincome":81400.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"3cc364b2-bf43-e611-80d5-00155da84802"  
      }  
   ]  
}  
```  
  
 **Console output**  
  
```  
Contacts filtered by fullname containing '(sample)':  
	1) Yvonne McKay (sample), Coffee Master, $45,000.00  
	2) Susanna Stubberod (sample), Senior Purchaser, $52,000.00  
	3) Nancy Anderson (sample), Activities Manager, $55,500.00  
	4) Maria Cambell (sample), Accounts Manager, $31,000.00  
	5) Nancy Anderson (sample), Logistics Specialist, $63,500.00  
	6) Scott Konersmann (sample), Accounts Manager, $38,000.00  
	7) Robert Lyon (sample), Senior Technician, $78,000.00  
	8) Paul Cannon (sample), Ski Instructor, $68,500.00  
	9) Rene Valdes (sample), Data Analyst III, $86,000.00  
	10) Jim Glynn (sample), Senior International Sales Manager, $81,400.00  
  
```  
  
### Dataverse query functions

Dataverse query functions provide a large number of options to build queries which are relevant for Dataverse. For a complete list of these functions, see <xref:Microsoft.Dynamics.CRM.QueryFunctionIndex>. More information:[Compose a query with functions](use-web-api-functions.md#bkmk_composeQueryWithFunctions)  
  
You will use these query functions in a manner similar to the standard query functions. The main difference is, when using Dataverse query functions, you must provide the full name of the function including the parameter name(s). For example, to get a list of contacts created in the last hour, you can construct a query using the <xref href="Microsoft.Dynamics.CRM.LastXHours?text=LastXHours Function" />.  
  
 **HTTP Request**  
  
```  
GET https://[Organization URI]/api/data/v9.0/contacts?$select=fullname,jobtitle,annualincome&$filter=Microsoft.Dynamics.CRM.LastXHours(PropertyName='createdon',PropertyValue='1') HTTP/1.1  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
Content-Type: application/json; charset=utf-8  
Prefer: odata.maxpagesize=10, odata.include-annotations=OData.Community.Display.V1.FormattedValue  
```  
  
 **HTTP Response**  
  
```  
HTTP/1.1 200 OK  
Content-Type: application/json; odata.metadata=minimal  
OData-Version: 4.0  
Preference-Applied: odata.include-annotations="OData.Community.Display.V1.FormattedValue"  
Preference-Applied: odata.maxpagesize=10  
Content-Length: 4284  
  
{  
   "@odata.context":"https://[Organization URI]/api/data/v9.0/$metadata#contacts(fullname,jobtitle,annualincome)",  
   "value":[  
      {  
         "@odata.etag":"W/\"619718\"",  
         "fullname":"Yvonne McKay (sample)",  
         "jobtitle":"Coffee Master",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$45,000.00",  
         "annualincome":45000.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"15c364b2-bf43-e611-80d5-00155da84802"  
      },  
      {  
         "@odata.etag":"W/\"619839\"",  
         "fullname":"Susanna Stubberod (sample)",  
         "jobtitle":"Senior Purchaser",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$52,000.00",  
         "annualincome":52000.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"1cc364b2-bf43-e611-80d5-00155da84802"  
      },  
      {  
         "@odata.etag":"W/\"619841\"",  
         "fullname":"Nancy Anderson (sample)",  
         "jobtitle":"Activities Manager",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$55,500.00",  
         "annualincome":55500.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"20c364b2-bf43-e611-80d5-00155da84802"  
      },  
      {  
         "@odata.etag":"W/\"619843\"",  
         "fullname":"Maria Cambell (sample)",  
         "jobtitle":"Accounts Manager",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$31,000.00",  
         "annualincome":31000.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"24c364b2-bf43-e611-80d5-00155da84802"  
      },  
      {  
         "@odata.etag":"W/\"619845\"",  
         "fullname":"Nancy Anderson (sample)",  
         "jobtitle":"Logistics Specialist",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$63,500.00",  
         "annualincome":63500.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"28c364b2-bf43-e611-80d5-00155da84802"  
      },  
      {  
         "@odata.etag":"W/\"619847\"",  
         "fullname":"Scott Konersmann (sample)",  
         "jobtitle":"Accounts Manager",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$38,000.00",  
         "annualincome":38000.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"2cc364b2-bf43-e611-80d5-00155da84802"  
      },  
      {  
         "@odata.etag":"W/\"619849\"",  
         "fullname":"Robert Lyon (sample)",  
         "jobtitle":"Senior Technician",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$78,000.00",  
         "annualincome":78000.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"30c364b2-bf43-e611-80d5-00155da84802"  
      },  
      {  
         "@odata.etag":"W/\"619851\"",  
         "fullname":"Paul Cannon (sample)",  
         "jobtitle":"Ski Instructor",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$68,500.00",  
         "annualincome":68500.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"34c364b2-bf43-e611-80d5-00155da84802"  
      },  
      {  
         "@odata.etag":"W/\"619853\"",  
         "fullname":"Rene Valdes (sample)",  
         "jobtitle":"Data Analyst III",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$86,000.00",  
         "annualincome":86000.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"38c364b2-bf43-e611-80d5-00155da84802"  
      },  
      {  
         "@odata.etag":"W/\"619855\"",  
         "fullname":"Jim Glynn (sample)",  
         "jobtitle":"Senior International Sales Manager",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$81,400.00",  
         "annualincome":81400.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"3cc364b2-bf43-e611-80d5-00155da84802"  
      }  
   ]  
}  
```  
  
 **Console output**  
  
```  
Contacts that were created within the last 1hr:  
	1) Yvonne McKay (sample), Coffee Master, $45,000.00  
	2) Susanna Stubberod (sample), Senior Purchaser, $52,000.00  
	3) Nancy Anderson (sample), Activities Manager, $55,500.00  
	4) Maria Cambell (sample), Accounts Manager, $31,000.00  
	5) Nancy Anderson (sample), Logistics Specialist, $63,500.00  
	6) Scott Konersmann (sample), Accounts Manager, $38,000.00  
	7) Robert Lyon (sample), Senior Technician, $78,000.00  
	8) Paul Cannon (sample), Ski Instructor, $68,500.00  
	9) Rene Valdes (sample), Data Analyst III, $86,000.00  
	10) Jim Glynn (sample), Senior International Sales Manager, $81,400.00  
```  
  
<a name="bkmk_operators"></a>

## Using operators

Use the [Standard filter operators](query-data-web-api.md#bkmk_buildInFilterOperators) (`eq`,`ne`,`gt`,`ge`,`lt`,`le`,`and`,`or`,`not`)  to further refine our results. In this example, we are requesting a list of all contacts with `fullname` containing `(sample)` and annual income greater than `55000`.  
  
 **HTTP Request**  
  
```  
GET https://[Organization URI]/api/data/v9.0/contacts?$select=fullname,jobtitle,annualincome&$filter=contains(fullname,'(sample)')%20and%20annualincome%20gt%2055000 HTTP/1.1  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
Content-Type: application/json; charset=utf-8  
Prefer: odata.maxpagesize=10, odata.include-annotations=OData.Community.Display.V1.FormattedValue  
```  
  
 **HTTP Response**  
  
```  
HTTP/1.1 200 OK  
Content-Type: application/json; odata.metadata=minimal  
OData-Version: 4.0  
Preference-Applied: odata.include-annotations="OData.Community.Display.V1.FormattedValue"  
Preference-Applied: odata.maxpagesize=10  
Content-Length: 2629  
  
{  
   "@odata.context":"https://[Organization URI]/api/data/v9.0/$metadata#contacts(fullname,jobtitle,annualincome)",  
   "value":[  
      {  
         "@odata.etag":"W/\"619841\"",  
         "fullname":"Nancy Anderson (sample)",  
         "jobtitle":"Activities Manager",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$55,500.00",  
         "annualincome":55500.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"20c364b2-bf43-e611-80d5-00155da84802"  
      },  
      {  
         "@odata.etag":"W/\"619845\"",  
         "fullname":"Nancy Anderson (sample)",  
         "jobtitle":"Logistics Specialist",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$63,500.00",  
         "annualincome":63500.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"28c364b2-bf43-e611-80d5-00155da84802"  
      },  
      {  
         "@odata.etag":"W/\"619849\"",  
         "fullname":"Robert Lyon (sample)",  
         "jobtitle":"Senior Technician",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$78,000.00",  
         "annualincome":78000.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"30c364b2-bf43-e611-80d5-00155da84802"  
      },  
      {  
         "@odata.etag":"W/\"619851\"",  
         "fullname":"Paul Cannon (sample)",  
         "jobtitle":"Ski Instructor",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$68,500.00",  
         "annualincome":68500.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"34c364b2-bf43-e611-80d5-00155da84802"  
      },  
      {  
         "@odata.etag":"W/\"619853\"",  
         "fullname":"Rene Valdes (sample)",  
         "jobtitle":"Data Analyst III",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$86,000.00",  
         "annualincome":86000.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"38c364b2-bf43-e611-80d5-00155da84802"  
      },  
      {  
         "@odata.etag":"W/\"619855\"",  
         "fullname":"Jim Glynn (sample)",  
         "jobtitle":"Senior International Sales Manager",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$81,400.00",  
         "annualincome":81400.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"3cc364b2-bf43-e611-80d5-00155da84802"  
      }  
   ]  
}  
```  
  
 **Console output**  
  
```  
Contacts filtered by fullname and annualincome (<$55,000):  
	1) Nancy Anderson (sample), Activities Manager, $55,500.00  
	2) Nancy Anderson (sample), Logistics Specialist, $63,500.00  
	3) Robert Lyon (sample), Senior Technician, $78,000.00  
	4) Paul Cannon (sample), Ski Instructor, $68,500.00  
	5) Rene Valdes (sample), Data Analyst III, $86,000.00  
	6) Jim Glynn (sample), Senior International Sales Manager, $81,400.00  
```  
  
<a name="bkmk_prededence"></a>
   
## Setting precedence
 
You will use parentheses to establish the order in which your conditions are evaluated.  
  
 In this example, we are requesting a list of all contacts with `fullname` containing `(sample)`, `jobtitle` containing either `senior` or `specialist`, and `annualincome` greater than `55000`. To get the results we want, parentheses are used to group the `jobtitle` filters together. Since all operators have the same precedence, omitting the parentheses will give the `or` operator the same precedence as the `and` operators.  Filters are applied from left to right. The order in which these statements appear in the filter can affect the results. This is what the query in this example looks like: `$filter=contains(fullname,'(sample)') and (contains(jobtitle,'senior') or contains(jobtitle,'specialist')) and annualincome gt 55000`.  
  
 **HTTP Request**  
  
```  
GET https://[Organization URI]/api/data/v9.0/contacts?$select=fullname,jobtitle,annualincome&$filter=contains(fullname,'(sample)')%20and%20(contains(jobtitle,'senior')%20or%20contains(jobtitle,'specialist'))%20and%20annualincome%20gt%2055000 HTTP/1.1  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
Content-Type: application/json; charset=utf-8  
Prefer: odata.maxpagesize=10, odata.include-annotations=OData.Community.Display.V1.FormattedValue  
```  
  
 **HTTP Response**  
  
```  
HTTP/1.1 200 OK  
Content-Type: application/json; odata.metadata=minimal  
OData-Version: 4.0  
Preference-Applied: odata.include-annotations="OData.Community.Display.V1.FormattedValue"  
Preference-Applied: odata.maxpagesize=10  
Content-Length: 1393  
  
{  
   "@odata.context":"https://[Organization URI]/api/data/v9.0/$metadata#contacts(fullname,jobtitle,annualincome)",  
   "value":[  
      {  
         "@odata.etag":"W/\"619845\"",  
         "fullname":"Nancy Anderson (sample)",  
         "jobtitle":"Logistics Specialist",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$63,500.00",  
         "annualincome":63500.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"28c364b2-bf43-e611-80d5-00155da84802"  
      },  
      {  
         "@odata.etag":"W/\"619849\"",  
         "fullname":"Robert Lyon (sample)",  
         "jobtitle":"Senior Technician",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$78,000.00",  
         "annualincome":78000.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"30c364b2-bf43-e611-80d5-00155da84802"  
      },  
      {  
         "@odata.etag":"W/\"619855\"",  
         "fullname":"Jim Glynn (sample)",  
         "jobtitle":"Senior International Sales Manager",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$81,400.00",  
         "annualincome":81400.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"3cc364b2-bf43-e611-80d5-00155da84802"  
      }  
   ]  
}  
```  
  
 **Console output**  
  
```  
Contacts filtered by fullname, annualincome and jobtitle (Senior or Specialist):  
	1) Nancy Anderson (sample), Logistics Specialist, $63,500.00  
	2) Robert Lyon (sample), Senior Technician, $78,000.00  
	3) Jim Glynn (sample), Senior International Sales Manager, $81,400.00  
```  
  
<a name="bkmk_orderresults"></a>

## Ordering results

You can specify either an ascending or descending order on the results by using the `$orderby` filter option . In this example, we will query for all contacts with `fullname` containing `(sample)` and request the data in ascending order based on the `jobtitle` property value and then in  descending based on the `annualincome` property value using this syntax: `$orderby=jobtitle asc, annualincome desc`. More information:[Order results](query-data-web-api.md#bkmk_order).  
  
 **HTTP Request**  
  
```  
GET https://[Organization URI]/api/data/v9.0/contacts?$select=fullname,jobtitle,annualincome&$filter=contains(fullname,'(sample)')%20&$orderby=jobtitle%20asc,%20annualincome%20desc HTTP/1.1  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
Content-Type: application/json; charset=utf-8  
Prefer: odata.maxpagesize=10, odata.include-annotations=OData.Community.Display.V1.FormattedValue  
```  
  
 **HTTP Response**  
  
```  
HTTP/1.1 200 OK  
Content-Type: application/json; odata.metadata=minimal  
OData-Version: 4.0  
Preference-Applied: odata.include-annotations="OData.Community.Display.V1.FormattedValue"  
Preference-Applied: odata.maxpagesize=10  
Content-Length: 4284  
  
{  
   "@odata.context":"https://[Organization URI]/api/data/v9.0/$metadata#contacts(fullname,jobtitle,annualincome)",  
   "value":[  
      {  
         "@odata.etag":"W/\"619847\"",  
         "fullname":"Scott Konersmann (sample)",  
         "jobtitle":"Accounts Manager",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$38,000.00",  
         "annualincome":38000.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"2cc364b2-bf43-e611-80d5-00155da84802"  
      },  
      {  
         "@odata.etag":"W/\"619843\"",  
         "fullname":"Maria Cambell (sample)",  
         "jobtitle":"Accounts Manager",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$31,000.00",  
         "annualincome":31000.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"24c364b2-bf43-e611-80d5-00155da84802"  
      },  
      {  
         "@odata.etag":"W/\"619841\"",  
         "fullname":"Nancy Anderson (sample)",  
         "jobtitle":"Activities Manager",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$55,500.00",  
         "annualincome":55500.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"20c364b2-bf43-e611-80d5-00155da84802"  
      },  
      {  
         "@odata.etag":"W/\"619718\"",  
         "fullname":"Yvonne McKay (sample)",  
         "jobtitle":"Coffee Master",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$45,000.00",  
         "annualincome":45000.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"15c364b2-bf43-e611-80d5-00155da84802"  
      },  
      {  
         "@odata.etag":"W/\"619853\"",  
         "fullname":"Rene Valdes (sample)",  
         "jobtitle":"Data Analyst III",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$86,000.00",  
         "annualincome":86000.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"38c364b2-bf43-e611-80d5-00155da84802"  
      },  
      {  
         "@odata.etag":"W/\"619845\"",  
         "fullname":"Nancy Anderson (sample)",  
         "jobtitle":"Logistics Specialist",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$63,500.00",  
         "annualincome":63500.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"28c364b2-bf43-e611-80d5-00155da84802"  
      },  
      {  
         "@odata.etag":"W/\"619855\"",  
         "fullname":"Jim Glynn (sample)",  
         "jobtitle":"Senior International Sales Manager",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$81,400.00",  
         "annualincome":81400.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"3cc364b2-bf43-e611-80d5-00155da84802"  
      },  
      {  
         "@odata.etag":"W/\"619839\"",  
         "fullname":"Susanna Stubberod (sample)",  
         "jobtitle":"Senior Purchaser",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$52,000.00",  
         "annualincome":52000.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"1cc364b2-bf43-e611-80d5-00155da84802"  
      },  
      {  
         "@odata.etag":"W/\"619849\"",  
         "fullname":"Robert Lyon (sample)",  
         "jobtitle":"Senior Technician",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$78,000.00",  
         "annualincome":78000.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"30c364b2-bf43-e611-80d5-00155da84802"  
      },  
      {  
         "@odata.etag":"W/\"619851\"",  
         "fullname":"Paul Cannon (sample)",  
         "jobtitle":"Ski Instructor",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$68,500.00",  
         "annualincome":68500.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"34c364b2-bf43-e611-80d5-00155da84802"  
      }  
   ]  
}  
```  
  
 **Console output**  
  
```  
Contacts ordered by jobtitle (ascending) and annualincome (descending):  
	1) Scott Konersmann (sample), Accounts Manager, $38,000.00  
	2) Maria Cambell (sample), Accounts Manager, $31,000.00  
	3) Nancy Anderson (sample), Activities Manager, $55,500.00  
	4) Yvonne McKay (sample), Coffee Master, $45,000.00  
	5) Rene Valdes (sample), Data Analyst III, $86,000.00  
	6) Nancy Anderson (sample), Logistics Specialist, $63,500.00  
	7) Jim Glynn (sample), Senior International Sales Manager, $81,400.00  
	8) Susanna Stubberod (sample), Senior Purchaser, $52,000.00  
	9) Robert Lyon (sample), Senior Technician, $78,000.00  
	10) Paul Cannon (sample), Ski Instructor, $68,500.00  
```  
  
<a name="bkmk_parameteralias"></a>

## Parameter alias

Use parameter aliases to more easily reuse  parameters in your filters. Parameterized aliases can be used in `$filter` and `$orderby` options. If the alias isn’t assigned a value it is assumed to be null. You can also use parameter aliases when calling functions. More information:[Use Web API functions](use-web-api-functions.md), [Use parameter aliases with system query options](query-data-web-api.md#bkmk_useParameterAliases). Taking the order results operation for example, we can write that query again using parameters and we would get the same output results.  
  
 **HTTP Request**  
  
```  
GET https://[Organization URI]/api/data/v9.0/contacts?$select=fullname,jobtitle,annualincome&$filter=contains(@p1,'(sample)')%20&$orderby=@p2%20asc,%20@p3%20desc&@p1=fullname&@p2=jobtitle&@p3=annualincome HTTP/1.1  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
Content-Type: application/json; charset=utf-8  
Prefer: odata.maxpagesize=10, odata.include-annotations=OData.Community.Display.V1.FormattedValue  
```  
  
 **HTTP Response**  
  
```  
HTTP/1.1 200 OK  
Content-Type: application/json; odata.metadata=minimal  
OData-Version: 4.0  
Preference-Applied: odata.include-annotations="OData.Community.Display.V1.FormattedValue"  
Preference-Applied: odata.maxpagesize=10  
Content-Length: 4284  
  
{  
   "@odata.context":"https://[Organization URI]/api/data/v9.0/$metadata#contacts(fullname,jobtitle,annualincome)",  
   "value":[  
      {  
         "@odata.etag":"W/\"619847\"",  
         "fullname":"Scott Konersmann (sample)",  
         "jobtitle":"Accounts Manager",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$38,000.00",  
         "annualincome":38000.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"2cc364b2-bf43-e611-80d5-00155da84802"  
      },  
      {  
         "@odata.etag":"W/\"619843\"",  
         "fullname":"Maria Cambell (sample)",  
         "jobtitle":"Accounts Manager",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$31,000.00",  
         "annualincome":31000.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"24c364b2-bf43-e611-80d5-00155da84802"  
      },  
      {  
         "@odata.etag":"W/\"619841\"",  
         "fullname":"Nancy Anderson (sample)",  
         "jobtitle":"Activities Manager",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$55,500.00",  
         "annualincome":55500.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"20c364b2-bf43-e611-80d5-00155da84802"  
      },  
      {  
         "@odata.etag":"W/\"619718\"",  
         "fullname":"Yvonne McKay (sample)",  
         "jobtitle":"Coffee Master",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$45,000.00",  
         "annualincome":45000.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"15c364b2-bf43-e611-80d5-00155da84802"  
      },  
      {  
         "@odata.etag":"W/\"619853\"",  
         "fullname":"Rene Valdes (sample)",  
         "jobtitle":"Data Analyst III",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$86,000.00",  
         "annualincome":86000.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"38c364b2-bf43-e611-80d5-00155da84802"  
      },  
      {  
         "@odata.etag":"W/\"619845\"",  
         "fullname":"Nancy Anderson (sample)",  
         "jobtitle":"Logistics Specialist",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$63,500.00",  
         "annualincome":63500.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"28c364b2-bf43-e611-80d5-00155da84802"  
      },  
      {  
         "@odata.etag":"W/\"619855\"",  
         "fullname":"Jim Glynn (sample)",  
         "jobtitle":"Senior International Sales Manager",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$81,400.00",  
         "annualincome":81400.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"3cc364b2-bf43-e611-80d5-00155da84802"  
      },  
      {  
         "@odata.etag":"W/\"619839\"",  
         "fullname":"Susanna Stubberod (sample)",  
         "jobtitle":"Senior Purchaser",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$52,000.00",  
         "annualincome":52000.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"1cc364b2-bf43-e611-80d5-00155da84802"  
      },  
      {  
         "@odata.etag":"W/\"619849\"",  
         "fullname":"Robert Lyon (sample)",  
         "jobtitle":"Senior Technician",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$78,000.00",  
         "annualincome":78000.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"30c364b2-bf43-e611-80d5-00155da84802"  
      },  
      {  
         "@odata.etag":"W/\"619851\"",  
         "fullname":"Paul Cannon (sample)",  
         "jobtitle":"Ski Instructor",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$68,500.00",  
         "annualincome":68500.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"34c364b2-bf43-e611-80d5-00155da84802"  
      }  
   ]  
}  
```  
  
 **Console output**  
  
```  
Contacts list using parameterized aliases:  
	1) Scott Konersmann (sample), Accounts Manager, $38,000.00  
	2) Maria Cambell (sample), Accounts Manager, $31,000.00  
	3) Nancy Anderson (sample), Activities Manager, $55,500.00  
	4) Yvonne McKay (sample), Coffee Master, $45,000.00  
	5) Rene Valdes (sample), Data Analyst III, $86,000.00  
	6) Nancy Anderson (sample), Logistics Specialist, $63,500.00  
	7) Jim Glynn (sample), Senior International Sales Manager, $81,400.00  
	8) Susanna Stubberod (sample), Senior Purchaser, $52,000.00  
	9) Robert Lyon (sample), Senior Technician, $78,000.00  
	10) Paul Cannon (sample), Ski Instructor, $68,500.00  
```  
  
<a name="bkmk_limitresults"></a>

## Limit results

Returning more data than you need is bad for performance. The server will return a maximum of 5000 table rows per request. You can limit the number of results returned using the `$top` query option or by adding `odata.maxpagesize` in the request header. The `$top` query option only returns the top number of rows from the result set and ignores the rest. The `odata.maxpagesize` request header specifies the number of rows returned per page with an `@odata.nextLink` property to get results of the next page. For more information about `odata.maxpagesize`, see the section on [Pagination](#bkmk_filterPagination) and see also [Limits on number of rows returned](query-data-web-api.md#bkmk_limits).  
  
<a name="bkmk_topResults"></a>
 
### Top results

We can apply the `$top` query option to limit the basic query operation to the first five contacts with `fullname` containing `(sample)`. In this case, the request actually produces at least 10 results, but only the first 5 entries are returned in the response.  
  
 **HTTP Request**  
  
```  
GET https://[Organization URI]/api/data/v9.0/contacts?$select=fullname,jobtitle,annualincome&$filter=contains(fullname,'(sample)')&$top=5 HTTP/1.1  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
Content-Type: application/json; charset=utf-8  
Prefer: odata.maxpagesize=10, odata.include-annotations=OData.Community.Display.V1.FormattedValue  
```  
  
 **HTTP Response**  
  
```  
HTTP/1.1 200 OK  
Content-Type: application/json; odata.metadata=minimal  
OData-Version: 4.0  
Preference-Applied: odata.include-annotations="OData.Community.Display.V1.FormattedValue"  
Content-Length: 2209  
  
{  
   "@odata.context":"https://[Organization URI]/api/data/v9.0/$metadata#contacts(fullname,jobtitle,annualincome)",  
   "value":[  
      {  
         "@odata.etag":"W/\"619718\"",  
         "fullname":"Yvonne McKay (sample)",  
         "jobtitle":"Coffee Master",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$45,000.00",  
         "annualincome":45000.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"15c364b2-bf43-e611-80d5-00155da84802"  
      },  
      {  
         "@odata.etag":"W/\"619839\"",  
         "fullname":"Susanna Stubberod (sample)",  
         "jobtitle":"Senior Purchaser",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$52,000.00",  
         "annualincome":52000.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"1cc364b2-bf43-e611-80d5-00155da84802"  
      },  
      {  
         "@odata.etag":"W/\"619841\"",  
         "fullname":"Nancy Anderson (sample)",  
         "jobtitle":"Activities Manager",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$55,500.00",  
         "annualincome":55500.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"20c364b2-bf43-e611-80d5-00155da84802"  
      },  
      {  
         "@odata.etag":"W/\"619843\"",  
         "fullname":"Maria Cambell (sample)",  
         "jobtitle":"Accounts Manager",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$31,000.00",  
         "annualincome":31000.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"24c364b2-bf43-e611-80d5-00155da84802"  
      },  
      {  
         "@odata.etag":"W/\"619845\"",  
         "fullname":"Nancy Anderson (sample)",  
         "jobtitle":"Logistics Specialist",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$63,500.00",  
         "annualincome":63500.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"28c364b2-bf43-e611-80d5-00155da84802"  
      }  
   ]  
}  
```  
  
 **Console output**  
  
```  
Contacts top 5 results:  
	1) Yvonne McKay (sample), Coffee Master, $45,000.00  
	2) Susanna Stubberod (sample), Senior Purchaser, $52,000.00  
	3) Nancy Anderson (sample), Activities Manager, $55,500.00  
	4) Maria Cambell (sample), Accounts Manager, $31,000.00  
	5) Nancy Anderson (sample), Logistics Specialist, $63,500.00  
  
```  
  
<a name="bkmk_resultCount"></a>

### Result count

You can get just the count of rows from a collection-valued property or a count of matched table rows in a filter. Getting a count tells us the number of possible rows in our result. However, the Dataverse server will return 5000 as the maximum count even if the result may have more. In this example, we constructed a filter with `jobtitle` containing either `Senior` or `Manager` and we also requested a `$count` of the result. The response contains the count in the `@odata.count` property as well as the results of the query. More information:[Retrieve a count of table rows](query-data-web-api.md#bkmk_retrieveCount).  
  
 **HTTP Request**  
  
```  
GET https://[Organization URI]/api/data/v9.0/contacts?$select=fullname,jobtitle,annualincome&$filter=contains(jobtitle,'senior')%20or%20contains(jobtitle,%20'manager')&$count=true HTTP/1.1  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
Content-Type: application/json; charset=utf-8  
Prefer: odata.maxpagesize=10, odata.include-annotations=OData.Community.Display.V1.FormattedValue  
```  
  
 **HTTP Response**  
  
```  
HTTP/1.1 200 OK  
Content-Type: application/json; odata.metadata=minimal  
OData-Version: 4.0  
Preference-Applied: odata.include-annotations="OData.Community.Display.V1.FormattedValue"  
Preference-Applied: odata.maxpagesize=10  
Content-Length: 2654  
  
{  
   "@odata.context":"https://[Organization URI]/api/data/v9.0/$metadata#contacts(fullname,jobtitle,annualincome)",  
   "@odata.count":6,  
   "value":[  
      {  
         "@odata.etag":"W/\"620258\"",  
         "fullname":"Susanna Stubberod (sample)",  
         "jobtitle":"Senior Purchaser",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$52,000.00",  
         "annualincome":52000.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"bf48fdee-c143-e611-80d5-00155da84802"  
      },  
      {  
         "@odata.etag":"W/\"620260\"",  
         "fullname":"Nancy Anderson (sample)",  
         "jobtitle":"Activities Manager",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$55,500.00",  
         "annualincome":55500.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"c348fdee-c143-e611-80d5-00155da84802"  
      },  
      {  
         "@odata.etag":"W/\"620262\"",  
         "fullname":"Maria Cambell (sample)",  
         "jobtitle":"Accounts Manager",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$31,000.00",  
         "annualincome":31000.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"c748fdee-c143-e611-80d5-00155da84802"  
      },  
      {  
         "@odata.etag":"W/\"620266\"",  
         "fullname":"Scott Konersmann (sample)",  
         "jobtitle":"Accounts Manager",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$38,000.00",  
         "annualincome":38000.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"cf48fdee-c143-e611-80d5-00155da84802"  
      },  
      {  
         "@odata.etag":"W/\"620268\"",  
         "fullname":"Robert Lyon (sample)",  
         "jobtitle":"Senior Technician",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$78,000.00",  
         "annualincome":78000.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"d348fdee-c143-e611-80d5-00155da84802"  
      },  
      {  
         "@odata.etag":"W/\"620274\"",  
         "fullname":"Jim Glynn (sample)",  
         "jobtitle":"Senior International Sales Manager",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$81,400.00",  
         "annualincome":81400.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"df48fdee-c143-e611-80d5-00155da84802"  
      }  
   ]  
}  
```  
  
 **Console output**  
  
```  
6 contacts have either 'Manager' or 'Senior' designation in their jobtitle.  
Manager or Senior:  
	1) Susanna Stubberod (sample), Senior Purchaser, $52,000.00  
	2) Nancy Anderson (sample), Activities Manager, $55,500.00  
	3) Maria Cambell (sample), Accounts Manager, $31,000.00  
	4) Scott Konersmann (sample), Accounts Manager, $38,000.00  
	5) Robert Lyon (sample), Senior Technician, $78,000.00  
	6) Jim Glynn (sample), Senior International Sales Manager, $81,400.00  
  
```  
  
<a name="bkmk_filterPagination"></a>

### Pagination

To retrieve a sequential subset of results for a query that returns a large number of rows, use the `odata.maxpagesize` instead of `$top`. More information:[Specify the number of rows to return in a page](query-data-web-api.md#bkmk_specifyNumber).  
  
In this example, we ask for a `$count` and we set the `odata.maxpagesize` to `4`. This filter matches 10 contacts, but we are only retrieving 4 at a time. We also use the count and the max page size to figured out how many total pages there are. The result of the first page is returned in this request.  
  
 **HTTP Request**  
  
```  
GET https://[Organization URI]/api/data/v9.0/contacts?$select=fullname,jobtitle,annualincome&$filter=contains(fullname,'(sample)')&$count=true HTTP/1.1  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
Content-Type: application/json; charset=utf-8  
Prefer: odata.maxpagesize=4, odata.include-annotations=OData.Community.Display.V1.FormattedValue  
```  
  
 **HTTP Response**  
  
```  
HTTP/1.1 200 OK  
Content-Type: application/json; odata.metadata=minimal  
OData-Version: 4.0  
Preference-Applied: odata.include-annotations="OData.Community.Display.V1.FormattedValue"  
Preference-Applied: odata.maxpagesize=4  
Content-Length: 2294  
  
{  
   "@odata.context":"https://[Organization URI]/api/data/v9.0/$metadata#contacts(fullname,jobtitle,annualincome)",  
   "@odata.count":10,  
   "value":[  
      {  
         "@odata.etag":"W/\"620138\"",  
         "fullname":"Yvonne McKay (sample)",  
         "jobtitle":"Coffee Master",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$45,000.00",  
         "annualincome":45000.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"b848fdee-c143-e611-80d5-00155da84802"  
      },  
      {  
         "@odata.etag":"W/\"620258\"",  
         "fullname":"Susanna Stubberod (sample)",  
         "jobtitle":"Senior Purchaser",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$52,000.00",  
         "annualincome":52000.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"bf48fdee-c143-e611-80d5-00155da84802"  
      },  
      {  
         "@odata.etag":"W/\"620260\"",  
         "fullname":"Nancy Anderson (sample)",  
         "jobtitle":"Activities Manager",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$55,500.00",  
         "annualincome":55500.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"c348fdee-c143-e611-80d5-00155da84802"  
      },  
      {  
         "@odata.etag":"W/\"620262\"",  
         "fullname":"Maria Cambell (sample)",  
         "jobtitle":"Accounts Manager",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$31,000.00",  
         "annualincome":31000.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"c748fdee-c143-e611-80d5-00155da84802"  
      }  
   ],  
   "@odata.nextLink":"https://[Organization URI]/api/data/v9.0/contacts?$select=fullname,jobtitle,annualincome&$filter=contains(fullname,'(sample)')&$count=true&$skiptoken=%3Ccookie%20pagenumber=%222%22%20pagingcookie=%22%253ccookie%2520page%253d%25221%2522%253e%253ccontactid%2520last%253d%2522%257bC748FDEE-C143-E611-80D5-00155DA84802%257d%2522%2520first%253d%2522%257bB848FDEE-C143-E611-80D5-00155DA84802%257d%2522%2520%252f%253e%253c%252fcookie%253e%22%20istracking=%22False%22%20/%3E"  
}  
```  
  
 **Console output**  
  
```  
Contacts total: 10 	Contacts per page: 4.  
Page 1 of 3:  
	1) Yvonne McKay (sample), Coffee Master, $45,000.00  
	2) Susanna Stubberod (sample), Senior Purchaser, $52,000.00  
	3) Nancy Anderson (sample), Activities Manager, $55,500.00  
	4) Maria Cambell (sample), Accounts Manager, $31,000.00  
  
```  
  
 To retrieve page 2, use a `GET` request with the value of the  `@odata.nextLink` property.  
  
 **HTTP Request**  
  
```  
GET https://[Organization URI]/api/data/v9.0/contacts?$select=fullname,jobtitle,annualincome&$filter=contains(fullname,'(sample)')&$count=true&$skiptoken=%3Ccookie%20pagenumber=%222%22%20pagingcookie=%22%253ccookie%2520page%253d%25221%2522%253e%253ccontactid%2520last%253d%2522%257bC748FDEE-C143-E611-80D5-00155DA84802%257d%2522%2520first%253d%2522%257bB848FDEE-C143-E611-80D5-00155DA84802%257d%2522%2520%252f%253e%253c%252fcookie%253e%22%20istracking=%22False%22%20/%3E HTTP/1.1  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
Content-Type: application/json; charset=utf-8  
Prefer: odata.maxpagesize=4, odata.include-annotations=OData.Community.Display.V1.FormattedValue  
```  
  
 **HTTP Response**  
  
```  
HTTP/1.1 200 OK  
Content-Type: application/json; odata.metadata=minimal  
OData-Version: 4.0  
Preference-Applied: odata.include-annotations="OData.Community.Display.V1.FormattedValue"  
Preference-Applied: odata.maxpagesize=4  
Content-Length: 2294  
  
{  
   "@odata.context":"https://[Organization URI]/api/data/v9.0/$metadata#contacts(fullname,jobtitle,annualincome)",  
   "@odata.count":10,  
   "value":[  
      {  
         "@odata.etag":"W/\"620264\"",  
         "fullname":"Nancy Anderson (sample)",  
         "jobtitle":"Logistics Specialist",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$63,500.00",  
         "annualincome":63500.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"cb48fdee-c143-e611-80d5-00155da84802"  
      },  
      {  
         "@odata.etag":"W/\"620266\"",  
         "fullname":"Scott Konersmann (sample)",  
         "jobtitle":"Accounts Manager",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$38,000.00",  
         "annualincome":38000.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"cf48fdee-c143-e611-80d5-00155da84802"  
      },  
      {  
         "@odata.etag":"W/\"620268\"",  
         "fullname":"Robert Lyon (sample)",  
         "jobtitle":"Senior Technician",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$78,000.00",  
         "annualincome":78000.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"d348fdee-c143-e611-80d5-00155da84802"  
      },  
      {  
         "@odata.etag":"W/\"620270\"",  
         "fullname":"Paul Cannon (sample)",  
         "jobtitle":"Ski Instructor",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$68,500.00",  
         "annualincome":68500.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"d748fdee-c143-e611-80d5-00155da84802"  
      }  
   ],  
   "@odata.nextLink":"https://[Organization URI]/api/data/v9.0/contacts?$select=fullname,jobtitle,annualincome&$filter=contains(fullname,'(sample)')&$count=true&$skiptoken=%3Ccookie%20pagenumber=%223%22%20pagingcookie=%22%253ccookie%2520page%253d%25222%2522%253e%253ccontactid%2520last%253d%2522%257bD748FDEE-C143-E611-80D5-00155DA84802%257d%2522%2520first%253d%2522%257bCB48FDEE-C143-E611-80D5-00155DA84802%257d%2522%2520%252f%253e%253c%252fcookie%253e%22%20istracking=%22False%22%20/%3E"  
}  
```  
  
 **Console output**  
  
```  
Page 2 of 3:  
	1) Nancy Anderson (sample), Logistics Specialist, $63,500.00  
	2) Scott Konersmann (sample), Accounts Manager, $38,000.00  
	3) Robert Lyon (sample), Senior Technician, $78,000.00  
	4) Paul Cannon (sample), Ski Instructor, $68,500.00  
```  
  
<a name="bkmk_expandresults"></a>

## Expanding results

To retrieve information on associated table rows, use the `$expand` query option on navigation properties. More information:[Retrieve related rows by expanding navigation properties](query-data-web-api.md#bkmk_expandRelated).  
  
### Expand on single-valued navigation property

A Single-valued navigation property represents a many-to-one relationships. In our sample data, the account has a relationship with a contact via the `primarycontactid` column (attribute). In this relationship, the account can only have one primary contact.  Using the <xref href="Microsoft.Dynamics.CRM.account?text=account EntityType" />, we can create a query to get information about the account and expanded information about its primary contact.  
  
 **HTTP Request**  
  
```  
GET https://[Organization URI]/api/data/v9.0/accounts(b2546951-c543-e611-80d5-00155da84802)?$select=name&$expand=primarycontactid($select=fullname,jobtitle,annualincome) HTTP/1.1  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
Content-Type: application/json; charset=utf-8  
Prefer: odata.maxpagesize=10, odata.include-annotations=OData.Community.Display.V1.FormattedValue  
```  
  
 **HTTP Response**  
  
```  
HTTP/1.1 200 OK  
Content-Type: application/json; odata.metadata=minimal  
OData-Version: 4.0  
Preference-Applied: odata.include-annotations="OData.Community.Display.V1.FormattedValue"  
Preference-Applied: odata.maxpagesize=10  
Content-Length: 700  
  
{  
   "@odata.context":"https://[Organization URI]/api/data/v9.0/$metadata#accounts(name,primarycontactid,primarycontactid(fullname,jobtitle,annualincome))/$entity",  
   "@odata.etag":"W/\"620641\"",  
   "name":"Contoso, Ltd. (sample)",  
   "accountid":"b2546951-c543-e611-80d5-00155da84802",  
   "primarycontactid":{  
      "@odata.etag":"W/\"620534\"",  
      "fullname":"Yvonne McKay (sample)",  
      "jobtitle":"Coffee Master",  
      "annualincome@OData.Community.Display.V1.FormattedValue":"$45,000.00",  
      "annualincome":45000.0000,  
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
      "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
      "contactid":"b3546951-c543-e611-80d5-00155da84802"  
   }  
}  
```  
  
 **Console output**  
  
```  
Account 'Contoso, Ltd. (sample)' has the following primary contact person:  
	Fullname: 'Yvonne McKay (sample)'   
	Jobtitle: 'Coffee Master'   
	Annualincome: '45000'  
```  
  
### Expand on partner property

Each navigation property has a corresponding “partner” property. Once an association is made, we can retrieve information through this association. Which column we use depends on the base table that the query is against. For example, in the previous operation, we created a query against the <xref href="Microsoft.Dynamics.CRM.account?text=account EntityType" /> and we wanted to get additional information about its primary contact. We did that via the `primarycontactid` column (attribute). If we look up the <xref href="Microsoft.Dynamics.CRM.account?text=account EntityType" />, under the [Single-valued navigation properties](/dynamics365/customer-engagement/web-api/account#Single-valued_navigation_properties) section, we can see that the partner property that corresponds to `primarycontactid` is  `account_primary_contact` collection-valued navigation property found on the <xref href="Microsoft.Dynamics.CRM.contact?text=contact EntityType" />.  
  
Writing a query against a contact, you can expand on the `account_primary_contact` column to get information about accounts where this contact is the primary contact. In the sample data, `Yvonne McKay (sample)` is the primary contact person for only one account. However, she can potentially be assigned to other accounts as primary contact. Because the `account_primary_contact` property has a many-to-one relationship the result is returned as an array of account rows.  
  
 **HTTP Request**  
  
```  
GET https://[Organization URI]/api/data/v9.0/contacts(b3546951-c543-e611-80d5-00155da84802)?$select=fullname,jobtitle,annualincome&$expand=account_primary_contact($select=name) HTTP/1.1  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
Content-Type: application/json; charset=utf-8  
Prefer: odata.maxpagesize=10, odata.include-annotations=OData.Community.Display.V1.FormattedValue  
```  
  
 **HTTP Response**  
  
```  
HTTP/1.1 200 OK  
Content-Type: application/json; odata.metadata=minimal  
OData-Version: 4.0  
Preference-Applied: odata.include-annotations="OData.Community.Display.V1.FormattedValue"  
Preference-Applied: odata.maxpagesize=10  
Content-Length: 737  
  
{  
   "@odata.context":"https://[Organization URI]/api/data/v9.0/$metadata#contacts(fullname,jobtitle,annualincome,account_primary_contact,account_primary_contact(name))/$entity",  
   "@odata.etag":"W/\"620534\"",  
   "fullname":"Yvonne McKay (sample)",  
   "jobtitle":"Coffee Master",  
   "annualincome@OData.Community.Display.V1.FormattedValue":"$45,000.00",  
   "annualincome":45000.0000,  
   "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
   "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
   "contactid":"b3546951-c543-e611-80d5-00155da84802",  
   "account_primary_contact":[  
      {  
         "@odata.etag":"W/\"620919\"",  
         "name":"Contoso, Ltd. (sample)",  
         "accountid":"b2546951-c543-e611-80d5-00155da84802"  
      }  
   ]  
}  
```  
  
 **Console output**  
  
```  
Contact 'Yvonne McKay (sample)' is the primary contact for the following accounts:  
	1) Contoso, Ltd. (sample)  
```  
  
### Expand on collection-valued navigation property

Collection-valued navigation properties support one-to-many or many-to-many relationships. For example, in our sample data, the account has a relationship with many contacts via the `contact_customer_accounts` column (attribute).  
  
Using the <xref href="Microsoft.Dynamics.CRM.account?text=account EntityType" />, we can create a query to get information about the account and expand information about its contacts. In this case, the `Contoso, Ltd. (sample)` is associated to nine other contacts via the `contact_customer_accounts` collection-valued navigation property.  
  
 **HTTP Request**  
  
```  
GET https://[Organization URI]/api/data/v9.0/accounts(86546951-c543-e611-80d5-00155da84802)?$select=name&$expand=contact_customer_accounts($select=fullname,jobtitle,annualincome) HTTP/1.1  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
Content-Type: application/json; charset=utf-8  
Prefer: odata.maxpagesize=10, odata.include-annotations=OData.Community.Display.V1.FormattedValue  
```  
  
 **HTTP Response**  
  
```  
HTTP/1.1 200 OK  
Content-Type: application/json; odata.metadata=minimal  
OData-Version: 4.0  
Preference-Applied: odata.include-annotations="OData.Community.Display.V1.FormattedValue"  
Preference-Applied: odata.maxpagesize=10  
Content-Length: 4073  
  
{  
   "@odata.context":"https://[Organization URI]/api/data/v9.0/$metadata#accounts(name,contact_customer_accounts,contact_customer_accounts(fullname,jobtitle,annualincome))/$entity",  
   "@odata.etag":"W/\"620921\"",  
   "name":"Contoso, Ltd. (sample)",  
   "accountid":"86546951-c543-e611-80d5-00155da84802",  
   "contact_customer_accounts":[  
      {  
         "@odata.etag":"W/\"620847\"",  
         "fullname":"Susanna Stubberod (sample)",  
         "jobtitle":"Senior Purchaser",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$52,000.00",  
         "annualincome":52000.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"8e546951-c543-e611-80d5-00155da84802"  
      },  
      {  
         "@odata.etag":"W/\"620849\"",  
         "fullname":"Nancy Anderson (sample)",  
         "jobtitle":"Activities Manager",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$55,500.00",  
         "annualincome":55500.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"92546951-c543-e611-80d5-00155da84802"  
      },  
      {  
         "@odata.etag":"W/\"620851\"",  
         "fullname":"Maria Cambell (sample)",  
         "jobtitle":"Accounts Manager",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$31,000.00",  
         "annualincome":31000.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"96546951-c543-e611-80d5-00155da84802"  
      },  
      {  
         "@odata.etag":"W/\"620853\"",  
         "fullname":"Nancy Anderson (sample)",  
         "jobtitle":"Logistics Specialist",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$63,500.00",  
         "annualincome":63500.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"9a546951-c543-e611-80d5-00155da84802"  
      },  
      {  
         "@odata.etag":"W/\"620855\"",  
         "fullname":"Scott Konersmann (sample)",  
         "jobtitle":"Accounts Manager",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$38,000.00",  
         "annualincome":38000.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"9e546951-c543-e611-80d5-00155da84802"  
      },  
      {  
         "@odata.etag":"W/\"620857\"",  
         "fullname":"Robert Lyon (sample)",  
         "jobtitle":"Senior Technician",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$78,000.00",  
         "annualincome":78000.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"a2546951-c543-e611-80d5-00155da84802"  
      },  
      {  
         "@odata.etag":"W/\"620859\"",  
         "fullname":"Paul Cannon (sample)",  
         "jobtitle":"Ski Instructor",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$68,500.00",  
         "annualincome":68500.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"a6546951-c543-e611-80d5-00155da84802"  
      },  
      {  
         "@odata.etag":"W/\"620861\"",  
         "fullname":"Rene Valdes (sample)",  
         "jobtitle":"Data Analyst III",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$86,000.00",  
         "annualincome":86000.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"aa546951-c543-e611-80d5-00155da84802"  
      },  
      {  
         "@odata.etag":"W/\"620863\"",  
         "fullname":"Jim Glynn (sample)",  
         "jobtitle":"Senior International Sales Manager",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$81,400.00",  
         "annualincome":81400.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"ae546951-c543-e611-80d5-00155da84802"  
      }  
   ]  
}  
```  
  
 **Console output**  
  
```  
Account 'Contoso, Ltd. (sample)' has the following contact customers:  
	1) Susanna Stubberod (sample), Senior Purchaser, $52,000.00  
	2) Nancy Anderson (sample), Activities Manager, $55,500.00  
	3) Maria Cambell (sample), Accounts Manager, $31,000.00  
	4) Nancy Anderson (sample), Logistics Specialist, $63,500.00  
	5) Scott Konersmann (sample), Accounts Manager, $38,000.00  
	6) Robert Lyon (sample), Senior Technician, $78,000.00  
	7) Paul Cannon (sample), Ski Instructor, $68,500.00  
	8) Rene Valdes (sample), Data Analyst III, $86,000.00  
	9) Jim Glynn (sample), Senior International Sales Manager, $81,400.00  
```  
  
### Expand on multiple navigation properties

You can expand on as many navigation properties as the query requires. However, the `$expand` option can only go one level deep.  
  
This example expands the `primarycontactid`, `contact_customer_accounts`, and `Account_Tasks` navigation properties of the <xref href="Microsoft.Dynamics.CRM.account?text=account EntityType" />.  This query returns a response containing information about the account and two collections: a contacts collection and  a tasks collection. The sample code will process these collections separately.  
  
 **HTTP Request**  
  
```  
GET https://[Organization URI]/api/data/v9.0/accounts(86546951-c543-e611-80d5-00155da84802)?$select=name&$expand=primarycontactid($select=fullname,jobtitle,annualincome),contact_customer_accounts($select=fullname,jobtitle,annualincome),Account_Tasks($select=subject,description) HTTP/1.1  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
Content-Type: application/json; charset=utf-8  
Prefer: odata.maxpagesize=10, odata.include-annotations=OData.Community.Display.V1.FormattedValue  
```  
  
 **HTTP Response**  
  
```  
HTTP/1.1 200 OK  
Content-Type: application/json; odata.metadata=minimal  
OData-Version: 4.0  
Preference-Applied: odata.include-annotations="OData.Community.Display.V1.FormattedValue"  
Preference-Applied: odata.maxpagesize=10  
Content-Length: 5093  
  
{  
   "@odata.context":"https://[Organization URI]/api/data/v9.0/$metadata#accounts(name,primarycontactid,contact_customer_accounts,Account_Tasks,primarycontactid(fullname,jobtitle,annualincome),contact_customer_accounts(fullname,jobtitle,annualincome),Account_Tasks(subject,description))/$entity",  
   "@odata.etag":"W/\"620921\"",  
   "name":"Contoso, Ltd. (sample)",  
   "accountid":"86546951-c543-e611-80d5-00155da84802",  
   "primarycontactid":{  
      "@odata.etag":"W/\"620726\"",  
      "fullname":"Yvonne McKay (sample)",  
      "jobtitle":"Coffee Master",  
      "annualincome@OData.Community.Display.V1.FormattedValue":"$45,000.00",  
      "annualincome":45000.0000,  
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
      "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
      "contactid":"87546951-c543-e611-80d5-00155da84802"  
   },  
   "contact_customer_accounts":[  
      {  
         "@odata.etag":"W/\"620847\"",  
         "fullname":"Susanna Stubberod (sample)",  
         "jobtitle":"Senior Purchaser",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$52,000.00",  
         "annualincome":52000.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"8e546951-c543-e611-80d5-00155da84802"  
      },  
      {  
         "@odata.etag":"W/\"620849\"",  
         "fullname":"Nancy Anderson (sample)",  
         "jobtitle":"Activities Manager",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$55,500.00",  
         "annualincome":55500.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"92546951-c543-e611-80d5-00155da84802"  
      },  
      {  
         "@odata.etag":"W/\"620851\"",  
         "fullname":"Maria Cambell (sample)",  
         "jobtitle":"Accounts Manager",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$31,000.00",  
         "annualincome":31000.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"96546951-c543-e611-80d5-00155da84802"  
      },  
      {  
         "@odata.etag":"W/\"620853\"",  
         "fullname":"Nancy Anderson (sample)",  
         "jobtitle":"Logistics Specialist",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$63,500.00",  
         "annualincome":63500.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"9a546951-c543-e611-80d5-00155da84802"  
      },  
      {  
         "@odata.etag":"W/\"620855\"",  
         "fullname":"Scott Konersmann (sample)",  
         "jobtitle":"Accounts Manager",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$38,000.00",  
         "annualincome":38000.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"9e546951-c543-e611-80d5-00155da84802"  
      },  
      {  
         "@odata.etag":"W/\"620857\"",  
         "fullname":"Robert Lyon (sample)",  
         "jobtitle":"Senior Technician",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$78,000.00",  
         "annualincome":78000.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"a2546951-c543-e611-80d5-00155da84802"  
      },  
      {  
         "@odata.etag":"W/\"620859\"",  
         "fullname":"Paul Cannon (sample)",  
         "jobtitle":"Ski Instructor",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$68,500.00",  
         "annualincome":68500.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"a6546951-c543-e611-80d5-00155da84802"  
      },  
      {  
         "@odata.etag":"W/\"620861\"",  
         "fullname":"Rene Valdes (sample)",  
         "jobtitle":"Data Analyst III",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$86,000.00",  
         "annualincome":86000.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"aa546951-c543-e611-80d5-00155da84802"  
      },  
      {  
         "@odata.etag":"W/\"620863\"",  
         "fullname":"Jim Glynn (sample)",  
         "jobtitle":"Senior International Sales Manager",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$81,400.00",  
         "annualincome":81400.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"ae546951-c543-e611-80d5-00155da84802"  
      }  
   ],  
   "Account_Tasks":[  
      {  
         "@odata.etag":"W/\"620840\"",  
         "subject":"Task 1",  
         "description":"Task 1 description",  
         "activityid":"8b546951-c543-e611-80d5-00155da84802"  
      },  
      {  
         "@odata.etag":"W/\"620842\"",  
         "subject":"Task 2",  
         "description":"Task 2 description",  
         "activityid":"8c546951-c543-e611-80d5-00155da84802"  
      },  
      {  
         "@odata.etag":"W/\"620844\"",  
         "subject":"Task 3",  
         "description":"Task 3 description",  
         "activityid":"8d546951-c543-e611-80d5-00155da84802"  
      }  
   ]  
}  
```  
  
 **Console output**  
  
```  
-- Expanding multiple property types in one request --   
Account 'Contoso, Ltd. (sample)' has the following primary contact person:  
	Fullname: 'Yvonne McKay (sample)'   
	Jobtitle: 'Coffee Master'   
	Annualincome: '45000'  
Account 'Contoso, Ltd. (sample)' has the following related contacts:  
	1) Susanna Stubberod (sample), Senior Purchaser, $52,000.00  
	2) Nancy Anderson (sample), Activities Manager, $55,500.00  
	3) Maria Cambell (sample), Accounts Manager, $31,000.00  
	4) Nancy Anderson (sample), Logistics Specialist, $63,500.00  
	5) Scott Konersmann (sample), Accounts Manager, $38,000.00  
	6) Robert Lyon (sample), Senior Technician, $78,000.00  
	7) Paul Cannon (sample), Ski Instructor, $68,500.00  
	8) Rene Valdes (sample), Data Analyst III, $86,000.00  
	9) Jim Glynn (sample), Senior International Sales Manager, $81,400.00  
Account 'Contoso, Ltd. (sample)' has the following tasks:  
	1) Task 1, Task 1 description  
	2) Task 2, Task 2 description  
	3) Task 3, Task 3 description  
```  
  
<a name="bkmk_fetchxml"></a>

## FetchXML queries

<!-- TODO:
Besides query filter operations, the Web API also supports FetchXML queries. FetchXml provides an alternative way to define queries and additional options to perform aggregations. More information:[Build queries with FetchXML](../org-service/build-queries-fetchxml.md)   -->
  
<!-- TODO: To use fetch xml you must compose a string representing the query. Make sure the query string conforms to the [FetchXML schema](../org-service/fetchxml-schema.md). Before you include the string in the URL you must URL encode the string.   -->
  
 All the query options we would normally define such as `$select`, `$filter`, and `$orderby` are now defined in the XML. In this operation, we query for all contacts whose `fullname` matches `(sample)`, and order the results descending by `fullname`. This is the XML for this query.  
  
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
    </filter>  
  </entity>  
</fetch>  
```  
  
 **HTTP Request**  
  
 The request query string is sent to the server in encoded form. The encoded header looks like this.  
  
```  
GET https://[Organization URI]/api/data/v9.0/contacts?fetchXml=%253Cfetch%2520mapping%253D%2522logical%2522%2520output-format%253D%2522xml-platform%2522%2520version%253D%25221.0%2522%2520distinct%253D%2522false%2522%253E%2520%2520%2520%253Centity%2520name%253D%2522contact%2522%253E%2520%2520%2520%2520%2520%253Cattribute%2520name%253D%2522fullname%2522%2520%252F%253E%2520%2520%2520%2520%2520%253Cattribute%2520name%253D%2522jobtitle%2522%2520%252F%253E%2520%2520%2520%2520%2520%253Cattribute%2520name%253D%2522annualincome%2522%2520%252F%253E%2520%2520%2520%2520%2520%253Corder%2520descending%253D%2522true%2522%2520attribute%253D%2522fullname%2522%2520%252F%253E%2520%2520%2520%2520%2520%253Cfilter%2520type%253D%2522and%2522%253E%2520%2520%2520%2520%2520%2520%2520%253Ccondition%2520value%253D%2522%2525(sample)%2525%2522%2520attribute%253D%2522fullname%2522%2520operator%253D%2522like%2522%2520%252F%253E%2520%2520%2520%2520%2520%253C%252Ffilter%253E%2520%2520%2520%253C%252Fentity%253E%2520%253C%252Ffetch%253E%2520 HTTP/1.1  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
Content-Type: application/json; charset=utf-8  
Prefer: odata.maxpagesize=10, odata.include-annotations=OData.Community.Display.V1.FormattedValue  
```  
  
 **HTTP Response**  
  
```  
HTTP/1.1 200 OK  
OData-Version: 4.0  
Preference-Applied: odata.include-annotations="OData.Community.Display.V1.FormattedValue"  
Content-Length: 4345  
  
{  
   "@odata.context":"https://[Organization URI]/api/data/v9.0/$metadata#contacts(fullname,jobtitle,annualincome,_transactioncurrencyid_value,transactioncurrencyid,contactid)",  
   "value":[  
      {  
         "@odata.etag":"W/\"621502\"",  
         "fullname":"Yvonne McKay (sample)",  
         "jobtitle":"Coffee Master",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$45,000.00",  
         "annualincome":45000.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"9255b257-c843-e611-80d5-00155da84802"  
      },  
      {  
         "@odata.etag":"W/\"621627\"",  
         "fullname":"Susanna Stubberod (sample)",  
         "jobtitle":"Senior Purchaser",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$52,000.00",  
         "annualincome":52000.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"9955b257-c843-e611-80d5-00155da84802"  
      },  
      {  
         "@odata.etag":"W/\"621635\"",  
         "fullname":"Scott Konersmann (sample)",  
         "jobtitle":"Accounts Manager",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$38,000.00",  
         "annualincome":38000.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"a955b257-c843-e611-80d5-00155da84802"  
      },  
      {  
         "@odata.etag":"W/\"621637\"",  
         "fullname":"Robert Lyon (sample)",  
         "jobtitle":"Senior Technician",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$78,000.00",  
         "annualincome":78000.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"ad55b257-c843-e611-80d5-00155da84802"  
      },  
      {  
         "@odata.etag":"W/\"621641\"",  
         "fullname":"Rene Valdes (sample)",  
         "jobtitle":"Data Analyst III",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$86,000.00",  
         "annualincome":86000.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"b555b257-c843-e611-80d5-00155da84802"  
      },  
      {  
         "@odata.etag":"W/\"621639\"",  
         "fullname":"Paul Cannon (sample)",  
         "jobtitle":"Ski Instructor",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$68,500.00",  
         "annualincome":68500.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"b155b257-c843-e611-80d5-00155da84802"  
      },  
      {  
         "@odata.etag":"W/\"621629\"",  
         "fullname":"Nancy Anderson (sample)",  
         "jobtitle":"Activities Manager",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$55,500.00",  
         "annualincome":55500.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"9d55b257-c843-e611-80d5-00155da84802"  
      },  
      {  
         "@odata.etag":"W/\"621633\"",  
         "fullname":"Nancy Anderson (sample)",  
         "jobtitle":"Logistics Specialist",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$63,500.00",  
         "annualincome":63500.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"a555b257-c843-e611-80d5-00155da84802"  
      },  
      {  
         "@odata.etag":"W/\"621631\"",  
         "fullname":"Maria Cambell (sample)",  
         "jobtitle":"Accounts Manager",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$31,000.00",  
         "annualincome":31000.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"a155b257-c843-e611-80d5-00155da84802"  
      },  
      {  
         "@odata.etag":"W/\"621643\"",  
         "fullname":"Jim Glynn (sample)",  
         "jobtitle":"Senior International Sales Manager",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$81,400.00",  
         "annualincome":81400.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"b955b257-c843-e611-80d5-00155da84802"  
      }  
   ]  
}  
```  
  
 **Console output**  
  
```  
Contacts Fetched by fullname containing '(sample)':  
	1) Yvonne McKay (sample), Coffee Master, $45,000.00  
	2) Susanna Stubberod (sample), Senior Purchaser, $52,000.00  
	3) Scott Konersmann (sample), Accounts Manager, $38,000.00  
	4) Robert Lyon (sample), Senior Technician, $78,000.00  
	5) Rene Valdes (sample), Data Analyst III, $86,000.00  
	6) Paul Cannon (sample), Ski Instructor, $68,500.00  
	7) Nancy Anderson (sample), Activities Manager, $55,500.00  
	8) Nancy Anderson (sample), Logistics Specialist, $63,500.00  
	9) Maria Cambell (sample), Accounts Manager, $31,000.00  
	10) Jim Glynn (sample), Senior International Sales Manager, $81,400.00  
```  
  
### FetchXML pagination

The way FetchXML handles paging is different than how query filter handles it. In FetchXML, you can specify a `count` column that will indicate how many results to return per page. In the same request, you use the `page` column to specify the page number you want. This operation will make a request for page 3 from the previous FetchXML sample. Based on our sample data, we should have ten contacts in our result. Breaking each page down to only four contacts per page, we should have three pages. Page 3 should contain only two contacts. If we then ask for page 4, the system will return zero results.  
  
```xml  
<fetch mapping="logical"  
       output-format="xml-platform"  
       version="1.0"  
       distinct="false"  
       page="3"  
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
    </filter>  
  </entity>  
</fetch>  
```  
  
 **HTTP Request**  
  
 The request query string is sent to the server in encoded form. The encoded header looks like this.  
  
```  
GET https://[Organization URI]/api/data/v9.0/contacts?fetchXml=%253Cfetch%2520mapping%253D%2522logical%2522%2520output-format%253D%2522xml-platform%2522%2520version%253D%25221.0%2522%2520distinct%253D%2522false%2522%2520page%253D%25223%2522%2520count%253D%25224%2522%253E%2520%2520%2520%253Centity%2520name%253D%2522contact%2522%253E%2520%2520%2520%2520%2520%253Cattribute%2520name%253D%2522fullname%2522%2520%252F%253E%2520%2520%2520%2520%2520%253Cattribute%2520name%253D%2522jobtitle%2522%2520%252F%253E%2520%2520%2520%2520%2520%253Cattribute%2520name%253D%2522annualincome%2522%2520%252F%253E%2520%2520%2520%2520%2520%253Corder%2520descending%253D%2522true%2522%2520attribute%253D%2522fullname%2522%2520%252F%253E%2520%2520%2520%2520%2520%253Cfilter%2520type%253D%2522and%2522%253E%2520%2520%2520%2520%2520%2520%2520%253Ccondition%2520value%253D%2522%2525(sample)%2525%2522%2520attribute%253D%2522fullname%2522%2520operator%253D%2522like%2522%2520%252F%253E%2520%2520%2520%2520%2520%253C%252Ffilter%253E%2520%2520%2520%253C%252Fentity%253E%2520%253C%252Ffetch%253E%2520 HTTP/1.1  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
Content-Type: application/json; charset=utf-8  
Prefer: odata.maxpagesize=10, odata.include-annotations=OData.Community.Display.V1.FormattedValue  
  
```  
  
 **HTTP Response**  
  
```  
HTTP/1.1 200 OK  
Content-Type: application/json; odata.metadata=minimal  
OData-Version: 4.0  
Preference-Applied: odata.include-annotations="OData.Community.Display.V1.FormattedValue"  
Content-Length: 1037  
  
{   
   "@odata.context":"https://[Organization URI]/api/data/v9.0/$metadata#contacts(fullname,jobtitle,annualincome,_transactioncurrencyid_value,transactioncurrencyid,contactid)",  
   "value":[   
      {   
         "@odata.etag":"W/\"621631\"",  
         "fullname":"Maria Cambell (sample)",  
         "jobtitle":"Accounts Manager",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$31,000.00",  
         "annualincome":31000.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"a155b257-c843-e611-80d5-00155da84802"  
      },  
      {   
         "@odata.etag":"W/\"621643\"",  
         "fullname":"Jim Glynn (sample)",  
         "jobtitle":"Senior International Sales Manager",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$81,400.00",  
         "annualincome":81400.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802",  
         "contactid":"b955b257-c843-e611-80d5-00155da84802"  
      }  
   ]  
}  
```  
  
 **Console output**  
  
```  
Contacts Fetched by fullname containing '(sample)' - Page 3:  
	1) Maria Cambell (sample), Accounts Manager, $31,000.00  
	2) Jim Glynn (sample), Senior International Sales Manager, $81,400.00  
```  
  
<a name="bkmk_predefinedqueries"></a>
 
## Predefined queries

You can use the Web API to execute predefined queries. More information:[Retrieve and execute predefined queries](retrieve-and-execute-predefined-queries.md).  
  
### Saved query

In this operation, we will make a request for the `savedqueryid` GUID of the saved query named **Active Accounts**. Then using the GUID and the `savedQuery` parameter, we will query for a list of active accounts.  
  
 Getting the saved query's GUID.  
  
 **HTTP Request**  
  
```  
GET https://[Organization URI]/api/data/v9.0/savedqueries?$select=name,savedqueryid&$filter=name%20eq%20'Active%20Accounts' HTTP/1.1  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
Content-Type: application/json; charset=utf-8  
Prefer: odata.maxpagesize=10, odata.include-annotations=OData.Community.Display.V1.FormattedValue  
Referer: https://localhost:1469/WebAPIQuery.html  
```  
  
 **HTTP Response**  
  
```  
HTTP/1.1 200 OK  
Content-Type: application/json; odata.metadata=minimal  
OData-Version: 4.0  
Content-Length: 251  
  
{   
   "@odata.context":"https://[Organization URI]/api/data/v9.0/$metadata#savedqueries(name,savedqueryid)",  
   "value":[   
      {   
         "@odata.etag":"W/\"443067\"",  
         "name":"Active Accounts",  
         "savedqueryid":"00000000-0000-0000-00aa-000010001002"  
      }  
   ]  
}  
```  
  
 Getting the saved query's content using the `savedQuery` parameter  
  
 **HTTP Request**  
  
```  
GET https://[Organization URI]/api/data/v9.0/accounts?savedQuery=00000000-0000-0000-00aa-000010001002 HTTP/1.1  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
Content-Type: application/json; charset=utf-8  
Prefer: odata.maxpagesize=10, odata.include-annotations=OData.Community.Display.V1.FormattedValue  
```  
  
 **HTTP Response**  
  
```  
HTTP/1.1 200 OK  
Content-Type: application/json; odata.metadata=minimal  
REQ_ID: 2bc532c4-d445-44cd-adae-1909a616d6bc  
OData-Version: 4.0  
Preference-Applied: odata.include-annotations="OData.Community.Display.V1.FormattedValue"  
Content-Length: 446  
  
{   
   "@odata.context":"https://[Organization URI]/api/data/v9.0/$metadata#accounts(name,_primarycontactid_value,primarycontactid,accountid)",  
   "value":[   
      {   
         "@odata.etag":"W/\"621613\"",  
         "name":"Contoso, Ltd. (sample)",  
         "_primarycontactid_value@OData.Community.Display.V1.FormattedValue":"Yvonne McKay (sample)",  
         "_primarycontactid_value":"9255b257-c843-e611-80d5-00155da84802",  
         "accountid":"9155b257-c843-e611-80d5-00155da84802"  
      }  
   ]  
}  
```  
  
 **Console output**  
  
```  
-- Saved Query --   
Saved Query (Active Accounts):  
	1) Contoso, Ltd. (sample)  
```  
  
### User query

This sample creates a user query, executes it, then deletes it from the system. This user query is asking for any contacts whose `fullname` contains `(sample)`, `jobtitle` contains `manager`, and `annualincome` greater than `55000`. Our sample data has two contacts matching this query.  
  
 Getting the user query's GUID.  
  
 **HTTP Request**  
  
```  
GET https://[Organization URI]/api/data/v9.0/userqueries?$select=name,userqueryid,&$filter=name%20eq%20'My%20User%20Query' HTTP/1.1  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
Content-Type: application/json; charset=utf-8  
Referer: https://localhost:1469/WebAPIQuery.html  
  
```  
  
 **HTTP Response**  
  
```  
Pragma: no-cache  
Content-Type: application/json; odata.metadata=minimal  
OData-Version: 4.0  
Content-Length: 246  
  
{   
   "@odata.context":"https://[Organization URI]/api/data/v9.0/$metadata#userqueries(name,userqueryid)",  
   "value":[   
      {   
         "@odata.etag":"W/\"621698\"",  
         "name":"My User Query",  
         "userqueryid":"7ec390ab-c943-e611-80d5-00155da84802"  
      }  
   ]  
}  
```  
  
 Getting the user query's content passing the GUID value with the `userQuery` parameter.  
  
 **HTTP Request**  
  
```  
GET https://[Organization URI]/api/data/v9.0/contacts?userQuery=7ec390ab-c943-e611-80d5-00155da84802 HTTP/1.1  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
Content-Type: application/json; charset=utf-8  
Prefer: odata.maxpagesize=10, odata.include-annotations=OData.Community.Display.V1.FormattedValue  
  
```  
  
 **HTTP Response**  
  
```  
HTTP/1.1 200 OK  
Content-Type: application/json; odata.metadata=minimal  
OData-Version: 4.0  
Content-Length: 1040  
  
{   
   "@odata.context":"https://[Organization URI]/api/data/v9.0/$metadata#contacts(fullname,contactid,jobtitle,annualincome,_transactioncurrencyid_value,transactioncurrencyid)",  
   "value":[   
      {   
         "@odata.etag":"W/\"621643\"",  
         "fullname":"Jim Glynn (sample)",  
         "contactid":"b955b257-c843-e611-80d5-00155da84802",  
         "jobtitle":"Senior International Sales Manager",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$81,400.00",  
         "annualincome":81400.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802"  
      },  
      {   
         "@odata.etag":"W/\"621629\"",  
         "fullname":"Nancy Anderson (sample)",  
         "contactid":"9d55b257-c843-e611-80d5-00155da84802",  
         "jobtitle":"Activities Manager",  
         "annualincome@OData.Community.Display.V1.FormattedValue":"$55,500.00",  
         "annualincome":55500.0000,  
         "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue":"US Dollar",  
         "_transactioncurrencyid_value":"518c78c9-d3f6-e511-80d0-00155da84802"  
      }  
   ]  
}  
```  
  
 **Console output**  
  
```  
-- User Query --   
Saved User Query:  
	1) Jim Glynn (sample), Senior International Sales Manager, $81,400.00  
	2) Nancy Anderson (sample), Activities Manager, $55,500.00  
```  
  
### See also

[Use the Dataverse Web API](overview.md)<br />
[Query Data using the Web API](query-data-web-api.md)<br />
[Retrieve and execute predefined queries](retrieve-and-execute-predefined-queries.md)<br />
[Web API Query Data Sample (C#)](samples/cdswebapiservice-query-data.md)<br />
[Web API Query Data Sample (Client-side JavaScript)](samples/query-data-client-side-javascript.md)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]