---
title: Card control in Power Apps
description: Learn about the details, properties and examples of the card control in Power Apps.
author: gregli-msft
ms.service: powerapps
ms.topic: reference
ms.component: canvas
ms.date: 10/25/2016
ms.subservice: canvas-maker
ms.author: gregli
ms.reviewer: tapanm
search.audienceType: 
  - maker
search.app: 
  - PowerApps
contributors:
  - tapanm-msft
  - chmoncay
  - gregli-msft
---
# Card control in Power Apps
Provides the display and editing experience for a single field of a **[Display form](control-form-detail.md)** or **[Edit form](control-form-detail.md)** control.

## Description
**[Display form](control-form-detail.md)** and **[Edit form](control-form-detail.md)** controls act as containers for displaying and viewing entire records. Each container can hold a set of **Card** controls that display individual fields or provide a way to update those fields. Each card has a **DataField** property that specifies which field of the record it works on.  

Predefined cards are defined for different data types and user experiences.  For example, there may be a card to edit a number field with a **[Text input](control-text-input.md)** control, which is great for use with the keyboard. Another card might support editing a number by using a **[Slider](control-slider.md)** control instead. With the form control selected, you can, in the right-hand pane, easily select a card based on a field.

Cards themselves contain controls. The controls of a card make up the experience for displaying and editing a single field. For example, a number card may consist of a **[Label](control-text-box.md)** control to provide the display name of the field and a **[Text input](control-text-input.md)** control to provide an editor for the value of the field. The card may also have a **[Label](control-text-box.md)** control that shows any validation errors that occur and a **[Label](control-text-box.md)** control for the common asterisk to indicate that a field is required.

You can customize the controls of a predefined card by resizing it, moving it, hiding it, adding controls to it, and making other changes. You can also start with an entirely blank card, a "custom card", to which you add controls from scratch.

Predefined cards are *locked* by default. In a locked card, you can modify only certain properties of the card or the controls within the card, and you can't delete a locked card. You can show the card lock and unlock it on the **View** tab of the **Advanced** view. If a property is locked and can't be modified, it appears with a lock icon next to its name. Unlocking a card is an advanced activity and should be done with care, because automatic formula generation will no longer occur for the card, and you can't relock a card.

Within the form's container, the **ThisItem** record is available and contains all the fields of the record.  For example, the card's **[Default](properties-core.md)** property is often set to **ThisItem**.*FieldName*.

You can use the **Parent** reference to configure a control to reference the properties of a card.  For example, a control should use **Parent.Default** to read the initial state of the field from the data source. By using **Parent** instead of directly accessing the information that you want, the card is better encapsulated, and you can change it to a different field without breaking internal formulas.

See [Understand data cards](../working-with-cards.md) for examples of how to customize, unlock, and create cards.

## Key properties
**DataField** – The name of the field within a record that this card displays and edits.

* Specify the name as a single static string that's enclosed in double quotation marks (for example, **"Name"**), not a formula.
* Unbind a card by setting its **DataField** property *blank*. The **Valid** and **Update** properties are ignored for unbound cards.

**[Default](properties-core.md)** – The initial value of a control before it is changed by the user.

* For each control in a card, set this property to **Parent.Default** to refer to the default value of the field according to the data source. For example, set a slider's **[Default](properties-core.md)** property to **Parent.Default** to ensure that the user starts with a generic value for that slider.

**DisplayMode** – Values can be **Edit, View,** or **Disabled**. Configures whether the control inside the card allows user input (**Edit**), only displays data (**View**) or is disabled (**Disabled**).  

* Allows a single card to be used in both edit and view forms, by configuring this property, which is tied to the Form's behavior by default.
* In **View** mode, child controls such as **[Text input](control-text-input.md)**, **[Drop down](control-drop-down.md)**, **[Date Picker](control-date-picker.md)** will only display the text value and will not render any interactive elements or decorations.

**DisplayName** – The user friendly name for a field in a data source.

* The **[DataSourceInfo](../functions/function-datasourceinfo.md)** function provides this metadata from the data source.
* Controls within the card should use **Parent.DisplayName** to refer to the name of the field.

**Error** – The user friendly error message to display for this field when validation fails.

* This property is set when **SubmitForm** is called.  
* The message describes validation problems based on the data source's metadata and checking the card's **Required** property.

**Required** – Whether a card, editing the field of a data source, must contain a value.

* The **[DataSourceInfo](../functions/function-datasourceinfo.md)** function provides the required metadata from the data source.
* Controls within the card should use **Parent.Required** to determine whether that card's field is required.

**Update** – The value to write back to the data source for a field.

* Use this property's formula to pull the values from the edit controls of the card in order to write back to the data source. For example, set a card's **Update** property to **Slider.Value** to update the data source with a value from the slider in that card.

**[Width](properties-size-location.md)** – The distance between a control's left and right edges.

**[WidthFit](properties-size-location.md)** – Whether a control automatically grows horizontally to fill any empty space in a container control such as an **[Edit form](control-form-detail.md)** control. If multiple cards have this property set to **true**, the space is divided between them. For more information, see [Understand data form layout](../working-with-form-layout.md).

## Additional properties
**[BorderColor](properties-color-border.md)** – The color of a control's border.

**[BorderStyle](properties-color-border.md)** – Whether a control's border is **Solid**, **Dashed**, **Dotted**, or **None**.

**[BorderThickness](properties-color-border.md)** – The thickness of a control's border.

**[Fill](properties-color-border.md)** – The background color of a control.

**[Height](properties-size-location.md)** – The distance between a control's top and bottom edges.

**Valid** – Whether a **Card** or **[Edit form](control-form-detail.md)** control contains valid entries, ready to be submitted to the data source.

**[Visible](properties-core.md)** – Whether a control appears or is hidden.

**[X](properties-size-location.md)** – The distance between the left edge of a control and the left edge of its parent container (screen if no parent container). For a **[Card](control-card.md)** control in a container that has multiple columns, this property determines the column in which the card appears.

**[Y](properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (screen if no parent container). For a **[Card](control-card.md)** control in a container that has multiple rows, this property determines the row in which the card appears.

## Examples
See [Understand data cards](../working-with-cards.md) and [Understand data form layout](../working-with-form-layout.md) for examples.


## Accessibility guidelines
### Color contrast
There must be adequate color contrast between:
* **[Fill](properties-color-border.md)** and any child controls. For example, if a card contains a **[Label](control-text-box.md)** and the label has transparent fill, then the card's **[Fill](properties-color-border.md)** effectively becomes the background color for the label. Thus, there should be adequate contrast between the card's **[Fill](properties-color-border.md)** and the label's **[Color](properties-color-border.md)**.

### Screen reader support
* **DisplayName** must be present.


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]