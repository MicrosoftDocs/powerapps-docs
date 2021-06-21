Contents

[Document Objective	2](#_Toc74830281)

[Introduction	2](#_Toc74830282)

[Data Model	3](#_Toc74830283)

>   [Entities	4](#_Toc74830284)

[Story	5](#_Toc74830285)

>   [App	5](#_Toc74830286)

>   [OnStart	5](#_Toc74830287)

>   [Loading Screen	6](#_Toc74830288)

>   [Home Screen	8](#_Toc74830289)

>   [Displaying the Welcome Dialog	8](#_Toc74830290)

>   [Displaying the Profile screen	10](#_Toc74830291)

>   [Home Screen	11](#_Toc74830292)

>   [Random Match Screen	13](#_Toc74830293)

>   [Connect with someone new	13](#_Toc74830294)

>   [Peer Match Screen	14](#_Toc74830295)

>   [Connect with a peer	14](#_Toc74830296)

>   [Skills Match Screen	15](#_Toc74830297)

>   [Connect with someone by skills	15](#_Toc74830298)

>   [Expert Match Screen	16](#_Toc74830299)

>   [Connect with an Expert	16](#_Toc74830300)

>   [About Screen	17](#_Toc74830301)

>   [Navigation	17](#_Toc74830302)

>   [Body	17](#_Toc74830303)

[Collections	18](#_Toc74830304)

[Global Variables	19](#_Toc74830305)

# Document Objective

This document covers the following pertaining to the How-to solution:

-   Data model and purpose of the various entities used.

-   List of all collections and variables used.

-   Detailed breakdown of each functionality.

# Introduction

How-to app in Teams offer an easy-to-use experience to create the app easily.

Benefits of using the How to app:

-   Understand the basics of Power Apps

-   Design the app

-   Share it with colleagues in Teams

    Become a Maker

# Data Model

## Entities

-   **Item Demo**

    A table to store Items. Details such as Name, Item type, Quantity,
    Description, Created on and when was it created or modified by are stored
    under the Item Demo entity.

-   **Item Checkout Demo**

    Item Checkout Demo stores items that are added to checkout with the checkout
    status.

    Details such as Name, Item, Checkout Status, Checkout Duration, Checkout
    Option, Checkout Reason when the items checkout was created on, modified on
    are stored under Item Checkout Demo entity.

-   **Item Type Demo**

    A Item Type Demo Entity shows type of items records such as Name, checkout
    address, checkout user and when it was created on, Modified on.

# Story

## App

### OnStart

#### Collections involved

| **Collection name** | **Description**                                       |
|---------------------|-------------------------------------------------------|
| colLocalization     | Collection of localized text based on users language. |

#### Variables involved

| **Variable name**     | **Description**                                               |
|-----------------------|---------------------------------------------------------------|
| gblAppLoaded          | - global variable to check if the app has loaded completely.  |
| gblUserLanguage       | - global variable to store the users language.                |
| **gblCurrUserEmail**  | - global variable to store the current user email address     |
| gblCurrUser           | - global variable to store the current user record            |

#### Detailed Steps

1.  When a user accesses the app, **gblAppLoaded** is set to false. The user’s
    language code is stored in **gblUserLanguage**, with English - US being the
    default one.

2.  The user’s language is then used to collect localized text used throughout
    the app (e.g. label and button text) in **colLocalization**.

## Welcome Screen

![](media/eb46e5290638897f9cb053ed62cad85e.png)

#### Collections involved

| **Collection name** | **Description**                                        |
|---------------------|--------------------------------------------------------|
| colLocalization     | collection of localized text based on user’s language. |

#### Variables involved

| **Variable name**               | **Description**                                                                                              |
|---------------------------------|--------------------------------------------------------------------------------------------------------------|
| **gblCurrUserEmail**            | - global variable to store the current user email address                                                    |
| gblThemeDark                    | - global variable to store if Teams is running in dark mode.                                                 |
| gblThemeHiCo                    | - global variable to store if Teams is running in contrast mode.                                             |
| gblAppColors                    | - global variable to store the app design colors                                                             |
| gblAppSizes                     | - global variable to store the app sizes for app in mobile and mobile on web                                 |
| gblAppStyles                    | - global variable to store styling properties for all controls (set on the OnVisible of the Loading Screen). |
| gblAppSetting_inputMobileOnWeb  | - global variable to scale fonts for mobile-oriented apps, running in desktop.                               |
| gblAppSetting_inputMobile       | - global variable to scale fonts for mobile-oriented apps.                                                   |
| gblAppSetting_inputScaleFontsBy | - global variable for scaling all fonts by a fixed amount.                                                   |

#### Detailed steps

1.  If **gblAppStyles** is not blank (which means the styling variable has been
    loaded),

2.  The loading screen will initialize all the global variables like
    **gblAppStyles, gblAppSizes,** gblAppColors to show the screen and color
    settings as per the user setup like dark mode or high contrast mode in Teams
    desktop or in browser

3.  In this screen you will find **Preview App**. Click on it which will
    redirect to Assets Screen

## Items Screen

![](media/d030439a92050d8654943d93ffc6652c.png)

#### Collections involved

| **Variable name** | **Description**                                          |
|-------------------|----------------------------------------------------------|
| colLocalization   | - collection of localized text based on user’s language. |

####   
Variables involved

| **Variable name**        | **Description**                                                                                              |
|--------------------------|--------------------------------------------------------------------------------------------------------------|
| **locShowItems**         | - local variable to show the items based on item type.                                                       |
| **locSelectedItemType**  | - local variable to show the selected item types                                                             |
| **gblThemeDark**         | - global variable to store if Teams is running in dark mode.                                                 |
| **gblThemeHiCo**         | - global variable to store if Teams is running in contrast mode.                                             |
| gblAppColors             | - global variable to store the app design colors                                                             |
| **gblAppStyles**         | - global variable to store styling properties for all controls (set on the OnVisible of the Loading Screen). |

#### Detailed steps

1.  The items screen will show Item types with the number of items available
    under each item which are stored in galItemTypes_Demo.

2.  The items will be show in galItems_Demo when user select any of the itemtype
    in galItemTypes_Demo.

## Checkout Screen

![](media/16e97c5f4570579838a294c9b15ddbd9.png)

![](media/b94e51d97ba66cc0c0b63acec040e70f.png)

#### Collections involved

| Collections     | Description                                            |
|-----------------|--------------------------------------------------------|
| colLocalization | collection of localized text based on user’s language. |

#### Variables involved

| Variable name               | Description                                                            |
|-----------------------------|------------------------------------------------------------------------|
| gblAppStyles                | global variable to store styling properties for all controls           |
| gblThemeDark                | global variable to store if Teams is running in dark mode              |
| locShowCheckoutConfirmation | local variable to show the connection by randomly shuffling the userid |
| gblAppColors                | global variable to store the app design colors                         |
| gblThemeHiCo                | global variable to store if Teams is running in contrast mode.         |
| locSelectedItem             | global variable to store the current user email address                |

#### Detailed steps

1.  When user selects any of the item which are needed, they can click on
    checkout based on availability of the item which are stored in
    locSelectedItem item.

2.  Once the item is checked out the confirmation message will be shown from
    locShowCheckoutConfirmation.

## My Checkout Screen

![](media/fb3dbca28066cdb97017bfad8cc625bc.png)

![](media/c47d9d224be9b7e2c0c3f7b9af07fba8.png)

#### Collections involved

| Variable name    | Description                                            |
|------------------|--------------------------------------------------------|
| colLocalization  | collection of localized text based on user’s language. |

#### Variables involved

| Variable name             | Description                                                                                                |
|---------------------------|------------------------------------------------------------------------------------------------------------|
| gblAppStyles              | global variable to store styling properties for all controls (set on the OnVisible of the Loading Screen). |
| gblThemeDark              | global variable to store if Teams is running in dark mode.                                                 |
| gblThemeHiCo              | global variable to store if Teams is running in contrast mode.                                             |
| gblAppColors              | global variable to store the app design colors                                                             |
| locShowReturnConfirmation | Local variable to show the return confirmation message when user click on return button                    |
| locSelectedItemType       | local variable to show the selected item types                                                             |
| locShowItems              | local variable to show the items based on item types                                                       |
| gblCurrUser               | global variable to store the current user record                                                           |
| locSelectedItemForReturn  | local variable to return the selected item back to items                                                   |

#### Detailed steps

1.  All the items checked out by the user will be show in this screen. The user
    will have option to return and show the days due for return

2.  Once user clicks on return the item will be returned back to items screen.

# Collections 

| Collection Name | Description                                                        | Screen Used                 |
|-----------------|--------------------------------------------------------------------|-----------------------------|
| colLocalization | Used to build a Localization Collection based on the User Language | OnStart property of the App |

# Global Variables 

| Variable Name                   | Type    | Description                                                           |
|---------------------------------|---------|-----------------------------------------------------------------------|
| gblUserLanguage                 | Text    | To check the logged in User’s Language                                |
| gblThemeDark                    | Boolean | To check whether the Teams theme is set to Dark                       |
| gblThemeHiCo                    | Boolean | To check whether the Teams theme is set to High Contrast              |
| gblAppSetting_inputMobileOnWeb  | Boolean | Variables to Scale fonts for mobile-oriented apps, running in desktop |
| gblAppSetting_inputScaleFontsby | Number  | Use this variable for scaling all fonts by a fixed amount             |
| gblAppSetting_inputMobile       | Boolean | Variables to Scale fonts for mobile-oriented apps                     |
| gblAppColors                    | Record  | Variable to set the Color value in the app                            |
| gblAppSizes                     | Record  | Variable to set the Color value in the app                            |
| gblAppStyles                    | Record  | Variable to set the Styling values in the app                         |
| gblCurrUserEmail                | Record  | gblCurrUserEmail                                                      |
| gblCurrUser                     | Record  | global variable to store the current user record                      |
