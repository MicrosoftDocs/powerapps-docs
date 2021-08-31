---
title: Controls and properties in canvas apps
description: Learn about properties of different controls in canvas apps.
author: chmoncay
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: tapanm-msft
ms.date: 01/24/2020
ms.subservice: canvas-maker
ms.author: chmoncay
search.audienceType:
  - maker
search.app:
  - PowerApps
contributors:
  - tapanm-msft
  - chmoncay
---
# Controls and properties in canvas apps

Configure the appearance and behavior of a control by setting one of its properties. Each type of control has a different set of properties. Some properties, such as **Height** and **Width**, are common to almost every type of control, but other properties, such as **CheckboxSize**, are specific to one type of control.

## Controls

**[Add picture](controls/control-add-picture.md)** – Load images from the local device, for upload to a data source.

**[Attachments](controls/control-attachments.md)** – Download and upload files from the local device to a data source.

**[Audio](controls/control-audio-video.md)** – Play an audio clip or the audio portion of a video clip.

**[Barcode scanner](controls/control-new-barcode-scanner.md)** – Scans barcodes, QR codes, and data-matrix codes on an Android or iOS device.

**[Button](controls/control-button.md)** – Interact with the app by clicking or tapping.

**[Camera](controls/control-camera.md)** – Take and save photos in the app or to a data source.

**[Card](controls/control-card.md)** – Display and edit an individual field of a record in a **[Edit form](controls/control-form-detail.md)** or **[Display form](controls/control-form-detail.md)** control.

**[Check box](controls/control-check-box.md)** – Select or clear an option to specify **true** or **false**.

**[Column chart](controls/control-column-line-chart.md)** – Show values as vertical bars relative to two axes.

**[Column](controls/control-column.md)** - Provides the display experience for a single field in a [**Data table**](controls/control-data-table.md) control.

**[Combo box](controls/control-combo-box.md)** - Allows users to make selections from provided choices. Supports search and multi-select.

**[Container (experimental)](controls/control-container.md)** - Create nested hierarchy for accessibility and responsiveness. 

**[Data table](controls/control-data-table.md)** - Show data in a tabular format.

**[Date picker](controls/control-date-picker.md)** – Specify a date by clicking or tapping.

**[Display form](controls/control-form-detail.md)** – Display records in a data source using a form.

**[Drop down](controls/control-drop-down.md)** – Show the first item in a list until a chevron is selected.

**[Edit form](controls/control-form-detail.md)** – Edit and create records in a data source using a form.

**[Display and Edit form](./controls/control-form-detail.md)** - Experimental feature: Add dynamic forms in which users can view, navigate, and edit relational data from the Microsoft Dataverse.

**[Export](controls/control-export-import.md)** – Export data for use elsewhere in Power Apps.

**[Gallery](controls/control-gallery.md)** – Show a list of records that can contain multiple types of data.

**[HTML text](controls/control-html-text.md)** – Convert HTML tags automatically.

**[Icon](controls/control-shapes-icons.md)** – Add graphic appeal and visual interest.

**[Image](controls/control-image.md)** – Show an image from, for example, a local file or a data source.

**[Import](controls/control-export-import.md)** – Import data from elsewhere in Power Apps.

**[Line chart](controls/control-column-line-chart.md)** – Show values as data points relative to two axes.

**[List box](controls/control-list-box.md)** – Select one or more items in a list.

**[Microphone](controls/control-microphone.md)** – Record and save sounds in the app or to a data source.

**[PDF viewer (experimental)](controls/control-pdf-viewer.md)** – Show the content of a PDF file on the Internet.

**[Pen input](controls/control-pen-input.md)** – Draw an image or text, and save it in the app or to a data source.

**[Pie chart](controls/control-pie-chart.md)** – Show how values relate to each other.

**[Power BI tile](controls/control-power-bi-tile.md)** – Display a Power BI tile inside an app.

**[Radio](controls/control-radio.md)** – Show options that are mutually exclusive.

**[Rating](controls/control-rating.md)** – Indicate a value between 1 and a specified number.

**[Rich text editor](controls/control-richtexteditor.md)** – Allows rich text formatting by app users.

**[Screen](controls/control-screen.md)** – Show and update data about a specific task.

**[Shape](controls/control-shapes-icons.md)** – Display arrows and geometric shapes, such as rectangles.

**[Slider](controls/control-slider.md)** – Specify a value by dragging a handle.

**[Stream Video](controls/control-stream-video.md)** – Play videos and browse through channels from the Microsoft Stream service.

**[Label](controls/control-text-box.md)** – Shows data such as text, numbers, dates, or currency,

**[Text input](controls/control-text-input.md)** – Type text, numbers, and other data.

**[Timer](controls/control-timer.md)** – Configure your app to respond after a certain amount of time passes.

**[Toggle](controls/control-toggle.md)** – Drag a handle to specify **true** or **false**.

**[Video](controls/control-audio-video.md)** – Play a video clip from a local file, a data source, or YouTube.

**[Web barcode scanner (experimental)](controls/control-barcodescanner.md)** – The legacy barcode scanner, which is obsolete but might be useful for scanning codes in a web browser.

