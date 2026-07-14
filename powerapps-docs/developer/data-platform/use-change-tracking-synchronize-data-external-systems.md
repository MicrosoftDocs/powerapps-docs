---
title: "Use change tracking to synchronize data with external systems (Microsoft Dataverse) | Microsoft Docs"
description: "The change tracking feature provides a way to keep the data synchronized in an efficient manner by detecting what data has changed since the data was initially extracted or last synchronized."
ms.date: 03/31/2026
ms.reviewer: pehecke
ms.topic: how-to
author: paulliew
ms.subservice: dataverse-developer
ms.author: paulliew 
search.audienceType:
  - developer
contributors:
  - PHecke
  - JimDaly
---

# Use change tracking to synchronize data with external systems

The change tracking feature in Microsoft Dataverse provides a way to keep data synchronized efficiently by detecting what data changed since the data was initially extracted or last synchronized. This article discusses how to enable and retrieve changes for a table.

## Enable change tracking for a table

Before retrieving the changes for a table, make sure that change tracking is enabled for that table.

You can check whether this feature is enabled or enable it by using [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc). Select **Data** > **Tables** and the specific table. Under **Advanced options**, you find the **Track changes** property.

Set this property programmatically by setting the [EntityMetadata.ChangeTrackingEnabled Property](xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.ChangeTrackingEnabled) to `True`.

> [!NOTE]
> After you enable change tracking for a table, you can't disable it.

For more information about how to use [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), see [Create and edit tables using Power Apps](../../maker/data-platform/create-edit-entities-portal.md).

To check whether change tracking is enabled for a table by using the Dataverse Web API, use one of the following methods:

1. Query `EntityDefinitions` by using the following `GET` request:

   ```http
   GET [Organization URI]/api/data/v9.2/EntityDefinitions?$select=SchemaName&$filter=ChangeTrackingEnabled eq true
   ```

   Some system tables have change tracking enabled, such as [Auditing (Audit)](reference/entities/audit.md). To see the full list, use the following query:

   ```http
   GET [Organization URI]/api/data/v9.2/EntityDefinitions?$filter=ChangeTrackingEnabled eq true and IsCustomEntity eq false&$select=LogicalName
   ```

   For more information, see [Query table definitions using the Web API](webapi/query-metadata-web-api.md).

