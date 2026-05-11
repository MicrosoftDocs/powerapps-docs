---
title: Add data connections to canvas apps
description: Learn how to add a data connection to an existing canvas app or to an app that you're building from scratch.
author: lancedMicrosoft

ms.topic: how-to
ms.custom: canvas
ms.reviewer: mkaur
ms.date: 05/11/2025
ms.subservice: canvas-maker
ms.author: lanced
search.audienceType: 
  - maker
contributors:
  - mduelae
  - lancedmicrosoft
---
# Add data connections to canvas apps

In Power Apps, add a data connection to an existing canvas app or to an app that you're building from scratch. Your app can connect to SharePoint, Microsoft Dataverse, Salesforce, OneDrive, or [many other data sources](connections-list.md).

After you add a connection, your next step is to display and manage data from that data source in your app, as in these examples:

- Connect to OneDrive, and manage data in an Excel workbook in your app.
- Connect to Twilio, and send an SMS message from your app.
- Connect to Microsoft Dataverse, and update a table from your app.
- Connect to SQL Server, and update a table from your app.

## Prerequisites

[Sign up](../signup-for-powerapps.md) for Power Apps, and then [sign in](https://make.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) by providing the same credentials that you used to sign up.

## Add a data source

1. Create a [blank canvas app](create-blank-app.md) or open an existing canvas app for editing.
1. In Power Apps Studio, select **Data** from the [app authoring menu](power-apps-studio.md#5--app-authoring-menu) on the left pane.
1. Select **Add data** at the top of the **Data** pane.
1. In the search box, type the name of the connector or data source you want&mdash;for example, **SharePoint** or **Dataverse**.
1. Select the connector from the results list.
   - If you already have a configured connection for that connector, select it to add it to your app.
   - If no existing connection appears, select **Add a connection** to create a new one.

> [!NOTE]
> When you connect to **Microsoft Dataverse**, you can select the environment from the drop-down list before choosing a table. By default, the connection uses your current working environment.

Some connectors, such as **Office 365 Outlook**, require no additional steps and you can show data from them immediately. Other connectors, such as [SharePoint](connections/connection-sharepoint-online.md) and [SQL Server](connections/sql-connection-overview.md), prompt you for additional information&mdash;like a site URL or server name&mdash;before the connection is complete.

> [!TIP]
> Not sure which connector to use? Browse the full list at [Connectors overview](connections-list.md). You can also describe your scenario to [Copilot in Power Apps](ai-overview.md) and it can suggest an appropriate data source.

## Identify or change a data source

If you're updating an app, you might need to identify or change the source of data that appears in a gallery, a form, or another control. For example, you might need to locate a data source in an app that someone else created or that you built long ago.

1. Select the control&mdash;such as a gallery or form&mdash;for which you want to identify or change the data source.
1. On the **Properties** tab of the right-hand pane, find the **Data source** or **Items** property. The name of the current data source appears there.
1. To change the data source, select the drop-down next to the data source name, or edit the **Items** property directly in the formula bar.
1. Select or create a different data source as needed.

> [!NOTE]
> If the expected data source is missing from the **Data** pane, the connection might have expired or been revoked. Select **Add data** again, search for the connector, and re-authenticate to restore it.

## Troubleshooting tips

- **Connection not appearing**: Refresh the **Data** pane by closing and reopening it, or sign out and sign back in to Power Apps to refresh your available connections.
- **Authentication errors**: Some connectors&mdash;for example, SQL Server&mdash;require credentials or an on-premises data gateway. Confirm that your gateway is running and your credentials are valid.
- **Dataverse table not found**: Confirm that you're connected to the correct environment. You can switch environments from the Power Apps home page before opening the app.

## Next steps

- To show and update data from a source such as SharePoint, Dataverse, or SQL Server, [add a gallery](add-gallery.md) and [add a form](add-form.md).
- For connector-specific functions such as sending email or translating text, review the [Connectors overview](connections-list.md).
- To learn about working with data sources in formulas, see [Working with data sources](working-with-data-sources.md).


[!INCLUDE[footer-include](../../includes/footer-banner.md)]