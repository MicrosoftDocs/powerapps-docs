---
title: Limitations and troubleshooting virtual tables with Power Apps
description: Understand the limitations and how to troubleshoot virtual tables.
author: NHelgren
ms.author: nhelgren
ms.service: powerapps
ms.subservice: dataverse-maker
ms.topic: troubleshooting-general
ms.date: 04/10/2026
ms.custom: template-how-to
contributors: 
  - psimolin
  - nravindra-msft
---
# Known limitations and troubleshooting with virtual tables

This article describes the known limitations and troubleshooting tips when working with virtual tables in Microsoft Dataverse.

The following list describes known limitations for virtual tables created by using the virtual connector provider.

## General limitations

- The table or list you use must include at least one string field to use as the primary field, and one GUID field. Without these string fields, you can't create the virtual table and an error occurs during the table details retrieval stage.
   - SharePoint uses the hidden numeric ID field present in all lists.
   - SQL can use a GUID or integer field.
   - Excel must have a GUID field.
- Dataverse can only create columns that include data types compatible with Dataverse. This limitation includes the following data types:
   - String
   - Multiline text (memo)
   - Whole Number/Integer
   - Decimal
   - Float
   - Date/time
   - Yes/No (boolean)
   - Choices (multi-value select)
   - Hyperlink/Url
- Dataverse doesn't support the following data types for virtual tables:
   - File and attachments
   - Image
- Maximum length of characters allowed for a text column in a virtual table is 4,000 characters. If the source table has a maximum character limit greater than this value, any create or update operation exceeding the max character limit results in a validation error, and the operation fails.
- Virtual table queries are limited to returning 1,000 records. If you have a 1:N or N custom multitable (polymorphic) relationship with a virtual table, any query that exceeds this limit fails and provides an error. Use filtering in your query to reduce the record set as a workaround to this limitation.
- Audit functionality isn't available for virtual tables because Dataverse can only perform and store audit data for locally stored data.
- Rollups and calculated fields can't be calculated for virtual tables. This limitation exists because rollups are a server side calculation in Dataverse, which requires the data to be stored locally.
- Formula columns can't use virtual tables.
- The **Microsoft Entra ID** virtual table provided by Microsoft only allows read access.
- Dataverse virtual tables can display values in fields that exceed the normal maximum values of Dataverse. This behavior occurs because the values being presented aren't stored locally. For example, the Dataverse integer maximum value is 100,000,000,000, but it could retrieve and display 9,000,000,000,000 from SharePoint. However, if the user attempts to edit the number to a size larger than the max accepted size in Dataverse, an error is provided indicating the record can't be saved because it exceeds the maximum size.
- Import and export functionality of table data isn't supported for virtual tables.
- Queries against virtual tables that use negative filter operators, such as Does Not Equal or Does Not Contain, might result in incorrect paging behavior beyond the first page. There's currently no supported workaround. Avoid using negative filters.

## Limitations for each data source

The following limitations apply to each data source.

# [SQL Server](#tab/sql)

- For functionality, SQL virtual tables use a GUID or an integer field as the primary key. 
- SQL Server tables without primary keys: You can select any nonstring field as the primary key. You can create the virtual table successfully. `RetrieveMultiple` works, but the other operations fail with the following error message (coming from SQL connector): "APIM request wasn't successful: BadRequest: No primary key exists in table." For functionality, you must use a GUID or integer field as the primary key.
- SQL Server tables that use a string primary key: The SQL string primary key is the only option available for the virtual table primary key. SQL Server string primary keys are supported only if the values can be parsed as GUID. If the values can't be parsed as GUID, the virtual table creation succeeds, but fails at runtime with the following errors:
   - Power Apps (make.powerapps.com): "We weren't able to open your table. Try reloading or reopening."
   - Network trace: "String primary keys are supported only if they can be parsed as GUID."
