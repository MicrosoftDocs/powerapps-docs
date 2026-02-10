---
title: "Quickstart: Create a code app from scratch"
description: "Learn how to create a code app from scratch"
ms.author: jordanchodak
author: jordanchodakWork
ms.date: 02/02/2026
ms.reviewer: jdaly
ms.topic: quickstart
contributors:
 - JimDaly
---
# Quickstart: Create a code app from scratch

This article shows how to set up a blank app from [Vite](https://vite.dev/) and turn it into a Power Apps code app. It covers configuring a TypeScript app by using the Power Apps SDK.

## Prerequisites

- [Power Platform environment with code apps enabled](../overview.md#enable-code-apps-on-a-power-platform-environment)
- [Node.js](https://nodejs.org/) Long term support (LTS) version
- [Power Platform CLI](/power-platform/developer/cli/introduction?tabs=windows)
- [Git](https://git-scm.com/)

## Steps

1. Open a new terminal and enter:

   ```bash
   npx degit github:microsoft/PowerAppsCodeApps/templates/vite my-app
   cd my-app 
   ```

1. Authenticate the Power Platform CLI against your Power Platform tenant and select your environment:

   ```bash
   pac auth create
   pac env select --environment < Your environment ID >
   ```

   Sign in by using your Power Platform account when prompted. All Power Platform apps, flows, and agents publish to an environment. The PAC CLI's [auth command](/power-platform/developer/cli/reference/auth) prompts you to authenticate by using your Microsoft Entra identity and ensures the code app you add connections to and publish to Power Platform go in the specified environment.

1. Install the Power Apps SDK and initialize your code app by using:
   

   ```bash
   npm install
   pac code init --displayname "App From Scratch"
   ```
   
1. Enter the following command to test your code app locally:

   ```bash
   npm run dev 
   ```

  Then, open the URL labelled **Local Play**.

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

In the terminal window, run these commands:

```powershell
npm run build | pac code push
```

- [npm run build](https://docs.npmjs.com/cli/v9/commands/npm-run-script) Runs the scripts configured in the `package.json` file with the key value of `build`. In this case, the script is `"tsc -b && vite build"`.
- [pac code push](/power-platform/developer/cli/reference/code#pac-code-push) Publishes a new version of a code app.

If successful, this command returns a Power Apps URL to run the app.

Optionally, you can open  [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) to see the app. You can play, share, or see details from there.

Congratulations! You successfully pushed your first code app!

### Related information

- [How to: Connect your code app to data](connect-to-data.md)  
- [Power Apps CLI](/power-platform/developer/cli/introduction)
