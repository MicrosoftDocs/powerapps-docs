---
title: Create a canvas app based on Excel data
description: Learn how to create a blank canvas app based on an Excel file.
author: mduelae
ms.topic: how-to
ms.custom: canvas
ms.collection: get-started
ms.reviewer: 
ms.date: 03/13/2025
ms.subservice: canvas-maker
ms.author: tapanm
search.audienceType: 
  - maker
contributors:
  - mduelae
---
# Create a canvas app based on Excel data

There are a few different ways to use Excel data to create a canvas app. 

In Excel, it's important to format your data as a table rather than just a range of cells. This makes it easier for Power Apps to read and interact with the data. To do this, select your data and select **Insert** > **Table** in Excel. This ensures that Power Apps can recognize and use the data effectively. More information: [Formatted as a table in Excel](https://support.office.com/article/Create-an-Excel-table-in-a-worksheet-E81AA349-B006-4F8A-9806-5AF9DF0AC664).

To create an app using Excel data, select one of the following options in [Power Apps](https://make.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).

|Create options using Excel  |Benefits | Navigation  |
|---------|---------|---------|
|[Import an external Excel or .CSV file to Power Apps](get-started-create-from-blank.md#import-an-external-excel-file) |  Uploaded Excel data generates a Dataverse table. With Dataverse's standard and custom tables, you can securely store your data in the cloud. These tables enable you to define your organization's data in a way that is tailored to your business needs, making it easier to use within your apps.| Select **Start with Data** > **Create new tables** > **Import an Excel file or .CSV** option.      | 
| [Connect to an external Excel file and use it to create a canvas app](get-started-create-from-blank.md#connect-to-an-external-excel-file-from-power-apps). Your data stay where it is. |  Using the Excel connector in Power Apps provides a straightforward, and fast method to create and deploy apps with data stored in Excel. It's especially advantageous for makers that already use Excel and want to enhance its functionality with minimal effort. Makers benefit from cloud access, easy data manipulation, rapid prototyping, and no need for a complex database setup. | Select **Start with Data** > **Connect external data** >  **From Excel**.   |
|[Create a blank canvas app and then add Excel data](get-started-create-from-blank.md#create-a-blank-canvas-app-and-add-excel-data)   | You have complete flexibility, control, and customization. It allows you to design an app that meets your exact specifications without being limited by predesigned templates, providing greater creative freedom and adaptability to suit your unique needs  |  On the left navigation pane, select **Create** > **Start with a blank canvas**.       |


## Import an external Excel file

When you import your Excel data to Power Apps, it doesn't just stay as an Excel file. Instead, it gets converted into a Dataverse table. This conversion lets your data be more easily integrated and managed within Power Apps, offering more powerful features compared to using Excel alone. More information: [Why use Dataverse?](../data-platform/data-platform-intro.md#why-use-dataverse)

1. Sign in to [Power Apps](https://make.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).
1. Select **Start with Data** > **Create new tables** > **Import an Excel file or .CSV**.
1. Select **Select from device** and navigate to the location where your Excel file is saved, and upload it.

    The maximum file size limit is 5 GB.

1. When the table is created, select a column name or the table name to edit the properties to suit your needs. If there are values in cells that are incompatible with the selected data type when changing column data types, those values are removed when the table is generated. More information: [Create and edit tables using Power Apps](../data-platform/create-edit-entities-portal.md#create-new-tables)
1. Select **Row ownership** and choose how you want to manage row ownership. 
1. When you're done, select **Save and open app**. The system uploads the first 20 rows of data so you can start reviewing the data in your app. The remaining data is uploaded in the background.

### Known issues

- The current data upload process doesn't take into account the environment data format setting.


## Connect to an external Excel file from Power Apps

Store the Excel file in a cloud storage service like Dropbox, Google Drive, OneDrive, or OneDrive for Business because Power Apps can only connect to Excel files that are stored in the cloud.

Power Apps has an Excel connector that allows you to access your Excel data. There are two versions available:

- The older version connects to Excel files stored in specific locations, such as OneDrive for Business. 

- We recommend that you use the newer version, called [Excel Online (Business)](/connectors/excelonlinebusiness/), which offers greater flexibility by accessing a wider variety of cloud-based file storage services.

1. Sign in to [Power Apps](https://make.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).
1. Depending on how you want to create your app, from the home screen, select one of the following options:
   - To create a single-page gallery app with a responsive layout, choose either:
     - **Start with data** > **Connect to external data** > **From Excel**.
     - **Start with page design** > **Gallery connected to external data** > **From Excel**.
   - To create a three screen mobile app, select **Start with an app template** > **From Excel**.
1. Only one connection is shown at a time. To select a different connection, select the **...** button to switch connection or add a new connection.
1. Enter the file location and select the table.
1. When you're done, select **Create app**.


For more information about how to share Excel data, see [Sharing Excel tables](connections/cloud-storage-blob-connections.md#sharing-excel-tables).


## Create a blank canvas app and add Excel data

Create a blank canvas app and then use Excel data that's [formatted as a table](https://support.office.com/article/Create-an-Excel-table-in-a-worksheet-E81AA349-B006-4F8A-9806-5AF9DF0AC664) as the source of the app's information.

Follow the example below to create an app with two screens where users can view (browse) the data from an Excel file on one screen, and on another screen, they can interact with (add, modify, or remove) that data. The data interaction features, such as creating, updating, and deleting records, are built into the second screen of the app.

### Prerequisites

1. Copy this data and paste it into an Excel file.

    | StartDay | StartTime | Volunteer | Backup |
    | --- | --- | --- | --- |
    | Saturday |10am-noon |Vasquez |Kumashiro |
    | Saturday |noon-2pm |Ice |Singhal |
    | Saturday |2pm-4pm |Myk |Mueller |
    | Sunday |10am-noon |Li |Adams |
    | Sunday | noon-2pm |Singh |Morgan |
    | Sunday | 2pm-4pm |Batye |Nguyen |

1. [Format the table in Excel](https://support.office.com/article/Create-an-Excel-table-in-a-worksheet-E81AA349-B006-4F8A-9806-5AF9DF0AC664) and name it **Schedule** so that Power Apps can parse the information.

1. Save the file under the name **eventsignup.xlsx**, close it, and then upload it to a [cloud-storage account](connections/cloud-storage-blob-connections.md) such as OneDrive.

> [!IMPORTANT]
> You can use your own Excel file and review this example for general concepts only. However, the data in the Excel file must be [formatted as a table](https://support.office.com/article/Create-an-Excel-table-in-a-worksheet-E81AA349-B006-4F8A-9806-5AF9DF0AC664).

### Create a blank app and connect to data

1. Sign in to [Power Apps](https://make.powerapps.com).

1. On the left navigation pane, select **Create** > **Start with a blank canvas**.

1. Select the **Phone size** layout.

    The app opens in [Power Apps Studio](power-apps-studio.md) where you can add data and start building the app.

1. In the middle of the screen, select **Connect to data**.

1. In the **Data** pane, select **Add data**. Select the connection for your cloud-storage account if it appears. Otherwise, follow these steps to add a connection such as OneDrive:

1. In the search box, enter **OneDrive** and select it.
1. Select **Add a connection**.
1. On the connection pane, select **Connect**.
1. If prompted, provide your credentials for that account.

1. Under **Choose an Excel file**, find and then select the **eventsignup.xlsx** that you saved earlier.

1. Under **Choose a table**, select the checkbox for **Schedule**, and then select **Connect**.

1. In the upper-right corner of the **Data** pane, close it by selecting the close icon (X).

### Create the view screen

1. On the command bar, select **New screen** > **List**.

    A screen is added with several default controls, such as a search box and a **[Gallery](controls/control-gallery.md)** control. The gallery covers the entire screen under the search box.

1. At the top of the new screen, select the **[Title]** [Label](controls/control-text-box.md) and rename it to **View records**.

     ![Change title bar for view records.](./media/get-started-create-from-blank/change-title-bar.png)

1. In the **Tree view**, select **BrowseGallery1**.

    ![Add a list screen.](./media/get-started-create-from-blank/select-gallery.png)

1. In the gallery's **Properties** pane, set the **Layout** to **Title, subtitle, and body**.

    ![Open the layout menu.](./media/get-started-create-from-blank/select-layout.png)

1. In the formula bar, replace **CustomGallerySample** with **Schedule**, and replace both instances of **SampleText** with **Volunteer**.

1. On the right edge of the formula bar, select the **Expand formula bar** down arrow, and then select **Format text**.

    The formula matches this example:

    ```power-fx
    SortByColumns(
        Search(
            Schedule,
            TextSearchBox1.Text,
            "Volunteer"
        ),
        "Volunteer",
        If(
            SortDescending1,
            SortOrder.Descending,
            SortOrder.Ascending
        )
    )
    ```

1. In the **Properties** pane, select **Edit** next to the **Fields** label.

1. In the **Title2** box, select **Volunteer**, in the **Subtitle2** box, select **StartDay**, and in the **Body1** box, select **StartTime**.

1. In the upper-right corner of the **Data** pane, close it by selecting the close icon (X).

    Users can sort and filter the gallery by volunteer name based on the **SortByColumns** and **Search** functions in that formula.

    - If a user types at least one letter in the search box, the gallery shows only those records for which the **Volunteer** field contains the text that the user typed.
    - If a user selects the sort button (between the refresh button and the plus button in the title bar), the gallery shows the records in ascending or descending order (depending on how many times the user selects the button) based on the **Volunteer** field.

For more information about these and other functions, see the [formula reference](formula-reference.md).

### Create the change screen

1. On the command bar, select **New screen** > **Form**.

1. In the **Tree view**, select **EditForm1**.

1. On the **Properties** pane, select the down arrow next to **Data source**, and then select **Schedule** in the list that appears.

1. Under the data source that you specified, select **Edit fields**.

1. In the **Fields** pane, select **Add field**, select the check box for each field, and then select **Add**.

1. Select the arrow next to the name of each field to collapse it, and then drag the **Volunteer** field up so that it appears at the top of the list of fields.

     ![Reorder fields.](./media/get-started-create-from-blank/reorder-fields.png)

1. In the upper-right corner of the **Fields** pane, close it by selecting the close icon (X).

1. Set the **Item** property of the form to this expression in the formula bar:

    `BrowseGallery1.Selected`

1. At the top of the screen, select the **[Label](controls/control-text-box.md)** control, and then replace **[Title]** with **Change records**.

    ![Change title bar.](./media/get-started-create-from-blank/change-title-bar2.png)

### Delete and rename screens

1. In the **Tree view**, select the ellipsis (...) for **Screen1**, and then select **Delete**.

    ![Delete screen.](./media/get-started-create-from-blank/delete-screen.png)

1. Select the ellipsis (...) for **Screen2**, select **Rename**, and then type or paste **ViewScreen**.

1. Select the ellipsis (...) for **Screen3**, select **Rename**, and then type or paste **ChangeScreen**.

### Configure icons on the view screen

1. Near the top of the **ViewScreen**, select the circular arrow icon.

    ![Add record for refresh.](./media/get-started-create-from-blank/refresh-icon.png)

1. Set the **OnSelect** property for that icon to this formula:

    `Refresh(Schedule)`

    When the user selects this icon, the data from **Schedule** refreshes from the Excel file.

    For more information about this and other functions, see [formula reference](formula-reference.md).

1. In the upper-right corner of the **ViewScreen**, select the plus icon.

    ![Add record.](./media/get-started-create-from-blank/add-record.png)

1. Set the **OnSelect** property for that icon to this formula:

    `NewForm(EditForm1);Navigate(ChangeScreen,ScreenTransition.None)`

    When the user selects this icon, **ChangeScreen** appears with each field empty, so the user can create a record more easily.

1. Select the right-pointing arrow for the first record in the gallery.

    ![Select arrow.](./media/get-started-create-from-blank/select-arrow.png)

1. Set the **OnSelect** property for the arrow to this formula:

    `EditForm(EditForm1); Navigate(ChangeScreen, ScreenTransition.None)`

    When the user selects this icon, **ChangeScreen** appears with each field showing the data for the selected record, so the user can edit or delete the record more easily.

### Configure icons on the change screen

1. On **ChangeScreen**, select the "X" icon in the upper left corner.

    ![Cancel icon.](./media/get-started-create-from-blank/cancel-icon.png)

1. Set the **OnSelect** property for that icon to this formula:

    `ResetForm(EditForm1);Navigate(ViewScreen, ScreenTransition.None)`

    When the user selects this icon, any changes made in this screen are discarded, and the view screen opens.

1. In the upper-right corner, select the checkmark icon.

    ![Checkmark icon.](./media/get-started-create-from-blank/checkmark-icon.png)

1. Set the **OnSelect** property for the checkmark to this formula:

    `SubmitForm(EditForm1); Navigate(ViewScreen, ScreenTransition.None)`

    When the user selects this icon, any changes made in this screen are saved, and the view screen opens.

1. On the **Insert** tab, select **Icons**, and then select the **Trash** icon.

1. Set the new icon's **Color** property to **White** and move the new icon so it appears next to the checkmark icon.

    ![Trash icon.](./media/get-started-create-from-blank/trash-icon.png)

1. Set the **Visible** property for the trash icon to this formula:

    `EditForm1.Mode = FormMode.Edit`

    This icon appears only when the form is in **Edit** mode, not in **New** mode.

1. Set the **OnSelect** property for the trash icon to this formula:

    `Remove(Schedule, BrowseGallery1.Selected); Navigate(ViewScreen, ScreenTransition.None)`

When the user selects this icon, the selected record is deleted from the data source and the view screen opens.

### Test the app

1. Select the **ViewScreen**, and then preview the app by pressing <kbd>F5</kbd> or select **Preview**.

    ![Open Preview mode.](./media/get-started-create-from-blank/open-preview.png)

1. Type or paste one or more letters in the search box to filter the list based on the volunteer's name.

1. Select the sort icon one or more times to show the data in ascending or descending order based on the volunteer's name.

1. Add a record.

1. Update the record that you added, and then save the changes.

1. Update the record that you added, and then cancel the changes.

1. Delete the record that you added.

1. Close Preview mode by pressing Esc or selecting the close icon in the upper-right corner.

## Next steps

- Press Ctrl+S to save your app in the cloud so you can run it from other devices.
- [Share the app](share-app.md) so other people can run it.



[!INCLUDE[footer-include](../../includes/footer-banner.md)]
