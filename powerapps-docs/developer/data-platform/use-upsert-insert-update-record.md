---
title: "Use Upsert to Create or Update a record (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "When loading data into Dataverse from an external system, you may not know if a record already exists in Dataverse and should be updated, or whether you must create a new record. Upsert is a combination of Update or Insert which enables the server to detect whether a record exists or not and apply the appropriate Update or Create operation in Dataverse. " # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 06/12/2022
ms.reviewer: pehecke
ms.topic: article
author: divka78 # GitHub ID
ms.subservice: dataverse-developer
ms.author: dikamath # MSFT alias of Microsoft employees only
manager: sunilg # MSFT alias of manager or PM counterpart
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

You can reduce the complexity involved with data integration scenarios by using the <xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest> message. When loading data into Microsoft Dataverse from an external system, for example in a bulk data integration scenario, you may not know if a record already exists in Dataverse. In such cases you won't know if you should call an <xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or a <xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> operation. This results in your querying for the record first to determine if it exists before performing the appropriate operation. You can reduce this complexity and load data into Dataverse more efficiently by using the `Upsert` message with the <xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest> class. 
  
<a name="BKMK_UsingUpsert"></a>   

## Using Upsert

It is best to use <xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest> only when you aren't sure if the record exists. That is, when you aren't sure if you should call a <xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or an <xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> operation. There is a performance decrease in using <xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest> versus using <xref:Microsoft.Xrm.Sdk.Messages.CreateRequest>. If you are sure the record doesn't exist, use <xref:Microsoft.Xrm.Sdk.Messages.CreateRequest>.  
  
The <xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest> includes a property named <xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest.Target>. This property contains the entity instance that will be used in an <xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or a <xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> operation. It also includes all the attributes required by the <xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> for the target entity so that the record can be created if it doesn't exist.  

Upsert is intended to be used to synchronize data from an external system. Unless the external system maintains a reference to the Dataverse primary key values, the Dataverse table will typically have alternate keys defined that store values that uniquely identify records in the external system and apply a unique constraint. When you define <xref:Microsoft.Xrm.Sdk.Entity> instances to use as the <xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest.Target> parameter, you will need to set the <xref:Microsoft.Xrm.Sdk.Entity.KeyAttributes> property with the alternate key values that uniquely identify the record instead of the primary key value. The <xref:Microsoft.Xrm.Sdk.Entity> class has two constructors that you can use to specify the key attributes.

If there is a single key attribute, you can use the [Entity(String, String, Object)](/dotnet/api/microsoft.xrm.sdk.entity.-ctor?view=dataverse-sdk-latest#microsoft-xrm-sdk-entity-ctor(system-string-system-string-system-object) constructor to specify a `keyName` and `keyValue`. This is shown in the sample below.

If there are multiple key attributes, define them using a <xref:Microsoft.Xrm.Sdk.KeyAttributeCollection> class and set them using the <xref:Microsoft.Xrm.Sdk.Entity(String,KeyAttributeCollection)?displayProperty=nameWithType> constructor.

After sending the request, you can inspect <xref:Microsoft.Xrm.Sdk.Messages.UpsertResponse.RecordCreated> to determine if the record was created. <xref:Microsoft.Xrm.Sdk.Messages.UpsertResponse.RecordCreated> will be true if the record didn't exist and was created. It will be false if the record already existed and was updated. <xref:Microsoft.Xrm.Sdk.Messages.UpsertResponse.Target> will be an `EntityReference` to the record that was found to exist or to the record that was created.  
  
To understand how <xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest> works, see the following section.  
  
<a name="BKMK_upsert"></a>

## Understanding the Upsert process  

 The following steps describe the processing logic when an <xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest> is received:  
  
1. Send <xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest> with enough data for a create or insert operation.  
  
2. Dataverse will look up the record targeted by the target entity.  
  
3. If the record exists:  
  
   1.  Set the ID property of the target entity with the ID of the found record.  
  
   2.  Remove any attributes from the Attributes collection that match the alternate keys set in the target.
  
   3. Call Update.  
  
   3.  Set the <xref:Microsoft.Xrm.Sdk.Messages.UpsertResponse.RecordCreated> to `false`.  
  
   4.  Create an <xref:Microsoft.Xrm.Sdk.EntityReference> from the target entity of the update as the value for <xref:Microsoft.Xrm.Sdk.Messages.UpsertResponse.Target>.  
  
   5.  Return the <xref:Microsoft.Xrm.Sdk.Messages.UpsertResponse>.  
  
4. If the record doesn't exist:  
  
   1.  Copy any alternate key values that the target does not already have in its attributes collection, into the target entity attributes.  
  
   2.  Call `Create`.  
  
   3.  Set the <xref:Microsoft.Xrm.Sdk.Messages.UpsertResponse.RecordCreated> to `true`.  
  
   4.  Create an <xref:Microsoft.Xrm.Sdk.EntityReference> from the target entity and the ID result of the `Create` request as the value for <xref:Microsoft.Xrm.Sdk.Messages.UpsertResponse.Target>.  
  
   5.  Return the <xref:Microsoft.Xrm.Sdk.Messages.UpsertResponse>.  
  
   The following illustration shows the process that unfolds when an <xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest> is received.  
  
   :::image type="content" source="media/upsert-flowchart.png" alt-text="upsert process flow":::
  
<a name="BKMK_SampleCode"></a>   

## Sample code

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
