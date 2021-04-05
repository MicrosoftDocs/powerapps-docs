---
title: Understand Bulletins app architecture | Microsoft Docs
description: Learn about the architecture of the Bulletins sample app.
author: navjotm
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 03/30/2021
ms.author: namarwah
ms.reviewer: tapanm
---

# Understand Bulletins sample app architecture

In this document, you'll learn about the collections and global variables used by the [Manage Bulletins](bulletins.md#manage-bulletins-app) and [Bulletins](bulletins.md#bulletins-app) apps, understand and how to use them effectively. If you want to learn more about how to install, and use the Bulletins sample app instead, go to [Bulletins sample app](bulletins.md).

## Prerequisites

To understand and use information in this article, you'll need to know about different controls, features, and capabilities of canvas apps.

- [Create and update a collection in a canvas app](canvas-apps/create-update-collection.md)
- [Collect, Clear, and ClearCollect functions in Power Apps](canvas-apps/functions/function-clear-collect-clearcollect.md)
- [Understand canvas-app variables in Power Apps](canvas-apps/working-with-variables.md)
- [Add and configure a canvas-app control in Power Apps](canvas-apps/add-configure-controls.md)
- [Add a screen to a canvas app and navigate between screens](canvas-apps/add-screen-context-variables.md)

## Data model

The following diagram explains the data model used by the Bulletins sample app.

![Bulletins sample app data model](media/bulletins-architecture/data-model.png "Bulletins sample app data model")

## Manage Bulletins app

This section explains collections, and global variables used by the Manage Bulletins app.

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
| colUserImages                     | Collection used to store the **UserImage** and **Username**.                                                    | OnHidden property of Bulletins Screen, FAQs Screen and Links and Contacts screen. |

### Global Variables

Manage Bulletins app uses following global variables.

| Variable Name                   | Type    | Description                                                                 |
|---------------------------------|---------|-----------------------------------------------------------------------------|
| gblAppLoaded                    | Boolean | To check whether the app is completely loaded.                               |
| gblUserLanguage                 | Text    | To check the logged in user’s language.                                      |
| gblPadding                      | Record  | Used to set padding values in the app.                                       |
| gblUser                         | Record  | Variable to get user record for the context.                                     |
| gblUserFirstName                | Text    | Variable to get the first name of the user.                                  |
| gblAppMenu                      | Record  | Variable to store the label, width and the screen name for the menu records. |
| gblAppSetting_inputMobileOnWeb  | Boolean | Variables to scale fonts for mobile-oriented apps, running in desktop devices.       |
| gblAppSetting_inputMobile       | Boolean | Variables to scale fonts for mobile-oriented apps.                           |
| gblAppSetting_inputScaleFontsby | Number  | Use this variable for scaling all fonts by a fixed amount.                   |
| gblThemeDark                    | Boolean | To check whether the Teams theme is set to Dark.                             |
| gblThemeHiCo                    | Boolean | To check whether the Teams theme is set to High Contrast.                    |
| gblAppColors                    | Record  | Variable to set the color value in the app.                                  |
| gblAppSizes                     | Record  | Variable to set the color value in the app.                                  |
| gblAppStyles                    | Record  | Variable to set the styling values in the app.                               |

## App OnStart

This section explains app OnStart collections, variables and execution details.

### OnStart Collections

Collections used during app OnStart:

| Collection name | Description |
| - | - |
| colStockImages | Collection of stock cover images. |
| colLocalization | Collection of localized text based on user’s    language.  |
| colCdsBulletins | Collection to hold bulletins data from Dataverse. |
| colCdsBulletinCategories | Collection to hold bulletin categories data from Dataverse. |
| colCdsBulletinReadReceipts | Collection to hold bulletin read receipts data from Dataverse. |
| colCdsBulletinBookmarks | Cllection to hold bulletin bookmarks data from Dataverse.
| colCdsBulletinUserSettings | Collection to hold bulletin user settings data from Dataverse. |
| colCdsBulletinCategoryPreferences | Collection to hold bulletin category preferences data from Dataverse. |
| colAppNewUserCategories | Collection to store user preferences. |

### OnStart variables

Variables used during app OnStart:

| Variable name | Description |
| - | - |
| gblAppLoaded | Global variable used to check if the app is loaded or not. |
| gblUserLanguage | Global variable which holds the user’s local language. |
| gblPadding | Global variable which holds the padding details of the app. |
| gblUser | Global variable to hold the user record for context. |
| gblUserFirstName | Global variable to hold the first name of the user. |
| gblAppMenu | Global variable to hold the menu details. |

