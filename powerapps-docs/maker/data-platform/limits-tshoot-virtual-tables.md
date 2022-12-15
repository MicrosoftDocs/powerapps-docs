---
title: Limitations and troubleshooting virtual tables with Power Apps
description: Understand the limitations and how to troubleshoot virtual tables.
author: NHelgren
ms.author: nhelgren
ms.service: powerapps
ms.topic: conceptual
ms.date: 10/28/2022
ms.custom: template-how-to
---
# Known limitations and troubleshooting with virtual tables

This article describes the known limitations and troubleshooting tips when working with virtual tables in Microsoft Dataverse.

## Known limitations

The following is a list of known limitations for virtual tables created using the virtual connector provider.

## General

- The table or list used must include at least one string field to be used as the primary field, and one GUID field. Without these, the virtual table can't be created and an error will be generated during the table details retrieval stage.
- Dataverse can only create columns that include data types compatible with Dataverse. This includes the following data types:
   - String
   - Multiline text (memo)
   - Whole Number/Integer
   - Decimal
   - Float
   - Date/time
   - Yes/No (boolean)
   - Choices (multi-value select)
   - Hyperlink/Url
   - Lookup
- Data types not supported for virtual tables:
   - File and attachments
   - Image
- Maximum length of characters allowed for a text column in a virtual table is 4000 characters. If the source table has a maximum character limit greater than this value, any create/update operation exceeding the max character limit will result in a validation error, and the operation will fail.
- Virtual table queries are limited to return 250 records. If you've a 1:N or N custom multi-table (polymorphic) relationship with a virtual table, any query exceeding this limit will fail and provide an error. Use filtering in your query to reduce the record set as a workaround to this limitation.
- Audit functionality isn't available for Virtual Tables, this is because Dataverse can only perform and store audit data for locally stored data.
- Rollups and calculated fields can't be calculated for virtual tables. This is because rollups are a server side calculation in Dataverse, which requires the data to be stored locally.
- The **AAD User** virtual table provided by Microsoft only allows read access.
- Dataverse virtual tables can display values in fields that exceed the normal maximum values of Dataverse. This is because the values being presented aren't stored locally. For example, the Dataverse integer maximum value is 100,000,000,000, but it could retrieve and display 9,000,000,000,000 from SharePoint. However, if the user attempts to edit the number to a size larger than the max accepted size in Dataverse an error will be provided indicating the record can't be saved because it exceeds the maximum size.


## For each data source

The following are limitations for each data source.

# [SQL Server](#tab/sql)

- SQL data type bigint columns in the source table will be mapped as a decimal data type in Dataverse virtual tables. When platform support is available for bigint mapping to a whole number, previously created columns in the virtual table will need to be deleted, and new columns should be created.
- SQL Server tables without primary keys: Any non-string field can be selected as the primary key. The virtual table should be created successfully. RetrieveMultiple will work, the other operations will fail with the following error message (coming from SQL connector): "APIM request wasn't successful: BadRequest: No primary key exists in table".
- SQL views can be used to create a virtual table but they'll only provide read operations.
- SQL Server tables with a string primary key: The SQL string primary key will be the only option available for the virtual table primary key. The virtual table creation will succeed, but fail at runtime with this error: "String primary keys are supported only if they can be parsed as GUID". SQL Server string primary keys are supported only if the values can be parsed as GUID.
- SQL Server tables without non-primary key string fields: The primary field list will be empty and the user won't be able to create the virtual table. At least one non-primary key string field is required.
- For SQL Server Connector limitations, go to [SQL Server connector reference](/connectors/sql/).
- The following column types can't be included in a virtual table at this time:
   - Time
   - Datetime2
   - Image
   - Geometry
   - Geography
   - Cursor
   - HierarchyID
   - XML
   - RowVersion
   - Sqlvariant

# [Microsoft Excel Online (Business)](#tab/excel)

- Excel files must be stored on a OneDrive to participate in a Virtual Table connection.
- The Primary key can only be a column holding GUID values: Because the Excel table metadata shows all columns as string, our current design assumes that the primary key will always be a GUID represented as a string.
  > [!NOTE]
  > No validation is performed when the virtual entity is created, if a non-GUID column is selected, the entity will fail at runtime with this error: "String primary keys are supported only if they can be parsed as GUID".
