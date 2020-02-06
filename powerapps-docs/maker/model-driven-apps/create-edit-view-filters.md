---
title: "Create or edit filters in model-driven app views | MicrosoftDocs"
description: "Learn how to create and edit filters or views for your app"
keywords: ""
ms.date: 2/04/2020
ms.service: powerapps
ms.custom: 
ms.topic: article
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "powerapps"
ms.assetid: 
author: iangpgh
ms.author: v-iapr
manager: matp
ms.reviewer: srihas
ms.suite: 
ms.tgt_pltfrm: 
caps.latest.revision: 25
topic-status: Drafting
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---

# Create or edit filters in model-driven app views

<a name="BKMK_CreateOrEditViewFilters"></a>   

The filters in a Power Apps view are important to the value provided by the view. Which filters are applied determine which records appear in the list by default. You can add or edit a filter for the columns that you include in a view by selecting the column and selecting **Filter by**. You can also use the Filters editor in the view designer. Use the Filters editor to add or edit filters for any fields in the view entity or any fields in a related entity. 

In this topic, you create or edit filters by performing the following tasks:

-   [Edit or remove a filter condition](create-edit-view-filters.md#edit-or-remove-a-filter-condition)

-   [Open the filter editor](create-edit-view-filters.md#open-the-filter-editor)

-   [Add conditions to a filter](create-edit-view-filters.md#add-conditions-to-a-filter)

-   [Add a group condition to a filter](create-edit-view-filters.md#add-a-group-condition-to-a-filter)

-   [Add a related entity to a condition](create-edit-view-filters.md#add-a-related-entity-to-a-condition)

-   [Group conditions of a filter](create-edit-view-filters.md#group-conditions-of-a-filter)

## Edit or remove a filter condition

1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).  

2. Expand **Data**, select **Entities**, select the entity that you want, and then select the **Views** tab.

3. Select a view to open it. The View properties panel lists existing filters.

    > [!div class="mx-imgBorder"] 
    > ![View panel filters](media/views-panel-filters.png)

4. On the View properties panel, select a filter condition.

    > [!div class="mx-imgBorder"] 
    > ![Edit filters](media/edit-filter-viewpanel.png)

5. Select the conditional operator that you want to use.

6. Type or select the comparison value for the condition.

7. Select **Apply**.

8. To remove a condition, select Remove filter. The condition is removed without confirmation.

### Open the filter editor

- On the View properties panel, select **Edit filters**.

    > [!div class="mx-imgBorder"] 
    > ![Filters editor](media/edit-create-filters.png)

### Add conditions to a filter

1. In the filters editor, select **Add > Add row**.

2. Select a field for the condition.

3. Select a conditional operator.

4. Select a comparison value.  

    Some filter conditions do not require a comparison value for the condition. For example, the operator **Contains data** does not require a comparison value. With other filter conditions, you choose the comparison value from an option set. For example, the status field has an option set that contains the values Active and Inactive.

    > [!div class="mx-imgBorder"] 
    > ![Filter condition](media/add-condition-filter.png)

5. Select **OK**.

### Add a group condition to a filter

1. In the filters editor, select **Add > Add group**.

2. Select the relational operator **Or** for the group. **And** is the default relational operator.

3. Specify the first clause of the grouped condition. Select the field, conditional operator, and comparison value.

4. Select **Add > Add group**

5. Specify the second clause of the grouped condition.

    > [!div class="mx-imgBorder"] 
    > ![Group condition filter](media/add-group-filter.png)

    You can select **Collapse** to display the group as a conditional expression.

### Add a related entity to a condition

1. In the filters editor, select **Add > Add related entity**.

2. Select a field from the related entity for the condition. You can select fields that have a Many to One, One to Many, or Many to Many relationships with the view entity.

3. Select a conditional operator.

4. Select or enter a comparison value.

    > [!div class="mx-imgBorder"] 
    > ![Related entity filter](media/add-relatedentity-filter.png)

### Group conditions of a filter

1. In the filters editor, select the checkbox for the conditions that you want to group.

2. Select the More commands menu for one of the conditions, and select **Make group**.

3. To ungroup a group, select More commands menu for the group, and select **Ungroup**

    > [!div class="mx-imgBorder"] 
    > ![Grouped condition filter](media/group-conditions-filter.png)

### Next steps
[Choose and configure columns](choose-and-configure-columns.md)  
[Edit filter criteria](edit-filter-criteria.md)  
[Create 1:N (one-to-many) or N:1 (many-to-one) relationships](../common-data-service/create-edit-1n-relationships.md)