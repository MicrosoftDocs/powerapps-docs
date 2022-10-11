---
title: "Use Power Fx with commands | MicrosoftDocs"
description: "Use Power Fx to customize the command bar."
Keywords: command bar, command designer, commanding, modern, dialog, flow
author: caburk
ms.author: caburk
ms.reviewer: matp
manager: kvivek
ms.date: 06/29/2022
ms.topic: conceptual
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---
# Using Power Fx with commands

This article covers aspects of Power Fx that are specific to commanding. Many other functions that are in use today within canvas apps can also be used. Keep in mind there are differences because commanding is for model-driven apps.

- All existing dataflow functions are supported. [What are dataflows?](/power-query/dataflows/overview-dataflows-across-power-platform-dynamics-365)
- Imperative functions that work with data are supported.
- Imperative functions for simple `Confirm` and `Notify` are supported.
- For a list of functions not supported, go to [Functions not supported](#functions-not-supported).

> [!NOTE]
> Publishing Power Fx commands may take a few minutes. It might not be obvious that background operations are still running even after the publish operation appears to have completed. You may need to wait a few minutes after publishing, then refresh the app to see your changes reflected. This typically takes longer the first time a Power Fx based command is published for an app.

## OnSelect

Defines the logic that will be executed when the button is selected within the app.

## Visible

Defines logic for hiding or showing the button when running the app. 

To define visibility logic select the command. Then select **Visibility** on the right command properties pane and choose **Show on condition from formula**. You may now select **Visible** on the left of the formula bar then write a Power Fx expression using the formula bar.

## Selected property

|Field  |Type  |Description  |
|---------|---------|---------|
|Item     |Record of DataSource         |One of the records selected from the DataSource.         |
|AllItems     |Table of records from the DataSource         |All of the records selected from the DataSource.        |
|State     |Enum    |State of the selected control. Edit (=0), New (=1), View (=2)    |
|Unsaved     |Boolean     |Returns true if Selected or SelectedItems have unsaved changes. Otherwise returns false. Always returns false if AutoSave is set to true (default option) within the command component library.     |

- The **Selected** property is provided by the host of the command.
- **Item** and **AllItems** names are somewhat consistent with the ComboBox control and Gallery control, but this is a new pattern.
- If there is no record selected, **Item** returns Blank (IsBlank returns true) and **AllItems** returns an empty table (IsEmpty returns true).
- Null DataSource for record references (polymorphic record types). Generic functions can be called, such as Save or IsType/AsType can be used.
- **Item** is always blank if **SelectionMax** <> 1.  This prevents writing formulas to just one item and not scaling to more than one.  

## AutoSave

- Many JavaScript commands start by saving the form buffer. This is because it makes the rest of the code easier to work with.
- By default, the form buffer is saved on behalf of the app maker.
  - The form is saved before the command is initiated.
  - Any problems that occur during the save operation are dealt with in the form's UI.

## Patch function

### Patch (update) the current selected record

```powerapps-dot
Patch(Accounts, Self.Selected.Item, {'Account Name': "Changed Account name"})
```

### Create a related record

> [!NOTE]
> If the related table is not already in the command component library you'll need to open it in canvas studio and add the data source there.

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
Self.Selected.Item.'Account Rating'>20
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

To navigate to the default view of the table, pass the table name as the first argument.

```powerappsfl
Navigate( Accounts )
```

### Navigate to specific system view of the table

To navigate to a specific system view of the table, pass the table's `Views` enum.

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

## RecordInfo function

Provides information about a [record](../canvas-apps/working-with-tables.md#elements-of-a-table) of a [data source](../canvas-apps/working-with-data-sources.md).

Use **RecordInfo** to obtain information about a particular record of a data source. At this time, only Microsoft Dataverse is supported.

The information available:

| Information argument | Description |
| --- | --- |
| **RecordInfo.DeletePermission** | Does the current user have permission to remove this record from the data source? |
| **RecordInfo.EditPermission** | Does the current user have permission to modify this record in the data source? |
| **RecordInfo.ReadPermission** | Does the current user have permission to view this record from the data source? |

**RecordInfo** returns a boolean value:

| Return value | Description |
| --- | --- |
| *true* | The user has the permission. |
| *false* | The user doesn't have permission. If the record is *blank* then **RecordInfo** will also return *false*. |

**RecordInfo** takes into account permissions at the data source level too.  For example, if the user has privileges at the record level to modify a record, but the user does not have privileges at the table level, then it will return *false* for **ModifyPermission**.  Use the [DataSourceInfo function](../canvas-apps/functions/function-datasourceinfo.md) to obtain information about the data source as a whole.

### RecordInfo Syntax

**RecordInfo**( *Record*, *Information* )

* *Record* – Required. The record to test.
* *Information* – Required. The desired information for the record.

### RecordInfo Examples

```powerapps-dot
RecordInfo(Self.Selected.Item, RecordInfo.EditPermission )
```

Used for the **Visible** property in this example. Checks whether the logged in user has edit privilege for the selected record. If the user has permission to edit this record and modify the `Accounts` data source in general, then **RecordInfo** will return *true* and the command will be visible. Otherwise the command will not be visible to the user.  

```powerapps-dot
CountRows(Filter(Self.Selected.AllItems, RecordInfo(ThisRecord,RecordInfo.EditPermission)))>0
```

Used for the **Visible** property for the **Main grid** location in this example. The button will be visible to the user running the app when one or more records within the grid are selected and the user has edit privilege to *at least one* of the selected records.

```powerapps-dot
CountRows(Filter(Self.Selected.AllItems, RecordInfo(ThisRecord,RecordInfo.EditPermission)))=CountRows(Self.Selected.AllItems)
```

Used for the **Visible** property for the **Main grid** location in this example. The button will be visible to the user running the app when one or more records within the grid are selected and the user has edit privilege for *all* of the selected records.

## DataSourceInfo function

Data sources can provide a wealth of information to optimize the user experience.

You can use [column](../canvas-apps/working-with-tables.md#columns)-level information to validate user input and provide immediate feedback to the user before using the [Patch function](../canvas-apps/functions/function-patch.md). The [Validate function](../canvas-apps/functions/function-validate.md) uses this same information.

You can use information at the data source level, for example, to disable or hide **Edit** and **New** buttons for users who don't have privileges to edit and create [records](../canvas-apps/working-with-tables.md#records).

### Data-source table information

You can use **DataSourceInfo** to obtain information about a data source as a whole. For commanding, it's also very common to use for **Visibility**. For example, to show or hide a command depending on whether the user has one or more privileges for the table.

| Information Argument | Result Type | Description |
| --- | --- | --- |
| **DataSourceInfo.AllowedValues** |Boolean |What types of permissions can users be granted for this data source? If not set by the data source, returns *blank*. |
| **DataSourceInfo.CreatePermission** |Boolean |Does the current user have privileges to create records in this data source? If not set by the data source, returns **true**. |
| **DataSourceInfo.DeletePermission** |Boolean |Does the current user have privileges to delete records in this data source? If not set by the data source, returns **true**. |
| **DataSourceInfo.EditPermission** |Boolean |Does the current user have privilege to edit records in this data source? If not set by the data source, returns **true**. |
| **DataSourceInfo.ReadPermission** |Boolean |Does the current user have privilege to read records in this data source? If not set by the data source, returns **true**. |

> [!NOTE]
> **DataSourceInfo** returns *true* if it can't determine whether the current user has the requested permission.  Permissions will be checked again by the server when the actual operation is carried out and an error is displayed if it was not allowed.  At this time, permissions checking with **DataSourceInfo** is only possible when using Microsoft Dataverse.

### DataSourceInfo syntax

**DataSourceInfo**( *DataSource*, *Information*, *ColumnName* )

* *DataSource* – Required. The data source to use.
* *Information* – Required. The type of information that you want to retrieve.
* *ColumnName* – Optional. For column-level information, the column name as a string. Column **Phone** would be passed as **"Phone"**, including the double quotes. For information at the data source level, the *ColumnName* argument can't be used.

### Data source column information

You can use **DataSourceInfo** to obtain information about a particular column of a data source.

| Information Argument | Result Type | Description |
| --- | --- | --- |
| **DataSourceInfo.DisplayName** |String |Display name for the column. If no display name is defined, returns the column name. |
| **DataSourceInfo.MaxLength** |Number |Maximum number of characters that the column can hold. Applies only to columns that contain strings. If a maximum isn't set, returns *blank*. |
| **DataSourceInfo.MaxValue** |Number |Maximum numeric value that a column can hold. Applies only to columns that contain numbers. If a maximum isn't set, returns *blank*. |
| **DataSourceInfo.MinValue** |Number |Minimum numeric value that a column can hold. Applies only to columns that contain numbers. If a minimum isn't set, returns *blank*. |
| **DataSourceInfo.Required** |Boolean |Is a value required for this column? If not set by the data source, returns **false**. |

### DataSourceInfo Examples

```powerapps-dot
DataSourceInfo(Accounts, DataSourceInfo.DeletePermission)
```

Used for the **Visible** property in this example. Checks whether the logged in user has delete privilege for records within the account table (determined by the security roles the user has). If the user has permission to delete account records, then **DataSourceInfo** will return *true* and the command will be visible. Otherwise the command will not be visible to the user.  

## Confirm function

The `Confirm` function displays a dialog box on top of the current screen. Two buttons are provided: a confirm button and a cancel button, which default to localized versions of "OK" and "Cancel", respectively. The user must confirm or cancel before the dialog box is dismissed and the function returns. Besides the dialog button, cancel can also be selected with the Esc key or other gestures that are platform-specific.

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

Simple confirmation dialog, asking the user to confirm deletion of a record before it is removed. Unless the user selects the **OK** button, the record will not be deleted.

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

> [!NOTE]
> `NotificationType.Success` is not currently supported and will result in an informational notification type.

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

## Functions not supported

The following Power Fx functions are currently not supported with commanding in model-driven apps.

- Back()
- Clear()
- Collect()
- Disable()
- Enable()
- Exit()
- InvokeControl()
- Language()
- LoadData()
- Param()
- ReadNFC()
- RequestHide()
- ResetForm()
- Revert()
- SaveData()
- ScanBarcode()
- Set()
- SubmitForm()
- UpdateContext()
- User()
- ViewForm()

### Enums not supported

- Align
- AlignInContainer
- BarcodeType
- BorderStyle
- Color
- Direction
- DisplayMode
- Font
- FontWeight
- FormPattern
- GridStyle
- ImagePosition
- ImageRotation
- LabelPosition
- Layout
- LayoutAlignItems
- LayoutDirection
- LayoutJustifyContent
- LayoutMode
- LayoutOverflow
- ListItemTemplate
- MapStyle
- Overflow
- PDFPasswordState
- PenMode
- RemoveFlags
- ScreenTransition
- TeamsTheme
- TextFormat
- TextMode
- TextPosition
- Themes
- Transition
- VerticalAlign
- VirtualKeyboardMode
- Zoom

### Other unsupported areas

- Acceleration
- App
- Compass
- Connection
- Environment
- Host
- Layout
- Location
- ScreenSize

### See also

[Understand behavioral formulas](../canvas-apps/working-with-formulas-in-depth.md)

[Formula reference](../canvas-apps/formula-reference.md)

[Overview of Power Fx](/power-platform/power-fx/overview)
