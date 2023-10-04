---
title: "FAQs for timeline control (section) in Power Apps | MicrosoftDocs"
description: "FAQs for timeline control (section) in Power Apps"
ms.date: 09/10/2021

ms.topic: troubleshooting
author: "lalexms"
ms.assetid: 7F495EE1-1208-49DA-9B02-17855CEB2FDF
ms.subservice: mda-maker
ms.author: "laalexan"
search.audienceType: 
  - maker
---

# FAQs for timeline control

## A command isn't working. How do I use the command checker tool for timeline?

For instructions on how to enable and use the command checker, go to [Troubleshooting ribbon issues in Power Apps](../../create-and-use-apps/ribbon-issues.md)

If you see error dialog saying "We can't compete the action you've selected" when trying to use the command action for activities on Timeline. It's likely the command action is hidden by custom rules. You can confirm by checking if the same action is hidden from Related activities.

![image](https://github.com/MicrosoftDocs/powerapps-docs-pr/assets/35553346/be1bfda9-a98a-4bce-8e33-b41737136d55)

From Related activities, select the same activity that you want to perform action on, and check if you can perform the same command action from here.

![image](https://github.com/MicrosoftDocs/powerapps-docs-pr/assets/35553346/74c06227-1ebd-4900-8098-116242e9b46f)

If the command action works here but not from Timeline, please contact MS support. 
Most likely, you cannot find the command action from Related Activity grid, then you can further debug the issue with command checker and find out which custom rule hides the command. 

To enable the Command Checker tool, you must append a &ribbondebug=true parameter to your Dynamics 365 application URL. 
For example:

![image](https://github.com/MicrosoftDocs/powerapps-docs-pr/assets/35553346/99540524-45ed-4b96-978c-1707f9f94874)

You'll see a new special "Command checker"  button to open the tool (it might be listed on the More overflow flyout menu).

![image](https://github.com/MicrosoftDocs/powerapps-docs-pr/assets/35553346/8f57d870-73b0-4f5d-86f5-629a0f74b805)

Find Group Id: Mscrm.SubGrid.activitypointer.MainTab.Actions, select the hidden command and go to Command properties to find out what custom rules to hide the command action.

![image](https://github.com/MicrosoftDocs/powerapps-docs-pr/assets/35553346/39cabbe2-ddf4-4cad-a529-947f655d6a1f)

Please note: Timeline always displays command actions without honoring the custom rules to hide/disable the command button because of performance reason. 

## See also

[Set up timeline control](set-up-timeline-control.md)

[Use the timeline control](../../user/add-activities.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
