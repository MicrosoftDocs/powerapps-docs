---
title: "Use Upsert to Create or Update a Record in Dataverse"
description: "Learn how to use the Upsert message in Microsoft Dataverse to automatically create or update records during data integration. Simplify your bulk data loading workflows."
ms.date: 03/09/2026
ms.reviewer: pehecke
ms.topic: how-to
author: MsSQLGirl
ms.subservice: dataverse-developer
ms.author: jukoesma
search.audienceType:
  - developer
contributors:
  - PHecke
  - JimDaly
---

# Use Upsert to Create or Update a record

You can reduce the complexity of data integration scenarios by using the `Upsert` message. When you load data into Microsoft Dataverse from an external system, such as in a bulk data integration scenario, you might not know if a record already exists in Dataverse. In these cases, you can't decide whether to use the `Update` or `Create` message. You must first retrieve the record to check if it exists before performing the appropriate operation. You can reduce this complexity and load data into Dataverse more efficiently by using the `Upsert` message.

There's a performance penalty when you use `Upsert` instead of `Create`. If you're sure the record doesn't exist, use `Create`.

> [!NOTE]
> While you can use primary key values with `Upsert`, it's generally expected that you'll use alternate keys because the common use case is data integration scenarios. For more information, see [Use an alternate key to reference a record](use-alternate-key-reference-record.md).

## Elastic table upsert

Elastic table behavior for `Upsert` differs from standard tables. By using elastic tables, the `Upsert` operation doesn't call the `Create` or `Update` message depending on whether the record already exists. `Upsert` directly applies the changes in the entity.

- **If the record exists**: The operation overwrites all the data in the record with the data in the entity. There's no `Update` event.
- **If the record doesn't exist**: The operation creates a new record. There's no `Create` event.

