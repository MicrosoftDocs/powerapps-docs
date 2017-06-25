<properties
    pageTitle="Share Excel files used by an app | Microsoft PowerApps"
    description="Share Excel files in Dropbox, OneDrive, and Google Drive. Users can edit and can view files and folders."
    services=""
    suite="powerapps"
    documentationCenter="na"
    authors="jamesol-msft"
    manager="anneta"
    editor=""
    tags=""
 />
<tags
    ms.service="powerapps"
    ms.devlang="na"
    ms.topic="article"
    ms.tgt_pltfrm="na"
    ms.workload="na"
    ms.date="10/16/2016"
    ms.author="jamesol"/>

# Share Excel data used by your app #
You can share Excel data with your app users in a [cloud account](cloud-storage-blob-connections.md), such as OneDrive.

For example, you might create an app that shows the names and phone numbers of the technical-support group at your company. The information is stored in an Excel spreadsheet, which you put in a folder in Dropbox. You then share the folder with your app users so that they can see the names and phone numbers.

You must share the data so that users can run and even modify your app. Users who aren't given the sharing permissions won't see the data in the Excel file.

This topic shows you how to share data in an Excel spreadsheet using Dropbox, OneDrive, and Google Drive. To create an app that displays data from an Excel file, see [Create an app from a set of data](get-started-create-from-data.md).

## Share data in Dropbox ##

1. Sign in to Dropbox using the same account that you used to create a connection from PowerApps to Dropbox.

1. Select the folder that contains the Excel file, and then select **Share**:  

	![Share command](./media/share-app-data/dropbox-share.png)

1. In the dialog box, enter the email addresses with which your app users sign in to Dropbox.  

	![Share on Dropbox](./media/share-app-data/dropbox-perms.png)

1. If your app users will add, modify, or delete data in your app,  select **Can edit**. Otherwise, select **Can view**.

1. Select **Share**.

For more information, see [Sharing folders on Dropbox](https://www.dropbox.com/en/help/19).

## Share data in OneDrive ##
1. Sign in to OneDrive using the same account that you used when you created a connection from PowerApps to OneDrive.

1. Select the folder that contains the file, and then select **Share**:  

	![Share command](./media/share-app-data/onedrive-share.png)

1. In the dialog box, select **Email**.

	![Share by email](./media/share-app-data/onedrive-email.png)

1. Specify the email addresses with which your app users sign in to OneDrive, and then select **Share**.  

	![Specify a user](./media/share-app-data/onedrive-perms.png)

For more information, see [Share OneDrive files and folders](https://support.office.com/article/Share-OneDrive-files-and-folders-and-change-permissions-9fcc2f7d-de0c-4cec-93b0-a82024800c07).

## Share data in Google Drive ##
1. Sign in to Google Drive using the same account with which you created a connection from PowerApps to Google Drive.

1. Right-click the folder that stores your Excel file, and then select **Share**.  

	![Share command](./media/share-app-data/googledrive-share.png)

1. In the dialog box, enter the email addresses with which your app users sign in to Google Drive:  

	![Specify a user](./media/share-app-data/googledrive-perms.png)

1. If your app users will add, modify, or delete data in your app, then select **Can edit** in the list of permissions. Otherwise, select **Can view**.

1. Select **Done**.

For more information, see [Share Google Drive files and folders](https://support.google.com/drive/answer/2494822).

## Known limitations

There are currently [certain limitations](./connections/cloud-storage-blob-connections.md#Sharing-Excel-Tables) with connectors involving Excel files. These affect apps that you share within your organization.
