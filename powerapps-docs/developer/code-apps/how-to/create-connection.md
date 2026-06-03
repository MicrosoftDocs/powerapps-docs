---
title: "How to: Create a connection from the CLI (preview)"
description: "Use the npx power-apps create-connection command to create a connector connection from the command line. (preview)"
ms.author: eschavez
author: eschavez
ms.date: 06/02/2026
ms.reviewer: jdaly
ms.topic: how-to
---
# Create a connection from the CLI (preview)

Starting with [Power Apps client library for code apps](https://www.npmjs.com/package/@microsoft/power-apps?activeTab=readme) version 1.1.9, the new npm-based CLI includes a `create-connection` command. Use this command to create a connection for a connector directly from the command line, without leaving your terminal or opening the Power Apps maker portal.

The connection is created in the Power Platform environment that your code app is currently targeting (the environment set in `power.config.json` when you ran `npx power-apps init`).

## Prerequisites

- An initialized Power Apps code app. See [Quickstart: Create a code app by using the npm CLI](./npm-quickstart.md).
- The connector you want to use must support single sign-on (SSO). See [Limitations](#limitations).

## Usage

Run the command from the root of your code app project:

```bash
npx power-apps create-connection --api-id <connectorId> [--display-name <name>] [--json]
```

### Options

|Option|Alias|Required|Description|
|---|---|---|---|
|`--api-id`|`-a`|Yes|Connector API identifier (for example, `shared_office365`, `shared_teams`).|
|`--display-name`|`-n`|No|Optional display name for the new connection. If not specified, a default is used.|
|`--json`|—|No|Output the result as JSON for scripting scenarios.|

### Examples

Create an Office 365 connection:

```bash
npx power-apps create-connection --api-id shared_office365
```

Create a Teams connection with a custom display name:

```bash
npx power-apps create-connection --api-id shared_teams --display-name "My Teams"
```

Create a connection and emit JSON output (useful in scripts and CI):

```bash
npx power-apps create-connection --api-id shared_office365 --json
```

On success, the command prints the new connection's ID. You can then reference that connection ID when adding the connector as a data source to your code app.

## Limitations

- **Only non-interactive SSO connection creation is supported.** The `create-connection` command succeeds only for connectors whose single authentication type is SSO-eligible — typically Microsoft Entra ID (Azure AD) based connectors such as Office 365 Outlook, SharePoint, OneDrive for Business, and Microsoft Teams.
- **Connectors that require user-supplied credentials or configuration are not supported.** Examples include SQL Server with SQL authentication, custom connectors that require API keys, and any connector that exposes multiple authentication methods for the user to choose from. To create those connections, use the [Power Apps maker portal](https://make.powerapps.com) instead.
