---
title: "Developers: Best practices and guidance regarding plug-in and workflow development for Microsoft Dataverse | Microsoft Docs"
description: Best practices and guidance regarding plug-in and workflow development for developers of Microsoft Dataverse in Power Apps.
suite: powerapps
author: jowells
ms.author: jowells
ms.reviewer: jdaly
ms.topic: article
ms.date: 04/03/2025
ms.subservice: dataverse-developer
search.audienceType: 
  - developer
---
# Best practices and guidance regarding plug-in and workflow development for Microsoft Dataverse


This list contains guidance and best practices regarding the plug-in and workflow development within Dataverse.

|Best Practice  |Description  |
|---------|---------|
|[Don't use batch request types in plug-ins and workflow activities](avoid-batch-requests-plugin.md)|Don't use ExecuteMultipleRequest or ExecuteTransactionRequest message request classes within the context of a plug-in or workflow activity.|
|[Develop `IPlugin` implementations as stateless](develop-iplugin-implementations-stateless.md)     |Members of classes that implement `IPlugin` are exposed to potential thread-safety issues, which could lead to data inconsistency or performance problems.         |
|[Don't duplicate plug-in step registration](do-not-duplicate-plugin-step-registration.md)     |Duplicate plug-in step registration cause the plug-in to fire multiple times on the same message/event.         |
|[Don't use parallel execution within plug-ins and workflow activities](do-not-use-parallel-execution-in-plug-ins.md)|Multi or parallel threading within plug-ins or custom workflow activities isn't supported.|
|[Implement all types of queries when filtering results using `PreOperation` `RetrieveMultiple`](implement-all-types-of-queries-when-filtering-preoperation-retrievemultiple.md)|For best performance and consistent results for all applications, you must implement filtering for all types of queries that can be used with plug-ins that are registered for the PreOperation stage of RetrieveMultiple|
|[Include filtering attributes with plug-in registration](include-filtering-attributes-plugin-registration.md)     |If no filtering attributes are set for a plug-in registration step, then the plug-in executes every time an update message occurs for that event.         |
|[Limit the registration of plug-ins for Retrieve and RetrieveMultiple messages](limit-registration-plugins-retrieve-retrievemultiple.md)     |Adding synchronous plug-in logic to the Retrieve and RetrieveMultiple message events can cause slowness.         |
|[Manage plug-ins in single solution](manage-plug-ins-single-solution.md)|The definition of a plug-in assembly should be maintained within a single solution. |
|[Optimize custom assembly development](optimize-assembly-development.md)     |Consider merging separate plug-ins/custom workflow activities into a single custom assembly to improve performance and maintainability and move plug-ins/custom workflow activities into multiple custom assemblies if an assembly size is near the sandbox assembly size constraints.         |
|[Set KeepAlive to false when interacting with external hosts in a plug-in](set-keepalive-false-interacting-external-hosts-plugin.md)     |KeepAlive property set to true in the HTTP request header or not explicitly defined as false can cause increased execution times of plug-ins.         |
|[Set Timeout when making external calls in a plug-in](set-timeout-for-external-calls-from-plug-ins.md)     |Limit the time period that external calls expect a response within plug-ins.|
|[Use InvalidPluginExecutionException in plug-ins and workflow activities](use-invalidpluginexecutionexception-plugin-workflow-activities.md)     |Use InvalidPluginExecutionException when raising errors within the context of a plug-in or workflow activity.         |
|[Use ITracingService in Plug-ins](use-itracingservice-plugins.md)| Use the ITracingService within your plug-ins to gain insight into what happens when your code runs.|
|[Verify certification dependencies for plug-ins making outbound calls](verify-certification-dependencies.md)|Ensure that any certificates that your code depends on for outbound calls have a valid chain of certificates.|
|[Write memory efficient code](/troubleshoot/power-platform/dataverse/plug-in-execution/dataverse-plug-ins-errors#worker-process-reaches-the-memory-limit)|Retrieve only data within your plugin that is needed.|


### See Also

[Apply business logic using code](../../apply-business-logic-with-code.md)<br />
[Use plug-ins to extend business processes](../../plug-ins.md)<br />
[Workflow extensions](../../workflow/workflow-extensions.md)<br />


[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
