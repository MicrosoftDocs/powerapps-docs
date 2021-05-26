---
title: Understand Bulletins sample app architecture
description: Learn about the architecture of the Bulletins sample app.
author: navjotm
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 05/24/2021
ms.author: namarwah
ms.reviewer: tapanm
contributors:
  - joel-lindstrom
  - navjotm
  - tapanm-msft
---

# Understand Bulletins sample app architecture

In this article, you'll learn about the collections and global variables used by the [Manage Bulletins](bulletins.md#manage-bulletins-app) and [Bulletins](bulletins.md#bulletins-app) apps, and understand how to use them effectively. If you want to learn more about how to install, and use the Bulletins sample app instead, go to [Bulletins sample app](bulletins.md).

## Prerequisites

To understand and use information in this article, you'll need to know about different controls, features, and capabilities of canvas apps.

- [Create and update a collection in a canvas app](../maker/canvas-apps/create-update-collection.md)
- [Collect, Clear, and ClearCollect functions in Power Apps](../maker/canvas-apps/functions/function-clear-collect-clearcollect.md)
- [Understand canvas-app variables in Power Apps](../maker/canvas-apps/working-with-variables.md)
- [Add and configure a canvas-app control in Power Apps](../maker/canvas-apps/add-configure-controls.md)
- [Add a screen to a canvas app and navigate between screens](../maker/canvas-apps/add-screen-context-variables.md)

You'll also need to know about how to [install](use-sample-apps-from-teams-store.md), and [use](bulletins.md) Bulletins sample app.

## Data model

The following diagram explains the data model used by the Bulletins sample app.

![Bulletins sample app data model](media/bulletins-architecture/data-model.png "Bulletins sample app data model")

## Manage Bulletins app

