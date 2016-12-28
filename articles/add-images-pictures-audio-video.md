<properties
	pageTitle="Embed multimedia files into a PowerApps app and upload | Microsoft PowerApps"
	description="Show multimedia files in an app, and upload them to a data source"
	services=""
	suite="powerapps"
	documentationCenter=""
	authors="RickSaling"
	manager="anneta"
	editor=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="12/28/2016"
   ms.author="ricksal"/>

# Add multimedia files and upload them to a data source

This topic shows you how to embed multimedia files into your app, and
describes several scenarios for uploading multimedia files to a data source. The data source used in this topic is an Excel file in OneDrive.

## Prerequisites

- [Sign up](../articles/signup-for-powerapps.md) for PowerApps, and [install](http://aka.ms/powerappsinstall) it. When you open PowerApps, sign in using the same credentials that you used to sign up.

- Create an app from a [template](../articles/get-started-test-drive.md), from [data](../articles/get-started-create-from-data.md), or from [scratch](../articles/get-started-create-from-blank.md).

- Familiarity with [adding and configuring controls](add-configure-controls.md).

- Familiarity with [configuring Excel data as a table](https://support.office.com/en-us/article/Format-an-Excel-table-6789619F-C889-495C-99C2-2F971C0E2370?ui=en-US&rs=en-US&ad=US).

- A [PowerApps connection](add-data-connection.md) to a cloud-storage account (such as Dropbox, OneDrive, or Google Drive) in which you can store an Excel file.


## Add media from a file ##
You can choose which media option to add. For example, if you have some pictures or a video available, consider adding one of these.

1. On the **Content** tab, select **Media**.
2. Under **Media**, select **Images**, **Videos**, or **Audio**, and then select **Browse**:  
	![][1]  
3. Select the file that you want to add, and then select **Open**.
4. When you finish adding files, go back to the app designer. You can also press Esc.
5. On the **Insert** tab, select **Media**, and then choose image, video, or audio:  
	![][8]

	- If you added an image control, set its **[Image](controls/properties-visual.md)** property to the file that you added:  

		![Set Image property][9]

	- If you added a video or audio control, set its **Media** property to the file that you added:  

		![Set Media property][10]

	**Note** Play a YouTube video by setting the **Media** property of a video control to the appropriate URL, enclosed in double quotation marks.

## Multimedia and data source scenarios

The first upload scenario require you to do the following:
* create a OneDrive data source based on an Excel file;
* generate an app from that file.
* modify that app to upload pen images to the data source;

In the second scenario, you add the images in an OneDrive Excel file to your app.

## Create the OneDrive data source and Excel file

1. In Excel, add **Caption** and **Image [image]** to any two cells that are side by side (for example, A1 and B1) and that are just above two empty cells.

2.	Create a table using the following steps:    

	a. Select a cell in the header row.

	b. On the **Insert** ribbon, select **Table**.

	c. In the dialog window, select **My table has headers**, and select **OK**.

		![Create a table](./media/add-images-pictures-audio-video/create-table.png)

		Your Excel file is now in a table format. See [Format the data as a table](https://support.office.com/en-us/article/Format-an-Excel-table-6789619F-C889-495C-99C2-2F971C0E2370) for more information on table formatting in Excel.

	d. Name the table **Media**:  

		![Rename table to Drawings](./media/add-images-pictures-audio-video/name-media-table.png)

3. Save the file (for example, as **MediaDemo**), and upload it to your cloud-storage account. If you are using OneDrive, you can save it directly there.

## Create an app from the data source

1. In PowerApps, click or tap **New** on the **File** menu (along the left edge if you haven't yet opened an app). Next click or tap **Phone layout** in the tile for your cloud-storage account, OneDrive in this tutorial.

	![Select your cloud-storage account](./media/add-images-pictures-audio-video/select-account.png)

2. Under **Choose an Excel file**, click or tap the file that you created.

	![](./media/add-images-pictures-audio-video/select-workbook.png)

3. Under **Choose a table**, click or tap the table that you created, and then click or tap **Connect**.

	![Select your table](./media/add-images-pictures-audio-video/select-table.png)


## Modify the app to use the pen control

In this scenario, you learn how to modify the app to upload pen drawings to your data source (OneDrive in this case), and examine how the drawings are stored in OneDrive.

1. As in the preceding sections, create an Excel file with one column named **Image [image]**, in a table named **Drawings**, and save the Excel file to OneDrive as **SavePen.xlsx**.

2.	In PowerApps, create a [blank app](get-started-create-from-blank.md).

3.	In your app, add the cloud storage account as a [data source](add-data-connection.md) by:

	*	click or tap the **Content** tab and then click or tap **Data sources**.

		![](./media/add-images-pictures-audio-video/choose-data-sources.png)

	*	click or tap **Add data source** and click or tap one, OneDrive in this case.

		![](./media/add-images-pictures-audio-video/select-source.png)

	*	Click or tap **SavePen.xlsx**.

	*	Select the **Drawings** table and click or tap **Connect**.

4. Once added as a data source, add **SavePen.xlsx** as a connection, and then select the **Drawings** table:  

	![Connect](./media/add-images-pictures-audio-video/savepen.png)  

	Now, the Drawings table is listed as a Data source.

5.  On the **Insert** menu, select **Text**, and then select **Pen input**. Rename it **MyPen**:  

	![Rename](./media/add-images-pictures-audio-video/rename-mypen.png)

6.	Add a **Button** control (**Insert** menu), and set its **OnSelect** property to the following formula:

			Patch(Drawings, Defaults(Drawings), {Image:MyPen.Image})

7.	Add an **Image gallery** control (**Insert** menu > **Gallery**), and set its **Items** property to `Drawings`. The **Image** property of the gallery control is automatically set to `ThisItem.Image`.

	Your screen should look similar to the following:  

	![Sample screen](./media/add-images-pictures-audio-video/screen.png)

8.	Press F5 or select Preview ( ![](./media/add-images-pictures-audio-video/preview.png) ). Draw something in MyPen, and the select the button. The first image in the gallery control displays what you drew. Add something else to your drawing, and select the button. The second image in the gallery control displays what you drew.

	Close the preview window.

9. Go to your cloud storage account. There's a new **SavePen_images** folder that is automatically created. You may need to refresh to see the new folder. This folder contains your saved images with IDs for their file names.

10.	Open **SavePen.xlsx**. The *Image* column specifies the path to the new images.

[!INCLUDE [testing-requirements](../includes/testing-requirements.md)]

## Add the images in an Excel file in OneDrive to your app

In this scenario, you save images in a cloud storage account, OneDrive, and then use an Excel table to display the images in your app. This scenario uses the [CreateFirstApp.zip](http://pwrappssamples.blob.core.windows.net/samples/CreateFirstApp.zip) that contains some .jpeg files.

> [!NOTE]
> When displaying images from an Excel file, the path to these images must use forward slashes. When PowerApps saves images to an Excel table (as with the previous steps), the path uses backslashes. So, you can also use the **SavePen_images** from the previous example. If you do, change the paths in the Excel table to use forward slashes instead of backslashes. Otherwise, the images will not display.  

1. Download [CreateFirstApp.zip](http://pwrappssamples.blob.core.windows.net/samples/CreateFirstApp.zip), and extract the **Assets** folder to your cloud storage account.

2. In an Excel spreadsheet, create a one-column table and fill it with the following data:

	![Jackets table](./media/add-images-pictures-audio-video/jackets.png)

3. Name the table **Jackets**. Name the Excel file **Assets.xlsx**. You can also rename the **Assets** folder to **Assets_images**.

4. In your app, add the **Jackets** table as a data source.  

5. Add an **Image only** control (**Insert** menu > **Gallery**), and set its **Items** property to `Jackets`:  

	![Items property](./media/add-images-pictures-audio-video/items-jackets.png)

	The gallery is automatically updated with the images:  

	![Jacket images](./media/add-images-pictures-audio-video/images.png)

When you set the Items property, the Excel table is automatically updated with a new column named __PowerAppsId__.

In the Excel table, the image path can also be the URL to an image. To see an example of this, download the [Flooring Estimates](http://pwrappssamples.blob.core.windows.net/samples/FlooringEstimates.xlsx) sample file to your cloud storage account, add the `FlooringEstimates` table as a data source in your app, and then set the gallery control to `FlooringEstimates`. The gallery is automatically updated with the images.

[!INCLUDE [testing-requirements](../includes/testing-requirements.md)]

## For more information

For information on more advanced scenarios involving uploading multimedia directly to a different data source, see [image capture pro tips](https://powerapps.microsoft.com/blog/image-capture-pro-tips/) and [custom api for image upload](https://powerapps.microsoft.com/blog/custom-api-for-image-upload/).

Another way to upload files to a data source is to use the [Patch](functions/function-patch.md) function.


[1]: ./media/add-images-pictures-audio-video/add-image-video-audio-file.png
[3]: ./media/add-images-pictures-audio-video/add-intro-sound.png
[4]: ./media/add-images-pictures-audio-video/add-picture.png
[5]: ./media/add-images-pictures-audio-video/camera-gallery.png
[6]: ./media/add-images-pictures-audio-video/audio-gallery.png
[7]: ./media/add-images-pictures-audio-video/pen-gallery.png
[8]: ./media/add-images-pictures-audio-video/mediaoptions.png
[9]: ./media/add-images-pictures-audio-video/imageproperty.png
[10]: ./media/add-images-pictures-audio-video/mediaproperty.png
[11]: ./media/add-images-pictures-audio-video/renamecamera.png
