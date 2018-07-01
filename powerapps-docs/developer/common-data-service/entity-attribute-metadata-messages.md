---
title: "Entity attribute metadata messages (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "About the messages used to edit entity attribute metadata, also known as properties or fields." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "JimDaly" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Entity attribute metadata messages

<!-- https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/entity-attribute-metadata-messages -->

An entity attribute is a container for a piece of data in an entity. The term *attribute* and *property* (class property) are often used interchangeably with the term *entity attribute*. Model-driven applications use the term *field* when they refer to entity attributes.  

> [!NOTE]
> It is possible to create and update entity attributes using the Web API. See [Create attributes](webapi/create-update-entity-definitions-using-web-api.md#create-attributes) for more details.

## Entity attribute messages  
 The following table lists the messages that you can use to perform actions on entity attributes.  
  
|Message|Web API Operation|SDK Assembly|   
|-------------|-----------------|-----------------|  
|CreateAttribute</br></br>Create entity attributes|POST to EntityMetadata Attributes collection-valued navigation property with JSON definition of attribute. More information: [Create attributes](webapi/create-update-entity-definitions-using-web-api.md#create-attributes)|<xref:Microsoft.Xrm.Sdk.Messages.CreateAttributeRequest>| 
|DeleteAttribute</br></br>Delete entity attributes|DELETE to the URL of the attribute.|<xref:Microsoft.Xrm.Sdk.Messages.DeleteAttributeRequest>|  
|DeleteOptionValue</br></br>Delete an option from <xref:Microsoft.Xrm.Sdk.Metadata.PicklistAttributeMetadata> or <xref:Microsoft.Xrm.Sdk.Metadata.StatusAttributeMetadata> attributes|<xref href="Microsoft.Dynamics.CRM.DeleteOptionValue?text=DeleteOptionValue Action" />|<xref:Microsoft.Xrm.Sdk.Messages.DeleteOptionValueRequest>|  
|InsertOptionValue</br></br>Add an option to a <xref:Microsoft.Xrm.Sdk.Metadata.PicklistAttributeMetadata> attribute|<xref href="Microsoft.Dynamics.CRM.InsertOptionValue?text=InsertOptionValue Action" />|<xref:Microsoft.Xrm.Sdk.Messages.InsertOptionValueRequest>|Add an option to a <xref:Microsoft.Xrm.Sdk.Metadata.PicklistAttributeMetadata> attribute.|  
|InsertStatusValue</br></br>Add an option to a <xref:Microsoft.Xrm.Sdk.Metadata.StatusAttributeMetadata> attribute|<xref href="Microsoft.Dynamics.CRM.InsertStatusValue?text=InsertStatusValue Action" />|<xref:Microsoft.Xrm.Sdk.Messages.InsertStatusValueRequest>|  |Changes the order of the options presented in an <xref:Microsoft.Xrm.Sdk.Metadata.PicklistAttributeMetadata> attribute|<xref href="Microsoft.Dynamics.CRM.OrderOption?text=OrderOption Action" />|<xref:Microsoft.Xrm.Sdk.Messages.OrderOptionRequest>|  
|RetrieveAttribute</br></br>Retrieve entity attributes|Use the Web API query mentioned in [Querying EntityMetadata attributes](webapi/query-metadata-web-api.md#bkmk_queryAttributesexample) to retrieve entity attributes.|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveAttributeRequest>|  
|UpdateAttribute</br></br>Update entity attributes|See [Update entities](webapi/create-update-entity-definitions-using-web-api.md#update-entities)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateAttributeRequest>|  
|UpdateStateValue</br></br>Update a label for a <xref:Microsoft.Xrm.Sdk.Metadata.StateAttributeMetadata> attribute|<xref href="Microsoft.Dynamics.CRM.UpdateStateValue?text=UpdateStateValue Action" />|<xref:Microsoft.Xrm.Sdk.Messages.UpdateStateValueRequest>|  

### See also  

[Attribute metadata](entity-attribute-metadata.md)<br />
[Create auto-number attribute](create-auto-number-attributes.md)<br />
[Work with Attributes](org-service/work-attribute-metadata.md)<br />
[Sample: Work with Attributes](org-service/sample-work-attribute-metadata.md)