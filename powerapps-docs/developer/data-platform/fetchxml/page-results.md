---
title: Page results using FetchXml
description: Learn how to use FetchXml to page results when you retrieve data from Microsoft Dataverse.
ms.date: 08/31/2023
ms.reviewer: jdaly
ms.topic: how-to
author: pnghub
ms.subservice: dataverse-developer
ms.author: gned
search.audienceType: 
  - developer
---
# Page results using FetchXml

Dataverse will return up to 5,000 rows of data with each request. If you need to get more rows of data, you need to send additional requests for subsequent pages. If you want your application to efficiently retrieve smaller set of data, you can use paging to specify the number of records to return.

## Simple paging

<!-- 
TODO: Clarify 'Legacy Paging'

Is Legacy Paging = Simple paging?
Docs suggest that no paging cookie returned with legacy paging.

 -->

You can implement simple client-side paging using FetchXml by setting the [fetch element](reference/fetch.md) `page` and `count` attributes together. Set the `count` to the number of records and the `page` number you want.

To get the first three records:

```xml
<fetch count='3' page='1'>
  <entity name='account'>
    <attribute name='name' />
  </entity>
</fetch>
```

To get the next three records, increment the `page` value and send another request.

```xml
<fetch count='3' page='2'>
  <entity name='account'>
    <attribute name='name' />
  </entity>
</fetch>
```

Simple paging works well for small data sets, but as the size of the data set increases, performance suffers. For this reason, you can only retrieve up to 50,000 total records using simple paging. For best performance in all cases, we recommend consistently using the *paging cookie*.

## PagingCookie

A paging cookie is additional data that is returned when you retrieve multiple records. When you request the next page of record, set the paging cookie value returned from the previous page. The paging cookie contains information about the first and last records of the previous request. This allows Dataverse to more efficiently retrieve the next page, improving performance.

<!-- 
TODO: 
 - Should people cache the paging cookie if their application enables navigation from one page to the next?
 - Or is mostly for people to get all the records that match the criteria, regardless of how many records there are? 
 - Update this sample: https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/C%23/UseFetchXMLWithPaging
   - Add a RetrieveAll function that will apply paging to a FetchExpression.Query
   - Parameters:
      - FetchXml
      - PageSize (optional)
-->


## Paging large result sets with Web API

When you're working with large result sets that hit the paging limit of 5,000, using paging cookies with the query helps improve performance. Request a paging cookie as an annotation. Use the `prefer: odata.include-annotations="Microsoft.Dynamics.CRM.fetchxmlpagingcookie"` request header or `prefer: odata.include-annotations="*"`, and a `@Microsoft.Dynamics.CRM.fetchxmlpagingcookie` annotation is returned with the result.

The following series of FetchXML requests show the use of paging cookies. This example uses a small `count` value (3) for brevity. Normally you wouldn't use paging cookies for such small page sizes.

```xml
<fetch count='3' page='1'>
  <entity name='contact'>
    <attribute name='fullname' />
    <attribute name='jobtitle' />
    <attribute name='annualincome' />
    <order descending='true' attribute='fullname' />
  </entity>
</fetch>
```

### First Page

Send the first page with the `page` value set to `'1'`. Use the `Prefer: odata.include-annotations="Microsoft.Dynamics.CRM.fetchxmlpagingcookie,Microsoft.Dynamics.CRM.morerecords"` request header to make sure the paging cookie and more records annotation in the response is returned.

**Request:**

```http
GET [Organization Uri]/api/data/v9.2/contacts?fetchXml=%3Cfetch%20count%3D%273%27%20page%3D%271%27%3E%0D%0A%3Centity%20name%3D%27contact%27%3E%0D%0A%3Cattribute%20name%3D%27fullname%27%2F%3E%0D%0A%3Cattribute%20name%3D%27jobtitle%27%2F%3E%0D%0A%3Cattribute%20name%3D%27annualincome%27%2F%3E%0D%0A%3Corder%20descending%3D%27true%27%20attribute%3D%27fullname%27%2F%3E%0D%0A%3C%2Fentity%3E%0D%0A%3C%2Ffetch%3E&$count=true
Prefer: odata.include-annotations="Microsoft.Dynamics.CRM.fetchxmlpagingcookie,Microsoft.Dynamics.CRM.morerecords"
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
```

**Response:**

