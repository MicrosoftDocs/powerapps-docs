<properties
    pageTitle="Conference Attendee Sample App | Microsoft PowerApps"
    description="Sample app with SQL Server as a data source"
    services=""
    suite="powerapps"
    documentationCenter="na"
    authors="merwanhade"
    manager="dwrede"
    editor=""
    tags=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="12/22/2015"
   ms.author="mhade"/>

# Sample app: conference attendee #

This sample app demonstrates key concepts such as:

- Binding galleries to data in a master-details pattern
- Navigational patterns such as tabs and back buttons
- Viewing and categorizing information in different ways
- Storing personalized data per user 

The app enables conference attendees to view a list of sessions, details about a particular session, and information about the session's speaker. In addition, attendees can also add sessions to a list of favorites.  
![Conference Attendee Display Image 1](./media/samples-conference-attendee/conference-attendee-display-1.png)
![Conference Attendee Display Image 2](./media/samples-conference-attendee/conference-attendee-display-2.png)
![Conference Attendee Display Image 3](./media/samples-conference-attendee/conference-attendee-display-3.png)

**Prerequisites**

- [Install PowerApps](http://aka.ms/powerappsinstall)
- A Dropbox, OneDrive, or Google Drive account. (In this tutorial, you'll use Dropbox.)

## Get the sample data ##
1. Download [this sample](http://aka.ms/conferenceattendeesample), and decompress it on your computer.

	The sample data includes:

	- a PowerApps file, named **conference-attendee-excel.msapp**
	- an Excel file, named **data.xlsx**
	- a folder, named **data_images** 

1. Create a folder named **ConferenceAttendee** in your cloud-storage account (for example, Dropbox).

	![Add folder in Dropbox](./media/samples-conference-attendee/dropbox-create-folder.png)

1. In the **ConferenceAttendee** folder, upload **data.xlsx**, and create a folder called **data_images**.

	![ConferenceAttendee folder in Dropbox](./media/samples-conference-attendee/dropbox-content-conferenceattendee-folder.png)

1. Upload all the files from the **data_images** folder on your computer to the corresponding folder in your cloud-storage account.

	![data_images folder in Dropbox](./media/samples-conference-attendee/dropbox-content-conferenceattendee-images.png)

## Connect from PowerApps to cloud storage ##
Skip this procedure if you've already created a connection from PowerApps to your cloud-storage account.

1. Open PowerApps, and then select **Connections** on the **File** menu (near the left edge of the screen).

	![Connections option on the File menu](./media/samples-conference-attendee/file-connections.png)

1.  Select **Available Connections**, select your cloud-storage provider, and then select **Connect**.

	![Choose Connect button](./media/samples-conference-attendee/powerapps-dropbox-connect.png)

1. When prompted, provide your credentials.

	![Provide credentials for cloud-storage account](./media/samples-conference-attendee/provide-credentials.png)

## Open the app ##

1. On the **File** menu, select **Open**.

	![Open option on the File menu](./media/samples-conference-attendee/file-open.png)

1. Near the upper-right corner, select **Browse**.

	![Browse to the conference-attendee-excel.msapp file](./media/samples-conference-attendee/browse-icon.png)

1. Navigate to the **conference-attendee-excel.msapp** file, and then select **Open**.

## Configure the app ##

1. When the app opens, select **Options** near the lower-right corner, and then select **Insert your data**.

	![Select Options, and then select Insert your data](./media/samples-conference-attendee/powerapps-insert-your-data.png)

1. Under **My connections**, select the connection to your cloud-storage provider.

	![Select the Dropbox connection you created](./media/samples-conference-attendee/powerapps-choose-dropbox-conn.png)

1. Open the **ConferenceAttendee** folder, and then select the **data.xlsx** file.

	![Select the data.xlsx file](./media/samples-conference-attendee/powerapps-select-data-xlsx.png)

1. Select the check box for each table, and then select **Insert**.

	![Select all tables](./media/samples-conference-attendee/powerapps-select-tables.png)

## Run the app ##

1. Change views by selecting the view toggle button. You can either view sessions by time or by track. 
</br>**Note** - The first time you run this app, you may have to click the toggle button to fetch data. </br>
![Select the toggle button](./media/samples-conference-attendee/conference-attendee-run-1.png)
![Select the toggle button-2](./media/samples-conference-attendee/conference-attendee-run-1-2.png)

2. Select a particular session from the list to view session details such as location and speaker information. 
![Select a session](./media/samples-conference-attendee/conference-attendee-run-2.png)

3. Select the speaker to view more information about the speaker. </br>
![Select the speaker](./media/samples-conference-attendee/conference-attendee-run-3.png)
4. In the speaker details screen, you can click on the LinkedIn and Twitter buttons to launch the respective websites or add other sessions by the speaker to your favorites.  
![Select the favorites button](./media/samples-conference-attendee/conference-attendee-run-4-1.png)
![Observe the favorites button](./media/samples-conference-attendee/conference-attendee-run-4-2.png)
5. You can view your favorite sessions by navigating to the **My sessions** tab on the home screen. </br>
![View favorited sessions](./media/samples-conference-attendee/conference-attendee-run-5.png)
 
