<properties
   pageTitle="Show data from Office 365 | Microsoft PowerApps"
   description="Show data about users (such as name, job title, and department) from Office 365 Users, and send mail from Office 365 Outlook."
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
   ms.date="01/15/2016"
   ms.author="anneta"/>

# Show data from Office 365 in PowerApps #

Connect to Office 365, and then configure your app to perform these tasks:

- Show information about the current user
- Show information about another user
- Show the direct reports of another user
- Search for users
- Send mail

**Prerequisites**

- Install [PowerApps](http://aka.ms/powerappsinstall), and then open it. (Advance through the welcome screens by selecting the arrow near the lower-right corner, and then sign in by providing your credentials.)
- Learn how to [configure a control](get-started-test-drive.md#configure-a-control) in PowerApps.

## Connect to Office 365 ##
1.  Open PowerApps, and then select **Connections** on the **File** menu (near the left edge), and then select **Add connection**.

1.  In the list of connection types, select **Office 365 Users** or **Office 365 Outlook**, select **Connect**, and then provide your credentials.

	The connection that you created appears under **My connections**.

	![Connections to Office 365 Users and Office 365 Outlook](./media/app-from-office/office-connections.png)

1. On the **File** menu, select **New**, and then select **Get started** under **Start from scratch**.

	![Open a blank app](./media/powerapps-api-functions/blank-app.png)

1. In the lower-right corner, select **Options**, and then select **Insert your data** in the **Screen** pane.

1. Select the connection you added earlier, and then select **Add Data Source**.

	Your selection appears under **Data Sources**.

1. Close the **Screen** pane by selecting the **X** in its upper-right corner.

	![Close the Screen pane](./media/powerapps-api-functions/close-options.png)

## Show information about the current user ##
1. If you haven't already, create a connection to **Office 365 Users** as described earlier in this topic.

1. On the **Insert** tab, select **Text box**, and then set the **Text** property of the text box to any of these formulas:

	- **office365users.MyProfile().Department**
	- **office365users.MyProfile().DisplayName**
	- **office365users.MyProfile().GivenName**
	- **office365users.MyProfile().Id**
	- **office365users.MyProfile().JobTitle**
	- **office365users.MyProfile().Mail**
	- **office365users.MyProfile().MailNickname**
	- **office365users.MyProfile().Surname**
	- **office365users.MyProfile().TelephoneNumber**
	- **office365users.MyProfile().UserPrincipalName**
	- **office365users.MyProfile().AccountEnabled**

The text box shows the information that you specified about the current user.

## Show information about another user ##
1. If you haven't already, create a connection to **Office 365 Users** as described earlier in this topic.

1. On the **Insert** tab, select **Text**, and then select **Input text**.

1. Rename the text-input control **InfoAbout** and, in it, type the name of a user in your organization.

1. On the **Insert** tab, select **Text box**, and then set the **Text** property of the text box to any of these formulas:

	- To show information about another user:<br>
		- **office365users.UserProfile(InfoAbout.Text).Department**
		- **office365users.UserProfile(InfoAbout.Text).DisplayName**
		- **office365users.UserProfile(InfoAbout.Text).GivenName**
		- **office365users.UserProfile(InfoAbout.Text).Id**
		- **office365users.UserProfile(InfoAbout.Text).JobTitle**
		- **office365users.UserProfile(InfoAbout.Text).Mail**
		- **office365users.UserProfile(InfoAbout.Text).MailNickname**
		- **office365users.UserProfile(InfoAbout.Text).Surname**
		- **office365users.UserProfile(InfoAbout.Text).TelephoneNumber**
		- **office365users.UserProfile(InfoAbout.Text).UserPrincipalName**
		- **office365users.UserProfile(InfoAbout.Text).AccountEnabled**

	- To show information about another user's manager:<br>
		- **office365users.Manager(InfoAbout.Text).Department**
		- **office365users.Manager(InfoAbout.Text).DisplayName**
		- **office365users.Manager(InfoAbout.Text).GivenName**
		- **office365users.Manager(InfoAbout.Text).Id**
		- **office365users.Manager(InfoAbout.Text).JobTitle**
		- **office365users.Manager(InfoAbout.Text).Mail**
		- **office365users.Manager(InfoAbout.Text).MailNickname**
		- **office365users.Manager(InfoAbout.Text).Surname**
		- **office365users.Manager(InfoAbout.Text).TelephoneNumber**
		- **office365users.Manager(InfoAbout.Text).UserPrincipalName**
		- **office365users.Manager(InfoAbout.Text).AccountEnabled**

	The text box shows the information that you specified about the user whom you specified or that user's manager.

## Show the direct reports of another user ##
1. If you haven't already, create a connection to **Office 365 Users** as described earlier in this topic.

1. On the **Insert** tab, select **Text**, and then select **Input text**.

1. Rename the text-input control **InfoAbout** and then, in it, type the email address of someone in your organization.

1. On the **Insert** tab, select **Gallery**, and then select the text gallery in **Portrait** orientation.

1. Set the gallery's **Items** property to this formula:

	**office365users.DirectReports(InfoAbout.Text)**

	The gallery shows information about the direct reports of the user that you specified.

1. (optional) With the gallery still selected, select **Options** in the lower-right corner, and then select **Mail** in the **Body1** list, **DisplayName** in the **Heading1** list, and **JobTitle** in the **Subtitle1** list.

## Search for users ##
1. If you haven't already, create a connection to **Office 365 Users** as described earlier in this topic.

1. On the **Insert** tab, select **Text**, and then select **Input text**.

1. Rename the text-input control **SearchTerm**, and then type a search term in that control.

1. On the **Insert** tab, select **Gallery**, and then select the text gallery in **Portrait** orientation.

1. Set the gallery's **Items** property to this formula:

	**office365users.SearchUser({searchTerm: SearchTerm.Text})**

	The gallery shows users whose information contains the term that you specified.

1. (optional) In the lower-right corner, select **Options**, and then select **Mail** in the **Body1** list, **DisplayName** in the **Heading1** list, and **JobTitle** in the **Subtitle1** list.

## Send email ##
For this function, you must specify the first three arguments, but all other arguments are optional:
<br>**office365.SendEmail(Subject, Body, To[, Attachments, From, CC, BCC, Importance, IsHtml])**

1. If you haven't already, create a connection to **Office 365 Outlook** as described earlier in this topic.

1. On the **Insert** tab, select **Text**, select **Input text**, and then repeat that process twice so that the screen contains three input-text controls.

1. Arrange the controls in a column, and give them these names:

	- **inputTo**
	- **inputSubject**
	- **inputBody**

1. On the **Insert** tab, select **Button**, and set the button's **OnSelect** property to this formula:<br>
**office365.SendEmail(inputSubject.text, inputBody.text, inputTo.text)**

1. Move the button so that it appears under all the other controls, and set its **Text** property to show **Send email**.

1. Press F5, type a valid email address in **inputTo**, and type whatever you want in the other two input-text controls.

1. Select **Send email** to send the message, and then press Esc to return to the default workspace.
