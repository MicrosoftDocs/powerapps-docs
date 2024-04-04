---
title: "Duplicate rule tables (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Read about tables containing data that define duplicate detection rules." # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 10/05/2023
ms.reviewer: pehecke
ms.topic: article
author: mayadumesh # GitHub ID
ms.subservice: dataverse-developer
ms.author: mayadu # MSFT alias of Microsoft employees only
search.audienceType: 
  - developer
---

# Duplicate rule tables

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]

For information about how to configure duplicate rules in the application, see [Administrators Guide: Set up duplicate detection rules to keep your data clean](/power-platform/admin/set-up-duplicate-detection-rules-keep-data-clean).

Duplicate detection rules are defined using the following tables:

- [DuplicateRule](reference/entities/duplicaterule.md): To detect duplicates in the system, create a *duplicate detection rule* for a specific table type. You can create multiple detection rules for the same table type. However, you can publish a maximum of five duplicate detection rules per table type at one time.  
- [DuplicateRuleCondition](reference/entities/duplicaterulecondition.md): A rule can have one or more *duplicate detection rule conditions* that are represented by the table. The conditions are combined by the system as in logical `AND` operation. A duplicate detection rule specifies a base table type and a matching table type. A duplicate rule condition specifies the name of a base column and the name of a matching column. For example, specify an account as a base table and a contact as a matching table to compare last names and addresses. The matching criteria consist of operators such as exactly match, first n-number of characters, or last n-number of characters. 


