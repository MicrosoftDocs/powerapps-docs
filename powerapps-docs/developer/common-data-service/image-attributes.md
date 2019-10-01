---
title: "Image attributes (Common Data Service) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn about image attributes that include image data witht in the application, and supporting attributes, Retrieving image data, and Uploading image data." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 10/01/2019
ms.reviewer: ""
ms.service: powerapps
ms.topic: "article"
author: "mayadumesh" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Image attributes

Certain system entities and all custom entities support images. Those entities that do support images can contain both a thumbnail and a full-size primary image. The thumbnail image can be seen in the web application when viewing the entity's form data. There can be multiple image attributes in an entity instance but there can be only one primary image. However, you can change the primary image from one image to another. Each full-sized image attribute is limited to 30 MB in size.

For information about which system entities support images, see [Entity images](/dynamics365/customer-engagement/developer/introduction-entities#entity-images).

In addition to image attributes, custom entities support zero or more file attributes that can contain any binary data. These file attributes can contain more binary data than image attributes. For more information see [File attributes](file-attributes.md).
  
<a name="BKMK_SupportingAttributes"></a>   
## Supporting attributes  
 For those entities that support image attributes, the <xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.SchemaName> of the entity image attribute is always `EntityImage`. When an image attribute is added to an entity some additional attributes are created to support it.  
  
### EntityImage_Timestamp attribute  
 Attribute Type Name:  `BigIntType`  
  
 The value represents when the image was last updated and is used to help make sure that the latest version of the image is downloaded and cached on the client.  
  
### EntityImage_URL attribute  
 Attribute Type Name: `StringType`  
  
 An absolute URL to display the entity image in a client.  
  
 The URL is composed this way:  
  
```http  
{0}/image/download.aspx?entity={1}&attribute={2}&id={3}&timestamp={4}
```  
  
- 0 : The organization URL  
  
- 1 : The entity logical name  
  
- 2 : The attribute logical name  
  
- 3 : The EntityImageId value.  
  
- 4 : The EntityImage_Timestamp value  
  
  For example:   
  `https://myorg.crm.dynamics.com/image/download.aspx?attribute=entityimage&entity=contact&id={ECB6D3DF-4A04-E311-AFE0-00155D9C3020}&timestamp=635120312218444444`  
  
### EntityImageId  
 Attribute Type Name: `UniqueIdentifierType`  
  
 The unique identifier of the image  
  
<a name="BKMK_RetrievingImages"></a>   
## Retrieving image data  
 When you use <xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*> or <xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*> the `EntityImage` is not included when the <xref:Microsoft.Xrm.Sdk.Query.ColumnSet>.`AllColumns` property is set to true. Because of the potential size of data in this attribute, to return this attribute you must explicitly request it.  
  
 The binary data representing the image isn’t returned using the deprecated <xref:Microsoft.Crm.Sdk.Messages.ExecuteFetchRequest> class. You should use <xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> instead.  
  
 More information: [Sample: Set and retrieve entity images](/dynamics365/customer-engagement/developer/sample-set-retrieve-entity-images).  
  
<a name="BKMK_UploadingImages"></a>   
## Uploading image data  
 To update images set the value of the `EntityImage` to a `byte[]` that contains the content of the file. All images are displayed in a 144x144 pixel square. Images will be cropped and resized to reduce the size of the data before being saved.  
  
- Images with at least one side larger than 144 pixels are cropped on center to 144x144.  
  
- Images with both sides smaller than 144 are cropped square to their smallest side.  
  
  The following table shows two examples.  
  
|Before|After|  
|------------|-----------|  
|![Image before resize](media/crm-itpro-cust-imagebeforeresize.png "Image before resize")<br /><br /> 300x428|![image after resize](media/crm-itpro-cust-imageafterresize.jpg "image after resize")<br /><br /> 144x144|  
|![Second image resize example](media/crm-itpro-cust-imagebeforeresizeexample2.png "Second image resize example")<br /><br /> 91x130|![second resize example](media/crm-itpro-cust-imageafterresizeexample2.jpg "second resize example")<br /><br /> 91x91|  
  
 More information: [Sample: Set and retrieve entity images](/dynamics365/customer-engagement/developer/sample-set-retrieve-entity-images).  
  
### See also  
[File attributes](file-attributes.md)  
[Introduction to Entities in Dynamics 365](/dynamics365/customer-engagement/developer/introduction-entities)   
 [Introduction to entity attributes in Dynamics 365](/dynamics365/customer-engagement/developer/introduction-entity-attributes)   
 [Sample: Set and retrieve entity images](/dynamics365/customer-engagement/developer/sample-set-retrieve-entity-images)
