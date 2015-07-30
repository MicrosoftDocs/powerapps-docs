<properties
	pageTitle="Configure a control in KratosApps Studio"
	description="Configure the properties of lists, sliders, toggles, cameras, microphones, and other controls so that users can review, add, and update data."
	services="kratosapps"
	authors="AFTOwen"
 />

# Configure a control in KratosApps Studio #

Configure a control to show data, gather data from users, or respond to user input. For each control, specify data, behavior, and design properties, which determine how a control looks, what happens when a user interacts with it or another control, and other characteristics.

**Prerequisites**

- [Create an app](kratosapps-tutorial-inventory.md) to learn how to perform basic tasks, such as adding a control.

## Controls ##

### Audio ###
Configure an audio control to play a file in any format that Internet Explorer supports, including the audio portion of a video file.

1. On the **Insert** tab, click **Media**, and then click **Audio**.
1. Press Alt-D, click **Media** in the left navigation bar, and then click **Import Media**.
1. Browse for the file that you want to play, click **Open**, and then press Esc.
1. Set the **Media** property of the audio control to the name of the file that you added, and then click the play button near the left side of the audio control.

	The file that you specified plays.

You can also use the audio control to play sounds that you record with a [microphone control](#microphone).

### Button ###

[Create an app](kratosapps-tutorial-inventory.md) to learn how to configure a button.

### Camera ###

Take multiple pictures with the camera on your device, and show them in an image gallery.

1. On the **Insert** tab, click **Media**, and then click **Camera**.
1. Click **Allow** if you're prompted for permissions, and then name the control **MyCamera**.

	The camera shows a live image of whatever it's pointed toward.

1. Set the **OnSelect** property of **MyCamera** to this function:

	**Collect(MyImages, {SinglePicture:MyCamera!Photo})**

	Later in this procedure, you'll click the camera, which will take a picture and save it to a collection named **MyImages**.

1. On the **Insert** tab, click **Gallery**, and then click the vertical **Image Only** gallery.
1. Shrink the width of the gallery to show three items, and then set its **Items** property to **MyImages**.
1. Press F5, click **MyCamera** multiple times, and then press Esc.

	Each picture that you take appears in the gallery.

1. Click the first image in the gallery, and then set its **OnSelect** property to this function:

	**Remove(MyImages, ThisItem)**

1. Press F5, click any image in the gallery to remove it, and then press Esc.

**Note:** If you close the app, you'll lose the images that you've collected unless you [save and load](kratosapps-tutorial-inventory.md) them.

### Chart ###
[Show a set of data](kratosapps-show-data.md) for examples of how to add and configure a chart.
 
### Checkbox ###

Specify the value of another property based on whether a checkbox is selected or cleared. In this example, you'll change the text that appears in a label. 

1. On the **Insert** tab, click **Controls**, and then click **Checkbox**.

1. Name the checkbox **MyCheckbox**, and set its **Text** property to **I'm ready.**

1. Add a label, and set its **Text** property to this function:

	**If(MyCheckbox!Value = true, "Let's go!", "I'll wait.")**

1. Press F5, select and clear the checkbox multiple times, and then press Esc.

	In Preview, the text of the label toggles between the two messages.

### Connected visuals ###

[Add data](kratosapps-add-data.md) for examples of how to connect to Office 365 Preview, Facebook, Twitter, Instagram, YouTube, and Coursera, in addition to using Bing to search the web and translate text.

### Drop-down list ###

Configure a drop-down list the same way as you configure a [radio-button control](#radio-buttons).

### Export ###

[Share data](kratosapps-share-data.md) for information about how to transfer data between apps created in KratosApps Studio.

### Gallery ###

[Create an app](kratosapps-tutorial-inventory.md) for an example of how to configure a gallery.

### HTML label ###
Show text and render HTML codes (including links, images, and CSS styles) in an RSS feed or other sources in this control. HTML labels don't execute JavaScript and aren't web-controls or iframes. Configure an HTML label the same way as you configure a label, as [Create an app](kratosapps-tutorial-inventory.md) describes.

### Image ###
1. On the **Insert** tab, click **Image**.

1. On the **Data** tab, click **Image**, and then click **Add an image file**.

1. Browse to and then click the file that you want to use, and then click **Open**.

	The image that you specified appears in the control that you added.

### Import ###

[Share data](kratosapps-share-data.md) for information about how to transfer data between apps created in KratosApps Studio.

### Input text ###

[Add data from the user](kratosapps-add-user-data.md) for an example of how to configure an input-text control.

### Label ###

[Create an app](kratosapps-tutorial-inventory.md) for an example of how to configure a label.

### Listbox ###
Choose multiple items in a listbox to determine properties of one or more other controls. For example, show or hide shapes, images, or other elements based on which items are chosen.

1. On the **Insert** tab, click **Controls**, and then click **ListBox**.

1. Name the listbox **MyListBox**, and then set its **Items** property to this function:

	**Table({Shape:"circle"}, {Shape:"triangle"}, {Shape:"rectangle"})**

1. On the **Insert** tab, click **Shapes**, click the circle, and move it under the listbox.

1. Add a triangle and a rectangle, and then arrange the shapes in a row under the listbox.

1. Set the **Visible** property of the circle to this function:

	**If("circle" in MyListbox!SelectedItems!Value, true)**

1. Set the **Visible** property of the triangle to this function:

	**If("triangle" in MyListbox!SelectedItems!Value, true)**

1. Set the **Visible** property of the rectangle to this function:

	**If("rectangle" in MyListbox!SelectedItems!Value, true)**

1. Press F5, click one or more options in the listbox, and then press Esc.

	In Preview, only the shape or shapes that you selected in the list appear.

### Microphone ###
Make a series of recordings and present them in a gallery.

1. On the **Insert** tab, click **Text**, click **Input Text**, and then name the new control **Description**.

On the **Insert** tab, click **Media**, click **Microphone**, and then click **Allow** if you're prompted for permissions.

1. Rename the control **MyMicrophone**, and set its **OnStop** property to this function:

	**Collect(Interviews, {Recordings:MyMicrophone!Audio, Notes:Description!Text})**

	By using this function, you create a collection named **Interviews**, which contains a column named **Recordings** and a column named **Notes**. Each row will contain a sound file that you create by using the microphone and any text that the input-text control contains when you stop recording.

1. On the **Insert** tab, click **Gallery**, click the vertical **Custom Gallery**, and then set its **Items** property to **Interviews**.

1. Click the first item in the gallery, click the **Insert** tab, click **Media**, and then click **Audio**.

1. Set the **Media** property for the audio control to **ThisItem!Recordings**.

	**Note:** You can save visual space by shrinking the audio control so that only the play button appears.

1. Add a label to the first item in that gallery, and set the **Text** property for the label to **ThisItem!Notes**.

1. Press F5, type a phrase in the **Description** box, and then click **MyMicrophone** to start to record.

1. When you finish recording, click **MyMicrophone** again to stop recording.

	Your description appears in the first item of the gallery, and your recording plays if you click the play button in the audio control.

1. Type something else in the **Description** box, make another recording, and repeat as many times as you want.

	Each description and recording appears in the gallery.

1. Press Esc to return to the design workspace.

**Note:** If you close the app, you'll lose the recordings and descriptions that you've collected unless you [save and load them](kratosapps-tutorial-inventory.md).

### Office 365 Preview (Send Message) ###
[Share data](kratosapps-share-data.md) for an example of how to configure this control.
 
### Pen ###
Create multiple drawings (or simulate a whiteboard), and show the results in a gallery.

1. On the **Insert** tab, click **Text**, click **Pen**, and then name the new control **Sketches**.

1. On the **Pen** tab, click **Show Controls**, and ensure that true appears in the Function Bar.

1. Add a button, set its **Text** property to **Add** and set its **OnSelect** property to this function:

	**Collect(Creativity, {Captures:Sketches!Image})**

1. On the **Insert** tab, click **Gallery**, click the vertical **Image Only** gallery, and then set the gallery's **Items** property to **Creativity**.

1. Shrink the width of the gallery to show three items, and then press F5.

1. Draw or write something in **Sketches**, and then click the button that you added.

	The contents of the pen control appear in the first item of the gallery.

1. Click the clear button (with the "x") in **Sketches**, write or draw something else in it, and then click the **Add** button again.

	The contents of the pen control appear in the second item of the gallery.

1. Repeat the previous step as many times as you want, and then press Esc to return to the design workspace.

	**Note:** If you close the app, you'll lose the recordings and descriptions that you've collected unless you [save and load them](kratosapps-tutorial-inventory.md).

1. (optional) Convert written text to typed text:

	1. Add a label, and set its **Text** property to **Sketches!RecognizedText**.

	1. Press F5, and then write a word in the pen control.

		The label shows the word as typed text.

### Radio buttons ###
Specify the choices that appear in a radio-button control, and change the value of a property for another control, such as the fill color for a circle, based on which radio button is chosen.

1. On the **Insert** tab, click **Controls**, click **Radio**, and then name the new control **Choices**.

1. Set its **Items** property of the control to this function, and then resize the control to show all options.

	**Table({Color:"red"}, {Color:"green"}, {Color:"blue"})**

1. On the **Insert** tab, click **Shapes**, and then click the circle.

1. Set the **Fill** property of the circle to this function:

	**If(Choices!Selected!Value = "red", RGBA(192, 0, 0, 1), Choices!Selected!Value = "green", RGBA(0, 176, 80, 1), Choices!Selected!Value = "blue", RGBA(0, 32, 96, 1))**

	In this function, you specify different color values based on which radio button is chosen.

1. Press F5, choose different radio buttons to change the color of the shape, and then press Esc to return to the design workspace.

### Rating ###
Configure the property of a control, such as label text, to change based on the rating that a user specifies.

1. On the **Insert** tab, click **Controls**, click **Rating**, and then name it **MyRating**.

1. Add a label, and then set its **Text** property to this function:

	**If(MyRating!Value > 3, "Thanks!", "Sorry!")**

	If a user specifies four or five stars, the label shows **Thanks!** Otherwise, the label shows **Sorry!**

1. Press F5, test the function by setting **MyRating** to different values, and then press Esc.

### Shapes ###
[Create an app](kratosapps-tutorial-inventory.md) for an example of how to configure a shape (rectangle).

### SharePoint Update ###
[Share data](kratosapps-share-data.md) for information about how to download data from a SharePoint list and add new data back to the list.

### Slider ###
[Create an app](kratosapps-tutorial-inventory.md) for an example of how to configure a slider.

### Timer ###
You can change the value of a property for a different control, such as the **Text** property of a label, based on how long a timer has been running.

1. Add a button, and name it **MyButton**.

1. On the **Insert** tab, click **Controls**, click **Timer**, and name it **MyTimer**.

1. On the **Timer** tab, click **Reset**, and then type or paste **MyButton!Pressed** in the Function Bar.

1. Add a label, and set its **Text** property to this function:

	**If(Timer1!Value=0, "", Timer1!Value<3000, "Ready!", Timer1!Value>3000 && Timer1!Value<6000, "Set!", Timer1!Value>6000, "Go!")**

1. Press F5, and then click the timer.

	Nothing appears in the label before the timer starts. The label shows "Ready!" for the first three seconds, "Set!" for the next three seconds, and "Go!" after at least six seconds have passed.

1. (optional) After all three messages have appeared, click **MyButton** to set the timer back to the start, and click the timer again to restart it.

1. Press Esc to return to the design workspace.

### Toggle ###
You can configure a toggle the same way as you configure a [checkbox](#checkbox).

### Video ###
1. On the **Insert** tab, click **Media**, and then click **Video**.

1. Press Alt-D, click **Media** in the left navigation bar, and then click **Import Media**.

1. Browse for the file that you want to play, click **Open**, and then press Esc.

1. Set the **Media** property of the control to the name of the file that you added, and then click the play button near the center of the control.

	The file that you specified plays.

[Add data](kratosapps-add-data.md) for an example of how to show a video on YouTube.

## Properties ##

### Data ###

### Behavior ###

### Design ###
