---
title: How to use a model-driven app on a mobile device | Microsoft Docs
description: Learn how to use a custom model-driven app on a mobile device.
author: sericks007
manager: tapanm-MSFT

ms.component: pa-user
ms.topic: quickstart
ms.date: 11/18/2022
ms.subservice: mobile
ms.author: sericks
ms.custom: ""
ms.reviewer: ""
ms.assetid: 
search.audienceType: 
  - enduser
search.app: 
  - PowerApps
  - D365CE
---

# Use model-driven apps on Power Apps mobile

Use Power Apps mobile to run model-driven apps on your mobile device. For more information about how to install and get started with an app, see [Install Power Apps mobile](run-powerapps-on-mobile.md).

> [!IMPORTANT]
> Model-driven apps for Dynamics 365 Sales, Dynamics 365 Customer Service, and Dynamics 365 Field Service don't run in Power Apps mobile. Instead, you use the Dynamics 365 for phones and tablets app. For more information, see [User Guide for Dynamics 365 for phones and tablets](/dynamics365/mobile-app/user-guide-mobile-app).

> [!IMPORTANT]
> In order to use your model-driven app in the Power Apps mobile app, your app maker must have set the **Primary mobile player** setting to **Power Apps mobile.** For more information, see [Manage model-driven app settings in the app designer](../maker/model-driven-apps/app-properties.md).

## Home screen 

It's easy to get around in Power Apps mobile. The following illustration shows the primary navigation elements on the Home screen. 

![Navigation controls, expanded view.](media/home_screen_iphone.png "Navigation controls, expanded view")

Legend:

1. **Site map**: Open the menu and move between apps, get to your favorite and recently used rows, access settings, and more.
2. **Search**: Search for app rows in Microsoft Dataverse.
3. **New**: Create a new row and quickly enter almost any type of information into the system.
4. **Assistant**: Use the assistant to monitor and track daily actions and communications. It helps you stay on top of your day with insight cards that are displayed prominently throughout the app to provide tailored and actionable insights.

## Site map 

From the Home screen, select the site map ![Site map icon.](media/pa_mobile_sitemap_icon.png "Site map icon") to access tables, favorite or most-used rows, other apps, and settings.

