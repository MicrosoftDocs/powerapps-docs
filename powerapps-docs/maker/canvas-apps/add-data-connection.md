---
title: Add data connections to canvas apps
description: Learn about how to add a data connection in an existing canvas app.
author: lancedMicrosoft
manager: kvivek
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 05/11/2021
ms.subservice: canvas-maker
ms.author: lanced
search.audienceType: 
  - maker
search.app: 
  - PowerApps
contributors:
  - tapanm-msft
  - lancedmicrosoft
---
# Add data connections to canvas apps

In Power Apps, add a data connection to an existing canvas app or to an app that you're building from scratch. Your app can connect to SharePoint, Microsoft Dataverse, Salesforce, OneDrive, or [many other data sources](connections-list.md).

Your [next step](#next-steps) after this article is to display and manage data from that data source in your app, as in these examples:

* Connect to OneDrive, and manage data in an Excel workbook in your app.
* Connect to Twilio, and send an SMS message from your app.
* Connect to Dataverse, and update a table from your app.
* Connect to SQL Server, and update a table from your app.

## Prerequisites

[Sign up](../signup-for-powerapps.md) for Power Apps, and then [sign in](https://make.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) by providing the same credentials that you used to sign up.

## Open a blank app

1. On the **Home** tab, select **Canvas app from blank**.

1. Specify a name for your app, and then select **Create**.

1. If the **Welcome to Power Apps Studio** dialog box appears, select **Skip**.

## Add data source

1. In the center pane, select **connect to data** to open the **Data** pane.

    If this were an existing app and the screen already contained a control, select **View** > **Data sources** to open the same pane.

1. Select **Add data source**.

1. Expand **Connectors**, and if the list of connections includes the one that you want, select it to add it to the app. Otherwise, skip to the next step. To connect to a table in Microsoft Dataverse instead, choose a table from the list of tables.

    ![Choose an existing connection.](./media/add-data-connection/choose-existing-connection.png)

1. To create a new connection, search for or select a connector such as SharePoint.

    ![Add connection.](./media/add-data-connection/add-connection.png)

1. Select **Create** to both create the connection and add it to your app.

    Some connectors, such as **Office 365 Outlook**, require no additional steps, and you can show data from them immediately. Other connectors prompt you to provide credentials, specify a particular set of data, or perform other steps. For example, [SharePoint](connections/connection-sharepoint-online.md) and [SQL Server](connections/connection-azure-sqldatabase.md) require additional information before you can use them. With [Dataverse](connections/connection-common-data-service.md), you can change the environment before you select a table.

## Identify or change a data source
If you're updating an app, you might need to identify or change the source of data that appears in a gallery, a form, or another control. For example, you might need to identify a data source as you update an app that someone else created or that you created long ago.

1. Select the control, such as a gallery, for which you want to identify or change the data source.

    The name of the data source appears on the **Properties** tab of the right-hand pane.

    ![Identify a connection.](./media/add-data-connection/identify-connection.png)

1. To show more information about the data source or to change it, select the down arrow next to its name.

    More information about the current data source appears, and you can select or create another source.

    ![Change a connection.](./media/add-data-connection/change-connection.png)

## Next steps

* To show and update data in a source such as Excel, SharePoint, Dataverse, or SQL Server, [add a gallery](add-gallery.md), and [add a form](add-form.md).
* For data in other sources, use connector-specific functions such as those for [Office 365 Outlook](connections/connection-office365-outlook.md), [Twitter](connections/connection-twitter.md), and [Microsoft Translator](connections/connection-microsoft-translator.md).


[!INCLUDE[footer-include](../../includes/footer-banner.md)]