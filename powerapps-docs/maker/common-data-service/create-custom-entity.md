---
title: Create a custom entity | Microsoft Docs
description: Step-by-step instructions for creating and configuring an entity to use with a PowerApps app.
services: ''
suite: powerapps
documentationcenter: na
author: Mattp123
manager: bycho
editor: ''
tags: ''

ms.service: powerapps
ms.devlang: na
ms.topic: article
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 03/21/2018
ms.author: matp

---
# Create a custom entity in PowerApps

With [!INCLUDE [powerapps](../../includes/powerapps.md)] you tailor your app to closely fit your organization’s industry, nomenclature, and unique business processes. [!INCLUDE [powerapps](../../includes/powerapps.md)] app development includes adding standard "out-of-box entities or creating custom entities. An entity defines the information you want to track in the form of records, which typically include properties such as company name, location, products, email, and phone. 

In this tutorial you create an entity and then add or customize key components such as fields, relationships, views, and forms. You learn how to:

- Create a custom entity
- Add custom fields to your entity
- Add an entity relationship
- Customize a view 
- Customize a form

> [!IMPORTANT]
> [!INCLUDE [cc-preview-features-definition](../../includes/cc-preview-features-definition.md)]

The tutorial will follow the company, Contoso, which is a pet grooming business that grooms dogs and cats. Contoso needs an app for client and pet tracking that can be used by employees across a variety of devices.

## Prerequisites

Sign in to [PowerApps](https://powerapps.microsoft.com/). If you don’t already have a [!INCLUDE [powerapps](../../includes/powerapps.md)] account, select the **Get started free** link from [powerapps.com](https://web.powerapps.com).

## Create a custom entity

1. On the left navigation pane under **Common Data Service**, select **Entities** and then select **New entity**.
    ![New entity](../../media/create-custom-entity/create-new-entity.png)
2. In the right pane, enter the following values, and then select **Next**.
  - **Display name**: *Pet* 
  - **Description**: *Pets serviced in the grooming facility.*
3. Select **Save Entity**.

## Add and customize fields

1. On the **Fields** tab, select the **Primary Name** field.
2. In the right pane make the following changes to the **Primary Name** field: 
  - Change the **Display name** from **Primary name** to *Pet Name*
  -	Select **Searchable**

    ![Change primary field](../../media/create-custom-entity/primary-field.png)
3. Select **Done**.
4. On the entity designer toolbar select **Add** field. On the **Field properties** pane, enter or select the following values and options.
  - **Display name**. *Species*
  - **Data type**. *Option Set*
  - **Option set**. *New*
5. Create the option set

    a. Select **Add new item**.
    b. Replace **New option** with *Dog*.
    c. Select **Add new item**.
    d  Replace **New option** with *Cat*.
    e. Select **Save**.

    ![New option set](../../media/create-custom-entity/optionset-add-items.png)
6. Select **Searchable**, and then select **Done**.
7. On the entity designer toolbar select **Add field**. On the **Field properties** pane, enter or select the following values, and then select **Done**.
  - **Display name**. *Breed*
  - **Data type**. *Text*
  - **Searchable**. *Yes*
8. On the entity designer toolbar select **Add field**. 
9. On the **Field properties** pane, enter or select the following values, and then select **Done**. 
  -	**Display name**. *Appointment date*
  - **Data type**. *Date and time*
10. Select **Save Entity**.

## Add a relationship

1. Select the **Relationships** tab, and then on the entity designer toolbar select **Add relationship**. 
2. On the right pane, in the **Related entity** list select **Account**, and then select **Done**.
3. Select **Save Entity**.

Notice that when you add a relationship, a field with the data type **Lookup** is automatically added to your list of fields on the **Fields** tab.
    ![Account lookup field](../../media/create-custom-entity/account-lookup-field.png)

## Customize a view

1. Select the **Views** tab and then select the **Active Pets** view.
2. On the view designer select **Add Columns**, select the following columns, and then select **OK**.
  - Account
  - Appointment date 
  - Breed 
  - Species
3. Select the **Created On** column, select **Remove**, and then select **OK** to confirm the column removal.
4. To arrange the columns, select the column you want to move and then use the <- and -> arrow buttons until your view looks like this.
    ![Active pets view](../../media/create-custom-entity/active-pets-view.png)
5. On the view designer toolbar, select **Save and Close**.  
6. Select **Save Entity**.

## Model-driven apps only: Customize the main form

Skip this step if you only want to use the Pet entity in a canvas app. 

1. On the [!INCLUDE [powerapps](../../includes/powerapps.md)] left navigation pane, select **Advanced**.
2. On the left navigation of the solution window, select **Entities**, expand **Pet**, and then select **Forms**.
3. Select **Information** next to the **Main** form type to open the form editor.
    ![Edit main form](../../media/create-custom-entity/main-form-edit.png)
4. On the form editor, drag and drop the **Species**, **Breed**, **Appointment date**, and **Account** fields located on the Field Explorer pane on to the General section of the form canvas until the form looks like this.
    ![Select fields for main form](../../media/create-custom-entity/main-form-edit2.png) 
5. Select **Save and Close**.
6. On the solution window, select **Publish All Customizations**.
    ![Publish all customizations](../../media/create-custom-entity/publish-all-customizations.png)

## Add the custom entity to an app

Now your entity is ready to be used to build an app, such as this canvas app that uses a phone layout.

![Example canvas app](../../media/create-custom-entity/pet-grooming-canvas-app.png)

Or added to a model-driven app.

![Example model-driven app](../../media/create-custom-entity/pet-grooming-model-app.png)

## Next steps

In this tutorial, you learned how to create an entity that can be used to create a useful app. To learn how to create a canvas app, see [Create an app from scratch](../canvas-apps/get-started-create-from-blank.md).
