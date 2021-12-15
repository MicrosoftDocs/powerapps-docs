---
title: "Define alternate keys using solution explorer | MicrosoftDocs"
description: "Learn how to define alternate keys that can be used to reference rows in Microsoft Dataverse using solution explorer"
ms.custom: ""
ms.date: 08/01/2020
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
ms.subservice: dataverse-maker
ms.author: "matp"
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---
# Define alternate keys using solution explorer

[!INCLUDE[cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

Solution explorer provides one way to view and create alternate keys for Microsoft Dataverse.

The [Power Apps portal](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) enables configuring the most common options, but certain options can only be set using solution explorer. <br />More information: 
- [Define alternate keys to reference rows](define-alternate-keys-reference-records.md)<br />
- [Define alternate keys using Power Apps portal](define-alternate-keys-portal.md)

> [!IMPORTANT]
> If the data within a column that is used in an alternate key will contain one of the following characters `/`,`<`,`>`,`*`,`%`,`&`,`:`,`\\`,`?` then `GET` or `PATCH` actions will not work. If you only need uniqueness then this approach will work, but if you need to use these keys as part of data integration then it is best to create the key on columns that won't have data with those characters.

## Open solution explorer

Part of the name of any alternate key you create is the customization prefix. This is set based on the solution publisher for the solution you’re working in. If you care about the customization prefix, make sure that you are working in an unmanaged solution where the customization prefix is the one you want for this table. More information: [Change the solution publisher prefix](create-solution.md#solution-publisher) 

[!INCLUDE [cc_navigate-solution-from-powerapps-portal](../../includes/cc_navigate-solution-from-powerapps-portal.md)]

## View alternate keys

1. With solution explorer open, under **Components** expand **Entities** and select the table where you want to view alternate keys.
2. Expand the table and select **Keys**.

    ![View alternate keys.](media/view-alternate-keys-solution-explorer.png)

## Create an alternate key

1. While [viewing alternate keys](#view-alternate-keys), select **New**.
1. On the form, enter the **Display Name**. The **Name** column will be auto-populated based on the **Display Name**. 
2. From the **Available Attributes** list, select each attribute and then **Add >** to move the attribute into the **Selected Attributes** list.
    ![Create Alternate key.](media/create-alternate-key-solution-explorer.png)
1. Select **OK** to close the form.

### (Optional) View the system job tracking creation of indexes

1. While [viewing alternate keys](#view-alternate-keys) after you have created a new alternate key you will see a row for the key you created.
2. In the **System Job** column you will find a link to the system job that monitors the creation of the indexes to support the alternate key. 
    
    This system job will have a name that follows this pattern: `Create index for {0} for table {1}` where `0` is the **Display Name** of the alternate key and `1` is the name of the table.

    The link to the system job will not be displayed after the system job completes successfully. More information: [Monitor and manage system jobs](/power-platform/admin/monitor-manage-system-jobs)


## Delete an alternate key

While [viewing alternate keys](#view-alternate-keys), select ![Delete command.](media/delete.gif).

### See also

[Define alternate keys to reference rows](define-alternate-keys-reference-records.md)<br />
[Define alternate keys using Power Apps portal](define-alternate-keys-portal.md)<br />
[Developer Documentation: Work with alternate keys](../../developer/data-platform/define-alternate-keys-entity.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]