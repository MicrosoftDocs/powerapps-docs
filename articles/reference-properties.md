<properties
   pageTitle="Find a property | Microsoft PowerApps"
   description="Find a property by control, by category, or alphabetically."
   services=""
   suite="powerapps"
   documentationCenter="na"
   authors="aftowen"
   manager="erikre"
   editor=""
   tags=""/>
<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="03/17/2016"
   ms.author="anneta"/>

# Controls and properties in PowerApps #

Configure the appearance and behavior of a control by setting one of its properties. Each type of control has a different set of properties. Some properties, such as **Height** and **Width**, are common to almost every type of control, but other properties, such as **CheckboxSize**, are specific to one type of control.

## Controls ##

**[Add picture](control-add-picture.md)** – Add image files to a data source.

**[Audio](control-audio-video.md)** – Play an audio clip or the audio portion of a video clip.

**[Button](control-button.md)** – Interact with the app by clicking or tapping.

**[Camera](control-camera.md)** – Take and save photos in the app or to a data source.

**[Card](control-card.md)** – Display and edit an individual field of a record in a **[Form](control-form-detail.md)** or **[View form](control-form-detail.md)** control.

**[Check box](control-check-box.md)** – Select or clear an option to specify **true** or **false**.

**[Column chart](control-column-line-chart.md)** – Show values as vertical bars relative to two axes.

**[Date picker](control-date-picker.md)** – Specify a date by clicking or tapping.

**[Display form](control-form-detail.md)** – Display records in a data source using a form.

**[Drop down](control-drop-down.md)** – Show the first item in a list until a chevron is selected.

**[Edit form](control-form-detail.md)** – Edit and create records in a data source using a form.

**[Export](control-export-import.md)** – Export data for use elsewhere in PowerApps.

**[Gallery](control-gallery.md)** – Show a list of records that can contain multiple types of data.

**[HTML text](control-html-text.md)** – Convert HTML tags automatically.

**[Icons](control-shapes-icons.md)** – Add graphic appeal and visual interest.

**[Image](control-image.md)** – Show an image from, for example, a local file or a data source.

**[Import](control-export-import.md)** – Import data from elsewhere in PowerApps.

**[Line chart](control-column-line-chart.md)** – Show values as data points relative to two axes.

**[List box](control-list-box.md)** – Select one or more items in a list.

**[Microphone](control-microphone.md)** – Record and save sounds in the app or to a data source.

**[PDF viewer](control-pdf-viewer.md)** – Show the content of a PDF file on the Internet.

**[Pen input](control-pen-input.md)** – Draw an image or text, and save it in the app or to a data source.

**[Pie chart](control-pie-chart.md)** – Show how values relate to each other.

**[Radio buttons](control-radio.md)** – Show options that are mutually exclusive.

**[Rating](control-rating.md)** – Indicate a value between 1 and a specified number.

**[Screen](control-screen.md)** – Show and update data about a specific task.

**[Shapes](control-shapes-icons.md)** – Display arrows and geometric shapes, such as rectangles.

**[Slider](control-slider.md)** – Specify a value by dragging a handle.

**[Text box](control-text-box.md)** – Shows data such as text, numbers, dates, or currency,

**[Text input](control-text-input.md)** – Type text, numbers, and other data.

**[Timer](control-timer.md)** – Configure your app to respond after a certain amount of time passes.

**[Toggle](control-toggle.md)** – Drag a handle to specify **true** or **false**.

**[Video](control-audio-video.md)** – Play a video clip from a local file, a data source, or YouTube.

## Common properties by category ##

**[Color and border](properties-color-border.md)** – Configure the color and border of a control that can change as a user interacts with it.

**[Core](properties-core.md)** – Configure whether the user can see and interact with a control.

**[Image](properties-visual.md)** – Configure what image is shown and how it fills the control.

**[Size and location](properties-size-location.md)** – Configure how big a control (or an element of a control) is and where it is in relation to the screen it's on.

**[Text](properties-text.md)** – Configure how text appears in controls, such as font characteristics, alignment, line height.  

## All properties ##

### A ###

[**Align**](properties\properties-text.md) – The location of text in relation to the horizontal center of its control.  Applies to many controls.

