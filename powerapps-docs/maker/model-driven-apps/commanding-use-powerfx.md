---
title: "Use Power Fx with commands | MicrosoftDocs"
description: "Use Power Fx to customize the command bar."
Keywords: command bar, command designer, commanding, modern, dialog, flow
author: caburk
ms.author: caburk
ms.reviewer: matp
manager: kvivek
ms.date: 07/26/2021
ms.service: powerapps
ms.topic: conceptual
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---
# Using Power Fx with commands (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

This section covers aspects of Power Fx that are specific to commanding. Many other functions that are in use today within canvas apps can also be used. Keep in mind there are differences because commanding is for model-driven apps.
- All existing data flow functions are supported.
- Imperative functions that work with data are supported.
- Imperative functions for simple Confirm and Notify are supported.

  > [!IMPORTANT]
  > - This is a preview feature, and may not be available in all regions.
  > - [!INCLUDE[cc_preview_features_definition](../../includes/cc-preview-features-definition.md)]

## AutoSave

- Many JavaScript commands start by saving the form buffer. This is because it makes the rest of the code easier to work with.
- By default, the form buffer is saved on behalf of the app maker.
  - The form is saved before the command is initiated.
  - Any problems that occur during the save operation are dealt with in the form's UI.
<!--- Not currently configurable:
  - We later need facilities for working with the buffer.  -->
 
 ## Selected property

|Field  |Type  |Description  |
|---------|---------|---------|
|Item     |Record of DataSource         |One of the records selected from the DataSource         |
|AllItems     |Table of records from the DataSource         |All of the records selected from the DataSource         |

- The **Selected** property is provided by the host of the command.
- **Item** and **AllItems** names are somewhat consistent with the ComboBox control and Gallery control, but this is a new pattern.
- If there is no record selected, **Item** returns Blank (IsBlank returns true) and **AllItems** returns an empty table (IsEmpty returns true).
- Null DataSource for record references (polymorphic record types). Generic functions can be called, such as Save or IsType/AsType can be used.
- **Item** is always Blank if **SelectionMax** <> 1.  This prevents writing formulas to just one item and not scaling to more than one.  

### Patch the current selected record

```powerapps-dot
Patch(Accounts, Self.Selected.Item, {'Account Name': "Changed Account name"})
```

### Create a related record

> [!NOTE]
> If the related table is not already in the command component library you will need to open it in canvas studio and add the data source there.

```powerapps-dot
Patch(Tasks,Defaults(Tasks),{Regarding:Self.Selected.Item},{Subject:"Subject of the Task"})
```

### Check and edit a date property

```powerapps-dot
If(Self.Selected.Item.'Last Date Included in Campaign'>DateAdd(Now(),-3), Patch(Accounts,Self.Selected.Item,{'Last Date Included in Campaign':Date(2021,10,19)}))
```

### Visible property: Only show the command if one or more records is selected in a grid view

```powerapps-dot
CountRows(Self.Selected.AllItems) > 0
```

### Control visibility based on record data

```powerapps-dot
//Button will be visible for accounts with Account Rating > 20
Self.ThisContext.SelectedItem.'Account Rating'>20
```

## Navigate

> [!NOTE]
> For additional options, see the client API reference to use JavaScript. More information: [navigateTo (Client API reference)](../../developer/model-driven-apps/clientapi/reference/Xrm-Navigation/navigateTo.md)

### Navigate to a custom page

To navigate to a custom canvas page within a model-driven app, pass the page name as the first argument.

```powerappsfl
Navigate( myCustomPage )
```
### Navigate to the default view of the table

To navigate to the default view of the table, passed table name as the first argument.

```powerappsfl
Navigate( Accounts )
```

### Navigate to specific system view of the table

To navigate to a specific system view of the table,pass the table's Views enum.

```powerappsfl
Navigate( 'Accounts (Views)'.'My Active Accounts' )
```

### Navigate to the default form of the table

To navigate to the default form of the table, pass the record as the first argument.

```powerappsfl
Navigate( Gallery1.Selected )
```

### Navigate to the default form of the table in create mode

To navigate to the default form of the table, pass a Dataverse record created from the [Defaults](../canvas-apps/functions/function-defaults.md) function. This will open the default form with the record as a new record. The **Defaults** function takes the table name to create the record.

```powerappsfl
Navigate( Defaults( Accounts ) )
```

## Confirm function

The `Confirm` function displays a dialog box on top of the current screen. Two buttons are provided: a confirm button and a cancel button, which default to localized versions of "OK" and "Cancel", respectively. The user must confirm or cancel before the dialog box is dismissed and the function returns. Besides the dialog button, cancel can also be selected with the Esc key or other gestures that are platform specific.

The `Message` parameter is displayed in the body of the dialog box. If the message is very long, it will either be truncated or a scroll bar provided.

Use the `OptionsRecord` parameter to specify options for the dialog box. Not all options are available on every platform and are handled on a "best effort" basis. 

> [!NOTE]
> The options in the table below aren't currently available with canvas apps.

|Option Field  |Description  |
|---------|---------|
|ConfirmButton     |The text to display on the *confirm* button, replacing the default, localized "OK" text.         |
|CancelButton     |The text to display on the *cancel* button, replacing the default, localized "Cancel" text.         |
|Title     |The text to display as the *title* of the dialog box. A larger, bolder font than the message font may be used to display this text. If this value is very long, it will be truncated.         |
|Subtitle     |   The text to display as the *subtitle* of the dialog box. A larger, bolder font than the message font may be used to display this text. If this value is very long, it will be truncated.      |

`Confirm` returns true if the confirm button was selected, false otherwise.

Use the `Notify` function to display a banner at the top of the app that doesn't need to be dismissed.

> [!NOTE]
> The `Notify` function isn't currently available with canvas apps.

### Syntax

**Confirm**( Message [, OptionsRecord ] )
- `Message` - Required. Message to display to the user.
- `OptionsRecord` - Optional. Provide advanced options for the dialog. Not all options are available on every platform and are handled on a best effort basis. At this time, in canvas apps, none of these options are supported.
	
### Examples

Simple confirmation dialog, asking the user to confirm deletion of a record before it is removed. Unless the user presses the **OK** button, the record will not be deleted.

```powerapps-dot
If( Confirm( "Are you sure?" ), Remove( ThisItem ) )
```

Same dialog as the last example, but adds title text.

```powerapps-dot
If( Confirm( "Are you sure?", {Title: "Delete Confirmation"} ), Remove( ThisItem ) )
```

Displays a message much like the `Notify` function does, but is modal and requires the user to select a button to proceed. Use in situations where it is important that the user acknowledge the message before proceeding. In this case, which button was selected isn't important.

```powerapps-dot
Confirm( "There was a problem, please review your order." )
```

## Add notifications to a model-driven app

A notification can be shown to app users by calling the [Notify function](../canvas-apps/functions/function-showerror.md).  

```powerappsfl
Notify( "Model-driven app notification message" )
```

## Other examples

### Launch a URL

```powerappsfl
Launch("https://www.bing.com");
```

### Access 1:N property

```powerappsfl
Self.Selected.Item.'Recurring Appointments'
```

### Check property of a related record

```powerappsfl
Self.Selected.Item.'Parent Account'.'Account Name'="parent"
```

### See also

[Understand behavioral formulas](../canvas-apps/working-with-formulas-in-depth.md)

[Formula reference](../canvas-apps/formula-reference.md)

[Overview of Power Fx](/power-platform/power-fx/overview)

