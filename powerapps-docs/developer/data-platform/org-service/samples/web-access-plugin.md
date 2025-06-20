---
title: "Sample: Web access from a plug-in (Microsoft Dataverse) | Microsoft Docs" 
description: "Learn how to write a plug-in that can access resources on the World Wide Web." 
ms.date: 01/24/2025
author: MsSQLGirl
ms.author: jukoesma
ms.reviewer: pehecke
ms.topic: sample
search.audienceType:
  - developer
contributors:
  - JimDaly
  - phecke
---

# Sample: Web access from a plug-in

[!INCLUDE[cc-terminology](../../includes/cc-terminology.md)]

This sample shows how to write a plug-in that can access network (web) resources like a web service or feed. It also demonstrates how to limit the time duration allowed for this call.

> [!div class="nextstepaction"]
> [SDK for .NET: Web access from a plug-in sample code](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/CSharp/WebAccessPlugin)

## How to run this sample

1. Download or clone the [Samples](https://github.com/Microsoft/PowerApps-Samples) repo so that you have a local copy. This sample is located under PowerApps-Samples-master\dataverse\orgsvc\C#\WebAccessPlugin.
1. Open the sample solution in Visual Studio, navigate to the project's properties, and verify the assembly is signed during the build. Press F6 to build the sample's assembly (WebAccessPlugin.dll).
1. Run the Plug-in Registration tool and register the assembly in the Microsoft Dataverse server's sandbox and database.
1. When registering a step, specify a web URI string (that is, `https://www.microsoft.com`) in the unsecure configuration column.
   - The default value `https://www.bing.com` is used if none is provided.
1. Using an app or write code to perform the appropriate operation to invoke the message and table request that you registered the plug-in on.
1. When the plug-in runs, if the duration of the call exceeds the 15-second limit, it throw's an error. Otherwise it should succeed.
1. When you're done testing, unregister the assembly and step using the Plug-in Registrations tool.

## What this sample does

When executed, the plug-in downloads web page data from the specified web service address (or the default address).
If the request exceeds the 15-second limit, it throws an [InvalidPluginExecutionException](/dotnet/api/microsoft.xrm.sdk.invalidpluginexecutionexception)
and write details to the Plug-in Trace Log.

- If the `HttpClientPlugin` plug-in fails, it writes something like the following to the Plug-in Trace log:

  ```
  Downloading the target URI: https://www.bing.com
  Inner Exceptions:
    Exception: System.Threading.Tasks.TaskCanceledException: A task was canceled.
  Exception: Microsoft.Xrm.Sdk.InvalidPluginExecutionException: An exception occurred while attempting to issue the request.
     at PowerApps.Samples.HttpClientPlugin.Execute(IServiceProvider serviceProvider)
  ```

  The [TaskCanceledException](/dotnet/api/system.threading.tasks.taskcanceledexception) is ambiguous about the cause of the task being canceled. For a more complete solution showing how to explicitly detect errors due to time-outs, see this blog post: [Better time out handling with HttpClient](https://thomaslevesque.com/2018/02/25/better-timeout-handling-with-httpclient/).

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample does the following:

### Setup

1. Checks the constructor's unsecure configuration parameter for a web address value; otherwise, the default value is used.
2. The [HttpClient Class](/dotnet/api/system.net.http.httpclient) class is used by the plug-in's `Execute` method to download web page data.
3. If the call exceeds the 15-second duration specified, an [InvalidPluginExecutionException](/dotnet/api/microsoft.xrm.sdk.invalidpluginexecutionexception) is thrown and details about the error is written to the Plug-in Trace Log.

### Demonstrate

#### HttpClientPlugin plugin

1. Uses the [HttpClient Class](/dotnet/api/system.net.http.httpclient) and sets the [Timeout Property](/dotnet/api/system.net.http.httpclient.timeout) to limit the allowed time for the operation to complete.
1. Catches the expected [AggregateException Class](/dotnet/api/system.aggregateexception) and examines the inner exceptions for the expected [TaskCanceledException](/dotnet/api/system.threading.tasks.taskcanceledexception)

### See also

[Access external web resources](../../access-web-services.md)<br/>
[Register a plug-in](../../register-plug-in.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
