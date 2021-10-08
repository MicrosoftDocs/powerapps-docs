---
title: "Calendar table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the Calendar table/entity."
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

# Calendar table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Calendar used by the scheduling system to define when an appointment or activity is to occur.


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|Create|POST [*org URI*]/api/data/v9.0/calendars<br />See [Create](/powerapps/developer/common-data-service/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|Delete|DELETE [*org URI*]/api/data/v9.0/calendars(*calendarid*)<br />See [Delete](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|ExpandCalendar|<xref href="Microsoft.Dynamics.CRM.ExpandCalendar?text=ExpandCalendar Function" />|<xref:Microsoft.Crm.Sdk.Messages.ExpandCalendarRequest>|
|Retrieve|GET [*org URI*]/api/data/v9.0/calendars(*calendarid*)<br />See [Retrieve](/powerapps/developer/common-data-service/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/calendars<br />See [Query Data](/powerapps/developer/common-data-service/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|Update|PATCH [*org URI*]/api/data/v9.0/calendars(*calendarid*)<br />See [Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|Calendars|
|DisplayCollectionName|Calendars|
|DisplayName|Calendar|
|EntitySetName|calendars|
|IsBPFEntity|False|
|LogicalCollectionName|calendars|
|LogicalName|calendar|
|OwnershipType|BusinessOwned|
|PrimaryIdAttribute|calendarid|
|PrimaryNameAttribute|name|
|SchemaName|Calendar|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [BusinessUnitId](#BKMK_BusinessUnitId)
- [CalendarId](#BKMK_CalendarId)
- [Description](#BKMK_Description)
- [HolidayScheduleCalendarId](#BKMK_HolidayScheduleCalendarId)
- [IsShared](#BKMK_IsShared)
- [Name](#BKMK_Name)
- [PrimaryUserId](#BKMK_PrimaryUserId)
- [Type](#BKMK_Type)


### <a name="BKMK_BusinessUnitId"></a> BusinessUnitId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the business unit with which the calendar is associated.|
|DisplayName|Business Unit|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|businessunitid|
|RequiredLevel|None|
|Targets|businessunit|
|Type|Lookup|


### <a name="BKMK_CalendarId"></a> CalendarId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the calendar.|
|DisplayName|Calendar|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|calendarid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_Description"></a> Description

|Property|Value|
|--------|-----|
|Description|Calendar used by the scheduling system to define when an appointment or activity is to occur.|
|DisplayName|Description|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|description|
|MaxLength|2000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_HolidayScheduleCalendarId"></a> HolidayScheduleCalendarId

|Property|Value|
|--------|-----|
|Description|Holiday Schedule CalendarId|
|DisplayName|Holiday Schedule CalendarId|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|holidayschedulecalendarid|
|RequiredLevel|None|
|Targets|calendar|
|Type|Lookup|


### <a name="BKMK_IsShared"></a> IsShared

|Property|Value|
|--------|-----|
|Description|Calendar is shared by other calendars, such as the organization calendar.|
|DisplayName|Is Shared|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|isshared|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### IsShared Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_Name"></a> Name

|Property|Value|
|--------|-----|
|Description|Name of the calendar.|
|DisplayName|Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|name|
|MaxLength|160|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_PrimaryUserId"></a> PrimaryUserId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the primary user of this calendar.|
|DisplayName|Primary User|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|primaryuserid|
|RequiredLevel|ApplicationRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_Type"></a> Type

|Property|Value|
|--------|-----|
|Description|Calendar type, such as User work hour calendar, or Customer service hour calendar.|
|DisplayName|Calendar type|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|type|
|RequiredLevel|SystemRequired|
|Type|Picklist|

#### Type Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|-1|Inner Calendar type||
|0|Default||
|1|Customer Service||
|2|Holiday Schedule||


<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [BusinessUnitIdName](#BKMK_BusinessUnitIdName)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedByYomiName](#BKMK_CreatedByYomiName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [HolidayScheduleCalendarIdName](#BKMK_HolidayScheduleCalendarIdName)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedByYomiName](#BKMK_ModifiedByYomiName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [OrganizationId](#BKMK_OrganizationId)
- [OrganizationIdName](#BKMK_OrganizationIdName)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_BusinessUnitIdName"></a> BusinessUnitIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|businessunitidname|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who created the calendar.|
|DisplayName|Created By|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_CreatedByName"></a> CreatedByName

|Property|Value|
|--------|-----|
|Description||
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
|Description||
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
|Description|Date and time when the calendar was created.|
|DisplayName|Created On|
|Format|DateAndTime|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the delegate user who created the calendar.|
|DisplayName|Created By (Delegate)|
|IsValidForForm|False|
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


### <a name="BKMK_HolidayScheduleCalendarIdName"></a> HolidayScheduleCalendarIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|holidayschedulecalendaridname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who last modified the calendar.|
|DisplayName|Modified By|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_ModifiedByName"></a> ModifiedByName

|Property|Value|
|--------|-----|
|Description||
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
|Description||
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
|Description|Date and time when the calendar was last modified.|
|DisplayName|Modified On|
|Format|DateAndTime|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the delegate user who last modified the calendar.|
|DisplayName|Modified By (Delegate)|
|IsValidForForm|False|
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


### <a name="BKMK_OrganizationId"></a> OrganizationId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the organization with which the calendar is associated.|
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
|MaxLength|100|
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

<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.

- [calendar_system_users](#BKMK_calendar_system_users)
- [Calendar_AsyncOperations](#BKMK_Calendar_AsyncOperations)
- [Calendar_Annotation](#BKMK_Calendar_Annotation)
- [calendar_customercalendar_holidaycalendar](#BKMK_calendar_customercalendar_holidaycalendar)
- [Calendar_BulkDeleteFailures](#BKMK_Calendar_BulkDeleteFailures)
- [BusinessUnit_Calendar](#BKMK_BusinessUnit_Calendar)
- [slabase_businesshoursid](#BKMK_slabase_businesshoursid)
- [calendar_organization](#BKMK_calendar_organization)
- [calendar_slaitem](#BKMK_calendar_slaitem)


### <a name="BKMK_calendar_system_users"></a> calendar_system_users

Same as systemuser table [calendar_system_users](systemuser.md#BKMK_calendar_system_users) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|systemuser|
|ReferencingAttribute|calendarid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|calendar_system_users|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Restrict<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_Calendar_AsyncOperations"></a> Calendar_AsyncOperations

Same as asyncoperation table [Calendar_AsyncOperations](asyncoperation.md#BKMK_Calendar_AsyncOperations) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|asyncoperation|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|Calendar_AsyncOperations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_Calendar_Annotation"></a> Calendar_Annotation

Same as annotation table [Calendar_Annotation](annotation.md#BKMK_Calendar_Annotation) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|annotation|
|ReferencingAttribute|objectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|Calendar_Annotation|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|


### <a name="BKMK_calendar_customercalendar_holidaycalendar"></a> calendar_customercalendar_holidaycalendar

Same as calendar table [calendar_customercalendar_holidaycalendar](calendar.md#BKMK_calendar_customercalendar_holidaycalendar) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|calendar|
|ReferencingAttribute|holidayschedulecalendarid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|calendar_customercalendar_holidaycalendar|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: RemoveLink<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_Calendar_BulkDeleteFailures"></a> Calendar_BulkDeleteFailures

Same as bulkdeletefailure table [Calendar_BulkDeleteFailures](bulkdeletefailure.md#BKMK_Calendar_BulkDeleteFailures) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|bulkdeletefailure|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|Calendar_BulkDeleteFailures|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_BusinessUnit_Calendar"></a> BusinessUnit_Calendar

Same as businessunit table [BusinessUnit_Calendar](businessunit.md#BKMK_BusinessUnit_Calendar) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|businessunit|
|ReferencingAttribute|calendarid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|BusinessUnit_Calendar|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: RemoveLink<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_slabase_businesshoursid"></a> slabase_businesshoursid

Same as sla table [slabase_businesshoursid](sla.md#BKMK_slabase_businesshoursid) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|sla|
|ReferencingAttribute|businesshoursid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|slabase_businesshoursid|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Restrict<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_calendar_organization"></a> calendar_organization

Same as organization table [calendar_organization](organization.md#BKMK_calendar_organization) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|organization|
|ReferencingAttribute|businessclosurecalendarid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|calendar_organization|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: RemoveLink<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_calendar_slaitem"></a> calendar_slaitem

**Added by**: Service Level Agreement (SLA) Solution

Same as slaitem table [calendar_slaitem](slaitem.md#BKMK_calendar_slaitem) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|slaitem|
|ReferencingAttribute|businesshoursid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|calendar_slaitem|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Restrict<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [lk_calendar_createdby](#BKMK_lk_calendar_createdby)
- [lk_calendar_createdonbehalfby](#BKMK_lk_calendar_createdonbehalfby)
- [lk_calendar_modifiedby](#BKMK_lk_calendar_modifiedby)
- [organization_calendars](#BKMK_organization_calendars)
- [calendar_customercalendar_holidaycalendar](#BKMK_calendar_customercalendar_holidaycalendar)
- [lk_calendar_modifiedonbehalfby](#BKMK_lk_calendar_modifiedonbehalfby)
- [business_unit_calendars](#BKMK_business_unit_calendars)


### <a name="BKMK_lk_calendar_createdby"></a> lk_calendar_createdby

See systemuser Table [lk_calendar_createdby](systemuser.md#BKMK_lk_calendar_createdby) One-To-Many relationship.

### <a name="BKMK_lk_calendar_createdonbehalfby"></a> lk_calendar_createdonbehalfby

See systemuser Table [lk_calendar_createdonbehalfby](systemuser.md#BKMK_lk_calendar_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_calendar_modifiedby"></a> lk_calendar_modifiedby

See systemuser Table [lk_calendar_modifiedby](systemuser.md#BKMK_lk_calendar_modifiedby) One-To-Many relationship.

### <a name="BKMK_organization_calendars"></a> organization_calendars

See organization Table [organization_calendars](organization.md#BKMK_organization_calendars) One-To-Many relationship.

### <a name="BKMK_calendar_customercalendar_holidaycalendar"></a> calendar_customercalendar_holidaycalendar

See calendar Table [calendar_customercalendar_holidaycalendar](calendar.md#BKMK_calendar_customercalendar_holidaycalendar) One-To-Many relationship.

### <a name="BKMK_lk_calendar_modifiedonbehalfby"></a> lk_calendar_modifiedonbehalfby

See systemuser Table [lk_calendar_modifiedonbehalfby](systemuser.md#BKMK_lk_calendar_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_business_unit_calendars"></a> business_unit_calendars

See businessunit Table [business_unit_calendars](businessunit.md#BKMK_business_unit_calendars) One-To-Many relationship.

### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.calendar?text=calendar EntityType" />