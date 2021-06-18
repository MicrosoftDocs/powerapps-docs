---
title: How to customize the Bulletins app
description: Learn about how the Buleltins sample apps can be customized
author: sbahl10
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 06/18/2021
ms.author: v-shrutibahl
ms.reviewer: tapanm
contributors:
    - v-ljoel
---

# How to customize the Bulletins app

The Bulletins Power App template for Microsoft Teams is designed to be a complete app experience as well as allowing makers to easily extend it for their own purposes. In this guide we will go over how to customize the Bulletins app in Power Apps in Microsoft Teams.

Before you can customize the app, you must install it from the Teams store. You can get the app at <https://aka.ms/TeamsBulletins> .

Once the app is installed you can then customize the app using the following steps:

## Opening Power Apps app in Microsoft Teams

1.  In Microsoft Teams, select the **…** button from the left menu.

2.  Type **Power Apps** in the search field.

    ![Search for Power Apps](media/customize-bulletins/search-power-apps.png "Search for Power Apps")

3.  Select the Power Apps app from the list to open the app. Power Apps will open inside of teams
    
4. Right click on the **Power Apps** logo and select **Pin** to lock the app to the side menu so it is easy to get to in the future.

![Power Apps icon on](media/customize-bulletins/power-apps-icon-left-navigation-menu.png)

5. It is recommended that you “pop out” Power Apps so that if you need to navigate  somewhere else in Microsoft Teams you won’t lose your app configuration. To pop out the Power Apps app, right mouse click on the Power Apps logo and select **Pop out app**.
6. Now that you have loaded the Power Apps app, select **Build**.
7. This screen will show all the teams that have Power Apps installed in them.
8. Select the team in which you installed the Bulletins app.

9. Select **Installed apps.** This will show all apps installed in the Team.

10. Bulletins solution includes two apps: **Bulletins** for users to view and bookmark communication, and **Manage bulletins** for managers to use to
    create Bulletins, FAQ’s, and links or contacts, as well as view metrics for bulletin read and bookmark statistics.

11. Select **See all** in the **Bulletins** tile.

![See all option on the Bulletins tile](media/customize-bulletins/installed-apps-see-all-option.png "See all option on the Bulletins tile")

6.  You will now see all of the apps, tables, flows, and chatbots in the Bulletin solution.
    
    ![All Bulletins app Objects list](media/customize-bulletins/bulletins-app-objects-list.png "All Bulletins app Objects list")

## Extend the Bulletins data model

If you are modifying or adding any fields to your app, you will want to first update or add these columns in their Dataverse tables. In this section we will
explore the data model for Bulletins and how to modify it in Power Apps in Microsoft Teams. Below is the data model for Bulletins.

![Data model](media/customize-bulletins/data-model.png "Data model")

Before modifying the fields, you need to first decide where the fields you want to add should go. What are the users doing when they should see or interact with these fields?

-   Bulletin table (msft_bulletin) is where bulletin data is stored

-   Bulletin Bookmark (msft_bulletin_bookmark) records are created when a user bookmarks a bulletin.
    
-   Bulletin Category (msft_bulletin_category) is a lookup table for bulletin categories.
    
-   Bulletin Category Preference (msft_bulletin_categorypreference) stores the category sort and display preferences.
    
-   Bulletin Read Receipt (msft_bulletin_readreceipt) records are created when a user reads a bulletin records.
    
-   Bulletin FAQ (msft_bulletin_faq) stores FAQ records.

-   Bulletin FAQ Category (msft_bulletin_faqcategory) stores the categories for FAQ’s.
    
-   Bulletin Link (msft_bulletin_link) stores link data for links/contacts.

-   Bulletin Contact (msft_bulletin_contact) stores contact data for links/contacts.
    
-   Bulletin Link Category (msft_bulletin_linkcategory) stores categories for links and contacts.
    
-   Bulletin User Setting (msft_bulletin_usersetting) record stores user settings for Bulletins.

## Bulletins Screens

