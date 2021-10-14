---
title: "Developers: Best practices and guidance regarding plug-in and workflow development for the Microsoft Dataverse | Microsoft Docs"
description: Best practices and guidance regarding plug-in and workflow development for developers of the Microsoft Dataverse in Power Apps.
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
ms.date: 9/23/2019
ms.subservice: dataverse-developer
ms.author: jowells
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Best practices and guidance regarding plug-in and workflow development for the Microsoft Dataverse

[!INCLUDE[cc-data-platform-banner](../../../../includes/cc-data-platform-banner.md)]

This list below contains all of the guidance and best practices regarding the plug-in and workflow development within the Dataverse.

|Best Practice  |Description  |
|---------|---------|
|[Do not use batch request types in plug-ins and workflow activities](avoid-batch-requests-plugin.md)|Don't use ExecuteMultipleRequest or ExecuteTransactionRequest message request classes within the context of a plug-in or workflow activity.|
|[Develop IPlugin implementations as stateless](develop-iplugin-implementations-stateless.md)     |Members of classes that implement IPlugin are exposed to potential thread-safety issues, which could lead to data inconsistency or performance problems.         |
|[Do not duplicate plug-in step registration](do-not-duplicate-plugin-step-registration.md)     |Duplicate plug-in step registration will cause the plug-in to fire multiple times on the same message/event.         |
|[Do not use parallel execution within plug-ins and workflow activities](do-not-use-parallel-execution-in-plug-ins.md)|Multi or parallel threading within plug-ins or custom workflow activities is not supported.|
|[Implement all types of queries when filtering results using PreOperation RetrieveMultiple](implement-all-types-of-queries-when-filtering-preoperation-retrievemultiple.md)|For best performance and consistent results for all applications, you must implement filtering for all types of queries that can be used with plug-ins that are registered for the PreOperation stage of RetrieveMultiple|
|[Include filtering attributes with plug-in registration](include-filtering-attributes-plugin-registration.md)     |If no filtering attributes are set for a plug-in registration step, then the plug-in will execute every time an update message occurs for that event.         |
|[Limit the registration of plug-ins for Retrieve and RetrieveMultiple messages](limit-registration-plugins-retrieve-retrievemultiple.md)     |Adding synchronous plug-in logic to the Retrieve and RetrieveMultiple message events can cause slowness.         |
|[Optimize custom assembly development](optimize-assembly-development.md)     |Consider merging separate plug-ins/custom workflow activities into a single custom assembly to improve performance and maintainability and move plug-ins/custom workflow activities into multiple custom assemblies if an assembly size is near the sandbox assembly size constraints.         |
|[Remove unsupported code that uses reflection in custom workflow activities](remove-unsupported-code-using-reflection-workflow-activities.md)|Workflow activities containing unsupported code that uses reflection will break in the coming months unless it is removed.|
|[Set KeepAlive to false when interacting with external hosts in a plug-in](set-keepalive-false-interacting-external-hosts-plugin.md)     |KeepAlive property set to true in the HTTP request header or not explicitly defined as false can cause increased execution times of plug-ins.         |
|[Set Timeout when making external calls in a plug-in](set-timeout-for-external-calls-from-plug-ins.md)     |Limit the time period that external calls will expect a response within plug-ins.|   
|[Use InvalidPluginExecutionException in plug-ins and workflow activities](use-invalidpluginexecutionexception-plugin-workflow-activities.md)     |Use InvalidPluginExecutionException when raising errors within the context of a plug-in or workflow activity.         |
|[Verify certification dependencies for plug-ins making outbound calls](verify-certification-dependencies.md)|Ensure that any certificates that your code depends on for outbound calls have a valid chain of certificates.|

### See Also

[Apply business logic using code](../../apply-business-logic-with-code.md)<br />
[Use plug-ins to extend business processes](../../plug-ins.md)<br />
[Workflow extensions](../../workflow/workflow-extensions.md)<br />


[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]