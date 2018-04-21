---
title: DSR guide for customer-authored data | Microsoft Docs
description: PowerApps DSR guide for customer-authored data
services: powerapps
suite: powerapps
documentationcenter: na
author: jamesol-msft
manager: kfile
editor: ''
tags: ''

ms.service: powerapps
ms.devlang: na
ms.topic: article
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 04/17/2018
ms.author: paulliew

---

# Responding to Data Subject Rights (DSR) requests for customer data in Common Data Service for Apps

## Introduction to DSR requests
The European Union (EU) General Data Protection Regulation (GDPR) gives rights to people (known in the regulation as *data subjects*) to manage the personal data that's been collected by an employer or other type of agency or organization (known as the *data controller* or just *controller*). Personal data is defined very broadly under the GDPR as any data that relates to an identified or identifiable natural person. The GDPR gives data subjects the right to do the following, as it pertains to their personal data:
 
* Obtain copies
* Request corrections
* Restrict processing
* Delete it
* Receive it in electronic format so it can be moved to another controller

A formal request by a data subject to a controller to take an action on his or her personal data is called a Data Subject Rights (DSR) request.

This article describes how Microsoft is preparing for the GDPR, and also provides examples of steps you can take to support GDPR compliance when using PowerApps, Microsoft Flow, and Common Data Service (CDS) for Apps. You'll learn how to use Microsoft products, services, and administrative tools to help controller customers find, access, and act on personal data in the Microsoft cloud in response to DSR requests.

The following actions are covered in this article:

* **Discover** — Use search and discovery tools to more easily find customer data that may be the subject of a DSR request. Once potentially responsive documents are collected, you can perform one or more of the following DSR actions to respond to the request. Alternatively, you may determine that the request doesn't meet your organization’s guidelines for responding to DSR requests.

* **Access** — Retrieve personal data that resides in the Microsoft cloud and, if requested, make a copy of that data available to the data subject.

* **Rectify** — Make changes or implement other requested actions on the personal data, where applicable.

* **Restrict** — Restrict the processing of personal data, either by removing licenses for various online services or turning off the desired services where possible. You can also remove data from the Microsoft cloud and retain it on-premises or at another location.

* **Delete** — Permanently remove personal data that resides in the Microsoft cloud.

* **Export** — Provide an electronic copy (in a machine-readable format) of personal data to the data subject.

##CDS for Apps customer data

> [!IMPORTANT]
> Applies to both CDS for Apps and the previous version of Common Data Service

CDS for Apps and the previous version of Common Data Service (CDS) have separate processes for interacting with personal data.

