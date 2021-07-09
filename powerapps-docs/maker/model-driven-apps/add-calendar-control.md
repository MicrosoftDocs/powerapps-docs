---
title: "Add the calendar control to tables in model-driven apps | MicrosoftDocs"
description: "Learn how to add the calendar control to tables in model-driven apps."
ms.date: 06/15/2021
ms.service: powerapps
ms.topic: how-to
author: sbmjais
ms.author: shjais
ms.reviewer: matp
manager: shujoshi
---

# Add the calendar control to tables

[!INCLUDE [cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

The **Calendar Control V2** control displays scheduled activities and their associated details in a calendar. You can view, create, and delete your activities in a day, week, or month view. You must be a system customizer or a system administrator to add the **Calendar Control V2** control.

**To add the control**

1.  In your app, select the **Settings** icon, and then select **Advanced Settings**.

    > [!div class="mx-imgBorder"]
    > ![Advanced settings](media/advanced-settings.png "Advanced settings") 

    The **Business Management** page opens in a new browser tab.

2.  On the navigation bar, select **Settings**, and then under **Customization**, select **Customizations**.

3.  Select **Customize the System**.

4.  Under **Components** in the solution explorer, expand **Tables**, and then select a table. For example, **Activity**.

    > [!IMPORTANT]
    > For **Description** and **Regarding** columns to be displayed in the Calendar Control v2, the table where the Calendar Control V2 is configured must be created as an activity table. More information: [Activity tables](../data-platform/types-of-entities.md#activity-tables)

5.  On the **Controls** tab, select **Add Control**.

    > [!div class="mx-imgBorder"]
    > ![Add control command](media/add-control.png "Add control command") 

6.  In the **Add Control** dialog box, select **Calendar Control V2**, and then select **Add**.

    > [!div class="mx-imgBorder"]
    > ![Add control dialog box](media/add-cal-control.png "Add control dialog box")

7.  The calendar control is added to the list of controls.

    > [!div class="mx-imgBorder"]
    > ![Calendar control added](media/cal-control-added.png "Calendar control added")

8.  **Read-only grid** is the default option, so when users select a table from the site map, they'll see a read-only grid of opportunities. To make the calendar view the default view instead, select the corresponding **Calendar Control V2** option buttons.

9.  Select the edit icon for each of the mandatory columns, and then select the binding values.

    > [!div class="mx-imgBorder"]
    > ![Binding values for mandatory columns](media/bind-values.png "Binding values for mandatory columns")

10. Select **Save** to save your changes.

11. To publish the changes you've made, select **Publish**.

### See also

[Work with rows in the new calendar view](../../user/calendar-view.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]