Your site map might look different if your app maker has customized the navigation bar to show or hide the **Home**, **Recent**, **Pinned** buttons in the site map. An app maker can also make groups collapsible. For more information, see [Hide or show the Home, Pinned, Recent, and collapsible groups](../user/navigation.md#hide-or-show-the-home-pinned-recent-and-collapsible-groups).
 
   > [!div class="mx-imgBorder"]
   > ![Site map screen.](media/go_to_sitemap_iphone.gif "This image demonstrates how to get to the site map screen")
   


The following illustration shows the primary navigation elements on the site map screen. 


![Site map and navigation.](media/site_map_iphone.png "Site map and navigation")

Legend

1. **App selector**: Open this menu to close your app and switch to another app.
2. **Home screen**: Select this to go back to the Home screen.
3. **Profile**: Go to the Profile screen to sign out or reconfigure the app. 
4. **Recent rows**: View a list of rows you were recently using. 
5. **Pinned rows**: View and open your favorite (pinned) rows. 
6. **Table navigator**: This area lists the table available in the app.
7. **Help**: Access help content for more information about how to use Power Apps mobile.
8. **Offline status**: Work with your data in offline mode, even when you don't have internet access. More information: [Work offline on your mobile device](/dynamics365/mobile-app/work-in-offline-mode)
9. **Settings**: Access settings.

## Pin favorite rows

The **Pinned** and **Recent** lists provide quick access to rows that you've recently used or pinned to favorites. Use the **Recent** list to pin favorite rows.  

1. From the site map ![Site map icon](media/pa_mobile_sitemap_icon.png "Site map icon"), select **Recent** ![Recent row icon](media/pa_mobile_recent_icon.png "Recent rows icon").

2. On the **Recent** rows screen, select the push-pin icon next to a row to add it to your favorites (pinned rows).

3. To view the newly pinned rows, select **X**, and then select **Pinned** ![Pinned favorites icon.](media/mobile_pinned_favs_icon.png "Pinned favorites icon").

   
   > [!div class="mx-imgBorder"]
   > ![Pin a row to favorites.](media/pin_to_fav.gif "This image demonstrates how to pin favorite rows")
   

### Unpin a row

1. From the site map ![Site map icon](media/pa_mobile_sitemap_icon.png "Site map icon"), select **Pinned** ![Pinned favorites icon](media/mobile_pinned_favs_icon.png "Pinned favorites icon").

2. Select the remove-pin icon ![Remove pin icon.](media/pa_mobile_remove_pin_icon.png "Remove pin icon") next to a row to remove it from favorites (pinned rows).


   > [!div class="mx-imgBorder"]
   > ![Unpin a row.](media/unpin_favs.gif "This image demonstrates how to unpin a row")
   

## Change views

- From the Home screen, select the down arrow ![Change view icon.](media/mobile_view_selector_icon.png "Change view icon") next to the current view, and then select a new view.


   > [!div class="mx-imgBorder"]
   > ![Change views.](media/change_views_iphone.gif "This image demonstrates how to select a different view")


## Add a row quickly

1. From the Home screen, select **New** ![Create row button.](media/pa1_create-record-button.png "Create row button").
2. Fill in the columns, and then select **Save**.
3. After the row is created, you can view the new row. 

   > [!div class="mx-imgBorder"]
   > ![Create a row.](media/pamobile_add_record_1.gif "This image demonstrates how create a new row")


-  To save and open the row that you created, select **More** ![More commands icon.](media/pa_mobile_more_commands_icon.png "More commnads icon"), and then select **Save and Open**.

- To save and create another row, select **More** ![More commands icon.](media/pa_mobile_more_commands_icon.png "More commands icon"), and then select **Save and Create new**.


   > [!div class="mx-imgBorder"]
   > ![Save and create another row.](media/pa_mobile_save_create_new.gif "This image demonstrates how to save a row and open it or save and create a new row")


## Sort rows

**Sort in ascending or descending order**: From a list view, select the arrow to sort the list in ascending or descending order.
 
   > [!div class="mx-imgBorder"]
   > ![Sorta rows by ascending or descending order.](media/sort-arrow.png "Sorta rows by ascending or descending order")

**Sort by field**: Select the current **Sort by** field and then select another field to sort by.

   > [!div class="mx-imgBorder"]
   > ![How to sort rows.](media/sort-rows-1.gif "This image demonstrates how to sort rows")
 
## Access the actions menu

From a list view, swipe left to access the actions menu for a row.

   > [!div class="mx-imgBorder"]
   > ![How to access actions for a row.](media/row-actions.gif "This image demonstrates access actions for a row")

>[!NOTE]
> The Flow actions menu in Power Apps mobile doesn't support flows created in a solution.
 
## Access more commands (Android)

1. From the Home screen, open a row.
2. On the open row, select **More** ![More row commands icon."](media/access_record_commands_icon.png "More row commands icon") to access more commands.


   > [!div class="mx-imgBorder"]
   > ![Commands on a row.](media/pa_mobile_view_record_commands.gif "This image demonstrates how to access more commands on a row")


## Edit a row

1. From the Home screen, open a row that you want to edit. 
2. When you're done editing the row, select **Save**. To cancel your changes, select **Discard**.


   > [!div class="mx-imgBorder"]
   > ![Edit a row.](media/save_on_iphone.gif "This image demonstrates how to edit and then save a row")



## Go back to the Home screen

- To get back to the Home screen when you're in a row, select **Back** ![Back icon.](media/pa_mobile_back_icon.png "Back icon").
- At any point, press and hold **Back** ![Back icon.](media/pa_mobile_back_icon.png "Back icon") to go back to the Home screen. 

   > [!div class="mx-imgBorder"]
   > ![Go back to the Home screen.](media/go_back_home.gif "This image demonstrates how to go back to the home screen by pressing and holding the back icon")


## Sign out

From the site map ![Site map icon](media/pa_mobile_sitemap_icon.png "Site map icon"), select the profile icon ![Profile icon](media/profile_icon.png "Site map icon"), and then select **Sign out**.

## Enhancements  (preview)

[This section has pre-release documentation and is subject to change.]

This section describes enhancements that have been made to model-driven apps on mobile devices.

### Lock tabs at the top of forms
Your app maker can choose to lock the tabs at the top of a form so they are always visible while users scroll through the data on the form.

![Tabs are locked at the top of the form.](media/Lock-tabs.png "Tabs are locked at the top of the form.")

Your app maker can turn on this feature. For more inforamtion, see [Features](../maker/model-driven-apps/app-properties.md#features).

### Mobile commanding improvements

Your app maker can enable [Mobile commanding improvements](../maker/model-driven-apps/app-properties.md#features) to provide easy access to contextual commands when you're using Power Apps mobile. Here's a list of improvements:

- The **Delete** command on a grid page is automatically hidden when a row is not selected thus, making room for other commands. When one or more rows is selected the **Delete** command is automatically displayed.
  
- The **Process** command is hidden when there's no process enabled for a table. Removing a nonfunctional command makes room for other commands. 

  | Before | After |
  | :---:         |     :---:      |
  | ![Old process command.](media/process.png "Process command shown.")| ![Process command.](media/process-2.png "Process command hidden.")| 
 
- Some commands have been moved from the main set of commands to an overflow menu. This gives priority to other commands, including custom commands. 
  
### Tablet optimization for command bar

The command bar on Power Apps mobile for tablets was at the bottom, now the command bar is located at the top.

![Command bar on tablet.](media/command-bar-tablet.png "Command bar on tablet.")

Your app maker can turn on this feature. For more inforamtion, see [Features](../maker/model-driven-apps/app-properties.md#features).
    













[!INCLUDE[footer-include](../includes/footer-banner.md)]