```http
HTTP/1.1 200 OK
OData-Version: 4.0
Preference-Applied: odata.include-annotations="Microsoft.Dynamics.CRM.fetchxmlpagingcookie,Microsoft.Dynamics.CRM.morerecords"

{
    "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#contacts(fullname,jobtitle,annualincome,_transactioncurrencyid_value,transactioncurrencyid,contactid,transactioncurrencyid())",
    "@Microsoft.Dynamics.CRM.fetchxmlpagingcookie": "<cookie pagenumber=\"2\" pagingcookie=\"%253ccookie%2520page%253d%25221%2522%253e%253cfullname%2520last%253d%2522Susanna%2520Stubberod%2520%2528sample%2529%2522%2520first%253d%2522Yvonne%2520McKay%2520%2528sample%2529%2522%2520%252f%253e%253ccontactid%2520last%253d%2522%257b70BF4D48-34CB-ED11-B596-0022481D68CD%257d%2522%2520first%253d%2522%257b49B0BE2E-D01C-ED11-B83E-000D3A572421%257d%2522%2520%252f%253e%253c%252fcookie%253e\" istracking=\"False\" />",
    "@Microsoft.Dynamics.CRM.morerecords": true,
    "value": [
        {
            "@odata.etag": "W/\"72201545\"",
            "fullname": "Yvonne McKay (sample)",
            "jobtitle": "Coffee Master",
            "annualincome": 45000.0000,
            "_transactioncurrencyid_value": "228f42f8-e646-e111-8eb7-78e7d162ced1",
            "contactid": "49b0be2e-d01c-ed11-b83e-000d3a572421"
        },
        {
            "@odata.etag": "W/\"80648856\"",
            "fullname": "Thomas Andersen (sample)",
            "jobtitle": "Purchasing Manager",
            "_transactioncurrencyid_value": "228f42f8-e646-e111-8eb7-78e7d162ced1",
            "contactid": "86bf4d48-34cb-ed11-b596-0022481d68cd"
        },
        {
            "@odata.etag": "W/\"80648695\"",
            "fullname": "Susanna Stubberod (sample)",
            "jobtitle": "Purchasing Manager",
            "_transactioncurrencyid_value": "228f42f8-e646-e111-8eb7-78e7d162ced1",
            "contactid": "70bf4d48-34cb-ed11-b596-0022481d68cd"
        }
    ]
}
```

In the response, the `@Microsoft.Dynamics.CRM.morerecords` annotation value indicates that more records exist that match the criteria.

The `@Microsoft.Dynamics.CRM.fetchxmlpagingcookie` annotation value provides the paging information about the record returned. The `@Microsoft.Dynamics.CRM.fetchxmlpagingcookie` value is an XML document. You need to use the `pagingcookie` attribute value of that document in the next request.

The `pagingcookie` attribute value is URL-encoded twice. The decoded value looks like this:

```xml
<cookie page="1"><fullname last="Susanna Stubberod (sample)" first="Yvonne McKay (sample)" /><contactid last="{70BF4D48-34CB-ED11-B596-0022481D68CD}" first="{49B0BE2E-D01C-ED11-B83E-000D3A572421}" /></cookie>
```


### Following Pages

In all subsequent requests where the previous page `@Microsoft.Dynamics.CRM.morerecords` annotation value indicates that more records exist, you need to:

1. Increment the `fetch` element `page` attribute value.
1. URL-decode the `pagingcookie` attribute value twice.
1. XML-encode the decoded `pagingcookie` attribute value and set it as the value of a `paging-cookie` attribute on the `fetch` element.

    Whether you must explicitly XML-encode the value may depend on the technology you use. In .NET, it might be done for you when you set the XML value to an attribute of another XML element.

1. URL Encode the entire FetchXml value as you did in the first request.

In the following request, the FetchXML looks like this before it's URL-encoded:

```xml
<fetch count='3' page='2' paging-cookie='&lt;cookie page="1"&gt;&lt;fullname last="Susanna Stubberod (sample)" first="Yvonne McKay (sample)" /&gt;&lt;contactid last="{70BF4D48-34CB-ED11-B596-0022481D68CD}" first="{49B0BE2E-D01C-ED11-B83E-000D3A572421}" /&gt;&lt;/cookie&gt;'>
  <entity name='contact'>
    <attribute name='fullname' />
    <attribute name='jobtitle' />
    <attribute name='annualincome' />
    <order descending='true' attribute='fullname' />
  </entity>
</fetch>
```

**Request:**

```http
GET [Organization Uri]/api/data/v9.2/contacts?fetchXml=%3Cfetch%20count%3D%273%27%20page%3D%272%27%20paging-cookie%3D%27%26lt%3Bcookie%20page%3D%221%22%26gt%3B%26lt%3Bfullname%20last%3D%22Susanna%20Stubberod%20%28sample%29%22%20first%3D%22Yvonne%20McKay%20%28sample%29%22%20%2F%26gt%3B%26lt%3Bcontactid%20last%3D%22%7B70BF4D48-34CB-ED11-B596-0022481D68CD%7D%22%20first%3D%22%7B49B0BE2E-D01C-ED11-B83E-000D3A572421%7D%22%20%2F%26gt%3B%26lt%3B%2Fcookie%26gt%3B%27%3E%0D%0A%3Centity%20name%3D%27contact%27%3E%0D%0A%3Cattribute%20name%3D%27fullname%27%2F%3E%0D%0A%3Cattribute%20name%3D%27jobtitle%27%2F%3E%0D%0A%3Cattribute%20name%3D%27annualincome%27%2F%3E%0D%0A%3Corder%20descending%3D%27true%27%20attribute%3D%27fullname%27%2F%3E%0D%0A%3C%2Fentity%3E%0D%0A%3C%2Ffetch%3E
Prefer: odata.include-annotations="Microsoft.Dynamics.CRM.fetchxmlpagingcookie,Microsoft.Dynamics.CRM.morerecords"
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
```

