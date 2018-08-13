---
title: "Integrate Common Data Service for Apps with SharePoint (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "The SharePoint integration feature enables you to store and manage documents on SharePoint in the context of a Common Data Service for Apps record, and use the SharePoint document management abilities in CDS for Apps, such as checking the document in and out, viewing version history, and changing document properties." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "JimDaly" #TODO: NoOwner
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Integrate Common Data Service for Apps with SharePoint

SharePoint Server is a collaboration and content management application that simplifies how people store, find, and share information. It helps people to collaborate effectively by having secure access to documents and information that they require to make business decisions.  
  
 The SharePoint integration feature enables you to store and manage documents on SharePoint in the context of a CDS for Apps Customer Engagement record, and use the SharePoint document management abilities in CDS for Apps, such as checking the document in and out, viewing version history, and changing document properties.  
  
 CDS for Apps supports two types of integration with SharePoint: client-to-server and server-to-server (server-based). More information: [Enable SharePoint integration](get-started-sharepoint-integration.md#SPIntegration)  
  
 Use the `SharePointSite` and `SharePointDocumentLocation` entities to store and manage the SharePoint Server location records in CDS for Apps, and the `UserMapping` entity to define custom claim mappings to use a value other than the default value used by CDS for Apps to authenticate and authorize CDS for Apps users in SharePoint.  
  
## In This Section  
 [Understanding Microsoft Dynamics 365 and SharePoint Integration](get-started-sharepoint-integration.md)  
  
 [Enable SharePoint Integration](enable-document-management-entities.md)  
  
 [Actions on SharePoint Location Records](actions-on-sharepoint-location-records.md)  
  
 [Define custom claim mapping for SharePoint server-based integration](define-custom-claim-mapping-sharepoint-server-based-integration.md)  
  
 [Sample: Enable Document Management for Entities](/dynamics365/customer-engagement/developer/integration-dev/sample-enable-document-management-entities)  
  
 [Sample: Create, Retrieve, Update, and Delete a SharePoint Location Record](/dynamics365/customer-engagement/developer/integration-dev/create-retrieve-update-delete-sharepoint-location-record)  
  
 [Sample: Retrieve Absolute URL and Site Collection URL of a Location Record](/dynamics365/customer-engagement/developer/integration-dev/retrieve-absolute-url-and-site-collection-url-of-a-location-record)  
  
## Reference  
 [Manage your documents using SharePoint](https://technet.microsoft.com/library/dn531062.aspx)  
  
 [SharePoint general development](https://msdn.microsoft.com/sharepoint/default.aspx)  
  
 [Overview of document management in SharePoint 2013](https://technet.microsoft.com/library/cc261933\(v=office.15\).aspx)  
  
## Related Sections  
 [Extend Microsoft Dynamics 365](/dynamics365/customer-engagement/developer/extend-dynamics-365-server)   
  
 [Integrate Microsoft Dynamics 365 with OneNote](/dynamics365/customer-engagement/developer/integrate-onenote)