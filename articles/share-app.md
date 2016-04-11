<properties
    pageTitle="Share an app | Microsoft PowerApps"
    description="Share your app by giving other users permission to run or modify it."
    services=""
    suite="powerapps"
    documentationCenter="na"
    authors="jamesol-msft"
    manager="dwrede"
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

Share your app with co-workers or other users by giving them permission either to just run the app or to not only run it but also to customize it and then share their own versions.

Share an app with:
1. Multiple co-workers at the same time.
1. A group in Active Directory.
1. All users within your organization.

If you share an app with a group, everyone in that group will have the permissions that you assign to it. If users are added to or deleted from the group, they will gain and lose permissions accordingly.

If you share an app with your organization, everyone in that group will have permission only to run the app by default.

[What is PowerApps?](https://aka.ms/pamktg)

## Prerequisites ##
- An account with which you've signed in to [powerapps.com](http://go.microsoft.com/fwlink/?LinkId=708209) or PowerApps.
- Either of the following:
	- An app that you built (from a [template](get-started-test-drive.md), from [data](get-started-create-from-data.md), or from [scratch](get-started-create-from-blank.md)).
	- An app that someone else built and given you permission to run, customize, and share.

## Share an app from web.powerapps.com ##
1. On [web.powerapps.com](http://go.microsoft.com/fwlink/?LinkId=708209), select **My PowerApps** in the left navigation bar.

	[[New image of the web portal nav bar]]

1. Select the tile of the app that you want to share.

1. Select the share icon for the app that you want to share.

	![Share icon](./media/share-app/share-icon.png)

1. In the dialog box that appears, type the first few letters of your co-worker’s name or email address, and then select the person you want in the list that appears.

1. In the list of permission types, select **Can view** to allow the user to just run the app, or select **Can edit** to allow the user to run your app, customize it, and share a new version of your app.

	On **powerapps.com**

	![Choose permissions](./media/share-app/permission-list-portal.png)

	In **PowerApps**

	![Choose permissions](./media/share-app/permissions-pa.png)

1. Select **Save** on powerapps.com or **Share** in PowerApps to send a message that notifies the user or users you've specified of your shared app.

	The message contains a link that a user can select to access the app. Any users who don't have PowerApps (or aren’t signed up to use it) are prompted to install it and sign up for it.

## Share an app from PowerApps ##
1. In PowerApps, select **Open** in the **File** menu (near the left edge of the screen).

 ![List apps on powerapps.com the web](./media/share-app/open-apps.png)

 **- Do we need a screenshot for the iOS and Android clients?**

## Change or remove permission ##
- On powerapps.com, select a different permission in the list that appears next to each user's name, or select the **x** icon to delete a user's permission.
- In PowerApps, hover over a user's name under **Shared with** to show options for changing or removing permission.
