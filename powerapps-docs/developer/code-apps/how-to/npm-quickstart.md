---
title: Create a code app by using the Power Apps CLI
description: Learn how to create, run, and publish a Power Apps code app by using the Power Apps CLI.
#customer intent: As a developer, I want to create and publish a Power Apps code app from the command line.
ms.topic: quickstart
ms.author: jordanchodak
ms.reviewer: jdaly
author: jordanchodakWork
ms.date: 08/03/2026
---

# Quickstart: Create a code app by using the Power Apps CLI

This article shows you how to install the Power Apps CLI, create a blank app from a Vite template, run the app locally, and publish it to Power Apps.

For a complete list of commands, see [Power Apps CLI command reference](../reference/cli.md).

## Prerequisites

- A Power Platform environment with code apps enabled
- [Node.js](https://nodejs.org/) Long Term Support (LTS) version
- [Git](https://git-scm.com/)

## Step 1: Create the project

Open a terminal and run the following commands:

```bash
npx degit github:microsoft/PowerAppsCodeApps/templates/vite my-app
cd my-app
```

For more information, see the [degit npm package](https://www.npmjs.com/package/degit).

## Step 2: Install dependencies and initialize the code app

Install the Power Apps CLI and the project dependencies:

```bash
npm install --global @microsoft/power-apps-cli
npm install --global @microsoft/power-apps
npm install
```

Use [`pa app init`](../reference/cli.md#pa-app-init) to initialize the code app. You can use interactive prompts or provide the required options in the command.

**Use interactive prompts:**

```bash
pa app init
```

**Provide options in the command:**

```bash
pa app init --display-name "App From Scratch" --environment-id <environment-id>
```

When you run [`pa app init`](../reference/cli.md#pa-app-init), the CLI prompts you to sign in if you're not already authenticated. Sign in by using your Power Platform account.

## Step 3: Run the app locally

Use [`pa app run`](../reference/cli.md#pa-app-run) to run the code app:

```bash
pa app run
```

Open the URL labeled **Local Play**.

> [!IMPORTANT]
> Open the URL in the same browser profile that you use for your Power Platform tenant.

> [!NOTE]
> **Local network access restrictions**
>
> Chrome and Microsoft Edge block requests from public origins to local endpoints by default.
>
> - Because your code app connects to localhost during development, you might need to grant browser permission or configure enterprise policies.
> - For embedded scenarios, include `allow="local-network-access"` in iframe tags.
> - For more information, see [Control a website's access to the local network in Microsoft Edge](https://support.microsoft.com/topic/control-a-website-s-access-to-the-local-network-in-microsoft-edge-ef7eff4c-676d-4105-935c-2acbcd841d51) and [New permission prompt for Local Network Access in Chrome](https://developer.chrome.com/blog/local-network-access).

The app opens in your browser.

:::image type="content" source="media/npm-run-dev-result.png" alt-text="A code app running locally in a browser":::

## Step 4: Build and publish the app

Build the app:

```bash
npm run build
```

Use [`pa app push`](../reference/cli.md#pa-app-push) to publish the compiled app to Power Apps:

```bash
pa app push
```

When the command finishes successfully, it returns a Power Apps URL where you can run the app.

You can also go to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) to play, share, or view details for the app.

## Related information

- [Connect your code app to data](connect-to-data.md)
- [Add a Dataverse action or function](add-dataverse-action-function.md)
- [Add Power Automate flows](add-flows.md)
- [Power Apps CLI command reference](../reference/cli.md)
