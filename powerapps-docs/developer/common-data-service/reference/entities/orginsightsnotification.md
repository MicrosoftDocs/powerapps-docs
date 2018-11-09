---
title: "OrgInsightsNotification Entity Reference (Common Data Service for Apps)| Microsoft Docs"
description: "Includes schema information and supported messages for the OrgInsightsNotification entity."
services: ''
suite: powerapps
documentationcenter: na
author: JimDaly
manager: kvivek
editor: ''
tags: ''
ms.service: powerapps
ms.devlang: na
ms.topic: reference
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 10/31/2018
ms.author: jdaly
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# OrgInsightsNotification Entity Reference

Stores data regarding organization insights notification

## Entity Properties

**DisplayName**: Organization Insights Notification<br />
**DisplayCollectionName**: Organization Insights Notification<br />
**SchemaName**: OrgInsightsNotification<br />
**CollectionSchemaName**: OrgInsightsNotifications<br />
**LogicalName**: orginsightsnotification<br />
**LogicalCollectionName**: orginsightsnotifications<br />
**EntitySetName**: orginsightsnotifications<br />
**PrimaryIdAttribute**: orginsightsnotificationid<br />
**PrimaryNameAttribute**: <br />
**OwnershipType**: OrganizationOwned<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [InternalName](#BKMK_InternalName)
- [Name](#BKMK_Name)
- [OrgInsightsNotificationId](#BKMK_OrgInsightsNotificationId)


### <a name="BKMK_InternalName"></a> InternalName

**Description**: Name of the notification which is used for retrieving the data<br />
**DisplayName**: Name of the notification that is used for retrieving the data<br />
**LogicalName**: internalname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 160


### <a name="BKMK_Name"></a> Name

**Description**: Legend Name used while displaying the notification<br />
**DisplayName**: Legend Name used wile displaying the notification<br />
**LogicalName**: name<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: True<br />
**MaxLength**: 160


### <a name="BKMK_OrgInsightsNotificationId"></a> OrgInsightsNotificationId

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: orginsightsnotificationid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />

<a name="read-only-attributes"></a>
## Read-only attributes
These attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [CreatedOn](#BKMK_CreatedOn)
- [JsonData](#BKMK_JsonData)
- [OrganizationId](#BKMK_OrganizationId)
- [OrganizationIdName](#BKMK_OrganizationIdName)


### <a name="BKMK_CreatedOn"></a> CreatedOn

**Description**: Date and time when the organization insights notification was created<br />
**DisplayName**: Created On<br />
**LogicalName**: createdon<br />
**IsValidForForm**: False<br />
**IsValidForRead**: False<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_JsonData"></a> JsonData

**Description**: Notification Data in Json format<br />
**DisplayName**: Notification Data in Json format<br />
**LogicalName**: jsondata<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Memo<br />
**Format**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 2000


### <a name="BKMK_OrganizationId"></a> OrganizationId

**Description**: Unique identifier of the organization associated with the record<br />
**DisplayName**: Organization<br />
**LogicalName**: organizationid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: False<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Lookup<br />
**Targets**: organization


### <a name="BKMK_OrganizationIdName"></a> OrganizationIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: organizationidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related entity. Listed by **SchemaName**.


### <a name="BKMK_organization_orginsightsnotification"></a> organization_orginsightsnotification

See organization Entity [organization_orginsightsnotification](organization.md#BKMK_organization_orginsightsnotification) One-To-Many relationship.
orginsightsnotification

