---
title: "Behavior and format of the date and time column (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "The DateTimeAttributeMetadata class is used to define and manage columns of type DateTime in Microsoft Dataverse." # 115-145 characters including spaces. This abstract displays in the search result.
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
# Behavior and format of the date and time column

If you have users and offices around the world, it is important to properly represent date and time values in multiple time zones. The `DateTimeAttributeMetadata` (<xref href="Microsoft.Dynamics.CRM.DateTimeAttributeMetadata?text=DateTimeAttributeMetadata EntityType" /> or <xref:Microsoft.Xrm.Sdk.Metadata.DateTimeAttributeMetadata> class) is used to define and manage columns of type `DateTime` in Microsoft Dataverse. Use the `DateTimeBehavior` property (For Organization Service see, <xref:Microsoft.Xrm.Sdk.Metadata.DateTimeAttributeMetadata>.<xref:Microsoft.Xrm.Sdk.Metadata.DateTimeAttributeMetadata.DateTimeBehavior>) to define whether to store date and time values with or without time zone information, and use the `DateTimeAttributeMetadata.Format` property to specify the display format of these columns.  

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]

You can also use the customization area in Dataverse to define the behavior and format of the date and time columns. More information: [Behavior and format of the date and time column](/dynamics365/customer-engagement/customize/behavior-format-date-time-field).  
  
> [!NOTE]
>  All date and time columns in Dataverse support values as early as 1/1/1753 12:00 AM.  
  
<a name="SpecifyBehavior"></a>   

## Specify the behavior of a date and time column

 You can use the `DateTimeBehavior` (<xref href="Microsoft.Dynamics.CRM.DateTimeBehavior?text=DateTimeBehavior ComplexType" /> or <xref:Microsoft.Xrm.Sdk.Metadata.DateTimeBehavior> class) to specify a value for the <xref href="Microsoft.Dynamics.CRM.DateTimeAttributeMetadata?text=DateTimeAttributeMetadata EntityType" />.DateTimeBehavior property. The `DateTimeBehavior` contains the following members; each member returns a string with the same value as the member name:  
  
