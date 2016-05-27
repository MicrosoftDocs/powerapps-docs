<properties
   pageTitle="Show data from Twitter | Microsoft PowerApps"
   description="Show a timeline, user information, a list of followers, and other information from Twitter"
   services=""
   suite="powerapps"
   documentationCenter="na"
   authors="aftowen"
   manager="erikre"
   editor=""
   tags=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="05/26/2016"
   ms.author="anneta"/>

# Show data from Twitter in PowerApps

Connect to Twitter, and then configure your app to send a tweet, search for tweets, show a timeline, or show information such as a user's name, bio, and followers.

**Prerequisites**

Know how to [add and configure a control](add-configure-controls.md).

## Connect to Twitter
1.  Open PowerApps, select **New**, and then create a **Blank app**. Choose phone or tablet layout. Tablet layout gives you more workspace:  

	![Open a blank app](./media/show-twitter-data/blank-app.png)

2. In the lower-right corner, select **Options**, and then select **Add data source**. 

3. Select **Add connection**, and then select **Twitter**:  

	![Connect to Twitter](./media/show-twitter-data/addconnection.png)

	![Connect to Twitter](./media/show-twitter-data/add-twitter.png)

4. Select **Connect**, enter your Twitter sign in credentials, and then select **Authorize app**.

5. Select **Add Data Source**. Your connection appears under **Data sources**:  
	![Close the Options pane](./media/show-twitter-data/twitterdatasource.png)

6. Close the **Screen** pane by selecting the **X** in its upper-right corner:  

	![Close the Options pane](./media/show-twitter-data/close-options.png)

The Twitter connection has been created, and added to your app. Now, it's ready to be used.

## Show a timeline
1. On the **Insert** menu, select **Gallery**, and add any of the **With text** galleries.
2. Let's show some timelines:  

	- To show the current user's timeline, set the **[Items](controls/properties-core.md)** property of the gallery to the following formulas:
	
		`Twitter.HomeTimeline().TweetText`  
		`Twitter.HomeTimeline({maxResults:3}).TweetText`  

	- To show another user's timeline, set the **[Items](controls/properties-core.md)** property of the gallery to the following formula:  

		`Twitter.UserTimeline( *TwitterHandle* ).TweetText`

		Enter a Twitter handle in double quotation marks or an equivalent value. For example, enter `"satyanadella"` or `"powerapps"` directly in the formula expression. 

	- Add a text input control named **Tweep**, and set its Default property to `Tweep.Text`. In the Tweep text box, type in a Twitter handle such as `satyanadella` (without quotation marks and without the @ symbol).
	
		In the gallery control, set the Items property to the following formula:  

		`Twitter.UserTimeline(Tweep.Text, {maxResults:5}).TweetText`

		The gallery control automatically shows the tweets of the Twitter handler you type in.

	**TIP** Some of these formulas use the **maxResults** argument to show the *x* number of most recent tweets in a timeline. 

3. Set the gallery's Items property to `Twitter.HomeTimeline()`. With the gallery selected, select **Options** near the lower-right corner. Select **TweetText** in the first list, select **TweetedBy** in the second list, and select **CreatedAt** in the third list.

	The gallery now shows the values of the properties you chose. 

## Show followers
1. Using a **With text** gallery, let's show some followers:  

	- To show the current user's followers, set the **[Items](controls/properties-core.md)** property of the gallery to the following formula:  
	
		`Twitter.MyFollowers()`  
		`Twitter.MyFollowers({maxResults:3})`

	- To show the another user's followers, set the **[Items](controls/properties-core.md)** property of the gallery to the following formula:  
	
		`Twitter.Followers( *TwitterHandle* )`

		Enter a Twitter handle in double quotation marks or an equivalent value. For example, enter `"satyanadella"` or `"powerapps"` directly in the formula expression. 

	- Add a text input control named **Tweep**, and set its Default property to `Tweep.Text`. In the Tweep text box, type in a Twitter handle such as `satyanadella` (without quotation marks and without the @ symbol).
	
		In the gallery control, set the Items property to the following formula:  

		`Twitter.Followers(Tweep.Text, {maxResults:5})`

		The gallery control automatically shows who is following the Twitter handle you type in.

	**TIP** Some of these formulas use the **maxResults** argument to show the *x* number of most recent tweets in a timeline. 

