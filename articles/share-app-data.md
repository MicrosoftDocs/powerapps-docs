<properties
    pageTitle="Share files used by an app | Microsoft PowerApps"
    description=""
    services=""
    suite="powerapps"
    documentationCenter="na"
    authors="KarthikB"
    manager="BillS"
    editor=""
    tags=""
 />
<tags
    ms.service="powerapps"
    ms.devlang="na"
    ms.topic="article"
    ms.tgt_pltfrm="na"
    ms.workload="na"
    ms.date="11/25/2015"
    ms.author="karthikb"/>

# Share data associated with an app #
If an app connects to files (say Excel) and is shared, then the receiver of the shared app needs access to those files before launching the shared app. The sharer has to configure access to those files outside of PowerApps. This walk-through outlines those steps when files are stored on Dropbox, OneDrive or Google Drive .

## Prerequisites ##
- An account with which you've signed in to [powerapps.com](http://go.microsoft.com/fwlink/?LinkId=708209) or PowerApps.
- Either of the following:
	- An app that you built (from a [template](get-started-test-drive.md), from [data](get-started-create-from-data.md), or from [scratch](get-started-create-from-blank.md)).
	- An app that someone else built and given you permission to run, customize, and share.

## Sharing files used by shared apps  ##
You need to share files in OneDrive, Dropbox or Google Drive used by your app before sharing the app with others.

### Sharing files stored on OneDrive ###

1. Login to OneDrive website and navigate to folder that contains the Excel file used in your app. You need to use the same credentials configured for the OneDrive connection used in PowerApps. If the app being shared was created using a template, you will have the "PowerApps" folder in your OneDrive.

1. Select the folder containing the file and click Share.

	![Share command](./media/share-app-data/OneDrive-folder.png)

1. In the dialog box that appears, type your co-worker’s OneDrive email address with whom the app will be shared with. You need to grant edit permissions if the receiver of the app enters data into the file using your app.

	![Specify a user](./media/share-app-data/OneDrive-folder-share.png)

For more details refer to [share files and folders on OneDrive](https://support.office.com/en-us/article/Share-files-and-folders-and-change-permissions-9fcc2f7d-de0c-4cec-93b0-a82024800c07).

### Sharing files stored on Dropbox ###

1. Login to Dropbox website and navigate to the folder that contains the Excel file used in your app. You need to use the same credentials configured for the Dropbox connection used in PowerApps. If the app being shared was created using a template, you will have the "PowerApps" folder in your Dropbox.

1. Select the folder containing the file and click on Share. Select **Invite people to collaborate**

	![Share command](./media/share-app-data/Dropbox-folder.png)

1. In the dialog box that appears, type your co-worker’s Dropbox email address with whom the app will be shared with. You need to grant edit permission if the receiver of the app enters data into the file using your app.

	![Specify a user](./media/share-app-data/Dropbox-folder-share.png)

For more details refer to [how do I share folders with other people using Dropbox](https://www.dropbox.com/en/help/19).

### Sharing files stored on Google Drive ###

1. Login to Google Drive website and navigate to folder that contains the Excel file used in your app. You need to use the same credentials configured for the Google Drive connection used in PowerApps. If the app being shared was created using a template, you will have the "PowerApps" folder in your Google Drive.

1. Select the folder and click Share.

	![Share command](./media/share-app-data/GoogleDrive-folder.png)

1. In the dialog box that appears, type your co-worker’s Dropbox email address with whom the app will be shared with. You need to grant edit permission if the receiver of the app enters data into the file using your app.

	![Specify a user](./media/share-app-data/GoogleDrive-folder-share.png)

For more details refer to [how to share folders using Google Drive](https://support.google.com/drive/answer/2494822?hl=en).
