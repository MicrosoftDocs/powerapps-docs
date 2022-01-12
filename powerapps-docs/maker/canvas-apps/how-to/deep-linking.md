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
    - TashasEv
    - slaouist
    - tapanm-msft
    - vasavib
---

# Create a canvas app with deep link to a specific screen

A common scenario when building apps is the need to share a "deep link" to a specific screen. Deep links are useful when you want to get users straight to a specific screen and data rather than asking them to navigate from the "home" screen of your app.

To deep link into a Power Apps app, you'll use this URL syntax: `https://web.powerapps.com/apps/{AppID}?query`.

In this syntax:
- **AppID**&mdash;ID of the app. Go to [Power Apps](https://make.powerapps.com) > **Apps** > Select your app > **Details**.
- Query&mdash;The query text allows you to supply the data to deep link to. You'll need to make some code changes to your canvas app to use the provided parameters to open the app using the query URL.

In this article, you'll learn about how to:

- Set up a canvas app to handle the query parameter.
- Create a UI for emailing a deep link directly from a screen of your app.
- Use the app to browse to a specific account, send an email with the deep link, and use the link from the received email to open the app directly to that account.

## Prerequisites

- [Power Apps license](/power-platform/admin/pricing-billing-skus)
- If you're new to Power Apps, familiarize yourself with Power Apps basics by [generating an app](../get-started-test-drive.md) and then customizing that app's [controls](../add-configure-controls.md), [gallery](../add-gallery.md), [forms](../working-with-forms.md), and [cards](../working-with-cards.md).
- To create an app, you must be assigned to the [Environment Maker](/power-platform/admin/database-security) security role.

## Create the app

1. Sign in to [Power Apps](https://make.powerapps.com).

1. Verify and if necessary, switch environments using the environments list from the top-right side of the screen.

1. Under **Start from data**, select **Dataverse**.

    :::image type="content" source="media/deep-linking/start-from-dataverse.png" alt-text="Start from data - Microsoft Dataverse." border="false":::

1. If you don't have an existing connection to Microsoft Dataverse, you'll be prompted to create it. Select **Create** this connection.

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

    :::image type="content" source="media/deep-linking/onselect-accountval.png" alt-text="Set AccountVal.":::

    The [Navigate()](../functions/function-navigate.md) function creates a context variable called **accountVal**. This variable is populated whenever you select a record from the gallery. Upon selecting record, you'll be taken to the **DetailScreen** with the selected value (in this example, account) in **accountVal**.

1. From the **Tree view** on the left-side of the screen, expand **DetailScreen1**, and select **DetailForm1**.

    :::image type="content" source="media/deep-linking/select-detailform1.png" alt-text="Select DetailForm1 from Tree view.":::

1. From the properties pane on the right-side of the screen, select **Edit fields**, and add **Account**, **Primary Contact**, and **Email** fields.

    :::image type="content" source="media/deep-linking/account-detail.png" alt-text="Accounts Detail view.":::

1. Select **DetailForm**, and set **Item** to **accountVal**.

    :::image type="content" source="media/deep-linking/set-account-detail.png" alt-text="AccountVal.":::

1. [Save](../save-publish-app.md#save-changes-to-an-app) with the name "Account deep linking".

## Get the App ID

**App ID** is a unique GUID representing a given app, and generated when you save the app to cloud.

To get the **App ID**, open a new tab and go to [Power Apps](https://make.powerapps.com) > **Apps** > Select your app > **Details**. More information: [Get an App ID](../get-sessionid.md#get-an-app-id)

  :::image type="content" source="media/deep-linking/app-detail.png" alt-text="App details.":::

## Enable deep link to a screen

The goal of this example is to take users to the **DetailsScreen1** when the app is launched with the **accountId** query parameter as part of the app URL. For this purpose, we'll use function [Param()](../functions/function-param.md) that retrieves the query string parameter supplied while launching the app.

1. Select **App** from the **Tree view** on the left-side of the screen.

    > [!TIP]
    > If you've closed Power Apps Studio, reopen the saved "Account deep linking" app by [editing](../edit-app.md) the app.

1. Select **OnStart** property from the list of properties.

1. To store the **App ID** value, update the **OnStart** property formula as below.

    ```powerapps-dot
    Set(AppID, "b76abea1-e888-409e-8fb6-630be198fa65");
    If(Not(IsBlank(Param("accountId"))),Set(accountId,Param("accountId")));
    ```

    In this formula, function [Set()](../functions/function-set.md) sets the **App ID** to the GUID of the app. And function [Param()](../functions/function-param.md) stores the value in the **accountId** variable, when not blank.

    > [!NOTE]
    > Ensure you replace the **App ID** (GUID) in the above example formula to your App ID as appropriate.

    :::image type="content" source="media/deep-linking/app-onstart.png" alt-text="App OnStart formula with Set and Param functions.":::

1. Select **StartScreen** property for the app, and add the following:

    ```powerapps-dot
    If(Not(IsBlank(Param("accountId"))),DetailScreen1,BrowseScreen1)
    ```

    This function checks if the Param is blank, then stay on the **BrowseScreen1**. Else, go to **DetailScreen1**.

    :::image type="content" source="media/deep-linking/app-startscreen.png" alt-text="App StartScreen formula with Param function to redirect or stay based on variable value.":::

1. Select **DetailScreen1** from the **Tree view**.

1. Select **OnVisible** property, and enter the following:

    ```powerapps-dot
    If(Not(IsBlank(accountId)), UpdateContext({accountVal:LookUp(Accounts, Account = GUID(accountId))}))
    ```

    This function uses **accountId** stored from the previous step to set **accountVal** variable.

    :::image type="content" source="media/deep-linking/detailscreen-onvisible.png" alt-text="DetailScreen1 with OnVisible property formula.":::

## Create the deep link URL

Your app is now configured to receive **accountId** as the parameter that contains the GUID for an account from the **Accounts** table. And when this parameter is provided with the request to the app, the app will directly open the details screen (**DetailScreen1**) with the given **accountId**.

To invoke app with the parameter value, we have to use the following syntax:

`https://web.powerapps.com/apps/[App ID]*}?*query*`

In the above syntax, we have to add the **App ID** and the query that contains **accountId** variable with its value.

For example, when the following URL was entered in a browser for the sample tenant, the app **Account deep linking** opened directly with the supplied **accountId** parameter value (in this example, "A. Datum Corporation (Sample)"): `https://apps.powerapps.com/play/061b64cd-e5a0-4a7a-a77f-b6f8586dd6c7?accountId=01e5bf81-7d44-ec11-8c60-002248094566`

:::image type="content" source="media/deep-linking/sample-link.png" alt-text="Sample link with A. Datum Corporation (Sample) details open.":::

## Send deep link in email

We can also supply a variable **accountVal** to point to the account's ID instead of using absolute link explained above while invoking the URL for the given account from inside the app.

For this purpose, we'll create a button and add the ability to invoke an email from within the app with the deep link to the selected account's details screen from the **Account deep linking** app.

1. Select **Data** from the left-side of the screen.

1. Select **Add data** > search for and select **Office 365 Outlook** > select **Connect**.

    > [!NOTE]
    > This action adds the Microsoft 365 Outlook connection so that we can use the next steps to invoke composing an email to share the account information.

1. Select **DetailScreen1** from the **Tree view**.

1. Insert a button at bottom-right of the screen, and rename it to **Share Account**.

1. On the button's **OnSelect** property, enter the following:

    ```powerapps-dot
    Office365Outlook.SendEmailV2("Recipient", "Subject", "Here's the deep link to the selected account - https://web.powerapps.com/apps/[App ID]?accountId=" & accountVal.Account)
    ```

    This formula uses the Microsoft 365 connector for Outlook to send an email using the [SendEmailV2](/connectors/office365/#send-an-email-(v2)) operation.

    > [!NOTE]
    > Replace **Recipient**, **Subject**, and **AppID** in the above formula with the email address of the recipient, subject for the email, and the ID of the app.

    :::image type="content" source="media/deep-linking/share-account-button.png" alt-text="Share Account button.":::

1. [Save and publish](../save-publish-app.md) the app.

## Test the app

Run the app, and go to the details screen for any account. And then, select the button **Share account**. The **OnSelect** button formula triggers an email to the recipient with the subject and body configured earlier. Here's a sample email sent by the configured app:

:::image type="content" source="media/deep-linking/sent-email.png" alt-text="Email sent using button Share account.":::

Open the email, and copy the deep link that points to the selected account, and you'll be taken directly to the account details screen in the **Account deep linking** app, instead of the default browse screen.

:::image type="content" source="media/deep-linking/app-opened-from-email.png" alt-text="App opened using the link from the email.":::

### See also

- [Create a canvas app from a template](../get-started-test-drive.md)
- [Add and configure controls in canvas apps](../add-configure-controls.md)
- [Get started with formulas in canvas apps](../working-with-formulas.md)
