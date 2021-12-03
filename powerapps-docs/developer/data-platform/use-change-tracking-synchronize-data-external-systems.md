---
title: "Use change tracking to synchronize data with external systems (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "The change tracking feature provides a way to keep the data synchronized in an efficient manner by detecting what data has changed since the data was initially extracted or last synchronized" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 03/24/2021
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "JimDaly" # GitHub ID
ms.subservice: dataverse-developer
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Use change tracking to synchronize data with external systems

[!INCLUDE[cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

The change tracking feature in Microsoft Dataverse provides a way to keep the data synchronized in an efficient manner by detecting what data has changed since the data was initially extracted or last synchronized. Previously, without this new feature, it was difficult to build a reliable and efficient mechanism to determine what records had changed in Dataverse. This article discusses how to retrieve changes for a table.  

## Enable change tracking for a table  

 Before retrieving the changes for a table, make sure that the change tracking feature is enabled for that table. This feature can be enabled by using the customization user interface (UI) or programmatically by setting the <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.ChangeTrackingEnabled> property to `True`. Annotation `Org.OData.Capabilities.V1.ChangeTracking` gets added to table sets that have change tracking enabled. To see annotations in table definitions, do 

 ```http 
 GET [Organization URI]/api/data/v9.0/$metadata?annotations=true
 ```
 Read more about metadata annotations on [Metadata annotations](webapi/web-api-types-operations.md#bkmk_metannot).
 
 For more information about using the customization user interface (UI), see [Enable change tracking to control data synchronization](/power-platform/admin/enable-change-tracking-control-data-synchronization).  
  

## Retrieve changes for a table using the Web API  

Changes made in tables can be tracked using Web API requests by adding `odata.track-changes` as a preference header. Preference header `odata.track-changes` is used to request that a *delta link* be returned which can subsequently be used to retrieve table changes.

Delta links are opaque, service-generated links that the client uses to retrieve subsequent changes to a result. They are based on a defining query that describes the set of results for which changes are being tracked; for example, the request that generated the results containing the delta link. The delta link encodes the collection of tables for which changes are being tracked, along with a starting point from which to track changes. Read more about delta links here [Oasis OData Version 4.0 - Delta Links](https://docs.oasis-open.org/odata/odata/v4.0/cs01/part1-protocol/odata-v4.0-cs01-part1-protocol.html#_Toc365046305)


## Retrieve changes in tables using Web API example

This example shows how to retrieve changes made in accounts data using the Web API.

Request
```http
GET [Organization URI]/api/data/v9.0/accounts?$select=name,accountnumber,telephone1,fax HTTP/1.1
Prefer: odata.track-changes
Cache-Control: no-cache
OData-Version: 4.0
Content-Type: application/json
```
Response
```json
{
  "@odata.context":"[Organization URI]/api/data/v9.0/$metadata#accounts(name,accountnumber,telephone1,fax)",
"@odata.deltaLink": "[Organization URI]/api/data/v9.0/accounts?$select=name,accountnumber,telephone1,fax&$deltatoken=919042%2108%2f22%2f2017%2008%3a10%3a44",
"value":[
           {
              "@odata.etag":"W/\"915244\"",
              "name":"Monte Orton",
              "accountnumber":null,
              "telephone1":"555000",
              "fax":"10101",
              "accountid":"60c4e274-0d87-e711-80e5-00155db19e6d"
           }
       ]
}
```
The delta link returned from the above example can be used to fetch changes in tables. In this example a new account was created and an existing account deleted. The delta link returned from the previous request fetches these changes, as shown in the example below.

Request
```http
GET [Organization URI]/api/data/v9.0/accounts?$select=name,accountnumber,telephone1,fax&$deltatoken=919042%2108%2f22%2f2017%2008%3a10%3a44
```
Response
```json
{
          "@odata.context":"[Organization URI]/data/v9.0/$metadata#accounts(name,telephone1,fax)/$delta",
          "@odata.deltaLink":"[Organization URI]/api/data/v9.0/accounts?$select=name,telephone1,fax&$deltatoken=919058%2108%2f22%2f2017%2008%3a21%3a20",
"value":
    [
        {
            "@odata.etag":"W/\"915244\"",
            "name":"Monte Orton",
            "telephone1":"555000",
            "fax":"10101",
            "accountid":"60c4e274-0d87-e711-80e5-00155db19e6d"
        },
        {
            "@odata.context":"[Organization URI]/api/data/v9.0/$metadata#accounts/$deletedEntity",
            "id":"2e451703-c686-e711-80e5-00155db19e6d",
            "reason":"deleted"
        }
    ]
}
```
The response for the delta link returned in the initial change tracking request contains another delta link. This delta link helps in retrieving all the subsequent changes in tables. An empty JSON response is returned if no table changes have occurred after the initial change tracking request was called.


## Retrieve count of the changes made in tables using Web API

`$count` can be added to the delta link returned from the initial change tracking request, as shown in the example below to get the number of changes made.

Request
```http
GET [Organization URI]/api/data/v9.0/accounts/$count?$deltatoken=919042%2108%2f22%2f2017%2008%3a10%3a44
```


## Query options not supported in Change Tracking Web API request

System query options `$filter`, `$orderby`, `$expand` and `$top` are not supported when using `odata.track-changes` as header in Web API request. An error message saying "The `$filter`/ `$orderby`/ `$expand` / `$top` query parameter isn't supported when Change Tracking is enabled." gets returned when using these query options in the Web API request.


## Retrieve changes for a table using the Organization Service

When change tracking is enabled for a table, you can use the <xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest> message to retrieve the changes for that table. The first time this message is used it returns all records for the table and that data can be used to populate the external storage. The message also returns a version number that will be sent back with the next use of the <xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest> message so that only data for those changes that occurred since that version will be returned.  
  
You should be aware of the following constraints when retrieving changes for a table:  
  
- Only one table will be tracked in retrieve changes. If retrieve changes is executed with no version / or token, the server will treat it as the system minimum version, returning all of the records as new. Deleted objects won’t be returned.  
  
- Changes will be returned if the last token is within a default value of 90 days. If it is more than 90 days, the system will return all the records.  
  
- If a client has a set of changes for a table, say version 1, a record is created and deleted prior to the next query for changes, they will get the deleted item even if they didn’t have the item to begin with.  
  
- Records are retrieved in the order determined by server side logic. Usually, the end user will always get all new or updated records first (sorted by version number) followed by deleted records.  If there are 3000 records created or updated and 2000 records deleted, Dataverse returns a collection of 5000 records, which have the first 3000 entries comprised of new or updated records and the last 2000 entries for deleted records.  
  
- If the new or updated item collection is greater than 5000, the user can page through the collection.  
  

## Sample code  
 The following code snippet shows how the `RetrieveEntityChangesRequest` message is used to retrieve the changes for a table. For the complete sample, see [Synchronize data with external systems using change tracking](https://github.com/microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23/Changetracking).  
  
```csharp
string token;

// Initialize page number.
int pageNumber = 1;
List<Entity> initialrecords = new List<Entity>();

// Retrieve records by using Change Tracking feature.
RetrieveEntityChangesRequest request = new RetrieveEntityChangesRequest();
request.EntityName = _customBooksEntityName.ToLower();
request.Columns = new ColumnSet("sample_bookcode", "sample_name", "sample_author");
request.PageInfo = new PagingInfo() { Count = 5000, PageNumber = 1, ReturnTotalRecordCount = false };


// Initial Synchronization. Retrieves all records as well as token value.
Console.WriteLine("Initial synchronization....retrieving all records.");
while (true)
{
    RetrieveEntityChangesResponse response = (RetrieveEntityChangesResponse)_serviceProxy.Execute(request);

    initialrecords.AddRange(response.EntityChanges.Changes.Select(x => (x as NewOrUpdatedItem).NewOrUpdatedEntity).ToArray());
    initialrecords.ForEach(x => Console.WriteLine("initial record id:{0}", x.Id));
    if (!response.EntityChanges.MoreRecords)
    {
        // Store token for later query
        token = response.EntityChanges.DataToken;
        break;

    }
    // Increment the page number to retrieve the next page.
    request.PageInfo.PageNumber++;
    // Set the paging cookie to the paging cookie returned from current results.
    request.PageInfo.PagingCookie = response.EntityChanges.PagingCookie;
}

```  
  
### See also  
 [Define alternate keys for a table](define-alternate-keys-entity.md)   
 [Using alternate keys](use-alternate-key-create-record.md)   
 [Update Dynamics 365 with external data using Upsert](use-upsert-insert-update-record.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
