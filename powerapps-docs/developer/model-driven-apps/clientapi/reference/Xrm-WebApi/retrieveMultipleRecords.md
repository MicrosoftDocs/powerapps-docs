---
title: "retrieveMultipleRecords (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the retrieveMultipleRecords method.
ms.date: 04/21/2021
ms.service: powerapps
ms.topic: "reference"
ms.assetid: d4e92999-3b79-4783-8cac-f656fc5f7fda
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
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
<td>The table logical name of the records you want to retrieve. For example: "account".</td>
</tr>
<tr>
<td>options</td>
<td>String</td>
<td>No</td>
<td><p>OData system query options or FetchXML query to retrieve your data. </p> 
<ul>
<li>Following system query options are supported: <b>$select</b>, <b>$top</b>, <b>$filter</b>, <b>$expand</b>, and <b>$orderby</b>.</li>
<li>To specify a FetchXML query, use the <code>fetchXml</code> column to specify the query.</li>
</ul>
<p>NOTE: You must always use the <b>$select</b> system query option to limit the properties returned for a table record by including a comma-separated list of property names. This is an important performance best practice. If properties aren’t specified using <b>$select</b>, all properties will be returned.</li>
<p>You specify the query options starting with <code>?</code>. You can also specify multiple system query options by using <code>&</code> to separate the query options.
<p>When you specify an OData query string for the <code>options</code> parameter, the query <b>should be encoded</b> for special characters.
<p>When you specify a FetchXML query for the <code>options</code> parameter, the query <b>should not be encoded</b>. 
<p>See examples later in this topic to see how you can define the <code>options</code> parameter for various retrieve multiple scenarios.</td>
</tr>
<tr>
<td>maxPageSize</td>
<td>Number</td>
<td>No</td>
<td><p>Specify a positive number that indicates the number of table records to be returned per page. If you do not specify this parameter, the value is defaulted to the maximum limit of 5000 records.</p> 
<p>If the number of records being retrieved is more than the specified <code>maxPageSize</code> value or 5000 records, <code>nextLink</code> column in the returned promise object will contain a link to retrieve records. </td>
</tr>
<tr>
<td>successCallback</td>
<td>Function</td>
<td>No</td>
<td><p>A function to call when table records are retrieved. An object with the following values is passed to the function:</p>
<ul>
<li><b>entities</b>: An array of JSON objects, where each object represents the retrieved table record containing columns and their values as <code>key: value</code> pairs. The Id of the table record is retrieved by default.</li>
<li><b>nextLink</b>: (optional) String. If the number of records being retrieved is more than the value specified in the <code>maxPageSize</code> parameter in the request, this returns the URL to return the next page of records.</li>
<li><b>fetchXmlPagingCookie</b>: (optional) String. For a fetchXml-based retrieveMultipleRecords operation with paging where the total record count is greater than the paging value, this attribute returns the paging cookie that can be used for a subsequent fetchXml operation to retrieve the next page of records.</li>
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

For a successful OData query retrieveMultipleRecords operation, returns a promise that contains an array of JSON objects (**entities**) containing the retrieved table records and the **nextLink** attribute (optional) with the URL pointing to next page of records in case paging (`maxPageSize`) is specified in the request, and the record count returned exceeds the paging value.

For a succesful FetchXML-based retrieveMultipleRecords operations the promise response will contain a **fetchXmlPagingCookie** (optional) attribute when the operation returns more records than the paging value. This attribute will contain the paging cookie string that can be included in a subsequent fetchXml request to fetch the next page of records.

## Examples

Most of the scenarios/examples mentioned in [Query Data using the Web API](../../../../data-platform/webapi/query-data-web-api.md) can be achieved using the **retrieveMultipleRecords** method. Some of the examples are listed below.

### Basic retrieve multiple

This example queries the accounts table set and uses the `$select` and `$top` system query options to return the name property for the first three accounts:

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

### Basic retrieve multiple with FetchXML

This example queries the `account` entity using fetchXML.

