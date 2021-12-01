---
title: "Global Discovery Service Sample (C#) (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to access the global Discovery Service using the OData V4 RESTful API" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 07/15/2021
ms.service: powerapps
ms.topic: "article"
author: "JimDaly" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
ms.reviewer: "pehecke"
manager: "kvivek" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Global Discovery Service Sample (C#)

[!INCLUDE[cc-terminology](../../includes/cc-terminology.md)]

This sample shows how to access the global Discovery Service using the Web API.

## How to run this sample

The sample source code is available on Github at [PowerApps-Samples](https://github.com/Microsoft/PowerApps-Samples)/cds/webapi/C#/GlobalDiscovery.

To run the sample:
1. Download or clone the sample so that you have a local copy.
2. Open the project solution file in Visual Studio.
3. Press F5 to build and run the sample.

## What this sample does

When run, the sample opens a logon form where you must specify the Microsoft Dataverse credentials for an enabled user. The program then displays to the console window a list of Dataverse environment instances that the specified user is a member of.

Other important aspects of this sample include:
1. Handles breaking API changes in different versions of Azure Active Directory Authentication Library (ADAL)
1. No dependency on helper code or a helper library since all required code, including authentication code, is provided.

## How this sample works

This sample uses an HttpClient to authenticate the specified user using ADAL, and then calls the global Discovery Service to return information about available Dataverse environment instances the user is a member of.

### Demonstrates

The sample depends on the `GetInstances` method and the `Instance` class below:

```csharp
/// <summary>
/// Uses the global discovery service to return environment instances
/// </summary>
/// <param name="username">The user name</param>
/// <param name="password">The password</param>
/// <returns>A list of Instances</returns>
static List<Instance> GetInstances(string username, string password)
{

    string GlobalDiscoUrl = "https://globaldisco.crm.dynamics.com/";
    HttpClient client = new HttpClient();
    client.DefaultRequestHeaders.Authorization = 
        new AuthenticationHeaderValue("Bearer", GetAccessToken(username, password, 
        new Uri("https://disco.crm.dynamics.com/api/discovery/")));
    client.Timeout = new TimeSpan(0, 2, 0);
    client.BaseAddress = new Uri(GlobalDiscoUrl);

    HttpResponseMessage response = 
        client.GetAsync("api/discovery/v2.0/Instances", HttpCompletionOption.ResponseHeadersRead).Result;

    if (response.IsSuccessStatusCode)
    {
        //Get the response content and parse it.
        string result = response.Content.ReadAsStringAsync().Result;
        JObject body = JObject.Parse(result);
        JArray values = (JArray)body.GetValue("value");

        if (!values.HasValues)
        {
            return new List<Instance>();
        }

        return JsonConvert.DeserializeObject<List<Instance>>(values.ToString());
    }
    else
    {
        throw new Exception(response.ReasonPhrase);
    }
}
```


```csharp
/// <summary>
  /// Object returned from the Discovery Service.
  /// </summary>
  class Instance
  {
    public string Id { get; set; }
    public string UniqueName { get; set; }
    public string UrlName { get; set; }
    public string FriendlyName { get; set; }
    public int State { get; set; }
    public string Version { get; set; }
    public string Url { get; set; }
    public string ApiUrl { get; set; }
    public DateTime LastUpdated { get; set; }
  }
```

## See Also

[Discover the URL for your organization](../discover-url-organization-web-api.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
