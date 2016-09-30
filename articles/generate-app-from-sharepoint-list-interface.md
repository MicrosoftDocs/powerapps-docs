<properties
   pageTitle="Generate an app to manage data from a SharePoint Online list | Microsoft PowerApps"
   description="Generate a three-screen app to manage data from a SharePoint online list, whether the site is on-premises or in the cloud."
   services=""
   suite="powerapps"
   documentationCenter="na"
   authors="RickSaling"
   manager="erikre"
   editor=""
   tags=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="09/29/2016"
   ms.author="ricksal"/>

# Generate an app from the SharePoint Online list interface#

In a SharePoint Online list, generate a three-screen app that manages the list.

The [roll-out of the new modern experience](https://blogs.office.com/2016/07/25/modern-sharepoint-lists-are-here-including-integration-with-microsoft-flow-and-powerapps/) for SharePoint Online ("SPO") lists was released to Office 365. As a part of this release, you can **Create a new app** using PowerApps from the command bar of any SPO custom list.

Apps generated through this flow show up as views within the new SharePoint modern list experience.  This allows you to leverage PowerApps to build custom, mobile-optimized views of your existing lists and share them with your co-workers.  Since PowerApps is a cross-platform service, you can run the apps you generate across all of your devices including Windows, iOS, Android, and the web browser.

## Prerequisites

If you're unfamiliar with PowerApps, see [Introduction to PowerApps](getting-started.md).

As of this writing, PowerApps supports custom lists but not libraries. In addition, you can show data in some types of columns, such as **Choice** and **Picture**, but you can't update that data. For more information, see [Known issues](connection-sharepoint-online.md#known-issues).

## Generate a new app

1. Open your SharePoint Online site.

    ![](./media/generate-app-from-sharepoint-list-interface/generate-new-app.png)

2. Select **Create a new app** to open a panel in SharePoint that allows you to enter a name for your app and start the app creation process.

    ![](./media/generate-app-from-sharepoint-list-interface/enter-app-name.png)

3. Select **Create** to launch the PowerApps Studio for Web in a new browser tab, which creates a default app automatically based on the list’s schema and data.  For details on how can you customize and test apps created from SharePoint lists, see the [Create an app from a SharePoint list tutorial](https://powerapps.microsoft.com/tutorials/app-from-sharepoint/).

    ![](./media/generate-app-from-sharepoint-list-interface/powerapp-studio-for-web.png)

4. The generated app now appears.

    ![](./media/generate-app-from-sharepoint-list-interface/open-app-in-browser.png)

5. Selecting **Open** from the app’s list view will launch the app in a new tab in the browser.

    ![](./media/generate-app-from-sharepoint-list-interface/open-app.png)

6. Press Ctrl-S to save the generated app.

## Next steps ##

- To customize the browse screen (which appears by default), see [Customize a layout](customize-layout-sharepoint.md).
- To customize the details or edit screens, see [Customize a form](customize-forms-sharepoint.md).
