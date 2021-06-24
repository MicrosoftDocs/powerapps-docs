---
title: "Set KeepAlive to false when interacting with external hosts in a plug-in | MicrosoftDocs"
description: "KeepAlive property set to true in the HTTP request header or not explicitly defined as false can cause increased execution times of plug-ins."
services: ''
suite: powerapps
documentationcenter: na
author: jowells
manager: austinj
editor: ''
tags: ''
ms.service: powerapps
ms.devlang: na
ms.topic: article
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 8/21/2019
ms.author: jowells
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Set KeepAlive to false when interacting with external hosts in a plug-in

[!INCLUDE[cc-data-platform-banner](../../../../includes/cc-data-platform-banner.md)]

**Category**: Performance

**Impact potential**: High

<a name='symptoms'></a>

## Symptoms

If a plug-in makes external web requests and is trying to use `KeepAlive` on a closed connection, the plug-in will ultimately fail to execute the web request. If the plug-in is registered:

- Synchronously, users may experience:

    - Unresponsive model-driven apps
    - Slow client interactions
    - The browser stops responding

- Asynchronously, plug-in executions may take an extended period of time before failing. 

<a name='guidance'></a>

## Guidance

1. In HTTP 1.1, all connections are considered persistent (`KeepAlive` is true) unless declared otherwise. Due to the fact that plug-ins run in isolation, the Sandbox service translates into them being short-lived executions that generally would not benefit from `KeepAlive`. To avoid problems with connecting to external services we recommend disabling `KeepAlive` within plug-ins. If your specific external service would benefit from using persistent sessions for performance reasons, actively send a `KeepAlive` at an interval of half the idle timeout (30 seconds) to keep the connection from closing.

The following examples show how to explicitly define `KeepAlive` to false based on the method you use to establish a connection to an external service:

- `HttpWebRequest` 
    ```csharp
    HttpWebRequest req = WebRequest.Create("https://www.contoso.com/api/stuff") as HttpWebRequest;
    
    if (req != null)
    {
        req.KeepAlive = false;
        HttpWebResponse response = (HttpWebResponse)req.GetResponse();
    }
    ```

-  `WebClient` 
    ```csharp
    private string RequestString(Uri location)
    {
        using (var client = new MyWebClient())
        {
            return client.DownloadString(location);
        }
    }

    internal class MyWebClient : WebClient
    {
        // Overrides the GetWebRequest method and sets keep alive to false
        protected override WebRequest GetWebRequest(Uri address)
        {
            HttpWebRequest req = (HttpWebRequest)base.GetWebRequest(address);
            req.KeepAlive = false;

            return req;
        }
    }
    ```

- `WCF ClientBase< T >` Instance 
    ```csharp
    OrganizationServiceClient client = null;
    
    try
    {
        var address = new EndpointAddress("https://www.contoso.com/Custom.svc");
        var transport = new HttpsTransportBindingElement();
        transport.KeepAliveEnabled = false;
    
        var binding = new CustomBinding(transport);
    
        client = new OrganizationServiceClient(binding, address);
    
        WhoAmIResponse response = client.Execute(new WhoAmIRequest()) as WhoAmIResponse;
    }
    catch (Exception ex)
    {
        client.Abort();
    }
    finally
    {
        client.Close();
    }
    ```

- `WCF ChannelFactory< TChannel >` Static Method 
    ```csharp
    IRequestChannel channel = null;
    try
    {
        var address = new EndpointAddress("https://www.contoso.com/Custom.svc");
        var transport = new HttpsTransportBindingElement();
        transport.KeepAliveEnabled = false;
    
        var binding = new CustomBinding(transport);
    
        channel = ChannelFactory<IRequestChannel>.CreateChannel(binding, address);
    
        Message request = Message.CreateMessage(MessageVersion.Soap12, "some action", "message body");
        Message response = channel.Request(request);
    }
    catch (Exception ex)
    {
        channel.Abort();
    }
    finally
    {
        channel.Close();
    }
    ```

- `WCF ChannelFactory< TChannel >` Instance 
    ```csharp
    ChannelFactory<IRequestChannel> factory = null;
    IRequestChannel channel = null;
    try
    {
        var address = new EndpointAddress("https://www.contoso.com/Custom.svc");
        var transport = new HttpsTransportBindingElement();
        transport.KeepAliveEnabled = false;
    
        var binding = new CustomBinding(transport);
    
        factory = new ChannelFactory<IRequestChannel>(binding, address);
        channel = factory.CreateChannel();
    
        Message request = Message.CreateMessage(MessageVersion.Soap12, "some action", "message body");
        Message response = channel.Request(request);
    }
    catch (Exception ex)
    {
        channel.Abort();
        factory.Abort();
    }
    finally
    {
        channel.Close();
        factory.Close();
    }
    ```

<a name='problem'></a>

## Problematic patterns

In order to override the default value of `KeepAlive` for the non-WCF interactions, the approach should be taken to leverage HttpWebRequest to perform the interactions with the web server, but first setting the `KeepAlive` property to false.

