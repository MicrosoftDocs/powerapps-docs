---
title: "Use OneDrive for Business| MicrosoftDocs"
ms.custom: ""
author: mduelae
manager: kvivek
ms.service: powerapps
ms.component: pa-user
ms.topic: conceptual
ms.date: 02/26/2020
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
# Use OneDrive for Business 

With [!INCLUDE[pn_crm_online_shortest](../includes/pn-crm-online-shortest.md)], you can use the right storage option for the right situation. For example, you can store your private documents by using the new [!INCLUDE[pn_onedrive_for_business](../includes/pn-onedrive-for-business.md)] option. For collaborative storage, you can use [!INCLUDE[pn_office_365_groups](../includes/pn-office-365-groups.md)] and for public documents use [!INCLUDE[pn_SharePoint_short](../includes/pn-sharepoint-short.md)].  

 You might use [!INCLUDE[pn_onedrive_for_business](../includes/pn-onedrive-for-business.md)] to start and work on a document privately, such as for a draft sales pitch. When the draft is far enough along, move it to an [!INCLUDE[pn_Office_365](../includes/pn-office-365.md)] group for team collaboration. You have lots of storage space (1 TB or more) with [!INCLUDE[pn_onedrive_for_business](../includes/pn-onedrive-for-business.md)], and documents stored there are automatically synced to your desktop and mobile devices. For example, if you put a presentation in Customer Engagement (on-premises) that's stored on [!INCLUDE[pn_onedrive](../includes/pn-onedrive.md)] linked with an opportunity, that presentation is synced to all devices running [!INCLUDE[pn_onedrive](../includes/pn-onedrive.md)].  


 Before you can use [!INCLUDE[pn_onedrive_for_business](../includes/pn-onedrive-for-business.md)], it must be enabled by your system administrator. [!include[](../includes/proc-more-information.md)]  

-   [Find your Dynamics 365 Customer Engagement administrator or support person](../basics/find-administrator-support.md)  

-   [Enable OneDrive for Business](../admin/connect-onedrive-business.md)  

> [!IMPORTANT]
> [!INCLUDE[cc_feature_requires_office_365](../includes/cc-feature-requires-office-365.md)]  

## The first time you view your documents  

1. Go to the record for which you want to view the associated documents. For example, select **Sales** > **Leads**.

2. If you're using the web app, on the command bar, select the down arrow beside the record name, and then select **Documents**. 

   ![Navigate to related documents of a record](media/go-to-related-documents.png "Navigate to related documents for a record")

   If you're using a mobile-optimized app, select the **Related** tab, and then select **Documents**.

   ![Open the Documents tab in a record in a mobile-optimized app](media/open-documents-tab-in-form.png "Open the Documents tab in a record in a mobile-optimized app")

   After [!INCLUDE[pn_onedrive_for_business](../includes/pn-onedrive-for-business.md)] is enabled, you'll see the following dialog box when you go to the Document Associated Grid to view documents in Customer Engagement (on-premises) and upload a file to [!INCLUDE[pn_onedrive](../includes/pn-onedrive.md)], or when you attempt to create a new document or folder.  

   ![Change your OneDrive folder](../basics/media/onedrive-first-time.png "Change your OneDrive folder")  

   Select **Change folder location** to pick a new location to store [!INCLUDE[pn_onedrive](../includes/pn-onedrive.md)] documents, or select **Continue** to accept the default folder location: \Dynamics365. 

   > [!NOTE]
   >  The default folder location is set to \CRM for users who haven't upgraded to the [!include[](../includes/pn-crm-9-0-0-online.md)]. 

## View existing OneDrive documents  
 Open the Document Associated Grid. The following example is for Opportunities, but works the same for all record types.  

1. Select **Sales** > **Opportunities**  

2. Choose an opportunity from the drop-down menu, and then select **Documents**.  

    > [!div class="mx-imgBorder"] 
    > ![Create record button](media/newrecord1.png "Create record button")
  

    Customer Engagement (on-premises) now organizes documents in a consolidated view.  

    ![List of documents on OneDrive for Business](media/list-of-documents-in-onedrive.png "List of documents on OneDrive")

3. Select **Document Location** to filter the document list.  

     ![Choose a document location](../basics/media/onedrive-choose-document-location.PNG "Choose a document location")  

4. Select a location as described in the following table:  


   |                            Document Location                             |                                                                  Description                                                                   |
   |--------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
   |                                All files                                 | All document locations associated with this Customer Engagement (on-premises) record (only available in the web app) |
   | [!INCLUDE[pn_SharePoint_short](../includes/pn-sharepoint-short.md)] site |                   Documents stored in your default [!INCLUDE[pn_SharePoint_short](../includes/pn-sharepoint-short.md)] site                    |
   |           [!INCLUDE[pn_onedrive](../includes/pn-onedrive.md)]            |                       Documents stored in [!INCLUDE[pn_onedrive_for_business](../includes/pn-onedrive-for-business.md)]                        |
   |                              Shared with me                              |     Documents that others shared with you that are associated with this Customer Engagement (on-premises) record     |

## Create a new document  
 To create a new [!INCLUDE[pn_SharePoint_short](../includes/pn-sharepoint-short.md)] or [!INCLUDE[pn_onedrive](../includes/pn-onedrive.md)] document in Customer Engagement (on-premises):  

1. Go to the Document Associated Grid.  

2. Select **Document Location**, and change the location to **OneDrive**.

3. Select **New**, and then choose a document type such as [!INCLUDE[pn_MS_Powerpoint](../includes/pn-ms-powerpoint.md)] or [!INCLUDE[pn_ms_Word_short](../includes/pn-ms-word-short.md)].  

4. Enter a document name, and then select **Save**.  

   The document is created and opened in the [!INCLUDE[pn_Office_365](../includes/pn-office-365.md)] Online application.  


> [!NOTE]
> If you're are using the mobile-optimized app on tablets and phones, the document is opened within the Office app such as [!INCLUDE[pn_MS_Powerpoint](../includes/pn-ms-powerpoint.md)] or [!INCLUDE[pn_ms_Word_short](../includes/pn-ms-word-short.md)].

## Change your OneDrive folder settings (web app only)
 You can change the location of your [!INCLUDE[pn_onedrive](../includes/pn-onedrive.md)] documents and rename the folder used for [!INCLUDE[pn_onedrive](../includes/pn-onedrive.md)].  

1. Select **Settings** > **Document Management** > **OneDrive for Business Folder Settings**.  

2. Enter a new location for Customer Engagement (on-premises) to store [!INCLUDE[pn_onedrive](../includes/pn-onedrive.md)] files, and then select **OK**.  

   > [!NOTE]
   >  The [!INCLUDE[pn_onedrive](../includes/pn-onedrive.md)] folder is renamed, and all existing files will now be associated with the new folder.  

## Things to consider  
 Be aware of the following regarding [!INCLUDE[pn_onedrive_for_business](../includes/pn-onedrive-for-business.md)] in Customer Engagement (on-premises):  

- [!INCLUDE[pn_onedrive](../includes/pn-onedrive.md)] storage folders are created in the user's current Customer Engagement (on-premises) language. If the language changes, new folders will be created in the new language. Old folders will remain in the previous language.  

- There may be a delay between when the documents are shared in [!INCLUDE[pn_onedrive](../includes/pn-onedrive.md)] and when they're available to other users.  
