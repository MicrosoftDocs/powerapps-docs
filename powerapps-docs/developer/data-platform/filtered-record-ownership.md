---
title: Filtered record ownership with code (preview)
description: "Learn how to configure filtered record ownership by using the Dataverse SDK for .NET or Web API."
ms.date: 09/23/2026
ms.reviewer: jdaly
ms.topic: article
author: paulliew
ms.subservice: dataverse-developer
ms.author: paulliew
search.audienceType:
  - developer
---
# Filtered record ownership by using code (preview)

[!INCLUDE [preview-banner](../../../shared/preview-includes/preview-banner.md)]

Filtered record ownership provides row-level data access based on conditions that evaluate column values. This article explains how developers can configure record filters by using the Dataverse SDK for .NET or Web API.

You don't need to write code to use this feature. Before using the examples in this article, learn the important concepts and how to configure the feature with Power Apps in [Filtered record ownership](../../maker/data-platform/filtered-view-record-ownership.md).

## How filtered record ownership works

A record filter contains a FetchXML query that defines which rows a user can access. An entity record filter associates the record filter with the table that the query targets. A security role then grants access to the filtered rows for one or more operations.

The following tables store the configuration:

|Table|Purpose|
|---|---|
|[recordfilter entity type](xref:Microsoft.Dynamics.CRM.recordfilter)<br />[Record Filter table](reference/entities/recordfilter.md)|Stores the display name, unique name, and FetchXML query that defines a filter.|
|[entityrecordfilter entity type](xref:Microsoft.Dynamics.CRM.entityrecordfilter)<br />[EntityRecordFilter table](reference/entities/entityrecordfilter.md)|Associates a record filter with a Dataverse table.|

Filtered record ownership doesn't give a row an owner. Rows in a filtered record ownership table can't be assigned or shared. Access is the union of the filters granted through all security roles assigned to the user or their teams. The system administrator security role has the system-provided **All records** filter.

## Prerequisites

- A user with the system administrator security role must configure the feature and security roles.
- An unmanaged solution and its unique name. All solution components created by the examples are associated with this solution.
- Know the table and column logical names used in the FetchXML query. The examples use a custom table named `new_store` with a `new_city` column.

## Create a filtered record ownership table

Set the table `OwnershipType` property to the new `Filtered` member when you create the table. `Filtered` has the value `32` and specifies that the table doesn't have an owner and data access privileges are based on a filter. You can't change the ownership type after you create the table.

