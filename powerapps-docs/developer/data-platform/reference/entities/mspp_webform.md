---
title: "Multistep Form (mspp_webform) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Multistep Form (mspp_webform) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Multistep Form (mspp_webform) table/entity reference (Microsoft Dataverse)

Defines the necessary properties and relationships to the other key entities in order to control the initialization of the form within a web portal.

## Messages

The following table lists the messages for the Multistep Form (mspp_webform) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /mspp_webforms<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /mspp_webforms(*mspp_webformid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: True |`GET` /mspp_webforms(*mspp_webformid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveEntityChanges`<br />Event: True | |<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|
| `RetrieveMultiple`<br />Event: True |`GET` /mspp_webforms<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `Update`<br />Event: True |`PATCH` /mspp_webforms(*mspp_webformid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /mspp_webforms(*mspp_webformid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|


## Events

The following table lists the events for the Multistep Form (mspp_webform) table.
Events are messages that exist so that you can subscribe to them. Unless you added the event, you shouldn't invoke the message, only subscribe to it.

|Name|Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `BulkRetain`|<xref:Microsoft.Dynamics.CRM.BulkRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `PurgeRetainedContent`|<xref:Microsoft.Dynamics.CRM.PurgeRetainedContent?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Retain`|<xref:Microsoft.Dynamics.CRM.Retain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `RollbackRetain`|<xref:Microsoft.Dynamics.CRM.RollbackRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `ValidateRetentionConfig`|<xref:Microsoft.Dynamics.CRM.ValidateRetentionConfig?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|

## Properties

The following table lists selected properties for the Multistep Form (mspp_webform) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Multistep Form** |
| **DisplayCollectionName** | **Multistep Forms** |
| **SchemaName** | `mspp_webform` |
| **CollectionSchemaName** | `mspp_webforms` |
| **EntitySetName** | `mspp_webforms`|
| **LogicalName** | `mspp_webform` |
| **LogicalCollectionName** | `mspp_webforms` |
| **PrimaryIdAttribute** | `mspp_webformid` |
| **PrimaryNameAttribute** |`mspp_name` |
| **TableType** | `Virtual` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [mspp_authenticationrequired](#BKMK_mspp_authenticationrequired)
- [mspp_createdby](#BKMK_mspp_createdby)
- [mspp_createdon](#BKMK_mspp_createdon)
- [mspp_editexistingrecordpermitted](#BKMK_mspp_editexistingrecordpermitted)
- [mspp_editexpiredmessage](#BKMK_mspp_editexpiredmessage)
- [mspp_editexpiredstatecode](#BKMK_mspp_editexpiredstatecode)
- [mspp_editexpiredstatuscode](#BKMK_mspp_editexpiredstatuscode)
- [mspp_editnotpermittedmessage](#BKMK_mspp_editnotpermittedmessage)
- [mspp_modifiedby](#BKMK_mspp_modifiedby)
- [mspp_modifiedon](#BKMK_mspp_modifiedon)
- [mspp_multiplerecordsperuserpermitted](#BKMK_mspp_multiplerecordsperuserpermitted)
- [mspp_name](#BKMK_mspp_name)
- [mspp_progressindicatorenabled](#BKMK_mspp_progressindicatorenabled)
- [mspp_progressindicatorignorelaststep](#BKMK_mspp_progressindicatorignorelaststep)
- [mspp_progressindicatorposition](#BKMK_mspp_progressindicatorposition)
- [mspp_progressindicatorprependstepnum](#BKMK_mspp_progressindicatorprependstepnum)
- [mspp_progressindicatortype](#BKMK_mspp_progressindicatortype)
- [mspp_provisionedlanguages](#BKMK_mspp_provisionedlanguages)
- [mspp_savechangeswarningmessage](#BKMK_mspp_savechangeswarningmessage)
- [mspp_savechangeswarningonclose](#BKMK_mspp_savechangeswarningonclose)
- [mspp_startnewsessiononload](#BKMK_mspp_startnewsessiononload)
- [mspp_startstep](#BKMK_mspp_startstep)
- [mspp_webformId](#BKMK_mspp_webformId)
- [mspp_websiteid](#BKMK_mspp_websiteid)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)

### <a name="BKMK_mspp_authenticationrequired"></a> mspp_authenticationrequired

|Property|Value|
|---|---|
|Description|**Redirect to sign in if the user is anonymous.**|
|DisplayName|**Authentication Required**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_authenticationrequired`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mspp_webform_mspp_authenticationrequired`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_mspp_createdby"></a> mspp_createdby

|Property|Value|
|---|---|
|Description|**Shows who created the record.**|
|DisplayName|**Created By**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_createdby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_mspp_createdon"></a> mspp_createdon

|Property|Value|
|---|---|
|Description|**Shows the date and time when the record was created.**|
|DisplayName|**Created On**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_createdon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|True|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_mspp_editexistingrecordpermitted"></a> mspp_editexistingrecordpermitted

|Property|Value|
|---|---|
|Description|**Determines if an existing record can be edited. This setting is ignored If the form mode on the form step is set to edit mode. Otherwise, an edit form wouldn't function properly.**|
|DisplayName|**Edit Existing Record Permitted**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_editexistingrecordpermitted`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mspp_webform_mspp_editexistingrecordpermitted`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_mspp_editexpiredmessage"></a> mspp_editexpiredmessage

|Property|Value|
|---|---|
|Description||
|DisplayName|**Edit Expired Message**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_editexpiredmessage`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|10000|

### <a name="BKMK_mspp_editexpiredstatecode"></a> mspp_editexpiredstatecode

|Property|Value|
|---|---|
|Description||
|DisplayName|**Edit Expired State Code**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_editexpiredstatecode`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_mspp_editexpiredstatuscode"></a> mspp_editexpiredstatuscode

|Property|Value|
|---|---|
|Description||
|DisplayName|**Edit Expired Status Code**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_editexpiredstatuscode`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_mspp_editnotpermittedmessage"></a> mspp_editnotpermittedmessage

|Property|Value|
|---|---|
|Description||
|DisplayName|**Edit Not Permitted Message**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_editnotpermittedmessage`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|10000|

### <a name="BKMK_mspp_modifiedby"></a> mspp_modifiedby

|Property|Value|
|---|---|
|Description|**Shows who last updated the record.**|
|DisplayName|**Modified By**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_modifiedby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_mspp_modifiedon"></a> mspp_modifiedon

|Property|Value|
|---|---|
|Description|**Shows the date and time when the record was modified.**|
|DisplayName|**Modified On**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_modifiedon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|True|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_mspp_multiplerecordsperuserpermitted"></a> mspp_multiplerecordsperuserpermitted

|Property|Value|
|---|---|
|Description||
|DisplayName|**Multiple Records Per User Permitted**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_multiplerecordsperuserpermitted`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mspp_webform_mspp_multiplerecordsperuserpermitted`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_mspp_name"></a> mspp_name

|Property|Value|
|---|---|
|Description|**The name of the custom entity.**|
|DisplayName|**Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_name`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_mspp_progressindicatorenabled"></a> mspp_progressindicatorenabled

|Property|Value|
|---|---|
|Description||
|DisplayName|**Enabled**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_progressindicatorenabled`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mspp_webform_mspp_progressindicatorenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_mspp_progressindicatorignorelaststep"></a> mspp_progressindicatorignorelaststep

|Property|Value|
|---|---|
|Description||
|DisplayName|**Ignore Last Step In Progress Count**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_progressindicatorignorelaststep`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mspp_webform_mspp_progressindicatorignorelaststep`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_mspp_progressindicatorposition"></a> mspp_progressindicatorposition

|Property|Value|
|---|---|
|Description|**Location of the progress indicator relative to the form**|
|DisplayName|**Position**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_progressindicatorposition`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|756150000|
|GlobalChoiceName|`mspp_webform_mspp_progressindicatorposition`|

#### mspp_progressindicatorposition Choices/Options

|Value|Label|
|---|---|
|756150000|**Top**|
|756150001|**Bottom**|
|756150002|**Left**|
|756150003|**Right**|

### <a name="BKMK_mspp_progressindicatorprependstepnum"></a> mspp_progressindicatorprependstepnum

|Property|Value|
|---|---|
|Description||
|DisplayName|**Prepend Step Number to Step Title**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_progressindicatorprependstepnum`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mspp_webform_mspp_progressindicatorprependstepnum`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_mspp_progressindicatortype"></a> mspp_progressindicatortype

|Property|Value|
|---|---|
|Description||
|DisplayName|**Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_progressindicatortype`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|756150000|
|GlobalChoiceName|`mspp_webform_mspp_progressindicatortype`|

#### mspp_progressindicatortype Choices/Options

|Value|Label|
|---|---|
|756150000|**Title**|
|756150001|**Numeric (Step 1 of N)**|
|756150002|**Progress Bar**|

### <a name="BKMK_mspp_provisionedlanguages"></a> mspp_provisionedlanguages

|Property|Value|
|---|---|
|Description||
|DisplayName|**Provisioned Languages**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_provisionedlanguages`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_mspp_savechangeswarningmessage"></a> mspp_savechangeswarningmessage

|Property|Value|
|---|---|
|Description|**Default message: Your changes have not been saved. To stay on the page so that you can save your changes, click Cancel.**|
|DisplayName|**Save Changes Warning Message**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_savechangeswarningmessage`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|10000|

### <a name="BKMK_mspp_savechangeswarningonclose"></a> mspp_savechangeswarningonclose

|Property|Value|
|---|---|
|Description|**Displays a warning message to the user if they close the browser, or refresh the page, or click the previous button in a multiple step form and they have changes that haven't been saved.**|
|DisplayName|**Display Save Changes Warning On Close**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_savechangeswarningonclose`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mspp_webform_mspp_savechangeswarningonclose`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_mspp_startnewsessiononload"></a> mspp_startnewsessiononload

|Property|Value|
|---|---|
|Description||
|DisplayName|**Start New Session On Load**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_startnewsessiononload`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mspp_webform_mspp_startnewsessiononload`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_mspp_startstep"></a> mspp_startstep

|Property|Value|
|---|---|
|Description|**Unique identifier for Form Step associated with Multistep Form.**|
|DisplayName|**Start Step**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_startstep`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|mspp_webformstep|

### <a name="BKMK_mspp_webformId"></a> mspp_webformId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Multistep Form**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`mspp_webformid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_mspp_websiteid"></a> mspp_websiteid

|Property|Value|
|---|---|
|Description|**Unique identifier for Website entity associated with this record**|
|DisplayName|**Website**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_websiteid`|
|RequiredLevel|ApplicationRequired|
|Type|Lookup|
|Targets|mspp_website|

### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|---|---|
|Description|**Status of the Multistep Form**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`mspp_webform_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the Multistep Form**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`mspp_webform_statuscode`|

#### statuscode Choices/Options

|Value|Details|
|---|---|
|1|Label: **Active**<br />State:0<br />TransitionData: None|
|2|Label: **Inactive**<br />State:1<br />TransitionData: None|


## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

- [mspp_systemuser_mspp_webform_createdby](#BKMK_mspp_systemuser_mspp_webform_createdby)
- [mspp_systemuser_mspp_webform_modifiedby](#BKMK_mspp_systemuser_mspp_webform_modifiedby)
- [mspp_webform_startstep](#BKMK_mspp_webform_startstep)
- [mspp_website_webform](#BKMK_mspp_website_webform)

### <a name="BKMK_mspp_systemuser_mspp_webform_createdby"></a> mspp_systemuser_mspp_webform_createdby

One-To-Many Relationship: [systemuser mspp_systemuser_mspp_webform_createdby](systemuser.md#BKMK_mspp_systemuser_mspp_webform_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`mspp_createdby`|
|ReferencingEntityNavigationPropertyName|`mspp_createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_systemuser_mspp_webform_modifiedby"></a> mspp_systemuser_mspp_webform_modifiedby

One-To-Many Relationship: [systemuser mspp_systemuser_mspp_webform_modifiedby](systemuser.md#BKMK_mspp_systemuser_mspp_webform_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`mspp_modifiedby`|
|ReferencingEntityNavigationPropertyName|`mspp_modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_webform_startstep"></a> mspp_webform_startstep

One-To-Many Relationship: [mspp_webformstep mspp_webform_startstep](mspp_webformstep.md#BKMK_mspp_webform_startstep)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_webformstep`|
|ReferencedAttribute|`mspp_webformstepid`|
|ReferencingAttribute|`mspp_startstep`|
|ReferencingEntityNavigationPropertyName|`mspp_startstep`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_website_webform"></a> mspp_website_webform

One-To-Many Relationship: [mspp_website mspp_website_webform](mspp_website.md#BKMK_mspp_website_webform)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_website`|
|ReferencedAttribute|`mspp_websiteid`|
|ReferencingAttribute|`mspp_websiteid`|
|ReferencingEntityNavigationPropertyName|`mspp_websiteid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [mspp_webform_webformmetadata_entityformforcreate](#BKMK_mspp_webform_webformmetadata_entityformforcreate)
- [mspp_webformstep_webform](#BKMK_mspp_webformstep_webform)
- [mspp_webpage_webform](#BKMK_mspp_webpage_webform)

### <a name="BKMK_mspp_webform_webformmetadata_entityformforcreate"></a> mspp_webform_webformmetadata_entityformforcreate

Many-To-One Relationship: [mspp_webformmetadata mspp_webform_webformmetadata_entityformforcreate](mspp_webformmetadata.md#BKMK_mspp_webform_webformmetadata_entityformforcreate)

|Property|Value|
|---|---|
|ReferencingEntity|`mspp_webformmetadata`|
|ReferencingAttribute|`mspp_entityformforcreate`|
|ReferencedEntityNavigationPropertyName|`mspp_webform_webformmetadata_entityformforcreate`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_webformstep_webform"></a> mspp_webformstep_webform

Many-To-One Relationship: [mspp_webformstep mspp_webformstep_webform](mspp_webformstep.md#BKMK_mspp_webformstep_webform)

|Property|Value|
|---|---|
|ReferencingEntity|`mspp_webformstep`|
|ReferencingAttribute|`mspp_webform`|
|ReferencedEntityNavigationPropertyName|`mspp_webformstep_webform`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseLabel`<br />Group: `Details`<br />Label: Steps<br />MenuId: null<br />Order: 103100<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_webpage_webform"></a> mspp_webpage_webform

Many-To-One Relationship: [mspp_webpage mspp_webpage_webform](mspp_webpage.md#BKMK_mspp_webpage_webform)

|Property|Value|
|---|---|
|ReferencingEntity|`mspp_webpage`|
|ReferencingAttribute|`mspp_webform`|
|ReferencedEntityNavigationPropertyName|`mspp_webpage_webform`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 107000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.mspp_webform?displayProperty=fullName>
