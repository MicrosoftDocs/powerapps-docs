---
title: "Extend Dynamics 365 for Outlook (Common Data Service for Apps) | Microsoft Docs"
description: "Dynamics 365 for Outlook lets users interact with data while they’re offline and not connected to a server. Common Data Service for Apps includes features that let you extend your solutions to offline scenarios by calling the web services offline from your custom code. In addition, the Sdk assembly provides programmatic support for basic Outlook actions such as synchronization, going offline or online, and Dynamics 365 for Outlook state verification. Offline programming uses the ASP.NET Development Server."
ms.custom: ""
ms.date: 10/31/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "sriharibs" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
<!-- https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/extend-customer-engagement-outlook 

This topic should be in powerapps-docs/developer/common-data-service/outlook-client/
-->

# Extend Dynamics 365 for Outlook

> [!IMPORTANT]
> As of 1/29/2018, based on overwhelming customer feedback and our desire to continue supporting our customers, we have **decided not to deprecate Dynamics 365 for Outlook** (Outlook add-in). Please read [this blog post](https://blogs.msdn.microsoft.com/crm/2018/01/29/continued-support-for-outlook-add-in-dynamics-365-for-outlook/) for more details.

Microsoft Dynamics 365 for Outlook lets users interact with data while they’re offline and not connected to a server. CDS for Apps includes features that let you extend your solutions to offline scenarios by calling the web services offline from your custom code. In addition, the <xref:Microsoft.Crm.Outlook.Sdk> assembly provides programmatic support for basic Outlook actions such as synchronization, going offline or online, and Dynamics 365 for Outlook state verification. Offline programming uses the ASP.NET Development Server.  
  
 Dynamics 365 includes features that allow administrators to customize and manage filters for their users. Filter templates provide the starting point for entity synchronization on Dynamics 365 for Outlook. Filters determine which entity collections are synchronized to Outlook and to SQL Server 2008 Express Edition for offline-enabled Dynamics 365 solutions.  
  
## In This Section

[Offline and Outlook Filters and Templates](offline-outlook-filters-templates.md)<br />  
[Sample: Retrieve Outlook Filters](sample-create-retrieve-outlook-filters.md)<br />  
[Sample: Use Outlook Methods](sample-outlook-methods.md)<br />
  
## Related Sections

<!-- TODO:
[Extend Dynamics 365](extend-dynamics-365-server.md)<br />
[Supported Extensions for Dynamics 365](supported-extensions.md)<br />
[The Metadata and Data Models in Dynamics 365](metadata-data-models.md)<br />
[Extend Dynamics 365 on the server](extend-dynamics-365-server.md)<br />
[Extend Dynamics 365 on the client](extend-client.md)<br />
[Customize Dynamics 365 applications](customize-dev/customize-applications.md)<br />
[Package and distribute extensions using solutions](package-distribute-extensions-use-solutions.md)<br />
[Integrate Dynamics 365 with SharePoint](integration-dev/integrate-sharepoint.md)<br />
 -->
<xref href="Microsoft.Dynamics.CRM.savedquery?text=savedquery EntityType" /><br />
[SavedQuery Entity](../reference/entities/savedquery.md)<br />
  

