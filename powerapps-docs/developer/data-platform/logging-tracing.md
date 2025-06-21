---
title: "Logging and tracing (Microsoft Dataverse) | Microsoft Docs"
description: "Use the plugin trace log to store plug-in execution information to aid in plug-in debugging."
ms.date: 06/20/2025
author: MsSQLGirl
ms.author: jukoesma
ms.reviewer: pehecke
ms.topic: concept-article
ms.subservice: dataverse-developer
search.audienceType: 
  - developer
contributors:
 - JimDaly
 - phecke
---
# Tracing and logging

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]

Use tracing to troubleshoot a plug-in or custom workflow activity (custom code). Tracing assists developers by recording run-time information as an aid in diagnosing the cause of code failures. Tracing is supported for synchronous or asynchronous execution.
  
Recording of run-time tracing information for Microsoft Dataverse is provided by a service named <xref:Microsoft.Xrm.Sdk.ITracingService>. Information provided to this service by custom code can be recorded in three different places as identified here.  

- **Trace log**  
  
    Trace log records are written to the [PluginTraceLog Table](reference/entities/plugintracelog.md). Writing of these records is controlled by the trace settings mentioned in [Enable trace logging](#enable-trace-logging).

    This data can be found in model-driven applications by navigating to **Settings** and choosing the **Plug-in Trace Log** tile. The tile is only visible if you have access to the trace log table records in your assigned security role.

    You may find it easier to view this data by using the Web API in your browser using the example shown in [Use Tracing](debug-plug-in.md#use-tracing) or by using the [Plugin Trace Viewer](#plugin-trace-viewer) community tool.

    > [!IMPORTANT]
    > Trace logging takes up organization storage space especially when many traces and exceptions are generated. You should only turn trace logging on for debugging and troubleshooting, and turn it off after your investigation is completed.  
  
- **Error dialog**  
  
     A synchronous registered plug-in or custom workflow activity that returns an exception from the platform results in an error dialog box in the web application presented to the logged on user. The user can select the **Download Log File** button in the dialog to view the log containing exception and trace output.  
  
- **System job**  
  
     For asynchronous registered plug-in or custom workflow activities that return an exception, the tracing information is shown in the **Details** area of the **System Job** form in the web application.  
  
<a name="bkmk_trace-settings"></a>

## Enable trace logging

Whether trace logs are written depends on the value of the [Organization](./reference/entities/organization.md) table [PluginTraceLogSetting](./reference/entities/organization.md#BKMK_PluginTraceLogSetting) column value. You can enable trace logging by programmatically updating the `PluginTraceLogSetting` value.

A second method to enable trace logging is through the legacy web application. Navigate to **Settings** > **Administration** > **System Settings**. In the **Customization** tab, locate the drop-down menu labeled **Enable logging to plug-in trace log** and select one of the available options. More information: [Settings in Unified Interface apps](/power-platform/admin/admin-settings#settings-in-unified-interface-apps), [Settings in legacy web client apps](/power-platform/admin/admin-settings#settings-in-legacy-web-client-apps)

A third option can be found in the Plug-in Registration tool. After connecting the tool to your organization (environment), select **Settings** > **Logging to Plug-in Trace Log** and then select one of the available options.
  
|Value|Option|Description|  
|------------|-----------------|-----------------|  
|0|Off|Writing to the trace log is disabled. No **PluginTraceLog** records are created. However, custom code can still call the <xref:Microsoft.Xrm.Sdk.ITracingService.Trace(System.String,System.Object[])> method even though no log is written.|  
|1|Exceptions|Trace information is written to the log if an exception is passed back to the platform from custom code.|  
|2|All|Trace information is written to the log upon code completion or an exception is passed back to the platform from the custom code.|  
  
If the trace logging setting is set to **Exception** and your custom code returns an exception back to the platform, a trace log record is created and tracing information is also written to one other location. For custom code that executes synchronously, the information is presented to the user in an error dialog box, otherwise, for asynchronous code, the information is written to the related system job.  

## Write to the tracing service

Before writing to the tracing service, you must first extract the tracing service object from the passed execution context. Afterwards, add <xref:Microsoft.Xrm.Sdk.ITracingService.Trace(System.String,System.Object[])> calls to your custom code where appropriate passing any relevant diagnostic information in that method call.  

 ```csharp
//Extract the tracing service for use in debugging plug-ins.
 ITracingService tracingService =
     (ITracingService)serviceProvider.GetService(typeof(ITracingService));

 // Use the tracing service 
 tracingService.Trace("Write your message here.");
 
```

Next, build and deploy the plug-in or custom workflow activity. During execution of the custom code, the information provided in the **Trace** method calls is written to a trace log table record by <xref:Microsoft.Xrm.Sdk.ITracingService>, if supported by your organization and enabled, and might also be made available to the user in a Web dialog or system job as described in the previous section. Tracing information written to the trace log is configured in the trace settings. For more information, see [Enable trace logging](#bkmk_trace-settings).  
  
> [!NOTE]
> If your custom code executes within a database transaction, and an exception occurs that causes a transaction rollback, all table data changes by your code are undone. However, the [PluginTraceLog](reference/entities/plugintracelog.md) records will remain after the rollback completes.  
  
## Additional information about the tracing service

The <xref:Microsoft.Xrm.Sdk.ITracingService> batches the information provided to it through the **Trace** method. The information is written to a new [PluginTraceLog](reference/entities/plugintracelog.md) record after the custom code successfully runs to completion or an exception is thrown.  

Each `Trace` call is logged as a new line in the [PluginTraceLog](reference/entities/plugintracelog.md) [MessageBlock](reference/entities/plugintracelog.md#BKMK_MessageBlock) column. Only 10 kb of text can be written. Older trace lines are removed to meet this limit so that only the most recent lines are saved.
  
[PluginTraceLog](reference/entities/plugintracelog.md) records have a finite lifetime. A bulk deletion background job runs once per day to delete records that are older than 24 hours from creation.

> [!CAUTION]
> While this job can be disabled or the frequency in which it occurs can be adjusted, failure to set it back to the original setting is frequently discovered to be the cause of performance issues later on.

## Community tools

### Plugin Trace Viewer

**[Plugin Trace Viewer](https://jonasr.app/PTV)** is a tool that XrmToolBox community developed. Please see the [Community tools for Dataverse](community-tools.md) topic for community developed tools.

> [!NOTE]
> Microsoft doesn't extend support to community tools.
> If you have questions pertaining to the tool, contact the publisher. More Information: [XrmToolBox](https://www.xrmtoolbox.com).  

### See also

[Plug-ins](plug-ins.md)  
[Debug a plug-in](debug-plug-in.md#use-tracing)  
[View trace logs](tutorial-write-plug-in.md#view-trace-logs)  
[Tracing service](write-plug-in.md#tracing-service)  
[PluginTraceLog Table](reference/entities/plugintracelog.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
