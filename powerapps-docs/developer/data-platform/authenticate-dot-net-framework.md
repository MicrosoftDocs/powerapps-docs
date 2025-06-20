---
title: "Authenticating .NET applications (Microsoft Dataverse) | Microsoft Docs" 
description: "Provides an overview of .NET based application authentication with Microsoft Dataverse web services." 
ms.custom: ""
ms.date: 01/06/2022
ms.reviewer: "pehecke"

ms.topic: concept-article
author: "paulliew" 
ms.subservice: dataverse-developer
ms.author: "jdaly"
search.audienceType: 
  - developer
---

# Authenticating .NET applications

This topic provides guidance when developing applications coded and built using .NET.

## .NET Framework applications

If you are using the .NET Framework when developing your application you can use classes within the [Xrm.Tooling](/dotnet/api/) namespace to easily authenticate and connect to the Microsoft Dataverse web services.

`Xrm.Tooling` classes in the SDK assemblies use the <xref:Microsoft.Xrm.Sdk.IOrganizationService> interface methods. This is the same style of programming used by plug-ins and workflow activities, making it one style that you can use everywhere for .NET Framework applications. We recommend using the <xref:Microsoft.Xrm.Tooling.Connector>.<xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient> class for web service connection.

The `Xrm.Tooling` classes provide many benefits including:
- You can define connection information using a connection string.
- Supports both OAuth and Microsoft 365 claims-based authentication.
- Thread safety for actions performed in a multi-threaded environment.
- Provides a common Windows Presentation Foundation (WPF) login control for a consistent sign-in experience from your Windows client applications.
- Support for secure storage of the sign-in credentials and reuse of the stored credentials to automatically sign in after initial sign in.
- Built-in diagnostic tracing and performance reporting of the actions performed, which you can configure based on your organization’s requirements.
- Support for X.509 certificate authentication.

The `Xrm.Tooling` classes are optimized to use the <xref:Microsoft.Xrm.Sdk.IOrganizationService> interface methods.

If you want to use the Web API, you can use the <xref:Microsoft.Xrm.Tooling.Connector>.<xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient>.<xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient.ExecuteCrmWebRequest*> method to compose requests using the Web API with all the other benefits provided with the `Xrm.Tooling` classes as long as you use OAuth.

More information: [Build Windows client applications using the XRM tools](xrm-tooling/build-windows-client-applications-xrm-tools.md)


### .NET Framework versions

Use .NET Framework version 4.6.2 or higher when you create client applications. Only applications using Transport Level Security (TLS) 1.2 or better security can connect. TLS 1.2 is not the default protocol used by .NET Framework 4.5.2, but it is in .NET Framework 4.6.2 or later.

### .NET Framework applications without using SDK assemblies

If you prefer to not have a dependency on any SDK assemblies, you can also use the patterns described in [Use OAuth with Microsoft Dataverse](authenticate-oauth.md) without taking a dependency on any SDK assemblies. Without the SDK assemblies, you can only use the OData Restful web services (Web API and OData Global Discovery Service). The [Web API Data operations Samples (C#)](webapi/web-api-samples-csharp.md) demonstrate this approach.

## .NET Core and .NET 6 applications

The SDK APIs available in [Microsoft.CrmSdk.XrmTooling.CoreAssembly](https://www.nuget.org/packages/Microsoft.CrmSdk.XrmTooling.CoreAssembly/) and other "crmsdk" owned NuGet packages do not support .NET Core code development.

For .NET Core application development there is a `DataverseServiceClient` class, that is patterned after the `CrmServiceClient` class mentioned previously. You can download the [Microsoft.PowerPlatform.Dataverse.Client](https://www.nuget.org/packages/Microsoft.PowerPlatform.Dataverse.Client/) package from Nuget.org to begin using this new service client class in your applications. Documentation and sample code for the `DataverseServiceClient` and related classes will be made available in a future documentation release.

To update existing .NET Framework based application code that uses `CrmServiceClient`, begin by substituting the `DataverseServiceClient` class for `CrmServiceClient` in your code. You will need to set the project type to build a .NET Core application, remove any .NET Framework specific references and NuGet packages, and then add the Microsoft.PowerPlatform.Dataverse.Client package to the project.

### See also

[Authentication with Dataverse web services](authentication.md)<br />
[Use OAuth with Dataverse](authenticate-oauth.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
