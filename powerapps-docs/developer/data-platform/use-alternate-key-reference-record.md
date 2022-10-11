---
title: "Use an alternate key to reference a record (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Alternate keys can be used to create instances of Entity and EntityReference classes. This topic discusses the usage patterns and possible exceptions that might be thrown when using alternate keys." # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 08/09/2022
ms.reviewer: pehecke
ms.topic: article
author: divka78 # GitHub ID
ms.subservice: dataverse-developer
ms.author: dikamath # MSFT alias of Microsoft employees only
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

When using the Web API you reference a specific record using a URL and then use the `POST`, `PATCH`, or `DELETE` Http methods to perform the data operation. You also use URLs to set values for single-valued navigation properties using the `@odata.bind` syntax, or as parameters to functions and actions.

The following table provides examples showing how to reference records using relative urls:

|Situation|Example|
|---------|---------|
|With a primary key|`/accounts(00000000-0000-0000-0000-000000000001)` OR<br />`accounts(accountid=00000000-0000-0000-0000-000000000001)`<br/>See note below about <xref:Microsoft.Dynamics.CRM.systemuser> and <xref:Microsoft.Dynamics.CRM.team> entity types|
|With single alternate key|`/accounts(accountnumber='ABC123')`|
|With multi-part alternate keys|`/contacts(firstname='Joe',emailaddress1='abc@example.com')`|
|With an alternate key that uses a lookup column|`/accounts(_primarycontactid_value=00000000-0000-0000-0000-000000000002)`<br />When an alternate key is defined for a lookup column, you must use the name of the corresponding [Lookup Property](webapi/web-api-properties.md#lookup-properties). A lookup property follows the following naming convention: `_<name of single-valued navigation property>_value`.|

> [!NOTE]
> Because of how <xref:Microsoft.Dynamics.CRM.systemuser> and <xref:Microsoft.Dynamics.CRM.team> entity types inherit from the <xref:Microsoft.Dynamics.CRM.principal> entity type, you cannot use a named primary key to reference these entities. The primary keys for both of these entities is `ownerid`, rather than `systemuserid` or `teamid`. The `principal` entity type doesn't support `GET` operations.  More information: [EntityType inheritance](webapi/web-api-entitytypes.md#entitytype-inheritance)

## Exceptions when using alternate keys with the Web API

You have to be aware of the following conditions and possible exceptions when using alternate keys:  
  
- If you specify a column that is not defined as a unique key, an error will be thrown indicating that use of unique key columns is required. The error message is: `The key in the request URI is not valid for resource 'Microsoft.Dynamics.CRM.<table logical name>'. Ensure that the names and number of key properties match the declared or alternate key properties for the resource 'Microsoft.Dynamics.CRM.<table logical name>'.`  

More information: [Retrieve using an alternate key](webapi/retrieve-entity-using-web-api.md#retrieve-using-an-alternate-key)

# [SDK for .NET](#tab/sdk)

When using the SDK for .NET, there are two ways to use alternate keys.

## Using the Entity class

When you create an instance of the <xref:Microsoft.Xrm.Sdk.Entity?text=Entity Class> you can specify the keys to use to identify the record using the following [Entity Constructors](/dotnet/api/microsoft.xrm.sdk.entity.-ctor): <!-- Not using <xref:Microsoft.Xrm.Sdk.Entity.%23ctor?text=Entity Constructors>: b/c it links to mid-page -->

```csharp  
// For use with the primary key
public Entity (string logicalName, Guid id) {…} 
// For use with a single alternate key value
public Entity (string logicalName, string keyName, object keyValue) {…} 
// For use with multiple alternate key values
public Entity (string logicalName, KeyAttributeCollection keyAttributes) {…}  
```

These values are added to the <xref:Microsoft.Xrm.Sdk.Entity.KeyAttributes?text=Entity.KeyAttributes Property>, not the <xref:Microsoft.Xrm.Sdk.Entity.Attributes?text=Entity.Attributes Property>. `KeyAttributes` are used to identify a record. `Attributes` contains the data for the record.

For example, when a table has an alternate key that includes two alternate key columns, you can define the entity this way.

```csharp
KeyAttributeCollection keys = new KeyAttributeCollection() {
   { "example_key1", 5 },
   { "example_key2", 5 }
};

Entity thing = new Entity("example_thing", keys);
thing["example_name"] = "Test Name";
```

## Using the EntityReference class

When you create an instance of the <xref:Microsoft.Xrm.Sdk.EntityReference?text=EntityReference Class> you can specify the keys to use to identify the record using the following <xref:Microsoft.Xrm.Sdk.EntityReference.%23ctor?text=EntityReference Constructors> that use the same pattern as the <xref:Microsoft.Xrm.Sdk.Entity?text=Entity Class> constructors.

```csharp
// For use with the primary key
public EntityReference(string logicalName, Guid id) {…}
// For use with a single alternate key value
public EntityReference(string logicalName, string keyName, object keyValue) {…} 
// For use with multiple alternate key values
public EntityReference(string logicalName, KeyAttributeCollection keyAttributeCollection) {…}    
```

- You can use `EntityReference` to set values for entity lookup columns. When used to set a lookup column, the key values are used to find the primary key value, and the primary key values is stored in the database.
- You can use `EntityReference` for messages that use this type as a property, such as `Delete` using <xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest?text=DeleteRequest>.

<a name="BKMK_Exceptions"></a>

## Exceptions when using alternate keys with the SDK for .NET

You have to be aware of the following conditions and possible exceptions when using alternate keys:  
  
- The <xref:Microsoft.Xrm.Sdk.Entity.Id?text=Entity.Id Property> will be used if it is provided. If it is not provided, it will examine the <xref:Microsoft.Xrm.Sdk.KeyAttributeCollection>.  If the <xref:Microsoft.Xrm.Sdk.KeyAttributeCollection> is not provided, it will throw an error.  
- If the provided <xref:Microsoft.Xrm.Sdk.KeyAttributeCollection> includes one column that is the primary key of the table and the value is valid, it populates the <xref:Microsoft.Xrm.Sdk.Entity.Id?text=Entity.Id Property> or <xref:Microsoft.Xrm.Sdk.EntityReference.Id?text=EntityReference.Id Property> with the provided value.  
- If the key columns are provided, the system attempts to match the set of columns provided with the keys defined for the <xref:Microsoft.Xrm.Sdk.Entity>.  If it does not find a match, it will throw an error.  If it does find a match, it will validate the provided values for those columns. If valid, it will retrieve the primary key value of the record that matched the provided alternate key values, and populate the <xref:Microsoft.Xrm.Sdk.Entity.Id?text=Entity.Id Property> or <xref:Microsoft.Xrm.Sdk.EntityReference.Id?text=EntityReference.Id Property> with this value.  
- If you specify a column that is not defined as a unique key, an error will be thrown indicating that use of unique key columns is required.  

---  

  
### See also

[Define alternate keys for a table](define-alternate-keys-entity.md)   
[Use change tracking to synchronize data with external systems](use-change-tracking-synchronize-data-external-systems.md)   
[Use Upsert to insert or update a record](use-upsert-insert-update-record.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
