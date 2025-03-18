---
title: System requirements and prerequisites for Wrap
description: Learn about system requirements and other prerequisites for wrap.
author: komala2019
ms.topic: article
ms.custom: canvas
ms.reviewer: smurkute
ms.date: 02/04/2025
ms.subservice: canvas-maker
ms.author: koagarwa
search.audienceType: 
  - maker
---

# System requirements and prerequisites for Wrap

Before you start using Wrap to create native mobile apps from your Power Apps canvas apps, ensure that your system meets the following requirements and prerequisites.

The following list explains what you'll need before you can start using wrap feature to publish one or more canvas apps as a mobile app package.

## Software and device requirements

- Mac device for [manual code signing with iOS](code-sign-ios.md)
- Windows PC for [manual code signing with Android](code-sign-android.md)
- To run the wrapped mobile app:
  - Android device with version 10 or higher
  - iOS device with version 14 or higher

> [!NOTE]
> Developing apps for the iOS platform requires an [Apple Developer Program](https://developer.apple.com/) account.

## Permissions and access requirements

1. You need access to:

    - One or more [canvas apps](../../canvas-apps/share-app.md) to build the wrap project.
    - Create azure blob storage and add the account name and container name. More information:[Create an Azure storage account](/azure/storage/common/storage-account-create?tabs=azure-portal)
    - [Azure portal](https://portal.azure.com/) to create [app registration](/azure/active-directory/develop/quickstart-register-app#prerequisites) and to register your app, which should be within the same environment as your Power Apps.

1. An Azure admin must grant you access to use the specific wrap app. More information: [API permissions](wrap-how-to.md#api-permissions).

1. This feature requires the apps to be part of a [managed or unmanaged solution](/power-platform/alm/solution-concepts-alm#managed-and-unmanaged-solutions). If your apps aren't part of a solution already, add them to an existing or a new solution. More information: [Create a canvas app from within a solution](../../canvas-apps/add-app-solution.md#add-an-existing-canvas-app-to-a-solution).

1. You need an Azure key vault to perform the automatic sign-in process through Wrap wizard. Ensure that your Azure key vault is in your tenant's default subscription. If it isn't, create one using your default subscription. More information: [Create a key vault using the Azure portal](/azure/key-vault/general/quick-create-portal).

    > [!NOTE]
    > This step will become mandatory from March 31, 2025.

1. Verify for the policies enabled for your application. More information: [Conditional Access policy templates](/entra/identity/conditional-access/concept-conditional-access-policy-common)

1. If multifactor authentication (MFA) is enabled, ensure that MFA is enabled for the accounts you'll use to sign in, or disable the conditional access policies.

There are two types of sign-in processes in Wrap:

- **Manual code sign-in for Android and iOS**: This is recommended. If you're creating a mobile app package for the Android platform and plan to code sign it manually, ensure you [generate keys](code-sign-android.md#generate-keys) and then [generate a signature hash](code-sign-android.md#generate-signature-hash) before you start. You need the generated signature hash to configure the [Redirect URI](overview.md#redirect-uri). More information: [Manual code sign-in for Android](code-sign-android.md).
- **Automatic sign-in using Wrap wizard**: This involves creating an Azure key vault. More information: [Create a key vault using the Azure portal](/azure/key-vault/general/quick-create-portal).

## Add canvas app to solution

Wrap for Power Apps requires the apps to be part of a solution. If your canvas apps aren't part of a solution already, add them to an existing or a new solution. From the left navigation pane, select **Solutions**. [!INCLUDE [left-navigation-pane](../../../includes/left-navigation-pane.md)] Select a solution and then select **Edit**.

:::image type="content" source="media/wrap-canvas-app/select-solution.png" alt-text="Select a solution.":::

Choose **+ Add existing** option from the top menu and select **App > Canvas app** in the dropdown list.

:::image type="content" source="media/wrap-canvas-app/select-add-existing.png" alt-text="Select Add existing from the menu.":::

Select **Outside Dataverse** tab and choose your app from the list. Press **Add** button to add this app to a solution.

:::image type="content" source="media/wrap-canvas-app/add-app.png" alt-text="Select Add app to a solution.":::

More information: [Add an app to a solution](../../canvas-apps/add-app-solution.md#add-an-existing-canvas-app-to-a-solution)


## Next steps

[Use the wrap wizard to build your mobile app](wrap-how-to.md)  

### See also

- [Troubleshoot issues with the wrap feature in Power Apps](/troubleshoot/power-platform/power-apps/manage-apps-and-solutions/wrap-issues)
- [Manual code sign on iOS](code-sign-ios.md)
- [Manual code sign on Android](code-sign-Android.md)
- [Code sign for Google Play Store](https://developer.android.com/studio/publish/app-signing)
- [Create your Azure Key Vault for automated code signing](create-key-vault-for-code-signing.md)
- [Frequently Asked Questions](faq.yml)
