---
title: "Walkthrough: Configure Microsoft Azure (SAS) for integration (Common Data Service for Apps) | Microsoft Docs"
description: "The walkthrough guides you through configuring the Azure Service Bus issuer, scope, and rules to allow a listener application to read the Common Data Service for Apps messages posted to the Azure Service Bus."
keywords: ""
ms.date: 10/31/2018
ms.service:
  - "powerapps"
ms.custom:
  - ""
ms.topic: article
ms.assetid: d7b24b11-57f0-ab05-4bec-0b64efee178d
author: brandonsimons # GitHub ID
ms.author: jdaly # MSFT alias of Microsoft employees only
manager: ryjones # MSFT alias of manager or PM counterpart
ms.reviewer: 
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Tutorial: Configure Azure (SAS) for integration with Common Data Service for Apps

<!-- https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/walkthrough-configure-azure-sas-integration -->

This walkthrough guides you through configuring the Azure Service Bus issuer, scope, and rules to allow a listener application to read the CDS for Apps messages posted to the Azure Service Bus.  
  
> [!NOTE]
>  This walkthrough applies to any Common Data Service for Apps deployment when using SAS authorization for Azure messaging. For more information about Azure Service Bus authorization, see [Service Bus authentication and authorization](https://azure.microsoft.com/en-us/documentation/articles/service-bus-authentication-and-authorization/).  
>   
> You must use the Plug-in Registration Tool. To download the plug-in registration tool, see [Download tools from NuGet](download-tools-NuGet.md).
  
## Prerequisites  
  
-   An Azure account with a license to create Service Bus entities.
  
-   A SAS configured service bus namespace.
  
-   A SAS configured service bus messaging entity: queue, topic, relay, or event hub.
  
-   The messaging entity must have the `Send` policy permission at a minimum. For a two-way relay, the policy must also have the `Listen` permission.  
-  The authorization connection string of your messaging entity. 
  
 ![Define the Azure policy permissions](media/policy-permissions.png "Define the Azure policy permissions")  
  
 Refer to the [Create a Service Bus namespace using the Azure portal](/azure/service-bus-messaging/service-bus-create-namespace-portal) for instructions on how to create a Service Bus namespace and messaging entity.  
  
## Create a service endpoint

A [ServiceEndpoint Entity ](reference/entities/serviceendpoint.md) contains configuration data that is required for external messaging with a Azure Service Bus solution endpoint. By using the Plug-in Registration Tool, you can easily create a service endpoint entity in a CDS for Apps organization and configure  the service bus endpoint issuer, scope, and rules. D:\GitHub\power-apps\powerapps-docs-pr\powerapps-docs\developer\common-data-service\reference\entities\serviceendpoint.md
  
### Register a Service Endpoint  
  
1.  Run the Plug-in Registration Tool and log into your target CDS for Apps organization.  
  
2.  Select **Register > Register New Service Endpoint**.  
  
3.  Check **Let's Start with the connection string from the Azure Service Bus Portal** and paste the connection string of your service bus messaging entity.  
  
 ![Provide authorization connection string](media/sas-connection-string.PNG "Provide authorization connection string")  
  
4.  Select **Next**.  
  
5.  Fill out the **Service Endpoint Registration** form by entering the **Designation Type**, **Message Format**, and optionally the **User Information Sent** and **Description** fields  
  
 ![Service endpoint registration](media/service-endpoint-registration.PNG "Service endpoint registration")  
  
   For more information about the message format, see [Write a listener application for a Azure solution](write-listener-application-azure-solution.md).  
  
6.  Select **Save**.  
  
7.  After a few seconds or so, you will see the new service endpoint in the **Registered Plug-ins & Custom Workflow Activities** list.  
  
 ![New service endpoint](media/new-service-endpoint.PNG "New service endpoint")  
  
### See also

[Azure Integration](azure-integration.md)<br />
[Azure Service Bus](/azure/service-bus-messaging/service-bus-fundamentals-hybrid-solutions.md)