1. Check the Web API $metadata service document. The annotation `Org.OData.Capabilities.V1.ChangeTracking` is set for entity sets that have change tracking enabled.

   To see annotations in the Web API CDSL service document, use this Web API query:

   ```http
   GET [Organization URI]/api/data/v9.2/$metadata?annotations=true
   ```

   The entity sets that represent tables where change tracking is enabled have this annotation:

   ```xml
   <Annotation Term="Org.OData.Capabilities.V1.ChangeTracking">
      <Record>
            <PropertyValue Property="Supported" Bool="true" />
      </Record>
   </Annotation>
   ```

   For more information, see [Metadata annotations](webapi/web-api-service-documents.md#metadata-annotations).

### Tables not eligible for change tracking

You can't enable change tracking for some tables. To check if a table is eligible for change tracking, check the [EntityMetadata.CanChangeTrackingBeEnabled](xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.CanChangeTrackingBeEnabled) managed property value. To see which tables can't be enabled for change tracking, use this Web API query:

```http
GET [Organization URI]/api/data/v9.2/EntityDefinitions?$select=SchemaName,ChangeTrackingEnabled&$filter=ChangeTrackingEnabled eq false and CanChangeTrackingBeEnabled/Value eq false
```

More information:

- [Query table definitions using the Web API: Use complex types in $filter operations](webapi/query-metadata-web-api.md#use-complex-types-in-filter-operations)
- [Managed properties](/power-platform/alm/managed-properties-alm)

## Retrieve changes for a table using the Web API

You can track changes made in tables by using Web API requests that include the `Prefer: odata.track-changes` header. This header requests that a _delta link_ is returned, which you can later use to retrieve table changes.

Delta links are opaque, service-generated links that the client uses to retrieve subsequent changes to a result. They're based on a defining query that describes the set of results for which changes are being tracked. For example, the request that generated the results containing the delta link. The delta link encodes the collection of tables for which changes are being tracked, along with a starting point from which to track changes. For more information, see [Oasis OData Version 4.0 - Delta Links](https://docs.oasis-open.org/odata/odata/v4.0/cs01/part1-protocol/odata-v4.0-cs01-part1-protocol.html#_Toc365046305).

### Retrieve changes in tables using Web API example

This example shows how to retrieve changes made for the account table by using the Web API.

**Request:**

```http
GET [Organization URI]/api/data/v9.0/accounts?$select=name,accountnumber,telephone1,fax HTTP/1.1
Prefer: odata.track-changes
OData-Version: 4.0
Content-Type: application/json
```

**Response:**

```http
HTTP/1.1 200 OK
OData-Version: 4.0
Preference-Applied: odata.track-changes

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

Use the `@odata.deltaLink` URI returned from the preceding example to fetch changes in tables. In this example, you created a new account and deleted an existing account. The delta link returned from the previous request fetches these changes, as shown in the following example.

**Request:**

```http
GET [Organization URI]/api/data/v9.0/accounts?$select=name,accountnumber,telephone1,fax&$deltatoken=919042%2108%2f22%2f2017%2008%3a10%3a44
OData-Version: 4.0
Content-Type: application/json
```

**Response:**

```http
HTTP/1.1 200 OK
OData-Version: 4.0

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

The response for the delta link returned in the initial change tracking request contains another delta link. This delta link helps in retrieving all the subsequent changes in tables. If no table changes occur after the initial change tracking request, the response contains empty JSON.

### Retrieve count of the changes made in tables using Web API

To get the number of changes, add `$count` to the delta link returned from the initial change tracking request, as shown in the following example.

**Request:**

```http
GET [Organization URI]/api/data/v9.0/accounts/$count?$deltatoken=919042%2108%2f22%2f2017%2008%3a10%3a44
OData-Version: 4.0
Content-Type: application/json
```

### Query options not supported in Change Tracking Web API request

System query options `$filter`, `$orderby`, `$expand`, and `$top` aren't supported when you use the `Prefer: odata.track-changes` header in a Web API request. If you use these query options in the Web API request, you get an error message: `The \"${filter|orderby|expand|top}\" query parameter isn't supported when Change Tracking is enabled.`.

## Retrieve changes for a table using .NET SDK

When you enable change tracking for a table, use the `RetrieveEntityChanges` message with the [RetrieveEntityChangesRequest Class](xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest) to retrieve the changes for that table.

The first time you use this message, it returns all records for the table. You can use that data to populate the external storage. The message also returns a version number that you send back with the next use of the `RetrieveEntityChanges` message so that only data for those changes that occurred since that version is returned.

Be aware of the following constraints when retrieving changes for a table:

- You can track only one table in retrieve changes. If you execute `RetrieveEntityChanges` with no version or token, the server treats it as the system minimum version and returns all of the records as new. Deleted objects aren't returned.
- Changes are returned if the last token is within a default value of seven days. The value of the [Organization table ExpireChangeTrackingInDays column](reference/entities/organization.md#BKMK_ExpireChangeTrackingInDays) controls this duration and can be changed. If unprocessed changes are older than the configured value, the system throws an exception.
- If a client has a set of changes for a table, say version 1, a record is created and deleted before the next query for changes, the client gets the deleted item even if they didn't have the item to begin with.
- Records are retrieved in the order determined by server side logic. Usually, the caller gets all new or updated records first (sorted by version number) followed by deleted records. If there are 3,000 records created or updated and 2,000 records deleted, Dataverse returns a collection of 5,000 records for standard tables, which have the first 3,000 entries comprised of new or updated records and the last 2,000 entries for deleted records.
- If the new or updated item collection is greater than 5,000, the user can page through the collection.
- The calling user must have organization level read access to the table. If the user has limited read access, the system throws a privilege check error.

### .NET SDK sample code

The following code snippet shows how to use the `RetrieveEntityChanges` message to retrieve the changes for a table. For the complete sample, see [Synchronize data with external systems using change tracking](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/CSharp/Changetracking).

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

[Define alternate keys for a table](define-alternate-keys-entity.md)<br />
[Use an alternate key to reference a record](use-alternate-key-reference-record.md)<br />
[Update Dynamics 365 with external data using Upsert](use-upsert-insert-update-record.md)<br />
[Query table definitions using the Web API](webapi/query-metadata-web-api.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
