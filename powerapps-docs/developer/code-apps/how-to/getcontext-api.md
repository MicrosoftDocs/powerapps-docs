---
title: "How to: Use the getContext API (preview)"
description: "Use the getContext API to get information about the app and signed-in user. This information enables apps to deliver personalized experiences and make informed decisions at runtime based on metadata."
ms.author:  jordanchodak
author: jordanchodakWork
ms.date: 10/15/2025
ms.reviewer: jdaly
ms.topic: how-to
contributors:
- JimDaly
---

# Why use `getContext`? (preview)

The `getContext` API provides rich details about the app and the user, enabling scenarios that go beyond basic app functionality. Here's why these properties matter:

- **Enhanced Telemetry and Debugging**: Parameters like `sessionId` allow you to correlate app sessions with platform telemetry, making it easier to troubleshoot issues. Access to identifiers such as [IAppContext.appId](#iappcontext) and [IUserContext.userPrincipalName](#iusercontext) helps track usage patterns and diagnose problems quickly.

- **Personalized Experiences**: User context properties simplify personalization without requiring additional data calls. You can tailor app behavior based on user identity, delivering dynamic experiences for different roles or individuals.

- **Feature Control and Conditional Logic**: Parameters can act as feature gates or flags, enabling you to turn features on or off for specific users or environments. They can also be used to show different UI elements or workflows depending on the context.

- **Consistency with Canvas Apps**: These parameters align with session details available in canvas apps, but now you can use them directly in code, unlocking more flexibility.

# How to: Use the `getContext` API

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

The context returned implements the [IContext](#icontext) interface.

### IContext

The following table describes the properties available in the `IContext` interface:

|Property|Type|Description|
|---|---|---|
| `app` | [IAppContext](#iappcontext) | The app's context |
| `user` | [IUserContext](#iusercontext) | The user's context |
| `host` | [IHostContext](#ihostcontext) | The host's context |

### IAppContext

The following table describes the properties available in the `IAppContext` interface:

|Property|Type|Description|
|---|---|---|
| `appId`| string | The ID of the app being played |
| `environmentId`| string | The ID of the environment where the app lives |
| `queryParams` | Record<string, string> | The query parameters added to the URL |

### IUserContext

The following table describes the properties available in the `IUserContext` interface:

|Property|Type|Description|
|---|---|---|
| `fullName` | string | The full name of the user playing the app |
| `objectId` | string | The ID of the user playing the app |
| `tenantId` | string | The ID of the tenant where the app lives |
| `userPrincipalName` | string | The UPN of the user playing the app |

### IHostContext

The following table describes the property available in the `IHostContext` interface:

|Property|Type|Description|
|---|---|---|
| `sessionId` | string | The ID of the current session. This changes every time the app is opened |
