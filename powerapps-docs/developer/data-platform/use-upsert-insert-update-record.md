---
title: "Use Upsert to Create or Update a record (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "When loading data into Dataverse from an external system, you may not know if a record already exists in Dataverse and should be updated, or whether you must create a new record. Upsert is a combination of Update or Insert which enables the server to detect whether a record exists or not and apply the appropriate Update or Create operation in Dataverse. " # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 07/26/2022
ms.reviewer: pehecke
ms.topic: article
author: divka78 # GitHub ID
ms.subservice: dataverse-developer
ms.author: dikamath # MSFT alias of Microsoft employees only
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors:
  - PHecke
  - JimDaly
---
# Use Upsert to Create or Update a record

You can reduce the complexity involved with data integration scenarios by using the `Upsert` message. When loading data into Microsoft Dataverse from an external system, for example in a bulk data integration scenario, you may not know if a record already exists in Dataverse. In such cases you won't know if you should use the `Update` or a `Create` message. You must retrieve the record first to determine if it exists before performing the appropriate operation. You can reduce this complexity and load data into Dataverse more efficiently by using the `Upsert` message.

There is a performance penalty in using `Upsert` versus using `Create`. If you are sure the record doesn't exist, use `Create`.

> [!NOTE]
> While you can use primary key values with `Upsert`, it is generally expected that you will be using alternate keys because the common use case is data integration scenarios. More information: [Use an alternate key to reference a record](use-alternate-key-reference-record.md)


<a name="BKMK_upsert"></a>

## Understanding the Upsert process  

`Upsert` messages are processed on the server. The SDK for .NET classes use the objects used on the server. Therefore, the following explaination uses the SDK for .NET classes to describe how an <xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest> instance is processed what is returned by the <xref:Microsoft.Xrm.Sdk.Messages.UpsertResponse> instance.

The following steps describe the processing logic on the server when an <xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest> is received:  
  
1. The <xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest> instance arrives with the <xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest.Target?text=Target Property> set with an <xref:Microsoft.Xrm.Sdk.Entity> instance containing the data for a `Create` or `Update` operation.
   - The <xref:Microsoft.Xrm.Sdk.Entity> instance will typically have the <xref:Microsoft.Xrm.Sdk.Entity.KeyAttributes?text=Entity.KeyAttributes Property> set with values used to identify the record using alternate keys.
1. If it exists, Dataverse will try to look up the record using the <xref:Microsoft.Xrm.Sdk.Entity.Id?text=Entity.Id> property of the <xref:Microsoft.Xrm.Sdk.Entity> instance set to the <xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest.Target> property. Otherwise it will use the alternate key values from the <xref:Microsoft.Xrm.Sdk.Entity.KeyAttributes?text=Entity.KeyAttributes Property>.
1. **If the record exists:**
   1. Set the `Target` <xref:Microsoft.Xrm.Sdk.Entity.Id?text=Entity.Id> with the primary key value of the found record.  
   1. Remove any data from the `Target` <xref:Microsoft.Xrm.Sdk.Entity.Attributes?text=Entity.Attributes> collection that have use the same keys used in the `Target` <xref:Microsoft.Xrm.Sdk.Entity.KeyAttributes?text=Entity.KeyAttributes> collection.
   1. Call `Update`.  
   1. Set the <xref:Microsoft.Xrm.Sdk.Messages.UpsertResponse.RecordCreated?text=UpsertResponse.RecordCreated> property to `false`.  
   1. Create an <xref:Microsoft.Xrm.Sdk.EntityReference> from the `Target` entity as the value for <xref:Microsoft.Xrm.Sdk.Messages.UpsertResponse.Target?text=UpsertResponse.Target>.  
   1. Return the <xref:Microsoft.Xrm.Sdk.Messages.UpsertResponse>.  
