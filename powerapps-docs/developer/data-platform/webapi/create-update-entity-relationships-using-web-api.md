---
title: "Create and update table relationships using the Web API (Microsoft Dataverse) | Microsoft Docs"
description: "Learn about creating and updating table relationships using the Web API"
ms.custom: ""
ms.date: 04/22/2021
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
ms.assetid: 923538e2-15fe-4718-8eae-d939c5d200cd
caps.latest.revision: 15
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

# Create and update table relationships using the Web API

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

The Web API supports working with relationship definitions (metadata). The concepts described in [Table relationship definitions](../entity-relationship-metadata.md) also apply to the Web API.  

<a name="bkmk_RelationshipEligibility"></a>

## Eligibility for relationships

Before you create a table (entity) relationship you should confirm whether the table is eligible to participate in the relationship. You can use the actions listed in the following table to determine eligibility. These actions correspond to the Organization service messages described in [Table relationship eligibility](../entity-relationship-eligibility.md).  
  
|Action|Description|  
|------------|-----------------|  
|<xref href="Microsoft.Dynamics.CRM.CanBeReferenced?text=CanBeReferenced Action" />|Checks whether the specified entity can be the primary entity (one) in a one-to-many relationship.|  
|<xref href="Microsoft.Dynamics.CRM.CanBeReferencing?text=CanBeReferencing Action" />|Checks whether the specified entity can be the referencing entity (many) in a one-to-many relationship.|  
|<xref href="Microsoft.Dynamics.CRM.CanManyToMany?text=CanManyToMany Action" />|Checks whether the entity can participate in a many-to-many relationship.|  
|<xref href="Microsoft.Dynamics.CRM.GetValidManyToMany?text=GetValidManyToMany Function" />|Returns the set of entities that can participate in a many-to-many relationship.|  
|<xref href="Microsoft.Dynamics.CRM.GetValidReferencedEntities?text=GetValidReferencedEntities Function" />|Returns the set of entities that are valid as the primary entity (one) from the specified entity in a one-to-many relationship.|  
|<xref href="Microsoft.Dynamics.CRM.GetValidReferencingEntities?text=GetValidReferencingEntities Function" />|Returns the set of entities that are valid as the related entity (many) to the specified entity in a one-to-many relationship.|  
  
<a name="bkmk_createOnetoMany"></a>

## Create a one-to-many relationship

