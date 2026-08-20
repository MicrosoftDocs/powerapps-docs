---
title: "How to: Create a Connection from the Power Apps CLI"
description: Learn how to use the Power Apps CLI to list connectors and create a connection for your Power Apps code app. Follow the steps to get started.
#customer intent: As a developer, I want to create Power Platform connections without leaving the command line.
ms.topic: how-to
ms.service: powerapps
ms.subservice: code-apps
ms.author: jordanchodak
ms.reviewer: jdaly
author: jordanchodakWork
ms.date: 08/19/2026
---

# How to: Create a connection from the Power Apps CLI

Use the Power Apps CLI to find connectors and create a connection without leaving your terminal or opening [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).

## Prerequisites

An initialized Power Apps code app. See [Quickstart: Create a code app by using the Power Apps CLI](create-an-app-from-scratch.md).

## Step 1: List available connectors

Run the commands in this article from the root of your code app project.

Use [`pa connector list` command](../reference/cli.md#pa-connector-list) to find the connectors available in the Power Platform environment configured for your code app:

```bash
pa connector list [--search <term>] [--json]
```
The environment is set in `power.config.json` when you run [`pa app init`](../reference/cli.md#pa-app-init).

In an interactive terminal, results appear in pages of 20 rows. Press <kbd>Enter</kbd> to show the next page. Press <kbd>Esc</kbd> or <kbd>Q</kbd> to exit. When you redirect the output or include `--json`, the command returns the complete list.  [Learn more about the output options for the `pa connector list` command](../reference/cli.md#pa-connector-list-output)

### List connectors examples

List all available connectors:

```bash
pa connector list
```

Search for connectors:

```bash
pa connector list --search teams
```

Return the connector list as JSON:

```bash
pa connector list --json
```

## Step 2: Create the connection

Use [`pa connection create`](../reference/cli.md#pa-connection-create) to create a connection in the environment configured for the code app:

```bash
pa connection create --connector <connector-id> [--display-name <name>] [--json]
```

### Create connectors examples

Create an Office 365 Outlook connection:

```bash
pa connection create --connector shared_office365
```

Create a Microsoft Teams connection with a custom display name:

```bash
pa connection create --connector shared_teams --display-name "My Teams"
```

Create a connection and return the result as JSON:

```bash
pa connection create --connector shared_office365 --json
```

When the command succeeds, it returns the connection ID. Use the connection ID when you add the connector as a data source to the code app.

## Related information

- [Connect your code app to data](connect-to-data.md)
- [Quickstart: Create a code app by using the Power Apps CLI](create-an-app-from-scratch.md)
- [Power Apps CLI command reference](../reference/cli.md)
