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
contributors:
  - mduelae
  - anuitz
---

# Controls and properties in cards

[!INCLUDE[cards-deprecation-banner](~/includes/cards-deprecation-notice.md)]

Configure the appearance and behavior of a control by setting one of its properties. Each type of control has a different set of properties. Some properties, such as **Height** and **Width**, are common to almost every type of control, but other properties, such as **OnSelect**, are specific to one type of control.

## Controls

**[Button](../controls/button.md)** – A button element that executes Power Fx on click.

**[Button set](../controls/button.md)** – A container for a set of button elements.

**[Check box](../controls/check-box.md)** – An checkbox that lets users choose between two options by selecting or clearing.

**[Column](../controls/column.md)** - An individual column, which acts as a container for other elements.

**[Column set](../controls/column-set.md)** - A collection of columns, each column is a container.

**[Container](../controls/container.md)** - A collection of other elements.

**[Date picker](../controls/date-picker.md)** – A field for users to select a date.

**[Drop down](../controls/drop-down.md)** – A menu that lets users choose one item from an expandable list of items.

**[Fact set](../controls/fact-set.md)** – A container element for facts.

**[Image](../controls/image.md)** – An image with properties to control what the image looks like.

**[Image set](../controls/image-set.md)** – A container of images that acts as a photo gallery.

**[Media](../controls/media.md)** – A video or image specified by its Url and MimeType.

**[Number input](../controls/number-input.md)** – A field for users to type a number.

**[Table](../controls/table.md)** – Present tabular data or any structured information that is best laid out in rows and columns. 

**[Text input](../controls/text-input.md)** – A field for users to type text.

**[Text label](../controls/text-label.md)** – A block of text with properties to control what the text looks like.

**[Time picker](../controls/time-picker.md)** – A field for users to select a time.

## All properties

### A

**Alt text** – Alternate text describing the image, audio, or video.

**Associated inputs** - Controls which inputs are associated with the action.

### B

**Background color** – Applies a background to a transparent image. This property respects the image style.

**Background image** – Specifies a background image. Acceptable formats are PNG, JPEG, and GIF.

**Bleed** – Determines whether the control should bleed through its parent's padding.

### C

**Choices** - The list of items the user can select from.

**Color** – Controls the color of the text.

**Content alignment** – Defines how the content should be aligned vertically within the column.

### D

**Default value** – The initial value for the property.

**Divider** – When true, draw a separating line at the top of the control.

### E

**Error message** – Error message to display when entered input is invalid.

### F

**Facts** - The facts to display in a fact set.

**Font type** – Type of font to use for rendering

### H

**Height** – Specifies the height of the property.

**Horizontal alignment** – Controls the horizontal alignment.

### I

**IconUrl** - Optional icon to be shown on the button beside the title. Supports data URI in version 1.2+.

**Image size** – Controls the approximate size of each image. The physical dimensions vary per host. Auto and stretch aren't supported for image set. The size defaults to medium if those values are set.

**InlineAction** – The inline action for the input. Typically displayed to the right of the input. It's recommended to provide an icon on the action (which is displayed instead of the title of the action).

**Initially visible** – If false, this item is removed from the visual tree.

### L

**Label** – Label for the input.

### M

**Max length** – Hint of maximum length characters to collect (may be ignored by some clients).

**Maximum lines** – Specifies the maximum number of lines to display.

**Maximum value** – Hint of maximum value (may be ignored by some clients).

**Minimum height** – Specifies the minimum height of the column set in pixels, like "80 px".

**Minimum value** – Hint of minimum value (may be ignored by some clients).

**Mode** – The mode can be defined as primary or secondary, to establish a hierarchy between card elements.

**Multiline** – If true, allow multiple lines of input.

**Multiple selection** – Allow multiple items to be selected.

### O

**OnSelect** - Actions to perform when the user taps or clicks on the button.

### P

**Placeholder** – Description of the input desired. Displayed when no selection has been made.

**Poster** – URL of an image to display before playing. Supports data URI in version 1.2+

**Present right-to-left** – When enabled, content in the container should be presented right to left. When disabled, content in this container should be presented left to right. When unset, layout direction will inherit from parent container or column. If unset in all ancestors, the default platform behavior applies.

### R

**Regex** – Regular expression indicating the required format of this text input.

**Repeat for every** – Repeat for every is used to display a control multiple times based on a data source. The repeat for every property is set to a collection or data source, then the relevant property can use `ThisItem` to reference specific items within the collection or data source.

By using the Dataverse Accounts table and a text label's **Repeat for every** property, a maker can create a card that displays the account name of every account within the Accounts table.

1. Add the Accounts table using the [Dataverse connection](../make-a-card/connectors/connector-intro.md).
1. Add a text label control.
1. Set the text label **Repeat for every** property to `Accounts`.
1. Set the text label **Text** property to `ThisItem.'Account Name'`.
1. Play the card, which shows a list of text labels the length of the Accounts table, each one displaying an account name.


**Required field** – Whether or not this input is required.


### S

**Screen** - The screen that is shown below the current card when a user taps or clicks on a button of type 'Show Screen'.

**Show grid lines** – Specifies whether grid lines should be displayed.

**Show when** – Conditional layout expression.

**Size** – Controls the approximate size of the image or text.

**Sources** - The media content to play. Plays the first one specified by default.

**Spacing** – Controls the amount of spacing between this control and the preceding control.

**Style** - Determines the styling of the control.

**Subtle** – If true, displays text slightly toned down to appear less prominent.

### T

**Target Elements** - The elements to change the visibility of when a user taps or clicks on a button of type 'Toggle Visibility'.

**Text** – Text to display. A subset of markdown is supported (https://aka.ms/ACTextFeatures).

**Title** - Label for this button.

**Tooltip** - Defines text that should be displayed to the end user as they hover the mouse over the action, and read when using narration software.

**Type** –  What action the button should take on select - can be Show Screen, Run Power Fx, Open Url, or Toggle Visibility.

### U

**Url** – The URL to the image or to open when a button is selected. Supports data URI in version 1.2+.

### V

**Value** – The initial item (or set of items) that should be selected. For multi-select, specify a comma-separated string of values.


### W

**Weight** – Controls the weight of the text.

**Width** – The desired width of a property.

**Wrap** – If true, allow text to wrap. Otherwise, text is clipped.
