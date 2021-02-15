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
ms.date: 3/5/2020
ms.author: JDaly
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Use InvalidPluginExecutionException in plug-ins and workflow activities

[!INCLUDE[cc-data-platform-banner](../../../../includes/cc-data-platform-banner.md)]

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