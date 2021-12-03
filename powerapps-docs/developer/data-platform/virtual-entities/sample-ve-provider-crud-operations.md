---
title: "Sample: Custom virtual table provider with CRUD operations (Microsoft Dataverse) | Microsoft Docs"
description: "Sample demonstrates how to implement a generic custom virtual table that supports CRUD operations.."
ms.date: 04/09/2021
ms.reviewer: "nabuthuk"
ms.service: powerapps
ms.topic: "samples"
ms.assetid: d329dade-16c5-46e9-8dec-4b8efb996d24
author: "Nkrb" # GitHub ID
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Sample: Custom virtual table provider with CRUD operations

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

This sample shows how to implement a custom data provider to create a virtual table that supports create, retrieve, update, and delete operations. For each of these operations, you implement a generic plug-in, register them using the Plugin Registration Tool, and enable virtual table data sources to create the virtual table.

To learn more about data providers and plug-in development, see [Custom data providers](./custom-ve-data-providers.md)

## Data source details

In this walkthrough, you will set up a simple table in an external SQL Server to create a virtual table. The table name used in this example is **VETicket**.

> [!NOTE]
> Update your plug-in code, if you wish to change the name of the table or column(s).

| Column Name | Data Type                      | Purpose                       |
|-------------|--------------------------------|-------------------------------|
| TicketID    | Unique Identified, Primary Key | Primary key for the table.   |
| Severity    | Integer                        | Severity value for the ticket. |
| Name        | String                         | Description of the ticket.     |

There are four steps to enable a custom data provider to create a virtual table.

