---
title: "PrincipalObjectAttributeAccess Entity Reference (Common Data Service)| MicrosoftDocs"
description: "Includes schema information and supported messages for the PrincipalObjectAttributeAccess entity."
ms.date: 04/01/2019
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "KumarVivek"
ms.author: "kvivek"
manager: "annbe"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# PrincipalObjectAttributeAccess Entity Reference

Defines CRM security principals (users and teams) access rights to secured field for an entity instance.


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|Create|POST [*org URI*]/api/data/v9.0/principalobjectattributeaccessset<br />See [Create](/powerapps/developer/common-data-service/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|Delete|DELETE [*org URI*]/api/data/v9.0/principalobjectattributeaccessset(*principalobjectattributeaccessid*)<br />See [Delete](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|Retrieve|GET [*org URI*]/api/data/v9.0/principalobjectattributeaccessset(*principalobjectattributeaccessid*)<br />See [Retrieve](/powerapps/developer/common-data-service/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/principalobjectattributeaccessset<br />See [Query Data](/powerapps/developer/common-data-service/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|Update|PATCH [*org URI*]/api/data/v9.0/principalobjectattributeaccessset(*principalobjectattributeaccessid*)<br />See [Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|

## Entity Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|PrincipalObjectAttributeAccesses|
|DisplayCollectionName|Field Sharing|
|DisplayName|Field Sharing|
|EntitySetName|principalobjectattributeaccessset|
|IsBPFEntity|False|
|LogicalCollectionName|principalobjectattributeaccesses|
|LogicalName|principalobjectattributeaccess|
|OwnershipType|OrganizationOwned|
|PrimaryIdAttribute|principalobjectattributeaccessid|
|PrimaryNameAttribute||
|SchemaName|PrincipalObjectAttributeAccess|

<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AttributeId](#BKMK_AttributeId)
- [ObjectId](#BKMK_ObjectId)
- [ObjectTypeCode](#BKMK_ObjectTypeCode)
- [PrincipalId](#BKMK_PrincipalId)
- [PrincipalIdType](#BKMK_PrincipalIdType)
- [PrincipalObjectAttributeAccessId](#BKMK_PrincipalObjectAttributeAccessId)
- [ReadAccess](#BKMK_ReadAccess)
- [UpdateAccess](#BKMK_UpdateAccess)


### <a name="BKMK_AttributeId"></a> AttributeId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the shared secured field|
|DisplayName|Secured field|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|attributeid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_ObjectId"></a> ObjectId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the entity instance with shared secured field|
|DisplayName|Entity instance|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|objectid|
|RequiredLevel|SystemRequired|
|Targets|account,appointment,businessunit,channelaccessprofile,connection,contact,customeraddress,email,fax,feedback,goal,holidaywrapper,kbarticle,knowledgearticle,knowledgearticleviews,knowledgebaserecord,letter,mailmergetemplate,msdyn_connector,phonecall,position,queue,queueitem,recurringappointmentmaster,reportcategory,sharepointdocumentlocation,sharepointsite,socialactivity,socialprofile,systemuser,task,team,territory|
|Type|Lookup|


### <a name="BKMK_ObjectTypeCode"></a> ObjectTypeCode

|Property|Value|
|--------|-----|
|Description|Type of the record with shared secured field|
|DisplayName|Entity object type|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|objecttypecode|
|RequiredLevel|SystemRequired|
|Type|EntityName|


### <a name="BKMK_PrincipalId"></a> PrincipalId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the principal to which secured field is shared|
|DisplayName|Principal|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|principalid|
|RequiredLevel|SystemRequired|
|Targets|systemuser,team|
|Type|Lookup|


### <a name="BKMK_PrincipalIdType"></a> PrincipalIdType

|Property|Value|
|--------|-----|
|Description|Type of the principal to which secured field is shared|
|DisplayName|Principal type|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|principalidtype|
|RequiredLevel|SystemRequired|
|Type|EntityName|


### <a name="BKMK_PrincipalObjectAttributeAccessId"></a> PrincipalObjectAttributeAccessId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the shared secured field instance|
|DisplayName|Shared secured field|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|principalobjectattributeaccessid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_ReadAccess"></a> ReadAccess

|Property|Value|
|--------|-----|
|Description|Read permission for secured field instance|
|DisplayName|Read permission|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|readaccess|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### ReadAccess Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_UpdateAccess"></a> UpdateAccess

|Property|Value|
|--------|-----|
|Description|Update permission for secured field instance|
|DisplayName|Update permission|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|updateaccess|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### UpdateAccess Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False


<a name="read-only-attributes"></a>

## Read-only attributes

These attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [OrganizationId](#BKMK_OrganizationId)
- [OrganizationIdName](#BKMK_OrganizationIdName)
- [PrincipalIdName](#BKMK_PrincipalIdName)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_OrganizationId"></a> OrganizationId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the associated organization.|
|DisplayName|Organization|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|organizationid|
|RequiredLevel|SystemRequired|
|Targets|organization|
|Type|Lookup|


### <a name="BKMK_OrganizationIdName"></a> OrganizationIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|organizationidname|
|MaxLength|160|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_PrincipalIdName"></a> PrincipalIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|principalidname|
|MaxLength|160|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|versionnumber|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|
|RequiredLevel|None|
|Type|BigInt|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related entity. Listed by **SchemaName**.

- [territory_principalobjectattributeaccess](#BKMK_territory_principalobjectattributeaccess)
- [msdyn_connector_PrincipalObjectAttributeAccesses](#BKMK_msdyn_connector_PrincipalObjectAttributeAccesses)
- [account_principalobjectattributeaccess](#BKMK_account_principalobjectattributeaccess)
- [contact_principalobjectattributeaccess](#BKMK_contact_principalobjectattributeaccess)
- [lk_principalobjectattributeaccess_organizationid](#BKMK_lk_principalobjectattributeaccess_organizationid)
- [team_principalobjectattributeaccess_principalid](#BKMK_team_principalobjectattributeaccess_principalid)
- [systemuser_principalobjectattributeaccess_principalid](#BKMK_systemuser_principalobjectattributeaccess_principalid)
- [knowledgearticle_PrincipalObjectAttributeAccess](#BKMK_knowledgearticle_PrincipalObjectAttributeAccess)
- [KnowledgeBaseRecord_PrincipalObjectAttributeAccess](#BKMK_KnowledgeBaseRecord_PrincipalObjectAttributeAccess)
- [team_principalobjectattributeaccess](#BKMK_team_principalobjectattributeaccess)
- [reportcategory_principalobjectattributeaccess](#BKMK_reportcategory_principalobjectattributeaccess)
- [mailmergetemplate_principalobjectattributeaccess](#BKMK_mailmergetemplate_principalobjectattributeaccess)
- [fax_principalobjectattributeaccess](#BKMK_fax_principalobjectattributeaccess)
- [socialactivity_principalobjectattributeaccess](#BKMK_socialactivity_principalobjectattributeaccess)
- [kbarticle_principalobjectattributeaccess](#BKMK_kbarticle_principalobjectattributeaccess)
- [phonecall_principalobjectattributeaccess](#BKMK_phonecall_principalobjectattributeaccess)
- [position_principalobjectattributeaccess](#BKMK_position_principalobjectattributeaccess)
- [customeraddress_principalobjectattributeaccess](#BKMK_customeraddress_principalobjectattributeaccess)
- [sharepointsite_principalobjectattributeaccess](#BKMK_sharepointsite_principalobjectattributeaccess)
- [systemuser_principalobjectattributeaccess](#BKMK_systemuser_principalobjectattributeaccess)
- [connection_principalobjectattributeaccess](#BKMK_connection_principalobjectattributeaccess)
- [appointment_principalobjectattributeaccess](#BKMK_appointment_principalobjectattributeaccess)
- [goal_principalobjectattributeaccess](#BKMK_goal_principalobjectattributeaccess)
- [email_principalobjectattributeaccess](#BKMK_email_principalobjectattributeaccess)
- [knowledgearticleview_principalobjectattributeaccess](#BKMK_knowledgearticleview_principalobjectattributeaccess)
- [feedback_principalobjectattributeaccess](#BKMK_feedback_principalobjectattributeaccess)
- [businessunit_principalobjectattributeaccess](#BKMK_businessunit_principalobjectattributeaccess)
- [sharepointdocumentlocation_principalobjectattributeaccess](#BKMK_sharepointdocumentlocation_principalobjectattributeaccess)
- [queueitem_principalobjectattributeaccess](#BKMK_queueitem_principalobjectattributeaccess)
- [queue_principalobjectattributeaccess](#BKMK_queue_principalobjectattributeaccess)
- [recurringappointmentmaster_principalobjectattributeaccess](#BKMK_recurringappointmentmaster_principalobjectattributeaccess)
- [task_principalobjectattributeaccess](#BKMK_task_principalobjectattributeaccess)
- [letter_principalobjectattributeaccess](#BKMK_letter_principalobjectattributeaccess)
- [socialprofile_principalobjectattributeaccess](#BKMK_socialprofile_principalobjectattributeaccess)


### <a name="BKMK_territory_principalobjectattributeaccess"></a> territory_principalobjectattributeaccess

**Added by**: Application Common Solution

See territory Entity [territory_principalobjectattributeaccess](territory.md#BKMK_territory_principalobjectattributeaccess) One-To-Many relationship.

### <a name="BKMK_msdyn_connector_PrincipalObjectAttributeAccesses"></a> msdyn_connector_PrincipalObjectAttributeAccesses

**Added by**: Power Connector Solution Solution

See msdyn_connector Entity [msdyn_connector_PrincipalObjectAttributeAccesses](msdyn_connector.md#BKMK_msdyn_connector_PrincipalObjectAttributeAccesses) One-To-Many relationship.

### <a name="BKMK_account_principalobjectattributeaccess"></a> account_principalobjectattributeaccess

See account Entity [account_principalobjectattributeaccess](account.md#BKMK_account_principalobjectattributeaccess) One-To-Many relationship.

### <a name="BKMK_contact_principalobjectattributeaccess"></a> contact_principalobjectattributeaccess

See contact Entity [contact_principalobjectattributeaccess](contact.md#BKMK_contact_principalobjectattributeaccess) One-To-Many relationship.

### <a name="BKMK_lk_principalobjectattributeaccess_organizationid"></a> lk_principalobjectattributeaccess_organizationid

See organization Entity [lk_principalobjectattributeaccess_organizationid](organization.md#BKMK_lk_principalobjectattributeaccess_organizationid) One-To-Many relationship.

### <a name="BKMK_team_principalobjectattributeaccess_principalid"></a> team_principalobjectattributeaccess_principalid

See team Entity [team_principalobjectattributeaccess_principalid](team.md#BKMK_team_principalobjectattributeaccess_principalid) One-To-Many relationship.

### <a name="BKMK_systemuser_principalobjectattributeaccess_principalid"></a> systemuser_principalobjectattributeaccess_principalid

See systemuser Entity [systemuser_principalobjectattributeaccess_principalid](systemuser.md#BKMK_systemuser_principalobjectattributeaccess_principalid) One-To-Many relationship.

### <a name="BKMK_knowledgearticle_PrincipalObjectAttributeAccess"></a> knowledgearticle_PrincipalObjectAttributeAccess

See knowledgearticle Entity [knowledgearticle_PrincipalObjectAttributeAccess](knowledgearticle.md#BKMK_knowledgearticle_PrincipalObjectAttributeAccess) One-To-Many relationship.

### <a name="BKMK_KnowledgeBaseRecord_PrincipalObjectAttributeAccess"></a> KnowledgeBaseRecord_PrincipalObjectAttributeAccess

See knowledgebaserecord Entity [KnowledgeBaseRecord_PrincipalObjectAttributeAccess](knowledgebaserecord.md#BKMK_KnowledgeBaseRecord_PrincipalObjectAttributeAccess) One-To-Many relationship.

### <a name="BKMK_team_principalobjectattributeaccess"></a> team_principalobjectattributeaccess

See team Entity [team_principalobjectattributeaccess](team.md#BKMK_team_principalobjectattributeaccess) One-To-Many relationship.

### <a name="BKMK_reportcategory_principalobjectattributeaccess"></a> reportcategory_principalobjectattributeaccess

See reportcategory Entity [reportcategory_principalobjectattributeaccess](reportcategory.md#BKMK_reportcategory_principalobjectattributeaccess) One-To-Many relationship.

### <a name="BKMK_mailmergetemplate_principalobjectattributeaccess"></a> mailmergetemplate_principalobjectattributeaccess

See mailmergetemplate Entity [mailmergetemplate_principalobjectattributeaccess](mailmergetemplate.md#BKMK_mailmergetemplate_principalobjectattributeaccess) One-To-Many relationship.

### <a name="BKMK_fax_principalobjectattributeaccess"></a> fax_principalobjectattributeaccess

See fax Entity [fax_principalobjectattributeaccess](fax.md#BKMK_fax_principalobjectattributeaccess) One-To-Many relationship.

### <a name="BKMK_socialactivity_principalobjectattributeaccess"></a> socialactivity_principalobjectattributeaccess

See socialactivity Entity [socialactivity_principalobjectattributeaccess](socialactivity.md#BKMK_socialactivity_principalobjectattributeaccess) One-To-Many relationship.

### <a name="BKMK_kbarticle_principalobjectattributeaccess"></a> kbarticle_principalobjectattributeaccess

See kbarticle Entity [kbarticle_principalobjectattributeaccess](kbarticle.md#BKMK_kbarticle_principalobjectattributeaccess) One-To-Many relationship.

### <a name="BKMK_phonecall_principalobjectattributeaccess"></a> phonecall_principalobjectattributeaccess

See phonecall Entity [phonecall_principalobjectattributeaccess](phonecall.md#BKMK_phonecall_principalobjectattributeaccess) One-To-Many relationship.

### <a name="BKMK_position_principalobjectattributeaccess"></a> position_principalobjectattributeaccess

See position Entity [position_principalobjectattributeaccess](position.md#BKMK_position_principalobjectattributeaccess) One-To-Many relationship.

### <a name="BKMK_customeraddress_principalobjectattributeaccess"></a> customeraddress_principalobjectattributeaccess

See customeraddress Entity [customeraddress_principalobjectattributeaccess](customeraddress.md#BKMK_customeraddress_principalobjectattributeaccess) One-To-Many relationship.

### <a name="BKMK_sharepointsite_principalobjectattributeaccess"></a> sharepointsite_principalobjectattributeaccess

See sharepointsite Entity [sharepointsite_principalobjectattributeaccess](sharepointsite.md#BKMK_sharepointsite_principalobjectattributeaccess) One-To-Many relationship.

### <a name="BKMK_systemuser_principalobjectattributeaccess"></a> systemuser_principalobjectattributeaccess

See systemuser Entity [systemuser_principalobjectattributeaccess](systemuser.md#BKMK_systemuser_principalobjectattributeaccess) One-To-Many relationship.

### <a name="BKMK_connection_principalobjectattributeaccess"></a> connection_principalobjectattributeaccess

See connection Entity [connection_principalobjectattributeaccess](connection.md#BKMK_connection_principalobjectattributeaccess) One-To-Many relationship.

### <a name="BKMK_appointment_principalobjectattributeaccess"></a> appointment_principalobjectattributeaccess

See appointment Entity [appointment_principalobjectattributeaccess](appointment.md#BKMK_appointment_principalobjectattributeaccess) One-To-Many relationship.

### <a name="BKMK_goal_principalobjectattributeaccess"></a> goal_principalobjectattributeaccess

See goal Entity [goal_principalobjectattributeaccess](goal.md#BKMK_goal_principalobjectattributeaccess) One-To-Many relationship.

### <a name="BKMK_email_principalobjectattributeaccess"></a> email_principalobjectattributeaccess

See email Entity [email_principalobjectattributeaccess](email.md#BKMK_email_principalobjectattributeaccess) One-To-Many relationship.

### <a name="BKMK_knowledgearticleview_principalobjectattributeaccess"></a> knowledgearticleview_principalobjectattributeaccess

See knowledgearticleviews Entity [knowledgearticleview_principalobjectattributeaccess](knowledgearticleviews.md#BKMK_knowledgearticleview_principalobjectattributeaccess) One-To-Many relationship.

### <a name="BKMK_feedback_principalobjectattributeaccess"></a> feedback_principalobjectattributeaccess

See feedback Entity [feedback_principalobjectattributeaccess](feedback.md#BKMK_feedback_principalobjectattributeaccess) One-To-Many relationship.

### <a name="BKMK_businessunit_principalobjectattributeaccess"></a> businessunit_principalobjectattributeaccess

See businessunit Entity [businessunit_principalobjectattributeaccess](businessunit.md#BKMK_businessunit_principalobjectattributeaccess) One-To-Many relationship.

### <a name="BKMK_sharepointdocumentlocation_principalobjectattributeaccess"></a> sharepointdocumentlocation_principalobjectattributeaccess

See sharepointdocumentlocation Entity [sharepointdocumentlocation_principalobjectattributeaccess](sharepointdocumentlocation.md#BKMK_sharepointdocumentlocation_principalobjectattributeaccess) One-To-Many relationship.

### <a name="BKMK_queueitem_principalobjectattributeaccess"></a> queueitem_principalobjectattributeaccess

See queueitem Entity [queueitem_principalobjectattributeaccess](queueitem.md#BKMK_queueitem_principalobjectattributeaccess) One-To-Many relationship.

### <a name="BKMK_queue_principalobjectattributeaccess"></a> queue_principalobjectattributeaccess

See queue Entity [queue_principalobjectattributeaccess](queue.md#BKMK_queue_principalobjectattributeaccess) One-To-Many relationship.

### <a name="BKMK_recurringappointmentmaster_principalobjectattributeaccess"></a> recurringappointmentmaster_principalobjectattributeaccess

See recurringappointmentmaster Entity [recurringappointmentmaster_principalobjectattributeaccess](recurringappointmentmaster.md#BKMK_recurringappointmentmaster_principalobjectattributeaccess) One-To-Many relationship.

### <a name="BKMK_task_principalobjectattributeaccess"></a> task_principalobjectattributeaccess

See task Entity [task_principalobjectattributeaccess](task.md#BKMK_task_principalobjectattributeaccess) One-To-Many relationship.

### <a name="BKMK_letter_principalobjectattributeaccess"></a> letter_principalobjectattributeaccess

See letter Entity [letter_principalobjectattributeaccess](letter.md#BKMK_letter_principalobjectattributeaccess) One-To-Many relationship.

### <a name="BKMK_socialprofile_principalobjectattributeaccess"></a> socialprofile_principalobjectattributeaccess

See socialprofile Entity [socialprofile_principalobjectattributeaccess](socialprofile.md#BKMK_socialprofile_principalobjectattributeaccess) One-To-Many relationship.

### See also

[About the Entity Reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.principalobjectattributeaccess?text=principalobjectattributeaccess EntityType" />