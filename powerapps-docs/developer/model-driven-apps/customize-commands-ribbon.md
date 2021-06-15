---
title: "Customize commands and the ribbon (model-driven apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces"
description: "Microsoft Dataverse displays commands in different ways depending on the table and the client. In most places in the web application, you will see a command bar instead of a ribbon. Dynamics 365 for tablets also uses data defined as ribbons to control what commands are available using a command bar that is optimized for touch." # 115-145 characters including spaces. This abstract displays in the search result."
keywords: ""
ms.date: 04/15/2021
ms.service: powerapps
ms.custom: "intro-internal"
ms.topic: article
ms.assetid: 926364b0-ede6-00e9-39d4-5aae5e00be0b
author: Nkrb # GitHub ID
ms.author: nabuthuk # MSFT alias of Microsoft employees only
manager: shilpas # MSFT alias of manager or PM counterpart
ms.reviewer: 
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Customize commands and the ribbon

Microsoft Dataverse displays commands in different ways depending on the table and the client. In most places in the web application, you will see a *command bar* instead of a ribbon. Dynamics 365 for Tablets also uses data defined as ribbons to control what commands are available using a command bar that is optimized for touch.  
  
The command bar provides better performance. The ribbon is still displayed in the web application for certain forms and it is still used for list views in Dynamics 365 for Outlook.  Both the command bar and the ribbon use the same underlying XML data to define what commands to display, when the commands are enabled, and what the commands do.  

[!INCLUDE[cc-terminology](../data-platform/includes/cc-terminology.md)]

The articles in this section introduce you to key concepts that you must understand, and common tasks you perform when you customize the command bar or the ribbon.  
  
> [!NOTE]
> Because the underlying XML schema was designed to display commands as ribbons, the term *ribbon* will continue to be used in the documentation.  
  
## Troubleshoot ribbon issues

If you are experiencing an issue with a ribbon command bar button, use this [troubleshooting guide](/troubleshoot/power-platform/power-apps/ribbon-issues-button-hidden?tabs=delete) to find and solve the problem.


## Community tool

The SDK describes the process of editing the ribbon by editing the customization.xml file directly. You can also use a community tool, [Ribbon Workbench](https://www.develop1.net/public/rwb/ribbonworkbench.aspx), to visually edit ribbons using the UI. 

> [!NOTE]
> Microsoft does not provide help or support for community tools. To obtain support or help to use these programs, contact the program publisher.  
  
  
## See also  

 [Ribbon Core Schema](ribbon-core-schema.md)  
 [Ribbon Types Schema](ribbon-types-schema.md)  
 [Ribbon WSS Schema](ribbon-wss-schema.md)<br/> 
 [Sample: Export Ribbon Definitions](sample-export-ribbon-definitions.md)<br/> 
 [Apply business logic using client scripting in model-driven apps](client-scripting.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]