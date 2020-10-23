---
title: "IOrganizationService Interface (Common Data Service) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn about the common methods exposed to perform data operations with Common Data Service." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 10/31/2018
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
# IOrganizationService Interface

[!INCLUDE[cc-data-platform-banner](../../../includes/cc-data-platform-banner.md)]

The <xref:Microsoft.Xrm.Sdk.IOrganizationService> interface provides a set of methods used to perform the most common operations on system and custom entities and on the metadata for your organization.

## Client applications

This interface is implemented in a number of classes that you can use in your code when creating client applications.

|Class|Description|
|--|--|
|<xref:Microsoft.Xrm.Sdk.Client.OrganizationServiceProxy>|This is the original low-level class which is used by WCF and the SOAP endpoint |
|<xref:Microsoft.Xrm.Sdk.WebServiceClient.OrganizationWebProxyClient>|This low-level class was created to enable OAuth authentication to the SOAP endpoint|
|<xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient>|This is the class you should use when creating .NET client applications. |

> [!NOTE]
> You may find older code or samples using the low-level <xref:Microsoft.Xrm.Sdk.Client.OrganizationServiceProxy> or <xref:Microsoft.Xrm.Sdk.WebServiceClient.OrganizationWebProxyClient> classes, but we recommend you use <xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient> for new .NET Client Applications

## Plug-ins

When you write plug-ins, there is also an object returned from the <xref:Microsoft.Xrm.Sdk.IOrganizationServiceFactory>.<xref:Microsoft.Xrm.Sdk.IOrganizationServiceFactory.CreateOrganizationService(System.Nullable{System.Guid})> which implements the <xref:Microsoft.Xrm.Sdk.IOrganizationService> interface but is not any of the types in the classes above.

## IOrganizationService Methods

Each of the classes which implement the <xref:Microsoft.Xrm.Sdk.IOrganizationService> interface may include additional properties and methods, but the <xref:Microsoft.Xrm.Sdk.IOrganizationService> interface has just 8 methods.


|Method  |Description  |
|---------|---------|
|<xref:Microsoft.Xrm.Sdk.IOrganizationService.Associate*>|Link two entities using an entity relationship|
|<xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|Create an entity record.|
|<xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|Delete an entity record|
|<xref:Microsoft.Xrm.Sdk.IOrganizationService.Disassociate*>|Remove the link between two entities using an entity relationship|
|<xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute*>|Invoke an operation defined as a message by passing an instance of an <xref:Microsoft.Xrm.Sdk.OrganizationRequest> or a class derived from it.|
|<xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|Retrieve an instance of an entity record.|
|<xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|Retrieve a collection of entity records that match the criteria set in a query.|
|<xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|Change the attribute values of an entity record.|

> [!NOTE]
> The Organization service exposes only the `Execute` method. The other methods in the <xref:Microsoft.Xrm.Sdk.IOrganizationService> interface are simply wrappers around the `Execute` method. These other methods are provided for convenience. You can perform all operations using only the `Execute` method. More information: [Use messages with the Organization service](use-messages.md)

## See also

[Use messages with the Organization service](use-messages.md)<br />
[Write a plug-in](../write-plug-in.md)<br />
[Entity Operations using the Organization service](entity-operations.md)
