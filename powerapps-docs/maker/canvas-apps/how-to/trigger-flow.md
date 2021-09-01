---
title: Build a canvas app that can trigger a Power Automate flow
description: Learn about how to build a canvas app that can trigger a Power Automate flow.
author: joel-lindstrom
ms.service: powerapps
ms.topic: article
ms.custom: canvas
ms.reviewer:
ms.date: 08/31/2021
ms.subservice: canvas-maker
ms.author: emcoope
search.audienceType: 
  - maker
search.app: 
  - PowerApps
contributors:
    - joel-lindstrom
    - tapanm-msft
---


# Build a canvas app that can trigger a Power Automate flow

Power Automate can be used to create logic that performs one or more tasks when an event occurs in a canvas app. For example, a button can be configured so that, when a user selects it, an item is created in a SharePoint list, an email, or meeting request is sent, a file is added to the cloud, or all of these. Any control in the app can be configured to start the flow, that continues to run even if you close the app.

In this article, we'll learn how create and trigger a flow using canvas apps.

## Prerequisites

To complete this lesson, you'll need Power Automate and Power Apps environment with a Dataverse database. If you don't have a license, you can sign up for the [Power Apps Developer Plan](../../developer-plan.md) or use [Power Apps trial](../../signup-for-powerapps.md).

## Create a trial environment

An environment in Power Apps is a space to store, manage, and share your organization’s business data, apps, chatbots, and flows. It also serves as a container to separate apps that might have different roles, security requirements, or target audiences. Each environment can have one Dataverse database.

To make sure that you have what you need to complete this lesson, we're going to create a new environment that includes a Dataverse database. This is a 30-day trial that will go away at the end of the 30 days, but you can upgrade it to a sandbox or production environment if you want to keep it.

We're going to create a trial environment that will include a Dataverse database, and the sample data used in this article.

