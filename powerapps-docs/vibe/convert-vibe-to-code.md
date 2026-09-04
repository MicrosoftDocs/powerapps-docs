---
title: Convert a vibe app to a code app
description: Learn how to download a Power Apps vibe app and convert it to a code app for local development.
ms.topic: how-to
ms.service: powerapps
ms.author: jordanchodak
ms.reviewer: mkaur
author: jordanchodakWork
ms.date: 09/03/2026
ms.custom: vibe
---

# Convert a vibe app to a code app

Power Apps vibe lets you generate and refine an app by using natural language. If you want to continue development in a local integrated development environment (IDE), download the source code and convert the app to a [Power Apps code app](/power-apps/developer/code-apps/overview).

After conversion, you can directly edit the source code, use source control, run the app locally, and publish it by using the Power Apps CLI.

> [!IMPORTANT]
> Converting a vibe app creates a new code app. The code app is disconnected from the original plan. Changes that you make to the code app don't appear in the vibe app or its plan.

> [!WARNING]
> Vibe-generated apps can use images hosted by the following URLs:
>
> - `https://res-dev.cdn.officeppe.net/`
> - `https://res-sdf.cdn.office.net/`
> - `https://cdn.hubblecontent.osi.office.net/`
>
> You must allowlist these URLs in the Content Security Policy (CSP) for code apps in the target environment. Otherwise, images in the converted app might not appear. For more information, see [Configure Content Security Policy for code apps](/power-apps/developer/code-apps/how-to/content-security-policy).

## Prerequisites

- A vibe app that you have permission to edit
- A Power Platform environment that has [code apps enabled](/power-apps/developer/code-apps/overview#enable-code-apps-on-a-power-platform-environment)
- [Node.js](https://nodejs.org/) Long Term Support (LTS) version
- The [Power Apps CLI](/power-apps/developer/code-apps/how-to/create-an-app-from-scratch#step-2-install-dependencies-and-initialize-the-code-app)
- An IDE, such as [Visual Studio Code](https://code.visualstudio.com/)

## Download the app source code

1. Sign in to [Power Apps vibe](https://vibe.powerapps.com/).
1. Open the app that you want to convert, and then select **Edit**.
1. Select **Download source**.

The source code downloads as a compressed file.

## Prepare the project

1. Extract the downloaded file.
1. In the extracted `apps` folder, find the folder that has the name of your app.
1. Open the app folder in your IDE.
1. Open `power.config.json`.
1. If the file contains `connectionReferences` or `databaseReferences` properties, copy those properties and all properties that follow them. Save the copied content temporarily.
1. Delete `power.config.json`.

> [!IMPORTANT]
> Keep the copied configuration until you finish the conversion. Initializing the code app creates a new `power.config.json` file.

## Install the project dependencies

Open a terminal in the app folder, and run the following command:

```bash
npm install --save-dev "oxlint-tsgolint@^7.0.2001" --allow-remote=all
```

## Initialize the code app

Use [`pa app init`](/power-apps/developer/code-apps/reference/cli#pa-app-init) to initialize the project:

```bash
pa app init
```

Follow the prompts:

1. Select the Power Platform environment where you want to create the code app.
1. Enter a display name for the new app.

> [!IMPORTANT]
> If the vibe app uses Dataverse tables or other environment-specific resources, select the environment that contains those dependencies.

## Restore the connection configuration

If you copied the configuration from the original `power.config.json` file:

1. Open the new `power.config.json` file created by `pa app init`.
1. Add the properties that you copied from the original file.
1. Ensure the result is valid JSON, and then save the file.

The project is now initialized as a code app.

## Run the app locally

Use [`pa app run`](/power-apps/developer/code-apps/reference/cli#pa-app-run) to run the app:

```bash
pa app run
```

Open the URL labeled **Local Play**.

> [!IMPORTANT]
> Open the URL in the same browser profile that you use for your Power Platform tenant.

Test the app and verify that its data sources and other dependencies work as expected. For more information about developing code apps, see [Power Apps code apps overview](/power-apps/developer/code-apps/overview).

## Build and publish the code app

Build the app:

```bash
npm run build
```

Use [`pa app push`](/power-apps/developer/code-apps/reference/cli#pa-app-push) to publish the compiled app:

```bash
pa app push
```

When the command finishes successfully, it returns a Power Apps URL where you can run the code app.

The code app is separate from the original vibe app. Continue developing and managing the new app by using the code apps development and application lifecycle management tools.

## Next steps

- [Create a code app by using the Power Apps CLI](/power-apps/developer/code-apps/how-to/create-an-app-from-scratch)
- [Connect your code app to data](/power-apps/developer/code-apps/how-to/connect-to-data)
- [Learn about application lifecycle management for code apps](/power-apps/developer/code-apps/how-to/alm)