**AutoDisableOnSelect** – Automatically disables the control while the OnSelect behavior is executing.  Applies to [**Button**](controls\control-button.md) and [**Image**](controls\control-image.md) controls.

[**AutoHeight**](controls\control-text-box.md) – Whether a text box automatically increases its **Height** property if its **Text** property contains more characters than the control can show at one time.  Applies to the [**Text box**](controls\control-text-box.md) control.

**AutoPause** – Whether an audio or video clip automatically pauses if the user navigates to a different screen.  Applies to [**Audio**](controls\control-audio-video.md), [**Video**](controls\control-audio-video.md), and [**Timer**](controls\control-timer.md) controls.

**AutoStart** – Whether an audio or video control automatically starts to play a clip when the user navigates to the screen that contains that control.  Applies to [**Audio**](controls\control-audio-video.md), [**Video**](controls\control-audio-video.md), and [**Timer**](controls\control-timer.md) controls.

### B ###

[**BackgroundImage**](properties\properties-visual.md) – The name of an image file that appears in the background of a screen.  Applies to the [**Screen**](controls\control-screen.md) control.

[**BorderColor**](properties\properties-color-border.md) – The color of a control's border.  Applies to many controls.

[**BorderStyle**](properties\properties-color-border.md) – Whether a control's border is **Solid**, **Dashed**, **Dotted**, or **None**.  Applies to many controls.

[**BorderThickness**](properties\properties-color-border.md) – The thickness of a control's border.  Applies to many controls.

[**Brightness**](controls\control-camera.md) – How much light the user is likely to perceive in an image.  Applies to the [**Camera**](controls\control-camera.md) control.

### C ###

[**Camera**](controls\control-camera.md) – On a device that has more than one camera, the numeric ID of the camera that the app uses.  Applies to the [**Camera**](controls\control-camera.md) control.

[**CheckboxBackgroundFill**](controls\control-check-box.md) – The background color of the box that surrounds the checkmark in a checkbox control.  Applies to the [**Check Box**](controls\control-check-box.md) control.

[**CheckboxBorderColor**](controls\control-check-box.md) – The color of the border that surrounds the checkmark in a checkbox control.  Applies to the [**Check Box**](controls\control-check-box.md) control.

[**CheckboxSize**](controls\control-check-box.md) – The width and height of the box that surrounds the checkmark in a checkbox control.  Applies to the [**Check Box**](controls\control-check-box.md) control.

[**CheckmarkFill**](controls\control-check-box.md) – The color of the checkmark in a checkbox control.  Applies to the [**Check Box**](controls\control-check-box.md) control.

[**ChevronBackground**](controls\control-drop-down.md) – The color behind the down arrow in a dropdown list.  Applies to the [**Drop down**](controls\control-drop-down.md) control.

[**ChevronFill**](controls\control-drop-down.md) – The color of the down arrow in a dropdown list.  Applies to the [**Drop down**](controls\control-drop-down.md) control.

[**Clear**](controls\control-text-input.md) – Whether a text-input control shows an "X" that the user can tap or click to clear the contents of that control.  Applies to the [**Text input**](controls\control-text-input.md) control.

[**Color**](properties\properties-color-border.md) – The color of text in a control.  Applies to many controls.

[**Contrast**](controls\control-camera.md) – How easily the user can distinguish between similar colors in an image.  Applies to the [**Camera**](controls\control-camera.md) control.

### D ###

[**Data**](controls\control-export-import.md) – The name of a collection that you want to export to a local file.  Applies to the [**Export**](controls\control-export-import.md) control.

[**DataField**](controls\control-card.md) – The name of the field within a record that this card displays and edits.  Applies to the [**Card**](controls\control-card.md) control.

[**DataSource**](controls\control-form-detail.md) – The data source that contains the record that the user will show, edit, or create.  Applies to [**Edit form**](controls\control-form-detail.md) and [**Display form**](controls\control-form-detail.md) controls.

[**Default**](properties\properties-core.md) – The initial value of a control before it is changed by the user.  Applies to many controls.

[**Direction**](controls\control-gallery.md) – Whether the first item in a gallery in landscape orientation appears near the left or right edge.  Applies to the [**Gallery**](controls\control-gallery.md) control.

