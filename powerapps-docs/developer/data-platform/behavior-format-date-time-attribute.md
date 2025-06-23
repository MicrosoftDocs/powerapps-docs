---
title: "Configure the behavior and format of the date and time column using code (Microsoft Dataverse) | Microsoft Docs" 
description: "The DateTimeAttributeMetadata class is used to define and manage columns of type DateTime in Microsoft Dataverse."
ms.date: 10/19/2023
ms.reviewer: jdaly
ms.topic: how-to
author: mkannapiran
ms.author: kamanick
ms.subservice: dataverse-developer
search.audienceType: 
  - developer
contributors:
 - JimDaly
---
# Configure the behavior and format of the date and time column using code

If you have users and offices around the world, it's important to properly represent date and time values in multiple time zones. The `DateTimeAttributeMetadata` ([DateTimeAttributeMetadata entity type](xref:Microsoft.Dynamics.CRM.DateTimeAttributeMetadata) or [DateTimeAttributeMetadata Class](xref:Microsoft.Xrm.Sdk.Metadata.DateTimeAttributeMetadata) ) is used to define and manage columns of type `DateTime` in Microsoft Dataverse. Use the `DateTimeBehavior` property (For SDK for .NET see, [DateTimeBehavior Property](xref:Microsoft.Xrm.Sdk.Metadata.DateTimeAttributeMetadata.DateTimeBehavior)) to define whether to store date and time values with or without time zone information, and use the [DateTimeAttributeMetadata.Format Property](xref:Microsoft.Xrm.Sdk.Metadata.DateTimeAttributeMetadata.Format) to specify the display format of these columns.  

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]

You can also use the customization area in Dataverse to define the behavior and format of the date and time columns. More information: [Behavior and format of the Date and Time column](../../maker/data-platform/behavior-format-date-time-field.md).  
  
> [!NOTE]
>  All date and time columns in Dataverse support values as early as 1/1/1753 12:00 AM.  
> 
> If your Date Only or Date Time field is in a solution, you can only change the behavior of an existing managed field if you are the publisher. In order to make a change to these fields, an Upgrade must be made to the solution that added the Date Only or Date Time column. More information: [Upgrade or update a solution](../../maker/data-platform/update-solutions.md)

  
<a name="SpecifyBehavior"></a>   

## Specify the behavior of a date and time column

 You can use the `DateTimeBehavior` ([DateTimeBehavior complex type](xref:Microsoft.Dynamics.CRM.DateTimeBehavior) or [DateTimeBehavior Class](xref:Microsoft.Xrm.Sdk.Metadata.DateTimeBehavior)) to specify a value for the [DateTimeAttributeMetadata entity type](xref:Microsoft.Dynamics.CRM.DateTimeAttributeMetadata).`DateTimeBehavior` property. The `DateTimeBehavior` contains the following members; each member returns a string with the same value as the member name:  
  
