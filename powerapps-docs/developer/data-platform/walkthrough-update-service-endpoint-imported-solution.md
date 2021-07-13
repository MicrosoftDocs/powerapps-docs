---
title: "Walkthrough: Update a service endpoint imported from a solution (Microsoft Dataverse) | Microsoft Docs"
description: "Demonstrates updating a Dataverse service endpoint imported from a solution."
keywords: ""
ms.date: 03/18/2021
ms.service: powerapps
ms.topic: article
ms.assetid: 66795838-3b15-bfb3-6f59-68cfe2fe988e
author: JimDaly # GitHub ID
ms.author: jdaly # MSFT alias of Microsoft employees only
manager: ryjones # MSFT alias of manager or PM counterpart
ms.reviewer: "pehecke"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Tutorial: Update a service endpoint imported from a solution

An extra step is required after importing into an organization a solution containing one or more service endpoints configured for SAS authorization. When the solution containing the service endpoints is exported, the exported solution does not contain the SAS Key for each service endpoint. After importing the solution into an organization, you must perform an additional step to provide the SAS Key for each service endpoint.  
  
Follow these steps to set the SAS Key for each service endpoint after solution import.  
  
## Update the SAS Key  
  
1. Run the Plug-in Registration tool, which is available for download from NuGet. More information: [Download tools from NuGet](download-tools-nuget.md)
  
1. Using the Plug-in Registration tool, sign in to the organization that contains the imported solution.  
  
1. Select the target service endpoint in the tab view of the organization.  
  
1. Select **Update**. You should see the following form with the fields already filled in.  
  
    ![Update service endpoint SAS key value.](media/sas-key.PNG "Update service endpoint SAS key value")  
  
1. The **SAS Key** field is displayed with a value of "*******".  Replace that value with the correct SAS key value. You can obtain the SAS Key for your Azure messaging entity (queue, topic, etc.) from the [Azure portal](https://portal.azure.com).  
  
1. Select **Save**.  
  
### See also

[Azure integration](azure-integration.md)<br />
[Service Bus authentication and authorization](/azure/service-bus-messaging/service-bus-authentication-and-authorization)<br />
[Service Bus access control with Shared Access Signatures](/azure/service-bus-messaging/service-bus-sas)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]