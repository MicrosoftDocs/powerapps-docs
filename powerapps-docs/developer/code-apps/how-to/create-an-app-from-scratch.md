---
title: "How to: Create a code app from scratch (preview)"
description: "Learn how to create a code app from scratch"
ms.author: jordanchodak
author: jordanchodakWork
ms.date: 11/19/2025
ms.reviewer: jdaly
ms.topic: how-to
contributors:
 - JimDaly
---
# How to: Create a code app from scratch (preview)

This article walks through how to set up a blank app from [Vite](https://vite.dev/) and turn it into a Power Apps code app. It covers configuring a TypeScript app using the Power Platform SDK.

> [!NOTE]
> [!INCLUDE [cc-preview-features-definition](../../../includes/cc-preview-features-definition.md)]

## Prerequisites

- [Power Platform environment with code apps enabled](../overview.md#enable-code-apps-on-a-power-platform-environment)
- [Node.js](https://nodejs.org/) Long term support (LTS) version
- [Power Platform CLI](/power-platform/developer/cli/introduction?tabs=windows)
- [Git](https://git-scm.com/)

## Steps

1. Open a new terminal and enter:

```shell
npx degit github:microsoft/PowerAppsCodeApps/templates/vite my-app
cd my-app 
```

2. Authenticate the Power Platform CLI against your Power Platform tenant and select your environment:

```shell 
pac auth create
pac env select --environment {environment id}
```
   Sign in using your Power Platform account when prompted. All Power Platform apps, flows, and agents publish to an environment. The PAC CLI's auth command prompts you to authenticate with your Microsoft Entra identity and ensure the code app you add connections to and publish to Power Platform go in the specified environment. 

3. Install the Power SDK and initialize your code app using:
   
```shell
npm install
pac code init --displayname "App From Scratch"
```
   
5. Enter the following to test your code app locally. Then, open the URL provided by the Power SDK Server:

```shell 
npm run dev 
``` 

   > [!IMPORTANT]
   > Open the URL in the same browser profile as your Power Platform tenant.

##TODO - add image here

You should see the app open similar to:

##TODO - add image here

### Related information

- [How to: Connect your code app to data](connect-to-data.md)  
- [Power Apps CLI](/power-platform/developer/cli/introduction)
