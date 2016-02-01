<properties
   pageTitle="Show data from Twitter | Microsoft PowerApps"
   description="Show a timeline, user information, a list of followers, and other information from Twitter"
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

# Show data from Twitter in PowerApps #

Connect to Twitter, and then configure your app to send a tweet, search for tweets, show a timeline, or show information such as a user's name, bio, and followers.

**Prerequisites**

Learn how to [add and configure a control](add-configure-controls.md).

## Connect to Twitter ##
1.  Open PowerApps, select **Connections** on the **File** menu (near the left edge), and then select **Add connection**.

1.  In the list of connection types, select **Twitter**, select **Connect**, and then provide your credentials.

	The connection that you created appears under **My connections**.

	![Connection to Twitter](./media/show-twitter-data/twitter-connection.png)

1. On the **File** menu, select **New**, and then select **Get started** under **Start from scratch**.

	![Open a blank app](./media/show-twitter-data/blank-app.png)

1. In the lower-right corner, select **Options**, and then select **Insert your data** in the **Screen** pane.

1. Select the connection you added earlier, and then select **Add Data Source**.

	Your selection appears under **Data Sources**.

1. Close the **Screen** pane by selecting the **X** in its upper-right corner.

	![Close the Screen pane](./media/show-twitter-data/close-options.png)

## Show a timeline ##
1. Add a text gallery, and follow either of these steps:

	- To show the current user's timeline, set the **Items** property of the gallery to this formula:<br>**twitter.HomeTimeline()**

	- To show another user's timeline, set the **Items** property of the gallery to this formula:<br>
	**twitter.UserTimeline(** *UserID* **)**

	Specify a *UserID* by including a Twitter handle enclosed in double quotation marks or an equivalent value. For example, specify **"satyan"** directly in the formula, or add a text-input control named **Tweep**, specify **Tweep.Text** in the formula, and then type a Twitter handle such as **satyan** (without quotation marks) in **Tweep**.

	**Tip:** Show only the most recent tweets in a timeline (for example, the last five tweets) by specifying the maxResults argument, as these formulas show:<br>
	**twitter.HomeTimeline({maxResults:5})**<br>
	**twitter.UserTimeline(Tweep.Text, {maxResults:5})**

1. If the **Screen** pane isn't showing, select **Options** near the lower-right corner.

1. In the **Screen** pane, select **TweetText** in the **Body1** list, **TweetedBy** in the **Heading1** list, and **CreatedAt** in the **Subtitle1** list.

### Show followers ###
1. Add a text gallery, and then follow either of these steps:

	- To show the current user's followers, set the **Items** property of the gallery to this formula:<br>**twitter.MyFollowers()**

	- To show the another user's followers, set the **Items** property of the gallery to this formula:<br>
	**twitter.Followers(** *UserID* **)**

	Specify a *UserID* by including a Twitter handle enclosed in double quotation marks or an equivalent value. For example, specify **"satyan"** directly in the formula, or add an input-text control named **Tweep**, specify **Tweep.Text** in the formula, and then type a Twitter handle such as **satyan** (without quotation marks) in **Tweep**.

	**Tip:** Show only, for example, five followers by specifying the maxResults argument, as these formulas show:<br>
	**twitter.MyFollowers({maxResults:5})**<br>
	**twitter.Followers(Tweep.Text, {maxResults:5})**

1. If the **Screen** pane isn't showing, select **Options** near the lower-right corner.

1. In the **Screen** pane, select **Description** in the **Body1** list, **UserName** in the **Heading1** list, and **FullName** in the **Subtitle1** list.

### Show followed users ###

1. Add a text gallery, and then follow either of these steps:

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
Add a text box, and then set its **Text** property to one of these formulas:
- **twitter.User(** *UserID* **)!Description**
- **twitter.User(** *UserID* **)!FullName**
- **twitter.User(** *UserID* **)!Location**
- **twitter.User(** *UserID* **)!UserName**
- **twitter.User(** *UserID* **)!FollowersCount**
- **twitter.User(** *UserID* **)!FriendsCount**
- **twitter.User(** *UserID* **)!Id**
- **twitter.User(** *UserID* **)!StatusesCount**

	Specify a *UserID* by including a Twitter handle enclosed in double quotation marks or an equivalent value. For example, specify **"satyan"** directly in the formula, or add an input-text control named **Tweep**, specify **Tweep.Text** in the formula, and then type a Twitter handle such as **satyan** (without quotation marks) in **Tweep**.

### Search tweets ###
1. Add a text gallery, and set its **Items** property to this formula:<br>
**twitter.SearchTweet(** *SearchTerm* **)**

	Specify a *SearchTerm* by enclosing a term in double quotation marks or by referring to an equivalent value. For example, specify **"PowerApps"** directly in the formula, or add an input-text control named **SearchTerm**, specify **SearchTerm.Text** in the formula, and then type **PowerApps** (no quotation marks) in **SearchTerm**.

	**Tip:** Show only, for example, the first five results by specifying the maxResults argument, as this formula shows:<br>
	**twitter.SearchTweet(SearchTerm.Text, {maxResults:5})**

1. If the **Screen** pane isn't showing, select **Options** near the lower-right corner.

1. In the **Screen** pane, select **TweetText** in the **Body1** list, **TweetedBy** in the **Heading1** list, and **CreatedAt** in the **Subtitle1** list.

### Send a tweet ###
1. Add a text-input control, and then rename it **MyTweet**.

1. Add a button, and then set its **OnSelect** property to this formula:<br>
**twitter.Tweet({tweetText: MyTweet.Text})**

1. Press F5, type some text into **MyTweet**, and then select the button to tweet the text that you specified.

1. Press Esc to return to the default workspace.
