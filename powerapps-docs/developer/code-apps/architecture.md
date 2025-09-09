---
title: "Power Apps code apps architecture"
description: "Power Apps code apps architecture during development and runtime"
ms.author: alaug
author: alaug
ms.date: 09/10/2025
ms.reviewer: jdaly
ms.topic: architecture
contributors:
 - JimDaly
---
# Code apps architecture

## App Development
An HTML or TypeScript/JavaScript app is a prerequisite to use code apps technology. The Power Platform CLI and Power Apps SDK allow you to augment your app to use Power Platform connectors and be hosted in a Power Platform environment. 

<p align="center">
 
</p>

1. Power.config.json is a file, generated from the Power Apps SDK, which contains metadata both the CLI and Power Apps SDK use for Power Platform connections and to publish an app to an environment. Your app logic is not expected to interact with the power.config.json file.
1. The Power Apps SDK is the npm package (@microsoft/power-apps) which has APIs your app can interact with directly and it contains logic that adds/removes models and services as connections are added/removed from an app. 
1. Power Platform CLI (PAC CLI) ‘pac code push’ takes a compiled app and publishes it in a Power Platform environment where it can then be shared with users and run from apps.powerapps.com.

## Runtime
When a code app runs there are three logical components: your code, the Power Apps SDK and the Power Apps host.

<p align="center">
  
</p>

1. At runtime, the Power Apps SDK is the npm package (@microsoft/power-apps) which exposes APIs that may be invoked by your code and the generated models and services your app uses to perform data requests via Power Platform connectors. 
1. The Power Apps host facilitates end-user authentication, app loading and presenting contextual messages to the user if an app fails to load.
