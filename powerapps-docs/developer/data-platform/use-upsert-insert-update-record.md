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

`Upsert` messages are processed on the server. The SDK for .NET classes are proxies for server-side objects. Therefore, the following explaination uses the SDK for .NET classes to describe how an <xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest> instance is processed what is returned by the <xref:Microsoft.Xrm.Sdk.Messages.UpsertResponse> instance.

> [!IMPORTANT]
> Even if you are using Web API, it is important to understand this process. For more information, see [Using Web API](#using-web-api) below.

The following steps describe the processing logic when an <xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest> is received:  
  
1. Send an <xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest> instance with the <xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest.Target?text=Target Property> set with the <xref:Microsoft.Xrm.Sdk.Entity> instance containing the data for a `Create` or `Update` operation.
   - The <xref:Microsoft.Xrm.Sdk.Entity> instance will typically have the <xref:Microsoft.Xrm.Sdk.Entity.KeyAttributes?text=Entity.KeyAttributes Property> set with values used to identify the record using alternate keys.
1. Dataverse will look up the record using the <xref:Microsoft.Xrm.Sdk.Entity.KeyAttributes?text=Entity.KeyAttributes Property> or the primary key value of the <xref:Microsoft.Xrm.Sdk.Entity> instance set to the <xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest.Target> property.  
1. **If the record exists:**
   1. Set the `Target` <xref:Microsoft.Xrm.Sdk.Entity.Id?text=Entity.Id> with the Id of the found record.  
   1. Remove any data from the `Target` <xref:Microsoft.Xrm.Sdk.Entity.Attributes?text=Entity.Attributes> collection that match the alternate keys set in the `Target`.
   1. Call `Update`.  
   1. Set the <xref:Microsoft.Xrm.Sdk.Messages.UpsertResponse.RecordCreated?text=UpsertResponse.RecordCreated> property to `false`.  
   1. Create an <xref:Microsoft.Xrm.Sdk.EntityReference> from the `Target` entity as the value for <xref:Microsoft.Xrm.Sdk.Messages.UpsertResponse.Target?text=UpsertResponse.Target>.  
   1. Return the <xref:Microsoft.Xrm.Sdk.Messages.UpsertResponse>.  
1. **If the record doesn't exist:**  
   1. Copy any alternate key values from the `Target` <xref:Microsoft.Xrm.Sdk.Entity.KeyAttributes?text=Entity.KeyAttributes> that the `Target` *does not already have* in its <xref:Microsoft.Xrm.Sdk.Entity.Attributes?text=Entity.Attributes> collection into the `Target` <xref:Microsoft.Xrm.Sdk.Entity.Attributes?text=Entity.Attributes>.  
   1. Call `Create`.  
   1. Set the <xref:Microsoft.Xrm.Sdk.Messages.UpsertResponse.RecordCreated?text=UpsertResponse.RecordCreated> to `true`.  
   1. Create an <xref:Microsoft.Xrm.Sdk.EntityReference> from the `Target` entity and the `id` result of the `Create` operation as the value for <xref:Microsoft.Xrm.Sdk.Messages.UpsertResponse.Target?text=UpsertResponse.Target>.  
   1. Return the <xref:Microsoft.Xrm.Sdk.Messages.UpsertResponse>.  
  
The following illustration shows the process that unfolds when an <xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest> is received.  
  
:::image type="content" source="media/upsert-flowchart.png" alt-text="upsert process flow":::

## Using Web API

Web API doesn't have the same object model as the SDK objects used in the description and the diagram above, but the data can be mapped as shown in the table below.

|Web API|SDK|Description|
|---------|---------|---------|
|Key values in URL |<xref:Microsoft.Xrm.Sdk.Entity.KeyAttributes?text=Entity.KeyAttributes Property>|Contains the alternate key data to identify the record.|
|Body of request|The <xref:Microsoft.Xrm.Sdk.Entity> set to the <xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest.Target?text=UpsertRequest.Target Property>|Contains the data to use for `Create` or `Update`.|

If you are using alternate keys, we recommend not including those key values in the body of the request. You can think of it this way:

- **If the record exists:** The data set in the body of the request for those alternate key values in the Url will be *removed*. This ensures that you cannot update the alternate key values of a record when you are using those alternate key values to identify it.
- **If the record doesn't exist:** Any alternate key data set in the body of the request will be used to create the new record, *even if it is different* than the data specified by the alternate keys in the Url. If there is no alternate key data in the body of the request, the alternate key data from the URL will be copied into the body of the request. To avoid a situation where the URL alternate key data and the corresponding alternate key data in the body doesn't match, it is best to not include it in the body at all. 

In both of these cases, alternate key data in the body of the request that corresponds to alternate key data in the Url isn't necessary because the alternate key data in the Url will be used.

### Detect when a record is created

With the Web API the `Upsert` and `Update` messages are both initiated using http `PATCH` against a specified entity set resource identified by the keys in the Url.

The difference is defined by whether the `If-Match: *` request header is included. If the `If-Match: *` request header is included and no resource can be identified by the key values in the Url, the request will return a `404 Not Found` status code. The inclusion of the `If-Match: *` request header ensures that the `PATCH` request is an `Update` operation.

If the `If-Match: *` request header is not included, the `PATCH` request is treated like an `Upsert` and a new record will be created if no records matching the keys in the URL are found. However, unlike the SDK, the response will not tell you whether a record was created. The status response will be `204 No Content` in either case.

If you include a `Prefer: return=representation` request header the system will return a `201 Created` status for `Create`, and a `200 OK` status for `Update`. This adds an additional `Retrieve` operation so it has an impact on performance. If you use this option, make sure that the `$select` query option you add only includes the primary key value. More information:

- [Create with data returned](webapi/create-entity-web-api.md#create-with-data-returned)
- [Update with data returned](webapi/update-delete-entities-using-web-api.md#update-with-data-returned)

With a `PATCH` request you can also include the `If-None-Match: *`  request header to block an `Update` if you only want to create records. More information: [Limit upsert operations](webapi/perform-conditional-operations-using-web-api.md#limit-upsert-operations)


<a name="BKMK_UsingUpsert"></a>

## Using SDK for .NET

It is best to use <xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest> only when you aren't sure if the record exists. That is, when you aren't sure if you should call a <xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or an <xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> operation. There is a performance decrease in using <xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest> versus using <xref:Microsoft.Xrm.Sdk.Messages.CreateRequest>. If you are sure the record doesn't exist, use <xref:Microsoft.Xrm.Sdk.Messages.CreateRequest>.  
  
The <xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest> includes a property named <xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest.Target>. This property contains the entity instance that will be used in an <xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or a <xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> operation. It also includes all the attributes required by the <xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> for the target entity so that the record can be created if it doesn't exist.  

Upsert is intended to be used to synchronize data from an external system. Unless the external system maintains a reference to the Dataverse primary key values, the Dataverse table will typically have alternate keys defined that store values that uniquely identify records in the external system and apply a unique constraint. When you define <xref:Microsoft.Xrm.Sdk.Entity> instances to use as the <xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest.Target> parameter, you will need to set the <xref:Microsoft.Xrm.Sdk.Entity.KeyAttributes> property with the alternate key values that uniquely identify the record instead of the primary key value. The <xref:Microsoft.Xrm.Sdk.Entity> class has two constructors that you can use to specify the key attributes.

If there is a single key attribute, you can use the [Entity(String, String, Object)](/dotnet/api/microsoft.xrm.sdk.entity.-ctor#microsoft-xrm-sdk-entity-ctor(system-string-system-string-system-object)) constructor to specify a `keyName` and `keyValue`. This is shown in the sample below.

If there are multiple key attributes, define them using a <xref:Microsoft.Xrm.Sdk.KeyAttributeCollection> class and set them using the [Entity(String, KeyAttributeCollection)](/dotnet/api/microsoft.xrm.sdk.entity.-ctor#microsoft-xrm-sdk-entity-ctor(system-string-microsoft-xrm-sdk-keyattributecollection))  constructor.

After sending the request, you can inspect <xref:Microsoft.Xrm.Sdk.Messages.UpsertResponse.RecordCreated> to determine if the record was created. <xref:Microsoft.Xrm.Sdk.Messages.UpsertResponse.RecordCreated> will be true if the record didn't exist and was created. It will be false if the record already existed and was updated. <xref:Microsoft.Xrm.Sdk.Messages.UpsertResponse.Target> will be an `EntityReference` to the record that was found to exist or to the record that was created.  
  
To understand how <xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest> works, see the following section.  
  



  
<a name="BKMK_SampleCode"></a>

### Sample code

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

        // Catch any service fault exceptions that Microsoft Dynamics CRM throws.
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