## Common properties by category

**[Color and border](controls/properties-color-border.md)** – Configure the color and border of a control that can change as a user interacts with it.

**[Core](controls/properties-core.md)** – Configure whether the user can see and interact with a control.

**[Image](controls/properties-visual.md)** – Configure what image is shown and how it fills the control.

**[Size and location](controls/properties-size-location.md)** – Configure how big a control (or an element of a control) is and where it is in relation to the screen it's on.

**[Text](controls/properties-text.md)** – Configure how text appears in controls, such as font characteristics, alignment, line height.  

## All properties

### A

**[ActualZoom](controls/control-pdf-viewer.md)** – The actual zoom of the control, which may differ from the zoom requested with the **Zoom** property.  Applies to the **[PDF viewer](controls/control-pdf-viewer.md)** control.

**[Align](controls/properties-text.md)** – The location of text in relation to the horizontal center of its control.  Applies to many controls.

**[AllItems](controls/control-gallery.md)** – All items in a gallery, including additional control values that are a part of the gallery's template.  Applies to the **[Gallery](controls/control-gallery.md)** control.

**AutoDisableOnSelect** – Automatically disables the control while the OnSelect behavior is executing.  Applies to **[Button](controls/control-button.md)** and **[Image](controls/control-image.md)** controls.

**[AutoHeight](controls/properties-size-location.md)** – Whether a label automatically increases its height if its **[Text](controls/properties-core.md)** property contains more characters than the control can show. Applies to the **[Label](controls/control-text-box.md)** control.

**AutoPause** – Whether an audio or video clip automatically pauses if the user navigates to a different screen.  Applies to **[Audio](controls/control-audio-video.md)**, **[Timer](controls/control-timer.md)**, and **[Video](controls/control-audio-video.md)** controls.

**AutoStart** – Whether an audio or video control automatically starts to play a clip when the user navigates to the screen that contains that control.  Applies to **[Audio](controls/control-audio-video.md)**, **[Timer](controls/control-timer.md)**, and **[Video](controls/control-audio-video.md)** controls.

### B

**[BackgroundImage](controls/properties-visual.md)** – The name of an image file that appears in the background of a screen.  Applies to the **[Screen](controls/control-screen.md)** control.

**[BorderColor](controls/properties-color-border.md)** – The color of a control's border.  Applies to many controls.

**[BorderStyle](controls/properties-color-border.md)** – Whether a control's border is **Solid**, **Dashed**, **Dotted**, or **None**.  Applies to many controls.

**[BorderThickness](controls/properties-color-border.md)** – The thickness of a control's border.  Applies to many controls.

**[Brightness](controls/control-camera.md)** – How much light the user is likely to perceive in an image.  Applies to the **[Camera](controls/control-camera.md)** control.

### C

**[CalculateOriginalDimensions](controls/control-image.md)** – Enables the **[OriginalHeight](controls/control-image.md)** and **[OriginalWidth](controls/control-image.md)** properties.  Applies to the **[Image](controls/control-image.md)** control.

**[Camera](controls/control-camera.md)** – On a device that has more than one camera, the numeric ID of the camera that the app uses.  Applies to the **[Camera](controls/control-camera.md)** control.

**[CheckboxBackgroundFill](controls/control-check-box.md)** – The background color of the box that surrounds the checkmark in a checkbox control.  Applies to the **[Check box](controls/control-check-box.md)** control.

**[CheckboxBorderColor](controls/control-check-box.md)** – The color of the border that surrounds the checkmark in a checkbox control.  Applies to the **[Check box](controls/control-check-box.md)** control.

**[CheckboxSize](controls/control-check-box.md)** – The width and height of the box that surrounds the checkmark in a checkbox control.  Applies to the **[Check box](controls/control-check-box.md)** control.

**[CheckmarkFill](controls/control-check-box.md)** – The color of the checkmark in a checkbox control.  Applies to the **[Check box](controls/control-check-box.md)** control.

**[ChevronBackground](controls/control-drop-down.md)** – The color behind the down arrow in a dropdown list.  Applies to the **[Drop down](controls/control-drop-down.md)** control.

**[ChevronFill](controls/control-drop-down.md)** – The color of the down arrow in a dropdown list.  Applies to the **[Drop down](controls/control-drop-down.md)** control.

**[Clear](controls/control-text-input.md)** – Whether a text-input control shows an "X" that the user can tap or click to clear the contents of that control.  Applies to the **[Text input](controls/control-text-input.md)** control.

**[Color](controls/properties-color-border.md)** – The color of text in a control.  Applies to many controls.

**[Contrast](controls/control-camera.md)** – How easily the user can distinguish between similar colors in an image.  Applies to the **[Camera](controls/control-camera.md)** control.

**[CurrentFindText](controls/control-pdf-viewer.md)** – The current search term that is in use.  Applies to the **[PDF viewer](controls/control-pdf-viewer.md)** control.

**[CurrentPage](controls/control-pdf-viewer.md)** – The number of the page in a PDF file that is actually being shown.  Applies to the **[PDF viewer](controls/control-pdf-viewer.md)** control.

