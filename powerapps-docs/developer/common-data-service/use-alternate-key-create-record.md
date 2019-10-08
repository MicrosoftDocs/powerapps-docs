---
title: "Use an alternate key to create a record (Common Data Service) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Alternate keys can be used to create instances of Entity and EntityReference classes. This topic discusses the usage patterns and possible exceptions that might be thrown when using alternate keys." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 04/21/2019
ms.reviewer: ""
ms.service: powerapps
ms.topic: "article"
author: "JimDaly" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Use an alternate key to create a record

You can use alternate keys to create instances of <xref:Microsoft.Xrm.Sdk.Entity> and <xref:Microsoft.Xrm.Sdk.EntityReference> classes. This topic discusses the usage patterns and possible exceptions that might be thrown when using alternate keys. To understand how to define alternate keys for an entity, see [Define alternate keys for an entity](define-alternate-keys-entity.md).  

> [!NOTE]
> You can also update records using alternate keys. More information: [Update with Alternate Key](org-service/entity-operations-update-delete.md#update-with-alternate-key)
  
<a name="BKMK_entity"></a>

## Using alternate keys to create an entity

You can create an <xref:Microsoft.Xrm.Sdk.Entity> with a primary ID, a single `KeyAttribute`, or a collection of key attributes in a single call using these constructors.  
  
```csharp  
public Entity (string logicalName, Guid id) {…}    
public Entity (string logicalName, string keyName, object keyValue) {…}  
public Entity (string logicalName, KeyAttributeCollection keyAttributes) {…}  
  
```  
  
 A valid <xref:Microsoft.Xrm.Sdk.Entity> used for update operations includes a logical name of the entity and one of the following:  
  
- A value for ID (primary key GUID value)
- A specified key value pair
- A <xref:Microsoft.Xrm.Sdk.KeyAttributeCollection> with a valid set of attributes matching a defined key for the entity.  
  
<a name="BKMK_EntityReference"></a>

## Using alternate keys to create an EntityReference

You can also create an <xref:Microsoft.Xrm.Sdk.EntityReference> with a primary ID, a single `KeyAttribute`, or a collection of key attributes in a single call using these constructors.  
  
```csharp  
public EntityReference(string logicalName, Guid id) {…}    
public EntityReference(string logicalName, string keyName, object keyValue) {…}    
public EntityReference(string logicalName, KeyAttributeCollection keyAttributeCollection) {…}  
  
```  
  
 A valid <xref:Microsoft.Xrm.Sdk.EntityReference> includes a logical name of the entity and either:  
  
- A value for ID (primary key GUID value)  
- A specified key value pair
- A <xref:Microsoft.Xrm.Sdk.KeyAttributeCollection> collection with a valid set of attributes matching a defined key for the entity.  
  
<a name="BKMK_input"></a> 
  
## Alternative input to messages

When passing entities to <xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> and <xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest>, values provided for lookup attributes using an <xref:Microsoft.Xrm.Sdk.EntityReference> can now use <xref:Microsoft.Xrm.Sdk.EntityReference> with alternate keys defined in <xref:Microsoft.Xrm.Sdk.EntityReference.KeyAttributes> to specify related record.  These will be resolved to and replaced by primary ID based entity references before the messages are processed.  
  
<a name="BKMK_Exceptions"></a>   

## Exceptions when using alternate keys

You have to be aware of the following conditions and possible exceptions when using alternate keys:  
  
- The primary ID is used if it is provided. If it is not provided, it will examine the <xref:Microsoft.Xrm.Sdk.KeyAttributeCollection>.  If the <xref:Microsoft.Xrm.Sdk.KeyAttributeCollection> is not provided, it will throw an error.  
  
- If the provided <xref:Microsoft.Xrm.Sdk.KeyAttributeCollection> includes one attribute that is the primary key of the entity and the value is valid, it populates the ID property of the <xref:Microsoft.Xrm.Sdk.Entity> or <xref:Microsoft.Xrm.Sdk.EntityReference> with the provided value.  
  
- If the key attributes are provided, the system attempts to match the set of attributes provided with the keys defined for the <xref:Microsoft.Xrm.Sdk.Entity>.  If it does not find a match, it will throw an error.  If it does find a match, it will validate the provided values for those attributes. If valid, it will retrieve the ID of the record that matched the provided key values, and populate the ID value of the <xref:Microsoft.Xrm.Sdk.Entity> or <xref:Microsoft.Xrm.Sdk.EntityReference> with this value.  
  
- If you specify an attribute set that is not defined as a unique key, an error will be thrown indicating that use of unique key attributes is required.  
  
### See also

[Define alternate keys for an entity](define-alternate-keys-entity.md)   
[Use change tracking to synchronize data with external systems](use-change-tracking-synchronize-data-external-systems.md)   
[Use Upsert to insert or update a record](use-upsert-insert-update-record.md)
