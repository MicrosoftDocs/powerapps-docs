---
title: "Use an alternate key to reference a record (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Alternate keys can be used to create instances of Entity and EntityReference classes. This topic discusses the usage patterns and possible exceptions that might be thrown when using alternate keys." # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 06/13/2022
ms.reviewer: pehecke
ms.topic: article
author: divka78 # GitHub ID
ms.subservice: dataverse-developer
ms.author: dikamath # MSFT alias of Microsoft employees only
manager: sunilg # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors:
  - PHecke
  - JimDaly
---
# Use an alternate key to reference a record

You will use alternate keys with data integration scenarios to perform data operations where you don't know the primary key value of a Dataverse record. You can only use alternate keys for tables where they are defined. Most Dataverse tables will not have alternate keys unless they have been customized to include them.

To understand how to define and identify alternate keys for a table, see the following topics:

- [Using Power Apps: Define alternate keys to reference rows](../../maker/data-platform/define-alternate-keys-reference-records.md)
- [Using Code: Work with alternate keys](define-alternate-keys-entity.md)

You can use alternate keys using either the Datverse Web API or the Dataverse SDK for .NET.

# [Web API](#tab/webapi)

When using the Web API you must include the alternate key values in the URL that you use to reference a record. Without an alternate key, you simply include the GUID primary key value after the entity set name. 

For example, to reference an `account` record with the `accountid` primary key value of `00000000-0000-0000-0000-000000000001`, you can use an absolute or relative URL like this: `/accounts(00000000-0000-0000-0000-000000000001)`

But if the `account` entity has been configured with an alternate key, for example on the `accountnumber` column, then you must include the name of the column in the URL referencing the unique value in that column like this `/accounts(accountnumber='ABC123')`

An alternate key may include more than one column in the definition. The combination of values in both columns guarantees uniqueness. To refer to a record that has multiple columns as part of the key, you continue the pattern for a single column, but separate the key/value pairs with a comma. For example, if the `contact` table has an alternate key using both the `firstname` and `emailaddress1` columns, you can refer to that record like this: `/contacts(firstname='Joe',emailaddress1='abc@example.com')`.

When an alternate key is defined for a lookup column, you must use the name of the corresponding [Lookup Property](webapi/web-api-properties.md#lookup-properties). A lookup property follows the following naming convention: `_<name of single-valued navigation property>_value`. So if the primarycontactid lookup column on the account table is defined as an alternate key, you can reference the account record with this URL: `/accounts(_primarycontactid_value=00000000-0000-0000-0000-000000000002)`

More information: [Retrieve using an alternate key](webapi/retrieve-entity-using-web-api.md#retrieve-using-an-alternate-key)

# [SDK for .NET](#tab/sdk)

SDK

---



You can use alternate keys to create instances of <xref:Microsoft.Xrm.Sdk.Entity> and <xref:Microsoft.Xrm.Sdk.EntityReference> classes. This article discusses the usage patterns and possible exceptions that might be thrown when using alternate keys.



> [!NOTE]
> You can also update records using alternate keys. More information: [Update with Alternate Key](org-service/entity-operations-update-delete.md#update-with-alternate-key)
  
## Using alternate keys to create a table

You can create an <xref:Microsoft.Xrm.Sdk.Entity> with a primary ID, a single `KeyAttribute`, or a collection of key columns in a single call using these constructors.  
  
```csharp  
public Entity (string logicalName, Guid id) {…}    
public Entity (string logicalName, string keyName, object keyValue) {…}  
public Entity (string logicalName, KeyAttributeCollection keyAttributes) {…}  
  
```  
  
 A valid <xref:Microsoft.Xrm.Sdk.Entity> used for update operations includes a logical name of the table and one of the following:  
  
- A value for ID (primary key GUID value)
- A specified key value pair
- A <xref:Microsoft.Xrm.Sdk.KeyAttributeCollection> with a valid set of columns matching a defined key for the table.  
 
## Using alternate keys to create an EntityReference

You can also create an <xref:Microsoft.Xrm.Sdk.EntityReference> with a primary ID, a single `KeyAttribute`, or a collection of key columns in a single call using these constructors.  
  
```csharp  
public EntityReference(string logicalName, Guid id) {…}    
public EntityReference(string logicalName, string keyName, object keyValue) {…}    
public EntityReference(string logicalName, KeyAttributeCollection keyAttributeCollection) {…}  
  
```  
  
 A valid <xref:Microsoft.Xrm.Sdk.EntityReference> includes a logical name of the table and either:  
  
- A value for ID (primary key GUID value)  
- A specified key value pair
- A <xref:Microsoft.Xrm.Sdk.KeyAttributeCollection> collection with a valid set of columns matching a defined key for the table.  
  
<a name="BKMK_input"></a> 
  
## Alternative input to messages

When passing tables to <xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> and <xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest>, values provided for lookup columns using an <xref:Microsoft.Xrm.Sdk.EntityReference> can now use <xref:Microsoft.Xrm.Sdk.EntityReference> with alternate keys defined in <xref:Microsoft.Xrm.Sdk.EntityReference.KeyAttributes> to specify related record.  These will be resolved to and replaced by primary ID based table references before the messages are processed.  
  
<a name="BKMK_Exceptions"></a>   

## Exceptions when using alternate keys

You have to be aware of the following conditions and possible exceptions when using alternate keys:  
  
- The primary ID is used if it is provided. If it is not provided, it will examine the <xref:Microsoft.Xrm.Sdk.KeyAttributeCollection>.  If the <xref:Microsoft.Xrm.Sdk.KeyAttributeCollection> is not provided, it will throw an error.  
  
- If the provided <xref:Microsoft.Xrm.Sdk.KeyAttributeCollection> includes one column that is the primary key of the table and the value is valid, it populates the ID property of the <xref:Microsoft.Xrm.Sdk.Entity> or <xref:Microsoft.Xrm.Sdk.EntityReference> with the provided value.  
  
- If the key columns are provided, the system attempts to match the set of columns provided with the keys defined for the <xref:Microsoft.Xrm.Sdk.Entity>.  If it does not find a match, it will throw an error.  If it does find a match, it will validate the provided values for those columns. If valid, it will retrieve the ID of the record that matched the provided key values, and populate the ID value of the <xref:Microsoft.Xrm.Sdk.Entity> or <xref:Microsoft.Xrm.Sdk.EntityReference> with this value.  
  
- If you specify a column set that is not defined as a unique key, an error will be thrown indicating that use of unique key columns is required.  
  
### See also

[Define alternate keys for a table](define-alternate-keys-entity.md)   
[Use change tracking to synchronize data with external systems](use-change-tracking-synchronize-data-external-systems.md)   
[Use Upsert to insert or update a record](use-upsert-insert-update-record.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]