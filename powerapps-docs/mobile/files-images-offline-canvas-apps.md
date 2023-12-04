---

title: Configure files and images in offline canvas apps (preview)
description: Learn how to configure files and images in offline canvas apps.
author: trdehove
ms.component: pa-user
ms.topic: article
ms.date: 12/04/2023
ms.subservice: mobile
ms.author: trdehove
ms.custom: ""
ms.reviewer: sericks
ms.assetid: 
search.audienceType: 
  - enduser
searchScope:
  - "Power Apps"
---


# Configure files and images in offline canvas apps (preview)
[This article is prerelease documentation and is subject to change.]

The support of files and images is currently in preview. To enable it, the canvas app must be enabled for offline and you must activate the feature.

> {!Important]
> - This is a preview feature.
> - Preview features aren't meant for production use and may have restricted functionality. These features are available before an official release so that customers can get early access and provide feedback.

## Turn on support for file/image column in Dataverse offline feature
1. In [Power Apps studio](../maker/canvas-apps/power-apps-studio.md), in the left side panel, select **Apps**.

1. Select your canvas app, and then select **Edit**.

1. Select **Settings**.

1. Select **Upcoming features**, and then select the **Preview** tab.

1. Turn on the **Enable support for file/image column in Dataverse offline** option.

In an offline-enabled canvas app, you can either allow the files and images to be downloaded **on view**, which is the default option or **on sync**. We recommend that you download files and images on sync if you don't expect to download a large number of files or images.

## Download files and images on view 
When files and images are configured to be downloaded **on view**, the content is downloaded on the device when the user explicitely opens a file or when an image is presented to the user. Files and images are downloaded when the device is connected to the network and can be used afterward without connectivity.

This mode is enabled by default without any specific configuration. 

## Download files and images on sync
When files and images are configured to be downloaded **on sync**, files and images are downloaded during the offline sync when the device is connected. The user can access the content without connectivity and is notified in the application when the download of the files and images is completed. 

### Add image columns to mobile offline 

It is required to add both the **Image Descriptor** and **FileAttachment** tables to your mobile offline profile to make images available in offline mode.

1. Go to Power Platform admin center, [https://admin.powerplatform.microsoft.com](https://admin.powerplatform.microsoft.com) and sign-in as an admin.

2. In the navigation panel, select **Environments**.
 
3. Choose an environment and then select **Settings**.
 
4. Expand **Users + permissions**, and then select **Mobile configuration**.

5. Select a mobile offline profile to edit it.

6. In **Data available offline** select **Add table**.

7. Select **Image Descriptor** and then select **Next**.

8. Under **Choose the rows that you want to make available offline**, select **Related rows only**.

9. Expand **Relationships** and select **Column name:** for each applicable column where **Data type** is set to **Image** (that is, as shown in the screenshot below for the **DemoTable1** and **DemoTable3** tables).

    > [!div class="mx-imgBorder"]
    > ![Add image descriptor.](media/offline-file-images-2.png "Add image descriptor")
  
10. Select **Save**.

11. In **Data available offline** select **Add table** > **FileAttachment** > **Next**. 

12. Expand **Relationships** and select **Image Descriptor, Column name: FileId**. Don't select **Image Descriptor, Column name: Regarding**.

    > [!div class="mx-imgBorder"]
    > ![Add FileAttachment table.](media/mobile-offline-edit-image.png "Add FileAttachment table")

13. Select **Save**.


### Add file columns to mobile offline 

It is required to add the **FileAttachment** tables to your mobile offline profile to make files available in offline mode.

1. Go to Power Platform Admin center, [https://admin.powerplatform.microsoft.com](https://admin.powerplatform.microsoft.com) and sign-in as an admin.

2. On the right, select **Environments**.
 
3. Choose an environment and then select **Settings**.
 
4. Expand **Users + permissions**,  and then select **Mobile configuration**.

5. Select a mobile offline profile to edit it.

6. In the **Data available offline** select **Add table**.

7. Select **FileAttachment**  and then select **Next**.

   > [!div class="mx-imgBorder"]
    >![Select FileAttachment.](media/offline-file-images-4.png "Select FileAttachment")

8. Under **Choose the records that you want to make available offline**, select **Related records only**.

9. Expand **Relationships** and select **Column name: Display name** for each applicable column where **Data type** is set to **File** (that is, as shown in the screenshot below for the **DemoTable3** table).

   > ![Note] Don't select **Column name: Regarding.**.

    > [!div class="mx-imgBorder"]
    >![Edit FileAttachment table.](media/offline-file-images-9.png "Edit FileAttachment table.")
   

 11. Select **Save**. 
