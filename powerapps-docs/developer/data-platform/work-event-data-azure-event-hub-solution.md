---
title: "Work with Microsoft Dataverse event data in your Azure Event Hub solution (Dataverse) | Microsoft Docs"
description: "Learn about working with event data in your Azure Event Hub solution."
keywords: ""
ms.date: 03/17/2021
ms.service: powerapps
ms.topic: article
ms.assetid: a3732c49-7f47-d87c-5062-585ef28ab511
author: JimDaly # GitHub ID
ms.subservice: dataverse-developer
ms.author: jdaly # MSFT alias of Microsoft employees only
manager: ryjones # MSFT alias of manager or PM counterpart
ms.reviewer: pehecke
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Work with Microsoft Dataverse event data in your Azure Event Hub solution

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]

Azure Event Hubs is a highly scalable publish-subscribe service that can ingest millions of events per second and stream them into multiple applications. The Dataverse-Azure interface enables your event data to be published to the Azure Service Bus and made available to your event hub solution subscribers. The following information describes the general tasks that must be completed to send Azure event data to an event hub solution.  
  
> [!NOTE]
> An Azure subscription and event hub license is required for access to event hubs.
  
## 1. Create an event hub

You can create an event hub in Azure either through API programming  or interactively by using the [Azure classic portal](https://manage.windowsazure.com). Either way, after creating your event hub you must obtain a copy of the event hub connection string and provide that string when registering the Azure service endpoint detailed in the next section.  

For more information about creating event hubs see the [Event Hubs documentation](https://azure.microsoft.com/documentation/services/event-hubs/).  
  
## 2. Register an endpoint

Registering a service endpoint for an event hub is similar to registering for any other supported contract type such as queues or topics. You use the Plug-in Registration tool (PRT) to register the service endpoint.  When filling out the PRT registration form specify a contract type of **Event Hub**. For the message body format, you can choose **XML** or **JSON**. In addition, only SAS authorization is permitted and you must provide the connection string obtained when you created the event hub. More information: [Tutorial: Configure Microsoft Azure (SAS) for integration with Dataverse](walkthrough-configure-azure-sas-integration.md).  
  
## 3. Register code

Dataverse needs to know the exact operation (table and message combination) that, when processed, would cause the Azure-aware plug-in to execute. Since you are creating an event hub, this operation would be related to the processing of Azure event data in particular. You must register a step for the Azure-aware plug-in in the Azure event execution pipeline.  For more information see  [Tutorial: Register an Azure-aware plug-in using the Plug-in Registration Tool](walkthrough-register-azure-aware-plug-in-using-plug-in-registration-tool.md).  

If you are using an Azure-aware custom workflow activity instead of a plug-in, you would register the activity's assembly using the Plug-in Registration tool and incorporate that activity into a workflow. For more information, see [Sample: Azure aware custom workflow activity](/dynamics365/customer-engagement/developer/sample-azure-aware-custom-workflow-activity).
  
## 4. Start listening

Start your Azure service hub solution application listening on the service endpoint.  
  
## 5. Trigger

Perform an operation in Dataverse that would cause the plug-in or workflow containing the custom workflow activity to execute. This is the same operation (table and message combination) that you registered the plug-in step for in the previous section of this topic. You can perform the intended operation by using the web application or through application code accessing the Azure web services.  
  
## 6. Verification

You can check the related system job in the Dataverse web application and look for a status of **Succeeded**. If you find a status of **Failed**, use the status information to identify the possible cause of the failure. You can then recheck the configurations of both systems or debug application code to locate and fix the problem, depending on the nature of the failure.  
  
### See also

 [Azure integration with Dataverse](azure-integration.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]