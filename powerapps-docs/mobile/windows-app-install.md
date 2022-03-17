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
  > [!NOTE]
  > If you run into issues during the installation process, then follow the steps in the next section: [WebView2 Runtime](windows-app-install.md#webview2-runtime)
2. Open Power Apps for Windows and [sign in](windows-app-use.md). 

## Webview2 Runtime

If you don't have WebView2 Runtime installed, you'll get this error message: **Update Microsoft Edge**

> [!div class="mx-imgBorder"]
> ![WebView2 Runtime errow.](media/webview2.png "WebView2")

If have an older version of WebView2 Runtime then Power Apps (Preview) for Windows won't run correctly. To check which version of WebView2 that you have installed; go to **Settings** > **Apps** > **Apps & features**. Search for **WebView** and verify that you have version **99.0 or later** installed.

In both cases to fix the issue, you need to install WebView2 Runtime.

### Install Webview2 Runtime

You need administrator rights on your Windows device to install WebView2. If you don't have administrator rights, then your administrator will need to install it for you. Without WebView2 Runtime, you won't be able to run your apps on Power Apps for Windows.

1. [Download the WebView2 Runtime](https://developer.microsoft.com/microsoft-edge/webview2/#download-section).
2. Download version **99.0 or later**. Installing an earlier version may cause Power Apps to crash.
3. Under **Evergreen Bootstrapper**, select **Download**.
4. Go over the license terms and privacy statement and then select **Accept and Download**.
5. When the download is complete, then run the **MicroEdgeWebview2Setup.exe**.

