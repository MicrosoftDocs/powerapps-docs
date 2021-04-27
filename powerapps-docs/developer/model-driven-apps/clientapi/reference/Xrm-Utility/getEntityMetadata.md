---
title: "getEntityMetadata (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the getEntityMetadata method.
ms.date: 04/21/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 89123cde-7c66-4c7d-94e4-e287285019f8
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# getEntityMetadata



[!INCLUDE[./includes/getEntityMetadata-description.md](./includes/getEntityMetadata-description.md)] 

## Syntax

`Xrm.Utility.getEntityMetadata(entityName,attributes).then(successCallback, errorCallback)`

## Parameters

|Name |Type |Required |Description |
|---|---|---|---|
|entityName|String|Yes|The logical name of the table.|
|attributes|array of strings|No|The columns to get definitions for.|
|successCallback|function|No|A function to call when the table definitions are returned.|
|errorCallback|function|No|A function to call when the operation fails.|

## Returns

**Type**: Object

**Description**: An object containing the table definitions information with the following values.

<table>
<tr>
<th>Name</th>
<th>Type</th>
<th>Description</th>
</tr>
<tr>
<td>ActivityTypeMask</td>
<td>Number</td>
<td>Whether a custom activity should appear in the activity menus in the Web application. 0 indicates that the custom activity doesn't appear; 1 indicates that it does appear.</td>
</tr>
<tr>
<td>AutoRouteToOwnerQueue</td>
<td>Boolean</td>
<td>Indicates whether to automatically move records to the owner’s default queue when a record of this type is created or assigned. </td>
</tr>

