---
title: "Use the PowerApps checker web API | Microsoft Docs"
description: "The PowerApps checker Web API provides a development experience that can be used across a wide variety of programming languages, platforms, and devices"
ms.custom: ""
ms.date: 06/3/2019
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
ms.assetid: 0d5f7579-304a-4d28-ba73-df30722205eb
caps.latest.revision: 1
author: "mhuguet" # GitHub ID
ms.author: "mhuguet"
ms.reviewer: "pehecke"
manager: "maustinjones"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Use the PowerApps checker web API

[!INCLUDE [cc-beta-prerelease-disclaimer](../../../../includes/cc-beta-prerelease-disclaimer.md)]

The PowerApps checker web API provides a mechanism to run static analysis checks against customizations and extensions to the Common Data Service platform. It is available for makers and developers to perform rich static analysis checks on their solutions against a set of best practice rules to quickly identify problematic patterns. The service provides the logic for the [solution checker feature](../../../../maker/common-data-service/use-powerapps-checker.md) in the PowerApps maker [portal](https://make.powerapps.com) and is included as part of the automation for [applications submitted to AppSource](../../publish-app-appsource.md). Interacting with the service directly in this manner allows for analysis of solutions that are included as part of on-premise (all supported versions) and online environments.

 > [!IMPORTANT]
 >
 > - The web API for PowerApps checker is a preview feature.
 > - [!INCLUDE[cc_preview_features_definition](../../../../includes/cc-preview-features-definition.md)]

<a name="bkmk_altApproaches"></a>

## Alternative approaches

Before reading through the details of how to interact at the lowest level with the web APIs, consider leveraging our PowerShell module, Microsoft.PowerApps.Checker.PowerShell, instead. It is a fully supported tool that is available in the [PowerShell Gallery](https://www.powershellgallery.com). The current restriction is that it does require Windows PowerShell. If unable to meet this requirement, then interacting with the APIs directly will likely be the best approach.

<a name="bkmk_getStarted"></a>

## Getting started

It is important to note that a solution analysis can result in a long running process. It can typically take sixty seconds to upwards of five minutes depending on a variety of factors, such as number, size, and complexity of customizations and code. The analysis flow is multi-step and asynchronous beginning with initiating an analysis job with the status API being used to query for job completion. An example flow for an analysis is as follows: 

1. Obtain an OAuth token
2. Call upload (for each file in parallel)
3. Call analyze (initiates the analysis job)
4. Call status until finished (looping with a pause in between calls until the end is signaled or thresholds are met)
5. Download the result(s) from the provided SAS URI

A few variations are:

- Include a lookup of the ruleset or rules as a pre-step. However, it would be slightly faster to pass in a configured or hard coded ruleset ID. It is recommended that you use a ruleset that meets your needs.
- You can opt to not use the upload mechanism (see the upload for limitations).

You will need to determine the following:

- [Which geography?](#determine-a-geography)
- [Which version?](#versioning)
- [Which rulesets and rules?](#rulesets-and-rules)
- [What is your tenant ID?](#find-your-tenant-id)

Refer to the following topics for documentation on the individual APIs:

[Retrieve the list of rulesets](retrieve-rulesets.md)<br />
[Retrieve the list of rules](retrieve-rules.md)<br />
[Upload a file](upload-file.md)<br />
[Invoke analysis](analyze.md)<br />
[Check for analysis status](check-status.md)<br />

<a name="bkmk_geo"></a>

## Determine a geography

When interacting with the PowerApps checker service, files are temporarily stored in Azure along with the reports that are generated. By using a geography specific API, you can control where the data is stored. It is suggested to use the same geography for each API call in the analysis lifecycle. Each geography may have a different version at any given point in time due to our multi-stage safe deployment approach and doing this ensures full version compatibility. It also may reduce execution time as the data will not have to travel as far of a distance in some cases. The following are the available geographies:

|Azure datacenter|Name|Geography|Base URI|
|---|---|---|---|
|Public|Preview|United States|unitedstatesfirstrelease.api.advisor.powerapps.com|
|Public|Production|United States|unitedstates.api.advisor.powerapps.com|
|Public|Production|Europe|europe.api.advisor.powerapps.com|
|Public|Production|Asia|asia.api.advisor.powerapps.com|
|Public|Production|Australia|australia.api.advisor.powerapps.com|
|Public|Production|Japan|japan.api.advisor.powerapps.com|
|Public|Production|India|india.api.advisor.powerapps.com|
|Public|Production|Canada|canada.api.advisor.powerapps.com|
|Public|Production|South America|southamerica.api.advisor.powerapps.com|
|Public|Production|United Kingdom|unitedkingdom.api.advisor.powerapps.com|

> [!NOTE]
>  You may choose to use the preview geography to incorporate the latest features and changes earlier. However, note that the preview uses United States Azure regions only.

<a name="bkmk_versioning"></a>

## Versioning

While not required, it is recommended to include the api-version query string parameter with the desired API version. The current API version is 1.0. For example, below is a ruleset HTTP request specifying to use the 1.0 API version:

`https://unitedstatesfirstrelease.api.advisor.powerapps.com/api/ruleset?api-version=1.0`

If not provided, the latest API version will be used by default. Using an explicit version number is recommended as the version will be incremented if breaking changes are introduced. If the version number is specified in a request, backward compatibility support in later (numerically greater) versions will be maintained.

<a name="bkmk_rules"></a>

## Rulesets and rules

PowerApps checker requires a list of rules when run. These rules can be provided in the form of individual rules or a grouping of rules, referred to as a *ruleset*. A ruleset is a convenient way to specify a group of rules instead of having to specify each rule individually. For example, the solution checker feature uses a ruleset named *Solution Checker*. As new rules are added or removed, the service will include these changes automatically without requiring any change by the consuming application. If you require that the list of rules not change automatically as described above, then the rules can be specified individually.
Rulesets can have one or more rules with no limit. A rule can be in no or multiple rulesets. You can get a list of all rulesets by calling the API as follows: `[Geographical URL]/api/ruleset`. This endpoint is open and does not require authentication.

### Solution checker ruleset

The solution checker ruleset contains a set of impactful rules that have limited chances for false positives. If running analysis against an existing solution, it is recommended that you start with this ruleset. This is the ruleset used by the [solution checker feature](../../../../maker/common-data-service/use-powerapps-checker.md).

### AppSource certification ruleset

When publishing applications on AppSource, you must get your application certified. [Applications published on AppSource](../../publish-app-appsource.md) are required to meet a high quality standard. The AppSource certification ruleset contains the rules that are part of the solution checker ruleset, plus additional rules to ensure only high quality applications are published on the store. Some of AppSource certification rules are more prone to false positives and may require additional attention to resolve.

<a name="bkmk_tenant"></a>

## Find your tenant ID

The ID of your tenant is needed to interact with the APIs that require a token. Refer to [this article](https://docs.microsoft.com/onedrive/find-your-office-365-tenant-id) for details on how to obtain the tenant ID. You can also use PowerShell commands to retrieve the tenant ID. The following example leverages the cmdlets in the [AzureAD module](https://docs.microsoft.com/powershell/module/azuread/?view=azureadps-2.0).

```powershell
# Login to AAD as your user
Connect-AzureAD

# Establish your tenant ID
$tenantId = (Get-AzureADTenantDetail).ObjectId
```

The tenant ID is the value of the `ObjectId` property that is returned from `Get-AzureADTenantDetail`. You may also see it after logging in using the Connect-AzureAD cmdlet in the cmdlet output. In this case it will be named `TenantId`.

<a name="bkmk_auth"></a>

## Authentication and authorization

 Querying for rules and rulesets do not require an OAuth token, but all of the other APIs do require the token. The APIs do support authorization discovery by calling any of the APIs that require a token. The response will be an unauthorized HTTP status code of 401 with a WWW-Authenticate header, the authorization URI, and the resource ID. You should also provide your tenant ID in the `x-ms-tenant-id` header. Refer to [PowerApps Checker authentication and authorization](/powershell/powerapps/overview#powerapps-checker-authentication-and-authorization) for more information. Below is an example of the response header returned from an API request:

```http
WWW-Authenticate →Bearer authorization_uri="https://login.microsoftonline.com/0082fff7-33c5-44c9-920c-c2009943fd1e", resource_id="https://api.advisor.powerapps.com/"
```

Once you have this information, you can choose to use the Azure Active Directory Authentication Library (ADAL) or some other mechanism to acquire the token. Below is an example of how this can be done using C# and the [ADAL library, version 4.5.1](https://www.nuget.org/packages/Microsoft.IdentityModel.Clients.ActiveDirectory/4.5.1):

```c#
// Call the status URI as it is the most appropriate to use with a GET.
// The GUID here is just random, but needs to be there.
Uri queryUri = new Uri($"{targetServiceUrl}/api/status/4799049A-E623-4B2A-818A-3A674E106DE5");
AuthenticationParameters authParams = null;

using (var client = new HttpClient())
{
    var request = new HttpRequestMessage(HttpMethod.Get, queryUri);
    request.Headers.Add("x-ms-tenant-id", tenantId.ToString());

    // NOTE - It is highly recommended to use async/await
    using (var response = client.SendAsync(request).GetAwaiter().GetResult())
    {
        if (response.StatusCode == System.Net.HttpStatusCode.Unauthorized)
        {
            // NOTE - It is highly recommended to use async/await
            authParams = AuthenticationParameters.CreateFromUnauthorizedResponseAsync(response).GetAwaiter().GetResult();
        }
        else
        {
            throw new Exception($"Unable to connect to the service for authorization information. {response.ReasonPhrase}");
        }
    }
}
```

Once you have acquired the token, it is advised that you provide the same token to subsequent calls in the request lifecycle. However, additional requests will likely warrant a new token be acquired for security reasons.

<a name="bkmk_transport"></a>

## Transport security
For best-in-class encryption, the checker service only supports communications using Transport Layer Security (TLS) 1.2 and above. For guidance on .NET best practices around TLS, refer to [Transport Layer Security (TLS) best practices with the .NET Framework](https://docs.microsoft.com/dotnet/framework/network-programming/tls).

<a name="bkmk_report"></a>

## Report format

The result of the solution analysis is a zip file containing one or more reports in a standardized JSON format. The report format is based on static analysis results referred to as Static Analysis Results Interchange Format (SARIF). There are tools available to view and interact with SARIF documents. Refer to this [web site](https://sarifweb.azurewebsites.net/) for details. The service leverages version two of the [OASIS standard](http://docs.oasis-open.org/sarif/sarif/v2.0/sarif-v2.0.html).


### See also

[Retrieve the list of rulesets](retrieve-rulesets.md)<br />
[Retrieve the list of rules](retrieve-rules.md)<br />
[Upload a file](upload-file.md)<br />
[Invoke analysis](analyze.md)<br />
[Check for analysis status](check-status.md)<br />