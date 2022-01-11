---
title: Create a canvas app with deep link to a specific screen
description: Learn how to deep link to a specific screen within canvas apps.
author: vasavib
ms.service: powerapps
ms.topic: article
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 01/10/2022
ms.subservice: canvas-maker
ms.author: vabhavir
search.audienceType: 
  - maker
search.app: 
  - PowerApps
contributors:
    - slaouist
    - tapanm-msft
    - vasavib
---

# Create a canvas app with deep link to a specific screen

A common scenario when building apps is the need to share a "deep link" to a specific screen. Deep links are useful when you want to get users straight to a specific screen and data rather than asking them to navigate from the "home" screen of your app.

To deep link into a Power Apps app, you'll use this URL format: `https://web.powerapps.com/apps/{AppID}?query`.

- To find the **AppID**, go to [Power Apps](https://make.powerapps.com) > **Apps** > Select your app > **Details**.
- The query text allows you to designate the data to deep link to. You'll need to make some code changes to your canvas app to use the provided parameters to open the app using the query URL.

In this article, you'll learn about how to:

- Set up a canvas app to handle the query parameter.
- Create a UI for emailing a deep link directly from a screen of your app.

## Prerequisites

- [Power Apps license](/power-platform/admin/pricing-billing-skus)
- If you're new to Power Apps, familiarize yourself with Power Apps basics by [generating an app](../get-started-test-drive.md) and then customizing that app's [controls](../add-configure-controls.md), [gallery](../add-gallery.md), [forms](../working-with-forms.md), and [cards](../working-with-cards.md).
- To create an app, you must be assigned to the [Environment Maker](/power-platform/admin/database-security) security role.

## Create the app

1. Sign in to [Power Apps](https://make.powerapps.com).

1. Verify and if necessary, switch environments using the environments list from the top-right side of the screen.

1. Under **Start from data**, select **Dataverse**.

    :::image type="content" source="media/deep-linking/start-from-dataverse.png" alt-text="Start from data - Microsoft Dataverse." border="false":::

1. If this is your first time, you're prompted to create a connection to Dataverse. Select **Create** this connection.

1. Under **Choose a table**, select **Accounts**, and then select **Connect**.

Your app opens to the **BrowseScreen**, that shows a list of accounts in a gallery. By default, this gallery shows an email address, a city, and an account name. The app also contains **DetailScreen** and **EditScreen**.

## Update navigation

Now you'll set the navigation to use a context that we'll use to take the user to another screen.

1. On **BrowseScreen** screen, select **Layout** under gallery properties, and select **Title, subtitle and body**

    :::image type="content" source="media/deep-linking/account-list.png" alt-text="Accounts list view.":::

1. Select first record of **BrowseGallery** gallery. And then, under **OnSelect**, enter the following:

    ```powerapps-dot
    Navigate(DetailScreen1, Fade, {accountVal:ThisItem})
    ```

    :::image type="content" source="media/deep-linking/onselect-accountval.png" alt-text="Set AccountVal." border="false":::

    <!--->:::image type="content" source="media/deep-linking/account-val.png" alt-text="Set AccountVal." border="false":::--->

    The [Navigate()](../functions/function-navigate.md) function creates a context variable called **accountVal**. This variable is populated whenever you select a record from the gallery. Upon selecting record, you'll be taken to the **DetailScreen** with the selected value (in this example, account) in **accountVal**.

1. From the **Tree view** on the left-side of the screen, expand **DetailScreen1**, and select **DetailForm1**.

    :::image type="content" source="media/deep-linking/select-detailform1.png" alt-text="Select DetailForm1 from Tree view.":::

1. From the properties pane on the right-side of the screen, select **Edit fields**, and add **Account**, **Primary Contact**, and **Email** fields.

    :::image type="content" source="media/deep-linking/account-detail.png" alt-text="Accounts Detail view.":::

1. Select **DetailForm**, and set **Item** to **accountVal**.

    :::image type="content" source="media/deep-linking/set-account-detail.png" alt-text="AccountVal.":::

1. [Save](../save-publish-app.md#save-changes-to-an-app) with the name "Account Deep linking".

## Get the App ID

**App ID** is a unique GUID representing a given app, and generated when you save the app to cloud. To get the **App ID**, go to [Power Apps](https://make.powerapps.com) > **Apps** > Select your app > **Details**. More information: [Get an App ID](../get-sessionid.md#get-an-app-id)

  :::image type="content" source="media/deep-linking/app-detail.png" alt-text="App details.":::

### Enable deep link within the canvas app

The objective of this example is to take users to the **DetailsScreen** when the app is launched with the **accountId** query parameter as part of the app URL. For this purpose, we'll use [Param()](../functions/function-param.md) function that retrieves the query string parameter supplied while launching the app.

1. Select **App** from the **Tree view** on the left-side of the screen.

1. Select **OnStart** property from the list of properties.

1. To store the **App ID** value, update the **OnStart** property formula as below.

    ```powerapps-dot
    Set(AppID, b76abea1-e888-409e-8fb6-630be198fa65);
    ```

    > [!NOTE]
    > Ensure you update the **App ID** (GUID) in the above formula for your app as appropriate.

2. Add the following formula --> ?

    ```powerapps-dot
    If(Not(IsBlank(Param("accountId"))),Set(accountId,Param("accountId")));
    ```

    If the Param is not blank, store it in the *accountId* variable.

3.  On **StartScreen**, add the following:

    ```powerapps-dot
    If(Not(IsBlank(Param("accountId"))),DetailScreen1,BrowseScreen1)
    ```

    If the Param is blank, stay on BrowseScreen, else navigate to DetailScreen.

**On DetailScreen:**

1.  On **OnVisible**, enter the following

    ```powerapps-dot
    If(Not(IsBlank(accountId)), UpdateContext({accountVal:LookUp(Accounts, Account = GUID(accountId))}))
    ```

    On BrowseScreen we stored the Param "**accountId**" into a variable with same name. If the variable accountId has value, we are using that to set **accountVal**.

### Create the deep link URL

The App URL uses this format: [https://web.powerapps.com/apps/{*AppID*}?*query*](https://web.powerapps.com/apps/%7bAppID%7d?query).

Our example App ID is eb355244-8241-4f2f-bf83-e0760caffd99.

The query can be an arbitrary key-value pair. We'll use **accountId**=***x*** where *x* is the GUID of the account we want to link to. For example, here is the URL for the Account with accountId = 68f1f132-9e6c-eb11-b0b0-000d3a1a1100, https://web.powerapps.com/apps/eb355244-8241-4f2f-bf83-e0760caffd99?accountId=68f1f132-9e6c-eb11-b0b0-000d3a1a1100

### Email a deep link from the detail screen

Create a UI button so that users can click **Share Account** to send a deep link to a specific account's detail page in your app.

1.  Insert a button at bottom right and rename it to **Share Account**.

2.  On the button's **OnSelect**, enter the following

    ```powerapps-dot
    Office365Outlook.SendEmailV2(*recipient*, *subject*, "https://web.powerapps.com/apps/{*AppID*}?accountId=" & accountVal.Account)
    ```

    Replace *recipient*, *subject* and*AppID* in the above formula.

    :::image type="content" source="media/deep-linking/share-account.png" alt-text="Share Account button." border="false":::

Finally save and publish the app.

### Testing the app

Once the app is saved and published, you can run the app using the following URL pattern, by replacing AppId and AccountGUID. https://web.powerapps.com/apps/{AppId}?accountId={AccountGUID}.

The app will open up to the detailed view of the specified Account GUID.

### See also

- [Create a canvas app from a template](../get-started-test-drive.md)
- [Add and configure controls in canvas apps](../add-configure-controls.md)
- [Get started with formulas in canvas apps](../working-with-formulas.md)
