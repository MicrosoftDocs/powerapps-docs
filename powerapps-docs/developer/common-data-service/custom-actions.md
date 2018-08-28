---
title: "Create your own actions (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Actions are custom messages that help in extending functionality of Dynamics 365 Customer Engagement. Learn more about how to create your own actions" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "brandonsimons" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Create your own actions

You can extend the functionality of Common Data Service for Apps by creating custom messages known as *actions*. These actions will have associated request/response classes and a Web API action will be generated. Actions are typically used to add new domain specific functionality to the organization web service or to combine multiple organization web service message requests into a single request. For example, in a support call center, you may want to combine the Create, Assign, and Setstate messages into a single new Escalate message.  
  
 The business logic of an action is implemented using a workflow. When you create an action, the associated real-time workflow is automatically registered to execute in stage 30 (core operation) of the execution pipeline. For more information about real-time workflows, see [Workflow types](/dynamics365/customer-engagement/developer/process-categories).  
  
 While actions are supported in both CDS for Apps, creating an action in code (using XAML) is only supported by  on-premises and IFD deployments. Online customers must create actions interactively in the web application.  
  
<a name="about_actions"></a>   

## About action definitions  

 An action is defined by using a `Workflow` entity record, similar to a real-time workflow. Some key points of what an action is and how it works are in the following list:  
  
- Can be associated with a single entity or be global (not associated with any particular entity).  
  
- Is executed in the core operation stage 30 of the event execution pipeline.  
  
- Supports the invocation of plug-ins registered in the pre-operation and post-operation stages of the event execution pipeline.  
  
- Can have plug-ins registered in the pre-operation or post-operation stages only when the action status is Activated.  
  
- Is available through the Web API or `organization.svc` and `organization.svc/web` endpoints.  
  
- Can be executed using a JavaScript web resource. More information: [Execute an action using a JavaScript web resource](/dynamics365/customer-engagement/developer/create-own-actions#BKMK_JavaScript)  
  
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

<!-- Removed much content about creating a custom action using code-->
  
<a name="bkmk_package"></a>   

## Package an action for distribution

 To distribute your action so that it can be imported into a CDS for Apps organization, add your action to a CDS for Apps solution. This is easily done using the web application by navigating to **Settings** > **Customizations** > **Solutions**. You can also write code to create the solution. For more information about solutions, see [Package and distribute extensions](/dynamics365/customer-engagement/developer/package-distribute-extensions-use-solutions).  
  
<a name="bkmk_gentypes"></a>

## Generate early-bound types for an action

 Using the CrmSvcUtil tool, you can generate request and response classes for your action to include in your application code. However, before you generate these classes, be sure to activate the action.  
  
To download the CrmSvcUtil.exe, see [Download tools from NuGet](download-tools-NuGet.md).
  
 The following sample shows the format for running the tool from the command line for an on-premises installation of CDS for Apps. You supply the parameter values for your installation.  
  
```ms-dos  
CrmSvcUtil.exe /url:http://<serverName>/<organizationName>/XRMServices/2011/Organization.svc /out:<outputFilename>.cs /username:<username> /password:<password> /domain:<domainName> /namespace:<outputNamespace> /serviceContextName:<serviceContextName> /generateActions  
```  
  
 The following sample shows the format for running the tool from the command line with CDS for Apps. You supply the parameter values appropriate for your account and server.  
  
```ms-dos  
CrmSvcUtil.exe /url:https://<organizationUrlName>.api.crm.dynamics.com/XRMServices/2011/Organization.svc /out:<outputFilename>.cs /username:<username> /password:<password> /namespace:<outputNamespace> /serviceContextName:<serviceContextName> /generateActions  
```  
  
 Notice the use of the `/generateActions` parameter. More information: [Create Early Bound Entity Classes with the Code Generation Tool (CrmSvcUtil.exe)](/dynamics365/customer-engagement/developer/org-service/create-early-bound-entity-classes-code-generation-tool).  
  
 You can use early-bound or late-bound types with the generated request and response classes for your action.  
  
<a name="bkmk_executeWebAPI"></a>

## Execute an action using the Web API

A new action is created in the Web API when it is created. If the action is created in the context of an entity, it is bound to that entity. Otherwise it is an unbound action. More information: [Use Web API actions](/dynamics365/customer-engagement/developer/webapi/use-web-api-actions).  
  
<a name="bkmk_execute"></a>

## Execute an action using the organization service

To execute an action using the organization web service using managed code, follow these steps.  
  
1. Include the early-bound types file that you generated using the CrmSvcUtil tool in your application’s project.  
  
2. In your application code, instantiate your action’s request and populate any required properties.  
  
3. Invoke <xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute*>, passing your request as an argument.  
  
   Before you run your application code, make sure the action is activated. Otherwise, you’ll receive a run-time error.  
  
<a name="BKMK_JavaScript"></a>   

### Execute an action using a JavaScript web resource

An action can be executed using the Web API just like any system action. More information: [Use Web API actions](/dynamics365/customer-enagagement/developer/webapi/use-web-api-actions).  

The [Sdk.Soap.js](http://code.msdn.microsoft.com/SdkSoapjs-9b51b99a) sample library demonstrates how messages can be used with JavaScript web resources and the Organization service (organization.svc/web). Use the companion [Sdk.Soap.js Action Message Generator](http://code.msdn.microsoft.com/SdkSoapjs-Action-Message-971be943) sample to generate JavaScript libraries that can be used with Sdk.Soap.js in the same way you can use the libraries for system messages provided in that sample. The files generated using the `Sdk.Soap.js` Action Message Generator are separate JavaScript libraries for each action. Each library contains a request and response class that correspond to the classes generated by the CrmSvcUtil.  
  
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
>  A best practice recommendation is that long running operations should be executed outside of CDS for Apps using .NET asynchronous or background processes.  
  
### See also  
 [Create real-time workflows](/dynamics365/customer-engagement/developer/create-real-time-workflows)   
 [Use dialogs for guided processes](/dynamics365/customer-engagement/developer/use-dialogs-guided-processes)   
 [Event Execution Pipeline](/dynamics365/customer-engagement/developer/event-execution-pipeline)   
 [Write Workflows to Automate Business Processes](/dynamics365/customer-engagement/developer/automate-business-processes-customer-engagement)   
 [Customize your system](https://technet.microsoft.com/library/dn531158.aspx)
