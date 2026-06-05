---
title: Connect to Dataverse with model context protocol in non-Microsoft clients
description: Learn how to connect to Dataverse using the Model Context Protocol (MCP) server in non-Microsoft clients such as Claude desktop or Claude Code. Follow step-by-step instructions to connect using the npm local proxy or the remote endpoint with a custom Entra app.
#customer intent: As a Power Apps maker, I want to connect to Dataverse using the Model Context Protocol server so that I can choose from different MCP clients that can interact with my data through natural language queries.
author: seanwat-msft
ms.author: spatankar
ms.reviewer: matp
ms.date: 03/07/2026
ms.topic: how-to
ms.collection: bap-ai-copilot
ms.subservice: dataverse-maker
---

# Connect to Dataverse with model context protocol in non-Microsoft clients

You can connect to Microsoft Dataverse using a non-Microsoft model context protocol (MCP) client, such as Claude desktop or Claude Code. There are two approaches for connecting non-Microsoft clients to a Dataverse MCP server:

- **Local proxy**: Use the `@microsoft/dataverse` npm package to run a local proxy that connects to the Dataverse MCP server on your behalf.
- **Remote endpoint**: Connect directly to the Dataverse MCP server remote endpoint (`/api/mcp`) by registering a custom Microsoft Entra app.

## Prerequisites

