---
title: Create or edit apps in a browser | Microsoft Docs
description: Create or edit apps in a browser by using PowerApps Studio for web.
services: ''
suite: powerapps
documentationcenter: na
author: karthik-1
manager: anneta
editor: ''
tags: ''

ms.service: powerapps
ms.devlang: na
ms.topic: article
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 10/06/2017
ms.author: sharik

---
# Create or edit apps in PowerApps Studio for web
Create and edit apps in PowerApps Studio for web, which opens in a browser window on Windows or other platforms.

## Prerequisites

* [Sign up](signup-for-powerapps.md) for PowerApps.
* Microsoft Edge, Google Chrome, or Internet Explorer 11 on a computer that's running Windows or a Mac.

## Open PowerApps Studio for web
1. Sign in to [powerapps.com](http://go.microsoft.com/fwlink/p/?LinkId=708209).
2. In the lower-left corner, click or tap **New app**.
   
    ![New app in left navigation bar](./media/create-app-browser/left-nav.png)

PowerApps Studio for web opens in a new tab in your browser, where you can create and edit apps in the same way as you can in PowerApps Studio for Windows.

## Next steps
* Automatically generate an app from your data in, for example, [Excel](get-started-create-from-data.md) or [SharePoint](app-from-sharepoint.md).
* Learn how to [add a control and set properties](maker/add-configure-controls.md) that determine how your app appears and behaves.
* Unleash your creativity by [creating an app from scratch](get-started-create-from-blank.md).

## Known limitations
1. **Create a connection.**
   
    To [create a connection](maker/add-manage-connections.md) to a data source that requires service authentication, use [powerapps.com](https://web.powerapps.com), and then [add the connection](maker/add-data-connection.md) to an app in PowerApps Studio for web.
2. **Edit and save an app locally**.
   
    For best results, use PowerApps Studio for Windows to edit and save apps locally. In a browser, you can't save changes to a local app, or you must save a new file instead of replacing the file that you opened.
3. **Use signal functions.**
   
    **[Acceleration and Compass](functions/signals.md)** functions return accurate values in a published app, but those functions return zero values as you create or modify an app in a browser.
4. **Export and import data.**
   
    You can [export and import data](controls/control-export-import.md) in a published app but not as you create or modify an app in a browser.
5. **Copy a control across two sessions.**
   
    You can't copy controls from one session of PowerApps Studio for web to another session of PowerApps Studio for web.

