---
title: "Create virtual tables using virtual connectors (Microsoft Dataverse) | Microsoft Docs"
description: "Learn how to create virtual tables using virtual connectors in Microsoft Dataverse."
ms.date: 03/28/2022
ms.reviewer: "jdaly"
ms.topic: sample
author: "NHelgren" # GitHub ID
ms.author: "jdaly"
manager: "kvivek"
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
## In this article
<<<<These need to be doc links>>>>
1.	Overview
2.	Getting started with virtual connector provider
3.	Create a virtual table using a virtual connector
4.	Known limitations
5.	Troubleshooting


Virtual tables enable integrating data from external data sources by seamlessly representing that data as tables in Microsoft Dataverse, without data replication. Solutions built on Microsoft Power Platform can leverage virtual tables as if they were native Dataverse tables. More information: [Get started with virtual tables](get-started-ve.md).



In this public preview release, we are introducing the virtual connector provider that supports creating virtual tables using the [SQL Server connector](/connectors/sql). We will continue to expand and support other tabular connectors as part of this provider in subsequent releases. 

In this public preview release, we are introducing the virtual connector provider that supports creating virtual tables using the following connectors:
> - [SQL Server](/connectors/sql) 
> - Microsoft Excel Online ([Business](connectors/excelonlinebusiness))
> - [Microsoft SharePoint](connectors/sharepointonline)
We will continue to expand and support other tabular connectors as part of this provider in subsequent releases.


To learn more about supported actions and limitations, see [connector reference for the SQL Server connector](/connectors/sql/), [connector reference for the Microsoft Excel Online Business connector](connectors/excelonlinebusiness/), [connector reference for the SharePoint Online connector](connectors/sharepointonline).


## Overview

Virtual Tables include the following components:
<<<<Insert Image here>>>>
- Data Source – the location where the external data is stored
- Data Provider – defines the behavior of the virtual table
- Connection – this sets up the ability to connect to the data source/ Authentication
- Connection Reference – this provides a way for Dataverse to use the connection to the data source

Virtual connector provider streamlines the creation experience by automating some of the creation process for you. When you establish a remote connection to an external source using a connector data source, the virtual connector provider automatically generates an Entity Catalog with a list of all the available tables by retrieving table definitions (metadata) from the external data source.

The **Entity Catalog** does not persist any information and always represents the external data source’s current state. You can select tables from the **Entity Catalog** to create virtual tables. If you're working with multiple external data sources, an **Entity Catalog** is generated for each external source.

The underlying data source is key for allowing the provider to establish an authenticated remote connection to the external data. It uses a connection reference that stores pertinent details regarding the external source. The information stored in the connection reference is specific to the connector type and the connection it refers to. 

> [!div class="mx-imgBorder"]
> ![Virtual connectors provider overview](../media/ve-connector-provider-overview.png "Virtual connectors provider overview")

For example, setting up the **SQL Server** connector needs server name, database name, the authentication method, username, password, and (optionally) gateway connection details. Each external data source needs a new connection reference defined to create an instance of its **Entity Catalog**.

The connector permissions enforce the ability for organizational users to access and operate on the virtual table. The connection can be shared with one user or can be shared with entire organization. This allows users to access and operate on virtual tables using a shared connection.

Application lifecycle management (ALM) is supported for virtual tables created using the virtual connector provider. Virtual tables should be part of the managed solution along with the connection reference to distribute the solution. The solution can have other components, such as a model-driven app that uses virtual tables. 

More information about Application lifecycle management (ALM) and solutions:

- [Application lifecycle management (ALM) in Microsoft Power Platform](/power-platform/alm/)

- [Solutions overview](/powerapps/maker/data-platform/solutions-overview)

## Getting started with virtual connector provider

### Create a virtual table using SQL Server connector

To create a virtual table using **SQL Server** connector: 

