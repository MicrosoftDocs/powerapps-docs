<properties
	pageTitle="Upload images, take a picture, play an audio and video file in KratosApps | Microsoft Azure"
	description=""
	services=""
	documentationCenter=""
	authors="MandiOhlinger"
	manager="dwrede"
	editor=""/>

<tags
   ms.service="na"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na" 
   ms.date="10/05/2015"
   ms.author="mandia"/>

# Using the image, picture, audio, and video multimedia options

**UPDATE YOUTUBE STEPS**

In KratosApps, there are several multimedia options available. You can use these options to do various things, including: 

- Upload images to your app
- Take pictures using the camera on your mobile device
- Import audio and play it on within your app
- Add a video and play it on within your app
- Use the microphone on your mobile device to make a recording
- Use a pen on a tablet to create a sketch or a drawing

This topic shows you how to do add these multimedia options to your KratosApps app. 

### Prerequisites

- Install KratosApps. Create a new app or open an existing app in KratosApps.
- To familiarize yourself with KratosApps and creating apps, step through the [Test Drive](get-started-test-drive.md ). It walks you through performing some key tasks.

## Upload an image
1. On the **Insert** tab, select **Image**:  
![][2]  
2. On the **Data** tab, select **Image**, and then select **Add an image file**.
3. Browse and select the file that you want to use, and then select **Open**. The image you selected appears in the control you added:  
![][3]  


## Take a picture using the camera control
Take multiple pictures with the camera on your computer or mobile device. Then, show the pictures in an image gallery. These steps use the camera on your computer. To test the camera control, start the camera on your computer or mobile device. 

1. On the **Insert** tab, select **Media**, and then select **Camera**:  
![][4]  
2. Select **Allow** if prompted for permissions. Rename the control to **MyCamera**:  
![][5]  
If your camera is enabled, it shows a live image of wherever it's pointed, which may be you. Smile.

3. Set the **OnSelect** property of **MyCamera** to the following function:  
```Collect(MyImages, {SinglePicture:MyCamera!Photo})```

	![][6]  
	When you click the camera, a picture is taken, and saved to a collection named **MyImages**; which we'll show you shortly. 

4. On the **Insert** tab, select **Gallery**, and then select the vertical **Image Only** gallery:
![][7]  
5. In the image gallery, select the middle image. This puts a grey border around the entire control. Use your mouse to shrink the width of the gallery so it shows three items:  
![][8]  
	Set its **Items** property to MyImages:  
	![][9]  
6. Preview (![][1]) your app. To take pictures, select **MyCamera** multiple times. Press the **Esc** key to go back to the app designer. Each picture that you take is shown in the gallery.
7. Select the first image in the gallery. Set its **OnSelect** property to the following function:  
```Remove(MyImages, ThisItem)```

8. Preview (![][1]) your app. Select any image in the gallery to remove it. Press the **Esc** key to go back to the app designer.

> [AZURE.NOTE] 
> - When you create a collection, you can see what's in your collection by going to the **File** tab, and then select **Collections**. 
> - When you select the first item in the gallery, any changes you make apply to everything in the gallery. In this example, we selected the first image in the gallery and updated it's **OnSelect** property. This means that the changes you make apply to all images in the gallery.
> - If you close the app, you'll lose the images that you've collected. If you want to keep them, go to the **File** tab, select **Save**.


## Add audio and play it in your app
Configure an audio control to play a file in any format that Internet Explorer supports, including the audio portion of a video file. For example, you can use a .wma file. If you don't have an audio recording, you create your own using the **Sound Recorder** or **Voice Recorder** in Windows. Search for **Sound Recorder** or **Voice Recorder** to open it.

1. On the **Insert** tab, select **Media**, and then select **Audio**:  
![][10]  
2. Press **Alt-D**, select **Media** in the left navigation bar, and then select **Import Media**.
3. Browse for the audio file that you want to play, select **Open**. Press the **Esc** key to go back to the app designer.
4. Set the **Media** property of the audio control to the name of the file that you added. Then select the play button near the left side of the audio control:  
![][11]  

	The file plays. You can also use the audio control to play sounds that you record using the **Microphone** control (also on the **Insert** tab > **Media**).

## Add video and play it in your app
Configure a video control to play a file in any format that Internet Explorer supports. For example, you can use a .wmv file. If you don't have a video, you can create your own using the  video recording feature of your webcam.

1. On the **Insert** tab, select **Media**, and then select **Video**:  
![][12]  
2. Press **Alt-D**, select **Media** in the left navigation bar, and then select **Import Media**.
3. Browse for the file that you want to play, select **Open**. Press the **Esc** key to go back to the app designer.
4. Set the **Media** property to the name of the file that you added. Then select the play button near the center of the control to watch your video:  
![][13]  


#### Play a YouTube video
You can also play videos from external sources, including YouTube. 

