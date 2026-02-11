---
title: Configure table relationship cascading behavior (Microsoft Dataverse) | Microsoft Docs
description: Configure cascading behaviors for a one-to-many relationship in Microsoft Dataverse to preserve data integrity and automate business processes.
suite: powerapps
author: MsSQLGirl
ms.author: jukoesma
ms.reviewer: jdaly
ms.topic: how-to
ms.date: 02/11/2026
ms.subservice: dataverse-developer
search.audienceType: 
  - developer
contributors:
 - JimDaly
---

# Configure table relationship cascading behavior  

You can configure cascading behaviors for a one-to-many relationship to preserve data integrity and automate business processes. Both Web API and SDK for .NET support configuring cascading behavior.

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]

## Use Web API to configure cascading behavior

When working with Web API, you define a one-to-many relationship by using the [OneToManyRelationshipMetadata entity type](xref:Microsoft.Dynamics.CRM.OneToManyRelationshipMetadata). This definition includes the name of the intersect table to create and how the relationship should appear in the application by using the [AssociatedMenuConfiguration complex type](xref:Microsoft.Dynamics.CRM.AssociatedMenuConfiguration), [Label complex type](xref:Microsoft.Dynamics.CRM.Label), and [LocalizedLabel complex type](xref:Microsoft.Dynamics.CRM.LocalizedLabel). 

