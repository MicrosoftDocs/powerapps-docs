---
title: "Power Apps code apps architecture (Preview)"
description: "Power Apps code apps architecture during development and runtime"
ms.author: alaug
author: alaug
ms.date: 09/10/2025
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

You will be more successful when you understand how these parts collaborate through development, publishing, and runtime execution. Learn about:

- The role of each layer (your code vs. SDK vs. host)
- How models/services are generated and consumed when you add or remove connectors
- What is packaged and published with [`pac code push`](/power-platform/developer/cli/reference/code#pac-code-push)

## App Development

An HTML or TypeScript/JavaScript app is a prerequisite to use code apps technology. Code apps support Single-Page Applications (SPAs). The Power Platform CLI and Power Apps SDK enable your app to use Power Platform connectors and be hosted in a Power Platform environment.


<!-- ```mermaid
---
config:
  theme: neutral
  look: classic
  layout: dagre
---
flowchart LR
 subgraph Project["Web app project"]
        App["TS/JS files"]
        Config["power.config.json"]
        SDK["Power Apps SDK"]
        Models["SDK generated<br>Models &amp; Services"]
  end
    CLI["Power Platform CLI"] --> Project & Services["Power Platform Services"]
    App --> SDK & Models
    SDK --> Config
    SDK <--> Models & Connectors["Power Platform Connectors"]

``` -->

:::image type="content" source="media/code-app-architecture-development.png" alt-text="Development architecture":::


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

:::image type="content" source="media/code-app-architecture-runtime.png" alt-text="Runtime architecture":::

1. The Power Apps SDK exposes APIs that may be invoked by your code and the generated models and services your app uses to perform data requests via Power Platform connectors.
1. The Power Apps host manages end-user authentication, app loading and presenting contextual messages to the user if an app fails to load.
