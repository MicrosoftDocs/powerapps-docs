---
title: "Power Apps Code Apps Architecture for Development and Runtime"
description: "Explore Power Apps code apps architecture for development and runtime to understand how connectors, configuration, publishing, and the host work together."
ms.author: jordanchodak
author: jordanchodakWork
ms.date: 08/12/2026
ms.reviewer: jdaly
ms.topic: article
contributors:
 - JimDaly
---
# Power Apps code apps architecture

Power Apps code apps architecture explains how the following components work together during development, publishing, and runtime so you can build and deploy code apps successfully:

- The [Power Apps client library for code apps](https://www.npmjs.com/package/@microsoft/power-apps), sometimes called the 'Power Apps SDK'
- Generated models and services for connectors
- The `power.config.json` configuration file
- The Power Apps host

Understanding how these parts work together through development, publishing, and runtime execution helps you succeed. Learn about:

- The role of each layer (your code vs. Power Apps client library for code apps vs. host)
- How models and services are generated and used when you add or remove connectors
- What [`pa app push`](reference/cli.md#pa-app-push) packages and publishes

## Code app development architecture

To use code apps technology, you need an HTML or TypeScript/JavaScript app. Code apps support single-page applications (SPAs). Use the Power Apps CLI and Power Apps client library for code apps to enable your app to use Power Platform connectors and be hosted in a Power Platform environment.

:::image type="content" source="media/app-development-architecture.png" alt-text="Screenshot of the code app development architecture and component relationships.":::

|Component|Description  |
|---------|---------|
|power.config.json|A file generated from the Power Apps client library for code apps, which contains metadata. Both the CLI and Power Apps client library for code apps use this metadata for Power Platform connections and to publish an app to an environment. Your app logic doesn't need to interact with the `power.config.json` file.|
|Power Apps client library for code apps|The [@microsoft/power-apps - npm package](https://www.npmjs.com/package/@microsoft/power-apps). It has APIs your app can interact with directly and it contains logic that manages models and services as connections are added and removed from an app.|
|Power Apps CLI|The [`pa app push`](reference/cli.md#pa-app-push) command takes a compiled app and publishes it in a Power Platform environment where it can then be shared with users and run from [Power Apps](https://make.powerapps.com).|

## Code app runtime architecture

When a code app runs, it includes three logical components:

- Your code
- The Power Apps client library for code apps
- The Power Apps host

:::image type="content" source="media/app-development-runtime.png" alt-text="Screenshot of the code app runtime architecture and its three logical components.":::

- The Power Apps client library for code apps exposes APIs that your code can use. It also provides the generated models and services your app uses to perform data requests through Power Platform connectors.
- The Power Apps host manages end-user authentication, app loading, and presenting contextual messages to the user if an app fails to load.

