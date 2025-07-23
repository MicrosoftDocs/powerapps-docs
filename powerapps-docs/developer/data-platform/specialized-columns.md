---
title: Specialized columns using code
description: "Learn about common elements and characteristics that formula, calculated, rollup, and prompt columns use. Learn how to retrieve a calculated rollup column value immediately, and about the SourceTypeMasks enumeration." 
ms.date: 07/23/2025
ms.reviewer: jdaly
ms.topic: article
author: MsSQLGirl
ms.subservice: dataverse-developer
ms.author: jukoesma
search.audienceType: 
  - developer
contributors:
 - JimDaly
 - sanjeevgoyalmsft
---
# Specialized columns using code

*Formula*, *calculated*, *rollup*, and *prompt* columns free the user from having to manually perform calculations and focus on their work. System administrators can define a field to contain the value of many common calculations without having to work with a developer. Developers can also use the platform capabilities to perform these calculations rather than with code.

This article focuses on how these columns are defined in the column definitions and APIs to interact with rollup columns. We don't support defining the formulas with code. You need to use [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) to set the formulas for the respective type of column. Learn how:

- [Work with formula columns (preview)](../../maker/data-platform/formula-columns.md)
- [Define calculated columns to automate calculations](../../maker/data-platform/define-calculated-fields.md)
- [Define rollup columns that aggregate values](../../maker/data-platform/define-rollup-fields.md)
  
<a name="BKMK_CommonElements"></a>

## Common elements and characteristics

Formula, calculated, and rollup columns share some common elements and characteristics, for example:  
  
- They're read-only.  
- They're not specific to the user.   
   The calculation is performed using a system user account, so the values may be based on records that the user doesn't otherwise have privileges to view, such as columns that have field-level security enabled.  
  
All columns that inherit from <xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata> have a <xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.SourceType> property that can contain the values shown in the following table.  
  
|Value|Description |
|-----|-----|
| Null |Not a valid type of column to be a formula, calculated, or rollup column.|
|0| Simple column. The column isn't defined as a formula, calculated, or rollup column.|
|1|Calculated column|
|2|Rollup column|
|3|Formula column|
|4|Prompt column|

  
Formula, calculated, rollup, and prompt columns are based on existing column types that inherit from <xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata>. The following tables show the available column types and which source types are supported:


|Type|Supported source types|
|---------|---------|
|<xref:Microsoft.Xrm.Sdk.Metadata.BooleanAttributeMetadata>|Formula, Calculated, & Rollup|
|<xref:Microsoft.Xrm.Sdk.Metadata.DateTimeAttributeMetadata> |Formula, Calculated, & Rollup|
|<xref:Microsoft.Xrm.Sdk.Metadata.DecimalAttributeMetadata>|Formula, Calculated, & Rollup|
|<xref:Microsoft.Xrm.Sdk.Metadata.StringAttributeMetadata>|Formula, Calculated, Rollup, & Prompt|
|<xref:Microsoft.Xrm.Sdk.Metadata.IntegerAttributeMetadata>|Calculated & Rollup only|
|<xref:Microsoft.Xrm.Sdk.Metadata.MoneyAttributeMetadata>|Calculated & Rollup only|
|<xref:Microsoft.Xrm.Sdk.Metadata.PicklistAttributeMetadata>|Calculated & Rollup only|

Each of these types of column has the following properties to support formulas, calculations, and rollups. 
  
| Property  |Definition|
|---------|--------|
|`FormulaDefinition`| Contains the definition of the formula used to perform the calculation or rollup. Formula columns are defined using YAML. Calculated and rollup columns are defined using XAML. The only supported way to change this value is through the [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) editor.|
|`SourceTypeMask`| The bitmask value of this read-only property describes the types of sources used in the formula of the column or if the formula of the column isn't valid.<br /><br /> -   0: `Undefined`. The default value for simple and rollup columns.<br />-   1: `Simple`. The formula or calculated column refers to a column in the same record.<br />-   2: `Related`. The formula or calculated column refers to a column in a related record.<br />-   4: `Logical`. The formula or calculated column refers to a column in the same record that is stored in a different database table. More information: [Logical columns](entity-attribute-metadata.md#logical-columns)<br />-   8: `Calculated`. The formula or calculated column refers to another formula or calculated column.<br />-   16: `Rollup`. The formula or calculated column refers a rollup column.<br />-   32: `Invalid`. The formula, calculated, or rollup column is invalid.<br />Typically, a column is invalid when it refers to a column that no longer exists.<br /><br />**Note:**  One or more of these conditions may be true for any calculated or rollup column. Because this is a bitmask value, you may find it useful to use the [SourceTypeMasks enumeration](specialized-columns.md#BKMK_SourceTypeMasks) when performing bitwise operations. |

