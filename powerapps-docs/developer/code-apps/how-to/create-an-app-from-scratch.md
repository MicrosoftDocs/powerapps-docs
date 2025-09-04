---
title: "How to: Create a code app from scratch"
description: "Learn how to create a code app from scratch"
ms.author: alaug
author: alaug
ms.date: 09/10/2025
ms.reviewer: jdaly
ms.topic: how-to
contributors:
 - JimDaly
---
# How to: Create a code app from scratch

This guide walks through how to set up an blank app from vite and turn it into a Power Apps code app. 

This guide covers configuring a TypeScript app using the Power Platform SDK

## Prerequisites

- [Power Platform environment with Code Apps enabled](../overview.md#enable-code-apps-on-a-power-platform-environment)
- [Visual Studio Code](https://code.visualstudio.com/)
- [Node.js](https://nodejs.org/) (LTS version)
- [Power Platform Tools for VS Code](/power-platform/developer/cli/introduction)

## Initialize your Vite App

1. Open Visual Studio Code and open a new PowerShell terminal and enter:

   ```powershell
   mkdir C:\CodeApps -Force
   cd C:\CodeApps
   npm create vite@latest AppFromScratch -- --template react-ts
   cd C:\CodeApps\AppFromScratch
   npm install
   ```

1. If you are asked, agree to install `create-vite`
1. Accept the default package name `appfromscratch` by pressing **Enter**.
1. If you are asked to select a framework, select **React**.
1. If you are asked to select a variant, select **TypeScript**.
1. At this time, the Power SDK requires the port to be 3000 in the default configuration. 

   Install the node type defintions using:

   ```powershell
   npm i --save-dev @types/node
   ```

   Open the `vite.config.ts`, and update to be:

   ```typescript
   import { defineConfig } from 'vite'
   import react from '@vitejs/plugin-react'
   import * as path from 'path'
   
   // https://vite.dev/config/
   export default defineConfig({
     base: "./",
     server: {
       host: "::",
       port: 3000,
     },
     plugins: [react()],
     resolve: {
       alias: {
         "@": path.resolve(__dirname, "./src"),
       },
     },
   });
   ```

1. **Save** the file.
1. Enter the following to test your vite app:

   ```powershell
   npm run dev
   ```

   > [!NOTE]
   > If you are developing on macOS, you may need to update package.json to not reference 'start vite'. For instance you'd change the dev entry from:
   >
   >```powershell
   >"scripts": {    
   >    "dev": "start vite && start pac code run",
   >    "build": "tsc -b && vite build",
   >   "lint": "eslint .",
   >   "preview": "vite preview"
   > }
   >```
   >
   > to
   >
   >```powershell
   >  "scripts": {    
   >    "dev": "vite && pac code run",
   >    "build": "tsc -b && vite build",
   >    "lint": "eslint .",
   >    "preview": "vite preview"
   >  }
   >```

1. The template project will start and run locally. Browse to the http://localhost:3000 address given.

   :::image type="content" source="media/sql-localhost.png" alt-text="Vite + React TypeScript starter page running on port 3000":::

   > [!IMPORTANT]
   > If you do not see the port 3000, then revisit the steps above.

1. Press `Ctrl + C` to stop the local server when you have checked it runs ok.

## Initialize your Code App

1. Authenticate the Power Platform CLI against your Power Platform tenant:

   ```powershell
   pac auth create
   ```

   Login as your Power Platform account when prompted. 

   > [!NOTE]
   > You can also use the Power Platform Tools VS Code Extension to do this.

1. **Select** your environment using:

   ```powershell
   pac env select -env <URL of your environment>
   ```

   You can also use the Power Platform Tools VS Code Extension to select the Environment

1. **Initialize** your code app using:

   ```powershell
   pac code init --displayName "App From Scratch"
   ```

   Notice that there is now a `power.config.json` file in your project.

1. **Install** the Power SDK using:

   ```powershell
   npm install --save-dev "@pa-client/power-code-sdk@https://github.com/microsoft/PowerAppsCodeApps/releases/download/v0.0.4/7-31-pa-client-power-code-sdk-0.0.1.tgz"
   ```

   > [!NOTE]
   > This SDK is currently not yet available on `npmjs.com` and must be installed from the GitHub release.

1. **Open** the `package.json`, and update the existing line:

   ```json
   "dev": "vite"
   ```

   to be:

   ```json
   "dev": "start pac code run && vite",
   ```

   Save the updated `pacakage.json`.

1. **Add a new file** under the `src` folder named `PowerProvider.tsx` and grab the code from [github.com/microsoft/PowerAppsCodeApps/docs/assets/PowerProvider.tsx](https://github.com/microsoft/PowerAppsCodeApps/blob/main/docs/assets/PowerProvider.tsx)
1. **Save** the file.
1. **Open** `main.tsx` and add the following import under the existing imports:

   ```
   import PowerProvider from './PowerProvider.tsx'
   ```

1. **Update** `main.tsx`

   ```
   <StrictMode>
     <App />
   </StrictMode>,
   ```

   to be

   ```
   <StrictMode>
     <PowerProvider>
       <App />
     </PowerProvider>
   </StrictMode>,
   ```

1. **Save** the file
1. You can now test the Code App by using:

    ```
    npm run dev
    ```

    This will run the vite server, but also start the Power SDK server:

   :::image type="content" source="media/sql-testapp.png" alt-text="Power SDK server page showing test app URL and status":::

1. Open the URL provided by the Power SDK Server.

   > [!IMPORTANT]
   > Open the url in the same browser profile as your power platform tenant.

1. You should see the app open similar to:

   :::image type="content" source="media/sql-vite-running-powerapps.png" alt-text="Vite React app running inside Power Apps Code Apps host":::
