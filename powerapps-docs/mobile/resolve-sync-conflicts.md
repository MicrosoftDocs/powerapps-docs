---

title: Resolve sync conflicts with the server
description: Learn how to resolve sync conflicts with the server.
author: trdehove
ms.component: pa-user
ms.topic: quickstart
ms.date: 05/13/2024
ms.subservice: mobile
ms.author: trdehove
ms.reviewer: sericks
ms.assetid: 
search.audienceType: 
  - enduser
searchScope:
  - "Power Apps"
---

# Resolve sync conflicts with the server

## The Sync Error table
In the event of a synchronization error, the system will automatically generate a new entry in the **Sync Error** table within Dataverse. This table is structured with the following columns:

|Column name | Description | Example |
|-------------------------------|----------------------------|--------------------------------|
|**Error Time**| Time when the error was created | 5/17/2024 7:16 AM |
|**Error Message**| Description of the error | Entity Account With Id = <RowId> Does Not Exist|
|**Error Type**| Type of the error (Conflict, Record Not Found, Others)| Record not found|
|**Record**| Updated Record in sync error | Contoso |
|**Owner**| User who updated the Record| John Doe|
|**Action**|Action applied to the Record to sync| Update|
|**Action Data**|Json containing the payload of the Action| {"lastname":"Contoso2"}|
|**Request Data**|Json containing the query | {"lastname":"Contoso2","syncerror__regardingentityid":<syncerrorId>,"entitylogicalname":"account"}|
|**Error Code**| Code of the error| -2147015424 |
  

## Recommendation on how to use the Sync Error table
The sync Error table is a standard Dataverse table. We recommend to create a [model-driven app](/power-apps/maker/model-driven-apps/create-model-driven-app) to manage the sync errors. 

If you run the model-driven app, you will able to see the sync error by users. If you select a sync error row, you can **Retry changes** from the command bar. 

### Sync error in the Device Status page
Sync errors natively show up in the Device status page. The device status page is available [out-of-the-box in model-driven apps](offline-sync-icon.md) but must be [configured in canvas apps](canvas-mobile-offline-setup.md#create-an-offline-canvas-app). 

### Use Flow to take actions on sync errors
you can create an [automated cloud flow](/power-automate/get-started-logic-flow) in Power Automate using the Dataverse trigger **when a row is added, modified or deleted**. The flow can automatically [send an email](/power-automate/email-customization) or [send a notification](power-apps-mobile-notification.md) on the device.

> [!Note]
> To retrieve the user’s email address within the flow, add the Dataverse action **Get a row by ID** using the **Owner** column of the **Sync Error** row.  


## Sync conflict

### How sync conflicts are resolved ? 
When a user makes changes to data in an offline app, updates to each column are pushed back to Dataverse as soon as the network is available. The last update to each column is stored in Dataverse, so this sync doesn't fail due to conflicting changes.

Server-side plug-ins and validation can invalidate changes. Those changes are reverted locally, and an error is written to the **Sync Errors** Dataverse table.

### conflict resolution settings

