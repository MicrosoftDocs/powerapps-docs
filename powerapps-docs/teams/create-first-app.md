---
title: Create your first app in Teams | Microsoft Docs
description: Learn how to create your first app in Teams. 
author: tapanm-msft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 09/24/2020
ms.author: tapanm
ms.reviewer: 
---

# Create your first app in Microsoft Teams

[!INCLUDE [cc-beta-prerelease-disclaimer.md](../includes/cc-beta-prerelease-disclaimer.md)]

You can create, edit, and delete [canvas apps](/powerapps/maker/canvas-apps/getting-started) in Teams.

If you're creating an app by using Power Apps in a Teams team for the first time, a new Project Oakdale environment will be created for you. More information: [About the Project Oakdale environment](/power-platform/admin/about-teams-environment)

## Get started with creating your first app

After installing the Power Apps app from the Teams store:

1. Start Teams, and sign in.

1. In the left pane, select **Power Apps**, and then select **Create an app**.

    ![Start creating an app](media/create-app-1.png "Start creating an app")

    > [!TIP]
    > If you don't see the **Power Apps** app in the left pane, select ![More added apps - ellipsis](media/more-added-apps-ellipsis.png "More added apps - ellipsis") (*More added apps*), and then select **Power Apps**.
    
    ![Power Apps](media/power-apps.png "Power Apps")

1. You'll be prompted to select a team where you want to create the app. Select a team to create the app.

    ![Select a team to create the app](media/create-app-2.png "Select a team to create the app")

    If this is the first app being created in the selected team, a new Project Oakdale environment will be created for the selected team. You'll see a message about this when you select the team. More information: [About the Project Oakdale environment](/power-platform/admin/about-teams-environment)

    ![Creating the first app in a team](media/create-app-3.png "Creating the first app in a team")

1. Select **Create**. You'll see a confirmation about the Project Oakdale environment being created, which might take some time. You'll be notified when the environment is available for you to create your first app.

    ![First app in a team](media/create-app-4.png "First app in a team")

