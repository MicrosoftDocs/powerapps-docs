---
title: Use a connection reference in a solution
description: Learn how to create a connection reference.
ms.custom: ""
ms.date: 07/28/2023
ms.reviewer: angieandrews
ms.topic: conceptual
author: ChrisGarty
contributors:
  - ChrisGarty
  - v-aangie
caps.latest.revision: 57
ms.subservice: dataverse-maker
ms.author: cgarty
search.audienceType: 
  - maker
---
# Use a connection reference in a solution

A *connector* is a proxy or a wrapper around an API that allows the underlying service to talk to Microsoft Power Automate, Microsoft Power Apps, and Azure Logic Apps. It provides a way for users to connect their accounts and use a set of prebuilt actions and triggers to build their apps and workflows.

A [connection](/power-automate/add-manage-connections) is a stored [authentication credential](/connectors/custom-connectors/connection-parameters#authentication-types) for a connector, for example OAuth credentials for the SharePoint connector.

A *connection reference* is a solution component that contains a reference to a connection about a specific connector. Both solution-aware canvas apps and operations within a [solution-aware flow](/power-automate/overview-solution-flows) bind to a connection reference instead of directly to a connection. During solution import into a target environment, a connection is provided for all the connection references so any referencing flows can be [turned on](/power-automate/disable-flow#turn-flows-on) automatically after the import completes. To change a specific connection associated with a canvas app or flow, you edit the connection reference component within the solution.

## Add connection references to a solution

Connection references can be added to a solution in different ways:
- When you're using the solution explorer to create a new connection reference in a solution.

- When you import a solution. To learn more, go to [Import solutions](import-update-export-solutions.md).

- Implicitly when you build your [canvas apps](../canvas-apps/add-app-solution.md) and [flows](/power-automate/create-flow-solution) that are defined in a Microsoft Dataverse solution.

> [!NOTE]
>
> - Canvas apps and flows handle connections differently. Flows use connection references for all connectors, whereas canvas apps only use them for implicitly shared (non-OAuth) connections, such as SQL Server Authentication. More information: [Security and types of authentication](../canvas-apps/connections-list.md#security-and-types-of-authentication)
> - A connection reference is automatically created when you create new connections from the flow and canvas app designers.
> - Canvas apps and flows added from outside solutions will not automatically be upgraded to use connection references. 
> - Connection references get associated with canvas apps only at the time a data source is added to the app. To upgrade apps you must remove the connection from the app and then add a connection containing an associated connection reference. 

## Manually add a connection reference to a solution using solution explorer

1. Sign in to [Power Apps](https://make.powerapps.com/) or [Power Automate](https://make.powerautomate.com/).

1. On the left pane, select **Solutions**. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]

1. Create a new or open an existing solution.

1. On the command bar, select **New** > **More** > **Connection Reference**.

1. On the **New Connection Reference** pane, enter the following information. Required columns are denoted with an asterisk (*).
   - **Display name**: Enter a unique and useful name to help differentiate this connection reference from others.
   - **Add a description**: Enter text that describes the connection.
   - **Connector**: Select an existing connector from the list such as in the screenshot here. You can also select **New** to create a new connection for this connection reference. Once your finished creating a new connection, select **Refresh** to select your connection from the list.  
   - **Connection**: Based on the **Connector** you selected, select an existing connection or select **New connection** to create one.

1. Select **Create**.
  
    :::image type="content" source="media/connection-reference-example.png" alt-text="Screenshot of the New Connection Reference panel.":::

## Connection reference naming

The display name of a connection reference should be unique so different connection references can be differentiated by name alone. By default, a connection reference name includes the target connector, the current solution name for context, and a random suffix to ensure uniqueness. Consider adjusting the connection reference name to something unique and something that explains what it will be used for.

## Reuse connections in a solution flow

Flows created outside a solution use connections directly. Flows created in a solution use connection references and the connection reference points at the connection. To reuse a connection within a solution flow, you first need to create a connection reference pointing at that connection.

## Update a flow to use connection references instead of connections

When a flow isn't in a solution, it uses connections. If that flow is then added into solution, it will continue to use connections initially.
Flows can be updated to use connections references instead of connections in one of two ways:

1. If the flow is exported in an unmanaged solution and imported, the connections will be removed and replaced with connection references.

1. When a solution flow is opened, the flow checker on the flow details page will show a warning to **Use connection references**. The warning message contains an action to **Remove connections so connection references can be added**. Selecting that action will remove connections from the trigger and actions in the flow and allow connection references to be selected and created.

## Automatic use of connection references in a solution flow

When an action is added to a solution flow, Power Automate will try to reuse existing connection references from the current solution or other solutions before creating a new connection reference. To ensure that the connection reference is inside the same solution as the flow, create or add a connection reference in the same solution and reference that connection reference from the flow.

## Share connections with another user so flows can be enabled

When a flow is turned on (enabled), the user turning on the flow needs to own all the connections. This is usually accomplished by having the flow owner create the connections inside all the connection references that the flow uses. If a user other than the flow owner provides the connections on a flow, then the flow needs to be turned on by the owner of those connections or the connections need to be shared with the user who is turning on the flow. 

> [!NOTE]
>
> Connections can only be explicitly shared with a user representing a service principal.

### Manual sharing of connections for flow enablement

Sharing connections can be accomplished with the following steps.

1. Go to  [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) and select the environment containing the connection.

1. Select **Connections** on the left navigation pane, and then select the connection you want to share. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]

1. From the menu, select **Share**.

1. From the sharing screen, enter the name of the user (service principal) who will enable the flow.

1. For the permissions, select **Can use**.

1. To complete the sharing, select **Save**.

### Automated sharing of connections for flow enablement

To automate sharing of connections, use the [Edit Connection Role Assignment action](/connectors/powerappsforappmakers/#edit-connection-role-assignment) on the Power Apps for Makers connector. 

<!-- This article can't be found -- You can find an automated connection sharing example in the **ShareConnectionWithServicePrincipal** flow in the [ALM Accelerator for Power Platform](/power-platform/guidance/coe/setup-almacceleratorpowerplatform-preview). -->

:::image type="content" source="media/share-connections-with-service-principal-flow.png" alt-text="Screenshot of a connection sharing example.":::

## Limits

- Connection references are now saved asynchronously. Unlike during the preview period, there's no longer a limit to how many flows can reference the same connection reference. When connection references are updated, an info banner that links to a panel containing asynchronous update details appears.
- There is also no limit to the number of actions in each flow that can be associated with the connection reference.
- Canvas apps don't recognize connection references on custom connectors. To work around this limitation, after a solution is imported to an environment the app must be edited to remove and then re-add the custom connector connection. Note, if this app is in a managed solution, proceeding to edit the app will create an unmanaged layer. More information: [Solution layers](solution-layers.md)

## FAQ

### Can a flow be enabled by the owner of its connections and then ownership transferred to another user?

Yes. When a flow is turned on (enabled) by the owner of the connections used by the flow, then the flow gets explicit permission to use those connections. Co-owners of the flow can then turn the flow off and on as needed.

Permissions granted to apps and flows using a connection can be seen in the details page for that connection in the **Apps using this connection** and **Flows using this connection** tabs.

If the flow is edited to add new actions that use additional connection references with new connections, then the owner of those new connections either needs to initially turn on the flow themselves or share the connections with the owner who turns on the flow. More information: [Share app resources](/power-apps/maker/canvas-apps/share-app-resources#connections)

## See also

[Connectors](/connectors/connectors)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
