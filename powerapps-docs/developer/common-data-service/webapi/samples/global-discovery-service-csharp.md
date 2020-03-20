---
title: "Global Discovery Service Sample (C#) (Common Data Service) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to access the global Discovery Service using the OData V4 RESTful API" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 1/16/2020
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

This sample shows how to access the Discovery Service using the OData V4 RESTful API.

## How to run this sample

This sample is available on Github at [https://github.com/Microsoft/PowerApps-Samples/tree/master/cds/webapi/C%23/GlobalDiscovery](https://github.com/Microsoft/PowerApps-Samples/tree/master/cds/webapi/C%23/GlobalDiscovery)

## What this sample does''
''
This sample returns the available Common Data Service instances for a given user credential.

## How this sample works

This sample will use credential information in the App.config file, but will not use the URL configured in the connection string.
Instead, it will just use the user credentials and the clientid.
''''''''''''
### Demonstrates

This sample uses a HttpClient to authenticate using ADAL (v2.29) and call the Discovery Service to return information about available instances the user can connect to.

The sample depends on the `GetInstances` method and the `Instance` class below:

```csharp    
    /// <summary>
    /// Uses the Discovery Service to return organization instances.
    /// </summary>
    /// <param name="clientId">The Azure AD client (app) registration</param>
    /// <param name="username">The user name</param>
    /// <param name="password">The password</param>
    /// <returns>A List of Instances</returns>
    static List<Instance> GetInstances(string clientId, string username, string password)
    {

      string GlobalDiscoUrl = "https://globaldisco.crm.dynamics.com/";
      AuthenticationContext authContext = new AuthenticationContext("https://login.microsoftonline.com", false);

      UserCredential cred = new UserCredential(username, password);
      AuthenticationResult authResult = authContext.AcquireToken(GlobalDiscoUrl, clientId, cred);
'
      HttpClient client = new HttpClient();
      client.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", authResult.AccessToken);
      client.Timeout = new TimeSpan(0, 2, 0);
      client.BaseAddress = new Uri(GlobalDiscoUrl);

      HttpResponseMessage response = client.GetAsync("api/discovery/v2.0/Instances", HttpCompletionOption.ResponseHeadersRead).Result;


      if (response.IsSuccessStatusCode)
      {
        //Get the response content and parse it.
        string result = response.Content.ReadAsStringAsync().Result;
        JObject body = JObject.Parse(result);
        JArray values = (JArray)body.GetValue("value");''

        if (!values.HasValues)
        {
          return new List<Instance>();
        }'

        return JsonConvert.DeserializeObject<List<Instance>>(values.ToString());
      }'
      else
      {
        throw new Exception(response.ReasonPhrase);
      }'
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

                                                                                                                    '''