1. **If the record doesn't exist:**  
   1. Copy any data from the `Target` <xref:Microsoft.Xrm.Sdk.Entity.KeyAttributes?text=Entity.KeyAttributes> that the `Target` *does not already have* in its <xref:Microsoft.Xrm.Sdk.Entity.Attributes?text=Entity.Attributes> collection into the `Target` <xref:Microsoft.Xrm.Sdk.Entity.Attributes?text=Entity.Attributes>.  
   1. Call `Create`.  
   1. Set the <xref:Microsoft.Xrm.Sdk.Messages.UpsertResponse.RecordCreated?text=UpsertResponse.RecordCreated> to `true`.  
   1. Create an <xref:Microsoft.Xrm.Sdk.EntityReference> from the `Target` entity and the `id` result of the `Create` operation as the value for <xref:Microsoft.Xrm.Sdk.Messages.UpsertResponse.Target?text=UpsertResponse.Target>.  
   1. Return the <xref:Microsoft.Xrm.Sdk.Messages.UpsertResponse>.  
  
The following diagram shows the process on the server when an <xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest> is received.  
  
:::image type="content" source="media/upsert-flowchart.png" alt-text="upsert process flow":::

## Guidance for composing requests

When using alternate keys to identify a record, including the alternate key data in the portion of the request that represents the data to be saved is not recommended or necessary.

#### [Web API](#tab/webapi)

If you are using the Web API and not familar with the SDK for .NET, the server-side process described above may be difficult to follow. The Web API doesn't have the same object model as the SDK objects used in the description and the diagram above, but the data can be mapped as shown in the table below.

|Web API|SDK|Description|
|---------|---------|---------|
|Key values in URL |<xref:Microsoft.Xrm.Sdk.Entity.KeyAttributes?text=Entity.KeyAttributes Property>|Contains the alternate key data to identify the record.|
|Body of request|The <xref:Microsoft.Xrm.Sdk.Entity> set to the <xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest.Target?text=UpsertRequest.Target Property>|Contains the data to use for `Create` or `Update`.|

Although these requests are processed on the server as described above, you can think of it this way:

- **If the record exists:** The data set in the body of the request for those alternate key values in the Url will be *removed*, so there is no point in including it. This ensures that you cannot update the alternate key values of a record when you are using those alternate key values to identify it. You can change alternate key values using the primary key or a different set of alternate keys.
- **If the record doesn't exist:** Any alternate key values set in the body of the request will be used to create the new record, *even if the data is different* than the values specified by the alternate keys in the Url. If there is no alternate key data in the body of the request, the alternate key data from the URL will be copied into the body of the request. To avoid a situation where the key values in the Url and the corresponding key values in the body don't match, it is best to not include them in the body at all.

#### [SDK for .NET](#tab/sdk)

- **If the record exists:** Any data in the <xref:Microsoft.Xrm.Sdk.Entity.Attributes?text=Entity.Attributes> collection of the <xref:Microsoft.Xrm.Sdk.Entity> instance set as the <xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest.Target?text=Target Property> that matches data found in the <xref:Microsoft.Xrm.Sdk.Entity.KeyAttributes?text=Entity.KeyAttributes Property> will be *removed*, so there is no point in including it. This ensures that you cannot update the alternate key values of a record when you are using those alternate key values to identify it. You can change alternate key values using the primary key or a different set of alternate keys.
- **If the record doesn't exist:** Any data in the <xref:Microsoft.Xrm.Sdk.Entity.Attributes?text=Entity.Attributes> collection of the <xref:Microsoft.Xrm.Sdk.Entity> instance set as the <xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest.Target?text=Target Property> that has the same keys as data found in the <xref:Microsoft.Xrm.Sdk.Entity.KeyAttributes?text=Entity.KeyAttributes Property> will be used to create the new record, *even if it the values are different* than the data in the <xref:Microsoft.Xrm.Sdk.Entity.KeyAttributes?text=Entity.KeyAttributes Property>. If there is no alternate key data in <xref:Microsoft.Xrm.Sdk.Entity.Attributes?text=Entity.Attributes> collection, the alternate key data from the <xref:Microsoft.Xrm.Sdk.Entity.KeyAttributes?text=Entity.KeyAttributes Property> will be copied into the <xref:Microsoft.Xrm.Sdk.Entity.Attributes?text=Entity.Attributes> collection. To avoid a situation where the values in the <xref:Microsoft.Xrm.Sdk.Entity.KeyAttributes?text=Entity.KeyAttributes> collection and the corresponding data in the <xref:Microsoft.Xrm.Sdk.Entity.Attributes?text=Entity.Attributes> collection doesn't match, it is best to not include this data in the <xref:Microsoft.Xrm.Sdk.Entity.Attributes?text=Entity.Attributes> at all.

