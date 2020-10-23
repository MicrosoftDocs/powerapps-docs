---
title: "Work with Dynamics 365 data in your Azure solution (Common Data Service) | Microsoft Docs"
description: "The ServiceBusPlugin plug-in contains the business logic to post the Dynamics 365 message execution context to the Azure Service Bus. To use this plug-in, you need to register a Azure Service Bus solution endpoint and a step for the plug-in. The step defines what message and entity combination being processed by the core Dynamics 365 operation should trigger the plug-in to execute. The ServiceBusPlugin can only be registered to run asynchronously."
keywords: ""
ms.date: 06/01/2019
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

# Work with Common Data Service data in your Azure solution

[!INCLUDE[cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

An internal plug-in named `ServiceBusPlugin` is provided with Common Data Service (CDS). The plug-in contains the business logic to post the CDS message execution context to the Azure Service Bus. To use this plug-in, you need to register a Azure Service Bus solution endpoint and a step for the plug-in. The step defines what message and entity combination being processed by the core CDS operation should trigger the plug-in to execute. The `ServiceBusPlugin` can only be registered to run asynchronously. For more information, see [Walkthrough: Register an Azure-aware Plug-in using the Plug-in Registration Tool](walkthrough-register-azure-aware-plug-in-using-plug-in-registration-tool.md).  
  
 In addition, you can write a custom plug-in that includes the required lines of code to post to the service bus. The plug-in is registered in a similar way, except that it must be registered in the sandbox and run under partial trust. For more information on writing a custom plug-in that can post to the Azure Service Bus, see [Write a Custom Azure-aware Plug-in](write-custom-azure-aware-plugin.md).  
  
 You can also write a custom workflow activity that can post the execution context to the service bus and include this activity in your workflows. Sample code for a custom Azure-aware workflow activity is provided in the topic [Sample: Azure Aware Custom Workflow Activity](/dynamics365/customer-engagement/developer/sample-azure-aware-custom-workflow-activity) 
  
### See also  
[Writing a Plug-in](write-plug-in.md)<br/>
[Event execution pipeline](event-framework.md#event-execution-pipeline)<br/> 
[ServiceEndPoint Entity](reference/entities/serviceendpoint.md)<br/>