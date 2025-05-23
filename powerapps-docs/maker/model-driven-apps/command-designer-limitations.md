---
title: "Command bar customization limitations | MicrosoftDocs"
description: "Discover the modern commanding limitations."
Keywords: command bar, command designer
author: caburk
ms.author: caburk
ms.reviewer: matp
contributors: aansu
ms.date: 02/19/2025
ms.subservice: mda-maker
ms.topic: how-to
search.audienceType: 
  - maker
---
# Modern commanding known limitations

## Power Fx and Command component libraries limitations

Power Fx shares certain infrastructure with custom pages and canvas apps. Relevant [limitations of custom pages](model-app-page-issues.md) are also applicable to commands.

- Not all Power Fx functions are currently supported for commands.
- Microsoft Dataverse is currently the only supported data source when using Power Fx with commands. However, custom pages can be used for connecting to external data.
-	To add additional tables, open the command component library from command designer. Or you may reopen command designer by selecting a different table in app designer.
-	When you write Power Fx formulas in the command designer, intellisense may sometimes provide recommendations for unsupported functions. It may not show an error for unsupported functions within command designer or the associated command component library.
-	Commands and the command component library created from one app can't be added to different apps. However, you can copy the command and paste it within another app or command bar location.
-	Not all out-of-the-box or custom visibility rules from classic commands are currently supported in Power Fx. Classic visibility is supported without using Power Fx. This is needed to migrate classic commands to modern and classic rule formats but won't be exposed in command designer. However, classic visibility is exposed within solution files and Dataverse.
-	To delete command component libraries, you must delete the app. Alternatively, you can delete the associated record within the model-driven app element table, then delete the component library. The model-driven app element record exists in Dataverse but isn't exposed in solutions. More information: [Delete a Model-Driven App Element record](#delete-a-model-driven-app-element-record)
- PowerFx based commands aren't supported and won't run within the Dynamics 365 app for Outlook or a model-driven app that's hosted within a Portal.
- Metadata changes for attributes might not reflect in the Power Fx expression. To update the metadata, open the component library using command bar actions in command designer. In Power Apps Studio for canvas apps select **Data sources**, select the data source, and then refresh. This updates the metadata for the component library.

## Command designer limitations

- Pre-existing classic commands can't be customized within the command designer until they're migrated to the modern infrastructure. This includes the out-of-the-box commands, which will be migrated incrementally over time. You may continue to use other mechanisms and third-party tools for customizing classic commands.
- Dynamically populated buttons aren't supported. We recommend creating them declaratively.
- Global application header and dashboard command bars aren't currently supported in command designer. These are customized infrequently. Share feedback if you find this valuable to prioritize.
- A single Power Fx component library is supported. The command designer might display the error message: "Unable to initialize component manager. There are multiple component libraries associated with your app." This error occurs when an app has multiple duplicate component libraries associated with it, which currently isn't supported with model-driven apps. To resolve this limitation, remove the additional `AppElement` entries for the app. Do this by removing the multiple library dependencies with the app, ensuring that only one `AppElement` entry exists.
- Editing commands on the commands page from the **Solutions** or **Tables** areas in Power Apps (make.powerapps.com) doesn't have the capability to set `Run formula` as the action or `Show on condition from formula` as the visibility rule. These capabilities are only available when editing commands from within the modern app designer.

## Delete a model-driven app element record

> [!WARNING] 
> If the app includes Power Fx-based commands, they will no longer work after you delete the app's model-driven app element table record.

Using the **Model-driven App Elements** table, do the following:

1. Create a flow to get a list of rows. More information: [Get a list of rows](/power-automate/dataverse/list-rows#get-a-list-of-rows)
   :::image type="content" source="media/list-rows-flow.png" alt-text="List model-driven app element Dataverse table rows using a flow":::
1. Then, run the flow to find the **Row id unique** value for the row you want to delete and copy it. You can also find this row value by viewing the table rows in the table hub for the Model-driven App Element table at make.powerapps.com.
1. Create a step to delete the row by using the unique ID value you copied in the previous step. More information: [Delete a row](/power-automate/dataverse/delete-row).
   :::image type="content" source="media/delete-row-flow.png" alt-text="Delete a row flow action using the model-driven app element Dataverse table row":::
1. Publish the model-driven app associated with the model-driven app element record.

### See also

[Modern commanding overview](command-designer-overview.md)

[Introducing Command Checker for model-app ribbons](https://powerapps.microsoft.com/blog/introducing-command-checker-for-model-app-ribbons/)
