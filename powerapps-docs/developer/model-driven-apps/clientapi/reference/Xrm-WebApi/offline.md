---
title: "Xrm.WebApi.offline (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the Xrm.WebApi.offline method.
ms.date: 04/21/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 848c277b-bd44-4388-852a-0f59a3a15538
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Xrm.WebApi.offline (Client API reference)



[!INCLUDE[./includes/offline-description.md](./includes/offline-description.md)] 

For information about the mobile offline feature, see  [Configure mobile offline synchronization to allow users to work in offline mode on their mobile device](/dynamics365/customer-engagement/mobile-app/configure-mobile-offline-synchronization-dynamics-365-phones-tablets)

`var offlineWebApi = Xrm.WebApi.offline;`

> [!NOTE]
> Use **Xrm.WebApi.offline** instead of the [deprecated](/dynamics365/get-started/whats-new/customer-engagement/important-changes-coming#some-client-apis-are-deprecated) **Xrm.Mobile.Offline** namespace to create and manage records in the mobile clients while working in the offline mode.

The **offlineWebApi** object provides the following methods. When in the offline mode, these methods will work only for tables that are enabled for mobile offline synchronization and available in current user’s mobile offline profile.

- [createRecord](createRecord.md)
- [deleteRecord](deleteRecord.md)
- [isAvailableOffline](isAvailableOffline.md)
- [retrieveRecord](retrieveRecord.md)
- [retrieveMultipleRecords](retrieveMultipleRecords.md)
- [updateRecord](updateRecord.md)

> [!IMPORTANT]
> While creating or updating record in the offline mode, only basic validation is performed on the input data. Basic validation includes things such as ensuring that the table column name specified is in lower case and does exist for a table, checking for data type mismatch for the specified column value, preventing records getting created with the same GUID value, checking whether the related table is offline enabled when retrieving related table records, and validating if the record that you want to retrieve, update, or delete actually exists in the offline data store. Business-level validations happen only when you are connected to the server and the data is synchronized. A record is created or updated only if the input data is completely valid.

### Related topics

[Xrm.WebApi.online](online.md)

[Xrm.WebApi](../xrm-webapi.md)





[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]