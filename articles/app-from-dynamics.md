<properties
   pageTitle="Create an app to manage data from Dynamics CRM Online | Microsoft PowerApps"
   description="Create an app to manage data, such as account information, from Dynamics CRM Online"
   services=""
   suite="powerapps"
   documentationCenter="na"
   authors="aftowen"
   manager="dwrede"
   editor=""
   tags=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="01/26/2016"
   ms.author="anneta"/>

# Create an app to manage data from Dynamics CRM Online #

Create an app for adding, updating, and deleting data about your customers and other information in Dynamics CRM Online. Connect to your account, add the connection to an app, and then specify which data you want to show.

**Prerequisites**

Install [PowerApps](http://aka.ms/powerappsinstall) on a tablet, a laptop, or a desktop computer that's running Windows, and then open PowerApps. If you haven't signed in before, advance through the welcome screens by selecting the arrow near the lower-right corner, and then provide your credentials.

## Create an app ##
1. On the **File** menu, select **New**, and then select **Get started** under **Start from your data**.

1. If you haven't already connected from PowerApps to your Dynamics CRM Online account, perform the following steps:

	1. Select **Available connections**, select **Dynamics CRM Online**.
	1. Select **Connect**, and then provide your credentials.

1. Under **Select a data set**, select the appropriate option for this app.

1. Under **Select a table**, select the appropriate option for this app (such as **Accounts**), and then select **Connect**.

	The app is created with a default interface, which includes a screen for browsing data (as this graphic shows), a screen for showing details, and a screen for creating and editing data.

	![App with default interface](./media/app-from-dynamics/default-app.png)

1. In the **Layout** tab of the **Quick tools** pane, select a layout (such as that highlights the data that you want to show.

	For example, select a layout that contains a heading, a subtitle, and a body element.

	![Choose a layout](./media/app-from-dynamics/choose-layout.png)

1. In the **Content** tab of the **Quick tools** pane, select the data that you want to show in each element. For example:

	- In the **Body1** list, select **websiteurl**.
	- In the **Heading1** list, select **accountnumber**.
	- In the **Subtitle1** list, select **name**.

	The browse screen of the app reflects your changes.

	![Specify data on the Content tab](./media/app-from-dynamics/specify-data.png)

1. Select any item in the list except the first one, and then copy and paste this formula into the formula bar, which is to the right of the **fx** button:

	**Sort(If(IsBlank(TextSearchBox1!Text), Accounts, Filter(Accounts, TextSearchBox1!Text in Text(name))), name, If(SortDescending1, Descending, Ascending))**

	The data is sorted in ascending order by the names of the accounts.

	![Data sorted in ascending order by name](./media/app-from-dynamics/sort-ascending.png)

## Test the app ##
1. Press F5, and then select the sort icon multiple times.

	![Sort icon](./media/app-from-dynamics/sort-button.png)

 	The data is sorted in ascending or descending order by name, depending on how many times you select the sort button.

1. Type part or all of the name of an account.

	The screen shows only those accounts for which the name contains the text that you type, regardless of case.

	![Filter example](./media/app-from-dynamics/filter-example.png)

1. In the upper-right corner, select the plus icon.

	A screen appears in which you can specify a new account.

	- To save your changes, select the checkmark in the upper-right corner.
	- To cancel your changes and return to the browse screen, select the close icon in the upper-left corner.

1. In the browse screen, select the arrow next to any account.

	The details screen shows more information about that account.

1. Select the pencil icon in the upper-right corner of the details screen.

1. In the edit screen, modify the data in one or more fields, and then save your changes by selecting the checkmark in the upper-right corner.

## Next steps ##
- Customize the default app by performing one or more of these tasks:
	- [add and configure controls](get-started-test-drive.md#configure-a-control)
	- [add a screen](add-screen-context-variables.md)
	- [build a formula](formula-reference.md)
- [Share the app](share-app.md) with others in your organization
