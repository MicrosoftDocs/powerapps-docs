---
title: "Connection references in solutions | MicrosoftDocs"
description: "Create a connection reference in Power Apps"
ms.custom: ""
ms.date: 08/27/2020
ms.reviewer: "matp"
ms.service: powerapps
ms.topic: "how-to"
author: "caburk"
caps.latest.revision: 57
ms.subservice: dataverse-maker
ms.author: "caburk"
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---
# Use a connection reference in a solution

[!INCLUDE[cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

A connection  is a proxy or a wrapper around an API that allows the underlying service to talk to Microsoft Power Automate, Microsoft Power Apps, and Azure Logic Apps. It provides a way for users to connect their accounts and use a set of pre-built actions and triggers to build their apps and workflows.

A connection reference is a solution component that contains information about a connector. Both canvas app and operations within a Power Automate flow bind to a connection reference. You can import your connection reference into a target environment with no further configuration needed after the import completes. To change a specific connection associated with a canvas app or flow, you edit the connection reference component within the solution.

You can add a connection reference to a solution in a few different ways:
- From the **Solutions** area as described in this article.
- During solution import. More information: [Import solutions](import-update-export-solutions.md)
- When you build your [canvas apps](../canvas-apps/add-app-solution.md) and [flows](/power-automate/create-flow-solution) in a solution.

> [!NOTE]
>
> - Canvas apps and flows handle connections differently. Flows use connection references for all connectors, whereas canvas apps only use them for implicitly shared (non-OAuth) connections, such as SQL Server Authentication. More information: [Security and types of authentication](../canvas-apps/connections-list.md#security-and-types-of-authentication)
> - A connection reference is automatically created when you create new connections from the flow and canvas app designers.
> - Canvas apps and flows added from outside solutions will not automatically be upgraded to use connection references. 
> - Connection references get associated with canvas apps only at the time a data source is added to the app. To upgrade apps you must remove the connection from the app and then add a connection containing an associated connection reference. 

1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), and on the left pane select **Solutions**. 
2. Create a new or open an existing solution.
3. On the command bar select **New**, and then in the list of components select Connection Reference. 
4. On the **New Connection Reference** pane, enter the following information. Required columns are denoted with an asterisk (*).
   - **Display name**: Enter a friendly name to help differentiate this connection reference from others.
   - **Description**: Enter text that describes the connection.
   - **Connector**: Choose from the following options:
       - Select an existing connector from the list.
       - Select **New** to create a new connection to use for this connection reference. Once your finished creating the connection, select **Refresh** to select your new connection from the list.  
5. Select **Create**.

## Limits

While connection references are in preview, one connection reference can only be used within a maximum of 16 flows. If the same connection needs to be used in more than 16 flows, then create another connection reference with a connection to the same connector. There is no limit to the number of actions in each flow that can be associated with the connection reference.

## Connection Reference usage tips

### Reusing connections in a solution flow 
Flows created outside a solution use Connections directly. Flows created in a solution use Connection References and the Connection Reference points at the Connection. To reuse a Connection within a solution flow, you first need to create a connection reference pointing at that connection.

### Automatic use of Connection References in a solution flow
When an action is added to a solution flow, Power Automate will try to reuse existing Connection References from the current solution or other solutions before creating a new Connection Reference. To ensure that the Connection Reference is inside the same solution as the flow, create or add a Connection Reference in the same solution and reference that Connection Reference from the flow.

### See also

[Connectors](/connectors/connectors)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
