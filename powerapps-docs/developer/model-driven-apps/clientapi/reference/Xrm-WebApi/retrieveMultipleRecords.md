---
title: "retrieveMultipleRecords (Client API reference) in model-driven apps| MicrosoftDocs"
ms.date: 05/24/2018
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: d4e92999-3b79-4783-8cac-f656fc5f7fda
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
---
# retrieveMultipleRecords (Client API reference)



[!INCLUDE[./includes/retrieveMultipleRecords-description.md](./includes/retrieveMultipleRecords-description.md)] 

## Syntax

`Xrm.WebApi.retrieveMultipleRecords(entityLogicalName, options, maxPageSize).then(successCallback, errorCallback);`

## Parameters

<table style="width:100%">
<tr>
<th>Name</th>
<th>Type</th>
<th>Required</th>
<th>Description</th>
</tr>
<tr>
<td>entityLogicalName</td>
<td>String</td>
<td>Yes</td>
<td>The entity logical name of the records you want to retrieve. For example: "account".</td>
</tr>
<tr>
<td>options</td>
<td>String</td>
<td>No</td>
<td><p>OData system query options or FetchXML query to retrieve your data. </p> 
<ul>
<li>Following system query options are supported: <b>$select</b>, <b>$top</b>, <b>$filter</b>, <b>$expand</b>, and <b>$orderby</b>.</li>
<li>To specify a FetchXML query, use the <code>fetchXml</code> attribute to specify the query.</li>
</ul>
<p>NOTE: You must always use the <b>$select</b> system query option to limit the properties returned for an entity record by including a comma-separated list of property names. This is an important performance best practice. If properties aren’t specified using <b>$select</b>, all properties will be returned.</li>
<p>You specify the query options starting with <code>?</code>. You can also specify multiple system query options by using <code>&</code> to separate the query options.
<p>See examples later in this topic to see how you can define the <code>options</code> parameter for various retrieve multiple scenarios.</td>
</tr>
<tr>
<td>maxPageSize</td>
<td>Number</td>
<td>No</td>
<td><p>Specify a positive number that indicates the number of entity records to be returned per page. If you do not specify this parameter, the default value is passed as 5000.</p>
<p>If the number of records being retrieved is more than the specified <code>maxPageSize</code> value, <code>nextLink</code> attribute in the returned promise object will contain a link to retrieve the next set of entities. </td>
</tr>
<tr>
<td>successCallback</td>
<td>Function</td>
<td>No</td>
<td><p>A function to call when entity records are retrived. An object with the following attributes is passed to the function:</p>
<ul>
<li><b>entities</b>: An array of JSON objects, where each object represents the retrieved entity record containing attributes and their values as <code>key: value</code> pairs. The Id of the entity record is retrieved by default.</li>
<li><b>nextLink</b>: String. If the number of records being retrieved is more than the value specified in the <code>maxPageSize</code> parameter in the request, this attribute returns the URL to return next set of records.</li>
</ul>
</td>
</tr>
<tr>
<td>errorCallback</td>
<td>Function</td>
<td>No</td>
<td>A function to call when the operation fails.</td>
</tr>
</table>

## Return Value

On success, returns a promise that contains an array of JSON objects (**entities**) containing the retrieved entity records and the **nextLink** attribute (optional) with the URL pointing to next set of records in case paging (`maxPageSize`) is specified in the request, and the record count returned exceeds the paging value.

## Examples

Most of the scenarios/examples mentioned in [Query Data using the Web API](../../../../common-data-service/webapi/query-data-web-api.md) can be achieved using the **retrieveMutipleRecords** method. Some of the examples are listed below.

### Basic retrieve multiple

This example queries the accounts entity set and uses the `$select` and `$top` system query options to return the name property for the first three accounts:

```JavaScript
Xrm.WebApi.retrieveMultipleRecords("account", "?$select=name&$top=3").then(
    function success(result) {
        for (var i = 0; i < result.entities.length; i++) {
            console.log(result.entities[i]);
        }                    
        // perform additional operations on retrieved records
    },
    function (error) {
        console.log(error.message);
        // handle error conditions
    }
);
```

### Specify the number of entities to return in a page

The following example demonstrates the use of the `maxPageSize` parameter to specify the number of records (3) to be displayed in a page.

```JavaScript
Xrm.WebApi.retrieveMultipleRecords("account", "?$select=name", 3).then(
    function success(result) {
        for (var i = 0; i < result.entities.length; i++) {
            console.log(result.entities[i]);
        }
        console.log("Next page link: " + result.nextLink);
        // perform additional operations on retrieved records
    },
    function (error) {
        console.log(error.message);
        // handle error conditions
    }
);
```

This example will display 3 records and a link to the next page. Here is an example outout from the **Console** in the browser developer tools:

