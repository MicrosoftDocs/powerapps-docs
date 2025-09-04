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

In this quickstart, you will build a code app, run it locally, and then publish it.

<!-- 
TODO: 
- Explain why people are performing the instructions in this quick start.
-->

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

<!-- 
TODO: 
- Explain the important contents of the HelloWorld folder
- Explain that this project uses [Vite](https://vite.dev/) and why this was chosen over alternatives that might be the readers preferred option. Will their preferred option work instead?
-->

## Authenticate PAC CLI and point to your first release environment

Visual Studio Code, open a new terminal window and use the [pac auth create](/power-platform/developer/cli/reference/auth#pac-auth-create) command to create an authentication profile.

```powershell
pac auth create --environment {environment id}
```

<!-- 
TODO: Explain why this is necessary
-->

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
