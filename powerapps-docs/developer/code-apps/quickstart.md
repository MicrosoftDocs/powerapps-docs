---
title: "Quickstart: Create your first code app"
description: "Create your first code app using this quick start"
ms.author: alaug
author: alaug
ms.date: 09/10/2025
ms.reviewer: jdaly
ms.topic: quickstart
contributors:
 - JimDaly
---
# Quickstart: Create your first code app

In this quickstart, you will build a code app, run it locally, and then publish it. You will be guided to download a sample code app, use PAC CLI to target a Power Platform environment to publish the app, you'll proceed with publishing the app and, last, you'll run the app hosted in Power Platform.  

## Prerequisites

> [!NOTE]
> Please refer to the general code app prerequisites: [Prerequisites](overview.md#prerequisites)

Clone the [PowerAppsCodeApps repository](https://github.com/microsoft/PowerAppsCodeApps)

This repository has the start of a TypeScript app that already includes the Power Platform SDK. Later we'll add guidance to that allows you to start from scratch without using this base app.


```powershell
git clone https://github.com/microsoft/PowerAppsCodeApps.git
cd PowerAppsCodeApps
```

## Open the HelloWorld sample

Open the `HelloWorld` sample using Visual Studio Code.

```powershell
cd samples\HelloWorld
code .
```

The base of this app project was created using Vite and it has two notable additions: 1) package.json has a reference to the Power Apps SDK which helps an app connect to Power Platform connectors and 2) PowerProvider.tsx which contains an initialize() function which the app uses to communicate to the Power Apps host that the app is ready to run. 

## Authenticate PAC CLI and point to your development environment

Visual Studio Code, open a new terminal window and use the [pac auth create](/power-platform/developer/cli/reference/auth#pac-auth-create) command to create an authentication profile.

```powershell
pac auth create --environment {environment id}
```

All Power Platform apps, flows and agents publish to an environment, including code apps. The PAC CLI's auth command will prompt you to authenticate with your MS Entra identity and ensure the code app you add connections to and publish to Power Platform go in the specififed environment. 

## Install dependencies

In the terminal window, run these commands:

```powershell
npm install
pac code init
```

- [npm install](https://docs.npmjs.com/cli/v11/commands/npm-install) Installs the dependent libraries found in the `package.json` file.
- [pac code init](/power-platform/developer/cli/reference/code#pac-code-init) Initializes a code app in the current directory.

## Run locally

In the terminal window, run these commands:

```powershell
npm run dev | pac code run
```

- [npm run dev](https://docs.npmjs.com/cli/v9/commands/npm-run-script) Runs the scripts configured in the `package.json` file with the key value of `dev`. In this case, the script are `"concurrently \"vite\" \"pac code run\""`. <!-- QUESTION: It looks like pac code run is invoked twice. Is this intentional? -->
- [pac code run](/power-platform/developer/cli/reference/code#pac-code-run) Runs a local server for connections loading locally in the app.


<!-- 
TODO:
There is an opportunity to describe what people will see here.
I think a lot of people don't actually run these quick starts, they just skim the content to get a sense for the experience provided.
You might add a screenshot showing what people should see here. 
-->



## Build and deploy to Power Apps

In the terminal window, run these commands:

```powershell
npm run build | pac code push
```

- [npm run build](https://docs.npmjs.com/cli/v9/commands/npm-run-script) Runs the scripts configured in the `package.json` file with the key value of `build`. In this case, the script are `"tsc -b && vite build"`. 
- [pac code push](/power-platform/developer/cli/reference/code#pac-code-push) Publishes a new version of a Code app..


If successful, this command should return a Power Apps URL to run the app. 

Optionally, you can open  [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) to see the app. You can play, share, or see details from there. 

Congratulations! You have successfully pushed your first code app!

## Troubleshooting

If you get stuck on the "fetching your app" loading screen or see an "App timed out" error screen, double check:

- That you ran `npm run build`
- There are no issues in `PowerProvider.tsx`