[**Disabled**](properties\properties-core.md) – Whether the user can interact with the control.  Applies to many controls.

[**DisabledBorderColor**](properties\properties-color-border.md) – The color of a control's border if the control's **Disabled** property is set to **true**.  Applies to many controls.

[**DisabledColor**](properties\properties-color-border.md) – The color of text in a control if its **Disabled** property is set to **true**.  Applies to many controls.

[**DisabledFill**](properties\properties-color-border.md) – The background color of a control if its **Disabled** property is set to **true**.  Applies to many controls.

[**DisplayName**](controls\control-card.md) – The user friendly name for a field in a data source.  Applies to the [**Card**](controls\control-card.md) control.

[**Document**](controls\control-pdf-viewer.md) – The URL, enclosed in double-quotation marks, of a PDF file.  Applies to the [**PDF viewer**](controls\control-pdf-viewer.md) control.

[**Duration**](controls\control-timer.md) – How long a timer runs.  Applies to the [**Timer**](controls\control-timer.md) control.

### E ###

[**EndYear**](controls\control-date-picker.md) – The latest year to which the user can set value of a date-picker control.  Applies to the [**Date Picker**](controls\control-date-picker.md) control.

**Error** – The meaning of this property is dependent on the control: 

- [**Card**](controls\control-card.md) control – The user friendly error message to display for this field when validation fails.
- [**Edit form**](controls\control-form-detail.md) control – A user friendly error message to display for this form when the **SubmitForm** function fails.

[**ErrorKind**](controls\control-form-detail.md) – If an error occurs when **SubmitForm** runs, the kind of error that occurred.  Applies to [**Edit form**](controls\control-form-detail.md) and [**Display form**](controls\control-form-detail.md) controls.

[**Explode**](controls\control-pie-chart.md) – The distance between wedges in a pie chart.  Applies to the [**Pie chart**](controls\control-pie-chart.md) control.

### F ###

[**Fill**](properties\properties-color-border.md) – The background color of a control.  Applies to many controls.

[**Font**](properties\properties-text.md) – The name of the family of fonts in which text appears.  Applies to many controls.

[**FontWeight**](properties\properties-text.md) – The weight of the text in a control: **Bold**, **Semibold**, **Normal**, or **Lighter**.  Applies to many controls.

### G ###

[**GridStyle**](controls\control-column-line-chart.md) – Whether a column or line chart shows its x-axis, its y-axis, both, or neither.  Applies to [**Column chart**](controls\control-column-line-chart.md) and [**Line chart**](controls\control-column-line-chart.md) controls.

### H ###

[**HandleActiveFill**](controls\control-slider.md) – The color of the handle for a slider as the user changes its value.  Applies to the [**Slider**](controls\control-slider.md) control.

[**HandleFill**](controls\control-slider.md) – The color of the handle (the element that changes position) in a toggle or slider control.  Applies to the [**Slider**](controls\control-slider.md) control.

[**HandleHoverFill**](controls\control-slider.md) – The color of the handle in a slider when the user keeps the mouse pointer on it.  Applies to the [**Slider**](controls\control-slider.md) control.

[**Height**](properties\properties-size-location.md) – The distance between a control's top and bottom edges.  Applies to many controls.

[**HintText**](controls\control-text-input.md) – Light-grey text that appears in an input-text control if it's empty.  Applies to the [**Text input**](controls\control-text-input.md) control.

[**HoverBorderColor**](properties\properties-color-border.md) – The color of a control's border when the user keeps the mouse pointer on that control.  Applies to many controls.

[**HoverColor**](properties\properties-color-border.md) – The color of the text in a control when the user keeps the mouse pointer on it.  Applies to many controls.

[**HoverFill**](properties\properties-color-border.md) – The background color of a control when the user keeps the mouse pointer on it.  Applies to many controls.

[**HTMLText**](controls\control-html-text.md) – Text that appears in an HTML text control and that may contain HTML tags.  Applies to the [**HTML text**](controls\control-html-text.md) control.

### I ###

