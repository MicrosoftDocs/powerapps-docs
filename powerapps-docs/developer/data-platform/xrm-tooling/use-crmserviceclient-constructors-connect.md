---
title: "Use CrmServiceClient constructors to connect to Microsoft Dataverse (Dataverse)| Microsoft Docs"
description: "You can create an instance of the CrmServiceClient class, and then use one of the constructors to connect to Microsoft Dataverse"
ms.date: 04/01/2022
author: MattB-msft
ms.author: mbarbour
ms.reviewer: pehecke
ms.topic: article
applies_to: 
  - "Dynamics 365 (online)"
search.audienceType: 
  - developer
contributors: 
  - JimDaly
  - phecke 
---
# Use CrmServiceClient constructors to connect to Microsoft Dataverse

Use the various constructors to create an instance of the <xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient> class to connect to Dataverse. More information: [CrmServiceClient Constructors](/dotnet/api/microsoft.xrm.tooling.connector.crmserviceclient.-ctor)

The [connection string](/dotnet/api/microsoft.xrm.tooling.connector.crmserviceclient.-ctor#Microsoft_Xrm_Tooling_Connector_CrmServiceClient__ctor_System_String_) constructor is the most easy, convenient way to get an instance of the <xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient> class. More information: [Use connection strings in XRM tooling to connect to Dataverse](use-connection-strings-xrm-tooling-connect.md)

> [!NOTE]
> Consider using the new `ServiceClient` class that brings in enhancements over the `CrmServiceClient` class, such as .NET cross-platform application support, MSAL authentication, ILogger support, and performance benefits. More information: [Transition client applications to Dataverse ServiceClient](../sdk-client-transition.md)

## See also

[ServiceClient Constructors](/dotnet/api/microsoft.powerplatform.dataverse.client.serviceclient.-ctor)  
[Use XRM Tooling Windows PowerShell Cmdlets to connect to Dataverse](use-powershell-cmdlets-xrm-tooling-connect.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