### D

**[Data](controls/control-export-import.md)** – The name of a collection that you want to export to a local file.  Applies to the **[Export](controls/control-export-import.md)** control.

**[DataField](controls/control-card.md)** – The name of the field within a record that this card displays and edits.  Applies to the **[Card](controls/control-card.md)** control.

**[DataSource](controls/control-form-detail.md)** – The data source that contains the record that the user will show, edit, or create.  Applies to **[Display form](controls/control-form-detail.md)** and **[Edit form](controls/control-form-detail.md)** controls.

**[Default](controls/properties-core.md)** – The initial value of a control before it is changed by the user.  Applies to many controls.

**[DefaultDate](controls/control-date-picker.md)** – The initial value of a date control before it is changed by the user.  Applies to the **[Date Picker](controls/control-date-picker.md)** control.

**[DefaultMode](controls/control-form-detail.md)** – The initial mode of a form control, either **Edit**, **New**, or **View**.  Applies to the **[Edit form](controls/control-form-detail.md)** control.

**[Direction](controls/control-gallery.md)** – Whether the first item in a gallery in landscape orientation appears near the left or right edge.  Applies to the **[Gallery](controls/control-gallery.md)** control.

**[Disabled](controls/properties-core.md)** – Whether the user can interact with the control.  Applies to many controls.

**[DisabledBorderColor](controls/properties-color-border.md)** – The color of a control's border if the control's **[Disabled](controls/properties-core.md)** property is set to **true**.  Applies to many controls.

**[DisabledColor](controls/properties-color-border.md)** – The color of text in a control if its **[Disabled](controls/properties-core.md)** property is set to **true**.  Applies to many controls.

**[DisabledFill](controls/properties-color-border.md)** – The background color of a control if its **[Disabled](controls/properties-core.md)** property is set to **true**.  Applies to many controls.

**[DisplayName](controls/control-card.md)** – The user friendly name for a field in a data source.  Applies to the **[Card](controls/control-card.md)** control.

**[DisplayMode](controls/properties-core.md)** – Values can be Edit, View, or Disabled. Configures whether the control allows user input (Edit), only displays data (View) or is disabled (Disabled).

**[Document](controls/control-pdf-viewer.md)** – The URL, enclosed in double-quotation marks, of a PDF file.  Applies to the **[PDF viewer](controls/control-pdf-viewer.md)** control.

**[Duration](controls/control-timer.md)** – How long a timer runs.  Applies to the **[Timer](controls/control-timer.md)** control.

### E

**[EndYear](controls/control-date-picker.md)** – The latest year to which the user can set value of a date-picker control.  Applies to the **[Date Picker](controls/control-date-picker.md)** control.

**Error** – The meaning of this property is dependent on the control:

* **[Add picture](controls/control-add-picture.md)** control - If there is a problem uploading an image, this property will contain an appropriate error string.
* **[Card](controls/control-card.md)** control – The user friendly error message to display for this field when validation fails.
* **[Edit form](controls/control-form-detail.md)** control – A user friendly error message to display for this form when the **[SubmitForm](functions/function-form.md)** function fails.

**[ErrorKind](controls/control-form-detail.md)** – If an error occurs when **SubmitForm** runs, the kind of error that occurred.  Applies to **[Display form](controls/control-form-detail.md)** and **[Edit form](controls/control-form-detail.md)** controls.

**[Explode](controls/control-pie-chart.md)** – The distance between wedges in a pie chart.  Applies to the **[Pie chart](controls/control-pie-chart.md)** control.

### F

**[Fill](controls/properties-color-border.md)** – The background color of a control.  Applies to many controls.

**[FindNext](controls/control-pdf-viewer.md)** – Finds the next instance of **FindText** in the document.  Applies to the **[PDF viewer](controls/control-pdf-viewer.md)** control.

**[FindPrevious](controls/control-pdf-viewer.md)** – Finds the previous instance of **FindText** in the document.  Applies to the **[PDF viewer](controls/control-pdf-viewer.md)** control.

**[FindText](controls/control-pdf-viewer.md)** – The search term to look for in the document.  Applies to the **[PDF viewer](controls/control-pdf-viewer.md)** control.

**[Font](controls/properties-text.md)** – The name of the family of fonts in which text appears.  Applies to many controls.

**[FontWeight](controls/properties-text.md)** – The weight of the text in a control: **Bold**, **Semibold**, **Normal**, or **Lighter**.  Applies to many controls.

### G

**[GridStyle](controls/control-column-line-chart.md)** – Whether a column or line chart shows its x-axis, its y-axis, both, or neither.  Applies to **[Column chart](controls/control-column-line-chart.md)** and **[Line chart](controls/control-column-line-chart.md)** controls.

### H

**[HandleActiveFill](controls/control-slider.md)** – The color of the handle for a slider as the user changes its value.  Applies to the **[Slider](controls/control-slider.md)** control.

**[HandleFill](controls/control-slider.md)** – The color of the handle (the element that changes position) in a toggle or slider control.  Applies to the **[Slider](controls/control-slider.md)** control.

