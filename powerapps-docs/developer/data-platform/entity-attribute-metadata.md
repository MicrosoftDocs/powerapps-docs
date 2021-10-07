---
title: Column definitions | Microsoft Docs
description: Learn about column definitions use in Microsoft Dataverse.
services: ""
suite: powerapps
documentationcenter: na
author: "mayadumesh" # GitHub ID
manager: kvivek
editor: ""
tags: ""
ms.service: powerapps
ms.devlang: na
ms.topic: article
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 14/19/2021
ms.subservice: dataverse-developer
ms.author: jdaly
search.audienceType:
  - developer
search.app:
  - PowerApps
  - D365CE
---

# Column definitions

Tables include a collection of columns that represent the data that can be included within each record. Developers need to understand the different types of columns and how to work with them.

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]

More information: [Introduction to table columns](/dynamics365/customer-engagement/developer/introduction-entity-attributes)

## Columns names

Like tables, each column has a unique name defined when it is created. This name is presented in several ways:

| Name          | Description                                                                 |
| ------------- | --------------------------------------------------------------------------- |
| `SchemaName`  | Typically, a Pascal cased version of the logical name. i.e. `AccountNumber` |
| `LogicalName` | All lower-case name. i.e. `accountnumber`                                   |

When you create a custom column, the name you choose will be prepended with the customization prefix value of the solution publisher associated with the solution that the column was created within.

You cannot change the names of a column after it is created.

Each column also has two properties that can display localized values. These are the values that are used to refer to the columns in an app.

| Name          | Description                                                                                                                                                                                                                                                                                |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `DisplayName` | Typically, the same as the schema name, but can include spaces. i.e. **Account Number**                                                                                                                                                                                                    |
| `Description` | A short sentence describing the column or providing guidance to the user. i.e. _Type an ID number or code for the account to quickly search and identify the account in system views._<br />In model-driven apps, this information will appear when users hover over the column in a form. |

These are the localizable values that are used to refer to the columns in an app. These values can be changed at any time. To add or edit localized values see [Microsoft Dataverse Customization Guide: Translate customized table and column text into other languages](/dynamics365/customer-engagement/customize/export-customized-entity-field-text-translation).

## Column types

The `AttributeTypeName` property describes the type of a column. This property contains a value of type `AttributeTypeDisplayName` which provides a label for each the different types of columns that exist.

> [!NOTE]
> Don't be confused by the [AttributeType](/dotnet/api/microsoft.xrm.sdk.metadata.attributemetadata.attributetype#Microsoft_Xrm_Sdk_Metadata_AttributeMetadata_AttributeType) property. The values in this older property are mostly aligned with [AttributeTypeName](/dotnet/api/microsoft.xrm.sdk.metadata.attributemetadata.attributetypename#Microsoft_Xrm_Sdk_Metadata_AttributeMetadata_AttributeTypeName) except that it shows `ImageAttributeMetadata` and `MultiSelectPicklistAttributeMetadata` as `Virtual`. Refer to the `AttributeTypeName` property rather than the `AttributeType` property.

In the following table:

- These types are grouped by category for comparison.
- For each `AttributeTypeDisplayName` value, the corresponding .NET assembly [AttributeMetadata](/dotnet/api/microsoft.xrm.sdk.metadata.attributemetadata) derived class is included where available. There is not a 1:1 relationship between these types and the `AttributeTypeDisplayName` label.
- Those column types that can be created as custom columns include the corresponding label displayed in the UI.

