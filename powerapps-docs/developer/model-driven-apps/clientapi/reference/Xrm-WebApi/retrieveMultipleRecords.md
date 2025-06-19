---
title: "retrieveMultipleRecords (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the retrieveMultipleRecords method.
author: sriharibs-msft
ms.author: srihas
ms.date: 04/29/2025
ms.reviewer: jdaly
ms.topic: reference
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# retrieveMultipleRecords (Client API reference)



[!INCLUDE[./includes/retrieveMultipleRecords-description.md](./includes/retrieveMultipleRecords-description.md)] 

## Syntax

`Xrm.WebApi.retrieveMultipleRecords(entityLogicalName, options, maxPageSize).then(successCallback, errorCallback);`

## Parameters

|Name|Type|Required|Description|
|---|---|---|---|
|`entityLogicalName`|String|Yes|The table logical name of the records you want to retrieve. For example: `account`.|
|`options`|String|No|OData system query options or FetchXML query to retrieve your data. See [Options](#options)|
|`maxPageSize`|Number|No|Specify a positive number that indicates the number of table records to be returned per page. If you don't specify this parameter, the value is defaulted to the maximum limit of 5,000 records for standard tables, 500 for elastic tables.<br /><br />If the number of records being retrieved is more than the specified `maxPageSize` value or the maximum limit for the table type, the `nextLink` column in the returned promise object will contain a link to retrieve records.|
|`successCallback`|Function|No|A function to call when table records are retrieved. See [Return Value](#return-value)|
|`errorCallback`|Function|No|[!INCLUDE [errorcallback-description](includes/errorcallback-description.md)]|

### Options

The following system query options are supported: `$select`, `$top`, `$filter`, `$expand`, and `$orderby`.

Use the `$expand` system query option to control what data from related tables is returned. If you just include the name of the navigation property, you'll receive all the properties for related records. You can limit the properties returned for related records using the `$select` system query option in parentheses after the navigation property name. Use this for both *single-valued* and *collection-valued* navigation properties. Note that for offline we only support nested `$select` option inside the `$expand`.

To specify a FetchXML query, use the `fetchXml` column to specify the query.

> [!NOTE]
> You must always use the `$select`system query option to limit the properties returned for a table record by including a comma-separated list of property names. This is an important performance best practice. If properties aren't specified using `$select`, all properties will be returned.

You specify the query options starting with `?`. You can also specify multiple system query options by using `&` to separate the query options.
  
When you specify an OData query string for the `options` parameter, the query **should be encoded** for special characters.

When you specify a FetchXML query for the `options` parameter, the query **should not be encoded**.

See [Examples](#examples) to see how you can define the `options` parameter for various retrieve multiple scenarios.
 
## Return Value

On success, returns a promise object to the `successCallback` with the following properties:

|Name|Type|Description|
|---|---|---|
|`entities`|Array of JSON objects|Each object represents the retrieved table record containing columns and their values as `key: value` pairs. The ID of the table record is retrieved by default|
|`nextLink`|String|(optional) If the number of records being retrieved is more than the value specified in the `maxPageSize` parameter in the request, this returns the URL to return the next page of records.|
|`fetchXmlPagingCookie`||(optional) For a fetchXml-based `retrieveMultipleRecords` operation with paging where the total record count is greater than the paging value, this attribute returns the paging cookie that can be used for a subsequent fetchXml operation to retrieve the next page of records.|

## Unsupported Attribute Types for OData query options in Mobile Offline

The following [Column types](../../../../data-platform/entity-attribute-metadata.md#column-types) aren't supported when doing a `Xrm.WebApi.retrieveMultipleRecords` operation with OData query string options (for example, `$select` and `$filter`) in mobile offline mode. You should use FetchXML if the attribute type you need to work with is in this list of unsupported attribute types.

- `MultiSelectPicklist`
- `File`
- `Image`
- `ManagedProperty`
- `CalendarRules`
- `PartyList`
- `Virtual`

## Unsupported features in Mobile Offline

The following features aren't supported in Mobile Offline:
- Grouping and Aggregation features

## Supported Filter Operations Per Attribute Type in Mobile Offline using FetchXML

The following operations are supported for all attribute types when working with FetchXML:
- Equals (`eq`)
- Not Equals (`neq`)
- Null (`null`)
- Not Null (`not-null`)

The following table lists more operations supported for each attribute type:


|Attribute Type|Supported Operations|
|---------|---------|
|BigInt, Decimal, Double, Integer|Greater Than (`gt`)<br />Greater Than or Equals (`gte`)<br />Less Than (`lt`)<br />Less Than or Equals (`lte`)|
|Boolean, Customer|In (`in`)<br />Not In (`not-in`)|
|EntityName, Picklist, State, Status|Like (`like`)<br />Not Like (`not-like`)<br />Begins With (`begins-with`)<br />Not Begin With (`not-begin-with`)<br />Ends With (`ends-with`)<br />Not End With (`not-end-with`)<br />In (`in`)<br />Not In (`not-in`)|
|Guid, Lookup|In (`in`)<br />Not In (`not-in`)<br />Equals User ID (`eq-userid`)<br />Not Equals User ID (`ne-userid`)|
|Money|Greater Than (`gt`)<br />Greater Than or Equals (`gte`)<br />Less Than (`lt`)<br />Less Than or Equals (`lte`)<br />In (`in`)<br />Not In (`not-in`)|
|Owner|In (`in`)<br />Not In (`not-in`)<br />Equals User ID (`eq-userid`)<br />Not Equals User ID (`ne-userid`)<br />Equals User Or Team (`eq-useroruserteams`)<br />|
|String|Like (`like`)<br />Not Like (`not-like`)<br />Begins With (`begins-with`)<br />Not Begin With (`not-begin-with`)<br />Ends With (`ends-with`)<br />Not End With (`not-end-with`)|
|DateTime|On Or After (`on-or-after`)<br />On (`on`)<br />On Or Before (`on-or-before`)<br />Today (`today`)<br />Tomorrow (`tomorrow`)<br />Yesterday (`yesterday`)<br />Next seven Days (`next-seven-days`)<br />Last seven Days (`last-seven-days`)<br />Next Week (`next-week`)<br />Last Week (`last-week`)<br />This Week (`this-week`)<br />Next Month (`next-month`)<br />Last Month (`last-month`)<br />This Month (`this-month`)<br />Next Year (`next-year`)<br />Last Year (`last-year`)<br />This Year (`this-year`)<br />Last X Days (`last-x-days`)<br />Next X Days (`next-x-days`)<br />Last X Weeks (`last-x-weeks`)<br />Next X Weeks (`next-x-weeks`)<br />Last X Months (`last-x-months`)<br />Next X Months (`next-x-months`)<br />Last X Years (`last-x-years`)<br />Next X Years (`next-x-years`)<br />Greater Than (`gt`)<br />Greater Than Or Equal (`gte`)<br />Less Than (`lt`)<br />Less Than Or Equal (`lte`)<br />|


## Examples

Most of the scenarios/examples mentioned in [Query Data using the Web API](../../../../data-platform/webapi/query/overview.md) can be achieved using the **retrieveMultipleRecords** method. Some of the examples are listed below.

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
For most single-valued navigation properties you'll find a computed, read-only property that uses the following naming convention: `_<name>_value` where the `<name>` is the name of the single-valued navigation property. For filtering purposes, the specific value of the single-valued navigation property can also be used.  However, for mobile clients in offline mode, these syntax options aren't supported, and the single-value navigation property name should be used for both retrieving and filtering. Also, the comparison of navigation properties to null isn't supported in offline mode.

More information: [Lookup properties](../../../../data-platform/webapi/web-api-properties.md#lookup-properties)

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

#### Using FetchXML to retrieve or filter by lookup properties (online and offline scenario)

You can use the `FetchXML` parameter while online or offline to retrieve the `name` and `primarycontactid` property for account records that have a primary contact that matches a condition:

```JavaScript
var fetchXml = `?fetchXml=
    <fetch mapping='logical'>
       <entity name='account'>
          <attribute name='name'/>
          <attribute name='primarycontactid'/>
          <link-entity name='contact' from='contactid' to='primarycontactid'>
             <filter type='and'>
                <condition attribute='lastname' operator='eq' value='Contoso'/>
             </filter>
          </link-entity>
       </entity>
    </fetch>`;

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

This example will display three records and a link to the next page. Here's an example output from the **Console** in the browser developer tools:

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

Use the query part in the URL in the `nextLink` property as the value for the `options` parameter in your subsequent **retrieveMultipleRecords** call to request the next set of records. Don't change or append any more system query options to the value. For every subsequent request for more pages, you should use the same `maxPageSize` value used in the original retrieve multiple request. Also, cache the results returned or the value of the nextLink property so that previously retrieved pages can be returned. 

For example, to get the next page of records, we'll pass in the query part of the `nextLink` URL to the `options` parameter:

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

This example will display three records and return a FetchXML Paging Cookie to the retrieve the results of the next page if there are more records belonging to the result set. Here's an example output from the **Console** in the browser developer tools:

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
  '<fetch><entity name="account"><attribute name="accountid"/><attribute name="name"/></entity></fetch>';

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

Use the **$expand** system query option in the navigation properties to control the data that is returned from related tables. The following example demonstrates how to retrieve the contact for all the account records. For the related contact records, we're only retrieving the `contactid` and `fullname`:

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
> [!NOTE] 
> Similar to the online scenario, use the **$expand** system query option to retrieve data from related tables in offline. However, many-to-many relationships are not supported in offline.

#### Deprecated method for mobile offline scenario

> [!NOTE] 
> The `@odata.nextLink` is deprecated for mobile offline scenarios. While it is still supported for existing customizations, it is not recommended to use it anymore.

An offline **\$expand** operation returns a `@odata.nextLink` annotation containing information on how to get to the related record's information. We use the `id`, `entityType`, and `options` parameter of that annotation to construct one or more additional `Xrm.WebApi.offline.retrieveRecord` request(s). The following piece of code provides a complete example of how to do this:

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

For more examples of retrieving multiple records using Web API, see [Query Data using the Web API](../../../../data-platform/webapi/query/overview.md).

 
### Related articles

[Query Data using the Web API](../../../../data-platform/webapi/query/overview.md)<br />
[Xrm.WebApi.retrieveRecord](retrieveRecord.md)<br />
[Xrm.WebApi](../xrm-webapi.md)






[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
