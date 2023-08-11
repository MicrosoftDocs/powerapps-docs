---
title: "IOrganizationService Interface (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn about the common web service methods exposed to perform data operations in Microsoft Dataverse." # 115-145 characters including spaces. This abstract displays in the search result.
ms.collection: get-started
ms.date: 09/30/2022
ms.reviewer: "pehecke"
ms.topic: "article"
author: "divkamath" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
search.audienceType: 
  - developer
contributors:
  - phecke
  - JimDaly
---

# IOrganizationService Interface

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

The <xref:Microsoft.Xrm.Sdk.IOrganizationService> interface exposes methods used to perform web service operations on system and custom tables and on the table definitions (metadata) for your environment.

## Client applications

This interface is implemented by a couple of classes that you can use in your code when creating client applications.

|Class|Description|
|--|--|
|<xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient>|This is the class you should use when creating .NET Framework client applications. |
|<xref:Microsoft.PowerPlatform.Dataverse.Client.ServiceClient>|This is the class you should use when creating .NET Framework or .NET Core client applications. |

## Plug-ins

When you write plug-ins, there is also an object returned from the <xref:Microsoft.Xrm.Sdk.IOrganizationServiceFactory>.<xref:Microsoft.Xrm.Sdk.IOrganizationServiceFactory.CreateOrganizationService(System.Nullable{System.Guid})> which implements the <xref:Microsoft.Xrm.Sdk.IOrganizationService> interface but is not any of the types in the service client classes above.

## IOrganizationService Methods

Each of the classes which implement the <xref:Microsoft.Xrm.Sdk.IOrganizationService> interface may include additional properties and methods, but the <xref:Microsoft.Xrm.Sdk.IOrganizationService> interface has just 8 methods.


|Method  |Description  |
|---------|---------|
|<xref:Microsoft.Xrm.Sdk.IOrganizationService.Associate*>|Link two table rows using a table relationship|
|<xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|Create a table row.|
|<xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|Delete a table row|
|<xref:Microsoft.Xrm.Sdk.IOrganizationService.Disassociate*>|Remove the link between two table rows using a table relationship|
|<xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute*>|Invoke an operation defined as a message by passing an instance of an <xref:Microsoft.Xrm.Sdk.OrganizationRequest> or a class derived from it.|
|<xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|Retrieve an instance of a table row.|
|<xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|Retrieve a collection of table rows that match the criteria set in a query.|
|<xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|Change the column values of a table row.|

> [!NOTE]
> The Organization service exposes only the `Execute` method. The other methods in the <xref:Microsoft.Xrm.Sdk.IOrganizationService> interface are simply wrappers around the `Execute` method. These other methods are provided for convenience. You can perform all operations using only the `Execute` method. More information: [Use messages with the Organization service](use-messages.md)

## See also

[Use messages with the Organization service](use-messages.md)<br />
[Write a plug-in](../write-plug-in.md)<br />
[Entity class operations using the Organization service](entity-operations.md)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
