---
title: "Cache schema data (Microsoft Dataverse) | Microsoft Docs"
description: "Create a cache of schema definitions and track changes over time."
ms.date: 10/12/2022
ms.topic: article
author: NHelgren
ms.subservice: dataverse-developer
ms.author: nhelgren
ms.reviewer: jdaly
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors:
 - JimDaly
---
# Cache Schema data

Some applications benefit from maintaining a persistent cache of schema definitions for a Dataverse organization. For example:

- Applications that need to work while disconnected from the Dataverse server
- Applications that are sensitive to limited network bandwidth, such as mobile applications

Dataverse has a lot of schema definition data, and few applications must track all of it. Limiting the amount of data to cache is essential.

The `RetrieveMetadataChanges` message provides two capabilities:

1. **Query**: Compose a single query to retrieve just the schema data you need. This is covered in [Query Schema Definitions](query-schema-definitions.md).
1. **Cache Management**: If you cache the schema definition data with your app, you can use `RetrieveMetadataChanges` to efficiently retrieve only the changes since your last query. Use the information about these changes to add or remove items in your cache. This may result in a significant improvement time for your application to start. This is the focus of this topic.

After you define a query for the schema data you want to cache, you can use additional capabilities of the `RetrieveMetadataChanges` message to create and maintain a cache of Dataverse schema data.

## Create a cache

As described in [Query Schema Definitions](query-schema-definitions.md), the first step is to create a query that defines the kind of schema information you are interested in.  Then use the `RetrieveMetadataChanges` message to execute that query and cache the schema definitions returned in your application. You should find a way to persist this data that is appropriate for the needs of your app. You might save it as a file that your application reads when it starts. You will also need to save data about the last time you ran the query.
Structure your cache in a way that makes sense for your application. To manage removal of deleted items, it is important that your cache use the `MetadataId` as a unique identifier. More information [Remove deleted items](#remove-deleted-items).

## Detect changes

There is no event available to detect when schema definition changes occur. Refreshing your cache should be driven by the needs of your application. This is typically when the application starts. But you might poll the system regularly if you want to detect changes over time.  Regardless of your strategy, it is important to keep track of the time you sent the previous request.

The `RetrieveMetadataChangesResponse` `ServerVersionStamp` property contains information about the point in time the call to `RetrieveMetadataChanges` occurred. You must take the `ServerVersionStamp` value from the previous response and use it as the value for the `RetrieveMetadataChangesRequest.ClientVersionStamp` when you call it again using the same query.

When you include the `ClientVersionStamp` property in the request, the `RetrieveMetadataChangesResponse.EntityMetadata` property returned will contain only the changed or added schema data since the previous call. See [Add changed items](#add-changed-items)

If you also include the `DeletedMetadataFilters` parameter, any schema items were deleted since the previous call, they will be included in the `RetrieveMetadataChangesResponse.DeletedMetadata` property. See [Remove deleted items](#remove-deleted-items)

This result should be much smaller and faster than executing the original query again.
To update your cache data, you need to add any new or changed items to your cache and remove any deleted items.


## Manage expired cache

Information about changes is stored for 90 days by default. This value is stored in the [Organization.ExpireSubscriptionsInDays](reference/entities/organization.md#BKMK_ExpireSubscriptionsInDays) property. If you send a request with a `ClientVersionStamp` value that is older than the setting value, Dataverse will return an `ExpiredVersionStamp` error (`0x80044352`). You should be prepared to handle this specific error and re-initialize your cache when it occurs.

> [!NOTE]
> You should be prepared to manage this error even if you think that your value will always be less than 90 days. This error will be thrown when any changes on the server affect accurately tracking deleted schema data. For example, changing the `Organization.ExpireSubscriptionsInDays` property will invalidate all previous `VersionStamp` values. Some of these changes may not be caused by actions you take, but could be triggered by system maintenance.


## Add changed items

Just as when you perform your initial query to initialize your cache, the `RetrieveMetadataChangesResponse.EntityMetadata` property returned for subsequent requests using `RetrieveMetadataChangesRequest.ClientVersionStamp` will include the full hierarchy of changed items.

Each item in the hierarchy has a nullable boolean `HasChanged` value. When this value is false, it means the current item hasn't changed but something below it in the hierarchy has changed. When the `HasChanged` value is true, it means the current item in the hierarchy has changed.

> [!NOTE]
> If you request `EntityMetadata.Privileges` in your query the privileges will always be returned, whether they have changed or not. Privileges typically don't change.

### Tracking Options

One area that may not seem intuitive is how options for choice columns are tracked. This is a good example to understand the `HasChanged` property.

When a new option is added to an choice column, the following data in the hierarchy will be returned with the `RetrieveMetadataChangesResponse.EntityMetadata` property:

#### [SDK for .NET](#tab/sdk)

- [EntityMetadataCollection](xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadataCollection)
   - [EntityMetadata](xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata)
      - [EntityMetadata.Attributes[]](xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.Attributes)
         - [EnumAttributeMetadata](xref:Microsoft.Xrm.Sdk.Metadata.EnumAttributeMetadata)
            - [EnumAttributeMetadata.OptionSet](xref:Microsoft.Xrm.Sdk.Metadata.EnumAttributeMetadata.OptionSet)
               - [OptionSetMetadata](xref:Microsoft.Xrm.Sdk.Metadata.OptionSetMetadata)
                  - [OptionSetMetadata.Options](xref:Microsoft.Xrm.Sdk.Metadata.OptionSetMetadata.Options)
                     - [OptionMetadata](xref:Microsoft.Xrm.Sdk.Metadata.OptionMetadata)
                        - [OptionMetadata.Color](xref:Microsoft.Xrm.Sdk.Metadata.OptionMetadata.Color)
                        - [OptionMetadata.Description](xref:Microsoft.Xrm.Sdk.Metadata.OptionMetadata.Description)
                        - [OptionMetadata.Label](xref:Microsoft.Xrm.Sdk.Metadata.OptionMetadata.Label)
                        - [OptionMetadata.Value](xref:Microsoft.Xrm.Sdk.Metadata.OptionMetadata.Value)
                        - [OptionMetadata.HasChanged](xref:Microsoft.Xrm.Sdk.Metadata.OptionMetadata.HasChanged)

#### [Web API](#tab/webapi)

---

You will know that the `EntityMetadata` and `EnumAttributeMetadata` have not changed because the `HasChanged` property will be false. Only the `OptionSetMetadata.HasChanged` property will be true. All the current valid options will be returned. The `OptionMetadata.HasChanged` property for all the options, including the new one, will be null.

Only the newly created option will include data for the `Label` property. The `OptionMetadata.HasChanged` property will be true only when one of it's properties (like `Color` or `Label`) changes.

## Remove deleted items

### See also

[Query Schema Definitions](query-schema-definitions.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
