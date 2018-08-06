---
title: "Work with Dynamics 365 data in your Azure solution (Common Data Service for Apps) | Microsoft Docs"
description: "The ServiceBusPlugin plug-in contains the business logic to post the Dynamics 365 message execution context to the Azure Service Bus. To use this plug-in, you need to register a Azure Service Bus solution endpoint and a step for the plug-in. The step defines what message and entity combination being processed by the core Dynamics 365 operation should trigger the plug-in to execute. The ServiceBusPlugin can only be registered to run asynchronously."
keywords: ""
ms.date: 08/01/2018
ms.service:
  - "powerapps"
ms.custom:
  - ""
ms.topic: article
ms.assetid: 1ef66369-71c9-3b89-ac1a-09d523ca737b
author: brandonsimons" # GitHub ID
ms.author: jdaly" # MSFT alias of Microsoft employees only
manager: ryjones" # MSFT alias of manager or PM counterpart
ms.reviewer: 
---

# Work with Common Data Service for Apps data in your Azure solution

<!-- https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/work-data-azure-solution -->

An internal plug-in named ServiceBusPlugin is provided with Dynamics 365 (online) Common Data Service for Apps. The plug-in contains the business logic to post the Dynamics 365 message execution context to the Azure Service Bus. To use this plug-in, you need to register a Azure Service Bus solution endpoint and a step for the plug-in. The step defines what message and entity combination being processed by the core Dynamics 365 operation should trigger the plug-in to execute. The ServiceBusPlugin can only be registered to run asynchronously. For more information, see [Walkthrough: Register an Azure-aware Plug-in using the Plug-in Registration Tool](walkthrough-register-azure-aware-plug-in-using-plug-in-registration-tool.md).  
  
 In addition, you can write a custom plug-in that includes the required lines of code to post to the service bus. The plug-in is registered in a similar way, except that it must be registered in the sandbox and run under partial trust. For more information on writing a custom plug-in that can post to the Azure Service Bus, see [Write a Custom Azure-aware Plug-in](write-custom-azure-aware-plugin.md).  
  
 You can also write a custom workflow activity that can post the execution context to the service bus and include this activity in your workflows. Sample code for a custom Azure-aware workflow activity is provided in the topic [Sample: Azure Aware Custom Workflow Activity](/dynamics365/customer-engagement/developer/sample-azure-aware-custom-workflow-activity) 
  
### See also  
 [Walkthrough: Register a Plug-in using the Plug-in Registration Tool](walkthrough-register-plugin-using-plugin-registration-tool.md)   
 [Writing a Plug-in](write-plug-in.md)   
 [Plug-in Isolation, Trust, and Statistics](plugin-isolation-trusts-statistics.md)   
 [Understand the Data Context Passed to a Plug-in](understand-data-context-passed-plugin.md)   
 [Registering Plug-ins](register-deploy-plugins.md) <!-- Todo -links needs to be updated -->   
 [Event Execution Pipeline](event-framework.md)   
 [Azure Extensions for Dynamics 365](azure-integration.md) 
 [ServiceEndPoint Entity](reference/entities/serviceendpoint.md)