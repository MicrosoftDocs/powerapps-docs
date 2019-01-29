---
title: "Logging and tracing (Common Data Service for Apps) | Microsoft Docs"
description: "Use the trace log to store plug-in execution information to aid in plug-in debugging."
ms.custom: ""
ms.date: 1/28/2019
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: phecke
ms.author: pehecke
manager: kvivek
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Logging and tracing

 An alternative method to troubleshoot a plug-in or custom workflow activity (custom code), compared to debugging in [!INCLUDE[pn_Visual_Studio](/powerapps/includes/pn-visual-studio.md)], is to use tracing. Tracing assists developers by recording run-time custom information as an aid in diagnosing the cause of code failures. Tracing is especially useful to troubleshoot [!INCLUDE[pn_CRM_Online](/powerapps/includes/pn-crm-online.md)] registered custom code as it is the only supported troubleshooting method for that scenario. Tracing is supported for sandboxed (partial trust) and full trust registered custom code and during synchronous or asynchronous execution. Tracing isn’t supported for custom code that executes in [!INCLUDE[pn_microsoft_dynamics_crm_for_outlook](/powerapps/includes/pn-microsoft-dynamics-crm-for-outlook.md)] or other mobile client.  
  
 Recording of run-time tracing information for [!INCLUDE[pn_dynamics_crm](/powerapps/includes/pn-dynamics-crm.md)] apps is provided by a service named <xref:Microsoft.Xrm.Sdk.ITracingService>. Information provided to this service by custom code can be recorded in three different places as identified here.  

> [!NOTE]
> Trace logging using `ITracingService` interface works only when the Plug-in is registered in Sandbox mode.

- **Trace log**  
  
     Trace log records of type **PluginTraceLog** can be found in the web application by navigating to **Settings** and choosing the **Plug-in Trace Log** tile. The tile is only visible if you have access to the trace log entity records in your assigned security role. Writing of these records is controlled by the trace settings mentioned in the next section.
  
    > [!NOTE]
    > Trace logging takes up organization storage space especially when many traces and exceptions are generated. You should only turn trace logging on for debugging and troubleshooting, and turn it off after your investigation is completed.  
  
- **Error dialog**  
  
     A synchronous registered plug-in or custom workflow activity that returns an exception back to the platform results in an error dialog box in the web application presented to the logged on user. The user may select the **Download Log File** button in the dialog to view the log containing exception and trace output.  
  
- **System job**  
  
     For asynchronous registered plug-in or custom workflow activities that returns an exception, the tracing information is shown in the **Details** area of the **System Job** form in the web application.  
  
<a name="bkmk_trace-settings"></a>   
## Enable trace logging  
 To enable trace logging in an organization that supports this feature, in the web application navigate to **Settings** > **Administration** > **System Settings**. In the **Customization** tab, locate the drop-down menu labeled **Enable logging to plug-in trace log** and select one of the available options.  
  
|Option|Description|  
|------------|-----------------|  
|Off|Writing to the trace log is disabled. No **PluginTraceLog** records will be created. However, custom code can still call the <xref:Microsoft.Xrm.Sdk.ITracingService.Trace(System.String,System.Object[])> method even though no log is written.|  
|Exceptions|Trace information is written to the log if an exception is passed back to the platform from custom code.|  
|All|Trace information is written to the log upon code completion or an exception is passed back to the platform from the custom code.|  
  
 If the trace logging setting is set to **Exception** and your custom code returns an exception back to the platform, a trace log record is created and tracing information is also written to one other location. For custom code that executes synchronously, the information is presented to the user in an error dialog box, otherwise, for asynchronous code, the information is written to the related system job.  
  
 By default, the System Administrator and System Customizer roles have the required privileges to change the trace logging setting, which is stored in a <xref:Microsoft.Xrm.Sdk.Deployment.TraceSettings> entity record. Trace settings have an organization scope.  
  
## Write to the tracing service  
 Before writing to the tracing service, you must first extract the tracing service object from the passed execution context. Afterwards, simply add <xref:Microsoft.Xrm.Sdk.ITracingService.Trace(System.String,System.Object[])> calls to your custom code where appropriate passing any relevant diagnostic information in that method call.  

 Download the sample: [Work with plug-ins](https://code.msdn.microsoft.com/Sample-Create-a-basic-plug-64d86ade).
  
 [!code-csharp[Plug-ins#AdvancedPlugin2](/dynamics365/customer-engagement/snippets/csharp/CRMV8/plug-ins/cs/advancedplugin2.cs#advancedplugin2)  
  
 Next, build and deploy the plug-in or custom workflow activity. During execution of the custom code, the information provided in the **Trace** method calls is written to a trace log entity record by <xref:Microsoft.Xrm.Sdk.ITracingService>, if supported by your organization and enabled, and may also be made available to the user in a Web dialog or system job as described in the previous section. Tracing information written to the trace log is configured in the trace settings. For more information see [Enable trace logging](#bkmk_trace-settings).  
  
> [!NOTE]
> If your custom code executes within a database transaction, and an exception occurs that causes a transaction rollback, all entity data changes by your code will be undone. However, the **PluginTraceLog** records will remain after the rollback completes.  
  
## Additional information about the tracing service

 The <xref:Microsoft.Xrm.Sdk.ITracingService> batches the information provided to it through the **Trace** method. The information is written to a new **PluginTraceLog** record after the custom code successfully runs to completion or an exception is thrown.  
  
 PluginTraceLog records have a finite lifetime. A bulk deletion background job runs once per day to delete records that are older than 24 hours from creation. This job can be disabled when needed. 

## Community tools

 ### Plug-in trace viewer

**Plugin Trace Viewer** is a tool that XrmToolbox community developed for [!INCLUDE[pn_dynamics_crm](/powerapps/includes/pn-dynamics-crm.md)] apps. Please see the [Developer tools](developer-tools.md) topic for community developed tools.

> [!NOTE]
> The community tools are not a product of [!include[pn_microsoft_dynamics](/powerapps/includes/pn-microsoft-dynamics.md)] apps and does not extend support to the community tools. 
> If you have questions pertaining to the tool, please contact the publisher. More Information: [XrmToolBox](https://www.xrmtoolbox.com).  

### See also

[Plug-ins](plug-ins.md)  
[Debug a plug-in](debug-plug-in.md#use-tracing)  
[View trace logs](tutorial-write-plug-in.md#view-trace-logs)  
[Use the tracing service](write-plug-in.md#use-the-tracing-service)