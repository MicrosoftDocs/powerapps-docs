---
title: "Tutorial: Write and register a plug-in (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn how to write plug-in code and then register the compiled assembly and step with Dataverse." # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 02/14/2025
ms.reviewer: "pehecke"
ms.topic: tutorial
author: MicroSri
ms.subservice: dataverse-developer
ms.author: sriknair
search.audienceType: 
  - developer
contributors:
  - PHecke
  - marcelbf 

---
# Tutorial: Write and register a plug-in

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]

This tutorial guides you through writing a plug-in and registering it with Microsoft Dataverse. You should first read the [Write a plug-in](write-plug-in.md) article to familiarize yourself with writing a plug-in.

You can find the complete plug-in solution files for this tutorial here: [Sample: Create a basic plug-in](org-service/samples/basic-followup-plugin.md).

## Goal

Create an asynchronous plug-in registered on the "Create" message of the account table. The plug-in creates a task activity that reminds the creator of the account to follow up one week later.

> [!NOTE]
> This goal can be easily achieved using a workflow without writing code. We are using this simple example so that we can focus on the process of creating and deploying a plug-in.

## Prerequisites

- A System User account with the Administrator or System Customizer role in the target Microsoft Dataverse environment.
- A model-driven app that includes the account and task tables.
  - If you don't have a model-driven app that includes these tables, see [Build your first model-driven app from scratch](../../maker/model-driven-apps/build-first-model-driven-app.md) for steps to make one in just a few minutes.
- Visual Studio 2019 (or later version).
- Knowledge of the Visual C# programming language.
- Plug-in Registration tool installed on the development computer. See [Dataverse development tools](download-tools-nuget.md).

## Create a plug-in project

This article demonstrates using Visual Studio to write the plug-in and build the assembly. However, you could use your favorite editor for coding and use MSBuild to build the assembly. In either case, you must use the Plug-in Registration tool to register the plug-in with Dataverse.