1. Go to [Power Platform admin center](https://admin.powerplatform.microsoft.com/).

1. Select **Environments**.

1. Select **New**.

1. Name the environment **Dataverse Trial**.

1. Select **Trial** for environment type.

1. Toggle **Create Database** to **Yes**.

1. Select **Next**.

1. Toggle **Deploy Sample Apps and Data** to **Yes**.

1. Select **Save**.

Your trial environment will now be created, including a Dataverse database and sample data.

## Build a canvas app

In this lesson, we'll build an app to search, view, and create customer accounts using the **Accounts** table in Dataverse.

1. Sign in to [Power Apps](https://make.powerapps.com).

1. Select the **Dataverse Trial** environment.

    ![Select the Dataverse Trial environment](media/trigger-flow/build-a-canvas-app-1.png "Select the Dataverse Trial environment")

1. Select the button for **Canvas app from blank**

    ![Select the button for Canvas app from blank](media/trigger-flow/build-a-canvas-app-2.png "Select the button for Canvas app from blank")

1. Enter a name, select **Format** as **Phone**, and then select **Create**.

    ![Give the app a name](media/trigger-flow/build-a-canvas-app-3.png "Give the app a name")

1. Select **Create a gallery**.

    ![Create a gallery](media/trigger-flow/build-a-canvas-app-4.png "Create a gallery")

1. Select **Accounts** table.

1. Stretch the gallery to the bottom of the screen, and add a label to the top with the text **Accounts**. And then, update the other properties as listed below.

    | Property | Value |
    | - | - |
    | Font | Open Sans |
    | Font size | 21 |
    | Font weight | Bold |
    | Text alignment | Center |
    | Auto height | Off |
    | Line height | 1.2 |
    | Overflow | Hidden |
    | Display mode | Edit |
    | Visible | On |
    | Position (X, Y) | 0, 0 |
    | Size (Width, Height) | 640, 71 |
    | Padding | 5 Top, 5 Bottom, 5 Left, 5 Right |

    ![Update gallery properties](media/trigger-flow/build-a-canvas-app-6.png "Update gallery properties")

1. Add an **Add** icon to the top-right of the screen by selecting **Insert** > **Icon** > **Add**. And then, update the properties of the icon to color white and padding of 5 from all sides.

    ![Add an **Add** icon](media/trigger-flow/build-a-canvas-app-7.png "Add an **Add** icon")

1. From the top-left side of the screen, select **New screen** > **Form**.

    ![Add new form](media/trigger-flow/build-a-canvas-app-8.png "Add new form")

1. Update the title of the form to **New Account**, and select the data source as **Accounts** from the pane on the right-side of the screen.

![Update title and select data source](media/trigger-flow/build-a-canvas-app-9.png "Update title and select data source")

1. Select **Edit fields** on the right-pane.

    ![Select edit fields](media/trigger-flow/build-a-canvas-app-10.png "Select edit fields")

1. Select **Add field** and add **Email** to the form.

    ![Add email field](media/trigger-flow/build-a-canvas-app-11.png "Add email field")

    The email field gets added to the form.

    ![The email field gets added](media/trigger-flow/build-a-canvas-app-12.png "The email field gets added")

1. et the default mode of the form to **New**.

    ![Default form mode](media/trigger-flow/build-a-canvas-app-13.png "Default form mode")

1. Select Screen1 that has the accounts gallery, and set the **OnSelect** property of the **+** icon to `Navigate(Screen2)`.

    ![Configure navigation to screen 2](media/trigger-flow/build-a-canvas-app-14.png "Configure navigation to screen 2")

1. Select **Insert** > **New screen** > **Blank screen** to add a new screen to the app.

1. Select **Insert** > **Icon**, and then select the Check (badge) icon to add it to the screen.

    ![Insert badge icon](media/trigger-flow/build-a-canvas-app-16.png "Insert badge icon")

1. Move the icon to the top center of the canvas.

    ![Move icon to top-center](media/trigger-flow/build-a-canvas-app-17.png "Move icon to top-center")

1. Add a label with text **Account was created successfully!**, and move it under the icon added in the earlier step.

    ![Add Account was created successfully label](media/trigger-flow/build-a-canvas-app-18.png "Add Account was created successfully label")

1. Add an additional label below the label added in the previous step with text **Send a welcome note to the Customer?**.

    ![Send a welcome note to the Customer](media/trigger-flow/build-a-canvas-app-19.png "Send a welcome note to the Customer")

1. Add a **Text Input** box by selecting **Insert** > **Input** > **Text Input**. Set the **Mode** of the control to **Multiline**, and default text to **Thank you for creating an account with us. We look forward to serving you!**. And move the control below the label added in the previous step.

    ![Add multiline text input control](media/trigger-flow/build-a-canvas-app-20.png "Add multiline text input control")

1. Set the **OnVisible** property of **Screen3** to `Reset(TextInput1)`.

    ![OnVisible property of screen 3](media/trigger-flow/build-a-canvas-app-21.png "OnVisible property of screen 3")

1. Add two buttons to the screen with text **Yes** and **No**, and place them below the input text box added in the previous step.

    ![Yes No buttons](media/trigger-flow/build-a-canvas-app-22.png "Yes No buttons")

1. Go to the **New Account** form screen, and set the **OnVisible** property of the screen to `ResetForm(EditForm3)`.

    ![OnVisible property of New Account form](media/trigger-flow/build-a-canvas-app-23.png "OnVisible property of New Account form")

1. Select the check icon on the top-right, and set the **OnSelect** property to `SubmitForm(EditForm3);Navigate(Screen3)`.

    ![Navigate to screen 3](media/trigger-flow/build-a-canvas-app-24.png "Navigate to screen 3")

1. Select the X button on the top-right, and set the **OnSelect** property to `Back()`.

    ![Back function for close](media/trigger-flow/build-a-canvas-app-25.png "Back function for close")

1. Go back to **Screen3** by selecting **Screen3** in the tree view.

    ![Go to screen 3](media/trigger-flow/build-a-canvas-app-26.png "Go to screen 3")

1. Select the **No** button, and set the button's **OnSelect** property to `Navigate(Screen1)`.

    ![Navigate to screen 1](media/trigger-flow/build-a-canvas-app-27.png "Navigate to screen 1")

1. Select the **Yes** button, select **Action** on the top, and then select **Power Automate**.

    ![Select the Yes button and select Action on the top](media/trigger-flow/build-a-canvas-app-28.png "Select the Yes button and select Action on the top")

1. Select **Create a new flow** to create a new Power Automate flow.

    ![Select Create a new flow to create](media/trigger-flow/build-a-canvas-app-29.png "Select Create a new flow to create")

## Create the Power Automate Flow

1. After Power Automate opens, select **+ Create** > **Instant cloud flow**.

    ![select the Instant cloud flow option](media/trigger-flow/create-the-power-automate-flow-1.png "select the Instant cloud flow option")

1. Enter a name for the flow as "Flow triggered by Power Apps", and select **Power Apps** as the trigger.

    ![Enter a name for the flow](media/trigger-flow/create-the-power-automate-flow-2.png "Enter a name for the flow")

1. Select **+ New Step**.

    ![Power Apps gets added as the trigger](media/trigger-flow/create-the-power-automate-flow-3.png "Power Apps gets added as the trigger")

1. Enter "Send an email" in the search connections textbox, and select **Send an email (V2)** action.

    ![Enter Send an email in the search connections textbox](media/trigger-flow/create-the-power-automate-flow-4.png "Enter Send an email in the search connections textbox")

1. For the **To** field, select **Add dynamic content** > select **Ask in Power Apps** > select **Sendanemail(V2)_To**.

    ![For the To field, select Add dynamic content](media/trigger-flow/create-the-power-automate-flow-5.png "For the To field, select Add dynamic content")

1. For the **Body** field, select **Add dynamic content** > select **Ask in Power Apps** > select **Sendanemail(V2)_Body**

    ![For the Body field, select Add dynamic content](media/trigger-flow/create-the-power-automate-flow-6.png "For the Body field, select Add dynamic content")

    ![select Ask in PowerApps and then select Sendanemail V2](media/trigger-flow/create-the-power-automate-flow-7.png "select Ask in PowerApps and then select Sendanemail V2")

1. Enter "Thank you for your business!" in the **Subject** field.

    ![Enter Thank you for your business](media/trigger-flow/create-the-power-automate-flow-8.png "Enter Thank you for your business")

1. Save the Power Automate flow, and go back to Power Apps.

## Trigger the flow from within the canvas app

1. Select the **Yes** button > select **Action** > **Power Automate**, and then select the flow created earlier.

    ![Flow triggered by a Powerapp](media/trigger-flow/trigger-the-flow-from-within-the-power-app-1.png "Flow triggered by a Powerapp")

    Function `FlowtriggeredbyaPowerapp.Run(` is also added to the **OnSelect** property.

1. Fill in the two parameters for the To email address and the Body of the email as follows:

    ```powerapps-dot
    FlowtriggeredbyaPowerapp.Run(
       EditForm3.LastSubmit.Email,
       TextInput1.Text
    );
    Navigate(Screen1);
    ```

    > [!NOTE]
    > The email address is picked up from the new account record created on the previous screen. and the body for the email is picked from the text box text captured on this screen.

    ![Fill in the two parameters for the To email address](media/trigger-flow/trigger-the-flow-from-within-the-power-app-2.png "Fill in the two parameters for the To email address")

## Test the app

Run the app in preview mode. In this test, we'll create a new account by entering details like account name, phone number, city, and email address on the **New Account** screen. On saving the new account details, we'll be prompted to send an email to the customer where we can update the verbiage of the email, and then select **Yes** to send the email. This will trigger the flow, and email will be sent to the email address on the account.

![Run the app in Preview mode](media/trigger-flow/test-the-app-1.png "Run the app in Preview mode")

![Create a new account by entering details like account name](media/trigger-flow/test-the-app-2.gif "Create a new account by entering details like account name")

An email like this should appear in your inbox

![Email like this should appear in your inbox](media/trigger-flow/test-the-app-3.png "mail like this should appear in your inbox")

### See also

[Start a flow in canvas apps](../using-logic-flows.md)