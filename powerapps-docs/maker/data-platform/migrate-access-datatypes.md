---
title: Data types and sizes for Access data migration to Dataverse  | Microsoft Docs
description: Data types and sizes supported for Microsoft Access data migration to Microsoft Dataverse 
author: NHelgren
ms.service: powerapps
ms.topic: overview
ms.custom: 
  - model
  - intro-internal
ms.reviewer: matp
ms.date: 10/18/2021
ms.subservice: teams
ms.author: NHelgren
search.audienceType: 
  - maker
search.app: 
  - PowerApps
contributors:
---
# Data types and sizes for Access data migration to Dataverse

When you migrate from Microsoft Access to Microsoft Dataverse, there are a few differences in the data types that you should be aware of. These differences include supported types, data type names, and column capacity.

When you migrate, a validation will be executed to ensure:

- The table only includes supported data types.
- The column values in the rows being migrated don't exceed the size limits of Dataverse.

This validation is done to prevent data loss. If a table has columns that exceed the maximum column value in Dataverse, or the table contains data types not supported by Dataverse, the user will be alerted by the Access migration tool validator and will be provided additional information.

Users can choose to either cancel the migration completely, or to continue to migrate over all supported content and keep the unsupported content in an Access table.

## Access data types supported by Dataverse

In the table below, the data type mappings supported can assist you in planning your data migration.

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

<sup>1</sup>One column multi-value lookups only. Because of the difference in how Dataverse and Access identify these lookups, a manual process is needed in Access before migration. More information: [Export multi-value lookup Access Fields to Dataverse choice columns](#export-multi-value-llookup-access-fields-to-dataverse-choice-columns)

### Access data types not supported for migration to Dataverse

- OLE Object
- Attachment
- Number Single<sup>2</sup>
- Number Double<sup>2</sup>
- Calculated<sup>3</sup>
- Rich Text

<sup>2</sup>Dataverse includes a float data type, however it has much lower limits than Access, so for now we have chosen not to support to prevent data loss.

<sup>3</sup>When you migrate, the calculated field will be created and the last calculated value will be migrated. Users will need to configure new calculated fields in Dataverse.

## Access and Dataverse data size comparison 

You'll notice some Dataverse columns don't have the same size capacity as Access. As noted above, if a column contains data too large to be migrated, the migration tool alerts the user that the contents can't be migrated. This is to prevent data loss. This decision is not based on the maximum possible size for the column, but rather the size of the actual data in each row.


|Access/Dataverse data type |Access limit  |Dataverse limit  |
|---------|---------|---------|
|Short Text/Text   |  255 characters   | 4000 charaters    |
|Long Text/Multiline Text  | 1 GB   | 1,048,576 characters    |
|Autonumber   |  2,147,483,647  | 4000 characters    |
|Date and Time   |  Standard data and time | Standard data and time   |
|Currency<sup>4</sup>  |  Min/max 922,337,203,685,477     |  min/max 922,337,203,685,477   |
|Decimal Number  | min/max - 10^28-1 up to 28 decimals   |  Min/max 100,000,000,000 up to 10 decimal places    |
|Yes/No  |  Boolean   | Boolean   |
|Int/Whole Number   |  Min/max 2^31   | Min/max 2,147,483,647   |
|Lookup Wizard/ Lookup   | Multiple column return   |  Single column return   |

<sup>4</sup>The migration tool assumes the currency coming from Access is the Dataverse base currency.

Calculated fields in Access will currently create a column in Dataverse that stores the calculated value. Dataverse can be used to create calculated fields for future calculations.

## Export multi-value lookup Access Fields to Dataverse choice columns 

Both Access and Dataverse offer users the ability to provide a list of multiple values a user can select from in a row. The ways these are implemented are different.  

Access uses a multi-value lookup, which is a lookup that allows the user to enter any number of values which will then be presented as a drop-down list for selection. Access has the ability to have more than one column of values for this function.

Dataverse uses choice columns, which is an enumerated list of values that each have a string label associated to them. Users locate and choose the values in a drop-down list using the label values that are stored in the background as an enum selection with a relationship to the table where the labels are stored.

Because of these differences, migrating multi-value lookup columns from Access into Dataverse presents some challenges. The following process must be followed to migrate:

1. Access can only start with a single column multi-value lookup.
1. Access users must add a new column to the multi-value lookup to act as the enum value expected by Dataverse.
1. At export, Dataverse will store this as 2 columns, which allows both Dataverse and Access to use the lookup appropriately in forms.

### Creating a valid choice field for export to Dataverse

To successfully migrate a choice field from Access, the field must be created in a similar manner.

1. Create a new table in Access.
1. Add a **Number** field to the table. It must be a **Number** field to support export to Dataverse.
1. Go to **Design View** in Access. Select the new field, and then select **Lookup Wizard**.
   :::image type="content" source="media/select-lookup-wizard.png" alt-text="Select Lookup Wizard in Access":::
1. In the Lookup Wizard select the **I will type in the values that I want** option, and then select **Next**.
1. In the next dialog enter *2* for the number of columns and then select the field below **Col1**.
1. In **Col1** enter values for three rows by entering *1*, *2*, and *3*. In **Col2** enter values for three rows by entering *red*, *green*, and *blue*.
   :::image type="content" source="media/access-lookup-wizard2.png" alt-text="Create two columns with three rows of data each":::
1. 

### See also

[Migrate Microsoft Access data to Microsoft Dataverse](migrate-access-to-dataverse.md)
