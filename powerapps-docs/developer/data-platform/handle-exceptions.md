---
title: "Handle exceptions in a plug-in (Microsoft Dataverse) | Microsoft Docs" 
description: "Understand system behavior when a plug-in passes an exception back to the caller."
ms.date: 02/05/2024
author: MsSQLGirl
ms.author: sriknair
ms.reviewer: pehecke
ms.topic: "article"
ms.subservice: dataverse-developer
search.audienceType: 
  - developer
contributors:
 - JimDaly
 - phecke
---
# Handle exceptions in plug-ins

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]

The way exceptions are managed in plug-ins depends on the type of plug-in step registration.

- Exceptions for synchronous plug-in steps cancel and roll back the operation. You have the ability to control the message returned to the user.
- Exceptions for asynchronous plug-in steps are logged and added to the **System Job** table, also known as the [AsyncOperation Table](reference/entities/asyncoperation.md).

<a name='cancelling-an-operation'></a>

## Cancelling the current operation

Within a synchronous plug-in, one of the options you have is to reject the request. If the operation doesn't follow the rules enforced by your plug-in, you can throw an <xref:Microsoft.Xrm.Sdk.InvalidPluginExecutionException> exception and provide the reasons why the operation was rejected in the message.

Ideally, you should only cancel operations using synchronous plug-ins registered in the **PreValidation** stage. This stage *usually* occurs outside the main database transaction. Cancelling an operation before it reaches the transaction is highly desirable because the canceled operation has to be rolled back. Rolling back the operation requires significant resources and has a performance impact on the system. Operations in the **PreOperation** and **PostOperation** stages are always within the database transaction.

Sometimes **PreValidation** stages are within a transaction when they're initiated by logic in another operation. For example, if you create a task record in the **PostOperation** stage of the creation of an account, the task creation passes through the event execution pipeline and occurs within the **PreValidation** stage, yet it's part of the transaction that is creating the account table record. You can tell whether an operation is within a transaction by the value of the <xref:Microsoft.Xrm.Sdk.IExecutionContext>.<xref:Microsoft.Xrm.Sdk.IExecutionContext.IsInTransaction> property.

### How Model-driven apps handle synchronous plug-in exceptions

When you throw an <xref:Microsoft.Xrm.Sdk.InvalidPluginExecutionException> exception within a synchronous plug-in, an error dialog with your message is displayed to the user. If you don't provide a message, a generic error dialog is shown to the user. If any other type of exception is thrown, the user sees an error dialog with a generic message and the exception message and stack trace are written to the [PluginTraceLog Table](reference/entities/plugintracelog.md).

> [!NOTE]
> In Unified Interface, the error dialog does not support HTML encoded content in the message. Text only please.

## Unexpected errors

However, when any exception occurs in the plug-in code for a synchronous step, the pipeline operation being processed in the database transaction is canceled and rolled back whether you throw an `InvalidPluginExecutionException` or not. `InvalidPluginExecutionException` is the only exception that provides you with the ability to control what exception message is displayed to the user. This is true if model-driven apps used by Dynamics 365 solutions.

Take a look at the available <xref:Microsoft.Xrm.Sdk.InvalidPluginExecutionException.%23ctor%2A> constructors to see what kind of error related data your plug-in can pass back to the platform.

> [!TIP]
> We recommend that you catch any error and throw an `InvalidPluginExecutionException` exception so you can control what is displayed to the user. This error may simply be "`An unexpected error occurred`", but you could also add some information that will help the administrator troubleshoot the issue. This way, you have some control. If you allow other types of exceptions to bubble up, the error will be presented as an `IsvUnExpected` error with the message `An unexpected error occurred from ISV code.`, which is not very helpful.


## How Asynchronous plug-ins exceptions are handled

The exception message for asynchronous registered plug-ins is written to a **System Job** table, also known as the [AsyncOperation Table](reference/entities/asyncoperation.md), which can be viewed in the **System Jobs** area of the web application. No dialog is displayed to the user. Async plug-ins don't participate in the database transaction that queued them, therefore they can't cancel the transaction.

### Retry an asynchronous plug-in

With an asynchronous plug-in step, you can retry when a plug-in fails. The cause of the failure may be due to a network error or some other retriable error calling an external resource.

To retry your plug-in, use the [InvalidPluginExecutionException(OperationStatus, Int32, String)](/dotnet/api/microsoft.xrm.sdk.invalidpluginexecutionexception.-ctor#microsoft-xrm-sdk-invalidpluginexecutionexception-ctor(microsoft-xrm-sdk-operationstatus-system-int32-system-string)) constructor using the [OperationStatus Enum](/dotnet/api/microsoft.xrm.sdk.operationstatus) `Retry` member value.

When your plug-in throws this type of exception, the asynchronous service attempts to execute your plug-in four times. If the plug-in execution doesn't succeed within four attempts, the call fails.


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
