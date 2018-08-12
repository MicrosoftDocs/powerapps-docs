---
title: "Get started with SharePoint integration (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "By using SharePoint Server document management capabilities, you can control how documents are created, reviewed, published and disposed or archived" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "JimDaly" #TODO: NoOwner
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Get started with SharePoint integration

SharePoint Server integration enables document management capabilities in Common Data Service for Apps. There are two aspects to SharePoint Server integration:  
  
- **Setting up SharePoint integration**. A system administrator sets up a SharePoint Server environment. The CDS for Apps administrator (a user who has the SharePoint Site Collection Administrator role) selects the CDS for Apps entities for which to enable the document management feature, and specifies the target SharePoint Server. As part of specifying the target server, the CDS for Apps administrator specifies the SharePoint Server site collection or the SharePoint Server site URL by using the                      `SharePointSite` entity.  
  
- **Creating and managing SharePoint document location records**. CDS for Apps users can create and manage SharePoint Server document location records after SharePoint Server integration is enabled. You can create and manage SharePoint Server document location records by using the                      `SharePointDocumentLocation` entity. CDS for Apps also allows for the automatic creation of folders on the server that is running SharePoint Server for entity records under certain conditions. However, automatic creation of folders cannot be done through the CDS for Apps web services. 
  
<a name="StorageConcepts"></a>   
## SharePoint storage concepts  
 By using SharePoint Server document management capabilities, you can control the life cycle of documents in your organization: how they are created, reviewed, published, and disposed or archived. SharePoint Server uses a hierarchical storage model to store and manage documents. Some of the SharePoint Server storage concepts that you should know are as follows:                  *Site Collection*,                  *Site*,                  *Document Library*, and                  *Document Folder*. These storage objects provide the framework for the content management infrastructure that SharePoint Server provides. For more information about these storage concepts, see                  [Storage levels: content storage benefits and considerations](http://go.microsoft.com/fwlink/p/?LinkId=196843).  
  
<a name="SupportedSPVersions"></a>   
## Software requirements for SharePoint Integration  
 For supported versions of SharePoint and CDS for Apps for SharePoint integration, see [SharePoint Document Management software requirements for Microsoft Dynamics 365](https://technet.microsoft.com/library/hh699758.aspx).  
  
<a name="SPIntegration"></a>   
## Enable SharePoint integration  
 SharePoint integration for CDS for Apps can only be enabled using the web or Dynamics 365 for Outlook. This isn’t supported through SDK. For more information, see                  [Set up SharePoint integration with Microsoft Dynamics CRM](https://technet.microsoft.com/library/dn531154.aspx).  
  
 CDS for Apps supports two types of integration with SharePoint: client-to-server and server-to-server (server-based).  
  
- **Client-to-server integration with SharePoint**: The client-to-server integration is enabled by default. However, for a richer user experience, install the Microsoft Dynamics CRM List Component for Microsoft SharePoint Server 2010 or SharePoint Server 2013.                  For more information about the component, see **Microsoft Dynamics CRM list component for Microsoft SharePoint Server** section later in this topic.  
  
- **Server-to-server integration with SharePoint**: This does not require you to install the Microsoft Dynamics CRM List Component in SharePoint or any other additional software to have the SharePoint document management functionality within CDS for Apps. After you enable server-based SharePoint integration for your organization, you can’t revert to the client-based authentication method.  
  
  After enabling SharePoint integration:  
  
- **Enable document management for entities**: Select the entities in CDS for Apps for which you want to create and manage documents on SharePoint Server. More information: [Enable SharePoint Integration for Entities](enable-document-management-entities.md).  
  
     When you enable document management for an entity in CDS for Apps, a **Documents** link under the **Common** group in the left pane is added for the all entity records in the CDS for Apps web application. You can use the **Documents** link to create or manage SharePoint Server location records for the entity record.  
  
- **Specify the target SharePoint server**: Specify the URL of a site or site collection on the SharePoint Online, SharePoint Server 2010, or SharePoint Server 2013. This URL is used to automatically create folders and document libraries on SharePoint.  
  
<a name="CRMListComponent"></a>   
## Microsoft Dynamics CRM list component for Microsoft SharePoint Server  
 Microsoft Dynamics CRM List Component for Microsoft SharePoint Server 2010 and SharePoint 2013 is a SharePoint Server solution package file (.wsp) that must be installed (uploaded and activated) on the site collection on the target SharePoint 2010 or 2013 server to enable the following:  
  
- View documents that are stored on the SharePoint Server 2010 server in a CDS for Apps List view (look and feel of Dynamics 365).  
  
- Automatic creation of the document locations on the SharePoint Server server.  
  
  You can [download and install the Microsoft Dynamics CRM 2013 List Component](http://go.microsoft.com/fwlink/p/?LinkId=516963) for SharePoint Server 2010 and SharePoint Server 2013. To install this component, you must have SharePoint Server site collection administrator privileges on the target SharePoint server.  
  
  There are two versions of the Microsoft Dynamics CRM List Component:  
  
- **Microsoft Dynamics CRM List Component for Microsoft SharePoint Server 2010** : This version only works with SharePoint 2010.  
  
- **SharePoint Server 2013** : This version only works with SharePoint 2013 and SharePoint Online.  
  
  For more information about installing the component, see [Configure SharePoint integration using the list component](https://technet.microsoft.com/library/dn894708.aspx)  
  
### See also  
 [Integrate SharePoint with Microsoft Dynamics 365 5](integrate-sharepoint.md)   
 [Enable SharePoint Integration for Entities](enable-document-management-entities.md)   
 [Actions on SharePoint Location Records](actions-on-sharepoint-location-records.md)   
 [Define custom claim mapping for SharePoint server-based integration](define-custom-claim-mapping-sharepoint-server-based-integration.md)  