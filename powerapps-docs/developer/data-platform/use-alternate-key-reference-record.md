---
title: Use an alternate key to reference a record
description: Alternate keys can be used to create instances of Entity and EntityReference classes. This article discusses the usage patterns and possible exceptions that might be thrown when using alternate keys.
#customer intent: As a developer working with data integration, I want to reference a Dataverse record using an alternate key, so that I can perform data operations without knowing the primary key value.
ms.date: 06/11/2026
ms.reviewer: pehecke
ms.topic: how-to
author: kewear
ms.subservice: dataverse-developer
ms.author: kewear
search.audienceType: 
  - developer
contributors:
  - PHecke
  - JimDaly
---
# Use an alternate key to reference a record

Use alternate keys with data integration scenarios to perform data operations when you don't know the primary key value of a Dataverse record. You can only use alternate keys for tables where they're defined. Most Dataverse tables don't have alternate keys unless you customize them to include alternate keys.

To understand how to define and identify alternate keys for a table, see the following articles:

- [Using Power Apps: Define alternate keys to reference rows](../../maker/data-platform/define-alternate-keys-reference-records.md)
- [Using Code: Work with alternate keys](define-alternate-keys-entity.md)

Use either the Dataverse Web API or SDK for .NET to work with alternate keys.

# [Web API](#tab/webapi)

When you use the Web API, you reference a specific record by using a URL. Then, use the `POST`, `PATCH`, or `DELETE` HTTP methods to perform the data operation. You also use URLs to set values for single-valued navigation properties by using the `@odata.bind` syntax, or as parameters to functions and actions.

The following table provides examples that show how to reference records by using relative URLs:

|Situation|Example|
|---------|---------|
|With a primary key|`/accounts(00000000-0000-0000-0000-000000000001)` OR<br />`accounts(accountid=00000000-0000-0000-0000-000000000001)`<br/>See following note about <xref:Microsoft.Dynamics.CRM.systemuser> and <xref:Microsoft.Dynamics.CRM.team> entity types|
|With single alternate key|`/accounts(accountnumber='ABC123')`|
|With multi-part alternate keys|`/contacts(firstname='Joe',emailaddress1='abc@example.com')`|
|With an alternate key that uses a lookup column|`/accounts(_primarycontactid_value=00000000-0000-0000-0000-000000000002)`<br />When you define an alternate key for a lookup column, you must use the name of the corresponding [Lookup Property](webapi/web-api-properties.md#lookup-properties). A lookup property follows the following naming convention: `_<name of single-valued navigation property>_value`.|

> [!NOTE]
> Because of how <xref:Microsoft.Dynamics.CRM.systemuser> and <xref:Microsoft.Dynamics.CRM.team> entity types inherit from the <xref:Microsoft.Dynamics.CRM.principal> entity type, you can't use a named primary key to reference these entities. The primary keys for both of these entities is `ownerid`, rather than `systemuserid` or `teamid`. The `principal` entity type doesn't support `GET` operations.  More information: [EntityType inheritance](webapi/web-api-entitytypes.md#entitytype-inheritance)

## Exceptions when using alternate keys with the Web API

Be aware of the following conditions and possible exceptions when using alternate keys:  

- If you specify a column that isn't defined as a unique key, an error occurs. The error message is: `The key in the request URI is not valid for resource 'Microsoft.Dynamics.CRM.<table logical name>'. Ensure that the names and number of key properties match the declared or alternate key properties for the resource 'Microsoft.Dynamics.CRM.<table logical name>'.`  
- Alternate key values can't include some special characters.

  [!INCLUDE [cc-filter-workaround-alternate-key](includes/cc-filter-workaround-alternate-key.md)]

More information: [Retrieve record using an alternate key](webapi/retrieve-entity-using-web-api.md#retrieve-record-using-an-alternate-key)

# [SDK for .NET](#tab/sdk)

When you use the SDK for .NET, you can use alternate keys in two ways.

## Using the Entity class

When you create an instance of the [Entity class](xref:Microsoft.Xrm.Sdk.Entity), specify the keys to identify the record by using the following [Entity Constructors](/dotnet/api/microsoft.xrm.sdk.entity.-ctor): 

```csharp  
// For use with the primary key
public Entity (string logicalName, Guid id) {…} 
// For use with a single alternate key value
public Entity (string logicalName, string keyName, object keyValue) {…} 
// For use with multiple alternate key values
public Entity (string logicalName, KeyAttributeCollection keyAttributes) {…}  
```

These constructors add values to the [Entity.KeyAttributes property](xref:Microsoft.Xrm.Sdk.Entity.KeyAttributes), not the [Entity.Attributes property](xref:Microsoft.Xrm.Sdk.Entity.Attributes). Use `KeyAttributes` to identify a record. `Attributes` contains the data for the record.

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

When you create an instance of the [EntityReference class](xref:Microsoft.Xrm.Sdk.EntityReference), specify the keys to identify the record by using the following [EntityReference constructors](xref:Microsoft.Xrm.Sdk.EntityReference.%23ctor) that use the same pattern as the [Entity class](xref:Microsoft.Xrm.Sdk.Entity) constructors.

```csharp
// For use with the primary key
public EntityReference(string logicalName, Guid id) {…}
// For use with a single alternate key value
public EntityReference(string logicalName, string keyName, object keyValue) {…} 
// For use with multiple alternate key values
public EntityReference(string logicalName, KeyAttributeCollection keyAttributeCollection) {…}    
```

- Use `EntityReference` to set values for entity lookup columns. When you use it to set a lookup column, the key values find the primary key value, and the primary key value is stored in the database.
- Use `EntityReference` for messages that use this type as a property, such as `Delete` by using the [DeleteRequest class](xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest).

<a name="BKMK_Exceptions"></a>

## Exceptions when using alternate keys with the SDK for .NET

Be aware of the following conditions and possible exceptions when using alternate keys:  
  
- The SDK uses the [Entity.Id property](xref:Microsoft.Xrm.Sdk.Entity.Id) if you provide it. If you don't provide it, the SDK examines the <xref:Microsoft.Xrm.Sdk.KeyAttributeCollection>. If you don't provide the <xref:Microsoft.Xrm.Sdk.KeyAttributeCollection>, the SDK throws an error.  
- If the provided <xref:Microsoft.Xrm.Sdk.KeyAttributeCollection> includes one column that is the primary key of the table and the value is valid, the SDK populates the [Entity.Id property](xref:Microsoft.Xrm.Sdk.Entity.Id) or [EntityReference.Id Property](xref:Microsoft.Xrm.Sdk.EntityReference.Id) with the provided value.  
- If you provide key columns, the system attempts to match the set of columns you provide with the keys defined for the <xref:Microsoft.Xrm.Sdk.Entity>.  If it doesn't find a match, it throws an error. If it finds a match, it validates the provided values for those columns. If valid, it retrieves the primary key value of the record that matched the provided alternate key values, and populates the [Entity.Id property](xref:Microsoft.Xrm.Sdk.Entity.Id) or [EntityReference.Id Property](xref:Microsoft.Xrm.Sdk.EntityReference.Id) with this value.  
- If you specify a column that isn't defined as a unique key, the SDK throws an error indicating that use of unique key columns is required.  

---  

  
### See also

[Define alternate keys for a table](define-alternate-keys-entity.md)   
[Use change tracking to synchronize data with external systems](use-change-tracking-synchronize-data-external-systems.md)   
[Use Upsert to insert or update a record](use-upsert-insert-update-record.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