- SQL Server tables without nonprimary key string fields for use as the primary name: If the SQL table doesn't have a string field available to use as the primary name, the configuration step displays the following error: "The table doesn't have a primary field."
- You can use SQL views to create a virtual table but they only provide read operations.
- For SQL Server connector limitations, go to [SQL Server connector reference](/connectors/sql/).
- SQL data type, *bigint columns*, in the source table are mapped as a decimal data type in Dataverse virtual tables. When platform support is available for bigint mapping to a whole number, you need to delete previously created columns in the virtual table and create new columns.
- You can't include the following column types in a virtual table at this time:
   - Time
   - Datetime2
   - Image
   - Geometry
   - Geography
   - RowVersion
   - Choice
 - The following column types are included in a virtual table but are only shown as text fields:
   - HierarchyID
   - XML
   - Sqlvariant

# [Microsoft Excel Online (Business)](#tab/excel)
- Excel is currently not supported in the table driven virtual table experience.
- To participate in a virtual table connection, you must store Excel files on a OneDrive. 
- Include the primary key column in the create form if you don't set up the column to increment during the design of the underlying source table automatically. You must enter a valid value in the primary key column for an insert operation to succeed. 
- If entity catalog creation takes a long time, you can check the job completion status by going to **Settings** > **Advanced settings** > **Settings** > **System Jobs**.
- The primary key can only be a column holding GUID values: Because the Excel table metadata shows all columns as string, the current design assumes that the primary key is always a GUID represented as a string. 
   > [!NOTE]
   > No validation is performed when the virtual table is created. If you select a non-GUID column, the table fails at runtime with this error: "String primary keys are supported only if they can be parsed as GUID". 