- Support for PowerAppsId__ auto-generated column: The _PowerAppsId_ auto-generated column will be used if found (it will be the only option available for primary key). Providing a value for PowerAppsId is required at record creation even if the value will actually be overwritten by an automatically generated one. This doesn't happen if the primary key column isn't the `PowerAppsId` auto-generated column.
- Currently, the **Time** column type can't be included in a virtual table.
- Specific Excel Connector Limitations: [Excel Online (Business) connector reference](/connectors/excelonlinebusiness/).

# [Microsoft SharePoint](#tab/sharepoint)

- You currently can't select an **All** view for SharePoint columns on a virtual table. This is a known issue.
- SharePoint lists can use an integer field as the GUID as long as it contains unique values.
- The following column types can't be included in a virtual table at this time:
   - Person
   - Image
   - Managed metadata
   - Location: coordinates
   - Attachment
- SharePoint specific columns that will be shown in the virtual table:
   - **Compliance Asset ID** is an internal column from SharePoint for tracking purposes. It can be ignored.
   - **ID** is the external primary key from SharePoint. It's read-only and can be ignored.

---

## Troubleshooting

- There's only one (1) record in your virtual table even though you have more in your source table.<br />
  **Solution:** Check your source table and make sure it has primary key defined.
- I get an error "Resource not found for the segment 'msdyn_get_required_fields" when Power Apps (make.powerapps.com) is retrieving my table list or when I select **Finish** to create my table.<br />
  **Solution**: In some cases you might not have the most up to date solution for the virtual connector provider. To determine whether your virtual connector provider solution needs an update:
  1. Select **Solutions** on the left navigation pane.
  1. Select the **History** tab.
  1. **Search** for ConnectorProvider.
  1. View the information to see whether the solution needs to be updated.
  1. If the history indicates an update is needed, go to [the Microsoft commercial marketplace](https://appsource.microsoft.com/) search for **Virtual Connector Provider**, and then select **Get it now** to import the solution into your environment.
  1. Follow the steps to create the virtual table again.

- A message is displayed "This table already exists, you're recreating the table. Primary field and Schema name cannot be changed."<br />
  **Solution**: This table has previously been created. Continuing with the creation will re-create the table, this results in any table changes made at the data source to be updated in the virtual table (this includes addition or removal of fields). Even if you provided a custom name and primary field, these will be changed back to the values of the original field if you proceed.

- Error message: “primary_key_name cannot be empty”
  **Solution**: You have chosen a table or list that doesn't include a GUID value for the primary key. You'll need to add an additional GUID column in your source table in order to create a virtual table.

- I created an Excel virtual table but I can't see it in "Tables".<br />
  **Solution**: Since the virtual table creation is asynchronous, you can check the status of the process in **System Jobs**. Look for system jobs with a Name starting `Microsoft.Wrm.DataProvider.Connector.Plugins.ConnectorGenerateVEPlugin` and a **Regarding** column's value equal to the name of the new virtual table. If status is still In Progress, just wait for the job to complete. If there's an error, you can get details by clicking the system, job name hyperlink. In this example, table creation is still pending:

   :::image type="content" source="media/ve-table-creation-pending.png" alt-text="table creation pending":::

   Here, table creation failed due to 429 "Too Many Requests" error:

   :::image type="content" source="media/ve-table-creation-failed-429-error.png" alt-text="table creation failed due to 429 error":::

- Table creation's system job succeeded but I'm getting runtime errors related to invalid or missing columns<br />
  **Solution**: If a failure occurs while creating a table's field, the table creation process won't fail and try to continue with the remaining fields. This is because we don't want to block the virtual table creation when some column types are unsupported. To get details on the error, you can enable logging in **Administration**> **System Settings** > **Customizations** > **Enable logging to plug-in trace log**, then delete the virtual table and try to create it again.

## Next steps

[Create virtual tables using the virtual connector provider (preview)](create-virtual-tables-using-connectors.md)

[Setting up a virtual table relationship](setup-virtual-table-relationships.md)
