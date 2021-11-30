---
title: "Calculated and rollup columns (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn about common elements and characteristics, calculated columns, rollup columns, retrieve a calculated rollup column value immediately, and SourceTypeMasks enumeration." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 03/12/2021
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "mayadumesh" # GitHub ID
ms.subservice: dataverse-developer
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Calculated and rollup columns

*Calculated* and *rollup* columns free the user from having to manually perform calculations and focus on their work. System administrators can now easily define a field to contain the value of many common calculations without having to work with a developer. Developers can also leverage the platform capabilities to perform these calculations rather than within their own code.  

[!INCLUDE[cc-terminology](includes/cc-terminology.md)] 
  
<a name="BKMK_CommonElements"></a>   

## Common elements and characteristics  
 Calculated and rollup columns share some common elements and characteristics, for example:  
  
- They’re read-only.  
  
- They’re not specific to the user. The calculation is performed using a system user account, so the values may be based on records that the user doesn’t otherwise have privileges to view, such as columns that have field-level security enabled.  
  
  All columns that inherit from <xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata> have a <xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.SourceType> property that can contain the values shown in the following table.  
  
|                 Value                 |                                    Description                                     |
|---------------------------------------|------------------------------------------------------------------------------------|
| Null |       Not a valid type of column to be a calculated or rollup column.        |
|                   0                   | Simple column. The column isn’t defined as a calculated or rollup column. |
|                   1                   |                                Calculated column                                |
|                   2                   |                                  Rollup column                                  |
  
 Calculated and rollup columns are based on existing column types that inherit from <xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata>. The following types of column have new properties:  
  
- <xref:Microsoft.Xrm.Sdk.Metadata.BooleanAttributeMetadata>  
  
- <xref:Microsoft.Xrm.Sdk.Metadata.DateTimeAttributeMetadata>  
  
- <xref:Microsoft.Xrm.Sdk.Metadata.DecimalAttributeMetadata>  
  
- <xref:Microsoft.Xrm.Sdk.Metadata.IntegerAttributeMetadata>  
  
- <xref:Microsoft.Xrm.Sdk.Metadata.MoneyAttributeMetadata>  
  
- <xref:Microsoft.Xrm.Sdk.Metadata.PicklistAttributeMetadata>  
  
- <xref:Microsoft.Xrm.Sdk.Metadata.StringAttributeMetadata>  
  
  Each of these types of column have the following properties to support calculations and rollups.  
  
