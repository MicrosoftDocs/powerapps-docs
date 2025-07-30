---
title: System requirements and prerequisites for Wrap
description: Learn about system requirements and other prerequisites for wrap.
author: komala2019
ms.topic: article
ms.custom: canvas
ms.reviewer: smurkute
ms.date: 07/09/2025
ms.subservice: canvas-maker
ms.author: koagarwa
search.audienceType: 
  - maker
---

# System requirements and prerequisites for Wrap

Before you use Wrap to create native mobile apps from your Power Apps canvas apps, check that your system meets these requirements.

## Software and device requirements

- You need a Mac device for [manual code signing with iOS](code-sign-ios.md).
- You need a Windows PC for [manual code signing with Android](code-sign-android.md).
- To run the wrapped mobile app:
  - Android device with version 10 or higher
  - iOS device with version 14 or higher

> [!NOTE]
> You need an [Apple Developer Program](https://developer.apple.com/) account to develop apps for iOS.

## Permissions and access requirements

1. You need access to:
    - One or more [canvas apps](../../canvas-apps/share-app.md) to build the wrap project.
    - Azure blob storage, including the account name and container name. More information: [Create an Azure storage account](/azure/storage/common/storage-account-create?tabs=azure-portal).
    - The [Azure portal](https://portal.azure.com/) to create [app registration](/azure/active-directory/develop/quickstart-register-app#prerequisites) and register your app, which should be in the same environment as your Power Apps.

1. An Azure admin must grant you access to use the specific wrap app. More information: [API permissions](wrap-how-to.md#grant-api-permissions-as-an-azure-tenant-admin).
1. Your apps must be part of a [managed or unmanaged solution](/power-platform/alm/solution-concepts-alm#managed-and-unmanaged-solutions). If not, add them to an existing or new solution. More information: [Create a canvas app from within a solution](../../canvas-apps/add-app-solution.md#add-an-existing-canvas-app-to-a-solution).
1. You need an Azure key vault to perform the automatic sign-in process through Wrap wizard. More information: [Create a key vault using the Azure portal](/azure/key-vault/general/quick-create-portal).
1. Check the policies enabled for your application. More information: [Conditional Access policy templates](/entra/identity/conditional-access/concept-conditional-access-policy-common)
1. If multifactor authentication (MFA) is enabled, make sure MFA is enabled for the accounts you'll use to sign in, or disable the conditional access policies.

## Sign-in options in Wrap

- **Manual code sign-in for Android and iOS**: This option is best for most scenarios. For Android, [generate keys](code-sign-android.md#generate-key-and-signature-hash) and [generate a signature hash](code-sign-android.md#generate-signature-hash-key-and-certificate) before you start. You need the signature hash to set up the [Redirect URI](overview.md#redirect-uri). More information: [manual code sign-in for Android](code-sign-android.md).
- **Automatic sign-in using Wrap wizard**: This option requires an Azure key vault. More information: [creating a key vault using the Azure portal](/azure/key-vault/general/quick-create-portal).

## Add canvas app to a solution

Wrap requires your apps to be part of a solution. If your canvas apps aren't already in a solution, add them to an existing or new solution.

1. In the left navigation pane, select **Solutions**. [!INCLUDE [left-navigation-pane](../../../includes/left-navigation-pane.md)]
1. Select a solution, and then select **Edit**.

:::image type="content" source="media/wrap-canvas-app/select-solution.png" alt-text="Screenshot of the Solutions page with a solution selected.":::

Select **+ Add existing** from the top menu, and then select **App > Canvas app** from the dropdown.

:::image type="content" source="media/wrap-canvas-app/select-add-existing.png" alt-text="Screenshot of the top menu showing the Add existing option selected from the menu.":::

Select the **Outside Dataverse** tab, select your app from the list, and then select **Add** to add the app to the solution.

:::image type="content" source="media/wrap-canvas-app/add-app.png" alt-text="Screenshot of the Outside Dataverse tab with a canvas app selected and the Add button highlighted.":::

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
