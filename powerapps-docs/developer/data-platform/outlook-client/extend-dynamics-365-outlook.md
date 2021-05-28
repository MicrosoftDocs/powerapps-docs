---
title: "Extend Dynamics 365 for Outlook (Microsoft Dataverse) | Microsoft Docs"
description: "Dynamics 365 for Outlook lets users interact with data while they’re offline and not connected to a server. Microsoft Dataverse includes features that let you extend your solutions to offline scenarios by calling the web services offline from your custom code. In addition, the Sdk assembly provides programmatic support for basic Outlook actions such as synchronization, going offline or online, and Dynamics 365 for Outlook state verification. Offline programming uses the ASP.NET Development Server."
ms.custom: ""
ms.date: 04/07/2020
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "sriharibs-msft" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Extend Dynamics 365 for Outlook

[!INCLUDE[cc-data-platform-banner](../../../includes/cc-data-platform-banner.md)]

> [!IMPORTANT]
> Effective March 2020, the legacy Dynamics 365 for Outlook (also referred to as Outlook COM add-in) is deprecated. Customers must transition to the modern [Dynamics 365 App for Outlook](/dynamics365/outlook-app/overview) before October 1, 2020. Microsoft will continue to provide support, security and other critical updates to the Outlook COM Add-in until October 1, 2020.
> 
> For further information and steps to make a smooth transition, download [Dynamics 365 for Outlook (COM add-in) Playbook](https://aka.ms/OutlookCOMPlaybook).

Dynamics 365 for Outlook lets users interact with data while they’re offline and not connected to a server. Microsoft Dataverse includes features that let you extend your solutions to offline scenarios by calling the web services offline from your custom code. In addition, the <xref:Microsoft.Crm.Outlook.Sdk> assembly provides programmatic support for basic Outlook actions such as synchronization, going offline or online, and Dynamics 365 for Outlook state verification. Offline programming uses the ASP.NET Development Server.  
  
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
  



[!INCLUDE[footer-include](../../../includes/footer-banner.md)]