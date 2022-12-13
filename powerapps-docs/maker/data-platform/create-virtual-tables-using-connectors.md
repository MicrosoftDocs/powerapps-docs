---
title: "Create virtual tables using virtual connectors (preview) (Microsoft Dataverse) | Microsoft Docs"
description: "Learn how to create virtual tables using virtual connectors in Microsoft Dataverse."
ms.date: 12/13/2022
ms.reviewer: matp
ms.topic: article
author: NHelgren # GitHub ID
ms.author: nhelgren
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
contributors: 
  - JimDaly
  - phecke 
---
# Create virtual tables using the virtual connector provider (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

Virtual tables enable integrating data from external data sources by seamlessly representing that data as tables in Microsoft Dataverse, without data replication. Solutions, apps, flows, and more can use virtual tables as if they were native Dataverse tables. Virtual tables allow for full create, read, update, and delete privileges unless the data source they are connecting to specifically forbids it. More information about virtual tables: [Create and edit virtual tables that contain data from an external data source](create-edit-virtual-entities.md).

In this public preview release, we're introducing a new user experience using Power Apps (make.powerapps.com) to create virtual tables using the following virtual connector providers:

- [SQL Server](/connectors/sql/) 
- [Microsoft SharePoint](/connectors/sharepointonline/)


## Overview

Virtual tables include the following components:

:::image type="content" source="media/ve-components.png" alt-text="Virtual table components":::

- Data Source – the location where the external data is stored.
- Data Provider – defines the behavior of the virtual table.
- Connection – this sets up the ability to connect to the data source and authentication.
- Connection reference – this provides a way for Dataverse to use the connection to the data source.

If you were to create a virtual table using a custom data provider, you'll need to write plugins that define how every Dataverse API would interact with the API on the system where the data is stored. This is a long process which requires knowledge of coding. Virtual connector providers streamline the creation experience by automating some of the creation for you and removing the need to use code to create the virtual tables.

When you establish a remote connection to an external source using a connector data source, the virtual connector provider automatically retrieves a list of all the available tables and lists by retrieving table definitions (metadata) from the external data source. You then select these tables and lists to generate the virtual table.

The underlying data source is key for allowing the provider to establish an authenticated remote connection to the external data. It uses a connection reference that stores pertinent details regarding the external source. The information stored in the connection reference is specific to the connector type and the connection it refers to.

:::image type="content" source="media/ve-connector-provider-overview.png" alt-text="Virtual connectors provider overview":::

When setting up the connection and connection reference for your data sources, specific information will be needed. For example, setting up the **SQL Server** connector needs server name, database name, the authentication method, username, password, and (optionally) gateway connection details. Each external data source will need a connection reference to be defined to create the virtual table. When using the Power Apps (make.powerapps.com) experience the connection reference can be generated automatically for you unless you wish to provide custom naming.

The connector permissions enforce the ability for organizational users to access and operate on the virtual table. The connection can be shared with one user or can be shared with entire organization. This allows users to access and operate virtual tables using a shared connection. Through the use of security roles, virtual table access can be restricted to a specific set of users within your organization. You can even specify which roles have create, read, update, or delete privileges in this way.

Application lifecycle management (ALM) is supported for virtual tables created using the virtual connector provider, you can even create the virtual tables from directly within the solution when using Power Apps (make.powerapps.com) portal. Virtual tables should be part of the managed solution along with the connection reference to distribute the solution. The solution can have other components, such as a model-driven app that uses virtual tables.

More information about application lifecycle management (ALM) and solutions:

- [Application lifecycle management (ALM) in Microsoft Power Platform](/power-platform/alm/)
- [Solutions overview](solutions-overview.md)

## Prerequisites

To create a virtual table, you must have a Microsoft Dataverse license through Power Apps or Microsoft Dynamics 365. Microsoft 365 or Teams licenses can't be used to create virtual tables.

## Videos that show how to create the connection

# [SQL Server](#tab/sql)

Watch a 4-minute video showing how to create a virtual table with the SQL virtual connector provider.