**[HandleHoverFill](controls/control-slider.md)** – The color of the handle in a slider when the user keeps the mouse pointer on it.  Applies to the **[Slider](controls/control-slider.md)** control.

**[Height](controls/properties-size-location.md)** – The distance between a control's top and bottom edges.  Applies to many controls.

**[HintText](controls/control-text-input.md)** – Light-grey text that appears in a text-input control if it's blank.  Applies to the **[Text input](controls/control-text-input.md)** control.

**[HoverBorderColor](controls/properties-color-border.md)** – The color of a control's border when the user keeps the mouse pointer on that control.  Applies to many controls.

**[HoverColor](controls/properties-color-border.md)** – The color of the text in a control when the user keeps the mouse pointer on it.  Applies to many controls.

**[HoverFill](controls/properties-color-border.md)** – The background color of a control when the user keeps the mouse pointer on it.  Applies to many controls.

**[HTMLText](controls/control-html-text.md)** – Text that appears in an HTML text control and that may contain HTML tags.  Applies to the **[HTML text](controls/control-html-text.md)** control.

### I

**[Image](controls/properties-visual.md)** – The name of the image that appears in an image, audio, or microphone control.  Applies to **[Audio](controls/control-audio-video.md)**, **[Image](controls/control-image.md)**, **[Microphone](controls/control-microphone.md)**, and **[Video](controls/control-audio-video.md)** controls.

**[ImagePosition](controls/properties-visual.md)** – The position (**Fill**, **Fit**, **Stretch**, **Tile**, or **Center**) of an image in a screen or a control if it isn't the same size as the image.  Applies to many controls.

**[Input](controls/control-pen-input.md)** – Input.  Applies to the **[Pen input](controls/control-pen-input.md)** control.

**[Italic](controls/properties-text.md)** – Whether the text in a control is italic.  Applies to many controls.

**[Item](controls/control-form-detail.md)** – The record in the **DataSource** that the user will show or edit.  Applies to **[Display form](controls/control-form-detail.md)** and **[Edit form](controls/control-form-detail.md)** controls.

**[ItemBorderColor](controls/control-pie-chart.md)** – The color of the border around each wedge in a pie chart.  Applies to the **[Pie chart](controls/control-pie-chart.md)** control.

**[ItemBorderThickness](controls/control-pie-chart.md)** – The thickness of the border around each wedge in a pie chart.  Applies to the **[Pie chart](controls/control-pie-chart.md)** control.

**ItemColorSet** – The color of each data point in a chart.  Applies to **[Column chart](controls/control-column-line-chart.md)**, **[Line chart](controls/control-column-line-chart.md)**, and **[Pie chart](controls/control-pie-chart.md)** controls.

**[ItemPaddingLeft](controls/control-list-box.md)** – The distance between text in a listbox and its left edge.  Applies to the **[List Box](controls/control-list-box.md)** control.

**[Items](controls/properties-core.md)** – The source of data that appears in a control such as a gallery, a list, or a chart.  Applies to many controls.

**[ItemsGap](controls/control-column-line-chart.md)** – The distance between columns in a column chart.  Applies to the **[Column chart](controls/control-column-line-chart.md)** control.

### L

**[LabelPosition](controls/control-pie-chart.md)** – The location of labels in a pie chart relative to its wedges.  Applies to the **[Pie chart](controls/control-pie-chart.md)** control.

**[LastSubmit](controls/control-form-detail.md)** – The last successfully submitted record, including any server generated fields.  Applies to the **[Edit form](controls/control-form-detail.md)** control.

**Layout** – Whether the user scrolls through a gallery or adjusts a slider top to bottom (**Vertical**) or left to right (**Horizontal**).  Applies to **[Gallery](controls/control-gallery.md)** and **[Slider](controls/control-slider.md)** controls.

**[LineHeight](controls/properties-text.md)** – The distance between, for example, lines of text or items in a list.  Applies to **[List Box](controls/control-list-box.md)**, **[Radio](controls/control-radio.md)**, **[Label](controls/control-text-box.md)**, and **[Text input](controls/control-text-input.md)** controls.

**[Loop](controls/control-audio-video.md)** – Whether an audio or video clip automatically starts over as soon as it finishes playing.  Applies to **[Audio](controls/control-audio-video.md)** and **[Video](controls/control-audio-video.md)** controls.

### M

**[Markers](controls/control-column-line-chart.md)** – Whether a column or line chart shows the value of each data point.  Applies to **[Column chart](controls/control-column-line-chart.md)** and **[Line chart](controls/control-column-line-chart.md)** controls.

**[MarkerSuffix](controls/control-column-line-chart.md)** – Text that appears after each value in a column chart for which the **[Markers](controls/control-column-line-chart.md)** property is set to **true**.  Applies to the **[Column chart](controls/control-column-line-chart.md)** control.

**Max** – The maximum value to which the user can set a slider or a rating.  Applies to **[Rating](controls/control-rating.md)** and **[Slider](controls/control-slider.md)** controls.

**[MaxLength](controls/control-text-input.md)** – The number of characters that the user can type into a text-input control.  Applies to the **[Text input](controls/control-text-input.md)** control.

