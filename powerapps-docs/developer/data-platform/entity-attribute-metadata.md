---
title: Column definitions | Microsoft Docs
description: Learn about column definitions use in Microsoft Dataverse.
suite: powerapps
author: NHelgren # GitHub ID
ms.topic: article
ms.date: 07/19/2023
ms.subservice: dataverse-developer
ms.author: nhelgren
search.audienceType:
  - developer
contributors:
 - JimDaly
---

# Column definitions

Tables include a collection of columns that represent the data that can be included within each record. Developers need to understand the different types of columns and how to work with them.

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]

## Columns names

Like tables, each column has a unique name defined when it's created. This name is presented in several ways:

| Name | Description  |
| ------------- | --------------------------------------------------------------------------- |
| `SchemaName`  | Typically, a Pascal cased version of the logical name. For example: `AccountNumber` |
| `LogicalName` | All lower-case name. For example: `accountnumber`|

When you create a custom column, the name you choose is prepended with the customization prefix value of the solution publisher associated with the solution that the column was created within.

You can't change the names of a column after it's created.

Each column also has two properties that can display localized values. The values of these properties are used to refer to the columns in an app.

| Name|Description|
|-----|-----|
| `DisplayName` | Typically, the same as the schema name, but can include spaces. For example: **Account Number**|
| `Description` | A short sentence describing the column or providing guidance to the user. For example:  _Type an ID number or code for the account to quickly search and identify the account in system views._<br />In model-driven apps, this information appears when users hover over the column in a form. |

These are localizable values that are used to refer to the columns in an app. These values can be changed at any time. To add or edit localized values see [Translate customized table, form, and column text into other languages](../../maker/data-platform/export-customized-entity-field-text-translation.md).

## Column types

The `AttributeTypeName` property describes the type of a column. This property contains a value of type `AttributeTypeDisplayName`, which provides a label for each the different types of columns that exist.

> [!NOTE]
> Don't be confused by the <xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.AttributeType> property. The values in this older property are mostly aligned with <xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.AttributeTypeName> except that it shows `ImageAttributeMetadata` and `MultiSelectPicklistAttributeMetadata` as `Virtual`. Refer to the `AttributeTypeName` property rather than the `AttributeType` property.

In the following table:

- These types are grouped by category for comparison.
- For each `AttributeTypeDisplayName` value, the corresponding .NET assembly <xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata> derived class is included where available. There isn't a 1:1 relationship between these types and the `AttributeTypeDisplayName` label.
- Those column types that can be created as custom columns include the corresponding label displayed in the UI.