> [!VIDEO https://www.microsoft.com/videoplayer/embed/RE4XLkU]

# [Microsoft SharePoint](#tab/sharepoint)

Watch a 4-minute video showing how to create a virtual table with the SharePoint virtual connector provider. 

> [!VIDEO https://www.microsoft.com/videoplayer/embed/RE4YcIk]

---

## Create a virtual table using a connection

In Power Apps, create a virtual table either from a solution or from a list of tables.

### Select the data source connection

1. Sign into [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), and then select **Solutions** on the left hand navigation pane.
1. Open an existing solution or create a new one.
1. Select **New** on the command bar, select **Table**, and then select **Table from external data**.
   :::image type="content" source="media/table-from-external-data-command.png" alt-text="Create a table from external data command":::
1. Choose from the following options for the connection:
   - To use an existing connection, select the connection you want.
   - If you have an existing connection but wish to create a new one, select **New Connection**, and complete the information on your screen that appears on a new browser tab.
   - If you don't have a connection for the data source you want, select **+Add Connection** next to the data source, and complete the information on your screen that appears on a new browser tab.
   - More information about creating a connection: [Create a SQL Server connection](/connectors/sql/#creating-a-connection) and [SharePoint connector](/connectors/sharepointonline/)

1. Select the connection reference, and then select **Next**.
1. [Configure the connection](#configure-the-connection)

### Configure the connection

1. Depending on the data source:
   - For SharePoint connections: 
      1. Paste the URL of your SharePoint site in the provided field, or select from your most recently used SharePoint sites. The most recently used list is populated by gathering information about your recently used sites using Graph and your Azure Active Directory credentials. Select **Next**. 
      > [!NOTE]
      > If you are entering your SharePoint URL, only include the information up to the site name, such as *https://microsoft.sharepoint.com/teams/Contoso*.
      1. **Search** your SharePoint site for a specific list, or select the one you want from the provided list, and then select **Next**.
      1. You can choose to modify the suggested table names by selecting [Configure table and column names that will be used in Dataverse](#configure-table-and-column-names-that-will-be-used-in-dataverse)

   - For SQL connections, enter the **SQL Server name** and **SQL database name**, and then select **Next**.  
      1. Select a table. Either **Search** the SQL database for a specific table and select it or select a table from the available tables.
      1. You can choose to modify the suggested table names by selecting [Configure table and column names that will be used in Dataverse](#configure-table-and-column-names-that-will-be-used-in-dataverse)

1. Select **Next**.

#### Manually create the connection reference (optional)

When you create a virtual table, your connection reference will automatically be created for you along with the virtual table. However, you can expand **Advanced Options** and then select the **Manually Configure Connection Reference** to manually create a connection reference for the virtual table.

> [!NOTE]
> - The benefit of optionally naming your connection reference is because it can be easier to find later if you need details about it.
> - If you are using an existing connection you can select an existing connection reference or create a new one. Creating a new connection reference is only used if you want to segment your virtual tables into completely unrelated solutions for use later.

When you manually configure your connection reference, you will be taken to the **Connection Reference** page. Select or name your connection reference and click **Next**.

Select or name your connection reference and select **Next**.

#### Configure table and column names that will be used in Dataverse

1. If you want to **Configure table and column names that will be used in Dataverse**, accept or change the following properties, and then select **Next**
   - **Display name**: The name that will be used to identify your virtual table.
   - **Plural name**: The plural of the virtual table name, used in appropriate situations where you refer to one or more record from the table, such as *Customer* is the table for multiple records refereed to as *Customers*.
   - **Schema name**: The logical name Dataverse uses for the virtual table, which includes the solution publisher prefix.
   - **Primary field**: This is the text value to be used when looking up records on your virtual table. Only string fields may be selected. A primary key is a required field but will be chosen by Dataverse.
 1. Choose if you would like to rename any of your columns. The following fields are provided: 
   - **External column**. This is the schema name of the column in the data source. This property is read only.
   - **Display name**. The name that's used to identify your column. 
   - **Schema name**. The logical name Dataverse will use for the column that will include your solution publisher prefix.
   There's a **Quick Format Names** option on the page, this will provide suggested name changes and can be useful if you have a large number of fields that include prefixed values from your SQL server such as &lt;tablename&gt;.&lt;column name&gt;. For example, *Database12.Products* would change to **Products**.

#### Complete the setup

1. The **Review and Finish** page shows you the table you are connecting to in your data source, and the table that will be created in Dataverse.
   > [!NOTE]
   > Select **Choose a different table** takes you back to the table selection screen. selecting **Edit Configuration of Table** takes you to the **Configuration** screen.
1.	If everything is correct select **Next**.

Once the table is created you are taken directly to your new virtual table where you can view your data and begin working with it. 

> [!NOTE]
> When you attempt to create a virtual table that already exists, you receive a message that the table already exists and that you will be re-creating it. You will not be able to change the primary field or schema name if this is the case. Re-creating the table will update any column changes that were made in the data source on the table.

### See also

[Developers Guide: Get started with virtual tables (entities)](../../developer/data-platform/virtual-entities/get-started-ve.md)
