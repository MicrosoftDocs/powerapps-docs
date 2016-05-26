<properties
	pageTitle="Overview of the Twitter connection | Microsoft PowerApps"
	description="See the available Twitter functions, responses, and examples"
	services=""	
	suite="powerapps"
	documentationCenter="" 	
	authors="MandiOhlinger"	
	manager="erikre"	
	editor="" 
	tags="" />

<tags
ms.service="powerapps"
ms.devlang="na"
ms.topic="article"
ms.tgt_pltfrm="na"
ms.workload="na"
ms.date="05/25/2016"
ms.author="mandia"/>


# Twitter

![Twitter](./media/connection-twitter/twittericon.png)

Twitter lets you post tweets and get tweets, timeline, friends and followers from your Twitter account.

You can display this information in a text box on your app. For example, you can add an input text box, ask the user to enter in some Tweet text, and then add a button that "posts" the tweet. You can use similar methods to get a tweet or search for a tweet, and then display the text in a text box or gallery control in your app.

This topic shows the available functions. For a deep-dive on the Twitter connection, go to [Show data from Twitter](../show-twitter-data.md).

&nbsp;

[AZURE.INCLUDE [connection-requirements](../../includes/connection-requirements.md)]

## View the available functions

This connection includes the following functions:

| Function Name |  Description |
| --- | --- |
|[UserTimeline](connection-twitter.md#usertimeline) | Retrieves a collection of the most recent tweets posted by the specified user  |
|[HomeTimeline](connection-twitter.md#hometimeline) | Retrieves the most recent tweets and re-tweets posted me and my followers  |
|[SearchTweet](connection-twitter.md#searchtweet) | Retrieves a collection of relevant tweets matching a specified query  |
|[Followers](connection-twitter.md#followers) | Retrieves users following the specified user  |
|[MyFollowers](connection-twitter.md#myfollowers) | Retrieves users who are following me |
|[Following](connection-twitter.md#following) | Retrieves users who the specified user is following |
|[MyFollowing](connection-twitter.md#myfollowing) | Retrieves users that I am following |
|[User](connection-twitter.md#user) | Retrieves details about the specified user (example: user name, description, followers count, etc.) |
|[Tweet](connection-twitter.md#tweet) |Tweet |
|[OnNewTweet](connection-twitter.md#onnewtweet) |Triggers a workflow when a new tweet is posted which matches your search query  |


## UserTimeline
Get user timeline: Retrieves a collection of the most recent tweets posted by the specified user 

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|userName|string|yes|Twitter handle|
|maxResults|integer|no|Maximum number of tweets to retrieve, e.g. {maxResults:5}|

#### Output properties

| Property Name | Data Type | Required |Description |
|---|---|---|---|
|TweetText|string|Yes | |
|TweetId|string|No | |
|CreatedAt|string|No | |
|RetweetCount|integer|Yes | |
|TweetedBy|string|Yes | |
|MediaUrls|array|No | |


## HomeTimeline
Get home timeline: Retrieves the most recent tweets and re-tweets posted me and my followers 

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|maxResults|integer|no|Maximum number of tweets to retrieve, e.g. {maxResults:5}|

#### Output properties

| Property Name | Data Type | Required |Description |
|---|---|---|---|
|TweetText|string|Yes | |
|TweetId|string|No | |
|CreatedAt|string|No | |
|RetweetCount|integer|Yes | |
|TweetedBy|string|Yes | |
|MediaUrls|array|No | |


## SearchTweet
Search tweet: Retrieves a collection of relevant tweets matching a specified query 

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|searchQuery|string|yes|Query text (you may use any Twitter supported query operators: http://www.twitter.com/search)|
|maxResults|integer|no|Maximum number of tweets to retrieve, e.g. {maxResults:5}|

#### Output properties

| Property Name | Data Type | Required |Description |
|---|---|---|---|
|TweetText|string|Yes | |
|TweetId|string|No | |
|CreatedAt|string|No | |
|RetweetCount|integer|Yes | |
|TweetedBy|string|Yes | |
|MediaUrls|array|No | |


## Followers
Get followers: Retrieves users following the specified user 

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|userName|string|yes|Twitter handle of the user|
|maxResults|integer|no|Maximum number of users to retrieve, e.g. {maxResults:5}|

#### Output properties

| Property Name | Data Type | Required |Description |
|---|---|---|---|
|FullName|string|Yes | |
|Location|string|Yes | |
|Id|integer|No | |
|UserName|string|Yes | |
|FollowersCount|integer|No | |
|Description|string|Yes | |
|StatusesCount|integer|No | |
|FriendsCount|integer|No | |


## MyFollowers
Get my followers: Retrieves users who are following me 

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|maxResults|integer|no|Maximum number of users to retrieve, e.g. {maxResults:5}|

#### Output properties

| Property Name | Data Type | Required |Description |
|---|---|---|---|
|FullName|string|Yes | |
|Location|string|Yes | |
|Id|integer|No | |
|UserName|string|Yes | |
|FollowersCount|integer|No | |
|Description|string|Yes | |
|StatusesCount|integer|No | |
|FriendsCount|integer|No | |


## Following
Get following: Retrieves users who the specified user is following 

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|userName|string|yes|Twitter handle of the user|
|maxResults|integer|no|Maximum number of users to retrieve, e.g. {maxResults:5}|

#### Output properties

| Property Name | Data Type | Required |Description |
|---|---|---|---|
|FullName|string|Yes | |
|Location|string|Yes | |
|Id|integer|No | |
|UserName|string|Yes | |
|FollowersCount|integer|No | |
|Description|string|Yes | |
|StatusesCount|integer|No | |
|FriendsCount|integer|No | |


## MyFollowing
Get my following: Retrieves users that I am following 

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|maxResults|integer|no|Maximum number of users to retrieve, e.g. {maxResults:5}|

#### Output properties

| Property Name | Data Type | Required |Description |
|---|---|---|---|
|FullName|string|Yes | |
|Location|string|Yes | |
|Id|integer|No | |
|UserName|string|Yes | |
|FollowersCount|integer|No | |
|Description|string|Yes | |
|StatusesCount|integer|No | |
|FriendsCount|integer|No | |


## User
Get user: Retrieves details about the specified user (example: user name, description, followers count, etc.) 

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|userName|string|yes|Twitter handle of the user|

#### Output properties

| Property Name | Data Type | Required |Description |
|---|---|---|---|
|FullName|string|Yes | |
|Location|string|Yes | |
|Id|integer|No | |
|UserName|string|Yes | |
|FollowersCount|integer|No | |
|Description|string|Yes | |
|StatusesCount|integer|No | |
|FriendsCount|integer|No | |


## Tweet
Post a new tweet: Tweet 

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|tweetText|string|no|Text to be posted|
|body|string |no|Media to be posted|

#### Output properties
| Property Name | Data Type | Required |Description |
|---|---|---|---|
|TweetId|string|Yes | |


## OnNewTweet
When a new tweet appears: Triggers a workflow when a new tweet is posted which matches your search query 

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|searchQuery|string|yes|Query text (you may use any Twitter supported query operators: http://www.twitter.com/search)|

#### Output properties

| Property Name | Data Type | Required |Description |
|---|---|---|---|
|value|array|No | |


## Helpful links

See all the [available connections](../connections-list.md).  
Learn how to [add connections](../add-manage-connections.md) to your apps.
