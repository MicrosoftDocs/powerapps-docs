---
title: Disconnect Git version control to edit canvas apps 
description: Learn how to disconnect Git version control to edit canvas app
author: angela21k
ms.topic: how-to
ms.custom: canvas
ms.reviewer: mkaur
ms.date: 5/14/2025
ms.subservice: canvas-maker
ms.author: angelakim
search.audienceType:
  - maker
contributors:
  - mduelae
  - angela21k
  - gregli-msft
  - mkaur-msft
  - gesnaaggarwal
---

# Disconnect Git version control to edit canvas apps 

Git version control for editing apps has been removed and is no longer supported. 

If your app currently uses this feature, follow these steps to disconnect it:

1. Open your [canvas app for editing](edit-app.md) in Power Apps Studio. On the command bar, select **Settings**.
1. Select **Git version control** and then select **Disconnect**.

If you are using PASopa, download your app from your Git provider and [pack the .zip file to an .msapp file](https://github.com/microsoft/PowerApps-Tooling/tree/master/src/PASopa#power-platform-cli-usage). Once your .msapp file is uploaded to Power Apps, follow the steps above to disconnect.


 > [!NOTE]
 > Git version control is replaced with the source control integration feature. More information: [Source code integration](/power-platform/alm/git-integration/canvas-apps-git-integration)


