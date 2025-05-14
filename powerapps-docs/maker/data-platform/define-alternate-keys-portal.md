---
title: "Define alternate keys using Power Apps"
description: "Learn how to define alternate keys using Power Apps"
ms.date: 05/14/2025
ms.reviewer: ""
ms.topic: "how-to"
author: "Mattp123"
ms.subservice: dataverse-maker
ms.author: "matp"
search.audienceType: 
  - maker
---
# Define alternate keys using Power Apps

Power Apps provides an easy way to view and create table alternate keys with Microsoft Dataverse. *Alternate keys* provide an efficient and accurate way of integrating data with external systems. It’s essential in cases when an external system doesn’t store the globally unique identifier (GUID) IDs that uniquely identify rows in Microsoft Dataverse. For more information about alternate keys, see [Define alternate keys to reference rows](define-alternate-keys-reference-records.md).

> [!IMPORTANT]
> If the data within a column that is used in an alternate key contains one of the following characters `/`, `#`,`<`,`>`,`*`,`%`,`&`,`:`,`\\`,`?`,`+` then `GET` or `PATCH` actions won't work. If you only need uniqueness, then this approach works, but if you need to use these keys as part of data integration then it's best to create the key on columns that won't have data with those characters.

## View alternate keys

1. In [Power Apps]([https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), go to **Solutions** and open the solution you want. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]
1. Select **Tables** on the left **Objects** pane, and then open the table that you want to view.
1. In the **Schema** area, select **Keys** to view a list of any alternate keys that might be defined.

## Create an alternate key

1. While [viewing alternate keys](#view-alternate-keys), select **New key**.
1. In the Key properties pane, enter the following information: 
   1. Set a **Display name** and choose the columns to use to create the alternate key. 
   1. The **Name** column is populated based on the display name. You can change it if you want.
   1. Select the columns that you want. For example, to identify an account row with an alternate key, you can use the **Account Number** column in combination with some other column, such as the **SIC Code**, which have values that shouldn't change.

    ![Example Alternate Key Definition.](media/alternate-key-account-number-sic-code.png)

1. Select **Save** to create the alternate key.

> [!NOTE]
> The alternate key isn't immediately available for use. A system job is initiated when you save the table to create database indexes to support the alternate key.

## Delete an alternate key

While [viewing alternate keys](#view-alternate-keys), select the key you want to delete and select **Remove** > **Remove from this solution** or to delete the key from the Power Platform environment **Delete from this environment** on the command bar.

### Related articles

[Developer Documentation: Work with alternate keys](../../developer/data-platform/define-alternate-keys-entity.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
