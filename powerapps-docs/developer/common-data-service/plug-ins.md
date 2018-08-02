---
title: "<Topic Title> (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "<Description>" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "brandonsimons" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Write plug-ins to extend business processes

<!-- Needs major attention

https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/plugin-development
https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/write-plugin
https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/understand-data-context-passed-plugin
https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/handle-exceptions-plugins
https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/pass-data-between-plug-ins
https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/impersonation-plugins
https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/register-deploy-plugins
https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/debug-plugin
https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/analyze-plugin-performance
https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/walkthrough-register-plugin-using-plugin-registration-tool
https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/sample-create-basic-plugin

https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/plug-in-entities
https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/plug-in-registration-entities

Notes:
https://microsoft-my.sharepoint.com/:w:/p/jdaly/ETkwQsIe2VtCvxAyqTPKfTIBKDrLhcEjAm4JaJPfakQ8ww?e=2pxLqD 

See tutorials
https://microsoft-my.sharepoint.com/:w:/p/jdaly/EZ1SzmOh-B5Bnt4C9rxGWysB6NtUQonOxq5sGSPkn5vNAA?e=bGWQN3
-->

## Tracing

## Context information available to your code

## Impersonation

There are two ways to apply impersonation in plug-ins: at registration or execution.

### At plug-in registration

When you register a plug-in step you can specify a user account to use when the code is run by choosing from the **Run in User's Context** option. By default this is set to use the **Calling User**, which is the user account which initiated the action. When this default option is applied, the [SdkMessageProcessingStep.ImpersonatingUserId](reference/entities/sdkmessageprocessingstep.md#BKMK_ImpersonatingUserId) will be set to null or <xref:System.Guid.Empty>.

### During plug-in execution

You can override the setting specified at registration at run time by setting the <xref:Microsoft.Xrm.Sdk.IOrganizationServiceFactory>.<xref:Microsoft.Xrm.Sdk.IOrganizationServiceFactory.CreateOrganizationService(System.Nullable{System.Guid})> `userId` parameter.

This is typically set to the <xref:Microsoft.Xrm.Sdk.ExecutionContext>.<xref:Microsoft.Xrm.Sdk.ExecutionContext.UserId> value which will apply the user account defined by the plug-in step registration.

```csharp
(IOrganizationServiceFactory)serviceProvider.GetService(typeof(IOrganizationServiceFactory));
    IOrganizationService service = serviceFactory.CreateOrganizationService(context.UserId);
```

If you want to override the step registration you can pass the value of the <xref:Microsoft.Xrm.Sdk.ExecutionContext>.<xref:Microsoft.Xrm.Sdk.ExecutionContext.InitiatingUserId> to have a service that will use the user account that initiated the action that caused the plug-in to run.

You can also provide the [SystemUser.SystemUserId](reference/entities/systemuser.md#BKMK_SystemUserId) from any valid user account. This will work as long as that user has the permissions to perform the operations in the plug-in.

## See also

[Sample: Web access from a sandboxed plug-in](org-service/samples/web-access-plugin.md)

<!-- https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/sample-web-access-sandboxed-plugin -->