You can identify which type of CDS environment you have by logging into [PowerApps](https://web.powerapps.com) and following these steps:

1. In the **Environment** drop-down list, select your environment.
2. In the navigation pane, click or tap **Data**, and then click or tap **Entities**.

    Your environment is CDS for Apps if you see the following entities listed:

    ![PowerApps Entities list](./media/common-data-service-gdpr-dsr-guide/powerapps-entities-list.png)

    Your environment is the previous version of CDS if you see the following entities listed:

    ![PowerApps Legacy Entities list](./media/common-data-service-gdpr-dsr-guide/powerapps-legacy-entities-list.png)

After you determine which type of CDS environment you have, follow the steps in the following sections to identify personal data.

> [!NOTE]
> You may have some environments in CDS for Apps and others in the previous version of CDS, so you'll need to repeat the processes outlined below for each environment in your organization.

## User personal data in CDS for Apps

### Prerequisites
You must create users in the Office 365 Admin Center and assign them an appropriate user license and security role before they can access and use CDS for Apps.

Standard user personal data (for example, UserName, UserID, Phone, Email, and Address) is kept and maintained in the Office 365 Admin Center. System administrators can update this personal data only in the Office 365 Admin Center, and the data is then automatically synced to the CDS for Apps system User entity in all environments. System administrators can also create custom attributes to capture additional user personal data within the CDS for Apps system User entity, and then manually maintain and manage these attributes.

To avoid interruption to business applications that may be critical to your organization’s operations, a user's records are not automatically removed from the CDS for Apps system User entity when that user is deleted within the Office 365 Admin Center. A CDS for Apps system administrator will need to locate and remove the user's personal data from CDS for Apps within the application.

Only Office 365 Global Administrators and CDS System Administrators can perform the discover, rectify, export, and delete actions listed below.

### Discover

System Administrators can create multiple CDS for Apps instances. These instances can be used for trial, development, or production purposes. Each of these instances has a copy of the system User entity with any custom attributes that may have been added by the system administrator, as well as the user personal data synced from the Office 365 Admin Center.

System administrators can find a list of all the CDS for Apps instances by navigating to the Dynamics 365 Administration Center from the PowerApps Admin Center.

From the [PowerApps admin center](https://admin.powerapps.com/), do the following:

1. In the navigation pane, click or tap **Environments**, and then select an environment from the list.

3.	Click or tap **Dynamics 365 Administration Center**.

    ![PowerApps Environment Details](./media/common-data-service-gdpr-dsr-guide/powerapps-environment-details.png)

    A list of all the instances displays.

    ![PowerApps Instance Picker](./media/common-data-service-gdpr-dsr-guide/powerapps-instance-picker.png)

You can find personal data from CDS for Apps users within the following resources:

|Resource | Purpose | Website access | Programmatic access
| --- | --- | --- | ---
| Entity record | Known as the system User entity, it stores a user's personal data | [PowerApps Admin Center](https://admin.powerapps.com) | Through the [Web API](https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/webapi/update-delete-entities-using-web-api#basic-update)
| Audit history | Allows customers to identify resources that users created, accessed, changed, or deleted at an entity level. | [PowerApps Admin Center](https://admin.powerapps.com) | Through the [Web API](https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/webapi/update-delete-entities-using-web-api#basic-update)

#### User
User personal data is stored in the Azure Active Directory and is automatically synced to all CDS for Apps environments. System administrators cannot update this personal data directly in CDS for Apps while the user is active&mdash;they must update the data from within the Office 365 Administration Center. System administrators can add personal data (for example, custom attributes) directly to CDS for Apps, but they must manually manage this data.

To find a user and his or her personal data, go to the [PowerApps Admin Center](https://admin.powerapps.com/) and do the following:

1. In the navigation pane, click or tap **Environments**, and then select an environment from the list.
2. Click or tap **Dynamics 365 Administration Center**, select an environment from the list, and then click or tap **Open**.
3. Go to **Settings** > **Security** > **Users**.
4. Enter the name of the user in the **Search** box, and then click or tap **Search**.
5. To view the user's personal data, double-click or double-tap the user's name.

    ![PowerApps User Form](./media/common-data-service-gdpr-dsr-guide/powerapps-user-form.png)

#### Audit history
When [audit tracking](https://docs.microsoft.com/dynamics365/customer-engagement/admin/audit-data-user-activity) is enabled for an entity in CDS for Apps, a user's personal data is logged in the audit history along with the actions that the user performs.

### Rectify
If a data subject asks you to rectify the personal data that resides in your organization’s data, you and your organization must determine whether it’s appropriate to honor the request. Rectifying data may include editing, redacting, or removing personal data from a document or other type of item.

You can use Azure Active Directory to manage the identities (personal data) of your users within CDS for Apps. Enterprise customers can manage DSR rectify requests by using the limited editing features within a given Microsoft service. As a data processor, Microsoft does not offer the ability to correct system-generated logs, because they reflect factual activities and constitute a historical record of events within Microsoft services. See [GDPR: Data Subject Requests (DSRs)](https://servicetrust.microsoft.com/ViewPage/GDPRDSR) for details.

Once a user record is deleted from Azure Active Directory, System Administrators can then remove any remaining personal data related to that user (such as custom attributes) from all the instances.  

### Export

#### System user
You can export a user's personal data stored in the system User entity to Excel from the user list within the administration center.

From the [PowerApps Admin Center](https://admin.powerapps.com/), do the following:

1. In the navigation pane, click or tap **Environments**, and then select an environment from the list.

2. Click or tap **Dynamics 365 Administration Center**, select an environment from the list, and then click or tap **Open**.

3. Go to **Settings** > **Security**, and then select **Enabled Users View**.
 
4. Click **Export to Excel**.

#### Audit history
You can take screenshots of the audit history from within the adminisration center.

From the [PowerApps Admin Center](https://admin.powerapps.com/), do the following:

1. In the navigation pane, click or tap **Environments**, and then select an environment from the list.

2. Click or tap **Dynamics 365 Administration Center**, select an environment from the list, and then click or tap **Open**.

3. Go to **Settings** > **Auditing**, and then select **Audit Summary View**. 

    ![PowerApps Audit History Menu](./media/common-data-service-gdpr-dsr-guide/powerapps-audit-history-menu.png)

4. Locate the user audit record, and then press Alt+PrtScn to take the screenshot.

    ![PowerApps Audit History Details](./media/common-data-service-gdpr-dsr-guide/powerapps-audit-history-details.png)

5. Save the screen shot to a file, which you can then send to the DSR requestor.

### Delete

#### User
When a user is deleted from Office 365 Admin Center, the user’s status is set to Disabled in CDS; however the user personal data is not automatically deleted to avoid interruption to business applications that may be critical to your organization’s operations.
To delete the user personal data from CDS, the System Administrator is required to manually remove the personal data of the disabled user.

#### Remove user personal data via user form
When the user record is deleted from Azure Active Directory, the following message is displayed on the user form.
This user’s information is no longer managed by Office 365. You can update this record to respond to DSR requests by removing or replacing all personal data associated with this user.

From the [PowerApps admin center](https://admin.powerapps.com/),
1.	Navigate to the Environments tab.
2.	From the list of Environments, select an Environment.
3.	Click on the Dynamics 365 Administration Center link.
4.	Click on the Name of the environment.
5.	Click the **Open** button.
6.	Click **Settings** > **Security** > **Users**.
7.	Select **Disabled Users** view.
8.	Enter user name in the **Search for records** and click the **Search** button.
9.	Double-click on the user name from the search results.
10.	Remove all the personal data and click **Save**.

#### Remove user personal data via Excel import/export
1.	Click **Settings** > **Security** > **Users**.
2.	Select **Disabled Users** view.
3.	Create an Excel template with all the user personal data columns that you want to update.
4.	Click on **Download File**
5.	Open the downloaded Excel file, make your updates, and save the file.
6.	Return to the Disabled Users view window and click Import Data.
7.	Choose your updated Excel in the Upload data file dialog box.
8.	Make all the necessary changes on the Map Fields window.
9.	Click Next and Submit.

See [additional Excel info](https://docs.microsoft.com/en-us/dynamics365/customer-engagement/admin/analyze-your-data-with-excel-templates) on using Excel templates.


#### Remove audit history via the Audit Summary View form

From the [PowerApps admin center](https://admin.powerapps.com/),
1.	Navigate to the Environments tab.
2.	From the list of Environments, select an Environment.
3.	Click on the Dynamics 365 Administration Center link.
4.	Click on the Name of the environment.
5.	Click the Open button.
6.	Click Settings > Auditing.
7.	Select Audit Summary view.
8.	Locate the Change History performed by the user
9.	Click the CheckBox on the row(s).
10.	Click the Delete Change History icon.

## Personal data stored in Common Data Service for Apps databases

### Prerequisites
You may be storing personal data from individuals (such as your own customers) in the content of your CDS entities.  

When an individual submits a DSR request to your organization, the CDS system administrator will need to locate all the entities that the individual might be referenced in within your application.  The CDS administrator is responsible for maintaining an inventory of where personal data is being stored within various entities you are using so that you can respond to DSR requests from individuals.

Personal data within your content can then be exported, rectified, or deleted in an entity using the in-product functionality.  

### Discover
When a CDS administrator receives a DSR request from an individual, the administrator will need to identify which Environments/CDS instances contain personal data from that individual.  You should develop policies and procedures for maintaining an inventory of environments, instances, and entities where you have decided to store personal data from individuals to help you identify personal data you’ve stored within your content.

Using the inventory of environments, instances, entities and fields where personal data is stored, you can configure the CDS Search engine to discover the personal data.  A CDS administrator can configure the search entities and fields – see [Configure Relevance Search](https://go.microsoft.com/fwlink/?linkid=872506) for details.
The CDS administrator can then access the CDS environment and perform a search.

1.	Click on the **Search** icon.
2.	Select **Relevance Search**

    ![PowerApps Relevance Search Menu](./media/common-data-service-gdpr-dsr-guide/powerapps-relevance-search-menu.png)

3.	Enter the individual’s personal data in the Search box.
4.	Click the Search button.

    ![PowerApps Relevance Search Results](./media/common-data-service-gdpr-dsr-guide/powerapps-relevance-search-results.png)

Personal data in your content is typically stored in the key entities, e.g. Account, Contact, Lead, Opportunity, etc., but it’s your responsibility to maintain an inventory of where you store personal data of individuals.

### Rectify
The CDS system administrator can update an individual’s personal data by using the list of results from the  Relevance Search.  However, you may have stored this individual’s personal data in other custom entities as well.  The CDS system administrator is responsible for maintaining an inventory of these other custom entities and making the appropriate update to the individual’s personal data.

From the Relevance Search results:

1.	Click on an item that the individual personal data was found.
2.	Update individual personal data where appropriate.
3.	Click Save

    ![PowerApps Account details](./media/common-data-service-gdpr-dsr-guide/powerapps-account-details.png)

### Export
A screenshot of the data can be captured and shared with your DSR requestor by taking the steps outlined below.

From the [PowerApps admin center](https://admin.powerapps.com/),
1.	Navigate to the Environments tab.
2.	From the list of Environments, select an Environment.
3.	Click on the Dynamics 365 Administration Center link.
4.	Click on the Name of the environment.
5.	Click on the **Search** icon.
6.	Select Relevance Search.
7.	Enter the individual’s personal data in the Search box.
8.	Click the Search button.
9.	Locate the item and double-click on it.
10.	Press <alt> <PrtScn> to capture the screen shot.
11.	Save the screen shot to a file.
12.	You can then send the file to your DSR requestor.

### Delete

The CDS administrator can delete an individual’s personal data from records where that data is stored.  The CDS administrator can choose to either (1) delete the record where the personal data is stored or (2) remove the contents of the personal data from the record.  

> [!NOTE]
> A CDS administrator can customize the environment to prevent a record from being deleted from an entity. If configured in this way, you will have to remove the contents of the personal data from the record rather than deleting the record itself.

From the Relevance Search results,
1.	Click on an item that the individual personal data was found.
2.	Click on the Delete icon on the ribbon (note: this icon is disabled if the record cannot be deleted).

    ![PowerApps Account delete](./media/common-data-service-gdpr-dsr-guide/powerapps-account-delete.png)

## Personal data stored in Common Data Service (Previous Version) databases

### Prerequisites

You may be storing personal data from individuals (such as your own customers or users) in the content of your CDS entities.  

When an individual submits a DSR request to your organization, the CDS system administrator will need to locate all the entities that the individual might be referenced in within your application.  The CDS administrator is responsible for maintaining an inventory of where personal data is being stored within various entities you are using so that you can respond to DSR requests from individuals.

Personal data within your content can then be exported, rectified, or deleted in an entity using the in-product functionality.  

### Discover
When a CDS administrator receives a DSR request from an individual, the administrator will need to identify which Environments/CDS instances contain personal data from that individual.  You should develop policies and procedures for maintaining an inventory of environments, instances, and entities where you have decided to store personal data from individuals to help you identify personal data you’ve stored within your content.

Personal data from individuals can be found in the following:

|Resources containing personal data | Purpose |	Website access |	Programmatic access
| --- | --- | --- | ---
|Entity records	| To capture business transactions in respective business entity. | PowerApps Maker Portal |  	No

#### Entity records
Individual personal data can be stored in any business entity.
This version of the Common Data Service contains its own database schema and infrastructure.  It has its own entities and the management of these entities is managed using the [PowerApps site](http://web.powerapps.com/).

To see a list of your entities:

1.	Select the Environment

    ![PowerApps Legacy Entities](./media/common-data-service-gdpr-dsr-guide/powerapps-legacy-entities.png)

2.	Navigate to **Data** > **Entities** tab.
3.	Select the entity, eg Account entity.

    ![PowerApps Legacy Entities details list](./media/common-data-service-gdpr-dsr-guide/powerapps-legacy-entities-details-list.png)

4.	Click on the entity.
5.	Click on the **Data** tab.
A list of records for the entity  will be displayed.

    ![PowerApps Legacy Account data](./media/common-data-service-gdpr-dsr-guide/powerapps-legacy-account-data.png)

6.	Click on the **Export data** icon.
7.	Open the Excel worksheet when the export is complete.
8.	Click the Enable editing box.
9.	Click on the Find and Search icon.
10.	Enter the personal info you want search.
Personal data in your content is typically stored in the key entities, e.g. Account, Contact, Lead, Opportunity, Worker etc., but it’s your responsibility to maintain an inventory of where you store personal data of individuals.
11.	Using the inventory list of entities where personal data is stored, **repeat the above steps for each of the business entities to discover the individual personal data**.

### Rectify
If a data subject has asked you to rectify the personal data that resides in your organization’s data, you and your organization will have to determine whether it’s appropriate to honor the request.  Rectifying the data may include taking actions such as editing, redacting, or removing personal data from a document or other type or item.

You may use Azure Active Directory to manage identities (personal data) of your end users in Common Data Service for Apps. Enterprise customers have the ability to manage DSR rectify requests, including limited editing features per the nature of a given Microsoft service.  As a data processor, Microsoft does not offer the ability to correct system-generated logs as it reflects factual activities and constitutes a historical record of events within Microsoft services.  

Please see [GDPR: Data Subject Requests (DSRs)](https://servicetrust.microsoft.com/ViewPage/GDPRDSR) for details.

To rectify personal data that resides in the CDS environment, you can export the entity data into an Excel worksheet, update it and import the updates back to the database.
The CDS Administrator is responsible for identifying all the entities that the individual personal data is stored and repeating the below steps for each of those entities.

From the [PowerApps site](http://web.powerapps.com/):

1.	Click **Data** > **Entities**.
2.	Click on the entity, eg. Account.
3.	Click on the **Data** option.
4.	Click the **Export data** icon.
5.	Click the **Open in Excel** icon (when the export is done).
6.	**Enable Editing** on the Excel worksheet, and make update to the personal data.
7.	**Save** your updated worksheet (do a **Save As** so you know where the file is located).

    ![PowerApps Legacy Account data](./media/common-data-service-gdpr-dsr-guide/powerapps-legacy-account-data.png)

8.	Make the necessary personal data updates
9.	Save your updates
10.	On the Data > Entities > Account form, click on Import data icon.
11.	Click the Search box.
12.	Choose the file that contains your updates.
13.	Click the Open box.
14.	Click the Import button.

### Export

You can view and export personal data from each entity into an Excel worksheet.

From the [PowerApps site](http://web.powerapps.com/):

1.	Navigate to **Data** > **Entities**.
2.	Select the **Entity** you want to view and export the data.
3.	Click on the **Data** option.
4.	Click the **Export data** icon. This Export operation runs in the background and you will be notified when it’s done.
5. To view the exported data, click on the Open in Excel icon.

### Delete
You can delete  personal data that is stored in entities by using the Export/Import data functionality.

The CDS administrator is responsible for identifying all the entities that contain the individual personal data and repeating the following steps for each of the entities.

From the [PowerApps site](http://web.powerapps.com/):

1.	Click **Data** > **Entities**.
2.	Scroll down the **Entity** list and locate the entity you want to remove the personal data.
3.	Click on the entity.
4.	Click on the **Data** option.
5.	Click the **Export data** icon.
6.	Click the **Open in Excel** icon (when the export is done).
7.	**Enable Editing** on the Excel worksheet.
8.	**Save** your updated worksheet (do a Save As so you know where the file is located).
9.	Delete the row(s) of the personal data records that you want to remove.
10.	Save your updates
11.	On the **Entities** form, click on **Import data** icon.
12.	Click the **Search** box.
13.	Choose the file that contains your updates.
14.	Click the **Open** box.
15.	Click the Import button.
