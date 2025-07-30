---
title: "IOrganizationService Interface (Microsoft Dataverse) | Microsoft Docs"
description: "Learn about the common web service methods exposed to perform data operations in Microsoft Dataverse." 
ms.collection: get-started
ms.date: 06/20/2025
ms.reviewer: pehecke
ms.topic: article
author: MsSQLGirl
ms.author: jukoesma
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

A couple of classes that you can use in your code when creating client applications implement the `IOrganizationService` interface:

|Class|Description|
|--|--|
|<xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient>|This is the class you should use when creating .NET Framework client applications. |
|<xref:Microsoft.PowerPlatform.Dataverse.Client.ServiceClient>|This is the class you should use when creating .NET Framework or .NET Core client applications. |

## Plug-ins

When you write plug-ins, there's also an object returned from the [IOrganizationServiceFactory.CreateOrganizationService method](xref:Microsoft.Xrm.Sdk.IOrganizationServiceFactory.CreateOrganizationService(System.Nullable{System.Guid})) that implements the <xref:Microsoft.Xrm.Sdk.IOrganizationService> interface but isn't any of the types in the client classes described in the previous section.

## IOrganizationService Methods

Each of the classes that implement the <xref:Microsoft.Xrm.Sdk.IOrganizationService> interface might include additional properties and methods, but the <xref:Microsoft.Xrm.Sdk.IOrganizationService> interface has just eight methods.


|Method  |Description  |
|---------|---------|
|<xref:Microsoft.Xrm.Sdk.IOrganizationService.Associate%2A>|Link two table rows using a table relationship|
|<xref:Microsoft.Xrm.Sdk.IOrganizationService.Create%2A>|Create a table row.|
|<xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete%2A>|Delete a table row|
|<xref:Microsoft.Xrm.Sdk.IOrganizationService.Disassociate%2A>|Remove the link between two table rows using a table relationship|
|<xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute%2A>|Invoke an operation defined as a message by passing an instance of an <xref:Microsoft.Xrm.Sdk.OrganizationRequest> or a class derived from it.|
|<xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve%2A>|Retrieve an instance of a table row.|
|<xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple%2A>|Retrieve a collection of table rows that match the criteria set in a query.|
|<xref:Microsoft.Xrm.Sdk.IOrganizationService.Update%2A>|Change the column values of a table row.|

> [!NOTE]
> The Organization service exposes only the `Execute` method. The other methods in the <xref:Microsoft.Xrm.Sdk.IOrganizationService> interface are simply wrappers around the `Execute` method. These other methods are provided for convenience. You can perform all operations using only the `Execute` method. More information: [Use messages with the SDK for .NET](use-messages.md)

## See also

[Use messages with the SDK for .NET](use-messages.md)<br />
[Write a plug-in](../write-plug-in.md)<br />
[Entity class operations using the SDK for .NET](entity-operations.md)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