| Category                          | AttributeTypeDisplayName/<br />AttributeMetadata Type                                                                                              | Can Create/<br />Label              | Description                                                                                                                                                                                                                                                                                                                                                  |
| --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Categorization                    | `BooleanType`<br />[BooleanAttributeMetadata](/dotnet/api/microsoft.xrm.sdk.metadata.booleanattributemetadata)                                     | Yes<br />**Two Options**            | Contains the selected value from Yes/No that usually indicate a true or false value.<br />More information: [Choice](#choice)                                                                                                                                                                                                                                |
| Categorization                    | `EntityNameType`<br />[EntityNameAttributeMetadata](/dotnet/api/microsoft.xrm.sdk.metadata.entitynameattributemetadata)                            | No                                  | Contains a value that corresponds to a table in the system. For internal use only.                                                                                                                                                                                                                                                                           |
| Categorization                    | `MultiSelectPicklistType`<br />[MultiSelectPicklistAttributeMetadata](/dotnet/api/microsoft.xrm.sdk.metadata.multiselectpicklistattributemetadata) | Yes<br />**MultiSelect Option Set** | Contains multiple selected values where multiple values can be selected.<br />More information: <br />[Choice](#choice)<br />[Choices columns](/dynamics365/customer-engagement/developer/multi-select-picklist)                                                                                                                                             |
| Categorization                    | `PicklistType`<br />[PicklistAttributeMetadata](/dotnet/api/microsoft.xrm.sdk.metadata.picklistattributemetadata)                                  | Yes<br />**Option Set**             | Contains the selected value where one option can be selected.<br />More information: [Choice](#choice)                                                                                                                                                                                                                                                       |
| Categorization                    | `StateType`<br />[StateAttributeMetadata](/dotnet/api/microsoft.xrm.sdk.metadata.stateattributemetadata)                                           | No                                  | Contains the value that describes the status of a table record.<br />More information: [Choice](#choice)                                                                                                                                                                                                                                                     |
| Categorization                    | `StatusType`<br />[StatusAttributeMetadata](/dotnet/api/microsoft.xrm.sdk.metadata.statusattributemetadata)                                        | No                                  | Contains the value that describes the reason for the status of a table record.<br />More information: [Choice](#choice)                                                                                                                                                                                                                                      |
| Collection                        | `CalendarRulesType`                                                                                                                                | No                                  | Contains a collection of `CalendarRules` table records.<br />There are no columns that use this type. When generating a proxy, the code generation tool will create two simulated columns that are not present in the definition. These columns represent a view of the calendar rules records associated in a one-to-many relationship to the table record. |
| Collection                        | `PartyListType`                                                                                                                                    | No                                  | Contains a collection of `ActivityParty` table records.<br />More information: [ActivityParty table](reference/entities/activityparty.md)                                                                                                                                                                                                                    |
| Date and Time                     | `DateTimeType`<br />[DateTimeAttributeMetadata](/dotnet/api/microsoft.xrm.sdk.metadata.datetimeattributemetadata)                                  | Yes<br />**Date and Time**          | Contains a date and time value.<br />All date and time columns support values as early as 1/1/1753 12:00 AM.                                                                                                                                                                                                                                                 |
| File                              | `FileType`<br />[FileAttributeMetadata](/dotnet/api/microsoft.xrm.sdk.metadata.fileattributemetadata)                                              | Yes<br />**File**                   | Contains data to support retrieving binary data for a table record.<br />More information: [File columns](file-attributes.md)                                                                                                                                                                                                                                |
| Image                             | `ImageType`<br />[ImageAttributeMetadata](/dotnet/api/microsoft.xrm.sdk.metadata.imageattributemetadata)                                           | Yes<br />**Image**                  | Contains data to support retrieving image data for a table record.<br />More information: [Entity Images](entity-metadata.md#entity-images)                                                                                                                                                                                                                  |
| Managed Property                  | `ManagedPropertyType`<br />[ManagedPropertyAttributeMetadata](/dotnet/api/microsoft.xrm.sdk.metadata.managedpropertyattributemetadata)             | No                                  | Contains data that describe whether the solution component stored in the table record can be customized when included in a managed solution.<br />More information: [Managed Properties](/power-platform/alm/managed-properties-alm)                                                                                                                         |
| Quantity                          | `BigIntType`<br />[BigIntAttributeMetadata](/dotnet/api/microsoft.xrm.sdk.metadata.bigintattributemetadata)                                        | No                                  | Contains a `BigInt` value. For internal use only.                                                                                                                                                                                                                                                                                                            |
| Quantity                          | `DecimalType`<br />[DecimalAttributeMetadata](/dotnet/api/microsoft.xrm.sdk.metadata.decimalattributemetadata)                                     | Yes<br />**Decimal Number**         | Contains a `Decimal` value. The `Precision` property sets the level of precision.                                                                                                                                                                                                                                                                            |
| Quantity                          | `DoubleType`<br />[DoubleAttributeMetadata](/dotnet/api/microsoft.xrm.sdk.metadata.doubleattributemetadata)                                        | Yes<br />**Floating Point Number**  | Contains a `Double` value. The `Precision` property sets the level of precision.                                                                                                                                                                                                                                                                             |
| Quantity                          | `IntegerType`<br />[IntegerAttributeMetadata](/dotnet/api/microsoft.xrm.sdk.metadata.integerattributemetadata)                                     | Yes<br />**Whole Number**           | Contains an `Int` value                                                                                                                                                                                                                                                                                                                                      |
| <a name='money_type'></a>Quantity | `MoneyType`<br />[MoneyAttributeMetadata](/dotnet/api/microsoft.xrm.sdk.metadata.moneyattributemetadata)                                           | Yes<br />**Currency**               | Contains a `Decimal` value. The `PrecisionSource` property determines where the level of precision is set.<br />0 : The `Precision` property<br />1 : The `Organization.PricingDecimalPrecision` column<br />2 : The `TransactionCurrency.CurrencyPrecision` column in the table record                                                                      |
| Reference                         | `CustomerType`<br />[LookupAttributeMetadata](/dotnet/api/microsoft.xrm.sdk.metadata.lookupattributemetadata)                                      | Yes<br />**Customer**               | Contains a reference to either an account or contact table record.                                                                                                                                                                                                                                                                                           |
| Reference                         | `LookupType`<br />[LookupAttributeMetadata](/dotnet/api/microsoft.xrm.sdk.metadata.lookupattributemetadata)                                        | Yes<br />**Lookup**                 | Contains a reference to a table record. The logical names of the valid records are usually stored in the `Targets` property of the column.                                                                                                                                                                                                                   |
| Reference                         | `OwnerType`<br />[LookupAttributeMetadata](/dotnet/api/microsoft.xrm.sdk.metadata.lookupattributemetadata)                                         | No                                  | Contains a reference to either a user or team table record.                                                                                                                                                                                                                                                                                                  |
| String                            | `MemoType`<br />[MemoAttributeMetadata](/dotnet/api/microsoft.xrm.sdk.metadata.memoattributemetadata)                                              | Yes<br />**Multiple Lines of Text** | Contains a string value intended to be displayed in a multi-line textbox.                                                                                                                                                                                                                                                                                    |
| String                            | `StringType`<br />[StringAttributeMetadata](/dotnet/api/microsoft.xrm.sdk.metadata.stringattributemetadata)                                        | Yes<br />**Single Line of Text**    | Contains a string value intended to be displayed in a single-line textbox.                                                                                                                                                                                                                                                                                   |
| Unique identifier                 | `UniqueidentifierType`<br />[UniqueIdentifierAttributeMetadata](/dotnet/api/microsoft.xrm.sdk.metadata.uniqueidentifierattributemetadata)          | No                                  | Contains a GUID unique identifier value.                                                                                                                                                                                                                                                                                                                     |
| Virtual                           | `VirtualType`                                                                                                                                      | No                                  | These columns cannot be used in code and can generally be ignored.                                                                                                                                                                                                                                                                                           |

## Supported operations and form usage for columns

Each column includes boolean properties that describe the kinds of operations it can participate in and how it can be in a form.

| Property            | Description                                                 |
| ------------------- | ----------------------------------------------------------- |
| `IsRequiredForForm` | Whether the column must be included in a form.              |
| `IsValidForCreate`  | Whether the column value can be set in a create operation.  |
| `IsValidForForm`    | Whether the column can be included as a column in a form.   |
| `IsValidForRead`    | Whether the column value can be retrieved.                  |
| `IsValidForUpdate`  | Whether the column value can be set in an update operation. |

If you try to set a value in a create or update operation for a column that is not valid for that operation, the value will be ignored.
If you try to retrieve a column that is not valid for read, a null value will be returned.

## Column requirement level

The `RequiredLevel` property is a Boolean managed property that describes if a column value is required.

This property can have the following values set:

| Name                  | Value | UI Label                 | Description                                           |
| --------------------- | ----- | ------------------------ | ----------------------------------------------------- |
| `None`                | 0     | **Optional**             | No requirements are specified.                        |
| `SystemRequired`      | 1     | **System Required**      | The data service requires the column to have a value. |
| `ApplicationRequired` | 2     | **Business Required**    | The application requires the column to have a value.  |
| `Recommended`         | 3     | **Business Recommended** | It is recommended that the column has a value.        |

Dataverse only enforces the `SystemRequired` option for columns created by the system. Custom columns cannot be set to use the `SystemRequired` option. The data service does not return an error when a column with `ApplicationRequired` applied does not have a value.

Model-driven apps will enforce the `ApplicationRequired` option and use a different presentation for the `Recommended` option. Creators of custom clients may use this information to require similar validation or presentation options.

Because this is a managed property, as a publisher of a managed solution you can decide whether consumers of your solution are able to change these settings on columns in your solution.

More information: [Managed Properties](/power-platform/alm/managed-properties-alm)

## Rollup and calculated columns

Calculated and rollup columns free the user from having to manually perform calculations and focus on their work. System administrators can define a column to contain the value of many common calculations without having to work with a developer. Developers can also leverage the platform capabilities to perform these calculations rather than within their own code.

More information:

- [Dataverse Customization Guide: Define rollup columns that aggregate values](/dynamics365/customer-engagement/customize/define-rollup-fields)
- [Dataverse Customization Guide: Calculated and rollup columns](/dynamics365/customer-engagement/customize/define-calculated-fields)
- [Calculated and rollup columns](/dynamics365/customer-engagement/developer/calculated-rollup-attributes)

## Column format

The format values for column controls how it is displayed in model-driven apps. Developer of custom apps may use this information to create similar experiences.

### Integer formats

Use the `Format` property with integer columns to display alternate user experiences for this type.

| Option     | Description                                                                                                                                                                                                                                      |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `None`     | Displays a text box to edit a number value                                                                                                                                                                                                       |
| `Duration` | Displays a drop-down list that contains time intervals. A user can select a value from the list or type an integer value that represents the number of minutes.                                                                                  |
| `TimeZone` | Displays a drop-down list that contains a list of time zones.                                                                                                                                                                                    |
| `Language` | Displays a drop-down list that contains a list of languages that have been enabled for the organization. If no other languages have been enabled, the base language will be the only option. The value saved is the LCID value for the language. |

### String formats

Use the `FormatName` property with string columns to set values from the [StringFormatName Class](/dotnet/api/microsoft.xrm.sdk.metadata.stringformatname) to control how the string column is formatted.

| Name            | Description                                                                                               |
| --------------- | --------------------------------------------------------------------------------------------------------- |
| `Email`         | The form column will validate the text value as an e-mail address and create a mailto link in the column. |
| `PhoneNumber`   | The form column will contain a link to initiate a phone call by using Skype.                              |
| `PhoneticGuide` | For internal use only.                                                                                    |
| `Text`          | The form will display a text box.                                                                         |
| `TextArea`      | The form will display a text area column.                                                                 |
| `TickerSymbol`  | The form will display a link that will open to display a quote for the stock ticker symbol.               |
| `URL`           | The form will display a link to open the URL.                                                             |
| `VersionNumber` | For internal use only.                                                                                    |

### Date and time formats

The `DateTimeBehavior` property to controls the behavior for Date and Time columns.
There are three options:

| Option                | Short Description                                                                      |
| --------------------- | -------------------------------------------------------------------------------------- |
| `UserLocal`           | Stores the date and time value as UTC value in the system.                             |
| `DateOnly`            | Stores the actual date value with the time value as 12:00 AM (00:00:00) in the system. |
| `TimeZoneIndependent` | Stores the actual date and time values in the system regardless of the user time zone. |

Use the `Format` property control how the value is to be displayed in a model-driven app regardless of the `DateTimeBehavior`.

| Option      | Description                    |
| ----------- | ------------------------------ |
| DateAndTime | Display the full date and time |
| DateOnly    | Display just the date.         |

More information: [Behavior and format of the date and time columns](/dynamics365/customer-engagement/developer/behavior-format-date-time-attribute)

## Auto-number columns

You can add an auto-number column for any table. Currently, you can add the column programmatically. There is no user interface to add this type of column.
More information: [Create auto-number columns](/dynamics365/customer-engagement/developer/create-auto-number-attributes)

## Choice

Those columns which display a set of options can reference a set of options defined by the column or they can reference a separate set of options that can be shared by more than one column. This is particularly useful when values in one column also apply to other columns. By referencing a common set of options, the options can be maintained in one place. Those choice that can be shared are _global_ choice. Those defined within the column are _local_ choice.

### Retrieve options data

The organization service provides request classes you can use to retrieve the options used by a column.

#### Use the organization service to retrieve options

Each of the columns with options inherit from [EnumAttributeMetadata](/dotnet/api/microsoft.xrm.sdk.metadata.enumattributemetadata) and include an [OptionSet Property](/dotnet/api/microsoft.xrm.sdk.metadata.enumattributemetadata.optionset). This property contains the [OptionSetMetadata](/dotnet/api/microsoft.xrm.sdk.metadata.optionsetmetadata) that includes the options within the [Options property](/dotnet/api/microsoft.xrm.sdk.metadata.optionsetmetadata.options).

With the organization service you can use the following messages to retrieve information about choice:

| Request Class                                                                                           | Description                                                                                                                                                                                                       |
| ------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [RetrieveAllOptionSetsRequest](/dotnet/api/microsoft.xrm.sdk.messages.retrievealloptionsetsrequest)     | Retrieves data about all _global_ choice                                                                                                                                                                          |
| [RetrieveAttributeRequest](/dotnet/api/microsoft.xrm.sdk.messages.retrieveattributerequest)             | Retrieves data about a column including any _local_ choice                                                                                                                                                        |
| [RetrieveMetadataChangesRequest](/dotnet/api/microsoft.xrm.sdk.messages.retrievemetadatachangesrequest) | Retrieves metadata based on a query that can include _local_ choice<br />More information: [Retrieve and detect changes to metadata](/dynamics365/customer-engagement/developer/retrieve-detect-changes-metadata) |
| [RetrieveOptionSetRequest](/dotnet/api/microsoft.xrm.sdk.messages.retrieveoptionsetrequest)             | Retrieves data about a _global_ choice.                                                                                                                                                                           |

More information:

- [Sample: Dump column choices table definitions to a file](/dynamics365/customer-engagement/developer/org-service/sample-dump-attribute-picklist-metadata-file)
- [Dataverse Developer Guide : Customize global choice](/dynamics365/customer-engagement/developer/org-service/customize-global-option-sets)

#### Use the Web API to retrieve choice values

The Web API provides a RESTful style for querying choice values. You can retrieve local or global choice by retrieving the column within a table. The following example returns the [OptionSetMetadata](/dynamics365/customer-engagement/web-api/optionsetmetadata) for the choice included in the [Account](reference/entities/account.md).[AccountCategoryCode property](reference/entities/account.md#BKMK_AccountCategoryCode).

`GET <organization url>/api/data/v9.0/EntityDefinitions(LogicalName='account')/Attributes(LogicalName='accountcategorycode')/Microsoft.Dynamics.CRM.PicklistAttributeMetadata?$select=LogicalName&$expand=OptionSet`

With the Web API you can also use the [RetrieveMetadataChanges Function](/dynamics365/customer-engagement/web-api/retrievemetadatachanges).

More information: [Query table definitions using the Web API > Querying EntityMetadata column](/dynamics365/customer-engagement/developer/webapi/query-metadata-web-api#querying-entitymetadata-attributes)

## Column mapping

When you create a new table record in the context of an existing table record, you can automatically transfer certain values from the existing table record as default values for the new table record. This streamlines data entry for people using model-driven apps. Application users see the mapped values and can edit them before saving the entity.

For developers creating custom clients, the same behavior can be achieved by using the `InitializeFrom` message (Organization service [InitializeFromRequest Class](/dotnet/api/microsoft.crm.sdk.messages.initializefromrequest) or Web API [InitializeFrom Function](/dynamics365/customer-engagement/web-api/initializefrom)) to get the entity data with the configured default values set.

More information

- [Dataverse Customization Guide: Map table columns](/dynamics365/customer-engagement/customize/map-entity-fields#BKMK_mappingEntityFields)
- [Dataverse Developer Guide Customize table and column mappings](/dynamics365/customer-engagement/developer/customize-entity-attribute-mappings)

### See also

[Dataverse tables](entities.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
