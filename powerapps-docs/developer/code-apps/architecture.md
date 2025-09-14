---
title: "Power Apps code apps architecture (Preview)"
description: "Power Apps code apps architecture during development and runtime"
ms.author: alaug
author: alaug
ms.date: 09/14/2025
ms.reviewer: jdaly
ms.topic: article
contributors:
 - JimDaly
---
# Code apps architecture (Preview)

> [!NOTE]
> [!INCLUDE [cc-preview-features-definition](../../includes/cc-preview-features-definition.md)]

Power Apps code app architecture consists of:

- The Power Apps SDK
- Generated models/services for connectors
- The `power.config.json` configuration file
- The Power Apps host

Understanding how these parts collaborate through development, publishing, and runtime execution make you more successful. Learn about:

- The role of each layer (your code vs. SDK vs. host)
- How models/services are generated and consumed when you add or remove connectors
- What is packaged and published with [`pac code push`](/power-platform/developer/cli/reference/code#pac-code-push)

## App Development

An HTML or TypeScript/JavaScript app is a prerequisite to use code apps technology. Code apps support Single-Page Applications (SPAs). The Power Platform CLI and Power Apps SDK enable your app to use Power Platform connectors and be hosted in a Power Platform environment.


:::image type="content" source="media/app-development-architecture.png" alt-text="Development architecture":::


|Component|Description  |
|---------|---------|
|power.config.json|A file generated from the Power Apps SDK, which contains metadata. Both the CLI and Power Apps SDK use this metadata for Power Platform connections and to publish an app to an environment. Your app logic isn't expected to interact with the `power.config.json` file.|
|Power Apps SDK|The [@microsoft/power-apps - npm package](https://www.npmjs.com/package/@microsoft/power-apps). It has APIs your app can interact with directly and it contains logic that manages models and services as connections are added and removed from an app.|
|Power Platform CLI|The PAC CLI [`pac code push`](/power-platform/developer/cli/reference/code#pac-code-push) command takes a compiled app and publishes it in a Power Platform environment where it can then be shared with users and run from [Power Apps](https://make.powerapps.com).|

## Runtime

When a code app runs, there are three logical components:

- Your code
- The Power Apps SDK
- The Power Apps host


:::image type="content" source="media/app-development-runtime.png" alt-text="Runtime architecture":::

1. The Power Apps SDK exposes APIs that your code can use and the generated models and services your app uses to perform data requests via Power Platform connectors.
1. The Power Apps host manages end-user authentication, app loading, and presenting contextual messages to the user if an app fails to load.