---

## Using Web API

With the Web API the `Upsert` and `Update` messages are both initiated using http `PATCH` against a specified `EntitySet` resource identified by the keys in the Url.

The difference between `Upsert` and `Update` is defined by whether the `If-Match: *` request header is included. If the `If-Match: *` request header is included and no resource can be identified by the key values in the Url, the request will return a `404 Not Found` status code. The `If-Match: *` request header ensures that the `PATCH` request is an `Update` operation.

If the `If-Match: *` request header is not included, the `PATCH` request is treated like an `Upsert` and a new record will be created if no records matching the keys in the URL are found. However, unlike the SDK, the response will not tell you whether a record was created. The status response will be `204 No Content` in either case.

If you include a `Prefer: return=representation` request header the system will return a `201 Created` status for `Create`, and a `200 OK` status for `Update`. This adds an additional `Retrieve` operation so it has an impact on performance. If you use this option, make sure that the `$select` query option you add only includes the primary key value. More information:

- [Create with data returned](webapi/create-entity-web-api.md#create-with-data-returned)
- [Update with data returned](webapi/update-delete-entities-using-web-api.md#update-with-data-returned)

With a `PATCH` request you can also include the `If-None-Match: *`  request header to block an `Update` if you only want to create records. More information: [Limit upsert operations](webapi/perform-conditional-operations-using-web-api.md#limit-upsert-operations)

### Web API Sample code

The following examples show `Upsert` operations using a table with two alternate key columns:

#### Create with Upsert

This request creates a record.

**Request**

```http
PATCH [Organization Uri]/api/data/v9.2/example_records(example_key1=2,example_key2=2) HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
Content-Type: application/json

{ "example_name": "2:2" }
```

**Response**

```http
HTTP/1.1 204 No Content
OData-Version: 4.0
OData-EntityId: [Organization Uri]/api/data/v9.2/example_records(example_key1=2,example_key2=2)
```

#### Update with Upsert

This request updates the record created by the request above.

**Request**

```http
PATCH [Organization Uri]/api/data/v9.2/example_records(example_key1=2,example_key2=2) HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
Content-Type: application/json

{ "example_name": "2:2 Updated" }
```

**Response**

```http
HTTP/1.1 204 No Content
OData-Version: 4.0
OData-EntityId: [Organization Uri]/api/data/v9.2/example_records(example_key1=2,example_key2=2)
```

> [!NOTE]
> The response is identical for Create or Update operations.

#### Create with Upsert and and return=representation preference

When you use the `Prefer: return=representation` header you can get a different status code in the response to indicate whether the record was created or updated.

The following request creates a new record and returns status `201 Created`.

**Request**

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

**Response**

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

This request updates the record created by the request above and returns status `200 OK` to show that this was an update operation.

**Request**

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

**Response**

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


## Using the SDK for .NET

Your client application will use the <xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute%2A?text=IOrganizationService.Execute Method> with an <xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest> instance which has the <xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest.Target?text=Target Property> set with an <xref:Microsoft.Xrm.Sdk.Entity> instance containing the data for a `Create` or `Update` operation. The <xref:Microsoft.Xrm.Sdk.Entity> instance will typically have the <xref:Microsoft.Xrm.Sdk.Entity.KeyAttributes?text=Entity.KeyAttributes Property> set with values used to identify the record using alternate keys.

The <xref:Microsoft.Xrm.Sdk.Messages.UpsertResponse.RecordCreated?text=UpsertResponse.RecordCreated Property> tells you whether the record was created, and the <xref:Microsoft.Xrm.Sdk.Messages.UpsertResponse.Target?text=UpsertResponse.Target> contains a reference to the record that was created or updated.
  
<a name="BKMK_SampleCode"></a>

### SDK for .NET Sample code

The [SampleMethod.cs](https://github.com/microsoft/PowerApps-Samples/blob/master/cds/orgsvc/C%23/InsertRecordUsingUpsert/InsertRecordUsingUpsert/SampleMethod.cs) file in the [Insert record using Upsert](https://github.com/microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23/InsertRecordUsingUpsert/InsertRecordUsingUpsert) sample contains the following `ProcessUpsert` method to apply the `UpsertRequest` message on the contents of an XML file to create new records or update existing ones.  
  
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
