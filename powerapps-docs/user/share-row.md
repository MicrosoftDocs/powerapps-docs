---
title: "Share a row| MicrosoftDocs"
description: How to share a row.
author: mduelae
manager: kvivek
ms.service: powerapps
ms.component: pa-user
ms.topic: conceptual
ms.date: 08/1/2021
ms.subservice: end-user
ms.author: mkaur
ms.custom: ""
ms.reviewer: ""
ms.assetid: 
search.audienceType: 
  - enduser
search.app: 
  - PowerApps
  - D365CE
---

 ## Share a row with someone else
 
 [!INCLUDE [cc-beta-prerelease-disclaimer](../includes/cc-beta-prerelease-disclaimer.md)]
 
 If you want to keep ownership of a row but let someone else work on the row with you then use the share option.
 
Any user that you want to share a row with needs to have basic level access that is granted by a system administrator. If you cannot select an option when you share a row the you need to check with your system administrator to see if that user or team can be granted basic access based on your organizations roles and access defined by your administrator.

> ![Note]
> This feature is not supported on Power Apps mobile or when you're using the app in offline mode with no internet connection. 


## Share rows

1. You can share a row from a view page or when you open a row.

    - **Share from the view page**: Select one or more rows on a view page and then select **Share** on the command bar.

      > [!div class="mx-imgBorder"]
      > ![Share rows from the view page](media/share-row-view-page.png "Share rows from the view page")


    - **Open a row and share**: Open a row and then select **Share** on the command bar. If you don't see the share option, then select the **More commands** ellipsis and then select **Share**.

      > [!div class="mx-imgBorder"]
      > ![Open a row and then select share](media/share-row-1.png "Open a row and then select share.")

2.  On the share dialog box, select the lookup column under **Add user/team**.  

    > [!div class="mx-imgBorder"]
    > ![Select add user or team.](media/share-row-share-dialog.png "Select add user or team")
   
3. Enter the name of the user or team in the [lookup column](lookup-field.md). The lookup will start displaying users or teams based what you typed, or you can select the lookup icon (magnifying glass) and an alphabetical list of names appears that you can select to assign access.

    > [!div class="mx-imgBorder"]
    > ![Select add user or team in the lookup.](media/share-row-lookup-rows.png "Select add user or team in the lookup")

4. The user or team that you selected is listed under the lookup column. To add additional users or teams repeat the process or to remove a user or team from the list select **X** next to the name.

    > [!div class="mx-imgBorder"]
    > ![Select add more users or team](media/share-row-add-more-users.png "Select to add more users or team")


5. Select a user or team one at a time, and then grant them the appropriate permissions to the row. <br> <br> If check boxes are disabled it means a user or team does not have basic privileges to the row. For more information on user access, see [Check your user access to a row](access-checker).


    > [!div class="mx-imgBorder"]
    > ![Select a user or team and assign them permission to the row.](media/share-row-assign-permission.png "Select a user or team and assign them permission to the row.")


6. Select **Share** to save your changes. The changes made to all users or teams will be shared and options saved.

    > [!div class="mx-imgBorder"]
    > ![Sharing is successful.](media/share-row-shared.png "Sharing is successful.")

  > ![NOTE] 
  > If you add additional users or teams after saving share access and the check box is disable but has a value, this means that your administrator has changed the basic privileges for the user, and they no longer have basic access rights, however, the share permissions is retained and isn't reset when the administrator changes the base privileges. Contact your system administrator to update a user’s access if you want to change or update the disabled options for sharing a row.
 
 ## Issues and errors
 
1. If are disconnected from the internet when sharing a row, then you won't be able to set or update options for users or teams. Sharing won't be available.

   > [!div class="mx-imgBorder"]
   > ![Sharing and not internet connection.](media/share-ts1.png "Sharing and not internet connection.")

2. If you get a generic error while sharing, this means that one or more of the rows could not be shared. The users will be hi-lighted in red. You can selcted on **Share** in the dialog to attempt another share with those users or you can close the dialog and retry. This usually happens if you are sharing lots of rows at once.

   > [!div class="mx-imgBorder"]
   > ![Can't share the row with user.](media/share-ts2.png "Can't share a row with user.")

3. You may see an error when the system is unable to retrieve the users to assign share rights or sharing fails due to access related issues.


   > [!div class="mx-imgBorder"]
   > ![Sharing failed](media/share-ts3.png "Sharing failed")

<br><br>

   > [!div class="mx-imgBorder"]
   > ![Unable to share.](media/share-ts4.png "Unable to share.")


