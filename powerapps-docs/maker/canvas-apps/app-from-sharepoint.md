---
title: Create a canvas app with data from a list
description: Create a Power Apps canvas app to manage data in Microsoft Lists or SharePoint Online.
author: joshuapartlow
ms.topic: how-to
ms.custom: canvas
ms.collection: get-started
ms.reviewer: joshuapa
ms.date: 11/02/2026
ai-usage: ai-assisted
ms.subservice: canvas-maker
ms.author: joshuapa
search.audienceType: 
  - maker
contributors:
  - Steven-Jia
  - joshuapartlow
  - navjotm
  - emcoope-msft
reviewer: joshuapartlow
---

# Create a canvas app with data from a list

Transform your Microsoft Lists or SharePoint data into a powerful mobile and web app in minutes with no coding required. This article shows you how to create a fully functional canvas app that connects directly to your existing lists, giving you and your team an intuitive way to view, edit, and manage data on any device.

You can also [connect to on-premises SharePoint lists](connections/connection-sharepoint-online.md#create-a-sharepoint-connection) through a data gateway.

You can create an app by using a list in SharePoint or Lists in two ways:

- Sign in to Power Apps and then [create an app by connecting to a list in SharePoint from Power Apps](app-from-sharepoint.md#use-a-list-in-sharepoint-or-lists-to-create-an-app).
- [Create an app directly from a list in SharePoint or Lists](app-from-sharepoint.md#create-an-app-directly-from-a-list-in-sharepoint-or-lists).

When you create the app, Power Apps Studio opens with a generated app connected to your list. The layout depends on the template available in your environment. The responsive single-screen template combines browsing and record editing on one screen. The updated modern-controls template provides a responsive records screen with grid and list views, plus separate screens for creating and editing records. See [Work with the updated template](#work-with-the-updated-template).

> [!NOTE]
> When you create or view a list in SharePoint, you're automatically redirected to Microsoft Lists. The list is always available in both Microsoft Lists and SharePoint. Learn more in [What is a list in Microsoft 365?](https://support.microsoft.com/office/what-is-a-list-in-microsoft-365-93262a88-20ad-4edc-8410-b6909b2f59a5)

## Prerequisites

Use SharePoint and Power Apps with a [subscription](https://www.microsoft.com/licensing/terms/productoffering) to [Microsoft 365](https://www.microsoft.com/licensing/terms/productoffering/Microsoft365/all) and [Microsoft Power Platform](https://www.microsoft.com/licensing/terms/productoffering/MicrosoftPowerPlatform/all).

## Create a list

Before you create an app from a list, [create a list](https://support.microsoft.com/office/create-a-list-0d397414-d95f-41eb-addd-5e6eff41b083).

For this example, create a list to track device orders for your company. Include the following columns with sample data:

1. Employee name
1. Device type
1. Request date
1. Reason for the order
1. Approved or denied
1. Status

    :::image type="content" source="media/app-from-sharepoint/sample-list.png" alt-text="Screenshot of a sample list in Microsoft Lists that tracks device orders." lightbox="media/app-from-sharepoint/sample-list.png":::

## Use a list in SharePoint or Lists to create an app

Now, use the list that you created to build an app from the list.

1. Sign in to [Power Apps](https://make.powerapps.com/).

1. From the home screen, select **Start with data**.

1. On the **Create an app** page, select **SharePoint**.

1. Enter the SharePoint URL, and then select **Connect**. Or, select a recent site.

1. Select a list or select the [sample list](app-from-sharepoint.md#create-a-list) you created earlier, and then select **Create app**.

   The app opens in Power Apps Studio, where you design, build, and manage the app. For more information, see [Understand Power Apps Studio](power-apps-studio.md).

1. Select the **Preview the app** icon to see how the app works.

1. [Save and publish](save-publish-app.md) your app.

    When you add or edit information in the app, the information in SharePoint or Lists also updates.

## Create an app directly from a list in SharePoint or Lists

Before you create the app, ensure you [create a list](app-from-sharepoint.md#create-a-list).

1. Sign in to SharePoint: `https://<yourorganizationname>.sharepoint.com`

1. Open a list in either SharePoint or Lists. If you open the list from SharePoint, you're taken to Lists to view the list.

1. Select **Integrate** > **Power Apps** > **Create an app**.

    :::image type="content" source="./media/app-from-sharepoint/generate-new-app.png" alt-text="Screenshot of the Integrate menu in Lists, showing the option to create an app in Power Apps.":::

1. Select the **Preview the app** icon to see how the app works.

1. [Save and publish](save-publish-app.md) your app.

    When you add or edit information in the app, the information in SharePoint or Lists also updates.

## Work with the updated template

The updated template uses responsive containers, a [modern Data Grid](controls/modern-controls/modern-control-data-grid.md), and [modern forms](controls/modern-controls/modern-control-form.md). It isn't the same as a customized list form hosted inside SharePoint. For that experience, see [Understand SharePoint forms integration](sharepoint-form-integration.md).

### Browse and select records

Use the view switch on the records screen to choose a grid or a list:

| View | Use |
| --- | --- |
| Grid | Review records in columns and select rows. The edit action appears when you select exactly one row. |
| List | Review a compact list and open an item to view its details. |

The template generates filter tabs from the connected data where applicable. Grid view filters a generated collection, while list view filters the connected data source. Check the same filter in both views after you connect your list. Generated counts and collection-backed results don't guarantee that every record in a large list is loaded. Review [delegation limits](delegation-overview.md) and [SharePoint data types and delegable operations](connections/connection-sharepoint-online.md#power-apps-delegable-functions-and-operations-for-sharepoint).

### Create or edit a record

Use the new-record action to open the form screen for a new item. Use a list item or the grid's edit action to open an existing record.

The new-record form uses one column below an app width of `768` and two columns at widths of `768` or greater. Its save action calls `SubmitForm` on the generated form. The form's **OnSuccess** action resets the form, shows a success notification, and returns to the previous screen. Its **OnFailure** action shows an error notification.

When you customize these screens, preserve the generated **DataSource**, **Item**, navigation formulas, and form success and failure actions unless you intentionally replace their behavior. The generated control and screen names can vary, so use the names in your app rather than names from an older tutorial.

### Check the connected app

Before sharing the generated app:

1. Preview both grid and list views at narrow and wide widths.
2. Apply a filter and check that both views show the expected records.
3. Create a test record, save it, and confirm the values in the source list.
4. Open that record, edit it, and confirm the changes in the source list.
5. Test required fields and a failed save. Don't treat a notification alone as proof that a data operation succeeded.

## Manage your app

After you create an app, you can play, save, share, and publish it.

Learn more about these [app actions](power-apps-studio.md#2--app-actions) in the Power Apps Studio interface.

## Related information

[Move SharePoint Custom Forms with Power Apps (white paper)](https://go.microsoft.com/fwlink/?linkid=2263521)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