|Member name and value|Description|  
|---------------------------|-----------------|  
|`UserLocal`|-   Stores the date and time value as UTC value in the system.<br />-   The retrieve operation returns the UTC value.<br />-   The update operation converts the UTC value to the current user’s time zone value, and then stores the updated value as is or as the equivalent UTC value depending on the kind ([DateTimeKind](https://msdn.microsoft.com/library/shx7s921.aspx)) of the value specified for update. If the specified value is of UTC kind, it’s stored as is. Otherwise, the UTC-equivalent value is stored.<br />-   Retrieving the formatted value converts from UTC to the user’s current time zone based on the time zone and locale setting of the user.<br />-   For the Web API, the column is exposed as DateTimeOffset.<br />-   This behavior is used for system columns like `CreatedOn` and `ModifiedOn`, and cannot be changed. You should use this behavior for custom columns where you want to store date and time values with the time zone information.|  
|`DateOnly`|-   Stores the actual date value with no time value.<br />-   Retrieving the formatted value displays the date value.<br />-   For the Web API, the column is exposed as Date.<br />-   This behavior should be used for custom columns that store birthdays and anniversaries, where the time information is not required.|  
|`TimeZoneIndependent`|-   Stores the actual date and time values in the system regardless of the user time zone.<br />-   For the retrieve and update operations, no time zone conversion is performed, and actual date and time values are returned and updated respectively in the system regardless of the user time zone.<br />-   Retrieving the formatted value displays the date and time value (without any time zone conversion) based on the format as specified by the current user’s time zone and locale setting.<br />-   For the Web API, the column is exposed as DateTimeOffset.<br />-   This behavior should be used for columns that store information such as check in and check out time for hotels.|  
  
 The following sample code demonstrates how to set a `UserLocal` behavior for a new date time column:  
  
 ```csharp
// Create a date time attribute for the Account
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
Console.WriteLine("Created attribute '{0}' with UserLocal behavior\nfor the Account.\n", 
                            dtAttribute.SchemaName);
```
  
 In the sample code, you can also set the value of the `DateTimeBehavior` property by directly specifying the string value: `DateTimeBehavior = "UserLocal"`  
  
 If you do not specify the behavior while creating a date and time column, the column is created with the `UserLocal` behavior by default. For the complete sample code, see [Sample: Convert date and time values](/dynamics365/customer-engagement/developer/org-service/sample-convert-date-time-behavior).  
  
> [!IMPORTANT]
>  -   Once you create a date and time column with behavior set to `DateOnly` or `TimeZoneIndependent`, you cannot change the behavior of the column. More information: [Change the behavior of a DateTime column](behavior-format-date-time-attribute.md#ChangeBehavior)  
> -   The date and time columns with the `DateOnly` or `TimeZoneIndependent` behavior will be treated like having the `UserLocal` behavior when edited in an earlier version of the Dynamics 365 for Outlook client in the offline mode. This is because the client doesn’t understand the new behaviors and won’t treat them differently from `UserLocal`. No date and time columns are converted to the new behaviors on upgrade so the best practice here would be to upgrade all Dataverse clients to the latest release before a customizer adopts one of the new behaviors. When online, editing data for columns with the new behaviors will work fine.  
  
<a name="SpecifyFormat"></a>   

## Specify format of the date and time column  

 Use the `Format` property to specify the date/time display format of the column irrespective of how it is stored in the system. You can use the `DateTimeFormat` enumeration (<xref href="Microsoft.Dynamics.CRM.DateTimeFormat?text=DateTimeFormat EnumType" /> or <xref:Microsoft.Xrm.Sdk.Metadata.DateTimeFormat> enumeration) to specify the display format: `DateAndTime` or `DateOnly`.  
  
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
   
## Using OData APIs to submit user local date and time values

In Microsoft Power Platform, when a user submits a date and time in the user-specific time zone through the UI, an automatic calculation sets the data to the correct date and time. It performs an analysis to change any submitted date to the corresponding UTC value based on the column and UI settings.
When submitting a date and time value using OData API operation, the calculation does not occur, resulting in unexplained data displays.
For example, if you are in the pacific time zone and you submit 4/4/2021 12:00, this is what happens:

-   **Original**: 4/4/2021 12:00 submitter is in the pacific time zone.
-   **Submitted through UI and retrieved as user local**: 4/4/2021 12:00
-   **Submitted through API and retrieved as user local**: 4/4/2021 04:00

### Submitting through the UI
UI is set to user local, and column is set to user local.
-   **Original Value:** 4/4/2021 12:00 in the pacific time zone.
-   **Value calculated to UTC and stored in Dataverse:** 4/4/2021 12:00 + 8:00 =  4/4/2021T20:00:00Z . This is because PST is -8:00 from UTC, so +8 is added to the stored value. 
-   **Value when displayed in UI by a user in the pacific time zone:** 4/4/2021 12:00. The UI applies the -8:00 UTC offset calculation to 4/4/2021T20:00:00Z for the correct value.

### Submitting through the API
UI is set to user local, and column is set to user local.
-   **Original Value:** 4/4/2021T12:00:00 or 4/4/2021T12:00:00Z – no offset or UTC indicator provided. The submitter is in the pacific time zone.
-   **Value calculated to UTC and stored in Dataverse:** No UI calculation is done on submission from OData APIs, so the value is stored as 4/4/2021T12:00:00Z.
-   **Value when displayed in UI by a user in the pacific time zone:** 4/4/2021 4:00. The UI applies the -8:00 UTC offset calculation on the value in Dataverse.

To prevent this issue when using API calls to input data to user local columns, you need to calculate the offset of the user submitting the data and apply the offset. 

Using the above example: 
**4/4/2021 12:00** would need to be submitted via the API as **4/4/2021T12:00:00-08:00**. The original time and date and include the offset calculation of the current user’s time zone. Alternately, the submitter can perform the calculation before submission and submit **4/4/2021T20:00:00Z**.

If you choose to include the offset calculation, you cannot have the Z, a UTC indicator, and will prevent the offset from being accepted by the system.
## Change the behavior of a date and time column  

 You can update a date and time column to change its behavior if you have the System Customizer role in your Dataverse instance and the `DateTimeAttributeMetadata.CanChangeDateTimeBehavior` managed property for the date and time column is set to `True`.  
  
> [!CAUTION]
>  Before changing the behavior of a date and time column, you should review all the dependencies of the column, such as business rules, workflows, and calculated or rollup columns, to ensure that there are no issues as a result of changing the behavior. System Customizers can restrict modifying the behavior of existing date and time columns using the `DateTimeAttributeMetadata.CanChangeDateTimeBehavior` managed property.  
>   
>  At the minimum, after changing the behavior of a date and time column, you should open each business rule, workflow, calculated column, and rollup column record that is dependent on the changed date and time column, review the information, and save the record to ensure that the latest column behavior and value is used.  
>   
>  After changing the data and time behavior of a calculated or rollup column, open the calculated or rollup column definition editor, and save the column definition to ensure that the column is still valid after the behavior change. System customizers can open the column definition editor for calculated or rollup column by clicking **Edit** next to **Field Type** in the customization area in Dataverse. More information: [Define calculated column](/dynamics365/customer-engagement/customize/define-calculated-fields) and [Define rollup column](/dynamics365/customer-engagement/developer/customize/define-rollup-fields)  
  
-   The behavior of the `CreatedOn` and `ModifiedOn` column for the out-of-box and custom tables is set to `UserLocal` by default, and the `DateTimeAttributeMetadata.CanChangeDateTimeBehavior` managed property is set to `False`, which implies that you cannot change the behavior of these columns. Although users can change the value of the `DateTimeAttributeMetadata.CanChangeDateTimeBehavior` managed property of these columns for custom tables, but they still can’t change the behavior of the columns.  
  
-   For new custom date and time columns, the `DateTimeAttributeMetadata.CanChangeDateTimeBehavior` managed property is set to `True`. This implies that you can change behavior of a custom date and time column from `UserLocal` to either `DateOnly` or `TimeZoneIndependent`; no other behavior transitions are allowed.  
  
     For custom date and time columns that are part of a Dataverse organization, the `DateTimeAttributeMetadata.CanChangeDateTimeBehavior` managed property is set to `True` unless the column or the parent table is not customizable.  
  
    > [!NOTE]
    >  When you update `DateTimeAttributeMetadata.DateTimeBehavior` property of a column from `UserLocal` to `DateOnly`, ensure that you also change the`DateTimeAttributeMetadata.Format` property from `DateAndTime` to `DateOnly`. Otherwise, an exception will occur.  
  
-   The following out-of-box date and time columns in Dataverse are by default set to `DateOnly` and the `DateTimeAttributeMetadata.CanChangeDateTimeBehavior` managed property is set to `False` of these columns, which implies that you cannot change the behavior for these columns:  
  
    |Date and time column|Parent table|  
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
  
     The behavior of these columns is set to `UserLocal` and the `DateTimeAttributeMetadata.CanChangeDateTimeBehavior` managed property to `True`, and you can change the behavior of these columns to `DateOnly` only. No other behavior transitions are allowed.  
  
 After updating the behavior of a column, you must publish the customizations for the change to take effect. Updating the behavior of a date and time column ensures that all the values entered/updated *after* the column behavior was changed, are stored in the system as per the new behavior. This does not impact the values that are already stored in the database, and they continue to be stored as UTC values. However, when you retrieve the existing values using SDK or view it in the UI, the existing values are displayed as per the new behavior of the column. For example, if you changed the behavior of a custom column on an account from `UserLocal` to `DateOnly` and retrieve an existing account record using SDK, the date and time will be displayed as \<Date> followed by time as 12 AM (00:00:00). Similarly, for the behavior change from `UserLocal` to `TimeZoneIndependent`, the actual value in the database will be displayed as is without any time zone conversions.  
  
 The following sample code demonstrates how to update the behavior of a date and time column:  
  
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

// Publish customizations to the account 
PublishXmlRequest pxReq = new PublishXmlRequest
{
    ParameterXml = String.Format("<importexportxml><entities><entity>account</entity></entities></importexportxml>")
};
_serviceProxy.Execute(pxReq);
Console.WriteLine("Published customizations to the Account .\n");
 
``` 
  
 For the complete sample code, see [Sample: Convert date and time values](/dynamics365/customer-engagement/developer/org-service/sample-convert-date-time-behavior).  
  
<a name="Convert"></a>   

## Convert behavior of existing date and time values in the database 

 When you update a date and time column to change its behavior from `UserLocal` to `DateOnly` or `TimeZoneIndependent`, it does not automatically convert the existing column values in the database. The behavior change affects only those values that will be entered or updated in the column *after* the behavior has been changed. The existing date and time values in the system continue to be in UTC, and displayed by Dataverse according to the new behavior when retrieved through SDK or in the UI as explained in the previous section. For columns whose behavior has changed from `UserLocal` to `DateOnly`, you can convert the existing UTC values in the database to appropriate `DateOnly` value to avoid any data anomalies by using the `ConvertDateAndTimeBehavior` message.  
  
 The message enables you to specify a conversion rule (If working with Organization Service see, <xref:Microsoft.Xrm.Sdk.Messages.ConvertDateAndTimeBehaviorRequest.ConversionRule>) to select the time zone to use for conversion of the values from UTC to DateOnly. You can specify one of the following conversion rules:  
  
-   `SpecificTimeZone`: Converts UTC value to a DateOnly value as per the specified Dataverse time zone code. In this case, you also need to specify a value for the <xref:Microsoft.Xrm.Sdk.Messages.ConvertDateAndTimeBehaviorRequest.TimeZoneCode> parameter.  
  
-   `CreatedByTimeZone`: Converts UTC value to a DateOnly value that the user who created the record would see in the UI.  
  
-   `OwnerTimeZone`: Converts UTC value to a DateOnly value that the user who owns the record would see in the UI.  
  
-   `LastUpdatedByTimeZone`: Converts UTC value to a DateOnly value that the user who last updated the record would see in the UI.  
  
 You can use one of the four members of the <xref:Microsoft.Xrm.Sdk.DateTimeBehaviorConversionRule> class to specify a valid value for the <xref:Microsoft.Xrm.Sdk.Messages.ConvertDateAndTimeBehaviorRequest.ConversionRule> parameter.  
  
> [!NOTE]
>  You must have the System Administrator role in your Dataverse instance to execute the <xref:Microsoft.Xrm.Sdk.Messages.ConvertDateAndTimeBehaviorRequest> message.  
  
 When you execute the `ConvertDateAndTimeBehavior` (If working with Organization Service see, <xref:Microsoft.Xrm.Sdk.Messages.ConvertDateAndTimeBehaviorRequest> message), a system job (asynchronous operation) is created to run the conversion request. The `ConvertDateAndTimeBehaviorResponse.JobId` column in the message response displays the ID of the system job that is created as a result of the conversion request. After the system job completes, check the job details (`AsyncOperation.Message`) to view conversion details or errors, if any.  
  
> [!NOTE]
>  We recommend that you group conversion of multiple columns into a single conversion job, and run a single conversion job at a time to ensure that there are no conflicts in the conversion and for optimum system performance.  
  
 Some important points to be considered while using the `ConvertDateAndTimeBehavior` message:  
  
-   You should avoid any major changes to the solutions in Dataverse during the execution of the message such as importing a solution or deleting a column or parent table. Doing so might lead to unexpected behavior; however no data loss will occur.  
  
-   Updates done in the system as a result of executing the message won’t run workflows and plug-ins.  
  
-   Updates done in the system as a result of executing the message won’t change the “last modified on” value for the columns, but will be audited to help the administrators to determine the time of the conversion and the original/changed values for a column.  
  
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
 
 ## Best practices for using time zone

### For my Date/Time column I was expecting (UTC/Local) and I am seeing the opposite value

This is caused by a lack of parity between the column setting and the app form setting. When a column is configured for Time Zone Independent or User Local, it determines if the time zone offset is honored or not when the data is being retrieved from the store. However, the app form also has a setting of UTC or Local. 
 
This tells the form how to interpret the data it receives from the Dataverse. If the data retrieved from the store is time zone independent, but the form is set to local, the UTC data will be displayed as user local time based on the user’s time zone in their profile. The reverse is also true, a user local value from the store will be displayed as UTC if the form is set to UTC. Fortunately, the form’s date time zone values can be modified without disrupting the existing records.

### I picked Date Only in my column, but my form is showing a time picker along with the date

This would happen if you chose a behavior of time zone independent or user local for your date only column. The Dataverse will store a time of 00:00:00 by default, but if you add the column to a form it will assume you need to set the time as well. If you leave the time pickers in the form, users can enter a time and it will be saved as something other than 00:00:00. Here is how can you fix this.
* Edit the form and remove the time picker and associated formulas. This will save the time as 00:00:00 and will still allow for time zone based date calculations.
* If your column is currently set to user local, and you don’t need the date to be time zone calculated, you can change it to date only. This is a permanent change and cannot be undone. This change cannot be made to time zone independent behavior columns. Always be careful changing behaviors as other apps, plugins, or workflows may be relying on the data.

### I have a date only column, but it is showing the wrong date for some users
If this happens, check the behavior that is set up for the date only column. If the column is set to time zone independent or user local, the included timestamp will cause the date to appear differently for different users. The form display settings of UTC or Local will determine if the date displayed is calculated using the user’s time zone settings or if it displays as the UTC value. Changing the form values to UTC instead of user local will prevent time zone offset calculations and will display the UTC date for the saved record. Alternately, if you need this to be a static date that does not change and the column is currently user local, you can change the column behavior to Date Only. Be cautious though as this is cannot be undone.

### My (script/plug-in) is supposed to intercept the date submitted using the Universal Client before the user local conversion occurs, but instead it is being treated as User Local data 

The web client and universal client have slightly different behaviors when it comes to when data is translated between UTC and User Local. 
In the web client, dates are entered into the client, passed to the API as provided, and converted later into user local time. This allowed scripts/plug-ins to retrieve the data and take action before data was passed to the platform services and translated into user local time. 
In the universal client, the translation of a date into user local values happens before the data is passed to the API, because of this, the data provided will not be a UTC date but rather a user local date based on the user who retrieved or posted it. 
To resolve this, a user can either:

* Change the form to time zone independent which will retain the UTC value. This only works if the user does not need the form to display in user local time.
* Modify their script to detect the time zone offset used, recalculate back to UTC within the script, and then take action.
  
### See also  

 [Sample: Convert date and time values](/dynamics365/customer-engagement/developer/org-service/sample-convert-date-time-behavior.md)   
 [Behavior and format of the date and time column](/dynamics365/customer-engagement/developer/customize/behavior-format-date-time-field)   
 [Customize column definitions](/dynamics365/customer-engagement/developer/customize-entity-attribute-metadata)          
 <xref:Microsoft.Xrm.Sdk.Messages.ConvertDateAndTimeBehaviorRequest>      
 <xref:Microsoft.Xrm.Sdk.Metadata.DateTimeAttributeMetadata> 
 [Blog: Working with time zones in the Dataverse](https://powerapps.microsoft.com/en-us/blog/working-with-time-zones-in-the-data-platform/)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