2. Set the gallery's Items property to `Twitter.MyFollowers()`. With the gallery selected, select **Options** near the lower-right corner. Select **UserName** in the second list, and select **FullName** in the third list.

	The gallery now shows the values of the properties you chose. 

## Show followed users

1. Using a **With text** gallery, let's show some followed users:  

	- To show which users the current user is following, set the **[Items](controls/properties-core.md)** property of the gallery to the following formula:  
	
		`Twitter.MyFollowing()`  
		`Twitter.MyFollowing({maxResults:3})`

	- To show which users another user is following, set the **[Items](controls/properties-core.md)** property of the gallery to to the following formula:

		`Twitter.Following( *TwitterHandle* )`

		Enter a Twitter handle in double quotation marks or an equivalent value. For example, enter `"satyanadella"` or `"powerapps"` directly in the formula expression. 

	- Add a text input control named **Tweep**, and set its Default property to `Tweep.Text`. In the Tweep text box, type in a Twitter handle such as `satyanadella` (without quotation marks and without the @ symbol).
	
		In the gallery control, set the Items property to the following formula:  

		`Twitter.Following(Tweep.Text, {maxResults:5})`

		The gallery control automatically shows the other handles you are following.

2. With the gallery selected, select **Options** near the lower-right corner. Select **Description** in the **Body1** list, **UserName** in the **Heading1** list, and **FullName** in the **Subtitle1** list.

	The gallery now shows the values of the properties you chose. 

## Show information about a user
Add a text box, and then set its **[Text](controls/properties-core.md)** property to one of these formulas:  

- `twitter.User( *TwitterHandle* ).Description`
- `twitter.User( *TwitterHandle* ).FullName`
- `twitter.User( *TwitterHandle* ).Location`
- `twitter.User( *TwitterHandle* ).UserName`
- `twitter.User( *TwitterHandle* ).FollowersCount`
- `twitter.User( *TwitterHandle* ).FriendsCount`
- `twitter.User( *TwitterHandle* ).Id`
- `twitter.User( *TwitterHandle* ).StatusesCount`

Enter a Twitter handle in double quotation marks or an equivalent value. For example, enter `"satyanadella"` or `"powerapps"` directly in the formula expression. 

Or, you can use an input text control to type in a Twitter handle, just as we have throughout this topic.

## Search tweets
1. Using a **With text** gallery, set its **[Items](controls/properties-core.md)** property to the following formula:  

	`Twitter.SearchTweet( *SearchTerm* ).TweetText`

	Enter a *SearchTerm* in double quotation marks or by referring to an equivalent value. For example, enter `"PowerApps"` or `"microsoft"` directly in the formula.

	Or, you can use an input text control to type in a Twitter handle, just as we have throughout this topic.

	**TIP** Show the first five results by using maxResults:  

	`Twitter.SearchTweet(SearchTerm.Text, {maxResults:5}).TweetText`

2. Set the gallery's Items property to `Twitter.SearchTweet(SearchTerm.Text, {maxResults:5})`. With the gallery selected, select **Options** near the lower-right corner. Select **TweetText** in the first list, **TweetedBy** in the second list, and **CreatedAt** in the third list.

	The gallery now shows the values of the properties you chose. 

## Send a tweet ##
1. Add a text input control, and then rename it **MyTweet**.

2. Add a button, and then set its **[OnSelect](controls/properties-core.md)** property to the following formula:  
	`Twitter.Tweet({tweetText: MyTweet.Text})`

3. Press F5, or select the Preview button (![](./media/show-twitter-data/preview.png)). Type some text into **MyTweet**, and then select the button to tweet the text that you entered.

4. Press Esc to return to the default workspace.

