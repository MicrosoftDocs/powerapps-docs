---
title: "Access external web services (Common Data Service for Apps) | MicrosoftDocs"
description: "Learn how to access a web service from a custom plug-in or workflow activity."
ms.custom: ""
ms.date: 2/6/2019
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "JimDaly"
ms.author: "pehecke"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Access external web services

Plug-ins and custom workflow activities executing in the sandbox can access the network through the HTTP and HTTPS protocols. This capability provides support for accessing popular web services like social sites, news feeds, web services, and more. The following web access restrictions apply to this sandbox capability.  
  
- Only the HTTP and HTTPS protocols are allowed.
- Access to localhost (loopback) is not permitted.
- IP addresses cannot be used. You must use a named web address that requires DNS name resolution.
- Anonymous authentication is supported and recommended. There is no provision for prompting the logged on user for credentials or saving those credentials.

Other methods of accessing web services include the use of webhooks and the [!INCLUDE [pn_azure_service_bus](../../includes/pn_azure_service_bus.md)]. Refer to the links provided below for more information on those topics.

## See also

[Plug-ins](plug-ins.md)<br />
[Workflow extensions](workflow/workflow-extensions.md)<br />
[Azure integration](azure-integration.md)<br />
[Use Web Hooks](use-webhooks.md)<br />
[Sample: Web Access from a Sandboxed Plug-in](org-service/samples/web-access-plugin.md)
