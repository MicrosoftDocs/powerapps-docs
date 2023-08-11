---
title: "getGlobalContext.client (Client API reference) in model-driven apps| MicrosoftDocs"
description: "Describes the client object returned from the getGlobalContext method."
author: adrianorth
ms.author: aorth
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
contributors:
  - JimDaly
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

Returns a value to indicate the state of the client. A client in offline-first mode (in preview) always indicates it's offline.

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

Returns information whether the client state is online or offline. A client in offline-first mode always reports it's offline.

### Syntax

`clientContext.isOffline()`

### Return Value

**Type**: Boolean

**Description**: **true** if the server is offline; **false** otherwise.

## isNetworkAvailable

Returns information whether the network is available or not, regardless of client mode.

[!INCLUDE [online-only-api-note](../../../includes/online-only-api-note.md)]

### Syntax

`clientContext.isNetworkAvailable()`

### Return Value

**Type**: Boolean

**Description**: **true** if the network is available; **false** otherwise.

## Related articles

[Organization Settings](organizationSettings.md)

[User Settings](userSettings.md)

[Xrm.Utility.getGlobalContext](../getGlobalContext.md)



[!INCLUDE[footer-include](../../../../../../includes/footer-banner.md)]
