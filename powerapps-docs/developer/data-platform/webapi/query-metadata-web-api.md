---
title: "Query table definitions using the Web API (Microsoft Dataverse) | Microsoft Docs"
description: "The capability to query table definitions (metadata) is available using the Web API as well as using the Organization service by using RetrieveMetadataChangesRequest"
ms.custom: ""
ms.date: 04/21/2021
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
ms.assetid: 3ad4a332-a304-421f-a9fa-82ea3e0503fe
caps.latest.revision: 18
author: "JimDaly" # GitHub ID
ms.author: "jdaly"
ms.reviewer: "pehecke"
manager: "annbe"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Query table definitions using the Web API

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

Because Microsoft Dataverse is a metadata-driven application, developers may need to query the system definitions at run-time to adapt to how an organization has been configured. This capability uses a RESTful query style.

> [!NOTE]
> You can also construct a query using an object-based style using the <xref:Microsoft.Dynamics.CRM.EntityQueryExpression?text=EntityQueryExpression ComplexType/> with the <xref:Microsoft.Dynamics.CRM.RetrieveMetadataChanges?text=RetrieveMetadataChanges Function/>. This function allows for capturing changes to table definitions between two periods of time as well as returning a limited set of definitions described by a query you specify.

<a name="bkmk_QueryingEntityMetadata"></a>

## Querying the EntityMetadata entity type

You’ll use the same techniques described in [Query data using the Web API](query-data-web-api.md) when you query EntityMetadata, with a few variations. Use the `EntityDefinitions` entity set path to retrieve information about the <xref:Microsoft.Dynamics.CRM.EntityMetadata?text=EntityMetadata EntityType/>. EntityMetadata entities contain a lot of data so you will want to be careful to only retrieve the data that you need. The following example shows the data returned for just the DisplayName, IsKnowledgeManagementEnabled, and EntitySetName properties of the definition for the `Account` entity. The `MetadataId` property value is always returned.  
  
 **Request**

```http
GET [Organization URI]/api/data/v9.0/EntityDefinitions(LogicalName='account')?$select=DisplayName,IsKnowledgeManagementEnabled,EntitySetName HTTP/1.1  
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
```

 **Response**
```http
HTTP/1.1 200 OK  
Content-Type: application/json; odata.metadata=minimal  
OData-Version: 4.0  

{  
 "@odata.context": "[Organization URI]/api/data/v9.0/$metadata#EntityDefinitions(DisplayName,IsKnowledgeManagementEnabled,EntitySetName)",  
 "value": [  
  {  
   "DisplayName": {  
    "LocalizedLabels": [  
     {  
      "Label": "Account",  
      "LanguageCode": 1033,  
      "IsManaged": true,  
      "MetadataId": "2a4901bf-2241-db11-898a-0007e9e17ebd",  
      "HasChanged": null  
     }  
    ],  
    "UserLocalizedLabel": {  
     "Label": "Account",  
     "LanguageCode": 1033,  
     "IsManaged": true,  
     "MetadataId": "2a4901bf-2241-db11-898a-0007e9e17ebd",  
     "HasChanged": null  
    }  
   },  
   "IsKnowledgeManagementEnabled": false,  
   "EntitySetName": "accounts",  
   "MetadataId": "70816501-edb9-4740-a16c-6a5efbc05d84"  
  }  
 ]  
}  
  
```

You can use any of the `EntityMetadata` properties with `$select` system query options and you can use `$filter` on any properties which use primitive or enumeration values.  

There are no limits on the number of metadata entities that will be returned in a query. There is no paging. All matching resources will be returned in the first response.  

<a name="bkmk_filterEnumTypes"></a>

## Use enum types in $filter operations

When you need to filter metadata entities based on the value of a property that uses an enumeration, you must include the namespace of the enumeration before the string value. Enum types are used as property values only in metadata entities and complex types. For example, if you need to filter entities based on the `OwnershipType` property, which uses the <xref href="Microsoft.Dynamics.CRM.OwnershipTypes?text=OwnershipTypes EnumType" />, you can use the following `$filter` to return only those entities that are UserOwned.