### OnStart execution flow

1. When a User loads the app, **gblAppLoaded** is set to false. The user’s
    language code is stored in **gblUserLanguage**, with English - US being the
    default one.

1. The user’s language is then used to collect localized text used throughout
    the app (e.g. label and button text) in **colLocalization**.

1. As the app loads it collects the data from theDataverse and stores in to the
    collections to use the data across the app. The collections that holds the
   Dataverse data are **colCdsBulletins , colCdsBulletinCategories ,
    colCdsBulletinReadReceipts , colCdsBulletinBookmarks,
    colCdsBulletinUserSettings** and **colCdsBulletinCategoryPreferences.**

1. The stock images are collected to **colStockImages** collection which helps
    the user to pick any images for the bulletin’s cover from the app itself.

1. The menu details on various screens of the app are collected to
    **gblAppMenu** which helps to create menu’s as per the screen.

1. The user preferences are collected to **colAppNewUserCategories,** which
    helps the user to have a personalized experience of the app as it shows the
    bulletins based on the user bulletin category preferences.

## Home screen

### Home screen collections

1. **colCdsBulletins –** collection to hold bulletins data from Dataverse.

1. **colCdsBulletinBookmarks –** collection to hold bulletin bookmarks data
    from Dataverse.

1. **colCdsBulletinCategoryPreferences –** collection to hold bulletin category
    preferences data from Dataverse.

### Home screen variables

1. **gblUser –** global variable to hold the User record for context.

1. **gblUserFirstName –** global variable to hold the First Name of the User.

1. **locVisibleDialog –** local variable used to show and hide the dialog
    pop-up

1. **locVisibleDialogBulletinReader –** local variable used to show and hide a
    bulletin

1. **locBulletinRecord –** local variable used to store the selected bulletin
    record

1. **locBulletinBody –** local variable used to store the selected bulletin’s
    body

### Home screen execution details

1. Using the collections **colCdsBulletins** and
    **colCdsBulletinCategoryPreferences** the screen is loaded with the
    published bulletins.

1. User can search any bulletin by the name or category of the bulletin using
    the search box available on this screen.

1. Based on the search the galleries will be filtered.

1. Once the user selects a bulletin, a dialog pop-up appears using the
    variables **locVisibleDialog** and **locVisibleDialogBulletinReader.**

1. The dialog will show the information of selected bulletin which include
    image, video, body etc.. from the bulletin record using the variables
    **locBulletinRecord** and **locBulletinBody**

1. If the user wants to close the dialog, the user will click on close button
    or the empty space around the dialog in order to set the
    **locVisibleDialog** and **locVisibleDialogBulletinReader** variables to
    false and there by hiding the dialog pop-up.

#### Screens<br>

![](media/bulletins-architecture/bcc2687977225e1b8f882564efa681b5.png)

![](media/bulletins-architecture/512d9dc4f1d134a06202ad09fcce66d9.png)

## FAQ screen 

### FAQ screen collections

**None**

### FAQ screen variables

1. **locVisibleDialog –** local variable used to show and hide the dialog
    pop-up

### FAQ screen execution details

1. This screen will mainly show the information of FAQ’s retrieved from Dataverse
    entities **Bulletin FAQs** and **Bulletin FAQ Categories**

1. User can search the needed FAQ’s using the search box by it’s name and the
    galleries showing these entities will get filtered as per the search.

1. User can use the open icon to open the FAQ in a dialog with the help of
    **locVisibleDialog.** On selecting the close button on the pop-up dialog
    using the variable the dialog will be hidden.

#### Screens<br>

![](media/bulletins-architecture/8abd811949156fadaeb378cb147333c4.png)

![](media/bulletins-architecture/ed1bfa385d5b091f9449705c2f3f7019.png)

## Links and contacts screen

### Links and contacts screen collections

**None**

### Links and contacts screen variables

**None**  


### Links and contacts screen execution details

1. This screen will mainly show the information of FAQ’s retrieved from Dataverse
    entities **Bulletin Link Categories** , **Bulletin Contacts** and **Bulletin
    Link Categories.**

1. User can search the needed **Bulletin Link Categories** , **Bulletin
    Contacts** and **Bulletin Link Categories** by using search box and the
    results will be filtered in the respective galleries

1. Using **launch** function, the links will be opened in a separate browser
    tab.

![](media/bulletins-architecture/eb8761027800310b693551a8b027bdfa.png)