Alternately, you can use [Power Platform CLI](/power-platform/developer/cli/reference/plugin-command) to quickly create a new project with boilerplate plug-in code using the command [pac plugin init](/power-platform/developer/cli/reference/plugin#pac-plugin-init). You would still use the Plug-in Registration tool to register the plug-in with Dataverse.

Another alternative is to use the Power Platform Tools extension as described here: [Create and register a plug-in package using Visual Studio](/power-platform/developer/howto/vs-create-plugin). In this case, the extension can create and register the plug-in so the Plug-in Registration Tool isn't needed.

### Create a Visual Studio project for the plug-in

1. Open Visual Studio and open a new **Class Library (.NET Framework)** project using **.NET Framework 4.6.2**

    ![Open a new class library (.NET Framework) project using .NET Framework 4.6.2.](media/tutorial-write-plug-in-create-visual-studio-project.png)

    The name used for the project is also the name of the assembly. This tutorial uses the name `BasicPlugin`.
1. In **Solution Explorer**, right-click the project and select **Manage NuGet Packages…** from the context menu.

    ![Manage NuGet packages.](media/tutorial-write-plug-in-manage-nuget-packages.png)

1. Select **Browse** and search for `Microsoft.CrmSdk.CoreAssemblies` and install the latest version.

    ![Install Microsoft.CrmSdk.CoreAssemblies NuGet Package.](media/tutorial-write-plug-in-install-microsoft.crmsdk.coreassemblies.png)

1. You must select **I Accept** in the **License Acceptance** dialog.

    > [!NOTE]
    > Adding the `Microsoft.CrmSdk.CoreAssemblies` NuGet package will include these assemblies in the build folder for your assembly, but you will not upload these assemblies with the assembly that includes your logic. These assemblies are already present in the sandbox runtime.
    >
    > Ensure only assemblies referenced directly by your project or through NuGet dependency chains are located in your build folder. You cannot include other assemblies when you register the assembly with your logic. You cannot assume that the assemblies other than those included in the  `Microsoft.CrmSdk.CoreAssemblies` NuGet package will be present on the server and compatible with your code.

1. In **Solution Explorer**, right-click the `Class1.cs` file and choose **Rename** in the context menu.

    ![Rename class.](media/tutorial-write-plug-in-rename-class.png)

1. Rename the `Class1.cs` file to `FollowupPlugin.cs`.
1. When prompted, allow Visual Studio to rename the class to match the file name.

    ![Confirm rename dialog.](media/tutorial-write-plug-in-rename-class-confirm.png)

### Edit the class file to define a plug-in

1. Add the following `using` statements to the top of the `FollowupPlugin.cs` file.

    ```csharp
    using System.ServiceModel;  
    using Microsoft.Xrm.Sdk;
    ```

1. Implement the <xref:Microsoft.Xrm.Sdk.IPlugin> interface by editing the class.

    > [!NOTE]
    > If you just type  `: IPlugin` after the class name, Visual Studio will auto-suggest implementing a stub for the **Execute** Method.

    ```csharp
    public class FollowupPlugin : IPlugin
    {
        public void Execute(IServiceProvider serviceProvider)
        {
            throw new NotImplementedException();
        }
    }
    ```

1. Replace the contents of the `Execute` method with the following code.

```csharp
// Obtain the tracing service
ITracingService tracingService =
(ITracingService)serviceProvider.GetService(typeof(ITracingService));

// Obtain the execution context from the service provider.  
IPluginExecutionContext context = (IPluginExecutionContext)
    serviceProvider.GetService(typeof(IPluginExecutionContext));

// The InputParameters collection contains all the data passed in the message request.  
if (context.InputParameters.Contains("Target") &&
    context.InputParameters["Target"] is Entity)
{
    // Obtain the target entity from the input parameters.  
    Entity entity = (Entity)context.InputParameters["Target"];

    // Obtain the IOrganizationService instance which you will need for  
    // web service calls.  
    IOrganizationServiceFactory serviceFactory =
        (IOrganizationServiceFactory)serviceProvider.GetService(typeof(IOrganizationServiceFactory));
    IOrganizationService service = serviceFactory.CreateOrganizationService(context.UserId);

    try
    {
        // Plug-in business logic goes here.  
    }

    catch (FaultException<OrganizationServiceFault> ex)
    {
        throw new InvalidPluginExecutionException("An error occurred in FollowUpPlugin.", ex);
    }

    catch (Exception ex)
    {
        tracingService.Trace("FollowUpPlugin: {0}", ex.ToString());
        throw;
    }
}
```

### About the code

- The <xref:Microsoft.Xrm.Sdk.ITracingService> enables writing to the tracing log.  You can see an example in the final catch block. More information: [Use tracing](debug-plug-in.md#use-tracing)
- The <xref:Microsoft.Xrm.Sdk.IPluginExecutionContext> provides access to the context for the event that executed the plugin.  More information: [Understand the execution context](understand-the-data-context.md).
- The code verifies that the context <xref:Microsoft.Xrm.Sdk.IExecutionContext.InputParameters> includes the expected parameters for the <xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> that this plug-in is to be registered for. If the <xref:Microsoft.Xrm.Sdk.Messages.CreateRequest.Target> property is present, the <xref:Microsoft.Xrm.Sdk.Entity> that was passed to the request is made available.
- The <xref:Microsoft.Xrm.Sdk.IOrganizationServiceFactory> interface provides access to a service variable that implements the <xref:Microsoft.Xrm.Sdk.IOrganizationService> interface, which provides the methods you'll use to interact with the service to create the task.

## Add business logic

The plug-in creates a task activity that reminds the creator of the account to follow up one week later.

Add the following code to the try block. Replace the comment `// Plug-in business logic goes here` with the following code.

```csharp
// Create a task activity to follow up with the account customer in 7 days. 
Entity followup = new Entity("task");

followup["subject"] = "Send e-mail to the new customer.";
followup["description"] =
    "Follow up with the customer. Check if there are any new issues that need resolution.";
followup["scheduledstart"] = DateTime.Now.AddDays(7);
followup["scheduledend"] = DateTime.Now.AddDays(7);
followup["category"] = context.PrimaryEntityName;

// Refer to the account in the task activity.
if (context.OutputParameters.Contains("id"))
{
    Guid regardingobjectid = new Guid(context.OutputParameters["id"].ToString());
    string regardingobjectidType = "account";

    followup["regardingobjectid"] =
    new EntityReference(regardingobjectidType, regardingobjectid);
}

// Create the task in Microsoft Dynamics CRM.
tracingService.Trace("FollowupPlugin: Creating the task activity.");
service.Create(followup);
```

### About the code

- This code uses the late-bound style to create a task and associate it with the account being created. More information: [Create tables using the SDK for .NET](org-service/entity-operations-create.md)
- Early bound classes can be used, but their use requires generating the classes for the tables and including the file defining those classes with the assembly project. Use of early-bound classes is mostly a personal preference, so those steps are left out of this tutorial for brevity. More information: [Late-bound and early-bound programming using the SDK for .NET](org-service/early-bound-programming.md)
- The <xref:Microsoft.Xrm.Sdk.Entity.Id> of the account being created is found in the context <xref:Microsoft.Xrm.Sdk.IExecutionContext.OutputParameters> and set as the `regardingobjectid` lookup column for the task.

## Build plug-in

In Visual Studio, press **F6** to build the assembly. Verify that it compiles without error.

## Sign the plug-in

1. In **Solution Explorer**, right-click the **BasicPlugin** project and in the context menu select **Properties**.

    ![Open project properties.](media/tutorial-write-plug-in-project-properties.png)

1. In the project properties, select the **Signing** tab and select the **Sign the assembly** checkbox.

    ![Sign the assembly.](media/tutorial-write-plug-in-sign-assembly.png)

1. In the **Choose a strong name key file**: dropdown, select **<New…>**.
1. In the **Create Strong Name Key** dialog, enter a **key file name**, and deselect the **Protect my key file with a password** checkbox.
1. Select **OK** to close the **Create Strong Name Key** dialog.
1. In the project properties **Build** tab, verify that the **Configuration** is set to **Debug**.
1. Press **F6** to build the plug-in again.
1. Using windows explorer, find the built plug-in at: `\bin\Debug\BasicPlugin.dll`.

> [!NOTE]
> Build the assembly using **Debug** configuration because you will use the Plug-in Profiler to debug it in a later tutorial. Before you include a plug-in with your solution, you should build it using the release configuration.

## Register plug-in

To register a plug-in, you'll need the Plug-in Registration tool.

[!INCLUDE [cc-connect-plugin-registration-tool](includes/cc-connect-plugin-registration-tool.md)]

### Register your assembly

1. In the **Register** drop-down, select **New Assembly**.

    ![Register new assembly.](media/tutorial-write-plug-in-register-new-assembly.png)

1. In the **Register New Assembly** dialog, select the ellipses (**…**) button and browse to the assembly you built in the previous step.

    ![Register new assembly dialog.](media/tutorial-write-plug-in-register-new-assembly-dialog.png)

1. For Microsoft 365 users, verify that the **isolation mode** is set to **sandbox** and the **location** to store the assembly is **Database**.

    > [!NOTE]
    > Other options for **isolation mode** and **location** apply to on-premises Dynamics 365 deployments. For the location, you can specify the D365 server's database, the server's local storage (disk), or the server's Global Assembly Cache. For more information, see [Plug-in storage](/dynamics365/customer-engagement/developer/register-deploy-plugins#plug-in-storage).

1. Click **Register Selected Plug-ins**.
1. You'll see a **Registered Plug-ins** confirmation dialog.

    ![Registerd plug-ins confirmation dialog.](media/tutorial-write-plug-in-register-new-assembly-dialog-confirm.png)

1. Select **OK** to close the dialog and close the **Register New Assembly** dialog.
1. You should now see the **(Assembly) BasicPlugin** assembly, which you can expand to view the **(Plugin) BasicPlugin.FollowUpPlugin** plugin.

    ![(Plugin) BasicPlugin.FollowUpPlugin plugin.](media/tutorial-write-plug-in-basic-followupplugin-plugin.png)

### Register a new step

1. Right-click the **(Plugin) BasicPlugin.FollowUpPlugin** and select **Register New Step**.

    ![Register a new step.](media/tutorial-write-plug-in-register-new-step.png)

1. In the **Register New Step** dialog, set the following fields.

    |Setting|Value|
    |--|--|
    |Message|Create|
    |Primary Entity|account|
    |Event Pipeline Stage of Execution|PostOperation|
    |Execution Mode|Asynchronous|

    ![Entering relevant step data.](media/tutorial-write-plug-in-register-new-step-dialog.png)

1. Select **Register New Step** to complete the registration and close the **Register New Step** dialog.
1. You can now see the registered step.

    ![View the registered step.](media/tutorial-write-plug-in-view-registered-step.png)

> [!NOTE]
> At this point the assembly and steps are part of the system **Default Solution**. When creating a production plug-in, you would add them to the unmanaged solution that you will distribute. These steps are not included in this tutorial. For more information, see [Add your assembly to a solution](register-plug-in.md#add-your-assembly-to-a-solution) and [Add step to solution](register-plug-in.md#add-a-step-to-a-solution) .

## Test plug-in

1. Open a model-driven app and create an account table.
1. Within a short time, open the account and you can verify the creation of the task.

    ![Account table record with related task activity create by plug-in.](media/tutorial-write-plug-in-test-plugin-in-model-app.png)

### What if the task wasn't created?

Because we are working with an asynchronous plug-in, the operation to create the task occurs after the account is created. Usually, the task creation happens immediately, but if it doesn't you may still be able to view the system job in the queue waiting to be applied. This step registration used the **Delete AsyncOperation if StatusCode = Successful** option, which is a best practice. This means as soon as the system job completes successfully, you'll not be able to view the system job data unless you re-register the plug-in with the **Delete AsyncOperation if StatusCode = Successful** option unselected.

However, if there was an error, you can view the system job to see the error message.

## View System jobs

Use the **Dynamics 365 --custom** app to view system jobs.

1. In your model-driven app, navigate to the app.

    ![view the dynamics 365 custom app.](media/dynamics-365-custom-app.png)

1. In the **Dynamics 365 --custom** app, navigate to **Settings** > **System** > **System Jobs**.

    ![navigate to system jobs.](media/navigate-system-jobs.png)

1. When viewing system jobs, you can filter by **Table (Entity)**. Select **Account**.

    ![Filter on accounts.](media/system-jobs-filter-entity-account.png)

1. If the job failed, you should see a record with the name **BasicPlugin.FollowupPlugin: Create of account**.

    ![Failed system job.](media/failed-system-job.png)

1. If you open the system job, you can expand the **Details** section to view the information written to the trace and details about the error.

    ![system job details.](media/system-job-failed-plug-in.png)

### Query System jobs

You can use the following Web API query to return failed system jobs for asynchronous plug-ins.

```
GET <your org uri>/api/data/v9.0/asyncoperations?$filter=operationtype eq 1 and statuscode eq 31&$select=name,message
```

More information: [Query data using the Web API](webapi/query/overview.md)

Or use the following FetchXml:

```xml
<fetch top='50' >
  <entity name='asyncoperation' >
    <attribute name='message' />
    <attribute name='name' />
    <filter type='and' >
      <condition attribute='operationtype' operator='eq' value='1' />
      <condition attribute='statuscode' operator='eq' value='31' />
    </filter>
  </entity>
</fetch>
```

More information: [Use FetchXML with FetchExpression](org-service/entity-operations-query-data.md)

## View trace logs

The sample code wrote a message to the trace log. These next steps describe how to view the logs.

By default, plug-in trace logs aren't enabled.

> [!TIP]
> IF you prefer to change this setting in code:
> This setting is in the [Organization table PluginTraceLogSetting column](reference/entities/organization.md#BKMK_PluginTraceLogSetting).
>
> The valid values are:
>
> |Value|Label|
> |--|--|
> |0|Off|
> |1|Exception|
> |2|All|

Use the following steps to enable them in a model-driven app.

1. Open the Dynamics 365 - custom  app.

    ![Open the Dynamics 365 - custom  app.](media/tutorial-write-plug-in-open-dynamics365-custom-app.png)

1. Navigate to **Settings** > **System** > **Administration**.

    ![navigate to administration.](media/tutorial-write-plug-in-navigate-administration.png)

1. In **Administration**, select **System Settings**.
1. In the **System Settings** dialog, in the customization tab, set **Enable logging to plug-in trace log** to **All**.

    ![System Settings Customization tab.](media/tutorial-write-plug-in-system-settings-customization-tab.png)

    > [!NOTE]
    > You should disable logging after you are finished testing your plug-in, or at least set it to **Exception** rather than **All**.

1. Select **OK** to close the **System Settings** dialog.
1. Repeat the steps to test your plug-in by creating a new account.
1. In the **Dynamics 365 -- custom app**, navigate to **Settings** > **Customization** > **Plug-In Trace Log**.
1. You should find that a new plug-in trace Log record is created.

    ![Plug-in trace log record.](media/tutorial-write-plug-in-plug-in-trace-log.png)

1. If you open the record you might expect that it would include the information you set in your trace, but it doesn't. It only verifies that the trace occurred.
1. To see the details, it's easier to query this data using the Web API in your browser using the following query with the <xref href="Microsoft.Dynamics.CRM.plugintracelog?text=plugintracelog EntityType" />, using the `typename` property to filter results in the `messageblock` property based on the name of the plug-in class.

    `GET <your org uri>/api/data/v9.0/plugintracelogs?$select=messageblock&$filter=typename eq 'BasicPlugin.FollowUpPlugin'`

1. You can expect to see this JSON formatted information returned with the Web API query.

    ```json
    {
        "@odata.context": "<your org uri>/api/data/v9.0/$metadata#plugintracelogs(messageblock)",
        "value": [{
            "messageblock": "FollowupPlugin: Creating the task activity.",
            "plugintracelogid": "f0c221d1-7f84-4f89-acdb-bbf8f7ce9f6c"
        }]
    }
    ```

## Next steps

In this tutorial, you created a simple plug-in and registered it. Complete [Tutorial: Debug a plug-in](tutorial-debug-plug-in.md) to learn how to debug this plug-in.

### See also

[Tutorial: Update a plug-in](tutorial-update-plug-in.md)  
[Write a plug-in](write-plug-in.md)  
[Register a plug-in](register-plug-in.md)  
[Debug Plug-ins.](debug-plug-in.md)  

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