- The Dataverse MCP server must be enabled for the environment. More information: [Configure and manage the Dataverse MCP server for an environment](data-platform-mcp-disable.md#configure-and-manage-the-dataverse-mcp-server)
- For the local proxy approach: [Node.js](https://nodejs.org/) (version 18 or later) installed on your machine.
- For the remote endpoint approach: Access to register an application in [Microsoft Entra ID](/entra/identity-platform/quickstart-register-app).

## Connect using the local proxy

The `@microsoft/dataverse` npm package provides a local proxy that handles authentication and communication with the Dataverse MCP server. This approach is recommended for most non-Microsoft MCP clients that can run local MCP servers.

### Grant tenant admin consent

A tenant administrator must grant admin consent for the Dataverse CLI app before users can authenticate. Navigate to the following URL in a browser, replacing `{your-tenant-id}` with your Microsoft Entra tenant ID:

`https://login.microsoftonline.com/{your-tenant-id}/adminconsent?client_id=0c412cc3-0dd6-449b-987f-05b053db9457`

Sign in with a tenant administrator account and accept the permissions prompt. This step only needs to be completed once per tenant.

### Enable the Dataverse CLI client in the Power Platform admin center

Before you can connect using the local proxy, the **Dataverse CLI** client must be enabled as an allowed MCP client in your environment.

1. Go to [Power Platform admin center](https://admin.powerplatform.microsoft.com/). Select **Manage** > **Environments**.
1. Select the environment where you want to enable the client, and then select **Settings**.
1. Under **Settings**, select **Product** > **Features**. Scroll down to locate **Dataverse Model Context Protocol** and select **Advanced Settings**.
1. Locate the **Dataverse CLI** client (app ID `0c412cc3-0dd6-449b-987f-05b053db9457`) and set **Is Enabled** to **Yes**.
1. Select **Save & Close**.

> [!NOTE]
> If the **Dataverse CLI** entry doesn't appear in the list of available clients, you can add it manually. Create a new client entry with any name and specify the app ID `0c412cc3-0dd6-449b-987f-05b053db9457`, and then enable it.

### Install the local proxy

You can install the `@microsoft/dataverse` package globally or run it directly with `npx`.

To install globally, run the following command in a terminal:

```bash
npm install -g @microsoft/dataverse
```

Alternatively, you can use `npx` to run the proxy without installing it globally:

```bash
npx @microsoft/dataverse mcp https://yourorg.crm.dynamics.com
```

> [!TIP]
> To connect to the preview endpoint (`/api/mcp_preview`) instead of the generally available endpoint (`/api/mcp`), add the `--preview` parameter to the command. For example: `npx @microsoft/dataverse mcp https://yourorg.crm.dynamics.com --preview`. The preview endpoint must be enabled in your environment. More information: [Use preview tools and upcoming features in Dataverse MCP server](data-platform-mcp-preview-tools.md)

### Configure the local proxy in Claude desktop

This section describes how to configure the Dataverse MCP server local proxy in Claude desktop. If you haven't already done so, [download and install Claude desktop](https://claude.ai/download).

1. Open Claude desktop and go to **File** > **Settings** > **Developer**.
1. Select **Edit Config** to open the `claude_desktop_config.json` file.
1. Add the following JSON snippet to the file. Replace `<friendly name>` with a name you can easily remember (for example, *MyDataverseMCPServer*) and replace `<your org URL>` with your Dataverse environment URL (for example, `https://contoso.crm.dynamics.com`).

   ```json
   {
     "mcpServers": {
       "<friendly name>": {
         "command": "npx",
         "args": [
           "-y",
           "@microsoft/dataverse",
           "mcp",
           "<your org URL>"
         ]
       }
     }
   }
   ```

1. Save the file.

#### Verify the connection in Claude desktop

1. Exit Claude desktop by selecting **File** > **Exit**, and then reopen it to apply the changes.
1. Sign in with your credentials when prompted to authenticate to your Dataverse environment.
1. Select **Search and tools** to verify that the Dataverse MCP server and its tools are available. You should see the friendly name you configured (for example, *MyDataverseMCPServer*).
1. Select the MCP server name to view the list of tools that are supported by the server.

> [!TIP]
> You can enable and disable individual tools for each MCP server registered with Claude desktop. This gives you control over which tools are available for use.

### Configure the local proxy in Claude Code

This section describes how to configure the Dataverse MCP server local proxy in Claude Code. If you haven't already done so, [download and install Claude Code](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview).

Run the following command to add the Dataverse MCP server. Replace `https://yourorg.crm.dynamics.com` with your Dataverse environment URL.

```bash
claude mcp add dataverse -t stdio -- npx -y @microsoft/dataverse mcp https://yourorg.crm.dynamics.com
```

### Verify and interact with the connection in Claude Code

1. Restart Claude Code to apply the changes.
1. Sign in with your credentials when prompted to authenticate to your Dataverse environment.
1. Verify that the Dataverse MCP server and its tools are available. You should see the friendly name you configured (for example, *MyDataverseMCPServer*).
1. Select the MCP server name to view the list of tools that are supported by the server.

If you have data in the Dataverse environment, you can test the setup by asking *list tables in Dataverse*, *describe table account*, or *how many accounts do I have*. More information: [Add and remove sample data](/power-platform/admin/add-remove-sample-data)

> [!TIP]
> If you have other MCP servers registered with Claude Code, include *Dataverse* in your prompt to specify which MCP server to use.

## Connect using the remote endpoint

You can connect non-Microsoft MCP clients directly to the Dataverse MCP server remote endpoint without using a local proxy. This approach requires you to register a custom application in Microsoft Entra ID and add its client ID to the allowed clients list in the Power Platform admin center.

### Register a custom Microsoft Entra app

Register an application in Microsoft Entra ID to use for authentication when connecting to the Dataverse MCP server. For general information about app registration, go to [Register an application with the Microsoft identity platform](/entra/identity-platform/quickstart-register-app).

Follow these steps to register an app for use with the Dataverse MCP server:

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com/).
1. Go to **Identity** > **Applications** > **App registrations**, and then select **New registration**.
1. Enter a name for your application (for example, *Dataverse MCP Client*), configure the supported account types for your scenario, and then select **Register**.
1. On the **Overview** page, note the **Application (client) ID**. You need this value to configure the allowed client in the Power Platform admin center and to configure your MCP client.

### Configure API permissions for the Dataverse MCP server

After you register the app, you must grant it permissions to access the Dataverse MCP server.

1. In the app registration, select **API permissions** from the left navigation pane.
1. Select **Add a permission**.
1. Select **Microsoft APIs**, and then select **Dynamics CRM**.
1. Select the **mcp.tools** permission, and then select **Add permissions**.

> [!NOTE]
> The authentication flow used by the Entra app depends on the MCP client you're using. Refer to your MCP client's documentation for the supported authentication methods.

### Add the custom app to the allowed clients list

After you register the Entra app, add its client ID to the list of allowed MCP clients for your environment.

1. Go to [Power Platform admin center](https://admin.powerplatform.microsoft.com/). Select **Manage** > **Environments**.
1. Select the environment where you want to allow the client, and then select **Settings**.
1. Under **Settings**, select **Product** > **Features**. Scroll down to locate **Dataverse Model Context Protocol** and select **Advanced Settings**.
1. Add a new client entry. Enter a name for the client and specify the **Application (client) ID** from your Entra app registration.
1. Set **Is Enabled** to **Yes**.
1. Select **Save & Close**.

### Connect to the remote endpoint

Configure your MCP client to connect to the Dataverse MCP server at the following URL:

`https://<your org URL>/api/mcp`

For example: `https://contoso.crm.dynamics.com/api/mcp`

Use the **Application (client) ID** from your Entra app registration for authentication. Refer to your MCP client's documentation for specific configuration steps.

## Related articles

[Connect to Dataverse with Model Context Protocol](data-platform-mcp.md)