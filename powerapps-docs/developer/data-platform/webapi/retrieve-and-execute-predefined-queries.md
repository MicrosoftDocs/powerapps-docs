---
title: "Retrieve and execute predefined queries (Microsoft Dataverse)| Microsoft Docs"
description: "Microsoft Dataverse provides a way for administrators to create system views that are available to all users. Read how you can use a predefined query to retrieve table data."
ms.date: 09/27/2022
author: MsSQLGirl
ms.author: jukoesma
ms.reviewer: jdaly
search.audienceType: 
  - developer
contributors: 
  - JimDaly
---

# Retrieve and execute predefined queries

Microsoft Dataverse provides a way for administrators to create system views that are available to all users. Individual users can save the Advanced Find queries for re-use in the application. Both of these represent predefined queries you can retrieve and execute using the Web API. 

> [!NOTE]
> Unlike queries using the OData syntax, data returned from pre-defined queries or fetchXml will not return properties with `null` values. When the value is `null`, the property will not be included in the results.

When a query is returned using OData syntax, a record will include a property with a `null` value like so:

```json
{
    "@odata.etag": "W/\"46849433\"",
    "name": "Contoso, Ltd. (sample)",
    "accountnumber": null,
    "accountid": "7a4814f9-b0b8-ea11-a812-000d3a122b89"
}
```

When retrieved using a pre-defined query or with FetchXml, the same record will not include the `accountnumber` property because it is `null`, like so:

```json
{
    "@odata.etag": "W/\"46849433\"",
    "name": "Contoso, Ltd. (sample)",
    "accountid": "7a4814f9-b0b8-ea11-a812-000d3a122b89"
}
```


<a name="bkmk_predefinedQueries"></a>

## Predefined queries

Dataverse allows you to define, save, and execute two types of queries as listed here.

|Query type|Description|
|----------------|-----------------|
|**Saved Query**|System-defined views for a table (entity). These views are stored in the <xref:Microsoft.Dynamics.CRM.savedquery?text=savedquery EntityType>. More information: [Customize table views](../../model-driven-apps/customize-entity-views.md)| 
|**User Query**|Advanced Find searches saved by users for a table (entity). These views are stored in the <xref:Microsoft.Dynamics.CRM.userquery?text=userquery EntityType>. More information: [UserQuery (saved view) table](../saved-queries.md)|

Records for both of these types of entities contain the FetchXML definition for the data to return. You can query the respective entity type to retrieve the primary key value. With the primary key value, you can execute the query by passing the primary key value. For example, to execute the **Active Accounts** saved query, you must first get the primary key using a query like this.

```http
GET [Organization URI]/api/data/v9.2/savedqueries?$select=name,savedqueryid&$filter=name eq 'Active Accounts'
```

You can then use the `savedqueryid` value and pass it as the value to the savedQuery parameter to the accounts entity set.

```http
GET [Organization URI]/api/data/v9.2/accounts?savedQuery=00000000-0000-0000-00aa-000010001002
```

Use the same approach to get the `userqueryid` and pass it as the value to the `userQuery` parameter to the entity set that matches the corresponding `returnedtypecode` of the saved query.

```http
GET [Organization URI]/api/data/v9.2/accounts?userQuery=121c6fd8-1975-e511-80d4-00155d2a68d1
```

### Apply a query to any collection of the appropriate type

In addition to simply applying the saved query to the main entity set collection, you can also use a saved query or user query to apply the same filtering on any collection of the appropriate type of entities. For example, if you want to apply a query against just the entities related to a specific entity, you can apply the same pattern. For example, the following URL will apply the **Open Opportunities** query against the opportunities related to a specific account via the `opportunity_parent_account` collection-valued navigation property.

```http
GET [Organization URI]/api/data/v9.2/accounts(8f390c24-9c72-e511-80d4-00155d2a68d1)/opportunity_parent_account/?savedQuery=00000000-0000-0000-00aa-000010003001
```
## See also

[Web API Query Data Sample (C#)](samples/webapiservice-query-data.md)<br />
[Web API Query Data Sample (Client-side JavaScript)](samples/query-data-client-side-javascript.md)<br />
[Perform operations using the Web API](perform-operations-web-api.md)<br />
[Compose Http requests and handle errors](compose-http-requests-handle-errors.md)<br />
[Query Data using the Web API](query/overview.md)<br />
[Create a table row using the Web API](create-entity-web-api.md)<br />
[Retrieve a table row using the Web API](retrieve-entity-using-web-api.md)<br />
[Update and delete table rows using the Web API](update-delete-entities-using-web-api.md)<br />
[Associate and disassociate table rows using the Web API](associate-disassociate-entities-using-web-api.md)<br />
[Use Web API functions](use-web-api-functions.md)<br />
[Use Web API actions](use-web-api-actions.md)<br />
[Execute batch operations using the Web API](execute-batch-operations-using-web-api.md)<br />
[Impersonate another user using the Web API](impersonate-another-user-web-api.md)<br />
[Perform conditional operations using the Web API](perform-conditional-operations-using-web-api.md)<br />

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
