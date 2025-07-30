---
title: "Xrm.WebApi (Client API reference) in model-driven apps"
description: "Provides properties and methods to use Web API to create and manage records and execute Web API actions and functions in model-driven apps."
author: sriharibs-msft
ms.author: srihas
ms.date: 11/18/2022
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
ms.subservice: mda-developer
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# Xrm.WebApi (Client API reference)

Provides properties and methods to use Web API to create and manage records and execute Web API actions and functions in model-driven apps. 

## Properties

|Property | Description |
|----- |-----|
|[online](xrm-webapi/online.md)|[!INCLUDE[xrm-webapi/includes/online-description.md](xrm-webapi/includes/online-description.md)]|
|[offline](xrm-webapi/offline.md)|[!INCLUDE[xrm-webapi/includes/offline-description.md](xrm-webapi/includes/offline-description.md)]|

## Methods

With mobile offline configured, the source for these records depends on the current client state. In offline mode, the source is the offline data store. In online mode, the source is the server. If the client is offline-first, the methods in [online](xrm-webapi/online.md) can be used to access tables and records that aren't part of the offline profile, as long as the client has network connectivity.

|Method | Description |
|------ |-------------|
|[createRecord](xrm-webapi/createRecord.md)|[!INCLUDE[xrm-webapi/includes/createRecord-description.md](xrm-webapi/includes/createRecord-description.md)]|
|[deleteRecord](xrm-webapi/deleteRecord.md)|[!INCLUDE[xrm-webapi/includes/deleteRecord-description.md](xrm-webapi/includes/deleteRecord-description.md)]|
|[retrieveRecord](xrm-webapi/retrieveRecord.md)|[!INCLUDE[xrm-webapi/includes/retrieveRecord-description.md](xrm-webapi/includes/retrieveRecord-description.md)]|
|[retrieveMultipleRecords](xrm-webapi/retrieveMultipleRecords.md)|[!INCLUDE[xrm-webapi/includes/retrieveMultipleRecords-description.md](xrm-webapi/includes/retrieveMultipleRecords-description.md)]|
|[updateRecord](xrm-webapi/updateRecord.md)|[!INCLUDE[xrm-webapi/includes/updateRecord-description.md](xrm-webapi/includes/updateRecord-description.md)]|
|[isAvailableOffline](xrm-webapi/isAvailableOffline.md)|[!INCLUDE[xrm-webapi/includes/isAvailableOffline-description.md](xrm-webapi/includes/isAvailableOffline-description.md)]|
|[execute](xrm-webapi/online/execute.md)|[!INCLUDE[xrm-webapi/online/includes/execute-description.md](xrm-webapi/online/includes/execute-description.md)]|
|[executeMultiple](xrm-webapi/online/executeMultiple.md)|[!INCLUDE[xrm-webapi/online/includes/executeMultiple-description.md](xrm-webapi/online/includes/executeMultiple-description.md)]|

### Related articles

[Use the Microsoft Dataverse Web API](../../../data-platform/webapi/overview.md)   
[Client API Xrm object](../clientapi-xrm.md)


[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
