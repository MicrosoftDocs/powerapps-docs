---
title: Work with data using the Dataverse CLI (preview)
description: Learn how to install and use the Dataverse CLI to work with data in Dataverse
ms.date: 07/31/2026
ms.reviewer: jdaly
ms.topic: overview
author: kewear
ms.author: kewear
search.audienceType: 
  - developer
contributors:
 - JimDaly
 - arorashivam96
ai-usage: ai-assisted
---
# Work with data by using the Dataverse CLI (preview)

> [!NOTE]
> - This is a preview feature.
> - [!INCLUDE [cc-preview-features-definition](../../../includes/cc-preview-features-definition.md)]

The Dataverse CLI is a cross-platform command-line tool for Microsoft Dataverse. Use it to manage authentication profiles, query and modify data, discover and invoke APIs, work with linked Finance and Operations (ERP) environments, and run a Model Context Protocol (MCP) server that lets AI assistants interact with your environment.

The CLI is distributed as the [`@microsoft/dataverse`](https://www.npmjs.com/package/@microsoft/dataverse) npm package. Key capabilities include:

- Profile-based authentication that's compatible with [Microsoft Power Platform CLI](/power-platform/developer/cli/introduction) authentication profiles.
- Environment commands (`org` / `env`) to view the current organization and list accessible environments.
- Data commands to query, get, create, update, upsert, delete, and count records; upload files to file columns; and associate or disassociate related records.
- Dynamic `api` commands to discover, describe, and invoke Dataverse custom APIs and ERP invocable service endpoints, or to send raw authenticated HTTP requests.
- `skill` commands to upload, download, list, and delete Dataverse skills used by AI agents.
- An MCP server for AI clients such as Claude Desktop.
- `--json` output on supported commands for scripting.

For a complete list of commands and their parameters, see the [Dataverse CLI reference](reference.md).

## Prerequisites

To install and run the CLI, you need [Node.js](https://nodejs.org/) (which includes npm) installed on a [supported platform](#supported-platforms).

Before you can authenticate and connect to a Dataverse environment with the MCP server, an administrator must complete the following three setup steps:

1. **Grant admin consent (Azure tenant admin).** An Azure tenant administrator grants admin consent for the Dataverse MCP CLI tool application by navigating to `https://login.microsoftonline.com/{your-tenant-id}/adminconsent?client_id=0c412cc3-0dd6-449b-987f-05b053db9457`, signing in, and accepting the requested permissions. Replace `{your-tenant-id}` with your actual Azure tenant ID.

1. **Enable the MCP server (Dataverse admin).** A Dataverse organization administrator enables the MCP server feature for the environment. See [Enable Dataverse MCP (production)](https://aka.ms/enableDataverseMcp) or [Enable Dataverse MCP (preview)](https://aka.ms/enableDataverseMcpPreview).

1. **Allow the MCP CLI tool (Dataverse admin).** A Dataverse organization administrator adds the Dataverse MCP CLI tool to the allowed client applications list by following [Configure MCP client list](https://aka.ms/configuremcpclientlist) and adding the application with App ID `0c412cc3-0dd6-449b-987f-05b053db9457`. It appears as **Dataverse MCP CLI tool** in the UI.

   Alternatively, a user with Dataverse admin permissions can add the application by using the [`mcp allow` command](reference.md#mcp-allow-command).

> [!NOTE]
> You must complete all three steps before you can successfully authenticate and connect to your Dataverse environment through the MCP server.

### Supported platforms

The Dataverse CLI supports the following platforms:

- Windows (x64, Arm64)
- macOS (x64, Arm64 / Apple silicon)
- Linux (x64, Arm64)

## Install the Dataverse CLI

Install the CLI globally by using npm:

```bash
npm install -g @microsoft/dataverse
```

Alternatively, run the CLI without installing it by using `npx`:

```bash
npx @microsoft/dataverse <command> [options]
```

To install a specific version, or to update to the latest version, use the [`install` command](reference.md#install-command):

```bash
dataverse install latest
dataverse install 1.0.0
```

The CLI automatically checks npm for newer versions when you run a command. If a newer version is available, it notifies you so that you can update.

## Use with Claude Desktop

You can run the CLI as an MCP server so that Claude Desktop can interact with your Dataverse environment.

The quickest way to add it is with the Claude CLI:

```bash
claude mcp add dataverse -t stdio -- npx -y @microsoft/dataverse mcp https://yourorg.crm.dynamics.com
```

To configure Claude Desktop manually, edit the MCP configuration file:

- Windows: `%APPDATA%\Claude\claude_desktop_config.json`
- macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
- Linux: `~/.config/Claude/claude_desktop_config.json`

Add the server to the `mcpServers` section:

```json
{
  "mcpServers": {
    "dataverse": {
      "command": "npx",
      "args": ["-y", "@microsoft/dataverse", "mcp", "https://yourorg.crm.dynamics.com"],
      "type": "stdio"
    }
  }
}
```

To capture detailed diagnostics, add the `--log-level Debug` and `--log-file` options to the `args` array. To use the preview MCP endpoint, add the `--preview` option. Restart Claude Desktop after you change the configuration.

For more information about starting the server, see the [`mcp` command](reference.md#mcp-command).

## Authentication

The CLI uses the Microsoft Authentication Library (MSAL) for authentication. It caches authentication profiles and tokens locally. These profiles work with Microsoft Power Platform CLI authentication profiles.

Create a profile the first time you connect by using the [`auth create` command](reference.md#auth-create-command):

```bash
dataverse auth create --environment https://myorg.crm.dynamics.com
```

This command opens a browser or system authentication dialog. After you sign in, the profile is saved. Subsequent commands, including `mcp`, use the cached tokens without prompting you again.

To work with more than one environment, create a named profile for each one. Switch between them by using the [`auth select` command](reference.md#auth-select-command):

```bash
dataverse auth create --environment https://dev.crm.dynamics.com --name dev
dataverse auth create --environment https://prod.crm.dynamics.com --name prod
dataverse auth select --name dev
```

For unattended scenarios such as CI/CD, authenticate with a service principal:

```bash
dataverse auth create --applicationId <appId> --clientSecret <secret> --tenant <tenantId> --environment https://myorg.crm.dynamics.com
```

For environments without a browser, use the device code flow by adding the `--deviceCode` option. To see all authentication options, including certificate, managed identity, and federated authentication, run `dataverse auth create --help`. To review, list, and remove profiles, see the [`auth who`](reference.md#auth-who-command), [`auth list`](reference.md#auth-list-command), and [`auth remove`](reference.md#auth-remove-command) commands.

## Get help

Every command and subcommand supports the `--help` option. It lists usage, options, and examples. For example:

```bash
dataverse --help
dataverse auth --help
dataverse auth create --help
dataverse org --help
dataverse mcp --help
dataverse data query --help
```

## Supported MCP operations

The MCP server supports the following operations:

- **Tools**: List and call Dataverse tools.
- **Prompts**: List and retrieve prompts.
- **Resources**: List and read Dataverse resources.

When the environment URL is a Finance and Operations (ERP) host, such as `https://myorg.operations.dynamics.com`, the `mcp` command automatically routes to the ERP MCP server.

## Troubleshooting

### Validate your setup

Before you start the server, validate authentication and MCP configuration by using the `--validate` option:

```bash
dataverse mcp https://yourorg.crm.dynamics.com --validate
```

This option checks the GA and preview endpoints and verifies that authentication works, the MCP server is enabled, and the MCP CLI tool is in the allowed applications list. If validation fails, the output identifies which prerequisite step to complete.

### Enable logging

If you encounter issues, enable file logging to capture detailed diagnostic information:

```bash
dataverse mcp https://yourorg.crm.dynamics.com --log-level Debug --log-file
```

Log files are written to your system's temporary directory. The exact location is displayed when logging starts.

### Common issues

**No compatible binary found for your platform**

The CLI supports Windows (x64, Arm64), macOS (x64, Arm64), and Linux (x64, Arm64). Other platforms aren't supported by the prebuilt binaries.

**Authentication failures**

- Confirm that you have access to the Dataverse environment.
- Confirm that the environment URL is correct.
- Clear your token cache and re-authenticate by using the [`auth create` command](reference.md#auth-create-command).

**MCP connection issues in Claude Desktop**

- Verify that the configuration JSON syntax is correct.
- Verify that the environment URL is accessible.
- Add the `--log-file` option to capture detailed error messages.
- Restart Claude Desktop after you change the configuration.

### See also

[Dataverse CLI reference](reference.md)