For more information, see [Create a One-to-Many relationship using Web API](webapi/create-update-entity-relationships-using-web-api.md#create-a-one-to-many-relationship).

## Use SDK for .NET to configure cascading behavior

When you use the <xref:Microsoft.Xrm.Sdk.Messages.CreateOneToManyRequest> or <xref:Microsoft.Xrm.Sdk.Messages.UpdateRelationshipRequest> classes, include an instance of the [OneToManyRelationshipMetadata class](xref:Microsoft.Xrm.Sdk.Metadata.OneToManyRelationshipMetadata) in the body of the request. In the <xref:Microsoft.Xrm.Sdk.Metadata.OneToManyRelationshipMetadata.CascadeConfiguration> property of that class, use the <xref:Microsoft.Xrm.Sdk.Metadata.CascadeConfiguration> class.  

The [CascadeConfiguration class](xref:Microsoft.Xrm.Sdk.Metadata.CascadeConfiguration) or [CascadeConfiguration complex type](xref:Microsoft.Dynamics.CRM.CascadeConfiguration) contains the properties representing actions that might be performed on the referenced table in the one-to-many relationship. Each property can be assigned one of the values of the [CascadeType enum type](xref:Microsoft.Dynamics.CRM.CascadeType).  

|Value|Application label|Description|  
|-----------|-----------------------|-----------------|  
|Active|Cascade Active|Perform the action on all active referencing table records associated with the referenced table record.|  
|Cascade|Cascade All|Perform the action on all referencing table records associated with the referenced table record.|  
|NoCascade|Cascade None|Do nothing.|  
|RemoveLink|Remove Link|Remove the value of the referencing column for all referencing table records associated with the referenced table record.|  
|Restrict|Restrict|Prevent the referenced table record from being deleted when referencing tables exist.|  
|UserOwned|Cascade User Owned|Perform the action on all referencing table records owned by the same user as the referenced table record.|  

**Active records considered for cascading action**

Cascading actions on active records only include records that have a state code of **Active**. The following state codes for these tables are considered active for cascade actions. Different labels (other than **Active**) might be used for this state code in different tables. Any custom state or status code with values other than those in the following table isn't processed as an active record for cascading purposes.

| Table Name                       |    State Code 0       |    State Code 1       |    State Code 2       |    State Code 3       | 
| :--------------------------------| :----------------:    | :----------------:    | :----------------:    | :-----------------:    |
|  Account                         |          x            |                         |                         |                         |
|  BulkOperation                   |          x            |                         |                         |                         |
|  BulkOperation                   |          x            |                         |                         |                         |
|  CampaignResponse                |          x            |                         |                         |                         |
|  Contact                          |          x            |                         |                         |                         |
|  Email                            |          x            |                         |                         |                         |
|  Fax                               |          x            |                         |                         |                         |
|  Incident                          |          x            |                         |                         |                         |
|  IncidentResolution              |          x            |                         |                         |                         |
|  Invoice                          |          x            |                         |                         |                         |
|  Lead                               |          x            |                         |                         |                         |
|  Letter                            |          x            |                         |                         |                         |
|  Opportunity                      |          x            |                         |                         |                         |
|  OpportunityClose                 |          x            |                         |                         |                         |
|  OrderClose                        |          x            |                         |                         |                         |
|  PhoneCall                        |          x            |                         |                         |                         |
|  SalesOrder                        |          x            |                         |                         |                         |
|  Task                               |          x            |                         |                         |                         |
|  All Custom Tables and Custom Activities |          x            |                         |                         |                         |
|  Quotes                          |                       |          x            |                         |                        |
|  Contract                        |                       |                       |          x            |                         |
|  Appointment                     |                       |                         |                         |          x            |
|  ServiceAppointment              |                       |                         |                         |          x            |
|  RecurringAppointmentMaster      |                       |                         |                         |          x            |



The SDK for .NET [CascadeConfiguration class](xref:Microsoft.Xrm.Sdk.Metadata.CascadeConfiguration) or Web API [CascadeConfiguration complex type](xref:Microsoft.Dynamics.CRM.CascadeConfiguration) contains the following properties representing actions that you can perform on the referenced table in the one-to-many relationship.  
  
|Action|Description|Valid options|  
|------------|-----------------|-------------------|  
|Assign|Change the referenced table record owner and/or business unit.|Active<br />Cascade<br />NoCascade<br />UserOwned|  
|Delete|Delete the referenced table record. **Note:**  The options for this action are limited.|Cascade<br />RemoveLink<br />Restrict|  
|Merge|Merge the record with another record. **Note:**  For referenced tables that can be merged, Cascade is the only valid option. In other cases, use NoCascade.|Cascade<br />NoCascade|  
|Reparent|See [About the reparent action](#about-the-reparent-action) later.|Active<br />Cascade<br />NoCascade<br />UserOwned|  
|Share|When the referenced table record is shared with another user.|Active<br />Cascade<br />NoCascade<br />UserOwned|  
|Unshare|When sharing is removed for the referenced table record.|Active<br />Cascade<br />NoCascade<br />UserOwned|  

> [!NOTE]
> Assign, Delete, Merge, and Reparent actions won't execute in the following situations:
> - If the original parent record and requested action contain the same values. Example: Attempting to trigger an Assign and 
>   choosing a contact that is already the owner of the record
> - Attempting to perform an action on a parent record that is already running a cascading action


> [!NOTE]
> When executing an assign, any workflows or business rules that are currently active on the records will automatically be 
> deactivated when the reassignment occurs. The new owner of the record will need to reactivate the workflow or business rule 
> if they want to continue using it.

### About the assign action

When you update the parent record, the assign action cascades updates to the owner, the owning business unit, or both the owner and business unit to all child records.

#### Allowed record ownership across business units not enabled

When the [allow record ownership across business units](/power-platform/admin/wp-security-cds#to-enable-this-matrix-data-access-structure-preview) isn't enabled, you can't explicitly update the owning business unit column when changing the record's owner. The following list shows the cascading behaviors when you update the parent's record owner.

If you update the owner:

- Default cascade assign behavior (cascade all)
  - Record owner updates to the new owner
  - Record business unit updates to new owner's business unit
  - Child records' owner updates to the new owner
  - Child records' business unit updates to new owner's business unit
- Cascade assign set to None
  - Record owner updates to the new owner
  - Record business unit updates to new owner's business unit
  - Child records' owner doesn't update (no cascade)
  - Child records' business unit doesn't update (no cascade)

#### Allowed record ownership across business units is enabled

When [allow record ownership across business units](/power-platform/admin/wp-security-cds#to-enable-this-matrix-data-access-structure-preview) is enabled,
you can explicitly update the owning business unit column when changing the record's owner. The following list shows the cascading behaviors when you update the parent's record owner and the business unit.

Set **AlwaysMoveRecordToOwnerBusinessUnit** in [environment database settings](/power-platform/admin/environment-database-settings) or by using the [OrgDBOrgSettings tool for Microsoft Dynamics CRM](https://support.microsoft.com/help/2691237/orgdborgsettings-tool-for-microsoft-dynamics-crm).

1. If you update the owner:

   **AlwaysMoveRecordToOwnerBusinessUnit** = true (default)

   - Default cascade assign behavior (cascade all)
     - Record owner updates to the new owner
     - Record business unit updates to new owner's business unit
     - Child records' owner updates to the new owner
     - Child records' business unit updates to new owner's business unit
   - Cascade assign set to None
     - Record owner updates to the new owner
     - Record business unit updates to new owner's business unit
     - Child records' owner doesn't update (no cascade)
     - Child records' business unit doesn't update (no cascade)

1. If you update the business unit:

   **AlwaysMoveRecordToOwnerBusinessUnit** = true (default)

    - Default cascade assign behavior (cascade all)
      -   Record owner doesn't update
      -   Record business unit updates to new business unit
      -   Child records' owner doesn't update 
      -   Child records' business unit updates to new business unit
    - Cascade assign set to None
      -   Record owner doesn't update
      -   Record business unit updates to new business unit
      -   Child records' owner doesn't update 
      -   Child records' business unit doesn't update

1. If you update the owner and business unit:

   **AlwaysMoveRecordToOwnerBusinessUnit** = true (default)

   - Default cascade assign behavior (cascade all)
     - Record owner updates to the new owner
     - Update record business unit to new business unit
     - Child records' owner updates to the new owner
     - Update child records' business unit to new business unit
   - Cascade assign set to None
     - Record owner updates to the new owner
     - Update record business unit to new business unit
     - Don't update child records' owner
     - Don't update child records' business unit 

#### Change the cascade behaviors by using the OrgDBSettings AlwaysMoveRecordToOwnerBusinessUnit

If you set **AlwaysMoveRecordToOwnerBusinessUnit** to false, the user owned records' Business unit isn't moved to the new user's business unit.

Set **AlwaysMoveRecordToOwnerBusinessUnit** in [environment database settings](/power-platform/admin/environment-database-settings) or by using the [OrgDBOrgSettings tool for Microsoft Dynamics CRM](https://support.microsoft.com/help/2691237/orgdborgsettings-tool-for-microsoft-dynamics-crm).

1. If you update the owner:

   **AlwaysMoveRecordToOwnerBusinessUnit** = false

   - Default cascade assign behavior (cascade all)
     - Record owner updates to the new owner
     - Don't update record business unit 
     - Child records' owner updates to the new owner
     - Don't update child records' business unit 
   - Cascade assign set to None
     - Record owner updates to the new owner
     - Don't update record business unit 
     - Don't update child records' owner
     - Don't update child records' business unit 

1. If you update the business unit:

   **AlwaysMoveRecordToOwnerBusinessUnit** = false

   - Default cascade assign behavior (cascade all)
     -   Record owner doesn't update
     -   Record business unit updates to new business unit
     -   Child records' owner doesn't update 
     -   Child records' business unit updates to new business unit
   - Cascade assign set to None
     -   Record owner doesn't update
     -   Record business unit updates to new business unit
     -   Child records' owner doesn't update 
     -   Child records' business unit doesn't update

1. If you update the owner and business unit:

   **AlwaysMoveRecordToOwnerBusinessUnit** = false

   - Default cascade assign behavior (cascade all)
     - Record owner updates to the new owner
     - Update record business unit to new business unit
     - Child records' owner updates to the new owner
     - Update child records' business unit to new business unit
   - Cascade assign set to None
     - Record owner updates to the new owner
     - Update record business unit to new business unit
     - Don't update child records' owner
     - Don't update child records' business unit

> [!NOTE]
> When **AlwaysMoveRecordToOwnerBusinessUnit** = false
> 
> Privilege requirements:
> - The parent record's owner privilege is validated. When you update the owner or business unit, the validation checks that the owner has the privilege for the business unit before it allows the updates.
> - However, the record's owner privilege for the child records isn't validated. You might run into a situation where you update the parent record's business unit and the business unit cascades down to the child records, the owner of the child records loses access to their record.
> 
> **Example 1**
> 
> A parent record belongs to owner 1 in business unit A and it has child records belonging to owner 2 in business unit B.  Owner 1 is assigned a security role from business units A and B and therefore can access the child records.  When you update the parent record to owner 3, the child records' owner also changes to owner 3 but the child records still belong to business unit B.  Owner 3 doesn't have access to these child records unless the owner has a security role in business unit B.
> 
> **Example 2**
> 
> A parent record belongs to owner 1 in business unit A and it has child records belonging to owner 2 in business unit B.  Owner 1 is assigned a security role from business units A, B, and C and therefore can access the child records. When you change the owning business unit to business unit C, the child records' business unit changes to business unit C.  Owner 2 of these child records doesn't have access to their records unless the owner is assigned a security role from business unit C.

<a name="BKMK_ReparentAction"></a>   

### About the reparent action

The reparent action is similar to the share action, but it deals with inherited access rights instead of explicit access rights. The reparent action occurs when you change the value of the referencing column in a parental relationship. When a reparent action occurs, the desired scope of the inherited access rights might change for `ReadAccess`, `WriteAccess`, `DeleteAccess`, `AssignAccess`, `ShareAccess`, `AppendAccess`, and `AppendToAccess` for related tables. It doesn't change for `CreateAccess`. The cascade actions related to the reparent action refer to changes to access rights indicated earlier for the table record and any table records related to it.  

<a name="BKMK_MergeAction"></a>

### About the merge action

A merge action can encounter problems completing if a record that is part of the operation set is deleted while the merge system job is running. Often, this problem results in an error that indicates the record is "differently parented" or the child record "might lose its parenting". If this problem occurs, and you prefer the merge to continue even if the record is missing, you can choose to disable the parent check when you select the columns to merge.


> [!NOTE]
> When you perform a merge between two custom tables, DateTime values don't merge. The DateTime of the target record remains unchanged.

## Cascade notification

Use two cascade async notification helper messages to notify a user or log when a cascading asynchronous job fails or succeeds. To implement this solution, write and register a custom plug-in that executes when those messages are processed and provides success or failure notification.

The two notification messages are:

|Name|Description|
|---------|---------|
|`cascadeAsync_FailureAPI`|This message is processed (executed) when an asynchronous cascade job pauses due to multiple failures. Use this message to inform users they need to review their dataset for problems with existing plug-ins, data problems, or workflow problems.<br />**InputParameters**:<br />`casadeAsyncExceptionDetails`: Details of the exception causing cascade async job failure.<br />`casadeAsyncJobName`:Name of the cascade async job.|
|`cascadeAsync_SuccessAPI`|This message is processed (executed) when the asynchronous cascade job is successfully completed.<br />**InputParameters**:<br />`casadeAsync_JobName`: Name of the cascade async job.|

Register the custom plug-in during the post-operation stage and set it to asynchronous mode. The following figure shows an example plug-in registration by using the Plug-in Registration tool.

:::image type="content" source="media/plugin-cascade-notification.png" alt-text="Register a plug-in for cascade notification":::

Here are some examples of the kind of notifications that your custom plug-in can provide:

- On success, add an entry to a run-time log.
- On failure, add an entry to a run-time log, and then send an email (or other communication) to the administrator indicating the date and time and nature of the failure.
- Display a message to the interactive user.

## Inherited access repair

After changing the cascading behavior of a table relationship for the **Reparent** or **Share** actions to **No Cascade**, the system tries to adjust user's inherited access rights to match the current table relationship cascading behavior. [Learn more about inherited access rights cleanup](../../maker/data-platform/create-edit-entity-relationships.md#inherited-access-rights-cleanup).

However, if this approach isn't successful, users might retain access to related records that should be removed. For steps to address this problem, see [Clean up inherited access](/troubleshoot/power-platform/power-apps/dataverse/cleanup-inherited-access).


### See also

[Table relationship definitions](entity-relationship-metadata.md)  



[!INCLUDE[footer-include](../../includes/footer-banner.md)]
