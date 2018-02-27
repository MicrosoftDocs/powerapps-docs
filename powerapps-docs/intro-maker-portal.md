---
title: Introduction to powerapps.com | Microsoft Docs
description: A new home for all makers of apps.
services: ''
suite: powerapps
documentationcenter: na
author: linhtranms
manager: anneta
editor: ''
tags: ''

ms.service: powerapps
ms.devlang: na
ms.topic: article
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 10/28/2016
ms.author: litran

---
# Introduction to powerapps.com
The PowerApps team is re-introducing [powerapps.com](http://web.powerapps.com) as the new home for app creators. We've re-designed the page as the primary site for creators to easily get started on creating apps, use the Microsoft Common Data Service, and manage their apps all in one location. In this article, I will walk you through the following:

* the header
* the homepage
* the **Apps** page

## Header
When you sign up and first sign in to powerapps.com, you will notice the site's new header. Near the left edge of the header is the Office waffle. This is a quick place for you to access all other Office products such as PowerPoint, OneNote, and Word, as well as Microsoft Flow and Dynamics 365.

![Header Waffle](./media/intro-maker-portal/waffle.png)

Near the right edge of the header, you'll first see an environment dropdown, where you can quickly switch between environments. **Default environment** is likely selected by default. [Learn more about environments](environments-overview.md).

![Header Environment](./media/intro-maker-portal/environment.png)

Next to the environment dropdown, you will see a download icon. Click or tap this icon to display a dialog box with links to download PowerApps Mobile (for iOS or Android) or PowerApps Studio for Windows.

![Header Download](./media/intro-maker-portal/downloads2.png)

Next to the download icon, you will see a gear icon for settings. Click or tap this icon to display links for connections, gateways, and the admin center.

![Header Settings](./media/intro-maker-portal/settings_items2.png)

Next to settings, you will see a question-mark icon for help. Click or tap this icon to display links to Guided learning, Documentation, Support, Community, Blogs, Legal and Privacy.

![Header Help](./media/intro-maker-portal/help_items2.png)

## Homepage
After you sign in to [powerapps.com](http://web.powerapps.com), you'll land on the homepage by default. We have changed the layout of this homepage to help you get started quickly, whether you're creating apps or want to explore the Common Data Service.

If you've signed in to PowerApps before and run or created some apps, the first section you will see on your homepage is a list of **Recent apps**. They are sorted by the date on which they were most recently opened.

![Recent Apps](./media/intro-maker-portal/recentapps2.png)

Near the upper-right corner, an arrow is labeled **Apps** and links to the **Apps** page directly so you can see all of your apps.

If you've never signed in, created an app, or run an app before, you won't see the **Recent apps** section. Instead you'll see the banner **Create an app**.

![Create an app](./media/intro-maker-portal/createapp.png)

Click or tap **Get started** on this banner to display options for creating an app using **PowerApps Studio for Windows** or **PowerApps Studio for the web**.

![Create app Modal](./media/intro-maker-portal/createmodal2.png)

Next to **Get started**, you can find links to our tutorial videos on how to quickly create an app from data (in either SharePoint or PowerApps) and then share the app. The **Learn more** arrow link will take you to a topic about how to create an app from existing data.

Below the **Create an app** banner is the **Use the Microsoft Common Data Service** banner.

![Microsoft Common Data Service](./media/intro-maker-portal/cds2.png)

Under **Common Data Service**, a different button will appear, depending on your license or permission.

* If the **Start trial** button appears, you don't have a PowerApps P2 license, which the Common Data Service requires. Click or tap this button to open the page where you can sign up for a free, 90-day trial of this license. [Learn more about PowerApps licenses](signup-for-powerapps.md).
* If the **Get started** button appears, you're in an environment that doesn't have a Common Data Service database or you don't have access to it. Click or tap this button to create an environment and database at once, so you can start to use Common Data Services for your apps. [Learn more about creating environments](administrator/environments-administration.md).
  
    ![Create an environment and a database](./media/intro-maker-portal/createenvanddb2.png)
  
    If you don't want to create an environment, you can always switch to an environment to which you have access.
* If the **Create database** button appears, you're in an environment that doesn't have a Common Data Service database but you have permission to create one.
  
    ![Create database](./media/intro-maker-portal/cds-createdb2.png)
  
    Clicking or tapping this button will provision a database for this environment.
  
    ![Create database](./media/intro-maker-portal/cds_createdb22.png)
* If the **Browse entities** button appears, you're in an environment that has a Common Data Service database provisioned already and you have access to it. Click or tap that button to open the **Entities** page.
  
    ![Create database](./media/intro-maker-portal/cds_browseentities2.png)

Below the **Use the Microsoft Common Data Service** banner, you'll see a set of sample apps and connected sample apps that we created for you to use.

* **Sample apps** - Sample apps were built for different business scenarios in either phone or tablet layout. You can click an app to quickly view a description of what the app does, what layout the app was built for, and what capabilities the app showcases such as camera, GPS, or radio buttons. It's a quick way for new users to learn capabilities of PowerApps, and you can use a template to create an identical app in PowerApps Studio for Windows.
  
    ![Sample Apps](./media/intro-maker-portal/sampleapps2.png)
* **Connected sample apps** - These apps connect to your data via a data connection such as Office 365, Salesforce, Trello, and Wunderlist. This set of apps is different from the sample apps above. When you click or tap a connected sample app, you actually provision a new instance of the app (think of it as a template). It will prompt you to enter your credentials to connect to your data. The beautiful thing about a connected sample app is that an instance is provisioned for you right here, and you can open it in PowerApps Studio to learn how the corresponding app was built. The downside is that it can take pretty long (up to a minute) to create. So please be patient and let the browser open when you click or tap a connected sample app.
  
    ![Connected Sample Apps](./media/intro-maker-portal/connectedsampleapps2.png)

## New Apps page
You can access the **Apps** page via the left navigation bar on [powerapps.com](http://web.powerapps.com).

![Left navigation](./media/intro-maker-portal/leftnav2.png)

The **Apps** page previously allowed you to switch between tile view and list view. After October 26, 2016, it supports only list view.

![Apps list view](./media/intro-maker-portal/listview2.png)

Please note that the list view shows only apps in the selected environment. To view apps in a different environment, switch to it by using the environment switcher in the header. [Learn more about switching environments](working-with-environments.md).

## What's new?

* Clicking or tapping an app now opens it in PowerApps Studio for web in a new tab.
* By default, the **Apps** page shows all apps that you have permission to edit. To view **All apps** (including apps you can only use), select the **All apps** filter.
  
   ![Apps filter](./media/intro-maker-portal/allapps_filter.png)

We also have:

* **Apps I can use**, which lists all apps that have been shared with you with User permission (can only run the app). Please note that you can also acquire these apps in [Dynamics 365](http://home.dynamics.com).
* **Apps I own**, which lists all apps you have authored.
* **Apps I contribute to**, which lists all apps that have been shared with you with Contributor permission.
* **Sample apps**, which lists all sample apps (not connected sample apps).

If you click or tap the information circle, the app details page opens.

![App Details](./media/intro-maker-portal/ibubble.png)

If you click the ellipsis for an app, options such as Play, Edit, Share, and Details appear.

![App's options](./media/intro-maker-portal/ellipsis.png)

That is mainly what's new on powerapps.com, which is geared toward app makers. We hope this is helpful to you. Please leave comments on what you like so far and would like to see. We'd love to hear your feedback!