This section explains collections, and global variables used by the [Manage Bulletins](bulletins.md#manage-bulletins-app) app.

### Collections

Manage Bulletins app uses following collections.

| Collection name                   | Description                                                                                            | Where used                                                                      |
|-----------------------------------|--------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| colAppNewUserCategoies            | App only collection, indicating a new user category was added.                                          | App OnStart                                                      |
| colCdsBulletinCategoryPreferences | Collection to collect the User’s category preferences from the **My Bulletin Category Preferences** view. | App OnStart                                                      |
| colCdsBulletinUserSettings        | Collection to collect the User setting record from the **My Bulletin Category Preferences** view.           | App OnStart                                                      |
| colCdsBulletinBookmarks           | Collection to collect the bookmarked bulletins record from the **My Bulletin bookmarks** view.              | App OnStart                                                      |
| colCdsBulletinReadReceipts        | Collection to collect the read receipts record from the **My Bulletin Read Receipts** view.                 | App OnStart                                                      |
| colCdsBulletinCategories          | Collection to collect the active bulletin categories from the **Active Bulletin** categories.               | App OnStart                                                      |
| colCdsBulletins                   | Collection to collect the list of published bulletins from the **Publication Group: Published** view.       | App OnStart                                                      |
| colStockImages                    | Collection to collect the stock images used in the app.                                                 | App OnStart                                                      |
| colLocalization                   | Used to build a localization collection based on the user language.                                     | App OnStart                                                      |
| colUserImages                     | Collection used to store the **UserImage** and **Username**.                                                    | OnHidden property of Bulletins Screen, FAQs Screen, and Links and Contacts screen. |

### Global Variables

Manage Bulletins app uses following global variables.

| Variable Name                   | Type    | Description                                                                 |
|---------------------------------|---------|-----------------------------------------------------------------------------|
| gblAppLoaded                    | Boolean | To check whether the app is loaded completely.                               |
| gblUserLanguage                 | Text    | To check the logged in user’s language.                                      |
| gblPadding                      | Record  | Used to set padding values in the app.                                       |
| gblUser                         | Record  | Variable to get user record for the context.                                     |
| gblUserFirstName                | Text    | Variable to get the first name of the user.                                  |
| gblAppMenu                      | Record  | Variable to store the label, width, and the screen name for the menu records. |
| gblAppSetting_inputMobileOnWeb  | Boolean | Variables to scale fonts for mobile-oriented apps, running in desktop devices.       |
| gblAppSetting_inputMobile       | Boolean | Variables to scale fonts for mobile-oriented apps.                           |
| gblAppSetting_inputScaleFontsby | Number  | Use this variable for scaling all fonts by a fixed amount.                   |
| gblThemeDark                    | Boolean | To check whether the Teams theme is set to Dark.                             |
| gblThemeHiCo                    | Boolean | To check whether the Teams theme is set to High Contrast.                    |
| gblAppColors                    | Record  | Variable to set the color value in the app.                                  |
| gblAppSizes                     | Record  | Variable to set the color value in the app.                                  |
| gblAppStyles                    | Record  | Variable to set the styling values in the app.                               |

## Bulletins app

This section explains collections, global variables used by the  [Bulletins](bulletins.md#bulletins-app) app, and the execution details for each screen.

### App OnStart

This section explains app OnStart collections, variables, and execution details.

#### OnStart collections

Collections used during app OnStart:

| Collection name | Description |
| - | - |
| colStockImages | Collection of stock cover images. |
| colLocalization | Collection of localized text based on user’s    language.  |
| colCdsBulletins | Collection to hold bulletins data from Dataverse. |
| colCdsBulletinCategories | Collection to hold bulletin categories data from Dataverse. |
| colCdsBulletinReadReceipts | Collection to hold bulletin read receipts data from Dataverse. |
| colCdsBulletinBookmarks | Collection to hold bulletin bookmarks data from Dataverse.
| colCdsBulletinUserSettings | Collection to hold bulletin user settings data from Dataverse. |
| colCdsBulletinCategoryPreferences | Collection to hold bulletin category preferences data from Dataverse. |
| colAppNewUserCategories | Collection to store user preferences. |

#### OnStart variables

Variables used during app OnStart:

| Variable name | Description |
| - | - |
| gblAppLoaded | Global variable used to check if the app is loaded or not. |
| gblUserLanguage | Global variable that holds the user’s local language. |
| gblPadding | Global variable that holds the padding details of the app. |
| gblUser | Global variable to hold the user record for context. |
| gblUserFirstName | Global variable to hold the first name of the user. |
| gblAppMenu | Global variable to hold the menu details. |

#### OnStart execution details

1. When a User loads the app, the **gblAppLoaded** variable is set to false. The user’s language code is stored in the **gblUserLanguage** variable, with "English - US" as the default.

1. The user’s language is then used to collect localized text used throughout the app (such as label and button text) in the **colLocalization** collection.

1. While continuing to load, the app collects the data from Dataverse, and stores it into the following collections.

    - colCdsBulletins
    - colCdsBulletinCategories
    - colCdsBulletinReadReceipts
    - colCdsBulletinBookmarks
    - colCdsBulletinUserSettings
    - colCdsBulletinCategoryPreferences

1. The stock images are collected to the **colStockImages** collection that helps the user to pick any images for the bulletin’s cover.

1. The menu details on various screens of the app are collected to
    the **gblAppMenu** variable that helps to create the menu as per the screen.

1. The user preferences are collected to the **colAppNewUserCategories** collection that  helps the user to have a personalized experience of the app as it shows the bulletins based on the user bulletin category preferences.

### Home screen

This section explains app home screen collections, variables, and execution details.

#### Home screen collections

Collections used by the home screen:

| Collection name | Description |
| - | - |
| colCdsBulletins | Collection to hold bulletins data from Dataverse. |
| colCdsBulletinBookmarks | Collection to hold bulletin bookmarks data from Dataverse. |
| colCdsBulletinCategoryPreferences | Collection to hold bulletin category preferences data from Dataverse. |

#### Home screen variables

Variables used by the home screen:

| Variable name | Description |
| - | - |
| gblUser | Global variable to hold the User record for context. |
| gblUserFirstName | Global variable to hold the first name of the user. |
| locVisibleDialog | Local variable used to show and hide the dialog pop-up. |
| locVisibleDialogBulletinReader | Local variable used to show and hide a bulletin. |
| locBulletinRecord | Local variable used to store the selected bulletin record. |
| locBulletinBody | Local variable used to store the selected bulletin’s  body. |

#### Home screen execution details

1. Using the collections **colCdsBulletins** and
    **colCdsBulletinCategoryPreferences**, the screen is loaded with the
    published bulletins. More information: [Understand the Bulletins app user interface](bulletins.md#understand-the-bulletins-app-user-interface)

1. User can search any bulletin by the name or category of the bulletin using
    the search box available on this screen.

1. Galleries are filtered depending on the search terms.

1. Once the user selects a bulletin, a dialog pop-up shows using the
    variables **locVisibleDialog** and **locVisibleDialogBulletinReader.**

1. The dialog shows the information of selected bulletin that includes
    image, video, and body from the bulletin record using the variables
    **locBulletinRecord** and **locBulletinBody**. More information: [View a post](bulletins.md#view-a-post)

1. To close the dialog, user can select the close button, or the empty space around the dialog. This action sets the
    **locVisibleDialog** and **locVisibleDialogBulletinReader** variables to *false* hiding the dialog pop-up.

### FAQs screen

This section explains app FAQs screen collections, variables, and execution details.

#### FAQs screen collections

FAQs screen doesn't use any collections.

#### FAQs screen variables

Variables used by the home screen:

| Variable name | Description |
| - | - |
| locVisibleDialog | Local variable used to show and hide the dialog pop-up. |

#### FAQs screen execution details

1. This screen will mainly show the information of FAQs retrieved from Dataverse&mdash;**Bulletin FAQs** and **Bulletin FAQ Categories**.

1. User can search the needed FAQs using the search box by its name and the galleries showing these entities will get filtered as per the search.

1. User can use the open icon to open the FAQ in a dialog with the help of **locVisibleDialog** variable. Upon selecting the close button on the pop-up dialog using the variable, the dialog will become hidden.

More information: [View frequently asked questions (FAQs)](bulletins.md#view-frequently-asked-questions-faqs)

### Links and contacts screen

This section explains the Links and contacts screen collections, variables, and execution details.

#### Links and contacts collections

Links and contacts screen doesn't use any collections.

#### Links and contacts screen variables

Links and contacts screen doesn't use any variables.

#### Links and contacts screen execution details

1. Links and contacts screen shows the information of FAQs retrieved from Dataverse&mdash;**Bulletin Link Categories**, **Bulletin Contacts**, and **Bulletin Link Categories**.

1. User can search the needed **Bulletin Link Categories, **Bulletin Contacts**, and **Bulletin Link Categories** by using search box and the results will be filtered in the respective galleries.

1. Using **launch** function, the links will be opened in a separate browser tab.

More information: [View links and contacts](bulletins.md#view-links-and-contacts)

### See also

[Bulletins sample app (Preview)](bulletins.md) <br>
[Use sample apps from the Microsoft Teams store](use-sample-apps-from-teams-store.md) <br>
[Customize sample apps installed from Teams store](customize-sample-apps.md) <br>
[Frequently Asked Questions (FAQs) for sample apps](sample-apps-faqs.md)
