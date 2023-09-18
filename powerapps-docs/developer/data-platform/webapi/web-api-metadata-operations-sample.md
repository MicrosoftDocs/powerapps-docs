---
title: "Web API Metadata Operations Sample (Microsoft Dataverse)| Microsoft Docs"
description: "This collection of code samples demonstrates how to perform operations that change the Dataverse data structures."
ms.date: 09/02/2022
author: NHelgren
ms.author: nhelgren
ms.reviewer: jdaly
search.audienceType: 
  - developer
contributors: 
  - JimDaly
---

# Web API Metadata Operations Sample

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

This collection of http requests and responses demonstrate how to perform selected operations that modify the Dataverse schema, or metadata, using the [Web API Metadata Operations Sample (C#)](samples/webapiservice-metadata-operations.md)
  
This article describes a common set of operations implemented by each sample in this group. This article describes the HTTP requests and responses and text output that each sample performs without the language specific details. See the language specific descriptions and the individual samples for details about how these operations are performed.  
  
<a name="bkmk_demonstrates"></a>  

## Demonstrates  

This sample is divided into the following sections, containing Dataverse Web API operations that are discussed in greater detail in the specified associated conceptual articles.  
  
|Code section|Associated conceptual and reference articles|  
|------------------|----------------------------------|  
|[Section 0: Create Publisher and Solution](#section-0-create-publisher-and-solution)|[Create a table row](create-entity-web-api.md)<br /><xref:Microsoft.Dynamics.CRM.publisher?text=publisher EntityType><br /><xref:Microsoft.Dynamics.CRM.solution?text=soluion EntityType>|
|[Section 1: Create, Retrieve and Update Table](#section-1-create-retrieve-and-update-table)|[Create and update table definitions](create-update-entity-definitions-using-web-api.md)<br /><xref:Microsoft.Dynamics.CRM.EntityMetadata?text=EntityMetadata EntityType>|
|[Section 2: Create, Retrieve and Update Columns](#section-2-create-retrieve-and-update-columns)<br />- [Boolean Column](#boolean-column)<br />&nbsp;&nbsp;&nbsp;- [Update Option Values](#update-option-values)<br />- [DateTime Column](#datetime-column)<br />- [Decimal Column](#decimal-column)<br />- [Integer Column](#integer-column)<br />- [Memo Column](#memo-column)<br />- [Money Column](#money-column)<br />- [Picklist Column](#picklist-column)<br />&nbsp;&nbsp;&nbsp;- [Add an option to the local optionset](#add-an-option-to-the-local-optionset)<br />&nbsp;&nbsp;&nbsp;- [Re-order choice column options](#re-order-choice-column-options)<br />&nbsp;&nbsp;&nbsp;- [Delete local option value](#delete-local-option-value)<br />- [Multi-Select Picklist Column](#multi-select-picklist-column)<br />- [Insert Status Value](#insert-status-value)|[Create columns](create-update-column-definitions-using-web-api.md#create-columns)<br />[Retrieving attributes](query-metadata-web-api.md#retrieving-attributes)<br />[InsertOptionValue Action](xref:Microsoft.Dynamics.CRM.InsertOptionValue)<br />[OrderOption Action](xref:Microsoft.Dynamics.CRM.OrderOption)<br />[DeleteOptionValue Action](xref:Microsoft.Dynamics.CRM.DeleteOptionValue)<br />[InsertStatusValue Action](xref:Microsoft.Dynamics.CRM.InsertStatusValue)|
|[Section 3: Create and use Global OptionSet](#section-3-create-and-use-global-optionset)|[Create and update choices (option sets)](create-update-optionsets.md)|
|[Section 4: Create Customer Relationship](#section-4-create-customer-relationship)|<xref:Microsoft.Dynamics.CRM.CreateCustomerRelationships?text=CreateCustomerRelationships Action>|
|[Section 5: Create and retrieve a one-to-many relationship](#section-5-create-and-retrieve-a-one-to-many-relationship)|[Eligibility for relationships](create-update-entity-relationships-using-web-api.md#eligibility-for-relationships)<br /> [Create a one-to-many relationship](create-update-entity-relationships-using-web-api.md#create-a-one-to-many-relationship)<br />[Querying relationship metadata](query-metadata-web-api.md#querying-relationship-metadata)|
|[Section 6: Create and retrieve a many-to-one relationship](#section-6-create-and-retrieve-a-many-to-one-relationship)|[Create a one-to-many relationship](create-update-entity-relationships-using-web-api.md#create-a-one-to-many-relationship)<br />[Querying relationship metadata](query-metadata-web-api.md#querying-relationship-metadata)|
|[Section 7: Create and retrieve a many-to-many relationship](#section-7-create-and-retrieve-a-many-to-many-relationship)|[Create a many-to-many relationship](create-update-entity-relationships-using-web-api.md#create-a-many-to-many-relationship)<br />[Querying relationship metadata](query-metadata-web-api.md#querying-relationship-metadata)|
|[Section 8: Export managed solution](#section-8-export-managed-solution)|[Export solutions](../../../maker/data-platform/export-solutions.md)|
|[Section 9: Delete sample records](#section-9-delete-sample-records)|[Basic delete](update-delete-entities-using-web-api.md#basic-delete)|
|[Section 10: Import and Delete managed solution](#section-10-import-and-delete-managed-solution)|[Import solutions](../../../maker/data-platform/import-update-export-solutions.md)|
  
> [!NOTE]
>  For brevity, less pertinent HTTP headers have been omitted. The URLs of the records will vary with the base organization address and the IDs set by the Dataverse server.  

## Section 0: Create Publisher and Solution

1. Create the publisher first since the solution must be related to it. All the items created or modified in this sample uses the publisher `customizationprefix` and `customizationoptionvalueprefix` values.

   **Request:**

   ```http
   POST [Organization Uri]/api/data/v9.2/publishers HTTP/1.1
   OData-MaxVersion: 4.0
   OData-Version: 4.0
   If-None-Match: null
   Accept: application/json

   {
   "friendlyname": "Example Publisher",
   "uniquename": "examplepublisher",
   "description": "An example publisher for samples",
   "customizationprefix": "sample",
   "customizationoptionvalueprefix": 72700
   }
   ```

   **Response:**

   ```http
   HTTP/1.1 204 NoContent
   OData-Version: 4.0
   OData-EntityId: [Organization Uri]/api/data/v9.2/publishers(a78ab7fc-102a-ed11-9db1-00224804f8e2)
   ```

   **Console output:**

   ```
   Created publisher Example Publisher
   ```

1. Then create the solution related to the publisher. 

    > [!NOTE]
    > Many of the items created or updated in is sample will use the `uniquename` value of this solution with the `MSCRM.SolutionUniqueName` request header so that the changes are included as part of this solution. Some actions have a `SolutionUniqueName` parameter that does the same thing. At the end of this sample this solution will be exported and contain the definitions of all the items created and changed in this sample.

   **Request:**

   ```http
   POST [Organization Uri]/api/data/v9.2/solutions HTTP/1.1
   OData-MaxVersion: 4.0
   OData-Version: 4.0
   If-None-Match: null
   Accept: application/json

   {
   "friendlyname": "Example Solution",
   "uniquename": "examplesolution",
   "description": "An example solution for samples",
   "version": "1.0.0.0",
   "publisherid@odata.bind": "publishers(a78ab7fc-102a-ed11-9db1-00224804f8e2)"
   }
   ```

   **Response:**

   ```http
   HTTP/1.1 204 NoContent
   OData-Version: 4.0
   OData-EntityId: [Organization Uri]/api/data/v9.2/solutions(5472b902-112a-ed11-9db1-00224804f8e2)
   ```

   **Console output:**

   ```
   Created solution Example Solution
   ```

## Section 1: Create, Retrieve and Update Table

1. Create the `sample_BankAccount` table.

   These properties are required: `SchemaName`, `DisplayName`, `DisplayCollectionName`, `HasNotes`, `HasActivities` and `PrimaryNameAttribute`, which must include the `LogicalName` value of the primary name column.

   The table must also include one <xref:Microsoft.Dynamics.CRM.StringAttributeMetadata?text=StringAttributeMetadata> column in the `Attributes` collection to be the primary name column for the table. That column definition must have `SchemaName`, `MaxLength`, and `DisplayName` values, and `IsPrimaryName` must be set to true.

   > [!NOTE]
   > The `MSCRM.SolutionUniqueName: examplesolution` request header associates this table to the solution.
   > The `SchemaName` value (`sample_BankAccount`) includes the customization prefix from the publisher.

   **Request:**

   ```http
   POST [Organization Uri]/api/data/v9.2/EntityDefinitions HTTP/1.1
   MSCRM.SolutionUniqueName: examplesolution
   OData-MaxVersion: 4.0
   OData-Version: 4.0
   If-None-Match: null
   Accept: application/json

   {
   "@odata.type": "Microsoft.Dynamics.CRM.EntityMetadata",
   "Description": {
      "@odata.type": "Microsoft.Dynamics.CRM.Label",
      "LocalizedLabels": [
         {
         "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
         "Label": "A table to store information about customer bank accounts",
         "LanguageCode": 1033,
         "IsManaged": false
         }
      ],
      "UserLocalizedLabel": {
         "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
         "Label": "A table to store information about customer bank accounts",
         "LanguageCode": 1033,
         "IsManaged": false
      }
   },
   "DisplayCollectionName": {
      "@odata.type": "Microsoft.Dynamics.CRM.Label",
      "LocalizedLabels": [
         {
         "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
         "Label": "Bank Accounts",
         "LanguageCode": 1033,
         "IsManaged": false
         }
      ],
      "UserLocalizedLabel": {
         "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
         "Label": "Bank Accounts",
         "LanguageCode": 1033,
         "IsManaged": false
      }
   },
   "DisplayName": {
      "@odata.type": "Microsoft.Dynamics.CRM.Label",
      "LocalizedLabels": [
         {
         "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
         "Label": "Bank Account",
         "LanguageCode": 1033,
         "IsManaged": false
         }
      ],
      "UserLocalizedLabel": {
         "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
         "Label": "Bank Account",
         "LanguageCode": 1033,
         "IsManaged": false
      }
   },
   "HasActivities": false,
   "HasNotes": false,
   "OwnershipType": "UserOwned",
   "PrimaryNameAttribute": "sample_name",
   "SchemaName": "sample_BankAccount",
   "Attributes": [
      {
         "@odata.type": "Microsoft.Dynamics.CRM.StringAttributeMetadata",
         "AttributeType": "String",
         "AttributeTypeName": {
         "Value": "StringType"
         },
         "MaxLength": 100,
         "Description": {
         "@odata.type": "Microsoft.Dynamics.CRM.Label",
         "LocalizedLabels": [
            {
               "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
               "Label": "The primary attribute for the Bank Account entity.",
               "LanguageCode": 1033,
               "IsManaged": false
            }
         ],
         "UserLocalizedLabel": {
            "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
            "Label": "The primary attribute for the Bank Account entity.",
            "LanguageCode": 1033,
            "IsManaged": false
         }
         },
         "DisplayName": {
         "@odata.type": "Microsoft.Dynamics.CRM.Label",
         "LocalizedLabels": [
            {
               "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
               "Label": "Account Name",
               "LanguageCode": 1033,
               "IsManaged": false
            }
         ],
         "UserLocalizedLabel": {
            "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
            "Label": "Account Name",
            "LanguageCode": 1033,
            "IsManaged": false
         }
         },
         "IsPrimaryName": true,
         "RequiredLevel": {
         "Value": "None",
         "CanBeChanged": false,
         "ManagedPropertyLogicalName": "canmodifyrequirementlevelsettings"
         },
         "SchemaName": "sample_Name"
      }
   ]
   }
   ```

   **Response:**

   ```http
   HTTP/1.1 204 NoContent
   OData-Version: 4.0
   OData-EntityId: [Organization Uri]/api/data/v9.2/EntityDefinitions(5872b902-112a-ed11-9db1-00224804f8e2)
   ```

   **Console output:**

   ```
   Sending request to create the sample_BankAccount table...
   Created sample_BankAccount table.
   ```

1. Retrieve the `sample_BankAccount` table definition.

   - This retrieve operation doesn't include any `$select` to filter the properties returned because this data is modified and sent back to update the table definition using `PUT`, which overwrites the existing value.
   - This query also doesn't include an `$expand` to include related data, such as attributes, because related data must be updated separately.

   > [!NOTE]
   > This request and others in this sample use the `Consistency: Strong` header. Use this header when you retrieve metadata definition changes right after you apply them. Metadata changes are cached for performance reasons and a request for a newly created item may return a 404 because it hasn't been cached yet. Caching may take 30 seconds. This header will force the server to read the latest version including your changes. By using this header, you negate the performance gain that caching provides, so you should only use it when in scenarios like this sample where you are retrieving changes you have just made. More information: [HTTP headers > Other headers](compose-http-requests-handle-errors.md#other-headers).

   **Request:**

   ```http
   GET [Organization Uri]/api/data/v9.2/EntityDefinitions(LogicalName='sample_bankaccount') HTTP/1.1
   Consistency: Strong
   OData-MaxVersion: 4.0
   OData-Version: 4.0
   If-None-Match: null
   Accept: application/json
   ```

   **Response:**

   ```http
   HTTP/1.1 200 OK
   OData-Version: 4.0

   {
   "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#EntityDefinitions/$entity",
   "ActivityTypeMask": 0,
   "AutoRouteToOwnerQueue": false,
   "CanTriggerWorkflow": true,
   "EntityHelpUrlEnabled": false,
   "EntityHelpUrl": null,
   "IsDocumentManagementEnabled": false,
   "IsOneNoteIntegrationEnabled": false,
   "IsInteractionCentricEnabled": false,
   "IsKnowledgeManagementEnabled": false,
   "IsSLAEnabled": false,
   "IsBPFEntity": false,
   "IsDocumentRecommendationsEnabled": false,
   "IsMSTeamsIntegrationEnabled": false,
   "SettingOf": null,
   "DataProviderId": null,
   "DataSourceId": null,
   "AutoCreateAccessTeams": false,
   "IsActivity": false,
   "IsActivityParty": false,
   "IsRetrieveAuditEnabled": false,
   "IsRetrieveMultipleAuditEnabled": false,
   "IsArchivalEnabled": false,
   "IsAvailableOffline": false,
   "IsChildEntity": false,
   "IsAIRUpdated": false,
   "IconLargeName": null,
   "IconMediumName": null,
   "IconSmallName": null,
   "IconVectorName": null,
   "IsCustomEntity": true,
   "IsBusinessProcessEnabled": false,
   "SyncToExternalSearchIndex": false,
   "IsOptimisticConcurrencyEnabled": true,
   "ChangeTrackingEnabled": false,
   "IsImportable": true,
   "IsIntersect": false,
   "IsManaged": false,
   "IsEnabledForCharts": true,
   "IsEnabledForTrace": false,
   "IsValidForAdvancedFind": true,
   "DaysSinceRecordLastModified": 0,
   "MobileOfflineFilters": "",
   "IsReadingPaneEnabled": true,
   "IsQuickCreateEnabled": false,
   "LogicalName": "sample_bankaccount",
   "ObjectTypeCode": 10393,
   "OwnershipType": "UserOwned",
   "PrimaryNameAttribute": "sample_name",
   "PrimaryImageAttribute": null,
   "PrimaryIdAttribute": "sample_bankaccountid",
   "RecurrenceBaseEntityLogicalName": null,
   "ReportViewName": "Filteredsample_BankAccount",
   "SchemaName": "sample_BankAccount",
   "IntroducedVersion": "1.0.0.0",
   "IsStateModelAware": true,
   "EnforceStateTransitions": false,
   "ExternalName": null,
   "EntityColor": null,
   "LogicalCollectionName": "sample_bankaccounts",
   "ExternalCollectionName": null,
   "CollectionSchemaName": "sample_BankAccounts",
   "EntitySetName": "sample_bankaccounts",
   "IsEnabledForExternalChannels": false,
   "IsPrivate": false,
   "UsesBusinessDataLabelTable": false,
   "IsLogicalEntity": false,
   "HasNotes": false,
   "HasActivities": false,
   "HasFeedback": false,
   "IsSolutionAware": false,
   "CreatedOn": "2022-09-01T16:13:40Z",
   "ModifiedOn": "2022-09-01T16:13:40Z",
   "HasEmailAddresses": false,
   "OwnerId": null,
   "OwnerIdType": 8,
   "OwningBusinessUnit": null,
   "MetadataId": "5872b902-112a-ed11-9db1-00224804f8e2",
   "HasChanged": null,
   "Description": {
      "LocalizedLabels": [
         {
         "Label": "A table to store information about customer bank accounts",
         "LanguageCode": 1033,
         "IsManaged": false,
         "MetadataId": "daf026b7-dfde-4b7b-8e52-91f31b098a9d",
         "HasChanged": null
         }
      ],
      "UserLocalizedLabel": {
         "Label": "A table to store information about customer bank accounts",
         "LanguageCode": 1033,
         "IsManaged": false,
         "MetadataId": "daf026b7-dfde-4b7b-8e52-91f31b098a9d",
         "HasChanged": null
      }
   },
   "DisplayCollectionName": {
      "LocalizedLabels": [
         {
         "Label": "Bank Accounts",
         "LanguageCode": 1033,
         "IsManaged": false,
         "MetadataId": "5c598c79-b89d-4679-8a40-9562d0a1e4fb",
         "HasChanged": null
         }
      ],
      "UserLocalizedLabel": {
         "Label": "Bank Accounts",
         "LanguageCode": 1033,
         "IsManaged": false,
         "MetadataId": "5c598c79-b89d-4679-8a40-9562d0a1e4fb",
         "HasChanged": null
      }
   },
   "DisplayName": {
      "LocalizedLabels": [
         {
         "Label": "Bank Account",
         "LanguageCode": 1033,
         "IsManaged": false,
         "MetadataId": "4e4c3fdc-7711-4b43-8eba-9155bb7100c0",
         "HasChanged": null
         }
      ],
      "UserLocalizedLabel": {
         "Label": "Bank Account",
         "LanguageCode": 1033,
         "IsManaged": false,
         "MetadataId": "4e4c3fdc-7711-4b43-8eba-9155bb7100c0",
         "HasChanged": null
      }
   },
   "IsAuditEnabled": {
      "Value": false,
      "CanBeChanged": true,
      "ManagedPropertyLogicalName": "canmodifyauditsettings"
   },
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
   "CanBeInCustomEntityAssociation": {
      "Value": true,
      "CanBeChanged": true,
      "ManagedPropertyLogicalName": "canbeincustomentityassociation"
   },
   "CanEnableSyncToExternalSearchIndex": {
      "Value": true,
      "CanBeChanged": true,
      "ManagedPropertyLogicalName": "canenablesynctoexternalsearchindex"
   },
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
   "CanChangeTrackingBeEnabled": {
      "Value": true,
      "CanBeChanged": true,
      "ManagedPropertyLogicalName": "canchangetrackingbeenabled"
   },
   "IsMailMergeEnabled": {
      "Value": false,
      "CanBeChanged": true,
      "ManagedPropertyLogicalName": "canmodifymailmergesettings"
   },
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
   "Privileges": [
      {
         "CanBeBasic": true,
         "CanBeDeep": true,
         "CanBeGlobal": true,
         "CanBeLocal": true,
         "CanBeEntityReference": false,
         "CanBeParentEntityReference": false,
         "Name": "prvCreatesample_BankAccount",
         "PrivilegeId": "44f00701-716e-4584-8bab-cb0d263c070b",
         "PrivilegeType": "Create"
      },
      {
         "CanBeBasic": true,
         "CanBeDeep": true,
         "CanBeGlobal": true,
         "CanBeLocal": true,
         "CanBeEntityReference": false,
         "CanBeParentEntityReference": false,
         "Name": "prvReadsample_BankAccount",
         "PrivilegeId": "9cad3243-d0fe-467e-a731-c8b3416a6252",
         "PrivilegeType": "Read"
      },
      {
         "CanBeBasic": true,
         "CanBeDeep": true,
         "CanBeGlobal": true,
         "CanBeLocal": true,
         "CanBeEntityReference": false,
         "CanBeParentEntityReference": false,
         "Name": "prvWritesample_BankAccount",
         "PrivilegeId": "dc5465ed-223f-4b13-a272-fff25e5b5270",
         "PrivilegeType": "Write"
      },
      {
         "CanBeBasic": true,
         "CanBeDeep": true,
         "CanBeGlobal": true,
         "CanBeLocal": true,
         "CanBeEntityReference": false,
         "CanBeParentEntityReference": false,
         "Name": "prvDeletesample_BankAccount",
         "PrivilegeId": "9a409df2-ca4a-4ad9-8218-df88424dd7a0",
         "PrivilegeType": "Delete"
      },
      {
         "CanBeBasic": true,
         "CanBeDeep": true,
         "CanBeGlobal": true,
         "CanBeLocal": true,
         "CanBeEntityReference": false,
         "CanBeParentEntityReference": false,
         "Name": "prvAssignsample_BankAccount",
         "PrivilegeId": "73bf7dd3-f532-4468-abfe-84bbf0eae058",
         "PrivilegeType": "Assign"
      },
      {
         "CanBeBasic": true,
         "CanBeDeep": true,
         "CanBeGlobal": true,
         "CanBeLocal": true,
         "CanBeEntityReference": false,
         "CanBeParentEntityReference": false,
         "Name": "prvSharesample_BankAccount",
         "PrivilegeId": "292f6e27-9603-4835-882d-e28c175432ed",
         "PrivilegeType": "Share"
      },
      {
         "CanBeBasic": true,
         "CanBeDeep": true,
         "CanBeGlobal": true,
         "CanBeLocal": true,
         "CanBeEntityReference": false,
         "CanBeParentEntityReference": false,
         "Name": "prvAppendsample_BankAccount",
         "PrivilegeId": "42401aa6-6447-4fdc-9679-bcb89b62bd76",
         "PrivilegeType": "Append"
      },
      {
         "CanBeBasic": true,
         "CanBeDeep": true,
         "CanBeGlobal": true,
         "CanBeLocal": true,
         "CanBeEntityReference": false,
         "CanBeParentEntityReference": false,
         "Name": "prvAppendTosample_BankAccount",
         "PrivilegeId": "847ba62d-2f33-4208-87e6-52532b331f60",
         "PrivilegeType": "AppendTo"
      }
   ],
   "Settings": []
   }
   ```

   **Console output:**

   The sample displays the JSON retrieved from the server.


1. Update the `sample_BankAccount` table. The only values that are changed are `HasActivities` and `Description`, but you must send the entire definition with `PUT`.

   **Request:**

   ```http
   PUT [Organization Uri]/api/data/v9.2/EntityDefinitions(LogicalName='sample_bankaccount') HTTP/1.1
   MSCRM.SolutionUniqueName: examplesolution
   MSCRM.MergeLabels: true
   OData-MaxVersion: 4.0
   OData-Version: 4.0
   If-None-Match: null
   Accept: application/json

   {
   "@odata.type": "Microsoft.Dynamics.CRM.EntityMetadata",
   "ActivityTypeMask": 0,
   "AutoCreateAccessTeams": false,
   "AutoRouteToOwnerQueue": false,
   "CanBeInCustomEntityAssociation": {
      "@odata.type": "Microsoft.Dynamics.CRM.BooleanManagedProperty",
      "Value": true,
      "CanBeChanged": true,
      "ManagedPropertyLogicalName": "canbeincustomentityassociation"
   },
   "CanBeInManyToMany": {
      "@odata.type": "Microsoft.Dynamics.CRM.BooleanManagedProperty",
      "Value": true,
      "CanBeChanged": true,
      "ManagedPropertyLogicalName": "canbeinmanytomany"
   },
   "CanBePrimaryEntityInRelationship": {
      "@odata.type": "Microsoft.Dynamics.CRM.BooleanManagedProperty",
      "Value": true,
      "CanBeChanged": true,
      "ManagedPropertyLogicalName": "canbeprimaryentityinrelationship"
   },
   "CanBeRelatedEntityInRelationship": {
      "@odata.type": "Microsoft.Dynamics.CRM.BooleanManagedProperty",
      "Value": true,
      "CanBeChanged": true,
      "ManagedPropertyLogicalName": "canberelatedentityinrelationship"
   },
   "CanChangeHierarchicalRelationship": {
      "@odata.type": "Microsoft.Dynamics.CRM.BooleanManagedProperty",
      "Value": true,
      "CanBeChanged": true,
      "ManagedPropertyLogicalName": "canchangehierarchicalrelationship"
   },
   "CanChangeTrackingBeEnabled": {
      "@odata.type": "Microsoft.Dynamics.CRM.BooleanManagedProperty",
      "Value": true,
      "CanBeChanged": true,
      "ManagedPropertyLogicalName": "canchangetrackingbeenabled"
   },
   "CanCreateAttributes": {
      "@odata.type": "Microsoft.Dynamics.CRM.BooleanManagedProperty",
      "Value": true,
      "CanBeChanged": false,
      "ManagedPropertyLogicalName": "cancreateattributes"
   },
   "CanCreateCharts": {
      "@odata.type": "Microsoft.Dynamics.CRM.BooleanManagedProperty",
      "Value": true,
      "CanBeChanged": true,
      "ManagedPropertyLogicalName": "cancreatecharts"
   },
   "CanCreateForms": {
      "@odata.type": "Microsoft.Dynamics.CRM.BooleanManagedProperty",
      "Value": true,
      "CanBeChanged": true,
      "ManagedPropertyLogicalName": "cancreateforms"
   },
   "CanCreateViews": {
      "@odata.type": "Microsoft.Dynamics.CRM.BooleanManagedProperty",
      "Value": true,
      "CanBeChanged": true,
      "ManagedPropertyLogicalName": "cancreateviews"
   },
   "CanEnableSyncToExternalSearchIndex": {
      "@odata.type": "Microsoft.Dynamics.CRM.BooleanManagedProperty",
      "Value": true,
      "CanBeChanged": true,
      "ManagedPropertyLogicalName": "canenablesynctoexternalsearchindex"
   },
   "CanModifyAdditionalSettings": {
      "@odata.type": "Microsoft.Dynamics.CRM.BooleanManagedProperty",
      "Value": true,
      "CanBeChanged": true,
      "ManagedPropertyLogicalName": "canmodifyadditionalsettings"
   },
   "CanTriggerWorkflow": true,
   "ChangeTrackingEnabled": false,
   "CollectionSchemaName": "sample_BankAccounts",
   "DaysSinceRecordLastModified": 0,
   "Description": {
      "@odata.type": "Microsoft.Dynamics.CRM.Label",
      "LocalizedLabels": [
         {
         "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
         "Label": "Contains information about customer bank accounts",
         "LanguageCode": 1033,
         "IsManaged": false
         }
      ],
      "UserLocalizedLabel": {
         "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
         "Label": "Contains information about customer bank accounts",
         "LanguageCode": 1033,
         "IsManaged": false
      }
   },
   "DisplayCollectionName": {
      "@odata.type": "Microsoft.Dynamics.CRM.Label",
      "LocalizedLabels": [
         {
         "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
         "Label": "Bank Accounts",
         "LanguageCode": 1033,
         "IsManaged": false,
         "MetadataId": "5c598c79-b89d-4679-8a40-9562d0a1e4fb"
         }
      ],
      "UserLocalizedLabel": {
         "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
         "Label": "Bank Accounts",
         "LanguageCode": 1033,
         "IsManaged": false,
         "MetadataId": "5c598c79-b89d-4679-8a40-9562d0a1e4fb"
      }
   },
   "DisplayName": {
      "@odata.type": "Microsoft.Dynamics.CRM.Label",
      "LocalizedLabels": [
         {
         "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
         "Label": "Bank Account",
         "LanguageCode": 1033,
         "IsManaged": false,
         "MetadataId": "4e4c3fdc-7711-4b43-8eba-9155bb7100c0"
         }
      ],
      "UserLocalizedLabel": {
         "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
         "Label": "Bank Account",
         "LanguageCode": 1033,
         "IsManaged": false,
         "MetadataId": "4e4c3fdc-7711-4b43-8eba-9155bb7100c0"
      }
   },
   "EnforceStateTransitions": false,
   "EntityHelpUrlEnabled": false,
   "EntitySetName": "sample_bankaccounts",
   "HasActivities": true,
   "HasFeedback": false,
   "HasNotes": false,
   "IntroducedVersion": "1.0.0.0",
   "IsActivity": false,
   "IsActivityParty": false,
   "IsAIRUpdated": false,
   "IsAuditEnabled": {
      "@odata.type": "Microsoft.Dynamics.CRM.BooleanManagedProperty",
      "Value": false,
      "CanBeChanged": true,
      "ManagedPropertyLogicalName": "canmodifyauditsettings"
   },
   "IsAvailableOffline": false,
   "IsBPFEntity": false,
   "IsBusinessProcessEnabled": false,
   "IsChildEntity": false,
   "IsConnectionsEnabled": {
      "@odata.type": "Microsoft.Dynamics.CRM.BooleanManagedProperty",
      "Value": false,
      "CanBeChanged": true,
      "ManagedPropertyLogicalName": "canmodifyconnectionsettings"
   },
   "IsCustomEntity": true,
   "IsCustomizable": {
      "@odata.type": "Microsoft.Dynamics.CRM.BooleanManagedProperty",
      "Value": true,
      "CanBeChanged": true,
      "ManagedPropertyLogicalName": "iscustomizable"
   },
   "IsDocumentManagementEnabled": false,
   "IsDocumentRecommendationsEnabled": false,
   "IsDuplicateDetectionEnabled": {
      "@odata.type": "Microsoft.Dynamics.CRM.BooleanManagedProperty",
      "Value": false,
      "CanBeChanged": true,
      "ManagedPropertyLogicalName": "canmodifyduplicatedetectionsettings"
   },
   "IsEnabledForCharts": true,
   "IsEnabledForExternalChannels": false,
   "IsEnabledForTrace": false,
   "IsImportable": true,
   "IsInteractionCentricEnabled": false,
   "IsIntersect": false,
   "IsKnowledgeManagementEnabled": false,
   "IsLogicalEntity": false,
   "IsMailMergeEnabled": {
      "@odata.type": "Microsoft.Dynamics.CRM.BooleanManagedProperty",
      "Value": false,
      "CanBeChanged": true,
      "ManagedPropertyLogicalName": "canmodifymailmergesettings"
   },
   "IsManaged": false,
   "IsMappable": {
      "@odata.type": "Microsoft.Dynamics.CRM.BooleanManagedProperty",
      "Value": true,
      "CanBeChanged": false,
      "ManagedPropertyLogicalName": "ismappable"
   },
   "IsMSTeamsIntegrationEnabled": false,
   "IsOfflineInMobileClient": {
      "@odata.type": "Microsoft.Dynamics.CRM.BooleanManagedProperty",
      "Value": false,
      "CanBeChanged": true,
      "ManagedPropertyLogicalName": "canmodifymobileclientoffline"
   },
   "IsOneNoteIntegrationEnabled": false,
   "IsOptimisticConcurrencyEnabled": true,
   "IsPrivate": false,
   "IsQuickCreateEnabled": false,
   "IsReadingPaneEnabled": true,
   "IsReadOnlyInMobileClient": {
      "@odata.type": "Microsoft.Dynamics.CRM.BooleanManagedProperty",
      "Value": false,
      "CanBeChanged": true,
      "ManagedPropertyLogicalName": "canmodifymobileclientreadonly"
   },
   "IsRenameable": {
      "@odata.type": "Microsoft.Dynamics.CRM.BooleanManagedProperty",
      "Value": true,
      "CanBeChanged": true,
      "ManagedPropertyLogicalName": "isrenameable"
   },
   "IsSLAEnabled": false,
   "IsSolutionAware": false,
   "IsStateModelAware": true,
   "IsValidForAdvancedFind": true,
   "IsValidForQueue": {
      "@odata.type": "Microsoft.Dynamics.CRM.BooleanManagedProperty",
      "Value": false,
      "CanBeChanged": true,
      "ManagedPropertyLogicalName": "canmodifyqueuesettings"
   },
   "IsVisibleInMobile": {
      "@odata.type": "Microsoft.Dynamics.CRM.BooleanManagedProperty",
      "Value": false,
      "CanBeChanged": true,
      "ManagedPropertyLogicalName": "canmodifymobilevisibility"
   },
   "IsVisibleInMobileClient": {
      "@odata.type": "Microsoft.Dynamics.CRM.BooleanManagedProperty",
      "Value": false,
      "CanBeChanged": true,
      "ManagedPropertyLogicalName": "canmodifymobileclientvisibility"
   },
   "LogicalCollectionName": "sample_bankaccounts",
   "LogicalName": "sample_bankaccount",
   "MobileOfflineFilters": "",
   "ObjectTypeCode": 10393,
   "OwnershipType": "UserOwned",
   "PrimaryIdAttribute": "sample_bankaccountid",
   "PrimaryNameAttribute": "sample_name",
   "Privileges": [
      {
         "@odata.type": "Microsoft.Dynamics.CRM.SecurityPrivilegeMetadata",
         "CanBeBasic": true,
         "CanBeDeep": true,
         "CanBeGlobal": true,
         "CanBeLocal": true,
         "CanBeEntityReference": false,
         "CanBeParentEntityReference": false,
         "Name": "prvCreatesample_BankAccount",
         "PrivilegeId": "44f00701-716e-4584-8bab-cb0d263c070b",
         "PrivilegeType": "Create"
      },
      {
         "@odata.type": "Microsoft.Dynamics.CRM.SecurityPrivilegeMetadata",
         "CanBeBasic": true,
         "CanBeDeep": true,
         "CanBeGlobal": true,
         "CanBeLocal": true,
         "CanBeEntityReference": false,
         "CanBeParentEntityReference": false,
         "Name": "prvReadsample_BankAccount",
         "PrivilegeId": "9cad3243-d0fe-467e-a731-c8b3416a6252",
         "PrivilegeType": "Read"
      },
      {
         "@odata.type": "Microsoft.Dynamics.CRM.SecurityPrivilegeMetadata",
         "CanBeBasic": true,
         "CanBeDeep": true,
         "CanBeGlobal": true,
         "CanBeLocal": true,
         "CanBeEntityReference": false,
         "CanBeParentEntityReference": false,
         "Name": "prvWritesample_BankAccount",
         "PrivilegeId": "dc5465ed-223f-4b13-a272-fff25e5b5270",
         "PrivilegeType": "Write"
      },
      {
         "@odata.type": "Microsoft.Dynamics.CRM.SecurityPrivilegeMetadata",
         "CanBeBasic": true,
         "CanBeDeep": true,
         "CanBeGlobal": true,
         "CanBeLocal": true,
         "CanBeEntityReference": false,
         "CanBeParentEntityReference": false,
         "Name": "prvDeletesample_BankAccount",
         "PrivilegeId": "9a409df2-ca4a-4ad9-8218-df88424dd7a0",
         "PrivilegeType": "Delete"
      },
      {
         "@odata.type": "Microsoft.Dynamics.CRM.SecurityPrivilegeMetadata",
         "CanBeBasic": true,
         "CanBeDeep": true,
         "CanBeGlobal": true,
         "CanBeLocal": true,
         "CanBeEntityReference": false,
         "CanBeParentEntityReference": false,
         "Name": "prvAssignsample_BankAccount",
         "PrivilegeId": "73bf7dd3-f532-4468-abfe-84bbf0eae058",
         "PrivilegeType": "Assign"
      },
      {
         "@odata.type": "Microsoft.Dynamics.CRM.SecurityPrivilegeMetadata",
         "CanBeBasic": true,
         "CanBeDeep": true,
         "CanBeGlobal": true,
         "CanBeLocal": true,
         "CanBeEntityReference": false,
         "CanBeParentEntityReference": false,
         "Name": "prvSharesample_BankAccount",
         "PrivilegeId": "292f6e27-9603-4835-882d-e28c175432ed",
         "PrivilegeType": "Share"
      },
      {
         "@odata.type": "Microsoft.Dynamics.CRM.SecurityPrivilegeMetadata",
         "CanBeBasic": true,
         "CanBeDeep": true,
         "CanBeGlobal": true,
         "CanBeLocal": true,
         "CanBeEntityReference": false,
         "CanBeParentEntityReference": false,
         "Name": "prvAppendsample_BankAccount",
         "PrivilegeId": "42401aa6-6447-4fdc-9679-bcb89b62bd76",
         "PrivilegeType": "Append"
      },
      {
         "@odata.type": "Microsoft.Dynamics.CRM.SecurityPrivilegeMetadata",
         "CanBeBasic": true,
         "CanBeDeep": true,
         "CanBeGlobal": true,
         "CanBeLocal": true,
         "CanBeEntityReference": false,
         "CanBeParentEntityReference": false,
         "Name": "prvAppendTosample_BankAccount",
         "PrivilegeId": "847ba62d-2f33-4208-87e6-52532b331f60",
         "PrivilegeType": "AppendTo"
      }
   ],
   "ReportViewName": "Filteredsample_BankAccount",
   "SchemaName": "sample_BankAccount",
   "Settings": [],
   "SyncToExternalSearchIndex": false,
   "UsesBusinessDataLabelTable": false,
   "MetadataId": "5872b902-112a-ed11-9db1-00224804f8e2"
   }
   ```

   **Response:**

   ```http
   HTTP/1.1 204 NoContent
   OData-Version: 4.0
   OData-EntityId: [Organization Uri]/api/data/v9.2/EntityDefinitions(LogicalName='sample_bankaccount')
   ```

   **Console output:**

   ```
   Sending request to update the sample_BankAccount table...
   Updated the Bank Account table
   ```

## Section 2: Create, Retrieve and Update Columns

This section creates and retrieves a selected group of column definitions. Each of these types are derived from <xref:Microsoft.Dynamics.CRM.AttributeMetadata?text=AttributeMetadata EntityType> so they share most of the same common properties. However, each derived type has a few special properties.

### Boolean Column

1. Create a Boolean column using <xref:Microsoft.Dynamics.CRM.BooleanAttributeMetadata?text=BooleanAttributeMetadata EntityType>. Despite the name, boolean columns have an `OptionSet` property just like choice columns. However, they always have only two options: `TrueOption` with value 1 and `FalseOption` with value 0.

   **Request:**

   ```http
   POST [Organization Uri]/api/data/v9.2/EntityDefinitions(LogicalName='sample_bankaccount')/Attributes HTTP/1.1
   MSCRM.SolutionUniqueName: examplesolution
   OData-MaxVersion: 4.0
   OData-Version: 4.0
   If-None-Match: null
   Accept: application/json

   {
   "@odata.type": "Microsoft.Dynamics.CRM.BooleanAttributeMetadata",
   "AttributeType": "Boolean",
   "AttributeTypeName": {
      "Value": "BooleanType"
   },
   "DefaultValue": false,
   "OptionSet": {
      "@odata.type": "Microsoft.Dynamics.CRM.BooleanOptionSetMetadata",
      "TrueOption": {
         "Value": 1,
         "Label": {
         "@odata.type": "Microsoft.Dynamics.CRM.Label",
         "LocalizedLabels": [
            {
               "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
               "Label": "True",
               "LanguageCode": 1033,
               "IsManaged": false
            }
         ],
         "UserLocalizedLabel": {
            "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
            "Label": "True",
            "LanguageCode": 1033,
            "IsManaged": false
         }
         }
      },
      "FalseOption": {
         "Value": 0,
         "Label": {
         "@odata.type": "Microsoft.Dynamics.CRM.Label",
         "LocalizedLabels": [
            {
               "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
               "Label": "False",
               "LanguageCode": 1033,
               "IsManaged": false
            }
         ],
         "UserLocalizedLabel": {
            "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
            "Label": "False",
            "LanguageCode": 1033,
            "IsManaged": false
         }
         }
      },
      "OptionSetType": "Boolean"
   },
   "Description": {
      "@odata.type": "Microsoft.Dynamics.CRM.Label",
      "LocalizedLabels": [
         {
         "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
         "Label": "Boolean Attribute",
         "LanguageCode": 1033,
         "IsManaged": false
         }
      ],
      "UserLocalizedLabel": {
         "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
         "Label": "Boolean Attribute",
         "LanguageCode": 1033,
         "IsManaged": false
      }
   },
   "DisplayName": {
      "@odata.type": "Microsoft.Dynamics.CRM.Label",
      "LocalizedLabels": [
         {
         "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
         "Label": "Sample Boolean",
         "LanguageCode": 1033,
         "IsManaged": false
         }
      ],
      "UserLocalizedLabel": {
         "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
         "Label": "Sample Boolean",
         "LanguageCode": 1033,
         "IsManaged": false
      }
   },
   "RequiredLevel": {
      "Value": "None",
      "CanBeChanged": false,
      "ManagedPropertyLogicalName": "canmodifyrequirementlevelsettings"
   },
   "SchemaName": "sample_Boolean"
   }
   ```

   **Response:**

   ```http
   HTTP/1.1 204 NoContent
   OData-Version: 4.0
   OData-EntityId: [Organization Uri]/api/data/v9.2/EntityDefinitions(LogicalName='sample_bankaccount')/Attributes(73f33b3d-112a-ed11-9db1-00224804f8e2)
   ```

1. Retrieve the Boolean column including `$expand=OptionSet` so that the options can be retrieved.

   > [!NOTE]
   > The URL for this request includes `/Microsoft.Dynamics.CRM.BooleanAttributeMetadata` which performs a cast operation that is required to return any property that is not defined within the <xref:Microsoft.Dynamics.CRM.AttributeMetadata?text=AttributeMetadata EntityType>. Without this, the `OptionSet` expansion is not possible.

   **Request:**

   ```http
   GET [Organization Uri]/api/data/v9.2/EntityDefinitions(LogicalName='sample_bankaccount')/Attributes(LogicalName='sample_boolean')/Microsoft.Dynamics.CRM.BooleanAttributeMetadata?$expand=OptionSet HTTP/1.1
   Consistency: Strong
   OData-MaxVersion: 4.0
   OData-Version: 4.0
   If-None-Match: null
   Accept: application/json
   ```

   **Response:**

   ```http
   HTTP/1.1 200 OK
   OData-Version: 4.0

   {
   "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#EntityDefinitions('sample_bankaccount')/Attributes/Microsoft.Dynamics.CRM.BooleanAttributeMetadata(OptionSet())/$entity",
   "MetadataId": "73f33b3d-112a-ed11-9db1-00224804f8e2",
   "HasChanged": null,
   "AttributeOf": null,
   "AttributeType": "Boolean",
   "ColumnNumber": 35,
   "DeprecatedVersion": null,
   "IntroducedVersion": "1.0.0.0",
   "EntityLogicalName": "sample_bankaccount",
   "IsCustomAttribute": true,
   "IsPrimaryId": false,
   "IsValidODataAttribute": true,
   "IsPrimaryName": false,
   "IsValidForCreate": true,
   "IsValidForRead": true,
   "IsValidForUpdate": true,
   "CanBeSecuredForRead": true,
   "CanBeSecuredForCreate": true,
   "CanBeSecuredForUpdate": true,
   "IsSecured": false,
   "IsRetrievable": false,
   "IsFilterable": false,
   "IsSearchable": false,
   "IsManaged": false,
   "LinkedAttributeId": null,
   "LogicalName": "sample_boolean",
   "IsValidForForm": true,
   "IsRequiredForForm": false,
   "IsValidForGrid": true,
   "SchemaName": "sample_Boolean",
   "ExternalName": null,
   "IsLogical": false,
   "IsDataSourceSecret": false,
   "InheritsFrom": null,
   "CreatedOn": "2022-09-01T16:15:08Z",
   "ModifiedOn": "2022-09-01T16:15:08Z",
   "SourceType": 0,
   "AutoNumberFormat": null,
   "DefaultValue": false,
   "FormulaDefinition": "",
   "SourceTypeMask": 0,
   "AttributeTypeName": {
      "Value": "BooleanType"
   },
   "Description": {
      "LocalizedLabels": [
         {
         "Label": "Boolean Attribute",
         "LanguageCode": 1033,
         "IsManaged": false,
         "MetadataId": "ea50b52d-53e4-4f8d-82ce-8f74a7554800",
         "HasChanged": null
         }
      ],
      "UserLocalizedLabel": {
         "Label": "Boolean Attribute",
         "LanguageCode": 1033,
         "IsManaged": false,
         "MetadataId": "ea50b52d-53e4-4f8d-82ce-8f74a7554800",
         "HasChanged": null
      }
   },
   "DisplayName": {
      "LocalizedLabels": [
         {
         "Label": "Sample Boolean",
         "LanguageCode": 1033,
         "IsManaged": false,
         "MetadataId": "9e4daa21-8774-4de9-b467-d046389459dc",
         "HasChanged": null
         }
      ],
      "UserLocalizedLabel": {
         "Label": "Sample Boolean",
         "LanguageCode": 1033,
         "IsManaged": false,
         "MetadataId": "9e4daa21-8774-4de9-b467-d046389459dc",
         "HasChanged": null
      }
   },
   "IsAuditEnabled": {
      "Value": true,
      "CanBeChanged": true,
      "ManagedPropertyLogicalName": "canmodifyauditsettings"
   },
   "IsGlobalFilterEnabled": {
      "Value": false,
      "CanBeChanged": true,
      "ManagedPropertyLogicalName": "canmodifyglobalfiltersettings"
   },
   "IsSortableEnabled": {
      "Value": false,
      "CanBeChanged": true,
      "ManagedPropertyLogicalName": "canmodifyissortablesettings"
   },
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
   "IsValidForAdvancedFind": {
      "Value": true,
      "CanBeChanged": true,
      "ManagedPropertyLogicalName": "canmodifysearchsettings"
   },
   "RequiredLevel": {
      "Value": "None",
      "CanBeChanged": false,
      "ManagedPropertyLogicalName": "canmodifyrequirementlevelsettings"
   },
   "CanModifyAdditionalSettings": {
      "Value": true,
      "CanBeChanged": true,
      "ManagedPropertyLogicalName": "canmodifyadditionalsettings"
   },
   "Settings": [],
   "OptionSet": {
      "MetadataId": "74f33b3d-112a-ed11-9db1-00224804f8e2",
      "HasChanged": null,
      "IsCustomOptionSet": true,
      "IsGlobal": false,
      "IsManaged": false,
      "Name": "sample_bankaccount_sample_boolean",
      "ExternalTypeName": null,
      "OptionSetType": "Boolean",
      "IntroducedVersion": "1.0.0.0",
      "Description": {
         "LocalizedLabels": [
         {
            "Label": "Boolean Attribute",
            "LanguageCode": 1033,
            "IsManaged": false,
            "MetadataId": "76f33b3d-112a-ed11-9db1-00224804f8e2",
            "HasChanged": null
         }
         ],
         "UserLocalizedLabel": {
         "Label": "Boolean Attribute",
         "LanguageCode": 1033,
         "IsManaged": false,
         "MetadataId": "76f33b3d-112a-ed11-9db1-00224804f8e2",
         "HasChanged": null
         }
      },
      "DisplayName": {
         "LocalizedLabels": [
         {
            "Label": "Sample Boolean",
            "LanguageCode": 1033,
            "IsManaged": false,
            "MetadataId": "75f33b3d-112a-ed11-9db1-00224804f8e2",
            "HasChanged": null
         }
         ],
         "UserLocalizedLabel": {
         "Label": "Sample Boolean",
         "LanguageCode": 1033,
         "IsManaged": false,
         "MetadataId": "75f33b3d-112a-ed11-9db1-00224804f8e2",
         "HasChanged": null
         }
      },
      "IsCustomizable": {
         "Value": true,
         "CanBeChanged": true,
         "ManagedPropertyLogicalName": "iscustomizable"
      },
      "TrueOption": {
         "Value": 1,
         "Color": null,
         "IsManaged": false,
         "ExternalValue": "",
         "ParentValues": [],
         "MetadataId": null,
         "HasChanged": null,
         "Label": {
         "LocalizedLabels": [
            {
               "Label": "True",
               "LanguageCode": 1033,
               "IsManaged": false,
               "MetadataId": "12049c5f-e99d-453f-8315-3933512539a1",
               "HasChanged": null
            }
         ],
         "UserLocalizedLabel": {
            "Label": "True",
            "LanguageCode": 1033,
            "IsManaged": false,
            "MetadataId": "12049c5f-e99d-453f-8315-3933512539a1",
            "HasChanged": null
         }
         },
         "Description": {
         "LocalizedLabels": [],
         "UserLocalizedLabel": null
         }
      },
      "FalseOption": {
         "Value": 0,
         "Color": null,
         "IsManaged": false,
         "ExternalValue": "",
         "ParentValues": [],
         "MetadataId": null,
         "HasChanged": null,
         "Label": {
         "LocalizedLabels": [
            {
               "Label": "False",
               "LanguageCode": 1033,
               "IsManaged": false,
               "MetadataId": "e3d4c2b1-ad54-4d3a-8e01-f759da0e476f",
               "HasChanged": null
            }
         ],
         "UserLocalizedLabel": {
            "Label": "False",
            "LanguageCode": 1033,
            "IsManaged": false,
            "MetadataId": "e3d4c2b1-ad54-4d3a-8e01-f759da0e476f",
            "HasChanged": null
         }
         },
         "Description": {
         "LocalizedLabels": [],
         "UserLocalizedLabel": null
         }
      }
   }
   }
   ```

   **Console output:**

   ```
   Original Option Labels:
   True Option Label:'True' Value: 1
   False Option Label:'False' Value: 0
   ```

1. Update the Boolean column. The only changes are to the `DisplayName`, `Description`, and `RequiredLevel` properties, but the entire definition is included because `PUT` is used.

   > [!NOTE]
   > Even though the `OptionSet` property is included in this payload, any changes to the options would not be applied because they are not considered part of the column definition. They must be updated separately and this sample will show you how in following steps.

   **Request:**

   ```http
   PUT [Organization Uri]/api/data/v9.2/EntityDefinitions(LogicalName='sample_bankaccount')/Attributes(LogicalName='sample_boolean') HTTP/1.1
   MSCRM.SolutionUniqueName: examplesolution
   MSCRM.MergeLabels: true
   OData-MaxVersion: 4.0
   OData-Version: 4.0
   If-None-Match: null
   Accept: application/json

   {
   "@odata.type": "Microsoft.Dynamics.CRM.BooleanAttributeMetadata",
   "AttributeType": "Boolean",
   "AttributeTypeName": {
      "Value": "BooleanType"
   },
   "DefaultValue": false,
   "FormulaDefinition": "",
   "SourceTypeMask": 0,
   "OptionSet": {
      "@odata.type": "Microsoft.Dynamics.CRM.BooleanOptionSetMetadata",
      "TrueOption": {
         "Value": 1,
         "Label": {
         "@odata.type": "Microsoft.Dynamics.CRM.Label",
         "LocalizedLabels": [
            {
               "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
               "Label": "True",
               "LanguageCode": 1033,
               "IsManaged": false,
               "MetadataId": "12049c5f-e99d-453f-8315-3933512539a1"
            }
         ],
         "UserLocalizedLabel": {
            "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
            "Label": "True",
            "LanguageCode": 1033,
            "IsManaged": false,
            "MetadataId": "12049c5f-e99d-453f-8315-3933512539a1"
         }
         },
         "Description": {
         "@odata.type": "Microsoft.Dynamics.CRM.Label",
         "LocalizedLabels": [],
         "UserLocalizedLabel": {
            "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
            "LanguageCode": 0,
            "IsManaged": false
         }
         },
         "IsManaged": false,
         "ExternalValue": ""
      },
      "FalseOption": {
         "Value": 0,
         "Label": {
         "@odata.type": "Microsoft.Dynamics.CRM.Label",
         "LocalizedLabels": [
            {
               "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
               "Label": "False",
               "LanguageCode": 1033,
               "IsManaged": false,
               "MetadataId": "e3d4c2b1-ad54-4d3a-8e01-f759da0e476f"
            }
         ],
         "UserLocalizedLabel": {
            "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
            "Label": "False",
            "LanguageCode": 1033,
            "IsManaged": false,
            "MetadataId": "e3d4c2b1-ad54-4d3a-8e01-f759da0e476f"
         }
         },
         "Description": {
         "@odata.type": "Microsoft.Dynamics.CRM.Label",
         "LocalizedLabels": [],
         "UserLocalizedLabel": {
            "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
            "LanguageCode": 0,
            "IsManaged": false
         }
         },
         "IsManaged": false,
         "ExternalValue": ""
      },
      "OptionSetType": "Boolean",
      "Description": {
         "@odata.type": "Microsoft.Dynamics.CRM.Label",
         "LocalizedLabels": [
         {
            "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
            "Label": "Boolean Attribute",
            "LanguageCode": 1033,
            "IsManaged": false,
            "MetadataId": "76f33b3d-112a-ed11-9db1-00224804f8e2"
         }
         ],
         "UserLocalizedLabel": {
         "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
         "Label": "Boolean Attribute",
         "LanguageCode": 1033,
         "IsManaged": false,
         "MetadataId": "76f33b3d-112a-ed11-9db1-00224804f8e2"
         }
      },
      "DisplayName": {
         "@odata.type": "Microsoft.Dynamics.CRM.Label",
         "LocalizedLabels": [
         {
            "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
            "Label": "Sample Boolean",
            "LanguageCode": 1033,
            "IsManaged": false,
            "MetadataId": "75f33b3d-112a-ed11-9db1-00224804f8e2"
         }
         ],
         "UserLocalizedLabel": {
         "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
         "Label": "Sample Boolean",
         "LanguageCode": 1033,
         "IsManaged": false,
         "MetadataId": "75f33b3d-112a-ed11-9db1-00224804f8e2"
         }
      },
      "IntroducedVersion": "1.0.0.0",
      "IsCustomizable": {
         "@odata.type": "Microsoft.Dynamics.CRM.BooleanManagedProperty",
         "Value": true,
         "CanBeChanged": true,
         "ManagedPropertyLogicalName": "iscustomizable"
      },
      "IsCustomOptionSet": true,
      "IsGlobal": false,
      "IsManaged": false,
      "Name": "sample_bankaccount_sample_boolean",
      "MetadataId": "74f33b3d-112a-ed11-9db1-00224804f8e2"
   },
   "CanBeSecuredForCreate": true,
   "CanBeSecuredForRead": true,
   "CanBeSecuredForUpdate": true,
   "CanModifyAdditionalSettings": {
      "@odata.type": "Microsoft.Dynamics.CRM.BooleanManagedProperty",
      "Value": true,
      "CanBeChanged": true,
      "ManagedPropertyLogicalName": "canmodifyadditionalsettings"
   },
   "ColumnNumber": 35,
   "Description": {
      "@odata.type": "Microsoft.Dynamics.CRM.Label",
      "LocalizedLabels": [
         {
         "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
         "Label": "Boolean Attribute Updated",
         "LanguageCode": 1033,
         "IsManaged": false
         }
      ],
      "UserLocalizedLabel": {
         "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
         "Label": "Boolean Attribute Updated",
         "LanguageCode": 1033,
         "IsManaged": false
      }
   },
   "DisplayName": {
      "@odata.type": "Microsoft.Dynamics.CRM.Label",
      "LocalizedLabels": [
         {
         "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
         "Label": "Sample Boolean Updated",
         "LanguageCode": 1033,
         "IsManaged": false
         }
      ],
      "UserLocalizedLabel": {
         "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
         "Label": "Sample Boolean Updated",
         "LanguageCode": 1033,
         "IsManaged": false
      }
   },
   "EntityLogicalName": "sample_bankaccount",
   "IntroducedVersion": "1.0.0.0",
   "IsAuditEnabled": {
      "@odata.type": "Microsoft.Dynamics.CRM.BooleanManagedProperty",
      "Value": true,
      "CanBeChanged": true,
      "ManagedPropertyLogicalName": "canmodifyauditsettings"
   },
   "IsCustomAttribute": true,
   "IsCustomizable": {
      "@odata.type": "Microsoft.Dynamics.CRM.BooleanManagedProperty",
      "Value": true,
      "CanBeChanged": true,
      "ManagedPropertyLogicalName": "iscustomizable"
   },
   "IsDataSourceSecret": false,
   "IsFilterable": false,
   "IsGlobalFilterEnabled": {
      "@odata.type": "Microsoft.Dynamics.CRM.BooleanManagedProperty",
      "Value": false,
      "CanBeChanged": true,
      "ManagedPropertyLogicalName": "canmodifyglobalfiltersettings"
   },
   "IsLogical": false,
   "IsManaged": false,
   "IsPrimaryId": false,
   "IsPrimaryName": false,
   "IsRenameable": {
      "@odata.type": "Microsoft.Dynamics.CRM.BooleanManagedProperty",
      "Value": true,
      "CanBeChanged": true,
      "ManagedPropertyLogicalName": "isrenameable"
   },
   "IsRequiredForForm": false,
   "IsRetrievable": false,
   "IsSearchable": false,
   "IsSecured": false,
   "IsSortableEnabled": {
      "@odata.type": "Microsoft.Dynamics.CRM.BooleanManagedProperty",
      "Value": false,
      "CanBeChanged": true,
      "ManagedPropertyLogicalName": "canmodifyissortablesettings"
   },
   "IsValidForAdvancedFind": {
      "@odata.type": "Microsoft.Dynamics.CRM.BooleanManagedProperty",
      "Value": true,
      "CanBeChanged": true,
      "ManagedPropertyLogicalName": "canmodifysearchsettings"
   },
   "IsValidForCreate": true,
   "IsValidForForm": true,
   "IsValidForGrid": true,
   "IsValidForRead": true,
   "IsValidForUpdate": true,
   "LogicalName": "sample_boolean",
   "RequiredLevel": {
      "Value": "ApplicationRequired",
      "CanBeChanged": false,
      "ManagedPropertyLogicalName": "canmodifyrequirementlevelsettings"
   },
   "SchemaName": "sample_Boolean",
   "SourceType": 0,
   "MetadataId": "73f33b3d-112a-ed11-9db1-00224804f8e2"
   }
   ```

   **Response:**

   ```http
   HTTP/1.1 204 NoContent
   OData-Version: 4.0
   OData-EntityId: [Organization Uri]/api/data/v9.2/EntityDefinitions(LogicalName='sample_bankaccount')/Attributes(LogicalName='sample_boolean')
   ```

   **Console output:**

   ```
   Updated Boolean Column properties
   ```

#### Update Option Values

Update each of the boolean options using <xref:Microsoft.Dynamics.CRM.UpdateOptionValue?text=UpdateOptionValue Action>. 

> [!NOTE]
> Here we are applying changes to options in a boolean attribute, but you will use `UpdateOptionValue` for options in any type of column that uses them except `status` columns, where you must use the <xref:Microsoft.Dynamics.CRM.UpdateStateValue?text=UpdateStateValue Action>.

1. Change the `TrueOption` value label to 'Up'.

   **Request:**

   ```http
   POST [Organization Uri]/api/data/v9.2/UpdateOptionValue HTTP/1.1
   OData-MaxVersion: 4.0
   OData-Version: 4.0
   If-None-Match: null
   Accept: application/json

   {
   "AttributeLogicalName": "sample_boolean",
   "EntityLogicalName": "sample_bankaccount",
   "Value": 1,
   "Label": {
      "@odata.type": "Microsoft.Dynamics.CRM.Label",
      "LocalizedLabels": [
         {
         "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
         "Label": "Up",
         "LanguageCode": 1033,
         "IsManaged": false
         }
      ],
      "UserLocalizedLabel": {
         "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
         "Label": "Up",
         "LanguageCode": 1033,
         "IsManaged": false
      }
   },
   "MergeLabels": true
   }
   ```

   **Response:**

   ```http
   HTTP/1.1 204 NoContent
   OData-Version: 4.0
   ```

1. Change the `FalseOption` value label to 'Down'.

   **Request:**

   ```http
   POST [Organization Uri]/api/data/v9.2/UpdateOptionValue HTTP/1.1
   OData-MaxVersion: 4.0
   OData-Version: 4.0
   If-None-Match: null
   Accept: application/json

   {
   "AttributeLogicalName": "sample_boolean",
   "EntityLogicalName": "sample_bankaccount",
   "Value": 0,
   "Label": {
      "@odata.type": "Microsoft.Dynamics.CRM.Label",
      "LocalizedLabels": [
         {
         "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
         "Label": "Down",
         "LanguageCode": 1033,
         "IsManaged": false
         }
      ],
      "UserLocalizedLabel": {
         "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
         "Label": "Down",
         "LanguageCode": 1033,
         "IsManaged": false
      }
   },
   "MergeLabels": true
   }
   ```

   **Response:**

   ```http
   HTTP/1.1 204 NoContent
   OData-Version: 4.0
   ```

   **Console output:**

   ```
   Updated option labels
   ```

1. Retrieve the modified option values for the Boolean column using the same query as before:

   **Console output:**

   ```
   Updated Option Labels:
   Updated True Option Label:'Up' Value: 1
   Updated False Option Label:'Down' Value: 0
   ```

### DateTime Column

1. Create a DateTime column using <xref:Microsoft.Dynamics.CRM.DateTimeAttributeMetadata?text=DateTimeAttributeMetadata EntityType>.

   **Request:**

   ```http
   POST [Organization Uri]/api/data/v9.2/EntityDefinitions(LogicalName='sample_bankaccount')/Attributes HTTP/1.1
   MSCRM.SolutionUniqueName: examplesolution
   OData-MaxVersion: 4.0
   OData-Version: 4.0
   If-None-Match: null
   Accept: application/json

   {
   "@odata.type": "Microsoft.Dynamics.CRM.DateTimeAttributeMetadata",
   "AttributeType": "DateTime",
   "AttributeTypeName": {
      "Value": "DateTimeType"
   },
   "Format": "DateOnly",
   "ImeMode": "Disabled",
   "DateTimeBehavior": {
      "Value": "DateOnly"
   },
   "Description": {
      "@odata.type": "Microsoft.Dynamics.CRM.Label",
      "LocalizedLabels": [
         {
         "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
         "Label": "DateTime Attribute",
         "LanguageCode": 1033,
         "IsManaged": false
         }
      ],
      "UserLocalizedLabel": {
         "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
         "Label": "DateTime Attribute",
         "LanguageCode": 1033,
         "IsManaged": false
      }
   },
   "DisplayName": {
      "@odata.type": "Microsoft.Dynamics.CRM.Label",
      "LocalizedLabels": [
         {
         "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
         "Label": "Sample DateTime",
         "LanguageCode": 1033,
         "IsManaged": false
         }
      ],
      "UserLocalizedLabel": {
         "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
         "Label": "Sample DateTime",
         "LanguageCode": 1033,
         "IsManaged": false
      }
   },
   "RequiredLevel": {
      "Value": "None",
      "CanBeChanged": false,
      "ManagedPropertyLogicalName": "canmodifyrequirementlevelsettings"
   },
   "SchemaName": "sample_DateTime"
   }
   ```

   **Response:**

   ```http
   HTTP/1.1 204 NoContent
   OData-Version: 4.0
   OData-EntityId: [Organization Uri]/api/data/v9.2/EntityDefinitions(LogicalName='sample_bankaccount')/Attributes(f1db3d43-112a-ed11-9db1-00224804f8e2)
   ```

   **Console output:**

   ```
   Created DateTime column with id:f1db3d43-112a-ed11-9db1-00224804f8e2
   ```

1. Retrieve selected values of the DateTime column.


   **Request:**

   ```http
   GET [Organization Uri]/api/data/v9.2/EntityDefinitions(LogicalName='sample_bankaccount')/Attributes(LogicalName='sample_datetime')/Microsoft.Dynamics.CRM.DateTimeAttributeMetadata?$select=SchemaName,Format,DateTimeBehavior HTTP/1.1
   Consistency: Strong
   OData-MaxVersion: 4.0
   OData-Version: 4.0
   If-None-Match: null
   Accept: application/json
   ```

   **Response:**

   ```http
   HTTP/1.1 200 OK
   OData-Version: 4.0

   {
   "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#EntityDefinitions('sample_bankaccount')/Attributes/Microsoft.Dynamics.CRM.DateTimeAttributeMetadata(SchemaName,Format,DateTimeBehavior)/$entity",
   "SchemaName": "sample_DateTime",
   "Format": "DateOnly",
   "MetadataId": "f1db3d43-112a-ed11-9db1-00224804f8e2",
   "DateTimeBehavior": {
      "Value": "DateOnly"
    }
   }
   ```

   **Console output:**

   ```
   Retrieved Datetime column properties:
         DateTime Format:'DateOnly'
         DateTime DateTimeBehavior:'DateOnly'
   ```

### Decimal Column

1. Create a Decimal Column using <xref:Microsoft.Dynamics.CRM.DecimalAttributeMetadata?text=DecimalAttributeMetadata EntityType>.

   **Request:**

   ```http
   POST [Organization Uri]/api/data/v9.2/EntityDefinitions(LogicalName='sample_bankaccount')/Attributes HTTP/1.1
   MSCRM.SolutionUniqueName: examplesolution
   OData-MaxVersion: 4.0
   OData-Version: 4.0
   If-None-Match: null
   Accept: application/json

   {
   "@odata.type": "Microsoft.Dynamics.CRM.DecimalAttributeMetadata",
   "AttributeType": "Decimal",
   "AttributeTypeName": {
      "Value": "DecimalType"
   },
   "MaxValue": 100.0,
   "MinValue": 0.0,
   "Precision": 1,
   "Description": {
      "@odata.type": "Microsoft.Dynamics.CRM.Label",
      "LocalizedLabels": [
         {
         "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
         "Label": "Decimal Attribute",
         "LanguageCode": 1033,
         "IsManaged": false
         }
      ],
      "UserLocalizedLabel": {
         "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
         "Label": "Decimal Attribute",
         "LanguageCode": 1033,
         "IsManaged": false
      }
   },
   "DisplayName": {
      "@odata.type": "Microsoft.Dynamics.CRM.Label",
      "LocalizedLabels": [
         {
         "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
         "Label": "Sample Decimal",
         "LanguageCode": 1033,
         "IsManaged": false
         }
      ],
      "UserLocalizedLabel": {
         "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
         "Label": "Sample Decimal",
         "LanguageCode": 1033,
         "IsManaged": false
      }
   },
   "RequiredLevel": {
      "Value": "None",
      "CanBeChanged": false,
      "ManagedPropertyLogicalName": "canmodifyrequirementlevelsettings"
   },
   "SchemaName": "sample_Decimal"
   }
   ```

   **Response:**

   ```http
   HTTP/1.1 204 NoContent
   OData-Version: 4.0
   OData-EntityId: [Organization Uri]/api/data/v9.2/EntityDefinitions(LogicalName='sample_bankaccount')/Attributes(f2db3d43-112a-ed11-9db1-00224804f8e2)
   ```

   **Console output:**

   ```
   Created Decimal column with id:f2db3d43-112a-ed11-9db1-00224804f8e2
   ```

1. Retrieve selected values of the Decimal column.

   **Request:**

   ```http
   GET [Organization Uri]/api/data/v9.2/EntityDefinitions(LogicalName='sample_bankaccount')/Attributes(LogicalName='sample_decimal')/Microsoft.Dynamics.CRM.DecimalAttributeMetadata?$select=SchemaName,MaxValue,MinValue,Precision HTTP/1.1
   Consistency: Strong
   OData-MaxVersion: 4.0
   OData-Version: 4.0
   If-None-Match: null
   Accept: application/json
   ```

   **Response:**

   ```http
   HTTP/1.1 200 OK
   OData-Version: 4.0

   {
   "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#EntityDefinitions('sample_bankaccount')/Attributes/Microsoft.Dynamics.CRM.DecimalAttributeMetadata(SchemaName,MaxValue,MinValue,Precision)/$entity",
   "SchemaName": "sample_Decimal",
   "MaxValue": 100,
   "MinValue": 0,
   "Precision": 1,
   "MetadataId": "f2db3d43-112a-ed11-9db1-00224804f8e2"
   }
   ```

   **Console output:**

   ```
   Retrieved Decimal column properties:
   Decimal MaxValue:100
   Decimal MinValue:0
   Decimal Precision:1
   ```

### Integer Column

1. Create an Integer column using <xref:Microsoft.Dynamics.CRM.IntegerAttributeMetadata?text=IntegerAttributeMetadata EntityType>.

   **Request:**

   ```http
   POST [Organization Uri]/api/data/v9.2/EntityDefinitions(LogicalName='sample_bankaccount')/Attributes HTTP/1.1
   MSCRM.SolutionUniqueName: examplesolution
   OData-MaxVersion: 4.0
   OData-Version: 4.0
   If-None-Match: null
   Accept: application/json

   {
   "@odata.type": "Microsoft.Dynamics.CRM.IntegerAttributeMetadata",
   "AttributeType": "Integer",
   "AttributeTypeName": {
      "Value": "IntegerType"
   },
   "MaxValue": 100,
   "MinValue": 0,
   "Format": "None",
   "SourceTypeMask": 0,
   "Description": {
      "@odata.type": "Microsoft.Dynamics.CRM.Label",
      "LocalizedLabels": [
         {
         "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
         "Label": "Integer Attribute",
         "LanguageCode": 1033,
         "IsManaged": false
         }
      ],
      "UserLocalizedLabel": {
         "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
         "Label": "Integer Attribute",
         "LanguageCode": 1033,
         "IsManaged": false
      }
   },
   "DisplayName": {
      "@odata.type": "Microsoft.Dynamics.CRM.Label",
      "LocalizedLabels": [
         {
         "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
         "Label": "Sample Integer",
         "LanguageCode": 1033,
         "IsManaged": false
         }
      ],
      "UserLocalizedLabel": {
         "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
         "Label": "Sample Integer",
         "LanguageCode": 1033,
         "IsManaged": false
      }
   },
   "RequiredLevel": {
      "Value": "None",
      "CanBeChanged": false,
      "ManagedPropertyLogicalName": "canmodifyrequirementlevelsettings"
   },
   "SchemaName": "sample_Integer"
   }
   ```

   **Response:**

   ```http
   HTTP/1.1 204 NoContent
   OData-Version: 4.0
   OData-EntityId: [Organization Uri]/api/data/v9.2/EntityDefinitions(LogicalName='sample_bankaccount')/Attributes(f5db3d43-112a-ed11-9db1-00224804f8e2)
   ```

   **Console output:**

   ```
   Created Integer column with id:f5db3d43-112a-ed11-9db1-00224804f8e2
   ```

1. Retrieve selected values of the Integer column.

   **Request:**

   ```http
   GET [Organization Uri]/api/data/v9.2/EntityDefinitions(LogicalName='sample_bankaccount')/Attributes(LogicalName='sample_integer')/Microsoft.Dynamics.CRM.IntegerAttributeMetadata?$select=SchemaName,MaxValue,MinValue,Format HTTP/1.1
   Consistency: Strong
   OData-MaxVersion: 4.0
   OData-Version: 4.0
   If-None-Match: null
   Accept: application/json
   ```

   **Response:**

   ```http
   HTTP/1.1 200 OK
   OData-Version: 4.0

   {
   "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#EntityDefinitions('sample_bankaccount')/Attributes/Microsoft.Dynamics.CRM.IntegerAttributeMetadata(SchemaName,MaxValue,MinValue,Format)/$entity",
   "SchemaName": "sample_Integer",
   "MaxValue": 100,
   "MinValue": 0,
   "Format": "None",
   "MetadataId": "f5db3d43-112a-ed11-9db1-00224804f8e2"
   }
   ```

   **Console output:**

   ```
   Retrieved Integer column properties:
   Integer MaxValue:100
   Integer MinValue:0
   Integer Format:None
   ```

### Memo Column

1. Create a Memo Column using <xref:Microsoft.Dynamics.CRM.MemoAttributeMetadata?text=MemoAttributeMetadata EntityType>.

   **Request:**

   ```http
   POST [Organization Uri]/api/data/v9.2/EntityDefinitions(LogicalName='sample_bankaccount')/Attributes HTTP/1.1
   MSCRM.SolutionUniqueName: examplesolution
   OData-MaxVersion: 4.0
   OData-Version: 4.0
   If-None-Match: null
   Accept: application/json

   {
   "@odata.type": "Microsoft.Dynamics.CRM.MemoAttributeMetadata",
   "AttributeType": "Memo",
   "AttributeTypeName": {
      "Value": "MemoType"
   },
   "Format": "TextArea",
   "ImeMode": "Disabled",
   "MaxLength": 500,
   "IsLocalizable": false,
   "Description": {
      "@odata.type": "Microsoft.Dynamics.CRM.Label",
      "LocalizedLabels": [
         {
         "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
         "Label": "Memo Attribute",
         "LanguageCode": 1033,
         "IsManaged": false
         }
      ],
      "UserLocalizedLabel": {
         "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
         "Label": "Memo Attribute",
         "LanguageCode": 1033,
         "IsManaged": false
      }
   },
   "DisplayName": {
      "@odata.type": "Microsoft.Dynamics.CRM.Label",
      "LocalizedLabels": [
         {
         "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
         "Label": "Sample Memo",
         "LanguageCode": 1033,
         "IsManaged": false
         }
      ],
      "UserLocalizedLabel": {
         "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
         "Label": "Sample Memo",
         "LanguageCode": 1033,
         "IsManaged": false
      }
   },
   "RequiredLevel": {
      "Value": "None",
      "CanBeChanged": false,
      "ManagedPropertyLogicalName": "canmodifyrequirementlevelsettings"
   },
   "SchemaName": "sample_Memo"
   }
   ```

   **Response:**

   ```http
   HTTP/1.1 204 NoContent
   OData-Version: 4.0
   OData-EntityId: [Organization Uri]/api/data/v9.2/EntityDefinitions(LogicalName='sample_bankaccount')/Attributes(f6db3d43-112a-ed11-9db1-00224804f8e2)
   ```

   **Console output:**

   ```
   Created Memo column with id:f6db3d43-112a-ed11-9db1-00224804f8e2
   ```

1. Retrieve selected values of the Memo Column.

   **Request:**

   ```http
   GET [Organization Uri]/api/data/v9.2/EntityDefinitions(LogicalName='sample_bankaccount')/Attributes(LogicalName='sample_memo')/Microsoft.Dynamics.CRM.MemoAttributeMetadata?$select=SchemaName,Format,ImeMode,MaxLength HTTP/1.1
   Consistency: Strong
   OData-MaxVersion: 4.0
   OData-Version: 4.0
   If-None-Match: null
   Accept: application/json
   ```

   **Response:**

   ```http
   HTTP/1.1 200 OK
   OData-Version: 4.0

   {
   "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#EntityDefinitions('sample_bankaccount')/Attributes/Microsoft.Dynamics.CRM.MemoAttributeMetadata(SchemaName,Format,ImeMode,MaxLength)/$entity",
   "SchemaName": "sample_Memo",
   "Format": "TextArea",
   "ImeMode": "Disabled",
   "MaxLength": 500,
   "MetadataId": "f6db3d43-112a-ed11-9db1-00224804f8e2"
   }
   ```

   **Console output:**

   ```
   Retrieved Memo column properties:
   Memo Format:TextArea
   Memo ImeMode:Disabled
   Memo MaxLength:500
   ```

### Money Column

1. Create a Money Column using <xref:Microsoft.Dynamics.CRM.MoneyAttributeMetadata?text=MoneyAttributeMetadata EntityType>.

   **Request:**

   ```http
   POST [Organization Uri]/api/data/v9.2/EntityDefinitions(LogicalName='sample_bankaccount')/Attributes HTTP/1.1
   MSCRM.SolutionUniqueName: examplesolution
   OData-MaxVersion: 4.0
   OData-Version: 4.0
   If-None-Match: null
   Accept: application/json

   {
   "@odata.type": "Microsoft.Dynamics.CRM.MoneyAttributeMetadata",
   "AttributeType": "Money",
   "AttributeTypeName": {
      "Value": "MoneyType"
   },
   "ImeMode": "Disabled",
   "MaxValue": 1000.0,
   "MinValue": 0.0,
   "Precision": 1,
   "PrecisionSource": 1,
   "SourceTypeMask": 0,
   "IsBaseCurrency": false,
   "Description": {
      "@odata.type": "Microsoft.Dynamics.CRM.Label",
      "LocalizedLabels": [
         {
         "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
         "Label": "Money Attribute",
         "LanguageCode": 1033,
         "IsManaged": false
         }
      ],
      "UserLocalizedLabel": {
         "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
         "Label": "Money Attribute",
         "LanguageCode": 1033,
         "IsManaged": false
      }
   },
   "DisplayName": {
      "@odata.type": "Microsoft.Dynamics.CRM.Label",
      "LocalizedLabels": [
         {
         "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
         "Label": "Sample Money",
         "LanguageCode": 1033,
         "IsManaged": false
         }
      ],
      "UserLocalizedLabel": {
         "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
         "Label": "Sample Money",
         "LanguageCode": 1033,
         "IsManaged": false
      }
   },
   "RequiredLevel": {
      "Value": "None",
      "CanBeChanged": false,
      "ManagedPropertyLogicalName": "canmodifyrequirementlevelsettings"
   },
   "SchemaName": "sample_Money"
   }
   ```

   **Response:**

   ```http
   HTTP/1.1 204 NoContent
   OData-Version: 4.0
   OData-EntityId: [Organization Uri]/api/data/v9.2/EntityDefinitions(LogicalName='sample_bankaccount')/Attributes(fddb3d43-112a-ed11-9db1-00224804f8e2)
   ```

   **Console output:**

   ```
   Created Money column with id:fddb3d43-112a-ed11-9db1-00224804f8e2
   ```

1. Retrieve selected values of the Money Column.

   **Request:**

   ```http
   GET [Organization Uri]/api/data/v9.2/EntityDefinitions(LogicalName='sample_bankaccount')/Attributes(LogicalName='sample_money')/Microsoft.Dynamics.CRM.MoneyAttributeMetadata?$select=SchemaName,MaxValue,MinValue,Precision,PrecisionSource,ImeMode HTTP/1.1
   Consistency: Strong
   OData-MaxVersion: 4.0
   OData-Version: 4.0
   If-None-Match: null
   Accept: application/json
   ```

   **Response:**

   ```http
   HTTP/1.1 200 OK
   OData-Version: 4.0

   {
   "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#EntityDefinitions('sample_bankaccount')/Attributes/Microsoft.Dynamics.CRM.MoneyAttributeMetadata(SchemaName,MaxValue,MinValue,Precision,PrecisionSource,ImeMode)/$entity",
   "SchemaName": "sample_Money",
   "MaxValue": 1000.0,
   "MinValue": 0.0,
   "Precision": 1,
   "PrecisionSource": 1,
   "ImeMode": "Disabled",
   "MetadataId": "fddb3d43-112a-ed11-9db1-00224804f8e2"
   }
   ```

   **Console output:**

   ```
   Retrieved Money column properties:
   Money MaxValue:1000
   Money MinValue:0
   Money Precision:1
   Money PrecisionSource:1
   Money ImeMode:Disabled
   ```

### Picklist Column

1. Create a Choice (Picklist) Column using <xref:Microsoft.Dynamics.CRM.PicklistAttributeMetadata?text=PicklistAttributeMetadata EntityType> with a local option set.

   **Request:**

   ```http
   POST [Organization Uri]/api/data/v9.2/EntityDefinitions(LogicalName='sample_bankaccount')/Attributes HTTP/1.1
   MSCRM.SolutionUniqueName: examplesolution
   OData-MaxVersion: 4.0
   OData-Version: 4.0
   If-None-Match: null
   Accept: application/json

   {
   "@odata.type": "Microsoft.Dynamics.CRM.PicklistAttributeMetadata",
   "AttributeType": "Picklist",
   "AttributeTypeName": {
      "Value": "PicklistType"
   },
   "SourceTypeMask": 0,
   "OptionSet": {
      "@odata.type": "Microsoft.Dynamics.CRM.OptionSetMetadata",
      "Options": [
         {
         "Value": 727000000,
         "Label": {
            "@odata.type": "Microsoft.Dynamics.CRM.Label",
            "LocalizedLabels": [
               {
               "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
               "Label": "Bravo",
               "LanguageCode": 1033,
               "IsManaged": false
               }
            ],
            "UserLocalizedLabel": {
               "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
               "Label": "Bravo",
               "LanguageCode": 1033,
               "IsManaged": false
            }
         }
         },
         {
         "Value": 727000001,
         "Label": {
            "@odata.type": "Microsoft.Dynamics.CRM.Label",
            "LocalizedLabels": [
               {
               "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
               "Label": "Delta",
               "LanguageCode": 1033,
               "IsManaged": false
               }
            ],
            "UserLocalizedLabel": {
               "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
               "Label": "Delta",
               "LanguageCode": 1033,
               "IsManaged": false
            }
         }
         },
         {
         "Value": 727000002,
         "Label": {
            "@odata.type": "Microsoft.Dynamics.CRM.Label",
            "LocalizedLabels": [
               {
               "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
               "Label": "Alpha",
               "LanguageCode": 1033,
               "IsManaged": false
               }
            ],
            "UserLocalizedLabel": {
               "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
               "Label": "Alpha",
               "LanguageCode": 1033,
               "IsManaged": false
            }
         }
         },
         {
         "Value": 727000003,
         "Label": {
            "@odata.type": "Microsoft.Dynamics.CRM.Label",
            "LocalizedLabels": [
               {
               "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
               "Label": "Charlie",
               "LanguageCode": 1033,
               "IsManaged": false
               }
            ],
            "UserLocalizedLabel": {
               "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
               "Label": "Charlie",
               "LanguageCode": 1033,
               "IsManaged": false
            }
         }
         },
         {
         "Value": 727000004,
         "Label": {
            "@odata.type": "Microsoft.Dynamics.CRM.Label",
            "LocalizedLabels": [
               {
               "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
               "Label": "Foxtrot",
               "LanguageCode": 1033,
               "IsManaged": false
               }
            ],
            "UserLocalizedLabel": {
               "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
               "Label": "Foxtrot",
               "LanguageCode": 1033,
               "IsManaged": false
            }
         }
         }
      ],
      "IsGlobal": false,
      "OptionSetType": "Picklist"
   },
   "Description": {
      "@odata.type": "Microsoft.Dynamics.CRM.Label",
      "LocalizedLabels": [
         {
         "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
         "Label": "Choice Attribute",
         "LanguageCode": 1033,
         "IsManaged": false
         }
      ],
      "UserLocalizedLabel": {
         "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
         "Label": "Choice Attribute",
         "LanguageCode": 1033,
         "IsManaged": false
      }
   },
   "DisplayName": {
      "@odata.type": "Microsoft.Dynamics.CRM.Label",
      "LocalizedLabels": [
         {
         "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
         "Label": "Sample Choice",
         "LanguageCode": 1033,
         "IsManaged": false
         }
      ],
      "UserLocalizedLabel": {
         "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
         "Label": "Sample Choice",
         "LanguageCode": 1033,
         "IsManaged": false
      }
   },
   "RequiredLevel": {
      "Value": "None",
      "CanBeChanged": false,
      "ManagedPropertyLogicalName": "canmodifyrequirementlevelsettings"
   },
   "SchemaName": "sample_Choice"
   }
   ```

   **Response:**

   ```http
   HTTP/1.1 204 NoContent
   OData-Version: 4.0
   OData-EntityId: [Organization Uri]/api/data/v9.2/EntityDefinitions(LogicalName='sample_bankaccount')/Attributes(4a154e49-112a-ed11-9db1-00224804f8e2)
   ```

   **Console output:**

   ```
   Created Choice column with id:4a154e49-112a-ed11-9db1-00224804f8e2
   ```

1. Retrieve options of the choice column using `$select=SchemaName&$expand=OptionSet`.

   **Request:**

   ```http
   GET [Organization Uri]/api/data/v9.2/EntityDefinitions(LogicalName='sample_bankaccount')/Attributes(LogicalName='sample_choice')/Microsoft.Dynamics.CRM.PicklistAttributeMetadata?$select=SchemaName&$expand=OptionSet HTTP/1.1
   Consistency: Strong
   OData-MaxVersion: 4.0
   OData-Version: 4.0
   If-None-Match: null
   Accept: application/json
   ```

   **Response:**

   ```http
   HTTP/1.1 200 OK
   OData-Version: 4.0

   {
   "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#EntityDefinitions('sample_bankaccount')/Attributes/Microsoft.Dynamics.CRM.PicklistAttributeMetadata(SchemaName,OptionSet())/$entity",
   "SchemaName": "sample_Choice",
   "MetadataId": "4a154e49-112a-ed11-9db1-00224804f8e2",
   "OptionSet": {
      "MetadataId": "4b154e49-112a-ed11-9db1-00224804f8e2",
      "HasChanged": null,
      "IsCustomOptionSet": true,
      "IsGlobal": false,
      "IsManaged": false,
      "Name": "sample_bankaccount_sample_choice",
      "ExternalTypeName": null,
      "OptionSetType": "Picklist",
      "IntroducedVersion": "1.0.0.0",
      "ParentOptionSetName": null,
      "Description": {
         "LocalizedLabels": [
         {
            "Label": "Choice Attribute",
            "LanguageCode": 1033,
            "IsManaged": false,
            "MetadataId": "4d154e49-112a-ed11-9db1-00224804f8e2",
            "HasChanged": null
         }
         ],
         "UserLocalizedLabel": {
         "Label": "Choice Attribute",
         "LanguageCode": 1033,
         "IsManaged": false,
         "MetadataId": "4d154e49-112a-ed11-9db1-00224804f8e2",
         "HasChanged": null
         }
      },
      "DisplayName": {
         "LocalizedLabels": [
         {
            "Label": "Sample Choice",
            "LanguageCode": 1033,
            "IsManaged": false,
            "MetadataId": "4c154e49-112a-ed11-9db1-00224804f8e2",
            "HasChanged": null
         }
         ],
         "UserLocalizedLabel": {
         "Label": "Sample Choice",
         "LanguageCode": 1033,
         "IsManaged": false,
         "MetadataId": "4c154e49-112a-ed11-9db1-00224804f8e2",
         "HasChanged": null
         }
      },
      "IsCustomizable": {
         "Value": true,
         "CanBeChanged": true,
         "ManagedPropertyLogicalName": "iscustomizable"
      },
      "Options": [
         {
         "Value": 727000000,
         "Color": null,
         "IsManaged": false,
         "ExternalValue": "",
         "ParentValues": [],
         "MetadataId": null,
         "HasChanged": null,
         "Label": {
            "LocalizedLabels": [
               {
               "Label": "Bravo",
               "LanguageCode": 1033,
               "IsManaged": false,
               "MetadataId": "bc8d1815-75b7-4c13-b618-7959aaf4abb6",
               "HasChanged": null
               }
            ],
            "UserLocalizedLabel": {
               "Label": "Bravo",
               "LanguageCode": 1033,
               "IsManaged": false,
               "MetadataId": "bc8d1815-75b7-4c13-b618-7959aaf4abb6",
               "HasChanged": null
            }
         },
         "Description": {
            "LocalizedLabels": [],
            "UserLocalizedLabel": null
         }
         },
         {
         "Value": 727000001,
         "Color": null,
         "IsManaged": false,
         "ExternalValue": "",
         "ParentValues": [],
         "MetadataId": null,
         "HasChanged": null,
         "Label": {
            "LocalizedLabels": [
               {
               "Label": "Delta",
               "LanguageCode": 1033,
               "IsManaged": false,
               "MetadataId": "c3613791-85a0-41ac-8575-91aca4bb91e8",
               "HasChanged": null
               }
            ],
            "UserLocalizedLabel": {
               "Label": "Delta",
               "LanguageCode": 1033,
               "IsManaged": false,
               "MetadataId": "c3613791-85a0-41ac-8575-91aca4bb91e8",
               "HasChanged": null
            }
         },
         "Description": {
            "LocalizedLabels": [],
            "UserLocalizedLabel": null
         }
         },
         {
         "Value": 727000002,
         "Color": null,
         "IsManaged": false,
         "ExternalValue": "",
         "ParentValues": [],
         "MetadataId": null,
         "HasChanged": null,
         "Label": {
            "LocalizedLabels": [
               {
               "Label": "Alpha",
               "LanguageCode": 1033,
               "IsManaged": false,
               "MetadataId": "8db04562-9ec3-4014-a170-0482bbb94e44",
               "HasChanged": null
               }
            ],
            "UserLocalizedLabel": {
               "Label": "Alpha",
               "LanguageCode": 1033,
               "IsManaged": false,
               "MetadataId": "8db04562-9ec3-4014-a170-0482bbb94e44",
               "HasChanged": null
            }
         },
         "Description": {
            "LocalizedLabels": [],
            "UserLocalizedLabel": null
         }
         },
         {
         "Value": 727000003,
         "Color": null,
         "IsManaged": false,
         "ExternalValue": "",
         "ParentValues": [],
         "MetadataId": null,
         "HasChanged": null,
         "Label": {
            "LocalizedLabels": [
               {
               "Label": "Charlie",
               "LanguageCode": 1033,
               "IsManaged": false,
               "MetadataId": "d00dc11e-ed91-478b-ac78-86b6784326ad",
               "HasChanged": null
               }
            ],
            "UserLocalizedLabel": {
               "Label": "Charlie",
               "LanguageCode": 1033,
               "IsManaged": false,
               "MetadataId": "d00dc11e-ed91-478b-ac78-86b6784326ad",
               "HasChanged": null
            }
         },
         "Description": {
            "LocalizedLabels": [],
            "UserLocalizedLabel": null
         }
         },
         {
         "Value": 727000004,
         "Color": null,
         "IsManaged": false,
         "ExternalValue": "",
         "ParentValues": [],
         "MetadataId": null,
         "HasChanged": null,
         "Label": {
            "LocalizedLabels": [
               {
               "Label": "Foxtrot",
               "LanguageCode": 1033,
               "IsManaged": false,
               "MetadataId": "36a565b7-cd21-4505-812b-5567c28eec23",
               "HasChanged": null
               }
            ],
            "UserLocalizedLabel": {
               "Label": "Foxtrot",
               "LanguageCode": 1033,
               "IsManaged": false,
               "MetadataId": "36a565b7-cd21-4505-812b-5567c28eec23",
               "HasChanged": null
            }
         },
         "Description": {
            "LocalizedLabels": [],
            "UserLocalizedLabel": null
         }
         }
      ]
   }
   }
   ```
   **Console output:**

   ```
   Retrieved Choice column options:
        Value:727000000 Label:Bravo
        Value:727000001 Label:Delta
        Value:727000002 Label:Alpha
        Value:727000003 Label:Charlie
        Value:727000004 Label:Foxtrot
   ```

#### Add an option to the local optionset

1. Add an option to the choice column using the <xref:Microsoft.Dynamics.CRM.InsertOptionValue?text=InsertOptionValue Action>.
   
   > [!NOTE]
   > `InsertOptionValue` and the following actions to work with options has a `SolutionUniqueName` parameter for you to set the solution unique name rather than by using the `MSCRM.SolutionUniqueName` request header.

   **Request:**

   ```http
   POST [Organization Uri]/api/data/v9.2/InsertOptionValue HTTP/1.1
   OData-MaxVersion: 4.0
   OData-Version: 4.0
   If-None-Match: null
   Accept: application/json

   {
   "AttributeLogicalName": "sample_choice",
   "EntityLogicalName": "sample_bankaccount",
   "Value": 727000005,
   "Label": {
      "@odata.type": "Microsoft.Dynamics.CRM.Label",
      "LocalizedLabels": [
         {
         "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
         "Label": "Echo",
         "LanguageCode": 1033,
         "IsManaged": false
         }
      ],
      "UserLocalizedLabel": {
         "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
         "Label": "Echo",
         "LanguageCode": 1033,
         "IsManaged": false
      }
   },
   "SolutionUniqueName": "examplesolution"
   }
   ```

   **Response:**

   ```http
   HTTP/1.1 200 OK
   OData-Version: 4.0

   {
   "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.InsertOptionValueResponse",
   "NewOptionValue": 727000005
   }
   ```

   **Console output:**

   ```
   Added new option with label 'Echo'
   ```

1. Retrieve the choice column options again using the same query as before:

   **Console output:**

   ```
   The option values for the picklist:
         Value: 727000000, Label:Bravo
         Value: 727000001, Label:Delta
         Value: 727000002, Label:Alpha
         Value: 727000003, Label:Charlie
         Value: 727000004, Label:Foxtrot
         Value: 727000005, Label:Echo
   ```

#### Re-order choice column options

1. Re-order the Choice column options using the <xref:Microsoft.Dynamics.CRM.OrderOption?text=OrderOption Action>.

   **Request:**

   ```http
   POST [Organization Uri]/api/data/v9.2/OrderOption HTTP/1.1
   OData-MaxVersion: 4.0
   OData-Version: 4.0
   If-None-Match: null
   Accept: application/json

   {
   "EntityLogicalName": "sample_bankaccount",
   "AttributeLogicalName": "sample_choice",
   "Values": [
      727000002,
      727000000,
      727000003,
      727000001,
      727000005,
      727000004
   ],
   "SolutionUniqueName": "examplesolution"
   }
   ```

   **Response:**

   ```http
   HTTP/1.1 204 NoContent
   OData-Version: 4.0
   ```

   **Console output:**

   ```
   Options re-ordered.
   ```

1. Retrieve the Choice column options again using the same query as before to see the options in the new order.

   **Console output:**

   ```
   The option values for the picklist in the new order:
        Value: 727000002, Label:Alpha
        Value: 727000000, Label:Bravo
        Value: 727000003, Label:Charlie
        Value: 727000001, Label:Delta
        Value: 727000005, Label:Echo
        Value: 727000004, Label:Foxtrot
   ```

#### Delete local option value

1. Delete an option using <xref:Microsoft.Dynamics.CRM.DeleteOptionValue?text=DeleteOptionValue Action>.

   **Request:**

   ```http
   POST [Organization Uri]/api/data/v9.2/DeleteOptionValue HTTP/1.1
   OData-MaxVersion: 4.0
   OData-Version: 4.0
   If-None-Match: null
   Accept: application/json

   {
   "AttributeLogicalName": "sample_choice",
   "EntityLogicalName": "sample_bankaccount",
   "Value": 727000004
   }
   ```

   **Response:**

   ```http
   HTTP/1.1 204 NoContent
   OData-Version: 4.0
   ```

   **Console output:**

   ```
   Deleting a local option value...
   Local OptionSet option value deleted.
   ```

### Multi-Select Picklist Column

1. Create a multi-select choice column using <xref:Microsoft.Dynamics.CRM.MultiSelectPicklistAttributeMetadata?text=MultiSelectPicklistAttributeMetadata EntityType>.

   **Request:**

   ```http
   POST [Organization Uri]/api/data/v9.2/EntityDefinitions(LogicalName='sample_bankaccount')/Attributes HTTP/1.1
   MSCRM.SolutionUniqueName: examplesolution
   OData-MaxVersion: 4.0
   OData-Version: 4.0
   If-None-Match: null
   Accept: application/json

   {
   "@odata.type": "Microsoft.Dynamics.CRM.MultiSelectPicklistAttributeMetadata",
   "AttributeType": "Virtual",
   "AttributeTypeName": {
      "Value": "MultiSelectPicklistType"
   },
   "SourceTypeMask": 0,
   "OptionSet": {
      "@odata.type": "Microsoft.Dynamics.CRM.OptionSetMetadata",
      "Options": [
         {
         "Value": 727000000,
         "Label": {
            "@odata.type": "Microsoft.Dynamics.CRM.Label",
            "LocalizedLabels": [
               {
               "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
               "Label": "Appetizer",
               "LanguageCode": 1033,
               "IsManaged": false
               }
            ],
            "UserLocalizedLabel": {
               "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
               "Label": "Appetizer",
               "LanguageCode": 1033,
               "IsManaged": false
            }
         }
         },
         {
         "Value": 727000001,
         "Label": {
            "@odata.type": "Microsoft.Dynamics.CRM.Label",
            "LocalizedLabels": [
               {
               "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
               "Label": "Entree",
               "LanguageCode": 1033,
               "IsManaged": false
               }
            ],
            "UserLocalizedLabel": {
               "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
               "Label": "Entree",
               "LanguageCode": 1033,
               "IsManaged": false
            }
         }
         },
         {
         "Value": 727000002,
         "Label": {
            "@odata.type": "Microsoft.Dynamics.CRM.Label",
            "LocalizedLabels": [
               {
               "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
               "Label": "Dessert",
               "LanguageCode": 1033,
               "IsManaged": false
               }
            ],
            "UserLocalizedLabel": {
               "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
               "Label": "Dessert",
               "LanguageCode": 1033,
               "IsManaged": false
            }
         }
         }
      ],
      "IsGlobal": false,
      "OptionSetType": "Picklist"
   },
   "Description": {
      "@odata.type": "Microsoft.Dynamics.CRM.Label",
      "LocalizedLabels": [
         {
         "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
         "Label": "MultiSelect Choice Attribute",
         "LanguageCode": 1033,
         "IsManaged": false
         }
      ],
      "UserLocalizedLabel": {
         "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
         "Label": "MultiSelect Choice Attribute",
         "LanguageCode": 1033,
         "IsManaged": false
      }
   },
   "DisplayName": {
      "@odata.type": "Microsoft.Dynamics.CRM.Label",
      "LocalizedLabels": [
         {
         "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
         "Label": "Sample MultiSelect Choice",
         "LanguageCode": 1033,
         "IsManaged": false
         }
      ],
      "UserLocalizedLabel": {
         "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
         "Label": "Sample MultiSelect Choice",
         "LanguageCode": 1033,
         "IsManaged": false
      }
   },
   "RequiredLevel": {
      "Value": "None",
      "CanBeChanged": false,
      "ManagedPropertyLogicalName": "canmodifyrequirementlevelsettings"
   },
   "SchemaName": "sample_MultiSelectChoice"
   }
   ```

   **Response:**

   ```http
   HTTP/1.1 204 NoContent
   OData-Version: 4.0
   OData-EntityId: [Organization Uri]/api/data/v9.2/EntityDefinitions(LogicalName='sample_bankaccount')/Attributes(2c1c3050-112a-ed11-9db1-00224804f8e2)
   ```

   **Console output:**

   ```
   Creating a MultiSelect Choice column...
   Created MultiSelect Choice column with id:2c1c3050-112a-ed11-9db1-00224804f8e2
   ```

1. Retrieve the multi-select choice column options using `GET EntityDefinitions(LogicalName='sample_bankaccount')/Attributes(LogicalName='sample_multiselectchoice')/Microsoft.Dynamics.CRM.MultiSelectPicklistAttributeMetadata?$select=SchemaName&$expand=OptionSet`

   **Console output:**

   ```
   The option values for the multi-select choice column:
         Value: 727000000, Label:Appetizer
         Value: 727000001, Label:Entree
         Value: 727000002, Label:Dessert
   ```

### Insert Status Value

Use <xref:Microsoft.Dynamics.CRM.InsertStatusValue?text=InsertStatusValue Action> to add a new option to a `statuscode` column. You must specify which `StateCode` it's valid for.

> [!NOTE]
> Notice that the value returned applies the publisher `customizationoptionvalueprefix` value (72700) automatically.

**Request:**

```http
POST [Organization Uri]/api/data/v9.2/InsertStatusValue HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json

{
  "AttributeLogicalName": "statuscode",
  "EntityLogicalName": "sample_bankaccount",
  "Label": {
    "@odata.type": "Microsoft.Dynamics.CRM.Label",
    "LocalizedLabels": [
      {
        "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
        "Label": "Frozen",
        "LanguageCode": 1033,
        "IsManaged": false
      }
    ],
    "UserLocalizedLabel": {
      "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
      "Label": "Frozen",
      "LanguageCode": 1033,
      "IsManaged": false
    }
  },
  "StateCode": 1,
  "SolutionUniqueName": "examplesolution"
}
```

**Response:**

```http
HTTP/1.1 200 OK
OData-Version: 4.0

{
  "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.InsertStatusValueResponse",
  "NewOptionValue": 727000000
}
```


**Console output:**

```
Created new Status value:727000000
```

## Section 3: Create and use Global OptionSet

1. Create a global choice (optionset). This optionset is named `sample_colors` and contains options for Red, Yellow, and Green.
   
   > [!NOTE]
   > The request specifies the option values using the publisher `customizationoptionvalueprefix`.

   **Request:**

   ```http
   POST [Organization Uri]/api/data/v9.2/GlobalOptionSetDefinitions HTTP/1.1
   MSCRM.SolutionUniqueName: examplesolution
   OData-MaxVersion: 4.0
   OData-Version: 4.0
   If-None-Match: null
   Accept: application/json

   {
   "@odata.type": "Microsoft.Dynamics.CRM.OptionSetMetadata",
   "Options": [
      {
         "Value": 727000000,
         "Label": {
         "@odata.type": "Microsoft.Dynamics.CRM.Label",
         "LocalizedLabels": [
            {
               "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
               "Label": "Red",
               "LanguageCode": 1033,
               "IsManaged": false
            }
         ],
         "UserLocalizedLabel": {
            "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
            "Label": "Red",
            "LanguageCode": 1033,
            "IsManaged": false
         }
         }
      },
      {
         "Value": 727000001,
         "Label": {
         "@odata.type": "Microsoft.Dynamics.CRM.Label",
         "LocalizedLabels": [
            {
               "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
               "Label": "Yellow",
               "LanguageCode": 1033,
               "IsManaged": false
            }
         ],
         "UserLocalizedLabel": {
            "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
            "Label": "Yellow",
            "LanguageCode": 1033,
            "IsManaged": false
         }
         }
      },
      {
         "Value": 727000002,
         "Label": {
         "@odata.type": "Microsoft.Dynamics.CRM.Label",
         "LocalizedLabels": [
            {
               "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
               "Label": "Green",
               "LanguageCode": 1033,
               "IsManaged": false
            }
         ],
         "UserLocalizedLabel": {
            "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
            "Label": "Green",
            "LanguageCode": 1033,
            "IsManaged": false
         }
         }
      }
   ],
   "Description": {
      "@odata.type": "Microsoft.Dynamics.CRM.Label",
      "LocalizedLabels": [
         {
         "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
         "Label": "Color Choice",
         "LanguageCode": 1033,
         "IsManaged": false
         }
      ],
      "UserLocalizedLabel": {
         "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
         "Label": "Color Choice",
         "LanguageCode": 1033,
         "IsManaged": false
      }
   },
   "DisplayName": {
      "@odata.type": "Microsoft.Dynamics.CRM.Label",
      "LocalizedLabels": [
         {
         "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
         "Label": "Colors",
         "LanguageCode": 1033,
         "IsManaged": false
         }
      ],
      "UserLocalizedLabel": {
         "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
         "Label": "Colors",
         "LanguageCode": 1033,
         "IsManaged": false
      }
   },
   "Name": "sample_colors",
   "OptionSetType": "Picklist"
   }
   ```

   **Response:**

   ```http
   HTTP/1.1 204 NoContent
   OData-Version: 4.0
   OData-EntityId: [Organization Uri]/api/data/v9.2/GlobalOptionSetDefinitions(7cfd8c56-112a-ed11-9db1-00224804f8e2)
   ```

   **Console output:**

   ```
   Created a new global option set with id:7cfd8c56-112a-ed11-9db1-00224804f8e2
   ```

1. Retrieve the global choice options.

   **Request:**

   ```http
   GET [Organization Uri]/api/data/v9.2/GlobalOptionSetDefinitions(7cfd8c56-112a-ed11-9db1-00224804f8e2)/Microsoft.Dynamics.CRM.OptionSetMetadata HTTP/1.1
   Consistency: Strong
   OData-MaxVersion: 4.0
   OData-Version: 4.0
   If-None-Match: null
   Accept: application/json
   ```

   **Response:**

   ```http
   HTTP/1.1 200 OK
   OData-Version: 4.0

   {
   "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#GlobalOptionSetDefinitions/Microsoft.Dynamics.CRM.OptionSetMetadata/$entity",
   "ParentOptionSetName": null,
   "IsCustomOptionSet": true,
   "IsGlobal": true,
   "IsManaged": false,
   "Name": "sample_colors",
   "ExternalTypeName": null,
   "OptionSetType": "Picklist",
   "IntroducedVersion": "1.0.0.0",
   "MetadataId": "7cfd8c56-112a-ed11-9db1-00224804f8e2",
   "HasChanged": null,
   "Options": [
      {
         "Value": 727000000,
         "Color": null,
         "IsManaged": false,
         "ExternalValue": "",
         "ParentValues": [],
         "MetadataId": null,
         "HasChanged": null,
         "Label": {
         "LocalizedLabels": [
            {
               "Label": "Red",
               "LanguageCode": 1033,
               "IsManaged": false,
               "MetadataId": "2c1fa94f-3714-4615-995b-690158d0d989",
               "HasChanged": null
            }
         ],
         "UserLocalizedLabel": {
            "Label": "Red",
            "LanguageCode": 1033,
            "IsManaged": false,
            "MetadataId": "2c1fa94f-3714-4615-995b-690158d0d989",
            "HasChanged": null
         }
         },
         "Description": {
         "LocalizedLabels": [],
         "UserLocalizedLabel": null
         }
      },
      {
         "Value": 727000001,
         "Color": null,
         "IsManaged": false,
         "ExternalValue": "",
         "ParentValues": [],
         "MetadataId": null,
         "HasChanged": null,
         "Label": {
         "LocalizedLabels": [
            {
               "Label": "Yellow",
               "LanguageCode": 1033,
               "IsManaged": false,
               "MetadataId": "a499c2fe-c13a-4c1e-b190-db8ae74396f5",
               "HasChanged": null
            }
         ],
         "UserLocalizedLabel": {
            "Label": "Yellow",
            "LanguageCode": 1033,
            "IsManaged": false,
            "MetadataId": "a499c2fe-c13a-4c1e-b190-db8ae74396f5",
            "HasChanged": null
         }
         },
         "Description": {
         "LocalizedLabels": [],
         "UserLocalizedLabel": null
         }
      },
      {
         "Value": 727000002,
         "Color": null,
         "IsManaged": false,
         "ExternalValue": "",
         "ParentValues": [],
         "MetadataId": null,
         "HasChanged": null,
         "Label": {
         "LocalizedLabels": [
            {
               "Label": "Green",
               "LanguageCode": 1033,
               "IsManaged": false,
               "MetadataId": "8378af2c-4b68-4ea4-ad37-e676f696e1ba",
               "HasChanged": null
            }
         ],
         "UserLocalizedLabel": {
            "Label": "Green",
            "LanguageCode": 1033,
            "IsManaged": false,
            "MetadataId": "8378af2c-4b68-4ea4-ad37-e676f696e1ba",
            "HasChanged": null
         }
         },
         "Description": {
         "LocalizedLabels": [],
         "UserLocalizedLabel": null
         }
      }
   ],
   "Description": {
      "LocalizedLabels": [
         {
         "Label": "Color Choice",
         "LanguageCode": 1033,
         "IsManaged": false,
         "MetadataId": "7efd8c56-112a-ed11-9db1-00224804f8e2",
         "HasChanged": null
         }
      ],
      "UserLocalizedLabel": {
         "Label": "Color Choice",
         "LanguageCode": 1033,
         "IsManaged": false,
         "MetadataId": "7efd8c56-112a-ed11-9db1-00224804f8e2",
         "HasChanged": null
      }
   },
   "DisplayName": {
      "LocalizedLabels": [
         {
         "Label": "Colors",
         "LanguageCode": 1033,
         "IsManaged": false,
         "MetadataId": "7dfd8c56-112a-ed11-9db1-00224804f8e2",
         "HasChanged": null
         }
      ],
      "UserLocalizedLabel": {
         "Label": "Colors",
         "LanguageCode": 1033,
         "IsManaged": false,
         "MetadataId": "7dfd8c56-112a-ed11-9db1-00224804f8e2",
         "HasChanged": null
      }
   },
   "IsCustomizable": {
      "Value": true,
      "CanBeChanged": true,
      "ManagedPropertyLogicalName": "iscustomizable"
   }
   }
   ```

   **Console output:**

   ```
   List the retrieved options for the colors global option set:
   Value: 727000000 Label:Red
   Value: 727000001 Label:Yellow
   Value: 727000002 Label:Green
   ```

1. Create a choice column that uses the global optionset. Associate the column definition to the global optionset using: `"GlobalOptionSet@odata.bind": "/GlobalOptionSetDefinitions(7cfd8c56-112a-ed11-9db1-00224804f8e2)"`.

   **Request:**

   ```http
   POST [Organization Uri]/api/data/v9.2/EntityDefinitions(LogicalName='sample_bankaccount')/Attributes HTTP/1.1
   MSCRM.SolutionUniqueName: examplesolution
   OData-MaxVersion: 4.0
   OData-Version: 4.0
   If-None-Match: null
   Accept: application/json

   {
   "@odata.type": "Microsoft.Dynamics.CRM.PicklistAttributeMetadata",
   "AttributeType": "Picklist",
   "AttributeTypeName": {
      "Value": "PicklistType"
   },
   "SourceTypeMask": 0,
   "GlobalOptionSet@odata.bind": "/GlobalOptionSetDefinitions(7cfd8c56-112a-ed11-9db1-00224804f8e2)",
   "Description": {
      "@odata.type": "Microsoft.Dynamics.CRM.Label",
      "LocalizedLabels": [
         {
         "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
         "Label": "Colors Global Picklist Attribute",
         "LanguageCode": 1033,
         "IsManaged": false
         }
      ],
      "UserLocalizedLabel": {
         "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
         "Label": "Colors Global Picklist Attribute",
         "LanguageCode": 1033,
         "IsManaged": false
      }
   },
   "DisplayName": {
      "@odata.type": "Microsoft.Dynamics.CRM.Label",
      "LocalizedLabels": [
         {
         "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
         "Label": "Sample Colors",
         "LanguageCode": 1033,
         "IsManaged": false
         }
      ],
      "UserLocalizedLabel": {
         "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
         "Label": "Sample Colors",
         "LanguageCode": 1033,
         "IsManaged": false
      }
   },
   "RequiredLevel": {
      "Value": "None",
      "CanBeChanged": false,
      "ManagedPropertyLogicalName": "canmodifyrequirementlevelsettings"
   },
   "SchemaName": "sample_Colors"
   }
   ```

   **Response:**

   ```http
   HTTP/1.1 204 NoContent
   OData-Version: 4.0
   OData-EntityId: [Organization Uri]/api/data/v9.2/EntityDefinitions(LogicalName='sample_bankaccount')/Attributes(81fd8c56-112a-ed11-9db1-00224804f8e2)
   ```

   **Console output:**

   ```
   Created Choice column with id:81fd8c56-112a-ed11-9db1-00224804f8e2 using colors global optionset.
   ```

## Section 4: Create Customer Relationship

1. Use the <xref:Microsoft.Dynamics.CRM.CreateCustomerRelationships?text=CreateCustomerRelationships Action> to create a customer relationship. This action adds a lookup column for the `sample_BankAccount` table that allows for either an `account` or `contact` record to be set.

   `CreateCustomerRelationships` has a `Lookup` <xref:Microsoft.Dynamics.CRM.ComplexLookupAttributeMetadata?text=ComplexLookupAttributeMetadata ComplexType> parameter and a `OneToManyRelationships` parameter containing a pair of relationships defined using <xref:Microsoft.Dynamics.CRM.ComplexOneToManyRelationshipMetadata?text=ComplexOneToManyRelationshipMetadata ComplexType>.

   **Request:**

   ```http
   POST [Organization Uri]/api/data/v9.2/CreateCustomerRelationships HTTP/1.1
   OData-MaxVersion: 4.0
   OData-Version: 4.0
   If-None-Match: null
   Accept: application/json

   {
   "Lookup": {
      "@odata.type": "Microsoft.Dynamics.CRM.ComplexLookupAttributeMetadata",
      "AttributeType": "Lookup",
      "AttributeTypeName": {
         "Value": "LookupType"
      },
      "Format": "None",      
      "Targets": [
         "account",
         "contact"
      ],
      "ColumnNumber": 0,
      "Description": {
         "@odata.type": "Microsoft.Dynamics.CRM.Label",
         "LocalizedLabels": [
         {
            "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
            "Label": "The owner of the bank account",
            "LanguageCode": 1033,
            "IsManaged": false
         }
         ],
         "UserLocalizedLabel": {
         "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
         "Label": "The owner of the bank account",
         "LanguageCode": 1033,
         "IsManaged": false
         }
      },
      "DisplayName": {
         "@odata.type": "Microsoft.Dynamics.CRM.Label",
         "LocalizedLabels": [
         {
            "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
            "Label": "Bank Account owner",
            "LanguageCode": 1033,
            "IsManaged": false
         }
         ],
         "UserLocalizedLabel": {
         "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
         "Label": "Bank Account owner",
         "LanguageCode": 1033,
         "IsManaged": false
         }
      },
      "RequiredLevel": {
         "Value": "ApplicationRequired",
         "CanBeChanged": false,
         "ManagedPropertyLogicalName": "canmodifyrequirementlevelsettings"
      },
      "SchemaName": "sample_CustomerId",
      "SourceType": 0
   },
   "OneToManyRelationships": [
      {
         "@odata.type": "Microsoft.Dynamics.CRM.ComplexOneToManyRelationshipMetadata",
         "ReferencedEntity": "account",
         "ReferencingEntity": "sample_bankaccount",
         "RelationshipBehavior": 0,
         "RelationshipType": "OneToManyRelationship",
         "SchemaName": "sample_BankAccount_Customer_Account",
         "SecurityTypes": "None"
      },
      {
         "@odata.type": "Microsoft.Dynamics.CRM.ComplexOneToManyRelationshipMetadata",
         "ReferencedEntity": "contact",
         "ReferencingEntity": "sample_bankaccount",
         "RelationshipBehavior": 0,
         "RelationshipType": "OneToManyRelationship",
         "SchemaName": "sample_BankAccount_Customer_Contact",
         "SecurityTypes": "None"
      }
   ],
   "SolutionUniqueName": "examplesolution"
   }
   ```

   **Response:**

   ```http
   HTTP/1.1 200 OK
   OData-Version: 4.0

   {
   "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.CreateCustomerRelationshipsResponse",
   "RelationshipIds": [
      "84fd8c56-112a-ed11-9db1-00224804f8e2",
      "8dfd8c56-112a-ed11-9db1-00224804f8e2"
   ],
   "AttributeId": "59478264-16af-4bcc-8baa-b154df0d6767"
   }
   ```

1. Use the <xref:Microsoft.Dynamics.CRM.CreateCustomerRelationshipsResponse>.`AttributeId` value to retrieve the lookup column `Targets` property for the customer relationship.

   **Request:**

   ```http
   GET [Organization Uri]/api/data/v9.2/EntityDefinitions(LogicalName='sample_bankaccount')/Attributes(LogicalName='sample_customerid')/Microsoft.Dynamics.CRM.LookupAttributeMetadata?$select=Targets HTTP/1.1
   Consistency: Strong
   OData-MaxVersion: 4.0
   OData-Version: 4.0
   If-None-Match: null
   Accept: application/json
   ```

   **Response:**

   ```http
   HTTP/1.1 200 OK
   OData-Version: 4.0

   {
   "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#EntityDefinitions('sample_bankaccount')/Attributes/Microsoft.Dynamics.CRM.LookupAttributeMetadata(Targets)/$entity",
   "Targets": [
      "account",
      "contact"
   ],
   "MetadataId": "59478264-16af-4bcc-8baa-b154df0d6767"
   }
   ```

   **Console output:**

   ```
   The Target values of the Lookup column created:
         account
         contact
   ```

1. Use the <xref:Microsoft.Dynamics.CRM.CreateCustomerRelationshipsResponse>.`RelationshipIds` values to retrieve the relationships for the customer column.

   First for the relationship to `account`:

   **Request:**

   ```http
   GET [Organization Uri]/api/data/v9.2/RelationshipDefinitions(84fd8c56-112a-ed11-9db1-00224804f8e2)/Microsoft.Dynamics.CRM.OneToManyRelationshipMetadata HTTP/1.1
   Consistency: Strong
   OData-MaxVersion: 4.0
   OData-Version: 4.0
   If-None-Match: null
   Accept: application/json
   ```

   **Response:**

   ```http
   HTTP/1.1 200 OK
   OData-Version: 4.0

   {
   "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#RelationshipDefinitions/Microsoft.Dynamics.CRM.OneToManyRelationshipMetadata/$entity",
   "ReferencedAttribute": "accountid",
   "ReferencedEntity": "account",
   "ReferencingAttribute": "sample_customerid",
   "ReferencingEntity": "sample_bankaccount",
   "IsHierarchical": false,
   "EntityKey": null,
   "IsRelationshipAttributeDenormalized": false,
   "ReferencedEntityNavigationPropertyName": "sample_BankAccount_Customer_Account",
   "ReferencingEntityNavigationPropertyName": "sample_CustomerId_account",
   "RelationshipBehavior": 1,
   "IsDenormalizedLookup": null,
   "DenormalizedAttributeName": null,
   "IsCustomRelationship": true,
   "IsValidForAdvancedFind": true,
   "SchemaName": "sample_BankAccount_Customer_Account",
   "SecurityTypes": "Append",
   "IsManaged": false,
   "RelationshipType": "OneToManyRelationship",
   "IntroducedVersion": "1.0.0.0",
   "MetadataId": "84fd8c56-112a-ed11-9db1-00224804f8e2",
   "HasChanged": null,
   "AssociatedMenuConfiguration": {
      "Behavior": "UseCollectionName",
      "Group": "Details",
      "Order": 10000,
      "IsCustomizable": true,
      "Icon": null,
      "ViewId": "00000000-0000-0000-0000-000000000000",
      "AvailableOffline": true,
      "MenuId": null,
      "QueryApi": null,
      "Label": {
         "LocalizedLabels": [],
         "UserLocalizedLabel": null
      }
   },
   "CascadeConfiguration": {
      "Assign": "NoCascade",
      "Delete": "RemoveLink",
      "Archive": "RemoveLink",
      "Merge": "Cascade",
      "Reparent": "NoCascade",
      "Share": "NoCascade",
      "Unshare": "NoCascade",
      "RollupView": "NoCascade"
   },
   "RelationshipAttributes": [],
   "IsCustomizable": {
      "Value": true,
      "CanBeChanged": true,
      "ManagedPropertyLogicalName": "iscustomizable"
   }
   }
   ```

   Then for the relationship to `contact`:

   **Request:**

   ```http
   GET [Organization Uri]/api/data/v9.2/RelationshipDefinitions(8dfd8c56-112a-ed11-9db1-00224804f8e2)/Microsoft.Dynamics.CRM.OneToManyRelationshipMetadata HTTP/1.1
   Consistency: Strong
   OData-MaxVersion: 4.0
   OData-Version: 4.0
   If-None-Match: null
   Accept: application/json
   ```

   **Response:**

   ```http
   HTTP/1.1 200 OK
   OData-Version: 4.0

   {
   "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#RelationshipDefinitions/Microsoft.Dynamics.CRM.OneToManyRelationshipMetadata/$entity",
   "ReferencedAttribute": "contactid",
   "ReferencedEntity": "contact",
   "ReferencingAttribute": "sample_customerid",
   "ReferencingEntity": "sample_bankaccount",
   "IsHierarchical": false,
   "EntityKey": null,
   "IsRelationshipAttributeDenormalized": false,
   "ReferencedEntityNavigationPropertyName": "sample_BankAccount_Customer_Contact",
   "ReferencingEntityNavigationPropertyName": "sample_CustomerId_contact",
   "RelationshipBehavior": 1,
   "IsDenormalizedLookup": null,
   "DenormalizedAttributeName": null,
   "IsCustomRelationship": true,
   "IsValidForAdvancedFind": true,
   "SchemaName": "sample_BankAccount_Customer_Contact",
   "SecurityTypes": "Append",
   "IsManaged": false,
   "RelationshipType": "OneToManyRelationship",
   "IntroducedVersion": "1.0.0.0",
   "MetadataId": "8dfd8c56-112a-ed11-9db1-00224804f8e2",
   "HasChanged": null,
   "AssociatedMenuConfiguration": {
      "Behavior": "UseCollectionName",
      "Group": "Details",
      "Order": 10000,
      "IsCustomizable": true,
      "Icon": null,
      "ViewId": "00000000-0000-0000-0000-000000000000",
      "AvailableOffline": true,
      "MenuId": null,
      "QueryApi": null,
      "Label": {
         "LocalizedLabels": [],
         "UserLocalizedLabel": null
      }
   },
   "CascadeConfiguration": {
      "Assign": "NoCascade",
      "Delete": "RemoveLink",
      "Archive": "RemoveLink",
      "Merge": "Cascade",
      "Reparent": "NoCascade",
      "Share": "NoCascade",
      "Unshare": "NoCascade",
      "RollupView": "NoCascade"
   },
   "RelationshipAttributes": [],
   "IsCustomizable": {
      "Value": true,
      "CanBeChanged": true,
      "ManagedPropertyLogicalName": "iscustomizable"
   }
   }
   ```

   **Console output:**

   ```
   The Schema Names of the relationships created:
         sample_BankAccount_Customer_Account
         sample_BankAccount_Customer_Contact
   ```

## Section 5: Create and retrieve a one-to-many relationship

Before you create a relationship using code, you should confirm that the relationship is valid. The designers in [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) use special functions to show you which combinations are valid. You can use the same functions in your code to detect whether a particular relationship can be created or not.

### Validate 1:N relationship eligibility

1. <xref:Microsoft.Dynamics.CRM.CanBeReferenced?text=CanBeReferenced Function> tells you whether a table the primary table (one) in a one-to-many relationship.

   **Request:**

   ```http
   POST [Organization Uri]/api/data/v9.2/CanBeReferenced HTTP/1.1
   OData-MaxVersion: 4.0
   OData-Version: 4.0
   If-None-Match: null
   Accept: application/json

   {
   "EntityName": "sample_bankaccount"
   }
   ```

   **Response:**

   ```http
   HTTP/1.1 200 OK
   OData-Version: 4.0

   {
   "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.CanBeReferencedResponse",
   "CanBeReferenced": true
   }
   ```

   **Console output:**

   ```
   The sample_BankAccount table is eligible to be a primary table in a one-to-many relationship.
   ```

1. <xref:Microsoft.Dynamics.CRM.CanBeReferencing?text=CanBeReferencing Function> tells you whether a table can be the referencing table in a one-to-many relationship. The referencing table is the table that has a Lookup column added to it to be the 'many' in the one-to-many relationship.

   **Request:**

   ```http
   POST [Organization Uri]/api/data/v9.2/CanBeReferencing HTTP/1.1
   OData-MaxVersion: 4.0
   OData-Version: 4.0
   If-None-Match: null
   Accept: application/json

   {
   "EntityName": "contact"
   }
   ```

   **Response:**

   ```http
   HTTP/1.1 200 OK
   OData-Version: 4.0

   {
   "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.CanBeReferencingResponse",
   "CanBeReferencing": true
   }
   ```

   **Console output:**

   ```
   The contact table is eligible to be a related table in a one-to-many relationship.
   ```

### Identify Potential Referencing Entities

In the context of a specific table that can be the parmary table in a one-to-many relationship, use the <xref:Microsoft.Dynamics.CRM.GetValidReferencingEntities?text=GetValidReferencingEntities Function> to identify what other tables can be the related to it.

**Request:**

```http
GET [Organization Uri]/api/data/v9.2/GetValidReferencingEntities(ReferencedEntityName='sample_bankaccount') HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
```

**Response:**

```http
HTTP/1.1 200 OK
OData-Version: 4.0

{
  "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.GetValidReferencingEntitiesResponse",
  "EntityNames": [
    "msdyn_slakpi",
    "workflowbinary",
    "apisettings",
    "flowsession",
    "knowledgearticle",
    "socialprofile",
    "goal",
    "metric",
    "goalrollupquery",
    "mailbox",
    "position",
    "channelaccessprofile",
    "externalparty",
    "channelaccessprofilerule",
    "channelaccessprofileruleitem",
    "sample_bankaccount",
    "privilegesremovalsetting",
    "knowledgebaserecord",
    "msdyn_insightsstorevirtualentity",
    "aaduser",
    "sharepointdocument",
    "msfp_unsubscribedrecipient",
    "msdyn_dataflow",
    "flowmachineimage",
    "queueitem",
    "appointment",
    "msdyn_federatedarticleincident",
    "msfp_surveyresponse",
    "msdyn_dataflowrefreshhistory",
    "mailmergetemplate",
    "contact",
    "organizationdatasyncstate",
    "bot",
    "knowledgearticleviews",
    "slaitem",
    "msfp_question",
    "category",
    "connection",
    "newprocess",
    "msfp_survey",
    "emailserverprofile",
    "appnotification",
    "feedback",
    "activityfileattachment",
    "organizationdatasyncsubscriptionentity",
    "msdyn_nonrelationalds",
    "expiredprocess",
    "msfp_surveyinvite",
    "msfp_alert",
    "businessunit",
    "msfp_alertrule",
    "slakpiinstance",
    "email",
    "datasyncstate",
    "msdyn_entityrefreshhistory",
    "msdyn_componentlayerdatasource",
    "account",
    "kbarticle",
    "systemuser",
    "task",
    "letter",
    "reportcategory",
    "phonecall",
    "actioncard",
    "msdyn_kmfederatedsearchconfig",
    "featurecontrolsetting",
    "translationprocess",
    "recurringappointmentmaster",
    "externalpartyitem",
    "msdyn_aibdatasetfile",
    "socialactivity",
    "flowmachineimageversion",
    "fax",
    "msdyn_kbattachment",
    "serviceplanmapping",
    "msdyn_knowledgearticletemplate",
    "msfp_emailtemplate",
    "conversationtranscript",
    "sharepointsite",
    "processstage",
    "msfp_localizedemailtemplate",
    "queue",
    "msdyn_richtextfile",
    "msdyn_serviceconfiguration",
    "team",
    "sharedlinksetting",
    "territory",
    "msdyn_federatedarticle",
    "msdyn_knowledgepersonalfilter",
    "sharepointdocumentlocation",
    "chat",
    "msfp_fileresponse",
    "msfp_satisfactionmetric",
    "msdyn_aibfeedbackloop",
    "msdyn_customcontrolextendedsettings",
    "msfp_surveyreminder",
    "msfp_questionresponse",
    "msfp_project"
  ]
}
```

**Console output:**

```
The contact table is in the list of potential referencing entities for sample_BankAccount.
```

### Create 1:N relationship

The following request creates a one-to-many relationship between `sample_BankAccount` and contact tables with a lookup column added to the `contact` table.

**Request:**

```http
POST [Organization Uri]/api/data/v9.2/RelationshipDefinitions HTTP/1.1
MSCRM.SolutionUniqueName: examplesolution
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json

{
  "@odata.type": "Microsoft.Dynamics.CRM.OneToManyRelationshipMetadata",
  "AssociatedMenuConfiguration": {
    "Behavior": "UseLabel",
    "Group": "Details",
    "Label": {
      "@odata.type": "Microsoft.Dynamics.CRM.Label",
      "LocalizedLabels": [
        {
          "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
          "Label": "Cardholders",
          "LanguageCode": 1033,
          "IsManaged": false
        }
      ],
      "UserLocalizedLabel": {
        "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
        "Label": "Cardholders",
        "LanguageCode": 1033,
        "IsManaged": false
      }
    },
    "Order": 10000,
    "ViewId": "00000000-0000-0000-0000-000000000000"
  },
  "CascadeConfiguration": {
    "Assign": "NoCascade",
    "Delete": "RemoveLink",
    "Merge": "Cascade",
    "Reparent": "NoCascade",
    "Share": "NoCascade",
    "Unshare": "NoCascade",
    "RollupView": "NoCascade"
  },
  "IsHierarchical": false,
  "ReferencedAttribute": "sample_bankaccountid",
  "ReferencedEntity": "sample_bankaccount",
  "ReferencingEntity": "contact",
  "Lookup": {
    "@odata.type": "Microsoft.Dynamics.CRM.LookupAttributeMetadata",
    "AttributeType": "Lookup",
    "AttributeTypeName": {
      "Value": "LookupType"
    },
    "Format": "None",
    "Description": {
      "@odata.type": "Microsoft.Dynamics.CRM.Label",
      "LocalizedLabels": [
        {
          "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
          "Label": "The bank account this contact has access to.",
          "LanguageCode": 1033,
          "IsManaged": false
        }
      ],
      "UserLocalizedLabel": {
        "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
        "Label": "The bank account this contact has access to.",
        "LanguageCode": 1033,
        "IsManaged": false
      }
    },
    "DisplayName": {
      "@odata.type": "Microsoft.Dynamics.CRM.Label",
      "LocalizedLabels": [
        {
          "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
          "Label": "Bank Account",
          "LanguageCode": 1033,
          "IsManaged": false
        }
      ],
      "UserLocalizedLabel": {
        "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
        "Label": "Bank Account",
        "LanguageCode": 1033,
        "IsManaged": false
      }
    },
    "SchemaName": "sample_BankAccountId"
  },
  "IsCustomRelationship": false,
  "IsManaged": false,
  "IsValidForAdvancedFind": false,
  "RelationshipType": "OneToManyRelationship",
  "SchemaName": "sample_BankAccount_Contacts",
  "SecurityTypes": "None"
}
```

**Response:**

```http
HTTP/1.1 204 NoContent
OData-Version: 4.0
OData-EntityId: [Organization Uri]/api/data/v9.2/RelationshipDefinitions(991efd5f-112a-ed11-9db1-00224804f8e2)
```



**Console output:**

```
Creating a one-to-many relationship...
Created one-to-many relationship: RelationshipDefinitions(991efd5f-112a-ed11-9db1-00224804f8e2)
```

### Retrieve 1:N relationship

The following request retrieves the relationship created by the previous request.

> [!NOTE]
> Because `RelationshipDefinitions` contains both one-to-many and many-to-many relationship definitions, you must include the following in the URL to cast to the type you want to retrieve: `/Microsoft.Dynamics.CRM.OneToManyRelationshipMetadata`.
> Otherwise, the value returned will be the <xref:Microsoft.Dynamics.CRM.RelationshipMetadataBase?text=RelationshipMetadataBase EntityType> and will not include the properties specific to the <xref:Microsoft.Dynamics.CRM.OneToManyRelationshipMetadata?text=OneToManyRelationshipMetadata EntityType>.

**Request:**

```http
GET [Organization Uri]/api/data/v9.2/RelationshipDefinitions(991efd5f-112a-ed11-9db1-00224804f8e2)/Microsoft.Dynamics.CRM.OneToManyRelationshipMetadata HTTP/1.1
Consistency: Strong
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
```

**Response:**

```http
HTTP/1.1 200 OK
OData-Version: 4.0

{
  "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#RelationshipDefinitions/Microsoft.Dynamics.CRM.OneToManyRelationshipMetadata/$entity",
  "ReferencedAttribute": "sample_bankaccountid",
  "ReferencedEntity": "sample_bankaccount",
  "ReferencingAttribute": "sample_bankaccountid",
  "ReferencingEntity": "contact",
  "IsHierarchical": false,
  "EntityKey": null,
  "IsRelationshipAttributeDenormalized": false,
  "ReferencedEntityNavigationPropertyName": "sample_BankAccount_Contacts",
  "ReferencingEntityNavigationPropertyName": "sample_BankAccountId",
  "RelationshipBehavior": 1,
  "IsDenormalizedLookup": null,
  "DenormalizedAttributeName": null,
  "IsCustomRelationship": true,
  "IsValidForAdvancedFind": false,
  "SchemaName": "sample_BankAccount_Contacts",
  "SecurityTypes": "Append",
  "IsManaged": false,
  "RelationshipType": "OneToManyRelationship",
  "IntroducedVersion": "1.0.0.0",
  "MetadataId": "991efd5f-112a-ed11-9db1-00224804f8e2",
  "HasChanged": null,
  "AssociatedMenuConfiguration": {
    "Behavior": "UseLabel",
    "Group": "Details",
    "Order": 10000,
    "IsCustomizable": true,
    "Icon": null,
    "ViewId": "00000000-0000-0000-0000-000000000000",
    "AvailableOffline": true,
    "MenuId": null,
    "QueryApi": null,
    "Label": {
      "LocalizedLabels": [
        {
          "Label": "Cardholders",
          "LanguageCode": 1033,
          "IsManaged": false,
          "MetadataId": "a99a420f-6778-4f2f-b42b-64bc84b2c2d2",
          "HasChanged": null
        }
      ],
      "UserLocalizedLabel": {
        "Label": "Cardholders",
        "LanguageCode": 1033,
        "IsManaged": false,
        "MetadataId": "a99a420f-6778-4f2f-b42b-64bc84b2c2d2",
        "HasChanged": null
      }
    }
  },
  "CascadeConfiguration": {
    "Assign": "NoCascade",
    "Delete": "RemoveLink",
    "Archive": "RemoveLink",
    "Merge": "NoCascade",
    "Reparent": "NoCascade",
    "Share": "NoCascade",
    "Unshare": "NoCascade",
    "RollupView": "NoCascade"
  },
  "RelationshipAttributes": [],
  "IsCustomizable": {
    "Value": true,
    "CanBeChanged": true,
    "ManagedPropertyLogicalName": "iscustomizable"
  }
}
```

**Console output:**

```
Retrieved relationship: sample_BankAccount_Contacts
```

## Section 6: Create and retrieve a many-to-one relationship

A many-to-one relationship is a one-to-many relationship viewed from the other direction. The following examples create a lookup column named `sample_relatedaccountid` on the `sample_BankAccount` table referencing a row in the `account` table.

### Create N:1 relationship

**Request:**

```http
POST [Organization Uri]/api/data/v9.2/RelationshipDefinitions HTTP/1.1
MSCRM.SolutionUniqueName: examplesolution
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json

{
  "@odata.type": "Microsoft.Dynamics.CRM.OneToManyRelationshipMetadata",
  "AssociatedMenuConfiguration": {
    "Behavior": "UseLabel",
    "Group": "Details",
    "Label": {
      "@odata.type": "Microsoft.Dynamics.CRM.Label",
      "LocalizedLabels": [
        {
          "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
          "Label": "Related Bank Accounts",
          "LanguageCode": 1033,
          "IsManaged": false
        }
      ],
      "UserLocalizedLabel": {
        "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
        "Label": "Related Bank Accounts",
        "LanguageCode": 1033,
        "IsManaged": false
      }
    },
    "Order": 10000,
    "ViewId": "00000000-0000-0000-0000-000000000000"
  },
  "CascadeConfiguration": {
    "Assign": "NoCascade",
    "Delete": "RemoveLink",
    "Merge": "Cascade",
    "Reparent": "NoCascade",
    "Share": "NoCascade",
    "Unshare": "NoCascade",
    "RollupView": "NoCascade"
  },
  "IsHierarchical": false,
  "ReferencedAttribute": "accountid",
  "ReferencedEntity": "account",
  "ReferencingEntity": "sample_bankaccount",
  "Lookup": {
    "@odata.type": "Microsoft.Dynamics.CRM.LookupAttributeMetadata",
    "AttributeType": "Lookup",
    "AttributeTypeName": {
      "Value": "LookupType"
    },
    "Format": "None",
    "Description": {
      "@odata.type": "Microsoft.Dynamics.CRM.Label",
      "LocalizedLabels": [
        {
          "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
          "Label": "An Account related to the bank account.",
          "LanguageCode": 1033,
          "IsManaged": false
        }
      ],
      "UserLocalizedLabel": {
        "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
        "Label": "An Account related to the bank account.",
        "LanguageCode": 1033,
        "IsManaged": false
      }
    },
    "DisplayName": {
      "@odata.type": "Microsoft.Dynamics.CRM.Label",
      "LocalizedLabels": [
        {
          "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
          "Label": "Related Account",
          "LanguageCode": 1033,
          "IsManaged": false
        }
      ],
      "UserLocalizedLabel": {
        "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
        "Label": "Related Account",
        "LanguageCode": 1033,
        "IsManaged": false
      }
    },
    "SchemaName": "sample_RelatedAccountId"
  },
  "IsCustomRelationship": false,
  "IsManaged": false,
  "IsValidForAdvancedFind": false,
  "RelationshipType": "OneToManyRelationship",
  "SchemaName": "sample_Account_BankAccounts",
  "SecurityTypes": "None"
}
```

**Response:**

```http
HTTP/1.1 204 NoContent
OData-Version: 4.0
OData-EntityId: [Organization Uri]/api/data/v9.2/RelationshipDefinitions(0901c466-112a-ed11-9db1-00224804f8e2)
```

**Console output:**

```
Created many-to-one relationship: RelationshipDefinitions(0901c466-112a-ed11-9db1-00224804f8e2)
```

### Retrieve N:1 relationship

**Request:**

```http
GET [Organization Uri]/api/data/v9.2/RelationshipDefinitions(0901c466-112a-ed11-9db1-00224804f8e2)/Microsoft.Dynamics.CRM.OneToManyRelationshipMetadata HTTP/1.1
Consistency: Strong
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
```

**Response:**

```http
HTTP/1.1 200 OK
OData-Version: 4.0

{
  "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#RelationshipDefinitions/Microsoft.Dynamics.CRM.OneToManyRelationshipMetadata/$entity",
  "ReferencedAttribute": "accountid",
  "ReferencedEntity": "account",
  "ReferencingAttribute": "sample_relatedaccountid",
  "ReferencingEntity": "sample_bankaccount",
  "IsHierarchical": false,
  "EntityKey": null,
  "IsRelationshipAttributeDenormalized": false,
  "ReferencedEntityNavigationPropertyName": "sample_Account_BankAccounts",
  "ReferencingEntityNavigationPropertyName": "sample_RelatedAccountId",
  "RelationshipBehavior": 1,
  "IsDenormalizedLookup": null,
  "DenormalizedAttributeName": null,
  "IsCustomRelationship": true,
  "IsValidForAdvancedFind": false,
  "SchemaName": "sample_Account_BankAccounts",
  "SecurityTypes": "Append",
  "IsManaged": false,
  "RelationshipType": "OneToManyRelationship",
  "IntroducedVersion": "1.0.0.0",
  "MetadataId": "0901c466-112a-ed11-9db1-00224804f8e2",
  "HasChanged": null,
  "AssociatedMenuConfiguration": {
    "Behavior": "UseLabel",
    "Group": "Details",
    "Order": 10000,
    "IsCustomizable": true,
    "Icon": null,
    "ViewId": "00000000-0000-0000-0000-000000000000",
    "AvailableOffline": true,
    "MenuId": null,
    "QueryApi": null,
    "Label": {
      "LocalizedLabels": [
        {
          "Label": "Related Bank Accounts",
          "LanguageCode": 1033,
          "IsManaged": false,
          "MetadataId": "b2ad2cce-5c7c-46aa-8bbf-7903d33ef019",
          "HasChanged": null
        }
      ],
      "UserLocalizedLabel": {
        "Label": "Related Bank Accounts",
        "LanguageCode": 1033,
        "IsManaged": false,
        "MetadataId": "b2ad2cce-5c7c-46aa-8bbf-7903d33ef019",
        "HasChanged": null
      }
    }
  },
  "CascadeConfiguration": {
    "Assign": "NoCascade",
    "Delete": "RemoveLink",
    "Archive": "RemoveLink",
    "Merge": "Cascade",
    "Reparent": "NoCascade",
    "Share": "NoCascade",
    "Unshare": "NoCascade",
    "RollupView": "NoCascade"
  },
  "RelationshipAttributes": [],
  "IsCustomizable": {
    "Value": true,
    "CanBeChanged": true,
    "ManagedPropertyLogicalName": "iscustomizable"
  }
}
```

**Console output:**

```
Retrieved relationship: sample_Account_BankAccounts
```

## Section 7: Create and retrieve a many-to-many relationship

Like one-to-many relationships, there are special functions used by the designers in [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) prevent invalid combinations when creating many-to-many relationships.
### Validate N:N relationship eligibility

1. <xref:Microsoft.Dynamics.CRM.CanManyToMany?text=CanManyToMany Function> tells you whether a table can participate in a many-to-many relationship. So this request tests the `contact` table.

   **Request:**

   ```http
   POST [Organization Uri]/api/data/v9.2/CanManyToMany HTTP/1.1
   OData-MaxVersion: 4.0
   OData-Version: 4.0
   If-None-Match: null
   Accept: application/json

   {
   "EntityName": "contact"
   }
   ```

   **Response:**

   ```http
   HTTP/1.1 200 OK
   OData-Version: 4.0

   {
   "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.CanManyToManyResponse",
   "CanManyToMany": true
   }
   ```

   **Console output:**

   ```
   The contact table can participate in many-to-many relationships.
   ```

1. This request performs the same test on the `sample_bankaccount` table.

   **Request:**

   ```http
   POST [Organization Uri]/api/data/v9.2/CanManyToMany HTTP/1.1
   OData-MaxVersion: 4.0
   OData-Version: 4.0
   If-None-Match: null
   Accept: application/json

   {
   "EntityName": "sample_bankaccount"
   }
   ```

   **Response:**

   ```http
   HTTP/1.1 200 OK
   OData-Version: 4.0

   {
   "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.CanManyToManyResponse",
   "CanManyToMany": true
   }
   ```


   **Console output:**

   ```
   The sample_bankaccount table can participate in many-to-many relationships.
   ```

### Identify Potential Entities for N:N relationships

Use the <xref:Microsoft.Dynamics.CRM.GetValidManyToMany?text=GetValidManyToMany Function> to get a list of tables that can participate in many-to-many relationships.

**Request:**

```http
GET [Organization Uri]/api/data/v9.2/GetValidManyToMany HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
```

**Response:**

```http
HTTP/1.1 200 OK
OData-Version: 4.0

{
  "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.GetValidManyToManyResponse",
  "EntityNames": [
    "msdyn_slakpi",
    "workflowbinary",
    "apisettings",
    "flowsession",
    "theme",
    "knowledgearticle",
    "socialprofile",
    "goal",
    "position",
    "externalparty",
    "channelaccessprofileruleitem",
    "routingruleitem",
    "sample_bankaccount",
    "synapselinkexternaltablestate",
    "synapsedatabase",
    "msdyn_aimodel",
    "aaduser",
    "applicationuser",
    "msfp_unsubscribedrecipient",
    "msdyn_aiconfiguration",
    "msdyn_dataflow",
    "flowmachineimage",
    "queueitem",
    "synapselinkschedule",
    "msdyn_federatedarticleincident",
    "flowmachine",
    "synapselinkprofile",
    "msdyn_dataflowrefreshhistory",
    "solutioncomponentrelationshipconfiguration",
    "contact",
    "organizationdatasyncstate",
    "botcomponent",
    "bot",
    "msdyn_componentlayer",
    "msdyn_odatav4ds",
    "msfp_question",
    "msdyn_aibfile",
    "msdyn_solutionhistorydatasource",
    "msdyn_solutionhealthruleset",
    "newprocess",
    "connectionreference",
    "msdyn_knowledgemanagementsetting",
    "msdyn_pmrecording",
    "msfp_survey",
    "msdyn_aibdatasetscontainer",
    "package",
    "msdyn_solutioncomponentsummary",
    "msdyn_helppage",
    "appnotification",
    "organizationdatasyncsubscriptionentity",
    "msdyn_aiodtrainingboundingbox",
    "msdyn_nonrelationalds",
    "expiredprocess",
    "msdyn_analysisresultdetail",
    "msfp_alertrule",
    "msdyn_solutioncomponentcountsummary",
    "msdyn_kalanguagesetting",
    "transactioncurrency",
    "exportsolutionupload",
    "msdyn_pmprocessusersettings",
    "datasyncstate",
    "msdyn_entityrefreshhistory",
    "msdyn_analysisresult",
    "msdyn_componentlayerdatasource",
    "account",
    "kbarticle",
    "systemuser",
    "task",
    "msdyn_analysisjob",
    "solutioncomponentconfiguration",
    "msdyn_knowledgesearchfilter",
    "stagesolutionupload",
    "msdyn_pmtemplate",
    "phonecall",
    "msdyn_solutioncomponentdatasource",
    "environmentvariablevalue",
    "msdyn_aitemplate",
    "userrating",
    "synapselinkprofileentity",
    "featurecontrolsetting",
    "translationprocess",
    "msdyn_pminferredtask",
    "customapirequestparameter",
    "externalpartyitem",
    "msdyn_aibdatasetfile",
    "flowmachinegroup",
    "flowmachineimageversion",
    "msdyn_aibdatasetrecord",
    "msdyn_kbattachment",
    "msdyn_aifptrainingdocument",
    "customapiresponseproperty",
    "msdyn_knowledgearticletemplate",
    "msdyn_aiodimage",
    "msdyn_knowledgesearchinsight",
    "msfp_emailtemplate",
    "catalog",
    "msdyn_knowledgeinteractioninsight",
    "conversationtranscript",
    "msdyn_pmanalysishistory",
    "msdyn_datalakeds",
    "canvasappextendedmetadata",
    "msfp_localizedemailtemplate",
    "msdynce_botcontent",
    "queue",
    "msdyn_solutionhealthruleargument",
    "msdyn_aibfileattacheddata",
    "msdyn_richtextfile",
    "msdyn_kmpersonalizationsetting",
    "msdyn_aiodtrainingimage",
    "msdyn_serviceconfiguration",
    "msdyn_knowledgearticleimage",
    "team",
    "territory",
    "msdyn_solutioncomponentcountdatasource",
    "catalogassignment",
    "msdyn_federatedarticle",
    "msdyn_solutionhealthrule",
    "msdyn_solutionhistory",
    "msdyn_knowledgepersonalfilter",
    "organizationdatasyncsubscription",
    "solutioncomponentbatchconfiguration",
    "connector",
    "solutioncomponentattributeconfiguration",
    "synapselinkprofileentitystate",
    "msdyn_aiodlabel",
    "customapi",
    "msdyn_aibdataset",
    "msfp_fileresponse",
    "environmentvariabledefinition",
    "msdyn_analysiscomponent",
    "msfp_satisfactionmetric",
    "msdyn_tour",
    "msdyn_customcontrolextendedsettings",
    "msfp_surveyreminder",
    "virtualentitymetadata",
    "msfp_questionresponse",
    "msfp_project"
  ]
}
```

**Console output:**

```
Contact is in the list of potential tables for N:N.
sample_BankAccount is in the list of potential tables for N:N.
```

### Create N:N relationship

This request creates a many-to-many relationship between `sample_BankAccount` and `Contact` tables.

**Request:**

```http
POST [Organization Uri]/api/data/v9.2/RelationshipDefinitions HTTP/1.1
MSCRM.SolutionUniqueName: examplesolution
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json

{
  "@odata.type": "Microsoft.Dynamics.CRM.ManyToManyRelationshipMetadata",
  "Entity1AssociatedMenuConfiguration": {
    "Behavior": "UseLabel",
    "Group": "Details",
    "Label": {
      "@odata.type": "Microsoft.Dynamics.CRM.Label",
      "LocalizedLabels": [
        {
          "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
          "Label": "Bank Accounts",
          "LanguageCode": 1033,
          "IsManaged": false
        }
      ],
      "UserLocalizedLabel": {
        "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
        "Label": "Bank Accounts",
        "LanguageCode": 1033,
        "IsManaged": false
      }
    },
    "Order": 10000,
    "ViewId": "00000000-0000-0000-0000-000000000000"
  },
  "Entity1LogicalName": "sample_bankaccount",
  "Entity2AssociatedMenuConfiguration": {
    "Behavior": "UseLabel",
    "Group": "Details",
    "Label": {
      "@odata.type": "Microsoft.Dynamics.CRM.Label",
      "LocalizedLabels": [
        {
          "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
          "Label": "Contacts",
          "LanguageCode": 1033,
          "IsManaged": false
        }
      ],
      "UserLocalizedLabel": {
        "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
        "Label": "Contacts",
        "LanguageCode": 1033,
        "IsManaged": false
      }
    },
    "Order": 10000,
    "ViewId": "00000000-0000-0000-0000-000000000000"
  },
  "Entity2LogicalName": "contact",
  "IntersectEntityName": "sample_sample_BankAccounts_Contacts",
  "IsCustomRelationship": false,
  "IsManaged": false,
  "IsValidForAdvancedFind": false,
  "RelationshipType": "OneToManyRelationship",
  "SchemaName": "sample_sample_BankAccounts_Contacts",
  "SecurityTypes": "None"
}
```

**Response:**

```http
HTTP/1.1 204 NoContent
OData-Version: 4.0
OData-EntityId: [Organization Uri]/api/data/v9.2/RelationshipDefinitions(55c9f86c-112a-ed11-9db1-00224804f8e2)
```

**Console output:**

```
Created Many-to-Many relationship at: RelationshipDefinitions(55c9f86c-112a-ed11-9db1-00224804f8e2)
```

### Retrieve N:N relationship

This request retrieves the many-to-many relationship created by the previous request.

> [!NOTE]
> As mentioned above, because `RelationshipDefinitions` contains both one-to-many and many-to-many relationship definitions, you must include the following in the URL to cast to the type you want to retrieve: `/Microsoft.Dynamics.CRM.ManyToManyRelationshipMetadata`.
> Otherwise, the value returned will be the <xref:Microsoft.Dynamics.CRM.RelationshipMetadataBase?text=RelationshipMetadataBase EntityType> and will not include the properties specific to the <xref:Microsoft.Dynamics.CRM.ManyToManyRelationshipMetadata?text=ManyToManyRelationshipMetadata EntityType>.

**Request:**

```http
GET [Organization Uri]/api/data/v9.2/RelationshipDefinitions(55c9f86c-112a-ed11-9db1-00224804f8e2)/Microsoft.Dynamics.CRM.ManyToManyRelationshipMetadata HTTP/1.1
Consistency: Strong
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
```

**Response:**

```http
HTTP/1.1 200 OK
OData-Version: 4.0

{
  "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#RelationshipDefinitions/Microsoft.Dynamics.CRM.ManyToManyRelationshipMetadata/$entity",
  "Entity1LogicalName": "sample_bankaccount",
  "Entity2LogicalName": "contact",
  "IntersectEntityName": "sample_sample_bankaccounts_contacts",
  "Entity1IntersectAttribute": "sample_bankaccountid",
  "Entity2IntersectAttribute": "contactid",
  "Entity1NavigationPropertyName": "sample_sample_BankAccounts_Contacts",
  "Entity2NavigationPropertyName": "sample_sample_BankAccounts_Contacts",
  "IsCustomRelationship": true,
  "IsValidForAdvancedFind": false,
  "SchemaName": "sample_sample_BankAccounts_Contacts",
  "SecurityTypes": "None",
  "IsManaged": false,
  "RelationshipType": "ManyToManyRelationship",
  "IntroducedVersion": "1.0.0.0",
  "MetadataId": "55c9f86c-112a-ed11-9db1-00224804f8e2",
  "HasChanged": null,
  "Entity1AssociatedMenuConfiguration": {
    "Behavior": "UseLabel",
    "Group": "Details",
    "Order": 10000,
    "IsCustomizable": true,
    "Icon": null,
    "ViewId": "00000000-0000-0000-0000-000000000000",
    "AvailableOffline": true,
    "MenuId": null,
    "QueryApi": null,
    "Label": {
      "LocalizedLabels": [
        {
          "Label": "Bank Accounts",
          "LanguageCode": 1033,
          "IsManaged": false,
          "MetadataId": "271999d1-6fd9-4413-b027-f2a1b231e0a4",
          "HasChanged": null
        }
      ],
      "UserLocalizedLabel": {
        "Label": "Bank Accounts",
        "LanguageCode": 1033,
        "IsManaged": false,
        "MetadataId": "271999d1-6fd9-4413-b027-f2a1b231e0a4",
        "HasChanged": null
      }
    }
  },
  "Entity2AssociatedMenuConfiguration": {
    "Behavior": "UseLabel",
    "Group": "Details",
    "Order": 10000,
    "IsCustomizable": true,
    "Icon": null,
    "ViewId": "00000000-0000-0000-0000-000000000000",
    "AvailableOffline": true,
    "MenuId": null,
    "QueryApi": null,
    "Label": {
      "LocalizedLabels": [
        {
          "Label": "Contacts",
          "LanguageCode": 1033,
          "IsManaged": false,
          "MetadataId": "1fcff441-9a41-42b1-a0d9-e92daa47230f",
          "HasChanged": null
        }
      ],
      "UserLocalizedLabel": {
        "Label": "Contacts",
        "LanguageCode": 1033,
        "IsManaged": false,
        "MetadataId": "1fcff441-9a41-42b1-a0d9-e92daa47230f",
        "HasChanged": null
      }
    }
  },
  "IsCustomizable": {
    "Value": true,
    "CanBeChanged": true,
    "ManagedPropertyLogicalName": "iscustomizable"
  }
}
```

**Console output:**

```
Retrieved Many-to-Many relationship:sample_sample_BankAccounts_Contacts
```

## Section 8: Export managed solution

Use the <xref:Microsoft.Dynamics.CRM.ExportSolution?text=ExportSolution Action> to export the solution as a managed solution. This action includes many switches you can use to include additional information as part of the solution, but in this case, all those options are turned off. More information: [Work with solutions](/power-platform/alm/solution-api)

**Request:**

```http
POST [Organization Uri]/api/data/v9.2/ExportSolution HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json

{
  "SolutionName": "examplesolution",
  "Managed": true,
  "ExportAutoNumberingSettings": false,
  "ExportCalendarSettings": false,
  "ExportCustomizationSettings": false,
  "ExportEmailTrackingSettings": false,
  "ExportGeneralSettings": false,
  "ExportMarketingSettings": false,
  "ExportOutlookSynchronizationSettings": false,
  "ExportRelationshipRoles": false,
  "ExportIsvConfig": false,
  "ExportSales": false,
  "ExportExternalApplications": false
}
```

**Response:**

```http
HTTP/1.1 200 OK
OData-Version: 4.0

{
  "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.ExportSolutionResponse",
  "ExportSolutionFile": "[ Binary content removed for brevity]"
}
```


**Console output:**

```
Solution Exported to E:\GitHub\PowerApps-Samples\dataverse\webapi\C#-NETx\MetadataOperations\bin\Debug\net6.0\examplesolution.zip
```

## Section 9: Delete sample records

References to all of the records created in this sample have been added to a list. In this section, all the records created are deleted using a `$batch` operation.

**Request:**

```http
POST [Organization Uri]/api/data/v9.2/$batch HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json

--batch_d6cb9873-6b53-490d-942d-0bea79b8ba9a
Content-Type: application/http
Content-Transfer-Encoding: binary
Content-Length: 136

DELETE /api/data/v9.2/RelationshipDefinitions(991efd5f-112a-ed11-9db1-00224804f8e2) HTTP/1.1


--batch_d6cb9873-6b53-490d-942d-0bea79b8ba9a
Content-Type: application/http
Content-Transfer-Encoding: binary
Content-Length: 130

DELETE /api/data/v9.2/EntityDefinitions(5872b902-112a-ed11-9db1-00224804f8e2) HTTP/1.1


--batch_d6cb9873-6b53-490d-942d-0bea79b8ba9a
Content-Type: application/http
Content-Transfer-Encoding: binary
Content-Length: 122

DELETE /api/data/v9.2/solutions(5472b902-112a-ed11-9db1-00224804f8e2) HTTP/1.1


--batch_d6cb9873-6b53-490d-942d-0bea79b8ba9a
Content-Type: application/http
Content-Transfer-Encoding: binary
Content-Length: 123

DELETE /api/data/v9.2/publishers(a78ab7fc-102a-ed11-9db1-00224804f8e2) HTTP/1.1


--batch_d6cb9873-6b53-490d-942d-0bea79b8ba9a
Content-Type: application/http
Content-Transfer-Encoding: binary
Content-Length: 139

DELETE /api/data/v9.2/GlobalOptionSetDefinitions(7cfd8c56-112a-ed11-9db1-00224804f8e2) HTTP/1.1


--batch_d6cb9873-6b53-490d-942d-0bea79b8ba9a--

```

**Response:**

```http
HTTP/1.1 200 OK
OData-Version: 4.0

--batchresponse_9fa66f62-38d1-4890-91ce-4185fd556745
Content-Type: application/http
Content-Transfer-Encoding: binary

HTTP/1.1 204 No Content
OData-Version: 4.0


--batchresponse_9fa66f62-38d1-4890-91ce-4185fd556745
Content-Type: application/http
Content-Transfer-Encoding: binary

HTTP/1.1 204 No Content
OData-Version: 4.0


--batchresponse_9fa66f62-38d1-4890-91ce-4185fd556745
Content-Type: application/http
Content-Transfer-Encoding: binary

HTTP/1.1 204 No Content
OData-Version: 4.0


--batchresponse_9fa66f62-38d1-4890-91ce-4185fd556745
Content-Type: application/http
Content-Transfer-Encoding: binary

HTTP/1.1 204 No Content
OData-Version: 4.0


--batchresponse_9fa66f62-38d1-4890-91ce-4185fd556745
Content-Type: application/http
Content-Transfer-Encoding: binary

HTTP/1.1 204 No Content
OData-Version: 4.0


--batchresponse_9fa66f62-38d1-4890-91ce-4185fd556745--

```



**Console output:**

```
Deleting created records...
```

## Section 10: Import and Delete managed solution

1. This step imports managed solution exported in [Section 8: Export managed solution](#section-8-export-managed-solution) using the <xref:Microsoft.Dynamics.CRM.ImportSolution?text=ImportSolution Action>.
   
   **Request:**

   ```http
   POST [Organization Uri]/api/data/v9.2/ImportSolution HTTP/1.1
   OData-MaxVersion: 4.0
   OData-Version: 4.0
   If-None-Match: null
   Accept: application/json

   {
   "OverwriteUnmanagedCustomizations": false,
   "PublishWorkflows": false,
   "CustomizationFile": "[ Binary content removed for brevity]",
   "ImportJobId": "00000000-0000-0000-0000-000000000000"
   }
   ```

   **Response:**

   ```http
   HTTP/1.1 204 NoContent
   OData-Version: 4.0
   ```

   **Console output:**

   ```
   Sending request to import the examplesolution solution...
   Solution imported as a managed solution.
   ```


1. Get the `solutionid` of the managed solution by `uniquename` so you can delete it.

   **Request:**

   ```http
   GET [Organization Uri]/api/data/v9.2/solutions?$select=solutionid&$filter=uniquename%20eq%20'examplesolution' HTTP/1.1
   OData-MaxVersion: 4.0
   OData-Version: 4.0
   If-None-Match: null
   Accept: application/json
   ```

   **Response:**

   ```http
   HTTP/1.1 200 OK
   OData-Version: 4.0

   {
   "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#solutions(solutionid)",
   "value": [
      {
         "@odata.etag": "W/\"13291034\"",
         "solutionid": "07439497-6992-4e30-81e0-628a91984af5"
      }
   ]
   }
   ```

### Delete managed solution

This final step deletes the managed solution imported to return the system to the original state.

**Request:**

```http
DELETE [Organization Uri]/api/data/v9.2/solutions(07439497-6992-4e30-81e0-628a91984af5) HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
```

**Response:**

```http
HTTP/1.1 204 NoContent
OData-Version: 4.0
```



**Console output:**

```
Sending request to delete the examplesolution solution...
Managed solution deleted.
--Metadata Operations sample completed--
```

### See also  

[Use the Dataverse Web API](overview.md)<br />
[Use the Web API with table definitions](use-web-api-metadata.md)<br />
[Query table definitions using the Web API](query-metadata-web-api.md)<br />
[Create and update table definitions using the Web API](create-update-entity-definitions-using-web-api.md)<br />
[Create and update table relationships using the Web API](create-update-entity-relationships-using-web-api.md)<br />
[Create and update choices (option sets) using the Web API](create-update-optionsets.md)<br />
[Web API Metadata Operations Sample (C#)](samples/webapiservice-metadata-operations.md)<br />



[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