[**Image**](properties\properties-visual.md) – The name of the image that appears in an image, audio, or microphone control.  Applies to [**Audio**](controls\control-audio-video.md), [**Video**](controls\control-audio-video.md), [**Image**](controls\control-image.md), and [**Microphone**](controls\control-microphone.md) controls.

[**ImagePosition**](properties\properties-visual.md) – The position (**Fill**, **Fit**, **Stretch**, **Tile**, or **Center**) of an image in a screen or a control if it isn't the same size as the image.  Applies to many controls.

[**Input**](controls\control-pen-input.md) – Input.  Applies to the [**Pen input**](controls\control-pen-input.md) control.

[**Italic**](properties\properties-text.md) – Whether the text in a control is italic.  Applies to many controls.

[**Item**](controls\control-form-detail.md) – The record in the **DataSource** that the user will show or edit.  Applies to [**Edit form**](controls\control-form-detail.md) and [**Display form**](controls\control-form-detail.md) controls.

[**ItemBorderColor**](controls\control-pie-chart.md) – The color of the border around each wedge in a pie chart.  Applies to the [**Pie chart**](controls\control-pie-chart.md) control.

[**ItemBorderThickness**](controls\control-pie-chart.md) – The thickness of the border around each wedge in a pie chart.  Applies to the [**Pie chart**](controls\control-pie-chart.md) control.

**ItemColorSet** – The color of each data point in a chart.  Applies to [**Column chart**](controls\control-column-line-chart.md), [**Line chart**](controls\control-column-line-chart.md), and [**Pie chart**](controls\control-pie-chart.md) controls.

[**ItemPaddingLeft**](controls\control-list-box.md) – The distance between text in a listbox and its left edge.  Applies to the [**List Box**](controls\control-list-box.md) control.

[**Items**](properties\properties-core.md) – The source of data that appears in a control such as a gallery, a list, or a chart.  Applies to many controls.

[**ItemsGap**](controls\control-column-line-chart.md) – The distance between columns in a column chart.  Applies to the [**Column chart**](controls\control-column-line-chart.md) control.

### L ###

[**LabelPosition**](controls\control-pie-chart.md) – The location of labels in a pie chart relative to its wedges.  Applies to the [**Pie chart**](controls\control-pie-chart.md) control.

[**LastSubmit**](controls\control-form-detail.md) – The last successfully submitted record, including any server generated fields.  Applies to the [**Edit form**](controls\control-form-detail.md) control.

**Layout** – Whether the user scrolls through a gallery or adjusts a slider top to bottom (**Vertical**) or left to right (**Horizontal**).  Applies to [**Gallery**](controls\control-gallery.md) and [**Slider**](controls\control-slider.md) controls.

[**LineHeight**](properties\properties-text.md) – The distance between, for example, lines of text or items in a list.  Applies to [**List Box**](controls\control-list-box.md), [**Radio**](controls\control-radio.md), [**Text box**](controls\control-text-box.md), and [**Text input**](controls\control-text-input.md) controls.

[**Loop**](controls\control-audio-video.md) – Whether an audio or video clip automatically starts over as soon as it finishes playing.  Applies to [**Audio**](controls\control-audio-video.md) and [**Video**](controls\control-audio-video.md) controls.

### M ###

[**Markers**](controls\control-column-line-chart.md) – Whether a column or line chart shows the value of each data point.  Applies to [**Column chart**](controls\control-column-line-chart.md) and [**Line chart**](controls\control-column-line-chart.md) controls.

[**MarkerSuffix**](controls\control-column-line-chart.md) – Text that appears after each value in a column chart for which the **Markers** property is set to **true**.  Applies to the [**Column chart**](controls\control-column-line-chart.md) control.

**Max** – The maximum value to which the user can set a slider or a rating.  Applies to [**Rating**](controls\control-rating.md) and [**Slider**](controls\control-slider.md) controls.

[**MaxLength**](controls\control-text-input.md) – The number of characters that the user can type into a text-input control.  Applies to the [**Text input**](controls\control-text-input.md) control.

[**Media**](controls\control-audio-video.md) – An identifier for the clip that an audio or video control plays.  Applies to [**Audio**](controls\control-audio-video.md) and [**Video**](controls\control-audio-video.md) controls.

