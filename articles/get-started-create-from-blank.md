<properties	pageTitle="Create an app from a blank screen in PowerApps"
	description="Create an app automatically based on one of several templates for a variety of scenarios. Explore how the app works by default, and then customize the app to better fit the way you work."
	services="powerapps"
	authors="AFTOwen"/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="hero-article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="10/20/2015"
   ms.author="anneta"/>

# Create an app from a blank screen #
Create your own app from scratch using any of a variety of data sources. Specify the appearance and behavior of each UI element so that you can optimize the app to meet your exact goals and workflow.

[What is PowerApps?](http://www.kratosapps.com/tutorials)

By following this tutorial, you'll create an app that shows users a set of data on its first screen:

![Screen in which users can scroll through a set of data](./media/get-started-create-from-blank/view-screen.jpg)

On another screen, users can create, update, or delete a record in that set of data:

![Screen in which users can scroll through a set of data](./media/get-started-create-from-blank/change-screen.jpg)

**Prerequisites**

- Sign up for and install [PowerApps](http://aka.ms/powerappsinstall)
- Familiarity with how to [configure a control](get-started-test-drive.md#configure-a-control) in PowerApps
- A set of data in the cloud, such as in DropBox or OneDrive

To follow this tutorial exactly:

1. Create an Excel file, and name it **eventsignup.xlsx**.

1. Add this data, which shows who has signed up to cover which shifts during a fictional event.

	![Source data in Excel](./media/get-started-create-from-blank/excel-data.jpg)

1. [Format the data as a table](https://support.office.com/en-us/article/Format-an-Excel-table-6789619F-C889-495C-99C2-2F971C0E2370), name the table **Schedule**, and save the file to a Dropbox account.

## Connect to a data source ##
1. In PowerApps, open the **File** menu, and then click **New**.

	![New option on the File menu](./media/get-started-create-from-blank/file-new.jpg)

1. Leave the default option to create a phone app.

	![Options to create a phone app or a tablet app](./media/get-started-create-from-blank/phone-app.jpg)

1. Under **Blank App**, click **Get Started**.

	![Option to create an app from scratch](./media/get-started-create-from-blank/blank-app.jpg)

1. If you haven't created a data connection, follow these steps:

	1. Open the **File** menu, and then click **Connections**.

	![Connections option on the File menu](./media/get-started-create-from-blank/file-connections.jpg)

	1. Click **Available Connections**, click the connection that you want to use (such as **Dropbox**), and then click **Connect**.

	![Dropbox option and Connect button](./media/get-started-create-from-blank/add-dropbox.jpg)

	1. Provide the requested credentials, and then click **Sign in**.

	1. In the upper-left corner, click the Back arrow to return to the default workspace.

	![Back arrow from Connections to default workspace](./media/get-started-create-from-blank/back-from-connections.jpg)

1. On the bottom edge of the screen, click **Options**.

	![Connections option on the File menu](./media/get-started-create-from-blank/open-options.jpg)

	The **Screen** tab of the **Options** pane appears.
1.  Under **Data Sources**, click **Insert your data**.

	![Option to specify data source](./media/get-started-create-from-blank/insert-your-data.jpg)

1. Click the data source that you want to use (such as the Excel file that you created and uploaded for this tutorial), and then click **Connect**.

	![Specify the Excel file that you want to use](./media/get-started-create-from-blank/select-excel-file.jpg)

1. Under **Select a table**, click the table that you want to use (such as **Schedule**), and then click **Connect**.

	![Specify the table in Excel that you want to use](./media/get-started-create-from-blank/select-table.jpg)

	The **Screen** tab shows which data sources you've added to your app. This tutorial requires only one source, but you can add more sources to better fit your needs.

1. In the upper-right corner of the **Options** pane, click the **Close** icon.

## Show the data ##
1. On the **Insert** tab of the ribbon, click **Gallery**, and then click the text gallery in **Portrait** orientation.

	![Option to add a text gallery in portrait orientation](./media/get-started-create-from-blank/add-gallery.jpg)

1. Set the **Items** property of the gallery to **Schedule**.

	![The Schedule data in the gallery by default](./media/get-started-create-from-blank/gallery-data-default.jpg)

1. In the lower-right corner, click **Quick Start**.

	![Option to open Quick Start pane](./media/get-started-create-from-blank/open-quick-start.jpg)

1. In the **Quick Start** pane, click **Content**.

	![Content tab of Quick Start pane](./media/get-started-create-from-blank/qs-content.jpg)

1. In the **Heading1** list, click **StartDay**.
1. In the **Subtitle1** list, click **StartTime**.

1. (optional) Move the gallery down a bit, resize it to show more items, and add a label that identifies the screen.

	![View screen with gallery and label](./media/get-started-create-from-blank/view-screen-gallery-label.jpg)

## Add a label to the gallery ##
1. In the first item of the gallery, click the **Subtitle1** label, and reduce its height by about half.

	![View screen with gallery and label](./media/get-started-create-from-blank/resize-subtitle1.jpg)

	**Note:** When you change the first item in a gallery, which is the gallery template, you automatically change all other items in the gallery.

1. With the **Subtitle1** label still selected, click the **Insert** tab on the ribbon, and then click **Label**.

	![The Label option on the Insert tab of the ribbon](./media/get-started-create-from-blank/insert-label.jpg)

1. On the **Content** tab of the **Quick Start** pane, click **Staff2** in the **Label1** list.

1. On the **Home** tab of the ribbon, set the **Size** of the label's font to **11**.

	![The Size option on the Home tab of the ribbon](./media/get-started-create-from-blank/change-font-size.jpg)

1. Resize and move the **Staff2** label so it appears under the **Staff1** label.

	![The ViewScreen with the gallery showing all fields](./media/get-started-create-from-blank/view-screen-staff2.jpg)

## Add a screen and navigation ##
1. [Rename the default screen](add-screen-context-variables.md#add-a-screen-and-navigation) to **ViewScreen**, add another screen, and name it **ChangeScreen**.

	![Thumbnails of ViewScreen and ChangeScreen](./media/get-started-create-from-blank/rename-screens.jpg)

1. On the **ViewScreen**, select the gallery template by clicking any item in the gallery except the first one and then clicking the pencil icon in the upper-left corner of the gallery.

	![Pencil icon to edit gallery template](./media/get-started-create-from-blank/edit-gallery-template.jpg)

1. On the **Insert** tab of the ribbon, click **Shapes**, and then click the Next arrow.

	![Option to add a next arrow](./media/get-started-create-from-blank/add-next-arrow.jpg)

1. Move the arrow to the right edge of the gallery, and then set its **OnSelect** property to this formula:

	**Navigate(ChangeScreen,ScreenTransition!Fade,{Record:ThisItem})**

	This formula includes the **Navigate** function, which you use to open one screen from another. That function requires at least two pieces of information (named arguments): the name of the screen that you want to open and the visual effect of that transition. In this example, the first argument specifies that you want to open the **ChangeScreen**, and the second argument specifies that you want that screen to fade into view.

	In addition, this formula specifies a context variable, named **Record,** that's set to a value of **ThisItem**. In other words, this formula tracks the gallery item in which the arrow was clicked, so that the controls on the **ChangeScreen** will automatically show the data from that item.

1. Click anywhere outside the gallery, click the **Insert** tab on the ribbon, and then click **Button**.

	![Button option on the Insert tab](./media/get-started-create-from-blank/insert-button.jpg)

1. Move the button under the gallery, and configure the button so that it shows the word **New**.

	![Button option on the Insert tab](./media/get-started-create-from-blank/view-screen-button.jpg)

1. Set the **OnSelect** property of the button to this formula:

 	**Navigate(ChangeScreen,ScreenTransition!Fade,{Record:Defaults(Schedule)})**

	As with the Next arrow in the gallery, this formula includes the **Navigate** function, and you use the same arguments to specify which screen to open and the visual effect to use. In this case, this formula sets the value of the **Record** context variable to the default values of the **Schedule** data source. That data source has no default values, so the  controls on the **ChangeScreen** will be blank. If the data source had default values, they would appear in the controls so that users could more easily accept or modify them.

1. On the **ChangeScreen**, add a label that identifies it, and [add a Back arrow](add-screen-context-variables.md#add-a-screen-and-navigation) that returns to the **ViewScreen** when a user clicks the arrow.

	![ChangeScreen with label and arrow](./media/get-started-create-from-blank/change-screen-blank.jpg)

## Add controls for adding or editing a record ##

1. On the **ChangeScreen**, add a label, and configure it to show **Day** in bold letters.

	![Added label with bold text to ChangeScreen](./media/get-started-create-from-blank/day-label.jpg)

1. On the **Insert** tab, click **Text**, and then click **Input Text**.

	![Text-input control on the Text option of the Insert tab](./media/get-started-create-from-blank/add-text-input.jpg)

1. Move the new input-text control just under the **Day** label.

	![Move text-input control under Day label](./media/get-started-create-from-blank/move-input-text.jpg)
1. Name the input-text control **inputDay**, and set its **Default** property to **Record!Day**.

	You'll refer to that control by its name later in this topic, when you configure the **Save** button.

	By setting the **Default** property as the previous step instructs, you configure the input-text control to show the **Day** value that's stored in the **Record** context variable.

	- If the user navigated to this screen by clicking the Next arrow in a gallery item on the **ViewScreen**, this control shows the **Day** value for that item.
	- If the user navigated to this screen by clicking the **New** button on the **ViewScreen**, this control shows the data source's default value for the **Day** column. Because this data source has no defaults, the control will be blank.

1. Copy the label and the input-text control, paste them three times, and arrange them in a column that alternates labels with input-text controls.

	![Create three copies of the label and the text-input control](./media/get-started-create-from-blank/copy-labels-input-text.jpg)

1. Configure the pasted labels to show these strings:
	- **Time**
	- **Staff1**
	- **Staff2**

	![Update the three copies of the label](./media/get-started-create-from-blank/update-pasted-labels.jpg)

1. Name each input-text control based on the text of the label above it:
	- **inputTime**
	- **inputStaff1**
	- **inputStaff2**

1. Set the **Default** property of each input-text control based on the text of the label above it:
	- **Record!Time**
	- **Record!Staff1**
	- **Record!Staff2**

## Test the controls for adding or editing a record ##
1. On the **ViewScreen**, press F5, and then click the arrow for any item in the gallery.

	The **ChangeScreen** appears and shows the data for the item you specified. You can easily edit one or more fields in the record.

1. Click the Back arrow, and click the **New** button.

	The **ChangeScreen** appears and shows nothing in the input-text controls. You can easily add information in each field of the record.

1. Press Esc to return to the default workspace.

## Add buttons for saving changes and removing a record ##

1. On the **ChangeScreen**, add two buttons, move them to the bottom of the screen, and configure them to show **Save** and **Remove**.

1. Set the **OnSelect** property of the **Save** button to this formula:

	**UpdateContext({Record:Patch(Schedule,Record,{StartDay:inputDay!Text,StartTime:inputTime!Text,Staff1:inputStaff1!Text,Staff2:inputStaff2!Text})});If(IsEmpty(Errors(Schedule,Record)),Navigate(ViewScreen,ScreenTransition!Fade))**

	In this formula, you use the **UpdateContext** function to change the value of the **Record** variable to the output of the **Patch** function. The **Patch** function adds or updates a record in a data source and requires three arguments: the name of the data source to update, the record to update, and the information that the record should contain after the change. In this case, the **Patch** function will update the **Schedule** data source. If the user clicked the **New** button on the **ViewScreen** to open the **ChangeScreen**, a record will be created. If the user clicked a Next arrow for a gallery item, the record for that item will be updated. In either case, the new or updated record will contain the information from each text-input control on the **ChangeScreen**.

 	In addition, you use the **If** function in this formula to open the **ViewScreen** only if the output of the **Errors** function is empty. The **Errors** function tracks whether any errors occurred when the app tried to create or update the record. (For example, an error would occur if the device wasn't connected to the network and couldn't update the **Schedule** data source.) If no errors occurred, the **ViewScreen** would fade open. If an error occurred, the **ChangeScreen** would remain open.

1. Set the **OnSelect** property of the **Remove** button to this formula:

	**UpdateContext({NewRecord:Remove(Schedule,Record)});If(IsEmpty(Errors(Schedule,Record)),Navigate(ViewScreen,ScreenTransition!Fade))**

	In this formula, you use the **UpdateContext** function to create a context variable named **NewRecord**, and you set the value of that variable to the output of the **Remove** function. The **Remove** function is simpler to use than **Patch** in that **Remove** requires the same two arguments to specify a data source and a record, but you don't need to specify any data to add or update. This formula also includes the same **If** that returns to the **ViewScreen** only if no errors occurred when the app tried to remove the record.  

1. Add a label, move it below the last input-text control, and set the label's **Text** property to this formula:

	**First(Filter(Errors(Schedule,Record),IsBlank(Column)))!Message**

	In this formula, you're configuring the label to show information about an error that might have occurred when the app tried to add, update, or remove a record. The formula centers around the **Errors** function, which tracks error information in a table. Overall, the formula shows the data from the **Message** column of that table for the **First** record in which the **Column** column is blank.