```
{@odata.etag: "W/"1035541"", name: "A. Datum", accountid: "475b158c-541c-e511-80d3-3863bb347ba8"}
@odata.etag: "W/"1035541""accountid: "475b158c-541c-e511-80d3-3863bb347ba8"name: "A. Datum"__proto__: Object
VM5595:4 
{@odata.etag: "W/"947306"", name: "Adventure Works", accountid: "a8a19cdd-88df-e311-b8e5-6c3be5a8b200"}
VM5595:4 
{@odata.etag: "W/"1033754"", name: "Alpine Ski House", accountid: "aaa19cdd-88df-e311-b8e5-6c3be5a8b200"}
VM5595:6 
Next page link: [Organization URI]/api/data/v9.0/accounts?$select=name&$skiptoken=%3Ccookie%20pagenumber=%222%22%20pagingcookie=%22%253ccookie%2520page%253d%25221%2522%253e%253caccountid%2520last%253d%2522%257bAAA19CDD-88DF-E311-B8E5-6C3BE5A8B200%257d%2522%2520first%253d%2522%257b475B158C-541C-E511-80D3-3863BB347BA8%257d%2522%2520%252f%253e%253c%252fcookie%253e%22%20istracking=%22False%22%20/%3E
```

Use the query part in the URL in the `nextLink` property as the value for the `options` parameter in your subsequent **retrieveMultipleRecords** call to request the next set of records. Don’t change or append any additional system query options to the value. For every subsequent request for additional pages, you should use the same `maxPageSize` value used in the original retrieve multiple request. Also, cache the results returned or the value of the nextLink property so that previously retrieved pages can be returned. 

For example, to get the next page of records, we will pass in the query part of the `nextLink` URL to the `options` parameter:

```JavaScript
Xrm.WebApi.retrieveMultipleRecords("account", "?$select=name&$skiptoken=%3Ccookie%20pagenumber=%222%22%20pagingcookie=%22%253ccookie%2520page%253d%25221%2522%253e%253caccountid%2520last%253d%2522%257bAAA19CDD-88DF-E311-B8E5-6C3BE5A8B200%257d%2522%2520first%253d%2522%257b475B158C-541C-E511-80D3-3863BB347BA8%257d%2522%2520%252f%253e%253c%252fcookie%253e%22%20istracking=%22False%22%20/%3E", 3).then(
    function success(result) {
        for (var i = 0; i < result.entities.length; i++) {
            console.log(result.entities[i]);
        }
        console.log("Next page link: " + result.nextLink);
        // perform additional operations on retrieved records
    },
    function (error) {
        console.log(error.message);
        // handle error conditions
    }
);
```

This will return the next page of the resultset:

```
{@odata.etag: "W/"1035542"", name: "Blue Yonder Airlines", accountid: "aca19cdd-88df-e311-b8e5-6c3be5a8b200"}
VM5597:4 
{@odata.etag: "W/"1031348"", name: "City Power & Light", accountid: "aea19cdd-88df-e311-b8e5-6c3be5a8b200"}
VM5597:4 
{@odata.etag: "W/"1035543"", name: "Coho Winery", accountid: "b0a19cdd-88df-e311-b8e5-6c3be5a8b200"}
VM5597:6 
Next page link: [Organization URI]/api/data/v9.0/accounts?$select=name&$skiptoken=%3Ccookie%20pagenumber=%223%22%20pagingcookie=%22%253ccookie%2520page%253d%25222%2522%253e%253caccountid%2520last%253d%2522%257bB0A19CDD-88DF-E311-B8E5-6C3BE5A8B200%257d%2522%2520first%253d%2522%257bACA19CDD-88DF-E311-B8E5-6C3BE5A8B200%257d%2522%2520%252f%253e%253c%252fcookie%253e%22%20istracking=%22False%22%20/%3E
``` 
  
> [!IMPORTANT]
>  The value of the `nextLink` property is URI encoded. If you URI encode the value before you send it, the XML cookie information in the URL will cause an error.

### Retrieve related entities by expanding navigation properties

Use the **$expand** system query option in the navigation properties to control the data that is returned from related entities. The following example demonstrates how to retrieve the contact for all the account records. For the related contact records, we are only retrieving the `contactid` and `fullname`:

```JavaScript
Xrm.WebApi.retrieveMultipleRecords("account", "?$select=name&$top=3&$expand=primarycontactid($select=contactid,fullname)", 3).then(
    function success(result) {
        for (var i = 0; i < result.entities.length; i++) {
            console.log(result.entities[i]);
        }        
        // perform additional operations on retrieved records
    },
    function (error) {
        console.log(error.message);
        // handle error conditions
    }
);
```


For more examples of retrieving multiple records using Web API, see [Query Data using the Web API](../../../../common-data-service/webapi/query-data-web-api.md).

 
### Related topics

[Query Data using the Web API](../../../../common-data-service/webapi/query-data-web-api.md)

[Xrm.WebApi.retrieveRecord](retrieveRecord.md)

[Xrm.WebApi](../xrm-webapi.md)




