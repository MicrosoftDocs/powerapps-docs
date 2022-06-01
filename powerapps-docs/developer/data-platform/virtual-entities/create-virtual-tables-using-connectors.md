---
title: "Create virtual tables using virtual connectors (Microsoft Dataverse) | Microsoft Docs"
description: "Learn how to create virtual tables using virtual connectors in Microsoft Dataverse."
ms.date: 06/01/2022
ms.reviewer: "jdaly"
ms.topic: article
author: "NHelgren" # GitHub ID
ms.author: "nhelgren"
manager: "sunilg"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors: 
  - JimDaly
  - phecke 
---
# Create virtual tables using the virtual connector provider (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../../includes/cc-beta-prerelease-disclaimer.md)]

Virtual tables enable integrating data from external data sources by seamlessly representing that data as tables in Microsoft Dataverse, without data replication. Solutions built on Microsoft Power Platform can leverage virtual tables as if they were native Dataverse tables. More information: [Get started with virtual tables](get-started-ve.md).

In this public preview release, we are introducing the virtual connector provider that supports creating virtual tables using the following connectors:
- [SQL Server](/connectors/sql/) 
- Microsoft Excel Online ([Business](/connectors/excelonlinebusiness/))
- [Microsoft SharePoint](/connectors/sharepointonline/)

We will continue to expand and support other tabular connectors as part of this provider in subsequent releases.

To learn more about supported actions and limitations, see:
- [Connector reference for the SQL Server connector](/connectors/sql/)
- [Connector reference for the Microsoft Excel Online Business connector](/connectors/excelonlinebusiness/)
- [Connector reference for the SharePoint Online connector](/connectors/sharepointonline).


## Overview

Virtual Tables include the following components:

:::image type="content" source="media/ve-components.png" alt-text="Virtual table components":::

- Data Source – the location where the external data is stored
- Data Provider – defines the behavior of the virtual table
- Connection – this sets up the ability to connect to the data source/ Authentication
- Connection Reference – this provides a way for Dataverse to use the connection to the data source

Virtual connector provider streamlines the creation experience by automating some of the creation process for you. When you establish a remote connection to an external source using a connector data source, the virtual connector provider automatically generates an Entity Catalog with a list of all the available tables by retrieving table definitions (metadata) from the external data source.

The **Entity Catalog** does not persist any information and always represents the external data source's current state. You can select tables from the **Entity Catalog** to create virtual tables. If you're working with multiple external data sources, an **Entity Catalog** is generated for each external source.

The underlying data source is key for allowing the provider to establish an authenticated remote connection to the external data. It uses a connection reference that stores pertinent details regarding the external source. The information stored in the connection reference is specific to the connector type and the connection it refers to. 

:::image type="content" source="../media/ve-connector-provider-overview.png" alt-text="Virtual connectors provider overview":::

For example, setting up the **SQL Server** connector needs server name, database name, the authentication method, username, password, and (optionally) gateway connection details. Each external data source needs a new connection reference defined to create an instance of its **Entity Catalog**.

The connector permissions enforce the ability for organizational users to access and operate on the virtual table. The connection can be shared with one user or can be shared with entire organization. This allows users to access and operate on virtual tables using a shared connection.

Application lifecycle management (ALM) is supported for virtual tables created using the virtual connector provider. Virtual tables should be part of the managed solution along with the connection reference to distribute the solution. The solution can have other components, such as a model-driven app that uses virtual tables. 

More information about Application lifecycle management (ALM) and solutions:

- [Application lifecycle management (ALM) in Microsoft Power Platform](/power-platform/alm/)
- [Solutions overview](/powerapps/maker/data-platform/solutions-overview)

## Create a virtual table with the virtual connector provider

Creating a virtual table with the virtual connector provider includes the following steps:

