---
title: Use FetchXML with Web API
description: FetchXML provides another way to define a query you can use with Web API to retrieve table data.
ms.topic: how-to
ms.date: 09/27/2022
author: divkamath
ms.author: dikamath
ms.reviewer: jdaly
search.audienceType: 
  - developer
contributors: 
  - JimDaly
ms.custom: bap-template
---
# Use FetchXML with Web API

FetchXML is a proprietary query language that can retrieve and aggregate data using the Web API and the .NET SDK. More information: [Use FetchXML to query data](../use-fetchxml-construct-query.md).

> [!NOTE]
> Unlike queries that use the OData syntax, FetchXML queries don't return properties with `null` values.

You can compose a FetchXML query for a specific table. Then, URL-encode the XML and use the `fetchXml` query string parameter to pass it to the entity set.

For example, the following FetchXML has `account` as the entity:

```xml  
<fetch mapping='logical'>
   <entity name='account'>
      <attribute name='accountid'/>
      <attribute name='name'/>
      <attribute name='accountnumber'/>      
</entity>
</fetch>
```

This FetchXML has the following URL-encoded value:

```text
%3Cfetch%20mapping%3D%27logical%27%3E%3Centity%20name%3D%27account%27%3E%3Cattribute%20name%3D%27accountid%27%2F%3E%3Cattribute%20name%3D%27name%27%2F%3E%3Cattribute%20name%3D%27accountnumber%27%2F%3E%3C%2Fentity%3E%3C%2Ffetch%3E
```

Most programming languages include a function to URL-encode a string.