[**Mic**](controls\control-microphone.md) – On a device that has more than one microphone, the numeric ID of the microphone that the app uses.  Applies to the [**Microphone**](controls\control-microphone.md) control.

[**Min**](controls\control-slider.md) – The minimum value to which the user can set a slider.  Applies to the [**Slider**](controls\control-slider.md) control.

[**MinimumBarWidth**](controls\control-column-line-chart.md) – The narrowest possible width of columns in a column chart.  Applies to the [**Column chart**](controls\control-column-line-chart.md) control.

**Mode** – The meaning of this property is dependent on the control: 

- [**Edit form**](controls\control-form-detail.md) control – The control is in **Edit** or **New** mode.
- [**Pen input**](controls\control-pen-input.md) control – The control is in **Draw**, **Erase**, or **Select** mode.
- [**Text input**](controls\control-text-input.md) control – The control is in **SingleLine**, **MultiLine**, or **Password** mode.

### N ###

[**NavigationStep**](controls\control-gallery.md) – How far a gallery scrolls if its **ShowNavigation** property is set to **true** and the user selects a navigation arrow at either end of that gallery.  Applies to the [**Gallery**](controls\control-gallery.md) control.

[**NumberOfSeries**](controls\control-column-line-chart.md) – How many columns of data are reflected in a column or line chart.  Applies to [**Column chart**](controls\control-column-line-chart.md) and [**Line chart**](controls\control-column-line-chart.md) controls.

### O ###

[**OnChange**](properties\properties-core.md) – How the app responds when the user changes the value of a control (for example, by adjusting a slider).  Applies to many controls.

**OnCheck** – How an app responds when the value of a checkbox or a toggle changes to **true**.  Applies to [**Check Box**](controls\control-check-box.md) and [**Toggle**](controls\control-toggle.md) controls.

[**OnEnd**](controls\control-audio-video.md) – How an app responds when an audio or video clip finishes playing.  Applies to [**Audio**](controls\control-audio-video.md) and [**Video**](controls\control-audio-video.md) controls.

[**OnFailure**](controls\control-form-detail.md) – How an app responds when a data operation has been unsuccessful.  Applies to the [**Edit form**](controls\control-form-detail.md) control.

[**OnHidden**](controls\control-screen.md) – How an app responds when the user navigates away from a screen.  Applies to the [**Screen**](controls\control-screen.md) control.

[**OnPause**](controls\control-audio-video.md) – How an app responds when the user pauses the clip that an audio or video control is playing.  Applies to [**Audio**](controls\control-audio-video.md) and [**Video**](controls\control-audio-video.md) controls.

[**OnReset**](controls\control-form-detail.md) – How an app responds when an **Edit form** control is reset.  Applies to the [**Edit form**](controls\control-form-detail.md) control.

[**OnSelect**](properties\properties-core.md) – How the app responds when the user taps or clicks a control.  Applies to many controls.

**OnStart** – How the app responds when the user starts to record with a microphone control.  Applies to [**Audio**](controls\control-audio-video.md), [**Video**](controls\control-audio-video.md), and [**Microphone**](controls\control-microphone.md) controls.

[**OnStop**](controls\control-microphone.md) – How the app responds when the user stops recording with a microphone control.  Applies to the [**Microphone**](controls\control-microphone.md) control.

[**OnStream**](controls\control-camera.md) – OnStream.  Applies to the [**Camera**](controls\control-camera.md) control.

[**OnSuccess**](controls\control-form-detail.md) – How an app responds when a data operation has been successful.  Applies to the [**Edit form**](controls\control-form-detail.md) control.

[**OnTimerEnd**](controls\control-timer.md) – How an app responds when a timer finishes running.  Applies to the [**Timer**](controls\control-timer.md) control.

[**OnTimerStart**](controls\control-timer.md) – How an app responds when a timer starts to run.  Applies to the [**Timer**](controls\control-timer.md) control.

**OnUncheck** – How an app responds when the value of a checkbox or a toggle changes to **false**.  Applies to [**Check Box**](controls\control-check-box.md) and [**Toggle**](controls\control-toggle.md) controls.

