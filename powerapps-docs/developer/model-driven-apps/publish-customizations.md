---
title: "Publish customizations (model-driven apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Publishing customizations makes the Web application aware of changes to the data that affects the user interface." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 04/14/2021
ms.reviewer: ""
ms.service: powerapps
ms.topic: "article"
author: "KumarVivek" # GitHub ID
ms.author: "kvivek" # MSFT alias of Microsoft employees only
manager: "shilpas" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Publish customizations

Publishing customizations makes the web application aware of changes to the data that affects the user interface.  
  
<a name="BKMK_WhenToPublishCustomizations"></a>   
## When to publish customizations  

Customizations are automatically published when new items are created or existing items are deleted.  You must publish changes after updating table definitions or tables that affect the user interface. You can decide to wait and publish a set of related changes together.  Only published customizations are exported with a solution. You should always publish customizations before exporting a solution.  

[!INCLUDE[cc-terminology](../data-platform/includes/cc-terminology.md)]

When you perform customizations that will appear in Dynamics 365 for tablets, you should always explicitly publish your customizations to make sure that every item is synchronized with the Dynamics 365 for tablets application.  
  
> [!NOTE]
> Publishing customizations can interfere with normal system operation. In a production environment, we recommend that you schedule publishing customizations when it’s least disruptive to users.  
  
## Publishing programmatically  

The following table lists the two messages that you can use to publish customizations.  
  
|Message|Description|  
|-------------|-----------------|  
|<xref:Microsoft.Crm.Sdk.Messages.PublishAllXmlRequest>|Publishes all customizations.|  
|<xref:Microsoft.Crm.Sdk.Messages.PublishXmlRequest>|Publishes the specified customizations.|  
  
 When you use the `PublishXmlRequest` message, you specify which items you want to publish by using the <xref:Microsoft.Crm.Sdk.Messages.PublishXmlRequest.ParameterXml> parameter. `ParameterXML` must comply with the [Publish Request Schema](publish-request-schema.md).  
  
<a name="BKMK_RetrieveUnpublishedMetadata"></a>   

## Retrieving unpublished metadata  

If you want to create an application to edit customizable items in model-driven apps, you must retrieve any unpublished definitions of those items. If a developer defines some changes but does not publish them, your application must be able to retrieve them to display them in the user interface. 
  
 Use the following two methods to retrieve unpublished metadata:  
  
 **RetrieveAsIfPublished parameter**  
 Retrieves table, colum, table relationship, and choice data by using the following messages:  
  
- <xref:Microsoft.Xrm.Sdk.Messages.RetrieveAllEntitiesRequest>  
  
- <xref:Microsoft.Xrm.Sdk.Messages.RetrieveAllOptionSetsRequest>  
  
- <xref:Microsoft.Xrm.Sdk.Messages.RetrieveAttributeRequest>  
  
- <xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityRequest>  
  
- <xref:Microsoft.Xrm.Sdk.Messages.RetrieveOptionSetRequest>  
  
- <xref:Microsoft.Xrm.Sdk.Messages.RetrieveRelationshipRequest>  
  
  **RetrieveUnpublished Request**  
  Retrieves user interface items, such as form, template, visualization and Web resource definitions, by using the following messages:  
  
- <xref:Microsoft.Crm.Sdk.Messages.RetrieveUnpublishedRequest>  
  
- <xref:Microsoft.Crm.Sdk.Messages.RetrieveUnpublishedMultipleRequest>  
  
### See also  

 [Extend table definitions model](../data-platform/metadata-services.md)<br/>
 [Publish request schema](publish-request-schema.md)<br/>
 [Customize forms](customize-entity-forms.md)<br/>
 [Customize views](customize-entity-views.md)<br/>
 [Change application navigation using the SiteMap](../../maker/model-driven-apps/create-site-map-app.md)



[!INCLUDE[footer-include](../../includes/footer-banner.md)]