The following examples show the problematic pattern based on the method you use to establish a connection to an external service:

> [!WARNING]
> These patterns should be avoided.

- `HttpWebRequest`

    ```csharp
    WebRequest request = WebRequest.Create("https://www.contoso.com/api/stuff");
    //KeepAlive not explicitly defined as true.  However, default behavior is KeepAlive = true.
    HttpWebResponse response = (HttpWebResponse)request.GetResponse();
    response.Close();
    ```

- `WebClient`

    ```csharp
    using (var client = new WebClient())
    {
        string url = "https://www.contoso.com/api/stuff";
        //KeepAlive not explicitly defined as true.  However, default behavior is KeepAlive = true.
        string result = client.DownloadString(url);
    }
    ```

- `WCF ClientBase< T >` Instance

    ```csharp
    OrganizationServiceClient client = null;
    
    try
    {
        var address = new EndpointAddress("https://www.contoso.com/Custom.svc");
        var binding = new BasicHttpsBinding();
        //KeepAlive not explicitly defined as true.  However, default behavior is KeepAlive = true.
        client = new OrganizationServiceClient(binding, address);
    
        WhoAmIResponse response = client.Execute(new WhoAmIRequest()) as WhoAmIResponse;
    }
    catch (Exception ex)
    {
        client.Abort();
    }
    finally
    {
        client.Close();
    }
    ```

- `WCF ChannelFactory< TChannel >` Static Method

    ```csharp
    IRequestChannel channel = null;
    try
    {
        var address = new EndpointAddress("https://www.contoso.com/Custom.svc");
        var binding = new BasicHttpsBinding();
        //KeepAlive not explicitly defined as true.  However, default behavior is KeepAlive = true.
    
        channel = ChannelFactory<IRequestChannel>.CreateChannel(binding, address);
    
        Message request = Message.CreateMessage(MessageVersion.Soap12, "some action", "message body");
        Message response = channel.Request(request);
    }
    catch (Exception ex)
    {
        channel.Abort();
    }
    finally
    {
        channel.Close();
    }
    ```

- `WCF ChannelFactory< TChannel >` Instance

    ```csharp
    ChannelFactory<IRequestChannel> factory = null;
    IRequestChannel channel = null;
    try
    {
        var address = new EndpointAddress("https://www.contoso.com/Custom.svc");
        var binding = new BasicHttpsBinding();
        //KeepAlive not explicitly defined as true.  However, default behavior is KeepAlive = true.
    
        factory = new ChannelFactory<IRequestChannel>(binding, address);
        channel = factory.CreateChannel();
    
        Message request = Message.CreateMessage(MessageVersion.Soap12, "some action", "message body");
        Message response = channel.Request(request);
    }
    catch (Exception ex)
    {
        channel.Abort();
        factory.Abort();
    }
    finally
    {
        channel.Close();
        factory.Close();
    }
    ```

<a name='additional'></a>

## Additional information

Plug-ins interacting with external services may experience abnormally increased execution times. The problem is due to the ([KeepAlive property](/dotnet/api/system.net.httpwebrequest.keepalive)) of HTTP requests issued to external web servers. If the `KeepAlive` property is set to true or not defined at all (default behavior is true) the Sandbox client on the server could continue to try and use a persistent session even though the session has become expired due to network device configuration. The cause of the extended execution time is due to the network retrying the request until the connection is, ultimately, reset.

> [!IMPORTANT]
> This affects all code that initiates HTTP Requests to a web server using [System.Net.WebClient](/dotnet/api/system.net.webclient), [System.Net.WebRequest](/dotnet/api/system.net.webrequest) or [System.Net.HttpWebRequest](/dotnet/api/system.net.httpwebrequest) as well as Windows Communications Foundation (WCF) client communications using an HTTP transport binding directly or indirectly via [ChannelFactory\<TChannel>](/dotnet/api/system.servicemodel.channelfactory-1) or [ClientBase\<T>](/dotnet/api/system.servicemodel.clientbase-1).

This behavior is transparent to end users and traditional logging as the execution is due to network delays.  If the plug-in was registered as a synchronous event, users could experience intermittent performance issues during those registered operations which could cause unresponsiveness of model-driven apps.  If the plug-in is registered asynchronously, the issue would only be observed by reviewing execution times of the plug-in and seeing the execution taking longer than normal or expected.

<a name='seealso'></a>

### See also

[Sample: Web access from a sandboxed plug-in](../../org-service/samples/web-access-plugin.md)<br />
[Load Balancing (WCF)](/dotnet/framework/wcf/load-balancing)<br />
[HttpTransportBindingElement.KeepAliveEnabled Property](/dotnet/api/system.servicemodel.channels.httptransportbindingelement.keepaliveenabled)<br />
[HttpWebRequest.KeepAlive Property](/dotnet/api/system.net.httpwebrequest.keepalive)<br />


[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]