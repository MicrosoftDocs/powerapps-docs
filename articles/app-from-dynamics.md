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

Create an app for adding, updating, and deleting data about accounts and other information from Dynamics CRM Online. Connect to your account, add the connection to an app, and then configure the interface.

**Prerequisites**

- Install [PowerApps](http://aka.ms/powerappsinstall), and then open it. (Advance through the welcome screens by selecting the arrow near the lower-right corner, and then sign in by providing your credentials.)
- Get an account in Dynamics CRM Online if you don't already have one.
- Learn how to [configure a control](get-started-test-drive.md#configure-a-control) in PowerApps.

## Create a connection ##
1.  Open PowerApps, and then select **Connections** on the **File** menu (near the left edge).

	![Connections option on the File menu](./media/app-from-dynamics/file-connections.png)

1.  Select **Add connection**.

	![Connections option on the File menu](./media/powerapps-api-functions/add-connection.png)
1.  In the list of connection types, select any of these options, and then select **Connect**:

	- **Office 365 Users**
	- **Office 365 Outlook**
	- **Twitter**
	- **Microsoft Translator**

1. Provide your credentials for the connection that you selected.

	The connection that you created appears under **My connections**.

	![Connections option on the File menu](./media/powerapps-api-functions/my-connections.png)

1. On the **File** menu, select **New**.

	![New option on the File menu](./media/powerapps-api-functions/file-new.png)

1. Under **Start from scratch**, select **Get started.**

	![Open a blank app](./media/powerapps-api-functions/blank-app.png)

1. In the lower-right corner, select **Options**.

	![Open the Screen pane](./media/powerapps-api-functions/open-options.png)

1. In the **Screen** pane, select **Insert your data**, select the connection you want, and then select **Add Data Source**.

	Your selection appears under **Data Sources**.

1. Close the **Screen** pane by selecting the **X** in its upper-right corner.

	![Close the Screen pane](./media/powerapps-api-functions/close-options.png)

## Office 365 ##
Connect to Office 365 Users or Office 365 Outlook, and then perform these tasks:

- Show information about the current user
- Show information about another user
- Show the direct reports of another user
- Search for users
- Send mail

### Show information about the current user ###
1. If you haven't already, [create a connection](powerapps-api-functions.md#create-a-connection) to **Office 365 Users**.

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

### Show information about another user ###
1. If you haven't already, [create a connection](powerapps-api-functions.md#create-a-connection) to **Office 365 Users**.

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

### Show the direct reports of another user ###
1. If you haven't already, [create a connection](powerapps-api-functions.md#create-a-connection) to **Office 365 Users**.

1. On the **Insert** tab, select **Text**, and then select **Input text**.

1. Rename the text-input control **InfoAbout** and then, in it, type the email address of someone in your organization.

1. On the **Insert** tab, select **Gallery**, and then select the text gallery in **Portrait** orientation.

1. Set the gallery's **Items** property to this formula:

	**office365users.DirectReports(InfoAbout.Text)**

	The gallery shows information about the direct reports of the user that you specified.

1. (optional) With the gallery still selected, select **Options** in the lower-right corner, and then select **Mail** in the **Body1** list, **DisplayName** in the **Heading1** list, and **JobTitle** in the **Subtitle1** list.

### Search for users ###
1. If you haven't already, [create a connection](powerapps-api-functions.md#create-a-connection) to **Office 365 Users**.

1. On the **Insert** tab, select **Text**, and then select **Input text**.

1. Rename the text-input control **SearchTerm**, and then type a search term in that control.

1. On the **Insert** tab, select **Gallery**, and then select the text gallery in **Portrait** orientation.

1. Set the gallery's **Items** property to this formula:

	**office365users.SearchUser({searchTerm: SearchTerm.Text})**

	The gallery shows users whose information contains the term that you specified.

1. (optional) In the lower-right corner, select **Options**, and then select **Mail** in the **Body1** list, **DisplayName** in the **Heading1** list, and **JobTitle** in the **Subtitle1** list.

### Send email ###
For this function, you must specify the first three arguments, but all other arguments are optional:
<br>**office365.SendEmail(Subject, Body, To[, Attachments, From, CC, BCC, Importance, IsHtml])**

1. If you haven't already, [create a connection](powerapps-api-functions.md#create-a-connection) to **Office 365 Outlook**.

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

## Twitter ##
Connect to Twitter, and then perform these tasks:

- Show a timeline
- Show followers
- Show followed users
- Show information about a user, such as full name, bio, and location
- Search tweets
- Send a tweet

### Show a timeline ###
1. If you haven't already, [create a connection](powerapps-api-functions.md#create-a-connection) to **Twitter**.

1. On the **Insert** tab, select **Gallery**, and then select the text gallery in **Portrait** orientation.

1. Do one of the following:

	- To show the current user's timeline, set the **Items** property of the gallery to this formula:<br>**twitter.HomeTimeline()**

	- To show another user's timeline, set the **Items** property of the gallery to this formula:<br>
	**twitter.UserTimeline(** *UserID* **)**

	Specify a *UserID* by including a Twitter handle enclosed in double quotation marks or an equivalent value. For example, specify **"satyan"** directly in the formula, or add an input-text control named **Tweep**, specify **Tweep.Text** in the formula, and then type a Twitter handle, such as **satyan** (without quotation marks), in **Tweep**.

	**Tip:** Show only the most recent tweets in a timeline (for example, the last five tweets) by specifying the maxResults argument, as these formulas show:<br>
	**twitter.HomeTimeline({maxResults:5})**<br>
	**twitter.UserTimeline(Tweep.Text, {maxResults:5})**

1. If the **Screen** pane isn't showing, select **Options** near the lower-right corner.

1. In the **Screen** pane, select **TweetText** in the **Body1** list, **TweetedBy** in the **Heading1** list, and **CreatedAt** in the **Subtitle1** list.

### Show followers ###
1. If you haven't already, [create a connection](powerapps-api-functions.md#create-a-connection) to **Twitter**.

1. On the **Insert** tab, select **Gallery**, and then select the text gallery in **Portrait** orientation.

1. Do one of the following:

	- To show the current user's followers, set the **Items** property of the gallery to this formula:<br>**twitter.MyFollowers()**

	- To show the another user's followers, set the **Items** property of the gallery to this formula:<br>
	**twitter.Followers(** *UserID* **)**

	Specify a *UserID* by including a Twitter handle enclosed in double quotation marks or an equivalent value. For example, specify **"satyan"** directly in the formula, or add an input-text control named **Tweep**, specify **Tweep.Text** in the formula, and then type a Twitter handle, such as **satyan** (without quotation marks), in **Tweep**.

	**Tip:** Show only, for example, five followers by specifying the maxResults argument, as these formulas show:<br>
	**twitter.MyFollowers({maxResults:5})**<br>
	**twitter.Followers(Tweep.Text, {maxResults:5})**

1. If the **Screen** pane isn't showing, select **Options** near the lower-right corner.

1. In the **Screen** pane, select **Description** in the **Body1** list, **UserName** in the **Heading1** list, and **FullName** in the **Subtitle1** list.

### Show followed users ###

1. If you haven't already, [create a connection](powerapps-api-functions.md#create-a-connection) to **Twitter**.

1. On the **Insert** tab, select **Gallery**, and then select the text gallery in **Portrait** orientation.

1. Do one of the following:

	- To show which users the current user is following, set the **Items** property of the gallery to this formula:<br>**twitter.MyFollowing()**

	- To show which users another user is following, set the **Items** property of the gallery to this formula:<br>
	**twitter.Following(** *UserID* **)**

	Specify a *UserID* by including a Twitter handle enclosed in double quotation marks or an equivalent value. For example, specify **"satyan"** directly in the formula, or add an input-text control named **Tweep**, specify **Tweep.Text** in the formula, and then type a Twitter handle, such as **satyan** (without quotation marks), in **Tweep**.

	**Tip:** Show only, for example, five followed users by specifying the maxResults argument, as these formulas show:<br>
	**twitter.MyFollowing({maxResults:5})**<br>
	**twitter.Following(Tweep.Text, {maxResults:5})**

1. If the **Screen** pane isn't showing, select **Options** near the lower-right corner.

1. In the **Screen** pane, select **Description** in the **Body1** list, **UserName** in the **Heading1** list, and **FullName** in the **Subtitle1** list.

### Show information about a user ###
1. If you haven't already, [create a connection](powerapps-api-functions.md#create-a-connection) to **Twitter**.

1. On the **Insert** tab, select **Text box**, and then set its **Text** property to one of these formulas:
	- **twitter.User(** *UserID* **)!Description**
	- **twitter.User(** *UserID* **)!FullName**
	- **twitter.User(** *UserID* **)!Location**
	- **twitter.User(** *UserID* **)!UserName**
	- **twitter.User(** *UserID* **)!FollowersCount**
	- **twitter.User(** *UserID* **)!FriendsCount**
	- **twitter.User(** *UserID* **)!Id**
	- **twitter.User(** *UserID* **)!StatusesCount**

	Specify a *UserID* by including a Twitter handle enclosed in double quotation marks or an equivalent value. For example, specify **"satyan"** directly in the formula, or add an input-text control named **Tweep**, specify **Tweep.Text** in the formula, and then type a Twitter handle, such as **satyan** (without quotation marks), in **Tweep**.

### Search tweets ###
1. If you haven't already, [create a connection](powerapps-api-functions.md#create-a-connection) to **Twitter**.

1. On the **Insert** tab, select **Gallery**, and then select the text gallery in **Portrait** orientation.

1. Set the **Items** property of the gallery to this formula:<br>
**twitter.SearchTweet(** *SearchTerm* **)**

	Specify a *SearchTerm* by enclosing a term in double quotation marks or by referring to an equivalent value. For example, specify **"PowerApps"** directly in the formula, or add an input-text control named **SearchTerm**, specify **SearchTerm.Text** in the formula, and then type **PowerApps** (no quotation marks) in **SearchTerm**.

	**Tip:** Show only, for example, the first five results by specifying the maxResults argument, as this formula shows:<br>
	**twitter.SearchTweet(SearchTerm.Text, {maxResults:5})**

1. If the **Screen** pane isn't showing, select **Options** near the lower-right corner.

1. In the **Screen** pane, select **TweetText** in the **Body1** list, **TweetedBy** in the **Heading1** list, and **CreatedAt** in the **Subtitle1** list.

### Send a tweet ###
1. If you haven't already, [create a connection](powerapps-api-functions.md#create-a-connection) to **Twitter**.

1. On the **Insert** tab, select **Text**, select **Input text**, and then rename the new control **MyTweet**.

1. On the **Insert** tab, select **Button**, and then set the **OnSelect** property of the button to this formula:<br>
**twitter.Tweet({tweetText: MyTweet.Text})**

1. Press F5, type some text into **MyTweet**, and then select the button to tweet the text that you specified.

1. Press Esc to return to the default workspace.

## Microsoft Translator ##

### Translate text ###
1. If you haven't already, [create a connection](powerapps-api-functions.md#create-a-connection) to **Microsoft Translator**.

1. On the **Insert** tab, select **Text**, and then select **Input text**.

1. Rename the input-text control **Source**.

1. On the **Insert** tab, select **Controls**, select **Drop-down**, and then move the drop-down list below the **Source** box.

1. Set the **Items** property of the drop-down list to this formula:<br>
**microsofttranslator.Languages()**

1. Rename the drop-down list **TargetLang**.

1. On the **Insert** tab, select **Text box**, move it below the drop-down list, and set its **Text** property to this formula:
<br>**microsofttranslator.Translate(Source.Text, TargetLang.Selected.Value)**

1. Type text into **Source**, and select a language in **TargetLang**.

	The text box shows the text that you specified in the language that you specified.

### Speak translated text ###
1. If you haven't already, follow the steps in the previous procedure for translating text.

1. Set the **Items** property of the **TargetLang** drop-down list to this formula:<br>
**microsofttranslator.SpeechLanguages()**

1. Rename the text box (not the **Source** box) to **Target**.

1. On the **Insert** tab, select **Media**, and then select **Audio**.

1. Set the **Media** property of the audio control to this formula:<br>
**microsofttranslator.TextToSpeech(Target.Text, TargetLang.Selected.Value)**

1. Press F5, type text into **Source**, select an option in **TargetLang**, and then select the play button in the audio control.

	The app plays an audio version of the text that you specified in the language that you specified.

1. Press Esc to return to the default workspace.

### Detect the source language ###
1. If you haven't already, [create a connection](powerapps-api-functions.md#create-a-connection) to **Microsoft Translator**.

1. On the **Insert** tab, select **Text**, select **Input Text**, and name the input-text control **Source**.

1. On the **Insert** tab, select **Text box**, and then move the text box under **Source**.

1. Set the **Text** property of the text box to this formula:
<br>**microsofttranslator.Detect(Source.Text)**

1. Type text into **Source**.

	The text box indicates the language of the text that you typed. For example, the text box shows **fr** (for French) if you type **bonjour** or **it** (for Italian) if you type **ciao**.