1. Go to [Microsoft AppSource](https://appsource.microsoft.com/) and search for `Virtual Connector` or select the link to download the provider: [Virtual connectors in Dataverse](https://appsource.microsoft.com/product/dynamics-365/mscrm.connector_provider?tab=Overview)

   > [!div class="mx-imgBorder"]
   > ![Virtual connectors in Dataverse](../media/ve-virtual-connectors-provider.png "Virtual connectors in Dataverse")

2. Select **Get it now**. In the sign-in dialog, enter work or school account email. Agree the terms and conditions and then select **Continue**. The Power Platform Admin Center will open automatically.

3. Select the environment where you want to install the solution. Agree the terms and conditions and then select **Install**. Once the installation is complete, you will see the **Virtual connectors in Dataverse** app installed under **Environments -> [your environment name] -> Dynamics 365 apps**.

   > [!div class="mx-imgBorder"]
   > ![Select environment to install connector](../media/ve-select-the-environment.png "Select environment to install connector")

4. You should also see the **Virtual Connector Provider** solution and other solutions enabled in the Power Apps environment.

    > [!div class="mx-imgBorder"]
    > ![Virtual connector provider solution](../media/ve-select-virtual-connectors-solution.png "Virtual connector provider solution")

### Create the connection
  
1. Now, go to [Power Apps](https://make.powerapps.com), select the environment in which you would like to set up the virtual table. 
  
2. In the left navigation pane, select **Data** > **Connections** then select **New connection**. 
<<<<Insert Image here>>>>
  
3. Select one of the following Virtual Connectors from the list of connections. 
> - SQL Server
> - Microsoft Excel Online (Business)
> - Microsoft SharePoint
  
4. You will be asked to provide additional details to connect to the data source. 
>#### **SQL Server:** 
> - Select SQL Server Authentication as Authentication Type. 
> - Enter SQL server name, SQL database name, the credentials needed to connect
> <<<<Insert Image here>>>> 
> - If you are using an on-premises SQL server also enter the Gateway information and then select Create.
  
>#### **Microsoft Excel Online (Business):**
>- Click Create, your current signed-in credentials will be used 
><<<<Insert Image here>>>> 
  
>#### **Microsoft SharePoint:** 
> - Select to Connect Directly (Cloud) or Connect Using on Premises Gateway
><<<<Insert Image here>>>> 
> - For Direct connection, Sign in to SharePoint
> <<<<Insert Image here>>>> 
> - For On Premises, Select your authentication type, provide your credentials, choose a Gateway and click Create
 <<<<Insert Image here>>>> 
  
### Create the Connection Reference

  5. Go to **Solutions**.
  
  6. Select the **Default Solution** or any other existing solution you have in your environment to create the virtual table.
  
  7. Select **New** and then select **Connection Reference (preview).**
  
  8. Enter **Display name**, select the connection you just created for the **Connectors** option and then select the data connection that you have created.

   > [!div class="mx-imgBorder"]
   > ![New connection reference](../media/ve-new-connection-reference.png "New connection reference")

### Create the Data Source
Now create the Virtual Table data source in Dataverse.
9. Select the **Gear icon -> Advanced Settings**
 <<<<Insert Image here>>>> 
  
10. In the top navigation bar select **Settings** and then **Administration**
 <<<<Insert Image here>>>> 
  
11. Select **Virtual Entity Data Source**
   <<<<Insert Image here>>>> 
  
12. Select **New**. In the pop-up dialog, select the Virtual Connector Data Provider. 
<<<<Insert Image here>>>> 
  
13.	Name your **Data Source** and select the **Connection Reference** you just created in the drop down list.
<<<<Insert Image here>>>>  
  
- SQL: Leave the Data Source field empty
- SharePoint: Paste the URL to your SharePoint site in the Data Source field (ex: https://contosoenvname.sharepoint.com/sites/sitename)
- Excel Online (Business): Paste in the file name including extension. Remember the file must be in the OneDrive that was used for the Connection setup. (Ex: SampleData.xlsx)
  
14. Click **Save**

### Entity Catalog
With the connection reference and the virtual table data source setup, an **Entity Catalog** is automatically generated. The **Entity Catalog** is specific to the data source and will list all the tables that are in the respective data source.
  
<<<<Insert Image here>>>> 
   > [!NOTE] 
   > - The creation of the entity catalog is an asynchronous process. Depending on your environment, this may take a few minutes. 
   > - The tables you see in the Entity Catalog are not virtual tables in themselves. You need to select from this list of tables representing the external data to create virtual table in Dataverse.
 #### View the Entity Catalog
  
- Select Data -> Tables and select the entity catalog that was created. Selecting the Data tab will show all available tables or lists.
>- SQL: All tables in the database that are eligible are shown
>- SharePoint: All lists in the site are shown
>- Excel: All tables in the Excel file are shown
<<<<Insert Image here>>>> 
- Select Advanced Find and use the Look for: column. The catalog will include a prefix Entity Catalog for followed by the connection reference (example: Entity Catalog for Adventure Works DB). Find the Entity Catalog for your respective data connection and select the Results button to see all the external data source tables. 


    > [!div class="mx-imgBorder"]
    > ![Advance find table catalog](../media/ve-advance-find-table-catalog.png "Advance find table catalog")

    >[!Note]
    > Bulk creation of virtual tables is not supported currently. Even though the Entity Catalog allows you to select multiple tables, you will have to select one table at a time to create virtual tables.

15. **create a virtual table** by clicking the record from the entity catalog. In the provided form set the **Create or Refresh Entity** column to **Yes**.
16. Select the Primary Key and Primary Field of the virtual entity by using the dropdowns to find the columns you wish to use. 
<<<<Insert Image here>>>>     

  Save the record to create the virtual table. Your Virtual Table is now created with a “Custom Entity” prefix. 
  Once the virtual table is created, you can either:
  - Select the newly created table in the Data -> Tables list and view the records by clicking the Data tab. Changing the view to All will show all the columns.
<<<<Insert Image here>>>>    
  
  - Use **Advanced Find** and select the virtual table to retrieve all the records.

    > [!div class="mx-imgBorder"]
    > ![Advance find virtual table](../media/ve-advance-find-virtual-table.png "Advance find virtual table")

   
    > [!IMPORTANT] 
    > - Virtual tables no longer require an associated GUID as a primary key with the virtual connector provider. 
    > - The provider automatically maps the primary key associated with the external data source when creating the virtual table. All CRUD operations can be performed on the generated virtual table. 
  > - All columns in the external data are automatically mapped to Dataverse types that are support by the connector. You can review the virtual table details and make changes by navigating to **Settings -> Customization – Entities** view.
  > - Virtual Tables require there to be at least one string field to use as the Primary Name column.

   Review the [SQL Server Connector documentation](/connectors/sql/) for the full list of [datatype mappings supported by SQL Server Connector](/connectors/sql/#power-apps-data-type-mappings).

Once you have created a virtual table, you can work with it much the same way as any other table. You can start defining the relationships with other tables, in the environment and use them in your Power Apps and Power Automate flows.

### Setting up virtual table relationship

Virtual tables are  enabled for relationships. You can set up 1:N, N:1, and N:N relationships. These relationships can be established between `native: virtual tables` and between `virtual: virtual tables`. You can only set up `virtual: virtual relationship` between tables from the same virtual table provider. 

For instance, you cannot set up a relationship between a virtual table created using the OData virtual table provider and a virtual table created using the Virtual Connector provider.

#### Defining relationships in virtual tables

Virtual tables created using the virtual connector provider automatically creates all the columns that are represented in the external source table. This will also include columns on which relationships are defined. However, the relationship definition will not be automatically created. You will have to define this relationship in Dataverse manually.

The following example creates an N:1 relationship between a virtual table (**Service Request**) and a native table (**Account**). The column used to set up the relationship is **AccountId**. This column is the primary key in the Account table and is a foreign key in the Service Request table.

A representation of the **Service Request** virtual table is shown below. You will notice that the **AccountId** column, which is the column used for relationship in the external source, is of type **Multiple Line of Text**. You need to have this column represented as a **Lookup** type to create a relationship.

> [!div class="mx-imgBorder"]
> ![Creating columns in virtual table](../media/ve-create-columns.png "Create columns in virtual table")

1. Go to **Advanced settings -> Settings -> Customization** and choose **Customize the System**.

2. In the left navigation pane, expand the **Entities** view and browse to the Service Request virtual table definition.

3. Select the **Fields** view and select the **AccountId** column and select **Delete**.

4. Choose **Delete** to confirm the deletion of this column.

5. To create the relationship, select the **N:1 Relationship** within the Service Request table.

6. Select **New Many-to-1 Relationship**.

7. Enter the following details to create the relationship between the Service Request virtual table and the Account table.

    1. In the **Relationship Definition** section – set the **Primary Entity** column value to **Account**.

    2. Optionally, if you want to edit the name of the relationship, you can do so in the **Name** column.

    3. In the **Lookup Field** section – set the **Display Name** to **Account.**

    4. The **Name** column will automatically populate with the lookup column name.

    5. Set the **External Name** value to **AccountId** (matching the column name in your source table).

        > [!div class="mx-imgBorder"]
        > ![Create Relationship](../media/ve-create-relationship.png "Create relationship")

8. Refer to the columns for the **Service Request** virtual table, and you will notice that the **AccountID** column is not a **Lookup** type. This column can now
be added to forms and views to see all associated accounts for each of the service request record.

   > [!div class="mx-imgBorder"]
   > ![Custom table columns](../media/ve-custom-table-columns.png "Custom table columns")

9. With the relationship established you can now create a new service request and pick accounts to associate them to.

   > [!div class="mx-imgBorder"]
   > ![New custom table](../media/ve-new-custom-table.png "New custom table")

   > [!NOTE]
   > You will have to edit the forms and views for this table to include the lookup column and other required columns prior to operation on the virtual table.

#### Tips

1. Primary Key column should be included in create form if you did not set up the column to increment during the design of the underlying source table automatically. You will have to enter a valid value in the primary key column for an insert operation to succeed.

2. If **Entity Catalog** creation takes a long time, you can check the job completion status by navigating to **Settings -> System Jobs** view.


## Known limitations

### General
1.	Maximum length of characters allowed for a text column in a virtual table is 4000 characters. If the source table has a maximum character limit greater than this value, any create/update operation exceeding the max character limit will result in a validation error, and the operation will fail.
2.	Virtual table queries are limited to return 250 records. If you have a 1:N or N:N relationship with a virtual table, any query exceeding this limit will fail and provide an error. Use filtering in your query to reduce the record set as a workaround to this limitation.
3.	Audit functionality is not available for Virtual Tables, this is because Dataverse can only perform and store audit data for locally stored data.
4.	Rollups cannot be calculated for Virtual tables, this is because Rollups are a server side calculation in Dataverse which requires the data to be stored locally.

### SQL
1.	SQL data type bigint columns in the source table will be mapped as a decimal data type in Dataverse virtual tables. When platform support is available for bigint mapping to a whole number, previously created columns in the virtual table will need to be deleted, and new columns should be created. 
2.	SQL Server tables without primary keys: Any non-string field can be selected as the primary key. The virtual table should be created successfully. RetrieveMultiple will work, the other operations will fail with the following error message (coming from SQL connector): "APIM request was not successful : BadRequest : No primary key exists in table".
3.	SQL Server tables with a string primary key: The SQL string primary key will be the only option available for the virtual table primary key. The virtual table creation will succeed, but fail at runtime with this error: "String primary keys are supported only if they can be parsed as GUID". SQL Server string primary keys are supported only if the values can be parsed as GUID.
4.	SQL Server tables without non-primary key string fields: The primary field list will be empty and the user will not be able to create the virtual table. At least one non-primary key string field is required.
5.	SQL Server Connector Limitations: see [SQL Server connector reference](/connectors/sql/). 

### Excel
1.	Excel files must be stored on a OneDrive to participate in a Virtual Table connection.

2.	The Primary key can only be a column holding GUID values: Because the Excel table metadata shows all columns as string, our current design assumes that the primary key will always be a GUID represented as a string.

Note that no validation is performed when the virtual entity is created, if a non-GUID column is selected, the entity will fail at runtime with this error: "String primary keys are supported only if they can be parsed as GUID".

3.	Support for PowerAppsId__ auto-generated column: The _PowerAppsId_ auto-generated column will be used if found (it will be the only option available for Primary key). Providing a value for PowerAppsId is required at record creation even if the value will actually be overwritten by an automatically generated one. This doesn't happen if the primary key column is not the PowerAppsId auto-generated column.
  
4.	Specific Excel Connector Limitations: [Excel Online (Business) connector reference](connectors/excelonlinebusiness/).

### SharePoint
1.	You currently cannot select an “All” view for SharePoint columns on a Virtual Table. This is a known bug and is being fixed.

  
## Troubleshooting


1. You are seeing only one (1) record in your virtual table even though you have more in your source table.

    **Solution:** Check your source table and make sure it has primary key defined.
  
2.	I created a virtual table but I can't see it in "Tables"
Solution: Since the virtual table creation is asynchronous, you can check the status of the process in "System Jobs". Look for system jobs with a Name starting Microsoft.Wrm.DataProvider.Connector.Plugins.ConnectorGenerateVEPlugin and a "Regarding" column's value equal to the name of the new virtual table. If status is still In Progress, just wait for the job to complete. If there is an error, you can get details by clicking the system, job name hyperlink.
In this example, table creation is still pending:
<<<<Insert Image here>>>>    
Here, table creation failed due to 429 "Too Many Requests" error:
 <<<<Insert Image here>>>>   
3.	Table creation's system job succeeded but I am getting runtime errors related to invalid or missing columns
Solution: If a failure occurs while creating a table's field, the table creation process will not fail and try to continue with the remaining fields. This is because we don't want to block the virtual table creation when some column types are unsupported. To get details on the error, you can enable logging in Administration > System Settings > Customizations > Enable logging to plug-in trace log, then delete the virtual table and try to create it again.


### See also

[Get started with virtual tables (entities)](get-started-ve.md)
