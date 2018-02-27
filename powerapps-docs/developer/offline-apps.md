
---
title: Develop offline-capable apps | Microsoft Docs
description: Develop offline-capable apps so your users are productive whether they are online or offline.
services: ''
suite: powerapps
documentationcenter: na
author: mgblythe
manager: anneta
editor: ''
tags: ''

ms.service: powerapps
ms.devlang: na
ms.topic: article
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 05/09/2017
ms.author: mblythe

---
# Develop offline-capable apps with PowerApps
One of the most common scenarios you face as a mobile app developer is enabling your users to be productive when there is limited connectivity or no connectivity at all. PowerApps has a set of features and behaviors that help you to develop offline-capable apps. You can:

* Launch the PowerApps mobile app when offline.
* Run apps you develop when offline.
* Determine when an app is offline, online, or in a metered connection by using the [Connection](../maker/functions/signals.md#connection) signal object.
* Use [collections](../maker/create-update-collection.md) and leverage functions such as [LoadData and SaveData](../maker/functions/function-savedata-loaddata.md) for basic data storage when offline.

## How to build offline capable apps
The first thing to think about in offline scenarios is how your apps work with data. Apps in PowerApps primarily access data through a set of [connectors](../maker/connections-list.md) that the platform provides, such as SharePoint, Office 365, and the Common Data Service. You can also build custom connectors that enable apps to access any service that provides a RESTful endpoint. This could be a Web API or a service such as Azure Functions. All these connectors use HTTPS over the Internet, which means your users must be online for them to access data and any other capabilities that a service offers.

![PowerApps app with connectors](./media/offline-apps/online-app.png)

### Handling offline data
One of the most interesting aspects of PowerApps is its set of capabilities and formulas that enable you to filter, search, sort, aggregate, and manipulate data in a consistent way regardless of the data source. Sources range from in-memory collections in the app, to SharePoint lists, to SQL databases and the Common Data Service. This consistency enables you to easily retarget an app to use a different backend. More importantly here, it also enables you to use local collections for data management with almost no changes to an app's logic. In fact, local collections are the primary mechanism for handling offline data.

## Building an offline Twitter app
To keep the focus on the offline aspects of app development, we'll show you a simple scenario focused around Twitter. We'll build an app that enables you to read Twitter posts and submit tweets while being offline. When the app comes online, the app posts tweets and reloads the local data.

At a high level, the app does the following:

1. On app startup (based on the first screen's **OnVisible** property):
   
   * If the device is online, we access the Twitter connector directly to fetch data, and populate a collection with that data.
   * If the device is offline, we load the data from a local cache file using [LoadData](../maker/functions/function-savedata-loaddata.md).
   * We enable the user to submit tweets - if online we post directly to Twitter and refresh the local cache.
2. Every 5 minutes, if online:
   
   * We post any tweets that we have in the local cache.
   * We refresh the local cache and save it using [SaveData](../maker/functions/function-savedata-loaddata.md).

### Step 1: Create a new phone app
1. Open PowerApps Studio.
2. Click or tap **New** > **Blank app** > **Phone layout**.
   
    ![Blank app, phone layout](./media/offline-apps/blank-app.png)

### Step 2: Add a Twitter connection

1. Click or tap **Content** > **Data sources**, then choose **Add data source** on the **Data sources** panel.

2. Click or tap **New Connection** , select **Twitter** , and click or tap **Create**.

3. Enter your credentials, and create the connection.
   
    ![Add a Twitter connection](./media/offline-apps/twitter-connection.png)

### Step 3: Load tweets into a LocalTweets collection on app startup
Select the **OnVisible** property for **Screen1** in the app, and copy in the following formula:

```
If(Connection.Connected,

    ClearCollect(LocalTweets, Twitter.SearchTweet("PowerApps", {maxResults: 100}));

    UpdateContext({statusText: "Online data"})

    ,

    LoadData(LocalTweets, "Tweets", true);

    UpdateContext({statusText: "Local data"})

);

LoadData(LocalTweetsToPost, "LocalTweets", true);

SaveData(LocalTweets, "Tweets")
```

![Formula to load tweets](./media/offline-apps/load-tweets.png)

This formula checks if the device is online:

* If the device is online, it loads into a **LocalTweets** collection up to 100 tweets with the search term "PowerApps".
* If the device is offline, it loads the local cache from a file called "Tweets," if it's available.

### Step 4: Add a gallery and bind it to the LocalTweets collection

1. Insert a new flexible height gallery: **Insert** > **Gallery** > **Blank flexible height**.

2. Set the **Items** property to **LocalTweets**.

3. Add four **Label** controls to display data from each tweet, and set the **Text** properties to:
   * **ThisItem.TweetText**
   * **ThisItem.UserDetails.FullName & " @" & ThisItem.UserDetails.UserName**
   * **"RT: " & ThisItem.RetweetCount**
   * **Text(DateTimeValue(ThisItem.CreatedAtIso), DateTimeFormat.ShortDateTime)**
4. Add an **Image** control, and set the **Image** property to **ThisItem.UserDetails.ProfileImageUrl**.

### Step 5: Add a connection status label
Insert a new **Label** control, and set its **Text** property to the following formula:

```
If (Connection.Connected, "Connected", "Offline")
```

This formula checks if the device is online. If it is, the text of the label is "Connected", otherwise it's "Offline".

### Step 6: Add a text input to compose new tweets

1. Insert a new **Text input** control named "NewTweetTextInput".

2. Set the **Reset** property of the text input to **resetNewTweet**.

### Step 7: Add a button to post the tweet
1. Add a **Button** control, and set the **Text** property to "Tweet".
2. Set the **OnSelect** property to the following formula:
   
    ```
    If (Connection.Connected,
   
        Twitter.Tweet("", {tweetText: NewTweetTextInput.Text}),
   
        Collect(LocalTweetsToPost, {tweetText: NewTweetTextInput.Text});
   
        SaveData(LocalTweetsToPost, "LocalTweetsToPost")
   
    );
   
    UpdateContext({resetNewTweet: true});
   
    UpdateContext({resetNewTweet: false})
    ```  

This formula checks if the device is online:

* If the device is online, it tweets the text immediately.
* If the device is offline, it captures the tweet in a **LocalTweetsToPost** collection, and saves it to the app.

Then the formula resets the text in the text box.

### Step 8: Add a timer to check for tweets every five minutes
Add a new **Timer** control:

* Set the **Duration** property to 300000.

* Set the **AutoStart** property to true.

* Set the **OnTimerEnd** to the following formula:
  
    ```
    If(Connection.Connected,
  
        ForAll(LocalTweetsToPost, Twitter.Tweet("", {tweetText: tweetText}));
  
        Clear(LocalTweetsToPost);
  
        Collect(LocalTweetsToPost, {tweetText: NewTweetTextInput.Text});
  
        SaveData(LocalTweetsToPost, "LocalTweetsToPost");
  
        UpdateContext({statusText: "Online data"})
    )
    ```

This formula checks if the device is online. If it is, the app tweets all the items in the **LocalTweetsToPost** collection. Then it clears the collection.

Now that the app is finished, let's check out how it looks before we move on to testing. On the left, the app is connected; and on the right, it's offline, with one tweet ready to post when it's online again.

![Finished app with online and offline modes](./media/offline-apps/finished-app.png)

## Testing the app
Use the following steps to test the app:

1. Run PowerApps on a mobile device while online. You must run an app at least once while being online, so you can download the app to the device.
2. Launch the Twitter app.
3. Notice that the tweets are loaded, and that the status shows **Connected**.
4. Close PowerApps completely.
5. Set the device to airplane mode to ensure that it's offline.
6. Run PowerApps. You can now run the Twitter app offline, and you have access to any other apps that you have previously run on this device while online (i.e. PowerApps hides any apps that haven't yet been downloaded to your device).
7. Run the app again.
8. Notice how it correctly reflects the connection state, with a status of **Offline**.
9. Write a new tweet. It will be stored locally in the **LocalTweetsToPost** collection.
10. Exit airplane mode. After the timer triggers, the app posts the tweet.

We hope this article gives you an idea of the capabilities that PowerApps has for building offline apps. As always, please provide feedback in our [forum](https://powerusers.microsoft.com/t5/PowerApps-Forum/bd-p/PowerAppsForum1) and share your examples of offline apps in the [PowerApps community blog](https://powerusers.microsoft.com/t5/PowerApps-Community-Blog/bg-p/PowerAppsBlog).

