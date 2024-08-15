---
title: Register a Dataverse service endpoint
description: Learn how to define a connection to an external system by registering a Dataverse service endpoint. In this scenario, we will establish a hybrid relay connection to an Azure listener app using the ServiceBus.
author: phecke
ms.author: pehecke
ms.subservice: dataverse-developer
ms.topic: how-to
ms.date: 08/14/2024
---

# Register a Dataverse service endpoint

 In this article, you will use the Plug-in Registration tool (PRT) to register a Dataverse service endpoint. You will configure the endpoint to use the default system plug-in, a REST contract, and an Azure hybrid relay connection.

A service endpoint configures a Dataverse connection to an external system. In this case, we are configuring the service endpoint to access a Azure hybrid relay connection using the ServiceBus. This enables Dataverse to post the execution context of its main operation on the service bus to be read by an active Azure listener app.

## Prerequisites

- Plug-in Registration tool installed on your development computer.
- Azure account with a license to create Service Bus entities.
- SAS configured Service Bus namespace.
- SAS configured Service Bus hybrid relay connection with Send and Listen policy permissions.

Detailed information on configuring the ServiceBus namespace and connection can be found in this article: [Configure an Azure hybrid relay connection](azure-configure-hybrid-relay.md).

To install the PRT, see [Dataverse development tools](download-tools-nuget.md).

## Obtain Azure namespace and connection information

We will now record the Azure connection information needed to create a service endpoint.

1. Logon to the Azure [portal](https://portal.azure.com).
1. Choose **ServiceBus** from the Azure services group or in the left navigation pane.
1. On the **Home** page, under the **Resources** group, select the relay that you configured. In this example, we named the relay "contoso-relay".
1. Select **Settings** > **Shared access policies**, and then choose **RootManagedSharedAccessKey**.
1. Record the values of the **Primary Key** and the **Primary Connection String** for the SAS policy named RootManageSharedAccessKey.
1. On the relay page, choose **Overview**, then near the page bottom below **Hybrid Connections** select the hybrid connection you configured.
1. On the **Hybrid Connection** page, record the **Hybrid Connection Url** value.

You can log out of the portal now.

## Launch the Plug-in Registration tool

Launch the PRT using the Power Platform CLI.

1. In Visual Studio Code or the standalone CLI, execute the following command to start the PRT.

`pac tool prt`

## Register a service endpoint

Now we can create a service endpoint using the PRT.

1. Step 1
1. Step 2
1. Step 3

<!-- 5. Next step/Related content------------------------------------------------------------------------

Optional: You have two options for manually curated links in this pattern: Next step and Related content. You don't have to use either, but don't use both.
  - For Next step, provide one link to the next step in a sequence. Use the blue box format
  - For Related content provide 1-3 links. Include some context so the customer can determine why they would click the link. Add a context sentence for the following links.

-->

## Next step

TODO: Add your next step link(s)

> [!div class="nextstepaction"]
> [Write concepts](article-concept.md)

<!-- OR -->

## Related content

TODO: Add your next step link(s)

- [Write concepts](article-concept.md)
