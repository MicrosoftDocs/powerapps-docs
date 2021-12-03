---
title: "Use InvalidPluginExecutionException in plug-ins and workflow activities | MicrosoftDocs"
description: "Use InvalidPluginExecutionException when raising errors within the context of a plug-in or workflow activity."
services: ''
suite: powerapps
documentationcenter: na
author: JimDaly
manager: ryjones
editor: ''
tags: ''
ms.service: powerapps
ms.devlang: na
ms.topic: article
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 03/06/2021
ms.subservice: dataverse-developer
ms.author: jdaly
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Use InvalidPluginExecutionException in plug-ins and workflow activities


**Category**: Supportability, Usability

**Impact potential**: Medium

<a name='symptoms'></a>

## Symptoms

If a synchronous plug-in returns an exception other than <xref:Microsoft.Xrm.Sdk.InvalidPluginExecutionException> back to the platform, in a Power Apps client an error  is displayed to the user with the message of the exception <xref:System.Exception.Message> and the stack trace. This provides an unfriendly user experience in what is likely already a frustrating situation.

If you are using <xref:Microsoft.Xrm.Sdk.InvalidPluginExecutionException> to intentionally cancel the operation because of data validation logic issue, you should provide guidance applicable to the application user so that they can correct the issue and continue.

If the error is unexpected, it is still recommended to catch the error and convert it into a <xref:Microsoft.Xrm.Sdk.InvalidPluginExecutionException> so that applications can show a friendly error message with guidance to help a user or technical staff quickly identify the issue.

<a name='guidance'></a>

## Guidance

Plug-ins should only return an <xref:Microsoft.Xrm.Sdk.InvalidPluginExecutionException> for the following reasons:

- Show a useful message to the user
- Avoiding event log/trace file bloat

Failure to convert the message into a <xref:Microsoft.Xrm.Sdk.InvalidPluginExecutionException> will result in an `IsvUnExpected` error with no message displayed to the user from a Power Apps client.

### Handle errors from functions called in plug-ins

Within your plug-in you will commonly call other functions to re-use code. How you handle errors in these functions is very important because an unhandled error may cause the worker process to crash. This will not only terminate your plug-in, but may also terminate any concurrent plug-ins running for your organization. More information: [Error: No Sandbox Worker processes are currently available](../../troubleshoot-plug-in.md#error-no-sandbox-worker-processes-are-currently-available)

<a name='problem'></a>

## Problematic patterns

> [!WARNING]
> These patterns should be avoided.

Do not use HTML within error message text. 

Web applications which access Dataverse data should HTML encode any error message text before they display it to a user. This will prevent any HTML in your message from rendered as you intend. It will just show the HTML code.


<a name='seealso'></a>

### See also

[Cancelling an operation](../../handle-exceptions.md#cancelling-an-operation)<br/>
[Debug Workflow Activities](../../workflow/workflow-extensions.md#debug-workflow-activities)<br/>


[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]