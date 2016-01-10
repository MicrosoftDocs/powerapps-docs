<properties
   pageTitle="Properties in PowerApps"
   description="In PowerApps, you can use the properties that this topic describes."
   services=""
   suite="powerapps"
   documentationCenter="na"
   authors="gregli-msft"
   manager="dwrede"
   editor=""
   tags=""/>
<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="11/05/2015"
   ms.author="gregli"/>

# Properties in PowerApps#

## Data ##

| Property | Description  |
|----------|--------------|
| AutoPause   | Set to true if you want the timer, audio player, or video player to pause automatically when, for example, the user navigates to a different screen. Otherwise, set to false. |
| AutoStart   | Set to true if you want the timer, audio player, or video player to start automatically if, for example, the user opens the screen that contains the control you're configuring. Otherwise, set to false. |
| Brightness  | Specify the level of brightness in the image that appears in the camera. |
| Clear       | Set to true if you want to clear all input from a pen control. Otherwise, set to false. |
| Contrast    | Specify the level of contrast in the image that appears in the camera. |
| Data Source | Specify the list that you want to update when a user clicks a SharePoint Update control. |
| Default     | Specify the default text that appears in an input-text control; the default value for a rating, slider, or toggle control; or the default option in a listbox or radio-button control. For a gallery, specify the item or items to show by default, as this [forum post](https://social.technet.microsoft.com/Forums/en-US/85b7995a-33f6-4113-a32e-fc017bb037ae/default-visibleindex?forum=projectsiena) describes. |
| Duration    | Specify how much time, in milliseconds, will elapse between when the timer starts and when it finishes if it isn't interrupted. |
| HTML Text   | Specify the text that appears in an HTML label, including markup that you want the control to render. |
| Image       | Specify the image that appears in an image control, an audio player, a video player, or a microphone. |
| Items       | Specify the data that you want to show in a gallery, a listbox, or a dropdown list. |
| Loop        | Set to true if you want the audio or video player to restart the clip automatically when the player finishes. Otherwise, set to false. |
| Max         | Specify the maximum value to which a user can set a slider or a rating control. |
| Media       | Specify the audio or video clip that you want a player to play. |
| Min         | Specify the minimum value to which a user can set a slider. |
| ReadOnly    | Set to true if you want a rating control to show a value but ignore user input. |
| Repeat      | Set to true if you want a timer that finishes to automatically start again from zero. |
| Reset       | Set to true if you want a timer to stop counting and return to zero. |
| Start       | Set to true if you want a timer to start and false if you want it to stop. |
| StartTime   | Specify how long, in seconds, from the start of a clip you want an audio or video player to start playing. |
| Text        | Specify the text that appears in a label, next to a checkbox, or on a button, an export control, an import control, or a SharePoint Update control. |
| Tooltip     | Specify the text that appears when a user hovers over a control. For example, you can display the percentage of an audio clip that has been played:<br>**Concatenate(Text(Round(AudioPlayback1.Time/AudioPlayback1.Duration*100,1)), "% complete")** |
| Zoom        | Specify the default zoom for a camera. |

## Behavior ##

| Property     | Description |
|--------------|-------------|
| OnChange     | Specifies how your app responds when, for example, a user adjusts a slider, specifies a rating, or chooses an option in a listbox. |
| OnCheck      | Specifies how your app responds when, for example, a user selects a checkbox. |
| OnEnd        | Specifies what else changes in your app when an audio or video clip finishes playing. |
| OnPause      | Specifies what else changes in your app when an audio or video clip is paused. |
| OnSelect     | Specifies how your app responds when, for example, a user clicks a button, a label, an image, or any other control for which you've set this property. |
| OnStart      | Specifies what else changes in your app when an audio or video clip starts to play or a microphone starts to record. |
| OnStop       | Specifies what else changes in your app when a microphone stops recording. |
| OnTimerEnd   | Specifies what else changes when a timer finishes running. |
| OnTimerStart | Specifies what else changes in your app when a timer starts to run. |
| OnUncheck    | Specifies how your app responds when, for example, a user clears a check box. |

## Design ##

| Property | Description |
|----------|-------------|
| Align                 | Specify **Align.Left**, **Align.Center**, **Align.Right**, or **Align.Justified** to change the alignment of text on a button or in a label, an input-text control, or another type of control. |
| Border Color          | Specify RGBA values or click an option to change the color of the border around a control. For example, you can specify **RGBA(192, 0, 0, 1)** to make a border red. |
| Border Style          | Specify **BorderStyle.Solid**, **BorderStyle.Dashed**, or **BorderStyle.Dotted** to change the style of the border around a control, or specify **BorderStyle.None** to remove the border. By default, this property is set to **BorderStyle.None**. |
| Border Thickness      | Specify a number to change the thickness of a border around a control. For example, **10** gives you the thickest border, and **0** removes the border altogether. By default, this property is set to **0**. |
| Camera                | Specify the numeric ID of the camera you want to use. For example, **0** might indicate a camera on the front of a device, and **1** might indicate the camera on the rear of a device. |
| Checkbox Size         | Specify a number that represents how large you want a checkbox to be. For example, **8** is the smallest, and **96** is the largest. |
| Clear                 | Specify **true** to show a small icon [**x**] that a user can click to remove all text from an input-text control, and specify **false** to hide the icon. |
| Color                 | Specify RGBA values or click an option to change the color of the text in a label, a button, or other control or the color of the input in a pen control. For example, you can specify **RGBA(192, 0, 0, 1)** to make the text or input red. |
| Direction             | Specify **Direction.Start** to show the first item at the left edge of a horizontal gallery, or specify **Direction.End** to show the first item at the right edge of a horizontal gallery. |
| Disabled              | Specify **true** to prevent users from interacting with a control. Otherwise, specify **false**. |
| Disabled Border Color | Specify RGBA values or click an option to change the color of the border around a control for which the **Disabled** property is set to true. For example, you can specify **RGBA(255, 255, 255, 1)** to make the border white. |
| Disabled Color        | Specify RGBA values or click an option to change the color of the text in a control for which the **Disabled** property is set to true. For example, you can specify **RGBA(255, 255, 255, 1)** to make the text white. |
| Fill                  | Specify RGBA values or click an option to change the background color of a control. For example, you can specify **RGBA(255, 255, 255, 1)** to change the background of a toggle light green when the handle is on the right side or the bottom of the control. |
| Font                  | Specify the name of the font that you want to use for the text in a label, input-text control, listbox, or other control. |
| FontWeight            | Specify **FontWeight.Normal**, **FontWeight.Lighter**, **FontWeight.Semibold**, or **FontWeight.Bold** to change the style of text on, for example, a button. |
| Handle Fill           | Specify RGBA values or click an option to change the color of the element that you drag to change the value of a toggle. For example, you can specify **RGBA(192, 0, 0, 1)** to make the element red. |
| Height                | Specify the number of pixels between the top of a control and the bottom of the same control. You can also resize a control by clicking it and then dragging a small square or triangle in the thick, gray selection box that appears. |
| Hint Text             | Specify text that appears in an input-text control if the **Default** property of that control is an empty string. Hint text appears in gray and disappears as soon as the user clicks the control. |
| Hover Border Color    | Specify RGBA values or click an option to change the color of the border for a control to which a user is pointing with a mouse, a trackpad, or a similar device. For example, you can specify **RGBA(192, 0, 0, 1)** to make the border red. |
| Hover Color           | Specify RGBA values or click an option to change the color of the text in a control to which a user is pointing with a mouse, a trackpad, or a similar device. For example, you can specify **RGBA(192, 0, 0, 1)** to make the text red. |
| Hover Fill            | Specify RGBA values or click an option to change the background color of a control to which a user is pointing with a mouse, a trackpad, or a similar device. For example, you can specify **RGBA(192, 0, 0, 1)** to make the background red. |
| Image Position        | Specify one of these expressions to change how an image appears, for example, in an image control or as the background of a microphone control that doesn't have the same dimensions as the image you want to show:<br>--**ImagePosition.Fill** changes the image's height and width proportionally so that the image reaches all four sides of the control while maintaining the original aspect ratio.<br>--**ImagePosition.Fit** changes either the height of the image (so it reaches both the top and the bottom of the control) or the width of the image (so it reaches both the left and the right side of the control) while maintaining the original aspect ratio.<br>--**ImagePosition.Center** shows the image with its original dimensions in the center of the control.<br>--**ImagePosition.Tile** shows one or more instances of the image with its original dimensions so that the entire control is covered.<br>--**ImagePosition.Stretch** changes the image's height and width to match the dimensions of the control. |
| Italic                | Specify **true** to italicize the text in a label, input-text, button, or other control. Otherwise, specify **false**. |
| Layout                | For a gallery, specify **Layout.Horizontal** to show the first item on the left side of a gallery and subsequent items in a row to the right. Specify **Layout.Vertical** to show the first item on the top of a gallery and subsequent items in a column toward the bottom. For a slider, specify **Layout.Horizontal** if you want users to adjust the value by dragging the thumb left or right, and specify **Layout.Vertical** if you want users to adjust the value by dragging the thumb up or down. |
| Line Height           | Specify a number that represents the amount of space between, for example, lines in a label, items in a listbox, or lines in an input-text control for which the **Mode** property is set to Multiline. |
| Mic                   | Specify the numeric ID of the microphone you want to use. For example, **0** might indicate a microphone on the front of a device, and **1** might indicate the microphone on the rear of a device. |
| Mode                  | Specify **Mode.SingleLine**, **Mode.Multiline**, or **Mode.Password** to determine what kinds of data an input-text control accepts. |
| Navigation Step       | Specify the number of gallery items that you want to scroll when you click the arrows that appear if **Show Navigation** is set to true. For example, specify **5** if your gallery shows five items at a time, and you want to show a different set every time a user clicks a navigation arrow. |
| Overflow              | Specify **Overflow.Scroll** to show a vertical scrollbar when a label is too small to show all of the text it contains, or specify **Overflow.Hidden** to hide that scrollbar. |
| Padding Bottom        | Specify a different value to change the distance between, for example, the text on a button and the bottom of the button. By default, text is centered vertically in a button. If you want that text to appear along the bottom of the button, set this property to **0**, and change the **Vertical Alignment** property to **Bottom**. |
| Padding Left          | Specify a different value to change the distance between, for example, the text on a button and the left edge of the button. By default, text is centered in a button. If you want that text to appear on the left edge of the button, set this property to **0**, and change the **Align** property to **Left**. |
| Padding Right         | Specify a different value to change the distance between, for example, the text on a button and the right edge of the button. By default, text is centered in a button. If you want that text to appear on the right edge of the button, set this property to **0**, and change the **Align** property to **Right**. |
| Padding Top           | Specify a different value to change the distance between, for example, the text on a button and the top of the button. By default, text is centered vertically in a button. If you want that text to appear along the top of the button, set this property to **0**, and change the **Vertical Alignment** property to **Top**. |
| PenMode               | Specify **PenMode.Draw**, **PenMode.Erase**, or **PenMode.Select** to determine what happens when a user drags a pointing device, such as a mouse, in a pen control. |
| Pressed Border Color  | Specify RGBA values or click an option to change the border color of a control when a user clicks that control. For example, you can specify **RGBA(192, 0, 0, 1)** to set this property to red. |
| Pressed Color         | Specify RGBA values or click an option to change the text color of a control when a user clicks that control. For example, you can specify **RGBA(192, 0, 0, 1)** to set this property to red. |
| Pressed Fill          | Specify RGBA values or click an option to change the background color of a control when a user clicks that control. For example, you can specify **RGBA(192, 0, 0, 1)** to set this property to red. |
| Rail Fill             | Specify RGBA values or click an option to change the color of the slider element on the right side of the thumb. (You drag the thumb to change the slider value.) For example, you can specify **RGBA(192, 0, 0, 1)** to set this property to red. |
| Radio Size            | Specify a different value to change the size of the circles that you click to choose an item in a radio-button control. |
| Rating Fill           | Specify RGBA values or click an option to change the color of the stars that indicate the value of a rating control. For example, you can specify **RGBA(192, 0, 0, 1)** to change the first four stars (counting from the left) red when the value of the control is four. |
| SelectionColor        | For a listbox or dropdown control, specify RGBA values or click an option to change the text color of an item the user chooses. For a pen control, specify RGBA values or click an option to change the color of the selection line when the **PenMode** property is set to **PenMode.Select**. For example, you can specify **RGBA(192, 0, 0, 1)** to set this property to red. |
| SelectionFill         | Specify RGBA values or click an option to change the fill color of an item chosen in a listbox or a dropdown control. For example, you can specify **RGBA(192, 0, 0, 1)** to set this property to red. |
| SelectionThickness    | Specify a value to change the thickness of the selection line when the **PenMode** property of a pen control is set to **PenMode.Select**. |
| SelectMultiple        | Specify **true** to allow users to choose more than one option at a time in a listbox, or specify **false** to allow only one option. |
| ShowControls          | Specify **true** to display, for example, play, pause, and rewind controls for a video or audio player or draw, erase, and clear controls for a pen. Specify **false** to hide those controls. |
| ShowNavigation        | Specify **true** to display arrows near the left and right edges of a horizontal gallery or the top and bottom edges of a vertical gallery. You can click these arrows to scroll through items in the gallery. Specify **false** to hide these arrows. |
| ShowValue             | Specify **true** to display the value of a slider or a rating control as a user changes that value, and specify **false** to hide the value. |
| Size                  | Specify a different value to change the size of the text on, for example, a button. |
| Snap                  | Specify **true** to turn on snapping when a user scrolls through a gallery. For example, when a user clicks the arrow on the right side of a horizontal gallery, the item furthest to the left disappears completely, and the item immediately to its right appears on the left edge of that gallery. Specify **false** to turn this behavior off. |
| Strikethrough         | Specify **true** to add a line through the horizontal center of text on, for example, a button, or specify **false** to remove such a line. |
| Template Fill         | Specify RGBA values or click an option to change the color behind all controls in each item of a gallery. For example, you can specify **RGBA(192, 0, 0, 1)** to set this property to red. |
| Template Padding      | Specify a different value to change the amount of space between items in a gallery. |
| Template Size         | Specify a different value to change the amount of horizontal space (in a horizontal gallery) or the amount of vertical space (in a vertical gallery) that each item can occupy. |
| Thumb Fill            | Specify RGBA values or click an option to change the fill color of the square that you drag to change the value of a slider. For example, you can specify **RGBA(192, 0, 0, 1)** to set this property to red. |
| ThumbSize             | Specify a different value to change the size of the square that you drag to change the value of a slider. |
| ToggleFill            | Specify RGBA values or click an option to change the fill color of the toggle when the handle is on the left side or top of the control. For example, you can specify **RGBA(192, 0, 0, 1)** to set this property to red. |
| Transition            | Specify **Transition.Push**, **Transition.Pop**, or **Transition.None** to change or remove the visual effect when you point to an item in a gallery. |
| Transparency          | Specify **0** to show an image in an image control, or specify any other value to hide the image. |
| Underline             | Specify **true** to add a line under the text on, for example, a button, or specify **false** to remove such a line. |
| Value Fill            | Specify RGBA values or click an option to change the color of the slider element on the left side of the thumb. (You drag the thumb to change the slider value.) For example, you can specify **RGBA(192, 0, 0, 1)** to set this property to red. |
| Vertical Align        | Specify **VerticalAlign.Top**, **VerticalAlign.Middle**, or **VerticalAlign.Bottom** to change the placement of text, for example, on a button. |
| Visible               | Specify **true** to show the control on a screen in your app, and specify **false** to hide the control. |
| Width                 | Specify a different number to change the distance, in pixels, between the left and right edges of a control. |
| X                     | Specify a different number to change the distance between the left edge of a screen and the left edge of a control on that screen. |
| Y                     | Specify a different number to change the distance between the top edge of a screen and the top edge of a control on that screen. |
