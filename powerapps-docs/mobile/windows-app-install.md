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

1. Go to the Microsoft Store and install [Power Apps for Windows](https://www.microsoft.com/store/apps/9MVC8P1Q3B29).
2. Verify that you have **WebView2 Runtime** installed on your Windows device; go to **Settings** > **Apps** > **Apps & features**.
3. Search for **WebView** and verify that you have version **99.0 or later** installed. If you have an earlier version, then follow the steps in the [WebView2 Runtime](windows-app-install.md#webview2-runtime) section below.
4. Open Power Apps for Windows and [sign in](windows-app-use.md). 

### Webview2 Runtime

If you don't have WebView2 Runtime installed, you may encounter the following error message: **Update Microsoft Edge**

> [!div class="mx-imgBorder"]
> ![WebView2 Runtime errow.](media/webview2.png "WebView2")

You need to have administrator rights on your Windows device to install WebView2. If you don't have administrator rights, then your administrator will need to install it for you. Without WebView2 Runtime, you won't be able to run your apps on Power Apps for Windows.

1. To install WebView2 Runtime, [download the WebView2 Runtime](https://developer.microsoft.com/microsoft-edge/webview2/#download-section).
2. Download version **99.0 or later**. Installing an earlier version may cause Power Apps to crash.
3. Under **Evergreen Bootstrapper**, select **Download**.
4. Go over the license terms and privacy statement and then select **Accept and Download**.
5. When the download is complete, then run the **MicroEdgeWebview2Setup.exe**.

