---

title: Resolve sync conflicts with the server
description: Learn how to resolve mobile sync conflicts with the server.
author: trdehove
ms.component: pa-user
ms.topic: quickstart
ms.date: 06/13/2024
ms.subservice: mobile
ms.author: trdehove
ms.reviewer: smurkute
ms.assetid: 
search.audienceType: 
  - enduser
searchScope:
  - "Power Apps"
---

# Resolve sync conflicts with the server

This article provides information to help you resolve mobile synchronization conflicts with the server.

## Sync Error table
In the event of a synchronization error, the system automatically generates a new entry in the **Sync Error** table within Dataverse. This table is structured with the following columns.

|Column name | Description | Example |
|-------------------------------|----------------------------|--------------------------------|
|**Error Time**| Time when the error was created. | 5/17/2024 7:16 AM |
|**Error Message**| Description of the error. | `Entity Account With Id = <RowId> Does Not Exist`|
|**Error Type**| Type of the error, such as a conflict or record not found error.| Record not found|
|**Record**| Updated record in sync error.| Contoso |
|**Owner**| User who updated the record.| John Doe|
|**Action**|Action applied to the record to sync.| Update|
|**Action Data**|Json containing the payload of the action.| {"lastname":"Contoso2"}|
|**Request Data**|Json containing the query. | {`"lastname":"Contoso2","syncerror__regardingentityid":<syncerrorId>,"entitylogicalname":"account"}`|
|**Error Code**| Code of the error. | -2147015424 |

> [!Note]
> Make sure that the role assigned to the user grants read privileges on the **Sync Error** table. Learn more: [Create or edit a security role to manage access](/power-platform/admin/create-edit-security-role)

## Recommendation on how to use the Sync Error table
The **Sync Error** table is a standard Dataverse table. We recommend that you create a [model-driven app](/power-apps/maker/model-driven-apps/create-model-driven-app) to manage the sync errors. 

If you run the model-driven app, you can see the sync errors by each user. If you select a sync error row, you can **Retry changes** from the command bar. 

### Sync error in the Device status page
Sync errors natively show up in the **Device status** page. The **Device status** page is available [out of the box in model-driven apps](offline-sync-icon.md), but must be set up in the canvas app. See [Using the Offline template and offline status icon](canvas-mobile-offline-setup.md#using-the-offline-template-and-offline-status-icon) for more information. 

### Use a cloud flow to take actions on sync errors
You can create an [automated cloud flow](/power-automate/get-started-logic-flow) in Power Automate using the Dataverse trigger **when a row is added, modified, or deleted**. The flow can automatically [send an email](/power-automate/email-customization) or [send a notification](power-apps-mobile-notification.md) on the device.

> [!Note]
> To retrieve the user’s email address within the flow, add the Dataverse action **Get a row by ID** using the **Owner** column of the **Sync Error** row.  

## Sync conflict
When there's a mismatch of data between client and server, conflict errors occur. By default, changes that are made by a user in offline mode are automatically synced to the server when the user is back online. 

### How sync conflicts are resolved
When a user makes changes to data in an offline app, updates to each column are pushed back to Dataverse as soon as the network is available. The last update to each column is stored in Dataverse, so this sync doesn't fail due to conflicting changes.

Server-side plug-ins and validation can invalidate changes. Those changes are reverted locally, and an error is written to the **Sync Errors** Dataverse table.

### Conflict resolution settings

> [!Important]
> The conflict resolution settings don't apply to canvas apps.   

If updates made while offline are being rejected too frequently, consider changing the conflict resolution setting to its default value.  

1. Sign in to the [Power Platform admin center](https://admin.powerplatform.microsoft.com/).
1. Select **Environments** in the navigation pane.
3. Select an environment.
4. Select **Settings** in the command bar.
5. Select **Product** > **Features**.
6. In the **Advanced mobile offline settings for model-driven apps** section, turn off the **Enable conflict detection for mobile offline synchronization** option. 

> [!Note]
> When this option is turned on (not recommended), updates on the server may prevent client updates being applied. Conflict errors must be resolved manually.
