---
title: "Bypass Custom Business Logic (Microsoft Dataverse) | Microsoft Docs" 
description: "Make data changes which bypass custom business logic" 
ms.custom: ""
ms.date: 01/04/2021
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "JimDaly" 
ms.author: "jdaly" 
manager: "ryjones" 
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Bypass Custom Business Logic

There are times when you want to be able to perform data operations without having custom business logic applied. For example, if you are going to import a lot of records which you know already conform to the data consistency logic for your business. You want this operation to be done as quickly as possible, so the additional time spent processing custom logic for each request is something you want to avoid.  

For these kinds of situations, you have the option to disable custom business logic which would normally be applied. There are two requirements:

1. You must send the requests using the `BypassCustomPluginExecution` option.
1. The user sending the requests must have the `prvByPassPlugins` privilege. By default, only users with the system administrator security role have this privilege.

## What does this do?

This solution targets the custom business logic that has been applied for your organization. When you send requests that bypass custom business logic, all plug-ins and workflows are disabled except:

1. Plug-ins which are part of the core Dataverse system or part of a solution shipped by Microsoft.
1. Workflows included in a solution where Microsoft is the publisher.

System plug-ins define the core behaviors for specific entities. Without these plug-ins you would encounter data inconsistencies that may not be easily fixed.

Solutions shipped by Microsoft that use Dataverse such as Microsoft Dynamics 365 Customer Service, or Dynamics 365 Sales also include critical business logic that cannot be bypassed with this option.

> [!IMPORTANT]
> You may have purchased and installed solutions from other Independant Software Vendors (ISVs) which include their own business logic. The logic applied by these solutions will be bypassed. You should check with these ISVs before you use this option to understand what impact there may be if you use this option with data that their solutions use.

## How do I use the BypassCustomPluginExecution option?

You can use this option with either the Web API or the Organization service.

### Using the Web API

To apply this option using the Web API, pass `MSCRM.BypassCustomPluginExecution : true` as a header in the request.


### Using the Organization Service

To apply this option using the Organization Service, set the [CrmServiceClient.BypassPluginExecution Property](/dotnet/api/microsoft.xrm.tooling.connector.crmserviceclient.bypasspluginexecution) to true.

## Frequently asked questions (FAQ)

### Does this bypass plug-ins for records created by Microsoft plug-ins?

No. If a plug-in or workflow in a Microsoft solution performs operations on other records, the plug-ins for those operations are not bypassed. Only those plugins or workflows that apply to the specific first level operation will be bypassed.

### Can I use this option for data operations I perform within a plug-in?

No. Plug-ins cannot use the Web API, they must use the Organization Service. Specifically, they use the methods exposed by the [IOrganizationService Interface](org-service/iorganizationservice-interface.md). There is no way to set this option from within a plug-in.

### Why was this only exposed for the CrmServiceClient class?

There are other older proxy classes that expose the IOrganizationService interface: [OrganizationServiceProxy Class](/dotnet/api/microsoft.xrm.sdk.client.organizationserviceproxy?view=dynamics-general-ce-9) and [OrganizationWebProxyClient Class](/dotnet/api/microsoft.xrm.sdk.webserviceclient.organizationwebproxyclient?view=dynamics-general-ce-9). This option is only available for the [CrmServiceClient Class](/dotnet/api/microsoft.xrm.tooling.connector.crmserviceclient) because we recommend using this class rather than the older classes when creating client applications.