When you create a one-to-many relationship, you define it by using the <xref href="Microsoft.Dynamics.CRM.OneToManyRelationshipMetadata?text=OneToManyRelationshipMetadata EntityType" />. This definition includes the lookup attribute, which is defined by using <xref href="Microsoft.Dynamics.CRM.LookupAttributeMetadata?text=LookupAttributeMetadata EntityType" /> and also requires complex properties using <xref href="Microsoft.Dynamics.CRM.AssociatedMenuConfiguration?text=AssociatedMenuConfiguration ComplexType" />, <xref href="Microsoft.Dynamics.CRM.CascadeConfiguration?text=CascadeConfiguration ComplexType" />, <xref href="Microsoft.Dynamics.CRM.Label?text=Label ComplexType" /> and <xref href="Microsoft.Dynamics.CRM.LocalizedLabel?text=LocalizedLabel ComplexType" />. The lookup attribute is set to the Lookup single-valued navigation property of the `OneToManyRelationshipMetadata` object and gets created at the same time using *deep insert*. More information: [Create related tables in one operation](create-entity-web-api.md#bkmk_CreateRelated) and [Table relationship metadata](../entity-relationship-metadata.md)
  
If you want to apply a custom navigation property name for a one-to-many relationship you can set values for the `ReferencingEntityNavigationPropertyName` and `ReferencedEntityNavigationPropertyName` properties.  
  
Once you have generated the necessary JSON to define the relationship and the lookup attribute, `POST` the JSON to the `RelationshipDefinitions` entity set. You must include the `@odata.type` property value of `Microsoft.Dynamics.CRM.OneToManyRelationshipMetadata` to clarify the type of relationship you’re creating because this same entity set is used to create many-to-many relationships. The uri for the resulting relationship is returned in the response.  
  
 **Request**  
```http 
POST [Organization URI]/api/data/v9.0/RelationshipDefinitions HTTP/1.1  
Accept: application/json  
Content-Type: application/json; charset=utf-8  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
  
{  
 "SchemaName": "new_contact_new_bankaccount",  
 "@odata.type": "Microsoft.Dynamics.CRM.OneToManyRelationshipMetadata",  
 "AssociatedMenuConfiguration": {  
  "Behavior": "UseCollectionName",  
  "Group": "Details",  
  "Label": {  
   "@odata.type": "Microsoft.Dynamics.CRM.Label",  
   "LocalizedLabels": [  
    {  
     "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",  
     "Label": "Bank Accounts",  
     "LanguageCode": 1033  
    }  
   ],  
   "UserLocalizedLabel": {  
    "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",  
    "Label": "Bank Accounts",  
    "LanguageCode": 1033  
   }  
  },  
  "Order": 10000  
 },  
 "CascadeConfiguration": {  
  "Assign": "Cascade",  
  "Delete": "Cascade",  
  "Merge": "Cascade",  
  "Reparent": "Cascade",  
  "Share": "Cascade",  
  "Unshare": "Cascade"  
 },  
 "ReferencedAttribute": "contactid",  
 "ReferencedEntity": "contact",  
 "ReferencingEntity": "new_bankaccount",  
 "Lookup": {  
  "AttributeType": "Lookup",  
  "AttributeTypeName": {  
   "Value": "LookupType"  
  },  
  "Description": {  
   "@odata.type": "Microsoft.Dynamics.CRM.Label",  
   "LocalizedLabels": [  
    {  
     "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",  
     "Label": "The owner of the account",  
     "LanguageCode": 1033  
    }  
   ],  
   "UserLocalizedLabel": {  
    "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",  
    "Label": "The owner of the account",  
    "LanguageCode": 1033  
   }  
  },  
  "DisplayName": {  
   "@odata.type": "Microsoft.Dynamics.CRM.Label",  
   "LocalizedLabels": [  
    {  
     "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",  
     "Label": "Account Owner",  
     "LanguageCode": 1033  
    }  
   ],  
   "UserLocalizedLabel": {  
    "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",  
    "Label": "Account Owner",  
    "LanguageCode": 1033  
   }  
  },  
  "RequiredLevel": {  
   "Value": "ApplicationRequired",  
   "CanBeChanged": true,  
   "ManagedPropertyLogicalName": "canmodifyrequirementlevelsettings"  
  },  
  "SchemaName": "new_AccountOwner",  
  "@odata.type": "Microsoft.Dynamics.CRM.LookupAttributeMetadata"  
 }  
}  
```  
  
 **Response**  
```http 
HTTP/1.1 204 No Content  
OData-Version: 4.0  
OData-EntityId: [Organization URI]/api/data/v9.0/RelationshipDefinitions(d475020f-5d7c-e511-80d2-00155d2a68d2)  
```  
  
<a name="bkmk_CreateManyToMany"></a>
  
## Create a many-to-many relationship

<!-- TODO:
When you create a many-to-many relationship, you must the relationship by using the <xref href="Microsoft.Dynamics.CRM.ManyToManyRelationshipMetadata?text=ManyToManyRelationshipMetadata EntityType" />. This definition includes the name of the intersect entity to be created as well as how the relationship should be displayed in the application by using <xref href="Microsoft.Dynamics.CRM.AssociatedMenuConfiguration?text=AssociatedMenuConfiguration ComplexType" />, <xref href="Microsoft.Dynamics.CRM.Label?text=Label ComplexType" /> and <xref href="Microsoft.Dynamics.CRM.LocalizedLabel?text=LocalizedLabel ComplexType" />. More information:[Many-to-many relationships](../customize-entity-relationship-metadata.md#BKMK_ManyToManyRelationships)   -->
  
 If you want to apply a custom navigation property name for a many-to-many relationship, you can set values for the `Entity1NavigationPropertyName` and `Entity2NavigationPropertyName` properties.  
  
 Once you have generated the necessary JSON to define the relationship, `POST` the JSON to the `RelationshipDefinitions` entity set. You must include the `@odata.type` property value of `Microsoft.Dynamics.CRM.ManyToManyRelationshipMetadata` to clarify the type of relationship you’re creating because this same entity set is used to create one-to-many relationships. The URI for the resulting relationship is returned in the response.  
  
 **Request**
  
```http 
POST [Organization URI]/api/data/v9.0/RelationshipDefinitions HTTP/1.1  
Accept: application/json  
Content-Type: application/json; charset=utf-8  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
  
{  
 "SchemaName": "new_accounts_campaigns",  
 "@odata.type": "Microsoft.Dynamics.CRM.ManyToManyRelationshipMetadata",  
 "Entity1AssociatedMenuConfiguration": {  
  "Behavior": "UseLabel",  
  "Group": "Details",  
  "Label": {  
   "@odata.type": "Microsoft.Dynamics.CRM.Label",  
   "LocalizedLabels": [  
    {  
     "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",  
     "Label": "Account",  
     "LanguageCode": 1033  
    }  
   ],  
   "UserLocalizedLabel": {  
    "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",  
    "Label": "Account",  
    "LanguageCode": 1033  
   }  
  },  
  "Order": 10000  
 },  
 "Entity1LogicalName": "account",  
 "Entity2AssociatedMenuConfiguration": {  
  "Behavior": "UseLabel",  
  "Group": "Details",  
  "Label": {  
   "@odata.type": "Microsoft.Dynamics.CRM.Label",  
   "LocalizedLabels": [  
    {  
     "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",  
     "Label": "Campaign",  
     "LanguageCode": 1033  
    }  
   ],  
   "UserLocalizedLabel": {  
    "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",  
    "Label": "Campaign",  
    "LanguageCode": 1033  
   }  
  },  
  "Order": 10000  
 },  
 "Entity2LogicalName": "campaign",  
 "IntersectEntityName": "new_accounts_campaigns"  
}  
```  
  
 **Response**  
```http 
HTTP/1.1 204 No Content  
OData-Version: 4.0  
OData-EntityId: [Organization URI]/api/data/v9.0/RelationshipDefinitions(420245fa-c77c-e511-80d2-00155d2a68d2)    
```  
  
<a name="bkmk_updateRelationships"></a>

## Update relationships

As discussed in [Update table definitions](create-update-entity-definitions-using-web-api.md#bkmk_updateEntities), you update relationships using the HTTP PUT method to replace the existing definition with changes you want to apply. You can’t edit individual properties using the HTTP PATCH method as you can with business data tables. Just like with entities and attributes, you should include a `MSCRM.MergeLabels` header with the value set to `true` to avoid overwriting localized labels not included in your update and you must publish customizations before they are active in the system.  
  
<a name="bkmk_deleteRelationship"></a>
 
## Delete relationships

To delete a relationship using the Web API, use the HTTP DELETE method with the URI for the relationship.  
  
### See also

<!-- TODO:
[Customize entity relationship metadata](../customize-entity-relationship-metadata.md)<br /> -->
[Use the Web API with table definitions](use-web-api-metadata.md)<br />
[Query table definitions using the Web API](query-metadata-web-api.md)<br />
[Retrieve table definitions by name or MetadataId](retrieve-metadata-name-metadataid.md)<br />
[Model tables and columns using the Web API](create-update-entity-definitions-using-web-api.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]