From the list of apps, chatbots, flows, and tables, select the **Bulletins** app.

![Select Bulletins from the solution](media/customize-bulletins/bulletins-objects-bulletins-app-selected.png "Select Bulletins from the solution")

Now that Bulletins is open in Power Apps in Microsoft Teams, select the **Tree View**.

![Bulletins app tree view](media/customize-bulletins/bulletins-app-tree-view.png "Bulletins app tree view")

From the Tree View you can see the screens included in the app. Selecting the arrow to the left of a screen will expand the contents of the screen, giving you access to the components of the screen, including galleries, buttons, text labels, and text input controls.

The following are the screens in Bulletins:

| **Screen**                | **Description**                                                                                                                                                                      |
|---------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Landing Screen            | This screen displays an image with the app title as the app is loading.                                                                                                              |
| Hidden Admin Screen       | This is a helper screen for admins to try and understand the way that theming works in the app and support for dark mode and high contrast. This screen is not visible to app users. |
| Home Screen               | This is the first screen that users see after the landing screen, which provides visibility for Bulletins.                                                                           |
| FAQ’s Screen              | This screen is visible when a user navigates to the FAQ tab.                                                                                                                         |
| Links and Contacts Screen | This screen displays links and contact records.                                                                                                                                      |

## Manage bulletins Screens

Now let’s look at the screens in the **Manage bulletins** app:

1.  In the Power Apps app, select the **Build** tab

2.  Select the team in which you installed the Bulletins app.

3.  Select **Installed apps.** This will show all apps installed in the Team.

4.  Select **Manage bulletins** in the **Bulletins** tile.

    ![Select Manage Bulletins from the Bulletins tile](media/customize-bulletins/select-manage-bulletins-app.png "Select Manage Bulletins from the Bulletins tile")

5.  Manage bulletins will open in the designer.

6.  Select the **Tree view** and review the screens in the Manage bulletins app.

![Manage Bulletins app tree view](media/customize-bulletins/manage-bulletins-app-tree-view.png "Manage Bulletins app tree view")

The following are the screens in the Manage bulletins app:

| Screen                        | Description                                                                                                                                                                          |
|-------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Landing Screen                | This screen displays an image with the app title as the app is loading.                                                                                                              |
| Hidden Admin Screen           | This is a helper screen for admins to try and understand the way that theming works in the app and support for dark mode and high contrast. This screen is not visible to app users. |
| Bulletins Screen              | This is the first screen that users see after the landing screen, which displays bulletin records.                                                                                   |
| Bulletins Detail Screen       | This screen is used toe create or update bulletin records.                                                                                                                           |
| Bulletin Overview Screen      | This screen displays metrics about a bulletin, including number of views and bookmarks.                                                                                              |
| FAQ’s Screen                  | This screen displays FAQ records.                                                                                                                                                    |
| FAQ Detail Screen             | This screen is used to edit and create FAQ records.                                                                                                                                  |
| Links and Contacts Screen     | This screen displays links and contacts.                                                                                                                                             |
| Link Detail Screen            | This screen is used to edit or create links.                                                                                                                                         |
| Contact Detail Screen         | This screen is used to edit or create contacts.                                                                                                                                      |
| About Screen                  | This screen provides more details about the app and links to learning resources and app configuration.                                                                               |
| Settings Screen               | Settings provides access to create or modify categories for bulletins, FAQ’s, and links.                                                                                             |
| Mobile Bulletins Screen       | This is the first screen that users see after the landing screen, which displays bulletin records on mobile.                                                                         |
| Mobile Bulletin Detail Screen | This screen is used to specify properties of bulletin records while using the app on mobile.                                                                                         |
| Mobile Bulletin Entry Screen  | This screen is used to enter bulletin data while using the app on mobile.                                                                                                            |
| Mobile FAQs Screen            | This screen displays FAQ records while using the app on mobile.                                                                                                                      |
| Mobile FAQ Detail Screen      | This screen is used to edit and create FAQ records while using the app on mobile.                                                                                                    |
| Mobile Links Screen           | This screen displays links while using the app on mobile.                                                                                                                            |
| Mobile Link Detail Screen     | This screen is used to edit or create links while using the app on mobile.                                                                                                           |
| Mobile Contacts Screen        | This screen is displays contacts while using the app on mobile.                                                                                                                      |
| Mobile Contact Detail Screen  | This screen is used to edit or create contacts while using the app on mobile.                                                                                                        |

