---
title: "Connection table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the Connection table/entity."
ms.date: 10/05/2021
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "KumarVivek"
ms.author: "kvivek"
manager: "margoc"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Connection table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Relationship between two entities.


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|Assign|PATCH [*org URI*]/api/data/v9.0/connections(*connectionid*)<br />[Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update) `ownerid` property.|<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
|Create|POST [*org URI*]/api/data/v9.0/connections<br />See [Create](/powerapps/developer/common-data-service/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|Delete|DELETE [*org URI*]/api/data/v9.0/connections(*connectionid*)<br />See [Delete](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|GrantAccess|<xref href="Microsoft.Dynamics.CRM.GrantAccess?text=GrantAccess Action" />|<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
|ModifyAccess|<xref href="Microsoft.Dynamics.CRM.ModifyAccess?text=ModifyAccess Action" />|<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
|Retrieve|GET [*org URI*]/api/data/v9.0/connections(*connectionid*)<br />See [Retrieve](/powerapps/developer/common-data-service/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/connections<br />See [Query Data](/powerapps/developer/common-data-service/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|RetrievePrincipalAccess|<xref href="Microsoft.Dynamics.CRM.RetrievePrincipalAccess?text=RetrievePrincipalAccess Function" />|<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
|RetrieveSharedPrincipalsAndAccess|<xref href="Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?text=RetrieveSharedPrincipalsAndAccess Function" />|<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
|RevokeAccess|<xref href="Microsoft.Dynamics.CRM.RevokeAccess?text=RevokeAccess Action" />|<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
|SetState|PATCH [*org URI*]/api/data/v9.0/connections(*connectionid*)<br />[Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update) `statecode` and `statuscode` properties.|<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
|Update|PATCH [*org URI*]/api/data/v9.0/connections(*connectionid*)<br />See [Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|Connections|
|DisplayCollectionName|Connections|
|DisplayName|Connection|
|EntitySetName|connections|
|IsBPFEntity|False|
|LogicalCollectionName|connections|
|LogicalName|connection|
|OwnershipType|UserOwned|
|PrimaryIdAttribute|connectionid|
|PrimaryNameAttribute|name|
|SchemaName|Connection|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ConnectionId](#BKMK_ConnectionId)
- [Description](#BKMK_Description)
- [EffectiveEnd](#BKMK_EffectiveEnd)
- [EffectiveStart](#BKMK_EffectiveStart)
- [EntityImage](#BKMK_EntityImage)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [Record1Id](#BKMK_Record1Id)
- [Record1IdObjectTypeCode](#BKMK_Record1IdObjectTypeCode)
- [Record1RoleId](#BKMK_Record1RoleId)
- [Record2Id](#BKMK_Record2Id)
- [Record2IdObjectTypeCode](#BKMK_Record2IdObjectTypeCode)
- [Record2RoleId](#BKMK_Record2RoleId)
- [StateCode](#BKMK_StateCode)
- [StatusCode](#BKMK_StatusCode)
- [TransactionCurrencyId](#BKMK_TransactionCurrencyId)


### <a name="BKMK_ConnectionId"></a> ConnectionId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the connection.|
|DisplayName|Connection|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|connectionid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_Description"></a> Description

|Property|Value|
|--------|-----|
|Description|Type additional information to describe the connection, such as the length or quality of the relationship.|
|DisplayName|Description|
|Format|TextArea|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|description|
|MaxLength|2000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_EffectiveEnd"></a> EffectiveEnd

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Enter the end date of the connection.|
|DisplayName|Ending|
|Format|DateOnly|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|effectiveend|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_EffectiveStart"></a> EffectiveStart

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Enter the start date of the connection.|
|DisplayName|Starting|
|Format|DateOnly|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|effectivestart|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_EntityImage"></a> EntityImage

|Property|Value|
|--------|-----|
|Description|The default image for the entity.|
|DisplayName|Entity Image|
|IsPrimaryImage|True|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|entityimage|
|MaxHeight|144|
|MaxWidth|144|
|RequiredLevel|None|
|Type|Image|


### <a name="BKMK_ImportSequenceNumber"></a> ImportSequenceNumber

|Property|Value|
|--------|-----|
|Description|Unique identifier of the data import or data migration that created this record.|
|DisplayName|Import Sequence Number|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|importsequencenumber|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_OverriddenCreatedOn"></a> OverriddenCreatedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time that the record was migrated.|
|DisplayName|Record Created On|
|Format|DateOnly|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|overriddencreatedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_OwnerId"></a> OwnerId

|Property|Value|
|--------|-----|
|Description|Enter the user or team who is assigned to manage the record. This field is updated every time the record is assigned to a different user.|
|DisplayName|Owner|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|ownerid|
|RequiredLevel|SystemRequired|
|Targets|systemuser,team|
|Type|Owner|


### <a name="BKMK_OwnerIdType"></a> OwnerIdType

|Property|Value|
|--------|-----|
|Description|Type of the owner of the connection, such as user, team, or business unit.|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owneridtype|
|RequiredLevel|SystemRequired|
|Type|EntityName|


### <a name="BKMK_Record1Id"></a> Record1Id

|Property|Value|
|--------|-----|
|Description|Choose the primary account, contact, or other record involved in the connection.|
|DisplayName|Connected From|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|record1id|
|RequiredLevel|None|
|Targets|account,activitypointer,appointment,channelaccessprofilerule,contact,email,fax,goal,knowledgearticle,knowledgebaserecord,letter,phonecall,position,processsession,recurringappointmentmaster,socialactivity,socialprofile,systemuser,task,team,territory|
|Type|Lookup|


### <a name="BKMK_Record1IdObjectTypeCode"></a> Record1IdObjectTypeCode

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|record1idobjecttypecode|
|RequiredLevel|None|
|Type|EntityName|


### <a name="BKMK_Record1RoleId"></a> Record1RoleId

|Property|Value|
|--------|-----|
|Description|Choose the primary party's role or relationship with the second party.|
|DisplayName|Role (From)|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|record1roleid|
|RequiredLevel|None|
|Targets|connectionrole|
|Type|Lookup|


### <a name="BKMK_Record2Id"></a> Record2Id

|Property|Value|
|--------|-----|
|Description|Select the secondary account, contact, or other record involved in the connection.|
|DisplayName|Connected To|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|record2id|
|RequiredLevel|None|
|Targets|account,activitypointer,appointment,channelaccessprofilerule,contact,email,fax,goal,knowledgearticle,knowledgebaserecord,letter,phonecall,position,processsession,recurringappointmentmaster,socialactivity,socialprofile,systemuser,task,team,territory|
|Type|Lookup|


### <a name="BKMK_Record2IdObjectTypeCode"></a> Record2IdObjectTypeCode

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|record2idobjecttypecode|
|RequiredLevel|None|
|Type|EntityName|


### <a name="BKMK_Record2RoleId"></a> Record2RoleId

|Property|Value|
|--------|-----|
|Description|Choose the secondary party's role or relationship with the primary party.|
|DisplayName|Role (To)|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|record2roleid|
|RequiredLevel|None|
|Targets|connectionrole|
|Type|Lookup|


### <a name="BKMK_StateCode"></a> StateCode

|Property|Value|
|--------|-----|
|Description|Shows whether the connection is active or inactive. Inactive connections are read-only and can't be edited unless they are reactivated.|
|DisplayName|Status|
|IsValidForCreate|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|statecode|
|RequiredLevel|SystemRequired|
|Type|State|

#### StateCode Choices/Options

|Value|Label|DefaultStatus|InvariantName|
|-----|-----|-------------|-------------|
|0|Active|1|Active|
|1|Inactive|2|Inactive|



### <a name="BKMK_StatusCode"></a> StatusCode

|Property|Value|
|--------|-----|
|Description|Reason for the status of the connection.|
|DisplayName|Status Reason|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|statuscode|
|RequiredLevel|None|
|Type|Status|

#### StatusCode Choices/Options

|Value|Label|State|
|-----|-----|-----|
|1|Active|0|
|2|Inactive|1|



### <a name="BKMK_TransactionCurrencyId"></a> TransactionCurrencyId

|Property|Value|
|--------|-----|
|Description|Choose the local currency for the record to make sure budgets are reported in the correct currency.|
|DisplayName|Currency|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|transactioncurrencyid|
|RequiredLevel|None|
|Targets|transactioncurrency|
|Type|Lookup|

<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedByYomiName](#BKMK_CreatedByYomiName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [EntityImage_Timestamp](#BKMK_EntityImage_Timestamp)
- [EntityImage_URL](#BKMK_EntityImage_URL)
- [EntityImageId](#BKMK_EntityImageId)
- [ExchangeRate](#BKMK_ExchangeRate)
- [IsMaster](#BKMK_IsMaster)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedByYomiName](#BKMK_ModifiedByYomiName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [Name](#BKMK_Name)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [Record1IdName](#BKMK_Record1IdName)
- [Record1ObjectTypeCode](#BKMK_Record1ObjectTypeCode)
- [Record1RoleIdName](#BKMK_Record1RoleIdName)
- [Record2IdName](#BKMK_Record2IdName)
- [Record2ObjectTypeCode](#BKMK_Record2ObjectTypeCode)
- [Record2RoleIdName](#BKMK_Record2RoleIdName)
- [RelatedConnectionId](#BKMK_RelatedConnectionId)
- [TransactionCurrencyIdName](#BKMK_TransactionCurrencyIdName)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|--------|-----|
|Description|Shows who created the record.|
|DisplayName|Created By|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|createdby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_CreatedByName"></a> CreatedByName

|Property|Value|
|--------|-----|
|Description|Name of the user who created the connection.|
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdbyname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_CreatedByYomiName"></a> CreatedByYomiName

|Property|Value|
|--------|-----|
|Description|YomiName of the user who created the connection.|
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdbyyominame|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Shows the date and time when the record was created. The date and time are displayed in the time zone selected in Microsoft Dynamics 365 options.|
|DisplayName|Created On|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|createdon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

|Property|Value|
|--------|-----|
|Description|Shows who created the record on behalf of another user.|
|DisplayName|Created By (Delegate)|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|createdonbehalfby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_CreatedOnBehalfByName"></a> CreatedOnBehalfByName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdonbehalfbyname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_CreatedOnBehalfByYomiName"></a> CreatedOnBehalfByYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdonbehalfbyyominame|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_EntityImage_Timestamp"></a> EntityImage_Timestamp

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|entityimage_timestamp|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|
|RequiredLevel|None|
|Type|BigInt|


### <a name="BKMK_EntityImage_URL"></a> EntityImage_URL

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Url|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|entityimage_url|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_EntityImageId"></a> EntityImageId

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Entity Image Id|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|entityimageid|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_ExchangeRate"></a> ExchangeRate

|Property|Value|
|--------|-----|
|Description|Shows the conversion rate of the record's currency. The exchange rate is used to convert all money fields in the record from the local currency to the system's default currency.|
|DisplayName|Exchange Rate|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|exchangerate|
|MaxValue|100000000000|
|MinValue|0.000000000001|
|Precision|12|
|RequiredLevel|None|
|Type|Decimal|


### <a name="BKMK_IsMaster"></a> IsMaster

|Property|Value|
|--------|-----|
|Description|Indicates that this is the master record.|
|DisplayName|Is Master|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|ismaster|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### IsMaster Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|--------|-----|
|Description|Shows who last updated the record.|
|DisplayName|Modified By|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|modifiedby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_ModifiedByName"></a> ModifiedByName

|Property|Value|
|--------|-----|
|Description|Name of the user who last modified the connection.|
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedbyname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ModifiedByYomiName"></a> ModifiedByYomiName

|Property|Value|
|--------|-----|
|Description|YomiName of the user who last modified the connection.|
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedbyyominame|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ModifiedOn"></a> ModifiedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Shows the date and time when the record was last updated. The date and time are displayed in the time zone selected in Microsoft Dynamics 365 options.|
|DisplayName|Modified On|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|modifiedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

|Property|Value|
|--------|-----|
|Description|Shows who last updated the record on behalf of another user.|
|DisplayName|Modified By (Delegate)|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|modifiedonbehalfby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_ModifiedOnBehalfByName"></a> ModifiedOnBehalfByName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedonbehalfbyname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ModifiedOnBehalfByYomiName"></a> ModifiedOnBehalfByYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedonbehalfbyyominame|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Name"></a> Name

|Property|Value|
|--------|-----|
|Description|Name of the connection.|
|DisplayName|Connection Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|name|
|MaxLength|500|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_OwnerIdName"></a> OwnerIdName

|Property|Value|
|--------|-----|
|Description|Name of the owner of the connection.|
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owneridname|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_OwnerIdYomiName"></a> OwnerIdYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owneridyominame|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_OwningBusinessUnit"></a> OwningBusinessUnit

|Property|Value|
|--------|-----|
|Description|Shows the business unit that the record owner belongs to.|
|DisplayName|Owning Business Unit|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owningbusinessunit|
|RequiredLevel|None|
|Targets|businessunit|
|Type|Lookup|


### <a name="BKMK_OwningTeam"></a> OwningTeam

|Property|Value|
|--------|-----|
|Description|Unique identifier of the team who owns the connection.|
|DisplayName|Owning Team|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owningteam|
|RequiredLevel|None|
|Targets|team|
|Type|Lookup|


### <a name="BKMK_OwningUser"></a> OwningUser

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who owns the connection.|
|DisplayName|Owning User|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owninguser|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_Record1IdName"></a> Record1IdName

|Property|Value|
|--------|-----|
|Description|Display name for the source record.|
|DisplayName|Name (From)|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|record1idname|
|MaxLength|800|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Record1ObjectTypeCode"></a> Record1ObjectTypeCode

|Property|Value|
|--------|-----|
|Description|Shows the record type of the source record.|
|DisplayName|Type (From)|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|record1objecttypecode|
|RequiredLevel|None|
|Type|Picklist|

#### Record1ObjectTypeCode Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Account|Business that represents a customer or potential customer. The company that is billed in business transactions.|
|2|Contact|Person with whom a business unit has a relationship, such as customer, supplier, and colleague.|
|8|User|Person with access to the Microsoft CRM system and who owns objects in the Microsoft CRM database.|
|9|Team|Collection of system users that routinely collaborate. Teams can be used to simplify record sharing and provide team members with common access to organization data when team members belong to different Business Units.|
|50|Position|Position of a user in the hierarchy|
|99|Social Profile|This entity is used to store social profile information of its associated account and contacts on different social channels.|
|2013|Territory|Territory represents sales regions.|
|4200|Activity|Task performed, or to be performed, by a user. An activity is any action for which an entry can be made on a calendar.|
|4201|Appointment|Commitment representing a time interval with start/end times and duration.|
|4202|Email|Activity that is delivered using email protocols.|
|4204|Fax|Activity that tracks call outcome and number of pages for a fax and optionally stores an electronic copy of the document.|
|4207|Letter|Activity that tracks the delivery of a letter. The activity can contain the electronic copy of the letter.|
|4210|Phone Call|Activity to track a telephone call.|
|4212|Task|Generic activity representing work needed to be done.|
|4216|Social Activity|For internal use only.|
|4251|Recurring Appointment|The Master appointment of a recurring appointment series.|
|4710|Process Session|Information that is generated when a dialog is run. Every time that you run a dialog, a dialog session is created.|
|9400|Channel Access Profile Rule|Defines the rules for automatically associating channel access profiles to external party records.For internal use only|
|9600|Goal|Target objective for a user or a team for a specified time period.|
|9930|Knowledge Base Record|Metadata of knowledge base (KB) articles associated with Microsoft Dynamics 365 entities.|
|9953|Knowledge Article|Organizational knowledge for internal and external use.|



### <a name="BKMK_Record1RoleIdName"></a> Record1RoleIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|record1roleidname|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_Record2IdName"></a> Record2IdName

|Property|Value|
|--------|-----|
|Description|Display name for the target record.|
|DisplayName|Name (To)|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|record2idname|
|MaxLength|800|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Record2ObjectTypeCode"></a> Record2ObjectTypeCode

|Property|Value|
|--------|-----|
|Description|Shows the record type of the target record.|
|DisplayName|Type (To)|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|record2objecttypecode|
|RequiredLevel|None|
|Type|Picklist|

#### Record2ObjectTypeCode Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Account|Business that represents a customer or potential customer. The company that is billed in business transactions.|
|2|Contact|Person with whom a business unit has a relationship, such as customer, supplier, and colleague.|
|8|User|Person with access to the Microsoft CRM system and who owns objects in the Microsoft CRM database.|
|9|Team|Collection of system users that routinely collaborate. Teams can be used to simplify record sharing and provide team members with common access to organization data when team members belong to different Business Units.|
|50|Position|Position of a user in the hierarchy|
|99|Social Profile|This entity is used to store social profile information of its associated account and contacts on different social channels.|
|2013|Territory|Territory represents sales regions.|
|4200|Activity|Task performed, or to be performed, by a user. An activity is any action for which an entry can be made on a calendar.|
|4201|Appointment|Commitment representing a time interval with start/end times and duration.|
|4202|Email|Activity that is delivered using email protocols.|
|4204|Fax|Activity that tracks call outcome and number of pages for a fax and optionally stores an electronic copy of the document.|
|4207|Letter|Activity that tracks the delivery of a letter. The activity can contain the electronic copy of the letter.|
|4210|Phone Call|Activity to track a telephone call.|
|4212|Task|Generic activity representing work needed to be done.|
|4216|Social Activity|For internal use only.|
|4251|Recurring Appointment|The Master appointment of a recurring appointment series.|
|4710|Process Session|Information that is generated when a dialog is run. Every time that you run a dialog, a dialog session is created.|
|9400|Channel Access Profile Rule|Defines the rules for automatically associating channel access profiles to external party records.For internal use only|
|9600|Goal|Target objective for a user or a team for a specified time period.|
|9930|Knowledge Base Record|Metadata of knowledge base (KB) articles associated with Microsoft Dynamics 365 entities.|
|9953|Knowledge Article|Organizational knowledge for internal and external use.|



### <a name="BKMK_Record2RoleIdName"></a> Record2RoleIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|record2roleidname|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_RelatedConnectionId"></a> RelatedConnectionId

|Property|Value|
|--------|-----|
|Description|Unique identifier for the reciprocal connection record.|
|DisplayName|Reciprocal Connection|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|relatedconnectionid|
|RequiredLevel|ApplicationRequired|
|Targets|connection|
|Type|Lookup|


### <a name="BKMK_TransactionCurrencyIdName"></a> TransactionCurrencyIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|transactioncurrencyidname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|--------|-----|
|Description|Version number of the connection.|
|DisplayName|Version Number|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|versionnumber|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|
|RequiredLevel|None|
|Type|BigInt|

<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.

- [Connection_AsyncOperations](#BKMK_Connection_AsyncOperations)
- [connection_related_connection](#BKMK_connection_related_connection)
- [connection_principalobjectattributeaccess](#BKMK_connection_principalobjectattributeaccess)
- [Connection_SyncErrors](#BKMK_Connection_SyncErrors)
- [Connection_ProcessSessions](#BKMK_Connection_ProcessSessions)


### <a name="BKMK_Connection_AsyncOperations"></a> Connection_AsyncOperations

Same as asyncoperation table [Connection_AsyncOperations](asyncoperation.md#BKMK_Connection_AsyncOperations) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|asyncoperation|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|Connection_AsyncOperations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_connection_related_connection"></a> connection_related_connection

Same as connection table [connection_related_connection](connection.md#BKMK_connection_related_connection) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|connection|
|ReferencingAttribute|relatedconnectionid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|connection_related_connection|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: RemoveLink<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_connection_principalobjectattributeaccess"></a> connection_principalobjectattributeaccess

Same as principalobjectattributeaccess table [connection_principalobjectattributeaccess](principalobjectattributeaccess.md#BKMK_connection_principalobjectattributeaccess) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|principalobjectattributeaccess|
|ReferencingAttribute|objectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|connection_principalobjectattributeaccess|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_Connection_SyncErrors"></a> Connection_SyncErrors

Same as syncerror table [Connection_SyncErrors](syncerror.md#BKMK_Connection_SyncErrors) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|syncerror|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|Connection_SyncErrors|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: Cascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|


### <a name="BKMK_Connection_ProcessSessions"></a> Connection_ProcessSessions

Same as processsession table [Connection_ProcessSessions](processsession.md#BKMK_Connection_ProcessSessions) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|processsession|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|Connection_ProcessSessions|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 110|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [knowledgearticle_connections1](#BKMK_knowledgearticle_connections1)
- [knowledgearticle_connections2](#BKMK_knowledgearticle_connections2)
- [KnowledgeBaseRecord_connections1](#BKMK_KnowledgeBaseRecord_connections1)
- [KnowledgeBaseRecord_connections2](#BKMK_KnowledgeBaseRecord_connections2)
- [processsession_connections1](#BKMK_processsession_connections1)
- [contact_connections1](#BKMK_contact_connections1)
- [recurringappointmentmaster_connections1](#BKMK_recurringappointmentmaster_connections1)
- [processsession_connections2](#BKMK_processsession_connections2)
- [letter_connections1](#BKMK_letter_connections1)
- [connection_role_connections2](#BKMK_connection_role_connections2)
- [systemuser_connections2](#BKMK_systemuser_connections2)
- [letter_connections2](#BKMK_letter_connections2)
- [appointment_connections1](#BKMK_appointment_connections1)
- [email_connections1](#BKMK_email_connections1)
- [account_connections1](#BKMK_account_connections1)
- [fax_connections2](#BKMK_fax_connections2)
- [activitypointer_connections2](#BKMK_activitypointer_connections2)
- [socialprofile_connections2](#BKMK_socialprofile_connections2)
- [createdby_connection](#BKMK_createdby_connection)
- [account_connections2](#BKMK_account_connections2)
- [phonecall_connections1](#BKMK_phonecall_connections1)
- [task_connections1](#BKMK_task_connections1)
- [modifiedby_connection](#BKMK_modifiedby_connection)
- [appointment_connections2](#BKMK_appointment_connections2)
- [phonecall_connections2](#BKMK_phonecall_connections2)
- [TransactionCurrency_Connection](#BKMK_TransactionCurrency_Connection)
- [task_connections2](#BKMK_task_connections2)
- [fax_connections1](#BKMK_fax_connections1)
- [position_connection2](#BKMK_position_connection2)
- [goal_connections1](#BKMK_goal_connections1)
- [connection_role_connections1](#BKMK_connection_role_connections1)
- [position_connection1](#BKMK_position_connection1)
- [email_connections2](#BKMK_email_connections2)
- [team_connections1](#BKMK_team_connections1)
- [lk_connectionbase_modifiedonbehalfby](#BKMK_lk_connectionbase_modifiedonbehalfby)
- [socialactivity_connections1](#BKMK_socialactivity_connections1)
- [connection_related_connection](#BKMK_connection_related_connection)
- [contact_connections2](#BKMK_contact_connections2)
- [lk_connectionbase_createdonbehalfby](#BKMK_lk_connectionbase_createdonbehalfby)
- [activitypointer_connections1](#BKMK_activitypointer_connections1)
- [systemuser_connections1](#BKMK_systemuser_connections1)
- [team_connections2](#BKMK_team_connections2)
- [business_unit_connections](#BKMK_business_unit_connections)
- [goal_connections2](#BKMK_goal_connections2)
- [socialprofile_connections1](#BKMK_socialprofile_connections1)
- [socialactivity_connections2](#BKMK_socialactivity_connections2)
- [recurringappointmentmaster_connections2](#BKMK_recurringappointmentmaster_connections2)
- [territory_connections1](#BKMK_territory_connections1)
- [territory_connections2](#BKMK_territory_connections2)


### <a name="BKMK_knowledgearticle_connections1"></a> knowledgearticle_connections1

See knowledgearticle Table [knowledgearticle_connections1](knowledgearticle.md#BKMK_knowledgearticle_connections1) One-To-Many relationship.

### <a name="BKMK_knowledgearticle_connections2"></a> knowledgearticle_connections2

See knowledgearticle Table [knowledgearticle_connections2](knowledgearticle.md#BKMK_knowledgearticle_connections2) One-To-Many relationship.

### <a name="BKMK_KnowledgeBaseRecord_connections1"></a> KnowledgeBaseRecord_connections1

See knowledgebaserecord Table [KnowledgeBaseRecord_connections1](knowledgebaserecord.md#BKMK_KnowledgeBaseRecord_connections1) One-To-Many relationship.

### <a name="BKMK_KnowledgeBaseRecord_connections2"></a> KnowledgeBaseRecord_connections2

See knowledgebaserecord Table [KnowledgeBaseRecord_connections2](knowledgebaserecord.md#BKMK_KnowledgeBaseRecord_connections2) One-To-Many relationship.

### <a name="BKMK_processsession_connections1"></a> processsession_connections1

See processsession Table [processsession_connections1](processsession.md#BKMK_processsession_connections1) One-To-Many relationship.

### <a name="BKMK_contact_connections1"></a> contact_connections1

See contact Table [contact_connections1](contact.md#BKMK_contact_connections1) One-To-Many relationship.

### <a name="BKMK_recurringappointmentmaster_connections1"></a> recurringappointmentmaster_connections1

See recurringappointmentmaster Table [recurringappointmentmaster_connections1](recurringappointmentmaster.md#BKMK_recurringappointmentmaster_connections1) One-To-Many relationship.

### <a name="BKMK_processsession_connections2"></a> processsession_connections2

See processsession Table [processsession_connections2](processsession.md#BKMK_processsession_connections2) One-To-Many relationship.

### <a name="BKMK_letter_connections1"></a> letter_connections1

See letter Table [letter_connections1](letter.md#BKMK_letter_connections1) One-To-Many relationship.

### <a name="BKMK_connection_role_connections2"></a> connection_role_connections2

See connectionrole Table [connection_role_connections2](connectionrole.md#BKMK_connection_role_connections2) One-To-Many relationship.

### <a name="BKMK_systemuser_connections2"></a> systemuser_connections2

See systemuser Table [systemuser_connections2](systemuser.md#BKMK_systemuser_connections2) One-To-Many relationship.

### <a name="BKMK_letter_connections2"></a> letter_connections2

See letter Table [letter_connections2](letter.md#BKMK_letter_connections2) One-To-Many relationship.

### <a name="BKMK_appointment_connections1"></a> appointment_connections1

See appointment Table [appointment_connections1](appointment.md#BKMK_appointment_connections1) One-To-Many relationship.

### <a name="BKMK_email_connections1"></a> email_connections1

See email Table [email_connections1](email.md#BKMK_email_connections1) One-To-Many relationship.

### <a name="BKMK_account_connections1"></a> account_connections1

See account Table [account_connections1](account.md#BKMK_account_connections1) One-To-Many relationship.

### <a name="BKMK_fax_connections2"></a> fax_connections2

See fax Table [fax_connections2](fax.md#BKMK_fax_connections2) One-To-Many relationship.

### <a name="BKMK_activitypointer_connections2"></a> activitypointer_connections2

See activitypointer Table [activitypointer_connections2](activitypointer.md#BKMK_activitypointer_connections2) One-To-Many relationship.

### <a name="BKMK_socialprofile_connections2"></a> socialprofile_connections2

See socialprofile Table [socialprofile_connections2](socialprofile.md#BKMK_socialprofile_connections2) One-To-Many relationship.

### <a name="BKMK_createdby_connection"></a> createdby_connection

See systemuser Table [createdby_connection](systemuser.md#BKMK_createdby_connection) One-To-Many relationship.

### <a name="BKMK_account_connections2"></a> account_connections2

See account Table [account_connections2](account.md#BKMK_account_connections2) One-To-Many relationship.

### <a name="BKMK_phonecall_connections1"></a> phonecall_connections1

See phonecall Table [phonecall_connections1](phonecall.md#BKMK_phonecall_connections1) One-To-Many relationship.

### <a name="BKMK_task_connections1"></a> task_connections1

See task Table [task_connections1](task.md#BKMK_task_connections1) One-To-Many relationship.

### <a name="BKMK_modifiedby_connection"></a> modifiedby_connection

See systemuser Table [modifiedby_connection](systemuser.md#BKMK_modifiedby_connection) One-To-Many relationship.

### <a name="BKMK_appointment_connections2"></a> appointment_connections2

See appointment Table [appointment_connections2](appointment.md#BKMK_appointment_connections2) One-To-Many relationship.

### <a name="BKMK_phonecall_connections2"></a> phonecall_connections2

See phonecall Table [phonecall_connections2](phonecall.md#BKMK_phonecall_connections2) One-To-Many relationship.

### <a name="BKMK_TransactionCurrency_Connection"></a> TransactionCurrency_Connection

See transactioncurrency Table [TransactionCurrency_Connection](transactioncurrency.md#BKMK_TransactionCurrency_Connection) One-To-Many relationship.

### <a name="BKMK_task_connections2"></a> task_connections2

See task Table [task_connections2](task.md#BKMK_task_connections2) One-To-Many relationship.

### <a name="BKMK_fax_connections1"></a> fax_connections1

See fax Table [fax_connections1](fax.md#BKMK_fax_connections1) One-To-Many relationship.

### <a name="BKMK_position_connection2"></a> position_connection2

See position Table [position_connection2](position.md#BKMK_position_connection2) One-To-Many relationship.

### <a name="BKMK_goal_connections1"></a> goal_connections1

See goal Table [goal_connections1](goal.md#BKMK_goal_connections1) One-To-Many relationship.

### <a name="BKMK_connection_role_connections1"></a> connection_role_connections1

See connectionrole Table [connection_role_connections1](connectionrole.md#BKMK_connection_role_connections1) One-To-Many relationship.

### <a name="BKMK_position_connection1"></a> position_connection1

See position Table [position_connection1](position.md#BKMK_position_connection1) One-To-Many relationship.

### <a name="BKMK_email_connections2"></a> email_connections2

See email Table [email_connections2](email.md#BKMK_email_connections2) One-To-Many relationship.

### <a name="BKMK_team_connections1"></a> team_connections1

See team Table [team_connections1](team.md#BKMK_team_connections1) One-To-Many relationship.

### <a name="BKMK_lk_connectionbase_modifiedonbehalfby"></a> lk_connectionbase_modifiedonbehalfby

See systemuser Table [lk_connectionbase_modifiedonbehalfby](systemuser.md#BKMK_lk_connectionbase_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_socialactivity_connections1"></a> socialactivity_connections1

See socialactivity Table [socialactivity_connections1](socialactivity.md#BKMK_socialactivity_connections1) One-To-Many relationship.

### <a name="BKMK_connection_related_connection"></a> connection_related_connection

See connection Table [connection_related_connection](connection.md#BKMK_connection_related_connection) One-To-Many relationship.

### <a name="BKMK_contact_connections2"></a> contact_connections2

See contact Table [contact_connections2](contact.md#BKMK_contact_connections2) One-To-Many relationship.

### <a name="BKMK_lk_connectionbase_createdonbehalfby"></a> lk_connectionbase_createdonbehalfby

See systemuser Table [lk_connectionbase_createdonbehalfby](systemuser.md#BKMK_lk_connectionbase_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_activitypointer_connections1"></a> activitypointer_connections1

See activitypointer Table [activitypointer_connections1](activitypointer.md#BKMK_activitypointer_connections1) One-To-Many relationship.

### <a name="BKMK_systemuser_connections1"></a> systemuser_connections1

See systemuser Table [systemuser_connections1](systemuser.md#BKMK_systemuser_connections1) One-To-Many relationship.

### <a name="BKMK_team_connections2"></a> team_connections2

See team Table [team_connections2](team.md#BKMK_team_connections2) One-To-Many relationship.

### <a name="BKMK_business_unit_connections"></a> business_unit_connections

See businessunit Table [business_unit_connections](businessunit.md#BKMK_business_unit_connections) One-To-Many relationship.

### <a name="BKMK_goal_connections2"></a> goal_connections2

See goal Table [goal_connections2](goal.md#BKMK_goal_connections2) One-To-Many relationship.

### <a name="BKMK_socialprofile_connections1"></a> socialprofile_connections1

See socialprofile Table [socialprofile_connections1](socialprofile.md#BKMK_socialprofile_connections1) One-To-Many relationship.

### <a name="BKMK_socialactivity_connections2"></a> socialactivity_connections2

See socialactivity Table [socialactivity_connections2](socialactivity.md#BKMK_socialactivity_connections2) One-To-Many relationship.

### <a name="BKMK_recurringappointmentmaster_connections2"></a> recurringappointmentmaster_connections2

See recurringappointmentmaster Table [recurringappointmentmaster_connections2](recurringappointmentmaster.md#BKMK_recurringappointmentmaster_connections2) One-To-Many relationship.

### <a name="BKMK_territory_connections1"></a> territory_connections1

**Added by**: Application Common Solution

See territory Table [territory_connections1](territory.md#BKMK_territory_connections1) One-To-Many relationship.

### <a name="BKMK_territory_connections2"></a> territory_connections2

**Added by**: Application Common Solution

See territory Table [territory_connections2](territory.md#BKMK_territory_connections2) One-To-Many relationship.

### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.connection?text=connection EntityType" />