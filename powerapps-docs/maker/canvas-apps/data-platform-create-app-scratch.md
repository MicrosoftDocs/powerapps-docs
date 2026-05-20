---
title: Create a canvas app using Microsoft Dataverse
description: Learn how to create a canvas app that displays, adds, updates, and deletes records in Microsoft Dataverse.
author: mduelae

ms.topic: how-to
ms.custom: canvas
ms.reviewer: 
ms.date: 05/20/2026
ms.subservice: canvas-maker
ms.author: tapanm
search.audienceType: 
  - maker
contributors:
  - mduelae
  - lancedmicrosoft
---
# Create a canvas app using Microsoft Dataverse

Microsoft Dataverse is a secure, cloud-based data platform for business data. In Power Apps, you can create canvas apps that connect directly to Dataverse to display, add, update, and manage records without setting up a separate database.

This article shows three ways to build a canvas app with Dataverse:

- Start with an existing Dataverse table.
- Create new Dataverse tables and generate an app.
- Build a blank app and connect it to Dataverse yourself.

## Prerequisites

Before you start:

- [Switch to an environment](intro-maker-portal.md#choose-an-environment) that already has a database with sample data. If you have the right license, you can also [create an environment](/power-platform/admin/create-environment).
- Make sure that you have the [Environment Maker](/power-platform/admin/database-security#predefined-security-roles) security role, either directly or through a Dataverse team that uses the **Microsoft Entra ID security group** category. Custom security roles aren't currently supported for canvas app maker scenarios.

## Create an app

1. Sign in to [Power Apps](https://make.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).
1. On the home page, choose one of the following options based on how you want to build your app with Dataverse.

   | Create options using Dataverse | Benefits | Navigation |
   |---|---|---|
   | A single-page gallery app | Use existing business data in Dataverse to create a lightweight responsive app quickly. | Select **Start with data** > **Dataverse**. Select a table, and then select **Create app**. |
   | Create new data and build an app | Create structured tables in Dataverse so you can build secure and scalable apps around new business data. | Select **Start with data** > **Create new data**. Use the table designer or Copilot to create tables, and then select **Save and exit**. |
   | Blank app that uses data from Dataverse | Start with a blank app when you want full control over the layout, screens, and controls. | In the left navigation pane, select **Create** > **Create from blank** > **Phone size**. |


1. Power Apps creates the app and opens [Power Apps Studio](power-apps-studio.md), where you can continue building.

## Start with data using Dataverse

The **Start with data** experience helps you quickly connect to an existing Dataverse table or create a new table and generate an app.

### Connect to an existing Dataverse table

1. Sign in to [Power Apps](https://make.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).
1. On the home page, select **Start with data**.
1. On the **Create an app** page, select **Dataverse**.
1. Select an existing Dataverse table, and then select **Create app**.

Power Apps Studio opens with a gallery app that is already connected to the selected table.

### Create new data

If you don't already have a table, create one directly from the **Start with data** experience.

1. On the home page, select **Start with data**.
1. Select **Create new data**.
1. In the **Create new tables** designer, choose one or more of these actions:
   - Select **+ New table** to create a table.
   - Select **+ Existing table** to add an existing table.
   - Use **Copilot** to describe the tables, columns, rows, and relationships that you need.
   - Select **Import data** in the Copilot pane to import data from Excel, .CSV files, or SharePoint lists.
1. When you finish defining your tables, select **Save and exit** to generate the app.

## Add a Dataverse table in a blank app

If you want to understand the building blocks of a Dataverse app, start with a blank app and add the data source yourself.

1. Sign in to [Power Apps](https://make.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).
1. In the left navigation pane, select **Create** > **Create from blank**.
1. Select an app size.
1. When Power Apps Studio opens, go to the [app authoring menu](power-apps-studio.md#5--app-authoring-menu) and select **Data**.

   > [!NOTE]
   > If this is your first time connecting to Dataverse, Power Apps prompts you to create a connection. Select **Create** to continue.

1. Select **Add data**, enter **Accounts** in the search box, and then select it. And close the **Data** pane by selecting the close icon in the upper-right corner.

   :::image type="content" source="./media/data-platform-create-app-scratch/add-and-close-data.png" alt-text="Screenshot of the close data pane." lightbox="./media/data-platform-create-app-scratch/add-and-close-data.png":::

### Add a list screen

1. On the command bar, select **New screen** > **List**.
1. In the left navigation bar, select **BrowseGallery1**, and then set the **Items** property to this formula:

   `SortByColumns(Search(CustomGallerySample, TextSearchBox1.Text, SampleText), "SampleText", If(SortDescending1, SortOrder.Descending, SortOrder.Ascending))`

   This formula does the following:

    This expression filters the CustomGallerySample table for records whose SampleText column contains the text entered in TextSearchBox1. It then sorts the filtered results by the SampleText column in descending order when SortDescending1 is true; otherwise, it sorts them in ascending order.

   You can use [these and many other functions](formula-reference.md) to control how your app looks and behaves.

   :::image type="content" source="./media/data-platform-create-app-scratch/gallery-items.png" alt-text="Screenshot that shows the gallery's Items property set to the SortByColumns and Search formula." lightbox="./media/data-platform-create-app-scratch/gallery-items.png":::

1. In the gallery's **Properties** pane, set **Layout** to **Title**.
1. Edit the **Title** text property and rename it to **Browse**. For more information, see [Customize a gallery](customize-layout-sharepoint.md).

   :::image type="content" source="./media/data-platform-create-app-scratch/rename-browse.png" alt-text="Screenshot of the Browse screen showing a list of accounts." lightbox="./media/data-platform-create-app-scratch/rename-browse.png":::

1. In the left app authoring pane, hover over **Screen1**, select the ellipsis icon (...), and then select **Delete**.
1. In the left app authoring pane, hover over **Screen2**, select the ellipsis icon (...), and then select **Rename**.
1. Type or paste **BrowseScreen**, and then rename the gallery in that screen to **BrowseGallery**.

   :::image type="content" source="./media/data-platform-create-app-scratch/rename-screens.png" alt-text="Screenshot of the renamed BrowseScreen and BrowseGallery in the tree view." lightbox="./media/data-platform-create-app-scratch/rename-screens.png":::

### Add a form screen

1. Repeat the first step in the previous procedure, but add a **Form** screen instead of a **List** screen.
1. Set the form's **DataSource** property to **Accounts** and its **Item** property to **BrowseGallery.Selected**, as shown on the **Advanced** tab of the right-hand pane.
1. On the **Properties** tab of the right-hand pane, in the **Fields** row select the **"N selected"** link (or the **Edit** pencil) to open the **Fields** pane.
1. Select **Add field**, choose these fields, and then select **Add**:

   - **Account Name**
   - **Address 1: Street 1**
   - **Address 1: City**
   - **Address 1: ZIP/Postal code**
   - **Number of Employees**
   - **Annual Revenue**

   > [!NOTE]
   > Outside of this scenario, you can create a custom field by selecting **New field**, entering the required information, and then selecting **Done**. For more information, see [Create a column](../data-platform/create-edit-field-portal.md#create-a-column).

   :::image type="content" source="./media/data-platform-create-app-scratch/choose-or-add-fields.png" alt-text="Screenshot of the Choose a field pane with the New field option highlighted." lightbox="./media/data-platform-create-app-scratch/choose-or-add-fields.png":::

1. Set the title bar's **Text** property to show **Create/Edit**.

   The screen reflects your changes.

   :::image type="content" source="./media/data-platform-create-app-scratch/field-list.png" alt-text="Screenshot of the Create/Edit form screen showing the configured fields." lightbox="./media/data-platform-create-app-scratch/field-list.png":::

1. Rename this screen **FormScreen**.

### Configure icons

1. On **BrowseScreen**, set the **OnSelect** property of the circular icon near the top of the screen to this formula:

   `Refresh(Accounts)`

   :::image type="content" source="./media/data-platform-create-app-scratch/refresh-icon.png" alt-text="Screenshot of the refresh icon." lightbox="./media/data-platform-create-app-scratch/refresh-icon.png":::

1. Set the **OnSelect** property of the plus icon to this formula:

   `NewForm(EditForm1); Navigate(FormScreen, ScreenTransition.None)`

   :::image type="content" source="./media/data-platform-create-app-scratch/plus-icon.png" alt-text="Screenshot of the plus add icon." lightbox="./media/data-platform-create-app-scratch/plus-icon.png":::

1. Set the **OnSelect** property of the first arrow that points to the right to this formula:

   `EditForm(EditForm1); Navigate(FormScreen, ScreenTransition.None)`

   :::image type="content" source="./media/data-platform-create-app-scratch/next-icon.png" alt-text="Screenshot of the next arrow icon." lightbox="./media/data-platform-create-app-scratch/next-icon.png":::

1. On **FormScreen**, set the **OnSelect** property of the cancel icon to this formula:

   `ResetForm(EditForm1);Navigate(BrowseScreen, ScreenTransition.None)`

   :::image type="content" source="./media/data-platform-create-app-scratch/cancel-icon.png" alt-text="Screenshot of the cancel icon." lightbox="./media/data-platform-create-app-scratch/cancel-icon.png":::

1. Set the **OnSelect** property of the checkmark icon to this formula:

   `SubmitForm(EditForm1); Navigate(BrowseScreen, ScreenTransition.None)`

   :::image type="content" source="./media/data-platform-create-app-scratch/checkmark-icon.png" alt-text="Screenshot of the checkmark icon." lightbox="./media/data-platform-create-app-scratch/checkmark-icon.png":::

1. On the **Insert** tab, select **Icons**, and then select the **Trash** icon.
1. Set the **Trash** icon's **Color** property to **White** and its **OnSelect** property to this formula:

   `Remove(Accounts, BrowseGallery.Selected); Navigate(BrowseScreen, ScreenTransition.None)`

   :::image type="content" source="./media/data-platform-create-app-scratch/trash-icon.png" alt-text="Screenshot of the trash delete icon." lightbox="./media/data-platform-create-app-scratch/trash-icon.png":::

### Test the app

1. On the actions menu, select the play button to **Preview the app**. For more information, see [Preview an app](preview-app.md).
1. Toggle the list between ascending and descending sort orders. Filter the list by one or more characters in the account name.
1. Add an account, edit the account that you added, start to update the account, cancel the changes, and then delete the account.

## See also

- [Overview of the new Power Apps vibe experience (preview)](../../vibe/overview.md)
- [Customize a gallery](customize-layout-sharepoint.md)
- [Create a column](../data-platform/create-edit-field-portal.md#create-a-column)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