> [!NOTE]
> Environment creation will fail if the Teams team that you selected has *Hiddenmembership* enabled. If this happens, try creating the app in a different team. More information: [Hidden membership groups](known-issues-limitations.md#hidden-membership-groups)

### Notification

Once the environment gets created, you'll see a notification on the bottom-right side of Teams.

![Bottom notification](media/notification-bottom.png "Bottom notification")

The notification also appears in Teams Activity.

![Activity notification](media/notification-activity.png "Activity notification")

## Creating an app in a team with a Microsoft 365 Group

When you select **Create** to create an app in the selected team, Power Apps automatically enables the selected team's Microsoft 365 Group for security. However, if the group can't be enabled for security, you'll see the following error: 

`The request failed with error: 'Insufficient privileges to complete the operation.' The tracking Id is '[xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx]'`.

To fix this issue, manually update the Microsoft 365 Group setting *SecurityEnabled* from
*False* to *True* by using PowerShell. For detailed steps, see [Share an app with Microsoft 365 Groups](../maker/canvas-apps/share-app.md#share-an-app-with-office-365-groups). More information: [Microsoft 365 Groups and Microsoft Teams](https://docs.microsoft.com/microsoftteams/office-365-groups)

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

    ![Get link to the channel](media/get-channel-link.png "Get link to the channel")

1. Copy the *GroupID* from the link.

    ![Group ID](media/group-id.png "Group ID")

    You can also copy the channel link by selecting **Copy**, and then pasting it into a text editor
to get the *GroupID* value.

    `https://teams.microsoft.com/l/channel/19%3a06f038959c9f4387a35f5d776484cff2%40thread.tacv2/General?groupId=40b7e373-a788-4e29-a590-5a86db7550e3&tenantId=00000000-0000-0000-0000-0000000000000000`

1. Now that you have the correct team's **GroupID** (ObjectID in Azure AD), use the instructions in
[Share an app with Microsoft 365 Groups](/powerapps/maker/canvas-apps/share-app#share-an-app-with-office-365-groups)
to enable security for the team's Microsoft 365 Group.

## Continue creating your first app

After your Project Oakdale environment has been created, you can go to the build hub and continue creating your first app.

> [!NOTE]
> If you wait in Teams for the environment to be created, you're automatically taken to the Power Apps Studio and a new app. In this situation, skip this step and go to [create your first table](#create-your-first-table).

1. Select the **Build** tab to view the environment created for your team.

    ![Build tab](media/build-tab-env.png "Build tab")

1. Select **Create** to get started building your first app. This action opens
Power Apps Studio, where you're prompted to name your app. 

1. Enter an app name, and then select **Save**.

    ![Name your app](media/name-your-app.png "Name your app")

    > [!TIP]
    > An app template is included with the app by default, so that you can get started with creating your table and using the app. More information: [Understand Power Apps Studio](understand-power-apps-studio.md)

### Create your first table

Data for apps built in Teams lives in Project Oakdale environments as tables. Like other data experiences, you can add additional columns to track different attributes of each record before filling up the table with multiple rows of data.

> [!TIP]
> To learn about Project Oakdale tables in detail, go to [Overview of Project Oakdale](overview-data-platform.md).

To get started creating your first table:

1. Select **Create new table**.

    ![Create your first table](media/create-first-table.png "Create your first table")

1. In the **Create a table** dialog box, type a meaningful name for your
new table that describes this dataset, and then select
**Create**.

1. After the table is created, you can add columns of different types, add rows, and
work with data in the Visual Editor.

   ![Visual Editor](media/table-designer-1.png "Visual Editor")

### Add columns to the table

To add a new column to track new data:

1. Select **Add column.**  

1. Enter a name that best describes your new column.

1. Select the type for your column.

    > [!TIP]
    > For more information about column types supported by the table
    designer, go to [Supported column types](understand-power-apps-studio.md#supported-column-types). To add columns that aren't supported by
    the Visual Editor, create a table by using the **Build** tab. More information: [Create tables](create-table.md)

1. If required, change **Advanced options** for the selected column type.

1. Select **Create**.

1. Repeat the previous steps to add the rest of the data columns.

### Add rows to the table

To add rows, select the empty row and start typing additional data, or
select **Add row**.

![Add rows](media/add-rows.png "Add rows")

### Update the app template

After you close the table, the app template that was added to the app screen by default is automatically refreshed to use the new table.

![Updated app template](media/updated-gallery.png "Updated app template")

Depending on the number of fields you added to your table, the app template might need updates to the form and the gallery.

#### Update background color for the selected gallery record

The gallery shows records created earlier. However, the background color needs to change for a record when selected from the gallery to show the selection.

To update the selected item background color:

1. Select the gallery.

    ![Select the gallery for background fill](media/select-gallery.png "Select the gallery for background fill")

2. Select *TemplateFill* property from the property drop-down on the top-left.

    ![Select TemplateFill property](media/select-templatefill.png "Select TemplateFill property")

3. Update the *TemplateFill* property value in the formula bar to the following formula:

    ```powerapps-dot
    If(ThisItem.IsSelected, RGBA(0,0,0,.05), RGBA(0,0,0,0))
    ```

    ![Update TemplateFill property](media/templatefill-property.png "Update TemplateFill property")

#### Update fields on the form

The template shows two fields inside the form by default. To add more fields to the form:

1. Select the form.

    ![Select the form](media/app-form.png "Select the form")

1. Select **Edit fields** from the property pane on the right.

    ![Edit fields](media/edit-form-fields.png "Edit fields")

1. Select **Add fields**.

    ![Add fields](media/add-fields.png "Add fields")

1. Select the fields that you want to add on the form.

    ![Select fields to add](media/add-fields-list.png "Select fields to add")

1. Select **Add**.

1. (Optional) Select fields to move up or down, or remove unwanted fields by selecting **Remove**.

    ![Move or remove fields](media/move-remove-field.png "Move or remove fields")

1. Close the fields pane.

Adding, removing, and reordering fields automatically updates the form.

![Updated form](media/form-updated.png "Updated form")

#### Update fields in the gallery

The gallery on the default app template might need updates to reflect the fields from the table you created.

![Default gallery](media/gallery-fields.png "Default gallery")

To update the fields in the gallery:

1. Select **Edit fields** from the property pane on the right.

    ![Edit fields for the gallery](media/edit-gallery-fields.png "Edit fields for the gallery")

1. Select the drop-down menu for a gallery component (such as image, title, or subtitle) and change the selection to the field you want.

    ![Edit selected field](media/gallery-fields-change.png "Edit selected field")

1. Close the data pane.

The gallery is updated with the selected changes.

![Updated gallery](media/gallery-fields-updated.png "Updated gallery")

#### Update the app title

To update the app title:

1. Select the label from the upper-left corner of the screen.

    ![Updated title](media/app-title.png "Updated title")

1. Change the *Text* property value from the properties pane on the right.

    ![Update title property](media/update-title.png "Update title property")

Verify all the changes you made to the app.

![Verify all changes](media/app-changes.png "Verify all changes")

> [!TIP]
> For better responsiveness, the [data cards](../maker/canvas-apps/working-with-cards.md) by default have [**Width fit**](../maker/canvas-apps/controls/properties-size-location.md#size) property set to *On*. If you want to resize the data cards manually, select the data cards and then set the **Width fit** property to *Off* first.

![Data card - width fit property](media/data-card-width-fit.png "Data card - width fit property")

### Save and preview the app

Now that you've created your first app with data, you can save your changes and preview the app.

![Save and preview](media/save-preview.png "Save and preview")

1. Select **Save**.

1. Select **Preview**.

    - To add a new record, select **New record** and fill in the form.
    - To edit a record, select the record from the left pane, and edit the values.
    - To close the preview, select **Close** or the **Esc** key.

## Add your app to a Teams channel as a tab

To use the app as a tab in your Teams channel, you'll need to save the app,
publish it, and then add it to your team's channel.

1. Go to your team in Teams.

1. Select the channel that you want to pin the app to, and then select +.

    ![Pin your app](media/pin-app.png "Pin your app")

1. Select **Power Apps**.

    ![Power Apps app in Teams](media/power-apps-app.png "Power Apps app in Teams")

1. Select **Add**.

1. Select your app from the list (in this example, **Sample app**), and then select **Save** to add the app as a tab.

Now that you've created your first app from a blank table, let's go through the
Power Apps interface, Studio, controls and how to create additional apps in
detail.

## Next steps

[Overview of the Power Apps app](overview-of-the-power-apps-app.md)<br/>
[Understand Power Apps Studio](understand-power-apps-studio.md)<br/>
[Use the Fluent UI controls](use-the-fluent-ui-controls.md)<br/>
[Create additional apps](create-additional-apps.md)