## Common customization scenarios:

In this section we discuss common customization/extension scenarios for Bulletins, and where you would make these changes.

### Send an alert when a new FAQ is posted

If you want to be notified when a new FAQ is published, you could do so with a Power Automate flow running when a row is added to the Bulletin FAQ table.

### Add contact phone in Links and Contacts section

By default, contacts in Bulletins do not include phone number. Add a phone number column to the Bulletin Contacts table and add the phone number to the Contact Detail Screen and Mobile Contacts Screen. For more details see **Add contact phone in Links and Contacts** **section**  (insert link).

### Add **notify me** settings to a category

If users wanted to be notified when a new bulletin was posted in a category, you can create a flow to notify them when a new bulletin is posted.

For more details see **Add notify me settings to category**.

## Publish changes

When you are done making modifications to the apps, select **Save** to save your changes**.**

>   ![Save button](media/customize-bulletins/save-button.png "Save button")

-   To preview your changes, select the ![Preview button](media/customize-bulletins/preview.png "Preview button") button
    -   The app will launch in preview mode, where you can test the user experience when running the app

    -   To exit preview mode, press **Escape** on your keyboard or select the **X** in the upper right corner

![Close button](media/customize-bulletins/close-button.png "Close button")

-   To publish your app changes, select the ![Publish button](media/customize-bulletins/publish-to-teams.png "Publish button") button
    
-   Publishing the app makes your changes visible to users of the app

-   A dialog will open confirming that you want to publish

    ![Confirm publishing to Teams](media/customize-bulletins/confirm-publishing-to-teams.png "Confirm publishing to Teams")

-   To change app settings, such as icon and background color, select **Edit details**

-   To publish the app, select **Next**

-   On the next screen, confirm the channel you want the app to appear. You can add to other channels in the Team by pressing the **+** button

    ![Add to Channel](media/customize-bulletins/add-to-channel.png "Add to channel")

-   To complete publishing your changes, select **Save and close**

## Customization considerations

Before modifying the Bulletins app, consider the following items:

-   Where are my table customizations? Columns and tables added by you will go to **built by this team** section of the Power Apps app. You can also add new tables in the **See all** area.

![Select See all option to view objects built by the team](media/customize-bulletins/list-of-items-built-by-the-team.png "Select See all option to view objects built by the team")

-   Changes made to an app will be added as a new version of the app. If you get a new version from store, your customizations will not be overridden. You will get a new version that has the latest features, but the new version will not be published.

    For example, if you make changes to the Bulletins app, then you install the latest version from the Teams store, your urgent field will still be visible
    in the app after the upgrade.

    ![Add Bulletins app to a team](media/customize-bulletins/bulletins-app-add-to-team.png "Add Bulletins app to a team")

Figure 1 After upgrading the solution your current app version will still be "live."

>   The updated version of the app is available from the version history of the app. Selecting **Details** from the app list will display the versions of
>   the app and allow you to publish the new version.

>   ![Bulletins app details](media/customize-bulletins/bulletins-app-details.png "Bulletins app details")

>   ![App versions](media/customize-bulletins/app-versions.png "App versions")

Figure 2 The new version is installed, but is not live. You can publish the new version if you want to overwrite your changes.

-   When customizing the app, pop out the Power Apps app in Teams so you don’t lose your changes when you navigate to other parts of Microsoft Teams.
    
-   The app theming has been developed to support dark and high contrast mode in Microsoft Teams. Changing the fill color of screens may break dark and high contrast modes.

