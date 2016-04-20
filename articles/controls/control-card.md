
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

**Form** and **View form** controls provide a container for displaying and viewing an entire record.  Each of these container controls can hold a set of **Card** controls that display and edit individual fields.  Each card has a **DataField** property that specifies which field of the record it works on.  

Predefined cards are defined for different data types and user experiences.  For example, there may be a card to edit a number field with a **Text input** control, great for use with the keyboard.  And there may be another card for editing a number, that uses a **Slider** control instead.  You can also define your own custom cards.  

Cards are themselves a container for controls.  The controls of a card make up the experience for displaying and editing a single field.  For example, a number card may consist of a **Text** control to provide the display name of the field and a **Text input** control to provide an editor for the value of the field.  It may also have another **Text** control to hold any validation errors, shown only if there is an issue, and another **Text** control for the common asterisk to indicate that a field is required.

Predefined cards are *locked* by default.  Only certain properties of the card can be modified, and only certain properties on the controls within the card can be modified.  The card lock can be viewed and unlocked in Advanced view.  Properties that are locked and that cannot be modified are shown with a lock icon next to their name.  Unlocking a card is an advanced activity and should be only done with care, as automatic formula generation will no longer occur for the card and the card cannot be re-locked.  See [**understand data cards**](working-with-data-cards.md) topic for more details.

## Key properties ##

**DataField** The name of the field within a record that this card displays and edits.

- The name must be in a single static string enclosed in double quotes and not a formula.  For example, to work with the "Name" field: **Card.DataField = "Name"**.
- Cards can also be unbound within the **Form** control (**DataField** property is blank).  The **Valid** and **Update** properties are ignored for unbound cards.

## Locked properties ##

The following properties are locked by default on predefined cards. To modify the formulas for these properties, you must first unlock the card.  See [**understand data cards**](working-with-data-cards.md) topic for more details. 

**Default** 

- Controls within the card should use **Parent.Default** to refer to the value of the field coming into the card.  For example, if a **Slider** control was going to be used to edit a field, use **Slider.Default = Parent.Default**

**Update** The value to write back to the data source for a field.

- Use this property's formula to pull the values from the edit controls of the card in order to write back to the data source.  For example, **Card.Update = Slider.Value** would use the slider's value for this card's field.

**DisplayName** The user friendly name for a field in a data source.
 
**Required**  Determines if the field of a record must contain a value or can be left blank.

## All properties ##

**DataField**

**Default** 

**Update**

**DisplayName**

**Required** 

**Fill**

**BorderColor**

**BorderStyle**

**BorderThickness**

**Error** The user friendly error message to display for this field when validation fails.

**Visible**

**Height**

**Width**

**X**

**Y**

**DataField**

**Required**

**Valid** 
