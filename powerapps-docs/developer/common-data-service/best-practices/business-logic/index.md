---
title: "Developers: Best practices and guidance regarding plug-in and workflow development for the Common Data Service for Apps | Microsoft Docs"
description: Best practices and guidance regarding plug-in and workflow development for developers of the Common Data Service for Apps in PowerApps.
services: ''
suite: powerapps
documentationcenter: na
author: jowells
manager: austinj
editor: ''
tags: ''
ms.service: powerapps
ms.devlang: na
ms.topic: article
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 12/12/2018
ms.author: jowells
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Best practices and guidance regarding plug-in and workflow development for the Common Data Service for Apps

This list below contains all of the guidance and best practices regarding the plug-in and workflow development within the Common Data Service for Apps.

|Best Practice  |Description  |
|---------|---------|
|[Avoid usage of batch request types in plug-ins and workflow activities](avoid-batch-requests-plugin.md)     |You shouldn't use ExecuteMultipleRequest or ExecuteTransactionRequest message request classes within the context of a plug-in or workflow activity.         |
|[Develop IPlugin implementations as stateless](develop-iplugin-implementations-stateless.md)     |Members of classes that implement IPlugin are exposed to potential thread-safety issues which could lead to data inconsistency or performance problems.         |
|[Do not duplicate plug-in step registration](do-not-duplicate-plugin-step-registration.md)     |Duplicate plug-in step registration will cause the plug-in to fire multiple times on the same message/event.         |
|[Include filtering attributes with plug-in registration](include-filtering-attributes-plugin-registration.md)     |If no filtering attributes are set for a plug-in registration step, then the plug-in will execute every time an update message occurs for that event.         |
|[Limit the registration of plug-ins for Retrieve and RetrieveMultiple messages](limit-registration-plugins-retrieve-retrievemultiple.md)     |Adding synchronous plug-in logic to the Retrieve and RetrieveMultiple message events can cause slowness.         |
|[Optimize custom assembly development](optimize-assembly-development.md)     |Consider merging separate plug-ins/custom workflow activities into a single custom assembly to improve performance and maintainability and move plug-ins/custom workflow activities into multiple custom assemblies if an assembly size is near the sandbox assembly size constraints.         |
|[Set KeepAlive to false when interacting with external hosts in a plug-in](set-keepalive-false-interacting-external-hosts-plugin.md)     |KeepAlive property set to true in the HTTP request header or not explicitly defined as false can cause increased execution times of plug-ins.         |
|[Use InvalidPluginExecutionException in plug-ins and workflow activities](use-invalidpluginexecutionexception-plugin-workflow-activities.md)     |Use InvalidPluginExecutionException when raising errors within the context of a plug-in or workflow activity.         |
|[Use ITracingService in Plug-ins](use-itracingservice-plugins.md)     |Debugging and/or troubleshooting plug-in issues or behaviors are complicated without rich and insightful logging or tracing.         |

# See Also
[Apply business logic using code](../../apply-business-logic-with-code.md)<br />
[Use plug-ins to extend business processes](../../plug-ins.md)<br />
[Workflow extensions](../../workflow/workflow-extensions.md)<br />