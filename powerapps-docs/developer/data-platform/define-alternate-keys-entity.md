---
title: "Work with alternate keys (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "The topic explains about how to create alternate keys for a table. Alternate keys can be created programmatically or by using the customization tools" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 03/12/2021
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "mayadumesh" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Work with alternate keys

All Microsoft Dataverse records have unique identifiers defined as GUIDs. These are the primary key for each table. When you need to integrate with an external data store, you might be able to add a column to the external database tables to contain a reference to the unique identifier in Dataverse. This allows you to have a local reference to link to the Dataverse record. However, sometimes you can't modify the external database. With alternate keys you can now define a column in a Dataverse table to correspond to a unique identifier (or unique combination of columns) used by the external data store. This alternate key can be used to uniquely identify a record in Dataverse in place of the primary key. You must be able to define which columns represent a unique identity for your records. Once you identify the columns that are unique to the table, you can declare them as alternate keys through the customization user interface (UI) or in the code. This topic provides information about defining alternate keys in the data model.  

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]

<a name="BKMK_Declare"></a>

## Create alternate keys  

You can create alternate keys programmatically or by using the customizations tools. For more information about using the customization tools, see [Define alternate keys using Power Apps](../../maker/data-platform/define-alternate-keys-portal.md).

To define alternate keys programmatically, you first have to create an object of type <xref:Microsoft.Xrm.Sdk.Metadata.EntityKeyMetadata> (or use <xref href="Microsoft.Dynamics.CRM.EntityKeyMetadata?text=EntityKeyMetadata EntityType" /> if working with Web API). This class contains the key columns. Once the key columns are set, you can use `CreateEntityKey` to create the keys for a table. This message takes the table name and `EntityKeyMetadata` values as input to create the key.  

You should be aware of the following constraints when creating alternate keys:  

- **Valid columns in key table definitions**  

   Only columns of the following types can be included in alternate key table definitions:  


  |      Column Type      |    Display Name     |
  |--------------------------|---------------------|
  | DecimalAttributeMetadata |   Decimal Number    |
  | IntegerAttributeMetadata |    Whole Number     |
  | StringAttributeMetadata  | Single line of text |
  | DateTimeAttributeMetadata   |      Date Time    |
  | LookupAttributeMetadata     |       Lookup        |
  | PicklistAttributeMetadata   |      Option Set       |


- **Valid key size**  

   When a key is created, the system validates that the key can be supported by the platform, including that the total key size does not violate SQL-based index constraints like 900 bytes per key and 16 columns per key. If the key size doesn't meet the constraints, an error message will be displayed.  

- **Maximum number of alternate key table definitions for a table**  

   There can be a maximum of ten alternate key table definitions for a table in a Dataverse instance.  

- **Unicode characters in key value**

  If the data within a column that is used in an alternate key will contain one of the following characters `/`,`<`,`>`,`*`,`%`,`&`,`:`,`\\`,`?` then retrieve (`GET`), update or upsert (`PATCH`) actions will not work.  If you only need uniqueness then this approach will work, but if you need to use these keys as part of data integration then it is best to create the key on columns that won't have data with those characters.

<a name="BKMK_crud"></a>   

## Retrieve and delete alternate keys  

If you need to retrieve or delete alternate keys, you can use the customization UI to do this, without writing any code. However, the SDK provides the following two messages to programmatically retrieve and delete alternate keys.  

|Message request class|Description|  
|---------------------------|-----------------|  
|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityKeyRequest>|Retrieves the specified alternate key.|  
|<xref:Microsoft.Xrm.Sdk.Messages.DeleteEntityKeyRequest>|Deletes the specified alternate key.|  

To retrieve all the keys for a table, use the new <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.Keys> property of `EntityMetadata` (<xref href="Microsoft.Dynamics.CRM.EntityMetadata?text=EntityMetadata EntityType" /> or <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata> class). It gets an array of keys for a table.  

<a name="BKMK_index"></a>   

## Monitor index creation for alternate keys  

Alternate keys use database indexes to enforce uniqueness and optimize lookup performance. If there are lots of existing records in a table, index creation can be a lengthy process. You can increase the responsiveness of the customization UI and solution import by doing the index creation as a background process. The `EntityKeyMetadata.AsyncJob` property (<xref href="Microsoft.Dynamics.CRM.EntityKeyMetadata?text=EntityKeyMetadata EntityType" /> or <xref:Microsoft.Xrm.Sdk.Metadata.EntityKeyMetadata>) refers to the asynchronous job that is doing the index creation. The `EntityKeyMetadata.EntityKeyIndexStatus` property specifies the status of the key as its index creation job progresses. The status could be any of the following:  

- Pending  
- In Progress  
- Active  
- Failed  

When an alternate key is created using the API, if the index creation fails, you can drill into details about the cause of the failure, correct the problems, and reactivate the key request using the `ReactivateEntityKey` (<xref href="Microsoft.Dynamics.CRM.ReactivateEntityKey?text=ReactivateEntityKey Action" /> or <xref:Microsoft.Xrm.Sdk.Messages.ReactivateEntityKeyRequest> message).  

If the alternate key is deleted while an index creation job is still pending or in progress, the job is cancelled and the index is deleted.  

### See also  
 [Using alternate keys](use-alternate-key-create-record.md)<br />
 [Use change tracking to synchronize data with external systems](use-change-tracking-synchronize-data-external-systems.md)<br />
 [Use Upsert to insert or update a record](use-upsert-insert-update-record.md)
 [Define alternate keys to reference records](../../maker/data-platform/define-alternate-keys-reference-records.md)
 


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