|Member name and value|Description|  
|---------------------------|-----------------|  
|`UserLocal`|-   Stores the date and time value as UTC value in the system.<br />-   The retrieve operation returns the UTC value.<br />-   The update operation converts the UTC value to the current user's time zone value, and then stores the updated value as is or as the equivalent UTC value depending on the kind ([DateTimeKind](xref:System.DateTimeKind)) of the value specified for update. If the specified value is of UTC kind, it's stored as is. Otherwise, the UTC-equivalent value is stored.<br />-   Retrieving the formatted value converts from UTC to the user's current time zone based on the time zone and locale setting of the user.<br />-   For the Web API, the column is exposed as DateTimeOffset.<br />-   This behavior is used for system columns like `CreatedOn` and `ModifiedOn`, and can't be changed. You should use this behavior for custom columns where you want to store date and time values with the time zone information.|  
|`DateOnly`|-   Stores the actual date value with no time value.<br />-   Retrieving the formatted value displays the date value.<br />-   For the Web API, the column is exposed as Date.<br />-   This behavior should be used for custom columns that store birthdays and anniversaries, where the time information isn't required.|  
|`TimeZoneIndependent`|-   Stores the actual date and time values in the system regardless of the user time zone.<br />-   For the retrieve and update operations, no time zone conversion is performed, and actual date and time values are returned and updated respectively in the system regardless of the user time zone.<br />-   Retrieving the formatted value displays the date and time value (without any time zone conversion) based on the format as specified by the current user's time zone and locale setting.<br />-   For the Web API, the column is exposed as DateTimeOffset.<br />-   This behavior should be used for columns that store information such as check in and check out time for hotels.|  
  
 The following sample code demonstrates how to set a `UserLocal` behavior for a new date time column:  
  
 ```csharp
/// <summary>
/// Create a new DateTime column for the Account table with UserLocal behavior
/// </summary>
/// <param name="service">Authenticated IOrganizationService instance</param>
static void CreateUserLocalDateTimeColumn(IOrganizationService service) {

    int _languageCode = 1033; //English

    DateTimeAttributeMetadata dtAttribute = new()
    {
        SchemaName = "new_SampleDateTimeAttribute",
        DisplayName = new Label("Sample Date Time Attribute", _languageCode),
        RequiredLevel = new AttributeRequiredLevelManagedProperty(AttributeRequiredLevel.None),
        Description = new Label("Created by SDK Sample", _languageCode),
        DateTimeBehavior = DateTimeBehavior.UserLocal,
        Format = Microsoft.Xrm.Sdk.Metadata.DateTimeFormat.DateAndTime,
        ImeMode = ImeMode.Disabled
    };

    CreateAttributeRequest request = new()
    {
        EntityName = Account.EntityLogicalName,
        Attribute = dtAttribute
    };

    service.Execute(request);
}
```
  
 In the sample code, you can also set the value of the `DateTimeBehavior` property by directly specifying the string value: `DateTimeBehavior = "UserLocal"`  
  
 If you don't specify the behavior while creating a date and time column, the column is created with the `UserLocal` behavior by default. 
  
