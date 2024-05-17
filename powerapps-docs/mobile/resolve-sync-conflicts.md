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
When there is a synchronization error, the system will automatically create a row in the **Sync Error** Dataverse table. This table contains the following columns:
|Column name | Description | Example value|
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

### Sync error in the Device Status page

### Use Flow to take actions on sync errors

## Conflict Resolution

### How does the conflict resolution work? 

### conflict resolution settings

