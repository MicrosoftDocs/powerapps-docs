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

Before using Wrap to create native mobile apps from your Power Apps canvas apps, make sure your system meets the following requirements.

## Software and device requirements

- A Mac device is required for [manual code signing with iOS](code-sign-ios.md).
- A Windows PC is required for [manual code signing with Android](code-sign-android.md).
- To run the wrapped mobile app:
  - Android device with version 10 or higher
  - iOS device with version 14 or higher

> [!NOTE]
> Developing apps for iOS requires an [Apple Developer Program](https://developer.apple.com/) account.

## Permissions and access requirements

1. You need access to:
    - One or more [canvas apps](../../canvas-apps/share-app.md) to build the wrap project.
    - Azure blob storage, including the account name and container name. More information: [Create an Azure storage account](/azure/storage/common/storage-account-create?tabs=azure-portal)
    - The [Azure portal](https://portal.azure.com/) to create [app registration](/azure/active-directory/develop/quickstart-register-app#prerequisites) and register your app, which should be in the same environment as your Power Apps.

2. An Azure admin must grant you access to use the specific wrap app. More information: [API permissions](wrap-how-to.md#api-permissions).

3. Your apps must be part of a [managed or unmanaged solution](/power-platform/alm/solution-concepts-alm#managed-and-unmanaged-solutions). If not, add them to an existing or new solution. More information: [Create a canvas app from within a solution](../../canvas-apps/add-app-solution.md#add-an-existing-canvas-app-to-a-solution).

4. You need an Azure key vault to perform the automatic sign-in process through Wrap wizard. Ensure your Azure key vault is in your tenant's default subscription. If not, create one using your default subscription. More information: [Create a key vault using the Azure portal](/azure/key-vault/general/quick-create-portal).

5. Verify the policies enabled for your application. More information: [Conditional Access policy templates](/entra/identity/conditional-access/concept-conditional-access-policy-common)

6. If multifactor authentication (MFA) is enabled, ensure MFA is enabled for the accounts you'll use to sign in, or disable the conditional access policies.

## Sign-in options in Wrap

- **Manual code sign-in for Android and iOS**: Recommended for most scenarios. For Android, [generate keys](code-sign-android.md#generate-keys) and [generate a signature hash](code-sign-android.md#generate-signature-hash) before starting. You'll need the signature hash to configure the [Redirect URI](overview.md#redirect-uri). More information: [Manual code sign-in for Android](code-sign-android.md).
- **Automatic sign-in using Wrap wizard**: Requires an Azure key vault. More information: [Create a key vault using the Azure portal](/azure/key-vault/general/quick-create-portal).

## Add canvas app to a solution

Wrap requires your apps to be part of a solution. If your canvas apps aren't already in a solution, add them to an existing or new solution. From the left navigation pane, select **Solutions**. [!INCLUDE [left-navigation-pane](../../../includes/left-navigation-pane.md)] Select a solution and then select **Edit**.

:::image type="content" source="media/wrap-canvas-app/select-solution.png" alt-text="Select a solution.":::

Choose **+ Add existing** from the top menu and select **App > Canvas app** from the dropdown.

:::image type="content" source="media/wrap-canvas-app/select-add-existing.png" alt-text="Select Add existing from the menu.":::

Select the **Outside Dataverse** tab and choose your app from the list. Press **Add** to add this app to a solution.

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
