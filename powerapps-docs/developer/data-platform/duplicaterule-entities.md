---
title: "Duplicate rule tables (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Read about tables containing data that define duplicate detection rules." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 03/26/2021
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "mayadumesh" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Duplicate rule tables

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]

For information about how to configure duplicate rules in the application, see [Administrators Guide: Set up duplicate detection rules to keep your data clean](/dynamics365/customer-engagement/admin/set-up-duplicate-detection-rules-keep-data-clean).

Duplicate detection rules are defined using the following tables:

- [DuplicateRule](reference/entities/duplicaterule.md): To detect duplicates in the system, create a *duplicate detection rule* for a specific table type. You can create multiple detection rules for the same table type. However, you can publish a maximum of five duplicate detection rules per table type at one time.  
- [DuplicateRuleCondition](reference/entities/duplicaterulecondition.md): A rule can have one or more *duplicate detection rule conditions* that are represented by the table. The conditions are combined by the system as in logical `AND` operation. A duplicate detection rule specifies a base table type and a matching table type. A duplicate rule condition specifies the name of a base column and the name of a matching column. For example, specify an account as a base table and a contact as a matching table to compare last names and addresses. The matching criteria consist of operators such as exactly match, first n-number of characters, or last n-number of characters. 


These two tables are related using the [DuplicateRule_DuplicateRuleConditions](/reference/entities/duplicaterule.md#BKMK_DuplicateRule_DuplicateRuleConditions) relationship.

Duplicate detection works by comparing generated match codes of existing records with each new record being created. These match codes are created as each new record is created. Therefore, there is potential for one or more duplicate records to be created if they are processed at the exact same moment. In addition to detecting duplicates as they are created, you should schedule duplicate detection jobs to check for other potential duplicate records.
 
 The duplicate detection rules are system-wide. You must publish them before running a duplicate detection job to detect duplicates for bulk data or retrieve duplicates for a particular table record. To publish a duplicate detection rule, use the `PublishDuplicateRule` message(<xref href="Microsoft.Dynamics.CRM.PublishDuplicateRule?text=PublishDuplicateRule Action" /> or <xref:Microsoft.Crm.Sdk.Messages.PublishDuplicateRuleRequest>). Duplicate rule publishing is an asynchronous operation that runs in the background.

The following writable columns in these tables control the behavior of duplicate detection rules.

## DuplicateRule

|Column|Description|
|-|-|
|[BaseEntityName](/reference/entities/duplicaterule.md#BKMK_BaseEntityName)| Record type of the record being evaluated for potential duplicates.|
|[Description](/reference/entities/duplicaterule.md#BKMK_Description)|Description of the duplicate detection rule.|
|[DuplicateRuleId](/reference/entities/duplicaterule.md#BKMK_DuplicateRuleId)|Unique identifier of the duplicate detection rule.|
|[ExcludeInactiveRecords](/reference/entities/duplicaterule.md#BKMK_ExcludeInactiveRecords)|Determines whether to flag inactive records as duplicates.<br /> **Note**: <br />The default value is `false`. Set it to `true` if you do not want inactive records to be flagged as duplicates, even if they meet duplication detection rule criteria. <br /> More information: [Inactive states](#inactive-states)|
|[IsCaseSensitive](/reference/entities/duplicaterule.md#BKMK_IsCaseSensitive)|Indicates if the operator is case-sensitive.|
|[MatchingEntityName](/reference/entities/duplicaterule.md#BKMK_MatchingEntityName)|Record type of the records being evaluated as potential duplicates.|
|[Name](/reference/entities/duplicaterule.md#BKMK_Name)|Name of the duplicate detection rule.|
|[OwnerId](/reference/entities/duplicaterule.md#BKMK_OwnerId)|Unique identifier of the user or team who owns the duplicate detection rule.|
|[OwnerIdType](/reference/entities/duplicaterule.md#BKMK_OwnerIdType)|Whether the owner is a user or a team.|
|[StatusCode](/reference/entities/duplicaterule.md#BKMK_StatusCode)|Reason for the status of the duplicate detection rule.|

### Inactive states

Most system tables and all custom tables have two `StateCode` column choices:

- `Value`: 0 `InvariantName`: `Active`
- `Value`: 1 `InvariantName`: `Inactive`

The label of the choice may be changed, but the `InvariantName` value will not.

Some system tables will have more than one active or inactive state.The following table lists examples of tables with more than one active or inactive state.

| StateCode |Active State(s)|Inactive State(s)|  
|--|--|--|  
|[Appointment.StateCode](/reference/entities/appointment.md#BKMK_StateCode)|`Open`, `Scheduled`|`Completed`, `Canceled`|  
|[CampaignActivity.StateCode](/reference/entities/CampaignActivity.md#BKMK_StateCode)|`Open`|`Closed`, `Canceled`|  
|[CampaignResponse.StateCode](/reference/entities/CampaignResponse.md#BKMK_StateCode)|`Open`|`Completed`, `Canceled`|  
|[Contract.StateCode](/reference/entities/Contract.md#BKMK_StateCode)|`Draft`, `Invoiced`, `On Hold`|`Canceled`, `Expired`|  
|[ContractDetail.StateCode](/reference/entities/ContractDetail.md#BKMK_StateCode)|`Existing`, `Renewed`|`Canceled`, `Expired`|  
|[Email.StateCode](/reference/entities/Email.md#BKMK_StateCode)|`Open`|`Completed`, `Canceled`|  
|[Fax.StateCode](/reference/entities/Fax.md#BKMK_StateCode)|`Open`|`Completed`, `Canceled`|  
|[Incident.StateCode](/reference/entities/Incident.md#BKMK_StateCode)|`Active`|`Resolved`, `Canceled`, `Closed`|  
|[Invoice.StateCode](/reference/entities/Invoice.md#BKMK_StateCode)|`Active`|`Closed`, `Paid`, `Canceled`|  
|[KbArticle.StateCode](/reference/entities/KbArticle.md#BKMK_StateCode)|`Draft`, `Unapproved`, `Published`|N/A|  
|[Lead.StateCode](/reference/entities/Lead.md#BKMK_StateCode)|`Open`|`Qualified`, `Disqualified`|  
|[Letter.StateCode](/reference/entities/Letter.md#BKMK_StateCode)|`Open`|`Completed`, `Canceled`|  
|[Opportunity.StateCode](/reference/entities/Opportunity.md#BKMK_StateCode)|`Open`|`Won`, `Lost`|  
|[PhoneCall.StateCode](/reference/entities/PhoneCall.md#BKMK_StateCode)|`Open`|`Completed`, `Canceled`|  
|[Quote.StateCode](/reference/entities/Quote.md#BKMK_StateCode)|`Draft`, `Active`|`Won`, `Closed`|  
|[SalesOrder.StateCode](/reference/entities/SalesOrder.md#BKMK_StateCode)|`Active`, `Submitted`, `Invoiced`|`Canceled`, `Fulfilled`|  
|[ServiceAppointment.StateCode](/reference/entities/ServiceAppointment.md#BKMK_StateCode)|`Open`, `Scheduled`|`Closed`, `Canceled`|  
|[Task.StateCode](/reference/entities/Task.md#BKMK_StateCode)|`Open`|`Completed`, `Canceled`|  

 For example, if you set the `ExcludeInactiveRecords` column to `true`, only `Active`, `Submitted`, and `Invoiced` sales orders will be considered for matching during duplicate detection. 


> [!NOTE]
> You can review the available `StateCode` choices for a table using the Metadata Browser described in [Browse the table and column definitions for your organization](browse-your-metadata.md).
>
> To retrieve the `StateCode` choices for a table you can use the following Web API query  by substituting the `LogicalName` of the table with `appointment` used below:
> ```HTTP
> GET [organization URI]/api/data/v9.0/EntityDefinitions(LogicalName='appointment')/Attributes(LogicalName='statecode')/Microsoft.Dynamics.CRM.StateAttributeMetadata/OptionSet?$select=Options
> ```

## DuplicateRule Special messages

[DuplicateRule](/reference/entities/duplicaterule.md) is a user-owned table and normal create, retrieve, update, assign, and delete operations are allowed as well as operations to control access. More information: [DuplicateRule Messages](/reference//reference/entities/duplicaterule.md#messages).

The following special messages can also be used:

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|CompoundUpdateDuplicateDetectionRule|<xref href="Microsoft.Dynamics.CRM.CompoundUpdateDuplicateDetectionRule?text=CompoundUpdateDuplicateDetectionRule Action" />|<xref:Microsoft.Crm.Sdk.Messages.CompoundUpdateDuplicateDetectionRuleRequest>|
|PublishDuplicateRule|<xref href="Microsoft.Dynamics.CRM.PublishDuplicateRule?text=PublishDuplicateRule Action" />|<xref:Microsoft.Crm.Sdk.Messages.PublishDuplicateRuleRequest>|
|PublishXml|<xref href="Microsoft.Dynamics.CRM.PublishXml?text=PublishXml Action" />|<xref:Microsoft.Crm.Sdk.Messages.PublishXmlRequest>|
|UnpublishDuplicateRule|<xref href="Microsoft.Dynamics.CRM.UnpublishDuplicateRule?text=UnpublishDuplicateRule Action" />|<xref:Microsoft.Crm.Sdk.Messages.UnpublishDuplicateRuleRequest>|


## DuplicateRuleCondition

|Column|Description|
|-|-|
|[BaseAttributeName](/reference/entities/duplicaterulecondition.md#BKMK_BaseAttributeName)|Field that is being compared.|
|[DuplicateRuleConditionId](/reference/entities/duplicaterulecondition.md#BKMK_DuplicateRuleConditionId)|Unique identifier of the condition.|
|[IgnoreBlankValues](/reference/entities/duplicaterulecondition.md#BKMK_IgnoreBlankValues)|Determines whether to consider blank values as non-duplicate values. <br /> **Note**: <br />The default value of this column is `false`. Set it to `true` if you do not want the duplicate detection rule to consider `null` values as equal. <br /> **Important**: <br /> For a duplicate detection rule with one condition, if you set the column value to `false`, it is treated by the system as a `true` value. |
|[MatchingAttributeName](/reference/entities/duplicaterulecondition.md#BKMK_MatchingAttributeName)|Field that is being compared with the base field.|
|[OperatorCode](/reference/entities/duplicaterulecondition.md#BKMK_OperatorCode)|Operator for this rule condition.<br /> **Important**: <br />If you set the `OperatorCode` column to `ExactMatch`, don’t set the `OperatorParam` column to any value|
|[OperatorParam](/reference/entities/duplicaterulecondition.md#BKMK_OperatorParam)|Parameter value of N if the operator is Same First Characters or Same Last Characters.<br /> **Important**: <br />Don’t set the `OperatorParam` to zero during create or update operations.|
|[RegardingObjectId](/reference/entities/duplicaterulecondition.md#BKMK_RegardingObjectId)|Unique identifier of the object with which the condition is associated.|

## DuplicateRuleCondition Special messages

[DuplicateRuleCondition](/reference/entities/duplicaterulecondition.md) is a child table to `DuplicateRule`. Access to retrieve or modify these tables is dependent on access to the `DuplicateRule` it is associated with. More information: [DuplicateRuleCondition Messages](/reference/entities/duplicaterulecondition.md#messages).

The following special messages can also be used:

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|CompoundUpdateDuplicateDetectionRule|<xref href="Microsoft.Dynamics.CRM.CompoundUpdateDuplicateDetectionRule?text=CompoundUpdateDuplicateDetectionRule Action" />|<xref:Microsoft.Crm.Sdk.Messages.CompoundUpdateDuplicateDetectionRuleRequest>|


### See also
<xref href="Microsoft.Dynamics.CRM.duplicaterule?text=duplicaterule EntityType" /><br/><xref href="Microsoft.Dynamics.CRM.duplicaterulecondition?text=duplicaterulecondition EntityType" /><br/><a href="detect-duplicate-data-with-code.md" data-raw-source="[Detect duplicate data](detect-duplicate-data-with-code.md)">Detect duplicate data</a><br />
<a href="enable-disable-duplicate-detection.md" data-raw-source="[Enable and disable duplicate detection](enable-disable-duplicate-detection.md)">Enable and disable duplicate detection</a><br />
<a href="run-duplicate-detection.md" data-raw-source="[Run duplicate detection](run-duplicate-detection.md)">Run duplicate detection</a><br />
<a href="duplicate-detection-messages.md" data-raw-source="[Duplicate detection messages](duplicate-detection-messages.md)">Duplicate detection messages</a><br />
<a href="org-service/samples/enable-duplicate-detection-and-retrieve-duplicates.md" data-raw-source="[Sample: Enable duplicate detection and retrieve duplicates](org-service/samples/enable-duplicate-detection-and-retrieve-duplicates.md)">Sample: Enable duplicate detection and retrieve duplicates</a><br />
<a href="org-service/samples/use-duplicate-detection-when-creating-and-updating-records.md" data-raw-source="[Sample: Use duplicate detection when creating and updating records](org-service/samples/use-duplicate-detection-when-creating-and-updating-records.md)">Sample: Use duplicate detection when creating and updating records</a><br />
<a href="/dynamics365/customer-engagement/developer/org-service/sample-detect-multiple-duplicate-records" data-raw-source="[Sample: Detect multiple duplicate records](org-service/samples/detect-multiple-duplicate-records.md)">Sample: Detect multiple duplicate records</a><br />


[!INCLUDE[footer-include](../../includes/footer-banner.md)]