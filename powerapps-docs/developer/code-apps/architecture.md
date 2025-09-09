---
title: "Power Apps code apps architecture"
description: "Power Apps code apps architecture during development and runtime"
ms.author: alaug
author: alaug
ms.date: 09/10/2025
ms.reviewer: jdaly
ms.topic: article
contributors:
 - JimDaly
---
# Code apps architecture

**This is an AI generated intro**

Power Apps code app architecture describes how your app code, the Power Apps SDK (@microsoft/power-apps), the generated models/services for connectors, the configuration file (power.config.json), and the Power Apps host collaborate through development, publishing, and runtime execution. Learn about:

1. Explain the role of each layer (your code vs. SDK vs. host).
2. Add or remove connectors and understand how models/services are generated and consumed.
3. Know exactly what is packaged and published with `pac code push`.

## App Development

An HTML or TypeScript/JavaScript app is a prerequisite to use code apps technology. Code apps support Single-Page Applications (SPAs). The Power Platform CLI and Power Apps SDK allow you to augment your app to use Power Platform connectors and be hosted in a Power Platform environment. 

:::image type="content" source="media/code-app-architecture-development.png" alt-text="Development architecture":::

1. Power.config.json is a file, generated from the Power Apps SDK, which contains metadata both the CLI and Power Apps SDK use for Power Platform connections and to publish an app to an environment. Your app logic isn't expected to interact with the power.config.json file.
1. The Power Apps SDK is the [@microsoft/power-apps - npm package](https://www.npmjs.com/package/@microsoft/power-apps) which has APIs your app can interact with directly and it contains logic that adds/removes models and services as connections are added/removed from an app. 
1. Power Platform CLI (PAC CLI) 'pac code push' takes a compiled app and publishes it in a Power Platform environment where it can then be shared with users and run from apps.powerapps.com.

## Runtime

When a code app runs, there are three logical components: 

- Your code
- The Power Apps SDK
- The Power Apps host.

:::image type="content" source="media/code-app-architecture-runtime.png" alt-text="Runtime architecture":::

1. At runtime, the Power Apps SDK is the npm package (@microsoft/power-apps) which exposes APIs that may be invoked by your code and the generated models and services your app uses to perform data requests via Power Platform connectors. 
1. The Power Apps host facilitates end-user authentication, app loading and presenting contextual messages to the user if an app fails to load.
