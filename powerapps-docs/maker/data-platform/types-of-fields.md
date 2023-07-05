---
title: "Column data types in Microsoft Dataverse (contains video) | MicrosoftDocs"
description: "Understand the different column data types available for your app"
keywords: ""
ms.date: 03/02/2023
ms.custom: 
ms.topic: article
author: "Mattp123"
ms.assetid: 734b4ffa-5543-4f88-8517-299589f433f7
ms.subservice: dataverse-maker
ms.author: matp
ms.reviewer: 
search.audienceType: 
  - maker
---
# Types of columns

The names used for types depend on the designer used. [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) uses a convention that includes the way the data is formatted. The solution explorer type uses a name aligned with the database data type with a format modifier.

Watch this video for a quick overview about data types in Dataverse:
> [!VIDEO https://www.microsoft.com/en-us/videoplayer/embed/RWJ4Su]

The following table includes the corresponding `AttributeTypeDisplayName` API type.

|Power Apps data type |Solution Explorer type| API type|
|--|--|--|
|**Big Integer**|**Time Stamp**|`BigIntType`|
|**Choice**|**Option Set**|`PicklistType`|
|**Choices**|**MultiSelect Field**|`MultiSelectPicklistType`|
|**Currency**|**Currency**|`MoneyType`|
|**Customer**|**Customer**|`CustomerType`|
|**Date and Time**|**Date and Time**<br />*Date and Time* Format|`DateTimeType`|
|**Date Only**|**Date and Time**<br />*Date Only* Format|`DateTimeType`|
|**Decimal Number**|**Decimal Number**|`DecimalType`|
|**Duration**|**Whole Number**<br />*Duration* Format|`IntegerType`|
|**Email**|**Single Line of Text**<br />*Email* Format|`StringType`|
|**File** | **File**   | `FileType`  |
|**Floating Point Number**|**Floating Point Number**|`DoubleType`|
|**Image**|**Image**|`ImageType`|
|**Language**|**Whole Number**<br />*Language* Format|`IntegerType`|
|**Lookup**|**Lookup**|`LookupType`|
|**Multiline Text**|**Multiple Lines of Text**|`MemoType`|
|**Owner**|**Owner**|`OwnerType`|
|**Phone**|**Single Line of Text**<br />*Phone* Format|`StringType`|
|**Status**|**Status**|`StateType`|
|**Status Reason**|**Status Reason**|`StatusType`|
|**Text**|**Single Line of Text**<br />*Text* Format|`StringType`|
|**Text Area**|**Single Line of Text**<br />*Text Area* Format|`StringType`|
|**Ticker Symbol**|**Single Line of Text**<br />Ticker Symbol Format|`StringType`|
|**Timezone**|**Whole Number**<br />*Time Zone* Format|`IntegerType`|
|**Unique Identifier**|**Unique Identifier** or **Primary Key**|`UniqueidentifierType`|
|**URL**|**Single Line of Text**<br />*URL* Format|`StringType`|
|**Whole Number**|**Whole Number**<br />*None* Format|`IntegerType`|
|**Yes/No**|**Two Options**|`BooleanType`|

For more descriptions for each type you can add or edit, see the article for the corresponding designer:
 - [Create and edit columns for Microsoft Dataverse using Power Apps portal: Column Data types](create-edit-field-portal.md#column-data-types)
 - [Create and edit columns for Dataverse using Power Apps solution explorer: Column Data types](create-edit-field-solution-explorer.md#column-data-types)

For more information about how column data types are defined in the API, see [Attribute metadata](../../developer/data-platform/entity-attribute-metadata.md)

## Column types used by the system

There are some columns used by the system that you can't add using the designer.

|Type|Description|
|--|--|
|**Time Stamp**| A Big Integer type used by the system to capture a version number for managing updates to a table.|
|**Customer**|A lookup column that you can use to specify a customer, which can be an account or contact.<br />**Note**: This attribute can be added using solution explorer designer.|
|**Owner**|A system lookup column that references the user or team that is assigned a user or team owned table row.|
|**Status Reason**|A system column that has options that provide additional detail about the Status column. Each option is associated with one of the available Status options. You can add and edit the options. <br /><br /> You can also include custom state transitions to control which status options are available for certain tables. More information: [Define status reason transitions for custom tables](define-status-reason-transitions.md)|
|**Status**|A system column that has options that generally correspond to active and inactive status. Some system attributes have additional options, but all custom attributes have only **Active** and **Inactive** status options.  |
|**Unique Identifier**|A system column stores a globally unique identifier (GUID) value for each row.|

## Text columns

Text columns can contain text characters. This column type has several format options that will change the presentation of the text.

Watch this video for a quick overview about text columns:
> [!VIDEO https://www.microsoft.com/en-us/videoplayer/embed/RWE7j0]

There are three basic text column types. All values indicated below are in number of characters.

|Column type name  |Default value  |Maximum value |Description  |
|---------|---------|---------|---------|
|Text    |    100     |  4000       |  Accepts a single line of text.       |
|Text Area   | 100        |  4000       |  Accepts multiple lines of text. The number of rows displayed for the column can be configured. Use for smaller amounts of text.       |
|Multiline Text   | 150        |  1048576       |  Accepts multiple lines of text. The number of rows displayed for the column can be configured. Use when large amounts of text are needed.       |

## Choices

You can customize forms (main, quick create, and quick view) and email templates by adding multi-select columns that are called **Choices**. When you add a choices column, you can specify multiple values that will be available for users to select. When users fill out the form they can select one, multiple, or all the values displayed in a drop-down list.

For example, if an organization operates in multiple areas or countries/regeions, you can include multiple locations or countries/regions in an 'Area of operation' column. A user can then select one or more locations from the list of available values.

Choices can be used with read-only grids, editable grids, and most forms. Multi-select choices can't be used with: 
- Workflows, business process flows, actions, dialogs, business rules, charts, rollup columns, or calculated columns.
- Reports, SLA<sup>1</sup>, and routing rules<sup>1</sup>.

<sup>1</sup>Table requires Dynamics 365 Customer Service.

### Forms

Choices multi-select columns are supported in the following types of forms:

|Form Type|Availability|
|--|--|
|**Turbo form**|Yes|
|**Refresh form**|Read-only (column will available but can't be edited)|
|**Legacy form**|No|
|**Bulk Edit form**|No|

You can use global choices that are defined in your organization to configure values for the multi-select choices.

<a name="BKMK_UsingTheRightTypeOfNumber"></a>
  
## Using the right type of number

When choosing the correct type of number column to use, the decision to use a **Whole Number** or **Currency** type should be straightforward. The choice between using **Floating Point** or **Decimal** numbers requires more thought.  

Watch this video to help you decide what number column type to use:
> [!VIDEO https://www.microsoft.com/en-us/videoplayer/embed/RWEmPd]
  
Decimal numbers are stored in the database exactly as specified. Floating point numbers store an extremely close approximation of the value. Why choose extremely close approximation when you can have the exact value? The answer is that you get different system performance.  
  
Use decimals when you need to provide reports that require very accurate calculations, or if you typically use queries that look for values that are equal or not equal to another value.  
  
Use floating point numbers when you store data that represents fractions or values that you'll typically query comparing to another value using greater than or less than operators. In most cases, the difference between decimal and float isn't noticeable. Unless you require the most accurate possible calculations, floating point numbers should work for you.  

Big Integers (or BigInt) are large numbers with a max value of 9,223,372,036,854,775,807. It's used to store very large numbers that exceed the capabilities of Whole Number and Decimal.  Some uses for this include storage of time stamp values and as unique IDs, as well as numbers larger than 100 billion.

> [!NOTE]
> BigInt is currently only available for use through API. This includes column creation, data creation, and data management.

## Using currency columns

Currency columns allow for an organization to configure multiple currencies that can be used for rows in the organization. When organizations have multiple currencies, they typically want to be able to perform calculations to provide values using their base currency. When you add a currency column to a table that has no other currency columns, two additional columns are added:  
  
- A lookup column called **Currency** that you can set to any active currency configured for your organization. You can configure multiple active currencies for your organization in **Settings** > **Business Management** > **Currencies**. There you can specify the currency and an exchange rate with the base currency set for your organization. If you have multiple active currencies, you can add the currency column to the form and allow people to specify which currency should be applied to money values for this row. This will change the currency symbol that is shown for the currency columns in the form.  
  
  Individuals can also change their personal options to select a default currency for the rows they create.
  
- A decimal column called **Exchange Rate** that provides the exchange rate for a selected currency associated with the table with respect to the base currency. If this column is added to the form, people can see the value, but they can't edit it. The exchange rate is stored with the currency.  
  
For each currency column you add, another currency column is added with the suffix `_Base` on the name. This column stores the calculation of the value of the currency column you added and the base currency. Again, if this column is added to the form, it can't be edited.  
  
When you configure a currency column you can choose the precision value. There are three options as shown in the following table.  
  
|Option|Description|  
|------------|-----------------|  
|Pricing Decimal Precision|This is a single organization precision to be used for prices found in **Settings** > **Administration** > **System Settings** > **General Tab**.|  
|Currency Precision|This option applies the precision defined for the currency in the row.|  
|Specific precision values|These settings allow for defining a specific set precision using values between  0 and 4.|  
  
<a name="BKMK_DifferentTypesOfLookups"></a> 
  
## Different types of lookups  

When you create a new lookup column you're creating a new Many-to-One (N:1) table relationship between the table you're working with and the **Target Row Type** defined for the lookup. There are additional configuration options for this relationship that are described in [Create and edit relationships between tables](create-edit-entity-relationships.md). But all custom lookups can only allow for a reference to a single row for a single target row type.  
  
However, you should be aware that not every lookup behaves this way. There are several different types of system lookups as shown here.  
  
|Lookup type|Description|  
|-----------------|-----------------|  
|**Simple**|Allows for a single reference to a specific table. All custom lookups are this type.|  
|**Customer**|Allows for a single reference to either an account or a contact row.|  
|**Owner**|Allows for a single reference to either a team or a user row. All team or user-owned tables have one of these. More information: [Add a table as a lookup option in your app](../model-driven-apps/team-entity-lookup.md)|  
|**PartyList**|Allows for multiple references to multiple tables. These lookups are found on the Email table **To** and **Cc** columns. They're also used in the Phone and Appointment tables.|  
|**Regarding**|Allows for a single reference to multiple tables. These lookups are found in the regarding column used in activities.|  

<a name="BKMK_ImageFields"></a>

## Image columns

Use image columns to display a single image per row in the application. Each table can have one image column. You can add an image column to custom tables but not to standard tables. Some standard tables have image columns defined.
  
Even though a table has an image column, displaying that image in a model-driven app requires that you enable two settings. 
- The standard table definition **Primary Image** property value must be set to **Default Image**. Custom tables require a custom image column. Then, you can select that image column for the **Primary Image** value in the custom table definition.  
- The table form where the image is to be displayed must have the **Show image in the form** property enabled.  
  
People choose the image to upload a picture from their computer. Images must be less than 10 MB and must be in one of the following formats:  
  
- jpg
- jpeg
- gif
- tif
- tiff
- bmp
- png
  
When the image is uploaded, it will be converted to a .jpg format and all downloaded images will also use this format. If an animated .gif is uploaded, only the first frame is saved.  
  
When an image is uploaded, it will be resized as a "thumbnail" image to a maximum size of 144 pixels by 144 pixels. People should resize or crop the images before they upload them so that they'll display well using this size. All images are cropped to be square. If both sides of an image are smaller than 144 pixels, the image will be cropped to be a square with the dimensions of the smaller side.

> [!NOTE]
> Image columns don't work with business process flows, business rules, charts, rollup columns, or calculated columns.

### Create an image column and add it to a form

1. Go to [https://make.powerapps.com](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), select **Solutions**, and then open the unmanaged solution that contains the table form where you want to add an image column.
1. Open the table, and then select the **Columns** area.
1. On the command bar, select **Add column**.
1. Enter or select values for the following properties, and then select **Done**.
   - **Display Name**, such as *Recipe image*. 
   - **Name**. This is the unique name that includes the solution publisher prefix and can't be changed once saved.
   - **Data Type**. Select **Image**.
   - **Primary Image**. Image columns that are set as the primary image are displayed in the upper right corner of the form. You can have only one primary image for each table.
   - **Enable column security**. Use to control access for specific columns. More information: [Field-level security to control access](/power-platform/admin/field-level-security)
   - **Enable auditing**. Enables the logging of changes that are made to table records and user access so you can review the activity later. More information: [Administrators Guide: Manage Dataverse auditing](/power-platform/admin/manage-dataverse-auditing)
   - **Sortable in interactive experience dashboard**. Specifies the column will be used to configure interactive dashboards. More information: [Configure filter columns, and security roles for interactive dashboards](../model-driven-apps/configure-interactive-experience-dashboards.md#configure-filter-columns-and-security-roles-for-the-interactive-dashboards)
   - **Maximum image size**. Default value is 10,240 KB. The minimum size is 1 KB and the maximum is 30,720 KB.

1. Select **Save table**.
1. Select the **Form** tab, and then open the form for editing, such as the table main form.
1. Add the image column to the form canvas.
1. On the form editor command bar, select **Save**, and then select **Publish** to make the image column available to users.

App users can now select the image to display on the form. When an app user opens the form for a record, they can select **Choose file**, select the image, and then save the record. Then, the image is displayed on the form where the image column is located.

The image column in this example is the primary image so the image also appears on the upper left of the form.

:::image type="content" source="media/primary-image-example.png" alt-text="Form at runtime with french fries primary image displayed on a recipe table record":::

Users can select **Open** to display the image full size in a new browser tab or select **Delete** to remove the image from the record and Dataverse.

More information for developers working with image data:
- [table metadata > table images](/powerapps/developer/data-platform/entity-metadata#entity-images)
- [Image attributes](../../developer/data-platform/image-attributes.md)

## File columns

The **File** column is used for storing binary data. The primary intended use of this column is to store a single image, note, or attachment. However, storage of other forms of binary data is also possible. One or more columns of this data type can be added to an existing standard customizable table or a custom table.

The default **Maximum file size** is 32 MB and the largest size you can set is 131,072 KB (131 MB). The file size limit can be set individually for each column of file type added to a table. 

>[!NOTE]
> - Once the maximum file size has been saved, it can't be changed.
> - File columns don't work with business process flows, business rules, charts, rollup columns, or calculated columns.

To create a file column, on the left pane in Power Apps select **Solutions**, open the solution you want, open the table you want, select the **Columns** area, select **Add Column**, and then in the **Column properties** pane, select **File** as the **Data type**. 

More information for developers working with file data: [File attributes](../../developer/data-platform/file-attributes.md)

## Fx Formula columns

Built on Power Fx, use an Fx formula column to perform operations that return values during fetch operations. Formula columns use the Power Fx syntax that's similar to Office Excel. More information: [Work with formula columns (preview)](formula-columns.md)

## Searching and sorting columns

Most columns have options to enable searching or sorting of the column's contents. 

### Searchable

Almost every column data type is created with the **Searchable** value enabled. This can be disabled at the time of creation, or later after the column is created. The following data types can't be search enabled:

- File. Files are stored and retrieved using reference URLS and because of this they can't be searched.
- Formulas. Formulas are used to create a dynamically calculated output and because of this can't be searched.
- Image. Images are stored and retrieved using reference URLS and because of this they can't be searched.
- Multivalue lookup (PartyList). Some system lookup columns can contain multiple values. For example, the **To** lookup column of **Email** rows can contain multiple recipients. Searching multivalue lookup columns isn't supported.

The **Customer** datatype is search enabled by default and this can't be disabled. It's required to be searchable by the system.

### Sortable

Almost every data type is created with the **Sortable** value disabled. The value can be changed at the time of creation or after later after the column is created. The following data types don't provide the ability to enable a sortable attribute:

- Choices. Sorting columns with multiple values isn't supported.
- Customer. Customer is a standard lookup column and can't be sorted because it's dynamically retrieved.
- File. Files are stored using reference URLS and sorting these aren't useful.
- Formulas. Formulas are used to create a dynamically calculated output and because of this can't be sorted.
- Image. There's no meaningful way to sort images.
- Multivalue lookup (PartyList). Some system lookup columns can contain multiple values. For example, the **To** lookup column of **Email** rows can contain multiple recipients. Sorting columns with multiple values isn't supported.

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
