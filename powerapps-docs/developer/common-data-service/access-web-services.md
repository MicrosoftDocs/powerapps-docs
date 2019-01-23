---
title: "Access external web resources (Common Data Service for Apps) | MicrosoftDocs"
description: "Learn how to access a web resource, for example a web service, from a custom plug-in or workflow activity."
ms.custom: ""
ms.date: 1/16/2019
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "phecke"
ms.author: "pehecke"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Access external web resources

Plug-ins and custom workflow activities executing in the sandbox can access the network through the HTTP and HTTPS protocols. This capability provides support for accessing popular web resources like social sites, news feeds, web services, and more. The following web access restrictions apply to this sandbox capability.  
  
- Only the HTTP and HTTPS protocols are allowed.
- Access to localhost (loopback) is not permitted.
- IP addresses cannot be used. You must use a named web address that requires DNS name resolution.
- Anonymous authentication is supported and recommended. There is no provision for prompting the logged on user for credentials or saving those credentials.
- 
> [!IMPORTANT]
> For sandboxed plug-ins to be able to access external Web services from an on-premise D365 server, the server's Sandbox Processing Service role must be exposed to the Internet, and the account that the sandbox service runs under must have Internet access. Only outbound connections on ports 80 and 443 are required. Inbound connection access is not required. Use the Windows Firewall control panel to enable outbound connections for the Microsoft.Crm.Sandbox.WorkerProcess application located on the server in the %PROGRAMFILES%\Dynamics 365 for Customer Engagement\Server\bin folder. Web access is supported by default for sandboxed plug-ins executing under CDS for Apps in the cloud.

Other methods of accessing web resources include the use of webhooks and the [!INCLUDE [pn_azure_service_bus](../../includes/pn_azure_service_bus.md)]. Refer to the links provided below for more information on those topics.

## See also

[Plug-ins](plug-ins.md)<br />
[Workflow extensions](workflow/workflow-extensions.md)<br />
[Azure integration](azure-integration.md)<br />
[Use Web Hooks](use-webhooks.md)<br />
[Sample: Web Access from a Sandboxed Plug-in](org-service/samples/web-access-plugin.md)
