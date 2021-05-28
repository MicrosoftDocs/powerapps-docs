---
title: "getGlobalContext.client (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the getGlobalContext method.
ms.date: 04/21/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 89123cde-7c66-4c7d-94e4-e287285019f8
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# getGlobalContext.client (Client API reference)



Provides access to the methods to determine which client is being used, whether the client is connected to the server, and what kind of device is being used.

`var clientContext = Xrm.Utility.getGlobalContext().client`

The following methods are available for the client context.

## getClient

Returns a value to indicate which client the script is executing in. 

### Syntax

`clientContext.getClient()`

### Return Value

**Type**: String

**Description**: The values returned are:

Value |Client | 
|---|---|
|Web |Web application|
|Web |Unified Interface|
|Outlook |Dynamics 365 for Outlook client (COM add-in)|
|Mobile |Mobile app |
|||

## getClientState

Returns a value to indicate the state of the client.

### Syntax

`clientContext.getClientState()`

### Return Value

**Type**: String

**Description**: The values returned are:

Value |Client | 
|---|---|
|Online |Web application, Dynamics 365 for Outlook client (COM add-in), Mobile app, Unified Interface|
|Offline |Outlook, Mobile app|
|||

## getFormFactor

Returns information about the kind of device the user is using.

### Syntax

`clientContext.getFormFactor()`

### Return Value

**Type**: Number

**Description**: The values returned are:

Value |Form Factor | 
|---|---|
|0 |Unknown|
|1 |Desktop|
|2 |Tablet |
|3 |Phone |

## isOffline

Returns information whether the server is online or offline.

### Syntax

`clientContext.isOffline()`

### Return Value

**Type**: Boolean

**Description**: **true** if the server is offline; **false** otherwise.

## isNetworkAvailable

Returns information whether the network is available or not.

### Syntax

`clientContext.isNetworkAvailable()`

### Return Value

**Type**: Boolean

**Description**: **true** if the network is available; **false** otherwise.

## Related topics

[Organization Settings](organizationSettings.md)

[User Settings](userSettings.md)

[Xrm.Utility.getGlobalContext](../getGlobalContext.md)



[!INCLUDE[footer-include](../../../../../../includes/footer-banner.md)]