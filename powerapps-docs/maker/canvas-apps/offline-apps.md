---
title: Develop offline-capable canvas apps | Microsoft Docs
description: Develop offline-capable canvas apps so that your users are productive whether they are online or offline.
author: gregli-msft
manager: kvivek
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: 
ms.date: 01/31/2019
ms.author: gregli
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---

# Develop offline-capable canvas apps

One of the most common scenarios you face as a mobile-app developer is enabling your users to be productive when there is limited connectivity or no connectivity at all. PowerApps has a set of features and behaviors that help you to develop offline-capable canvas apps. You can:

- Launch PowerApps Mobile when offline.
- Run apps that you develop when offline.
- Determine when an app is offline, online, or in a metered connection by using the [Connection](../canvas-apps/functions/signals.md#connection) signal object.
- Use [collections](../canvas-apps/create-update-collection.md) and leverage functions such as [LoadData and SaveData](../canvas-apps/functions/function-savedata-loaddata.md) for basic data storage when offline.

## Limitations

**LoadData** and **SaveData** combine to form a simple mechanism to store small amounts of data on a local device. By using these functions, you can add simple offline capabilities to your app.

These functions are limited by the amount of available app memory because they operate on an in-memory collection. Available memory can vary depending on the device, the operating system, the memory that PowerApps Mobile uses, and the complexity of the app in terms of screens and controls. If you store more than a few megabytes of data, test your app with expected scenarios on the devices on which you expect it to run. You should generally expect to have between 30 and 70 megabytes of available memory.  

The functions also don't automatically resolve merge conflicts when a device returns to connectivity from offline – configuration on what data is saved and how to handle reconnection is up to the maker when writing expressions.

We're working to expand the capabilities for offline scenarios. Stay tuned here and on the [PowerApps blog](https://powerapps.microsoft.com/blog/) for updates when they become available.

## How to build offline-capable apps

The first thing to think about in offline scenarios is how your apps work with data. Apps in PowerApps primarily access data through a set of [connectors](../canvas-apps/connections-list.md) that the platform provides, such as SharePoint, Office 365, and the Common Data Service. You can also build custom connectors that enable apps to access any service that provides a RESTful endpoint. This could be a Web API or a service such as Azure Functions. All these connectors use HTTPS over the Internet, which means your users must be online for them to access data and any other capabilities that a service offers.

![PowerApps app with connectors](./media/offline-apps/online-app.png)

### Handling offline data

One of the most interesting aspects of PowerApps is its set of capabilities and formulas that enable you to filter, search, sort, aggregate, and manipulate data in a consistent way regardless of the data source. Sources range from in-memory collections in the app to SharePoint lists to SQL databases and Common Data Service. This consistency enables you to easily retarget an app to use a different backend. More importantly here, it also enables you to use local collections for data management with almost no changes to an app's logic. In fact, local collections are the primary mechanism for handling offline data.

## Build an offline Twitter app

To keep the focus on the offline aspects of app development, we'll show you a simple scenario focused around Twitter. We'll build an app that enables you to read Twitter posts and submit tweets while being offline. When the app comes online, the app posts tweets and reloads the local data.

At a high level, the app performs these tasks:

1. When the user opens the app:

    - If the device is online, the app fetches data through the Twitter connector and populates a collection with that data.
    - If the device is offline, the app loads the data from a local cache file by using the [**LoadData**](../canvas-apps/functions/function-savedata-loaddata.md) function.
    - The user can submit tweets. If the app is online, it posts the tweets directly to Twitter and refreshes the local cache.

1. Every five minutes while the app is online:

    - The app posts any tweets in the local cache.
    - The app refreshes the local cache and saves it by using the [**SaveData**](../canvas-apps/functions/function-savedata-loaddata.md) function.

### Step 1: Create a blank phone app

1. In PowerApps Studio, select **File** > **New**.

1. On the **Blank app** tile, select **Phone layout**.

    ![Blank app, phone layout](./media/offline-apps/blank-app.png)

### Step 2: Add a Twitter connection

1. On the **View** tab, select **Data sources**.

1. In the **Data** pane, select **Add data source**.

1. Select **New Connection** > **Twitter** > **Create**.

1. Enter your credentials, and create the connection.

### Step 3: Load tweets into a LocalTweets collection

1. In the **Tree view** pane, select **App**, and then set its **OnStart** property to this formula:

    ```powerapps-dot
    If( Connection.Connected,
        ClearCollect( LocalTweets, Twitter.SearchTweet( "PowerApps", {maxResults: 100} ) );
            Set( statusText, "Online data" ),
        LoadData( LocalTweets, "LocalTweets", true );
            Set( statusText, "Local data" )
    );
    SaveData( LocalTweets, "LocalTweets" );
    ```

    ![Formula to load tweets](./media/offline-apps/load-tweets.png)

1. In the **Tree view** pane, select the ellipsis menu for the **App** object, and then select **Run OnStart** to run that formula.

    ![Run formula to load tweets](./media/offline-apps/load-tweets-run.png)

    > [!NOTE]
    > The **LoadData** and **SaveData** functions might show an error in PowerApps Studio because browsers don't support them. However, they'll perform normally after you deploy this app to a device.

This formula checks whether the device is online:

- If the device is online, the formula loads up to 100 tweets with the search term "PowerApps" into a **LocalTweets** collection.
- If the device is offline, the formula loads the local cache from a file called "LocalTweets" if it's available.

### Step 4: Bind a gallery to the LocalTweets collection

1. On the **Insert** tab, select **Gallery** > **Blank flexible height**.

1. Set the **Items** property to `LocalTweets`.

1. Add four **Label** controls, and set the **Text** property of each to one of these values:

    - `ThisItem.TweetText`
    - `ThisItem.UserDetails.FullName & " \@" & ThisItem.UserDetails.UserName`
    - `"RT: " & ThisItem.RetweetCount`
    - `Text(DateTimeValue(ThisItem.CreatedAtIso), DateTimeFormat.ShortDateTime)`

1. Add an **Image** control, and set its **Image** property to this expression:

    - `ThisItem.UserDetails.ProfileImageUrl`

### Step 5: Show connection status

Insert a **Label** control, and set its **Text** property to this formula:

`If( Connection.Connected, "Connected", "Offline" )`

This formula determines whether the device is online. If it is, the label shows **Connected**; otherwise, it shows **Offline**.

### Step 6: Add a box to compose tweets

Insert a **Text input** control, rename it **NewTweetTextInput**, and then set its **Default** property to `""`.

### Step 7: Add a button to post the tweet

1. Add a **Button** control, and set the **Text** property to this value:

    `"Tweet"`

1. Set the **OnSelect** property to the following formula:

    ```powerapps-dot
    If( Connection.Connected,
        Twitter.Tweet( "", {tweetText: NewTweetTextInput.Text} ),
        Collect( LocalTweetsToPost, {tweetText: NewTweetTextInput.Text} );
            SaveData( LocalTweetsToPost, "LocalTweetsToPost" )
    );
    Reset( NewTweetTextInput );
    ```  

1. In the **OnStart** property for the **App**, add a line at the end of the formula:

    ```powerapps-dot
    If( Connection.Connected,
        ClearCollect( LocalTweets, Twitter.SearchTweet( "PowerApps", {maxResults: 100} ) );
            Set( statusText, "Online data" ),
        LoadData( LocalTweets, "LocalTweets", true );
            Set( statusText, "Local data" )
    );
    SaveData( LocalTweets, "LocalTweets" );
    LoadData( LocalTweetsToPost, "LocalTweetsToPost", true );  // added line
    ```

    ![Run formula to load tweets with uncommented line](./media/offline-apps/load-tweets-save.png)

This formula determines whether the device is online:

- If the device is online, it posts the tweet immediately.
- If the device is offline, it captures the tweet in a **LocalTweetsToPost** collection and saves it to the device.

Then the formula resets the text in the text-input box.

### Step 8: Check for tweets every five minutes

1. Add a **Timer** control.

1. Set its **Duration** property to **300000**.

1. Set its **AutoStart** property to **true**.

1. Set its **Repeat** property to **true**.

1. Set its **OnTimerEnd** to this formula:

    ```powerapps-dot
    If( Connection.Connected,
        ForAll( LocalTweetsToPost, Twitter.Tweet( "", {tweetText: tweetText} ) );
            Clear( LocalTweetsToPost )
    )
    ```

This formula determines whether the device is online. If it is, the app tweets all the items in the **LocalTweetsToPost** collection and then clears the collection.

Now that the app is finished, let's check out how it looks before we move on to testing. On the left, the app is connected; and on the right, it's offline, with one tweet ready to post when it's online again.

![Finished app with online and offline modes](./media/offline-apps/finished-app.png)

## Test the app

1. On a mobile device that's online, open PowerApps, and then open the Twitter app.

    The tweets are loaded, and the status shows **Connected**.

1. Close the Twitter app, and then enable the device's airplane mode to ensure that it's offline.

1. Open the Twitter app again.

    The status label shows that the app is **Offline**.

1. Write a tweet.

    The tweet is stored locally in the **LocalTweetsToPost** collection.

1. Disable the device's airplane mode to bring the app online again.

    In five minutes or less, the app posts the tweet.

We hope this article gives you an idea of the capabilities that PowerApps has for building offline apps. As always, please provide feedback in our [forum](https://powerusers.microsoft.com/t5/PowerApps-Forum/bd-p/PowerAppsForum1) and share your examples of offline apps in the [PowerApps community blog](https://powerusers.microsoft.com/t5/PowerApps-Community-Blog/bg-p/PowerAppsBlog).