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

A common scenario when building apps is the need to share a "deep link" to a specific screen. This is useful to get someone straight to a specific screen and data rather than asking them to navigate from the "home" screen of your app.

To deep link into a Power Apps app, you'll use the URL format: https://web.powerapps.com/apps/{*AppID*}?*query*.

-   AppID can be found on the make.powerapps.com Detail page for the app.

-   The query allows you to designate the data to deep link to. You'll need to make some code changes to your canvas app to use the provided parameter(s) when the app is opened using the URL.

The example scenario below shows how to set up a canvas app to handle the query parameter and how to create a UI for emailing a deep link directly from a screen of your app.

## Example

### Create the app

This example is built using Microsoft Dataverse as the data source and can be customized to use any other data source. More information: Create a canvas app with data from Microsoft Dataverse

1.  Sign in to Power Apps and, if necessary, switch environments.

2.  Under **Start from data**, select **Dataverse**.

    :::image type="content" source="media/deep-linking/start-from-dataverse.png" alt-text="Start from data - Microsoft Dataverse." border="false":::

3.  If this is your first time, you're prompted to create a connection to Dataverse. Select **Create** this connection. Otherwise, under **Choose a table**, select **Accounts**, and then select **Connect**.

4.  If the **Welcome to Power Apps Studio** dialog box appears, select **Skip**.

Your app opens to the **BrowseScreen**, which shows a list of accounts in a gallery. On the BrowseScreen, by default, the gallery shows an email address, a city, and an account name. The app also contains a **DetailScreen** and **EditScreen**.

### Set the navigation to use a context variable

1.  On BrowseScreen, select Layout under gallery Properties and change the **Layout** to **"Title, subtitle and body"**

    :::image type="content" source="media/deep-linking/account-list.png" alt-text="Accounts list view." border="false":::

2.  Select first record of BrowseGallery and under **OnSelect**, enter the following:

    ```powerapps-dot
    Navigate(DetailScreen, Fade, {accountVal:ThisItem})
    ```

    :::image type="content" source="media/deep-linking/account-val.png" alt-text="Set AccountVal." border="false":::

    This creates a context variable called *accountVal*. This value is populated anytime a record is selected from the Gallery. The user is navigated to the DetailScreen with the selected account stored in *accountVal*.

3.  In the DetailScreen, select **Edit fields** under **Properties**, and add **Account**, **Primary Contact**, and **Email** fields.

    :::image type="content" source="media/deep-linking/account-detail.png" alt-text="Accounts Detail view.":::

4.  Select DetailForm, and set **Item** to *accountVal*.

    :::image type="content" source="media/deep-linking/set-account-detail.png" alt-text="AccountVal.":::


### Save the app

1.  Select **Settings**.

2.  Set the app name to **Account Deep linking** and select **Save**.

3.  Close the settings dialog.

4.  Near the left edge, select **Save as** and then, in the lower-right corner, select **Save**.

### Retrieve the App ID

The App ID is a unique GUID representing a given app. It is generated when you save the app to cloud. You can get the app details, including App ID by navigating to your maker portal and looking at the Details tab.

In make.powerapps.com, on the **Apps** tab, select the ellipsis ( **. . .** ), then **Details** to view app details.

  :::image type="content" source="media/deep-linking/app-detail.png" alt-text="App details.":::

Make a note of the 'App ID' which will be used in the next set of steps. Our example App ID is eb355244-8241-4f2f-bf83-e0760caffd99.

### Enable deep linking within the canvas app

The next set of steps navigate to the DetailScreen if the app is launched with the accountId parameter as part of the URL.

The [Param](https://powerapps.microsoft.com/en-us/tutorials/function-param/) function retrieves the query string parameter if one was supplied when launching the app.

Select **App**

1.  On **OnStart**, store the retrieved App ID value.

    ```powerapps-dot
    Set(AppID, eb355244-8241-4f2f-bf83-e0760caffd99);
    ```

2. Add the following formula

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
