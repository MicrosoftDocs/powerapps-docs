---
title: "Use the IOrganization web service in a custom workflow activity (Common Data Service for Apps) | Microsoft Docs"
description: "Learn on how to get the IOrganizationService from within the Execute method of your custom workflow activity."
ms.custom: ""
ms.date: 06/16/2018
ms.reviewer: ""
ms.service: "crm-online"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
    - "Dynamics 365 (online)"
ms.assetid: 639d3a2d-9979-40aa-8947-1f5bbb489d79
caps.latest.revision: 23
author: "JimDaly"
ms.author: "jdaly"
manager: "amyla"
---
# Use the IOrganization web service in a custom workflow activity

To call Common Data Service for Apps organization web service methods from within a custom workflow activity, you must first obtain a reference to the web service. This is described in the following procedure and sample code.  
  
1.  Get a reference to <xref:Microsoft.Xrm.Sdk.IOrganizationServiceFactory>.  
2.  Use the <xref:Microsoft.Xrm.Sdk.IOrganizationServiceFactory>.<xref:Microsoft.Xrm.Sdk.IOrganizationServiceFactory.CreateOrganizationService(System.Nullable{System.Guid})> method to create an instance of<xref:Microsoft.Xrm.Sdk.IOrganizationService>.  
3.  Use the<xref:Microsoft.Xrm.Sdk.IOrganizationService> instance to call the supported methods.  
  
## Example  

The following sample shows how to get the<xref:Microsoft.Xrm.Sdk.IOrganizationService> from within the `Execute` method of your custom workflow activity.  
  
```csharp  
  
protected override void Execute(CodeActivityContext executionContext)  
{  
   // Get the context service.  
   IWorkflowContext context = executionContext.GetExtension<IWorkflowContext>();  
   IOrganizationServiceFactory serviceFactory = executionContext.GetExtension<IOrganizationServiceFactory>();  
  
   // Use the context service to create an instance of IOrganizationService.  
   IOrganizationService _orgService = serviceFactory.CreateOrganizationService(context.InitiatingUserId);  
  
   // Use the service reference to call web methods.  
   _orgService.Execute(…);  
}  
  
```  
  
### See also  

[Custom workflow activities (workflow assemblies)](custom-workflow-activities-workflow-assemblies.md)<br />
[Register and use a custom workflow activity assembly](register-use-custom-workflow-activity-assembly.md)<br />
[Sample: Create a Custom Workflow Activity](sample-create-custom-workflow-activity.md)<br />
<!-- TODO:
[IOrganizationService Web Service](../org-service/use-organization-service-read-write-data-metadata.md)<br />
[Organization service methods](../org-service/organization-service-methods.md)<br /> -->
<xref:Microsoft.Xrm.Sdk.Workflow.IWorkflowContext><br />
<xref:Microsoft.Xrm.Sdk.IOrganizationServiceFactory><br />
<xref:Microsoft.Xrm.Sdk.IOrganizationService>