## Formula and calculated columns

Formula and calculated columns are calculated in real-time when they're retrieved. Formula and calculated can be composed using different data types. For example, an Integer calculated column may reference values from Decimal or Currency columns.
  
Only calculated column values are available in the retrieve plug-in pipeline. Post image of a table record update or create contains the calculated column value in stage 40. More information: [Event execution pipeline](event-framework.md#event-execution-pipeline) and [Entity images](understand-the-data-context.md#entity-images)

### Formula column limitations

- Formula columns don't have values when a user with mobile client is offline.  
- `MaxValue` and `MinValue` column definitions properties can't be set on formula columns. More information: 
[Guidelines and limitations](../../maker/data-platform/formula-columns.md#guidelines-and-limitations)

### Calculated column limitations

You can't use values in calculated columns on a *[Logical value](entity-attribute-metadata.md#logical-columns)* in the same table to sort data returned by a query. Although your query can specify that the results should be ordered using a calculated column, the sort direction is ignored and doesn't throw an error. If the calculated column references only simple values in the same record, sorting works normally. You can determine the sources used in a calculated column using the `SourceTypeMask` property on the column definitions.
  
- Only columns from an immediate parent table can be used in a calculated column.  
- Saved queries, charts, and visualizations can have a maximum of 50 unique calculated columns.  
- Calculated columns can reference other calculated columns in their formula, but they can't reference themselves.  
- Calculated columns don't have values when a user with mobile client is offline.  
- `MaxValue` and `MinValue` column definitions properties can't be set on calculated columns  
  
<a name="BKMK_Rollup"></a>

## Rollup columns

Because rollup columns persist in the database, they can be used for filtering or sorting just like regular columns. Any kind of process or plug-in uses the most recently calculated value of the column. System jobs calculate the rollup column values asynchronously. Administrators set when a job is run or pause the job. By default, each column is updated hourly.
  
When a rollup column is created or updated, a **Mass Calculated Rollup Fields** job is scheduled to run in 12 hours. The 12-hour delay is intended to perform this resource intensive operation during a time that affects users the least. After the job completes, the next time it's scheduled to run will be 10 years in the future. If there's a problem with the calculation, the problem is reported with the system job. Locate the system job to find any errors with rollup fields. To find the system job, see [View Rollup jobs](../../maker/data-platform/define-rollup-fields.md#view-rollup-jobs).

> [!TIP]
>  As a developer testing a solution in a development environment you may not want to wait for 12 hours. You can make it happen faster. In the **System Jobs** list, use the **Recurring System Jobs** view to filter the list and locate the **Mass Calculate Rollup Fields** job. With the job selected, use **More Actions** > **Postpone** and set the time to something that occurs sooner.  
>   
>  If you want to trigger the creation of a new **Mass Calculated Rollup Fields** job programmatically, retrieve the <xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata> for the rollup column using <xref:Microsoft.Xrm.Sdk.Messages.RetrieveAttributeRequest> and use <xref:Microsoft.Xrm.Sdk.Messages.UpdateAttributeRequest> to update the column without making any actual changes.  
  
The **Mass Calculated Rollup Fields** job occurs immediately when a solution containing a rollup column is imported. This is another reason to only install solutions during times that won't adversely impact users.  
  
Each rollup column for a table will also include two supporting columns for the rollup column:  
  
- *\<attribute SchemaName>* `_Date`: DateTime – When the rollup was last calculated.  
- *\<attribute SchemaName>* `_State`: Integer – The state of the rollup calculation. More information: [Rollup state values](specialized-columns.md#BKMK_RollupStateValues)  
  
<a name="BKMK_RollupStateValues"></a>

### Rollup state values

The state of a rollup column calculation is available in the corresponding *\<attribute SchemaName>*`_State` column and in the <xref:Microsoft.Crm.Sdk.Messages.CalculateRollupFieldResponse>.`FieldState` property. Values that indicate the state are shown in the following table.  
  
|State Value|Description|  
|-----|-----|  
|0|`NotCalculated`: Column value is yet to be calculated.|
|1|`Calculated`: Column value has been calculated per the last update time in *\<attribute SchemaName>*`_Date` column.|
|2|`OverflowError`: Column value calculation lead to overflow error.|
|3|`OtherError`: Column value calculation failed due to an internal error, next run of calculation job will likely fix it.|
|4|`RetryLimitExceeded`: Column value calculation failed because the maximum number of retry attempts to calculate the value were exceeded likely due to high number of concurrency and locking conflicts.|
|5|`HierarchicalRecursionLimitReached`: Column value calculation failed because maximum hierarchy depth limit for calculation was reached.|
|6|`LoopDetected`: Column value calculation failed because a recursive loop was detected in the hierarchy of the record.|
  
### Retrieve a calculated rollup column value immediately  

Rollup columns support a `CalculateRollupField` message that developers can use to calculate a rollup column value on demand. For the SDK, use the [CalculateRollupFieldRequest class](xref:Microsoft.Crm.Sdk.Messages.CalculateRollupFieldRequest) and for Web API use the [CalculateRollupField Function](xref:Microsoft.Dynamics.CRM.CalculateRollupField)

This message is a synchronous operation for just the column identified in the request. If the value of that record is included as part of other rollup columns, the values of those columns don't take the possible value change caused by calling this method into consideration until the regularly scheduled asynchronous jobs that perform those calculations occur.  
  
### Rollup column limitations

- Rollup columns can't be used as a workflow event or wait condition. These columns don't raise the event to trigger workflows.  
- The `ModifiedBy` and `ModifiedOn` columns for the table aren't updated when the rollup column is updated.  
- A maximum of 100 rollup columns can be defined within an organization. Each table can have no more than 10 rollup column.  
- A rollup column formula can't reference another rollup column.  
- A rollup column formula can't reference complex calculated or formula column. Only calculated  or formula columns that reference simple columns in the same record can be used with rollups.  
- A rollup column formula can't include records in many-to-many (N:N) relationships. It can only include records in one-to-many (1:N) relationships.  
- Rollup column formulas can't use one-to-many (1:N) relationships with the `ActivityPointer` or `ActivityParty` table.  
  
<a name="BKMK_SourceTypeMasks"></a>

## Prompt columns

Prompt column values are populated when records are created and when the input column values are updated. When prompt columns are added to tables with records, the existing records' new prompt columns aren't populated automatically. Outputs persist in the database and can be used for filtering and sorting like regular columns.

### Prompt column limitations

- Create and update for prompt column using API is not supported at this time.
- Importing and exporting solutions with prompt columns is not supported at this time.

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
    /// Simple: 1 - The calculated or formula column refers to a column in the same record.  
    /// </summary>  
    Simple = 1,  
    /// <summary>  
    /// Related: 2 - The calculated or formula column refers to a column in a related record.  
    /// </summary>  
    Related = 2,  
    /// <summary>  
    /// Logical: 4 - The calculated or formula column refers to a logical column.  
    /// </summary>  
    Logical = 4,  
    /// <summary>  
    /// Calculated: 8 - The calculated or formula column refers to another calculated column.  
    /// </summary>  
    Calculated = 8,  
    /// <summary>  
    /// Rollup: 16 - The calculated or formula column refers a rollup column.   
    /// </summary>  
    Rollup = 16,  
    /// <summary>  
    /// Invalid: 32 - The calculated,formula, or rollup column is invalid.  
    /// Typically this would be where a field refers to a column that no longer exists.   
    /// </summary>  
    Invalid = 32  
}  
```  
  
### See also  

[Column definitions](entity-attribute-metadata.md)   
[Work with formula columns (preview)](../../maker/data-platform/formula-columns.md)   
[Define calculated columns](../../maker/data-platform/define-calculated-fields.md)   
[Define rollup columns](../../maker/data-platform/define-rollup-fields.md)   
[Sample: Rollup records related to a specific record](org-service/samples/rollup-records-related-to-specificed-record.md)   

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
