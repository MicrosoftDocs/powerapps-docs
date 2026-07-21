---
title: "How to: Create a connection from the CLI (preview)"
description: "Use the power-apps create-connection command to create a connector connection from the command line. (preview)"
ms.author: eschavez
author: eschavez
ms.date: 07/20/2026
ms.reviewer: jdaly
ms.topic: how-to
---
# Create a connection from the CLI (preview)

Use the [Power Apps client library for code apps](https://www.npmjs.com/package/@microsoft/power-apps?activeTab=readme) `create-connection` command to create a connection for a connector directly from the command line, without leaving your terminal or opening [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) as described in [How to: Connect your code app to data](connect-to-data.md).

Starting with version 1.2.7, use the `list-connectors` command to see connectors available in your environment.

## Prerequisites

An initialized Power Apps code app. See [Quickstart: Create a code app by using the npm CLI](./npm-quickstart.md).

## List available connectors

Before you create a connection, use the `list-connectors` command to see which connectors are available in your Power Platform environment and to find a connector's API identifier. This is the value you pass to `create-connection` command `api-id` option.

The `list-connectors` command lists connectors from the Power Platform environment that your code app is currently targeting. This is the environment set in `power.config.json` when you ran `power-apps init`.

### Usage

Run the command from the root of your code app project:

```bash
power-apps list-connectors [--search <term>] [--json]
```

### Options

Use the following options with `list-connectors`.

| Option | Alias | Required | Description |
|--------|-------|----------|-------------|
| `--search` | `-s` | No | Filter the results to connectors whose name or display name matches the search term. |
| `--json` | — | No | Output the full connector list as JSON for scripting scenarios. |

### Output

By default, the command prints a table with two columns:

| Column | Description |
|---|---|
| Display Name | The connector's friendly name, for example, *Office 365 Outlook*. |
| Connector | The connector's unique name / API identifier, for example, `shared_office365`. This is the value you pass to `create-connection` command `--api-id` option. |

When you run the command in an interactive terminal, it returns results in pages of 20 rows. Press <kbd>Enter</kbd> to show the next page, or <kbd>Esc</kbd>/<kbd>q</kbd> to exit. When you redirect the output (non-interactive), or you pass `--json`, the command emits the full list at once.

The `--json` output includes additional fields for each connector beyond the two table columns:

| Field | Description |
|-------|-------------|
| `id` | The connector's ID. |
| `name` | The connector's unique name (API identifier), for example `shared_office365`. |
| `displayName` | The connector's friendly display name. |
| `description` | The connector's description. |
| `isTabular` | Indicates whether the connector supports tabular (table) data operations. |

### Examples

List all connectors available in the current environment:

```bash
power-apps list-connectors
```

Search for connectors by name:

```bash
power-apps list-connectors --search teams
```

Emit the full connector list as JSON. This is useful in scripts and  continuous integration (CI):

```bash
power-apps list-connectors --json
```

 ## Create the connection

Use the `create-connection` command to create a connection for a connector directly from the command line, without leaving your terminal or opening the Power Apps maker portal.

The connection is created in the Power Platform environment that your code app is currently targeting. This environment is set in `power.config.json` when you run `power-apps init`.

## Usage

Run the command from the root of your code app project:

```bash
power-apps create-connection --api-id <connectorId> [--display-name <name>] [--json]
```

### Options

Use the following options with `create-connection`.

|Option|Alias|Required|Description|
|---|---|---|---|
|`--api-id`|`-a`|Yes|Connector API identifier (for example, `shared_office365`, `shared_teams`).|
|`--display-name`|`-n`|No|Optional display name for the new connection. If not specified, a default is used.|
|`--json`|—|No|Output the result as JSON for scripting scenarios.|

### Examples

Create an Office 365 connection:

```bash
power-apps create-connection --api-id shared_office365
```

Create a Teams connection with a custom display name:

```bash
power-apps create-connection --api-id shared_teams --display-name "My Teams"
```

Create a connection and emit JSON output.  This is useful in scripts and  continuous integration (CI):

```bash
power-apps create-connection --api-id shared_office365 --json
```

On success, the command prints the new connection's ID. You can then reference that connection ID when adding the connector as a data source to your code app.

