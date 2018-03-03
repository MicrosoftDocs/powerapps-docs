---
title: Create a data loss prevention (DLP) policy | Microsoft Docs
description: Walkthrough of how to create a data loss prevention (DLP) policy
services: ''
suite: powerapps
documentationcenter: na
author: SKjerland
manager: kfile
editor: ''
tags: ''

ms.service: powerapps
ms.devlang: na
ms.topic: quickstart
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 03/02/2018
ms.author: sharik

---
# Quickstart: Create a data loss prevention (DLP) policy
To protect data in your organization, PowerApps lets you create and enforce policies that define which consumer services/connectors specific business data can be shared with. These policies that define how data can be shared are referred to as data loss prevention (DLP) policies. DLP policies ensure that data is managed in a uniform manner across your organization, and they prevent important business data from being accidentally published to services such as social media sites.

In this quickstart, you'll learn how to create a DLP policy that prevents data that's stored in your SharePoint database from being published to Twitter.

## Prerequisites
To follow this quickstart, the following items are required:
* Either PowerApps Plan 2 or Flow Plan 2. Alternatively, you can sign up for a [free PowerApps Plan 2 trial](https://web.powerapps.com/signup?redirect=marketing&email=).
* Either Environment Admin or Tenant Admin permissions.

## Sign in to Dynamics 365
Sign in to Dynamics 365 at [https://home.dynamics.com]([https://home.dynamics.com).

## Find an app on the Home page
The Home page may show several types of business apps, but you can find a specific app by typing part of its name in the search box. You can also filter the list to show only apps created by a specific source, such as PowerApps. To do this, click or tap **Filter** and then select the source.

If you've recently installed the app, it might not immediately appear in the list of apps. Click or tap **Sync** to show all of your apps. This process may take up to a minute.

![](./media/run-app-browser/dynamics-365-home.png)

## Run an app from the task pane
After you find an app, you can pin it to the task pane for easier access. To pin an app, click or tap the ellipsis (...) on the app tile, and then click or tap **Pin this app**.

![](./media/run-app-browser/homepage-pin.png)

To run the pinned app from the task pane, click or tap **Dynamics 365** in the upper-left corner, locate the app under **My apps**, and then click or tap it.

![](./media/run-app-browser/taskpane.png)

## Run an app from a URL
You can save an app's URL as a bookmark in your browser and run it by selecting the bookmark, or you can send a URL as a link through email. If someone else created an app and shared it with you in an email, you can run the app by clicking or tapping the link in the email. When running an app using a URL, you may be prompted to sign in using your Azure Active Directory credentials.

![](./media/run-app-browser/web-login.png)

## Connect to data
If an app requires a connection to a data source or permission to use the device's capabilities (such as the camera or location services), you must give consent before you can use the app. Typically, you're prompted only the first time.

![Connection](./media/run-app-browser/app-connection.png)

## Close an app
To close an app, sign out of the Dynamics 365 Home page, or open another app.

## Next steps
In this quickstart, you learned how to run a canvas-based or model-driven app in a web browser. To learn more about PowerApps, continue to the PowerApps tutorials.

> [!div class="nextstepaction"]
> [PowerApps Tutorials](get-started-create-from-blank.md)