[**OnVisible**](controls\control-screen.md) – How an app responds when the user navigates to a screen.  Applies to the [**Screen**](controls\control-screen.md) control.

[**Overflow**](controls\control-text-box.md) – Whether a scrollbar appears in a text box if its **Wrap** property is set to **true** and the value of the control's **Text** property contains more characters than the control can show at one time.  Applies to the [**Text box**](controls\control-text-box.md) control.

### P ###

[**Padding**](properties\properties-size-location.md) – The distance between the text on an import or export button and the edges of that button.  Applies to [**Export**](controls\control-export-import.md) and [**Import**](controls\control-export-import.md) controls.

[**PaddingBottom**](properties\properties-size-location.md) – The distance between text in a control and the bottom edge of that control.  Applies to many controls.

[**PaddingLeft**](properties\properties-size-location.md) – The distance between text in a control and the left edge of that control.  Applies to many controls.

[**PaddingRight**](properties\properties-size-location.md) – The distance between text in a control and the right edge of that control.  Applies to many controls.

[**PaddingTop**](properties\properties-size-location.md) – The distance between text in a control and the top edge of that control.  Applies to many controls.

[**Page**](controls\control-pdf-viewer.md) – The number of the page in a PDF file that you want to show.  Applies to the [**PDF viewer**](controls\control-pdf-viewer.md) control.

[**PressedBorderColor**](properties\properties-color-border.md) – The color of a control's border when the user taps or clicks that control.  Applies to many controls.

[**PressedColor**](properties\properties-color-border.md) – The color of text in a control when the user taps or clicks that control.  Applies to many controls.

[**PressedFill**](properties\properties-color-border.md) – The background color of a control when the user taps or clicks that control.  Applies to many controls.

### R ###

[**RadioBackgroundFill**](controls\control-radio.md) – The background color of the circles in a radio-button control.  Applies to the [**Radio**](controls\control-radio.md) control.

[**RadioBorderColor**](controls\control-radio.md) – The color of the circle for each option in a radio-button control.  Applies to the [**Radio**](controls\control-radio.md) control.

[**RadioSelectionFill**](controls\control-radio.md) – The color that appears inside the circle of the selected option in a radio-button control.  Applies to the [**Radio**](controls\control-radio.md) control.

[**RadioSize**](controls\control-radio.md) – The diameter of the circles in a radio-button control.  Applies to the [**Radio**](controls\control-radio.md) control.

[**RadiusBottomLeft**](properties\properties-size-location.md) – The degree to which the bottom-left corner of a control is rounded.  Applies to many controls.

[**RadiusBottomRight**](properties\properties-size-location.md) – The degree to which the bottom-right corner of a control is rounded.  Applies to many controls.

[**RadiusTopLeft**](properties\properties-size-location.md) – The degree to which the top-left corner of a control is rounded.  Applies to many controls.

[**RadiusTopRight**](properties\properties-size-location.md) – The degree to which the top-right corner of a control is rounded.  Applies to many controls.

**RailFill** – The background color of the rectangle in a toggle control when its value is **false** or the color of the line to the right of the handle in a slider control.  Applies to [**Slider**](controls\control-slider.md) and [**Toggle**](controls\control-toggle.md) controls.

**RailHoverFill** – When you hover on a toggle control or a slider, the background color of the rectangle in a toggle control when its value is **false** or the color of the line to the right of the handle in a slider control.  Applies to [**Slider**](controls\control-slider.md) and [**Toggle**](controls\control-toggle.md) controls.

[**RatingFill**](controls\control-rating.md) – The color of the stars in a rating control.  Applies to the [**Rating**](controls\control-rating.md) control.

**ReadOnly** – Whether a user can change the value of a slider or rating control.  Applies to [**Rating**](controls\control-rating.md) and [**Slider**](controls\control-slider.md) controls.

[**Repeat**](controls\control-timer.md) – Whether a timer automatically restarts when it finishes running.  Applies to the [**Timer**](controls\control-timer.md) control.

[**Required**](controls\control-card.md) – Whether a card, editing the field of a data source, must contain a value.  Applies to the [**Card**](controls\control-card.md) control.

[**Reset**](properties\properties-core.md) – Whether a control reverts to its default value.  Applies to many controls.