The following examples create the `new_Store` table and the `new_City` column used by the other examples in this article. Tables and columns are solution components, so the examples use the [SolutionUniqueName optional parameter](optional-parameters.md#associate-a-solution-component-with-a-solution) to associate them with an unmanaged solution when they're created.

### [SDK for .NET](#tab/sdk)

Set [EntityMetadata.OwnershipType](/dotnet/api/microsoft.xrm.sdk.metadata.entitymetadata.ownershiptype) to [OwnershipTypes](/dotnet/api/microsoft.xrm.sdk.metadata.ownershiptypes).`Filtered` in a [CreateEntityRequest](/dotnet/api/microsoft.xrm.sdk.messages.createentityrequest).

```csharp
var createTableRequest = new CreateEntityRequest
{
    SolutionUniqueName = "<Solution Unique Name>",
    Entity = new EntityMetadata
    {
        SchemaName = "new_Store",
        DisplayName = new Label("Store", 1033),
        DisplayCollectionName = new Label("Stores", 1033),
        Description = new Label("Stores organized by city.", 1033),
        OwnershipType = OwnershipTypes.Filtered,
        IsActivity = false
    },
    PrimaryAttribute = new StringAttributeMetadata
    {
        SchemaName = "new_Name",
        DisplayName = new Label("Name", 1033),
        RequiredLevel = new AttributeRequiredLevelManagedProperty(
            AttributeRequiredLevel.None),
        MaxLength = 100,
        FormatName = StringFormatName.Text
    }
};

service.Execute(createTableRequest);

var createCityColumnRequest = new CreateAttributeRequest
{
    SolutionUniqueName = "<Solution Unique Name>",
    EntityName = "new_store",
    Attribute = new StringAttributeMetadata
    {
        SchemaName = "new_City",
        DisplayName = new Label("City", 1033),
        RequiredLevel = new AttributeRequiredLevelManagedProperty(
            AttributeRequiredLevel.None),
        MaxLength = 100,
        FormatName = StringFormatName.Text
    }
};

service.Execute(createCityColumnRequest);
```

For more information, see [Create a custom table using the SDK for .NET](org-service/create-custom-entity.md).

### [Web API](#tab/webapi)

Set the [OwnershipTypes enum type](/power-apps/developer/data-platform/webapi/reference/ownershiptypes) value to `Filtered` in the [EntityMetadata entity type](/power-apps/developer/data-platform/webapi/reference/entitymetadata) definition. Include both the primary name column and the `new_City` column in the `Attributes` collection.

**Request**

```http
POST [Organization URI]/api/data/v9.2/EntityDefinitions HTTP/1.1
Accept: application/json
Content-Type: application/json; charset=utf-8
OData-MaxVersion: 4.0
OData-Version: 4.0
MSCRM.SolutionUniqueName: <Solution Unique Name>

{
  "@odata.type": "Microsoft.Dynamics.CRM.EntityMetadata",
  "SchemaName": "new_Store",
  "DisplayName": {
    "@odata.type": "Microsoft.Dynamics.CRM.Label",
    "LocalizedLabels": [
      {
        "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
        "Label": "Store",
        "LanguageCode": 1033
      }
    ]
  },
  "DisplayCollectionName": {
    "@odata.type": "Microsoft.Dynamics.CRM.Label",
    "LocalizedLabels": [
      {
        "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
        "Label": "Stores",
        "LanguageCode": 1033
      }
    ]
  },
  "Description": {
    "@odata.type": "Microsoft.Dynamics.CRM.Label",
    "LocalizedLabels": [
      {
        "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
        "Label": "Stores organized by city.",
        "LanguageCode": 1033
      }
    ]
  },
  "OwnershipType": "Filtered",
  "IsActivity": false,
  "HasActivities": false,
  "HasNotes": false,
  "Attributes": [
    {
      "@odata.type": "Microsoft.Dynamics.CRM.StringAttributeMetadata",
      "SchemaName": "new_Name",
      "DisplayName": {
        "@odata.type": "Microsoft.Dynamics.CRM.Label",
        "LocalizedLabels": [
          {
            "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
            "Label": "Name",
            "LanguageCode": 1033
          }
        ]
      },
      "IsPrimaryName": true,
      "RequiredLevel": { "Value": "None" },
      "MaxLength": 100,
      "FormatName": { "Value": "Text" }
    },
    {
      "@odata.type": "Microsoft.Dynamics.CRM.StringAttributeMetadata",
      "SchemaName": "new_City",
      "DisplayName": {
        "@odata.type": "Microsoft.Dynamics.CRM.Label",
        "LocalizedLabels": [
          {
            "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
            "Label": "City",
            "LanguageCode": 1033
          }
        ]
      },
      "RequiredLevel": { "Value": "None" },
      "MaxLength": 100,
      "FormatName": { "Value": "Text" }
    }
  ]
}
```

**Response**

```http
HTTP/1.1 204 No Content
OData-EntityId: [Organization URI]/api/data/v9.2/EntityDefinitions(00000000-0000-0000-0000-000000000003)
```

For more information, see [Create table definitions using the Web API](webapi/create-update-entity-definitions-using-web-api.md#create-table-definitions).

---

## Apply record filter to existing user or team and Organization record ownership tables 

While the record filter is the only row-level data access for the new **Filtered** record ownership table, the following record filter can also be used in existing user/team and organization record ownership tables.

## Create a record filter

The following examples create a record filter that selects rows where the `new_city` value is `Redmond`. The FetchXML root table must match the table you associate with the filter.

### [SDK for .NET](#tab/sdk)

Use a [CreateRequest](/dotnet/api/microsoft.xrm.sdk.messages.createrequest) so that you can set the `SolutionUniqueName` optional parameter when you create the `recordfilter` row.

```csharp
string fetchXml = """
    <fetch>
      <entity name="new_store">
        <filter type="and">
          <condition attribute="new_city" operator="eq" value="Redmond" />
        </filter>
      </entity>
    </fetch>
    """;

Entity recordFilter = new("recordfilter")
{
    ["displayname"] = "Stores in Redmond",
    ["uniquename"] = "new_storesinredmond",
    ["fetchxml"] = fetchXml
};

  CreateRequest createRecordFilterRequest = new()
  {
    Target = recordFilter
  };
  createRecordFilterRequest["SolutionUniqueName"] = "<Solution Unique Name>";

  CreateResponse createRecordFilterResponse =
    (CreateResponse)service.Execute(createRecordFilterRequest);
  Guid recordFilterId = createRecordFilterResponse.id;
```

### [Web API](#tab/webapi)

Create a `recordfilter` row. The `OData-EntityId` response header contains the ID of the new row.

**Request**

```http
POST [Organization URI]/api/data/v9.2/recordfilters HTTP/1.1
Accept: application/json
Content-Type: application/json; charset=utf-8
OData-MaxVersion: 4.0
OData-Version: 4.0
MSCRM.SolutionUniqueName: <Solution Unique Name>

{
  "displayname": "Stores in Redmond",
  "uniquename": "new_storesinredmond",
  "fetchxml": "<fetch><entity name=\"new_store\"><filter type=\"and\"><condition attribute=\"new_city\" operator=\"eq\" value=\"Redmond\" /></filter></entity></fetch>"
}
```

**Response**

```http
HTTP/1.1 204 No Content
OData-EntityId: [Organization URI]/api/data/v9.2/recordfilters(00000000-0000-0000-0000-000000000001)
```

---

## Associate the filter with a table

Create an entity record filter to associate the record filter with the table. Set `objecttypecode` to the table logical name and `recordfilterid` to the record filter you created in the previous step.

### [SDK for .NET](#tab/sdk)

```csharp
Entity entityRecordFilter = new("entityrecordfilter")
{
    ["name"] = "Stores in Redmond",
    ["objecttypecode"] = "new_store",
    ["recordfilterid"] = new EntityReference("recordfilter", recordFilterId)
};

  CreateRequest createEntityRecordFilterRequest = new()
  {
    Target = entityRecordFilter
  };
  createEntityRecordFilterRequest["SolutionUniqueName"] = "<Solution Unique Name>";

  CreateResponse createEntityRecordFilterResponse =
    (CreateResponse)service.Execute(createEntityRecordFilterRequest);
  Guid entityRecordFilterId = createEntityRecordFilterResponse.id;
```

### [Web API](#tab/webapi)

Use the `RecordFilterId` single-valued navigation property to associate the record filter.

**Request**

```http
POST [Organization URI]/api/data/v9.2/entityrecordfilters HTTP/1.1
Accept: application/json
Content-Type: application/json; charset=utf-8
OData-MaxVersion: 4.0
OData-Version: 4.0
MSCRM.SolutionUniqueName: <Solution Unique Name>

{
  "name": "Stores in Redmond",
  "objecttypecode": "new_store",
  "RecordFilterId@odata.bind": "/recordfilters(00000000-0000-0000-0000-000000000001)"
}
```

**Response**

```http
HTTP/1.1 204 No Content
OData-EntityId: [Organization URI]/api/data/v9.2/entityrecordfilters(00000000-0000-0000-0000-000000000002)
```

---

## Retrieve filters for a table

Retrieve the entity record filters for a table to inspect the active configuration. The following examples also return values from the related record filter.

### [SDK for .NET](#tab/sdk)

```csharp
QueryExpression query = new("entityrecordfilter")
{
    ColumnSet = new ColumnSet("name", "objecttypecode", "statecode"),
    Criteria = new FilterExpression(LogicalOperator.And)
    {
        Conditions =
        {
            new ConditionExpression("objecttypecode", ConditionOperator.Equal, "new_store"),
            new ConditionExpression("statecode", ConditionOperator.Equal, 0)
        }
    }
};

LinkEntity recordFilterLink = query.AddLink(
    "recordfilter",
    "recordfilterid",
    "recordfilterid");
recordFilterLink.EntityAlias = "recordfilter";
recordFilterLink.Columns = new ColumnSet("displayname", "uniquename", "fetchxml");

EntityCollection results = service.RetrieveMultiple(query);
```

### [Web API](#tab/webapi)

**Request**

```http
GET [Organization URI]/api/data/v9.2/entityrecordfilters?$select=name,objecttypecode,statecode&$filter=objecttypecode eq 'new_store' and statecode eq 0&$expand=RecordFilterId($select=displayname,uniquename,fetchxml) HTTP/1.1
Accept: application/json
OData-MaxVersion: 4.0
OData-Version: 4.0
```

**Response**

```http
HTTP/1.1 200 OK
Content-Type: application/json; odata.metadata=minimal
OData-Version: 4.0

{
  "value": [
    {
      "name": "Stores in Redmond",
      "objecttypecode": "new_store",
      "statecode": 0,
      "RecordFilterId": {
        "displayname": "Stores in Redmond",
        "uniquename": "new_storesinredmond",
        "fetchxml": "<fetch><entity name=\"new_store\"><filter type=\"and\"><condition attribute=\"new_city\" operator=\"eq\" value=\"Redmond\" /></filter></entity></fetch>"
      }
    }
  ]
}
```

---

## Grant access with security roles

After creating the record filter and entity record filter, grant the filter for the required **Create**, **Read**, **Write**, **Delete**, **Append**, or **Append to** table privileges in a security role. Assign the role to users or teams. For the configuration steps, see [Create and assign a security role](../../maker/data-platform/filtered-view-record-ownership.md#create-and-assign-a-security-role).

Filter access from all roles is cumulative. Test with a nonadministrator account because system administrators receive the **All records** filter and don't experience the same row restrictions.

## Manage filter records

Use the standard create, retrieve, update, and delete operations supported by the [Record Filter table](reference/entities/recordfilter.md) and [EntityRecordFilter table](reference/entities/entityrecordfilter.md). Deleting a record filter also deletes its associated entity record filters. Before changing or removing a filter, review every role that grants it to avoid unintended changes in data access.

## Limitations

For current limitations, including behavior for linked tables and Dataverse Search, see [Filtered record ownership limitations](../../maker/data-platform/filtered-view-record-ownership.md#limitations).

## Related articles

- [Filtered record ownership](../../maker/data-platform/filtered-view-record-ownership.md)
- [Use FetchXML to query data](fetchxml/overview.md)
- [Create a table row using the Web API](webapi/create-entity-web-api.md)
- [Create records using the SDK for .NET](org-service/entity-operations-create.md)
