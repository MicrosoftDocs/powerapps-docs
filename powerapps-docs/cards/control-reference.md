---
title: Controls and properties in cards for Power Apps
description: Learn about properties of different controls available in cards for Power Apps.
author: anuitz
ms.topic: reference
ms.custom: 
ms.reviewer: mkaur
ms.date: 03/01/2023
ms.author: anuitz
search.audienceType:
  - maker
search.app:
  - PowerApps
contributors:
  - mduelae
  - anuitz
---

# Controls and properties in cards for Power Apps

Configure the appearance and behavior of a control by setting one of its properties. Each type of control has a different set of properties. Some properties, such as **Height** and **Width**, are common to almost every type of control, but other properties, such as **CheckboxSize**, are specific to one type of control.

## Controls

**[Button](controls/button.md)** – A button element that executes PowerFx on click. 

**[Button set](controls/button.md)** – A container for a set of button elements.

**[Check box](controls/check-box.md)** – An checkbox that lets users choose between two options by selecting or clearing.

**[Column](controls/column.md)** - An individual column which acts as a container for other elements.

**[Column set](controls/column-set.md)** - A collection of columns, each column is a container.

**[Container](controls/container.md)** - A collection of other elements.

**[Date picker](controls/date-picker.md)** – A field for users to select a date.

**[Drop down](controls/drop-down.md)** – A menu that lets users choose one item from an expandable list of items.

**[Fact set](controls/fact-set.md)** – A container element for facts.

**[Image](controls/image.md)** – An image with properties to control what the image looks like.

**[Image set](controls/image-set.md)** – A container of images that acts as a photo gallery.

**[Media](controls/media.md)** – A video or image specified by its Url and MimeType.

**[Number input](controls/number-input.md)** – A field for users to type a number.

**[Text input](controls/text-input.md)** – A field for users to type text.

**[Text label](controls/text-label.md)** – A block of text with properties to control what the text looks like.

**[Time picker](controls/time-picker.md)** – A field for users to select a time.

## All properties

### A

**Associated inputes** - Controls which inputs are associated with the action.

### B

**Background image** – Specifies a background image. Acceptable formats are PNG, JPEG, and GIF.

**Bleed** – Determines whether the control should bleed through its parent's padding.

### C

**Content alignment** – Defines how the content should be aligned vertically within the column.

### D

**Default value** – The initial value for this property.

**Divider** – When true, draw a separating line at the top of the control.

### E

**ErrorMessage** – Error message to display when entered input is invalid.

### F


### G



### H

**Height** – Specifies the height of the control.

**Horizontal alignment** – Controls the horizontal alignment of the column set.

### I

**IconUrl** - Optional icon to be shown on the button in conjunction with the title. Supports data URI in version 1.2+.

**Initially visible** – If false, this item will be removed from the visual tree.

### L

**Label** – Label for the input.


### M

**Maximum value** – Hint of maximum value expressed in YYYY-MM-DD (may be ignored by some clients).

**Minimum height** – Specifies the minimum height of the column set in pixels, like "80px".

**Minimum value** – Hint of minimum value expressed in YYYY-MM-DD (may be ignored by some clients).


### N

**Name** – A unique identifier associated with a property.

### O

**OnSelect** - Actions to perform when the user taps or clicks on the button.


### P

**Placeholder** – Description of the input desired. Displayed when no selection has been made.


### R

**Repeat for every** – Data context expression.

**Required field** – Whether or not this input is required.

**Requires** – A series of key/value pairs indicating features that the item requires with corresponding minimum version. When a feature is missing or of insufficient version, fallback is triggered.

### S

**SelectAction** – An Action that will be invoked when the column set is tapped or selected. Action.ShowCard is not supported.

**Show when** – Conditional layout expression.

**Spacing** – Controls the amount of spacing between this control and the preceding control.

**Style** - Controls the style of a property.

### T

**Title** - Label for this button.

**Type** – 


### U


### V



### W

**Width** – Auto, stretch, a number representing relative width of the column in the column group, or in version 1.1 and higher, a specific pixel width, like "50px".

**Wrap** – If true, allow text to wrap. Otherwise, text is clipped.

### X


### Y

*

### Z



### See also

[Limitations of controls for cards in Power Apps](control-limitations.md)