This behavior affects where you apply business logic for events. You can create a new record by using either `Create` or `Upsert`. You can update a record by using either `Update` or `Upsert`. If you need to apply logic consistently for `Create` or `Update` in elastic tables, you must also include that logic in `Upsert`. For more information, see [Upsert a record in an elastic table](use-elastic-tables.md#upsert-a-record-in-an-elastic-table).

<a name="BKMK_upsert"></a>

## Understand the upsert process for standard tables

The server processes `upsert` messages. The SDK for .NET classes use the same objects as the server. Therefore, the following explanation uses the SDK for .NET classes to describe how the server processes an [UpsertRequest class](xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest) instance and returns an [UpsertResponse class](xref:Microsoft.Xrm.Sdk.Messages.UpsertResponse) instance.

The following steps describe the processing logic on the server when it receives an [UpsertRequest](xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest) for a standard table:

1. The [UpsertRequest](xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest) instance arrives with the [Target property](xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest.Target) set to an [Entity](xref:Microsoft.Xrm.Sdk.Entity) instance containing the data for a `Create` or `Update` operation.
      - The [Entity](xref:Microsoft.Xrm.Sdk.Entity) instance typically has the [Entity.KeyAttributes property](xref:Microsoft.Xrm.Sdk.Entity.KeyAttributes) set with values that identify the record by using alternate keys.
1. If it exists, Dataverse tries to look up the record by using the [Entity.Id](xref:Microsoft.Xrm.Sdk.Entity.Id) property of the [Entity](xref:Microsoft.Xrm.Sdk.Entity) instance set to the [Target](xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest.Target) property. Otherwise, it uses the alternate key values from the [Entity.KeyAttributes property](xref:Microsoft.Xrm.Sdk.Entity.KeyAttributes).
1. **If the record exists:**
   1. Set the `Target` [Entity.Id](xref:Microsoft.Xrm.Sdk.Entity.Id) to the primary key value of the found record.
   1. Remove any data from the `Target` [Entity.Attributes](xref:Microsoft.Xrm.Sdk.Entity.Attributes) collection that uses the same keys as the `Target` [Entity.KeyAttributes](xref:Microsoft.Xrm.Sdk.Entity.KeyAttributes) collection.
   1. Call `Update`.
   1. Set the [UpsertResponse.RecordCreated](xref:Microsoft.Xrm.Sdk.Messages.UpsertResponse.RecordCreated) property to `false`.
   1. Create an [EntityReference](xref:Microsoft.Xrm.Sdk.EntityReference) from the `Target` entity as the value for [UpsertResponse.Target](xref:Microsoft.Xrm.Sdk.Messages.UpsertResponse.Target).
   1. Return the [UpsertResponse](xref:Microsoft.Xrm.Sdk.Messages.UpsertResponse).
1. **If the record doesn't exist:**
   1. Copy any data from the `Target` [Entity.KeyAttributes](xref:Microsoft.Xrm.Sdk.Entity.KeyAttributes) that the `Target` _doesn't already have_ in its [Entity.Attributes](xref:Microsoft.Xrm.Sdk.Entity.Attributes) collection into the `Target` [Entity.Attributes](xref:Microsoft.Xrm.Sdk.Entity.Attributes).
   1. Call `Create`.
   1. Set the [UpsertResponse.RecordCreated](xref:Microsoft.Xrm.Sdk.Messages.UpsertResponse.RecordCreated) to `true`.
   1. Create an [EntityReference](xref:Microsoft.Xrm.Sdk.EntityReference) from the `Target` entity and the `id` result of the `Create` operation as the value for [UpsertResponse.Target](xref:Microsoft.Xrm.Sdk.Messages.UpsertResponse.Target).
   1. Return the [UpsertResponse](xref:Microsoft.Xrm.Sdk.Messages.UpsertResponse).

The following diagram shows the process on the server when it receives an [UpsertRequest](xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest).

:::image type="content" source="media/upsert-flowchart.png" alt-text="Screenshot of the upsert process flow for standard tables in Dataverse.":::

## Guidance for composing requests

When you use alternate keys to identify a record, don't include the alternate key data in the portion of the request that represents the data to save.

#### [Web API](#tab/webapi)

If you're using the Web API and aren't familiar with the SDK for .NET, the server-side process described earlier might be difficult to follow. The Web API doesn't have the same object model as the SDK objects used in the description and the diagram earlier, but you can map the data as shown in the following table.

| Web API | SDK | Description |
| --- | --- | --- |
| Key values in URL | [Entity.KeyAttributes property](xref:Microsoft.Xrm.Sdk.Entity.KeyAttributes) | Contains the alternate key data to identify the record. |
| Body of request | The [Entity](xref:Microsoft.Xrm.Sdk.Entity) set to the [UpsertRequest.Target property](xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest.Target) | Contains the data to use for `Create` or `Update`. |

Although the server processes these requests as described earlier, you can think of it this way:

- **If the record exists:** The server removes the data set in the body of the request for those alternate key values in the URL, so there's no point in including it. This practice ensures that you can't update the alternate key values of a record when you're using those alternate key values to identify it. You can change alternate key values by using the primary key or a different set of alternate keys.
- **If the record doesn't exist:** The server uses any alternate key values set in the body of the request to create the new record, _even if the data is different_ than the values specified by the alternate keys in the URL. If there's no alternate key data in the body of the request, the server copies the alternate key data from the URL into the body of the request. To avoid a situation where the key values in the URL and the corresponding key values in the body don't match, don't include them in the body.

#### [SDK for .NET](#tab/sdk)

- **If the record exists:** The server removes any data in the [Entity.Attributes](xref:Microsoft.Xrm.Sdk.Entity.Attributes) collection of the [Entity](xref:Microsoft.Xrm.Sdk.Entity) instance set as the [Target property](xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest.Target) that matches data found in the [Entity.KeyAttributes property](xref:Microsoft.Xrm.Sdk.Entity.KeyAttributes), so there's no point in including it. This practice ensures that you can't update the alternate key values of a record when you're using those alternate key values to identify it. You can change alternate key values by using the primary key or a different set of alternate keys.
- **If the record doesn't exist:** The server uses any data in the [Entity.Attributes](xref:Microsoft.Xrm.Sdk.Entity.Attributes) collection of the [Entity](xref:Microsoft.Xrm.Sdk.Entity) instance set as the [Target property](xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest.Target) that has the same keys as data found in the [Entity.KeyAttributes property](xref:Microsoft.Xrm.Sdk.Entity.KeyAttributes) to create the new record, _even if the values are different_ than the data in the [Entity.KeyAttributes property](xref:Microsoft.Xrm.Sdk.Entity.KeyAttributes). If there's no alternate key data in the [Entity.Attributes](xref:Microsoft.Xrm.Sdk.Entity.Attributes) collection, the server copies the alternate key data from the [Entity.KeyAttributes property](xref:Microsoft.Xrm.Sdk.Entity.KeyAttributes) into the [Entity.Attributes](xref:Microsoft.Xrm.Sdk.Entity.Attributes) collection. To avoid a situation where the values in the [Entity.KeyAttributes](xref:Microsoft.Xrm.Sdk.Entity.KeyAttributes) collection and the corresponding data in the [Entity.Attributes](xref:Microsoft.Xrm.Sdk.Entity.Attributes) collection doesn't match, don't include this data in the [Entity.Attributes](xref:Microsoft.Xrm.Sdk.Entity.Attributes).

---

## Use Web API

By using the Web API, you can initiate the `Upsert` and `Update` messages by sending an HTTP `PATCH` request to a specified `EntitySet` resource. The keys in the URL identify the resource.

The difference between `Upsert` and `Update` depends on whether you include the `If-Match: *` request header. If you include the `If-Match: *` request header and no resource matches the key values in the URL, the request returns a `404 Not Found` status code. The `If-Match: *` request header ensures that the `PATCH` request is an `Update` operation.

If you don't include the `If-Match: *` request header, the `PATCH` request is treated like an `Upsert`. The request creates a new record if it doesn't find any records matching the keys in the URL. However, unlike the SDK, the response doesn't tell you whether it created a record. The status response is `204 No Content` in either case.

If you include a `Prefer: return=representation` request header, the system returns a `201 Created` status for `Create`, and a `200 OK` status for `Update`. Adding this header adds an extra `Retrieve` operation, so it affects performance. If you use this option, make sure that the `$select` query option you add only includes the primary key value. For more information, see:

- [Create with data returned](webapi/create-entity-web-api.md#create-with-data-returned)
- [Update with data returned](webapi/update-delete-entities-using-web-api.md#update-with-data-returned)

By using a `PATCH` request, you can also include the `If-None-Match: *` request header to block an `Update` if you only want to create records. For more information, see [Limit upsert operations](webapi/perform-conditional-operations-using-web-api.md#limit-upsert-operations).

### Web API sample code

The following examples show `Upsert` operations by using a table with two alternate key columns:

#### Create with upsert

This request creates a record.

**Request:**

```http
PATCH [Organization Uri]/api/data/v9.2/example_records(example_key1=2,example_key2=2) HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
Content-Type: application/json

{ "example_name": "2:2" }
```

**Response:**

```http
HTTP/1.1 204 No Content
OData-Version: 4.0
OData-EntityId: [Organization Uri]/api/data/v9.2/example_records(example_key1=2,example_key2=2)
```

#### Update with upsert

This request updates the record created by the preceding request.

**Request:**

```http
PATCH [Organization Uri]/api/data/v9.2/example_records(example_key1=2,example_key2=2) HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
Content-Type: application/json

{ "example_name": "2:2 Updated" }
```

**Response:**

```http
HTTP/1.1 204 No Content
OData-Version: 4.0
OData-EntityId: [Organization Uri]/api/data/v9.2/example_records(example_key1=2,example_key2=2)
```

> [!NOTE]
> The response is identical for Create or Update operations.

#### Create with upsert and return=representation preference

When you use the `Prefer: return=representation` header, you can get a different status code in the response to indicate whether the record was created or updated.

The following request creates a new record and returns status `201 Created`.

**Request:**

```http
PATCH [Organization Uri]/api/data/v9.2/example_records(example_key1=3,example_key2=3)?$select=example_recordid HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
Prefer: return=representation
Content-Type: application/json

{ "example_name": "3:3" }
```

**Response:**

```http
HTTP/1.1 201 Created
Content-Type: application/json; odata.metadata=minimal
ETag: W/"71004878"
Preference-Applied: return=representation
OData-Version: 4.0

{
  "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#example_records(example_recordid)/$entity",
  "@odata.etag": "W/\"71004878\"",
  "example_recordid": "ef0d112e-d70e-ed11-82e5-00224822577b"
}
```

#### Update with Upsert and return=representation preference

This request updates the record created by the preceding request and returns status `200 OK` to show that this was an update operation.

**Request:**

```http
PATCH [Organization Uri]/api/data/v9.2/example_records(example_key1=3,example_key2=3)?$select=example_recordid HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
Prefer: return=representation
Content-Type: application/json

{ "example_name": "3:3 Updated" }
```

**Response:**

```http
HTTP/1.1 200 OK
Content-Type: application/json; odata.metadata=minimal
ETag: W/"71004880"
OData-Version: 4.0

{
  "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#example_records(example_recordid)/$entity",
  "@odata.etag": "W/\"71004880\"",
  "example_recordid": "ef0d112e-d70e-ed11-82e5-00224822577b"
}
```

## Use the SDK for .NET

Your client application uses the [IOrganizationService.Execute Method](xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute%2A) with an [UpsertRequest](xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest) instance that has the [Target property](xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest.Target) set with an [Entity](xref:Microsoft.Xrm.Sdk.Entity) instance containing the data for a `Create` or `Update` operation. Typically, you set the [Entity.KeyAttributes property](xref:Microsoft.Xrm.Sdk.Entity.KeyAttributes) on the [Entity](xref:Microsoft.Xrm.Sdk.Entity) instance with values used to identify the record by using alternate keys.

The [UpsertResponse.RecordCreated property](xref:Microsoft.Xrm.Sdk.Messages.UpsertResponse.RecordCreated) tells you whether the record was created, and the [UpsertResponse.Target](xref:Microsoft.Xrm.Sdk.Messages.UpsertResponse.Target) contains a reference to the record that was created or updated.

<a name="BKMK_SampleCode"></a>

### SDK for .NET sample code

The [SampleMethod.cs](https://github.com/microsoft/PowerApps-Samples/blob/9a95523fdd33574fe2e60624d43b1bba5c6be155/dataverse/orgsvc/CSharp/InsertRecordUsingUpsert/InsertRecordUsingUpsert/SampleMethod.cs#L145-L190) file in the [Insert record using Upsert](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/CSharp/InsertRecordUsingUpsert/InsertRecordUsingUpsert) sample contains the following `ProcessUpsert` method. This method applies the `UpsertRequest` message on the contents of an XML file to create new records or update existing ones.

```csharp
public static void ProcessUpsert(CrmServiceClient service, String Filename)
{
    Console.WriteLine("Executing upsert operation.....");
    XmlTextReader tr = new XmlTextReader(Filename);
    XmlDocument xdoc = new XmlDocument();
    xdoc.Load(tr);
    XmlNodeList xnlNodes = xdoc.DocumentElement.SelectNodes("/products/product");

    foreach (XmlNode xndNode in xnlNodes)
    {
        String productCode = xndNode.SelectSingleNode("Code").InnerText;
        String productName = xndNode.SelectSingleNode("Name").InnerText;
        String productCategory = xndNode.SelectSingleNode("Category").InnerText;
        String productMake = xndNode.SelectSingleNode("Make").InnerText;

        //use alternate key for product
        Entity productToCreate = new Entity("sample_product", "sample_productcode", productCode);

        productToCreate["sample_name"] = productName;
        productToCreate["sample_category"] = productCategory;
        productToCreate["sample_make"] = productMake;
        var request = new UpsertRequest()
        {
            Target = productToCreate
        };

        try
        {
            // Execute UpsertRequest and obtain UpsertResponse.
            var response = (UpsertResponse)service.Execute(request);
            if (response.RecordCreated)
                Console.WriteLine("New record {0} is created!", productName);
            else
                Console.WriteLine("Existing record {0} is updated!", productName);
        }

        // Catch any service fault exceptions that Dataverse throws.
        catch (FaultException<Microsoft.Xrm.Sdk.OrganizationServiceFault>)
        {
            throw;
        }
    }
}
```

### See also

[Use change tracking to synchronize data with external systems](use-change-tracking-synchronize-data-external-systems.md)  
[Define alternate keys for a table](define-alternate-keys-entity.md)  
[Use an alternate key to reference a record](use-alternate-key-reference-record.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