> [!IMPORTANT]
>  -   Once you create a date and time column with behavior set to `DateOnly` or `TimeZoneIndependent`, you cannot change the behavior of the column. More information: [Change the behavior of a DateTime column](behavior-format-date-time-attribute.md#ChangeBehavior)  
> -   The date and time columns with the `DateOnly` or `TimeZoneIndependent` behavior will be treated like having the `UserLocal` behavior when edited in an earlier version of the Dynamics 365 for Outlook client in the offline mode. This is because the client doesn't understand the new behaviors and won't treat them differently from `UserLocal`. No date and time columns are converted to the new behaviors on upgrade so the best practice here would be to upgrade all Dataverse clients to the latest release before a customizer adopts one of the new behaviors. When online, editing data for columns with the new behaviors will work fine.  
  
<a name="SpecifyFormat"></a>

## Specify format of the date and time column  

 Use the `Format` property to specify the date/time display format of the column irrespective of how it's stored in the system. You can use the `DateTimeFormat` enumeration ([DateTimeFormat enum type](xref:Microsoft.Dynamics.CRM.DateTimeFormat) or [DateTimeFormat Enum](xref:Microsoft.Xrm.Sdk.Metadata.DateTimeFormat)) to specify the display format: `DateAndTime` or `DateOnly`.  
  
 If the `DateTimeAttributeMetadata.DateTimeBehavior` property is set to `DateOnly`, you can't set or change the value of the `DateTimeAttributeMetadata.Format` property to `DateAndTime`.  
  
<a name="UnsupportedQueryOperators"></a>   

## Date and time query operators not supported for DateOnly behavior  

Time-related query operators aren't supported for the `DateOnly` behavior. Other than the time-specific query operators listed here, all the other query operators are supported.  
  
- Older Than X Minutes
- Older Than X Hours  
- Last X Hours  
- Next X Hours  
  
 More information: [Datetime data operators](fetchxml/reference/operators.md#datetime-data)  
  
<a name="ChangeBehavior"></a>
   
## Using OData APIs to submit user local date and time values

In Microsoft Power Platform, when a user submits a date and time in the user-specific time zone through the UI, an automatic calculation sets the data to the correct date and time. It performs an analysis to change any submitted date to the corresponding UTC value based on the column and UI settings.
When you submit a date and time value using Web API operation, the calculation doesn't occur, resulting in unexplained data displays.
For example, if you are in the Pacific time zone and you submit 4/4/2021 12:00, the following happens:

- **Original**: 4/4/2021 12:00 submitter is in the Pacific time zone.
- **Submitted through UI and retrieved as user local**: 4/4/2021 12:00
- **Submitted through API and retrieved as user local**: 4/4/2021 04:00

### Submitting through the UI

UI is set to user local, and column is set to user local.

- **Original Value:** 4/4/2021 12:00 in the Pacific time zone.
- **Value calculated to UTC and stored in Dataverse:** 4/4/2021 12:00 + 8:00 =  4/4/2021T20:00:00Z . This is because PST is -8:00 from UTC, so +8 is added to the stored value. 
- **Value when displayed in UI by a user in the Pacific time zone:** 4/4/2021 12:00. The UI applies the -8:00 UTC offset calculation to 4/4/2021T20:00:00Z for the correct value.

### Submitting through the API

UI is set to user local, and column is set to user local.

- **Original Value:** 4/4/2021T12:00:00 or 4/4/2021T12:00:00Z – no offset or UTC indicator provided. The submitter is in the Pacific time zone.
- **Value calculated to UTC and stored in Dataverse:** No UI calculation is done on submission from OData APIs, so the value is stored as 4/4/2021T12:00:00Z.
- **Value when displayed in UI by a user in the Pacific time zone:** 4/4/2021 4:00. The UI applies the -8:00 UTC offset calculation on the value in Dataverse.

To prevent this issue when using API calls to input data to user local columns, you need to calculate the offset of the user submitting the data and apply the offset.

Using the above example:
**4/4/2021 12:00** would need to be submitted via the API as **4/4/2021T12:00:00-08:00**. The original time and date and include the offset calculation of the current user's time zone. Alternately, the submitter can perform the calculation before submission and submit **4/4/2021T20:00:00Z**.

If you choose to include the offset calculation, you can't have the `Z`, a UTC indicator, because Dataverse won't accept it.

## Change the behavior of a date and time column

 You can update a date and time column to change its behavior if you have the System Customizer role in your Dataverse instance and the `DateTimeAttributeMetadata.CanChangeDateTimeBehavior` managed property for the date and time column is set to `True`.  
  
> [!CAUTION]
>  Before changing the behavior of a date and time column, you should review all the dependencies of the column, such as business rules, workflows, and calculated or rollup columns, to ensure that there are no issues as a result of changing the behavior. System Customizers can restrict modifying the behavior of existing date and time columns using the `DateTimeAttributeMetadata.CanChangeDateTimeBehavior` managed property.  
>   
>  At the minimum, after changing the behavior of a date and time column, you should open each business rule, workflow, calculated column, and rollup column record that is dependent on the changed date and time column, review the information, and save the record to ensure that the latest column behavior and value is used.  
>   
>  After changing the data and time behavior of a calculated or rollup column, open the calculated or rollup column definition editor, and save the column definition to ensure that the column is still valid after the behavior change. System customizers can open the column definition editor for calculated or rollup column by clicking **Edit** next to **Field Type** in the customization area in Dataverse. More information: [Define calculated columns to automate calculations](../../maker/data-platform/define-calculated-fields.md) and [Define rollup columns that aggregate values](../../maker/data-platform/define-rollup-fields.md)  
  
- The behavior of the `CreatedOn` and `ModifiedOn` column for the out-of-box and custom tables is set to `UserLocal` by default, and the `DateTimeAttributeMetadata.CanChangeDateTimeBehavior` managed property is set to `False`, which implies that you can't change the behavior of these columns. Although users can change the value of the `DateTimeAttributeMetadata.CanChangeDateTimeBehavior` managed property of these columns for custom tables, but they still can't change the behavior of the columns.  
  
- For new custom date and time columns, the `DateTimeAttributeMetadata.CanChangeDateTimeBehavior` managed property is set to `True`. This implies that you can change behavior of a custom date and time column from `UserLocal` to either `DateOnly` or `TimeZoneIndependent`; no other behavior transitions are allowed.  
  
     For custom date and time columns that are part of a Dataverse organization, the `DateTimeAttributeMetadata.CanChangeDateTimeBehavior` managed property is set to `True` unless the column or the parent table isn't customizable.  
  
    > [!NOTE]
    >  When you update `DateTimeAttributeMetadata.DateTimeBehavior` property of a column from `UserLocal` to `DateOnly`, ensure that you also change the`DateTimeAttributeMetadata.Format` property from `DateAndTime` to `DateOnly`. Otherwise, an exception will occur.  
  
- The following out-of-box date and time columns in Dataverse are by default set to `DateOnly` and the `DateTimeAttributeMetadata.CanChangeDateTimeBehavior` managed property is set to `False` of these columns, which implies that you can't change the behavior for these columns:  
  
    |Date and time column|Parent table|  
    |---|---|  
    |`anniversary`|Contact|  
    |`birthdate`|Contact|  
    |`duedate`|Invoice|  
    |`estimatedclosedate`|Lead|  
    |`actualclosedate`|Opportunity|  
    |`estimatedclosedate`|Opportunity|  
    |`finaldecisiondate`|Opportunity|  
    |`validfromdate`|Product|  
    |`validtodate`|Product|  
    |`closedon`|Quote|  
    |`expireson`|Quote|  
  
   The behavior of these columns is set to `UserLocal` and the `DateTimeAttributeMetadata.CanChangeDateTimeBehavior` managed property to `True`, and you can change the behavior of these columns to `DateOnly` only. No other behavior transitions are allowed.  
  
 After updating the behavior of a column, you must publish the customizations for the change to take effect. Updating the behavior of a date and time column ensures that all the values entered/updated *after* the column behavior was changed, are stored in the system as per the new behavior. This doesn't impact the values that are already stored in the database, and they continue to be stored as UTC values. However, when you retrieve the existing values using SDK or view it in the UI, the existing values are displayed as per the new behavior of the column. For example, if you changed the behavior of a custom column on an account from `UserLocal` to `DateOnly` and retrieve an existing account record using SDK, the date and time are displayed as \<Date> followed by time as 12 AM (00:00:00). Similarly, for the behavior change from `UserLocal` to `TimeZoneIndependent`, the actual value in the database will be displayed as is without any time zone conversions.  
  
 The following sample code demonstrates how to update the behavior of a date and time column:
  
```csharp
/// <summary>
/// Update the behavior of a DateTime column
/// </summary>
/// <param name="service">Authenticated IOrganizationService instance</param>
static void UpdateBehaviorOfDateTimeColumn(IOrganizationService service) {

    // Retrieve the attribute to update its behavior and format
    RetrieveAttributeRequest retrieveColumnRequest = new()
    {
        EntityLogicalName = Account.EntityLogicalName,
        LogicalName = "new_sampledatetimeattribute",
        RetrieveAsIfPublished = false
    };
    // Execute the request
    RetrieveAttributeResponse attributeResponse =
                    (RetrieveAttributeResponse)service.Execute(retrieveColumnRequest);

    // Modify the values of the retrieved attribute
    DateTimeAttributeMetadata retrievedAttributeMetadata =
                    (DateTimeAttributeMetadata)attributeResponse.AttributeMetadata;

    retrievedAttributeMetadata.DateTimeBehavior = DateTimeBehavior.DateOnly;
    retrievedAttributeMetadata.Format = Microsoft.Xrm.Sdk.Metadata.DateTimeFormat.DateOnly;

    // Update the attribute with the modified value
    UpdateAttributeRequest updateRequest = new()
    {
        Attribute = retrievedAttributeMetadata,
        EntityName = Account.EntityLogicalName,
        MergeLabels = false
    };
    service.Execute(updateRequest);


    // Publish customizations to the account 
    PublishXmlRequest pxReq = new()
    {
        ParameterXml = "<importexportxml><entities><entity>account</entity></entities></importexportxml>"
    };
    service.Execute(pxReq);
}
 
``` 
 
  
<a name="Convert"></a>   

## Convert behavior of existing date and time values in the database

When you update a date and time column to change its behavior from `UserLocal` to `DateOnly` or `TimeZoneIndependent`, it doesn't automatically convert the existing column values in the database. The behavior change affects only those values that will be entered or updated in the column *after* the behavior has been changed. The existing date and time values in the system continue to be in UTC, and displayed by Dataverse according to the new behavior when retrieved through SDK or in the UI as explained in the previous section. For columns whose behavior has changed from `UserLocal` to `DateOnly`, you can convert the existing UTC values in the database to appropriate `DateOnly` value to avoid any data anomalies by using the `ConvertDateAndTimeBehavior` message.  
  
The message enables you to specify a conversion rule (If working with SDK for .NET see, [ConvertDateAndTimeBehaviorRequest.ConversionRule property](xref:Microsoft.Xrm.Sdk.Messages.ConvertDateAndTimeBehaviorRequest.ConversionRule)) to select the time zone to use for conversion of the values from UTC to DateOnly. You can specify one of the following conversion rules:  
  
- `SpecificTimeZone`: Converts UTC value to a DateOnly value as per the specified Dataverse time zone code. In this case, you also need to specify a value for the [ConvertDateAndTimeBehaviorRequest.TimeZoneCode property](xref:Microsoft.Xrm.Sdk.Messages.ConvertDateAndTimeBehaviorRequest.TimeZoneCode).  
- `CreatedByTimeZone`: Converts UTC value to a DateOnly value that the user who created the record would see in the UI.
- `OwnerTimeZone`: Converts UTC value to a DateOnly value that the user who owns the record would see in the UI.
- `LastUpdatedByTimeZone`: Converts UTC value to a DateOnly value that the user who last updated the record would see in the UI.  
  
 You can use one of the four members of the [DateTimeBehaviorConversionRule class](xref:Microsoft.Xrm.Sdk.DateTimeBehaviorConversionRule) to specify a valid value for the [ConversionRule property](xref:Microsoft.Xrm.Sdk.Messages.ConvertDateAndTimeBehaviorRequest.ConversionRule).  
  
> [!NOTE]
>  You must have the System Administrator role in your Dataverse instance to execute the [ConvertDateAndTimeBehaviorRequest class](xref:Microsoft.Xrm.Sdk.Messages.ConvertDateAndTimeBehaviorRequest).  
  
 When you execute the `ConvertDateAndTimeBehavior` (If working with SDK for .NET see, <xref:Microsoft.Xrm.Sdk.Messages.ConvertDateAndTimeBehaviorRequest> message), a system job (asynchronous operation) is created to run the conversion request. The `ConvertDateAndTimeBehaviorResponse.JobId` column in the message response displays the ID of the system job that is created as a result of the conversion request. After the system job completes, check the job details (`AsyncOperation.Message`) to view conversion details or errors, if any.  
  
> [!NOTE]
>  We recommend that you group conversion of multiple columns into a single conversion job, and run a single conversion job at a time to ensure that there are no conflicts in the conversion and for optimum system performance.  
  
 Some important points to be considered while using the `ConvertDateAndTimeBehavior` message:  
  
- You should avoid any major changes to the solutions in Dataverse during the execution of the message such as importing a solution or deleting a column or parent table. Doing so might lead to unexpected behavior; however no data loss occurs.  
- Updates done in the system as a result of executing the message don't run workflows and plug-ins.  
- Updates done in the system as a result of executing the message don't change the "last modified on" value for the columns, but will be audited to help the administrators to determine the time of the conversion and the original/changed values for a column.  
  
 The following sample code shows how to use the message:  
  
```csharp
/// <summary>
/// Demonstrates use of the ConvertDateAndTimeBehavior message
/// </summary>
/// <param name="service">Authenticated IOrganizationService instance</param>
static void ConvertDateAndTimeBehavior(IOrganizationService service)
{

    ConvertDateAndTimeBehaviorRequest request = new()
    {
        Attributes = new EntityAttributeCollection()
        {
            new KeyValuePair<string, StringCollection>("account", new StringCollection()
            { "new_sampledatetimeattribute" })
        },
        ConversionRule = DateTimeBehaviorConversionRule.SpecificTimeZone.Value,
        TimeZoneCode = 190, // Time zone code for India Standard Time (IST) in Dataverse
        AutoConvert = false // Conversion must be done using ConversionRule
    };

    // Execute the request
    var response = (ConvertDateAndTimeBehaviorResponse)service.Execute(request);

    Console.WriteLine($"Asynchronous Job ID: {response.JobId}");
}

```

## Web Client handles time zone conversion differently from Unified Interface

Web Client was [deprecated in 2019](/power-platform/important-changes-coming#legacy-web-client-is-deprecated). If you're migrating [client scripts](../model-driven-apps/client-scripting.md) to its successor, Unified Interface, note the difference in how the two clients handle time zone conversion for User Local columns.

In Web Client, time zone conversion wasn't done on the client side. If a user entered `2018-10-15 07:30` in a Web Client form, the Client API `Xrm.Page.getAttribute(<column name>).getValue()` returned `2018-10-15 07:30`. This value is sent to the server and time zone adjustments happen there when saving the value.

In Unified Client, time zone conversion is done on the client side. If a user in UTC+8 time zone enters `2018-10-15 07:30` in a Unified Client form, the Client API `formContext.getAttribute(<column name>).getValue()` returns the adjusted value `2018-10-14T23:30:00Z`. The server accepts the value as is and not perform further time zone adjustments.

To account for this difference, you can:

- Get the user's time zone offset with [Component Framework UserSettings.getTimeZoneOffsetMinutes method](../component-framework/reference/usersettings/gettimezoneoffsetminutes.md) or [Xrm.Utility.getGlobalContext().userSettings.getTimeZoneOffsetMinutes method](../model-driven-apps/clientapi/reference/Xrm-Utility/getGlobalContext/userSettings.md#gettimezoneoffsetminutes-method) and modify your scripts to account for it.
- Change the column behavior from `UserLocal` to `TimeZoneIndependent` so that entered times aren't adjusted. This is only possible if time zones aren't applicable for the column.


### See also  

 [Behavior and format of the Date and Time column](../../maker/data-platform/behavior-format-date-time-field.md)   
 [Troubleshoot date and time issues in model-driven apps](/troubleshoot/power-platform/power-apps/isolate-and-troubleshoot-common-issues/troubleshoot-model-driven-app-date-time-issues)   
 [Columns overview](../../maker/data-platform/fields-overview.md)   
 [ConvertDateAndTimeBehaviorRequest class](xref:Microsoft.Xrm.Sdk.Messages.ConvertDateAndTimeBehaviorRequest)   
 [DateTimeAttributeMetadata class](xref:Microsoft.Xrm.Sdk.Metadata.DateTimeAttributeMetadata)   
 [Blog: Does how you submit date and time data matter?](https://powerapps.microsoft.com/en-us/blog/does-how-you-submit-date-and-time-data-matter/)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
