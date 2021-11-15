---
title: "Edit multiple rows (Bulk edit)| MicrosoftDocs"
description: Edit multiple rows in model-driven Power Apps.
author: mduelae
manager: kvivek
ms.service: powerapps
ms.component: pa-user
ms.topic: conceptual
ms.date: 08/1/2021
ms.subservice: end-user
ms.author: mkaur
ms.custom: ""
ms.reviewer: ""
ms.assetid: 
search.audienceType: 
  - enduser
search.app: 
  - PowerApps
  - D365CE
---

 # Edit multiple rows (Bulk edit)
 
 [!INCLUDE [cc-beta-prerelease-disclaimer](../includes/cc-beta-prerelease-disclaimer.md)]
 
You can edit multiple rows in model-driven apps and quickly update several columns of data across multiple rows in a single action. This is useful in scenarios when you need to update the same column for multiple rows.

>[!NOTE]
> Your administrator must grant you the Bulk Edit [miscellaneous privilege](/power-platform/admin/miscellaneous-privileges#:~:text=prvBulkEdit) to edit multiple rows.

Columns such as timeline wall, quick view forms, reference panel, and etc. aren't available when you're editing multiple rows.

1. To edit multiple rows, go to view page with the list of rows and select two or more rows.
2. On the command bar, select **Edit**.

   ![Edit multiple rows.](media/bulk-edit.gif "Edit multiple rows")


The **Edit (number of rows) records** dialog opens with your last used form for the table.

> [!div class="mx-imgBorder"]
> ![How to user bulk edit](media/bulk-edit-legend.png "How to use bulk edit")

Legend

1. Shows the number of rows that you're editing.
2. Shows the form title.
3. Select the chevron icon to switch from the default form to another form.
4. Select a tab to edit the columns on the form. The header column is always listed on the last tab. 
5. If you changed the data for a required column, it needs to contain data otherwise you won't be able to save your changes.
6. Shows the form details that can be edited.
7. Save or cancel your changes. Saved changes are saved for all selected rows.

### See also

[How to import data](/powerapps/user/import-data)  
[Remove a large amount of specific, targeted data with bulk deletion](/power-platform/admin/delete-bulk-records)  


[!INCLUDE[footer-include](../includes/footer-banner.md)]
