---
title: "Cache schema data (Microsoft Dataverse) | Microsoft Docs"
description: "Create a cache of schema definitions and track changes over time."
ms.date: 10/17/2022
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

The `RetrieveMetadataChangesResponse.ServerVersionStamp` property contains information about the point in time the request to `RetrieveMetadataChanges` occurred. You must take the `ServerVersionStamp` value from the previous response and use it as the value for the `RetrieveMetadataChangesRequest.ClientVersionStamp` when you send it again using the same query.

When you include the `ClientVersionStamp` property in the request, the `RetrieveMetadataChangesResponse.EntityMetadata` property returned will contain only the changed or added schema data since the previous request. You can add them to your cache.

If you also include the `DeletedMetadataFilters` parameter, any schema items deleted since the previous request will be included in the `RetrieveMetadataChangesResponse.DeletedMetadata` property. You can remove them from your cache.

This result should be much smaller and faster than executing the original query again.


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
   - [EntityMetadata](xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata): The table definition.
      - [EntityMetadata.Attributes[]](xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.Attributes)
         - [EnumAttributeMetadata](xref:Microsoft.Xrm.Sdk.Metadata.EnumAttributeMetadata): The base class for Choice columns.
            - [EnumAttributeMetadata.OptionSet](xref:Microsoft.Xrm.Sdk.Metadata.EnumAttributeMetadata.OptionSet)
               - [OptionSetMetadata](xref:Microsoft.Xrm.Sdk.Metadata.OptionSetMetadata): `HasChanged` will be true.
                  - [OptionSetMetadata.Options](xref:Microsoft.Xrm.Sdk.Metadata.OptionSetMetadata.Options): All options are returned.
                     - [OptionMetadata](xref:Microsoft.Xrm.Sdk.Metadata.OptionMetadata)
                        - [OptionMetadata.Color](xref:Microsoft.Xrm.Sdk.Metadata.OptionMetadata.Color): Only new option will have value, if set.
                        - [OptionMetadata.Label](xref:Microsoft.Xrm.Sdk.Metadata.OptionMetadata.Label): Only new option will have value.
                        - [OptionMetadata.Value](xref:Microsoft.Xrm.Sdk.Metadata.OptionMetadata.Value): Always has value.
                        - [OptionMetadata.HasChanged](xref:Microsoft.Xrm.Sdk.Metadata.MetadataBase.HasChanged): Value will be null.

You will know that the `EntityMetadata` and `EnumAttributeMetadata` have not changed because the `HasChanged` property will be false. Only the `OptionSetMetadata.HasChanged` property will be true. All the current valid options will be returned. The `OptionMetadata.HasChanged` property for all the options, including the new one, will be null.

Only the newly created option will include data for the `Label` property. The `OptionMetadata.HasChanged` property will be true only when one of it's properties (like `Color` or `Label`) changes.

#### [Web API](#tab/webapi)

- Collection([ComplexEntityMetadata](xref:Microsoft.Dynamics.CRM.ComplexEntityMetadata))
   - [ComplexEntityMetadata](xref:Microsoft.Dynamics.CRM.ComplexEntityMetadata): The table definition.
      - ComplexEntityMetadata.Attributes
         - [ComplexEnumAttributeMetadata](xref:Microsoft.Dynamics.CRM.ComplexEnumAttributeMetadata): The base class for Choice columns.
            - ComplexEnumAttributeMetadata.OptionSet
               - [ComplexOptionSetMetadata](xref:Microsoft.Dynamics.CRM.ComplexOptionSetMetadata): `HasChanged` will be true.
                  - ComplexOptionSetMetadata.Options : All options are returned.
                     - [OptionMetadata](xref:Microsoft.Dynamics.CRM.OptionMetadata)
                        - OptionMetadata.Color: Only new option will have value, if set.
                        - OptionMetadata.Label: Only new option will have value.
                        - OptionMetadata.Value: Always has value.
                        - OptionMetadata.HasChanged: Value will be null.

You will know that the `ComplexEntityMetadata` and `ComplexEnumAttributeMetadata` have not changed because the `HasChanged` property will be false. Only the `ComplexOptionSetMetadata.HasChanged` property will be true. All the current valid options will be returned. The `OptionMetadata.HasChanged` property for all the options, including the new one, will be null.

Only the newly created option will include data for the `Label` property. The `OptionMetadata.HasChanged` property will be true only when one of it's properties (like `Color` or `Label`) changes.

---

## Remove deleted items

When you include both `ClientVersionStamp` and `DeletedMetadataFilters` parameters for a `RetrieveMetadataChanges` message, the `RetrieveMetadataChangesResponse.DeletedMetadata` property will contain data about any deleted items. This property is a `DeletedMetadataCollection` that contains a set of `Keys` and `Values`. The keys are `DeletedMetadataFilters` enum values and you can use these to access a sub-set the deleted values.

> [!NOTE]
> The `DeletedMetadataFilters` parameter is optional and there is some performance impact when you include it because the data is retrieved from the database directly rather than from the internal cache. Use it only when you must detect deleted items and set the filter value to the minimum amount of data you need to have returned.

The deleted values are returned as a collection of `Guid` values. The values for deleted items is not filtered based on your query. There will be many `Guid` values which are not in your cache, but the `Guid` values for your cached item will be included. You must look for any matching `Guid` values and remove those items. Disregard any values that are not in your cache.

> [!NOTE]
> The definition of the Web API [DeletedMetadataFilters EnumType](xref:Microsoft.Dynamics.CRM.DeletedMetadataFilters) is slightly different from the SDK [DeletedMetadataFilters Enum](xref:Microsoft.Xrm.Sdk.Metadata.Query.DeletedMetadataFilters).
>
> The Web API [DeletedMetadataFilters EnumType](xref:Microsoft.Dynamics.CRM.DeletedMetadataFilters) doesn't have the `Entity` member. You must use `Default` instead.

### Tracking Deleted Options

Notice that the `DeletedMetadataFilters` enum contains a member for `OptionSet`, but not option. If any options are removed from a choice column, you will not find a reference to a specific option that was deleted. You will need to go to your cached options and compare them to the current options returned for that `OptionSet`.

### See also

[Web API Query schema definitions and detect changes Sample (C#)](webapi/samples/retrievemetadatachanges.md)<br />
[SDK for .NET Query schema definitions and detect changes Sample (C#)](org-service/samples/query-metadata-changes.md)<br />
[Query Schema Definitions](query-schema-definitions.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
