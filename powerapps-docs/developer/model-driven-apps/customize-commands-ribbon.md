---
title: "Customize commands and the ribbon (model-driven apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces"
description: "Common Data Service for Apps displays commands in different ways depending on the entity and the client. In most places in the web application you will see a command bar instead of a ribbon. Dynamics 365 for tablets also uses data defined as ribbons to control what commands are available using a command bar that is optimized for touch." # 115-145 characters including spaces. This abstract displays in the search result."
keywords: ""
ms.date: 08/01/2018
ms.service:
  - "powerapps"
ms.custom:
  - ""
ms.topic: article
ms.assetid: 926364b0-ede6-00e9-39d4-5aae5e00be0b
author: JimDaly # GitHub ID
ms.author: jdaly # MSFT alias of Microsoft employees only
manager: shilpas # MSFT alias of manager or PM counterpart
ms.reviewer: 
---

# Customize commands and the ribbon

<!-- https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/customize-dev/customize-commands-ribbon -->

Dynamics 365 Common Data Service for Apps displays commands in different ways depending on the entity and the client. In most places in the web application you will see a *command bar* instead of a ribbon. Dynamics 365 for Tablets also uses data defined as ribbons to control what commands are available using a command bar that is optimized for touch.  
  
 The command bar provides better performance. The ribbon is still displayed in the web application for certain entity forms and it is still used for list views in Dynamics 365 for Outlook.  
  
 Both the command bar and the ribbon use the same underlying XML data to define what commands to display, when the commands are enabled, and what the commands do.  
  
 The topics in this section introduce you to key concepts that you must understand, and common tasks you perform when you customize the command bar or the ribbon.  
  
> [!NOTE]
>  Because the underlying XML schema was designed to display commands as ribbons, the term *ribbon* will continue to be used in the documentation.  
  
 The SDK describes the process of editing the ribbon by editing the customization.xml file directly. Several people have created ribbon editors that provide a user interface to make editing the ribbon easier. Currently the following projects are available on Codeplex and other locations:  
  
- [Ribbon Workbench](http://www.develop1.net/public/rwb/ribbonworkbench.aspx)  
  
- [MS CRM 2011 : Pragma Toolkit : Ribbon, Site Map Editor](http://pragmatoolkit.codeplex.com/)  
  
- [CRM 2011 Visual Ribbon Editor](http://crmvisualribbonedit.codeplex.com/)  
  
  To obtain support or help to use these programs, contact the program publisher.  
  
  
## See also  
 [Ribbon Core Schema](ribbon-core-schema.md)  
  
 [Ribbon Types Schema](ribbon-types-schema.md)  
  
 [Ribbon WSS Schema](ribbon-wss-schema.md) 

 [Sample: Export Ribbon Definitions](sample-export-ribbon-definitions.md) 
  
 [Apply business logic using client scripting in model-driven apps](client-scripting.md)