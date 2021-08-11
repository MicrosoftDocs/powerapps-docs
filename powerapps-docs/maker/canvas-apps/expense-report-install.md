---
title: Set up and learn about the Expense Report sample app in Power Apps
description: Use the Expense Report sample app to create a canvas app, and preview the app features before you customize for business requirements.
author: norliu
ms.service: powerapps
ms.topic: sample
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 03/22/2021
ms.subservice: canvas-maker
ms.author: norliu
search.audienceType: 
  - maker
search.app: 
  - PowerApps
contributors:
  - tapanm-msft
  - norliu
---

# Set up and learn about the Expense Report sample app in Power Apps

Track expense reports from submission to approval. Tally line items as individual expenses accrue and submit for approval when ready. This app requires a small amount of setup to make it your own.

![Opening screen of the Expense Report PowerApp.](./media/expense-report-install/expense-report-powerapp.png)

## Where can I run the app?

You can run this sample app in your browser, on a tablet, or other device that has a similar form factor.

## How do I use the sample app and run?

Expense Report sample app is available in [Power Apps](https://make.powerapps.com). Follow these steps to open the sample app and run the app.

1. Sign in to [Power Apps](https://make.powerapps.com).

1. On the left-pane, select **Create**.

1. On the right-side of the screen, scroll down to **Start from template** section.

1. Select **Expense Report** from the available sample app templates.

    ![Open Expense Report sample app.](./media/expense-report-install/use-expense-report-sample-template.png "Open Expense Report sample app")

1. Enter a name.

1. Select **Create**.

1. When prompted, select **Allow** to let the app use the connections.

1. Press **F5** on the keyboard, or use ![Preview button.](./media/expense-report-install/preview.png "Preview button") to play the app.

> [!NOTE]
> This sample app includes locally saved information using [collections](create-update-collection.md). To use the app for business purpose, customize the app to store information using [connectors](/connectors/connector-reference/connector-reference-powerapps-connectors).

## How do I build the app myself?

Expense Report sample app includes the functionality commonly used in Power Apps. You can extend the app functionality by using connectors and connect the app to a data source instead of the default [collections](create-update-collection.md) used by the sample app.

[Save](save-publish-app.md#save-changes-to-an-app) the app, and update the app to use data source such as [SharePoint](connections/connection-sharepoint-online.md), or [Microsoft Dataverse](connections/connection-common-data-service.md).

You can also enable the capability to send emails or approval routing using [Power Automate flow](using-logic-flows.md) or [Approvals connector](/connectors/approvals).

## Next steps

[Design the app inteface - add, configure controls](add-configure-controls.md)

### See also

[Canvas apps connectors for Power Apps](connections-list.md) <br>
[Formula reference](formula-reference.md) <br>
[Controls reference](reference-properties.md) <br>
[Share a canvas app](share-app.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
