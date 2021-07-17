---
title: Convert Issue reporting sample app to Work order management app
description: Learn how to rename labels in the Issue reporting sample app for Teams so that the app can be used for other purposes, such as tracking work orders.
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 07/16/2021
author: joel-lindstrom		
ms.author: v-ljoel
ms.reviewer: tapanm
contributors:
  - joel-lindstrom
  - navjotm
  - tapanm-msft
---

# Convert Issue reporting sample app to Work order management app

The Issue Reporting template Power App for Microsoft Teams is designed to be flexible and extendable, including for scenarios other than tracking issues.

For example, in a simple work scheduling scenario, you may want to use it as a work order management app. There are many similarities between issues and work order—assigned users, task descriptions, and due dates.

In this lesson, we'll walk through changing the app to a work order management app.

1. Open the Power Apps app in Teams. We recommend you right-click on the icon for Power Apps in Teams, and pop out the app so you won’t lose your changes if you go somewhere else in Teams.

    ![Pop out Power Apps](media/extend-issue-rename-work-order/pop-out-app.png "Pop out Power Apps")

1. Select the **Build** tab.

1. Select the team in which the app is installed.

1. Select **Installed apps** tab.

1. Select **Issue reporting** in Issue reporting tile.

   ![Select Installed apps](media/extend-issue-rename-work-order/installed-apps.png "Select Installed apps")

   The app will open in the designer with the Landing Screen displayed.

1. Select the text label control under the image that says **Issue Reporting** and expand the formula bar.

## Understanding localization

Before we continue, it's important to understand localization in canvas apps. All text labels in Issue reporting use localization variables to localize text language to eight different languages. If you overwrite this formula with static text, the app won't be localized for other languages.

To maintain localization, create a spreadsheet with these three columns:

- **OOBTextID**&mdash;this is the identifier for the text control.
- **LocalizedText**&mdash;this is the text to display.
- **LanguageTag**&mdash;this is the code for the language.

For example, in the current expression for the label on the Landing Screen sets the OOBTextID of the text label to **lblLoadingText__locText**. Since static data in the app isn't modifiable, we'll choose a new OOBTextID for the control so the original one will no longer be displayed.

The spreadsheet we would import would look like this:

| **OOBTextID**            | **LocalizedText**  | **LanguageTag** |
|--------------------------|--------------------|-----------------|
| lblLoadingText2__locText | Work Order Tracker | en-US           |

Add another rows for each additional language that you'll use, and add rows for each additional control for which you'll be updating the text. Then import to the app. Update the following parts of the expression formula:

![Update formulas](media/extend-issue-rename-work-order/replacement-code.png "Update formulas")

The app loading screen now displays **Work Order Tracker**

![Updated loading screen](media/extend-issue-rename-work-order/work-order-tracker-splash.png "Updated loading screen")

## Update the other screens in the app

Let’s update the other references to **Issue Reporting** to change to **Work order**

## Update Insights screen

1. Select **Tree View** from the left-pane.

1. Select **Insights Screen.**

    ![Select Insights Screen](media/extend-issue-rename-work-order/insights-screen.png "Select Insights screen")

1. Select the **Report an issue** button and select the **Text** property.

1. Following the steps in the previous section, add a row to the spreadsheet for a new OOBTextId with the LocalizedText **Create a Work Order** and update the button text formula to reference the new OOBTextId.

1. Select the **Issues reported by you** text label, and select the **Text** property.

1. Following the steps in the previous section, add a row to the spreadsheet for a new OOBTextId with the LocalizedText **Work orders you created**, and update the text expression to reference the new OOBTextId.

1. The **Last 7 days** area is a component that combines text and dynamic content for record counts. The text is set in the **Items** property. In the area highlighted in the below image there are two text strings, one for singular and the second for plural. Following the steps in the previous section, add a row in the spreadsheet with a new OOBTextIID with localized text, one for Work item and the other for Work items.

    ![Insights screen code](media/extend-issue-rename-work-order/issues-reported-code.png "Insights screen code")

## Update Issue Report screen

The issue report screen is the screen that users see when the create an item, such as an issue or a work order. We'll use the same method to update the field text as we did on the Insights screen.

1. Select the **Tree view**.

1. Select **Issue Report Screen**.

1. Update the following properties:

    1. Change **Select an issue type** Text property to **Select a work order type**.
    1. Change **Submit Issue** button Text property to **Create work order**.

    ![Modified Issue Report screen](media/extend-issue-rename-work-order/issue-report-screen.png "Modified Issue Report screen")

## Update Template Selection Screen

The template selection screen is what users use to select the type of issue. Since we're changing the purpose of the app to a work order tracker, we'll want to change the **Back to issue** link at the top of the screen to say **Back to work order.**

The header of this screen is a component as it is reused between multiple screens.

1. In **Tree view** select **Template Selection Screen**.

1. Select **Back to issue**.

1. Select the **InputHeaderText** property.

1. Change text to **Back to work order**.

## Update Assignment Selection Screen

The assignment selection screen is what users use to select the person to whom the item should be assigned.

1. In **Tree view** select **Assignment Selection Screen**.

1. Select **Back to issue**.

1. Select the **InputHeaderText** property.

1. Change text to **Back to work order**.

## Update Issue Submission Screen

The issue submission screen is the screen that users see after an issue has been submitted. This has a text display control that displays a mixture of localized text and dynamic data for first name.

1. In **Tree view** select **Issue Submission Screen**.

1. Select the text label with the text **Thanks, (first name). Your issue has been reported and should be resolved by”**.

1. In the **HtmlText** property, find this section:

    ![HtmlText property](media/extend-issue-rename-work-order/html.png "HtmlText property")

1. In your spreadsheet, define a new OOBTextId and set the text to

    ```
    Thanks, {0}, your work order has been created.
    ```

    The 0 will be replaced with the first name of the user.

1. Update the highlighted part of the formula to reference your new OOBTextId.

## Rename the Issue Reporting tab

We've now changed all of the references to “issue reporting” in the app, so now we want to change the name of the app so that users will see the correct name in Teams.

1. In Teams, go to the channel in which the app is installed.

2. Right-click on the app tab, and select **Rename**.

3. Change the name of the tab to **Work order tracker**.

   ![Rename the app tab](media/extend-issue-rename-work-order/rename.png "Rename the app tab")

## Rename the app

We'll also want to change the name of the app so that users who select the app for general distribution from the Teams store can find it.

1. Open Issue Reporting in the **Power Apps** app in Teams.

1. In the upper right corner, select the app name.

1. Enter **Work Order Tracker**  and select **Save**.

## Next steps

To complete the scenario, consider making similar changes to the Manage Issues app so that the administrator experience also follows the same logic.

### See also

- [Understand Issue Reporting sample app architecture](issue-reporting-architecture.md)
- [Customize issue reporting app](customize-issue-reporting.md)
- [Sample apps FAQs](sample-apps-faqs.md)
- [Use sample apps from the Teams store](use-sample-apps-from-teams-store.md)

[!INCLUDE[footer-include](../includes/footer-banner.md)]