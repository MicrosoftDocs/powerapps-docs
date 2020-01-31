---
title: "Handle exceptions in a plug-in (Common Data Service) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Understand system behavior when a plug-in passes an exception back to the caller."
ms.custom: ""
ms.date: 09/20/2019
ms.reviewer: ""
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

There are two possible outcomes when a plug-in allows an exception to be passed back to the D365 system: information about the exception is logged or displayed to the user, and the current message request being processed is cancelled. The exact behavior as described below is dependent on how the plug-in is executed: in the sandbox or not, synchronous or asynchronous.

<a name='cancelling-an-operation'></a>

## Cancelling the current operation

Your code can cause the current message request processing operation to be cancelled by throwing an exception or passing a uncaught exception back to the D365 system. Any exception passed back to the plug-in caller will cause the current operation to be cancelled, so it is important that you apply coding best practices to manage any exceptions that are thrown and to determine whether to allow the exception to cancel the current operation or not.

If your business logic dictates that the operation should be cancelled, you should throw an <xref:Microsoft.Xrm.Sdk.InvalidPluginExecutionException> exception and provide a message to explain why the operation was cancelled.

Ideally, you should only cancel operations using synchronous plug-ins registered in the **PreValidation** stage. This stage *usually* occurs outside the main database transaction. Cancelling an operation before it reaches the transaction is highly desirable because the cancelled operation has to be rolled back. Rolling back the operation requires significant resources and has a performance impact on the system. Operations in the **PreOperation** and **PostOperation** stages are always within the database transaction.

Sometimes **PreValidation** stages will be within a transaction when they are initated by logic in another operation. For example, if you create a task entity record in the **PreOperation** stage of the creation of an account, the task creation will pass through the event execution pipeline and occur within the **PreValidation** stage yet it will be part of the transaction that is creating the account entity record. You can tell whether an operation is within a transaction by the value of the <xref:Microsoft.Xrm.Sdk.IExecutionContext>.<xref:Microsoft.Xrm.Sdk.IExecutionContext.IsInTransaction> property.

## How the system handles plug-in exceptions

When you throw an <xref:Microsoft.Xrm.Sdk.InvalidPluginExecutionException> exception within a synchronous plug-in an error dialog with your message will be displayed to the user. If you don't provide a message, a generic error dialog will be shown to the user. If any other type of exception is thrown, the user will see an error dialog with a generic message and the exception message and stack trace will be written to the [PluginTraceLog Entity](reference/entities/plugintracelog.md).

The exception message for asynchronous registered plug-ins is written to a System Job [AsyncOperation Entity](reference/entities/asyncoperation.md) record which can be viewed in the **System Jobs** area of the web application. No dialog will be displayed to the user. Async plug-ins do not participate in the database transaction that queued them, therefore they cannot cancel the transaction.

> [!NOTE]
> In the Unified Interface, the error dialog does not support HTML encoded content or messaging.