<tr>
<td>CanEnableSyncToExternalSearchIndex</td>
<td>Boolean</td>
<td>For internal use only.</td>
</tr>
<tr>
<td>CanTriggerWorkflow</td>
<td>Boolean</td>
<td>Indicates whether the table can trigger a workflow process.</td>
</tr>
<tr>
<td>Description</td>
<td>String</td>
<td>Description for the table.</td>
</tr>
<tr>
<td>DisplayCollectionName</td>
<td>String</td>
<td>Plural display name for the table.</td>
</tr>
<tr>
<td>DisplayName</td>
<td>String</td>
<td>Display name for the table.</td>
</tr>
<tr>
<td>EnforceStateTransitions</td>
<td>Boolean</td>
<td>Indicates whether the table will enforce custom state transitions.</td>
</tr>
<tr>
<td>EntityColor</td>
<td>String</td>
<td>The hexadecimal code to represent the color to be used for this table in the application.</td>
</tr>
<tr>
<td>EntitySetName</td>
<td>String</td>
<td>The name of the Web API table set for this table.</td>
</tr>
<tr>
<td>HasActivities</td>
<td>Boolean</td>
<td>Indicates whether activities are associated with this table.</td>
</tr>
<tr>
<td>IsActivity</td>
<td>Boolean</td>
<td>Indicates whether the table is an activity.</td>
</tr>
<tr>
<td>IsActivityParty</td>
<td>Boolean</td>
<td>Indicates whether the email messages can be sent to an email address stored in a record of this type.</td>
</tr>
<tr>
<td>IsBusinessProcessEnabled</td>
<td>Boolean</td>
<td>Indicates whether the table is enabled for business process flows.</td>
</tr>
<tr>
<td>IsBPFEntity</td>
<td>Boolean</td>
<td>Indicates whether the table is a business process flow table.</td>
</tr>
<tr>
<td>IsChildEntity</td>
<td>Boolean</td>
<td>Indicates whether the table is a child table.</td>
</tr>
<tr>
<td>IsConnectionsEnabled</td>
<td>Boolean</td>
<td>Indicates whether connections are enabled for this table.</td>
</tr>
<tr>
<td>IsCustomEntity</td>
<td>Boolean</td>
<td>Indicates whether the table is a custom table.</td>
</tr>
<tr>
<td>IsCustomizable</td>
<td>Boolean</td>
<td>Indicates whether the table is customizable.</td>
</tr>
<tr>
<td>IsDocumentManagementEnabled</td>
<td>Boolean</td>
<td>Indicates whether document management is enabled.</td>
</tr>
<tr>
<td>IsDocumentRecommendationsEnabled</td>
<td>Boolean</td>
<td>Indicates whether the document recommendations is enabled.</td>
</tr>
<tr>
<td>IsDuplicateDetectionEnabled</td>
<td>Boolean</td>
<td>Indicates whether duplicate detection is enabled.</td>
</tr>
<tr>
<td>IsEnabledForCharts</td>
<td>Boolean</td>
<td>Indicates whether charts are enabled.</td>
</tr>
<tr>
<td>IsImportable</td>
<td>Boolean</td>
<td>Indicates whether the table can be imported using the Import Wizard.</td>
</tr>
<tr>
<td>IsInteractionCentricEnabled</td>
<td>Boolean</td>
<td>Indicates the table is enabled for interactive experience.</td>
</tr>
<tr>
<td>IsKnowledgeManagementEnabled</td>
<td>Boolean</td>
<td>Indicates whether knowledge management is enabled for the table.</td>
</tr>
<tr>
<td>IsMailMergeEnabled</td>
<td>Boolean</td>
<td>Indicates whether mail merge is enabled for this table.</td>
</tr>
<tr>
<td>IsManaged</td>
<td>Boolean</td>
<td>Indicates whether the table is part of a managed solution.</td>
</tr>
<tr>
<td>IsOneNoteIntegrationEnabled</td>
<td>Boolean</td>
<td>Indicates whether OneNote integration is enabled for the table.</td>
</tr>
<tr>
<td>IsOptimisticConcurrencyEnabled</td>
<td>Boolean</td>
<td>Indicates whether optimistic concurrency is enabled for the table.</td>
</tr>
<tr>
<td>IsQuickCreateEnabled</td>
<td>Boolean</td>
<td>Indicates whether the table is enabled for quick create forms.</td>
</tr>
<tr>
<td>IsStateModelAware</td>
<td>Boolean</td>
<td>Indicates whether the table supports setting custom state transitions.</td>
</tr>
<tr>
<td>IsValidForAdvancedFind</td>
<td>Boolean</td>
<td>Indicates whether the table is will be shown in Advanced Find.</td>
</tr>
<tr>
<td>IsVisibleInMobileClient</td>
<td>Boolean</td>
<td>Indicates whether Microsoft Dynamics 365 for tablets users can see data for this table.</td>
</tr>
<tr>
<td>IsEnabledInUnifiedInterface</td>
<td>Boolean</td>
<td>Indicates whether the table is enabled for Unified Interface.</td>
</tr>
<tr>
<td>LogicalCollectionName</td>
<td>String</td>
<td>The logical collection name.</td>
</tr>
<tr>
<td>LogicalName</td>
<td>String</td>
<td>The logical name for the table.</td>
</tr>
<tr>
<td>ObjectTypeCode</td>
<td>Number</td>
<td>The table type code.</td>
</tr>
<tr>
<td>OwnershipType</td>
<td>String</td>
<td>The ownership type for the table: "UserOwned" or "OrganizationOwned".</td>
</tr>
<tr>
<td>PrimaryIdAttribute</td>
<td>String</td>
<td>The name of the column that is the primary id for the table.</td>
</tr>
<tr>
<td>PrimaryImageAttribute</td>
<td>String</td>
<td>The name of the primary image column for a table.</td>
</tr>
<tr>
<td>PrimaryNameAttribute</td>
<td>String</td>
<td>The name of the primary column for a table.</td>
</tr>
<tr>
<td>Privileges</td>
<td>Array of objects</td>
<td>The privilege definitions for the table where *each* object contains the following values to define the security privilege for access to a table:
<ul>
<li><b>CanBeBasic</b>: Boolean. Whether the privilege can be basic access level.</li>
<li><b>CanBeDeep</b>: Boolean. Whether the privilege can be deep access level.</li>
<li><b>CanBeEntityReference</b>: Boolean. Whether the privilege for an external party can be basic access level.</li>
<li><b>CanBeGlobal</b>: Boolean. Whether the privilege can be global access level.</li>
<li><b>CanBeLocal</b>: Boolean. Whether the privilege can be local access level.</li>
<li><b>CanBeParentEntityReference</b>: Boolean. Whether the privilege for an external party can be parent access level.</li>
<li><b>Name</b>: String. The name of the privilege.</li>
<li><b>PrivilegeId</b>: String. The ID of the privilege.</li>
<li><b>PrivilegeType</b>: Number. The type of privilege, which is one of the following:</li>
<ul>
<li>0: None</li>
<li>1: Create</li>
<li>2: Read</li>
<li>3: Write</li>
<li>4: Delete</li>
<li>5: Assign</li>
<li>6: Share</li>
<li>7: Append</li>
<li>8: AppendTo</li>
</ul>
</ul></td>
</tr>
<tr>
<td>Attributes</td>
<td>Collection</td>
<td>A collection of column definitions objects. The object returned depends on the type of column definitions.
<p><b>Column definitions for the <i>base</i> type</b><br/>
An object returned with the following properties:</p>
<ul>
<li><b>AttributeType</b>: Number. Type of a column. For a list of column type values, see <a href="/dotnet/api/microsoft.xrm.sdk.metadata.attributetypecode">AttributeTypeCode</a></li>
<li><b>DisplayName</b>: String. Display name for the column.</li>
<li><b>EntityLogicalName</b>: String. Logical name of the table that contains the column.</li>
<li><b>LogicalName</b>: String. Logical name for the column.</li></ul>