**Media** – An identifier for the clip that an audio or video control plays.  Applies to **[Add picture](controls/control-add-picture.md)**, **[Audio](controls/control-audio-video.md)**, and **[Video](controls/control-audio-video.md)** controls.

**[Mic](controls/control-microphone.md)** – On a device that has more than one microphone, the numeric ID of the microphone that the app uses.  Applies to the **[Microphone](controls/control-microphone.md)** control.

**[Min](controls/control-slider.md)** – The minimum value to which the user can set a slider.  Applies to the **[Slider](controls/control-slider.md)** control.

**[MinimumBarWidth](controls/control-column-line-chart.md)** – The narrowest possible width of columns in a column chart.  Applies to the **[Column chart](controls/control-column-line-chart.md)** control.

**Mode** – The meaning of this property is dependent on the control:

* **[Edit form](controls/control-form-detail.md)** control – The control is in **Edit** or **New** mode.
* **[Pen input](controls/control-pen-input.md)** control – The control is in **Draw**, **Erase**, or **Select** mode.
* **[Text input](controls/control-text-input.md)** control – The control is in **SingleLine**, **MultiLine**, or **Password** mode.

### N

**[NavigationStep](controls/control-gallery.md)** – How far a gallery scrolls if its **[ShowNavigation](controls/control-gallery.md)** property is set to **true** and the user selects a navigation arrow at either end of that gallery.  Applies to the **[Gallery](controls/control-gallery.md)** control.

**[NumberOfSeries](controls/control-column-line-chart.md)** – How many columns of data are reflected in a column or line chart.  Applies to **[Column chart](controls/control-column-line-chart.md)** and **[Line chart](controls/control-column-line-chart.md)** controls.

### O

**[OnChange](controls/properties-core.md)** – The behavior of an app when the user changes the value of a control (for example, by adjusting a slider).  Applies to many controls.

**OnCheck** – The behavior of an app when the value of a checkbox or a toggle changes to **true**.  Applies to **[Check box](controls/control-check-box.md)** and **[Toggle](controls/control-toggle.md)** controls.

**[OnEnd](controls/control-audio-video.md)** – The behavior of an app when an audio or video clip finishes playing.  Applies to **[Audio](controls/control-audio-video.md)** and **[Video](controls/control-audio-video.md)** controls.

**[OnFailure](controls/control-form-detail.md)** – The behavior of an app when a data operation has been unsuccessful.  Applies to the **[Edit form](controls/control-form-detail.md)** control.

**[OnHidden](controls/control-screen.md)** – The behavior of an app when the user navigates away from a screen.  Applies to the **[Screen](controls/control-screen.md)** control.

**[OnPause](controls/control-audio-video.md)** – The behavior of an app when the user pauses the clip that an audio or video control is playing.  Applies to **[Audio](controls/control-audio-video.md)** and **[Video](controls/control-audio-video.md)** controls.

**[OnReset](controls/control-form-detail.md)** – The behavior of an app when an **[Edit form](controls/control-form-detail.md)** control is reset.  Applies to the **[Edit form](controls/control-form-detail.md)** control.

**[OnSelect](controls/properties-core.md)** – The behavior of an app  when the user taps or clicks a control.  Applies to many controls.

**OnStart** – The behavior of an app when the user opens it or starts to record with a microphone control. Applies to **[Audio](controls/control-audio-video.md)**, **[Microphone](controls/control-microphone.md)**, **[Screen](controls/control-screen.md)**, and **[Video](controls/control-audio-video.md)** controls.

**[OnStateChange](controls/control-pdf-viewer.md)** – The behavior of an app when the state of the control changes. Applies to the **[PDF viewer](controls/control-pdf-viewer.md)** control.

**[OnStop](controls/control-microphone.md)** – The behavior of an app when the user stops recording with a microphone control. Applies to the **[Microphone](controls/control-microphone.md)** control.

**[OnStream](controls/control-camera.md)** – The behavior of an app when the **[Stream](controls/control-camera.md)** property is updated.  Applies to the **[Camera](controls/control-camera.md)** control.

**[OnSuccess](controls/control-form-detail.md)** – The behavior of an app when a data operation has been successful.  Applies to the **[Edit form](controls/control-form-detail.md)** control.

**[OnTimerEnd](controls/control-timer.md)** – The behavior of an app when a timer finishes running.  Applies to the **[Timer](controls/control-timer.md)** control.

**[OnTimerStart](controls/control-timer.md)** – The behavior of an app when a timer starts to run.  Applies to the **[Timer](controls/control-timer.md)** control.

**OnUncheck** – The behavior of an app when the value of a checkbox or a toggle changes to **false**.  Applies to **[Check box](controls/control-check-box.md)** and **[Toggle](controls/control-toggle.md)** controls.

**[OnVisible](controls/control-screen.md)** – The behavior of an app the user navigates to a screen.  Applies to the **[Screen](controls/control-screen.md)** control.

**[OriginalHeight](controls/control-image.md)** – Original height of an image, enabled with the **[CalculateOriginalDimensions](controls/control-image.md)** property.  Applies to the **[Image](controls/control-image.md)** control.

