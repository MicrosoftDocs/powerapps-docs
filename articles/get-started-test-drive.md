<properties
	pageTitle="Create an app from a template | Microsoft PowerApps"
	description="Step-by-step instructions for creating an app automatically based on a template, customizing the app, and then publishing it."
	services=""
	suite="powerapps"
	documentationCenter="na"
	authors="AFTOwen"
	manager="dwrede"
	editor=""
	tags=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="hero-article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="01/04/2015"
   ms.author="anneta"/>

# Create an app from a template #

[AZURE.VIDEO nb:cid:UUID:b95d313a-0d00-80c4-8bbc-f1e59201f745]

Create an app automatically based on one of several templates for a variety of scenarios. Explore how the app works by default, customize it to better fit the way you work, and then publish it.

**Prerequisites**

- Install [PowerApps](http://aka.ms/powerappsinstall)

- An account on DropBox, OneDrive, or GoogleDrive for storing sample data in the cloud

## Open a template ##
1. Open PowerApps.

1. If you haven't opened PowerApps before, select the right-pointing arrow near the lower-right corner to advance through the opening screens, and then sign in.

1. In PowerApps, select **Connections** in the **File** menu (near the left edge of the screen).

	![The Connections option on the File menu](./media/get-started-test-drive/file-connections.png)

1. Select **Available connections**, select **Dropbox** (or another cloud-storage account), and then select **Connect**.

	![Option to add Dropbox as a data connection](./media/get-started-test-drive/add-dropbox.png)

1. Provide your credentials, and then select **Sign in**.

	![Prompt to provide credentials for Dropbox](./media/get-started-test-drive/dropbox-credentials.png)

1. Select **New** on the **File** menu (near the left edge of the screen).

	![The New option on the File menu](./media/get-started-test-drive/file-new.png)

1. Leave the default option to create an app for a phone.

	![The option to create an app for a tablet or a phone](./media/get-started-test-drive/phone-app.png)

	**Note:** You can create an app for a tablet, but this tutorial focuses on the phone option.

1. Under **Start from a template**, select **Get started**.

	![Open a PowerApps template](./media/get-started-test-drive/open-template.png)

1. In the list of template categories, select **Events & Calendar**, select **Event SignUp**, and then select **Use** (near the lower-right corner).

	![Open the Event Signup template template](./media/get-started-test-drive/choose-template.png)

	When the app is created, the **VolunteerDetailsScreen** appears.

	![VolunteerDetailsScreen with default information](./media/get-started-test-drive/volunteer-default.png)

## Explore the app's default behavior ##
Apps from templates open in the default workspace, where you'll spend most of your time customizing an app or creating one from scratch. Before you make changes, you'll explore how the app works in **Preview**.

**Tip:** Design and develop apps in the default workspace, but test them in **Preview** before you share them with others.

1. In the left navigation bar, select the thumbnail for the **VolunteerDetailsScreen**.

	![Thumbnail for the VolunteerDetails screen](./media/get-started-test-drive/vdetails-thumbnail.png)

1. Press F5 (or select the right arrow in the upper-right corner) to open **Preview**.

	![Button to open Preview](./media/get-started-test-drive/preview-button.png)

1. Select a t-shirt size, and then select **Next**.

	![Options for specifying a t-shirt size and a Next button](./media/get-started-test-drive/tshirt-size.png)

	**ScheduleScreen** appears with columns for days, timeslots, and names of volunteers.

1. Select a **Sign up** button to schedule yourself for a timeslot.

	![Button for signing up for a particular timeslot](./media/get-started-test-drive/signup-button.png)

	**Note:** When you sign up for a timeslot, any remaining **Sign up** buttons for the same timeslot become unavailable.

1. (optional) Verify that the data in your cloud account reflects your changes.

1. (optional) Remove yourself from a timeslot by selecting the "X" icon next to your name.

1. Return to the default workspace by selecting the "X" icon in the upper-right corner (under the PowerApps title bar).

	![Button to close Preview](./media/get-started-test-drive/close-preview.png)

## Configure a control ##
As you customize the interface of an app or develop one from scratch, you'll add and configure elements that show text, images, and other information. To configure how an element appears or what it does, you select it, which adds a thick, gray box around it.

**Important:** If you select another element or a blank area of the screen, you can no longer configure the first element.

When an element is selected, you can configure it in these ways:

- Change it directly (for example, by moving it).
- Select a tab on the ribbon near the top of the screen, and then select an option on that tab.
- Select an option in the properties list, and then type a value in the formula bar. These elements appear near the top of the screen and are separated by an equals sign and the function button. In this example, the **Items** property appears in the properties list, and the value of that property (**Schedule**) appears in the formula bar.

	![Properties list and formula bar](./media/get-started-test-drive/properties-list.png)

If you can't find a property on the ribbon, find it in the properties list, which shows properties alphabetically.

1. Near the top of the screen, select **Event Signup**.

	![A text box surrounded by a selection box](./media/get-started-test-drive/selected-label.png)

1. Move the text box to the left edge of the screen by dragging the selection box around the text box.

1. Highlight the text inside the text box (for example, by triple-clicking it), and then change the text by typing **Sign up for PowerApps Conference**.

1. Resize the text box by dragging a handle in the upper-right or lower-right corner of the selection box until all the text appears in the box.

	![Resizing a control](./media/get-started-test-drive/resize-label.png)

1. With the text box still selected, select **Text** in the properties list, and then type **Now()** in the formula bar.

	The text box shows the current date and time.

1. With the text box still selected, rename it by selecting **Label11_2** on the **Home** tab and then typing **Banner**.

	![Renaming a control](./media/get-started-test-drive/rename-label.png)

	**Note:** As you develop or customize an app, you'll configure some controls to reference other controls. For example, you'll probably configure a button or other control to open one screen from another. That type of configuration will be much easier if the screens have names that are easier to remember than **Screen1**, **Screen2**, and so on.

## Save and share your app ##
After you finish developing and testing your app, share it with other people by saving it to [powerapps.com](https://web.powerapps.com) and sending mail that your app is available. Specify which people can run your app or even customize it to create their own versions.

1. On the **File** menu, select **App Settings**.

	![The App Settings option on the File menu](./media/get-started-test-drive/file-settings.png)

2. Update any of these settings.

	- the name of your app

		![Option to rename your app](./media/get-started-test-drive/rename-app.png)

	- the color of your app's tile

		![Color options for your app's tile](./media/get-started-test-drive/tile-color.png)

	- the image on your app's tile

		![Import an image to appear on your app's tile](./media/get-started-test-drive/tile-image.png)

	- the screen size and orientation of your app

		![Aspect-ratio options, such as 3:2 and 4:3](./media/get-started-test-drive/aspect-ratio.png)

		**Note:** If you change the size and orientation, select **Apply** (near the lower-right corner) to save the changes.

		![Apply button](./media/get-started-test-drive/apply-button.png)

2. On the **File** menu, select **Save As**.

	![Save As option on the File menu](./media/get-started-test-drive/file-save.png)

3. Under **Save As**, leave the default value of **PowerApps cloud**, and then select **Save**.

	![Save an app](./media/get-started-test-drive/save-powerapps.png)

6. On the **File** menu, select **Share**.

	An email template appears.

**Note**: Before you share an app, make sure that the people with whom you're sharing it have access to the data. For example, you must [share an Excel or other file](share-app-data.md) in a cloud-storage account.

1. Type the email addresses of the people with whom you want to share your app, and then select one of these options:

	- **Can view** allows the users you specify to run your app
	- **Can edit** allows the users you specify not only to run your app but also to create their own versions of it.

	![Text box for specifying email addresses](./media/get-started-test-drive/share-to.png)

1. Edit the text in the message box, and then select **Share**.

	The people with whom you shared your app will receive an email message that contains a link that they can select to install PowerApps and run your app.
