---
title: "Disable AutoSave in a model-driven app with Power Apps | MicrosoftDocs"
description: Learn how to configure AutoSave for a model-driven app in Power Apps.
ms.custom: ""
ms.date: 04/21/2025
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "conceptual"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
author: "Mattp123"
ms.assetid: 2e7f75dd-7a3f-4716-b995-b626929c0501
caps.latest.revision: 14
ms.subservice: mda-maker
ms.author: "matp"
search.audienceType: 
  - maker
---
# Disable AutoSave in a model-driven app

AutoSave helps app users focus on their work without having to manage saving data in the form. Most people appreciate not having to explicitly save data each time they update a row, but some organizations might have customizations that were designed expecting an explicit save. For these organizations there are options to manage how AutoSave is applied.  
  
## How AutoSave works

 By default all main forms for [Updated tables and classic tables](create-design-forms.md#updated-versus-classic-tables) have AutoSave enabled. After a row is created (initially saved), any changes made to a form are automatically saved 30 seconds after the change is made. If no changes are made in the form, the automatic save doesn't occur while the form is open. After a change is made, the 30-second period before an AutoSave begins again. If someone else has updated the same row while you're editing it, those changes are retrieved and displayed in the form when AutoSave occurs.  
  
 With AutoSave enabled, the save button only appears for the initial save of the row. After the row is created, the save button in the command bar isn't shown, but you can see a ![Auto save button.](media/auto-save-icon.png "Auto save button") button in the lower right corner that shows if there are any unsaved changes. This control is also displayed if AutoSave is disabled.  
  
 You can select this button to save the row and refresh data in the form immediately. When  AutoSave is enabled the row is saved whenever you navigate away from a row or close a separate window displaying a row. There's no need for the **Save & Close** button that appears in forms for tables that aren't updated.  
  
## Should you disable AutoSave?  

If you have plug-ins, workflows, or form scripts that execute when a row is saved, they run each time AutoSave occurs. This pattern might lead to undesirable behaviors if these extensions weren't designed to work with AutoSave. Whether AutoSave is enabled or not, plug-ins, workflows, and form scripts should be designed to look for specific changes, and shouldn't execute indiscriminately for each save event.  
  
If you have auditing configured for a table, each save is treated like a separate update. If someone lingers on a form with unsaved changes for more than 30 seconds, you observe another entry only if they add more data after the AutoSave is performed. If you have reports that depend on auditing data and treat each save as an individual "touch" of a row, you might see an increase in the frequency of touches. If you're using this approach, you should consider that individual user behaviors make it an unreliable metric with or without AutoSave enabled.  
  
## Disable AutoSave for the organization

If you determine that AutoSave causes problems with extensions you're using, Power Platform admins can disable it for the environment. There's no setting to disable AutoSave for individual tables or forms.  

1. Sign into the [Power Platform admin center](https://admin.powerplatform.microsoft.com), go to **Manage** > **Environments**, and then open the environment you want.
1. Select **Settings** on the command bar. 
1. Expand **Product**, and then select **Behavior**.  
1. Under **Basic behavior**, for the **Auto save**, select **Off**.  
  
## Disable AutoSave for a form

 If you want to disable AutoSave for specific table forms, you can add code to the `OnSave` event in a table.  
  
> [!NOTE]
>  By using this method, auto-save is disabled for the form, but data is still saved when you select the ![Auto save button.](media/auto-save-icon.png "Auto save button") button in the lower-right corner. If you attempt to navigate away from a form or close a form where data was changed, you get a prompt to save changes before you're allowed to navigate away or close the form. 
>  
>  Using the procedure here causes the **Save and close** button on the form to not work, as it calls `preventDefault` on `saveMode` 2, which references **Save and Close**. You can remove the `getSaveMode() == 2` check to avoid this, but then the form autosaves when you attempt to navigate away from the form or close the form where data has changed. The **Save and Continue** button also doesn't work for this reason.
  
1.  Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).  

2.  Select **Tables** on the left navigation pane, select the table that you want, and then select the **Forms** area. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]
   
    You can also make adjustments to the tables from within a [solution](../model-driven-apps/model-driven-app-glossary.md#solution).  To do this, select **Solutions** on the left pane, select the table, and then select the **Forms** area. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]
  
3.  Open the form you want to edit.

4.  Select **Switch to classic** to edit the form in the classic form designer.
  
5.  Create a JavaScript web resource and add it to the form:  
  
    1.  In the form editor, in the **Form** group, choose **Form Properties**.  
  
    2.  On the **Events** tab, below **Form Libraries** choose **Add**.  
  
    3.  In the **Look Up Row** dialog box, choose **New**.  
  
    4.  Enter the following information in the web resource form:  
  
        |Title|Reference|  
        |-|-|  
        |**Name**|preventAutoSave|  
        |**Display Name**|Prevent AutoSave|  
        |**Type**|Script (JScript)|  
  
    5.  Next to the **Type** column, choose **Text Editor**.  
  
    6.  In the **Source** column, paste the following code:  
  
        ```javascript  
        function preventAutoSave(econtext) {  
            var eventArgs = econtext.getEventArgs();  
            if (eventArgs.getSaveMode() == 70 || eventArgs.getSaveMode() == 2) {  
                eventArgs.preventDefault();  
            }  
        }  
  
        ```  
  
    7.  Choose **OK** to close the text editor.  
  
    8.  Choose **Save** to save the web resource and then close the web resource window.  
  
    9. In the **Look Up Row** dialog the new web resource you created is selected. Choose **Add** to close the dialog.  
  
6.  Configure the `OnSave` event:  
  
    1.  In the **Form Properties** window, in the **Event Handlers** section, set **Event** to **OnSave**.  
  
    2.  Select **Add**.  
  
    3.  In the **Handler Properties** window, set **Library** to the web resource you added in the previous step.  
  
    4.  Type '`preventAutoSave`' in the **Function** column. This is case sensitive. Don't include quotation marks.  
  
    5.  Make sure that **Enabled** is checked.  
  
    6.  Check **Pass execution context as first parameter**.  
  
        > [!IMPORTANT]
        >  If you don't do this the script won't work.  
  
         The **Handler Properties** dialog should look like this. The customization prefix: "new_" might vary based on the customization prefix set for the default publisher for your organization.  
  
         ![OnSave event handler to prevent autosave in Dynamics 365.](media/prevent-auto-save-script.png "OnSave event handler to prevent autosave in Dynamics 365")  
  
    7.  Select **OK** to close the **Handler Properties** dialog.  
  
    8.  If there are any other event handlers for the `OnSave` event, use the green arrows to move this one to the top.  

        The **Form Properties** should display as follows. Note in the example shown here, the update has taken place from within a solution and as a result the publisher prefix (dspin_) isn't the same as the one provided by the default publisher (new_). This is because a different [publisher](../model-driven-apps/model-driven-app-glossary.md#publisher) is used for the solution.

    :::image type="content" source="../../maker/model-driven-apps/media/disable-autosave-handler-complete.png" alt-text="Advanced Settings":::
  
7. Select **OK** to close the **Form Properties** dialog.  
  
8. Select **Save and Close** to close the form.  
  
9.  In the solution explorer, select **Publish All Customizations**.  
  
 After you apply this script to the `OnSave` event, when users edit a row using this form the message **unsaved changes** appears in the bottom right corner of the form just as it would if AutoSave wasn't disabled. But this message won't go away until people select the ![Auto save button.](media/auto-save-icon.png "Auto save button") button next to it.
  
## Next steps

[Create and design forms](create-design-forms.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