1. [Download and install the Virtual connector](#download-and-install-the-virtual-connector)
1. [Create the connection](#create-the-connection)
1. [Create the Connection Reference](#create-the-connection-reference)
1. [Create the Data Source](#create-the-data-source)
1. [Entity Catalog](#entity-catalog)
1. [Setting up virtual table relationship](#setting-up-virtual-table-relationship)


### Download and install the Virtual connector

1. Go to [Microsoft AppSource](https://appsource.microsoft.com/) and search for `Virtual Connector` or select the link to download the provider: [Virtual connectors in Dataverse](https://appsource.microsoft.com/product/dynamics-365/mscrm.connector_provider?tab=Overview)

   > [!div class="mx-imgBorder"]
   > ![Virtual connectors in Dataverse](../media/ve-virtual-connectors-provider.png "Virtual connectors in Dataverse")

1. Select **Get it now**. In the sign-in dialog, enter work or school account email. Agree the terms and conditions and then select **Continue**. The Power Platform Admin Center will open automatically.

1. Select the environment where you want to install the solution. Agree the terms and conditions and then select **Install**. Once the installation is complete, you will see the **Virtual connectors in Dataverse** app installed under **Environments -> [your environment name] -> Dynamics 365 apps**.

   > [!div class="mx-imgBorder"]
   > ![Select environment to install connector](../media/ve-select-the-environment.png "Select environment to install connector")

1. You should also see the **Virtual Connector Provider** solution and other solutions enabled in the Power Apps environment.

    > [!div class="mx-imgBorder"]
    > ![Virtual connector provider solution](../media/ve-select-virtual-connectors-solution.png "Virtual connector provider solution")

### Create the connection

# [SQL Server](#tab/sql)
Watch a 4 minute video showing how to create a virtual table with the SQL virtual connector provider. 

> [!VIDEO https://www.microsoft.com/videoplayer/embed/RE4XLkU]

# [Microsoft Excel Online (Business)](#tab/excel)
Watch a 4 minute video showing how to create a virtual table with the Excel virtual connector provider. 

> [!VIDEO https://www.microsoft.com/videoplayer/embed/RE4YcGf]

# [Microsoft SharePoint](#tab/sharepoint)
Watch a 4 minute video showing how to create a virtual table with the SharePoint virtual connector provider. 

> [!VIDEO https://www.microsoft.com/videoplayer/embed/RE4YcIk]

---

1. Go to [Power Apps](https://make.powerapps.com), select the environment in which you would like to set up the virtual table. 
1. In the left navigation pane, select **Data** > **Connections** then select **New connection**. 

   :::image type="content" source="media/ve-create-connection.png" alt-text="Create new connection in power apps":::

1. Select one of the following Virtual Connectors from the list of connections. 
   - SQL Server
   - Microsoft Excel Online (Business)
   - Microsoft SharePoint  
1. You will be asked to provide additional details to connect to the data source. 

# [SQL Server](#tab/sql)

- Select SQL Server Authentication as Authentication Type. 
- Enter SQL server name, SQL database name, the credentials needed to connect.

   :::image type="content" source="media/ve-sql-connection-server.png" alt-text="Connect to SQL":::

- If you are using an on-premises SQL server also enter the Gateway information and then select **Create**.

   :::image type="content" source="media/ve-sql-connection-on-prem.png" alt-text="Connect to SQL on-premises with gateway information":::

# [Microsoft Excel Online (Business)](#tab/excel)

Click **Create**, your current signed-in credentials will be used.

:::image type="content" source="media/ve-excel-connection.png" alt-text="Connect to Excel":::

# [Microsoft SharePoint](#tab/sharepoint)

- Select to Connect Directly (Cloud) or Connect Using on Premises Gateway

   :::image type="content" source="media/ve-sharepoint-connect.png" alt-text="Connect to Sharepoint":::

- For Direct connection, Sign in to SharePoint

   :::image type="content" source="media/ve-sharepoint-direct-connect.png" alt-text="Use Direct connection":::

- For On Premises, Select your authentication type, provide your credentials, choose a Gateway and click **Create**.

   :::image type="content" source="media/ve-sharepoint-connect-on-premises.png" alt-text="Connect to SharePoint with a gateway":::

---
  
### Create the Connection Reference

1. Go to **Solutions**.
1. Select the **Default Solution** or any other existing solution you have in your environment to create the virtual table.
1. Select **New** and then select **Connection Reference (preview).**
1. Enter **Display name**, select the connection you just created for the **Connectors** option and then select the data connection that you have created.

   :::image type="content" source="../media/ve-new-connection-reference.png" alt-text="New connection reference":::

### Create the Data Source

Now create the Virtual Table data source in Dataverse.

1. Select the **Gear icon -> Advanced Settings**

   :::image type="content" source="media/ve-power-apps-advanced-settings.png" alt-text="Advanced Settings command":::

1. In the top navigation bar select **Settings** and then **Administration**

   :::image type="content" source="media/ve-advanced-settings-system-administration.png" alt-text="Navigate to system administration":::

1. Select **Virtual Entity Data Source**

   :::image type="content" source="media/ve-virtual-entity-data-sources-settings.png" alt-text="Virtual entity data sources settings":::

1. Select **New**. In the pop-up dialog, select the Virtual Connector Data Provider.

   :::image type="content" source="media/ve-create-new-data-source.png" alt-text="New Data source":::

   :::image type="content" source="media/ve-select-data-provider.png" alt-text="Select Virtual Connector Data Provider":::

1. Name your **Data Source** and select the **Connection Reference** you just created in the drop down list.

   :::image type="content" source="media/ve-name-data-source.png" alt-text="Name data source and select connection reference":::

   - SQL Server
      - Leave the Data Source field empty
   - Microsoft Excel Online (Business)
      - Paste in the file name including extension. Remember the file must be in the OneDrive that was used for the Connection setup. (Ex: SampleData.xlsx)      
   - Microsoft SharePoint
      - Paste the URL to your SharePoint site in the Data Source field (ex: https://contosoenvname.sharepoint.com/sites/sitename)
      
1. Click **Save**

### Entity Catalog

With the connection reference and the virtual table data source setup, an **Entity Catalog** is automatically generated. The **Entity Catalog** is specific to the data source and will list all the tables that are in the respective data source.

:::image type="content" source="media/ve-entity-catalog.png" alt-text="Entity Catalog":::

> [!NOTE] 
> - The creation of the entity catalog is an asynchronous process. Depending on your environment, this may take a few minutes. 
> - The tables you see in the Entity Catalog are not virtual tables in themselves. You need to select from this list of tables representing the external data to create virtual table in Dataverse.
 
#### View the Entity Catalog
  
- Select Data -> Tables and select the entity catalog that was created. 
- Select **Advanced Find** and use the Look for: column. The catalog will include a prefix Entity Catalog for followed by the connection reference (example: Entity Catalog for Adventure Works DB). Find the Entity Catalog for your respective data connection and select the Results button to see all the external data source tables. 

  :::image type="content" source="../media/ve-advance-find-table-catalog.png" alt-text="Advanced find table catalog":::

  >[!Note]
  > Bulk creation of virtual tables is not supported currently. Even though the Entity Catalog allows you to select multiple tables, you will have to select one table at a time to create virtual tables.

1.   To create a virtual table, a model driven app must be built for the entity catalog. Select the entity catalog table.

2.   Click Create an app in the top navigation.

:::image type="content" source="media/entity-catalog-table-selected-table-view.jpg" alt-text="Entity catalog with a table selected, table view":::

3.   Name the app and click Create

:::image type="content" source="media/Create-an-app-screen.jpg" alt-text="Create a Model Driven app screen":::

The app will automatically be generated using the entity catalog table. 

4.   Once the app is completed, you can click Publish to complete the app and use it later, or you can click Play to create your virtual table now without publishing the app. 

:::image type="content" source="media/completed-model-driven-app.jpg" alt-text="Completed model driven app":::

All eligible data sets from your data source will be provided in the app view.
-   SQL: All tables in the database that are eligible are shown
-   SharePoint: All lists in the site are shown
-   Excel: All tables in the Excel file are shown

5.   Select the data set you wish to use from the entity catalog, and click Edit in the navigation bar.

:::image type="content" source="media/model-driven-app-entity-catalog-view.jpg" alt-text="Model Driven app Entity Catalog view with a data set selected":::

Wait for the form to fully load before editing. When loaded the form will look like this:

:::image type="content" source="media/edit-form-for-entity-catalog-model-driven-app.jpg" alt-text="Entity Catalog edit form all fields blank":::

6.   In the provided form set the Create or Refresh Entity column to Yes.

7.   Select the Primary Key and Primary Field of the virtual entity by using the dropdowns to find the columns you wish to use.

:::image type="content" source="media/edit-form-entity-catalog-fields-completed.jpg" alt-text="Entity Catalog edit form all fields completed":::

8.   Save the record to create the virtual table. 

> [!Note] 
> After the save completes, the form will "reset" with all fields shown as blank, this is normal. 

Return to the Maker portal's home page and select Data, your virtual table is now created with a "Custom Entity" prefix. It may take a few moments for the creation to complete.
:::image type="content" source="media/maker-table-view-virtual-table.png" alt-text="Maker portal with virtual table selected":::

> [!IMPORTANT] 
> - Virtual tables no longer require an associated GUID as a primary key with the virtual connector provider. 
> - The provider automatically maps the primary key associated with the external data source when creating the virtual table. All CRUD operations can be performed on the generated virtual table. 
> - All columns in the external data are automatically mapped to Dataverse types that are support by the connector. You can review the virtual table details and make changes by navigating to **Settings -> Customization – Entities** view.
> - Virtual Tables require there to be at least one string field to use as the Primary Name column.

Once you have created a virtual table, you can work with it much the same way as any other table. You can start defining the relationships with other tables, in the environment and use them in your Power Apps and Power Automate flows.

### Setting up virtual table relationship

Virtual tables are  enabled for relationships. You can set up 1:N, N:1, and N:N relationships. Relationships can be established between:
- Local tables in Dataverse and Virtual Tables
- Virtual tables and other virtual tables from the same provider (Example: SQL->SQL)

For instance, you cannot set up a relationship between a virtual table created using the OData virtual table provider and a virtual table created using the Virtual Connector provider.

#### Defining relationships in virtual tables

Virtual tables created using the virtual connector provider automatically creates all the columns that are represented in the external source table. This will also include columns on which relationships are defined. However, the relationship definition will not be automatically created. You will have to define this relationship in Dataverse manually.

The following example creates an N:1 relationship between a virtual table (**Service Request**) and a native table (**Account**). The column used to set up the relationship is **AccountId**. This column is the primary key in the Account table and is a foreign key in the Service Request table.

A representation of the **Service Request** virtual table is shown below. You will notice that the **AccountId** column, which is the column used for relationship in the external source, is of type **Multiple Line of Text**. You need to have this column represented as a **Lookup** type to create a relationship.

:::image type="content" source="../media/ve-create-columns.png" alt-text="Create columns in virtual table":::

1. Go to **Advanced settings -> Settings -> Customization** and choose **Customize the System**.
1. In the left navigation pane, expand the **Entities** view and browse to the Service Request virtual table definition.
1. Select the **Fields** view and select the **AccountId** column and select **Delete**.
1. Choose **Delete** to confirm the deletion of this column.
1. To create the relationship, select the **N:1 Relationship** within the Service Request table.
1. Select **New Many-to-1 Relationship**.
1. Enter the following details to create the relationship between the Service Request virtual table and the Account table.
   1. In the **Relationship Definition** section – set the **Primary Entity** column value to **Account**.
   1. Optionally, if you want to edit the name of the relationship, you can do so in the **Name** column.
   1. In the **Lookup Field** section – set the **Display Name** to **Account.**
   1. The **Name** column will automatically populate with the lookup column name.
   1. Set the **External Name** value to **AccountId** (matching the column name in your source table).
   
      :::image type="content" source="../media/ve-create-relationship.png" alt-text="Create relationship":::
   
1. Refer to the columns for the **Service Request** virtual table, and you will notice that the **AccountID** column is not a **Lookup** type. This column can now
be added to forms and views to see all associated accounts for each of the service request record.

   :::image type="content" source="../media/ve-custom-table-columns.png" alt-text="Custom table columns":::

1. With the relationship established you can now create a new service request and pick accounts to associate them to.

   :::image type="content" source="../media/ve-new-custom-table.png" alt-text="New custom table":::

  > [!NOTE]
  > You will have to edit the forms and views for this table to include the lookup column and other required columns prior to operation on the virtual table.

#### Tips

- Primary Key column should be included in create form if you did not set up the column to increment during the design of the underlying source table automatically. You will have to enter a valid value in the primary key column for an insert operation to succeed.
- If **Entity Catalog** creation takes a long time, you can check the job completion status by navigating to **Settings -> System Jobs** view.


## Known limitations

The following is a list of known limitations for virtual tables created using the virtual connector provider.

### General

- Maximum length of characters allowed for a text column in a virtual table is 4000 characters. If the source table has a maximum character limit greater than this value, any create/update operation exceeding the max character limit will result in a validation error, and the operation will fail.
- Virtual table queries are limited to return 250 records. If you have a 1:N or N:N relationship with a virtual table, any query exceeding this limit will fail and provide an error. Use filtering in your query to reduce the record set as a workaround to this limitation.
- Audit functionality is not available for Virtual Tables, this is because Dataverse can only perform and store audit data for locally stored data.
- Rollups cannot be calculated for Virtual tables, this is because Rollups are a server side calculation in Dataverse which requires the data to be stored locally.

### For each data source

The following are limitations for each data source.

# [SQL Server](#tab/sql)

- SQL data type bigint columns in the source table will be mapped as a decimal data type in Dataverse virtual tables. When platform support is available for bigint mapping to a whole number, previously created columns in the virtual table will need to be deleted, and new columns should be created. 
- SQL Server tables without primary keys: Any non-string field can be selected as the primary key. The virtual table should be created successfully. RetrieveMultiple will work, the other operations will fail with the following error message (coming from SQL connector): "APIM request was not successful : BadRequest : No primary key exists in table".
- SQL Server tables with a string primary key: The SQL string primary key will be the only option available for the virtual table primary key. The virtual table creation will succeed, but fail at runtime with this error: "String primary keys are supported only if they can be parsed as GUID". SQL Server string primary keys are supported only if the values can be parsed as GUID.
- SQL Server tables without non-primary key string fields: The primary field list will be empty and the user will not be able to create the virtual table. At least one non-primary key string field is required.
- SQL Server Connector Limitations: see [SQL Server connector reference](/connectors/sql/). 

# [Microsoft Excel Online (Business)](#tab/excel)

- Excel files must be stored on a OneDrive to participate in a Virtual Table connection.
- The Primary key can only be a column holding GUID values: Because the Excel table metadata shows all columns as string, our current design assumes that the primary key will always be a GUID represented as a string.
  > [!NOTE]
  > No validation is performed when the virtual entity is created, if a non-GUID column is selected, the entity will fail at runtime with this error: "String primary keys are supported only if they can be parsed as GUID".
- Support for PowerAppsId__ auto-generated column: The _PowerAppsId_ auto-generated column will be used if found (it will be the only option available for Primary key). Providing a value for PowerAppsId is required at record creation even if the value will actually be overwritten by an automatically generated one. This doesn't happen if the primary key column is not the PowerAppsId auto-generated column.
- Specific Excel Connector Limitations: [Excel Online (Business) connector reference](/connectors/excelonlinebusiness/).

# [Microsoft SharePoint](#tab/sharepoint)
You currently cannot select an "All" view for SharePoint columns on a Virtual Table. This is a known bug and is being fixed.

---

## Troubleshooting

- You are seeing only one (1) record in your virtual table even though you have more in your source table.<br />
  **Solution:** Check your source table and make sure it has primary key defined.
  
- I created a virtual table but I can't see it in "Tables".<br />
  **Solution**: Since the virtual table creation is asynchronous, you can check the status of the process in "System Jobs". Look for system jobs with a Name starting Microsoft.Wrm.DataProvider.Connector.Plugins.ConnectorGenerateVEPlugin and a "Regarding" column's value equal to the name of the new virtual table. If status is still In Progress, just wait for the job to complete. If there is an error, you can get details by clicking the system, job name hyperlink. In this example, table creation is still pending:

   :::image type="content" source="media/ve-table-creation-pending.png" alt-text="table creation pending":::

   Here, table creation failed due to 429 "Too Many Requests" error:
   
   :::image type="content" source="media/ve-table-creation-failed-429-error.png" alt-text="table creation failed due to 429 error":::

- Table creation's system job succeeded but I am getting runtime errors related to invalid or missing columns<br />
  **Solution**: If a failure occurs while creating a table's field, the table creation process will not fail and try to continue with the remaining fields. This is because we don't want to block the virtual table creation when some column types are unsupported. To get details on the error, you can enable logging in **Administration**> **System Settings** > **Customizations** > **Enable logging to plug-in trace log**, then delete the virtual table and try to create it again.

### See also

[Get started with virtual tables (entities)](get-started-ve.md)
