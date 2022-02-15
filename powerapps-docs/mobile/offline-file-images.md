---
title: "Configure mobile offline profiles for files and images| Microsoft Docs"
description: Configure mobile offline profiles for files and images.
author: mduelae
ms.component: pa-user
ms.topic: quickstart
ms.date: 02/15/2022
ms.subservice: mobile
ms.author: mkaur
ms.custom: ""
ms.reviewer: ""
ms.assetid: 
search.audienceType: 
  - enduser
search.app: 
  - PowerApps
  - D365CE
searchScope:
  - "Power Apps"
---

# Configure mobile offline profiles for images and files 

To work with file and image columns in offline mode, you need to add additional tables and relationships.

Follow the steps in this topic, for a mobile offline profile that has a table with a column where **Data type** is set to **File** or **Image**.



## View column properties for a file or image 

1. Sign in to [Power Apps](https://make.powerapps.com).

2. On the left nav select **Data** to expand it and then select **Tables**.  

   > [!div class="mx-imgBorder"]
   >![Go to tables.](media/maker-data-tables.png "Go to tables")
  
  
3. Select the **Display name** of a column where **Data type** is set to **File** or **Image**.

4. The column properties show the **Data type**. Expand **Advanced options** to view the maximum size for a file or image.

   > [!div class="mx-imgBorder"]
   >![Maximum size for files and images.](media/offline-file-images-1.png "Maximum file and image size")


## Add image columns to mobile offline 

It is required to add both the **Image Descriptor** and **FileAttachment** tables to your mobile offline profile to make images available in offline mode.

1. Go to Power Platform Admin center, [https://admin.powerplatform.microsoft.com](https://admin.powerplatform.microsoft.com) and sign-in as an admin.

2. On the right, select **Environments**.

   > [!div class="mx-imgBorder"]
   >![Select a Environment.](media/offline_admincenter_enviroments.png "Select a Environment")
 
3. Choose an environment and then select **Settings**.

   > [!div class="mx-imgBorder"]
   >![Environment settings.](media/offline_open_an_enviroment.png "Environment settings")
 
4. Expand **Users + permissions**, and then select **Mobile configuration**.

   > [!div class="mx-imgBorder"]
   >![Mobile configuration setting.](media/offline_mobile_config_settings.png "Mobile configuration settings")

5. Select a mobile offline profile to edit it.

6. In **Data available offline** select **Add table**.

7. Select **Image Descriptor** and then select **Next**.

   > [!div class="mx-imgBorder"]
    >![Select image descriptor.](media/offline-file-images.png "Select image descriptor")

8. Under **Choose the records that you want to make available offline**, select **Related records only**.
9. Expand **Relationships** and select **Column name:** for each applicable column where **Data type** is set to **Image** (that is, as shown in the screenshot below for the **DemoTable1** and **DemoTable3** tables).

   > [!div class="mx-imgBorder"]
    >![Add image descriptor.](media/offline-file-images-2.png "Add image descriptor")
  
10. Select **Save**.
11. In **Data available offline** select **Add table** > **FileAttachment** > **Next**. 
12. Expand **Relationships** and select **Image Descriptor, Column name: FileId**.
    
    > ![Note] Don't select **Image Descriptor, Column name: Regarding**.

    > [!div class="mx-imgBorder"]
    > ![Add FileAttachment table.](media/mobile-offline-edit-image.png "Add FileAttachment table")

10. Select **Save**.


## Add file columns to mobile offline 

It is required to add the **FileAttachment** tables to your mobile offline profile to make files available in offline mode.

1. Go to Power Platform Admin center, [https://admin.powerplatform.microsoft.com](https://admin.powerplatform.microsoft.com) and sign-in as an admin.

2. On the right, select **Environments**.

   > [!div class="mx-imgBorder"]
   >![Select a Environment.](media/offline_admincenter_enviroments.png "Select a Environment")
 
3. Choose an environment and then select **Settings**.

   > [!div class="mx-imgBorder"]
   >![Environment settings.](media/offline_open_an_enviroment.png "Environment settings")
 
4. Expand **Users + permissions**,  and then select **Mobile configuration**.

   > [!div class="mx-imgBorder"]
   >![Mobile configuration setting.](media/offline_mobile_config_settings.png "Mobile configuration settings")

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
   
  
## Offline status of files and images

You can use the **[Offline Status](work-in-offline-mode.md#see-whether-offline-mode-is-available)** page to see the number of files and images to be downloaded and the current progress.

- The number of images is listed for the **Image Descriptor** table.
- The number of files are listed for each table with file attachments (that is, as shown in the screenshot below for the **DemoTable2** table).

  > [!div class="mx-imgBorder"]
  >![Offline status of files and images.](media/offline-status.png "Offline status of files and images.")
