<properties
    pageTitle="Share an app | Microsoft PowerApps"
    description="Share your app by giving other users permission to run or modify it."
    services=""
    suite="powerapps"
    documentationCenter="na"
<<<<<<< HEAD
    authors="jamesol-msft"
    manager="dwrede"
=======
    authors="AFTOwen"
    manager="erikre"
>>>>>>> 14faefd57481faea0496e429441498246b15d099
    editor=""
    tags=""
 />
<tags
    ms.service="powerapps"
    ms.devlang="na"
    ms.topic="article"
    ms.tgt_pltfrm="na"
    ms.workload="na"
    ms.date="04/07/2016"
    ms.author="jamesol"/>

# Share an app #
[AZURE.VIDEO nb:cid:UUID:4a51313a-0d00-80c4-1ead-f1e5920c334e]

[[[We need to either remove or update this video]]]

Share your app with co-workers or other users by giving them permission either to just run the app or to not only run it but also to customize it and then share their own versions.

Share an app with:
1. Multiple co-workers at the same time.
1. A group in Active Directory.
1. All users within your organization.

If you share an app with a group, everyone in that group will have the permissions that you assign to it. If users are added to or deleted from the group, they will gain and lose permissions accordingly.

If you share an app with your organization, everyone in that group will have permission only to run the app by default.

**Note**: Before you share an app, make sure that the people with whom you're sharing it have access to the data. For example, you must [share an Excel or other file](share-app-data.md) in a cloud-storage account.

## Prerequisites ##
- An account with which you've signed in to [powerapps.com](http://go.microsoft.com/fwlink/?LinkId=708209) or PowerApps.
- Either of the following:
	- An app that you built (from a [template](get-started-test-drive.md), from [data](get-started-create-from-data.md), or from [scratch](get-started-create-from-blank.md)).
	- An app that someone else built and given you permission to run, customize, and share.

## Share an app from web.powerapps.com ##
1. On [web.powerapps.com](http://go.microsoft.com/fwlink/?LinkId=708209), select **My Apps** in the left navigation bar.

	[[New image of the web portal nav bar]]

1. Select the tile of the app that you want to share.

1. Select the **Permissions** tab.

	[[Image of the Permissions tab in the App details page]]

1. If you want to share this app with a co-worker or work group then, in the dialog box that appears, type the first few letters of your co-worker’s work name or email address or work group's name or email address, and then select the person you want in the list that appears.

  In the list of permission types:
  - Select **Can use** to allow the user or group members to just run the app. This user will not be able to share your app with other users or groups.
  - Select **Can use and share** to allow the user or group members to run your app and share your app.
  - Select **Can edit** to allow the user or group memebers to run your app, customize it, and share a new version of your app.

	[[New portal image of 3 permission types]]

1. If you want to share this app with all users within your organization the select the checkbox for **Allow access to others users in my organization**.

1. Select **Save** to send a message that notifies the user or users you've specified of your shared app.

	The message contains a link that a user can select to access the app. Any users who don't have PowerApps (or aren’t signed up to use it) are prompted to install it and sign up for it.

## Share an app from PowerApps ##
1. In PowerApps, select **Open** in the **File** menu (near the left edge of the screen).

 ![List apps on powerapps.com the web](./media/share-app/open-apps.png)

1. Select the share icon for the app that you want to share.

  [[Client share icon]]

1. If you want to share this app with a co-worker or work group then, in the dialog box that appears, type the first few letters of your co-worker’s work name or email address or work group's name or email address, and then select the person you want in the list that appears.

  In the list of permission types:
  - Select **Can use** to allow the user or group members to just run the app. This user will not be able to share your app with other users or groups.
  - Select **Can use and share** to allow the user or group members to run your app and share your app.
  - Select **Can edit** to allow the user or group memebers to run your app, customize it, and share a new version of your app.

	[[New client image of 3 permission types]]

1. If you want to share this app with all users within your organization the select the checkbox for **Allow access to others users in my organization**.

1. Select **Share** to send a message that notifies the user or users you've specified of your shared app.

	The message contains a link that a user can select to access the app. Any users who don't have PowerApps (or aren’t signed up to use it) are prompted to install it and sign up for it.

## Change or remove permission ##
- On powerapps.com,
  - Select a different permission in the list that appears next to each user's name, or select the **x** icon to delete a user's permission.
  - Select the **x** icon next for the **My org** item to no longer share this app with all users within your organization.
- In PowerApps,
 - Select a user's name under **Shared with** to show options for changing or removing permission.
 - Select the **My org** item in the list under **Shared with** and then select **Delete** in order to no longer share this app with all users within your organization.
