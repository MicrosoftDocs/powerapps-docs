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

This article walks through how to set up a blank app from [Vite](https://vite.dev/) and turn it into a Power Apps code app. It covers configuring a TypeScript app using the Power Platform SDK

## Prerequisites

- [Power Platform environment with code apps enabled](../overview.md#enable-code-apps-on-a-power-platform-environment)
- [Visual Studio Code](https://code.visualstudio.com/)
- [Node.js](https://nodejs.org/) Long term support (LTS) version)
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

1. If asked, agree to install `create-vite`
1. Accept the default package name `appfromscratch` by pressing **Enter**.
1. If asked to select a framework, select **React**.
1. If asked to select a variant, select **TypeScript**.
1. At this time, the Power SDK requires the port to be 3000 in the default configuration.

   Install the node type definition using:

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
1. Enter the following to test your Vite app:

   ```powershell
   npm run dev
   ```

   > [!NOTE]
   > If you're developing on macOS, you might need to update package.json to not reference `start vite`. For instance you'd change the dev entry from `start vite && start pac code run`:
   >
   >```json
   >"scripts": {    
   >    "dev": "start vite && start pac code run",
   >    "build": "tsc -b && vite build",
   >   "lint": "eslint .",
   >   "preview": "vite preview"
   > }
   >```
   >
   > to `vite && pac code run`
   >
   >```json
   >  "scripts": {    
   >    "dev": "vite && pac code run",
   >    "build": "tsc -b && vite build",
   >    "lint": "eslint .",
   >    "preview": "vite preview"
   >  }
   >```

1. The template project starts and runs locally. Browse to the `http://localhost:3000` address given.

   :::image type="content" source="media/sql-localhost.png" alt-text="Vite + React TypeScript starter page running on port 3000":::

   > [!IMPORTANT]
   > If you don't see port 3000, then revisit the previous steps.

1. Press <kbd>Ctrl + C</kbd> to stop the local server.

## Initialize your code app

1. Authenticate the Power Platform CLI against your Power Platform tenant:

   ```powershell
   pac auth create
   ```

   Sign-in using your Power Platform account when prompted. 

   > [!NOTE]
   > You can also use the [Power Platform Tools VS Code Extension](/power-platform/developer/howto/install-vs-code-extension) to do authenticate.

1. **Select** your environment using:

   ```powershell
   pac env select -env <URL of your environment>
   ```

   You can also use the Power Platform Tools VS Code Extension to select the environment

1. **Initialize** your code app using:

   ```powershell
   pac code init --displayName "App From Scratch"
   ```

   Notice that there's now a `power.config.json` file in your project.

1. **Install** the Power SDK using:

   ```powershell
   npm install --save "@microsoft/power-apps"
   ```

1. **Open** the `package.json`, and update the existing line:

   ```json
   "dev": "vite"
   ```

   Change it to:

   ```json
   "dev": "start pac code run && vite",
   ```

   Save the updated `package.json`.

1. **Add a new file** under the `src` folder named `PowerProvider.tsx` and grab the code from [github.com/microsoft/PowerAppsCodeApps/docs/assets/PowerProvider.tsx](https://github.com/microsoft/PowerAppsCodeApps/blob/main/docs/assets/PowerProvider.tsx)
1. **Save** the file.
1. **Open** `main.tsx` and add the following import under the existing imports:

   ```typescript
   import PowerProvider from './PowerProvider.tsx'
   ```

1. **Update** `main.tsx`

   ```typescript
   <StrictMode>
     <App />
   </StrictMode>,
   ```

   Change it to:

   ```typescript
   <StrictMode>
     <PowerProvider>
       <App />
     </PowerProvider>
   </StrictMode>,
   ```

1. **Save** the file
1. You can now test the code app by using:

    ```powershell
    npm run dev
    ```

    This runs the Vite server, but also starts the Power SDK server:

   :::image type="content" source="media/sql-testapp.png" alt-text="Power SDK server page showing test app URL and status":::

1. Open the URL provided by the Power SDK Server.

   > [!IMPORTANT]
   > Open the url in the same browser profile as your power platform tenant.

1. You should see the app open similar to:

   :::image type="content" source="media/sql-vite-running-powerapps.png" alt-text="Vite React app running inside Power Apps code apps host":::

### Related articles

[How to: Connect your code app to data](connect-to-data.md)  
[Power Apps CLI](/power-platform/developer/cli/introduction)
