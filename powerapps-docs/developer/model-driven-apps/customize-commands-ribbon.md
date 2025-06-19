---
title: "Customize commands and the ribbon (model-driven apps)"
description: "Model-driven apps display commands in different ways depending on the table and the client. In most places in model-driven apps, you will see a command bar instead of a ribbon. Dynamics 365 for tablets also uses data defined as ribbons to control what commands are available using a command bar that is optimized for touch."
author: clromano
ms.author: clromano
ms.date: 10/03/2022
ms.reviewer: jdaly
ms.topic: article
ms.subservice: mda-developer
search.audienceType: 
  - developer
contributors: 
  - JimDaly
---

# Customize commands and the ribbon

[!INCLUDE [cc-modern-commanding](../data-platform/includes/cc-modern-commanding.md)]

Model-driven apps display commands in different ways depending on the table and the client. In most places in the model-driven apps, you will see a *command bar* instead of a ribbon. Dynamics 365 for Tablets also uses data defined as ribbons to control what commands are available using a command bar that is optimized for touch.  
  
The command bar provides better performance. The ribbon is still displayed in the web application for certain forms and it is still used for list views in Dynamics 365 for Outlook.  Both the command bar and the ribbon use the same underlying XML data to define what commands to display, when the commands are enabled, and what the commands do.  

[!INCLUDE[cc-terminology](../data-platform/includes/cc-terminology.md)]

The articles in this section introduce you to key concepts that you must understand, and common tasks you perform when you customize the command bar or the ribbon.  
  
> [!NOTE]
> Because the underlying XML schema was designed to display commands as ribbons, the term *ribbon* will continue to be used in the documentation.  
  
## Troubleshoot ribbon issues

If you are experiencing an issue with a ribbon command bar button, use this [troubleshooting guide](/troubleshoot/power-platform/power-apps/ribbon-issues-button-hidden?tabs=delete) to find and solve the problem.

## Reference documentation

You can find reference documentation for Ribbon XML elements here: [Ribbon XML reference](/previous-versions/dynamicscrm-2016/developers-guide/gg327947%28v=crm.8%29). This documentation is not maintained and includes many elements that are no longer relevant. It provides information about the elements defined in the ribbon schema files: [Ribbon core schema](ribbon-core-schema.md), [Ribbon types schema](ribbon-types-schema.md), and [Ribbon WSS schema](ribbon-wss-schema.md). There are some remarks within this reference that may be helpful.


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
