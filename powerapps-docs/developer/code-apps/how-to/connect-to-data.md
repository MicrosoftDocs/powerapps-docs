---
title: "How to: Connect your code app to data"
description: "Learn how to connect your code app to data"
ms.author: jordanchodak
author: jordanchodakWork
ms.date: 02/02/2026
ms.reviewer: jdaly
ms.topic: how-to
contributors:
 - JimDaly
 - alaug
---
# How to: Connect your code app to data

Code apps can connect to Power Platform connectors.

Use the following steps:

1. [Create and set up connections in Power Apps](#create-and-set-up-connections-in-power-apps)
1. [Add a connection to a code app](#add-a-connection-to-a-code-app)
1. [Update the app to call connections](#update-the-app-to-call-connections)

> [!NOTE]
> Use these steps after you initialize the app by using [pac code init](/power-platform/developer/cli/reference/code#pac-code-init). This step is the third step in [how to create a code app from scratch](create-an-app-from-scratch.md).


## Create and set up connections in Power Apps

Start by creating and configuring connections at [Power Apps](https://make.powerapps.com). Copy connection metadata from there for use in later steps.

All connectors are officially supported except the ones listed in the following section.

### Connectors that aren't yet supported

- [Excel Online (Business)](/connectors/excelonlinebusiness/)
- [Excel Online (OneDrive)](/connectors/excelonline/)

> [!IMPORTANT]
> For the initial release, you can only configure code apps to use existing connections in [Power Apps](https://make.powerapps.com). You can't create new connections through PAC CLI commands. Support for creating new connections will be added in a future release.

### Launch the Power Apps Connections page

   Go to [Power Apps](https://make.powerapps.com) and navigate to the **Connections** page from the left-hand navigation.

   :::image type="content" source="media/powerapps-create-connection.png" alt-text="Power Apps Connections page showing New connection button":::

#### Example: Create an Office 365 Users connection

Select **+ New connection** and select **Office 365 Users**. Select **Create**.

> [!NOTE]
> If you already have an Office 365 Users connection, use that connection instead of creating a new one.

:::image type="content" source="media/powerapps-create-office-connection.png" alt-text="Create Office 365 Users connection in Power Apps":::

#### (Optional) Create a SQL connection (or a connection for another tabular data source)

> [!TIP]
> For a step-by-step guide to connecting your code app to Azure SQL, see [How to: Connect your code app to Azure SQL](connect-to-azure-sql.md).

### Get connection metadata for all created connections

Use one of the following methods:

- [Use PAC CLI](#use-pac-cli)
- [Use Power Apps URL](#use-power-apps-url)

#### Use PAC CLI

Use the Power Apps CLI to list your available connections and retrieve their IDs by using the [pac connection list](/power-platform/developer/cli/reference/connection#pac-connection-list) command.

`pac connection list` displays a table of all your connections, including the **Connection ID** and **API Name**. The API name serves as the `appId` when you add a data source.

:::image type="content" source="media/pac-cli-connection-list.png" alt-text="PAC CLI list output showing Connection ID and API Name":::

#### Use Power Apps URL

You can also retrieve this information by using Power Apps. When you view the details of a connection, you can see the URL.

:::image type="content" source="media/powerapps-select-connection.png" alt-text="Select a connection in Power Apps to view its details":::

The API name and connection ID appear in the URL:

:::image type="content" source="media/powerapps-connection-apiname-connectionid.png" alt-text="Connection details showing API name and Connection ID values":::

Copy the API name and the connection ID from PAC CLI to the URL for each connection.

## Add a connection to a code app

After you create or identify existing connections to use, and copy the connection metadata from the previous step, add those connections to the app.

When you add the data sources to the app, the process automatically generates a typed TypeScript model and service file in the repo. For example, the Office 365 Users data source produces `Office365UsersModel` and `Office365UsersService` files.

### Add a nontabular data source

Add a nontabular data source (such as Office 365 Users) to the app by using the PAC CLI [pac code add-data-source](/power-platform/developer/cli/reference/code#pac-code-add-data-source) command.

From a command line, run the following command. Use the API name and connection ID that you collected from previous steps.

```powershell
pac code add-data-source -a <apiName> -c <connectionId>
```

For example:

```powershell
pac code add-data-source -a "shared_office365users" -c "aaaaaaaa000011112222bbbbbbbbbbbb"
   ```

### Add a tabular data source

SQL or SharePoint are examples of tabular data sources.

Use the same PAC CLI [pac code add-data-source](/power-platform/developer/cli/reference/code#pac-code-add-data-source) command, but include a table ID and dataset name. The schema of your tabular data source specifies these values. If you don't already have these values, see [Retrieve a dataset name and table ID](#retrieve-a-dataset-name-and-table-id).

```powershell
pac code add-data-source -a <apiName> -c <connectionId> -t <tableId> -d <datasetName> 
```

For example:

```powershell
pac code add-data-source `
-a "shared_sql" `
-c "aaaaaaaa000011112222bbbbbbbbbbbb" `
-t "[dbo].[MobileDeviceInventory]" `
-d "paconnectivitysql0425.database.windows.net,paruntimedb"

pac code add-data-source `
-a "shared_sql" `
-c "aaaaaaaa000011112222bbbbbbbbbbbb" `
-t "[dbo].[EmployeeInformation]" `
-d "paconnectivitysql0425.database.windows.net,paruntimedb" 
```

#### Retrieve a dataset name and table ID

> [!IMPORTANT]
> The following steps to retrieve a dataset name and table ID are a temporary workaround. We plan to add an easier mechanism to get these values.

If you don't already have the table and dataset name, you can get them by running a canvas app and copying the values from the browser network inspector:

1. Create a new canvas app in Studio.
1. Add the connection to the canvas app.
1. Bind the connection to a gallery control.
1. Publish and run the app.
1. Open your browser's **Developer Tools**, go to the **Network** tab, and inspect requests made when the app loads. Check the "invoke" request, and go to its response.
1. Find an Azure API Management (APIM) request with the connection ID, dataset name, and table ID, and copy those values.

   Using this example data request URL through APIM, look for the `<Connection ID>`, `<Dataset name>`, and `<Table ID>` values in these places in the URL:

   ```http
   https[]()://{id value}.01.common.azure-apihub.net/apim/sharepointonline/<Connection ID>/datasets/<Dataset name>/tables/<Table ID>/items
   ```

### Add a SQL stored procedure as a data source

From a command line, run the following command. Use the API name and connection ID that you collected previously.

```powershell
pac code add-data-source -a <apiId> -c <connectionId> -d <dataSourceName> -sp <storedProcedureName> 
```

For example:

```powershell
pac code add-data-source `
–a "shared_sql" `
-c "33dd33ddee44ff55aa6677bb77bb77bb" `
-d "paconnectivitysql0425.database.windows.net,paruntimedb" `
-sp "[dbo].[GetRecordById]" 
```

### Delete data sources

If needed, you can delete data sources after adding them.

From a command line, run the following command. Use the API name and connection ID that you collected previously.

```powershell
pac code delete-data-source -a <apiName> -ds <dataSourceName> 
```

For example:

```powershell
pac code delete-data-source `
-a "shared_sql" `
-ds "MobileDeviceInventory" 
```

> [!IMPORTANT]
> If the schema on a connection changes, no command exists to refresh the typed model and service files. Instead, delete the data source and readd it.

### Use connection references to add a data source

Starting in version 1.51.1 of the Power Apps CLI released in December 2025, you can use connection references to add data sources to your code app. A connection reference is a solution component that points to a specific connection for a connector. Instead of binding your app directly to a user-specific connection, bind it to a reference. This approach makes the solution environment-aware and portable across Dev, Test, and Prod environments for smooth application lifecycle management.

> [!NOTE]
> This section assumes you have a basic knowledge of solutions in Power Apps and connection references. You should have a solution created already and a connection reference in that solution for your data source. If you don't, follow the steps outlined in the links below to create one.
>
> - [Learn about solutions in Power Apps](../../../maker/data-platform/solutions-overview.md).
> - [Learn about connection references and what makes them useful to your Power Apps](../../../maker/data-platform/create-connection-reference.md).
>

#### Get the solution ID

Use one of the following methods to get the ID of your solution:

**Use the PAC CLI solution list command:**

1. Open a command prompt or terminal window.
1. Run the following command to get a list of solutions in [the environment you're connected to](/power-platform/developer/cli/introduction#manage-auth-profiles):

   ```powershell
   pac solution list --json | ConvertFrom-Json | Format-Table
   ```

   This command outputs a table to the console with the `Id`, `SolutionUniqueName`, and `FriendlyName` solution properties.

1. Copy the solution `Id` and save it for later use.

**Use the Power Apps solution explorer:**

1. Sign in to [Power Apps](https://make.powerapps.com).
1. On the left pane, select **Solutions**. If the item isn't in the side panel pane, select **More** and then select the item you want.
1. Find the solution that contains the connection reference for your data source.
1. Select the solution to open it.
1. In the URL of the browser, find the solution ID at the end of the URL. Your URL is of the form:

   ```
   https://make.powerapps.com/environments/environmentId/solutions/solutionId
   ```
  
1. Copy the solution ID from the URL and save it for later use.

#### Get the name of the connection reference to your data source

Use one of the following methods to get the connection reference to your data source:

**Use the PAC CLI code command to list the connection references in a solution:**
 
1. Open a command prompt or terminal window.
1. Run the following command to get the solution ID and name of the connection reference to your data source:
     
   ```shell
    pac code list-connection-references -env <environmentURL> -s <solutionID>
   ```

1. The output includes the display name, logical name, and description of the connection references in the solution.

**Use the Power Apps solution explorer to examine the connection references in a solution:**

1. Sign in to [Power Apps](https://make.powerapps.com).
1. On the left pane, select **Solutions**. If the item isn't in the side panel pane, select **More** and then select the item you want.
1. Find the solution that contains the connection reference for your data source.
1. Select **Connection References** from the list of **Objects** in the left pane.

#### Add the data source to your code app by using the connection reference

From a command line, run the following command. Use the solution ID and connection reference logical name collected from previous steps.

```shell
pac code add-data-source -a <apiName> -cr <connectionReferenceLogicalName> -s <solutionID>
```

The app now uses the connection associated with the connection reference in your Power Apps solution.

## Update the app to call connections

After you add connections, update the app to use the generated model and service.

> [!NOTE]
> You can also make these changes by using an agent in your IDE. For instance, in Visual Studio Code, you might use GitHub Copilot agent mode to make them for you after you add the data sources.
   
1. **Import required types and services**

   When you add a data source, the portal automatically generates model and service files. It places these files in the `/generated/services/` folder.
   For example, if you add `Office365Users` as a data source, the portal creates the following files:

   - `Office365UsersModel.ts` – Defines the data model for request and response objects in the `Office365Users` connector.
   - `Office365UsersService.ts` – Provides service methods for interacting with the `Office365Users` data.

   Import and use these files in your code like this:

   ```typescript
   import { Office365UsersService } from './generated/services/Office365UsersService';
   import type { User } from './generated/models/Office365UsersModel';
   ```

1. **Update the app to use the nontabular data source (for example, Office 365 Users)**

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

   Use this command in the terminal:

   ```powershell
   npm run build | pac code push
   ```


