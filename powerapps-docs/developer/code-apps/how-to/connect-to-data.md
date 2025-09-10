---
title: "How to: Connect your code app to data"
description: "Learn how to connect your code app to data"
ms.author: alaug
author: alaug
ms.date: 09/10/2025
ms.reviewer: jdaly
ms.topic: how-to
contributors:
 - JimDaly
---
# How to: Connect your code app to data

Code apps enable connecting to Power Platform connectors.

Use the following steps:

1. [Create and set up connections in Power Apps](#create-and-set-up-connections-in-power-apps)
1. [Add a connection to a code app](#add-a-connection-to-a-code-app)
1. [Update the app to call connections](#update-the-app-to-call-connections)

> [!NOTE]
> Use these steps after you initialize the app with [pac code init](/power-platform/developer/cli/reference/code#pac-code-init). See the steps leading up to the [Initialize your code app](create-an-app-from-scratch.md#initialize-your-code-app) section in [How to: Create a code app from scratch](create-an-app-from-scratch.md).

> [!IMPORTANT]
> The following connectors are officially supported: SQL, SharePoint, Office 365 Users, Office 365 Groups, Azure Data Explorer, OneDrive for work or school, Power Apps for Makers, Microsoft Teams, MSN Weather, and Microsoft Translator V2. [Dataverse create, read, update, and delete operations](./connect-to-dataverse.md) are officially supported. Other connectors are expected to work but are untested.


## Create and set up connections in Power Apps

Start by creating and configuring connections at [Power Apps](https://make.powerapps.com). Copy connection metadata from there for use in later steps.

> [!IMPORTANT]
> For the initial release, you can only configure code apps to use existing connections in [Power Apps](https://make.powerapps.com). You can't create new connections through PAC CLI commands. Support for creating new connections will be added in a future release.

### Launch the Power Apps Connections page

   Go to [Power Apps](https://make.powerapps.com) and navigate to the **Connections** page from the left-hand navigation.

   :::image type="content" source="media/powerapps_create_connection.png" alt-text="Power Apps Connections page showing New connection button":::


#### Example Create an Office 365 Users connection

Select **+ New connection** and select **Office 365 Users**. Select **Create**.

> [!NOTE]
> If you already have an Office 365 Users connection, you can use that instead of creating a new one.

:::image type="content" source="media/powerapps_create_office_connection.png" alt-text="Create Office 365 Users connection in Power Apps":::

#### (Optional) Create a SQL connection (or a connection for another tabular data source)

> [!TIP]
> For a step-by-step guide to connecting your code app to Azure SQL, see [How to: Connect your code app to Azure SQL](connect-to-azure-sql.md).

### Get connection metadata for all created connections

There are two ways to do this:

- Use the PAC CLI [pac connection list](/power-platform/developer/cli/reference/connection#pac-connection-list) command.
- Get data from the URL in Power Apps.

#### Use PAC CLI

You can use the Power Apps CLI to list your available connections and retrieve their IDs using [pac connection list](/power-platform/developer/cli/reference/connection#pac-connection-list) command.

`pac connection list` displays a table of all your connections, including the **Connection ID** and **API Name**, which is used as the `appId` when adding a data source.

:::image type="content" source="media/pac_cli_connection_list.png" alt-text="PAC CLI list output showing Connection ID and API Name":::

#### Use Power Apps

You can also retrieve this information using Power Apps by viewing the URL when you examine the details of a connection.

:::image type="content" source="media/powerapps_select_connection.png" alt-text="Select a connection in Power Apps to view its details":::

Notice how the API name and connection ID are appended to the URL:

:::image type="content" source="media/powerapps_connection_apiName_connectionId.png" alt-text="Connection details showing API name and Connection ID values":::

Copy the API name and the connection ID from PAC CLI the URL for each connection.

## Add a connection to a code app

After you create or identify existing connections to use, and copied the connection metadata from the previous step, add those connections to the app.

Adding the data sources to the app will automatically generate a typed TypeScript model and service file in the repo. For example, the Office 365 Users data source produces `Office365UsersModel` and `Office365UsersService`.

1. Add a nontabular data source (For example Office 365 Users) to the app using the PAC CLI [pac code add-data-source](/power-platform/developer/cli/reference/code#pac-code-add-data-source) command.

   From a command line, run the following. Use the API name and connection ID collected from previous steps.

   ```powershell
   pac code add-data-source -a <apiName> -c <connectionId>
   ```

   For example:

   ```powershell
   pac code add-data-source -a "shared_office365users" -c "aaaaaaaa000011112222bbbbbbbbbbbb"
   ```

1. (Optional) Add a tabular data source (for example SQL or SharePoint) to the app.

   Use the same PAC CLI [pac code add-data-source](/power-platform/developer/cli/reference/code#pac-code-add-data-source) command, but include a table ID and dataset name. The schema of your tabular data source specifies these values. If you don't already have these, see [Retrieve a dataset name and table ID](#retrieve-a-dataset-name-and-table-id).

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

1. (Optional) Add a SQL stored procedure as a data source

   From a command line, run the following. Use the API name and connection ID collected previously.

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

1. (Optional) If needed, you can delete data sources after adding

   From a command line, run the following. Use the API name and connection ID collected previously.

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
   > If the schema on a connection changes, there's no command to refresh the typed model and service files. Delete the data source and readd it instead.

## Update the app to call connections

Once connections are added, you can update the app to use the generated model and service.

> [!NOTE]
> These changes can also be made via with an IDE's agent. For instance, in Visual Studio Code you might use GitHub Copilot agent mode to make them for you after the data sources are added.

1. Update the app to use the nontabular data source (for example, Office 365 Users)

   You can see the generated files under the src/Models and src/Services folders for the typed connection API.

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

1. (Optional) Update the app to use the tabular data source (for example, SQL)

   You can see the generated files under the `src/Models` and `src/Services` folders for the typed connection API.

   Example

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

1. Run the app locally to verify changes

   ```powershell
   npm run dev
   ```

1. Push the app to run on Power Apps

   ```powershell
   npm run build | pac code push
   ```

## Retrieve a dataset name and table ID

> [!IMPORTANT]
> The following steps to retrieve a dataset name and table ID are a temporary workaround. We plan to add an easier mechanism to get these values.

If you don't already have the table and dataset name, you can get them by running a canvas app and copying the values from the browser network inspector:

1. Create a new canvas app in Studio.
1. Add the connection to a canvas app.
1. Bind the connection to a gallery control.
1. Publish and run the app.
1. Open your browser's **Developer Tools**, go to the **Network** tab, and inspect requests made when the app loads. Check the "invoke" request, and go to its response.
1. Find an Azure API Management (APIM) request with the connection ID, dataset name, and table ID, and copy those values.

Example data request URL through APIM. The bolded sections are the **connection ID**, **dataset name**, and **table ID**.

https[]()://00aa00aa-bb11-cc22-dd33-44ee44ee44ee.01.common.azure-apihub.net/apim/sharepointonline/**11bb11bbcc22dd33ee4455ff55ff55ff**/datasets/**https%253A%252F%252Ftstgeo.sharepoint.com%252Fsites%252FTEST_TST**/tables/**22cc22cc-dd33-ee44-ff55-66aa66aa66aa**/items

| property| example value|
|---|---|
| Connection ID | 11bb11bbcc22dd33ee4455ff55ff55ff|
| Dataset name  |https%253A%252F%252Ftstgeo.sharepoint.com%252Fsites%252FTEST_TST |
| Table ID      | 22cc22cc-dd33-ee44-ff55-66aa66aa66aa|
