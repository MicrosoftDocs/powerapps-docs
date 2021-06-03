---
title: "Define ribbon commands (model-driven apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces"
description: "A Ribbon command creates a reusable definition that can be referenced by ribbon control elements." # 115-145 characters including spaces. This abstract displays in the search result."
keywords: ""
ms.date: 03/27/2020
ms.service: powerapps
ms.topic: article
ms.assetid: 60933770-8c7c-499c-12b4-8b64f6eedb35
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

# Define ribbon commands

<!-- https://docs.microsoft.com/dynamics365/customer-engagement/developer/customize-dev/define-ribbon-commands -->

A *Ribbon* command creates a reusable definition that can be referenced by ribbon control elements.  
  
## Ribbon command elements  
 The `<CommandDefinition>` element defines a command in the ribbon. The `Id` attribute specifies a unique identifier for the command that can be referenced by ribbon control elements by using the `Command` parameter.  
  
 A ribbon command defines three things:  
  
- **Enable Rules**: Specifies when a specific ribbon control is enabled.  
  
- **Display Rules**: Specifies when a specific ribbon element is visible.  
  
- **Actions**: Specifies what code executes when a ribbon control is used.  
  
> [!IMPORTANT]
>  All command definitions are downloaded to a user's computer so that they can be evaluated at run time. This means that a user without the privileges to see a particular control in the ribbon can use the browser **View Source** command, review the code, and determine that a control exists that isn’t displayed to them.  
  
### See also  
 [Customize commands and the ribbon](customize-commands-ribbon.md)   
 [Use localized labels with Ribbons](use-localized-labels-ribbons.md)   
 [Define Ribbon enable rules](define-ribbon-enable-rules.md)
 [Troubleshoot ribbon issues](/troubleshoot/power-platform/power-apps/ribbon-issues-button-hidden?tabs=delete)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]