- In JavaScript, you use the [encodeURI](https://www.ecma-international.org/ecma-262/5.1/) function.
- In .NET, you can use the [System.NET.WebUtility.UrlEncode(String) method](/dotnet/api/system.net.webutility.urlencode)

You should URL-encode any request that you send to any RESTful web service. If you paste a URL into the address bar of your browser, it should URL-encode the address automatically.

The following example shows a `GET` request using the previous FetchXML with the entity set path for `accounts`. It passes the encoded XML using this parameter: `?fetchXml=`

**Request:**

```http
GET [Organization URI]/api/data/v9.2/accounts?fetchXml=%3Cfetch%20mapping%3D%27logical%27%3E%3Centity%20name%3D%27account%27%3E%3Cattribute%20name%3D%27accountid%27%2F%3E%3Cattribute%20name%3D%27name%27%2F%3E%3Cattribute%20name%3D%27accountnumber%27%2F%3E%3C%2Fentity%3E%3C%2Ffetch%3E HTTP/1.1
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
  "@odata.context":"[Organization URI]/api/data/v9.2/$metadata#accounts(accountid,name)","value":[  
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

Recall that properties with null values aren't included in results returned using FetchXML. In this example, only the first record returned has an `accountnumber` value.

<a name="bkmk_WebAPIFetchPaging"></a>

## Paging with FetchXML

With FetchXML, you can apply simple paging by setting the `page` and `count` attributes of the `fetch` element. For example, the following fetchXML queries accounts, limits the number of entities to 2, and returns just the first page:

```xml
<fetch mapping="logical"
   page="1"
   count="2">
   <entity name="account">
      <attribute name="accountid" />
      <attribute name="name" />
      <attribute name="industrycode" />
      <order attribute="name" />
   </entity>
</fetch>
```

### Paging large result sets

When you're working with large result sets that hit the paging limit of 5,000, using paging cookies with the query helps improve performance. Request a paging cookie as an annotation. Use the `prefer: odata.include-annotations` request header to use or include `Microsoft.Dynamics.CRM.fetchxmlpagingcookie`, and a `@Microsoft.Dynamics.CRM.fetchxmlpagingcookie` annotation is returned with the result.

The following series of FetchXML requests show the use of paging cookies. This example uses a small `count` value (3) for brevity. Normally you wouldn't use paging cookies for such small page sizes.

```xml
<fetch page='1'
   count='3'
   paging-cookie=''
   mapping='logical'
   output-format='xml-platform'
   version='1.0'
   distinct='false'>
   <entity name ='contact'>
      <attribute name ='fullname' />
      <attribute name ='jobtitle' />
      <attribute name ='annualincome' />
      <order descending ='true'
         attribute='fullname' />
      <filter type ='and'>
         <condition value ='%(sample)%'
            attribute='fullname'
            operator='like' />
         <condition value ='18717e9c-643f-ed11-9db0-002248225e95'
            attribute='parentcustomerid'
            operator='eq' />
      </filter>
   </entity>
</fetch>
```

#### First Page

Send the first page with the `page` value set to `'1'`. Use the `Prefer: odata.include-annotations="*"` request header to make sure necessary annotations in the response are returned.

**Request:**

```http
GET [Organization Uri]/api/data/v9.2/contacts?fetchXml=%3Cfetch+page%3D%221%22+count%3D%223%22+mapping%3D%22logical%22+output-format%3D%22xml-platform%22+version%3D%221.0%22+distinct%3D%22false%22%3E%0D%0A++%3Centity+name%3D%22contact%22%3E%0D%0A++++%3Cattribute+name%3D%22fullname%22+%2F%3E%0D%0A++++%3Cattribute+name%3D%22jobtitle%22+%2F%3E%0D%0A++++%3Cattribute+name%3D%22annualincome%22+%2F%3E%0D%0A++++%3Corder+descending%3D%22true%22+attribute%3D%22fullname%22+%2F%3E%0D%0A++++%3Cfilter+type%3D%22and%22%3E%0D%0A++++++%3Ccondition+value%3D%22%25(sample)%25%22+attribute%3D%22fullname%22+operator%3D%22like%22+%2F%3E%0D%0A++++++%3Ccondition+value%3D%2218717e9c-643f-ed11-9db0-002248225e95%22+attribute%3D%22parentcustomerid%22+operator%3D%22eq%22+%2F%3E%0D%0A++++%3C%2Ffilter%3E%0D%0A++%3C%2Fentity%3E%0D%0A%3C%2Ffetch%3E&$count=true HTTP/1.1
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
  "@Microsoft.Dynamics.CRM.globalmetadataversion": "74343461",
  "@Microsoft.Dynamics.CRM.fetchxmlpagingcookie": "<cookie pagenumber=\"2\" pagingcookie=\"%253ccookie%2520page%253d%25221%2522%253e%253cfullname%2520last%253d%2522Robert%2520Lyon%2520%2528sample%2529%2522%2520first%253d%2522Susanna%2520Stubberod%2520%2528sample%2529%2522%2520%252f%253e%253ccontactid%2520last%253d%2522%257b30717E9C-643F-ED11-9DB0-002248225E95%257d%2522%2520first%253d%2522%257b20717E9C-643F-ED11-9DB0-002248225E95%257d%2522%2520%252f%253e%253c%252fcookie%253e\" istracking=\"False\" />",
  "@Microsoft.Dynamics.CRM.morerecords": true,
  "value": [
    {
      "@odata.etag": "W/\"74359676\"",
      "fullname": "Susanna Stubberod (sample)",
      "jobtitle": "Senior Purchaser",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$52,000.00",
      "annualincome": 52000.0,
      "contactid": "20717e9c-643f-ed11-9db0-002248225e95"
    },
    {
      "@odata.etag": "W/\"74359706\"",
      "fullname": "Scott Konersmann (sample)",
      "jobtitle": "Accounts Manager",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$38,000.00",
      "annualincome": 38000.0,
      "contactid": "2c717e9c-643f-ed11-9db0-002248225e95"
    },
    {
      "@odata.etag": "W/\"74359716\"",
      "fullname": "Robert Lyon (sample)",
      "jobtitle": "Senior Technician",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$78,000.00",
      "annualincome": 78000.0,
      "contactid": "30717e9c-643f-ed11-9db0-002248225e95"
    }
  ]
}
```

In the response, the `@Microsoft.Dynamics.CRM.morerecords` annotation value indicates that more records exist that match the criteria.

The `@Microsoft.Dynamics.CRM.fetchxmlpagingcookie` annotation value provides the paging information about the record returned. The `@Microsoft.Dynamics.CRM.fetchxmlpagingcookie` value is an XML document. You need to use the `pagingcookie` attribute value of that document in the next request.

The `pagingcookie` attribute value is URL-encoded twice. The decoded value looks like this:

```xml
<cookie page="1"><fullname last="Robert Lyon (sample)" first="Susanna Stubberod (sample)" /><contactid last="{30717E9C-643F-ED11-9DB0-002248225E95}" first="{20717E9C-643F-ED11-9DB0-002248225E95}" /></cookie>
```


#### Following Pages

In all subsequent requests where the previous page `@Microsoft.Dynamics.CRM.morerecords` annotation value indicates that more records exist, you need to:

1. Increment the `fetch` element `page` attribute value.
1. URL-decode the `pagingcookie` attribute value twice.
1. XML-encode the decoded `pagingcookie` attribute value and set it as the value of a `paging-cookie` attribute on the `fetch` element.

    Whether you must explicitly XML-encode the value may depend on the technology you use. In .NET, it might be done for you when you set the XML value to an attribute of another XML element.

1. URL Encode the entire FetchXml value as you did in the first request.

In the following request, the FetchXML looks like this before it's URL-encoded:

```xml
<fetch page="2" count="3" mapping="logical" output-format="xml-platform" version="1.0" distinct="false" paging-cookie="&lt;cookie page=&quot;1&quot;&gt;&lt;fullname last=&quot;Robert Lyon (sample)&quot; first=&quot;Susanna Stubberod (sample)&quot; /&gt;&lt;contactid last=&quot;{30717E9C-643F-ED11-9DB0-002248225E95}&quot; first=&quot;{20717E9C-643F-ED11-9DB0-002248225E95}&quot; /&gt;&lt;/cookie&gt;">
  <entity name="contact">
    <attribute name="fullname" />
    <attribute name="jobtitle" />
    <attribute name="annualincome" />
    <order descending="true" attribute="fullname" />
    <filter type="and">
      <condition value="%(sample)%" attribute="fullname" operator="like" />
      <condition value="18717e9c-643f-ed11-9db0-002248225e95" attribute="parentcustomerid" operator="eq" />
    </filter>
  </entity>
