---
title: "Add the calendar control to tables in model-driven apps | MicrosoftDocs"
description: "Learn how to add the calendar control to tables in model-driven apps."
ms.date: 1/23/2024
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

[!INCLUDE [cc-classic-interface-control-migration](../../includes/cc-classic-interface-control-migration.md)]

The **Calendar** control displays scheduled activities and their associated details in a calendar. Activities can be viewed, created, and deleted in a day, week, or month view. System customizer or system administrator privileges are needed to add the **Calendar Control** control.

## To add the control

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
