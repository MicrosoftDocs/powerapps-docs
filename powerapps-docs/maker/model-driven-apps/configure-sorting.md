---
title: "Sort records in a model-driven app view in Power Apps | MicrosoftDocs"
ms.custom: ""
ms.date: 06/27/2018
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
ms.assetid: 25f5aa52-56dc-4be5-884e-9346616f665f
caps.latest.revision: 25
ms.author: "matp"
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---
# Sort records in a model-driven app view

When you create or edit a view you can configure the sort order for either ascending or descending.   
  
1.  Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).  

2.  Expand **Data**, select **Entities**, and then select the entity that you want, such as **Accounts**.   

3.  Select the **Views** tab, and if shown, select **Remove filter**, and then open the view you want, such as **Active Accounts**.

4.  In the view designer, select **Configure Sorting**.  

    > [!div class="mx-imgBorder"] 
    > ![Configure sorting](media/configure-sorting.png)
  
5.  In the **Configure Sort Order** dialog box, in the **Sort By** list, select the column you want to sort, then select **Ascending Order** or **Descending Order**.  
  
6.  Select **OK** to close the **Configure Sort Order** dialog box. 

## Columns of a grid don't show data when the grid loads

Grids in Unified Interface apps take the list of displayed columns from the underlying FetchXML of the view. If the FetchXML that is returned from the server does not have a column, then that column is not displayed. This is in contrast to the classic web application, where if a column is not present in FetchXML but is in LayoutXML, such a column is automatically added to the list of displayed columns. Unified Interface apps use OData directly with FetchXML to retrieve data from the server.

## Next steps
[Create or edit a view](create-edit-views.md)
[Use FetchXML to query data](../../developer/common-data-service/use-fetchxml-construct-query.md)
