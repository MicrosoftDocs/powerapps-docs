---
title: Integrate SharePoint Online into Power Apps overview
description: Integrate SharePoint Online lists into Microsoft Power Apps.
author: NickWaggoner

ms.topic: conceptual
ms.reviewer: mkaur
ms.date: 06/18/2020
ms.subservice: canvas-maker
ms.author: niwaggon
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

This article guides you through creating a SharePoint list, integrating that list into Power Apps, and customizing the list in your app.

When you add data to a Power Apps app, you can choose a SharePoint list as a source. Alternatively, you can create an app based on a SharePoint list through the integrate feature in Microsoft Lists. Once your list is in your app, you can filter it, set permissions, and customize the list.

## Prerequisites

- A [subscription](https://www.microsoft.com/licensing/terms/productoffering) to [Microsoft 365](https://www.microsoft.com/licensing/terms/productoffering/Microsoft365/all) and [Microsoft Power Platform](https://www.microsoft.com/licensing/terms/productoffering/MicrosoftPowerPlatform/all).

- Have a basic familiarity with SharePoint Online and Power Apps:

  - [Get started with SharePoint](https://support.microsoft.com/en-us/office/get-started-with-sharepoint-909ec2f0-05c8-4e92-8ad3-3f8b0b6cf261)
  - [What is Power Apps?](../../powerapps-overview.md)

## Create a SharePoint list

You can create a new SharePoint list through the Microsoft Lists app in [Create a list](https://support.microsoft.com/en-us/office/create-a-list-0d397414-d95f-41eb-addd-5e6eff41b083).

## Integrate a SharePoint list

### Connect with a SharePoint list in Power Apps

One way to work with a SharePoint list in your app is to connect to SharePoint through the **Data** menu of a Power Apps app to import a list. The list serves as a data source.

:::image type="content" source="media/sharepoint-integration/connect-to-sharepoint-through-data.png" alt-text="Screenshot showing where you can connect to a SharePoint list through the Data, Add data, and Connectors menu.":::

Learn more in [Connect to SharePoint from a canvas app](connections/connection-sharepoint-online.md).

### Create an app based on a SharePoint list

When viewing a SharePoint list in SharePoint Online, you automatically go to Microsoft Lists where you can integrate a list with Power Apps:

:::image type="content" source="media/sharepoint-integration/microsoft-lists-integrate-menu.png" alt-text="Screenshot that shows location of the integrate option of the top bar in Microsoft Lists. You can choose this menu to customize the form for a list in a Power Apps app or create a new app based on the list." lightbox="media/sharepoint-integration/microsoft-lists-integrate-menu.png":::

Learn more in [Create a canvas app with data from Microsoft Lists](app-from-sharepoint.md).

## Customize a SharePoint list form

When you import a list into Power Apps as a data source, it might be used to display as a form on a screen. You can customize what your SharePoint list looks like in your app such as the formatting and behavior for the list.

Customization includes how the list displays the:

- Addition or removal of fields
- Control type and data type for the fields
- Layout orientation and how many columns should show
- Formatting like alignment, color, and borders
- Interactive features such as **OnFailure** or **OnSuccess**

Learn how to customize a list in [Customize a form for a SharePoint list](/sharepoint/dev/business-apps/power-apps/get-started/create-your-first-custom-form).

Learn more about form properties in [Understand SharePoint forms integration](sharepoint-form-integration.md).

## Filter a list in Power Apps

You can apply formulas to interface elements of your app such as filters. For a list, you can add a filter formula to a [vertical gallery](add-gallery.md) in your app screen by adding the formula to the formula bar of an *item* property.

Learn more in [Filter, Search, and LookUp functions](/power-platform/power-fx/reference/function-filter-lookup).

### Example of a search and filter function

This example formula is put on an items gallery for the *Items* property. The formula searches for the status in a column and filters for the *Active* status. The list then only shows the list items with an *Active* status.

```powerfx
SortByColumns(Filter('Issue Tracking', 'Issue Status'.Value = "Active", StartsWith(Title, TextSearchBox1.Text)), "Title", If(SortDescending1, Descending, Ascending))
```

The formula contains the following functions:

- [SortByColumns](/power-platform/power-fx/reference/function-sort) for sorting columns
- [Filter](/power-platform/power-fx/reference/function-filter-lookup) to filter items
- [StartsWith](/power-platform/power-fx/reference/function-startswith) to allow search based on entered text in the search box on the top
- [If](/power-platform/power-fx/reference/function-if) for sorting items based on the sort icon selection

## Related information

[Using the SharePoint connector with canvas apps](/power-platform/guidance/architecture/real-world-examples/sharepoint-canvas)

### Security

- [Customize permissions for a SharePoint list or library](https://support.microsoft.com/en-us/office/customize-permissions-for-a-sharepoint-list-or-library-02d770f3-59eb-4910-a608-5f84cc297782)
- [Control settings for Microsoft Lists](/sharepoint/control-lists)

### Controls for the display

- [Drop down control in Power Apps](controls/control-drop-down.md)
- [Controls and properties in canvas apps](reference-properties.md)

### List features

- [How to link lists from Microsoft Lists using a lookup column in Power Apps](sharepoint-lookup-fields.md)
- [Formula reference - canvas apps](/power-platform/power-fx/formula-reference-canvas-apps)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