**[OriginalWidth](controls/control-image.md)** – Original width of an image, enabled with the **[CalculateOriginalDimensions](controls/control-image.md)** property.  Applies to the **[Image](controls/control-image.md)** control.

**[Overflow](controls/control-text-box.md)** – Whether a scrollbar appears in a label if its **[Wrap](controls/control-text-box.md)** property is set to **true** and the value of the control's **[Text](controls/properties-core.md)** property contains more characters than the control can show at one time.  Applies to the **[Label](controls/control-text-box.md)** control.

### P

**[Padding](controls/properties-size-location.md)** – The distance between the text on an import or export button and the edges of that button.  Applies to **[Add picture](controls/control-add-picture.md)**, **[Export](controls/control-export-import.md)**, and **[Import](controls/control-export-import.md)** controls.

**[PaddingBottom](controls/properties-size-location.md)** – The distance between text in a control and the bottom edge of that control.  Applies to many controls.

**[PaddingLeft](controls/properties-size-location.md)** – The distance between text in a control and the left edge of that control.  Applies to many controls.

**[PaddingRight](controls/properties-size-location.md)** – The distance between text in a control and the right edge of that control.  Applies to many controls.

**[PaddingTop](controls/properties-size-location.md)** – The distance between text in a control and the top edge of that control.  Applies to many controls.

**[Page](controls/control-pdf-viewer.md)** – The number of the page that you want to show.  Applies to the **[PDF viewer](controls/control-pdf-viewer.md)** control.

**[PageCount](controls/control-pdf-viewer.md)** – The number of pages in a document.  Applies to the **[PDF viewer](controls/control-pdf-viewer.md)** control.

**[Paused](controls/control-audio-video.md)** – *True* if a media playback control is currently paused, *false* otherwise.  Applies to **[Audio](controls/control-audio-video.md)** and **[Video](controls/control-audio-video.md)** controls.

**[Photo](controls/control-camera.md)** – The image captured  when the user takes a picture.  Applies to the **[Camera](controls/control-camera.md)** control.

**[Pressed](controls/control-button.md)** – *True* while a control is being pressed, *false* otherwise.  Applies to the **[Button](controls/control-button.md)** control.

**[PressedBorderColor](controls/properties-color-border.md)** – The color of a control's border when the user taps or clicks that control.  Applies to many controls.

**[PressedColor](controls/properties-color-border.md)** – The color of text in a control when the user taps or clicks that control.  Applies to many controls.

**[PressedFill](controls/properties-color-border.md)** – The background color of a control when the user taps or clicks that control.  Applies to many controls.

### R

**[RadioBackgroundFill](controls/control-radio.md)** – The background color of the circles in a radio-button control.  Applies to the **[Radio](controls/control-radio.md)** control.

**[RadioBorderColor](controls/control-radio.md)** – The color of the circle for each option in a radio-button control.  Applies to the **[Radio](controls/control-radio.md)** control.

**[RadioSelectionFill](controls/control-radio.md)** – The color that appears inside the circle of the selected option in a radio-button control.  Applies to the **[Radio](controls/control-radio.md)** control.

**[RadioSize](controls/control-radio.md)** – The diameter of the circles in a radio-button control.  Applies to the **[Radio](controls/control-radio.md)** control.

**[RadiusBottomLeft](controls/properties-size-location.md)** – The degree to which the bottom-left corner of a control is rounded.  Applies to many controls.

**[RadiusBottomRight](controls/properties-size-location.md)** – The degree to which the bottom-right corner of a control is rounded.  Applies to many controls.

**[RadiusTopLeft](controls/properties-size-location.md)** – The degree to which the top-left corner of a control is rounded.  Applies to many controls.

**[RadiusTopRight](controls/properties-size-location.md)** – The degree to which the top-right corner of a control is rounded.  Applies to many controls.

**RailFill** – The background color of the rectangle in a toggle control when its value is **false** or the color of the line to the right of the handle in a slider control.  Applies to **[Slider](controls/control-slider.md)** and **[Toggle](controls/control-toggle.md)** controls.

**RailHoverFill** – When you hover on a toggle control or a slider, the background color of the rectangle in a toggle control when its value is **false** or the color of the line to the right of the handle in a slider control.  Applies to **[Slider](controls/control-slider.md)** and **[Toggle](controls/control-toggle.md)** controls.

**[RatingFill](controls/control-rating.md)** – The color of the stars in a rating control.  Applies to the **[Rating](controls/control-rating.md)** control.

**ReadOnly** – Whether a user can change the value of a slider or rating control.  Applies to **[Rating](controls/control-rating.md)** and **[Slider](controls/control-slider.md)** controls.

**[Repeat](controls/control-timer.md)** – Whether a timer automatically restarts when it finishes running.  Applies to the **[Timer](controls/control-timer.md)** control.

**[Required](controls/control-card.md)** – Whether a card, editing the field of a data source, must contain a value.  Applies to the **[Card](controls/control-card.md)** control.

**[Reset](controls/properties-core.md)** – Whether a control reverts to its default value.  Applies to many controls.  Also see the **[Reset](functions/function-reset.md)** function.

