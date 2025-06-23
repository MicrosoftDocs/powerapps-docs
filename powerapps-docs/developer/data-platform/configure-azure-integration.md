---
title: "Configure Azure integration (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn about configuring Azure integration with Microsoft Dataverse." # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 07/19/2024
ms.reviewer: "pehecke"
ms.topic: how-to
author: "jaredha" # GitHub ID
ms.subservice: dataverse-developer
ms.author: "jdaly" # MSFT alias of Microsoft employees only
search.audienceType: 
  - developer
contributors:
  - PHecke
---
# Configure Azure integration with Microsoft Dataverse

You can post the message request data for the current Dataverse core operation to cloud hosted applications listening on the Azure Service Bus. To enable this capability in Dataverse, perform the tasks detailed in this topic.

## Configure Azure For Dataverse integration

Because you'll use SAS for authorization, you need to configure the rules and issuers of your Azure solution to allow a listener application to read the Dataverse message posted to the Azure Service Bus. In addition, you must configure the service bus rules to accept the Dataverse issuer claim. The recommended method to configure Azure is to use the Plug-in Registration tool (PRT).

For instructions on configuring authorization see [Tutorial: Configure Azure (SAS) for integration with Dataverse](walkthrough-configure-azure-sas-integration.md).

## Test Configuration

After configuring Azure integration, you'll need to perform these other tasks.

1. Write and register a listener application with an Azure Service Bus solution endpoint. For more information, see the Azure Service Bus [documentation](/azure/service-bus-messaging/service-bus-messaging-overview).
1. Register an Azure aware plug-in or an Azure-aware custom workflow activity with Dataverse. More information: [Tutorial: Register an Azure-aware plug-in using the Plug-in Registration tool](walkthrough-register-azure-aware-plug-in-using-plug-in-registration-tool.md)
1. Perform the necessary Dataverse operation that triggers the plug-in or custom workflow activity to run.

If all of the preceding steps were performed correctly, a message containing the Dataverse data context should be sent to an Azure queue or topic and ultimately received by the listener application. You can navigate to the System Jobs grid in the Power Apps web application, under **Advanced settings**, and check the status of the related system job to see if the post to the Azure Service Bus succeeded. If errors occur, the message section of the system job displays the error details.

### See also

[Azure integration](azure-integration.md)<br />
[Use plug-ins to extend business processes](plug-ins.md)<br />
[Work with Dataverse data in your Azure solution](work-data-azure-solution.md)<br />
[Write a listener application for a Azure solution](write-listener-application-azure-solution.md)<br />
[What is Azure Service Bus?](/azure/service-bus-messaging/service-bus-messaging-overview)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
