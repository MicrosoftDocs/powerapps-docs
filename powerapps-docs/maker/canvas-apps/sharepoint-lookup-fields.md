---
title: Link lists using a lookup column in Power Apps
description: Learn about linking lists and using lookup columns in Microsoft Power Apps.
author: emcoope-msft

ms.topic: how-to
ms.custom: canvas
ms.reviewer: 
ms.date: 3/1/2025
ms.subservice: canvas-maker
ms.author: emcoope
search.audienceType: 
  - maker
contributors:
  - mduelae
  - navjotm
  - wimcoor
---

# Link lists using a lookup column in Power Apps

This tutorial shows you how to connect two lists with a lookup column in a canvas app in Power Apps.

SharePoint provides two types of lookup columns:

- **Lookup**: Links to another list. For example, an **Orders** list might have a lookup column that links to customers in a **Customer** list.
- **Choice**: Selecting a column displays a menu of items you can choose.

> [!NOTE]
> When you create or view a list in SharePoint, you're automatically redirected to Microsoft Lists. The list can always be found in both Microsoft Lists and SharePoint. Learn more in [What is a list in Microsoft 365?](https://support.microsoft.com/en-us/office/what-is-a-list-in-microsoft-365-93262a88-20ad-4edc-8410-b6909b2f59a5)

## Prerequisites

- A [SharePoint license](https://www.microsoft.com/en-us/microsoft-365/sharepoint/compare-sharepoint-plans?msockid=142399bb7d966f5511fe8cc47c2c6ec1) or a [Microsoft 365 license](https://www.microsoft.com/en-us/microsoft-365/business/compare-all-microsoft-365-business-products?msockid=142399bb7d966f5511fe8cc47c2c6ec1)
- A SharePoint site

  To create a SharePoint site, see [Guided walkthrough: Creating an organization site](/sharepoint/guided-walkthrough-creating-organization-site).

## Why use a lookup column?

Data in an enterprise is large and complex. Data in one list often relates to data in another list. Lookup columns are the primary way such business data comes together.

For example, you might have an **Orders** list which has a lookup column that links to a **Customers** list, to show which customer placed the order. The lookup column in the **Orders** list lets you get other data from the **Customers** list as well.

You might also use a lookup column to connect the **Orders** list to a **Product** list, and bring in information you need about the product ordered, such as product pictures, specifications, or manufacturer details.

## What are choice columns used for?

**Choice** columns are used for short lists. Instead of  creating a separate list, you include the list values in a small menu. This menu appears when you select a **Choice** column, and then you can select one of the values from the menu.

Examples include data like Customer Status Code, Product Availability, State Codes—any fixed, relatively short list.

The choice data can stay as a separate list, if you use a **Lookup** column to link them. However, a **Choice** column implementation is easier and quicker than a **Lookup** column implementation.

Learn more in [Integrate SharePoint Online into Power Apps overview](sharepoint-list-integration-overview.md).

## Create the lists

In this tutorial, you link two lists together, **Assets** and **RepairShop**. The **Assets** list is used to track hardware equipment in a team. Since hardware breaks from time to time, we use the **RepairShop** list to track the local shops which can fix it.

### The lookup column used in this example

The **RepairShop** list uses the *ContactEmail* column to identify the shop. This list is defined first so that each row in the **Assets** list points to something.

The **Assets** list has two lookup columns:

- *RepairShop*, of type **Lookup**, uses email addresses to point to entries in the **RepairShop** list.
- *AssetType*, of type **Choice**, lists the asset types for hardware.

You can define more columns, depending on the information you need to track.

### Define the RepairShop list and add data

Create this list first, so when you add data to the **Assets** list, **RepairShop** entries are available from the *Assets.RepairShop* lookup column.

1. On any SharePoint site, create a new **RepairShop** list from a **Blank list** template.

    :::image type="content" source="./media/sharepoint-lookup-fields/new-list.png" alt-text="Screenshot of the location of a List option in the New menu of a SharePoint site.":::
1. Select **Add a column** of type **Text** and name it *ContactEmail*, then choose **Save**.
1. Select **+ Add new item** to enter at least three rows with different *ContactEmail* sample values. When an asset needs to be repaired, you choose one of these repair shops.

    :::image type="content" source="./media/sharepoint-lookup-fields/add-repair-shops.png" alt-text="Screenshot of the location of the Add new item button on a SharePoint site page.":::

### Define the Assets list

1. On the same SharePoint site, create a new **Assets** list from a **Blank list** template.
1. Select **+ Add column** and choose the **Choice** column type. Select **Next** and name it *AssetType*. Fill in the *Choice* values under the **Choices** section with sample assets such as *Desktop*, *Laptop*, *Android phone*, *iPhone*, and *Windows tablet*.

    :::image type="content" source="./media/sharepoint-lookup-fields/define-choice-column.png" alt-text="Screenshot showing where you can define the column choices when you create a column.":::
1. Select **Save**.
1. Select **+ Add column** and choose the **Lookup** column type, then select **Next**.
1. In the **Create a column** pane, add RepairShop to the **Name** field. Go to **Select a list as a source** and choose **RepairShop**. Go to **Select a column from the list above** and choose **ContactEmail**.
1. Select **Save**.

   You see the column *RepairShop* has a two-arrows icon that indicates it's a lookup type column.

   :::image type="content" source="./media/sharepoint-lookup-fields/repair-shop-lookup-column.png" alt-text="Screenshot showing the RepairShop column in the Assets list.":::

## Create an app from the Assets list

Create a [canvas app](app-from-sharepoint.md) from the [Assets list](#define-the-assets-list) created earlier.

## Add data to the Assets list

Let's [preview the app](preview-app.md) and add items to your **Assets** list.

1. Press F5 or select Preview ( ![Preview icon.](./media/sharepoint-lookup-fields/preview.png) ).

2. Select the **+** symbol in the upper right corner of your app to add an entry.

3. Enter a **Title** for this asset, for example *Micah's Laptop*.

4. Select the **AssetType** dropdown arrow. The values displayed are values you entered when you created this column. Choose one of the entries.

   :::image type="content" source="./media/sharepoint-lookup-fields/fill-asset-type-3.png" alt-text="Screenshot that shows the AssetType list when you select the dropdown arrow.":::

5. Select the **RepairShop** dropdown arrow. Choose one of the entries.

   :::image type="content" source="./media/sharepoint-lookup-fields/fill-repair-shop-3.png" alt-text="Scrrenshot that shows the RepairShop list when you select the dropdown arrow.":::

6. Select the check mark to save the new entry.

7. (Optional) Add more items to the list.

8. Press `Esc` to return to the default workspace.

9. [Save and publish](save-publish-app.md) the app.

## Related information

- Configure [Drop down control in Power Apps](controls/control-drop-down.md) in your list.
- [Generate an app by using a Microsoft Dataverse database](data-platform-create-app.md)
- [Create an app from scratch using a Dataverse database](data-platform-create-app-scratch.md)
- [Move SharePoint Custom Forms with Power Apps (white paper)](https://go.microsoft.com/fwlink/?linkid=2263521)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
