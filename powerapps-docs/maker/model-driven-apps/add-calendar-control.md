---
title: "Add the calendar control to tables in model-driven apps with Power Apps"
description: "Learn how to add the calendar control to tables in model-driven apps."
ms.date: 5/15/2025
ms.topic: how-to
author: sriharibs-msft
ms.subservice: mda-maker
ms.author: srihas
ms.reviewer: matp
contributors:
 - shwetamurkute
 - anuitz
 - srihas
---

# Add the calendar control to tables

The **Calendar** control displays scheduled activities and their associated details in a calendar. Activities can be viewed, created, and deleted in a day, week, or month view. 

:::image type="content" source="media/calendar-control-appointments.png" alt-text="Calendar control for the appoinment table view":::

System customizer or system administrator privileges are needed to add the **Calendar Control** control.

## Add the control using the modern app designer

When you add the calendar control to a table, you can specify the columns that are used for the start date, end date, description, and duration. The calendar control is available in the modern app designer.

> [!NOTE]
> When you add the control to a table view, it replaces the standard view for all views for that table.

1. While working in the app designer on the **Pages** tab, hover over the table view and then select the **Edit view** (pencil icon).  
1. Open the view where you want to replace the standard view with the calendar control.
   The view designer opens.
1. On the command bar select **Components**, and then select **Add a component**.
1. On the **Add a control** page, select **Calendar**.
1. On the **Add a calendar** properties page, select the table columns and clients to display the control. For example, with appointment table, you specify these columns.
   - **Start date**. Select the column that is used for the start date on the calendar, such as **Start Time (Date and Time)**.
   - **Description**. Select the column that is used for the description, such as **Subject (Text)**.
   - **End date**. Select the column that is used for the end date on the calendar, such as **End Time (Date and Time)**.
   - **Duration**: Select the column that is used for the duration on the calendar, such as **Duration (Duration)**.
   :::image type="content" source="media/calendar-control-properties.png" alt-text="Properties for the calendar control":::
1. Select **Done**, and then select **Save**.
1. To make the updated view available in model-driven apps, select **Save and publish**.

## Add the control using the classic solution explorer

1. In the app, select the **Settings** icon, and then select **Advanced Settings**.

    > [!div class="mx-imgBorder"]
    > ![Advanced settings.](media/advanced-settings.png "Advanced settings")

    The **Business Management** page opens in a new browser tab.
1. On the navigation bar, select **Settings**, and then under **Customization**, select **Customizations**.
1. Select **Customize the System**.
1. Under **Components** in the solution explorer, expand **Tables**, and then select a table. For example, **Activity**.

    > [!IMPORTANT]
    > For **Description** and **Regarding** columns to be displayed in the Calendar Control, the table where the Calendar Control is configured must be created as an activity table. More information: [Activity tables](../data-platform/types-of-entities.md#activity-tables)
1. On the **Controls** tab, select **Add Control**.

    > [!div class="mx-imgBorder"]
    > ![Add control command.](media/add-control.png "Add control command")

1. In the **Add Control** dialog box, select **Calendar**, and then select **Add**.

1. The calendar control is added to the list of controls.

1. **Read-only grid** is the default option, so when users select a table from the site map, they see a read-only grid of opportunities. To make the calendar view the default view instead, select the corresponding **Calendar** option buttons.

1. Select the edit icon for each of the mandatory columns indicated by a red asterisk, and then select the binding values.

    > [!div class="mx-imgBorder"]
    > ![Calendar control added.](media/cal-control-added.png "Calendar control added")

1. Select **Save** to save changes.

1. To publish the changes, select **Publish**.

### Mobile experience

The **Calendar** control is available when working on mobile devices with a different user experience that is optimized for mobile form factors. There's a scrollable day bar for selecting which date to view. The Day/Week/Month selection dropdown isn't available on mobile devices.

### See also

[Work with rows in the new calendar view](../../user/calendar-view.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