<p><b>Column definitions for the <i>boolean</i> type</b><br/>
An object returned with the following properties in addition to the <i>base</i> column definitions type properties:</p>
<ul>
<li><b>DefaultFormValue</b>: Boolean. Default value for a Yes/No column.</li>
<li><b>Choice</b>: Object. Options for the boolean column where each option is a key:value pair.</li></ul>

<p><b>Column definitions for the <i>enum</i> type</b><br/>
An object returned with the following properties in addition to the <i>base</i> column definitions type properties:</p>
<ul>
<li><b>Choice</b>: Object. Options for the column where each option is a key:value pair.</li></ul>

<p><b>Column definitions for the <i>choices</i> type</b><br/>
An object returned with the following properties in addition to the <i>base</i> column definitions type properties:</p>
<ul>
<li><b>DefaultFormValue</b>: Number. Default form value for the column.</li>
<li><b>Choice</b>: Object. Options for the column where each option is a key:value pair.</li></ul>

<p><b>Column definitions for the <i>state</i> type</b><br/>
An object returned with the following properties in addition to the <i>base</i> column definitions type properties:</p>
<ul>
<li><b>Choice</b>: Object. Options for the column where each option is a key:value pair.</li></ul>
<p>The object also contains the following methods:</p>
<ul>
<li><b>getDefaultStatus(arg)</b>: Returns the default status (number) based on the passed in state value for a table. For default state and status values for a table, see table definitions information of the table in <a href="/powerapps/developer/data-platform/reference/about-entity-reference">table/entity reference</a>.</li>
<li><b>getStatusValuesForState(arg)</b>: Returns possible status values (array of numbers) for a specified state value. For state and status values for a table, see table definitions information of the table in <a href="/powerapps/developer/data-platform/reference/about-entity-reference">table/entity reference</a>.</li></ul>

<p><b>Column definitions for the <i>status</i> type</b><br/>
An object returned with the following properties in addition to the <i>base</i> column definitions type properties:</p>
<ul>
<li><b>Choice</b>: Object. Options for the column where each option is a key:value pair.</li></ul>
<p>The object also contains the following method:</p>
<ul>
<li><b>getState(arg)</b>: Returns the state value (number) for the specified status value (number). For default state and status values for a table, see table definitions information of the table in <a href="/powerapps/developer/data-platform/reference/about-entity-reference">table/entity reference</a>.</li>
</ul>
</td>
</tr>
</table>

### Related topics

[Xrm.Utility](../xrm-utility.md)



[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]