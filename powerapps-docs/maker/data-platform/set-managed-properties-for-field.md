---
title: "Set managed properties for columns in Power Apps | MicrosoftDocs"
description: "Learn how to set managed properties for a column"
ms.custom: ""
ms.date: 06/19/2018
ms.reviewer: ""
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "powerapps"
author: "Mattp123"
ms.assetid: 4ddcfcf3-5604-4b93-a5ee-589d4fb97fa4
caps.latest.revision: 33
ms.subservice: dataverse-maker
ms.author: "matp"
manager: "kvivek"
tags: 
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---
# Set managed properties for columns

[!INCLUDE[cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

<a name="BKMK_SettingManagedProperties"></a>   

 Managed properties only apply when you include columns in a managed solution and import the solution into another environment. These settings allow a solution maker to have some control over the level of customization that people who install their managed solution can have when they customize this column. To set managed properties for a column, select **Managed Properties** on the menu bar.  
  
 The **Can be customized** option controls all the other options. If this option is `False`, none of the other settings apply. When it is `True`, you can specify the other customization options.  
  
 If the column is customizable, you set the following options to `True` or `False`.  
  
- **Display name can be modified**  
  
- **Can change requirement level**  
  
- **Can change Additional Properties**  
  
 These options are self-explanatory. If you set all the individual options to `False`, you might as well set **Can be customized** to `False`.  

 ## Next steps

 [Create and edit columns](create-edit-fields.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]