### S ###

[**SelectionColor**](properties\properties-color-border.md) – The text color of a selected item or items in a list or the color of the selection tool in a pen control.  Applies to [**Drop down**](controls\control-drop-down.md), [**List Box**](controls\control-list-box.md), and [**Pen input**](controls\control-pen-input.md) controls.

[**SelectionFill**](properties\properties-color-border.md) – The background color of a selected item or items in a list or a selected area of a pen control.  Applies to [**Drop down**](controls\control-drop-down.md) and [**List Box**](controls\control-list-box.md) controls.

[**SelectionThickness**](controls\control-pen-input.md) – The thickness of the selection tool for a pen-input control.  Applies to the [**Pen input**](controls\control-pen-input.md) control.

[**SelectMultiple**](controls\control-list-box.md) – Whether a user can select more than one item in a listbox.  Applies to the [**List Box**](controls\control-list-box.md) control.

[**SeriesAxisMax**](controls\control-column-line-chart.md) – The maximum value of the y-axis for a column or line chart.  Applies to the [**Column chart**](controls\control-column-line-chart.md) control.

[**SeriesAxisMin**](controls\control-column-line-chart.md) – A number that determines the minimum value of the y-axis for a column chart.  Applies to the [**Column chart**](controls\control-column-line-chart.md) control.

**ShowControls** – Whether an audio or video player shows, for example, a play button and a volume slider, and a pen control shows, for example, icons for drawing, erasing, and clearing.  Applies to [**Audio**](controls\control-audio-video.md), [**Video**](controls\control-audio-video.md), and [**Pen input**](controls\control-pen-input.md) controls.

[**ShowLabels**](controls\control-pie-chart.md) – Whether a pie chart shows the value that's associated with each of its wedges.  Applies to the [**Pie chart**](controls\control-pie-chart.md) control.

[**ShowNavigation**](controls\control-gallery.md) – Whether an arrow appears at each end of a gallery so that a user can scroll through the items in the gallery by clicking or tapping an arrow.  Applies to the [**Gallery**](controls\control-gallery.md) control.

[**ShowScrollbar**](controls\control-gallery.md) – Whether a scrollbar appears when the user hovers over a gallery.  Applies to the [**Gallery**](controls\control-gallery.md) control.

**ShowValue** – Whether a slider's or rating's value appears as the user changes that value or hovers over the control.  Applies to [**Rating**](controls\control-rating.md) and [**Slider**](controls\control-slider.md) controls.

[**Size**](properties\properties-text.md) – The font size of the text that appears on a control.  Applies to many controls.

[**Snap**](controls\control-gallery.md) – Whether, when a user scrolls through a gallery, it automatically snaps so that the next item appears in full.  Applies to the [**Gallery**](controls\control-gallery.md) control.

**Start** – Whether an audio or video clip plays.  Applies to [**Audio**](controls\control-audio-video.md), [**Video**](controls\control-audio-video.md), and [**Timer**](controls\control-timer.md) controls.

[**StartTime**](controls\control-audio-video.md) – The time after the start of an audio or video clip when the clip starts to play.  Applies to [**Audio**](controls\control-audio-video.md) and [**Video**](controls\control-audio-video.md) controls.

[**StartYear**](controls\control-date-picker.md) – The earliest year to which the user can set the value of a date-picker control.  Applies to the [**Date Picker**](controls\control-date-picker.md) control.

[**StreamRate**](controls\control-camera.md) –  Applies to the [**Camera**](controls\control-camera.md) control.

[**Strikethrough**](properties\properties-text.md) – Whether a line appears through the text that appears on a control.  Applies to many controls.

### T ###

[**TemplateFill**](controls\control-gallery.md) – The background color of a gallery.  Applies to the [**Gallery**](controls\control-gallery.md) control.

[**TemplatePadding**](controls\control-gallery.md) – The distance between items in a gallery.  Applies to the [**Gallery**](controls\control-gallery.md) control.

[**TemplateSize**](controls\control-gallery.md) – The height of the template for a gallery in vertical/portrait orientation or the width of the template for a gallery in horizontal/landscape orientation.  Applies to the [**Gallery**](controls\control-gallery.md) control.

