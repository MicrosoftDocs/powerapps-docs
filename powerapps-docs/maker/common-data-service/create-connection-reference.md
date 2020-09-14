---
title: "Connection references in solutions | MicrosoftDocs"
description: "Create a connection reference in Power Apps"
ms.custom: ""
ms.date: 08/27/2020
ms.reviewer: "matp"
ms.service: powerapps
ms.topic: "article"
author: "caburk"
caps.latest.revision: 57
ms.author: "caburk"
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---
# Create a connection reference from a solution

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

A connection  is a proxy or a wrapper around an API that allows the underlying service to talk to Microsoft Power Automate, Microsoft Power Apps, and Azure Logic Apps. It provides a way for users to connect their accounts and use a set of pre-built actions and triggers to build their apps and workflows.

A connection reference is a solution component that contains information about a connector. Both canvas app and operations within a Power Automate flow bind to a connection reference. You can import your connection reference into a target environment with no further configuration needed after the import completes. To change a specific connection associated with a canvas app or flow, you edit the connection reference component within the solution.

> [!NOTE]
>
> - Canvas apps and flows handle connections differently. Flows use connection references for all connectors, whereas canvas apps only use them for implicitly shared connections, such as SQL Server. More information: [Security and types of authentication](../canvas-apps/connections-list#security-and-types-of-authentication)
> - A connection reference is automatically created when you create new connections from the flow and canvas app designers.

1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), and on the left pane select **Solutions**. 
2. Create a new or open an existing solution.
3. On the command bar select **New**, and then in the list of components select Connection Reference. 
4. On the **New Connection Reference** pane, enter the following information. Required fields a denoted with an asterisk (*).
   - **Display name**: Enter a friendly name to help differentiate this connection reference from others.
   - **Description**: Enter text that describes the connection.
   - **Connector**: Choose from the following options:
       - Select an existing connector from the list.
       - Select **New** to create a new connection to use for this connection reference. Once your finished creating the connection, select **Refresh** to select your new connection from the list.  
5. Select **Create**.

## Limits

During the preview, the same connection reference can be used a maximum of 16 times in flows.

### See also

[Connectors](/connectors/connectors)
