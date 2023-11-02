---
title: "FAQs for timeline control in Power Apps | MicrosoftDocs"
description: "Frequently asked questions (FAQs) for the timeline control in Power Apps"
ms.date: 10/05/2023
ms.topic: troubleshooting
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

## Why aren't posts appearing in timeline? Or, why can't I create a new post?

Check the following criteria:
1. Posts do not work in CDS orgs. They only work for CRM organizations.

2. User posts are disabled on timeline by default for new organizations. To re-enable them, please go to Customer Service admin center -> Miscellaneous -> New and upcoming features -> check Timeline User Posts
![image](https://github.com/MicrosoftDocs/powerapps-docs-pr/assets/35553346/b352e76f-0c57-4710-b729-97a800e211a0)

3. Check if the current entity has its post configuration activated. Go to Settings > Activity Feeds configurations -> post configurations. In the example below, you can see that it is active for cases.
![image](https://github.com/MicrosoftDocs/powerapps-docs-pr/assets/35553346/e3a9b8d5-e957-428b-88c5-740e05c10092)

If you don’t see your entity listed here, try to look for it in the “inactive post configurations” view. If it's still not listed, hitting the refresh button will make it appear.

![image](https://github.com/MicrosoftDocs/powerapps-docs-pr/assets/35553346/f973470c-1c4e-41fc-898c-820139280f19)

4. Make sure posts are enabled from timeline configuration on the current form.
   
![image](https://github.com/MicrosoftDocs/powerapps-docs-pr/assets/35553346/01dab0d5-97ec-4494-aa18-63927ed611d8)

5. Verify the "Enable User Posts" setting is enabled on the current form. There is a known issue where this checkbox appears checked, but it is not. This issue is affecting you if the "Enable post attachments" setting is greyed out. Try unchecking, and re-checking the box, then saving and publishing changes.
    
![image](https://github.com/MicrosoftDocs/powerapps-docs-pr/assets/35553346/cd4a3473-6050-482c-8103-6051baedfc3c)

> [!NOTE]
> We are deprecating user posts in the future. Please use notes as an alternative.

## Why do the "Modified On" fields of my records get changed when no changes are made to them?
This can be caused by cascading behavior with the parent record. For example, when a case is assigned to another user. Refer to [Table Relationships](../data-platform/create-edit-entity-relationships.md) to configure this behaviour.

Alternatively, you can configure timeline to sort notes by their "created on" date. See [Notes on timeline](set-up-timeline-control.md#notes-on-timeline)

## What permissions does timeline need to run?
* To see attachments, you need read access to the "Activity file attachment" entity
* For personal settings and bookmarks, you need read/write/create access to the "Custom Control Extended Setting" entity

## How do I configure timeline for mobile offline?
For general guidance on enabling mobile offline for your app, see [Set Up Mobile Online](../mobile/setup-mobile-offline.md) 
The offline profile must have the **Note** and **User** tables in order for timeline to function.

> [!NOTE]
> Only notes are available when offline

## Issues regarding email tracking/auto capture
Refer to [Auto Capture in Dynamics 365 sales](https://learn.microsoft.com/en-us/dynamics365/sales/free-auto-capture#what-is-auto-capture) for general information, or refer to the [auto capture FAQ](https://learn.microsoft.com/en-us/dynamics365/sales/faqs-sales-insights#auto-capture).

## See also

[Set up timeline control](set-up-timeline-control.md)

[Use the timeline control](../../user/add-activities.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
