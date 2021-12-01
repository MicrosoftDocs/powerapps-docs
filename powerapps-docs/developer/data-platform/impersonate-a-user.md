---
title: "Impersonate a user (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn how to write plug-in code to act on behalf of a specific user."
ms.custom: ""
ms.date: 03/15/2021
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: JimDaly
ms.subservice: dataverse-developer
ms.author: pehecke
manager: kvivek
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Impersonate a user

Sometimes you need the code in a plug-in to run in the context of a different user, for example to perform an operation on their behalf.

There are two ways to apply impersonation in plug-ins: at registration or execution.

## At plug-in registration

When you register a plug-in step you can specify a user account to use when the code is run by choosing from the **Run in User's Context** option. By default this is set to use the **Calling User**, which is the user account which initiated the action. When this default option is applied, the [SdkMessageProcessingStep.ImpersonatingUserId](reference/entities/sdkmessageprocessingstep.md#BKMK_ImpersonatingUserId) will be set to null or <xref:System.Guid.Empty>.

More information: [Register plug-in step](register-plug-in.md#register-plug-in-step)

## During plug-in execution

You can override the setting specified at registration at run time by setting the <xref:Microsoft.Xrm.Sdk.IOrganizationServiceFactory>.<xref:Microsoft.Xrm.Sdk.IOrganizationServiceFactory.CreateOrganizationService(System.Nullable{System.Guid})> `userId` parameter.

This is typically set to the <xref:Microsoft.Xrm.Sdk.IExecutionContext>.<xref:Microsoft.Xrm.Sdk.IExecutionContext.UserId> value which will apply the user account defined by the plug-in step registration.

```csharp
(IOrganizationServiceFactory)serviceProvider.GetService(typeof(IOrganizationServiceFactory));
    IOrganizationService service = serviceFactory.CreateOrganizationService(context.UserId);
```

If you want to override the step registration you can pass the value of the <xref:Microsoft.Xrm.Sdk.IExecutionContext>.<xref:Microsoft.Xrm.Sdk.IExecutionContext.InitiatingUserId> to have a service that will use the user account that initiated the action that caused the plug-in to run.

You can also provide the [SystemUser.SystemUserId](reference/entities/systemuser.md#BKMK_SystemUserId) from any valid user account. This will work as long as that user has the permissions to perform the operations in the plug-in.

### See also

[Plug-ins](plug-ins.md)  
[Write a plug-in](write-plug-in.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]