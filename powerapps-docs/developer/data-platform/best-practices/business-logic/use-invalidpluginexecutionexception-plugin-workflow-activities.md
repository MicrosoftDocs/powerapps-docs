---
title: "Use InvalidPluginExecutionException in plug-ins and workflow activities | MicrosoftDocs"
description: "Use InvalidPluginExecutionException when raising errors within the context of a plug-in or workflow activity."
ms.date: 06/20/2025
author: MsSQLGirl
ms.author: jukoesma
ms.reviewer: pehecke
suite: powerapps
ms.topic: article
ms.subservice: dataverse-developer
search.audienceType: 
  - developer
contributors:
 - JimDaly
 - phecke
---
# Use InvalidPluginExecutionException in plug-ins and workflow activities


**Category**: Supportability, Usability

**Impact potential**: Medium

<a name='symptoms'></a>

## Symptoms

If a synchronous plug-in returns an exception other than <xref:Microsoft.Xrm.Sdk.InvalidPluginExecutionException> back to the platform, a Power Apps client displays an error to the user with the message of the exception <xref:System.Exception.Message> and the stack trace. This provides an unfriendly user experience in what is likely already a frustrating situation.

If you're using <xref:Microsoft.Xrm.Sdk.InvalidPluginExecutionException> to intentionally cancel the operation because of data validation logic issue, you should provide guidance applicable to the application user so that they can correct the issue and continue.

If the error is unexpected, it's still recommended to catch the exception, convert it into a <xref:Microsoft.Xrm.Sdk.InvalidPluginExecutionException>, and then throw the new exception so that applications can show a friendly error message with guidance to help a user or technical staff quickly identify the issue.

<a name='guidance'></a>

## Guidance

Plug-ins should only return an <xref:Microsoft.Xrm.Sdk.InvalidPluginExecutionException> for the following reasons:

- Show a useful message to the user
- Avoiding event log/trace file bloat

A thrown <xref:Microsoft.Xrm.Sdk.InvalidPluginExecutionException> returns to the caller with a friendly message and an `IsvAborted` error code. Failure to catch and convert an exception into a <xref:Microsoft.Xrm.Sdk.InvalidPluginExecutionException> results in an `IsvUnExpected` error code with no friendly message displayed to the user from a Power Apps client. 

### Handle errors from functions called in plug-ins

Plug-ins commonly call other functions to reuse code. How you handle errors in these functions is important because an unhandled error might cause the worker process to crash. This crashing worker process not only terminates your plug-in, but might also terminate any concurrent plug-ins running for your organization. More information: [Error: Sandbox Worker process crashed](../../troubleshoot-plug-in.md#error-sandbox-worker-process-crashed)

<a name='problem'></a>

## Problematic patterns

> [!WARNING]
> These patterns should be avoided.

Don't use HTML within error message text. 

Web applications that access Dataverse data should HTML encode any error message text before they display it to a user. This encoding prevents any HTML in your message from rendered as you intend. It just shows the HTML code.


<a name='seealso'></a>

### See also

[Cancelling an operation](../../handle-exceptions.md#cancelling-an-operation)<br/>
[Debug Workflow Activities](../../workflow/workflow-extensions.md#debug-workflow-activities)<br/>


[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