### S

**Selected** – The selected item.  Applies to **[Drop down](controls/control-drop-down.md)** and **[Gallery](controls/control-gallery.md)** controls.

**[SelectedDate](controls/control-date-picker.md)** – The date currently selected in a date control.  Applies to the **[Date Picker](controls/control-date-picker.md)** control.

**[SelectionColor](controls/properties-color-border.md)** – The text color of a selected item or items in a list or the color of the selection tool in a pen control.  Applies to **[Drop down](controls/control-drop-down.md)**, **[List Box](controls/control-list-box.md)**, and **[Pen input](controls/control-pen-input.md)** controls.

**[SelectionFill](controls/properties-color-border.md)** – The background color of a selected item or items in a list or a selected area of a pen control.  Applies to **[Drop down](controls/control-drop-down.md)** and **[List Box](controls/control-list-box.md)** controls.

**[SelectionThickness](controls/control-pen-input.md)** – The thickness of the selection tool for a pen-input control.  Applies to the **[Pen input](controls/control-pen-input.md)** control.

**[SelectMultiple](controls/control-list-box.md)** – Whether a user can select more than one item in a listbox.  Applies to the **[List Box](controls/control-list-box.md)** control.

**[SeriesAxisMax](controls/control-column-line-chart.md)** – The maximum value of the y-axis for a column or line chart.  Applies to the **[Column chart](controls/control-column-line-chart.md)** control.

**[SeriesAxisMin](controls/control-column-line-chart.md)** – A number that determines the minimum value of the y-axis for a column chart.  Applies to the **[Column chart](controls/control-column-line-chart.md)** control.

**ShowControls** – Whether an audio or video player shows, for example, a play button and a volume slider, and a pen control shows, for example, icons for drawing, erasing, and clearing.  Applies to **[Audio](controls/control-audio-video.md)**, **[PDF viewer](controls/control-pdf-viewer.md)**, **[Pen input](controls/control-pen-input.md)**, and **[Video](controls/control-audio-video.md)** controls.

**[ShowLabels](controls/control-pie-chart.md)** – Whether a pie chart shows the value that's associated with each of its wedges.  Applies to the **[Pie chart](controls/control-pie-chart.md)** control.

**[ShowNavigation](controls/control-gallery.md)** – Whether an arrow appears at each end of a gallery so that a user can scroll through the items in the gallery by clicking or tapping an arrow.  Applies to the **[Gallery](controls/control-gallery.md)** control.

**[ShowScrollbar](controls/control-gallery.md)** – Whether a scrollbar appears when the user hovers over a gallery.  Applies to the **[Gallery](controls/control-gallery.md)** control.

**ShowValue** – Whether a slider's or rating's value appears as the user changes that value or hovers over the control.  Applies to **[Rating](controls/control-rating.md)** and **[Slider](controls/control-slider.md)** controls.

**[Size](controls/properties-text.md)** – The font size of the text that appears on a control.  Applies to many controls.

**[Snap](controls/control-gallery.md)** – Whether, when a user scrolls through a gallery, it automatically snaps so that the next item appears in full.  Applies to the **[Gallery](controls/control-gallery.md)** control.

**Start** – Whether an audio or video clip plays.  Applies to **[Audio](controls/control-audio-video.md)**, **[Timer](controls/control-timer.md)**, and **[Video](controls/control-audio-video.md)** controls.

**[StartTime](controls/control-audio-video.md)** – The time after the start of an audio or video clip when the clip starts to play.  Applies to **[Audio](controls/control-audio-video.md)** and **[Video](controls/control-audio-video.md)** controls.

**[StartYear](controls/control-date-picker.md)** – The earliest year to which the user can set the value of a date-picker control.  Applies to the **[Date Picker](controls/control-date-picker.md)** control.

**[Stream](controls/control-camera.md)** – Automatically updated image based on the **[StreamRate](controls/control-camera.md)** property.  Applies to the **[Camera](controls/control-camera.md)** control.

**[StreamRate](controls/control-camera.md)** – How often to update the image on the **[Stream](controls/control-camera.md)** property, in milliseconds.  This value can range from 100 (1/10th of a second) to 3,600,000 (1 hour).  Applies to the **[Camera](controls/control-camera.md)** control.

**[Strikethrough](controls/properties-text.md)** – Whether a line appears through the text that appears on a control.  Applies to many controls.

### T

**[TemplateFill](controls/control-gallery.md)** – The background color of a gallery.  Applies to the **[Gallery](controls/control-gallery.md)** control.

**[TemplatePadding](controls/control-gallery.md)** – The distance between items in a gallery.  Applies to the **[Gallery](controls/control-gallery.md)** control.

**[TemplateSize](controls/control-gallery.md)** – The height of the template for a gallery in vertical/portrait orientation or the width of the template for a gallery in horizontal/landscape orientation.  Applies to the **[Gallery](controls/control-gallery.md)** control.

**[Text](controls/properties-core.md)** – Text that appears on a control or that the user types into a control.  Applies to many controls.