| Category| AttributeTypeDisplayName/<br />AttributeMetadata Type| Can Create/<br />Label| Description|
|-----|-----|-----|-----|
|Categorization| `BooleanType`<br /><xref:Microsoft.Xrm.Sdk.Metadata.BooleanAttributeMetadata>|Yes<br />**Two Options**|Contains the selected value from Yes/No that usually indicate a true or false value.<br />More information: [Choice](#choice)|
|Categorization| `EntityNameType`<br /><xref:Microsoft.Xrm.Sdk.Metadata.EntityNameAttributeMetadata>| No| Contains a value that corresponds to a table in the system. For internal use only.|
|Categorization| `MultiSelectPicklistType`<br /><xref:Microsoft.Dynamics.CRM.MultiSelectPicklistAttributeMetadata>| Yes<br />**MultiSelect Option Set** | Contains multiple selected values where multiple values can be selected.<br />More information: <br />[Choice](#choice)<br />[Choices columns](multi-select-picklist.md)|
|Categorization| `PicklistType`<br /><xref:Microsoft.Xrm.Sdk.Metadata.PicklistAttributeMetadata>| Yes<br />**Option Set**| Contains the selected value where one option can be selected.<br />More information: [Choice](#choice)|
|Categorization| `StateType`<br /><xref:Microsoft.Xrm.Sdk.Metadata.StateAttributeMetadata>|No| Contains the value that describes the status of a table record.<br />More information: [Choice](#choice)|
|Categorization| `StatusType`<br /><xref:Microsoft.Xrm.Sdk.Metadata.StatusAttributeMetadata>| No| Contains the value that describes the reason for the status of a table record.<br />More information: [Choice](#choice)|
|Collection| `CalendarRulesType`| No| Contains a collection of `CalendarRules` table records.<br />There are no columns that use this type. When generating a proxy, the code generation tool creates two simulated columns that aren't present in the definition. These columns represent a view of the calendar rules records associated in a one-to-many relationship to the table record. |
|Collection| `PartyListType`| No| Contains a collection of `ActivityParty` table records.<br />More information: [ActivityParty table](reference/entities/activityparty.md)|
|Date and Time| `DateTimeType`<br /><xref:Microsoft.Xrm.Sdk.Metadata.DateTimeAttributeMetadata>| Yes<br />**Date and Time**| Contains a date and time value.<br />All date and time columns support values as early as 1/1/1753 12:00 AM.|
|File| `FileType`<br /><xref:Microsoft.Xrm.Sdk.Metadata.FileAttributeMetadata>| Yes<br />**File**| Contains data to support retrieving binary data for a table record.<br />More information: [File columns](file-attributes.md)|
|Image| `ImageType`<br /><xref:Microsoft.Xrm.Sdk.Metadata.ImageAttributeMetadata>| Yes<br />**Image**| Contains data to support retrieving image data for a table record.<br />More information: [Entity Images](entity-metadata.md#entity-images)|
|Managed Property| `ManagedPropertyType`<br /><xref:Microsoft.Xrm.Sdk.Metadata.ManagedPropertyAttributeMetadata>| No| Contains data that describe whether the solution component stored in the table record can be customized when included in a managed solution.<br />More information: [Managed Properties](/power-platform/alm/managed-properties-alm)|
|Quantity| `BigIntType`<br /><xref:Microsoft.Xrm.Sdk.Metadata.BigIntAttributeMetadata>| No | Contains a `BigInt` value. For internal use only.|
|Quantity| `DecimalType`<br /><xref:Microsoft.Xrm.Sdk.Metadata.DecimalAttributeMetadata>| Yes<br />**Decimal Number**| Contains a `Decimal` value. The `Precision` property sets the level of precision. |
|Quantity| `DoubleType`<br /><xref:Microsoft.Xrm.Sdk.Metadata.DoubleAttributeMetadata> | Yes<br />**Floating Point Number**  | Contains a `Double` value. The `Precision` property sets the level of precision.|
|Quantity| `IntegerType`<br /><xref:Microsoft.Xrm.Sdk.Metadata.IntegerAttributeMetadata>| Yes<br />**Whole Number**  | Contains an `Int` value|
| <a name='money_type'></a>Quantity | `MoneyType`<br /><xref:Microsoft.Xrm.Sdk.Metadata.MoneyAttributeMetadata>| Yes<br />**Currency**| Contains a `Decimal` value. The `PrecisionSource` property determines where the level of precision is set.<br />0: The `Precision` property<br />1: The `Organization.PricingDecimalPrecision` column<br />2: The `TransactionCurrency.CurrencyPrecision` column in the table record |
|Reference| `CustomerType`<br /><xref:Microsoft.Xrm.Sdk.Metadata.LookupAttributeMetadata>| Yes<br />**Customer**| Contains a reference to either an account or contact table record. |
|Reference| `LookupType`<br /><xref:Microsoft.Xrm.Sdk.Metadata.LookupAttributeMetadata> | Yes<br />**Lookup**| Contains a reference to a table record. The logical names of the valid records are usually stored in the `Targets` property of the column. |
|Reference| `OwnerType`<br /><xref:Microsoft.Xrm.Sdk.Metadata.LookupAttributeMetadata>  | No | Contains a reference to either a user or team table record.  |
|String| `MemoType`<br /><xref:Microsoft.Xrm.Sdk.Metadata.MemoAttributeMetadata>| Yes<br />**Multiple Lines of Text** | Contains a string value intended to be displayed in a multi-line textbox.|
|String| `StringType`<br /><xref:Microsoft.Xrm.Sdk.Metadata.StringAttributeMetadata>| Yes<br />**Single Line of Text** | Contains a string value intended to be displayed in a single-line textbox.  |
|Unique identifier| `UniqueidentifierType`<br /><xref:Microsoft.Xrm.Sdk.Metadata.UniqueIdentifierAttributeMetadata>| No | Contains a GUID unique identifier value.|
|Virtual| `VirtualType`| No | These columns can't be used in code and can generally be ignored. |

## Supported operations and form usage for columns

Each column includes boolean properties that describe the kinds of operations it can participate in and how it can be in a form.

| Property| Description |
|-----|-----|
|`IsRequiredForForm`| Whether the column must be included in a form|
|`IsValidForCreate`| Whether the column value can be set in a create operation|
|`IsValidForForm`| Whether the column can be included as a column in a form|
|`IsValidForRead`| Whether the column value can be retrieved|
|`IsValidForUpdate`| Whether the column value can be set in an update operation|

If you try to set a value in a create or update operation for a column that isn't valid for that operation, the value is ignored.
If you try to retrieve a column that isn't valid for read, a null value is returned.

## Column requirement level

The `RequiredLevel` property is a Boolean managed property that describes if a column value is required.

This property can have the following values set:

| Name| Value | UI Label| Description |
|-----|-----|-----|-----|
| `None` | 0  | **Optional** | No requirements are specified.|
| `SystemRequired`| 1  | **System Required**| Dataverse requires the column to have a value. |
| `ApplicationRequired` | 2  | **Business Required** | The application requires the column to have a value.  |
| `Recommended`| 3  | **Business Recommended** | It's recommended that the column has a value.|

Dataverse only enforces the `SystemRequired` option for columns created by the system. Custom columns can't be set to use the `SystemRequired` option. Dataverse doesn't return an error when a column with `ApplicationRequired` applied doesn't have a value.

Model-driven apps enforce the `ApplicationRequired` option and use a different presentation for the `Recommended` option. Creators of custom clients may use this information to require similar validation or presentation options.

Because `RequiredLevel` is a managed property, as a publisher of a managed solution you can decide whether consumers of your solution are able to change these settings on columns in your solution.

More information: [Managed Properties](/power-platform/alm/managed-properties-alm)

## Formula, rollup, and calculated columns

Formula, rollup, and calculated columns free the user from having to manually perform calculations and focus on their work. System administrators can define a column to contain the value of many common calculations without having to work with a developer. Developers can also use the platform capabilities to perform these calculations rather than within their own code.

More information:

- [Define rollup columns that aggregate values](../../maker/data-platform/define-rollup-fields.md)
- [Define calculated columns to automate calculations](../../maker/data-platform/define-calculated-fields.md)
- [Formula, rollup, and calculated columns](calculated-rollup-attributes.md)

## Column format

The format values for column controls how it's displayed in model-driven apps. Developer of custom apps may use this information to create similar experiences.

### Integer formats

Use the `Format` property with integer columns to display alternate user experiences for this type.

| Option  | Description  |
|-----|-----|
| `None`  | Displays a text box to edit a number value |
| `Duration` | Displays a drop-down list that contains time intervals. A user can select a value from the list or type an integer value that represents the number of minutes. |
| `TimeZone` | Displays a drop-down list that contains a list of time zones.|
| `Language` | Displays a drop-down list that contains a list of languages that have been enabled for the organization. If no other languages have been enabled, the base language is the only option. The value saved is the LCID value for the language. |

### String formats

Use the `FormatName` property with string columns to set values from the <xref:Microsoft.Xrm.Sdk.Metadata.StringFormatName> to control how the string column is formatted.

| Name| Description  |
|-----|-----|
| `Email`| The form column validates the text value as an e-mail address and creates a mailto link in the column. |
| `PhoneNumber`| The form column contains a link to initiate a phone call by using Skype.|
| `PhoneticGuide` | For internal use only.|
| `Text` | The form displays a text box. |
| `TextArea`| The form displays a text area column.  |
| `TickerSymbol`  | The form displays a link that opens to display a quote for the stock ticker symbol.|
| `URL`  | The form displays a link to open the URL. |
| `VersionNumber` | For internal use only.|

### Date and time formats

The `DateTimeBehavior` property controls the behavior for Date and Time columns.
There are three options:

| Option | Short Description |
|-----|-----|
| `UserLocal`  | Stores the date and time value as UTC value in the system.  |
| `DateOnly`| Stores the actual date value with the time value as 12:00 AM (00:00:00) in the system. |
| `TimeZoneIndependent` | Stores the actual date and time values in the system regardless of the user time zone. |

Use the `Format` property control how the value is to be displayed in a model-driven app regardless of the `DateTimeBehavior`.

| Option| Description  |
|-----|-----|
| DateAndTime | Display the full date and time |
| DateOnly | Display just the date.|

More information: [Behavior and format of the Date and Time column](../../maker/data-platform/behavior-format-date-time-field.md)

## Auto-number columns

You can add an auto-number column for any table. Currently, you can add the column programmatically. There's no user interface to add this type of column.
More information: [Create autonumber columns](create-auto-number-attributes.md)

## Choice

Columns that display a set of options can reference a set of options defined by the column, or they can reference a separate set of options that can be shared by more than one column. This is useful when values in one column also apply to other columns. By referencing a common set of options, the options can be maintained in one place. Those choice that can be shared are _global_ choice. Those defined within the column are _local_ choice.

### Retrieve options data

The organization service provides request classes you can use to retrieve the options used by a column.

#### Use the organization service to retrieve options

Each of the columns with options inherit from <xref:Microsoft.Xrm.Sdk.Metadata.EnumAttributeMetadata> include an [OptionSet Property](xref:Microsoft.Xrm.Sdk.Metadata.EnumAttributeMetadata.OptionSet). This property contains the <xref:Microsoft.Xrm.Sdk.Metadata.OptionSetMetadata> that includes the options within the [Options property](xref:Microsoft.Xrm.Sdk.Metadata.OptionSetMetadata.Options).

With the organization service you can use the following messages to retrieve information about choice:

| Request Class|Description |
|-----|-----|
|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveAllOptionSetsRequest>| Retrieves data about all _global_ choice|
|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveAttributeRequest>| Retrieves data about a column including any choice|
|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMetadataChangesRequest>| Retrieves metadata based on a query that can include choice<br />More information: [Query schema definitions](query-schema-definitions.md) |
|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveOptionSetRequest>| Retrieves data about a _global_ choice.|

More information:

- [Create and edit global choices overview](../../maker/data-platform/create-edit-global-option-sets.md)
- [Sample: Dump choices/picklist information to a file](org-service/samples/dump-picklist-information.md)
- [Customize choices](org-service/metadata-option-sets.md)

#### Use the Web API to retrieve choice values

The Web API provides a RESTful style for querying choice values. You can retrieve local or global choice by retrieving the column within a table. The following example returns the <xref:Microsoft.Dynamics.CRM.OptionSetMetadata> for the choice included in the [Account.AccountCategoryCode property](reference/entities/account.md#BKMK_AccountCategoryCode).

`GET <organization url>/api/data/v9.2/EntityDefinitions(LogicalName='account')/Attributes(LogicalName='accountcategorycode')/Microsoft.Dynamics.CRM.PicklistAttributeMetadata?$select=LogicalName&$expand=OptionSet`

With the Web API, you can also use the [RetrieveMetadataChanges Function](xref:Microsoft.Dynamics.CRM.RetrieveMetadataChanges).

More information: [Query table definitions using the Web API > Retrieving attributes](webapi/query-metadata-web-api.md#retrieving-attributes)

## Column mapping

When you create a new table record in the context of an existing table record, you can automatically transfer certain values from the existing table record as default values for the new table record. This streamlines data entry for people using model-driven apps. Application users see the mapped values and can edit them before saving the entity.

For developers creating custom clients, the same behavior can be achieved by using the `InitializeFrom` message (SDK [InitializeFromRequest Class](xref:Microsoft.Crm.Sdk.Messages.InitializeFromRequest) or Web API [InitializeFrom Function](xref:Microsoft.Dynamics.CRM.InitializeFrom)) to get the entity data with the configured default values set.

More information

- [Map table columns](../../maker/data-platform/map-entity-fields.md)
- [Customize table and column mappings](customize-entity-attribute-mappings.md)

## Logical columns

Logical columns contain values which are stored in different database tables than other columns in the table. In most cases this internal implementation is not relevant to working with Dataverse. When you use logical columns as sources for a calculated field, the values in the calculated field cannot be sorted. Use the [AttributeMetadata.IsLogical](xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.IsLogical) property to detect if an attribute is a logical attribute.

### See also

[Dataverse tables](entities.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
