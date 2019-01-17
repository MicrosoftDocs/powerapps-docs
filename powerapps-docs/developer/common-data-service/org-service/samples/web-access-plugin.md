---
title: "Sample: Web access from a plug-in (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to write a plug-in that can access resources on the web (network)." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 1/16/2019
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "samples"
author: "phecke"
ms.author: "pehecke" # MSFT alias of Microsoft employees only
manager: "kvivek" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Sample: Web access from a plug-in

This sample shows how to write a plug-in that can access web (network) resources like a web service or feed. You can download the sample from [here](https://github.com/Microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23/WebAccessPlugin).

## Prerequisites
[!INCLUDE[sdk-prerequisite](../includes/sdk-prerequisite.md)]

## Requirements  
 This sample code is for a Dynamics 365 for Customer Engagement apps deployment or a Dynamics 365 for Customer Engagement apps (on-premise) deployment with a running sandbox process.
  
 Register the compiled plug-in to run in the sandbox on the [!INCLUDE[pn_dynamics_crm](../includes/pn-dynamics-crm.md)] server.  
  
## Demonstrates
 Demonstrates how to write plug-in code that can access a web service.  
  
## Example
 [!code-csharp[Plug-ins#WebClientPlugin](../snippets/csharp/CRMV8/plug-ins/cs/webclientplugin.cs#webclientplugin)]  
  
## See also
[Access external web resources](../../access-web-services.md)<br/>
[Write a plug-in](../../write-plug-in.md)<br/>
 <xref:Microsoft.Xrm.Sdk.IPlugin><br/>
 <xref:Microsoft.Xrm.Sdk.ITracingService>