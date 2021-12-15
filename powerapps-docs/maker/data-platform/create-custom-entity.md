---
title: Create a custom table that has components with Power Apps | Microsoft Docs
description: Topic with step-by-step instructions for creating and configuring a table to use with a Power Apps app.
author: Mattp123
manager: kvivek
ms.service: powerapps
ms.component: cds
ms.topic: tutorial
ms.date: 01/26/2021
ms.subservice: dataverse-maker
ms.author: matp
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---

# Create a custom table that has components in Power Apps

[!INCLUDE[cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

With Power Apps, you tailor your app to closely fit your organization’s industry, nomenclature, and unique business processes. Power Apps app development includes adding standard "out-of-box" tables or creating custom tables. A table defines the information you want to track in the form of records, which typically include properties such as company name, location, products, email, and phone.

In this article you create a table and then add or customize key components such as columns, relationships, views, and forms. You learn how to:

- Create a custom table.
- Add custom columns to your table.
- Add a table relationship.
- Customize a view.
- Customize a form.

The article will follow the company, Contoso, which is a pet grooming business that grooms dogs and cats. Contoso needs an app for client and pet tracking that can be used by employees across a variety of devices.

## Prerequisites

Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc). If you don’t already have a Power Apps account, select the **Get started free** link from [powerapps.com](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).

## Create a custom table

1. On the left navigation pane expand **Data**, select **Tables**, and then select **New table**.

    > [!div class="mx-imgBorder"] 
    > ![New table.](media/create-custom-entity/create-new-entity.png)

2. In the right pane, enter the following values, and then select **Create**.

    - **Display name**: *Pet* 
    - **Description**: *Custom table to track pet services*

## Add and customize columns

1. Open the **Pet** table that was created in the previous section.

1. On the **Columns** tab, select the **Pet** column.

1. In the right pane make the following changes to the **Display name** column: 

    - Change the **Display name** from **Pet** to *Pet Name*.
    - Make sure **Searchable** is selected.
  
      > [!div class="mx-imgBorder"] 
      > ![Change primary column.](media/create-custom-entity/primary-field.png)

1. Select **Done**.

1. On the **Columns** tab on the table designer toolbar select **Add column**. On the **Column properties** pane, enter or select the following values and options.
    - **Display name**. *Species*
    - **Data type**. *Choice*
    - **Choice**. *New choice*
  
1. Select **View more**, and then select **Local choice**.

1. Create the choice:

      a. Replace **New option** with *Dog*.
      
      b. Select **Add new item**. 
        
      c.  Replace **New option** with *Cat*. 
        
      d. Select **Done**.

    > [!div class="mx-imgBorder"] 
    > ![New choice .](media/create-custom-entity/optionset-add-items.png)

1. Make sure **Searchable** is selected, and then select **Done**.

1. On the table designer toolbar select **Add column**. On the **Column properties** pane, enter or select the following values:
    - **Display name**. *Breed*
    - **Data type**. *Text*

1. Make sure **Searchable** is selected, and then select **Done**.

1. On the table designer toolbar select **Add column**. 

1. On the **Column properties** pane, enter or select the following values, and then select **Done**.
    - **Display name**. *Appointment date*
    - **Data type**. *Date and time*

## Add a relationship

1. Select the **Relationships** tab. Then, on the table designer toolbar, select **Add relationship**, and then select **Many-to-one**.

1. On the right pane, in the **Related** list select **Account**.

1. Select **Done**.

1. Select **Save table**.

  Notice that when you add a many-to-one relationship, an **Account** column with the data type **Lookup** is automatically added to your list of columns on the **Columns** tab.
  > [!div class="mx-imgBorder"]
  > ![Account lookup column.](media/create-custom-entity/account-lookup-field.png)

## Customize a view

1. Select the **Views** tab, and then open the **Active Pets** view. If you don't see the **Active Pets** view, change the filter on the command bar from **Default** to **All**.

1. On the view designer **Table columns** left pane, select the following columns to add them to the view.

    - **Account**
    - **Appointment date**
    - **Breed**
    - **Species**

1. On the view designer canvas, select the **Created On** column, and then select **Remove**.

1. To arrange the columns, on the view designer canvas, select the column you want to move and then use **Move Left** or **Move Right**. Your view should look like this.
    > [!div class="mx-imgBorder"] 
    > ![Active pets view.](media/create-custom-entity/active-pets-view.png)

1. On the view designer toolbar, select **Save**, and then select **Publish**.  

## Model-driven apps only: Customize the main form

Skip this step if you only want to use the Pet table in a canvas app.

1. Select **Back** to close the view designer and return to Power Apps.

1. On the left navigation pane, expand **Data**, select **Tables**, and then select **Pet**.

1. In the **Pet** table, select the **Forms** tab, and then select **Information** next to the **Main** form type to open the form designer.

    > [!div class="mx-imgBorder"] 
    > ![Edit main form.](media/create-custom-entity/main-form-edit.png)

1. On the form editor, select the  **Table columns** on the left pane. Then, drag and drop the **Species**, **Breed**, **Appointment date**, and **Account** columns located on the pane on to the **General** section of the form designer canvas until the form looks like this.

    > [!div class="mx-imgBorder"] 
    > ![Select columns for main form.](media/create-custom-entity/main-form-edit2.png) 

1. Select **Save**.

1. Select **Publish**.

1. Select **Back** to return to Power Apps.

## Add the custom table to an app

Now your table is ready to be used to build either a canvas or model-driven app.

## Next steps

In this topic, you learned how to create a table that can be used to create a useful app. 
- To learn how to create a model-driven app, see [Build your first model-driven app](../model-driven-apps/build-first-model-driven-app.md).
- To learn how to create a canvas app, see [Create an app from scratch](../canvas-apps/get-started-create-from-blank.md).


[!INCLUDE[footer-include](../../includes/footer-banner.md)]