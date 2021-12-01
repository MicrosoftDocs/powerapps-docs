---
title: "Define alternate keys to reference rows with Microsoft Dataverse | MicrosoftDocs"
description: "Learn how to define alternate keys that can be used to reference rows in Microsoft Dataverse"
ms.custom: ""
ms.date: 06/24/2020
ms.reviewer: ""
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "conceptual"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "powerapps"
author: "Mattp123"
ms.assetid: 29e53691-0b18-4fde-a1d0-7490aa227898
caps.latest.revision: 10
ms.subservice: dataverse-maker
ms.author: "matp"
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---
# Define alternate keys to reference rows

[!INCLUDE[cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

*Alternate keys* provide an efficient and accurate way of integrating data with external systems. It’s essential in cases when an external system doesn’t store the Globally Unique Identifier (GUID) IDs that uniquely identify rows in Microsoft Dataverse. 

A data integration system will use alternate keys to uniquely identify rows using one or more table column values that represent a unique combination. Each alternate key has a unique name. 

For example, to identify an account row with an alternate key, you can use the account number or the account number column in combination with some other columns which have values that should not change.

> [!NOTE]
> While you can define alternate keys with Power Apps, they can only be used programmatically in code. 
> To learn more about using alternate keys programmatically, see:   
> - [Developer Documentation: Use an alternate key to create a row](/dynamics365/customer-engagement/developer/use-alternate-key-create-record) 
> - [Developer Documentation: Retrieve a row with the Web API using an alternate key](/dynamics365/customer-engagement/developer/webapi/retrieve-entity-using-web-api#retrieve-using-an-alternate-key)

Some of the benefits of the alternate keys feature include:  
  
- Faster lookup of the rows.  
- More robust bulk data operations.  
- Simplified programming with data imported from external systems without row IDs.  
  

## Creating an alternate key

There are two designers you can use to create alternate keys:

|Designer| Description|
|--|--|
|[Power Apps portal](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc)|Provides an easy streamlined experience, but some options are not available.<br />More information: [Define alternate keys using Power Apps portal](define-alternate-keys-portal.md)|
|Solution explorer|Not as easy, but provides for more flexibility for less common requirements.<br />More information: [Define alternate keys using solution explorer](define-alternate-keys-solution-explorer.md) |

> [!NOTE]
> You can also create an alternate key in your environment using the following:
> - Import a solution that contains the definition of the alternate key.
> - A developer can also write code to create them. More information: [Developer Documentation: Define alternate keys for a table](/dynamics365/customer-engagement/developer/define-alternate-keys-entity)

Information in this topic will help you choose which designer you can use. 

You should use the [Power Apps portal](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) to create alternate keys unless you need to address any of the following requirements:

- Create an alternate key within a solution other than the Common Data Service Default Solution
- You want to easily track the system job created that tracks the progress of creating the supporting indexes


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

### Number of keys

You can define up to ten different keys for a table.
 
### Valid key size

When a key is created, the system validates that the key can be supported by the platform, including that the total key size does not violate SQL-based index constraints like 900 bytes per key and 16 columns per key. If the key size doesn’t meet the constraints, an error message will be displayed.

### Unicode characters in key value

If the data within a column that is used in an alternate key will contain one of the following characters `<`,`>`,`*`,`%`,`&`,`:`,`/`,`\\` then update or upsert (PATCH) actions will not work.

If you only need uniqueness then this approach will work, but if you need to use these keys as part of data integration then it is best to create the key on columns that won't have data with these characters.

## Track the status of the creation of the alternate key

When an alternate key is created it will initiate a system job to create indexes on the database tables to enforce unique constraints on the columns used by the alternate key. The alternate key will not be in effect until these indexes are created. Creating these indexes may take some time depending on the amount of data in the system. 

The status of the system job determines the state of the alternate key. The alternate key can have the following states:
- **Pending**
- **In Progress**
- **Active**
- **Failed**

When the system job is completed, the alternate key status is **Active** and it is available for use.

If the system job fails, locate the system job to view any errors. The system job will have a name that follows this pattern: `Create index for {0} for table {1}` where `0` is the **Display Name** of the alternate key and `1` is the name of the table.


> [!NOTE]
> If you want to monitor the status of the system job you should use solution explorer to create the index. It will include a link to the system job so you can monitor it. More information: [(Optional) View the system job tracking creation of indexes](define-alternate-keys-solution-explorer.md#optional-view-the-system-job-tracking-creation-of-indexes)
  
  
### See also  

[Define alternate keys using Power Apps portal](define-alternate-keys-portal.md)<br />
[Define alternate keys using solution explorer](define-alternate-keys-solution-explorer.md)<br />
[Developer Documentation: Define alternate keys for a table](/dynamics365/customer-engagement/developer/define-alternate-keys-entity)<br />
[Developer Documentation: Use an alternate key to create a row](/dynamics365/customer-engagement/developer/use-alternate-key-create-record)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