1. On the **Insert** tab, select **Connected Visuals**, and then select **YouTube Watch**:  
![][14]  
2. Select the video control by clicking in its center, and then set its **Media** property to the URL of the video you want to show. For example, set it to the following video on the Microsoft YouTube channel:  
[https://www.youtube.com/watch?v=tGGCHmb9bro](https://www.youtube.com/watch?v=tGGCHmb9bro)  
![][15]  

	**Note** Use the double quotation marks around the URL.

3. Preview (![][1]) your app. Select the play button the middle of the video player. To return to the app designer, press the **Esc** key.


## Use the microphone and pen controls

#### Use the microphone to make recordings and play them in your app
Using the microphone to create recordings, and show these recordings in a gallery. 

1. On the **Insert** tab, select **Text**, select **Input Text**, and rename the new control **Description**.
2. On the **Insert** tab, select **Media**, and select **Microphone**. If prompted for permissions, select **Allow**.
3. Rename the control to **MyMicrophone**, and set its **OnStop** property to the following function:  
```Collect(Interviews, {Recordings:MyMicrophone!Audio, Notes:Description!Text})```  
	![][16]  
	By using this function, you create a collection named **Interviews**, which contains a column named **Recordings** and a column named **Notes**. Each row contains a sound file that you create by using the microphone and any text that the Input Text control contains when you stop recording.

4. On the **Insert** tab, select **Gallery**, select the vertical **Custom Gallery**, and then set its **Items** property to **Interviews**.
5. Select the first item in the gallery, select the **Insert** tab, select **Media**, and then select **Audio**.
6. Set the **Media** property for the audio control to ```ThisItem!Recordings```.  
	**Note** You can save visual space by shrinking the audio control so that only the play button appears.
7. Add a label to the first item in that gallery, and set the label's **Text** property to  ```ThisItem!Notes```. Your gallery control looks similar to the following:  
![][17]
8. Preview (![][1]) your app. Type a phrase in the Description box, and then select **MyMicrophone** to start recording. When done recording, select **MyMicrophone** again to stop recording.

	Your description appears in the first item of the gallery, and your recording plays if you click the play button in the audio control.

	Type something else in the **Description** box, and make another recording. Repeat as many times as you want. Each description and recording appears in the gallery.

Press the **Esc** key to return to the app designer.

#### Use the pen to write or draw directly within the app
Create multiple drawings (or simulate a whiteboard), and show the results in a gallery.

1. On the **Insert** tab, select **Text**, select **Pen**, and then rename the new control to **Sketches**. 
2. On the **Pen** tab, select **Show Controls**:  
![][18]  
	Confirm that ```ShowControls``` is equal to ```true``` in the Function Bar. 
3. Add a button, set its **Text** property to ```Add``` and set its **OnSelect** property to the following function:  
```Collect(Creativity, {Captures:Sketches!Image})```
4. On the **Insert** tab, select **Gallery**, and select the vertical **Image Only** gallery. Shrink the width of the gallery to show three items. 
5. Set the gallery's **Items** property to ```Creativity```. 
6. Preview (![][1]) to see what you created. 

	Draw or write something in **Sketches**, and then select the **Add** button. The contents of the pen control appear in the first item of the gallery.

	Select the clear button (with the "x") in Sketches, write or draw something else in it, and then select the **Add** button again. The contents of the pen control appear in the second item in the gallery.

Repeat these steps as many times as you like. Press the **Esc** key to return to the designer. 

You can also convert written text to typed text:

1. Add a label, and set its **Text** property to ```Sketches!RecognizedText```.
2. Preview (![][1]) your app. Write a word in the pen control. The label shows the word as typed text.

## Tips and Tricks
- At anytime, you can select the preview button (![][1]) to see what you created and test it.
- When designing your app, you can re-size the controls and move them around using click-and-drag.
- Press **ESC** to close the preview window.
- **Save** your work using the **File** menu, or press **Ctrl** + **S**,

## What you learned

In this topic, you:

- Added single images and used the Camera control to take pictures. You used Excel-like functions to create a collection to display the pictures you took. 
- Used the Audio and Video control to add sound and videos to your app, including playing a YouTube video. 
- Additional multimedia options, including the Microphone and Pen controls, are available to make recordings, and write text directly in the app. 


[1]: ./media/add-images-pictures-audio-video/preview.png
[2]: ./media/add-images-pictures-audio-video/insertimage.png
[3]: ./media/add-images-pictures-audio-video/imagecontrol.png
[4]: ./media/add-images-pictures-audio-video/camera.png
[5]: ./media/add-images-pictures-audio-video/renamecamera.png
[6]: ./media/add-images-pictures-audio-video/onselectfunction.png
[7]: ./media/add-images-pictures-audio-video/verticalimage.png
[8]: ./media/add-images-pictures-audio-video/threeitems.png
[9]: ./media/add-images-pictures-audio-video/itemsmyimages.png
[10]: ./media/add-images-pictures-audio-video/audio.png
[11]: ./media/add-images-pictures-audio-video/audiorecording.png
[12]: ./media/add-images-pictures-audio-video/video.png
[13]: ./media/add-images-pictures-audio-video/videorecording.png
[14]: ./media/add-images-pictures-audio-video/youtube.png
[15]: ./media/add-images-pictures-audio-video/youtubevideo.png
[16]: ./media/add-images-pictures-audio-video/microphoneonstop.png
[17]: ./media/add-images-pictures-audio-video/gallery.png
[18]: ./media/add-images-pictures-audio-video/pentab.png

[19]: ./media/add-images-pictures-audio-video/
[20]: ./media/add-images-pictures-audio-video/
[21]: ./media/add-images-pictures-audio-video/