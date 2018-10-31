---
title: "Behavior and format of the date and time attribute (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "The DateTimeAttributeMetadata class is used to define and manage attributes of type DateTime in Dynamics 365 Customer Engagement." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 10/31/2018
ms.reviewer: ""
ms.service: "powerapps"
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
# Behavior and format of the date and time attribute

If you have users and offices around the world, it is important to properly represent date and time values in multiple time zones. The `DateTimeAttributeMetadata` (<xref href="Microsoft.Dynamics.CRM.DateTimeAttributeMetadata?text=DateTimeAttributeMetadata EntityType" /> or <xref:Microsoft.Xrm.Sdk.Metadata.DateTimeAttributeMetadata> class) is used to define and manage attributes of type `DateTime` in Common Data Service for Apps. Use the `DateTimeBehavior` property (For Organization Service see, <xref:Microsoft.Xrm.Sdk.Metadata.DateTimeAttributeMetadata>.<xref:Microsoft.Xrm.Sdk.Metadata.DateTimeAttributeMetadata.DateTimeBehavior>) to define whether to store date and time values with or without time zone information, and use the `DateTimeAttributeMetadata.Format` property to specify the display format of these attributes.  

  
 You can also use the customization area in CDS for Apps to define the behavior and format of the date and time attributes. More information: [Behavior and format of the Date and Time field](/dynamics365/customer-engagement/customize/behavior-format-date-time-field).  
  
> [!NOTE]
>  All date and time attributes in Common Data Service for Apps support values as early as 1/1/1753 12:00 AM.  
  
<a name="SpecifyBehavior"></a>   

## Specify the behavior of a date and time attribute

 You can use the `DateTimeBehavior` (<xref href="Microsoft.Dynamics.CRM.DateTimeBehavior?text=DateTimeBehavior ComplexType" /> or <xref:Microsoft.Xrm.Sdk.Metadata.DateTimeBehavior> class) to specify a value for the <xref href="Microsoft.Dynamics.CRM.DateTimeAttributeMetadata?text=DateTimeAttributeMetadata EntityType" />.DateTimeBehavior property. The `DateTimeBehavior` contains the following members; each member returns a string with the same value as the member name:  
  
