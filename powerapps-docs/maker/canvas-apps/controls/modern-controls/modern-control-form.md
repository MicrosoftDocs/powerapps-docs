---
title: Form modern control in canvas apps - Power Apps
description: Learn about the details, properties, and examples of the modern Edit form and Display form controls in Power Apps canvas apps.
author: yogeshgupta698
ms.topic: reference
ms.custom: canvas
ms.date: 07/20/2026
ms.subservice: canvas-maker
ms.author: yogupt
ms.reviewer: mkaur
search.audienceType:
  - maker
---

# Form modern control in canvas apps

Use a modern form to display, edit, and create records in a data source.

## Description

The modern **Form** control lets users view and work with a single record from a data source. Add an **Edit form** to let users create a record or edit an existing one and save the changes. Or, add a **Display form** to show a record as read-only. The modern form is built on the Microsoft Fluent 2 design system, so it uses updated styling, spacing, and accessibility defaults. It adapts its layout to different screen sizes.

Each field in the record appears in the form. You choose which columns to show and the order in which they appear. When you select a field, you can change the column it's bound to and how the value displays.

Key properties for this control are **DataSource**, **Item**, and **DefaultMode**.

## Modern vs. classic form


The modern **Form** control and the classic [Edit form and Display form controls](../control-form-detail.md)both use the same underlying form model. You set the same **DataSource** and **Item** properties. You use the same [form functions](/power-platform/power-fx/reference/function-form) - **SubmitForm**, **NewForm**, **EditForm**, **ViewForm**, and **ResetForm** - to control the form. Your existing knowledge and formulas carry over.

The modern form differs from the classic form in these ways:

- It uses the Microsoft Fluent 2 design system for a consistent, modern appearance.
- It applies responsive spacing and layout that adjust to the available width.
- It provides updated accessibility defaults, such as a clearer required-field indicator.

Both the classic and modern forms are supported, so you can choose the one that fits your app. To use modern controls, turn on modern controls and themes in your app settings.

## Key features

The modern **Form** control provides these capabilities:

- **Microsoft Fluent 2 design**: Fields, labels, and validation messages use the Fluent 2 design system for a clean, consistent appearance that matches the rest of your modern app.
- **Responsive layout**: The form adjusts its spacing and layout to the available width, so it works across desktop, tablet, and mobile without manual repositioning.
- **Theming**: The form follows the app theme, so you can style forms consistently from one place.
- **Built-in accessibility**: The form provides accessible defaults, including a clear required-field indicator and screen reader support.
- **Familiar form model**: The form uses the same **DataSource**, **Item**, and **DefaultMode** properties and the same form functions as the classic form, so your existing patterns and formulas carry over.

## General

**DataSource** – The data source that contains the record the form displays or edits. The data source also provides column display names and validation, such as which fields are required.

**Item** – The record to display or edit. For example, set **Item** to the **Selected** item of a [Gallery](modern-control-table.md) or to a function such as `First(Accounts)` or `LookUp(Accounts, "Fabrikam" in name)`. In **New** mode, the **Item** property is ignored and the form shows default values from the data source.

**DefaultMode** – The initial mode of the form. Accepts `FormMode` enum values:

| Value | Description |
|-------|-------------|
| `FormMode.Edit` | The form edits the record in the **Item** property. Default. |
| `FormMode.New` | The form creates a record, starting from the default values of the data source. |
| `FormMode.View` | The form displays the record in the **Item** property as read-only. |

## Behavior

**OnSuccess** – Actions to perform when a data operation succeeds after **SubmitForm** runs.

**OnFailure** – Actions to perform when a data operation fails after **SubmitForm** runs.

**OnReset** – Actions to perform when the form resets, such as when **ResetForm** runs.

**DisplayMode** – Whether the control allows input (**Edit**), only displays data (**View**), or is disabled (**Disabled**). The form's mode determines this value.

**Visible** – Whether the control appears or is hidden.

## Output properties

**Mode** – The current mode of the form: **Edit**, **New**, or **View**.

**Unsaved** – Whether the form has changes that the user hasn't saved yet. Use this property to warn users before they navigate away from unsaved edits.

**Updates** – A record of the values in the form's fields, ready to pass to a function such as **Patch**.

**Valid** – Whether all fields in the form, including required fields, currently hold valid values.

**Error** – A user-friendly error message to display when a data operation fails. Available after **OnFailure** runs.

**ErrorKind** – The kind of error that occurred, expressed as an `ErrorKind` enum value.

**LastSubmit** – The last successfully submitted record, including any server-generated values such as an ID. Available after **OnSuccess** runs.

## Work with the form

Use the [form functions](/power-platform/power-fx/reference/function-form) to change the form's mode and to save changes. Set these formulas on the **OnSelect** property of buttons.

- Switch to **New** mode so the user can create a record:

  ```power-fx
  NewForm(Form1)
  ```

- Switch to **Edit** mode to change the record in the **Item** property:

  ```power-fx
  EditForm(Form1)
  ```

- Switch to **View** mode to show the record as read-only:

  ```power-fx
  ViewForm(Form1)
  ```

- Save the changes in the form to the data source:

  ```power-fx
  SubmitForm(Form1)
  ```

- Discard changes in progress and reset the form to the default values:

  ```power-fx
  ResetForm(Form1)
  ```

When **SubmitForm** runs, the form validates required fields before it writes to the data source. If validation succeeds, the form saves the record and runs **OnSuccess**. If it fails, the form runs **OnFailure** and sets the **Error** and **ErrorKind** properties.

## Recent improvements

Recent releases added the following improvements to the modern **Form** control:

- **New screen templates**: Updated screen templates give the form and header cleaner default spacing, padding, and description text when you add a form-based screen.
- **Clearer required fields**: The required-field indicator appears in red, so users can spot required fields more easily.
- **Consistent typography**: Font size and bold styling are consistent across the form's fields and labels.
- **Display names for people fields**: A person or group field shows the display name of the selected user instead of an identifier.
- **Reliable date fields**: A date field keeps its value when the form switches to **Edit** mode.
- **Accurate validation**: Required-field validation stays accurate when the form's bound data source changes.

## See also

- [Modern controls overview](overview-modern-controls.md)
- [List of modern controls and properties](modern-controls-reference.md)
- [Edit form and Display form controls (classic)](../control-form-detail.md)
- [Understand canvas-app forms](../../working-with-forms.md)
- [EditForm, NewForm, SubmitForm, ResetForm, and ViewForm functions](/power-platform/power-fx/reference/function-form)