```http
GET [Organization URI]/api/data/v9.0/EntityDefinitions?$select=LogicalName&$filter=OwnershipType eq Microsoft.Dynamics.CRM.OwnershipTypes'UserOwned'  
```

<a name="bkmk_complexTypesAsFilters"></a>

## Use complex types in $filter operations

When you need to filter metadata entities based on the value of a property that uses a complex type, you must include the path to the underlying primitive type. Complex types are used as property values only in metadata entities. For example, if you need to filter entities based on the CanCreateAttributes property, which uses the <xref href="Microsoft.Dynamics.CRM.BooleanManagedProperty?text=BooleanManagedProperty ComplexType" />, you can use the following `$filter` to return only those entities that have a `Value` of `true`.

```http
GET [Organization URI]/api/data/v9.0/EntityDefinitions?$select=LogicalName&$filter=CanCreateAttributes/Value eq true  
```

This pattern works with <xref href="Microsoft.Dynamics.CRM.BooleanManagedProperty?text=BooleanManagedProperty ComplexType" /> because the primitive value to check is one level deep. However, this does not work on properties of <xref href="Microsoft.Dynamics.CRM.Label?text=Label ComplexType" />.  

<a name="bkmk_queryAttributes"></a>

## Querying EntityMetadata attributes

You can query entity attributes in the context of an entity by expanding the `Attributes` collection-valued navigation property but this will only include the common properties available in the <xref href="Microsoft.Dynamics.CRM.AttributeMetadata?text=AttributeMetadata EntityType" /> which all attributes share. For example the following query will return the `LogicalName` of the entity and all the expanded Attributes which have an `AttributeType` value equal to the <xref href="Microsoft.Dynamics.CRM.AttributeTypeCode?text=AttributeTypeCode EnumType" /> value of `Picklist`.

<a name="bkmk_queryAttributesexample"></a>

```http
GET [Organization URI]/api/data/v9.0/EntityDefinitions(LogicalName='account')?$select=LogicalName&$expand=Attributes($select=LogicalName;$filter=AttributeType eq Microsoft.Dynamics.CRM.AttributeTypeCode'Picklist')  
```

But you can’t include the `OptionSet` or `GlobalOptionSet` collection-valued navigation properties that <xref href="Microsoft.Dynamics.CRM.PicklistAttributeMetadata?text=PicklistAttributeMetadata EntityType" /> attributes have within the `$select` filter of this query.  

In order to retrieve the properties of a specific type of attribute you must cast the `Attributes` collection-valued navigation property to the type you want. The following query will return only the <xref href="Microsoft.Dynamics.CRM.PicklistAttributeMetadata?text=PicklistAttributeMetadata EntityType" /> attributes and will include the `LogicalName` as well as expanding the `OptionSet` and `GlobalOptionSet` collection-valued navigation properties  

```http
GET [Organization URI]/api/data/v9.0/EntityDefinitions(LogicalName='account')/Attributes/Microsoft.Dynamics.CRM.PicklistAttributeMetadata?$select=LogicalName&$expand=OptionSet,GlobalOptionSet  
```

