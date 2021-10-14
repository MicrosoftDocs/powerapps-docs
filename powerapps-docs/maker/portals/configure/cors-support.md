---
title: Setup HTTP headers in portals
description: Learn how to setup HTTP headers in portals.
author: sandhangitmsft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 04/21/2021
ms.subservice: portals
ms.author: sandhan
ms.reviewer: tapanm
contributors:
    - tapanm-msft
    - sandhangitmsft
---

# Setup HTTP headers in portals

The [cross-origin resource sharing (CORS)](https://www.w3.org/TR/cors/) protocol consists of a set of headers that indicates whether a response can be shared with another domain. You can configure CORS support in Power Apps portals using the Portal Management app by adding and configuring the site settings.

The following site settings are used to configure CORS:

| Site Setting | Request Header | Description |
|-|-|-|
| HTTP/Access-Control-Allow-Credentials | Access-Control-Allow-Credentials | The only valid value for this header is true (case-sensitive). If you don't need credentials, omit this header entirely (rather than setting its value to false). 
| HTTP/Access-Control-Allow-Headers | Access-Control-Allow-Headers | A comma-delimited list of the supported HTTP request headers.
| HTTP/Access-Control-Allow-Methods | Access-Control-Allow-Methods | A comma-delimited list of the allowed HTTP request methods such as GET, POST, OPTIONS.
| HTTP/Access-Control-Allow-Origin | Access-Control-Allow-Origin | URL of the Dynamics 365 instance, such as https://contoso.crm.dynamics.com. To allow any URI to access your resources, use \*.                 |
|  HTTP/Access-Control-Expose-Headers | Access-Control-Expose-Headers | A comma-delimited list of HTTP header names other than the simple response headers that the resource might use and can be exposed.
| HTTP/Access-Control-Max-Age | Access-Control-Max-Age |  Maximum number of seconds the results can be cached.
| HTTP/Content-Security-Policy | Content-Security-Policy | Controls resources the user agent is allowed to load for a given page.
| HTTP/Content-Security-Policy-Report-Only | Content-Security-Policy-Report-Only | Allows web developers to experiment with policies by monitoring, but not enforcing, their effects. These violation reports consist of JSON documents sent via an HTTP POST request to the specified URI.
| HTTP/X-Frame-Options | X-Frame-Options | Indicates whether a browser should be allowed to render a page in a *\<frame\>*, *\<iframe\>*, *\<embed\>* or *\<object\>*.
| HTTP/X-Content-Type-Options | X-Content-Type-Options | Disables MIME sniffing and forces browser to use the type given in *Content-Type*.

For more information about how to configure site settings in portal, go to [Manage portal site settings](configure-site-settings.md#manage-portal-site-settings).


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]