</fetch>
```

**Request:**

```http
GET [Organization Uri]/api/data/v9.2/contacts?fetchXml=%3Cfetch+page%3D%222%22+count%3D%223%22+mapping%3D%22logical%22+output-format%3D%22xml-platform%22+version%3D%221.0%22+distinct%3D%22false%22+paging-cookie%3D%22%26lt%3Bcookie+page%3D%26quot%3B1%26quot%3B%26gt%3B%26lt%3Bfullname+last%3D%26quot%3BRobert+Lyon+(sample)%26quot%3B+first%3D%26quot%3BSusanna+Stubberod+(sample)%26quot%3B+%2F%26gt%3B%26lt%3Bcontactid+last%3D%26quot%3B%7B30717E9C-643F-ED11-9DB0-002248225E95%7D%26quot%3B+first%3D%26quot%3B%7B20717E9C-643F-ED11-9DB0-002248225E95%7D%26quot%3B+%2F%26gt%3B%26lt%3B%2Fcookie%26gt%3B%22%3E%0D%0A++%3Centity+name%3D%22contact%22%3E%0D%0A++++%3Cattribute+name%3D%22fullname%22+%2F%3E%0D%0A++++%3Cattribute+name%3D%22jobtitle%22+%2F%3E%0D%0A++++%3Cattribute+name%3D%22annualincome%22+%2F%3E%0D%0A++++%3Corder+descending%3D%22true%22+attribute%3D%22fullname%22+%2F%3E%0D%0A++++%3Cfilter+type%3D%22and%22%3E%0D%0A++++++%3Ccondition+value%3D%22%25(sample)%25%22+attribute%3D%22fullname%22+operator%3D%22like%22+%2F%3E%0D%0A++++++%3Ccondition+value%3D%2218717e9c-643f-ed11-9db0-002248225e95%22+attribute%3D%22parentcustomerid%22+operator%3D%22eq%22+%2F%3E%0D%0A++++%3C%2Ffilter%3E%0D%0A++%3C%2Fentity%3E%0D%0A%3C%2Ffetch%3E&$count=true HTTP/1.1
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
  "@Microsoft.Dynamics.CRM.globalmetadataversion": "74343461",
  "@Microsoft.Dynamics.CRM.fetchxmlpagingcookie": "<cookie pagenumber=\"2\" pagingcookie=\"%253ccookie%2520page%253d%25222%2522%253e%253cfullname%2520last%253d%2522Nancy%2520Anderson%2520%2528sample%2529%2522%2520first%253d%2522Rene%2520Valdes%2520%2528sample%2529%2522%2520%252f%253e%253ccontactid%2520last%253d%2522%257b24717E9C-643F-ED11-9DB0-002248225E95%257d%2522%2520first%253d%2522%257b38717E9C-643F-ED11-9DB0-002248225E95%257d%2522%2520%252f%253e%253c%252fcookie%253e\" istracking=\"False\" />",
  "@Microsoft.Dynamics.CRM.morerecords": true,
  "value": [
    {
      "@odata.etag": "W/\"74359736\"",
      "fullname": "Rene Valdes (sample)",
      "jobtitle": "Data Analyst III",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$86,000.00",
      "annualincome": 86000.0,
      "contactid": "38717e9c-643f-ed11-9db0-002248225e95"
    },
    {
      "@odata.etag": "W/\"74359726\"",
      "fullname": "Paul Cannon (sample)",
      "jobtitle": "Ski Instructor",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$68,500.00",
      "annualincome": 68500.0,
      "contactid": "34717e9c-643f-ed11-9db0-002248225e95"
    },
    {
      "@odata.etag": "W/\"74359686\"",
      "fullname": "Nancy Anderson (sample)",
      "jobtitle": "Activities Manager",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$55,500.00",
      "annualincome": 55500.0,
      "contactid": "24717e9c-643f-ed11-9db0-002248225e95"
    }
  ]
}
```



#### Last Page

On the final page, the `@Microsoft.Dynamics.CRM.morerecords` and `@Microsoft.Dynamics.CRM.fetchxmlpagingcookie` annotations aren't included in the response.

**Request:**

```http
GET [Organization Uri]/api/data/v9.2/contacts?fetchXml=%3Cfetch+page%3D%223%22+count%3D%223%22+mapping%3D%22logical%22+output-format%3D%22xml-platform%22+version%3D%221.0%22+distinct%3D%22false%22+paging-cookie%3D%22%26lt%3Bcookie+page%3D%26quot%3B2%26quot%3B%26gt%3B%26lt%3Bfullname+last%3D%26quot%3BNancy+Anderson+(sample)%26quot%3B+first%3D%26quot%3BRene+Valdes+(sample)%26quot%3B+%2F%26gt%3B%26lt%3Bcontactid+last%3D%26quot%3B%7B24717E9C-643F-ED11-9DB0-002248225E95%7D%26quot%3B+first%3D%26quot%3B%7B38717E9C-643F-ED11-9DB0-002248225E95%7D%26quot%3B+%2F%26gt%3B%26lt%3B%2Fcookie%26gt%3B%22%3E%0D%0A++%3Centity+name%3D%22contact%22%3E%0D%0A++++%3Cattribute+name%3D%22fullname%22+%2F%3E%0D%0A++++%3Cattribute+name%3D%22jobtitle%22+%2F%3E%0D%0A++++%3Cattribute+name%3D%22annualincome%22+%2F%3E%0D%0A++++%3Corder+descending%3D%22true%22+attribute%3D%22fullname%22+%2F%3E%0D%0A++++%3Cfilter+type%3D%22and%22%3E%0D%0A++++++%3Ccondition+value%3D%22%25(sample)%25%22+attribute%3D%22fullname%22+operator%3D%22like%22+%2F%3E%0D%0A++++++%3Ccondition+value%3D%2218717e9c-643f-ed11-9db0-002248225e95%22+attribute%3D%22parentcustomerid%22+operator%3D%22eq%22+%2F%3E%0D%0A++++%3C%2Ffilter%3E%0D%0A++%3C%2Fentity%3E%0D%0A%3C%2Ffetch%3E&$count=true HTTP/1.1
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
  "@Microsoft.Dynamics.CRM.globalmetadataversion": "74343461",
  "value": [
    {
      "@odata.etag": "W/\"74359696\"",
      "fullname": "Maria Cambell (sample)",
      "jobtitle": "Accounts Manager",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$31,000.00",
      "annualincome": 31000.0,
      "contactid": "28717e9c-643f-ed11-9db0-002248225e95"
    },
    {
      "@odata.etag": "W/\"74359746\"",
      "fullname": "Jim Glynn (sample)",
      "jobtitle": "Senior International Sales Manager",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$81,400.00",
      "annualincome": 81400.0,
      "contactid": "3c717e9c-643f-ed11-9db0-002248225e95"
    }
  ]
}
```

<a name="bkmk_FetchXMLwithinBatch"></a>

## Use FetchXML within a batch request

The length of a URL in a `GET` request is limited. Including FetchXML as a parameter in the URL can reach the limit. You can execute a `$batch` operation using a `POST` request as a way to move the FetchXML out of the URL and into the body of the request where the limit doesn't apply. Sending a `GET` request within a `$batch` allows for URLs up to 64 KB (65,536 characters) in length. More than with a normal `GET` request, but it isn't unlimited. More information: [Execute batch operations using the Web API](execute-batch-operations-using-web-api.md).

### Example

**Request:**

```http
POST [Organization URI]/api/data/v9.2/$batch HTTP/1.1
Content-Type:multipart/mixed;boundary=batch_AAA123
Accept:application/json
OData-MaxVersion:4.0
OData-Version:4.0

