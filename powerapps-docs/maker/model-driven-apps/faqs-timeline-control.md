---
title: "FAQs for timeline control in Power Apps | MicrosoftDocs"
description: "Frequently asked questions (FAQs) for the timeline control in Power Apps"
ms.date: 10/05/2023
ms.topic: faq
author: "lalexms"
ms.subservice: mda-maker
ms.author: "laalexan"
contributors:
- dsierman
search.audienceType: 
  - maker
---
# FAQs for the timeline control

## A command isn't working. How do I use the command checker tool for timeline?

For instructions about how to enable and use the command checker, go to  [Troubleshooting ribbon issues in Power Apps](/troubleshoot/power-platform/power-apps/create-and-use-apps/ribbon-issues)

If an error dialog box displays "We can't compete the action you've selected" when trying to use the command action for activities on a timeline, it might be that the command action is hidden by custom rules. You can confirm by checking if the same action is hidden from **Related** > **Activities**.

:::image type="content" source="media/related-activities.png" alt-text="Go to related activities in the timeline":::

From the **Activities** tab, select the same activity that you want to perform the action on, and then check if you can perform the same command action from there.

:::image type="content" source="media/select-related-activity.png" alt-text="Select the related activity that you want":::

If the command action works here but not from the timeline, contact [Microsoft Support](/power-platform/admin/get-help-support).

If you can't find the command action from the related activity grid, you can further troubleshoot the issue with [command checker](https://powerapps.microsoft.com/en-us/blog/introducing-command-checker-for-model-app-ribbons/) to find out which custom rule hides the command.

1. Play the model-driven app that has the timeline.
1. From a table record that displays the timeline, select **Related** > **Activities** to go to the **Open Activity Associated View**.
1. Enable the command checker tool by appending the `&ribbondebug=true` parameter to the app URL.

   :::image type="content" source="media/command-checker-url-param.png" alt-text="Append URL parameter to add command checker":::

1. Select the **Command checker** command, which now appears on the app command bar. It might be listed on the **More** overflow flyout menu.

   :::image type="content" source="media/start-command-checker.png" alt-text="Start command  checker":::

1. From the command checker page that is displayed, select **Group Id: Mscrm.SubGrid.activitypointer.MainTab.Actions**, select a hidden command such as **Mark Complete (hidden)**, and then select the **Command properties** tab on the right to find out what custom rules are used to hide the command action.

   :::image type="content" source="media/find-group-id.png" alt-text="Find group ID":::

> [!NOTE]
> The timeline always displays command actions without honoring the custom rules to hide or disable the command button for performance reasons.

## Why aren't posts appearing in timeline and why can't I create a new post?

Posts in the timeline are only available for Dynamics 365 app enabled Dataverse environments and posts are disabled with timelines by default for new environments. To enable, follow these steps:

1. Go to the Dynamics 365 Customer Service admin center > **Miscellaneous** > **New and upcoming features**, and then select **Timeline User Posts**.

   :::image type="content" source="media/faqs-timeline-control/enable-posts-csac.png" alt-text="Enable post from Customer Service admin center":::

1. Check if the current table has the post configuration property activated. Go to **Settings** > **Activity Feeds configurations** > **Post Configurations**. In the example below, it's active for cases.

   :::image type="content" source="media/faqs-timeline-control/post-configurations-enabled.png" alt-text="Enabled post configuration for tables":::

   If the table isn't listed, look for it in the **Inactive Post Configurations** view. If the table you want isn't listed, select **Refresh** on the command bar. Select the table, and then select **Activate**.

1. Make sure posts are enabled from timeline configuration on the current form. More information: [Record types to show](set-up-timeline-control.md#record-types-to-show)

1. Verify the **Enable user posts** setting is enabled on the current form. If the checkbox is selected, clear it and select it again. Save and publish the changes from the form designer.

   :::image type="content" source="media/faqs-timeline-control/enable-user-posts-property.png" alt-text="Enable user post property":::

## Why do the "Modified On" columns of my records get changed when no changes are made to them?

This can be caused by the cascading behavior with the parent record. For example, when a case is assigned to another user. Go to [Table Relationships](../data-platform/create-edit-entity-relationships.md) for information about how to configure this behavior.

Alternatively, you can configure timeline to sort notes by their **Created on** date. More information: [Notes on timeline](set-up-timeline-control.md#notes-on-timeline)

## What privileges do I need to use timeline?

* To open attachments, you need read privilege for the **Activity file attachment** table.
* For personal settings and bookmarks, you need read, write, and create privileges on the **Custom Control Extended Setting** table.

Power Platform admins can assign users these privileges. More information [Security roles and privileges](/power-platform/admin/security-roles-privileges)

## How do I configure timeline for mobile offline?

For general guidance on enabling mobile offline for your app, go to [Set up mobile offline](../../mobile/setup-mobile-offline.md).

> [!NOTE]
>
> * The offline profile must have the **Note** and **User** tables in order for the timeline to work.
> * Only notes are available when offline.

## How can I resolve issues with email tracking or auto capture?

Go to [Auto Capture in Dynamics 365 sales](/dynamics365/sales/free-auto-capture#what-is-auto-capture) for general information or go to the [auto capture FAQ](/dynamics365/sales/faqs-sales-insights#auto-capture).

## See also

[Set up timeline control](set-up-timeline-control.md)

[Use the timeline control](../../user/add-activities.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
