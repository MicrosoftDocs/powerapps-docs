---
title: "Quickstart: Your first Power Apps native app"
description: Build a native mobile app with the Power Platform mobile-app plugin, from empty folder to a device-ready app. Follow the step-by-step guide and deploy today.
author: shwetamurkute
ms.author: ruchidixit
ms.reviewer: smurkute
ms.service: powerapps
ms.subservice: mobile
ms.date: 09/07/2026
ms.topic: how-to
search.audienceType:
  - developer
  - maker
---

# Quickstart: Build a native mobile app with the Power Platform mobile-app plugin (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

This article walks you through going from an empty folder to a working app running on a physical device. You create a project from the native template, install the mobile-app plugin in your AI coding host, generate an app from a natural-language description, approve the planning gates, run the app on a device with hot reload, and deploy it to your Power Platform environment. Learn more about mobile-app plugin in [Power Apps Standalone App Template](https://github.com/microsoft/power-platform-skills/blob/main/plugins/mobile-apps/template/README.md).

## Step 1: Create the project from the template

Create the project folder and install the following dependencies:

```bash
npx degit microsoft/power-platform-skills/plugins/mobile-apps/template#main field-inspector
cd field-inspector
npm install
```

## Step 2: Install the mobile-app plugin

Install the plugin from the Power Platform Skills marketplace.

 **GitHub Copilot CLI**:

 ```bash
 copilot plugin marketplace add microsoft/power-platform-skills
 copilot plugin install mobile-app@power-platform-skills
 ```

 **Claude Code**:

 ```bash
 claude plugin marketplace add microsoft/power-platform-skills
 claude plugin install mobile-app@power-platform-skills --scope user
 ```

 **Visual Studio Code with Copilot Chat**:

 1. Open the **Extensions** view.
 1. Search for `@agentPlugins mobile-app`.
 1. Install the extension.
 1. Reload Visual Studio Code if prompted, then open Copilot Chat in Agent mode.

## Step 3: Generate the app

Open the template folder in Visual Studio Code and run the skill from Copilot Chat.
From the template folder, in your host, run: 

```text
/create-mobile-app "describe what you want"
```
Examples of sample prompts:

- Create an app for a retail store to help the sales manager track orders and manage inventory. Staff scan products by using the native barcode scanner to check stock or log orders. 

- Create an app for a beverage distributor to help delivery drivers track deliveries and manage stock at retail locations. Enable continuous location tracking so the manager can see each driver's live route and stop history on a map. 
 
## Step 4: Sign in and select an environment

Sign in with an account that has access to the target Power Platform environment.

> [!NOTE]
> Power Apps CLI and Azure CLI use separate authentication caches. Signing in to one doesn't change the other.

## Step 5: Review and approve the planning gates

The plugin generates `native-app-plan.md` and pauses at each planning gate. Review and approve the plan before continuing.

The approved plan is reused for future `/edit-app` operations.

1. **Data model**: Review the tables, columns, relationships, and alternate keys that the app uses. The generated plan includes an entity relationship (ER) diagram.

2. **Native capabilities**: Review the approved native capabilities, such as camera, scanner, or GPS.

3. **Connectors**: Review the first-party and custom connectors that are included in the solution.

4. **Screens**: Review the screen specifications and navigation flow. Before code is generated, the plugin creates a visual preview in `_plan_preview.html`.

## Step 6: Configure app registration

The plugin identifies the Microsoft Entra tenant associated with the selected environment and provides the following options:

- **Recommended**: The plugin opens `make.powerapps.com/environments/<env-id>/wraps#create-app-registration`. Copy the **Application (client) ID** and paste it into the plugin prompt.

- Use an existing client ID from a Wrap-configured app registration.

- Configure it later by running:

   ```text
   /set-app-registration-native
   ```

   Complete this step before the first device sign-in.

## Step 7: Wait for scaffolding to complete

After the planning gates are approved, the plugin generates the design system and scaffolds the app.

The process includes the following stages:

1. **Design system**
   generates assets under the `brand/` folder, including:
   - `design-system.md` for specs
   - `tokens.ts` for tokens
   - `design-system.html` for gallery

1. **Initialization**
   runs:
   ```bash
   npx power-apps init
   ```

1. **Schemas and Dataverse**
   - Generates schemas.
   - Creates or reuses tables.
   - Regenerates services in `src/generated/services/`.

1. **Connectors**
   adds and configures connectors.

1. **Native wrappers**
   generates approved native capability wrappers in `src/native/`.

1. **Screens**
   generates screens from the approved screen specifications.

1. **Verification**
   runs TypeScript compilation and validation checks.

1. **Preview**
   generates a static `preview.html` file.

The time required depends on the complexity of the app. Apps that include Dataverse provisioning, offline profiles, or multiple connectors can take longer to build because Dataverse metadata operations can be affected by other platform activities.

## Step 8: Run the app on a device

1. Run:
    ```bash
    npm run dev
    ```
1. Wait for dev server to print a QR code.
1. Open the **Power Apps Developer** app on your device.
1. Scan the **Dev Server QR** code to load the bundle.
1. Sign in with an account that has access to the selected environment.

The app loads on the device and supports hot reload. Changes made to files in the `app/` directory appear without a full rebuild.

## Step 9: Update the app

Use the following commands to refine the app. Each update is recorded in `memory-bank.md`.

| Command | Description |
|----------|----------|
| `/edit-app "..."` | Updates the plan, applies changes, rebuilds affected screens, and refreshes `preview.html`. |
| `/add-dataverse` | Extends the schema and regenerates typed services. |
| `/add-native camera` | Adds a typed wrapper for a supported native capability. |
| `/add-connector` | Adds a Power Platform connector by using `npx power-apps add-data-source`. |
| `/preview-screens` | Regenerates the static HTML preview without dev server. |
| `/debug-app "<symptom>"` | Diagnoses issues in a running app by using dev server output. |

## Step 10: Deploy the app

To deploy the app, run:

```text
/deploy
```

This command publishes your app to the Power Platform environment recorded in `power.config.json`.


### See also

[Troubleshoot issues in the native mobile app](troubleshoot-native-apps.md)