---
title: "How to: Use the getContext API (preview)"
description: "Use the getContext API to get information about the app and signed-in user. This information enables apps to deliver personalized experiences and make informed decisions at runtime based on metadata."
ms.author:  jordanchodak
author: jordanchodakWork
ms.date: 10/14/2025
ms.reviewer: jdaly
ms.topic: how-to
contributors:
- JimDaly
---

# How to: Use the getContext API (preview)

The `getContext()` API retrieves contextual information about the app and the signed-in user. This information enables apps to deliver personalized experiences and make informed decisions at runtime based on metadata. The API communicates with the web player to obtain context data and is designed to be lightweight. It focuses on metadata and authentication-related properties.

## Steps

1. Import the `getContext` API

   ```typescript
   import { initialize, getContext } from '@microsoft/power-apps/app'; 
   ```

1. Initialize

   You must call and wait for `initialize()` to be done before making any data calls to ensure that the SDK is fully initialized.

   ```typescript
   await initialize(); 
   ```

1. Retrieve context

   Call `getContext()` as an asynchronous function to get the context object.

   ```typescript
   const ctx = await getContext();
   ```

## API Response

The context returned is an [IContext](#icontext) type.

### IContext

The following table describes the properties available in the `IContext` object:

|Property|Type|Description|
|---|---|---|
| `app` | [IAppContext](#iappcontext) | The app's context |
| `user` | [IUserContext](#iusercontext) | The user's context |
| `host` | [IHostContext](#ihostcontext) | The host's context |

### IAppContext

The following table describes the properties available in the `IAppContext` object:

|Property|Type|Description|
|---|---|---|
| `appId`| string | The ID of the app being played |
| `environmentId`| string | The ID of the environment where the app lives |
| `queryParams` | Record<string, string> | The query parameters added to the URL |

### IUserContext

The following table describes the properties available in the `IUserContext` object:

|Property|Type|Description|
|---|---|---|
| `fullName` | string | The full name of the user playing the app |
| `objectId` | string | The ID of the user playing the app |
| `tenantId` | string | The ID of the tenant where the app lives |
| `userPrincipalName` | string | The UPN of the user playing the app |

### IHostContext

The following table describes the property available in the `IHostContext` object:

|Property|Type|Description|
|---|---|---|
| `sessionId` | string | The ID of the current session. This changes every time the app is opened |