[**Text**](properties\properties-core.md) – Text that appears on a control or that the user types into a control.  Applies to many controls.

[**Tooltip**](properties\properties-core.md) – Explanatory text that appears when the user hovers over a control.  Applies to many controls.

[**Transition**](controls\control-gallery.md) – The visual effect (**Pop**, **Push**, or **None**) when the user hovers over an item in a gallery.  Applies to the [**Gallery**](controls\control-gallery.md) control.

[**Transparency**](controls\control-image.md) – The degree to which controls behind an image remain visible.  Applies to the [**Image**](controls\control-image.md) control.

### U ###

[**Underline**](properties\properties-text.md) – Whether a line appears under the text that appears on a control.  Applies to many controls.

[**Unsaved**](controls\control-form-detail.md) – True if the **Edit form** control contains user changes that have not been saved.  Applies to the [**Edit form**](controls\control-form-detail.md) control.

[**Update**](controls\control-card.md) – The value to write back to the data source for a field.  Applies to the [**Card**](controls\control-card.md) control.

### V ###

**Valid** – Whether a **Card** or **Edit form** control contains valid entries, ready to be submitted to the data source.  Applies to [**Card**](controls\control-card.md) and [**Edit form**](controls\control-form-detail.md) controls.

[**Value**](properties\properties-core.md) – The value of an input control.  Applies to [**Radio**](controls\control-radio.md), [**Slider**](controls\control-slider.md), and [**Toggle**](controls\control-toggle.md) controls.

**ValueFill** – The background color of the rectangle in a toggle control when its value is **true** or the color of the line to the left of the handle in a slider control.  Applies to [**Slider**](controls\control-slider.md) and [**Toggle**](controls\control-toggle.md) controls.

**ValueHoverFill** – When you keep the mouse pointer on a toggle control or a slider, the background color of the rectangle in a toggle control when its value is **true** or the color of the line to the left of the handle in a slider control.  Applies to [**Slider**](controls\control-slider.md) and [**Toggle**](controls\control-toggle.md) controls.

[**VerticalAlign**](properties\properties-text.md) – The location of text on a control in relation to the vertical center of that control.  Applies to many controls.

[**Visible**](properties\properties-core.md) – Whether a control appears or is hidden.  Applies to many controls.

### W ###

[**Width**](properties\properties-size-location.md) – The distance between a control's left and right edges.  Applies to many controls.

[**Wrap**](controls\control-text-box.md) – Whether text that's too long to fit in a text box wraps to the next line.  Applies to the [**Text box**](controls\control-text-box.md) control.

[**WrapCount**](controls\control-gallery.md) – How many records appear in each item of a gallery.  Applies to the [**Gallery**](controls\control-gallery.md) control.

### X ###

[**X**](properties\properties-size-location.md) – The distance between the left edge of a control and the left edge of the screen.  Applies to many controls.

[**XLabelAngle**](controls\control-column-line-chart.md) – The angle of the labels below the x-axis of a column or line chart.  Applies to [**Column chart**](controls\control-column-line-chart.md) and [**Line chart**](controls\control-column-line-chart.md) controls.

### Y ###

[**Y**](properties\properties-size-location.md) – The distance between the top edge of a control and the top edge of the screen.  Applies to many controls.

[**YAxisMax**](controls\control-column-line-chart.md) – The maximum value of the y-axis for a line chart.  Applies to the [**Column chart**](controls\control-column-line-chart.md) control.

[**YAxisMin**](controls\control-column-line-chart.md) – The minimum value of the y-axis for a line chart.  Applies to the [**Column chart**](controls\control-column-line-chart.md) control.

[**YLabelAngle**](controls\control-column-line-chart.md) – The angle of the labels next to the y-axis of a line or column chart.  Applies to [**Column chart**](controls\control-column-line-chart.md) and [**Line chart**](controls\control-column-line-chart.md) controls.

### Z ###

**Zoom** – The percentage by which an image from a camera is magnified or the view of a file in a PDF viewer.  Applies to [**Camera**](controls\control-camera.md) and [**PDF viewer**](controls\control-pdf-viewer.md) controls.
