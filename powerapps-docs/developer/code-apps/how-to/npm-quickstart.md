---
title: "How to: Quickstart with npm CLI"
description: "Create a Power Apps code app using the new npm CLI."
ms.author: jordanchodak
author: jordanchodakWork
ms.date: 02/18/2026
ms.reviewer: jdaly
ms.topic: how-to
contributors:
 - JimDaly
---

# Quickstart: Create a code app from scratch with the new npm CLI

Here we use the new npm CLI (Public Preview) included starting with v1.0.4 of the [Power Apps SDK](https://www.npmjs.com/package/@microsoft/power-apps?activeTab=readme)

This article shows you how to set up a blank app from Vite and convert it into a Power Apps code app using the Power Apps SDK with TypeScript configuration.

## Prerequisites

- Power Platform environment with code apps enabled
- [Node.js](https://nodejs.org/) (LTS version)
- [Git](https://git-scm.com/)

## Step 1: Initialize the project

Open a terminal and execute:

```bash
npx degit github:microsoft/PowerAppsCodeApps/templates/vite my-app
cd my-app
```

## Step 2: Install dependencies and initialize the code app

Install the project dependencies and the Power Apps SDK:

```bash
npm install
npm install @microsoft/power-apps
```

Initialize your code app. You can either provide options directly or use interactive prompts:

**Option A: Interactive mode** (the CLI will prompt you for required information):

```bash
npx power-apps init
```

**Option B: Pass options directly:**

```bash
npx power-apps init --displayName "App From Scratch" --environmentId <Your environment ID>
```

When you run the `init` command, the CLI will authenticate you automatically. Sign in with your Power Platform account when prompted.

## Step 3: Test locally

Run the code app locally for development:

```bash
npx power-apps run
```

This starts a local development server. Open the URL labeled **Local Play**.

> [!IMPORTANT]
   > Open the URL in the same browser profile as your Power Platform tenant.

   > [!NOTE]
   > **Local Network Access Restrictions**
   > 
   > Since December 2025, Chrome and Microsoft Edge browsers block requests from public origins to local endpoints by default.
   > - Because your code app connects to localhost during development, you might need to grant browser permission or configure enterprise policies.
   > - For embedded scenarios, include `allow="local-network-access"` in iframe tags.
   > - Learn to [Control a website's access to the local network in Microsoft Edge](https://support.microsoft.com/topic/control-a-website-s-access-to-the-local-network-in-microsoft-edge-ef7eff4c-676d-4105-935c-2acbcd841d51) and about the [new permission prompt for Local Network Access using Chrome](https://developer.chrome.com/blog/local-network-access) for details.

You should see the app open similar to:

:::image type="content" source="media/npm-run-dev-result.png" alt-text="See the test app playing locally in the browser":::

## Build and deploy to Power Apps

Build your app and push it to your Power Apps environment:

```bash
npm run build
npx power-apps push
```

**Command details:**

- `npm run build` - Runs scripts from `package.json` (executes `tsc -b && vite build`)
- `npx power-apps push` - Publishes a new version of the code app to your environment

Upon successful completion, the command returns a Power Apps URL to run the app.

Optionally, visit [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) to view, play, share, or review app details.