```JavaScript
var fetchXml = "?fetchXml=<fetch mapping='logical'><entity name='account'><attribute name='accountid'/><attribute name='name'/></entity></fetch>";

Xrm.WebApi.retrieveMultipleRecords("account", fetchXml).then(
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

### Retrieve or filter by lookup properties
For most single-valued navigation properties you will find a computed, read-only property that uses the following naming convention: `_<name>_value` where the `<name>` is the name of the single-valued navigation property. For filtering purposes, the specific value of the single-valued navigation property can also be used.  However, for mobile clients in offline mode, these syntax options are not supported, and the single-value navigation property name should be used for both retrieving and filtering. Also, the comparison of navigation properties to null is not supported in offline mode.

More information: [Lookup properties](../../../../data-platform/webapi/web-api-types-operations.md#bkmk_lookupProperties)

Here are code examples for both the scenarios:

#### For online scenario (connected to server)

This example queries the accounts table set and uses the `$select` and `$filter` system query options to return the name and primarycontactid property for accounts that have a particular primary contact:

```JavaScript
Xrm.WebApi.retrieveMultipleRecords("account", "?$select=name,_primarycontactid_value&$filter=primarycontactid/contactid eq a0dbf27c-8efb-e511-80d2-00155db07c77").then(
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

#### For mobile offline scenario

This example queries the accounts table set and uses the `$select` and `$filter` system query options to return the name and primarycontactid property for accounts that have a particular primary contact when working in the offline mode:

```JavaScript
Xrm.WebApi.retrieveMultipleRecords("account", "?$select=name,primarycontactid&$filter=primarycontactid eq a0dbf27c-8efb-e511-80d2-00155db07c77").then(
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
### Specify the number of tables to return in a page

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

This example will display 3 records and a link to the next page. Here is an example output from the **Console** in the browser developer tools:

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

#### FetchXML Example (online scenario)
The following example demonstrates the use of the `count` parameter of the FetchXML to specify the number of records (3) to be displayed in a page.

> [!NOTE]
> The FetchXML paging cookie is only returned for online `retrieveMultipleRecords` operations.  ([Xrm.WebApi.online](online.md)). It is not supported offline.

```JavaScript
var fetchXml = "?fetchXml=<fetch mapping='logical' count='3'><entity name='account'><attribute name='accountid'/><attribute name='name'/></entity></fetch>";

Xrm.WebApi.online.retrieveMultipleRecords("account", fetchXml).then(
    function success(result) {
        for (var i = 0; i < result.entities.length; i++) {
            console.log(result.entities[i]);
        }          

        console.log("Paging cookie: " + result.fetchXmlPagingCookie);

        // perform additional operations on retrieved records
    },
    function (error) {
        console.log(error.message);
        // handle error conditions
    }
);
```

This example will display 3 records and return a FetchXML Paging Cookie to the retrieve the results of the next page if there are additional records belonging to the result set. Here is an example output from the **Console** in the browser developer tools:

```JSON
{
	"entities": [
		{
			"@odata.etag": "W/\"1035542\"",
			"accountid": "aca19cdd-88df-e311-b8e5-6c3be5a8b200",
			"name": "Blue Yonder Airlines"
		},
		{
			"@odata.etag": "W/\"1031348\"",
			"accountid": "aea19cdd-88df-e311-b8e5-6c3be5a8b200",
			"name": "City Power & Light"
		},
		{
			"@odata.etag": "W/\"1035543\"",
			"accountid": "b0a19cdd-88df-e311-b8e5-6c3be5a8b200",
			"name": "Coho Winery"
		}
	],
	"fetchXmlPagingCookie": "<cookie pagenumber=\"2\" pagingcookie=\"%253ccookie%2520page%253d%25221%2522%253e%253caccountid%2520last%253d%2522%257b0748C6EC-55A8-EB11-B1B5-000D3AFEF6FA%257d%2522%2520first%253d%2522%257bFC47C6EC-55A8-EB11-B1B5-000D3AFEF6FA%257d%2522%2520%252f%253e%253c%252fcookie%253e\" istracking=\"False\" />"
}
```

We can use the `fetchXmlPagingCookie` as shown in the example below to fetch large result sets with paging.

```JavaScript
function CreateXml(fetchXml, pagingCookie, page, count) {
  var domParser = new DOMParser();
  var xmlSerializer = new XMLSerializer();

  var fetchXmlDocument = domParser.parseFromString(fetchXml, "text/xml");

  if (page) {
    fetchXmlDocument
      .getElementsByTagName("fetch")[0]
      .setAttribute("page", page.toString());
  }

  if (count) {
    fetchXmlDocument
      .getElementsByTagName("fetch")[0]
      .setAttribute("count", count.toString());
  }

  if (pagingCookie) {
    var cookieDoc = domParser.parseFromString(pagingCookie, "text/xml");
    var innerPagingCookie = domParser.parseFromString(
      decodeURIComponent(
        decodeURIComponent(
          cookieDoc
            .getElementsByTagName("cookie")[0]
            .getAttribute("pagingcookie")
        )
      ),
      "text/xml"
    );
    fetchXmlDocument
      .getElementsByTagName("fetch")[0]
      .setAttribute(
        "paging-cookie",
        xmlSerializer.serializeToString(innerPagingCookie)
      );
  }

  return xmlSerializer.serializeToString(fetchXmlDocument);
}

function retrieveAllRecords(entityName, fetchXml, page, count, pagingCookie) {
  if (!page) {
    page = 0;
  }

  return retrievePage(entityName, fetchXml, page + 1, count, pagingCookie).then(
    function success(pageResults) {
      if (pageResults.fetchXmlPagingCookie) {
        return retrieveAllRecords(
          entityName,
          fetchXml,
          page + 1,
          count,
          pageResults.fetchXmlPagingCookie
        ).then(
          function success(results) {
            if (results) {
              return pageResults.entities.concat(results);
            }
          },
          function error(e) {
            throw e;
          }
        );
      } else {
        return pageResults.entities;
      }
    },
    function error(e) {
      throw e;
    }
  );
}

function retrievePage(entityName, fetchXml, pageNumber, count, pagingCookie) {
  var fetchXml =
    "?fetchXml=" + CreateXml(fetchXml, pagingCookie, pageNumber, count);

  return Xrm.WebApi.online.retrieveMultipleRecords(entityName, fetchXml).then(
    function success(result) {
      return result;
    },
    function error(e) {
      throw e;
    }
  );
}

var count = 3;
var fetchXml =
  '<fetch mapping="logical"><entity name="account"><attribute name="accountid"/><attribute name="name"/></entity></fetch>';

retrieveAllRecords("account", fetchXml, null, count, null).then(
  function success(result) {
    console.log(result);

    // perform additional operations on retrieved records
  },
  function error(error) {
    console.log(error.message);
    // handle error conditions
  }
);

```

### Retrieve related tables by expanding navigation properties
#### For online scenario (connected to server)

Use the **$expand** system query option in the navigation properties to control the data that is returned from related tables. The following example demonstrates how to retrieve the contact for all the account records. For the related contact records, we are only retrieving the `contactid` and `fullname`:

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
The above piece of code returns a result with a schema like:
```JSON
{
	"entities": [
		{
			"@odata.etag": "W/\"1459919\"",
			"name": "Test Account",
			"accountid": "119edfac-19c6-ea11-a81a-000d3af5e732",
			"primarycontactid": {
				"contactid": "6c63a1b7-19c6-ea11-a81a-000d3af5e732",
				"fullname": "Test Contact"
			}
		}
	]
}
```

#### For mobile offline scenario
**$expand** for the mobile offline scenario is different from the online scenario and is a multi-part process. An offline **\$expand** operation returns a `@odata.nextLink` annotation containing information on how to get to the related record's information. We use the `id`, `entityType`, and `options` parameter of that annotation to construct one or more additional `Xrm.WebApi.offline.retrieveRecord` request(s). The following piece of code provides a complete example of how to do this:

```JavaScript
Xrm.WebApi.offline.retrieveMultipleRecords("account", "?$select=name&$top=3&$expand=primarycontactid($select=contactid,fullname)").then(function(resultSet) {
    /**
     *  resultSet has a structure like:
     *  {
     *      "entities": [
     *          {
     *              "accountid": "119edfac-19c6-ea11-a81a-000d3af5e732",
     *              "name": "Test Account",
     *              "primarycontactid@odata.nextLink": {
     *                  "API": "{Xrm.Mobile.offline}.{retrieveRecord}",
     *                  "id": "119edfac-19c6-ea11-a81a-000d3af5e732",
     *                  "entityType": "account",
     *                  "options": "?$select=accountid&$expand=primarycontactid($select=contactid,fullname)&$getOnlyRelatedEntity=true"
     *              },
     *              "primarycontactid": {}
     *          }
     *      ]
     *  }
     *
     *  Notice the empty `primarycontactid` property but an additional `primarycontactid@odata.nextLink` 
     *  annotation that lets us know how to get to the linked data that we need.
     **/

    var promises = resultSet.entities.map(function(outerItem) {
        // We do a retrieveRecord() for every item in the result set of retrieveMultipleRecords() and then
        // combine the results into the retrieveMultipleRecords() result set itself.
       return Xrm.WebApi.offline.retrieveRecord(
           outerItem["primarycontactid@odata.nextLink"].entityType, 
           outerItem["primarycontactid@odata.nextLink"].id,
           outerItem["primarycontactid@odata.nextLink"].options
        ).then(function(innerResult) {            
            if (innerResult.value.length === 0) {
                return outerItem;
            }
            outerItem.primarycontactid = innerResult.value[0];
            return outerItem;
        });
    });

    return Promise.all(promises);
}).then(function(allResults) {
    for (var i = 0; i < allResults.length; i++) {
        console.log(allResults[i]);
    }
    // perform additional operations on retrieved records
}, function(error) {
    console.error(error);
    // handle error conditions
});
```

For more examples of retrieving multiple records using Web API, see [Query Data using the Web API](../../../../data-platform/webapi/query-data-web-api.md).

 
### Related topics

[Query Data using the Web API](../../../../data-platform/webapi/query-data-web-api.md)

[Xrm.WebApi.retrieveRecord](retrieveRecord.md)

[Xrm.WebApi](../xrm-webapi.md)






[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]