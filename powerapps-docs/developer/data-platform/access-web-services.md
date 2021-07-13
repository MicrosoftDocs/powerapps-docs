---
title: "Access external web services (Microsoft Dataverse) | MicrosoftDocs"
description: "Learn how to access a web service from a custom plug-in or workflow activity."
ms.custom: ""
ms.date: 03/16/2021
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "JimDaly"
ms.subservice: dataverse-developer
ms.author: "pehecke"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Access external web services

Plug-ins and custom workflow activities can access the network through the HTTP and HTTPS protocols. This capability provides support for accessing popular web services like social sites, news feeds, web services, and more. The following web access restrictions apply to this sandbox capability.  
  
- Your server must have the current [TLS and cipher suites](/power-platform/admin/onpremises-server-cipher-tls-requirements).
- Only the HTTP and HTTPS protocols are allowed.
- Access to localhost (loopback) is not permitted.
- IP addresses cannot be used. You must use a named web address that requires DNS name resolution.
- Anonymous authentication is supported and recommended. There is no provision for prompting the logged on user for credentials or saving those credentials.

Other methods of accessing web services include the use of WebHooks and the [!INCLUDE [pn_azure_service_bus](../../includes/pn_azure_service_bus.md)]. Refer to the links provided below for more information on those topics.

## How to access external web services

Today most people are familiar with  the [System.Net.Http.HttpClient Class](/dotnet/api/system.net.http.httpclient). `HttpClient` was introduced with .NET 4.5 and provides significant capabilities over the [System.Net.WebClient Class](/dotnet/api/system.net.webclient) which is still available.

For new plug-ins you should use `HttpClient` because [the .NET team doesn't recommend WebClient for new development](/dotnet/api/system.net.webclient?#remarks). However, this doesn't mean you must replace any legacy code uses of `WebClient` that you find. Most of the advantages provided in `HttpClient` do not necessarily provide advantages within a plug-in. `HttpClient` is intended to be re-used and is asynchronous by default. Unless you are making multiple HTTP requests within your plug-in, `WebClient` is designed for a single request. Because `HttpClient` is asynchronous by default, you need to break away from typical use patterns and add code to force the operations to be performed synchronously, typically by removing the `await` keyword and appending `.Result` to any asynchronous calls.

`WebClient` provides simple synchronous methods such as [UploadData](/dotnet/api/system.net.webclient.uploaddata), [DownloadFile](/dotnet/api/system.net.webclient.downloadfile) which don't clearly expose the underlying HTTP method used, but they can be set using specific overrides such as [UploadString(String, String, String)](/dotnet/api/system.net.webclient.uploadstring#System_Net_WebClient_UploadString_System_String_System_String_System_String_) in case you want to use `PATCH` instead of `POST`.

In most cases outside of plug-ins, you will want to use `HttpClient`. Within plug-ins, you can also use `WebClient` if you prefer.

## Best practices

As called out in the following best practices topics:

- [Set KeepAlive to false when interacting with external hosts in a plug-in](best-practices/business-logic/set-keepalive-false-interacting-external-hosts-plugin.md)
- [Set Timeout when making external calls in a plug-in](best-practices/business-logic/set-timeout-for-external-calls-from-plug-ins.md)

You should make sure to set an appropriate `Timeout` period for your external calls and disable `KeepAlive`. See the above links for more information.


## See also

[Plug-ins](plug-ins.md)<br />
[Workflow extensions](workflow/workflow-extensions.md)<br />
[Azure integration](azure-integration.md)<br />
[Use WebHooks](use-webhooks.md)<br />
[Sample: Web access from a sandboxed plug-in](org-service/samples/web-access-plugin.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]