---
title: Data types and sizes for Access data migration to Dataverse  | Microsoft Docs
description: Data types and sizes supported for Microsoft Access data migration to Microsoft Dataverse 
author: NHelgren
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
  - model
ms.reviewer: matp
ms.date: 11/19/2021
ms.subservice: dataverse-maker
ms.author: NHelgren
search.audienceType: 
  - maker
search.app: 
  - PowerApps
contributors:
---
# Data types and sizes for Access data migration to Dataverse (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

When you migrate from Microsoft Access to Microsoft Dataverse or Microsoft Dataverse for Teams, you should be aware of a few differences in the data types. These differences include supported types, data type names, and column capacity.

When you migrate, a validation will be executed to ensure:

- The table only includes supported data types.
- The column values in the rows being migrated don't exceed the size limits of Dataverse.

This validation is done to prevent data loss. If a table has columns that exceed the maximum column value in Dataverse, or the table contains data types not supported by Dataverse, the user will be alerted by the Access migration tool validator and will be provided additional information.

Users can choose to either cancel the migration completely, or to continue to migrate all supported content and keep the unsupported content in an Access table.

> [!NOTE]
> [Join the Microsoft Access beta to start your migration](https://aka.ms/AccessAndPowerPlatform)

## Access data types supported by Dataverse

In the following table, the data type mappings supported can assist you in planning your data migration.

|Access data type |Dataverse data type | Can migrate?  |
|---------|---------|---------|
|Short Text  | Text     |   Yes    |
|Long Text   | Multiline text   | Yes   |
|Autonumber  | Autonumber    |  Yes  |
|Date/Time  | Date and Time   |  Yes    |
|Currency  | Currency  | Yes  |
|Number: Decimal  | Decimal Number  | Yes  |
|Yes/No  | Yes/No  |  Yes   |
|Int   | Whole Number   | Yes   |
|Lookup Wizard  | Lookup   | Yes  |
|Multi-Value Lookups   | Choice    | Yes<sup>1</sup>        |
|Hyperlink  | URL   |  Yes       |
|Attachment |File | Yes<sup>2</sup>|

<sup>1</sup>One column multi-value lookups only. Because of the difference in how Dataverse and Access identify these lookups, a manual process is needed in Access before migration. More information: [Export multi-value lookup Access Fields to Dataverse choice columns](#export-multi-value-lookup-access-fields-to-dataverse-choice-columns)

<sup>2</sup> Attachments can be migrated for single attachments per column at this time. 

### Access data types not supported for migration to Dataverse

- OLE Object
- Number Single<sup>3</sup>
- Number Double<sup>3</sup>
- Calculated<sup>4</sup>
- Rich Text

<sup>3</sup>Dataverse includes a float data type; however, it has lower limits than Access. More information including a workaround: [Migrate Number:Single and Number:Double columns to Dataverse](#migrate-numbersingle-and-numberdouble-columns-to-dataverse). You can change these types to decimal in Access and then migrate without data loss.

<sup>4</sup>When you migrate, the calculated field will migrate the last calculated value into a column. Users will need to configure new calculation columns in Dataverse. More information: [Define calculated columns to automate calculations](define-calculated-fields.md)

## Access and Dataverse data size comparison

You'll notice some Dataverse columns don't have the same size capacity as Access. As noted above, if a column contains data too large to be migrated, the migration tool alerts the user that the contents can't be migrated. This is to prevent data loss. This decision is not based on the maximum possible size for the column, but rather the size of the actual data in each row.

|Access/Dataverse data type |Access limit  |Dataverse limit  |
|---------|---------|---------|
|Short Text/Text   |  255 characters   | 4,000 characters    |
|Long Text/Multiline Text  | 1 GB   | 1,048,576 characters    |
|Autonumber   |  2,147,483,647  | 4,000 characters    |
|Date and Time   |  Standard date and time | Standard data and time   |
|Currency<sup>5</sup>  |  Min/max -922,337,203,685,477/+922,337,203,685,477   |  Min/max -922,337,203,685,477/+922,337,203,685,477   |
|Decimal Number  | Min/max -10^28-1/+10^28-1 up to 28 decimals   |  Min/max -100,000,000,000/+100,000,000,000 up to 10 decimal places    |
|Yes/No  |  Boolean   | Boolean   |
|Int/Whole Number   |  Min/max -2^31/+2^31   | Min/max -2,147,483,647/+2,147,483,647   |
|Lookup Wizard/ Lookup   | Multiple column return   |  Single column return   |

<sup>5</sup>The migration tool assumes the currency coming from Access is the Dataverse base currency.

Calculated fields in Access will currently create a column for the content type in Dataverse that stores the calculated value. This could be text, whole number, decimal, and so on. Dataverse can be used to create calculated fields to enable calculations. 

## Export multi-value lookup Access Fields to Dataverse choice columns

Both Access and Dataverse offer users the ability to provide a list of multiple values a user can select from in a row. The ways these are implemented are different.  

Access uses a multi-value lookup, which is a lookup that allows the user to enter any number of values, which will then be presented as a dropdown list for selection. Access has the ability to have more than one column of values for this function.

Dataverse uses choice columns, which are an enumerated list of values that each have a string label associated to them. Users locate and choose the values in a dropdown list using the label values that are stored in the background as an enum selection with a relationship to the table where the labels are stored.

Because of these differences, migrating multi-value lookup columns from Access into Dataverse presents some challenges. The following process must be followed to migrate:

1. Access can only start with a single column multi-value lookup.
1. Access users must add a new column to the multi-value lookup to act as the enum value expected by Dataverse.
1. At export, Dataverse will store this as two columns, which allows both Dataverse and Access to use the lookup appropriately in forms.

### Creating a valid choice field for export to Dataverse

To successfully migrate a choice field from Access, the field must be created in a manner that is similar to the steps described here.

1. Create a new table in Access.
1. Add a **Number** field to the table. It must be a **Number** field to support export to Dataverse.
1. Go to **Design View** in Access. Select the new field, and then select **Lookup Wizard**.
 
   :::image type="content" source="media/select-lookup-wizard.png" alt-text="Select Lookup Wizard in Access":::
   
1. In the Lookup Wizard, select the **I will type in the values that I want** option, and then select **Next**.
1. In the next dialog, enter *2* for the number of columns and then select the field below **Col1**.
1. In **Col1** enter values for three rows by entering *1*, *2*, and *3*. In **Col2** enter values for three rows by entering *red*, *green*, and *blue*.
 
   :::image type="content" source="media/access-lookup-wizard2.png" alt-text="Create two columns with three rows of data each":::
   
1. Select the separator between **Col1** and **Col2** and slide it to the left so that only **Col2** appears.

   :::image type="content" source="media/access-lookup-wizard3.png" alt-text="Move the slider between the columns to the left":::
   
1. Select **Next** > **Next** > **Finish** to complete the Lookup Wizard.
1. Save your changes and return to the **Datasheet View**.
1. Create a new record to validate the choice field works as expected. It should appear like this if it was configured properly.
 
   :::image type="content" source="media/access-lookup-wizard4.png" alt-text="How the choice field should appear in Access":::
   
1. Close the table and migrate it to Dataverse.
1. If everything worked properly, the choice column in Dataverse will appear like this when adding a new record.
 
   :::image type="content" source="media/access-lookup-wizard5.png" alt-text="How the choice column should appear in Dataverse after migration from Access":::

## Migrate Number:Single and Number:Double columns to Dataverse

Both Access and Dataverse include the ability to store floating point numbers. Access uses `Number:Single` and `Number:Double` for this. These data types are often used for any number column. Dataverse has a **Floating Point Number** data type, but it has some limitations with how it's implemented. Dataverse only allows a maximum of five decimal places. Therefore, there is a danger of losing data when migrating floating point numbers from Access to Dataverse. Because of this possibility of data loss, `Number:Single` and `Number:Double` values can't currently be migrated to Dataverse.

However, you can migrate Access `Number:Single` and `Number:Double` data to Dataverse by changing the data type in Access. You can use the Access table designer and change the type of `Number:Single` and `Number:Double` columns to **Decimal**. Then any row that does not exceed the minimum/maximum decimal limits can be migrated.

### See also

[Migrate Microsoft Access data to Microsoft Dataverse](migrate-access-to-dataverse.md)
