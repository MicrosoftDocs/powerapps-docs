---
title: "Delete columns in Power Apps | MicrosoftDocs"
description: "Learn how to delete columns"
ms.custom: ""
ms.date: 06/20/2018
ms.reviewer: ""
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "how-to"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "powerapps"
author: "Mattp123"
ms.assetid: 578ac950-da16-4ec6-a0a4-25f3aaa3b96e
caps.latest.revision: 33
ms.author: "matp"
manager: "kvivek"
tags: 
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---
# Delete columns

[!INCLUDE[cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

<a name="BKMK_DeletingFields"></a>   
As someone with the system administrator security role, you can delete any custom columns that aren’t part of a managed solution. When you delete a column, any data stored in the column is lost. The only way to recover data from a column that was deleted is to restore the database from a point before the column was deleted.  
  
Before you can delete a custom table, you must remove any dependencies that may exist in other solution components.
1. In the **Solutions** area of Power Apps, open the solution that includes the column that you want to delete.
1. Open the table, select the **Column** tab, and then select the column you want to delete.
1. Select **Show Dependencies** on the command bar to view the **Dependent components** page.

For example, if the column is used in a form or view, you must first remove the column from those solution components.  
  
If you delete a lookup column, the 1:N table relationship for it will automatically be deleted.  

### See also

 [Delete a custom table](data-platform-delete-entity.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]