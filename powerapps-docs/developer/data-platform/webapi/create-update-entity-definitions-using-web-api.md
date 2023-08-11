---
title: "Create and update table definitions using the Web API"
description: "Learn about creating and updating Dataverse table definitions using the Web API."
ms.date: 06/07/2023
author: NHelgren
ms.author: nhelgren
ms.reviewer: jdaly
search.audienceType: 
  - developer
contributors: 
  - JimDaly
---
# Create and update table definitions using the Web API

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

You can perform all the same operations on table definitions using the Web API that you can with the Organization service. This article focuses on working with table definitions (metadata) using the Web API. To find details about the table definition properties, see [Customize table definitions](../customize-entity-metadata.md) and [EntityMetadata EntityType](xref:Microsoft.Dynamics.CRM.EntityMetadata).

<a name="bkmk_createEntities"></a>

> [!TIP]
> Entities, attributes, and global option sets (also known as tables, columns, and choices) are all solution components. When you create them you can associate them with a solution by using the `MSCRM.SolutionUniqueName` request header and setting the value to the  unique name of the solution it should be part of.

## Create table definitions

To create a table definition, `POST` the JSON representation of the entity definition data to the `EntityDefinitions` entity set path. The entity must include the definition for the primary name attribute. You don't need to set values for all the properties. The items on this list except for Description are required, although setting a description is a recommended best practice. Property values you don't specify are set to default values. To understand the default values, look at the example in the [Update table definitions](#bkmk_updateEntities) section. The example in this article uses the following entity properties.  
  
|EntityMetadata property|Value|  
|---------------------|-----------|  
|`SchemaName`|`new_BankAccount` **Note:**  You should include the customization prefix that matches the solution publisher. Here the default value "new_" is used, but you should choose the prefix that works for your solution.|  
|`DisplayName`|Bank Account|  
|`DisplayCollectionName`|Bank Accounts|  
|`Description`|An entity to store information about customer bank accounts.|  
|`OwnershipType`|`UserOwned` **Note:**  For the values you can set here, see [OwnershipTypes EnumType](xref:Microsoft.Dynamics.CRM.OwnershipTypes).|  
|`IsActivity`|false|  
|`HasActivities`|false|  
|`HasNotes`|false|  
  
 In addition to the properties listed previously, the `EntityMetadataAttributes` property must contain an array that includes one 
 [StringAttributeMetadata EntityType](xref:Microsoft.Dynamics.CRM.StringAttributeMetadata) to represent the primary name attribute for the entity. The attribute `IsPrimaryName` property must be true. The following table describes the properties set in the example.  
  
|Primary Attribute property|Value|  
|--------------------------------|-----------|  
|`SchemaName`|`new_AccountName`|  
|`RequiredLevel`|None <br />**Note:**  For the values you can set here, see [AttributeRequiredLevelManagedProperty ComplexType](xref:Microsoft.Dynamics.CRM.AttributeRequiredLevelManagedProperty) and [AttributeRequiredLevel EnumType](xref:Microsoft.Dynamics.CRM.AttributeRequiredLevel).|  
|`MaxLength`|100|  
|`FormatName`|`Text` <br />**Note:**  The primary name attribute must use Text format. For format options available for other string attributes, see [String formats](../entity-attribute-metadata.md#string-formats).|  
|`DisplayName`|Account Name|  
|`Description`|Type the name of the bank account.|  
|`IsPrimaryName`|true|  
  
> [!NOTE]
>  When you create or update labels using the [Label ComplexType](xref:Microsoft.Dynamics.CRM.Label), you only need to set the `LocalizedLabels` property. The `UserLocalizedLabel` value returned is based on the user's language preference and is read-only.  
  
The following example shows the creation of a custom table with the properties set. The language is English using the locale ID (LCID) of 1033. [!INCLUDE [lcid](../../../includes/lcid.md)]  
  
 **Request:**

```http 
POST [Organization URI]/api/data/v9.2/EntityDefinitions HTTP/1.1
MSCRM.SolutionUniqueName: examplesolution
Accept: application/json  
Content-Type: application/json; charset=utf-8  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
  
{  
  "@odata.type": "Microsoft.Dynamics.CRM.EntityMetadata",  
 "Attributes": [  
  {  
   "AttributeType": "String",  
   "AttributeTypeName": {  
    "Value": "StringType"  
   },  
   "Description": {  
     "@odata.type": "Microsoft.Dynamics.CRM.Label",  
    "LocalizedLabels": [  
     {  
       "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",  
      "Label": "Type the name of the bank account",  
      "LanguageCode": 1033  
     }  
    ]  
   },  
   "DisplayName": {  
     "@odata.type": "Microsoft.Dynamics.CRM.Label",  
    "LocalizedLabels": [  
     {  
       "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",  
      "Label": "Account Name",  
      "LanguageCode": 1033  
     }  
    ]  
   },  
   "IsPrimaryName": true,  
   "RequiredLevel": {  
    "Value": "None",  
    "CanBeChanged": true,  
    "ManagedPropertyLogicalName": "canmodifyrequirementlevelsettings"  
   },  
   "SchemaName": "new_AccountName",  
    "@odata.type": "Microsoft.Dynamics.CRM.StringAttributeMetadata",  
   "FormatName": {  
    "Value": "Text"  
   },  
   "MaxLength": 100  
  }  
 ],  
 "Description": {  
   "@odata.type": "Microsoft.Dynamics.CRM.Label",  
  "LocalizedLabels": [  
   {  
     "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",  
    "Label": "An entity to store information about customer bank accounts",  
    "LanguageCode": 1033  
   }  
  ]  
 },  
 "DisplayCollectionName": {  
   "@odata.type": "Microsoft.Dynamics.CRM.Label",  
  "LocalizedLabels": [  
   {  
     "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",  
    "Label": "Bank Accounts",  
    "LanguageCode": 1033  
   }  
  ]  
 },  
 "DisplayName": {  
   "@odata.type": "Microsoft.Dynamics.CRM.Label",  
  "LocalizedLabels": [  
   {  
     "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",  
    "Label": "Bank Account",  
    "LanguageCode": 1033  
   }  
  ]  
 },  
 "HasActivities": false,  
 "HasNotes": false,  
 "IsActivity": false,  
 "OwnershipType": "UserOwned",  
 "SchemaName": "new_BankAccount"  
}  
```  
  
 **Response:**

```http 
HTTP/1.1 204 No Content  
OData-Version: 4.0  
OData-EntityId: [Organization URI]/api/data/v9.2/EntityDefinitions(417129e1-207c-e511-80d2-00155d2a68d2)  
```  
  
<a name="bkmk_updateEntities"></a>
 
## Update table definitions
  
> [!IMPORTANT]
>  You can't use the `PATCH` method to update data model entities. The table definitions have parity with the Organization service 
>  [UpdateEntityRequest Class](xref:Microsoft.Xrm.Sdk.Messages.UpdateEntityRequest) that replaces the entity definition with the one included.
>  Therefore, you must use the `PUT` method when updating data model entities and be careful to include all the existing properties that you don't intend to change.
>  You can't update individual properties.  
  
 When you update table definitions with labels, you should include a custom `MSCRM.MergeLabels` request header to control how any labels in the update should be handled. If a label for an item already has labels for other languages and you update it with a label that contains only one label for a specific language, the `MSCRM.MergeLabels` header controls whether to overwrite the existing labels or merge your new label with any existing language labels. With `MSCRM.MergeLabels` set to `true`, any new labels defined will only overwrite existing labels when the language code matches. If you want to overwrite the existing labels to include only the labels you include, set `MSCRM.MergeLabels` to `false`.  
  
> [!IMPORTANT]
>  If you don't include a `MSCRM.MergeLabels` header, the default behavior is as if the value were `false` and any localized labels not included in your update will be lost.  
  
When you update a table or column definition, you must use the  [PublishXml Action](xref:Microsoft.Dynamics.CRM.PublishXml) or 
[PublishAllXml Action](xref:Microsoft.Dynamics.CRM.PublishAllXml) before the changes you make are applied to the application. More information: [Publish customizations](../../model-driven-apps/publish-customizations.md)  
  
Typically, you'll retrieve the JSON definition of the entity attribute and modify the properties before you send it back. The following example contains all the definition properties of the table created in the [Create table definitions](#bkmk_createEntities) example, but with the `DisplayName` changed to "Bank Business Name." It may be useful to note that the JSON here provides the default values for properties not set in the [Create table definitions](#bkmk_createEntities) example.  

> [!NOTE]
> Some of the examples below use the `MetadataId` primary key value. But you can also use the `LogicalName` alternate key to reference schema entities. More information: [Retrieve table definitions by name or MetadataId](retrieve-metadata-name-metadataid.md)
  
 **Request:**

```http 
PUT [Organization URI]/api/data/v9.2/EntityDefinitions(417129e1-207c-e511-80d2-00155d2a68d2) HTTP/1.1
MSCRM.SolutionUniqueName: examplesolution
Accept: application/json  
Content-Type: application/json; charset=utf-8  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
MSCRM.MergeLabels: true  
  
{  
 "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#EntityDefinitions/$entity",  
 "ActivityTypeMask": 0,  
 "AutoRouteToOwnerQueue": false,  
 "CanTriggerWorkflow": true,  
 "Description": {  
  "LocalizedLabels": [  
   {  
    "Label": "An entity to store information about customer bank accounts",  
    "LanguageCode": 1033,  
    "IsManaged": false,  
    "MetadataId": "edc3abd7-c5ae-4822-a3ed-51734fdd0469",  
    "HasChanged": null  
   }  
  ]  
 },  
 "DisplayCollectionName": {  
  "LocalizedLabels": [  
   {  
    "Label": "Bank Accounts",  
    "LanguageCode": 1033,  
    "IsManaged": false,  
    "MetadataId": "7c758e0c-e9cf-4947-93b0-50ec30b20f60",  
    "HasChanged": null  
   }  
  ]  
 },  
 "DisplayName": {  
  "@odata.type": "Microsoft.Dynamics.CRM.Label",  
  "LocalizedLabels": [  
   {  
    "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",  
    "Label": "Bank Business Name",  
    "LanguageCode": 1033  
   }  
  ]  
 },  
 "EntityHelpUrlEnabled": false,  
 "EntityHelpUrl": null,  
 "IsDocumentManagementEnabled": false,  
 "IsOneNoteIntegrationEnabled": false,  
 "IsInteractionCentricEnabled": false,  
 "IsKnowledgeManagementEnabled": false,  
 "AutoCreateAccessTeams": false,  
 "IsActivity": false,  
 "IsActivityParty": false,  
 "IsAuditEnabled": {  
  "Value": false,  
  "CanBeChanged": true,  
  "ManagedPropertyLogicalName": "canmodifyauditsettings"  
 },  
 "IsAvailableOffline": false,  
 "IsChildEntity": false,  
 "IsAIRUpdated": false,  
 "IsValidForQueue": {  
  "Value": false,  
  "CanBeChanged": true,  
  "ManagedPropertyLogicalName": "canmodifyqueuesettings"  
 },  
 "IsConnectionsEnabled": {  
  "Value": false,  
  "CanBeChanged": true,  
  "ManagedPropertyLogicalName": "canmodifyconnectionsettings"  
 },  
 "IconLargeName": null,  
 "IconMediumName": null,  
 "IconSmallName": null,  
 "IsCustomEntity": true,  
 "IsBusinessProcessEnabled": false,  
 "IsCustomizable": {  
  "Value": true,  
  "CanBeChanged": true,  
  "ManagedPropertyLogicalName": "iscustomizable"  
 },  
 "IsRenameable": {  
  "Value": true,  
  "CanBeChanged": true,  
  "ManagedPropertyLogicalName": "isrenameable"  
 },  
 "IsMappable": {  
  "Value": true,  
  "CanBeChanged": false,  
  "ManagedPropertyLogicalName": "ismappable"  
 },  
 "IsDuplicateDetectionEnabled": {  
  "Value": false,  
  "CanBeChanged": true,  
  "ManagedPropertyLogicalName": "canmodifyduplicatedetectionsettings"  
 },  
 "CanCreateAttributes": {  
  "Value": true,  
  "CanBeChanged": false,  
  "ManagedPropertyLogicalName": "cancreateattributes"  
 },  
 "CanCreateForms": {  
  "Value": true,  
  "CanBeChanged": true,  
  "ManagedPropertyLogicalName": "cancreateforms"  
 },  
 "CanCreateViews": {  
  "Value": true,  
  "CanBeChanged": true,  
  "ManagedPropertyLogicalName": "cancreateviews"  
 },  
 "CanCreateCharts": {  
  "Value": true,  
  "CanBeChanged": true,  
  "ManagedPropertyLogicalName": "cancreatecharts"  
 },  
 "CanBeRelatedEntityInRelationship": {  
  "Value": true,  
  "CanBeChanged": true,  
  "ManagedPropertyLogicalName": "canberelatedentityinrelationship"  
 },  
 "CanBePrimaryEntityInRelationship": {  
  "Value": true,  
  "CanBeChanged": true,  
  "ManagedPropertyLogicalName": "canbeprimaryentityinrelationship"  
 },  
 "CanBeInManyToMany": {  
  "Value": true,  
  "CanBeChanged": true,  
  "ManagedPropertyLogicalName": "canbeinmanytomany"  
 },  
 "CanEnableSyncToExternalSearchIndex": {  
  "Value": true,  
  "CanBeChanged": true,  
  "ManagedPropertyLogicalName": "canenablesynctoexternalsearchindex"  
 },  
 "SyncToExternalSearchIndex": false,  
 "CanModifyAdditionalSettings": {  
  "Value": true,  
  "CanBeChanged": true,  
  "ManagedPropertyLogicalName": "canmodifyadditionalsettings"  
 },  
 "CanChangeHierarchicalRelationship": {  
  "Value": true,  
  "CanBeChanged": true,  
  "ManagedPropertyLogicalName": "canchangehierarchicalrelationship"  
 },  
 "IsOptimisticConcurrencyEnabled": true,  
 "ChangeTrackingEnabled": false,  
 "IsImportable": true,  
 "IsIntersect": false,  
 "IsMailMergeEnabled": {  
  "Value": true,  
  "CanBeChanged": true,  
  "ManagedPropertyLogicalName": "canmodifymailmergesettings"  
 },  
 "IsManaged": false,  
 "IsEnabledForCharts": true,  
 "IsEnabledForTrace": false,  
 "IsValidForAdvancedFind": true,  
 "IsVisibleInMobile": {  
  "Value": false,  
  "CanBeChanged": true,  
  "ManagedPropertyLogicalName": "canmodifymobilevisibility"  
 },  
 "IsVisibleInMobileClient": {  
  "Value": false,  
  "CanBeChanged": true,  
  "ManagedPropertyLogicalName": "canmodifymobileclientvisibility"  
 },  
 "IsReadOnlyInMobileClient": {  
  "Value": false,  
  "CanBeChanged": true,  
  "ManagedPropertyLogicalName": "canmodifymobileclientreadonly"  
 },  
 "IsOfflineInMobileClient": {  
  "Value": false,  
  "CanBeChanged": true,  
  "ManagedPropertyLogicalName": "canmodifymobileclientoffline"  
 },  
 "DaysSinceRecordLastModified": 0,  
 "IsReadingPaneEnabled": true,  
 "IsQuickCreateEnabled": false,  
 "LogicalName": "new_bankaccount",  
 "ObjectTypeCode": 10009,  
 "OwnershipType": "UserOwned",  
 "PrimaryNameAttribute": "new_accountname",  
 "PrimaryImageAttribute": null,  
 "PrimaryIdAttribute": "new_bankaccountid",  
 "Privileges": [  
  {  
   "CanBeBasic": true,  
   "CanBeDeep": true,  
   "CanBeGlobal": true,  
   "CanBeLocal": true,  
   "CanBeEntityReference": false,  
   "CanBeParentEntityReference": false,  
   "Name": "prvCreatenew_BankAccount",  
   "PrivilegeId": "d1a8de4b-27df-42e1-bc5c-b863e002b37f",  
   "PrivilegeType": "Create"  
  },  
  {  
   "CanBeBasic": true,  
   "CanBeDeep": true,  
   "CanBeGlobal": true,  
   "CanBeLocal": true,  
   "CanBeEntityReference": false,  
   "CanBeParentEntityReference": false,  
   "Name": "prvReadnew_BankAccount",  
   "PrivilegeId": "726043b1-de2c-487e-9d6d-5629fca2bf22",  
   "PrivilegeType": "Read"  
  },  
  {  
   "CanBeBasic": true,  
   "CanBeDeep": true,  
   "CanBeGlobal": true,  
   "CanBeLocal": true,  
   "CanBeEntityReference": false,  
   "CanBeParentEntityReference": false,  
   "Name": "prvWritenew_BankAccount",  
   "PrivilegeId": "fa50c539-b6c7-4eaf-bd49-fd8224bc51b6",  
   "PrivilegeType": "Write"  
  },  
  {  
   "CanBeBasic": true,  
   "CanBeDeep": true,  
   "CanBeGlobal": true,  
   "CanBeLocal": true,  
   "CanBeEntityReference": false,  
   "CanBeParentEntityReference": false,  
   "Name": "prvDeletenew_BankAccount",  
   "PrivilegeId": "17c1fd6e-f856-45e7-b563-796f53108b85",  
   "PrivilegeType": "Delete"  
  },  
  {  
   "CanBeBasic": true,  
   "CanBeDeep": true,  
   "CanBeGlobal": true,  
   "CanBeLocal": true,  
   "CanBeEntityReference": false,  
   "CanBeParentEntityReference": false,  
   "Name": "prvAssignnew_BankAccount",  
   "PrivilegeId": "133ca81d-668e-4c19-a71e-10c6dfe099cd",  
   "PrivilegeType": "Assign"  
  },  
  {  
   "CanBeBasic": true,  
   "CanBeDeep": true,  
   "CanBeGlobal": true,  
   "CanBeLocal": true,  
   "CanBeEntityReference": false,  
   "CanBeParentEntityReference": false,  
   "Name": "prvSharenew_BankAccount",  
   "PrivilegeId": "15f27df4-9c67-47c9-b1f1-274e1c44f24a",  
   "PrivilegeType": "Share"  
  },  
  {  
   "CanBeBasic": true,  
   "CanBeDeep": true,  
   "CanBeGlobal": true,  
   "CanBeLocal": true,  
   "CanBeEntityReference": false,  
   "CanBeParentEntityReference": false,  
   "Name": "prvAppendnew_BankAccount",  
   "PrivilegeId": "ac8b1920-8f93-4e9d-94e3-c680e2a2f228",  
   "PrivilegeType": "Append"  
  },  
  {  
   "CanBeBasic": true,  
   "CanBeDeep": true,  
   "CanBeGlobal": true,  
   "CanBeLocal": true,  
   "CanBeEntityReference": false,  
   "CanBeParentEntityReference": false,  
   "Name": "prvAppendTonew_BankAccount",  
   "PrivilegeId": "f63a5f46-3bc7-4eac-81d0-7f77f566ef46",  
   "PrivilegeType": "AppendTo"  
  }  
 ],  
 "RecurrenceBaseEntityLogicalName": null,  
 "ReportViewName": "Filterednew_BankAccount",  
 "SchemaName": "new_BankAccount",  
 "IntroducedVersion": "1.0",  
 "IsStateModelAware": true,  
 "EnforceStateTransitions": false,  
 "EntityColor": null,  
 "LogicalCollectionName": "new_bankaccounts",  
 "CollectionSchemaName": "new_BankAccounts",  
 "EntitySetName": "new_bankaccounts",  
 "IsEnabledForExternalChannels": false,  
 "IsPrivate": false,  
 "MetadataId": "417129e1-207c-e511-80d2-00155d2a68d2",  
 "HasChanged": null  
}  
```  
  
 **Response:**

```http
HTTP/1.1 204 No Content  
OData-Version: 4.0  
```

### See also

[Use the Web API with Microsoft Dataverse metadata](use-web-api-metadata.md)  
[Create and update column definitions using the Web API](create-update-column-definitions-using-web-api.md)  
[Query table definitions using the Web API](query-metadata-web-api.md)  
[Retrieve table definitions by name or MetadataId](retrieve-metadata-name-metadataid.md)  
[Model table relationships using the Web API](create-update-entity-relationships-using-web-api.md)  
[Work with table definitions using the Organization service](../org-service/work-with-metadata.md)  
[Column (attribute) definitions](../entity-attribute-metadata.md)  
[Web API Metadata Operations Sample](web-api-metadata-operations-sample.md)  
[Web API Metadata Operations Sample (C#)](samples/webapiservice-metadata-operations.md)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
