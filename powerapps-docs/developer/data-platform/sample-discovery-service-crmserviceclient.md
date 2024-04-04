---
title: "Sample: Use CrmServiceClient to access the Global Discovery Service (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample code shows how to use discovery services" # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 07/18/2022
author: JimDaly
ms.author: jdaly
ms.reviewer: pehecke
search.audienceType:
  - developer
contributors:
  - JimDaly
  - phecke
---

# Sample: Use CrmServiceClient to access the Global Discovery Service

This sample code shows how to use the discovery service with the <xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient.DiscoverGlobalOrganizations%2A?text=CrmServiceClient.DiscoverGlobalOrganizations Method>.

> [!div class="nextstepaction"]
> [SDK for .NET: Use CrmServiceClient to access the Global Discovery Service sample code](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/C%23/DiscoveryService)

> [!NOTE]
> This sample is limited to .NET Full Framework.
> There is a newer sample compatible with .NET Core using the <xref:Microsoft.PowerPlatform.Dataverse.Client.ServiceClient.DiscoverOnlineOrganizationsAsync%2A?text=Dataverse.Client.ServiceClient.DiscoverOnlineOrganizationsAsync Method>. See [Sample: Global Discovery Service (C#)](sample-global-discovery-service-csharp.md).

## How to run this sample

This sample will not open dialog to prompt you for connection information.

If you have set and values in the App.config connection strings, it will use them. Otherwise, set the `username` and `password` variables in the `SampleProgram.Main` method.

## What this sample does

This sample uses the SDK Assembly `CrmServiceClient` to query the global discovery service with a user's credentials to determine which environments they can connect with.

If one or more environments are returned, the sample will prompt the user to choose one, and then use a `WhoAmIRequest` to return the `SystemUser.UserId` for that environment.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

This sample requires no special setup except that there are valid user credential username and password to use.

If you know the regional data center that your environments are in, the sample will run faster if you set this value at line 40 of the SampleProgram.cs file.

In SampleMethods.cs there is a `Clouds` enumeration for each of the known global discovery centers. Each enumeration member is decorated with a `Description` notation. All of these members except `Unknown` have the URL for the global discovery service set as the description.

### Demonstrate

1. Using the user credentials and the `cloud` value, the program uses the `GetAllOrganizations` static method to retrieve all known environments for the user.
1. The `GetAllOrganizations`method detects whether the `cloud` value is set to `Cloud.Unknown`. If it is set to this member, this method will choose the commerical `Cloud` enum and retrieve any environments that are found using the `GetOrganizationsForCloud` static method.

   If a specific data center is set, `GetAllOrganizations` will simply call `GetOrganizationsForCloud` with those values.

1. The `GetOrganizationsForCloud` method extracts the cloud's discovery service Url from the member `Description` decoration and uses it together with the user credentials to execute the `DiscoverGlobalOrganizations` CrmServiceClient helper message.

   A `System.ServiceModel.Security.SecurityAccessDeniedException` is expected when the user has no environments in a specific data center.

1. If any environments are returned by the `GetAllOrganizations` method, they will be listed in the console and you will be prompted to choose one by typing a number. If your choice is valid, the selected environment data is used to execute a `WhoAmIRequest` and return the `SystemUser.UserId` for the user in that environment.

### Clean up

This sample creates no records. No cleanup is required.

### See Also

[Discover user organizations](discovery-service.md)<br />
[Sample: Global Discovery Service (C#)](sample-global-discovery-service-csharp.md)<br />
[Sample: Blazor WebAssembly with Global Discovery](sample-blazor-web-assembly-global-discovery.md)

[!INCLUDE [footer-banner](../../includes/footer-banner.md)]
