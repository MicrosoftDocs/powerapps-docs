---
title: Short video tutorial on creating new data columns
description: Learn to add new columns with our short video for enhanced data capture in your apps
ms.date: 03/10/2025
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: overview
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "powerapps"
author: "Mattp123"
ms.subservice: dataverse-maker
ms.author: "matp"
search.audienceType: 
  - maker
---
# Create new data columns in Dataverse

Columns in Microsoft Dataverse define the individual data items that can be used to store information in a table. Column data is used in apps to display information on forms, in views, and can be used in searches within an app. By default, the account main form has several columns,  such as account name, phone, fax, website, and so on.

:::image type="content" source="media/account-main-form-columns.png" alt-text="Several columns on the default account main form":::

With the exception of choices columns, all columns depend on a table. Columns support many different data types, such as text, number, date and time, lookup (links to another table), currency, autonumber, file, or Power Fx formula.

Create new columns to capture data when existing standard tables don’t have columns that meet your requirements. After you create a new column, be sure to include it on the appropriate forms and views for the table so that they are available in your app.

Watch this short video that shows you how to quickly create a column.
> [!VIDEO https://learn-video.azurefd.net/vod/player?id=f0015291-5024-4427-a669-dd230cf5c0c8]

## Create a column

1. Go to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), and then select **Solutions** in the left navigation pane. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]
1. Select the table where you want to add a column. If the solution doesn't already have the table, select **Add existing** > **Table** or to create a new table select **New** > **Table**.
1. On the tables page, select **New** > **Column**.

Go to these articles for more information about creating columns:

- [Types of columns](types-of-fields.md)
- [Create and edit columns in Dataverse using Power Apps](create-edit-field-portal.md)
- [Create and edit choice columns overview](create-edit-global-option-sets.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
