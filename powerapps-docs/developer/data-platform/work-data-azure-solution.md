---
title: "Work with Dynamics 365 data in your Azure solution (Microsoft Dataverse) | Microsoft Docs"
description: "Provides an overview of passing data from Dataverse to an Azure cloud hosted solution."
keywords: ""
ms.date: 03/17/2021
ms.service: powerapps
ms.topic: article
ms.assetid: 1ef66369-71c9-3b89-ac1a-09d523ca737b
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

# Work with Microsoft Dataverse data in your Azure solution

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]

An internal full-trust plug-in named `ServiceBusPlugin` is provided with Dataverse. The plug-in contains the business logic to post the Dataverse message execution context to the Azure Service Bus. To use this plug-in, you need to register a Azure Service Bus solution endpoint and a step for the plug-in. The step defines what message and table combination being processed by the core Dataverse operation should trigger the plug-in to execute. The `ServiceBusPlugin` can only be registered to run asynchronously. For more information, see [Walkthrough: Register an Azure-aware Plug-in using the Plug-in Registration Tool](walkthrough-register-azure-aware-plug-in-using-plug-in-registration-tool.md).  
  
 In addition, you can write a custom plug-in that includes the required lines of code to post to the service bus. The plug-in is registered in a similar way, except that it must be registered in the sandbox and run under partial trust. For more information on writing a custom plug-in that can post to the Azure Service Bus, see [Write a Custom Azure-aware Plug-in](write-custom-azure-aware-plugin.md).  
  
 You can also write a custom workflow activity that can post the execution context to the service bus and include this activity in your workflows. Sample code for a custom Azure-aware workflow activity is provided in the topic [Sample: Azure Aware Custom Workflow Activity](/dynamics365/customer-engagement/developer/sample-azure-aware-custom-workflow-activity) 
  
### See also

[Writing a Plug-in](write-plug-in.md)<br/>
[Event execution pipeline](event-framework.md#event-execution-pipeline)<br/> 
[ServiceEndPoint Entity](reference/entities/serviceendpoint.md)<br/>


[!INCLUDE[footer-include](../../includes/footer-banner.md)]