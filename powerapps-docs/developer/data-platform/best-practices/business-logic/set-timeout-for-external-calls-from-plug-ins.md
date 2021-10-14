---
title: "Set Timeout when making external calls in a plug-in | MicrosoftDocs"
description: "Limit the time period that external calls will expect a response within plug-ins"
services: ''
suite: powerapps
documentationcenter: na
author: JimDaly
manager: ryjones
editor: ''
tags: ''
ms.service: powerapps
ms.devlang: na
ms.topic: article
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 03/06/2021
ms.subservice: dataverse-developer
ms.author: jdaly
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Set Timeout when making external calls in a plug-in


**Category**: Performance

**Impact potential**: High

<a name='symptoms'></a>

## Symptoms

If a plug-in makes external web requests that fail to respond quickly, the plug-in will wait for the full default timeout period before failing. This duration may cause a long transaction that can effect other operations. If the plug-in is registered:

- Synchronously, users may experience:

    - Unresponsive model-driven apps
    - Slow client interactions
    - The browser stops responding

- Asynchronously, plug-in executions may take an extended period of time before failing. 

<a name='guidance'></a>

## Guidance

The default timeout value for .Net Http clients is 100 seconds, just 20 seconds short of the time available for the plug-in to complete. It is best to establish an expected baseline time that a calling service will respond. The longer it exceeds this normal response time, the higher the probability it will ultimately fail. As a performance best practice, it is best to fail quickly rather than allow the default timeout period to expire. You should control the period that your call to the external service will wait.

The timeout value you should set will depend on the service. For example, if you can monitor the performance of the service you may determine a duration where 99.999% of requests succeed and set your timeout period to that duration with a few seconds buffer. This will prevent the the occasional outliers from having an inordinate impact on the performance of your plug-in.

If you are using [System.Net.Http.HttpClient Class](/dotnet/api/system.net.http.httpclient), you can set the `Timeout` value explicitly, as shown in this example setting the timeout to 15 seconds.

```csharp
using (HttpClient client = new HttpClient())
{
  client.Timeout = TimeSpan.FromMilliseconds(15000); //15 seconds
  client.DefaultRequestHeaders.ConnectionClose = true; //Set KeepAlive to false
  

  HttpResponseMessage response =  client.GetAsync(webAddress).ConfigureAwait(false).GetAwaiter().GetResult(); //Make sure it is synchronous
  response.EnsureSuccessStatusCode();

  string responseText = response.Content.ReadAsStringAsync().ConfigureAwait(false).GetAwaiter().GetResult(); //Make sure it is synchronous
  tracingService.Trace(responseText);
  //Log success in the Plugin Trace Log:
  tracingService.Trace("HttpClientPlugin completed successfully.");
}
```

If you are using [System.Net.WebClient Class](/dotnet/api/system.net.webclient), you need to create a derived class and override the base [GetWebRequest Method](/dotnet/api/system.net.webclient.getwebrequest) to set the timeout:

```csharp
  /// <summary>
  /// A class derived from WebClient with 15 second timeout and KeepAlive disabled
  /// </summary>
  public class CustomWebClient : WebClient
  {
    protected override WebRequest GetWebRequest(Uri address)
    {
      HttpWebRequest request = (HttpWebRequest)base.GetWebRequest(address);
      if (request != null)
      {
        request.Timeout = 15000; //15 Seconds
        request.KeepAlive = false;
      }
      return request;
    }
  }
```

Then you can use this class in your plug-in code:

```csharp
using (CustomWebClient client = new CustomWebClient())
{
  byte[] responseBytes = client.DownloadData(webAddress);
  string response = Encoding.UTF8.GetString(responseBytes);
  tracingService.Trace(response);
  //Log success in the Plugin Trace Log:
  tracingService.Trace("WebClientPlugin completed successfully.");
}
```

<a name='seealso'></a>

### See also

[Sample: Web access from a sandboxed plug-in](../../org-service/samples/web-access-plugin.md)<br />
[Set KeepAlive to false when interacting with external hosts in a plug-in](set-keepalive-false-interacting-external-hosts-plugin.md)


[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]