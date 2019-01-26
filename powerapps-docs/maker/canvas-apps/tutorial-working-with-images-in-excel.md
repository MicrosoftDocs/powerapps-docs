---
title: Save images in an Excel file | Microsoft Docs
description: How to save image in an Excel table in a cloud storage account
author: emcoope-msft
manager: kvivek
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: 
ms.date: 06/15/2016
ms.author: emcoope
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# How to save images in an Excel file, and then add these images to your app

In this tutorial, we:

* Create an Excel file and format it as a table
* Create a connection to OneDrive for Business. Any cloud storage account will work. In this walk-through, OneDrive for Business is used.
* Create an app with a pen input control
* Save the images created from the pen input control to an Excel file
* Display images from an Excel file in your app

[!INCLUDE [app-customization-requirements](../../includes/app-customization-requirements.md)]
* Learn how to [add a data source](add-data-connection.md)

## Create the Excel file as a table

1. In a blank Excel file, name a column **Image [image]**.
2. Create a table using the following steps:    
   
   1. Select any piece of data in any row and any column. For example, select **Image**.
   2. On the **Insert** ribbon, select **Table**.
   3. In the dialog window, select **My table has headers**, and select **OK**.
      
      Your Excel file is now in a table format. [Format the data as a table](https://support.office.com/article/Format-an-Excel-table-6789619F-C889-495C-99C2-2F971C0E2370) provides additional details on table formatting in Excel.
   4. Name the table **Drawings**:  
      
      ![Rename table to Drawings](./media/tutorial-working-with-images-in-excel/drawings-table.png)
3. Name the Excel file **SavePen.xlsx**, and save the file to your cloud storage account (OneDrive for Business, Dropbox, and so on).

## Create an app with the pen control
1. In PowerApps, create a [blank app](get-started-create-from-blank.md).
2. In your app, add the cloud storage account as a [data source](add-data-connection.md). Once added as a data source, add **SavePen.xlsx** as a connection, and then select the **Drawings** table:  
   ![Connect](./media/tutorial-working-with-images-in-excel/savepen.png)  
   
   Now, the Drawings table is listed as a Data source.
3. On the **Insert** menu, select **Text**, and then select **Pen input**. Rename it **MyPen**:  
   
   ![Rename](./media/tutorial-working-with-images-in-excel/rename-mypen.png)
4. Add a **Button** control (**Insert** menu), and set its **OnSelect** property to the following formula:  
   `Patch(Drawings, Defaults(Drawings), {Image:MyPen.Image})`
5. Add an **Image gallery** control (**Insert** menu > **Gallery**), and set its **Items** property to `Drawings`. The **Image** property of the gallery control is automatically set to `ThisItem.Image`.
   
   Your screen should look similar to the following:  
   
   ![Sample screen](./media/tutorial-working-with-images-in-excel/screen.png)  
6. Press F5 or select Preview (![](./media/tutorial-working-with-images-in-excel/preview.png)). Draw something in MyPen, and the select the button. The first image in the gallery control displays what you drew. Add something else to your drawing, and select the button. The second image in the gallery control displays what you drew.
   
   Close the preview window.
7. Go to your cloud storage account. There's a new **SavePen_images** folder that is automatically created. You may need to refresh to see the new folder. This folder contains your saved images with IDs for their file names.
   
    Open SavePen.xlsx. The Image column includes the path to these new images.

## Add the image in an Excel file to your app
In another example, you can save images in a cloud storage account, and then use an Excel table to display the images in your app.

In this example, we use the [CreateFirstApp.zip](http://pwrappssamples.blob.core.windows.net/samples/CreateFirstApp.zip) that contains some .jpeg files.

> [!NOTE]
> When displaying images from an Excel file, the path to these images must use forward slashes. When PowerApps saves images to an Excel table (as with the previous steps), the path uses backslashes. So, you can also use the **SavePen_images** from the previous example. If you do, change the paths in the Excel table to use forward slashes instead of backslashes. Otherwise, the images will not display.  

1. Download [CreateFirstApp.zip](http://pwrappssamples.blob.core.windows.net/samples/CreateFirstApp.zip), and extract the **Assets** folder to your cloud storage account.
2. In an Excel spreadsheet, create a table that looks similar to the following:
   
    ![Jackets table](./media/tutorial-working-with-images-in-excel/jackets.png)
3. Name the table **Jackets**. Name the Excel file **Assets.xlsx**. You can also rename the **Assets** folder to **Assets_images**.
4. In your app, add the **Jackets** table as a data source.  
5. Add an **Image only** control (**Insert** menu > **Gallery**), and set its **Items** property to `Jackets`:  
   
    ![Items property](./media/tutorial-working-with-images-in-excel/items-jackets.png)
   
    The gallery is automatically updated with the images:  
   
    ![Jacket images](./media/tutorial-working-with-images-in-excel/images.png)

When you set the Items property, the Excel table is automatically updated with a new column named **PowerAppsId**.

In the Excel table, the image path can also be the URL to an image. Download the [Flooring Estimates](http://pwrappssamples.blob.core.windows.net/samples/FlooringEstimates.xlsx) sample file to your cloud storage account, add the `FlooringEstimates` table as a data source in your app, and then set the gallery control to `FlooringEstimates`. The gallery is automatically updated with the images.

## Learn more
[Add an image, a video, or a sound](add-images-pictures-audio-video.md)  
[Show data in a line, pie, or bar chart in your app](use-line-pie-bar-chart.md)  
[Understand tables and records in PowerApps](working-with-tables.md)