--batch_AAA123
Content-Type: application/http
Content-Transfer-Encoding: binary

GET [Organization URI]/api/data/v9.2/accounts?fetchXml=%3Cfetch%20mapping='logical'%3E%3Centity%20name='account'%3E%3Cattribute%20name='accountid'/%3E%3Cattribute%20name='name'/%3E%3Cattribute%20name='telephone1'/%3E%3Cattribute%20name='accountid'/%3E%3Cattribute%20name='creditonhold'/%3E%3C/entity%3E%3C/fetch%3E HTTP/1.1
Content-Type: application/json
OData-Version: 4.0
OData-MaxVersion: 4.0

--batch_AAA123--
```

**Response:**

```json
--batchresponse_cbfd44cd-a322-484e-913b-49e18af44e34
Content-Type: application/http
Content-Transfer-Encoding: binary

HTTP/1.1 200 OK
Content-Type: application/json; odata.metadata=minimal
OData-Version: 4.0

{  
   "@odata.context":"[Organization URI]/api/data/v9.2/$metadata#accounts(accountid,name,telephone1,creditonhold)",
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

### See also

[Use FetchXML to construct a query](../use-fetchxml-construct-query.md)   
[Query data using the Web API](query-data-web-api.md)   
[Retrieve and execute predefined queries](retrieve-and-execute-predefined-queries.md)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
