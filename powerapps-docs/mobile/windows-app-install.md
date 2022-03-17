---
title: Install Power Apps for Windows (preview) | Microsoft Docs
description: Install Power Apps for Windows (preview).
author: mduelae
ms.component: pa-user
ms.topic: quickstart
ms.date: 02/25/2022
ms.subservice: mobile
ms.author: mkaur
ms.custom: ""
ms.reviewer: ""
ms.assetid: 
search.audienceType: 
  - enduser
search.app: 
  - PowerApps
  - D365CE
searchScope:
  - "Power Apps"
---

# Install Power Apps for Windows (preview) 

[!INCLUDE [cc-beta-prerelease-disclaimer](../includes/cc-beta-prerelease-disclaimer.md)]

Install Power Apps for Windows to run model-driven app or canvas app on your Windows device. For more information on Power Apps, see [What is Power Apps](/powerapps/powerapps-overview).


> [!IMPORTANT]
> - This is a preview feature.
> - Preview features aren’t meant for production use and may have restricted functionality. These features are available before an official release so that customers can get early access and provide feedback.
> - This feature is being gradually rolled out across regions and might not be available yet in your region.

## Install the app

1. Go to the Microsoft Store and install [Power Apps (Preview)](https://www.microsoft.com/store/apps/9MVC8P1Q3B29) for Windows.  
2. When the app is installed, open it and [sign in](windows-app-use.md). 
> [!NOTE]
> If you run into issues during the installation process or the app closes without warning, follow the steps in the next section: [WebView2 Runtime](windows-app-install.md#webview2-runtime)

## Webview2 Runtime

If you get an **Update Microsoft Edge** error message when you're installing Power Apps for Windows, this means you don't have WebView2 Runtime on your device.

> [!div class="mx-imgBorder"]
> ![WebView2 Runtime errow.](media/webview2.png "WebView2")

Power Apps for Windows also won't run correctly if you have an older version of WebView2. Follow these steps to see which version you have installed:

1. On your device, go to **Settings** > **Apps** > **Apps & features**.
2. Search for **WebView**. You need version **99.0 or later** installed to run Power Apps for Windows.

In both cases, whether you or get an error message or have an older version installed, you need to install WebView2 Runtime.

You need administrator rights on your device to install WebView2. If you don't have admin rights, ask your administrator to install it for you. 
 
1. [Download the WebView2 Runtime](https://developer.microsoft.com/microsoft-edge/webview2/#download-section).
2. Download version **99.0 or later**. Installing an earlier version may cause Power Apps to crash.
3. Under **Evergreen Bootstrapper**, select **Download**.
4. Go over the license terms and privacy statement and then select **Accept and Download**.
5. Run **MicroEdgeWebview2Setup.exe**.