|Member name and value|Description|  
|---------------------------|-----------------|  
|`UserLocal`|-   Stores the date and time value as UTC value in the system.<br />-   The retrieve operation returns the UTC value.<br />-   The update operation converts the UTC value to the current user’s time zone value, and then stores the updated value as is or as the equivalent UTC value depending on the kind ([DateTimeKind](https://msdn.microsoft.com/library/shx7s921.aspx)) of the value specified for update. If the specified value is of UTC kind, it’s stored as is. Otherwise, the UTC-equivalent value is stored.<br />-   Retrieving the formatted value converts from UTC to the user’s current time zone based on the time zone and locale setting of the user.<br />-   For the Web API, the attribute is exposed as DateTimeOffset.<br />-   This behavior is used for system attributes like `CreatedOn` and `ModifiedOn`, and cannot be changed. You should use this behavior for custom attributes where you want to store date and time values with the time zone information.|  
|`DateOnly`|-   Stores the actual date value with the time value as 12:00 AM (00:00:00) in the system.<br />-   For the retrieve and update operations, no time zone conversion is performed, and the time value is always 12 AM (00:00:00).<br />-   Retrieving the formatted value displays the date value without any time zone conversion.<br />-   For the Web API, the attribute is exposed as DateTimeOffset.<br />-   This behavior should be used for custom attributes that store birthdays and anniversaries, where the time information is not required.|  
|`TimeZoneIndependent`|-   Stores the actual date and time values in the system regardless of the user time zone.<br />-   For the retrieve and update operations, no time zone conversion is performed, and actual date and time values are returned and updated respectively in the system regardless of the user time zone.<br />-   Retrieving the formatted value displays the date and time value (without any time zone conversion) based on the format as specified by the current user’s time zone and locale setting.<br />-   For the Web API, the attribute is exposed as DateTimeOffset.<br />-   This behavior should be used for attributes that store information such as check in and check out time for hotels.|  
  
 The following sample code demonstrates how to set a `UserLocal` behavior for a new date time attribute:  
  
 ```csharp
// Create a date time attribute for the Account entity
// with the UserLocal behavior
dtAttribute = new DateTimeAttributeMetadata
{                             
    SchemaName = "new_SampleDateTimeAttribute",
    DisplayName = new Label("Sample Date Time Attribute", _languageCode),
    RequiredLevel = new AttributeRequiredLevelManagedProperty(AttributeRequiredLevel.None),                
    Description = new Label("Created by SDK Sample", _languageCode),                
    DateTimeBehavior = DateTimeBehavior.UserLocal,
    Format = DateTimeFormat.DateAndTime,
    ImeMode = ImeMode.Disabled
};

CreateAttributeRequest createAttributeRequest = new CreateAttributeRequest
{
    EntityName = Account.EntityLogicalName,
    Attribute = dtAttribute
};
_serviceProxy.Execute(createAttributeRequest);
Console.WriteLine("Created attribute '{0}' with UserLocal behavior\nfor the Account entity.\n", 
                            dtAttribute.SchemaName);
```
  
 In the sample code, you can also set the value of the `DateTimeBehavior` property by directly specifying the string value: `DateTimeBehavior = "UserLocal"`  
  
 If you do not specify the behavior while creating a date and time attribute, the attribute is created with the `UserLocal` behavior by default. For the complete sample code, see [Sample: Convert date and time values](/dynamics365/customer-engagement/developer/org-service/sample-convert-date-time-behavior).  
  
> [!IMPORTANT]
>  -   Once you create a date and time attribute with behavior set to `DateOnly` or `TimeZoneIndependent`, you cannot change the behavior of the attribute. More information: [Change the behavior of a DateTime attribute](behavior-format-date-time-attribute.md#ChangeBehavior)  
> -   The date and time attributes with the `DateOnly` or `TimeZoneIndependent` behavior will be treated like having the `UserLocal` behavior when edited in an earlier version of the Dynamics 365 for Outlook client in the offline mode. This is because the client doesn’t understand the new behaviors and won’t treat them differently from `UserLocal`. No date and time attributes are converted to the new behaviors on upgrade so the best practice here would be to upgrade all CDS for Apps clients to the latest release before a customizer adopts one of the new behaviors. When online, editing data for fields with the new behaviors will work fine.  
  
<a name="SpecifyFormat"></a>   

## Specify format of the date and time attribute  

 Use the `Format` property to specify the date/time display format of the attribute irrespective of how it is stored in the system. You can use the `DateTimeFormat` enumeration (<xref href="Microsoft.Dynamics.CRM.DateTimeFormat?text=DateTimeFormat EnumType" /> or <xref:Microsoft.Xrm.Sdk.Metadata.DateTimeFormat> enumeration) to specify the display format: `DateAndTime` or `DateOnly`.  
  
 If the `DateTimeAttributeMetadata.DateTimeBehavior` property is set to `DateOnly`, you cannot set or change the value of the `DateTimeAttributeMetadata.Format` property to `DateAndTime`.  
  
<a name="UnsupportedQueryOperators"></a>   

## Date and time query operators not supported for DateOnly behavior  

 Time-related query operators are not supported for the `DateOnly` behavior. Other than the time-specific query operators listed here, all the other query operators are supported.  
  
-   Older Than X Minutes  
  
-   Older Than X Hours  
  
-   Last X Hours  
  
-   Next X Hours  
  
 More information: [Date and time query operators in FetchXML](/dynamics365/customer-engagement/developer/org-service/fiscal-date-older-datetime-query-operators-fetchxml)  
  
<a name="ChangeBehavior"></a>
   
## Change the behavior of a date and time attribute  

 You can update a date and time attribute to change its behavior if you have the System Customizer role in your CDS for Apps instance and the `DateTimeAttributeMetadata.CanChangeDateTimeBehavior` managed property for the date and time attribute is set to `True`.  
  
> [!CAUTION]
>  Before changing the behavior of a date and time attribute, you should review all the dependencies of the attribute, such as business rules, workflows, and calculated or rollup attributes, to ensure that there are no issues as a result of changing the behavior. System Customizers can restrict modifying the behavior of existing date and time attributes using the `DateTimeAttributeMetadata.CanChangeDateTimeBehavior` managed property.  
>   
>  At the minimum, after changing the behavior of a date and time attribute, you should open each business rule, workflow, calculated attribute, and rollup attribute record that is dependent on the changed date and time attribute, review the information, and save the record to ensure that the latest attribute behavior and value is used.  
>   
>  After changing the data and time behavior of a calculated or rollup attribute, open the calculated or rollup field definition editor, and save the field definition to ensure that the attribute is still valid after the behavior change. System customizers can open the field definition editor for calculated or rollup attribute by clicking **Edit** next to **Field Type** in the customization area in CDS for Apps. More information: [Define calculated fields](/dynamics365/customer-engagement/customize/define-calculated-fields) and [Define rollup fields](/dynamics365/customer-engagement/developer/customize/define-rollup-fields)  
  
-   The behavior of the `CreatedOn` and `ModifiedOn` attributes for the out-of-box and custom entities is set to `UserLocal` by default, and the `DateTimeAttributeMetadata.CanChangeDateTimeBehavior` managed property is set to `False`, which implies that you cannot change the behavior of these attributes. Although users can change the value of the `DateTimeAttributeMetadata.CanChangeDateTimeBehavior` managed property of these attributes for custom entities, but they still can’t change the behavior of the attributes.  
  
-   For new custom date and time attributes, the `DateTimeAttributeMetadata.CanChangeDateTimeBehavior` managed property is set to `True`. This implies that you can change behavior of a custom date and time attribute from `UserLocal` to either `DateOnly` or `TimeZoneIndependent`; no other behavior transitions are allowed.  
  
     For custom date and time attributes that are part of a CDS for Apps organization, the `DateTimeAttributeMetadata.CanChangeDateTimeBehavior` managed property is set to `True` unless the attribute or the parent entity is not customizable.  
  
    > [!NOTE]
    >  When you update `DateTimeAttributeMetadata.DateTimeBehavior` property of an attribute from `UserLocal` to `DateOnly`, ensure that you also change the`DateTimeAttributeMetadata.Format` property from `DateAndTime` to `DateOnly`. Otherwise, an exception will occur.  
  
-   The following out-of-box date and time attributes in CDS for Apps are by default set to `DateOnly` and the `DateTimeAttributeMetadata.CanChangeDateTimeBehavior` managed property is set to `False` of these attributes, which implies that you cannot change the behavior for these attributes:  
  
    |Date and time attribute|Parent entity|  
    |-----------------------------|-------------------|  
    |anniversary|Contact|  
    |birthdate|Contact|  
    |duedate|Invoice|  
    |estimatedclosedate|Lead|  
    |actualclosedate|Opportunity|  
    |estimatedclosedate|Opportunity|  
    |finaldecisiondate|Opportunity|  
    |validfromdate|Product|  
    |validtodate|Product|  
    |closedon|Quote|  
    |expireson|Quote|  
  
     The behavior of these attributes is set to `UserLocal` and the `DateTimeAttributeMetadata.CanChangeDateTimeBehavior` managed property to `True`, and you can change the behavior of these attributes to `DateOnly` only. No other behavior transitions are allowed.  
  
 After updating the behavior of an attribute, you must publish the customizations for the change to take effect. Updating the behavior of a date and time attribute ensures that all the values entered/updated *after* the attribute behavior was changed, are stored in the system as per the new behavior. This does not impact the values that are already stored in the database, and they continue to be stored as UTC values. However, when you retrieve the existing values using SDK or view it in the UI, the existing values are displayed as per the new behavior of the attribute. For example, if you changed the behavior of a custom attribute on an account entity from `UserLocal` to `DateOnly` and retrieve an existing account record using SDK, the date and time will be displayed as \<Date> followed by time as 12 AM (00:00:00). Similarly, for the behavior change from `UserLocal` to `TimeZoneIndependent`, the actual value in the database will be displayed as is without any time zone conversions.  
  
 The following sample code demonstrates how to update the behavior of a date and time attribute:  
  
```csharp
// Retrieve the attribute to update its behavior and format
RetrieveAttributeRequest attributeRequest = new RetrieveAttributeRequest
{
    EntityLogicalName = Account.EntityLogicalName,
    LogicalName = "new_sampledatetimeattribute",
    RetrieveAsIfPublished = false
};
// Execute the request
RetrieveAttributeResponse attributeResponse =
                (RetrieveAttributeResponse)_serviceProxy.Execute(attributeRequest);

Console.WriteLine("Retrieved the attribute '{0}'.",
                attributeResponse.AttributeMetadata.SchemaName);

// Modify the values of the retrieved attribute
DateTimeAttributeMetadata retrievedAttributeMetadata =
                (DateTimeAttributeMetadata)attributeResponse.AttributeMetadata;
retrievedAttributeMetadata.DateTimeBehavior = DateTimeBehavior.DateOnly;
retrievedAttributeMetadata.Format = DateTimeFormat.DateOnly;

// Update the attribute with the modified value
UpdateAttributeRequest updateRequest = new UpdateAttributeRequest
{
    Attribute = retrievedAttributeMetadata,
    EntityName = Account.EntityLogicalName,
    MergeLabels = false
};
_serviceProxy.Execute(updateRequest);
Console.WriteLine("Updated the behavior and format of '{0}' to DateOnly.",
    retrievedAttributeMetadata.SchemaName);

// Publish customizations to the account entity
PublishXmlRequest pxReq = new PublishXmlRequest
{
    ParameterXml = String.Format("<importexportxml><entities><entity>account</entity></entities></importexportxml>")
};
_serviceProxy.Execute(pxReq);
Console.WriteLine("Published customizations to the Account entity.\n");
 
``` 
  
 For the complete sample code, see [Sample: Convert date and time values](/dynamics365/customer-engagement/developer/org-service/sample-convert-date-time-behavior).  
  
<a name="Convert"></a>   
## Convert behavior of existing date and time values in the database 

 When you update a date and time attribute to change its behavior from `UserLocal` to `DateOnly` or `TimeZoneIndependent`, it does not automatically convert the existing attribute values in the database. The behavior change affects only those values that will be entered or updated in the attribute *after* the behavior has been changed. The existing date and time values in the system continue to be in UTC, and displayed by CDS for Apps according to the new behavior when retrieved through SDK or in the UI as explained in the previous section. For attributes whose behavior has changed from `UserLocal` to `DateOnly`, you can convert the existing UTC values in the database to appropriate `DateOnly` value to avoid any data anomalies by using the `ConvertDateAndTimeBehavior` message.  
  
 The message enables you to specify a conversion rule (If working with Organization Service see, <xref:Microsoft.Xrm.Sdk.Messages.ConvertDateAndTimeBehaviorRequest.ConversionRule>) to select the time zone to use for conversion of the values from UTC to DateOnly. You can specify one of the following conversion rules:  
  
-   `SpecificTimeZone`: Converts UTC value to a DateOnly value as per the specified CDS for Apps time zone code. In this case, you also need to specify a value for the <xref:Microsoft.Xrm.Sdk.Messages.ConvertDateAndTimeBehaviorRequest.TimeZoneCode> parameter.  
  
-   `CreatedByTimeZone`: Converts UTC value to a DateOnly value that the user who created the record would see in the UI.  
  
-   `OwnerTimeZone`: Converts UTC value to a DateOnly value that the user who owns the record would see in the UI.  
  
-   `LastUpdatedByTimeZone`: Converts UTC value to a DateOnly value that the user who last updated the record would see in the UI.  
  
 You can use one of the four members of the <xref:Microsoft.Xrm.Sdk.DateTimeBehaviorConversionRule> class to specify a valid value for the <xref:Microsoft.Xrm.Sdk.Messages.ConvertDateAndTimeBehaviorRequest.ConversionRule> parameter.  
  
> [!NOTE]
>  You must have the System Administrator role in your CDS for Apps instance to execute the <xref:Microsoft.Xrm.Sdk.Messages.ConvertDateAndTimeBehaviorRequest> message.  
  
 When you execute the `ConvertDateAndTimeBehavior` (If working with Organization Service see, <xref:Microsoft.Xrm.Sdk.Messages.ConvertDateAndTimeBehaviorRequest> message), a system job (asynchronous operation) is created to run the conversion request. The `ConvertDateAndTimeBehaviorResponse.JobId` attribute in the message response displays the ID of the system job that is created as a result of the conversion request. After the system job completes, check the job details (`AsyncOperation.Message`) to view conversion details or errors, if any.  
  
> [!NOTE]
>  We recommend that you group conversion of multiple attributes into a single conversion job, and run a single conversion job at a time to ensure that there are no conflicts in the conversion and for optimum system performance.  
  
 Some important points to be considered while using the `ConvertDateAndTimeBehavior` message:  
  
-   You should avoid any major changes to the solutions in CDS for Apps during the execution of the message such as importing a solution or deleting an attribute or parent entity. Doing so might lead to unexpected behavior; however no data loss will occur.  
  
-   Updates done in the system as a result of executing the message won’t run workflows and plug-ins.  
  
-   Updates done in the system as a result of executing the message won’t change the “last modified on” value for the attributes, but will be audited to help the administrators to determine the time of the conversion and the original/changed values for an attribute.  
  
 The following sample code shows how to use the message:  
  
```csharp
ConvertDateAndTimeBehaviorRequest request = new ConvertDateAndTimeBehaviorRequest()
{
    Attributes = new EntityAttributeCollection() 
            { 
                new KeyValuePair<string, StringCollection>("account", new StringCollection() 
                { "new_sampledatetimeattribute" }) 
            },
    ConversionRule = DateTimeBehaviorConversionRule.SpecificTimeZone.Value,
    TimeZoneCode = 190, // Time zone code for India Standard Time (IST) in CRM
    AutoConvert = false // Conversion must be done using ConversionRule
};

// Execute the request
ConvertDateAndTimeBehaviorResponse response = (ConvertDateAndTimeBehaviorResponse)_serviceProxy.Execute(request);

```
  
 For the complete sample code, see [Sample: Convert date and time values](/dynamics365/customer-engagement/developer/org-service/sample-convert-date-time-behavior)  
  
### See also  
 [Sample: Convert date and time values](/dynamics365/customer-engagement/developer/org-service/sample-convert-date-time-behavior.md)   
 [Behavior and format of the Date and Time field](/dynamics365/customer-engagement/developer/customize/behavior-format-date-time-field)   
 [Customize Entity Attribute Metadata](/dynamics365/customer-engagement/developer/customize-entity-attribute-metadata)          
 <xref:Microsoft.Xrm.Sdk.Messages.ConvertDateAndTimeBehaviorRequest>      
 <xref:Microsoft.Xrm.Sdk.Metadata.DateTimeAttributeMetadata> 