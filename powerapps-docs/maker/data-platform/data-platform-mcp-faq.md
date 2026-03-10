---
title: Connect to Dataverse with model context protocol FAQ
description: Frequently asked questions about using Microsoft Dataverse with a model context protocol server. 
author: seanwat-msft
ms.component: cds
ms.topic: how-to
ms.date: 03/07/2026
ms.subservice: dataverse-maker
ms.author: spatankar
ms. reviewer: matp
search.audienceType: 
  - maker
---
# Connect to Dataverse with model context protocol FAQ

This article provides answers to frequently asked questions about using Microsoft Dataverse with a model context protocol (MCP) server.

## I can’t authenticate. What is the problem?

Verify that the Dataverse environment URL in your MCP client configuration is correct. Go to [Power Apps](https://make.powerapps.com), select the correct environment, and then select **Settings** (gear icon) > **Session details** to confirm your instance URL.

Also verify that the MCP client you’re using is enabled in the Power Platform admin center. More information: [Configure and manage the Dataverse MCP server for an environment](data-platform-mcp-disable.md#configure-and-manage-the-dataverse-mcp-server)


## Which MCP tools are available and what do they do?

The Dataverse MCP server provides tools for common data operations such as querying records, creating and updating rows, describing table schemas, and listing tables. For the full list of tools and descriptions, go to [Connect to Dataverse with Model Context Protocol](data-platform-mcp.md#list-of-tools).

## Can I restrict which tables or records are accessible through the MCP server?

Yes. The Dataverse MCP server respects Dataverse security roles and row-level security. Users can only access tables and records that their security role permits. No additional MCP-specific access controls are needed beyond standard Dataverse security configuration.

## Are there costs associated with using the Dataverse MCP server?

Starting December 15, 2025, Dataverse MCP tools are charged when accessed by AI agents created outside of Microsoft Copilot Studio. If you have qualifying Dynamics 365 Premium licenses or a Microsoft 365 Copilot User Subscription License (USL), you aren’t charged for accessing Dynamics 365 data. For information about billing rates, go to [Connect to Dataverse with Model Context Protocol](data-platform-mcp.md#list-of-tools).

## Can I use the Dataverse MCP server with multiple environments?

Yes. Each Dataverse environment can have its own MCP server configuration. You can connect to multiple environments by configuring separate MCP server entries in your client, each pointing to a different environment URL.

## What should I do if a Dataverse MCP tool returns an error?

If a tool returns an error, try rephrasing your prompt and submitting it again. Use more specific language to describe what you want to accomplish. If the error persists, verify that you have the appropriate Dataverse permissions for the operation you’re attempting.

## Why don’t I see the Search tool in the Dataverse MCP server?

The Search tool is only available when Dataverse search is enabled for your environment. If Dataverse search isn’t turned on, the Search tool doesn’t appear in the list of available MCP tools. To enable Dataverse search, go to [Configure Dataverse search for your environment](/power-platform/admin/configure-relevance-search-organization).

## Why do I see different tools on the /api/mcp and /api/mcp_preview endpoints?

The /api/mcp endpoint provides the generally available set of Dataverse MCP tools, while the /api/mcp_preview endpoint includes additional preview tools that are being evaluated before general availability. Preview tools might change or be removed without notice. To access the preview tools, an administrator must enable the preview features setting in the Power Platform admin center. More information: [Use preview tools and upcoming features in Dataverse MCP server](data-platform-mcp-preview-tools.md)

## How do I enable debug logging for the local proxy?

If you experience issues with the local proxy (`@microsoft/dataverse`), you can enable debug logging to capture detailed output for troubleshooting. Add the `--log-level` and `--log-file` arguments to the proxy command:

```bash
npx @microsoft/dataverse mcp https://yourorg.crm.dynamics.com --log-level Debug --log-file
```

The log file is written to the system temporary directory. The default location depends on your operating system:

| Operating system | Log file location |
|---|---|
| Windows | `C:\Users\<username>\AppData\Local\Temp\` |
| Linux | `/tmp/` |
| macOS | The directory specified by the `$TMPDIR` environment variable, typically `/var/folders/.../T/`. Run `echo $TMPDIR` in a terminal to find the exact path. |

You can share the output log file with Microsoft when opening a support incident to help diagnose the issue.
