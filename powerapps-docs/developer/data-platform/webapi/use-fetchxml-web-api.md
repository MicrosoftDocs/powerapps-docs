---
title: "Use FetchXml with Web API (Microsoft Dataverse)| Microsoft Learn"
description: "FetchXml provides another way to define a query you can use with Web API to retrieve table data."
ms.date: 09/27/2022
author: divka78
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
# Use FetchXml with Web API

FetchXML is a proprietary query language that provides capabilities to perform aggregation. More information: [Use FetchXML to query data](../use-fetchxml-construct-query.md)

> [!NOTE]
> Unlike queries using the OData syntax, data returned from FetchXML will not return properties with `null` values. When the value is `null`, the property will not be included in the results.

You can compose a FetchXML query for a specific table. Then, URL encode the XML and pass it to the entity set using the `fetchXml` query string parameter.

For example, you can have the following FetchXML that has `account` as the entity.  

```xml  
<fetch mapping='logical'>
   <entity name='account'>
      <attribute name='accountid'/>
      <attribute name='name'/>
      <attribute name='accountnumber'/>      
</entity>
</fetch>
```

The URL encoded value of this FetchXML is as shown here.

```text
%3Cfetch%20mapping%3D%27logical%27%3E%3Centity%20name%3D%27account%27%3E%3Cattribute%20name%3D%27accountid%27%2F%3E%3Cattribute%20name%3D%27name%27%2F%3E%3Cattribute%20name%3D%27accountnumber%27%2F%3E%3C%2Fentity%3E%3C%2Ffetch%3E
```

Most programming languages include a function to URL encode a string. For example, in JavaScript you use the [encodeURI](https://www.ecma-international.org/ecma-262/5.1/) function. You should URL encode any request that you send to any RESTful web service. If you paste a URL into the address bar of your browser it should URL encode the address automatically. The following example shows a GET request using the FetchXML shown previously using the entity set path for accounts. Note that it passes the encoded XML using this parameter: `?fetchXml=`

**Request**

```http
GET [Organization URI]/api/data/v9.0/accounts?fetchXml=%3Cfetch%20mapping%3D%27logical%27%3E%3Centity%20name%3D%27account%27%3E%3Cattribute%20name%3D%27accountid%27%2F%3E%3Cattribute%20name%3D%27name%27%2F%3E%3Cattribute%20name%3D%27accountnumber%27%2F%3E%3C%2Fentity%3E%3C%2Ffetch%3E HTTP/1.1
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
  "@odata.context":"[Organization URI]/api/data/v9.0/$metadata#accounts(accountid,name)","value":[  
    {  
        "@odata.etag":"W/\"506678\"",
        "accountid":"89390c24-9c72-e511-80d4-00155d2a68d1",
        "name":"Fourth Coffee (sample)", 
        "accountnumber":"1234",
    },{  
        "@odata.etag":"W/\"502172\"",
        "accountid":"8b390c24-9c72-e511-80d4-00155d2a68d1",
        "name":"Litware, Inc. (sample)"  
    },{  
        "@odata.etag":"W/\"502174\"",
        "accountid":"8d390c24-9c72-e511-80d4-00155d2a68d1",
        "name":"Adventure Works (sample)"  
    },{  
        "@odata.etag":"W/\"506705\"",
        "accountid":"8f390c24-9c72-e511-80d4-00155d2a68d1",
        "name":"Fabrikam, Inc. (sample)"  
    }
  ]  
}  
```

> [!NOTE]
> Properties with null values will not be included in results returned using FetchXml. In the example above, only the first record returned has an `accountnumber` value.

<a name="bkmk_WebAPIFetchPaging"></a>

### Paging with FetchXML

With FetchXML you can apply simple paging by setting the `page` and `count` attributes of the `fetch` element. For example, to set a query for accounts and limit the number of entities to 2 and to return just the first page, the following fetchXML:

```xml
<fetch mapping="logical" page="1" count="2">  
 <entity name="account">  
  <attribute name="accountid" />  
  <attribute name="name" />  
  <attribute name="industrycode" />  
 <order attribute="name" />  
 </entity>  
</fetch>
```

<!-- TODO:
With a request using FetchXML you can also request a paging cookie and include it with your query. More information:[Page large result sets with FetchXML](../org-service/page-large-result-sets-with-fetchxml.md)   -->

A paging cookie must be requested as an annotation. Set the `odata.include-annotations` preference to use (or include) `Microsoft.Dynamics.CRM.fetchxmlpagingcookie` and a `@Microsoft.Dynamics.CRM.fetchxmlpagingcookie` property will be returned with the result.

<a name="bkmk_FetchXMLwithinBatch"></a>

### Use FetchXML within a batch request

The length of a URL in a `GET` request is limited. Including FetchXML as a parameter in the URL can reach this limit.  You can execute a `$batch` operation using a `POST` request as a way to move the FetchXML out of the URL and into the body of the request where this limit will not apply. More information:[Execute batch operations using the Web API](execute-batch-operations-using-web-api.md).

> [!NOTE]
> Sending a `GET` request within a Batch allows for URLs up to 64 KB (65,536 characters) in length. Much more than with a normal `GET` request, but it isn't unlimited.

#### Example

**Request**

```http
POST [Organization URI]/api/data/v9.0/$batch HTTP/1.1

Content-Type:multipart/mixed;boundary=batch_AAA123
Accept:application/json
OData-MaxVersion:4.0
OData-Version:4.0

--batch_AAA123
Content-Type: application/http
Content-Transfer-Encoding: binary

GET [Organization URI]/api/data/v9.0/accounts?fetchXml=%3Cfetch%20mapping='logical'%3E%3Centity%20name='account'%3E%3Cattribute%20name='accountid'/%3E%3Cattribute%20name='name'/%3E%3Cattribute%20name='telephone1'/%3E%3Cattribute%20name='accountid'/%3E%3Cattribute%20name='creditonhold'/%3E%3C/entity%3E%3C/fetch%3E HTTP/1.1
Content-Type: application/json
OData-Version: 4.0
OData-MaxVersion: 4.0

--batch_AAA123--
```

**Response**

```json
--batchresponse_cbfd44cd-a322-484e-913b-49e18af44e34
Content-Type: application/http
Content-Transfer-Encoding: binary

HTTP/1.1 200 OK
Content-Type: application/json; odata.metadata=minimal
OData-Version: 4.0

{  
   "@odata.context":"[Organization URI]/api/data/v9.0/$metadata#accounts(accountid,name,telephone1,creditonhold)",
   "value":[  
      {  
         "@odata.etag":"W/\"563737\"",
         "accountid":"1f55c679-485e-e811-8151-000d3aa3c22a",
         "name":"Fourth Coffee (sample)",
         "telephone1":"+1-425-555-0121",
         "creditonhold":false
      },
      {  
         "@odata.etag":"W/\"563739\"",
         "accountid":"2555c679-485e-e811-8151-000d3aa3c22a",
         "name":"Litware, Inc. (sample)",
         "telephone1":"+1-425-555-0120",
         "creditonhold":false
      }
   ]
}
--batchresponse_cbfd44cd-a322-484e-913b-49e18af44e34--
```

## See also

[Use FetchXML to construct a query](../use-fetchxml-construct-query.md)<br />
[Query data using the Web API](query-data-web-api.md)<br />
[Retrieve related table records with a query](retrieve-related-entities-query.md)<br />
[Retrieve and execute predefined queries](retrieve-and-execute-predefined-queries.md)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]