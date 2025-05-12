---
title: "Use Power Fx with commands | MicrosoftDocs"
description: "Use Power Fx to customize the command bar."
Keywords: command bar, command designer, commanding, modern, dialog, flow
author: caburk
ms.author: caburk
ms.reviewer: matp
ms.date: 07/17/2024
ms.topic: how-to
ms.subservice: mda-maker
search.audienceType: 
  - maker
---
# Using Power Fx with commands

This article covers aspects of Power Fx that are specific to commanding. Many other functions that are in use today within canvas apps can also be used. Keep in mind there are differences because commanding is for model-driven apps.

- All existing dataflow functions are supported. [What are dataflows?](/power-query/dataflows/overview-dataflows-across-power-platform-dynamics-365)
- Imperative functions that work with data are supported.
- Imperative functions for simple `Confirm` and `Notify` are supported.
- For a list of functions not supported, go to [Functions not supported](#functions-not-supported).

> [!NOTE]
> Publishing Power Fx commands might take a few minutes. It might not be obvious that background operations are still running even after the publish operation appears to complete. You might need to wait a few minutes after publishing, then refresh the app to see your changes reflected. This operation typically takes longer the first time a Power Fx based command is published for an app.

## OnSelect

Defines the logic that is executed when the button is selected within the app.

## Visible

Defines logic for hiding or showing the button when running the app. 

To define visibility logic, select the command. Then select **Visibility** on the right command properties pane and choose **Show on condition from formula**. You can select **Visible** on the left of the formula bar then write a Power Fx expression using the formula bar.

## Selected property

|Field  |Type  |Description  |
|---------|---------|---------|
|Item     |Record of DataSource         |One of the records selected from the DataSource.         |
|AllItems     |Table of records from the DataSource         |All of the records selected from the DataSource.        |
|State     |Enum    |State of the selected control. Edit (=0), New (=1), View (=2)    |
|Unsaved     |Boolean     |Returns true if Selected or SelectedItems have unsaved changes. Otherwise returns false. Always returns false if AutoSave is set to true (default option) within the command component library.     |

- The **Selected** property is provided by the host of the command.
- **Item** and **AllItems** names are somewhat consistent with the ComboBox control and Gallery control, but this is a new pattern.
- If there's no record selected, **Item** returns Blank (IsBlank returns true) and **AllItems** returns an empty table (IsEmpty returns true).
- Null DataSource for record references (polymorphic record types). Generic functions can be called, such as Save or IsType/AsType can be used.
- **Item** is always blank if **SelectionMax** <> 1. This prevents writing formulas to just one item and not scaling to more than one.  

## AutoSave

- Many JavaScript commands start by saving the form buffer. This is because it makes the rest of the code easier to work with.
- By default, the form buffer is saved on behalf of the app maker.
  - The form is saved before the command is initiated.
  - Any problems that occur during the save operation are dealt with in the form's UI.

## Patch function

### Patch (update) the current selected record

```power-fx
Patch(Accounts, Self.Selected.Item, {'Account Name': "Changed Account name"})
```

### Create a related record

> [!NOTE]
> If the related table is not already in the command component library, you need to open it in canvas studio and add the data source there.

```power-fx
Patch(Tasks,Defaults(Tasks),{Regarding:Self.Selected.Item},{Subject:"Subject of the Task"})
```

### Check and edit a date property

```power-fx
If(Self.Selected.Item.'Last Date Included in Campaign'>DateAdd(Now(),-3), Patch(Accounts,Self.Selected.Item,{'Last Date Included in Campaign':Date(2021,10,19)}))
```

### Visible property: Only show the command if one or more records is selected in a grid view

```power-fx
CountRows(Self.Selected.AllItems) > 0
```

### Control visibility based on record data

```power-fx
//Button will be visible for accounts with Account Rating > 20
Self.Selected.Item.'Account Rating'>20
```

## Navigate

> [!NOTE]
> For additional options, see the client API reference to use JavaScript. More information: [navigateTo (Client API reference)](../../developer/model-driven-apps/clientapi/reference/Xrm-Navigation/navigateTo.md)

### Navigate to a custom page

To navigate to a custom canvas page within a model-driven app, pass the page name as the first argument.

```power-fx
Navigate( myCustomPage )
```

### Navigate to the default view of the table

To navigate to the default view of the table, pass the table name as the first argument.

```power-fx
Navigate( Accounts )
```

### Navigate to specific system view of the table

To navigate to a specific system view of the table, pass the table's `Views` enum.

```power-fx
Navigate( 'Accounts (Views)'.'My Active Accounts' )
```

### Navigate to the default form of the table

To navigate to the default form of the table, pass the record as the first argument.

```power-fx
Navigate( Gallery1.Selected )
```

### Navigate to the default form of the table in create mode

To navigate to the default form of the table, pass a Dataverse record created from the [Defaults](../canvas-apps/functions/function-defaults.md) function. This opens the default form with the record as a new record. The **Defaults** function takes the table name to create the record.

```power-fx
Navigate( Defaults( Accounts ) )
```

## Optimize the user experience with data source and record information

Use the [**DataSourceInfo** function](/power-platform/power-fx/reference/function-datasourceinfo) and [**RecordInfo** function](/power-platform/power-fx/reference/function-recordinfo) to optimize the user experience with information about the data being displayed and manipulated.

For example, use **RecordInfo** to determine if the current user has permission to modify a record and appropriately show or hide an "Edit" button using its **Visible** property:

```power-fx
EditButton.Visible = 
   RecordInfo( Gallery1.Selected, RecordInfo.EditPermission )
```

For example, use **DataSourceInfo** to determine if the current user has permission to create a record and appropriately show or hide a "Create" button using its **Visible** property:

```power-fx
CreateButton.Visible = 
   DataSourceInfo( Accounts, DataSourceInfo.CreatePermission )
```

## Ask for confirmation before taking action

Use the [**Confirm** function](/power-platform/power-fx/reference/function-confirm) to display a dialog box on top of the current screen.

```power-fx
Notify( Confirm( "Are you sure?", 
                 { ConfirmButton: "Yes", CancelButton: "No" } 
        ) 
)
```

Displays a notification **true** if the **Yes** button is pressed, and a notification **false** if the **No** button is pressed.


## Notify the user

A notification can be shown to app users by calling the [Notify function](../canvas-apps/functions/function-showerror.md).

> [!NOTE]
> `NotificationType.Success` isn't currently supported and results in an informational notification type.

```power-fx
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

## Functions available with commanding

For information about the formulas supported with commanding in model-driven apps, go to [Formula reference - model-driven apps](/power-platform/power-fx/formula-reference-model-driven-apps).

### Functions not supported

The following Power Fx functions are *currently not supported* with commanding in model-driven apps.

- Back()
- Clear()
- Collect()
- Copy()
- Disable()
- Enable()
- Exit()
- InvokeControl()
- Language()
- LoadData()
- Param()
- Print()
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
- Dataverse file type columns
- Environment
- Host
- Layout
- Location
- ScreenSize

### See also

[Understand behavioral formulas](../canvas-apps/working-with-formulas-in-depth.md)

[Formula reference](../canvas-apps/formula-reference.md)

[Overview of Power Fx](/power-platform/power-fx/overview)
