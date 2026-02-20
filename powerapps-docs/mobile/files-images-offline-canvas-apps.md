---

title: Configure files and images in offline canvas apps
description: Learn how to configure files and images in offline canvas apps.
author: trdehove
ms.component: pa-user
ms.topic: how-to
ms.date: 02/20/2026
ms.subservice: mobile
ms.author: ritwikganni
ms.custom: ""
ms.reviewer: smurkute
ms.assetid: 
search.audienceType: 
  - enduser
searchScope:
  - "Power Apps"
---

# Configure files and images in offline canvas apps

This article explains how to configure files and images in a Power Apps table for offline canvas apps.

## Prerequisites

Have an existing canvas app with Dataverse tables. For more information, see [Build an app](../maker/canvas-apps/getting-started.md#build-an-app).

### View column properties for a file or image

1. Sign in to [Power Apps](https://make.powerapps.com).

1. In the left navigation menu, select **Tables**. [!INCLUDE [left-navigation-pane](../includes/left-navigation-pane.md)] 

1. Select the table that has the columns you want to view. 

1. Under **Schema**, select **Columns**.
  
1. Select the **Display name** of a column where **Data type** is set to **File** or **Image**.

1. The column properties show the **Data type**. Expand **Advanced options** to view the maximum size for a file or image. For more information about columns, see [Columns overview](../maker/data-platform/fields-overview.md).


## Download options

In an offline-enabled canvas app, there are two ways to download files and images:

- **On view**: Downloaded when you view them—the default option.
- **On sync**: Downloaded during offline sync when device is connected.

### Download files and images on view

When files and images are configured to download **on view**, the content is downloaded on the device when the user opens a file or when an image is presented to the user. Files and images are downloaded when the device is connected to the network and can be used afterward without connectivity.

This mode is enabled by default without any specific configuration.

If you want to keep this default, then you don't need to proceed with this article.

### Download files and images on sync

When files and images are configured to download **on sync**, they're downloaded during the offline sync when the device is connected. The user can access the content without connectivity and is notified when the download of the files and images is completed. **On sync** is recommended if you don't need to download a large number of files or images.

The remainder of this article helps you configure on sync.

## Configure on sync

To configure the automatic download of files and images on sync, you need to [create a custom, mobile offline profile](canvas-mobile-offline-setup.md#create-profiles-from-within-power-platform-admin-center-with-admin-rights). There are two ways to configure sync.

### Configure on sync from within Power apps studio

1. Sign in to [Power Apps](https://make.powerapps.com).

1. In the left navigation pane, select **Apps**.

1. Select a canvas app, and then on the command bar, select **Edit** to open your app in editing mode in canvas app designer.

1. Select **Settings > General**.

1. Set the **Can be used offline** toggle to On.

1. Under **Select offline profile**, select **Edit selected profile** from the "...".

1. Select the table that has file or image column that you want to enable for offline.

1. In the table details pane that appears, under the section **Related rows + Files and Images**, select the file and image column that you want to configure on sync.

1. Go back and select **Save**.

### Configure on sync from within Power Platform admin center (requires admin access)

You can add both the **Image Descriptor** and **FileAttachment** tables to your mobile offline profile by configuring the settings of your environment.

1. Go to [Power Platform admin center](https://admin.powerplatform.microsoft.com) and sign-in as an admin.
1. Select **Environments** from the navigation menu.
1. Choose an environment and then select **Settings** on the menu bar.
1. Expand **Users + permissions**, then select **Mobile configuration**.
1. Select a mobile offline profile to edit it.
1. In the **Data available offline** section, select **Add table**.
1. To enable offline access for images and files, add the **Image Descriptor** and **FileAttachment** tables to your mobile offline profile. To add the Image Descriptor table, follow these steps:
   1. Select **Image Descriptor** and then select **Next**.
   1. Under **Choose the rows that you want to make available offline**, select **Related rows only**.
   1. Expand **Relationships** and select **Column name: Display name** for each column where **Data type** is set to **Image**. In this example, we select the unnamed column names from the **DemoTable1** and **DemoTable3** tables.
   1. Select **Save**.
1. To add the FileAttachment table, follow these steps:
   1. Select **FileAttachment** and then select **Next**.
   1. Under **Choose the rows that you want to make available offline**, select **Related rows only**.
   1. Expand **Relationships** and select **Column name: My column name** for each column where **Data type** is set to **File**. In this example we add **Column name: MyFile** from the **DemoTable3** table.
    _Don't_ select **Column name: Regarding.**.
   1. Select **Save**.
