---
title: "Quickstart: Your first Power Apps native app"
description: Build a native mobile app with the Power Platform mobile-app plugin, from empty folder to a device-ready app. Follow the step-by-step guide and deploy today.
author: shwetamurkute
ms.author: ruchidixit
ms.reviewer: smurkute
ms.service: powerapps
ms.subservice: mobile
ms.date: 10/30/2026
ms.topic: how-to
ai-usage: ai-assisted
search.audienceType:
  - developer
  - maker
---

# Quickstart: Build a native mobile app with the Power Platform mobile-app plugin (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

This article walks you through going from an empty folder to a working app running on a physical device. You create a project from the native template, install the mobile-app plugin in your AI coding host, generate an app from a natural-language description, approve the planning gates, run the app on a device with hot reload, and deploy it to your Power Platform environment. Learn more about mobile-app plugin in [Power Apps Standalone App Template](https://github.com/microsoft/power-platform-skills/blob/main/plugins/mobile-apps/template/README.md).

## Step 1: Create the project from the template

Open Command Prompt and run these commands to create the project folder and install the dependencies:

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

Your app needs a Microsoft Entra app registration. The registration gives the app the permissions it needs to run, including in the Power Apps Developer app, so you need one whether or not you plan to wrap the app. Choose one option:

- **Create a registration (recommended)**. The plugin opens the app registration page in Power Apps: `make.powerapps.com/environments/<env-id>/wraps#create-app-registration`. The address contains `wraps`, but the registration isn't tied to Wrap. Copy the **Application (client) ID** and paste it into the plugin prompt.

- **Reuse a registration you use with Wrap**. If you already wrap other apps (canvas or native), you can use the same registration here. A new registration also works with Wrap.

- **Configure it later**. Run the following command from the project folder before you first sign in on a device:

   ```text
   /set-app-registration-native
   ```

## Step 7: Wait for scaffolding to complete

After you approve the planning gates, the plugin generates the design system and scaffolds the app.

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

The time required depends on the complexity of the app. Apps that include Dataverse provisioning, offline profiles, or multiple connectors can take longer to build because other platform activities can affect Dataverse metadata operations.

## Step 8: Run the app on a device

1. Connect your computer and device to the same network. Open Command Prompt in the project folder and run the following command to start the development server:

    ```bash
    npm run dev
    ```

2. Wait for the development server to print a QR code.
3. Open the **Power Apps Developer** app on your device.
4. Scan the development server QR code to load the bundle.
5. Sign in with an account that has access to the selected environment.

The app loads on the device and supports hot reload. Changes made to files in the `app/` directory appear without a full rebuild. Keep the development server running while you test.

### Connect through a dev tunnel

If the app doesn't load after you scan the QR code, network restrictions might be blocking the connection between your device and computer. Use a private dev tunnel to connect over HTTPS instead of the local network:

1. Stop the development server by pressing **Ctrl+C**.
2. Sign in to Azure CLI and start the development server with tunneling enabled.

   ```bash
   az login
   npm run dev -- --tunnel
   ```

3. After the tunnel connects, scan the new QR code by using the **Power Apps Developer** app. Don't reuse the previous QR code.

To use a specific Microsoft Entra tenant, run:

```bash
az login --tenant <tenant-id>
npm run dev -- --tunnel --tunnel-tenant <tenant-id>
```

Replace `<tenant-id>` with your organization's tenant ID.

> [!NOTE]
> Tunnel mode requires outbound HTTPS connections on port 443 with TLS 1.2 or later, to `login.microsoftonline.com`, `global.rel.tunnels.api.visualstudio.com`, `*.rel.tunnels.api.visualstudio.com`, and `*.devtunnels.ms`. If your network blocks these endpoints, contact your network administrator.

The tunnel is authenticated and deleted when the development server exits. Don't share the QR code publicly.

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

## Step 10: Deploy your app

From the project folder, run the following command in your AI coding host:

```text
/deploy
```

When prompted, review and confirm the target environment. The command builds and publishes your app to the Power Platform environment specified in `power.config.json`. Wait until the build and deployment complete successfully before you continue.

Publishing to Power Platform doesn't create or distribute an installable iOS or Android package. To create an installable package for iOS or Android, use Power Apps Wrap:

1. Open [Power Apps](https://make.powerapps.com) and select the same environment used for deployment.
2. Open **Wrap** and create or open a Wrap project for the deployed app.
3. Configure the target platforms, bundle ID, app registration, branding, and signing settings. Use the app registration configured in step 6.
4. Build and sign the package, and then test it on a physical device before distribution.
5. Distribute the signed package through your organization's approved channel.

Learn more in [Customize and build your mobile app using the wrap wizard](../../maker/common/wrap/wrap-how-to.md).

## Step 11: Add push notifications by using Firebase Cloud Messaging

To receive push notifications in your native app, use React Native Firebase for Firebase Cloud Messaging (FCM) and `expo-notifications` for permissions and foreground notification display.

> [!IMPORTANT]
> The Power Apps Mobile Preview app doesn't currently support testing push notifications. You also can't build apps that use push notifications by using the Power Apps Wrap process in step 10. The template's `npm run build:android` and `npm run build:ios` commands use Wrap, so they aren't a supported build path for these apps.

1. From the app directory, install these exact versions:

   ```bash
   npm install --save-exact @react-native-firebase/app@25.1.0 @react-native-firebase/messaging@25.1.0 expo-notifications@55.0.23 expo-build-properties@55.0.14
   ```

2. Add Firebase client configuration. Register your Android and iOS apps in the [Firebase console](https://console.firebase.google.com/). Download `firebase/google-services.json` and `firebase/GoogleService-Info.plist` into your app project. The registered app identifiers must match your app's configuration. For iOS, enable the Apple Push Notifications capability and configure APNs credentials in Firebase. See the [Firebase Android integration guide](https://firebase.google.com/docs/cloud-messaging/android/get-started) and [Firebase Apple integration guide](https://firebase.google.com/docs/cloud-messaging/ios/get-started).

3. Update `app.config.js`. Merge these settings into the existing `customizeExpoConfig` function. Preserve the template's `createPowerAppsExpoConfig` call, app identity, and other settings. Merge existing plugin entries instead of adding duplicates, and include only the Firebase client files for platforms you build.

   | Setting | Change |
   |---------|--------|
   | `plugins` | Add `'expo-notifications'`, `'@react-native-firebase/app'`, and `'@react-native-firebase/messaging'`. |
   | `expo-build-properties` plugin | Add `['expo-build-properties', { ios: { useFrameworks: 'static', forceStaticLinking: ['RNFBApp', 'RNFBMessaging'] } }]`. |
   | `android.googleServicesFile` | Set to `'./firebase/google-services.json'`. |
   | `ios.googleServicesFile` | Set to `'./firebase/GoogleService-Info.plist'`. |
   | `ios.entitlements['aps-environment']` | Set to `'development'` for development signing or `'production'` for distribution signing. |
   | `ios.infoPlist.UIBackgroundModes` | Add `'remote-notification'`, preserving other modes. |

4. Add client-side notification handling. Create a native-only helper such as `src/native/pushNotifications.ts` and wire it into your app. See [React Native Firebase messaging](https://rnfirebase.io/messaging/usage) and [Expo SDK 55 notifications](https://docs.expo.dev/versions/v55.0.0/sdk/notifications/) for the client-side integration.

   Subscribe opted-in users to an agreed public topic, or register their FCM tokens through an authenticated backend. Handle `onTokenRefresh`, account changes, and opt-out. Topic membership isn't authorization; don't include confidential data in notifications.

5. Rebuild and reinstall your app-specific native binary before testing. JavaScript-only deployment doesn't apply native dependency or configuration changes. Test permissions, foreground display, background delivery, and notification taps on physical devices. Expo Go doesn't include React Native Firebase; don't assume a shared developer player contains your Firebase configuration. The Preview app and Wrap limitations described earlier apply.

## See also

- [Wrap requirements and prerequisites](../../maker/common/wrap/prerequisites.md)  
- [Manual code sign for iOS](../../maker/common/wrap/code-sign-ios.md)  
- [Code sign for Android](../../maker/common/wrap/code-sign-android.md)  
- [Troubleshoot issues in the native mobile app](troubleshoot-native-apps.md)  
 