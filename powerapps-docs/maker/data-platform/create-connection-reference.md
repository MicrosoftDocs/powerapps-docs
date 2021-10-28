---
title: "Connection references in solutions | MicrosoftDocs"
description: "Create a connection reference"
ms.custom: ""
ms.date: 08/02/2021
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

A connection is a proxy or a wrapper around an API that allows the underlying service to talk to Microsoft Power Automate, Microsoft Power Apps, and Azure Logic Apps. It provides a way for users to connect their accounts and use a set of pre-built actions and triggers to build their apps and workflows.

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

1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) or [Power Automate](https://flow.microsoft.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), and on the left pane select **Solutions**.
1. Create a new or open an existing solution.
1. On the command bar select **New**, and then in the list of components select **Connection Reference**.
1. On the **New Connection Reference** pane, enter the following information. Required columns are denoted with an asterisk (*).
   - **Display name**: Enter a friendly name to help differentiate this connection reference from others.
   - **Add a description**: Enter text that describes the connection.
   - **Connector**: Select an existing connector from the list such as in the screenshot here. You can also select **New** to create a new connection for this connection reference. Once your finished creating a new connection, select **Refresh** to select your connection from the list.  
   - **Connection**: Based on the **Connector** you selected, select an existing connection or select **New connection** to create one.
   :::image type="content" source="media/connection-reference-example.png" alt-text="Connection reference example":::

1. Select **Create**.

## Limits

Connection references are now saved asynchronously, so unlike during the preview period, there is no longer a limit to how many flows can reference the same connection reference. When connection references are updated, an info banner will be shown that links to a panel containing asynchronous update details.
There is also no limit to the number of actions in each flow that can be associated with the connection reference.

## Updating a flow to use connection references instead of connections

When a flow is not in a solution it uses connections. If that flow is then added into solution, it will continue to use connections intially. 
Flows can be updated to use connections references instead of connections in one of two ways:
1. If the flow is exported in an unmanaged solution and imported, the connections will be removed and replaced with connection references. 
2. When a solution flow is opened, the flow checker on the flow details page will show a warning to **Use connection references**. The warning message contains an action to **Remove connections so connection references can be added**. Clicking that action will remove connections from the trigger and actions in the flow and allow connection references to be selected and created.

## Connection Reference usage tips

### Reusing connections in a solution flow

Flows created outside a solution use Connections directly. Flows created in a solution use Connection References and the Connection Reference points at the Connection. To reuse a Connection within a solution flow, you first need to create a connection reference pointing at that connection.

### Automatic use of Connection References in a solution flow

When an action is added to a solution flow, Power Automate will try to reuse existing Connection References from the current solution or other solutions before creating a new Connection Reference. To ensure that the Connection Reference is inside the same solution as the flow, create or add a Connection Reference in the same solution and reference that Connection Reference from the flow.

### Enabling flows containing connections from another user

When a flow is enabled, the enabling user needs to own all the connections. This is usually accomplished by having the flow owner create the connections inside all the connection references that the flow uses. 
Directly sharing a connection with someone else is not currently possible. So if a user other than the owner needs to provide the connections, then [an admin account can impersonate that user](/powerapps/developer/data-platform/impersonate-another-user) and then enable the flow. This impersonation mechanism is one that is used to [activate flows in the ALM accelerator](https://github.com/microsoft/coe-alm-accelerator-templates/blob/main/Pipelines/Templates/activate-flows.yml).

### See also

[Connectors](/connectors/connectors)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
