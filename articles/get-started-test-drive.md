<properties
	pageTitle="Create an app from a template in PowerApps"
	description="Create an app automatically based on one of several templates for a variety of scenarios. Explore how the app works by default, and then customize the app to better fit the way you work."
	services="powerapps"
	authors="AFTOwen"
 />

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="hero-article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="10/20/2015"
   ms.author="anneta"/>
# Create an app from a template
Create an app automatically based on one of several templates for a variety of scenarios. Explore how the app works by default, customize it to better fit the way you work, and then publish it.

[What is PowerApps?](http://www.kratosapps.com/tutorials)

**Prerequisites**

In addition to signing up for and installing PowerApps, you'll also need an account, such as DropBox or OneDrive, for storing sample data in the cloud.

## Open an app template ##
1. Open PowerApps, and then click **Connections** in the left naviation bar.

	![The Connections option in the left navigation bar](./media/get-started-test-drive/file-connections.jpg)

1. Click **Available Connections**, click **Dropbox** or another cloud-storage account, and then click **Connect**.

	![Option to add Dropbox as a data connection](./media/get-started-test-drive/add-dropbox.jpg)

1. Provide your credentials, and then click **Sign in**.

1. Click **New** in the left navigation bar.

	![The New option in the left navigation bar](./media/get-started-test-drive/file-new.jpg)

1. Leave the default option to create a phone app.

	![The options buttons for creating a tablet or phone app](./media/get-started-test-drive/phone-app.jpg)

1. Under **Start from Template**, click **Get started**.

	![Open an app template](./media/get-started-test-drive/open-template.jpg)

2. Click **Event SignUp**, and then click **Choose**.

	The **VolunteerDetailsScreen** of your app appears.

	![VolunteerDetailsScreen with default information](./media/get-started-test-drive/volunteer-default.jpg)

## Explore the app's default appearance and behavior ##
App templates open in the default workspace, where you'll spend most of your time customizing a template or creating an app from scratch. Before you make changes, you'll explore how the app works in **Preview**.

**Tip:** Design and develop apps in the default workspace, but test them in **Preview** before you share them with others.

1. In the left navigation bar, click the thumbnail for the **VolunteerDetailsScreen**.

	![Thumbnail for the VolunteerDetails screen](./media/get-started-test-drive/vdetails-thumbnail.jpg)

	By default, your information appears in the text boxes for name and address. You can change that information if you want.

1. Press F5 (or click the right arrow in the upper-right corner) to open **Preview**.

	![Button to open Preview](./media/get-started-test-drive/preview-button.jpg)

1. Click a t-shirt size, and then click **Next**.

	![Options for specifying a t-shirt size and a Next button](./media/get-started-test-drive/tshirt-size.jpg)

	The **Schedule** screen appears with columns for days, timeslots, and names of volunteers.
1. Click a **Sign up** button to schedule yourself (or a fictional volunteer) for a timeslot.

	![Button for signing up a volunteer for a particular timeslot](./media/get-started-test-drive/signup-button.jpg)

	**Note:** If you click a **Sign up** button, the other **Sign up** button for the same timeslot stops being available.

1. (optional) Remove yourself or the volunteer from a timeslot by clicking the "X" icon to the right of the volunteer's name.

1. Return to the default workspace by pressing Esc (or by clicking the "X" icon in the upper-right corner).

1. (optional) Verify that the data in the cloud reflects your changes.

## Configure a control ##
As you customize the interface of an app or develop one from scratch, you'll add and configure elements that show text, images, and other information. To configure how an element appears or what it does, you first click it so that a thick, gray selection box appears around it.

**Important:** If you click another element or a blank area of the screen, that element or screen becomes selected, and you can no longer configure the first element.

When an element is selected, you can configure it in these ways:

- Change it directly (for example, by moving it).
- Click a tab on the ribbon near the top of the screen, and then click an option on that tab.
- Click an option in the properties list, and then type a value in the Function Bar. These elements appear near the top of the screen and are separated by an equals sign and the function button. In this example, the **Items** property appears in the properties list, and the value of that property (**ScheduleItems**) appears in the Function Bar.

	![Properties list and Function Bar](./media/get-started-test-drive/properties-list.jpg)

If you can't find a property on the ribbon, find it in the properties list, which shows all properties alphabetically.

1. Near the top of the screen, click **PowerApps at OneWeek** to select that label.

	![A label surrounded by a selection box](./media/get-started-test-drive/selected-label.jpg)

1. Resize the label by dragging the white triangle in the lower-right corner of the selection box.

	![Resizing a control](./media/get-started-test-drive/resize-label.jpg)

1. Move the label to the right side of the screen by dragging the selection box itself (not a triangle or square in the selection box).

1. With the label still selected, rename it by clicking **Label11_7** on the **Home** tab and then typing **Banner**.

	![Renaming a control](./media/get-started-test-drive/rename-label.jpg)

	**Note:** As you develop or customize an app, you'll configure some controls to reference other controls. For example, you'll probably configure a button or other control to open one screen from another. That configuration will be much easier if the screens have names that are easier to remember than **Screen1**, **Screen2**, and so on.

1. With the label still selected, click **Text** in the properties list, and then type **Today()** in the Function Bar.

	The label shows the current date.

1. Change the text in the label by triple-clicking it and then typing in anything you want.

## Save and share your app ##
After you finish developing and testing your app, you share it with other people by saving it to the portal and then sending mail that your app is available. You specify which people can run your app or even customize it to create their own versions.

1. On the **File** menu, click **App Settings**.

	![The App Settings option on the File menu](./media/get-started-test-drive/file-settings.jpg)

2. Update any of these settings.

	- the name of your app

		![Option to rename the app](./media/get-started-test-drive/rename-app.jpg)

	- the color of your app's tile

		![Color options for your app's time](./media/get-started-test-drive/tile-color.jpg)

	- the image on your app's tile

		![Import an image to appear on your app's tile](./media/get-started-test-drive/tile-image.jpg)

	- the screen size and orientation of your app

		![Aspect-ratio options, such as 3:2 and 4:3](./media/get-started-test-drive/aspect-ratio.jpg)

2. On the **File** menu, click **Save As**.

3. Under **Save As**, leave the default value of **PowerApps**, and then click **Save**.

	![Save an app to PowerApps](./media/get-started-test-drive/save-powerapps.jpg)

6. On the **File** menu, click **Share**.

	An email template appears.

1. In the **To** text box, type the email addresses of the people with whom you want to share your app.

	![Text box for specifying email addresses](./media/get-started-test-drive/share-to.jpg)

1. In the drop-down list, click **Can View** to allow users to run your app, or click **Can edit** to allow users to run your app and create their own versions of it.

	![Drop-down list for specifying permissions on an app you share](./media/get-started-test-drive/share-level.jpg)

1. Edit the text in the **Subject** and **Message** text boxes, and then click **Share**.

	The people with whom you shared your app will receive an email message that contains a link they can click to install PowerApps and run your app.
