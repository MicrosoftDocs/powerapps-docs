---
title: "getContext API"
description: "Use the getContext API for information about the app and signed-in user"
ms.author:  jordanchodak
author: jordanchodakWork
ms.date: 10/13/2025
ms.reviewer: 
ms.topic: how-to
contributors:

---

# How to: Use the getContext API (preview)

The getContext() API retrieves contextual information about the app and the signed-in user. This enables apps to deliver personalized experiences and make informed decisions at runtime based on metadata. The API communicates with the web player to obtain context data and is designed to be lightweight, focusing on metadata and authentication-related properties.

## Steps

1. Import the getContext API

```powershell
import { initialize, getContext } from ‘@microsoft/power-apps/app’; 
```

2. Initialize 
You must call and wait for initialize() to be done before making any data calls to ensure that the SDK is fully initialized. 

```typescript
await initialize(); 
```

3. Retrieve context
Call getContext() as an asynchronous function to get the context object. 

```typescript
const ctx = await getContext();
```
		
## API Response

|Property|Type|Description|
|---|---|---|
| IContext.app | IAppContext | The app's context |
| IContext.user | IUserContext | The user's context |
| IContext.host | IHostContext | The host's context |
| IAppContext.appId | string | The ID of the app being played |
| IAppContext.environmentId | string | The ID of the environment where the app lives |
| IAppContext.queryParams | Record<string, string> | The query parameters added to the URL |
| IUserContext.fullName | string | The full name of the user playing the app |
| IUserContext.objectId | string | The ID of the user playing the app |
| IUserContext.tenantId | string | The ID of the tenant where the app lives |
| IUserContext.userPrincipalName | string | The UPN of the user playing the app |
| IHostContext.sessionId | string | The ID of the current session. This will change every time the app is opened |
 
