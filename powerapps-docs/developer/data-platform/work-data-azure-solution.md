---
title: "Work with Microsoft Dataverse data in your Azure solution (Microsoft Dataverse) | Microsoft Docs"
description: "Provides an overview of passing data from Dataverse to an Azure cloud hosted solution."
ms.date: 07/19/2024
author: swylezol
ms.author: swylezol
ms.reviewer: pehecke
ms.topic: article
ms.subservice: dataverse-developer
search.audienceType: 
  - developer
contributors:
 - JimDaly
 - phecke
---

# Work with Microsoft Dataverse data in your Azure solution

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]

A default Azure-aware plug-in is provided with Dataverse. The plug-in contains the business logic to post the Dataverse message execution context to the Azure Service Bus. To use this plug-in, you need to register a service endpoint and a step. The step defines what message and table combination being processed by the core Dataverse operation should trigger the plug-in to execute. For more information, see [Walkthrough: Register an Azure-aware Plug-in using the Plug-in Registration Tool](walkthrough-register-azure-aware-plug-in-using-plug-in-registration-tool.md).  
  
In addition, you can write a custom plug-in that includes the required lines of code to post to the Azure service. The plug-in is registered in a similar way, except that it must be registered in the sandbox. For more information on writing a custom plug-in that can post to the Azure Service Bus, see [Write a Custom Azure-aware Plug-in](write-custom-azure-aware-plugin.md).  
  
You can also write a custom workflow activity that can post the execution context to the Azure service and include this activity in your workflows. Sample code for a custom Azure-aware workflow activity is provided in the [Sample: Azure aware custom workflow activity](org-service/samples/azure-aware-custom-workflow-activity.md).

> [!NOTE]
> Any service endpoint registered for a synchronous step will send the execution context data to the Azure service immediately. If an error occurs after the request was sent, the data operation will rollback but the request sent the the Azure service cannot be recalled.

### See also

[Writing a Plug-in](write-plug-in.md)<br/>
[Event execution pipeline](event-framework.md#event-execution-pipeline)<br/>
[ServiceEndPoint Entity](reference/entities/serviceendpoint.md)<br/>

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
