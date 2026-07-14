---
title: "Calendar table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Calendar table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Calendar table/entity reference (Microsoft Dataverse)

Calendar used by the scheduling system to define when an appointment or activity is to occur.

## Messages

The following table lists the messages for the Calendar table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /calendars<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: True |`DELETE` /calendars(*calendarid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `ExpandCalendar`<br />Event: False |<xref:Microsoft.Dynamics.CRM.ExpandCalendar?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ExpandCalendarRequest>|
| `Retrieve`<br />Event: True |`GET` /calendars(*calendarid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /calendars<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `Update`<br />Event: True |`PATCH` /calendars(*calendarid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `Upsert`<br />Event: False |`PATCH` /calendars(*calendarid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|

## Properties

The following table lists selected properties for the Calendar table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Calendar** |
| **DisplayCollectionName** | **Calendars** |
| **SchemaName** | `Calendar` |
| **CollectionSchemaName** | `Calendars` |
| **EntitySetName** | `calendars`|
| **LogicalName** | `calendar` |
| **LogicalCollectionName** | `calendars` |
| **PrimaryIdAttribute** | `calendarid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `BusinessOwned` |

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
|---|---|
|Description|**Unique identifier of the business unit with which the calendar is associated.**|
|DisplayName|**Business Unit**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`businessunitid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|businessunit|

### <a name="BKMK_CalendarId"></a> CalendarId

|Property|Value|
|---|---|
|Description|**Unique identifier of the calendar.**|
|DisplayName|**Calendar**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`calendarid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_Description"></a> Description

|Property|Value|
|---|---|
|Description|**Calendar used by the scheduling system to define when an appointment or activity is to occur.**|
|DisplayName|**Description**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`description`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2000|

### <a name="BKMK_HolidayScheduleCalendarId"></a> HolidayScheduleCalendarId

|Property|Value|
|---|---|
|Description|**Holiday Schedule CalendarId**|
|DisplayName|**Holiday Schedule CalendarId**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`holidayschedulecalendarid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|calendar|

### <a name="BKMK_IsShared"></a> IsShared

|Property|Value|
|---|---|
|Description|**Calendar is shared by other calendars, such as the organization calendar.**|
|DisplayName|**Is Shared**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isshared`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`calendar_isshared`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_Name"></a> Name

|Property|Value|
|---|---|
|Description|**Name of the calendar.**|
|DisplayName|**Name**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|160|

### <a name="BKMK_PrimaryUserId"></a> PrimaryUserId

|Property|Value|
|---|---|
|Description|**Unique identifier of the primary user of this calendar.**|
|DisplayName|**Primary User**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`primaryuserid`|
|RequiredLevel|ApplicationRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_Type"></a> Type

|Property|Value|
|---|---|
|Description|**Calendar type, such as User work hour calendar, or Customer service hour calendar.**|
|DisplayName|**Calendar type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`type`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`calendar_type`|

#### Type Choices/Options

|Value|Label|
|---|---|
|-1|**Inner Calendar type**|
|0|**Default**|
|1|**Customer Service**|
|2|**Holiday Schedule**|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [OrganizationId](#BKMK_OrganizationId)
- [VersionNumber](#BKMK_VersionNumber)

### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who created the calendar.**|
|DisplayName|**Created By**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`createdby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|---|---|
|Description|**Date and time when the calendar was created.**|
|DisplayName|**Created On**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`createdon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the delegate user who created the calendar.**|
|DisplayName|**Created By (Delegate)**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`createdonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who last modified the calendar.**|
|DisplayName|**Modified By**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`modifiedby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_ModifiedOn"></a> ModifiedOn

|Property|Value|
|---|---|
|Description|**Date and time when the calendar was last modified.**|
|DisplayName|**Modified On**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`modifiedon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the delegate user who last modified the calendar.**|
|DisplayName|**Modified By (Delegate)**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`modifiedonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_OrganizationId"></a> OrganizationId

|Property|Value|
|---|---|
|Description|**Unique identifier of the organization with which the calendar is associated.**|
|DisplayName|**Organization**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`organizationid`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|organization|

### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`versionnumber`|
|RequiredLevel|None|
|Type|BigInt|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|

## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

- [business_unit_calendars](#BKMK_business_unit_calendars)
- [calendar_customercalendar_holidaycalendar](#BKMK_calendar_customercalendar_holidaycalendar-many-to-one)
- [lk_calendar_createdby](#BKMK_lk_calendar_createdby)
- [lk_calendar_createdonbehalfby](#BKMK_lk_calendar_createdonbehalfby)
- [lk_calendar_modifiedby](#BKMK_lk_calendar_modifiedby)
- [lk_calendar_modifiedonbehalfby](#BKMK_lk_calendar_modifiedonbehalfby)
- [organization_calendars](#BKMK_organization_calendars)

### <a name="BKMK_business_unit_calendars"></a> business_unit_calendars

One-To-Many Relationship: [businessunit business_unit_calendars](businessunit.md#BKMK_business_unit_calendars)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`businessunitid`|
|ReferencingEntityNavigationPropertyName|`businessunitid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_calendar_customercalendar_holidaycalendar-many-to-one"></a> calendar_customercalendar_holidaycalendar

One-To-Many Relationship: [calendar calendar_customercalendar_holidaycalendar](#BKMK_calendar_customercalendar_holidaycalendar-one-to-many)

|Property|Value|
|---|---|
|ReferencedEntity|`calendar`|
|ReferencedAttribute|`calendarid`|
|ReferencingAttribute|`holidayschedulecalendarid`|
|ReferencingEntityNavigationPropertyName|`holidayschedulecalendarid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_calendar_createdby"></a> lk_calendar_createdby

One-To-Many Relationship: [systemuser lk_calendar_createdby](systemuser.md#BKMK_lk_calendar_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_calendar_createdonbehalfby"></a> lk_calendar_createdonbehalfby

One-To-Many Relationship: [systemuser lk_calendar_createdonbehalfby](systemuser.md#BKMK_lk_calendar_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_calendar_modifiedby"></a> lk_calendar_modifiedby

One-To-Many Relationship: [systemuser lk_calendar_modifiedby](systemuser.md#BKMK_lk_calendar_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_calendar_modifiedonbehalfby"></a> lk_calendar_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_calendar_modifiedonbehalfby](systemuser.md#BKMK_lk_calendar_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organization_calendars"></a> organization_calendars

One-To-Many Relationship: [organization organization_calendars](organization.md#BKMK_organization_calendars)

|Property|Value|
|---|---|
|ReferencedEntity|`organization`|
|ReferencedAttribute|`organizationid`|
|ReferencingAttribute|`organizationid`|
|ReferencingEntityNavigationPropertyName|`organizationid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [BusinessUnit_Calendar](#BKMK_BusinessUnit_Calendar)
- [Calendar_Annotation](#BKMK_Calendar_Annotation)
- [Calendar_AsyncOperations](#BKMK_Calendar_AsyncOperations)
- [Calendar_BulkDeleteFailures](#BKMK_Calendar_BulkDeleteFailures)
- [calendar_calendar_rules](#BKMK_calendar_calendar_rules)
- [calendar_customercalendar_holidaycalendar](#BKMK_calendar_customercalendar_holidaycalendar-one-to-many)
- [calendar_organization](#BKMK_calendar_organization)
- [calendar_slaitem](#BKMK_calendar_slaitem)
- [calendar_system_users](#BKMK_calendar_system_users)
- [inner_calendar_calendar_rules](#BKMK_inner_calendar_calendar_rules)
- [slabase_businesshoursid](#BKMK_slabase_businesshoursid)

### <a name="BKMK_BusinessUnit_Calendar"></a> BusinessUnit_Calendar

Many-To-One Relationship: [businessunit BusinessUnit_Calendar](businessunit.md#BKMK_BusinessUnit_Calendar)

|Property|Value|
|---|---|
|ReferencingEntity|`businessunit`|
|ReferencingAttribute|`calendarid`|
|ReferencedEntityNavigationPropertyName|`BusinessUnit_Calendar`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Calendar_Annotation"></a> Calendar_Annotation

Many-To-One Relationship: [annotation Calendar_Annotation](annotation.md#BKMK_Calendar_Annotation)

|Property|Value|
|---|---|
|ReferencingEntity|`annotation`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`Calendar_Annotation`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Calendar_AsyncOperations"></a> Calendar_AsyncOperations

Many-To-One Relationship: [asyncoperation Calendar_AsyncOperations](asyncoperation.md#BKMK_Calendar_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`Calendar_AsyncOperations`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Calendar_BulkDeleteFailures"></a> Calendar_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure Calendar_BulkDeleteFailures](bulkdeletefailure.md#BKMK_Calendar_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`Calendar_BulkDeleteFailures`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_calendar_calendar_rules"></a> calendar_calendar_rules

Many-To-One Relationship: [calendarrule calendar_calendar_rules](calendarrule.md#BKMK_calendar_calendar_rules)

|Property|Value|
|---|---|
|ReferencingEntity|`calendarrule`|
|ReferencingAttribute|`calendarid`|
|ReferencedEntityNavigationPropertyName|`calendar_calendar_rules`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_calendar_customercalendar_holidaycalendar-one-to-many"></a> calendar_customercalendar_holidaycalendar

Many-To-One Relationship: [calendar calendar_customercalendar_holidaycalendar](#BKMK_calendar_customercalendar_holidaycalendar-many-to-one)

|Property|Value|
|---|---|
|ReferencingEntity|`calendar`|
|ReferencingAttribute|`holidayschedulecalendarid`|
|ReferencedEntityNavigationPropertyName|`calendar_customercalendar_holidaycalendar`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_calendar_organization"></a> calendar_organization

Many-To-One Relationship: [organization calendar_organization](organization.md#BKMK_calendar_organization)

|Property|Value|
|---|---|
|ReferencingEntity|`organization`|
|ReferencingAttribute|`businessclosurecalendarid`|
|ReferencedEntityNavigationPropertyName|`calendar_organization`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_calendar_slaitem"></a> calendar_slaitem

Many-To-One Relationship: [slaitem calendar_slaitem](slaitem.md#BKMK_calendar_slaitem)

|Property|Value|
|---|---|
|ReferencingEntity|`slaitem`|
|ReferencingAttribute|`businesshoursid`|
|ReferencedEntityNavigationPropertyName|`calendar_slaitem`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_calendar_system_users"></a> calendar_system_users

Many-To-One Relationship: [systemuser calendar_system_users](systemuser.md#BKMK_calendar_system_users)

|Property|Value|
|---|---|
|ReferencingEntity|`systemuser`|
|ReferencingAttribute|`calendarid`|
|ReferencedEntityNavigationPropertyName|`calendar_system_users`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_inner_calendar_calendar_rules"></a> inner_calendar_calendar_rules

Many-To-One Relationship: [calendarrule inner_calendar_calendar_rules](calendarrule.md#BKMK_inner_calendar_calendar_rules)

|Property|Value|
|---|---|
|ReferencingEntity|`calendarrule`|
|ReferencingAttribute|`innercalendarid`|
|ReferencedEntityNavigationPropertyName|`inner_calendar_calendar_rules`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_slabase_businesshoursid"></a> slabase_businesshoursid

Many-To-One Relationship: [sla slabase_businesshoursid](sla.md#BKMK_slabase_businesshoursid)

|Property|Value|
|---|---|
|ReferencingEntity|`sla`|
|ReferencingAttribute|`businesshoursid`|
|ReferencedEntityNavigationPropertyName|`slabase_businesshoursid`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.calendar?displayProperty=fullName>