**Response:**

```http
HTTP/1.1 200 OK
OData-Version: 4.0
Preference-Applied: odata.include-annotations="Microsoft.Dynamics.CRM.fetchxmlpagingcookie,Microsoft.Dynamics.CRM.morerecords"

{
    "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#contacts(fullname,jobtitle,_transactioncurrencyid_value,transactioncurrencyid,contactid,annualincome,transactioncurrencyid())",
    "@Microsoft.Dynamics.CRM.fetchxmlpagingcookie": "<cookie pagenumber=\"2\" pagingcookie=\"%253ccookie%2520page%253d%25222%2522%253e%253cfullname%2520last%253d%2522Scott%2520Konersmann%2520%2528sample%2529%2522%2520first%253d%2522Susan%2520Burk%2520%2528sample%2529%2522%2520%252f%253e%253ccontactid%2520last%253d%2522%257b78BF4D48-34CB-ED11-B596-0022481D68CD%257d%2522%2520first%253d%2522%257b84BF4D48-34CB-ED11-B596-0022481D68CD%257d%2522%2520%252f%253e%253c%252fcookie%253e\" istracking=\"False\" />",
    "@Microsoft.Dynamics.CRM.morerecords": true,
    "value": [
        {
            "@odata.etag": "W/\"80648842\"",
            "fullname": "Susan Burk (sample)",
            "jobtitle": "Owner",
            "_transactioncurrencyid_value": "228f42f8-e646-e111-8eb7-78e7d162ced1",
            "contactid": "84bf4d48-34cb-ed11-b596-0022481d68cd"
        },
        {
            "@odata.etag": "W/\"80648744\"",
            "fullname": "Sidney Higa (sample)",
            "jobtitle": "Owner",
            "_transactioncurrencyid_value": "228f42f8-e646-e111-8eb7-78e7d162ced1",
            "contactid": "76bf4d48-34cb-ed11-b596-0022481d68cd"
        },
        {
            "@odata.etag": "W/\"80648758\"",
            "fullname": "Scott Konersmann (sample)",
            "jobtitle": "Purchasing Manager",
            "_transactioncurrencyid_value": "228f42f8-e646-e111-8eb7-78e7d162ced1",
            "contactid": "78bf4d48-34cb-ed11-b596-0022481d68cd"
        }
    ]
}
```



### Last Page

On the final page, the `@Microsoft.Dynamics.CRM.morerecords` and `@Microsoft.Dynamics.CRM.fetchxmlpagingcookie` annotations aren't included in the response.

**Request:**

```http
GET [Organization Uri]/api/data/v9.2/contacts?fetchXml=%3Cfetch%20count%3D%273%27%20page%3D%275%27%20paging-cookie%3D%27%26lt%3Bcookie%20page%3D%224%22%26gt%3B%26lt%3Bfullname%20last%3D%22Maria%20Campbell%20%28sample%29%22%20first%3D%22Patrick%20Sands%20%28sample%29%22%20%2F%26gt%3B%26lt%3Bcontactid%20last%3D%22%7B74BF4D48-34CB-ED11-B596-0022481D68CD%7D%22%20first%3D%22%7B82BF4D48-34CB-ED11-B596-0022481D68CD%7D%22%20%2F%26gt%3B%26lt%3B%2Fcookie%26gt%3B%27%3E%0D%0A%3Centity%20name%3D%27contact%27%3E%0D%0A%3Cattribute%20name%3D%27fullname%27%2F%3E%0D%0A%3Cattribute%20name%3D%27jobtitle%27%2F%3E%0D%0A%3Cattribute%20name%3D%27annualincome%27%2F%3E%0D%0A%3Corder%20descending%3D%27true%27%20attribute%3D%27fullname%27%2F%3E%0D%0A%3C%2Fentity%3E%0D%0A%3C%2Ffetch%3E
Prefer: odata.include-annotations="Microsoft.Dynamics.CRM.fetchxmlpagingcookie,Microsoft.Dynamics.CRM.morerecords"
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
    "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#contacts(fullname,jobtitle,_transactioncurrencyid_value,transactioncurrencyid,contactid,annualincome,transactioncurrencyid())",
    "value": [
        {
            "@odata.etag": "W/\"87523026\"",
            "fullname": "Jim Glynn (sample)",
            "jobtitle": "Owner",
            "_transactioncurrencyid_value": "228f42f8-e646-e111-8eb7-78e7d162ced1",
            "contactid": "80bf4d48-34cb-ed11-b596-0022481d68cd"
        }
    ]
}
```

## Next steps

Learn how to aggregate data.

> [!div class="nextstepaction"]
> [Aggregate data](aggregate-data.md)

[!INCLUDE [footer-banner](../../../includes/footer-banner.md)]