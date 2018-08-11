---
title: "Calculated and rollup attributes (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn about common elements and characterstics, calculated attributes, rollup attributes, retrieve a calculated rollup field value immediately, and SourceTypeMasks enumeration." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "mayadumesh" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Calculated and rollup attributes

*Calculated* and *rollup* attributes free the user from having to manually perform calculations and focus on their work. System administrators can now easily define a field to contain the value of many common calculations without having to work with a developer. Developers can also leverage the platform capabilities to perform these calculations rather than within their own code.  
  
 [Video: Rollup and Calculated Fields in Microsoft Dynamics CRM 2015](http://youtu.be/RoahCH1p3T8)  
  
<a name="BKMK_CommonElements"></a>   
## Common elements and characteristics  
 Calculated and rollup attributes share some common elements and characteristics, for example:  
  
- They’re read-only.  
  
- They’re not specific to the user. The calculation is performed using a system user account, so the values may be based on records that the user doesn’t otherwise have privileges to view, such as attributes that have field-level security enabled.  
  
  All attributes that inherit from <xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata> have a <xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.SourceType> property that can contain the values shown in the following table.  
  
|                 Value                 |                                    Description                                     |
|---------------------------------------|------------------------------------------------------------------------------------|
| Null |       Not a valid type of attribute to be a calculated or rollup attribute.        |
|                   0                   | Simple attribute. The attribute isn’t defined as a calculated or rollup attribute. |
|                   1                   |                                Calculated attribute                                |
|                   2                   |                                  Rollup attribute                                  |
  
 Calculated and rollup attributes are based on existing attribute types that inherit from <xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata>. The following types of attributes have new properties:  
  
- <xref:Microsoft.Xrm.Sdk.Metadata.BooleanAttributeMetadata>  
  
- <xref:Microsoft.Xrm.Sdk.Metadata.DateTimeAttributeMetadata>  
  
- <xref:Microsoft.Xrm.Sdk.Metadata.DecimalAttributeMetadata>  
  
- <xref:Microsoft.Xrm.Sdk.Metadata.IntegerAttributeMetadata>  
  
- <xref:Microsoft.Xrm.Sdk.Metadata.MoneyAttributeMetadata>  
  
- <xref:Microsoft.Xrm.Sdk.Metadata.PicklistAttributeMetadata>  
  
- <xref:Microsoft.Xrm.Sdk.Metadata.StringAttributeMetadata>  
  
  Each of these types of attributes have the following properties to support calculations and rollups.  
  
|      Property       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        Definition                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `FormulaDefinition` |                                                                                                                                                                                                                                                                                                                                                                                                                                                                   Contains the XAML definition of the formula used to perform the calculation or rollup. The only supported way to change this value is through the application formula editor.<br /><br /> For information about configuring the formulas for these attributes see the following topics in the customization guide: [Define rollup fields](https://technet.microsoft.com/library/dn832162.aspx) and [Define calculated fields](https://technet.microsoft.com/library/dn832103.aspx).                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|  `SourceTypeMask`   | The bitmask value of this read-only property describes the types of sources used in the formula of the calculated attribute or if the formula of a calculated or rollup attribute is not valid.<br /><br /> -   0: **Undefined**. The default value for simple and rollup attributes.<br />-   1: **Simple**. The calculated attribute refers to an attribute in the same record.<br />-   2: **Related**. The calculated attribute refers to an attribute in a related record.<br />-   4: `Logical`. The calculated attribute refers to an attribute in the same record which is actually stored in a different database table. More information: [Logical attributes](introduction-to-entity-attributes.md#BKMK_LogicalAttributes)<br />-   8: `Calculated`. The calculated attribute refers to another calculated attribute.<br />-   16: `Rollup`. The calculated attribute refers a rollup attribute.<br />-   32: `Invalid`. The calculated or rollup field is invalid.<br />     Typically this would be where a field refers to an attribute that no longer exists. **Note:**  One or more of these conditions may be true for any calculated or rollup field. Because this is a bitmask value, you may find it useful to use the [SourceTypeMasks enumeration](calculated-rollup-attributes.md#BKMK_SourceTypeMasks) when performing bitwise operations. |
  
<a name="BKMK_Calculated"></a>   
## Calculated attributes  
 Calculated attributes are calculated in real-time when they are retrieved. Calculated attributes can be composed using different data types. For example, an Integer calculated attribute may reference values from Decimal or Currency attributes. More information: [Define calculated fields](https://technet.microsoft.com/library/dn832103.aspx).  
  
 Calculated attribute values are available in the retrieve plug-in pipeline. Post image of entity record update or create contains the calculated attribute value in stage 40. More information: [Event Execution Pipeline](event-execution-pipeline.md)  
  
### Limitations  
 You can’t use values in calculated attributes that reference a related entity, another calculated attribute, or a *logical value* in the same entity to sort data returned by a query. Although your query can specify that the results should be ordered using a calculated attribute, the sort direction will be ignored and will not throw an error. If the calculated attribute references only simple values in the same record, sorting works normally. You can determine the sources used in a calculated field using the `SourceTypeMask` property on the attribute metadata. More information: [Logical attributes](/dynamics365/customer-engagement/developer/introduction-to-entity-attributes.md#BKMK_LogicalAttributes)  
  
 Only attributes from an immediate parent entity can be used in a calculated attribute.  
  
 Saved queries, charts, and visualizations can have a maximum of 10 unique calculated attributes.  
  
 Calculated attributes can reference other calculated attributes in their formula, but they can’t reference themselves.  
  
 Calculated attributes don’t have values when a user with Dynamics 365 for Outlook is offline.  
  
 `MaxValue` and `MinValue` metadata properties can’t be set on calculated attributes  
  
<a name="BKMK_Rollup"></a>   
## Rollup attributes  
 Because rollup attributes persist in the database, they can be used for filtering or sorting just like regular attributes. Any kind of process or plug-in will use the most recently calculated value of the attribute. Rollup attribute values are calculated asynchronously by scheduled system jobs. Administrators set when a job is run or pause the job. By default, each attribute is updated hourly. More information: [Define rollup fields](https://technet.microsoft.com/library/dn832103.aspx).  
  
 When a rollup attribute is created or updated a **Mass Calculated Rollup Fields** job is scheduled to run in 12 hours. The 12-hour delay is intended to perform this resource intensive operation during a time that will affect users the least. After the job completes, the next time it is scheduled to run will be 10 years in the future. If there is a problem with the calculation, this will be reported with the system job. Locate the system job in **Settings** > **System Jobs** to find any errors with rollup fields.  
  
> [!TIP]
>  As a developer testing a solution in a development environment you may not want to wait for 12 hours. You can make it happen faster. In the **System Jobs** list, use the **Recurring System Jobs** view to filter the list and locate the **Mass Calculate Rollup Fields** job. With the job selected, use **More Actions** > **Postpone** and set the time to something that occurs sooner.  
>   
>  If you want to trigger the creation of a new **Mass Calculated Rollup Fields** job programmatically, retrieve the <xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata> for the rollup attribute using <xref:Microsoft.Xrm.Sdk.Messages.RetrieveAttributeRequest> and use <xref:Microsoft.Xrm.Sdk.Messages.UpdateAttributeRequest> to update the attribute without making any actual changes.  
  
 The **Mass Calculated Rollup Fields** job will occur immediately when a solution containing a rollup attribute is imported. This assumes that you are installing a solution during a time that won’t adversely impact users.  
  
 Each rollup attribute for an entity will also include two supporting attributes for the rollup attribute:  
  
- *\<attribute SchemaName>* `_Date`: DateTime – When the rollup was last calculated.  
  
- *\<attribute SchemaName>* `_State`: Integer – The state of the rollup calculation. More information: [Rollup state values](calculated-rollup-attributes.md#BKMK_RollupStateValues)  
  
<a name="BKMK_RollupStateValues"></a>   
### Rollup state values  
 The state of a rollup field calculation is available in the corresponding *\<attribute SchemaName>*`_State` attribute and in the <xref:Microsoft.Crm.Sdk.Messages.CalculateRollupFieldResponse>.`FieldState` property. Values that indicate the state are shown in the following table.  
  
|State Value|Description|  
|-----------------|-----------------|  
|0|`NotCalculated`: Attribute value is yet to be calculated.|  
|1|`Calculated`: Attribute value has been calculated per the last update time in *\<attribute SchemaName>*`_Date` attribute.|  
|2|`OverflowError`: Attribute value calculation lead to overflow error.|  
|3|`OtherError`: Attribute value calculation failed due to an internal error, next run of calculation job will likely fix it.|  
|4|`RetryLimitExceeded`: Attribute value calculation failed because the maximum number of retry attempts to calculate the value were exceeded likely due to high number of concurrency and locking conflicts.|  
|5|`HierarchicalRecursionLimitReached`: Attribute value calculation failed because maximum hierarchy depth limit for calculation was reached.|  
|6|`LoopDetected`: Attribute value calculation failed because a recursive loop was detected in the hierarchy of the record.|  
  
### Retrieve a calculated rollup field value immediately  
 Rollup attributes support a `CalculateRollupField` message that developers can use to calculate a rollup attribute value on demand. The request and response, along with the members, are shown in the following table.  
  
|Request/Response|Members|  
|-----------------------|-------------|  
|<xref:Microsoft.Crm.Sdk.Messages.CalculateRollupFieldRequest>|`Target`: <xref:Microsoft.Xrm.Sdk.EntityReference> for the record.<br /><br /> `FieldName`: String representing the logical name of the attribute.|  
|<xref:Microsoft.Crm.Sdk.Messages.CalculateRollupFieldResponse>|`Entity`: <xref:Microsoft.Xrm.Sdk.Entity> containing the rollup attribute and the supporting *\<attribute SchemaName>*`_Date` and *\<attribute SchemaName>*`_State` attributes.|  
  
 This message is a synchronous operation for just the attribute identified in the request. If the value of that record is included as part of other rollup fields, the values of those fields won’t take the possible value change caused by calling this method into consideration until the regularly scheduled asynchronous jobs that perform those calculations occur.  
  
### Limitations  
 Rollup attributes can’t be used as a workflow event or wait condition. These attributes don’t raise the event to trigger workflows.  
  
 The ModifiedBy and ModifiedOn attributes for the entity aren’t updated when the rollup attribute is updated.  
  
 A maximum of 100 rollup attributes can be defined within an organization. Each entity can have no more than 10 rollup attributes.  
  
 A rollup attribute formula can’t reference another rollup attribute.  
  
 A rollup attribute formula can’t reference complex calculated attributes. Only calculated attributes that reference simple attributes in the same record can be used with rollups.  
  
 A rollup attribute formula can’t include records in many-to-many (N:N) relationships. It can only include records in one-to-many (1:N) relationships.  
  
 Rollup attribute formulas can’t use one-to-many (1:N) relationships with the `ActivityPointer` or `ActivityParty` entity.  
  
<a name="BKMK_SourceTypeMasks"></a>   
## SourceTypeMasks enumeration  
 The `SourceTypeMask` property for those attributes that support calculated and rollup fields contains a bitmask value. To extract the relevant information from the value, it helps to have an enumeration when performing bitwise operations. Use the following `SourceTypeMasks` enumeration when comparing the `SourceTypeMask` property value.  
  
```csharp  
 public enum SourceTypeMasks  
{  
    /// <summary>  
    /// Undefined: 0 - The default value for simple and rollup attributes.  
    /// </summary>  
    Undefined = 0,  
    /// <summary>  
    /// Simple: 1 - The calculated attribute refers to an attribute in the same record.  
    /// </summary>  
    Simple = 1,  
    /// <summary>  
    /// Related: 2 - The calculated attribute refers to an attribute in a related record.  
    /// </summary>  
    Related = 2,  
    /// <summary>  
    /// Logical: 4 - The calculated attribute refers to a logical attribute.  
    /// </summary>  
    Logical = 4,  
    /// <summary>  
    /// Calculated: 8 - The calculated attribute refers to another calculated attribute.  
    /// </summary>  
    Calculated = 8,  
    /// <summary>  
    /// Rollup: 16 - The calculated attribute refers a rollup attribute.   
    /// </summary>  
    Rollup = 16,  
    /// <summary>  
    /// Invalid: 32 - The calculated or rollup attribute is invalid.  
    /// Typically this would be where a field refers to an attribute that no longer exists.   
    /// </summary>  
    Invalid = 32  
}  
```  
  
### See also  
 [Video: Rollup and Calculated Fields in Microsoft Dynamics CRM 2015](http://youtu.be/RoahCH1p3T8)   
 [Introduction to entity attributes](/dynamics365/customer-engagement/developer/introduction-to-entity-attributes)   
 [Define calculated fields](https://technet.microsoft.com/library/dn832103.aspx)   
 [Define rollup fields](https://technet.microsoft.com/library/dn832103.aspx)
