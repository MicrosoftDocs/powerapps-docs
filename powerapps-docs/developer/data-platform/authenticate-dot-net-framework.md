---
title: "Authenticating .NET applications (Microsoft Dataverse) | Microsoft Docs"
description: "Provides an overview of .NET based application authentication with Microsoft Dataverse web services." 
ms.custom: ""
ms.date: 07/02/2026
ms.reviewer: "pehecke"

ms.topic: concept-article
author: "paulliew" # GitHub ID
ms.subservice: dataverse-developer
ms.author: "jdaly" # MSFT alias of Microsoft employees only
search.audienceType: 
  - developer
---

# Authenticating .NET applications

This article provides guidance for developing applications coded and built by using .NET.

## .NET Framework applications

When you use the .NET Framework to develop your application, use classes in the [Xrm.Tooling](/dotnet/api/) namespace to easily authenticate and connect to the Microsoft Dataverse web services.

`Xrm.Tooling` classes in the SDK assemblies use the <xref:Microsoft.Xrm.Sdk.IOrganizationService> interface methods. This programming style is the same style used by plug-ins and workflow activities, so you can use it everywhere for .NET Framework applications. Use the <xref:Microsoft.Xrm.Tooling.Connector>.<xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient> class for web service connection.

The `Xrm.Tooling` classes provide many benefits, including:
- You can define connection information by using a connection string.
- Supports both OAuth and Microsoft 365 claims-based authentication.
- Thread safety for actions performed in a multithreaded environment.
- Provides a common Windows Presentation Foundation (WPF) sign-in control for a consistent sign-in experience from your Windows client applications.
- Support for secure storage of the sign-in credentials and reuse of the stored credentials to automatically sign in after initial sign in.
- Built-in diagnostic tracing and performance reporting of the actions performed, which you can configure based on your organization's requirements.
- Support for X.509 certificate authentication.

The `Xrm.Tooling` classes are optimized to use the <xref:Microsoft.Xrm.Sdk.IOrganizationService> interface methods.

If you want to use the Web API, you can use the <xref:Microsoft.Xrm.Tooling.Connector>.<xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient>.<xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient.ExecuteCrmWebRequest*> method to compose requests by using the Web API with all the other benefits provided by the `Xrm.Tooling` classes as long as you use OAuth.

More information: [Build Windows client applications using the XRM tools](xrm-tooling/build-windows-client-applications-xrm-tools.md)


### .NET Framework versions

Use a [supported .NET Framework version](supported-customizations.md#support-for-net-framework-versions) when you create new client applications.

### .NET Framework applications without using SDK assemblies

If you prefer not to depend on any SDK assemblies, you can use the patterns described in [Use OAuth with Microsoft Dataverse](authenticate-oauth.md) without taking a dependency on any SDK assemblies. Without the SDK assemblies, you can only use the OData Restful web services (Web API and OData Global Discovery Service). The [Web API Data operations Samples (C#)](webapi/web-api-samples-csharp.md) demonstrate this approach.

## .NET Core applications

The SDK APIs available in [Microsoft.CrmSdk.XrmTooling.CoreAssembly](https://www.nuget.org/packages/Microsoft.CrmSdk.XrmTooling.CoreAssembly/) and other "crmsdk" owned NuGet packages don't support .NET Core code development.

For .NET Core application development, there's a `DataverseServiceClient` class that's patterned after the `CrmServiceClient` class mentioned previously. You can download the [Microsoft.PowerPlatform.Dataverse.Client](https://www.nuget.org/packages/Microsoft.PowerPlatform.Dataverse.Client/) package from NuGet.org to begin using this new service client class in your applications. Documentation and sample code for the `DataverseServiceClient` and related classes will be made available in a future documentation release.

To update existing .NET Framework based application code that uses `CrmServiceClient`, substitute the `DataverseServiceClient` class for `CrmServiceClient` in your code. Set the project type to build a .NET Core application, remove any .NET Framework specific references and NuGet packages, and then add the Microsoft.PowerPlatform.Dataverse.Client package to the project.

### See also

[Authentication with Dataverse web services](authentication.md)<br />
[Use OAuth with Dataverse](authenticate-oauth.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
