---
title: "Access external web services (Microsoft Dataverse) | MicrosoftDocs"
description: "Learn how to access a web service from a custom plug-in or workflow activity."
ms.custom: ""
ms.date: 01/24/2025
ms.reviewer: "pehecke"
ms.topic: "article"
author: MicroSri
ms.subservice: dataverse-developer
ms.author: "pehecke"
search.audienceType: 
  - developer
contributors:
  - PHecke
---
# Access external web services

Plug-ins and custom workflow activities can access the network through the HTTP and HTTPS protocols. This capability provides support for accessing popular web services like social sites, news feeds, web services, and more. The following web access restrictions apply to this sandbox capability.  
  
- Your server must have the current [TLS and cipher suites](/power-platform/admin/onpremises-server-cipher-tls-requirements).
- Only the HTTP and HTTPS protocols are allowed.
- Access to localhost (loopback) isn't permitted.
- IP addresses can't be used. You must use a named web address that requires DNS name resolution.
- Anonymous authentication is supported and recommended. There's no provision for prompting the logged on user for credentials, or saving those credentials.
- Your server must allow connections from [Power Platform and Dynamics 365 services IP address values specified under the AzureCloud service tag](/power-platform/admin/online-requirements#ip-addresses-required).

Other methods of accessing web services include the use of Webhooks and the [!INCLUDE [pn_azure_service_bus](../../includes/pn_azure_service_bus.md)]. Refer to the links provided in the next sections for more information on those topics.

## How to access external web services

Today most people are familiar with  the [System.Net.Http.HttpClient Class](/dotnet/api/system.net.http.httpclient). `HttpClient` was introduced with .NET Framework 4.5 and provides significant capabilities over the [System.Net.WebClient Class](/dotnet/api/system.net.webclient), which is now obsolete.

`HttpClient` is intended to be reused and is asynchronous by default. Because `HttpClient` is asynchronous by default, you need to break away from typical use patterns and add code to force the operations to be performed synchronously, typically by removing the `await` keyword and appending `.GetAwaiter().GetResult()` to any asynchronous calls.

```csharp
public void Execute(IServiceProvider serviceProvider)
{
  //Extract the tracing service for use in plug-in debugging.
  ITracingService tracingService =
      (ITracingService)serviceProvider.GetService(typeof(ITracingService));

  try
  {
    tracingService.Trace("Downloading the target URI: " + webAddress);

    try
    {
      // Download the target URI using a Web client. Any .NET class that uses the
      // HTTP or HTTPS protocols and a DNS lookup should work.
      using (HttpClient client = new HttpClient())
      {
        client.Timeout = TimeSpan.FromMilliseconds(15000); //15 seconds
        client.DefaultRequestHeaders.ConnectionClose = true; //Set KeepAlive to false
        

        HttpResponseMessage response =  client.GetAsync(webAddress).Result; //Make sure it is synchonrous
        response.EnsureSuccessStatusCode();

        string responseText = response.Content.ReadAsStringAsync().Result; //Make sure it is synchonrous
        tracingService.Trace(responseText);
        //Log success in the Plugin Trace Log:
        tracingService.Trace("HttpClientPlugin completed successfully.");
      }
    }

    catch (AggregateException aex)
    {
      tracingService.Trace("Inner Exceptions:");

      foreach (Exception ex  in aex.InnerExceptions) {
        tracingService.Trace("  Exception: {0}", ex.ToString());
      }

      throw new InvalidPluginExecutionException(string.Format(CultureInfo.InvariantCulture,
          "An exception occurred while attempting to issue the request.", aex));
    }
  }
  catch (Exception e)
  {
    tracingService.Trace("Exception: {0}", e.ToString());
    throw;
  }
}
```

More information: [Sample: Web access from a plug-in](org-service/samples/web-access-plugin.md)

## Best practices

As called out in the following best practices articles:

- [Set KeepAlive to false when interacting with external hosts in a plug-in](best-practices/business-logic/set-keepalive-false-interacting-external-hosts-plugin.md)
- [Set time-out when making external calls in a plug-in](best-practices/business-logic/set-timeout-for-external-calls-from-plug-ins.md)

You should make sure to set an appropriate `Timeout` period for your external calls and disable `KeepAlive`. See the previous links for more information.

## See also

[Plug-ins](plug-ins.md)<br />
[Workflow extensions](workflow/workflow-extensions.md)<br />
[Azure integration](azure-integration.md)<br />
[Use Webhooks](use-webhooks.md)<br />

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
