---
title: "Create your own actions (Common Data Service) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Actions are custom messages that help in extending functionality of Common Data Service. Learn more about how to create your own actions" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 09/20/2019
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "JimDaly" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Create your own actions

You can extend the functionality of Common Data Service by creating custom messages known as *actions*. These actions will have associated request/response classes and a Web API action will be generated. Actions are typically used to add new domain specific functionality to the organization web service or to combine multiple organization web service message requests into a single request. For example, in a support call center, you may want to combine the Create, Assign, and Update messages into a single new Escalate message.  
  
The business logic of an action is implemented using a workflow. When you create an action, the associated real-time workflow is automatically registered to execute in the main operation stage of the execution pipeline. 
  
  
<a name="about_actions"></a>   

## About action definitions  

 An action is defined by using a `Workflow` entity record, similar to a real-time workflow. Some key points of what an action is and how it works are in the following list:  
  
- Can be associated with a single entity or be global (not associated with any particular entity).  
  
- Is executed in the main operation stage of the event execution pipeline.  
  
- Supports the invocation of plug-ins registered in the pre-operation and post-operation stages of the event execution pipeline.  
  
- Can have plug-ins registered in the pre-operation or post-operation stages only when the action status is Activated.  
  
- Is available through the Web API or `organization.svc` and `organization.svc/web` endpoints.  
  
- Can be executed using a JavaScript web resource. 
  
- Always runs under the security context of the calling user.  
  
- Record can’t be deleted while there are plug-in steps registered on the action.  
  
- Can optionally, through a configuration setting, participate in the current database transaction.  
  
- Doesn’t support a scope where the execution is restricted to a user, business unit, or organization. Actions always execute in organization scope.  
  
- Supports input and output arguments.  
  
- Supports auditing of data changes.  
  
- Isn’t supported with offline clients.  
  
- Can be invoked  by a web service method call.  
  
- Can be invoked directly from a workflow.  
  
<a name="bkmk_permissions"></a> 
  
## Required permissions
  
 A security privilege named Activate Real-time Processes (`prvActivateSynchronousWorkflow`) is required to activate an action’s real-time workflow so that it can be executed. This is in addition to any privileges needed to create a workflow.  

  
<a name="bkmk_package"></a>   

## Package an action for distribution

 To distribute your action so that it can be imported into a Common Data Service organization, add your action to a Common Data Service solution. This is easily done using the web application by navigating to **Settings** > **Customizations** > **Solutions**. You can also write code to create the solution. For more information about solutions, see [Introduction to solutions](introduction-solutions.md).  
  
<a name="bkmk_gentypes"></a>

## Generate early-bound types for an action

 Using the CrmSvcUtil tool, you can generate request and response classes for your action to include in your application code. However, before you generate these classes, be sure to activate the action.  
  
To download the CrmSvcUtil.exe, see [Download tools from NuGet](download-tools-NuGet.md).
 
 The following sample shows the format for running the tool from the command line with Common Data Service. You supply the parameter values appropriate for your account and server.  
  
```ms-dos  
CrmSvcUtil.exe /interactivelogin ^
/out:<outputFilename>.cs ^
/namespace:<outputNamespace> ^
/serviceContextName:<serviceContextName> ^
/generateActions
```  
  
 Notice the use of the `/generateActions` parameter. More information: [Generate early-bound classes for the Organization service](org-service/generate-early-bound-classes.md).  
  
 You can use early-bound or late-bound types with the generated request and response classes for your action.  
  
<a name="bkmk_executeWebAPI"></a>

## Execute an action using the Web API

A new action is created in the Web API when it is created. If the action is created in the context of an entity, it is bound to that entity. Otherwise it is an unbound action. More information: [Use Web API actions](webapi/use-web-api-actions.md).  
  
<a name="bkmk_execute"></a>

## Execute an action using the organization service

To execute an action using the organization web service using managed code, follow these steps.  
  
1. Include the early-bound types file that you generated using the CrmSvcUtil tool in your application’s project.  
  
2. In your application code, instantiate your action’s request and populate any required properties.  
  
3. Invoke <xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute*>, passing your request as an argument.  
  
   Before you run your application code, make sure the action is activated. Otherwise, you’ll receive a run-time error.  
  
<a name="BKMK_JavaScript"></a>   

### Execute an action using a JavaScript web resource

An action can be executed using the Web API just like any system action. More information: [Use Web API actions](webapi/use-web-api-actions.md).  

  
<a name="bkmk_execute-process"></a>

## Execute an action using a process

You can execute an action from workflows, dialogs, or other process actions. Activated custom actions are available to processes by selecting the **Perform Action** item in the **Add Step** drop down of the web application process form. After the step is added to your process, you can select your new custom action (or any action) from the **Action** list provided in the step. Select **Set Properties** in the step to specify any input parameters that your custom action requires.  
  
> [!NOTE]
>  If a custom action has unsupported parameter types, for example Picklist, Entity, or Entity Collection, the custom action isn’t listed in the **Action** list.  
  
The existing <xref:Microsoft.Xrm.Sdk.IExecutionContext.Depth> platform checks ensure an infinite loop does not occur. For more information on depth limits see <xref:Microsoft.Xrm.Sdk.Deployment.WorkflowSettings.MaxDepth>.  
  
<a name="bkmk_longrunning"></a>

## Watch out for long running actions

If one of the steps in the action’s real-time workflow is a custom workflow activity, that custom workflow activity is executed inside the isolated sandbox run-time environment and will be subject to the two minute timeout limit, similar to how sandboxed plug-ins are managed. However, there are no restrictions on the amount of overall time the action itself can take. In addition, if an action participates in a transaction, where rollback is enabled, SQL Server timeouts will apply.  

> [!TIP]
>  A best practice recommendation is that long running operations should be executed outside of Common Data Service using .NET asynchronous or background processes.  
  
### See also  
 [Use actions](/flow/actions)<br />
 [Event execution pipeline](event-framework.md#event-execution-pipeline)<br />
 [Classic Common Data Service workflows](/flow/workflow-processes)<br />

