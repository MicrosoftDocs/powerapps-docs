<properties
    pageTitle="Share Excel files used by an app | Microsoft PowerApps"
    description="Share Excel files in Dropbox, OneDrive, and Google Drive. Users can edit and can view files and folders."
    services=""
    suite="powerapps"
    documentationCenter="na"
    authors="jamesol-msft"
    manager="erikre"
    editor=""
    tags=""
 />
<tags
    ms.service="powerapps"
    ms.devlang="na"
    ms.topic="article"
    ms.tgt_pltfrm="na"
    ms.workload="na"
    ms.date="04/19/2016"
    ms.author="jamesol"/>

# Share Excel data used by your app #

You can share Excel data with your app users using Dropbox, OneDrive, and Google Drive.

For example, you have an Excel spreadsheet that lists the names and phone numbers of the technical support group at your company. You want to create an app that shows the information in this spreadsheet. To do this, you can put the Excel file in Dropbox, OneDrive, or Google Drive. Then, "share" the Excel spreadsheet so your app users can see the names and phone numbers.

Sharing the file is required so users can run and even modify your app. Users who aren't given the sharing permissions won't see the data in the Excel file.

This topic shows you how to share an Excel spreadsheet using Dropbox, OneDrive, and Google Drive. To create an app that displays data from an Excel file, see [Create an app from a set of data](get-started-create-from-data.md).

## Share data in Dropbox ##

1. When you create a connection to Dropbox, you sign-in with a specific Dropbox account. Sign-in to Dropbox using this same account.

1. Go to the folder that stores your Excel file.

	> [AZURE.NOTE] When you share an app that you [created using a template](get-started-test-drive.md), then the "PowerApps" folder is automatically created in your Dropbox account.

1. Select the folder that contains the Excel file, and then select **Share**:  

	![Share command](./media/share-app-data/Dropbox-folder.png)

1. Select **Invite people to collaborate**.

1. In the dialog box, enter the email addresses that your app users use to sign-in to Dropbox:  

	![Specify a user](./media/share-app-data/Dropbox-folder-share.png)

1. If your app users will add, modify, or delete data in your app, then select **can edit**. Otherwise, select **can view**.

1. Select **Share folder**.

[Sharing folders on Dropbox](https://www.dropbox.com/en/help/19) provides more information on sharing files using Dropbox.


## Share data in OneDrive ##

1. When you create a connection to OneDrive, you sign-in with a specific OneDrive account. Sign-in to OneDrive using this same account.

1. Go to the folder that stores your Excel file.

	> [AZURE.NOTE] When you share an app that you [created using a template](get-started-test-drive.md), then the "PowerApps" folder is automatically created in your OneDrive account.

1. Select the folder that contains the file, and then select **Share**:  

	![Share command](./media/share-app-data/OneDrive-folder.png)

1. In the dialog box, enter the email addresses that your app users use to sign-in to OneDrive:  

	![Specify a user](./media/share-app-data/OneDrive-folder-share.png)

1. If your app user will add, modify, or delete data in your app, then select **Can edit** in the list of permissions. Otherwise, select **Can view**.

1. Select **Share**.

[Share OneDrive files and folders ](https://support.office.com/article/Share-OneDrive-files-and-folders-and-change-permissions-9fcc2f7d-de0c-4cec-93b0-a82024800c07) provides more information on sharing files using OneDrive.


## Share data in Google Drive ##

1. When you create a connection to Google Drive, you sign-in with a specific Google Drive account. Sign-in to Google Drive using this same account.

1. Go to the folder that stores your Excel file.

	> [AZURE.NOTE] When you share an app that you [created using a template](get-started-test-drive.md), then the "PowerApps" folder is automatically created in your Google Drive account.

1. Select the folder, and then select the icon to share it:  

	![Share command](./media/share-app-data/GoogleDrive-folder.png)

1. In the dialog box, enter the email addresses that your app users use to sign-in to Google Drive:  

	![Specify a user](./media/share-app-data/GoogleDrive-folder-share.png)

1. If your app user will add, modify, or delete data in your app, then select **Can edit** in the list of permissions. Otherwise, select **Can view**.

1. Select **Done**.

[Share Google Drive files and folders](https://support.google.com/drive/answer/2494822) provides more information on sharing files using Google Drive.
