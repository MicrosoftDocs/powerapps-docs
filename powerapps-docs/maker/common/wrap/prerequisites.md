---
title: System requirements and prerequisites for Wrap
description: Learn about system requirements and other prerequisites for wrap.
author: komala2019
ms.topic: article
ms.custom: canvas
ms.reviewer: smurkute
ms.date: 02/03/2025
ms.subservice: canvas-maker
ms.author: koagarwa
search.audienceType: 
  - maker
---

## System requirements

The following list explains what you'll need before you can start using wrap feature to publish one or more canvas apps as a mobile app package.

### Permissions and access requirements

- Access to one or more [canvas apps](../../canvas-apps/share-app.md) to build the wrap project
- Access to Azure portal to create [app registration](/azure/active-directory/develop/quickstart-register-app#prerequisites)
- Access to [Microsoft App Center](https://appcenter.ms/)

### Software and device requirements

- Mac device for [code signing with iOS](code-sign-ios.md)
- Windows PC for [code signing with Android](code-sign-android.md)
- To run the wrapped mobile app:
    - Android device with version 10 or higher
    - iOS device with version 14 or higher

> [!NOTE]
> Developing apps for the iOS platform requires an [Apple Developer Program](https://developer.apple.com/) account.

## Prerequisites

You need access to:
- [Azure portal](https://portal.azure.com/) to register your app which should be within same environment as that of Power Apps.
- You will also need Azure admin to grant you access to use the specific wrap app. More information : [API permissions](wrap-how-to.md#step-2-register-app)
- [App center](https://appcenter.ms/) to add new organization and apps which should be in the same environment as your Azure portal and Power Apps.
- This feature requires the apps to be part of a  [managed or unmanaged solution](/power-platform/alm/solution-concepts-alm#managed-and-unmanaged-solutions). If your apps aren't part of a solution already, add them to an existing or a new solution. More information: [Create a canvas app from within a solution](../../canvas-apps/add-app-solution.md#add-an-existing-canvas-app-to-a-solution). 

There are 2 types of sign in process in wrap:
- Manual code sign in Android and IOS which is recommended. If you're creating a mobile app package for Android platform and you plan to code sign it manually, ensure you [<u>generate keys</u>](code-sign-android.md#generate-keys), and then [generate signature hash](code-sign-android.md#generate-signature-hash) before you start. You need the generated signature hash to configure the [Redirect URI](overview.md#redirect-uri). More information: [Manual code sign in Android](code-sign-android.md) 
- Automatic sign in using wrap wizard by creating Azure key vault. More information: [Create Azure Key Vault for wrap in Power Apps](create-key-vault-for-code-signing.md)

## Add canvas app to solution

Wrap for Power Apps requires the apps to be part of a solution. If your canvas apps aren't part of a solution already, add them to an existing or a new solution. From the left navigation pane, select **Solutions**. [!INCLUDE [left-navigation-pane](../../../includes/left-navigation-pane.md)] Select a solution and then select **Edit**.

:::image type="content" source="media/wrap-canvas-app/select-solution.png" alt-text="Select a solution.":::

Choose **+ Add existing** option from the top menu and select **App > Canvas app** in the dropdown list.

:::image type="content" source="media/wrap-canvas-app/select-add-existing.png" alt-text="Select Add existing from the menu.":::

Select **Outside Dataverse** tab and choose your app from the list. Press **Add** button to add this app to a solution.

:::image type="content" source="media/wrap-canvas-app/add-app.png" alt-text="Select Add app to a solution.":::

More information: [Add an app to a solution](../../canvas-apps/add-app-solution.md#add-an-existing-canvas-app-to-a-solution)