These two tables are related using the [DuplicateRule_DuplicateRuleConditions](reference/entities/duplicaterule.md#BKMK_DuplicateRule_DuplicateRuleConditions) relationship.

Duplicate detection works by comparing generated match codes of existing records with each new record being created. These match codes are created as each new record is created. Therefore, there's potential for one or more duplicate records to be created if they're processed at the exact same moment. In addition to detecting duplicates as they're created, you should schedule duplicate detection jobs to check for other potential duplicate records.
 
The duplicate detection rules are system-wide. You must publish them before running a duplicate detection job to detect duplicates for bulk data or retrieve duplicates for a particular table record. To publish a duplicate detection rule, use the `PublishDuplicateRule` message(<xref:Microsoft.Dynamics.CRM.PublishDuplicateRule?text=PublishDuplicateRule Action> or <xref:Microsoft.Crm.Sdk.Messages.PublishDuplicateRuleRequest>). Duplicate rule publishing is an asynchronous operation that runs in the background.

The following writable columns in these tables control the behavior of duplicate detection rules.

## DuplicateRule

|Column|Description|
|------|-----------|
|[BaseEntityName](reference/entities/duplicaterule.md#BKMK_BaseEntityName)| Record type of the record being evaluated for potential duplicates.|
|[Description](reference/entities/duplicaterule.md#BKMK_Description)|Description of the duplicate detection rule.|
|[DuplicateRuleId](reference/entities/duplicaterule.md#BKMK_DuplicateRuleId)|Unique identifier of the duplicate detection rule.|
|[ExcludeInactiveRecords](reference/entities/duplicaterule.md#BKMK_ExcludeInactiveRecords)|Determines whether to flag inactive records as duplicates.<br /> **Note**: <br />The default value is `false`. Set it to `true` if you don't want inactive records to be flagged as duplicates, even if they meet duplication detection rule criteria. <br /> More information: [Inactive states](#inactive-states)|
|[IsCaseSensitive](reference/entities/duplicaterule.md#BKMK_IsCaseSensitive)|Indicates if the operator is case-sensitive.|
|[MatchingEntityName](reference/entities/duplicaterule.md#BKMK_MatchingEntityName)|Record type of the records being evaluated as potential duplicates.|
|[Name](reference/entities/duplicaterule.md#BKMK_Name)|Name of the duplicate detection rule.|
|[OwnerId](reference/entities/duplicaterule.md#BKMK_OwnerId)|Unique identifier of the user or team who owns the duplicate detection rule.|
|[OwnerIdType](reference/entities/duplicaterule.md#BKMK_OwnerIdType)|Whether the owner is a user or a team.|
|[StatusCode](reference/entities/duplicaterule.md#BKMK_StatusCode)|Reason for the status of the duplicate detection rule.|

### Inactive states

Most system tables and all custom tables have two `StateCode` column choices:

- `Value`: 0 `InvariantName`: `Active`
- `Value`: 1 `InvariantName`: `Inactive`

The label of the choice may be changed, but the `InvariantName` value won't.

Some system tables have more than one active or inactive state. The following table lists examples of tables with more than one active or inactive state.

| StateCode |Active State(s)|Inactive State(s)|  
|-----------|---------------|-----------------|  
|[Appointment.StateCode](reference/entities/appointment.md#BKMK_StateCode)|`Open`, `Scheduled`|`Completed`, `Canceled`|  
|CampaignActivity.StateCode|`Open`|`Closed`, `Canceled`|  
|CampaignResponse.StateCode|`Open`|`Completed`, `Canceled`|  
|Contract.StateCode|`Draft`, `Invoiced`, `On Hold`|`Canceled`, `Expired`|  
|ContractDetail.StateCode|`Existing`, `Renewed`|`Canceled`, `Expired`|  
|[Email.StateCode](reference/entities/Email.md#BKMK_StateCode)|`Open`|`Completed`, `Canceled`|  
|[Fax.StateCode](reference/entities/Fax.md#BKMK_StateCode)|`Open`|`Completed`, `Canceled`|  
|Incident.StateCode|`Active`|`Resolved`, `Canceled`, `Closed`|  
|Invoice.StateCode|`Active`|`Closed`, `Paid`, `Canceled`|  
|[KbArticle.StateCode](reference/entities/KbArticle.md#BKMK_StateCode)|`Draft`, `Unapproved`, `Published`|N/A|  
|Lead.StateCode|`Open`|`Qualified`, `Disqualified`|  
|[Letter.StateCode](reference/entities/Letter.md#BKMK_StateCode)|`Open`|`Completed`, `Canceled`|  
|Opportunity.StateCode|`Open`|`Won`, `Lost`|  
|[PhoneCall.StateCode](reference/entities/PhoneCall.md#BKMK_StateCode)|`Open`|`Completed`, `Canceled`|  
|Quote.StateCode|`Draft`, `Active`|`Won`, `Closed`|  
|SalesOrder.StateCode|`Active`, `Submitted`, `Invoiced`|`Canceled`, `Fulfilled`|  
|ServiceAppointment.StateCode|`Open`, `Scheduled`|`Closed`, `Canceled`|  
|[Task.StateCode](reference/entities/Task.md#BKMK_StateCode)|`Open`|`Completed`, `Canceled`|  

 For example, if you set the `ExcludeInactiveRecords` column to `true`, only `Active`, `Submitted`, and `Invoiced` sales orders are considered for matching during duplicate detection. 


> [!NOTE]
> You can review the available `StateCode` choices for a table using the Metadata Browser described in [Browse the table and column definitions for your organization](browse-your-metadata.md).
>
> To retrieve the `StateCode` choices for a table you can use the following Web API query  by substituting the `LogicalName` of the table with `appointment` used below:
> ```HTTP
> GET [organization URI]/api/data/v9.0/EntityDefinitions(LogicalName='appointment')/Attributes(LogicalName='statecode')/Microsoft.Dynamics.CRM.StateAttributeMetadata/OptionSet?$select=Options
> ```

## DuplicateRule Special messages

[DuplicateRule](reference/entities/duplicaterule.md) is a user-owned table and normal create, retrieve, update, assign, and delete operations are allowed as well as operations to control access. More information: [DuplicateRule Messages](reference/entities/duplicaterule.md#messages).

The following special messages can also be used:

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|CompoundUpdateDuplicateDetectionRule|<xref:Microsoft.Dynamics.CRM.CompoundUpdateDuplicateDetectionRule?text=CompoundUpdateDuplicateDetectionRule Action>|<xref:Microsoft.Crm.Sdk.Messages.CompoundUpdateDuplicateDetectionRuleRequest>|
|PublishDuplicateRule|<xref:Microsoft.Dynamics.CRM.PublishDuplicateRule?text=PublishDuplicateRule Action>|<xref:Microsoft.Crm.Sdk.Messages.PublishDuplicateRuleRequest>|
|PublishXml|<xref:Microsoft.Dynamics.CRM.PublishXml?text=PublishXml Action>|<xref:Microsoft.Crm.Sdk.Messages.PublishXmlRequest>|
|UnpublishDuplicateRule|<xref:Microsoft.Dynamics.CRM.UnpublishDuplicateRule?text=UnpublishDuplicateRule Action>|<xref:Microsoft.Crm.Sdk.Messages.UnpublishDuplicateRuleRequest>|


## DuplicateRuleCondition

|Column|Description|
|------|-----------|
|[BaseAttributeName](reference/entities/duplicaterulecondition.md#BKMK_BaseAttributeName)|Field that is being compared.|
|[DuplicateRuleConditionId](reference/entities/duplicaterulecondition.md#BKMK_DuplicateRuleConditionId)|Unique identifier of the condition.|
|[IgnoreBlankValues](reference/entities/duplicaterulecondition.md#BKMK_IgnoreBlankValues)|Determines whether to consider blank values as nonduplicate values. <br /> **Note**: <br />The default value of this column is `false`. Set it to `true` if you don't want the duplicate detection rule to consider `null` values as equal. <br /> **Important**: <br /> For a duplicate detection rule with one condition, if you set the column value to `false`, it's treated by the system as a `true` value. |
|[MatchingAttributeName](reference/entities/duplicaterulecondition.md#BKMK_MatchingAttributeName)|Field that is being compared with the base field.|
|[OperatorCode](reference/entities/duplicaterulecondition.md#BKMK_OperatorCode)|Operator for this rule condition.<br /> **Important**: <br />If you set the `OperatorCode` column to `ExactMatch`, don't set the `OperatorParam` column to any value|
|[OperatorParam](reference/entities/duplicaterulecondition.md#BKMK_OperatorParam)|Parameter value of N if the operator is Same First Characters or Same Last Characters.<br /> **Important**: <br />Don't set the `OperatorParam` to zero during create or update operations.|
|[RegardingObjectId](reference/entities/duplicaterulecondition.md#BKMK_RegardingObjectId)|Unique identifier of the object with which the condition is associated.|

## DuplicateRuleCondition Special messages

[DuplicateRuleCondition](reference/entities/duplicaterulecondition.md) is a child table to `DuplicateRule`. Access to retrieve or modify these tables is dependent on access to the `DuplicateRule` it's associated with. More information: [DuplicateRuleCondition Messages](reference/entities/duplicaterulecondition.md#messages).

The following special messages can also be used:

|Message|Web API Operation|SDK Assembly|
|-------|-----------------|------------|
|CompoundUpdateDuplicateDetectionRule|<xref:Microsoft.Dynamics.CRM.CompoundUpdateDuplicateDetectionRule?text=CompoundUpdateDuplicateDetectionRule Action>|<xref:Microsoft.Crm.Sdk.Messages.CompoundUpdateDuplicateDetectionRuleRequest>|


### See also

<xref:Microsoft.Dynamics.CRM.duplicaterule?text=duplicaterule EntityType><br/>
<xref:Microsoft.Dynamics.CRM.duplicaterulecondition?text=duplicaterulecondition EntityType><br/>
[Detect duplicate data using code](detect-duplicate-data-with-code.md)<br />
[Enable and disable duplicate detection](enable-disable-duplicate-detection.md)<br />
[Run duplicate detection](run-duplicate-detection.md)<br />
[Duplicate detection messages](duplicate-detection-messages.md)<br />
[Sample: Enable duplicate detection and retrieve duplicates](org-service/samples/enable-duplicate-detection-and-retrieve-duplicates.md)<br />
[Sample: Use duplicate detection when creating and updating records](org-service/samples/use-duplicate-detection-when-creating-and-updating-records.md)<br />
[Sample: Detect multiple duplicate records](org-service/samples/detect-multiple-duplicate-records.md)<br />


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
