---
title: "Define ribbon commands (model-driven apps)"
description: "A Ribbon command creates a reusable definition that can be referenced by ribbon control elements."
author: clromano
ms.author: clromano
ms.date: 05/24/2022
ms.reviewer: jdaly
ms.topic: article
ms.subservice: mda-developer
search.audienceType: 
  - developer
contributors: 
  - JimDaly
  - caburk
---

# Define ribbon commands

[!INCLUDE [cc-modern-commanding](../data-platform/includes/cc-modern-commanding.md)]

A *Ribbon* command creates a reusable definition that can be referenced by ribbon control elements.  
  
## Ribbon command elements

 The `<CommandDefinition>` element defines a command in the ribbon. The `Id` attribute specifies a unique identifier for the command that can be referenced by ribbon control elements by using the `Command` parameter.  
  
 A ribbon command defines three things:  
  
- **Enable Rules**: Specifies when a specific ribbon control is enabled.  
  
- **Display Rules**: Specifies when a specific ribbon element is visible.  
  
- **Actions**: Specifies what code executes when a ribbon control is used.  
  
> [!IMPORTANT]
>  All command definitions are downloaded to a user's computer so that they can be evaluated at run time. This means that a user without the privileges to see a particular control in the ribbon can use the browser **View Source** command, review the code, and determine that a control exists that isn't displayed to them.  
  
### See also

[Customize commands and the ribbon](customize-commands-ribbon.md)   
[Use localized labels with Ribbons](use-localized-labels-ribbons.md)   
[Define Ribbon enable rules](define-ribbon-enable-rules.md)
[Troubleshoot ribbon issues](/troubleshoot/power-platform/power-apps/ribbon-issues-button-hidden?tabs=delete)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
