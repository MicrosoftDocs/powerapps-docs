---
title: "Set managed properties for columns in Power Apps"
description: "Learn how to set managed properties for a column in Microsoft Dataverse."
ms.custom: ""
ms.date: 04/10/2025
ms.reviewer: ""
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
tags: 
search.audienceType: 
  - maker
---
# Set managed properties for columns

Managed properties only apply when you export columns in a managed solution and import the solution into another environment. These settings allow a solution maker to have some control over the level of customization that people who install their managed solution can have when they customize this column.

To view and set managed properties for a column, follow these steps:

1. Sign into [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) and select **Solutions** from the left navigation. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]
1. Open the solution, open the table you want, and then open the **Columns** area.
1. Select the column you want.
1. On the command bar select **More Actions**, and then select **Managed properties**.  
1. Select the [managed properties options](#managed-properties-options) you want, and then select **Set**.

## Managed properties options

The **Allow customizations** option controls all the other options. If this option is `False`, none of the other settings apply. When it is `True`, you can specify the other customization options.  
  
 If the column is customizable, you set the following options to `True` or `False`.  
  
- **Display name can be modified**  
  
- **Can change requirement level**  
  
- **Can change additional properties**  
  
These options are self-explanatory. If you set all the individual options to `False`, you might as well set **Allow customizations** to `False`.  

## Next steps

[Create and edit columns](create-edit-fields.md)

[Solutions overview](solutions-overview.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]


## Related information

[Set managed properties for columns with Power Apps (video)](https://youtu.be/nKlRG5tHW2M?feature=shared)