**[Time](controls/control-audio-video.md)** – A media control's current position.  Applies to **[Audio](controls/control-audio-video.md)** and **[Video](controls/control-audio-video.md)** controls.

**[Tooltip](controls/properties-core.md)** – Explanatory text that appears when the user hovers over a control.  Applies to many controls.

**[Transition](controls/control-gallery.md)** – The visual effect (**Pop**, **Push**, or **None**) when the user hovers over an item in a gallery.  Applies to the **[Gallery](controls/control-gallery.md)** control.

**[Transparency](controls/control-image.md)** – The degree to which controls behind an image remain visible.  Applies to the **[Image](controls/control-image.md)** control. Decimal values range from 0 to 1.  Where 0 is opaque, 0.5 is semi-transparent and 1 is transparent.

### U

**[Underline](controls/properties-text.md)** – Whether a line appears under the text that appears on a control.  Applies to many controls.

**[Unsaved](controls/control-form-detail.md)** – True if the **[Edit form](controls/control-form-detail.md)** control contains user changes that have not been saved.  Applies to the **[Edit form](controls/control-form-detail.md)** control.

**[Update](controls/control-card.md)** – The value to write back to the data source for a field.  Applies to the **[Card](controls/control-card.md)** control.

**[Updates](controls/control-form-detail.md)** – The values to write back to the data source for a record loaded in a form control.  Applies to the **[Edit form](controls/control-form-detail.md)** control.

### V

**Valid** – Whether a **[Card](controls/control-card.md)** or **[Edit form](controls/control-form-detail.md)** control contains valid entries, ready to be submitted to the data source.  Applies to **[Card](controls/control-card.md)** and **[Edit form](controls/control-form-detail.md)** controls.

**[Value](controls/properties-core.md)** – The value of an input control.  Applies to **[Check box](controls/control-check-box.md)**, **[Radio](controls/control-radio.md)**, **[Slider](controls/control-slider.md)**, and **[Toggle](controls/control-toggle.md)** controls.

**ValueFill** – The background color of the rectangle in a toggle control when its value is **true** or the color of the line to the left of the handle in a slider control.  Applies to **[Slider](controls/control-slider.md)** and **[Toggle](controls/control-toggle.md)** controls.

**ValueHoverFill** – When you keep the mouse pointer on a toggle control or a slider, the background color of the rectangle in a toggle control when its value is **true** or the color of the line to the left of the handle in a slider control.  Applies to **[Slider](controls/control-slider.md)** and **[Toggle](controls/control-toggle.md)** controls.

**[VerticalAlign](controls/properties-text.md)** – The location of text on a control in relation to the vertical center of that control.  Applies to many controls.

**[Visible](controls/properties-core.md)** – Whether a control appears or is hidden.  Applies to many controls.

### W

**[Width](controls/properties-size-location.md)** – The distance between a control's left and right edges.  Applies to many controls.

**[WidthFit](controls/properties-size-location.md)** – Whether a control automatically grows horizontally to fill any empty space of a container control such as an **[Edit form](controls/control-form-detail.md)** control. If multiple cards have this property set to **true**, the space is divided between them. For more information, see [Understand data form layout](working-with-form-layout.md).

**[Wrap](controls/control-text-box.md)** – Whether text that's too long to fit in a label wraps to the next line.  Applies to the **[Label](controls/control-text-box.md)** control.

**[WrapCount](controls/control-gallery.md)** – How many records appear in each item of a gallery.  Applies to the **[Gallery](controls/control-gallery.md)** control.

### X

**[X](controls/properties-size-location.md)** – The distance between the left edge of a control and the left edge of its parent container (screen if no parent container). Applies to many controls. For a **[Card](controls/control-card.md)** control in a container that has multiple columns, this property determines the column in which the card appears.

**[XLabelAngle](controls/control-column-line-chart.md)** – The angle of the labels below the x-axis of a column or line chart.  Applies to **[Column chart](controls/control-column-line-chart.md)** and **[Line chart](controls/control-column-line-chart.md)** controls.

### Y

**[Y](controls/properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (screen if no parent container). Applies to many controls. For a **[Card](controls/control-card.md)** control in a container that has multiple rows, this property determines the row in which the card appears.

**[YAxisMax](controls/control-column-line-chart.md)** – The maximum value of the y-axis for a line chart.  Applies to the **[Line chart](controls/control-column-line-chart.md)** control.

**[YAxisMin](controls/control-column-line-chart.md)** – The minimum value of the y-axis for a line chart.  Applies to the **[Line chart](controls/control-column-line-chart.md)** control.

**[YLabelAngle](controls/control-column-line-chart.md)** – The angle of the labels next to the y-axis of a line or column chart.  Applies to **[Column chart](controls/control-column-line-chart.md)** and **[Line chart](controls/control-column-line-chart.md)** controls.

### Z

**Zoom** – The percentage by which an image from a camera is magnified or the view of a file in a PDF viewer.  Applies to **[Camera](controls/control-camera.md)** and **[PDF viewer](controls/control-pdf-viewer.md)** controls.

### See also

[Limitations of controls in Power Apps](control-limitations.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
