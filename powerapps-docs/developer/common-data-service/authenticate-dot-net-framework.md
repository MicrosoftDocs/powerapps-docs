---
title: "Authentication with .NET Framework applications (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "How .NET Framework applications can authenticate with Common Data Service for Apps" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 10/31/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "paulliew" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Authentication with .NET Framework applications

If you are using the .NET Framework you can use classes within the [Xrm.Tooling](/dotnet/api/?view=dynamics-xrmtooling-ce-9) namespace to authenticate and connect to the Organization service and the Web Api.

With `Xrm.Tooling` classes you can use the SDK assemblies using the <xref:Microsoft.Xrm.Sdk.IOrganizationService> interface methods. This is the same style of programming used by plug-ins and workflow activities, making it one style that you can use everywhere for .NET Framework applications.

With the `Xrm.Tooling` classes, use the <xref:Microsoft.Xrm.Tooling.Connector>.<xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient> class.

> [!NOTE]
> You may find older code or samples using the low-level <xref:Microsoft.Xrm.Sdk.Client.OrganizationServiceProxy> or <xref:Microsoft.Xrm.Sdk.WebServiceClient.OrganizationWebProxyClient> classes. These remain supported and are not deprecated, but we recommend you use <xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient> for new .NET Framework Client Applications.

The `Xrm.Tooling` classes provide many benefits including:
- You can define connection information using a connection string.
- Supports both OAuth and Office 365 claims-based authentication.
- Thread safety for actions performed in a multithreaded environment. 
- A common Windows Presentation Foundation (WPF) login control for a consistent sign-in experience from your Windows client applications.
- Supports for secure storage of the sign-in credentials and reuse of the stored credentials to automatically sign in after initial sign in.
- Built-in diagnostic tracing and performance reporting of the actions performed, which you can configure based on your organization’s requirements.
- Support for X.509 certificate authentication.

The `Xrm.Tooling` classes are optimized to use the <xref:Microsoft.Xrm.Sdk.IOrganizationService> interface methods. 

If you want to use the Web API, you can use the <xref:Microsoft.Xrm.Tooling.Connector>.<xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient>.<xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient.ExecuteCrmWebRequest*> method to compose requests using the Web API with all the other benefits provided with the `Xrm.Tooling` classes as long as you use OAuth.

More information: [Build Windows client applications using the XRM tools](xrm-tooling/build-windows-client-applications-xrm-tools.md)


## .NET Framework versions

Use .NET Framework version 4.6.2 or higher when you create client applications. Only applications using Transport Level Security (TLS) 1.2 or better security can connect. TLS 1.2 is not the default protocol used by .NET Framework 4.5.2, but it is in .NET Framework 4.6.2.

> [!NOTE]
> **Known Issue with Visual Studio 2015**
> 
> When you are running your project/solution in VS 2015 in debug mode, you may not be able to connect. This happens regardless of whether you are using a Target Framework of 4.6.2 or higher. This can occur because the Visual Studio hosting process is compiled against .NET 4.5 which means by default it does not support TLS 1.2. You can disable the Visual Studio hosting process as a work around. 
>
> Right-click on the name of your project in Visual Studio and then click **Properties**. On the **Debug** tab you can uncheck the **Enable the Visual Studio hosting process** option. 
>
> This only impacts the debug experience in VS 2015. This does not impact the binaries or executable that are built. The same issue does not occur in Visual Studio 2017.

> [!IMPORTANT]
> When developing Plug-in and workflow activity assemblies, which do not require authentication, you must use .NET Framework 4.5.2

## .NET Framework applications without SDK assemblies

If you prefer to not have a dependency on any SDK assemblies, you can also use the patterns described in [Use OAuth with Common Data Service for apps](authenticate-oauth.md) without taking a dependency on any SDK assemblies. Without the SDK assemblies, you can only use the OData Restful web services (Web API and OData Global Discovery Service). The [Web API Data operations Samples (C#)](webapi/web-api-samples-csharp.md) demonstrate this approach.

### See also

[Authentication with Common Data Service for Apps web services](authentication.md)<br />
[Use OAuth with Common Data Service for apps](authenticate-oauth.md)

