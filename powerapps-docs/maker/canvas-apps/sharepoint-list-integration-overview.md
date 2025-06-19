---
title: Integrate SharePoint Online into Power Apps overview
description: An overview of how to integrate lists from SharePoint Online or Microsoft Lists into Microsoft Power Apps.
author: NickWaggoner

ms.topic: concept-article
ms.reviewer: mkaur
ms.date: 3/1/2025
ms.subservice: canvas-maker
ms.author: mkaur
search.audienceType: 
  - maker
contributors:
  - mduelae
  - navjotm
  - wimcoor
ms.custom: canvas
ms.collection: get-started
---

# Integrate SharePoint Online into Power Apps overview

This article guides you through creating a list from SharePoint or Microsoft Lists, integrating that list into Power Apps, and customizing the list in your app.

When you add data to an app, you can choose a SharePoint list or Microsoft Lists as a source. Alternatively, you can create an app based on a SharePoint list through the integrate menu in Microsoft Lists. Once your list is in your app, you can filter it and customize the list.

> [!NOTE]
> When you create or view a list in SharePoint, you're automatically redirected to Microsoft Lists. The list can always be found in both Microsoft Lists and SharePoint. Learn more in [What is a list in Microsoft 365?](https://support.microsoft.com/en-us/office/what-is-a-list-in-microsoft-365-93262a88-20ad-4edc-8410-b6909b2f59a5)

## Prerequisites

- A [subscription](https://www.microsoft.com/licensing/terms/productoffering) to [Microsoft 365](https://www.microsoft.com/licensing/terms/productoffering/Microsoft365/all) and [Microsoft Power Platform](https://www.microsoft.com/licensing/terms/productoffering/MicrosoftPowerPlatform/all).

- A basic familiarity with SharePoint Online and Power Apps:

  - [Get started with SharePoint](https://support.microsoft.com/en-us/office/get-started-with-sharepoint-909ec2f0-05c8-4e92-8ad3-3f8b0b6cf261)
  - [What is Power Apps?](../../powerapps-overview.md)

## Create a list

You can create a new SharePoint list through the Microsoft Lists app in [Create a list](https://support.microsoft.com/en-us/office/create-a-list-0d397414-d95f-41eb-addd-5e6eff41b083).

## Integrate a list

Once you have a list, you can integrate it into Power Apps or create an app based on a Sharepoint list or Microsoft Lists.

### Connect with a list in Power Apps

One way to work with a list in your app is to connect to SharePoint through the **Data** menu of an app to import a list. The list serves as a data source in Power Apps.

:::image type="content" source="media/sharepoint-integration/connect-to-sharepoint-through-data.png" alt-text="Screenshot showing where you can connect to a SharePoint list through the Data, Add data, and Connectors menu.":::

Learn more in [Connect to SharePoint from a canvas app](connections/connection-sharepoint-online.md).

### Create an app based on a list

When viewing a SharePoint list, you automatically go to Microsoft Lists where you can integrate a list with Power Apps:

:::image type="content" source="media/sharepoint-integration/microsoft-lists-integrate-menu.png" alt-text="Screenshot that shows location of the integrate option of the top bar in Microsoft Lists. You can choose this menu to customize the form for a list in an app or create a new app based on the list." lightbox="media/sharepoint-integration/microsoft-lists-integrate-menu.png":::

Learn more in [Create a canvas app with data from Microsoft Lists](app-from-sharepoint.md).

## Customize a list or form

When you import a list into Power Apps as a data source, it might be used to display as a form on a screen. You can customize what your list looks like in your app such as the formatting and behavior for the list.

Customization includes how the list displays the:

- Addition or removal of fields
- Control type and data type for the fields
- Layout orientation and how many columns should show
- Formatting like alignment, color, and borders
- Interactive features such as **OnFailure** or **OnSuccess**

Learn how to customize a list in [Customize a form for a SharePoint list](/sharepoint/dev/business-apps/power-apps/get-started/create-your-first-custom-form).

Learn more about form properties in [Understand SharePoint forms integration](sharepoint-form-integration.md).

## Filter a list in Power Apps

You can apply formulas to interface elements of your app such as filters. For a list, you can add a filter formula to a [vertical gallery](add-gallery.md) in your app screen by adding the formula to the formula bar of an *Items* property.

Learn more in [Filter, Search, and LookUp functions](/power-platform/power-fx/reference/function-filter-lookup).

### Example of a search and filter function

This example formula is put on a gallery for the *Items* property. The formula searches for the status in a column and filters for the *Active* status. The list then only shows the list items with an *Active* status.

```powerfx
SortByColumns(Filter('Issue Tracking', 'Issue Status'.Value = "Active", StartsWith(Title, TextSearchBox1.Text)), "Title", If(SortDescending1, Descending, Ascending))
```

The formula contains the following functions:

- [SortByColumns](/power-platform/power-fx/reference/function-sort) sorts a table based on one or more columns.
- [Filter](/power-platform/power-fx/reference/function-filter-lookup) finds the records in a table according to a formula that you specify.
- [StartsWith](/power-platform/power-fx/reference/function-startswith) tests whether one text string begins with another text string.
- [If](/power-platform/power-fx/reference/function-if) returns a value depending on whether a condition is true or false.

Learn more in [Formula reference - canvas apps](/power-platform/power-fx/formula-reference-canvas-apps).

### Linking lists with a lookup column

You can link two lists where one list uses one of its columns as a *lookup* column. A lookup column is the point where the list connects to another list.

Learn more in [How to link lists from Microsoft Lists using a lookup column in Power Apps](sharepoint-lookup-fields.md).

If you want your lookup column to be a dropdown list with options, use the [Choices](/power-platform/power-fx/reference/function-choices) function. The choices function returns a table of the possible values for a lookup column.

For example, you can add a choices function to a [dropdown control](controls/control-drop-down.md) in your canvas app by adding this formula to your *Items* property of the control. You include your list name and the name of the lookup column in the formula.

```powerappsfl
Choices([@'Your list name'].Lookup_x0020_column)
```

## Related information

- [Using the SharePoint connector with canvas apps](/power-platform/guidance/architecture/real-world-examples/sharepoint-canvas)
- [Customize permissions for a SharePoint list or library](https://support.microsoft.com/office/customize-permissions-for-a-sharepoint-list-or-library-02d770f3-59eb-4910-a608-5f84cc297782)
- [Move SharePoint Custom Forms with Power Apps (white paper)](https://go.microsoft.com/fwlink/?linkid=2263521)
- [Create a report quickly from a SharePoint list or library](/power-bi/create-reports/service-quick-create-sharepoint-list)
- [Embed a report web part in SharePoint Online](/power-bi/collaborate-share/service-embed-report-spo)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
