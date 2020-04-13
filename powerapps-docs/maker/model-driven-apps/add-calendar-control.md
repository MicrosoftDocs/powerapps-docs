---
title: "Add the calendar control to entities in model-driven apps | MicrosoftDocs"
description: "Learn how to add the calendar control to entities in model-driven apps."
ms.date: 04/15/2020
ms.service:
  - "dynamics-365-sales"
ms.topic: article
author: sbmjais
ms.author: shjais
manager: shujoshi
---

# Add the calendar control to entities

The **Calendar Control v2** control displays scheduled activities and their associated details in a calendar. You can view, create, and delete your activities in a day, week, or month view. You must be a system customizer or a system administrator to add the **Calendar Control v2** control.

**To add the control**

1.  In your app, select the **Settings** icon, and then select **Advanced Settings**.

    > [!div class="mx-imgBorder"]
    > ![Advanced settings](media/advanced-settings.png "Advanced settings") 

    The **Business Management** page opens in a new browser tab.

2.  On the navigation bar, select **Settings**, and then under **Customization**, select **Customizations**.

3.  Select **Customize the System**.

4.  Under **Components** in the solution explorer, expand **Entities**, and then select an entity. For example, **Activity**.

5.  On the **Controls** tab, select **Add Control**.

    > [!div class="mx-imgBorder"]
    > ![Add control command](media/add-control.png "Add control command") 

6.  In the **Add Control** dialog box, select **Calendar Control v2**, and then select **Add**.

    > [!div class="mx-imgBorder"]
    > ![Add control dialog box](media/add-cal-control.png "Add control dialog box")

7.  The calendar control is added to the list of controls.

    > [!div class="mx-imgBorder"]
    > ![Calendar control added](media/cal-control-added.png "Calendar control added")

8.  **Read-only grid** is the default option, so when users select an entity from the site map, they'll see a read-only grid of opportunities. To make the calendar view the default view instead, select the corresponding **Calendar Control v2** option buttons.

9.  Select the edit icon for each of the mandatory fields, and then select the binding values.

    > [!div class="mx-imgBorder"]
    > ![Binding values for mandatory fields](media/bind-values.png "Binding values for mandatory fields")

10. Select **Save** to save your changes.

11. To publish the changes you've made, select **Publish**.

### See also

[Work with records in the new calendar view](../../user/calendar-view.md)