|      Property       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        Definition                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `FormulaDefinition` |                                                                                                                                                                                                                                                                                                                                                                                                                                                                   Contains the XAML definition of the formula used to perform the calculation or rollup. The only supported way to change this value is through the application formula editor.<br /><br /> For information about configuring the formulas for these columns see the following topics in the customization guide: [Define rollup columns](../../maker/data-platform/define-rollup-fields.md) and [Define calculated columns](../../maker/data-platform/define-calculated-fields.md).                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|  `SourceTypeMask`   | The bitmask value of this read-only property describes the types of sources used in the formula of the calculated column or if the formula of a calculated or rollup column is not valid.<br /><br /> -   0: **Undefined**. The default value for simple and rollup columns.<br />-   1: **Simple**. The calculated column refers to a column in the same record.<br />-   2: **Related**. The calculated column refers to a column in a related record.<br />-   4: `Logical`. The calculated column refers to a column in the same record which is actually stored in a different database table. More information: [Logical columns](/dynamics365/customer-engagement/developer/introduction-to-entity-attributes#BKMK_LogicalAttributes)<br />-   8: `Calculated`. The calculated column refers to another calculated column.<br />-   16: `Rollup`. The calculated column refers a rollup column.<br />-   32: `Invalid`. The calculated or rollup column is invalid.<br />     Typically this would be where a column refers to a column that no longer exists. **Note:**  One or more of these conditions may be true for any calculated or rollup column. Because this is a bitmask value, you may find it useful to use the [SourceTypeMasks enumeration](calculated-rollup-attributes.md#BKMK_SourceTypeMasks) when performing bitwise operations. |
  

## Calculated columns 
 
 Calculated columns are calculated in real-time when they are retrieved. Calculated columns can be composed using different data types. For example, an Integer calculated column may reference values from Decimal or Currency columns. More information: [Define calculated columns](../../maker/data-platform/define-calculated-fields.md).  
  
 Calculated column values are available in the retrieve plug-in pipeline. Post image of a table record update or create contains the calculated column value in stage 40. More information: [Event execution pipeline](event-framework.md#event-execution-pipeline) and [Entity images](understand-the-data-context.md#entity-images)
  
### Limitations  
 You can’t use values in calculated columns on a *logical value* in the same table to sort data returned by a query. Although your query can specify that the results should be ordered using a calculated column, the sort direction will be ignored and will not throw an error. If the calculated column references only simple values in the same record, sorting works normally. You can determine the sources used in a calculated column using the `SourceTypeMask` property on the column definitions. More information: [Logical columns](/dynamics365/customer-engagement/developer/introduction-to-entity-attributes.md#BKMK_LogicalAttributes)  
  
 Only columns from an immediate parent table can be used in a calculated column.  
  
 Saved queries, charts, and visualizations can have a maximum of 10 unique calculated columns.  
  
 Calculated columns can reference other calculated columns in their formula, but they can’t reference themselves.  
  
 Calculated columns don’t have values when a user with Dynamics 365 for Outlook is offline.  
  
 `MaxValue` and `MinValue` column definitions properties can’t be set on calculated columns  
  
<a name="BKMK_Rollup"></a>   

## Rollup columns  
 Because rollup columns persist in the database, they can be used for filtering or sorting just like regular columns. Any kind of process or plug-in will use the most recently calculated value of the column. Rollup column values are calculated asynchronously by scheduled system jobs. Administrators set when a job is run or pause the job. By default, each column is updated hourly. More information: [Define rollup columns](../../maker/data-platform/define-rollup-fields.md).  
  
 When a rollup column is created or updated a **Mass Calculated Rollup Fields** job is scheduled to run in 12 hours. The 12-hour delay is intended to perform this resource intensive operation during a time that will affect users the least. After the job completes, the next time it is scheduled to run will be 10 years in the future. If there is a problem with the calculation, this will be reported with the system job. Locate the system job in **Settings** > **System Jobs** to find any errors with rollup fields.  
  
> [!TIP]
>  As a developer testing a solution in a development environment you may not want to wait for 12 hours. You can make it happen faster. In the **System Jobs** list, use the **Recurring System Jobs** view to filter the list and locate the **Mass Calculate Rollup Fields** job. With the job selected, use **More Actions** > **Postpone** and set the time to something that occurs sooner.  
>   
>  If you want to trigger the creation of a new **Mass Calculated Rollup Fields** job programmatically, retrieve the <xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata> for the rollup column using <xref:Microsoft.Xrm.Sdk.Messages.RetrieveAttributeRequest> and use <xref:Microsoft.Xrm.Sdk.Messages.UpdateAttributeRequest> to update the column without making any actual changes.  
  
 The **Mass Calculated Rollup Fields** job will occur immediately when a solution containing a rollup column is imported. This assumes that you are installing a solution during a time that won’t adversely impact users.  
  
 Each rollup column for a table will also include two supporting columns for the rollup column:  
  
- *\<attribute SchemaName>* `_Date`: DateTime – When the rollup was last calculated.  
  
- *\<attribute SchemaName>* `_State`: Integer – The state of the rollup calculation. More information: [Rollup state values](calculated-rollup-attributes.md#BKMK_RollupStateValues)  
  
<a name="BKMK_RollupStateValues"></a>   

### Rollup state values  
 The state of a rollup column calculation is available in the corresponding *\<attribute SchemaName>*`_State` column and in the <xref:Microsoft.Crm.Sdk.Messages.CalculateRollupFieldResponse>.`FieldState` property. Values that indicate the state are shown in the following table.  
  
|State Value|Description|  
|-----------------|-----------------|  
|0|`NotCalculated`: Column value is yet to be calculated.|  
|1|`Calculated`: Column value has been calculated per the last update time in *\<attribute SchemaName>*`_Date` column.|  
|2|`OverflowError`: Column value calculation lead to overflow error.|  
|3|`OtherError`: Column value calculation failed due to an internal error, next run of calculation job will likely fix it.|  
|4|`RetryLimitExceeded`: Column value calculation failed because the maximum number of retry attempts to calculate the value were exceeded likely due to high number of concurrency and locking conflicts.|  
|5|`HierarchicalRecursionLimitReached`: Column value calculation failed because maximum hierarchy depth limit for calculation was reached.|  
|6|`LoopDetected`: Column value calculation failed because a recursive loop was detected in the hierarchy of the record.|  
  
### Retrieve a calculated rollup column value immediately  

 Rollup columns support a `CalculateRollupField` message that developers can use to calculate a rollup column value on demand. The request and response, along with the members, are shown in the following table.  
  
|Request/Response|Members|  
|-----------------------|-------------|  
|<xref:Microsoft.Crm.Sdk.Messages.CalculateRollupFieldRequest>|`Target`: <xref:Microsoft.Xrm.Sdk.EntityReference> for the record.<br /><br /> `FieldName`: String representing the logical name of the column.|  
|<xref:Microsoft.Crm.Sdk.Messages.CalculateRollupFieldResponse>|`Entity`: <xref:Microsoft.Xrm.Sdk.Entity> containing the rollup column and the supporting *\<attribute SchemaName>*`_Date` and *\<attribute SchemaName>*`_State` columns.|  
  
 This message is a synchronous operation for just the column identified in the request. If the value of that record is included as part of other rollup columns, the values of those columns won’t take the possible value change caused by calling this method into consideration until the regularly scheduled asynchronous jobs that perform those calculations occur.  
  
### Limitations  
 Rollup columns can’t be used as a workflow event or wait condition. These columns don’t raise the event to trigger workflows.  
  
 The ModifiedBy and ModifiedOn columns for the table aren’t updated when the rollup column is updated.  
  
 A maximum of 100 rollup columns can be defined within an organization. Each table can have no more than 10 rollup column.  
  
 A rollup column formula can’t reference another rollup column.  
  
 A rollup column formula can’t reference complex calculated column. Only calculated column that reference simple columns in the same record can be used with rollups.  
  
 A rollup column formula can’t include records in many-to-many (N:N) relationships. It can only include records in one-to-many (1:N) relationships.  
  
 Rollup column formulas can’t use one-to-many (1:N) relationships with the `ActivityPointer` or `ActivityParty` table.  
  
<a name="BKMK_SourceTypeMasks"></a>   

## SourceTypeMasks enumeration  
 The `SourceTypeMask` property for those columns that support calculated and rollup columns contains a bitmask value. To extract the relevant information from the value, it helps to have an enumeration when performing bitwise operations. Use the following `SourceTypeMasks` enumeration when comparing the `SourceTypeMask` property value.  
  
```csharp  
 public enum SourceTypeMasks  
{  
    /// <summary>  
    /// Undefined: 0 - The default value for simple and rollup columns.  
    /// </summary>  
    Undefined = 0,  
    /// <summary>  
    /// Simple: 1 - The calculated column refers to a column in the same record.  
    /// </summary>  
    Simple = 1,  
    /// <summary>  
    /// Related: 2 - The calculated column refers to a column in a related record.  
    /// </summary>  
    Related = 2,  
    /// <summary>  
    /// Logical: 4 - The calculated column refers to a logical column.  
    /// </summary>  
    Logical = 4,  
    /// <summary>  
    /// Calculated: 8 - The calculated column refers to another calculated column.  
    /// </summary>  
    Calculated = 8,  
    /// <summary>  
    /// Rollup: 16 - The calculated column refers a rollup column.   
    /// </summary>  
    Rollup = 16,  
    /// <summary>  
    /// Invalid: 32 - The calculated or rollup column is invalid.  
    /// Typically this would be where a field refers to a column that no longer exists.   
    /// </summary>  
    Invalid = 32  
}  
```  
  
### See also  
 [Video: Rollup and calculated columns in Dataverse](https://youtu.be/RoahCH1p3T8)   
 [Introduction to table columns](/dynamics365/customer-engagement/developer/introduction-to-entity-attributes)   
 [Define calculated columns](../../maker/data-platform/define-calculated-fields.md)   
 [Define rollup columns](../../maker/data-platform/define-rollup-fields.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
