---
title: Create your first app in Teams | Microsoft Docs
description: Learn how to create your first app in Teams. 
author: mduelae

ms.topic: how-to
ms.collection: get-started
ms.date: 01/13/2026
ms.subservice: teams
ms.author: saperlmu
ms.reviewer: mkaur-msft
contributors:
  - mduelae
  - wimcoor
  - msftsamperl
---

# Create your first app in Microsoft Teams

You can create, edit, and delete [canvas apps](../maker/canvas-apps/getting-started.md) in Teams. If you're creating an app by using Power Apps in a Teams team for the first time, you also create a new Dataverse for Teams environment. For more information, see [About the Dataverse for Teams environment](/power-platform/admin/about-teams-environment).

Creating an app in Microsoft Teams is a quick and easy three-step process.

1. [Create your app](#create-your-app)
1. [Create your first table](#create-your-first-table)
1. [Customize and publish your app](#customize-and-publish-your-app)

![Create your first app in 3 steps.](media/create-your-first-app.png "Create your first app in 3 steps")

Watch this video to learn how to create your first app.
> [!VIDEO https://learn-video.azurefd.net/vod/player?id=3e63d41c-d4eb-411e-b99a-7cc87bb2992d]
Ensure you refer to the [latest steps](#create-your-first-table) when creating the table.

Now let's go through each step in detail.

## Create your app

After installing the Power Apps app template:

1. Start Teams, and sign in.

1. In the left pane, select **Power Apps**, and then select **Start now**.

    ![Start creating an app.](media/create-app-1.png "Start creating an app")

    > [!TIP]
    > If you don't see the **Power Apps** app in the left pane, select ![More added apps - ellipsis.](media/more-added-apps-ellipsis.png "More added apps - ellipsis") (*More added apps*), and then select **Power Apps**.

    ![Power Apps.](media/power-apps.png "Power Apps")

1. Select a team where you want to create the app. This is where the app lives. Team members can't see the app until you publish the app. You can also share the app with colleagues within your company that are not part of the team. For more information, see [Set permission and share apps with colleagues](set-perms-and-share.md).

    ![Select a team to create the app.](media/select-a-team-for-this-app.png "Select a team to create the app")

    If this is the first app you're creating in the selected team, a new Dataverse for Teams environment is created for the selected team. You see a message about this when you select the team. For more information, see [About the Dataverse for Teams environment](/power-platform/admin/about-teams-environment).

    ![Creating the first app in a team.](media/select-a-team-for-this-app-environment.png "Creating the first app in a team")

1. Select **Create**. You see a confirmation about the Dataverse for Teams environment being created, which might take some time. You're notified when the environment is available for you to create your first app by using an email and a Teams notification.

    ![First app in a team.](media/create-app-4.png "First app in a team")

    > [!NOTE]
    > Environment creation fails if the Teams team that you selected has *Hiddenmembership* enabled. If this happens, try creating the app in a different team. For more information, see [Hidden membership groups](known-issues-limitations.md#hidden-membership-groups).

1. Enter an app name, and then select **Save**.

    ![Name your app.](media/name-your-app.png "Name your app")

    > [!TIP]
    > An app template is included with the app by default, so that you can get started with creating your table and using the app. For more information, see [Understand Power Apps Studio](understand-power-apps-studio.md).

## Create your first table

Data for apps built in Teams lives in Dataverse for Teams environments as tables. Like other data experiences, you can add extra columns to track different attributes of each record before filling the table with multiple rows of data.

> [!TIP]
> For more information about Dataverse for Teams tables, see [Overview of Dataverse for Teams](overview-data-platform.md).

To create your first table:

1. Select **With data**.

    ![Select With data](media/start-with-data.png "Select With data")

1. Select **Create new table** > **Start with blank table**.

    ![Create your first table.](media/create-first-table.png "Create your first table")

1. In the **Create a table** dialog box, select **Edit table properties** and type a meaningful name for your
new table that describes this dataset, and then select
**Save**.

1. After the table is created, add columns of different types, add rows, and
work with data in the visual editor.

   ![Visual editor.](media/table-designer-1.png "Visual editor")

### Add columns to the table

To add a new column to track new data:

1. Select **New column.**  

1. Enter a name that best describes your new column.

1. Select the type for your column.

    > [!TIP]
    > For more information about column types supported by the visual editor, go to [Supported column types](understand-power-apps-studio.md#supported-column-types). To add columns that aren't supported by
    the visual editor, create a table by using the solution explorer. More information: [Create tables](create-table.md)

1. If required, change **Advanced options** for the selected column type.

1. Select **Save**.

1. Repeat the previous steps to add the rest of the data columns.

### Add rows to the table

Select **Add row** to add rows.


#### Paste the copied data into the table

You can paste up to **50 rows** of data into a table. To create new rows from the copied data, add empty rows in the table first. Adding new empty rows ensures pasting data from clipboard doesn't accidentally overwrite your existing data.

> [!CAUTION]
> Paste operations are automatically saved, and there's no undo option. Use caution when pasting data over existing rows since this action overwrites your existing data in the table.

To paste the data from clipboard into the table:

1. Select the record that you want to add new records above or below.

1. Select **Insert row above**, or **Insert row below** to insert rows before or after existing rows.
    <br> For example, inserting row above the selected row:

    ![Insert row above.](media/insert-row.png "Insert row above")

1. Repeat the preceding step to add more empty rows, as needed.

    > [!TIP]
    > If you're unsure of how many rows you need, create additional empty rows before pasting data. You can delete extra empty rows later.

1. Select the top-left cell from the newly created rows.

    ![Select top-left cell.](media/select-top-left-cell.png "Select top-left cell")

1. Paste the copied data.

    ![Paste rows.](media/paste-rows.png "Paste rows")

    > [!NOTE]
    > If you paste data when the cell is in edit mode (if you *double-clicked* top-left cell), the data is pasted inside the cell. If this problem happens, delete the incorrectly pasted data, select any other cell, select the top-left cell, and try to paste again.

    ![Incorrect pasting of rows.](media/paste-inside-edit-cell.png "Incorrect pasting of rows")

1. Remove any extra empty rows.

    ![Delete extra row.](media/delete-extra-row.png "Delete extra row")

    > [!TIP]
    > To delete multiple rows that are together, select the top row, and press the **Shift** key on the keyboard. Keep the key pressed, select the last row in the chunk of the rows that you want to delete. Then, select **Delete X record(s)**.

    ![Delete multiple rows.](media/delete-multiple-records.png "Delete multiple rows")

Changes to the table are automatically saved. However, check for errors, and fix them before you close the visual editor.

## Customize and publish your app

When you close the table, the app template that you added to the app screen by default automatically refreshes to use the new table.

> [!NOTE]
> To add new data sources, such as a new table, or to reopen the app, see [Manually connect data to the app](#manually-connect-data-to-the-app) for steps to manually refresh the app with the new data.

![Updated app template.](media/updated-gallery.png "Updated app template")

Depending on the number of fields you add to your table, you might need to update the form and the gallery in the app template.

### Manually connect data to the app

The gallery and the edit form components on the screen automatically refresh with the data only for the first data source. If you add extra data sources, such as a new table, or if you reopen the app, you need to manually connect the data to the template gallery and form.

> [!TIP]
> Skip these steps if the app screen is already connected to the table that you created.

To manually connect to the new data:

1. Select the gallery, and then select the correct data source.

    ![Change the gallery data source.](media/select-gallery-source.png "Change the gallery data source")

1. Select the form, and then select the correct data source.

    ![Change the form data source.](media/select-form-source.png "Change the form data source")

1. If you see any formula error, select **Edit in the formula bar**, and update the formula with the data source name.

    ![Edit the formula.](media/edit-formula.png "Edit the formula")

    For example, to change from using *Instructions* as the data source name for the edit form to *Recipes*, replace the name of the data source.

    Change from:

    ```power-fx
    Remove(Instructions, selectedRecord); If(IsEmpty(Errors(Instructions, selectedRecord)),UpdateContext( {itemSelected:false, editMode:false, newMode:false, deleteMode:false}); Set(CurrentItem,First(Instructions)););
    ```
    Change to:

    ```power-fx
    Remove(Recipes, selectedRecord); If(IsEmpty(Errors(Recipes, selectedRecord)),UpdateContext( {itemSelected:false, editMode:false, newMode:false, deleteMode:false}); Set(CurrentItem,First(Recipes)););
    ```

1. Repeat the earlier step to fix any extra formula errors.

### Update background color for the selected gallery record

The gallery shows records you created earlier. However, you need to change the background color for a record when you select it from the gallery to show the selection.

To update the selected item background color:

1. Select the gallery.

    ![Select the gallery for background fill.](media/select-gallery.png "Select the gallery for background fill")

1. Select *TemplateFill* property from the property drop-down on the top-left.

    ![Select TemplateFill property.](media/select-templatefill.png "Select TemplateFill property")

1. Update the *TemplateFill* property value in the formula bar to the following formula:

    ```power-fx
    If(ThisItem.IsSelected, RGBA(0,0,0,.05), RGBA(0,0,0,0))
    ```

### Update fields on the form

The template shows two fields inside the form by default. To add more fields to the form:

1. Select the form.

    ![Select the form.](media/app-form.png "Select the form")

1. Select **Edit fields** from the property pane on the right.

    ![Edit fields.](media/edit-form-fields.png "Edit fields")

1. Select **Add fields**.

    ![Add fields.](media/add-fields.png "Add fields")

1. Select the fields that you want to add on the form.

    ![Select fields to add.](media/add-fields-list.png "Select fields to add")

1. Select **Add**.

1. (Optional) Select fields to move up or down, or remove unwanted fields by selecting **Remove**.

    ![Move or remove fields.](media/move-remove-field.png "Move or remove fields")

1. Close the fields pane.

When you add, remove, or reorder fields, the form updates automatically.

![Updated form.](media/form-updated.png "Updated form")

### Update fields in the gallery

You might need to update the gallery on the default app template to reflect the fields from the table you created.

![Default gallery.](media/gallery-fields.png "Default gallery")

To update the fields in the gallery:

1. Select **Edit fields** from the property pane on the right.

1. Select the drop-down menu for a gallery component (such as image, title, or subtitle) and change the selection to the field you want.

    ![Edit selected field.](media/gallery-fields-change.png "Edit selected field")

1. Close the data pane.

The gallery updates with the selected changes.

![Updated gallery.](media/gallery-fields-updated.png "Updated gallery")

### Update the app title

To update the app title:

1. Select the label from the upper-left corner of the screen.

    ![Updated title.](media/app-title.png "Updated title")

1. Change the *Text* property value from the properties pane on the right.

    ![Update title property.](media/update-title.png "Update title property")

Verify all the changes you made to the app.

![Verify all changes.](media/app-changes.png "Verify all changes")

> [!TIP]
> For better responsiveness, the [data cards](../maker/canvas-apps/working-with-cards.md) by default have the [**Width fit**](../maker/canvas-apps/controls/properties-size-location.md#size) property set to *On*. If you want to resize the data cards manually, select the data cards and then set the **Width fit** property to *Off*.

![Data card - width fit property.](media/data-card-width-fit.png "Data card - width fit property")

### Save and preview the app

Now that you've created your first app with data, you can save your changes and preview the app.

![Save and preview.](media/save-preview.png "Save and preview")

1. Select **Save**.

1. Select **Preview**.

    - To add a new record, select **New record** and fill in the form.
    - To edit a record, select the record from the left pane, and edit the values.
    - To close the preview, select **Close** or the **Esc** key.

### Publish and add app to Teams channel

Select **Publish to Teams** to publish the app so others in your team can use the app, and add the app to Teams channel. More information: [Publish and add an app to Teams](publish-and-share-apps.md)

Now that you've created your first app from a blank table, let's go through the
Power Apps interface, Studio, controls and how to create additional apps in
detail.

## Additional considerations for Microsoft 365 Group

When you select **Create** to create an app in the selected team, Power Apps automatically enables the selected team's Microsoft 365 Group for security. However, if the group can't be enabled for security, you see the following error: 

`The request failed with error: 'Insufficient privileges to complete the operation.' The tracking Id is '[xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx]'`.

To fix this issue, manually update the Microsoft 365 Group setting *SecurityEnabled* from
*False* to *True* by using PowerShell. For detailed steps, see [Share an app with Microsoft 365 Groups](../maker/canvas-apps/share-app.md#share-an-app-with-microsoft-365-groups). For more information, see [Microsoft 365 Groups and Microsoft Teams](/microsoftteams/office-365-groups).

### Enabling security for teams with same names

Team names aren't always unique. It's possible for more than one
team in Teams to share the same display name. For example, there might be
more than one team with the name "Inspection" in a tenant. However, the
Microsoft 365 Group associated with each team has a different *ObjectId* in
Azure Active Directory (Azure AD), even when the team names are the same. The *ObjectId* in
Azure AD for a Microsoft 365 Group is the same as the *GroupId* in
Teams for the associated team.

To find the **GroupId** (ObjectID in Azure AD) of a team:

1. Go to the team in Teams.

1. Select any channel in the team.

1. Select **More options** (...) from the upper-right corner, and then select **Get link to channel**.

    ![Get link to the channel.](media/get-channel-link.png "Get link to the channel")

1. Copy the *GroupID* from the link.

    ![Group ID.](media/group-id.png "Group ID")

    You can also copy the channel link by selecting **Copy**, and then pasting it into a text editor
to get the *GroupID* value.

    `https://teams.microsoft.com/l/channel/19%3a06f038959c9f4387a35f5d776484cff2%40thread.tacv2/General?groupId=40b7e373-a788-4e29-a590-5a86db7550e3&tenantId=00000000-0000-0000-0000-0000000000000000`

1. Now that you have the correct team's **GroupID** (ObjectID in Azure AD), use the instructions in
[Share an app with Microsoft 365 Groups](../maker/canvas-apps/share-app.md#share-an-app-with-microsoft-365-groups)
to enable security for the team's Microsoft 365 Group.

## Next steps

[Overview of the Power Apps app](overview-of-the-power-apps-app.md)<br/>
[Understand Power Apps Studio](understand-power-apps-studio.md)<br/>
[Use the Fluent UI controls](use-the-fluent-ui-controls.md)<br/>
[Create additional apps](create-additional-apps.md)


[!INCLUDE[footer-include](../includes/footer-banner.md)]
