---
title: "Offline use of services (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn about how various services can be used offline. There are several messages that are supported offline. You can also determine whether a IOrganizationService message works offline by checking the SdkMessage.Availability attribute for the desired message" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 10/31/2018
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

# Offline use of services

[!INCLUDE[cc-data-platform-banner](../../../includes/cc-data-platform-banner.md)]

Dynamics 365 for Outlook with Offline Access enables you to continue your work when you are disconnected from the server.  
  
 In addition, the event and plug-in infrastructure lets you leverage development investments across solutions by using the same APIs and programming model. The <xref:Microsoft.Xrm.Sdk.IOrganizationService> methods and the Microsoft Dataverse OData service methods function both online and offline. When using a method such as `Create` or `Update` offline, the data is written locally and then when the user connects to the server, the actions are played back to the server.  
  
 For more information about whether a message is supported offline, see <xref:Microsoft.Crm.Sdk.Messages>. You can also determine whether a <xref:Microsoft.Xrm.Sdk.IOrganizationService> message works offline by checking the `SdkMessage.Availability` attribute for the desired message. If the message works for multiple entity types, you must also check the `SdkMessageFilter.Availability` attribute to see whether the message is available offline for the entity you want to work with. For example, the `Create` message is available offline, but not for the queue, user, or site entities.  
  
 Tracing can be enabled on the Dynamics 365 for Microsoft Office Outlook with Offline Access for debugging. For more information about the event viewer and platform tracing, see [Monitoring and troubleshooting Dynamics 365](/previous-versions/dynamicscrm-2016/deployment-administrators-guide/hh699694(v=crm.8)).  
  
### See also  
 
 <xref:Microsoft.Xrm.Sdk.IOrganizationService>   
 [Organization Service Methods](/dynamics365/customer-engagement/developer/org-service/organization-service-methods)   
 <xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>   
 <xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]