---
title: Power Apps native mobile apps overview (preview)
description: Power Apps native apps let developers build code-first, AI-guided mobile apps for iOS and Android. Start building faster with the mobile-app plugin today.
author: shwetamurkute
ms.author: ruchidixit
ms.reviewer: smurkute
ms.service: powerapps
ms.subservice: mobile
ms.topic: overview
ms.date: 09/07/2026
ms.collection: get-started
search.audienceType:
  - developer
  - maker
---

# Power Apps native mobile apps overview (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

Native mobile apps are standalone iOS and Android applications built with the help of an AI coding agent by using the mobile-app plugin. You describe your app in natural language, review a proposed plan, and then generate a React Native, Expo, and TypeScript project that connects to Power Platform services.

> [!IMPORTANT]
>
> - This is a preview feature.
> - Preview features aren't meant for production use and might have restricted functionality. These features are subject to [supplemental terms of use](https://go.microsoft.com/fwlink/?linkid=2216214), and are available before an official release so that customers can get early access and provide feedback.

The planning experience helps you review the app's:

- Data model
- Native capabilities
- Connectors
- Design
- Screens

After you approve the plan, the plugin generates the application project.

## Key characteristics
| Characteristics | Description |
|------------|-------------|
| Runtime | Standalone iOS and Android applications. |
| Technology stack | React Native, Expo, and TypeScript. |
| Identity | Microsoft Entra app registration. |
| Data | Dataverse tables and Power Platform connectors. |
| Distribution | App Store, Google Play, and Mobile Device Management (MDM). |

## Benefits

Native mobile apps provide several benefits for organizations that require advanced mobile experiences. Choose native mobile apps when:

- Performance is critical. You need lower latency and near real-time processing.
- You need deep hardware or OS integration, such as advanced camera controls, sensors, Bluetooth/NFC, complex background tasks, widgets, or tight OS-level integrations.
- User experience and polish matter most. You want the app to feel like a native iOS or Android app and match platform conventions precisely.
- You're targeting a single platform. If you need only iOS or only Android, there is no cross-platform code-sharing benefit to consider.
- You're making a long-term investment in a single platform. Native apps aren't recommended for minimum viable product (MVP)-scoped projects.

## Prerequisites

Before you begin, ensure that your development environment, Power Platform environment, and mobile device meet the following requirements.

### Workstation

Your workstation must have:

- Node.js 24 (LTS)
- Git 2.30 or later
- One of the following supported hosts:
  - GitHub Copilot CLI
  - Visual Studio Code with Copilot Chat
  - Claude Code

Use the following commands to verify the installed versions:

```bash
    node --version  # expected version is v24.x or later
    npm --version   # expected version is 10.x or later
    git --version   # expected version is 2.30.x or later
```

### Power Platform environment 

- Dataverse enabled if the app uses Dataverse tables. 
- System Customizer role or equivalent for the planned schema operations. 
- Admin support for app registration, Wrap, and (if used) publishing/assigning Mobile Offline Profiles. 

### Mobile device 

- Supported iOS or Android device with the Power Apps Developer app installed. You need to install the app for [iOS](https://apps.apple.com/in/app/power-apps-mobile-preview/id6753083462) or [Android](https://play.google.com/store/apps/details?id=com.microsoft.PreviewApp) from respective marketplace.
- Device and workstation on the same reachable network
    

## Limitations

The following capabilities aren't currently supported:

- Push notifications.
- AI-first controls created through agent integration with MCS.
- Power Automate Flow integration.
- Converting existing canvas apps to native apps.
- Apple CarPlay support.

## Next steps

[Quickstart](quickstart-native-apps.md)