[Step 1: Implementing CRUD plug-ins and registering the assembly](#step-1-implementing-crud-plug-ins-and-registering-the-assembly)

[Step 2: Creating  data provider and adding plug-ins to the provider](#step-2-creating-data-provider-and-adding-plug-ins-to-the-provider)

[Step 3: Creating a virtual table in Dataverse environment](#step-3-creating-a-virtual-table-in-dataverse-environment)

[Step 4: Create, update, view, and delete records using a virtual table](#step-4-create-update-view-and-delete-records-using-a-virtual-table)

## Step 1: Implementing CRUD plug-ins and registering the assembly


1. Create your plug-in project and install the following NuGet packages. The solution in this example is named **StubProvider**.

   |Assembly                                         |  URL |
   |-------------------------------------------------|-------|
   | Microsoft.CrmSdk.CoreAssemblies                 | https://www.nuget.org/packages/Microsoft.CrmSdk.CoreAssemblies  |
   | Microsoft.CrmSdk.Data                           | https://www.nuget.org/packages/Microsoft.CrmSdk.Data            |
   | Microsoft.CrmSdk.Deployment                     | https://www.nuget.org/packages/Microsoft.CrmSdk.Deployment      |
   | Microsoft.CrmSdk.Workflow                       | https://www.nuget.org/packages/Microsoft.CrmSdk.Workflow        |
   | Microsoft.CrmSdk.XrmTooling.CoreAssembly        | https://www.nuget.org/packages/Microsoft.CrmSdk.XrmTooling.CoreAssembly   |
   | Microsoft.IdentityModel.Clients.ActiveDirectory | https://www.nuget.org/packages/Microsoft.IdentityModel.Clients.ActiveDirectory |
   | Microsoft.Rest.ClientRuntime                    | https://www.nuget.org/packages/Microsoft.Rest.ClientRuntime                    |
   | Newtonsoft.Json                                 | https://www.nuget.org/packages/Newtonsoft.Json/13.0.1-beta2    |
   |||

1. Add the following six class files to your solution. In each of the class files, add the following using statements

    ```csharp
    using System; 
    using System.Collections.Generic; 
    using System.Data.SqlClient; 
    using System.Linq; using System.Text; 
    using System.Threading.Tasks; 
    using Microsoft.Xrm.Sdk; 
    using Microsoft.Xrm.Sdk.Extensions; 
    using Microsoft.Xrm.Sdk.Data.Exceptions; 
    using Newtonsoft.Json; 
    ```

    > [!NOTE]
    > In each of these class files, update the table name to match the source table name you have setup. The example uses **VETicket** as the source table name.

    | Class file name    | Purpose          |
    |------------|------------------------------------|
    | **Connection.cs**   | This class contains code for creating and managing connection to the external SQL data source. It includes connection string parameters specific to the external database and SQL-based authentication information required to establish the connection. Replace the values respective to your: Database server, UserID, Password, and table name that you will be creating a virtual table in Dataverse. |
    | **CreatePlugin.cs**  | This class contains code that handles the create operation for the virtual table. |
    | **UpdatePlugin.cs**  | This class contains code that handles updating records in the virtual table.  |
    | **RetrievePlugin.cs**  | This class contains code that retrieves a specific record from the virtual table. |
    | **RetrieveMultiplePlugin.cs**  | This class contains code for fetching multiple records from the virtual table.  |
    | **DeletePlugin.cs**  | This class contains code that allows you to delete a record in the virtual table.|
    |||

     #### Code for Connection.cs   

     ```csharp
      public static class Connection
    {
        public static SqlConnection GetConnection()
        {
            try
            {
                //sample database to connect to 
                SqlConnectionStringBuilder builder = new SqlConnectionStringBuilder();
                builder.DataSource = "Enter name or network address of the SQL Server";
                builder.UserID = "Enter User Name";
                builder.Password = "Enter password";
                builder.InitialCatalog = "Enter database details";
                SqlConnection connection = new SqlConnection(builder.ConnectionString);
                return connection;
            }
            catch (SqlException e)
            {
                Console.WriteLine(e.ToString());
                throw;
            }
        }
    }
     ```

    #### Code for CreatePlugin.cs  

    ```csharp
    public class CreatePlugin : IPlugin
    {
        public void Execute(IServiceProvider serviceProvider)
        {
            var context = serviceProvider.Get<IPluginExecutionContext>();
            if (context.InputParameters.Contains("Target") && context.InputParameters["Target"] is Entity)
            {
                Entity entity = (Entity)context.InputParameters["Target"];
                Guid id = Guid.NewGuid();
                //change the table name below to the source table name you have created 
                string cmdString = "INSERT INTO VETicket (TicketID,Name,Severity) VALUES (@TicketID, @Name, @Severity)";
                SqlConnection connection = Connection.GetConnection();
                using (SqlCommand command = connection.CreateCommand())
                {
                    command.CommandText = cmdString;
                    command.Parameters.AddWithValue("@TicketID", id);
                    command.Parameters.AddWithValue("@Name", entity["new_name"]);
                    command.Parameters.AddWithValue("@Severity", entity["new_severity"]);
                    connection.Open();
                    try
                    {
                        var numRecords = command.ExecuteNonQuery();
                        Console.WriteLine("inserted {0} records", numRecords);
                    }
                    finally
                    {
                        connection.Close();
                    }
                    // other codes. 
                }
                context.OutputParameters["id"] = id;
            }
        }
    }
    ```
    #### Code for UpdatePlugin.cs 

    ```csharp
    public class UpdatePlugin: IPlugin {
        public void Execute(IServiceProvider serviceProvider)
        {
            var context = serviceProvider.Get<IPluginExecutionContext>();
            Guid id = Guid.Empty;
            if (context.InputParameters.Contains("Target") && context.InputParameters["Target"] is Entity)
            {
                Entity entity = (Entity)context.InputParameters["Target"];
                //change the table name below to the source table name you have created  
                string cmdString = "UPDATE VETicket SET {0} WHERE TicketID=@TicketID";
                SqlConnection connection = Connection.GetConnection();
                using (SqlCommand command = connection.CreateCommand())
                {
                    command.Parameters.AddWithValue("@TicketID", entity["new_ticketid"]);
                    List<string> setList = new List<string>();
                    if (entity.Attributes.Contains("new_name"))
                    {
                        command.Parameters.AddWithValue("@Name", entity["new_name"]);
                        setList.Add("Name=@Name");
                    }
                    if (entity.Attributes.Contains("new_severity"))
                    {
                        command.Parameters.AddWithValue("@Severity", entity["new_severity"]);
                        setList.Add("Severity=@Severity");
                    }
                    command.CommandText = string.Format(cmdString, string.Join(",", setList)); connection.Open();
                    try
                    {
                        var numRecords = command.ExecuteNonQuery();
                        Console.WriteLine("updated {0} records", numRecords);
                    }
                    finally
                    {
                        connection.Close();
                    }
                    // other codes. 
                }
            }
        }
    }
    ```

    #### Code for RetrievePlugin.cs  

    ```csharp
    public class RetrievePlugin : IPlugin
    {
        public void Execute(IServiceProvider serviceProvider)
        {
            var context = serviceProvider.Get<IPluginExecutionContext>();
            Guid id = Guid.Empty;
            if (context.InputParameters.Contains("Target") && context.InputParameters["Target"] is EntityReference)
            {
                EntityReference entityRef = (EntityReference)context.InputParameters["Target"];
                Entity e = new Entity("new_ticket");
                //change the table name below to the source table name you have created  
                string cmdString = "SELECT TicketID, Severity, Name FROM VETicket WHERE TicketID=@TicketID";
                SqlConnection connection = Connection.GetConnection();
                using (SqlCommand command = connection.CreateCommand())
                {
                    command.CommandText = cmdString;
                    command.Parameters.AddWithValue("@TicketID", entityRef.Id);
                    connection.Open();
                    try
                    {
                        using (SqlDataReader reader = command.ExecuteReader())
                        {
                            if (reader.Read())
                            {
                                e.Attributes.Add("new_ticketid", reader.GetGuid(0));
                                e.Attributes.Add("new_severity", reader.GetInt32(1));
                                e.Attributes.Add("new_name", reader.GetString(2));
                            }
                        }
                    }
                    finally
                    {
                        connection.Close();
                    }
                    // other codes. 
                }
                context.OutputParameters["BusinessEntity"] = e;
            }
        }
    }
    ```
    #### Code for RetrieveMultiplePlugin.cs 

    ```csharp
    public class RetrieveMultiplePlugin : IPlugin
    {
        public void Execute(IServiceProvider serviceProvider)
        {
            var context = serviceProvider.Get<IPluginExecutionContext>();
            EntityCollection collection = new EntityCollection();
            //change the table name below to the source table name you have created  
            string cmdString = "SELECT TicketID, Severity, Name FROM VETicket";
            SqlConnection connection = Connection.GetConnection();
            using (SqlCommand command = connection.CreateCommand())
            {
                command.CommandText = cmdString;
                connection.Open();
                try
                {
                    using (SqlDataReader reader = command.ExecuteReader())
                    {
                        while (reader.Read())
                        {
                            Entity e = new Entity("new_ticket");
                            e.Attributes.Add("new_ticketid", reader.GetGuid(0));
                            e.Attributes.Add("new_severity", reader.GetInt32(1));
                            e.Attributes.Add("new_name", reader.GetString(2));
                            collection.Entities.Add(e);
                        }
                    }
                }
                finally
                {
                    connection.Close();
                }
                context.OutputParameters["BusinessEntityCollection"] = collection;
            }
        }
    }
    ```

    #### Code for DeletePlugin.cs 

    ```csharp
    public class DeletePlugin : IPlugin
    {
        public void Execute(IServiceProvider serviceProvider)
        {
            var context = serviceProvider.Get<IPluginExecutionContext>();
            //comment 
            Guid id = Guid.Empty;
            if (context.InputParameters.Contains("Target") && context.InputParameters["Target"] is EntityReference)
            {
                EntityReference entityRef = (EntityReference)context.InputParameters["Target"];
                id = entityRef.Id;
                //change the table name below to the source table name you have created 
                string cmdString = "DELETE VETicket WHERE TicketID=@TicketID";
                SqlConnection connection = Connection.GetConnection();
                using (SqlCommand command = connection.CreateCommand())
                {
                    command.CommandText = cmdString; command.Parameters.AddWithValue("@TicketID", id);
                    connection.Open();
                    try
                    {
                        var numRecords = command.ExecuteNonQuery();
                        Console.WriteLine("deleted {0} records", numRecords);
                    }
                    finally
                    {
                        connection.Close();
                    }
                    // other codes. 
                }
            }
        }
    }
    ```

1. Compile and build the solution. You will now have an assembly file (.dll) that you can use to register in your Dataverse environment. You will find this file in the  ***solution folder/bin/Debug*** directory.

    > [!div class="mx-imgBorder"]
    > ![Assembly dll.](../media/custom-ve-assembly-dll.png "Assembly dll")

1. Register the assembly using the Plugin Registration Tool. You can get the latest Plugin Registration Tool package from [NuGet](https://www.nuget.org/packages/Microsoft.CrmSdk.XrmTooling.PluginRegistrationTool).

1. Open the Plugin Registration Tool. You need to have system administration privileges to register the assembly.Select **CREATE NEW CONNECTION** to connect to your Dataverse environment. Select the **Register** drop-down  and then select **Register New Assembly**.

   > [!div class="mx-imgBorder"]
   > ![Register new step.](../media/custom-ve-register-plugin-step.png "Register new step")

1. Select the assembly file and register the plug-ins. Make sure that you have selected all the plug-ins (Create, Update, Delete, Retrieve, and RetrieveMultiple plug-ins).

    > [!div class="mx-imgBorder"]
    > ![Register new assembly.](../media/custom-ve-register-assembly-step.png "Register new assembly")

## Step 2: Creating data provider and adding plug-ins to the provider

1. Select the **Register** drop-down and then select **Register New Data Provider**.

1. In the **Register New Data Provider** dialog, enter the following details:

    1. Enter **Data Provider Name**.

    2. In the **Solutions** option, select an existing solution or create a new solution in the drop-down. If you want to create a new solution, select the **NewSolution** option from the drop-down. In the **Create New Solution** dialog, enter the required details and select **Save**. 

    3. In the **Data Source Table (Entity)** option, select **Create New Data Source**. Enter the details. Make sure that the data source is part of the solution you created or selected.

        > [!NOTE]
        > The data source table in Dataverse holds the configuration data for a data source record to be passed to the provider plug-ins.

    4. Map each of the registered plug-in to its respective operations.

    5. Register the new data provider.

        > [!div class="mx-imgBorder"]
        > ![Register data provider.](../media/custom-ve-register-new-data-provider.png "Register data provider")

1. In the Plugin Registration Tool, you'll see the new data source record and the associated data provider. Selecting the data source will display the details which include the plug-ins and their registered GUID.

    > [!div class="mx-imgBorder"]
    > ![Registered data provider.](../media/custom-ve-registered-data-provider.png "Registered data provider")

## Step 3: Creating a virtual table in Dataverse environment

1. Create a new virtual table data source by navigating to **Setting** > **Administration** > **Virtual Table (Entity) Data Sources**.

2. Select **New** and then select the data provider you created in the previous step from the drop-down.

3. Enter a name for the data source and select **Save and Close**.

4. You are now ready to create the virtual table that represents the external data source. To do this, go to **Settings** > **Customize the System**.

5. In the left navigation pane of solution explorer, Select **Tables (Entities)**, and then select **New**.

6. Enter the following details:

    | Column                     | Description                                                                                     |
    |---------------------------|-------------------------------------------------------------------------------------------|
    | Data Source               | Select the data source you created in the previous step.                                          |
    | Display Name              | Virtual table name.                                                                        |
    | Plural Name               | The value will be automatically populated based on the display name.                       |
    | Name                      | This will also be created automatically based on the value you enter for the display name. |
    | External Name             | The name of the source table.                                                              |
    | External Collections Name | You can use the same value from the plural name column.                                     |

7. Select **Save and Close.**

    > [!div class="mx-imgBorder"]
    > ![Create new record.](../media/custom-ve-create-new-record.png "Create new record")

8. In the left navigation pane, select and expand on the virtual table you created.

9. Select **Fields** to update and create new columns representing the external source.

10. Select the **Primary Key** column for the virtual table and select **Edit**.

11. Update the **External Name** column to match the column name in your external data source. In this example, the external column name is **TicketID**.

    > [!div class="mx-imgBorder"]
    > ![Create new table.](../media/custom-ve-create-new-entity.png "Create new table")

12. Select **Save and Close**.

13. Select the **Name** field for the virtual table and select **Edit**.

14. Update the **External Name** field to match the field name in your external data source. In this example, the external column name is **Name**.

    > [!div class="mx-imgBorder"]
    > ![Create new name field.](../media/custom-ve-create-new-name-field.png "Create new name field")

15. Select **Save and Close**.

16. Select **New** to create a new column in the virtual table. This column will represent the severity column in the external data source.

17. Enter the following information for the new columns:

    | Column Name        | Value             |
    |-------------------|-------------------|
    | Display Name      | Severity          |
    | Name              | new_severity      |
    | External Name     | Severity          |
    | Field Requirement | Business Required |
    | Data Type         | Whole Number      |

    > [!div class="mx-imgBorder"]
    > ![Create new severity field.](../media/custom-ve-create-new-severity-field.png "Create new severity field")

18. Select **Save and Close**.

## Step 4: Create, update, view, and delete records using a virtual table

Create a model-driven app and add the virtual table to the site map. Then select the virtual table main form and the Advanced field view. Publish the app. More information: [Build your first model-driven app from scratch](../../../maker/model-driven-apps/build-first-model-driven-app.md?branch=matp-2190993)

> [!div class="mx-imgBorder"]
> ![Create model-driven app.](../media/custom-ve-create-new-model-driven-app.png "Create model-driven app")

Application users can perform read, create, update, delete operations using the virtual table just like any other table in Microsoft Dataverse.

### See also

[Getting started with virtual tables](./get-started-ve.md)<br/>
[API considerations for virtual tables](./api-considerations-ve.md)<br/>
[Custom virtual table data providers](./custom-ve-data-providers.md)<br/>
[Virtual table walkthrough using OData v4 Data Provider](../../../maker/data-platform/virtual-entity-walkthrough-using-odata-provider.md)