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

## See also

[Set up timeline control](set-up-timeline-control.md)

[Use the timeline control](../../user/add-activities.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
