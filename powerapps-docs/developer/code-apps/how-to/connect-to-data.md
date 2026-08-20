---
title: "How to: Connect Your Code App to Data"
description: "Learn how to connect your code app to data with Power Platform connectors, add tabular or nontabular sources, and call generated services."
ms.author: jordanchodak
author: jordanchodakWork
ms.date: 08/19/2026
ms.reviewer: jdaly
ms.topic: how-to
contributors:
 - JimDaly
 - alaug
---
# How to: Connect your code app to data

Learn how to connect your code app to data by using Power Platform connectors, so you can add data sources and call generated services from your app.

Use the following steps:

1. [Create and set up connections with the Power Apps CLI](#create-and-set-up-connections-with-the-power-apps-cli)
1. [Add a connection to a code app](#add-a-connection-to-a-code-app)
1. [Update the app to call connections](#update-the-app-to-call-connections)

> [!NOTE]
> Use these steps after you initialize the app by using [`pa app init`](../reference/cli.md#pa-app-init).


## Create and set up connections with the Power Apps CLI

Use the Power Apps CLI to find a connector and create its connection. Follow [Create a connection from the Power Apps CLI](create-connection.md), and save the connection ID returned by the command.

All connectors are officially supported except the ones listed in the following section.

### Connectors that aren't yet supported

- [Excel Online (Business)](/connectors/excelonlinebusiness/)
- [Excel Online (OneDrive)](/connectors/excelonline/)

> [!TIP]
> For a step-by-step guide to connecting your code app to Azure SQL, see [How to: Connect your code app to Azure SQL](connect-to-azure-sql.md).

### Get connection metadata

Use [`pa connection list`](../reference/cli.md#pa-connection-list) to list your available connections and get their IDs if you didn't save the ID returned by [`pa connection create`](../reference/cli.md#pa-connection-create):

```bash
pa connection list
```

The command shows a table of connections, including the **Connection ID** and connector identifier. Use these values when you add a data source.

:::image type="content" source="media/pac-cli-connection-list.png" alt-text="Screenshot of Power Apps CLI output with connection IDs and connector identifiers.":::

## Add a connection to a code app

After you create or identify existing connections to use, and copy the connection metadata from the previous step, add those connections to the app.

When you add the data sources to the app, the process automatically generates a typed TypeScript model and service file in the repo. For example, the Office 365 Users data source produces `Office365UsersModel` and `Office365UsersService` files.

### Add a non-tabular data source

Add a non-tabular data source, such as Office 365 Users, by using [`pa app add data-source`](../reference/cli.md#pa-app-add-data-source).

From a command line, run the following command. Use the connector identifier and connection ID that you collected from previous steps.

```powershell
pa app add data-source --connector <connector-id> --connection-id <connection-id>
```

For example:

```powershell
pa app add data-source --connector "shared_office365users" --connection-id "aaaaaaaa000011112222bbbbbbbbbbbb"
   ```

### Add a tabular data source

SQL or SharePoint are examples of tabular data sources.

Use the same [`pa app add data-source`](../reference/cli.md#pa-app-add-data-source) command, but include the table and dataset. The schema of your tabular data source specifies these values. If you don't already have these values, see [Discover available datasets and tables](#discover-available-datasets-and-tables).

```powershell
pa app add data-source `
--connector <connector-id> `
--connection-id <connection-id> `
--table <table-id> `
--dataset <dataset-name>
```

#### SQL example

```powershell
pa app add data-source `
--connector "shared_sql" `
--connection-id "aaaaaaaa000011112222bbbbbbbbbbbb" `
--table "[dbo].[MobileDeviceInventory]" `
--dataset "paconnectivitysql0425.database.windows.net,paruntimedb"

pa app add data-source `
--connector "shared_sql" `
--connection-id "aaaaaaaa000011112222bbbbbbbbbbbb" `
--table "[dbo].[EmployeeInformation]" `
--dataset "paconnectivitysql0425.database.windows.net,paruntimedb" 
```

#### SharePoint example

For SharePoint, `--table` is the list name and `--dataset` is the SharePoint site:

```powershell
pa app add data-source `
--connector "shared_sharepointonline" `
--connection-id "aaaaaaaa000011112222bbbbbbbbbbbb" `
--table "Travel%20Request" `
--dataset "https://contoso.sharepoint.com/sites/TravelPolicies"
```

#### Discover available datasets and tables

Use the [`pa connection`](../reference/cli.md) commands to discover available datasets, tables, and stored procedures for your connections.

**[List datasets](../reference/cli.md#pa-connection-list-datasets):**

```powershell
pa connection list-datasets --connector <connector-id> --connection-id <connection-id>
```

**[List tables](../reference/cli.md#pa-connection-list-tables):**

```powershell
pa connection list-tables --connector <connector-id> --connection-id <connection-id> --dataset <dataset-name>
```

**[List SQL stored procedures](../reference/cli.md#pa-connection-list-procedures):**

```powershell
pa connection list-procedures --connection-id <connection-id> --dataset <dataset-name>
```

**Example workflow for SQL Server:**

```powershell
# Step 1: List available datasets
pa connection list-datasets --connector "shared_sql" --connection-id "aaaaaaaa000011112222bbbbbbbbbbbb"

# Step 2: List tables in the dataset
pa connection list-tables --connector "shared_sql" --connection-id "aaaaaaaa000011112222bbbbbbbbbbbb" `
  --dataset "paconnectivitysql0425.database.windows.net,paruntimedb"

# Step 3: Add the table to your code app
pa app add data-source --connector "shared_sql" --connection-id "aaaaaaaa000011112222bbbbbbbbbbbb" `
  --table "[dbo].[MobileDeviceInventory]" `
  --dataset "paconnectivitysql0425.database.windows.net,paruntimedb"
```

> [!TIP]
> Copy the exact **Name** values from the command output when you use them with [`pa app add data-source`](../reference/cli.md#pa-app-add-data-source). Names are case-sensitive and might contain special characters.

### Add a SQL stored procedure as a data source

Run the following command from a command line. Use the connector identifier and connection ID that you collected previously.

```powershell
pa app add data-source `
--connector <connector-id> `
--connection-id <connection-id> `
--dataset <dataset-name> `
--procedure <stored-procedure-name>
```

For example:

```powershell
pa app add data-source `
--connector "shared_sql" `
--connection-id "33dd33ddee44ff55aa6677bb77bb77bb" `
--dataset "paconnectivitysql0425.database.windows.net,paruntimedb" `
--procedure "[dbo].[GetRecordById]" 
```

### Remove a data source

If needed, you can delete data sources after adding them.

Use [`pa app remove data-source`](../reference/cli.md#pa-app-remove-data-source) with the connector identifier and data source name.

```powershell
pa app remove data-source --connector <connector-id> --name <data-source-name>
```

For example:

```powershell
pa app remove data-source `
--connector "shared_sql" `
--name "MobileDeviceInventory" 
```

### Refresh a data source

If the schema changes, use [`pa app refresh data-source`](../reference/cli.md#pa-app-refresh-data-source) to refresh the generated model and service files:

```bash
pa app refresh data-source --name <data-source-name>
```

### Use connection references to add a data source

Use connection references to add data sources to your code app. A connection reference is a solution component that points to a specific connection for a connector. Instead of binding your app directly to a user-specific connection, bind it to a reference. This approach makes the solution environment-aware and portable across Dev, Test, and Prod environments for smooth application lifecycle management.

> [!NOTE]
> This section assumes you have a basic knowledge of solutions in Power Apps and connection references. You should have a solution created already and a connection reference in that solution for your data source. If you don't, follow the steps outlined in the links in the next section to create one.
>
> - [Learn about solutions in Power Apps](../../../maker/data-platform/solutions-overview.md).
> - [Learn about connection references and what makes them useful to your Power Apps](../../../maker/data-platform/create-connection-reference.md).
>

#### Get the solution ID

Use the solution list command to get the ID of your solution.

1. Open a command prompt or terminal window.
1. Run the following command to get a list of solutions in [the environment you're connected to](/power-platform/developer/cli/introduction#manage-auth-profiles):

   ```powershell
   pa solution list
   ```

   This command outputs a table to the console with the `Id`, `SolutionUniqueName`, `Version` and `FriendlyName` solution properties.

1. Copy the solution `Id` and save it for later use.

#### Get the name of the connection reference to your data source

Use the Power Apps CLI to list the connection references in a solution:
 
1. Open a command prompt or terminal window.
1. Use [`pa connection list-references`](../reference/cli.md#pa-connection-list-references) to get the solution ID and name of the connection reference to your data source:
     
   ```shell
   pa connection list-references --solution-id <solution-id>
   ```

1. The output includes the display name, logical name, and description of the connection references in the solution.

#### Add the data source to your code app by using the connection reference

From a command line, run the following command. Use the solution ID and connection reference logical name collected from previous steps.

```shell
pa app add data-source `
--connector <connector-id> `
--connection-ref <connection-reference-logical-name> `
--solution-id <solution-id>
```

The app now uses the connection associated with the connection reference in your Power Apps solution.

## Update the app to call connections

After you add connections, update the app to use the generated model and service.

> [!NOTE]
> You can also make these changes by using an agent in your IDE. For instance, in Visual Studio Code, you might use GitHub Copilot agent mode to make them for you after you add the data sources.
   
1. **Import required types and services**

   When you add a data source, the CLI automatically generates model and service files. It places these files in the `/generated/services/` folder.
   For example, if you add `Office365Users` as a data source, the portal creates the following files:

   - `Office365UsersModel.ts` – Defines the data model for request and response objects in the `Office365Users` connector.
   - `Office365UsersService.ts` – Provides service methods for interacting with the `Office365Users` data.

   Import and use these files in your code like this:

   ```typescript
   import { Office365UsersService } from './generated/services/Office365UsersService';
   import type { User } from './generated/models/Office365UsersModel';
   ```

1. **Update the app to use the non-tabular data source (for example, Office 365 Users)**

   For the typed connection API, view the generated files under the `src/generated/models` and `src/generated/services` folders.

   ```javascript
   await Office365UsersService.MyProfile() 
   ```

   ```javascript
   const profile = (await Office365UsersService.MyProfile_V2("id,displayName,jobTitle,id,userPrincipalName")).data; 
      setUser(profile); 
      if (profile?.id || profile?.userPrincipalName) { 
         // Try both id and userPrincipalName for photo 
         let photoData = null; 
         try { 
         photoData = (await Office365UsersService.UserPhoto_V2(profile.id || profile.userPrincipalName)).data; 
         } catch { 
         // fallback to userPrincipalName if id fails 
         if (profile.userPrincipalName) { 
            photoData = (await Office365UsersService.UserPhoto_V2(profile.userPrincipalName)).data; 
         } 
         } 
         if (photoData) setPhoto(`data:image/jpeg;base64,${photoData}`); 
   ```

1. **(Optional) Update the app to use the tabular data source (for example, SQL)**

   For the typed connection API, view the generated files under the `src/Models` and `src/Services` folders.

   For example:

   ```javascript
   await MobileDeviceInventoryService.create(<record>) 
   await MobileDeviceInventoryService.update(id, <record>) 
   await MobileDeviceInventoryService.delete(id) 
   await MobileDeviceInventoryService.get(id) 
   await MobileDeviceInventoryService.getall() 
   ```

   ```javascript
   await MobileDeviceInventoryService.update(assetId, changedFields); 
   setAssets((prevAssets) => 
     prevAssets.map((asset) => { 
       if (asset.id === assetId) { 
   ```

1. **Run the app locally to verify changes**

   Use this command in the terminal:

   ```powershell
   npm run dev
   ```

1. **Push the app to run on Power Apps**

   Build the app, and then use [`pa app push`](../reference/cli.md#pa-app-push) to publish it:

   ```powershell
   npm run build
   pa app push
   ```
