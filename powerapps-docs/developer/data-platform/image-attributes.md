---
title: "Image columns (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn about how to create image columns using the Dataverse APIS" # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 01/11/2023
ms.reviewer: jdaly
ms.topic: article
author: NHelgren # GitHub ID
ms.subservice: dataverse-developer
ms.author: nhelgren # MSFT alias of Microsoft employees only
search.audienceType: 
  - developer
contributors:
 - JimDaly
---
# Image columns

Use image columns to store image data. A custom or customizable table can have zero or more image columns. This article is about working with column definitions in code. To use data stored in these columns, see [Use image column data](image-column-data.md).

## Create image columns

The recommended way to create image columns is to use [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) and define your columns using the designer. More information: [Image columns](../../maker/data-platform/types-of-fields.md#image-columns).

You can also create image columns using the Dataverse SDK for .NET or using the Web API. The following examples show how:

#### [SDK for .NET](#tab/sdk)

Use the [ImageAttributeMetadata Class](xref:Microsoft.Xrm.Sdk.Metadata.ImageAttributeMetadata) with the [CreateAttributeRequest Class](xref:Microsoft.Xrm.Sdk.Messages.CreateAttributeRequest) to create an image column.


```csharp
public static void CreateImageColumn(IOrganizationService service, string entityLogicalName, string imageColumnSchemaName) {

    ImageAttributeMetadata imageColumn = new()
    {
        SchemaName = imageColumnSchemaName,
        DisplayName = new Label("Sample Image Column", 1033),
        RequiredLevel = new AttributeRequiredLevelManagedProperty(
                AttributeRequiredLevel.None),
        Description = new Label("Sample Image Column for ImageOperation samples", 1033),
        MaxSizeInKB = 30 * 1024, // 30 MB
        CanStoreFullImage = true

    };

    CreateAttributeRequest createimageColumnRequest = new() {
        EntityName = entityLogicalName,
        Attribute = imageColumn                   
    };

    service.Execute(createimageColumnRequest);

}
```

More information:

- [What is the Organization service](org-service/overview.md)
- [IOrganizationService.Execute](xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute*)

#### [Web API](#tab/webapi)

POST a [ImageAttributeMetadata EntityType](xref:Microsoft.Dynamics.CRM.ImageAttributeMetadata) to the `Attributes` collection for the table.

**Request:**

```http
POST [Organization Uri]/api/data/v9.2/EntityDefinitions(LogicalName='account')/Attributes HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
Content-Type: application/json; charset=utf-8
Content-Length: 1393

{
  "@odata.type": "Microsoft.Dynamics.CRM.ImageAttributeMetadata",
  "AttributeTypeName": {
    "Value": "ImageType"
  },
  "SchemaName": "sample_ImageColumn",
  "MaxSizeInKB": 30720,
  "CanStoreFullImage": true,
  "Description": {
    "@odata.type": "Microsoft.Dynamics.CRM.Label",
    "LocalizedLabels": [
      {
        "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
        "Label": "Sample Image Column for ImageOperation samples",
        "LanguageCode": 1033,
        "IsManaged": false
      }
    ]
  },
  "DisplayName": {
    "@odata.type": "Microsoft.Dynamics.CRM.Label",
    "LocalizedLabels": [
      {
        "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
        "Label": "Sample Image Column",
        "LanguageCode": 1033,
        "IsManaged": false
      }
    ]
  }
}
```

**Response:**

```http
HTTP/1.1 204 NoContent
OData-Version: 4.0
OData-EntityId: [Organization Uri]/api/data/v9.2/EntityDefinitions(LogicalName='account')/Attributes(9554c5f9-8c51-ed11-bba1-000d3a9933c9)
```

More information:

- [Create and update table definitions using the Web API](webapi/create-update-entity-definitions-using-web-api.md)
- [Web API Metadata Operations Sample (C#)](webapi/samples/webapiservice-metadata-operations.md)

---

## Update image columns

In addition to the properties inherited from the [AttributeMetadata class](xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata) | [AttributeMetadata EntityType](xref:Microsoft.Dynamics.CRM.AttributeMetadata), you can also update the following properties of the [ImageAttributeMetadata class](xref:Microsoft.Xrm.Sdk.Metadata.ImageAttributeMetadata) | [ImageAttributeMetadata EntityType](xref:Microsoft.Dynamics.CRM.ImageAttributeMetadata).


|Property|Label |Description  |
|---------|---------|---------|
|`MaxSizeInKB`|**Maximum image size**|Set this value to the smallest useable data size appropriate for your particular application. The default setting is `10240`, or 10 MB. The maximum value is `30720` KB (30 MB). This value can't be changed in [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) using the designer after you create the image column, but you can change it using the API.|
|`CanStoreFullImage`|**Can store full images**|When this is false, only thumbnail-sized images will be available. Full images are stored in file storage on the Azure blob to reduce data storage consumption.<br /><br />You can query the [Image Attribute Configuration (AttributeImageConfig)  table](reference/entities/attributeimageconfig.md) to find which image columns support full-sized images. More information: [Detect which image columns support full-sized images](image-column-data.md#detect-which-image-columns-support-full-sized-images)|
|`IsPrimaryImage`|**Primary image column**|Whether the column will be the one image column used to represent a table row in applications.<br /><br />If there's only one image column for a table, this will be set by default. When another image column already exists for a table, this value will be ignored if set to true when creating a new image column. However, you can update the column after you create it to make the new column the primary image column.<br /><br />`IsPrimaryImage` can't be set to false, an exception will be thrown if you try. You must choose another image column and set that `IsPrimaryImage` value to true.<br /><br />If you delete a column that is the current primary image column, another image column for the table will be selected automatically to be the current primary image column.<br /><br />You can query the [Entity Image Configuration (EntityImageConfig)  table](reference/entities/entityimageconfig.md) to know which image columns are the primary images for any table. More information: [Primary Images](image-column-data.md#primary-images)|

> [!NOTE]
> The `MaxHeight` and `MaxWidth` values are always 144 and cannot be changed. These define the size of the thumbnail-sized images that are created for every image column value.

More information:

- [Update a column using Web API](webapi/create-update-column-definitions-using-web-api.md#update-a-column)
- [Update a column using SDK](org-service/metadata-attributemetadata.md#update-a-column)

## Retrieve image column definitions

Use these queries to retrieve image column definitions.

# [SDK for .NET](#tab/sdk)

The static `GetImageColumns` method uses the <xref:Microsoft.Xrm.Sdk.Messages.RetrieveMetadataChangesRequest> class to define a query to return details about all image columns in Dataverse or limited to a specific table. 

The condition evaluated is whether the [AttributeMetadata.AttributeTypeName property](xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.AttributeTypeName) value equals [AttributeTypeDisplayName.ImageType](xref:Microsoft.Xrm.Sdk.Metadata.AttributeTypeDisplayName.ImageType)

```csharp
/// <summary> 
/// Returns the image columns
/// </summary> 
/// <param name="service">The IOrganizationService</param> 
/// <param name="tableLogicalName">Optional filter by table logical name</param> 
static void GetImageColumns(IOrganizationService service, string tableLogicalName = "account") 
{ 
    // The Query definition 
    EntityQueryExpression entityQuery = new EntityQueryExpression() 
    {                 
        Properties = new MetadataPropertiesExpression("SchemaName","Attributes"), 
        AttributeQuery = new AttributeQueryExpression() 
        { 
            Properties = new MetadataPropertiesExpression( 
                "SchemaName", 
                "CanStoreFullImage", 
                "IsPrimaryImage", 
                "MaxSizeInKB") 
        } 
    }; 

    // Enable optional filtering by table logical name 
    if (!string.IsNullOrEmpty(tableLogicalName)){ 

        entityQuery.Criteria.Conditions.Add( 
            new MetadataConditionExpression( 
                propertyName: "LogicalName", 
                conditionOperator: MetadataConditionOperator.Equals, 
                value: tableLogicalName)); 
    } 

    // Only Image columns 
    entityQuery.AttributeQuery.Criteria.Conditions.Add( 
        new MetadataConditionExpression( 
            propertyName: "AttributeTypeName", 
            conditionOperator: MetadataConditionOperator.Equals, 
            value: AttributeTypeDisplayName.ImageType)); 


    // The request 
    RetrieveMetadataChangesRequest request = new RetrieveMetadataChangesRequest() {  
            Query = entityQuery 
    }; 

    // Send the request 
    var response = (RetrieveMetadataChangesResponse)service.Execute(request); 

    //Display the results: 
    response.EntityMetadata.ToList().ForEach(e => { 
        if (e.Attributes.Count() > 0) 
        { 
            Console.WriteLine($"Table: {e.SchemaName}"); 

            e.Attributes.ToList().ForEach(a => { 

                // To access image column properties 
                var  imageColumn = (ImageAttributeMetadata)a; 

                Console.WriteLine($"\t{a.SchemaName}"); 
                Console.WriteLine($"\t\tCanStoreFullImage:{imageColumn.CanStoreFullImage}"); 
                Console.WriteLine($"\t\tIsPrimaryImage:{imageColumn.IsPrimaryImage }"); 
                Console.WriteLine($"\t\tMaxSizeInKB:{imageColumn.MaxSizeInKB}"); 
            }); 

            Console.WriteLine(); 
        }             
    }); 
} 
```

More information: [Query schema definitions](query-schema-definitions.md)


# [Web API](#tab/webapi)

This request will return all the image column definitions for the account table. The filtering is provided by specifying `/Microsoft.Dynamics.CRM.ImageAttributeMetadata` in the URL. More information: [Retrieving attributes](webapi/query-metadata-web-api.md#retrieving-attributes)

**Request:**

```http
GET [Organization URI]/api/data/v9.2/EntityDefinitions(LogicalName='account')/Attributes/Microsoft.Dynamics.CRM.ImageAttributeMetadata?$select=SchemaName,CanStoreFullImage,MaxSizeInKB,IsPrimaryImage
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
```

**Response:**

```http
HTTP/1.1 200 OK
Content-Type: application/json; odata.metadata=minimal
OData-Version: 4.0

{
  "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#EntityDefinitions('account')/Attributes/Microsoft.Dynamics.CRM.ImageAttributeMetadata(SchemaName,CanStoreFullImage,MaxSizeInKB)",
  "value": [
    {
      "SchemaName": "sample_ImageColumn",
      "CanStoreFullImage": true,
      "MaxSizeInKB": 30720,
      "IsPrimaryImage": true,
      "MetadataId": "53ba4b29-6a8c-ed11-81ad-000d3a9933c9"
    }
  ]
}
```

---

## Restrictions with Customer Managed Keys (CMK)

The same restrictions that apply to file columns also apply to image columns configured to store full-sized images. More information: [Restrictions with Customer Managed Keys (CMK)](file-attributes.md#restrictions-with-customer-managed-keys-cmk)

### See also

[Use image column data](image-column-data.md)<br />
[File columns](file-attributes.md)<br />
[Sample: Image Operations using Dataverse SDK for .NET](org-service/samples/set-retrieve-entity-images.md)<br />
[Sample: Image Operations using Dataverse Web API](webapi/samples/image-operations.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
