
<properties
    pageTitle="Card control: reference | Microsoft PowerApps"
    description="Information, including properties and examples, about the Card control"
    services=""
    suite="powerapps"
    documentationCenter="na"
    authors="gregli-msft"
    manager="erikre"
    editor=""
    tags=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="02/29/2016"
   ms.author="gregli"/>

# Card control in PowerApps #

Provides the display and editing experience for a single field of a **Form** or **View form** control.

## Description ##

**Form** and **View form** controls provide a container for displaying and viewing an entire record.  Each of these containers can hold a set of **Card** controls that display and edit individual fields.  Each card has a **DataField** property that specifies which field of the record it works on.  

Predefined cards are defined for different data types and user experiences.  For example, there may be a card to edit a number field with a **Text input** control, great for use with the keyboard.  And there may be another card for editing a number, that uses a **Slider** control instead.  With the form control selected, the "Options" pane allows for the easy selection of cards based on the field.    

Cards are themselves a container for controls.  The controls of a card make up the experience for displaying and editing a single field.  For example, a number card may consist of a **Text** control to provide the display name of the field and a **Text input** control to provide an editor for the value of the field.  It may also have another **Text** control to hold any validation errors, shown only if there is an issue, and another **Text** control for the common asterisk to indicate that a field is required.

The controls of a predefined card can be customized.  Controls can be resized, moved, made invisible, and other aspects modified.  Additional controls can be added to the card.  And you can start with an entirely blank card, a "custom card", in which to add controls. 

Predefined cards are *locked* by default.  Only certain properties of the card can be modified, and only certain properties on the controls within the card can be modified.  Controls cannot be removed.  The card lock can be viewed and unlocked in "Advanced" view, available on the "View" tab.  Properties that are locked and that cannot be modified are shown with a lock icon next to their name.  Unlocking a card is an advanced activity and should be done with care, as automatic formula generation will no longer occur for the card and the card cannot be re-locked.

Within the form's container, the **ThisItem** record is available containing all the fields of the record.  For example, the card's **Default** property is often set to **ThisItem.*FieldName***.    

Controls can reference the card's properties by using the **Parent** reference.  For example, a control should use **Parent.Default** to read the initial state of the field from the data source.  By using **Parent** instead of directly accessing the desired information, the card is better encapsulated and can be changed to a different field without requiring internal formulas to be modified.

See the [**understanding data cards**](working-with-data-cards.md) topic for examples of customizing, unlocking, and creating cards.

## Key properties ##

**DataField** The name of the field within a record that this card displays and edits.

- The name must be in a single static string enclosed in double quotes and not a formula.  For example, to work with the "Name" field: **Card.DataField = "Name"**.
- Cards can be unbound with their **DataField** property set to *blank*.  The **Valid** and **Update** properties are ignored for unbound cards.

**Default** The initial value of a control before it is changed by the user.

- Controls within the card should use **Parent.Default** to refer to the value of the field coming into the card.  For example, if a **Slider** control was going to be used to edit a field, use **Slider.Default = Parent.Default**

**Update** The value to write back to the data source for a field.

- Use this property's formula to pull the values from the edit controls of the card in order to write back to the data source.  For example, **Card.Update = Slider.Value** would use the slider's value for this card's field.

**DisplayName** The user friendly name for a field in a data source.

- The **DataSourceInfo** function provides the display name meta-data from the data source.
- Controls within the card should use **Parent.DisplayName** to refer to the value of the field coming into the card. 
 
**Required**  Whether a card, editing the field of a data source, must contain a value.

- The **DataSourceInfo** function provides the required meta-data from the data source.
- Controls within the card should use **Parent.Required** to refer to the value of the field coming into the card. 

**Error**  The user friendly error message to display for this field when validation fails.

- This property is set when **SubmitForm** is called.  
- The message includes validation problems based on the data source's meta-data and checking the card's **Required** property.

## All properties ##

**DataField** – The name of the field within a record that this card displays and edits.

**Default** – The initial value of a control before it is changed by the user.

**Update** – The value to write back to the data source for a field.

**DisplayName** – The user friendly name for a field in a data source.

**Required** – Whether a card, editing the field of a data source, must contain a value.

**Fill** – The background color of a control.

**BorderColor** – The color of a control's border.

**BorderStyle** – Whether a control's border is **Solid**, **Dashed**, **Dotted**, or **None**.

**BorderThickness** The thickness of a control's border.

**Error** The user friendly error message to display for this field when validation fails.

**Visible** Whether a control appears or is hidden.

**Height** The distance between a control's top and bottom edges.

**Width** The distance between a control's left and right edges.

**X** The distance between the left edge of a control and the left edge of the screen.

**Y** The distance between the top edge of a control and the top edge of the screen.

**Valid** Whether a **Card** or **Edit form** control contains valid entries, ready to be submitted to the data source. 

## Examples ##

See the [**understanding data cards**](working-with-data-cards.md) topic for examples.

