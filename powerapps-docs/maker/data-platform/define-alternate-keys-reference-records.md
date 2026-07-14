---
title: "Define alternate keys to reference rows with Microsoft Dataverse | MicrosoftDocs"
description: "Learn how to define alternate keys that can be used to reference rows in Microsoft Dataverse"
ms.custom: ""
ms.date: 12/01/2023
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: article
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "powerapps"
author: "Mattp123"
contributors:
- NHelgren
ms.assetid: 29e53691-0b18-4fde-a1d0-7490aa227898
caps.latest.revision: 10
ms.subservice: dataverse-maker
ms.author: "matp"
search.audienceType: 
  - maker
---
# Define alternate keys to reference rows

*Alternate keys* provide an efficient and accurate way of integrating data with external systems. It's essential in cases when an external system doesn't store the Globally Unique Identifier (GUID) IDs that uniquely identify rows in Microsoft Dataverse. 

A data integration system uses alternate keys to uniquely identify rows using one or more table column values that represent a unique combination. Each alternate key has a unique name. 

For example, to identify an account row with an alternate key, you can use the account number or the account number column in combination with some other columns, which have values that shouldn't change.

> [!NOTE]
> While you can define alternate keys with Power Apps, they can only be used programmatically in code. 
> To learn more about using alternate keys programmatically, see:   
> - [Developer Documentation: Use an alternate key to reference a record](../../developer/data-platform/use-alternate-key-reference-record.md)
> - [Developer Documentation: Retrieve record using an alternate key](../../developer/data-platform/webapi/retrieve-entity-using-web-api.md#retrieve-record-using-an-alternate-key)

Some of the benefits of the alternate keys feature include:  
  
- Faster lookup of the rows.  
- More robust bulk data operations.  
- Simplified programming with data imported from external systems without row IDs.  
  

## Creating an alternate key

There are two designers you can use to create alternate keys:

|Designer| Description|
|--|--|
|[Power Apps portal](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc)|Provides an easy streamlined experience, but some options aren't available.<br />More information: [Define alternate keys using Power Apps portal](define-alternate-keys-portal.md)|
|Solution explorer|Not as easy, but provides for more flexibility for less common requirements.<br />More information: [Define alternate keys using solution explorer](define-alternate-keys-solution-explorer.md) |

> [!NOTE]
> You can also create an alternate key in your environment using the following:
> - Import a solution that contains the definition of the alternate key.
> - A developer can also write code to create them. More information: [Developer Documentation: Work with alternate keys](../../developer/data-platform/define-alternate-keys-entity.md)

Information in this article helps you choose which designer you can use. 

You should use the [Power Apps portal](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) to create alternate keys unless you need to address any of the following requirements:

- Create an alternate key within a solution other than the Common Data Service Default Solution.
- You want to easily track the system job created that tracks the progress of creating the supporting indexes.


## Limits in creating alternate keys

There are constraints on alternate key creation.

### Fields that can be used for alternate keys

Only these kinds of columns can be used to create alternate keys:
 - Decimal
 - Whole Number (Integer)
 - Single line of Text (String)
 - Date and Time
 - Lookup
 - Choice

> [!NOTE]
>
> - Columns that have the **Enable column security** property enabled can't be used as an alternate key. More information: [Field security tables]( /power-apps/developer/data-platform/field-security-entities)
> - When NULL values are used in alternate key columns, uniqueness will not be enforced. To avoid duplicate records, don't use null values in the columns defined in the unique constraint of the alternate key.

### Number of keys

You can define up to 10 different keys for a table.
 
### Valid key size

When a key is created, the system validates that the key can be supported by the platform, including that the total key size doesn't violate SQL-based index constraints like 900 bytes per key and 16 columns per key. If the key size doesn't meet the constraints, an error message is displayed.

### Unicode characters in key value

If the data within a column that is used in an alternate key contains one of the following characters `<`,`>`,`*`,`%`,`&`,`:`,`/`,`\\`,`#` then update or upsert (PATCH) actions won't work.

If you only need uniqueness, then this approach works, but if you need to use these keys as part of data integration then it's best to create the key on columns that doesn't have data with these characters.

## Track the status of the creation of the alternate key

When an alternate key is created, it initiates a system job to create indexes on the database tables to enforce unique constraints on the columns used by the alternate key. The alternate key won't be in effect until these indexes are created. Creating these indexes might take some time depending on the amount of data in the system. 

The status of the system job determines the state of the alternate key. The alternate key can have the following states:
- **Pending**
- **In Progress**
- **Active**
- **Failed**

When the system job is completed, the alternate key status is **Active** and it's available for use.

If the system job fails, locate the system job to view any errors. The system job will have a name that follows this pattern: `Create index for {0} for table {1}` where `0` is the **Display Name** of the alternate key and `1` is the name of the table.


> [!NOTE]
> If you want to monitor the status of the system job you should use solution explorer to create the index. It will include a link to the system job so you can monitor it. More information: [(Optional) View the system job tracking creation of indexes](define-alternate-keys-solution-explorer.md#optional-view-the-system-job-tracking-creation-of-indexes)
  
  
### See also  

[Define alternate keys using Power Apps portal](define-alternate-keys-portal.md)  
[Define alternate keys using solution explorer](define-alternate-keys-solution-explorer.md)  
[Developer Documentation: Work with alternate keys](../../developer/data-platform/define-alternate-keys-entity.md)  
[Developer Documentation: Use an alternate key to reference a record](../../developer/data-platform/use-alternate-key-reference-record.md)  
[Developer Documentation: Retrieve record using an alternate key](../../developer/data-platform/webapi/retrieve-entity-using-web-api.md#retrieve-record-using-an-alternate-key)  


[!INCLUDE[footer-include](../../includes/footer-banner.md)]