- Support for `PowerAppsId__` autogenerated column: The `PowerAppsId` autogenerated column is used if found (it's the only option available for primary key). Providing a value for `PowerAppsId` is required at record creation even if the value is actually overwritten by an automatically generated one. This requirement doesn't happen if the primary key column isn't the `PowerAppsId` autogenerated column. 
- You can't include the following column types in a virtual table at this time: 
   - Time (these are created as date and time fields).
- For specific Excel connector limitations, go to: [Excel Online (Business) connector reference](/connectors/excelonlinebusiness/).

# [Microsoft SharePoint](#tab/sharepoint)

- You currently can't select an **All** view for SharePoint columns on a virtual table. This limitation is a known issue.
- You can't include the following column types in a virtual table at this time:
   - Person
   - Image
   - Managed metadata
   - Location: coordinates
   - Attachment
- The virtual table shows the following SharePoint specific columns:
   - **Compliance Asset ID** is an internal column from SharePoint for tracking purposes. You can ignore it.
   - **ID** is the external primary key from SharePoint. It's read-only and you can ignore it.

# [Salesforce (preview)](#tab/salesforce)

- For Salesforce connector limitations, go to [Salesforce connector reference](/connectors/salesforce/).
- You can't unlock fields that reference other Salesforce objects.

# [Oracle (preview)](#tab/oracle)

- For Oracle connector limitations, go to [Oracle connector reference](/connectors/oracle/).
- You need to define a primary key for the Oracle table.
- The Oracle table needs to have at least one string type field besides the primary key.

---

## Troubleshooting

- There's only one (1) record in your virtual table even though you have more in your source table.<br />
  **Solution:** Check your source table and make sure it has a primary key defined.
  
- You get one of the following errors when Power Apps (make.powerapps.com) is retrieving a table list or when you select **Finish** to create a table:
   - "Resource not found for the segment `msdyn_get_required_fields`"
   - "Error calling... please verify that connection... exists in environment"
   - "Sequence matches no element for `msdyn_get_required_fields`"<br />
  **Solution**: In some cases you might not have the most up to date solution for the virtual connector provider. To determine whether your virtual connector provider solution needs an update:

  1. Select **Solutions** on the left navigation pane. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]
  1. Select the **History** tab.
  1. **Search** for `ConnectorProvider`.
  1. View the information to see whether the solution needs to be updated.
  1. If the history indicates an update is needed, go to [the Microsoft commercial marketplace](https://marketplace.microsoft.com/) search for **Virtual Connector Provider**, and then select **Get it now** to import the solution into your environment.
  1. Follow the steps to create the virtual table again.

- A message is displayed "Connection 'xyz' not found in current environment." when retrieving the list of connections.<br />
   **Solution**: This occurs when there are a large number of connections in the user's Dataverse environment. This is fixed with version 1,029 of the Connector Provider solution.
  To determine whether your virtual connector provider solution needs an update:

  1. Select **Solutions** on the left navigation pane. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]
  1. Select the **History** tab.
  1. **Search** for `ConnectorProvider`.
  1. View the information to see whether the solution needs to be updated.
  1. If the history indicates an update is needed, go to [the Microsoft commercial marketplace](https://marketplace.microsoft.com/) search for **Virtual Connector Provider**, and then select **Get it now** to import the solution into your environment.
  1. Follow the steps to create the virtual table again.

- You get notified that a timeout occurred during the virtual table creation. <br />
   **Solution**: This can occur when other existing jobs cause the virtual table creation to be delayed. Wait for a few minutes and try again.

- You get notified that "An unexpected error occurred" <br />
  **Solution**: This occurs when the virtual table data source was created with invalid values. To resolve this, you need to locate the virtual table data source that is causing the error, delete it, and then re-create the virtual table.

   1. Select **Settings** (gear icon) > **Advanced settings** from [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).
   2. In the top menu, select **Settings**.
   3. Go to **Solutions**. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]
   4. Go to the solution that includes your virtual table (if you weren't using a solution then go to Common Data Services Default Solution).
   5. In the left hand panel, select **Virtual table data sources**.
   6. Double-click each data source (they all start with `VCP_DS_..."`), when you locate the one with the error, delete that data source.
   7. Re-create your virtual table.

- A message is displayed "This table already exists, you're recreating the table. Primary field and Schema name can't be changed."<br />
  **Solution**: This table has previously been created. Continuing with the creation re-creates the table, this results in any table changes made at the data source to be updated in the virtual table (this includes addition or removal of fields). The custom name and primary field values won't be editable.

- Error message: "primary_key_name can't be empty"<br />
  **Solution**: You have chosen a table or list that doesn't include a GUID value for the primary key. You need to add an additional GUID column in your source table in order to create a virtual table.

- You created an Excel virtual table but don't see it in the **Tables** area in Power Apps.<br />
  **Solution**: Since the virtual table creation is asynchronous, you can check the status of the process in **System Jobs**. Look for system jobs with a Name starting `Microsoft.Wrm.DataProvider.Connector.Plugins.ConnectorGenerateVEPlugin` and a **Regarding** column's value equal to the name of the new virtual table. If status is still **In Progress**, just wait for the job to complete. If there's an error, you can get details by selecting the system, job name hyperlink. In this example, table creation is still pending:

   :::image type="content" source="media/ve-table-creation-pending.png" alt-text="table creation pending":::

   Here, table creation failed due to 429 "Too Many Requests" error:

   :::image type="content" source="media/ve-table-creation-failed-429-error.png" alt-text="table creation failed due to 429 error":::

- Table creation's system job succeeded but you receive runtime errors related to invalid or missing columns.<br />
  **Solution**: If a failure occurs while you create a table field, the table creation process doesn't fail and try to continue with the remaining fields. This is because the system doesn't want to block the virtual table creation when some column types are unsupported. To get details on the error, enable logging in **Administration**> **System Settings** > **Customizations** > **Enable logging to plug-in trace log**, then delete the virtual table and try to create it again.

- If you deleted the connection connected to virtual table and recreated it, the Virtual Connector Provider app loses permission to access the new connection, preventing data retrieval.<br />
**Solution**: Manually share the recreated connection with the 'Virtual Connector Provider' app using the connection's share feature to restore access.

- When a custom data provider for a virtual table is updated to support new operations (e.g., create, update, delete), the platform does not automatically add corresponding permissions to the existing virtual table entity.<br />
**Solution**: To enable new permissions, the user must recreate the virtual table entity after updating the data provider.
  
## Next steps

[Create virtual tables using the virtual connector provider (preview)](create-virtual-tables-using-connectors.md)

[Setting up a virtual table relationship](setup-virtual-table-relationships.md)
