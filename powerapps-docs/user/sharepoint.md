---
title: "Manage your SharePoint documents and document locations| MicrosoftDocs"
ms.custom: ""
author: mduelae
manager: kvivek
ms.service: powerapps
ms.component: pa-user
ms.topic: conceptual
ms.date: 02/28/2020
ms.author: mduelae
ms.custom: ""
ms.reviewer: ""
ms.assetid: 
search.audienceType: 
  - enduser
search.app: 
  - PowerApps
  - D365CE
---
# Manage your SharePoint documents and document locations 

With Common Data Service, you can store your documents on SharePoint and manage them from within your app.

The documents that you create in your app are stored on SharePoint, and are automatically synced to your desktop and mobile devices.

Before you can use SharePoint to store documents, it must be enabled by your system administrator. More information:

-   [Find your administrator or support person](find-admin.md)  

-   [Manage your documents using SharePoint](https://docs.microsoft.com/power-platform/admin/manage-documents-using-sharepoint)  

## Where do you access the documents from?

1. For record types that support document management, open the record, select the **Related** tab, and then select **Documents**.

   > [!div class="mx-imgBorder"]
   > ![Open the Documents tab in a record ](media/onedrive_nav.png "Open the Documents tab in a record")

2. Select **Document Location** > **Documents on Default Site 1**. When SharePoint is enabled, by default, the location is set to  **Documents on Default Site 1**.

   > [!div class="mx-imgBorder"]
   > ![Default location](media/sharepoint_defualtsite.png "Default location")


## Create a new document 

To create a new document and save it in SharePoint:

1. Open a record and go to the Document Associated Grid. For example, open a contact record.

2. On the open record, select the **Related** tab, and then select **Documents**.
 
    > [!div class="mx-imgBorder"]
    > ![Open the Documents tab in a record ](media/onedrive_nav.png "Open the Documents tab in a record")

2. Select **Document Location**, and change the location to **Documents on Default Site 1**.

3. Select **New**, and then choose a document type such as Word, Excel, PowerPoint and so on. 

    > [!div class="mx-imgBorder"]
    > ![Creat a new documents ](media/onedrive_new_doc.png "Creat a new documents ")

4. Enter a document name, and then select **Save**.  

## Create a new folder 

To create a new folder in the default SharePoint site location:

1. Open a record and go to the Document Associated Grid. For example, open a contact record.

2. On the open record, select the **Related** tab, and then select **Documents**.
 
    > [!div class="mx-imgBorder"]
    > ![Open the Documents tab in a record](media/onedrive_nav.png "Open the Documents tab in a record")

2. Select **Document Location**, and change the location to **Documents on Default Site 1**.

3. Select **New**, and then choose **Folder**.

    > [!div class="mx-imgBorder"]
    > ![Creat a new folder](media/Sharepoint_new_folder.png "Creat a new folder")
    
 4. Enter a folder name, and then select **Save**.  
 
 
 ## Upload a document

To upload existing document to SharePoint from your app:

1. Go to the record you want to create the document for, select the **Related** tab and then select **Documents**.
 
2. Select **Upload.**

   > [!div class="mx-imgBorder"]
   > ![Upload documents](media/upload_doc.png "Upload documents")

3. Choose the file you want to upload. You can choose only one file at a time.

   The document is created in the current document location you're in.

   > [!Note]
   > You can upload a file of up to 50 MB. If your internet connection is slow, you might get an error while uploading large files.

4. If files with the same name exist in SharePoint, select whether you want to overwrite the files.

5. Select **OK**.

## Manage SharePoint locations

You can create new or edit existing SharePoint locations from your app in Common Data Service.

### Edit a location

1. Open a record and select the **Related** tab and then select **Documents**.

2. Select **Edit Location** and select a SharePoint site location.

   The **Edit Location** dialog box appears.

   > [!div class="mx-imgBorder"]
   > ![Edit Location](media/edit_location.png "Edit Location")

3. The display name, parent site, and folder name are automatically populated. Enter details about the new location, and then select **Save**.

### Add a new location

1. Open a record and select the **Related** tab and then select **Documents**.
2. Select **Add Location**. 

   The **Add Location** dialog box appears.

   > [!div class="mx-imgBorder"]
   > ![Add Location](media/add_location.png "Add Location")

3. The display name, parent site, and folder name are automatically populated. Change the details if required, and then select **Save**.

## Files tab FAQ
*Why was the location to access documents moved?* 
- We moved the command to make documents easier to find with fewer clicks.

*Has the Documents tab gone away?*
- No, it hasn’t gone away. Users can still access the documents associated with the record in question the old way, simply by clicking the Related menu and then the Documents link.

*With the change, will subfolders in SharePoint still be created automatically?*
- Yes. The behavior is similar to that of the **Documents** link under the **Related** menu. When a user selects the **Files** tab for the first time, the corresponding SharePoint sub-folder is created by the system. 

*Is there a way to add the Files tab to other entities or remove it?*
- Yes. To add or remove the File tab, follow the steps in this article. [Add the SharePoint documents tab to the main form for an entity](../maker/model-driven-apps/add-documents-tab-entity-main-form.md)  
