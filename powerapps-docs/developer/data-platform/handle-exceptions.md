---
title: "Handle exceptions in a plug-in (Microsoft Dataverse) | Microsoft Docs" 
description: "Understand system behavior when a plug-in passes an exception back to the caller."
ms.custom: ""
ms.date: 04/30/2021
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: JimDaly
ms.author: pehecke
manager: kvivek
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Handle exceptions in plug-ins

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]

The way exceptions are managed in plug-ins depends on the type of plug-in step registration.

- Exceptions for synchronous plug-in steps will cancel and rollback the operation. You have the ability to control the message returned to the user.
- Exceptions for asynchronous plug-in steps will be logged and added to the **System Job** table, also known as the [AsyncOperation Table](reference/entities/asyncoperation.md).

<a name='cancelling-an-operation'></a>

## Cancelling the current operation

Within a synchronous plug-in one of the options you have is to reject the request. If the operation doesn't follow the rules enforced by your plug-in, you can simply throw an <xref:Microsoft.Xrm.Sdk.InvalidPluginExecutionException> exception and provide the reasons why the operation was rejected in the message.

Ideally, you should only cancel operations using synchronous plug-ins registered in the **PreValidation** stage. This stage *usually* occurs outside the main database transaction. Cancelling an operation before it reaches the transaction is highly desirable because the cancelled operation has to be rolled back. Rolling back the operation requires significant resources and has a performance impact on the system. Operations in the **PreOperation** and **PostOperation** stages are always within the database transaction.

Sometimes **PreValidation** stages will be within a transaction when they are initiated by logic in another operation. For example, if you create a task record in the **PostOperation** stage of the creation of an account, the task creation will pass through the event execution pipeline and occur within the **PreValidation** stage yet it will be part of the transaction that is creating the account table record. You can tell whether an operation is within a transaction by the value of the <xref:Microsoft.Xrm.Sdk.IExecutionContext>.<xref:Microsoft.Xrm.Sdk.IExecutionContext.IsInTransaction> property.

### How Model-driven apps handle synchronous plug-in exceptions

When you throw an <xref:Microsoft.Xrm.Sdk.InvalidPluginExecutionException> exception within a synchronous plug-in an error dialog with your message will be displayed to the user. If you don't provide a message, a generic error dialog will be shown to the user. If any other type of exception is thrown, the user will see an error dialog with a generic message and the exception message and stack trace will be written to the [PluginTraceLog Table](reference/entities/plugintracelog.md).

> [!NOTE]
> In Unified Interface, the error dialog does not support HTML encoded content in the message. Text only please.

## Unexpected errors

However, when any exception occurs in the plug-in code for a synchronous step, the operation will be cancelled and rolled back whether you throw an `InvalidPluginExecutionException` or not. `InvalidPluginExecutionException` is the only exception that provides you with the ability to control what exception message will be displayed to the user. This is particularly true in the case of model-driven apps used by Dynamics 365 solutions.

> [!TIP]
> We recommend that you catch any error and throw an `InvalidPluginExecutionException` exception so you can control what is displayed to the user. This may simply be "`An unexpected error occurred`", but you could also add some information that will help the administrator troubleshoot the issue. This way, you have some control. If you allow other types of exceptions to bubble up, the error will be presented as an `IsvUnExpected` error with the message `An unexpected error occurred from ISV code.`, which is not very helpful.


## How Asynchronous plug-ins exceptions are handled

The exception message for asynchronous registered plug-ins is written to a **System Job** table, also known as the [AsyncOperation Table](reference/entities/asyncoperation.md)  which can be viewed in the **System Jobs** area of the web application. No dialog will be displayed to the user. Async plug-ins do not participate in the database transaction that queued them, therefore they cannot cancel the transaction.

### Retry an asynchronous plug-in

With an asynchronous plug-in step, you can re-try when a plug-in fails. This may be due to a network error or some other re-triable error calling an external resource. 

To retry your plug-in, use the [InvalidPluginExecutionException(OperationStatus, Int32, String)](/dotnet/api/microsoft.xrm.sdk.invalidpluginexecutionexception.-ctor?view=dynamics-general-ce-9#Microsoft_Xrm_Sdk_InvalidPluginExecutionException__ctor_Microsoft_Xrm_Sdk_OperationStatus_System_Int32_System_String_) constructor using the [OperationStatus Enum](/dotnet/api/microsoft.xrm.sdk.operationstatus?view=dynamics-general-ce-9) `Retry` member value.

When your plug-in throws this type of exception, the asynchronous service will attempt to run your plug-in four times. If it doesn't succeed within four attempts it will fail.


[!INCLUDE[footer-include](../../includes/footer-banner.md)]