> [!NOTE]
> Despite the fact that the `OptionSet` and `GlobalOptionSet` collection-valued navigation properties are defined within <xref href="Microsoft.Dynamics.CRM.EnumAttributeMetadata?text=EnumAttributeMetadata EntityType" />, you cannot cast the attributes to this type. This means that if you want to filter on other types which also inherit these properties (see [Entity types that inherit from EnumAttributeMetadata](/dynamics365/customer-engagement/web-api/enumattributemetadata?view=dynamics-ce-odata-9#Derived_Types) ), you must perform separate queries to filter for each type.

Another example of this is accessing the `Precision` property available in <xref href="Microsoft.Dynamics.CRM.MoneyAttributeMetadata?text=MoneyAttributeMetadata EntityType" /> and <xref href="Microsoft.Dynamics.CRM.DecimalAttributeMetadata?text=DecimalAttributeMetadata EntityType" /> attributes. To access this property you must cast the attributes collection either as <xref href="Microsoft.Dynamics.CRM.MoneyAttributeMetadata?text=MoneyAttributeMetadata EntityType" /> or <xref href="Microsoft.Dynamics.CRM.DecimalAttributeMetadata?text=DecimalAttributeMetadata EntityType" />. An example showing casting to `MoneyAttributeMetadata` is shown here.

```http
GET [Organization URI]/api/data/v9.0/EntityDefinitions(LogicalName='account')/Attributes/Microsoft.Dynamics.CRM.MoneyAttributeMetadata?$select=LogicalName,Precision
```

### Filtering by required level

The <xref href="Microsoft.Dynamics.CRM.AttributeMetadata?text=AttributeMetadata EntityType" /> `RequiredLevel` property uses a special <xref href="Microsoft.Dynamics.CRM.AttributeRequiredLevelManagedProperty?text=AttributeRequiredLevelManagedProperty ComplexType" /> where the `Value` property is a <xref href="Microsoft.Dynamics.CRM.AttributeRequiredLevel?text=AttributeRequiredLevel EnumType" />. In this case you must combine patterns found in [Use complex types in $filter operations](query-metadata-web-api.md#bkmk_complexTypesAsFilters) and [Use enum types in $filter operations](query-metadata-web-api.md#bkmk_filterEnumTypes) to filter by this unique property. The following query will filter those attributes in the account entity that are ApplicationRequired.

```http
GET [Organization URI]/api/data/v9.0/EntityDefinitions(LogicalName='account')/Attributes?$select=SchemaName&$filter=RequiredLevel/Value eq Microsoft.Dynamics.CRM.AttributeRequiredLevel'ApplicationRequired'  
```

<a name="bkmk_retrieveAttributes"></a>

## Retrieving attributes

When you know the MetadataId for both the EntityMetadata and the AttributeMetadata, you can retrieve an individual attribute and access the property values using a query like the following. This query retrieves the LogicalName property of the attribute as well as expanding the OptionSet collection-valued navigation property. Note that you must cast the attribute as a Microsoft.Dynamics.CRM.PicklistAttributeMetadata to access the OptionSet collection-valued navigation property.  

 **Request**
 ```http
GET [Organization URI]/api/data/v9.0/EntityDefinitions(LogicalName='account')/Attributes(5967e7cc-afbb-4c10-bf7e-e7ef430c52be)/Microsoft.Dynamics.CRM.PicklistAttributeMetadata?$select=LogicalName&$expand=OptionSet HTTP/1.1  
Accept: application/json  
Content-Type: application/json; charset=utf-8  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
```

 **Response**
 ```http
HTTP/1.1 200 OK  
Content-Type: application/json; odata.metadata=minimal  
OData-Version: 4.0

{
 "@odata.context": "[Organization URI]/api/data/v9.0/$metadata#EntityDefinitions(70816501-edb9-4740-a16c-6a5efbc05d84)/Attributes/Microsoft.Dynamics.CRM.PicklistAttributeMetadata(LogicalName,OptionSet)/$entity",  
 "LogicalName": "preferredappointmentdaycode",  
 "MetadataId": "5967e7cc-afbb-4c10-bf7e-e7ef430c52be",  
 "OptionSet@odata.context": "[Organization URI]/api/data/v9.0/$metadata#EntityDefinitions(70816501-edb9-4740-a16c-6a5efbc05d84)/Attributes(5967e7cc-afbb-4c10-bf7e-e7ef430c52be)/Microsoft.Dynamics.CRM.PicklistAttributeMetadata/OptionSet/$entity",  
 "OptionSet": {  
  "Options": [  
   {  
    "Value": 0,  
    "Label": {  
     "LocalizedLabels": [  
      {  
       "Label": "Sunday",  
       "LanguageCode": 1033,  
       "IsManaged": true,  
       "MetadataId": "21d6a218-2341-db11-898a-0007e9e17ebd",  
       "HasChanged": null  
      }  
     ],  
     "UserLocalizedLabel": {  
      "Label": "Sunday",  
      "LanguageCode": 1033,  
      "IsManaged": true,  
      "MetadataId": "21d6a218-2341-db11-898a-0007e9e17ebd",  
      "HasChanged": null  
     }  
    },  
    "Description": {  
     "LocalizedLabels": [],  
     "UserLocalizedLabel": null  
    },  
    "Color": null,  
    "IsManaged": true,  
    "MetadataId": null,  
    "HasChanged": null  
   }  
Additional options removed for brevity  
  ],  
  "Description": {  
   "LocalizedLabels": [  
    {  
     "Label": "Day of the week that the account prefers for scheduling service activities.",  
     "LanguageCode": 1033,  
     "IsManaged": true,  
     "MetadataId": "1b67144d-ece0-4e83-a38b-b4d48e3f35d5",  
     "HasChanged": null  
    }  
   ],  
   "UserLocalizedLabel": {  
    "Label": "Day of the week that the account prefers for scheduling service activities.",  
    "LanguageCode": 1033,  
    "IsManaged": true,  
    "MetadataId": "1b67144d-ece0-4e83-a38b-b4d48e3f35d5",  
    "HasChanged": null  
   }  
  },  
  "DisplayName": {  
   "LocalizedLabels": [  
    {  
     "Label": "Preferred Day",  
     "LanguageCode": 1033,  
     "IsManaged": true,  
     "MetadataId": "ebb7e979-f9e3-40cd-a86d-50b479b1c5a4",  
     "HasChanged": null  
    }  
   ],  
   "UserLocalizedLabel": {  
    "Label": "Preferred Day",  
    "LanguageCode": 1033,  
    "IsManaged": true,  
    "MetadataId": "ebb7e979-f9e3-40cd-a86d-50b479b1c5a4",  
    "HasChanged": null  
   }  
  },  
  "IsCustomOptionSet": false,  
  "IsGlobal": false,  
  "IsManaged": true,  
  "IsCustomizable": {  
   "Value": true,  
   "CanBeChanged": false,  
   "ManagedPropertyLogicalName": "iscustomizable"  
  },  
  "Name": "account_preferredappointmentdaycode",  
  "OptionSetType": "Picklist",  
  "IntroducedVersion": null,  
  "MetadataId": "53f9933c-18a0-40a6-b4a5-b9610a101735",  
  "HasChanged": null  
 }  
}  
```

If you don’t require any properties of the attribute and only want the values of a collection-valued navigation property such as OptionsSet, you can include that in the URL and limit the properties with a `$select` system query option for a somewhat more efficient query. In the following example only the Options property of the OptionSet are included.  

 **Request**
 ```http
GET [Organization URI]/api/data/v9.0/EntityDefinitions(LogicalName='account')/Attributes(5967e7cc-afbb-4c10-bf7e-e7ef430c52be)/Microsoft.Dynamics.CRM.PicklistAttributeMetadata/OptionSet?$select=Options HTTP/1.1  
Accept: application/json  
Content-Type: application/json; charset=utf-8  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
```

 **Response**
 ```http
HTTP/1.1 200 OK  
Content-Type: application/json; odata.metadata=minimal  
OData-Version: 4.0  

{  
 "@odata.context": "[Organization URI]/api/data/v9.0/$metadata#EntityDefinitions('account')/Attributes(5967e7cc-afbb-4c10-bf7e-e7ef430c52be)/Microsoft.Dynamics.CRM.PicklistAttributeMetadata/OptionSet(Options)/$entity",  
 "Options": [{  
   "Value": 0,  
   "Label": {  
    "LocalizedLabels": [{  
     "Label": "Sunday",  
     "LanguageCode": 1033,  
     "IsManaged": true,  
     "MetadataId": "21d6a218-2341-db11-898a-0007e9e17ebd",  
     "HasChanged": null  
    }],  
    "UserLocalizedLabel": {  
     "Label": "Sunday",  
     "LanguageCode": 1033,  
     "IsManaged": true,  
     "MetadataId": "21d6a218-2341-db11-898a-0007e9e17ebd",  
     "HasChanged": null  
    }  
   },  
   "Description": {  
    "LocalizedLabels": [],  
    "UserLocalizedLabel": null  
   },  
   "Color": null,  
   "IsManaged": true,  
   "MetadataId": null,  
   "HasChanged": null  
  }  
Additional options removed for brevity  
 ],  
 "MetadataId": "53f9933c-18a0-40a6-b4a5-b9610a101735"  
}  
```

<a name="bkmk_queryRelationshipMetadata"></a>

## Querying relationship metadata

You can retrieve relationship metadata in the context of a given entity much in the same way that you can query attributes. The `ManyToManyRelationships`, `ManyToOneRelationships`, and `OneToManyRelationships` collection-valued navigation properties can be queried just like the `Attributes` collection-valued navigation property. More information:  [Querying EntityMetadata Attributes](query-metadata-web-api.md#bkmk_queryAttributes)  

However, entity relationships can also be queried using the `RelationshipDefinitions` entity set. You can use a query like the following to get the `SchemaName` property for every relationship.

```http
GET [Organization URI]/api/data/v9.0/RelationshipDefinitions?$select=SchemaName  
```

The properties available when querying this entity set are limited to those in the <xref href="Microsoft.Dynamics.CRM.RelationshipMetadataBase?text=RelationshipMetadataBase EntityType" />. To access properties from the entity types that inherit from `RelationshipMetadataBase` you need to include a cast in the query like the following one to return only <xref href="Microsoft.Dynamics.CRM.OneToManyRelationshipMetadata?text=OneToManyRelationshipMetadata EntityType" />.  

```http
GET [Organization URI]/api/data/v9.0/RelationshipDefinitions/Microsoft.Dynamics.CRM.OneToManyRelationshipMetadata?$select=SchemaName  
```

Because the entities returned are typed as `OneToManyRelationshipMetadata`, you can filter on the properties such as `ReferencedEntity` to construct a query to return only the one-to-many entity relationships for a specific entity, such as the account entity as shown in the following query:  

```http
GET [Organization URI]/api/data/v9.0/RelationshipDefinitions/Microsoft.Dynamics.CRM.OneToManyRelationshipMetadata?$select=SchemaName&$filter=ReferencedEntity eq 'account' 
```

That query will return essentially the same results as the following query, which is filtered because it is included in the `EntityMetadataOneToManyRelationships` collection-valued navigation property of the account entity. The difference is that for the previous query you don’t need to know the `MetadataId` for the account entity.  

```http
GET [Organization URI]/api/data/v9.0/EntityDefinitions(LogicalName='account')/OneToManyRelationships?$select=SchemaName  
```

<a name="bkmk_GlobalOptionSets"></a>

## Querying Global OptionSets

You can use the `GlobalOptionSetDefinitions` entity set path to retrieve information about global option sets, but this path does not support the use of the `$filter` system query option. So, unless you know the `MetadataId` for a specific global option set, you can only retrieve all of them. You can also access the definition of a global option set from within the `GlobalOptionSet` single-valued navigation property for any attribute that uses it. This is available for all the [EnumAttributeMetadata EntityType Derived Types](/dynamics365/customer-engagement/web-api/enumattributemetadata?view=dynamics-ce-odata-9#Derived_Types). More information:  [Retrieving attributes](query-metadata-web-api.md#bkmk_retrieveAttributes)  

### See also

[Use the Web API with Dataverse metadata](use-web-api-metadata.md)<br />
[Retrieve metadata by name or MetadataId](retrieve-metadata-name-metadataid.md)<br />
[Metadata entites and attributes using the Web API](create-update-entity-definitions-using-web-api.md)<br />
[Metadata entity relationships using the Web API](create-update-entity-relationships-using-web-api.md)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]