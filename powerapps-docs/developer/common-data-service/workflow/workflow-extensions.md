---
title: "Workflow Extensions (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "You can extend the options available within the designer for workflows. These extensions are added by adding an assembly that contains a class the extends the CodeActivity class. These extensions are commonly called workflow assemblies or workflow activities." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 10/28/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "JimDaly" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Workflow extensions

You can extend the options available within the designer for workflows used in Common Data Service for Apps. These extensions are added by adding an assembly that contains a class the extends the [CodeActivity](/dotnet/api/system.activities.codeactivity) class. These extensions are commonly called workflow assemblies or workflow activities.

You can use these custom extensions within the designer used for workflows, custom actions, and dialogs.

> [!IMPORTANT]
> Whenever possible, you should first consider applying one of the several declarative options to define business logic. More information: [Apply business logic in Common Data Service for Apps](../../../maker/common-data-service/cds-processes.md)<br/><br/>
> Use workflow extensions when a declarative process doesn’t meet your requirement.

## When to create a workflow extension

If you don’t find the functionality you require using the default process activities, you can add custom activities so that they are available in the editor used to compose workflow, dialog, and action processes.

By default, these processes include a common set of activities you can perform as shown in the following table:

|Activity|Workflow|Action|Dialog|
|--|--|--|--|
|Query Data|||X|
|Assign Value||X|X|
|Create Record|X|X|X|
|Update Record|X|X|X|
|Assign Record|X|X|X|
|Send Email|X|X|X|
|Start Child Workflow|X|X|X|
|Perform Action|X|X||
|Link Child Dialog|||X|
|Change Status|X|X|X|
|Stop Workflow|X|X||
|Stop Dialog|||X|

You can use the **Perform Action** activity to execute any custom actions or the following system messages called **Command Actions**:

||||
|--|--|--|
|AddToQueue|AddUserToRecordTeam|RemoveUserFromRecordTeam|
|SetProcess|SetWordTemplate||

If you have Dynamics 365 Customer Engagement Sales or Service solutions, you can find other command actions depending on the solution:

||||
|--|--|--|
|ApplyRoutingRule|CalculateActualValue|CloseOpportunity|
|GetQuoteProductsFromOpportunity|GetSalesOrderProductsFromOpportunity|LockInvoicePricing|
|LockSalesOrderPricing|QualifyLead|RemoveUserFromRecordTeam|
|ResolveIncident|ResolveQuote|Revise|
|UnlockInvoicePricing|UnlockSalesOrderPricing|

More information: 

- [Configure workflow stages and steps](/flow/configure-workflow-steps)
- [Use CDS for Apps dialogs for guided processes](/flow/use-cds-for-apps-dialogs)
- [Create a custom action](/flow/create-actions)



## Technology used

Because processes use Windows Workflow foundation, you can register an assembly built using the [.NET Framework Activity library](/dotnet/framework/windows-workflow-foundation/net-framework-4-5-built-in-activity-library) that defines custom activities that will appear within the web application editor and will be invoked when the process runs.

Custom workflow activities require creating a .NET Framework assembly that includes one or more classes that are derived from the abstract [CodeActivity Class](/dotnet/api/system.activities.codeactivity?view=netframework-4.5.2). This class provides the [Execute(CodeActivityContext) Method](/dotnet/api/system.activities.codeactivity.execute?view=netframework-4.5.2) called by the CDS for Apps platform when the activity is executed. Each class in your assembly will define a specific activity.

Workflow activities can also define input and output parameters which are visible in the process designer and enable someone to pass data into the workflow activity and receive the processed output. When you write the class you will add properties for these parameters and annotate them with [.NET attributes](/dotnet/standard/attributes/index) to provide the metadata that CDS for Apps will use to expose your custom workflow activity with any parameters in the designer.

## Visual Studio requirements

To create custom workflow activities, you must install Visual Studio with the **.NET desktop development** workload and the **Windows Workflow Foundation** individual component.

You can use the free Visual Studio 2017 Community edition or the Professional and Enterprise editions.

To verify installation or to add this component:

1. Open Visual Studio 2017
1. Select **Tools** > **Get Tools and Features…** . This will open the Visual Studio Installer
1. In the **Workloads** tab, ensure that **.NET desktop development** workload is selected.
    ![Required Visual Studio workloads](media/visual-studio-workloads-workflow-extensions.png)
1. Select **Individual Components** and scroll down to the **Development activities** section.
    ![Required visual studio individual components](media/visual-studio-individual-components-workflow-extensions.png)
1. If **Windows Workflow Foundation** is not selected, select it. The **Windows Communication Foundation** component will be included as well.
1. If you added new workloads or components, click **Modify** to allow the Visual Studio Installer to install it. Otherwise, close Visual Studio Installer.

More information: [Install Visual Studio 2017](/visualstudio/install/install-visual-studio)

## Create a custom workflow activity assembly

These are general steps used to create a custom workflow activity using Visual Studio. For a complete step-by-step example see [Tutorial: Create workflow extension ](tutorial-create-workflow-extension.md).

1. Create a Workflow Activity Library project using .NET Framework 4.5.2 as the target framework
1. Delete the Activity1.xaml file generated with the project
1. Install the [Microsoft.CrmSdk.Workflow](https://www.nuget.org/packages/Microsoft.CrmSdk.Workflow/) NuGet package.

    This package includes the [Microsoft.CrmSdk.CoreAssemblies](https://www.nuget.org/packages/Microsoft.CrmSdk.CoreAssemblies/) package.

1. (Optional) If you wish to use early bound entity classes, include them in the project.

    More information: 

    - [Late-bound and Early-bound programming using the Organization service](../org-service/early-bound-programming.md)
    - [Generate early-bound classes for the Organization service](../org-service/generate-early-bound-classes.md) 

1. Add a public class. The name of the class should correspond with the action to be performed by the activity.
1. Add the following using directives

    ```csharp
    using System.Activities;
    using Microsoft.Xrm.Sdk;
    using Microsoft.Xrm.Sdk.Workflow;
    ```

1. Add properties to the class to represent any input or output parameters and use [.NET attributes](/dotnet/standard/attributes/index) to provide necessary metadata to expose these properties to the workflow process designer.

    More information: [Add parameters](#add-parameters)

1. Make your class derive from the [CodeActivity Class](/dotnet/api/system.activities.codeactivity?view=netframework-4.5.2) and implement the [Execute(CodeActivityContext) Method](/dotnet/api/system.activities.codeactivity.execute?view=netframework-4.5.2) that contains the operations your activity will perform.

    More information: [Add your code to the Execute method](#add-your-code-to-the-execute-method)

1. Sign your assembly
1. Build your assembly.
1. Register your assembly using the Plug-in Registration tool and set the Name and WorkflowActivityGroupName properties to define the text that will be visible in the Dyn365CE process designer.

    More information: [Register your assembly](#register-your-assembly)

1. Test your workflow activity by invoking it from within a Workflow, dialog, or action processes
1. (Recommended) Add your workflow activity to a solution.

## Add parameters

When you define parameters for your class you must define them as [InArgument<T>](/dotnet/api/system.activities.inargument-1), [OutArgument<T>](/dotnet/api/system.activities.outargument-1), or [InOutArgument<T>](/dotnet/api/system.activities.inoutargument-1) types. These types provide methods inherited from a common [Argument Class](/dotnet/api/system.activities.argument) to Get or Set the parameters. Your code will use these methods in the Execute method. More information: [Add your code to the Execute method](#add-your-code-to-the-execute-method)

When your custom workflow activity uses input or output parameters you must add appropriate .NET Attributes to the public class properties that define them. This data will be read by the process designer to define how the parameters can be set in the process designer.

You can use the following types of properties as input or output parameters:

||||
|--|--|--|
|[bool](/dotnet/api/system.boolean)|[DateTime](/dotnet/api/system.datetime)|[Decimal](/dotnet/api/system.decimal)|
|[Double](/dotnet/api/system.double)|<xref:Microsoft.Xrm.Sdk.EntityReference>|[int](/dotnet/api/system.int32)|
|<xref:Microsoft.Xrm.Sdk.Money>|<xref:Microsoft.Xrm.Sdk.OptionSetValue>|[string](/dotnet/api/system.string)|

### Input and Output parameters

To define the text to display for an input or output parameter in the process designer, you will use the following pattern using [.NET Attributes](/dotnet/standard/attributes/index).

```csharp
[Input("Integer input")]
public InArgument<int> IntInput { get; set; }
```

or

```csharp
[Output("Integer output")]
public OutArgument<int> IntOutput { get; set; }
```

A single property in your class can be both an input and output parameter by including both attributes:

```csharp
[Input("Int input")]  
[Output("Int output")]  
public InOutArgument<int> IntParameter { get; set; }
```


### Required values

If you want to make an input parameter required when using the workflow activity in a process you must use the `[RequiredArgument]` attribute.

### Default values

When a value passed in as an input parameter or set as an output parameter is not defined, you can specify a default value. For example, to set the default value for a bool property:

```csharp
[Input("Bool input")]
[Default("True")]
public InArgument<bool> Bool { get; set; }
```

The format for the default value depends on the type of property. Examples are in the following table:

|Type|Example|
|--|--|
|[bool](/dotnet/api/system.boolean)|[Default("True")]|
|[DateTime](/dotnet/api/system.datetime)|[Default("2004-07-09T02:54:00Z")]|
|[Decimal](/dotnet/api/system.decimal)|[Default("23.45")]|
|[Double](/dotnet/api/system.double)|[Default("23.45")]|
|<xref:Microsoft.Xrm.Sdk.Money>|[Default("23.45")]|
|<xref:Microsoft.Xrm.Sdk.EntityReference>|[Default("3B036E3E-94F9-DE11-B508-00155DBA2902", "account")]|
|[int](/dotnet/api/system.int32)|[Default("23")]|
|<xref:Microsoft.Xrm.Sdk.OptionSetValue>|[Default("3")]|
|[string](/dotnet/api/system.string)|[Default("string default")]|

### EntityReference parameters

When you define a property for an <xref:Microsoft.Xrm.Sdk.EntityReference> parameter you must use the `ReferenceTarget` attribute. This establishes which type of attribute is permitted. For example:

```csharp
[Input("EntityReference input")]
[Output("EntityReference output")]
[ReferenceTarget("account")]
public InOutArgument<EntityReference> AccountReference { get; set; }
```

### OptionSetValue parameters

When you define a property for an <xref:Microsoft.Xrm.Sdk.OptionSetValue> parameter you must use the `AttributeTarget` attribute. This attribute defines which entity and attribute contains the valid set of values for the parameter. For example:

```csharp
[Input("Account IndustryCode value")]
[AttributeTarget("account", "industrycode")]
[Default("3")]
public InArgument<OptionSetValue> IndustryCode { get; set; }
```

## Add your code to the Execute method

The logic you include in the [CodeActivity.Execute(CodeActivityContext) Method](/dotnet/api/system.activities.codeactivity.execute?view=netframework-4.5.2) method defines what your workflow activity does.

> [!IMPORTANT]
> The code in the `Execute` method should be written to be stateless. It is not recommended to use global or member variables to pass data from one invocation to the next.
> For improved performance, CDS for Apps caches custom workflow activity instances. Because of this, the constructor is not called for every invocation of the custom workflow activity. Also, multiple system threads could execute the custom workflow activity at the same time. You should only use the information that is passed via the [CodeActivityContext](/dotnet/api/system.activities.codeactivitycontext) parameter to the `Execute` method.

### Reference parameters

To reference parameters defined for your class you will use the [Argument.Get](/dotnet/api/system.activities.argument.get?view=netframework-4.5.2) or [Argument.Set(ActivityContext, Object)](/dotnet/api/system.activities.argument.set?view=netframework-4.5.2) methods they provide which require the [CodeActivityContext](/dotnet/api/system.activities.codeactivitycontext) instance that is passed to the `Execute` method. The following example shows accessing the value of an input parameter and setting the value of an output parameter.

```csharp
using Microsoft.Xrm.Sdk.Workflow;
using System.Activities;

namespace SampleWorkflowActivity
{
  public class IncrementByTen : CodeActivity
  {
    [RequiredArgument]
    [Input("Decimal input")]
    public InArgument<decimal> DecInput { get; set; }

    [Output("Decimal output")]
    public OutArgument<decimal> DecOutput { get; set; }

    protected override void Execute(CodeActivityContext context)
    {
      decimal input = DecInput.Get(context);
      DecOutput.Set(context, input + 10);
    }
  }
}
```

### Get Contextual information

When your code requires contextual information you can access this using the [CodeActivityContext.GetExtension<T> method](/dotnet/api/system.activities.activitycontext.getextension) with the <xref:Microsoft.Xrm.Sdk.Workflow.IWorkflowContext> Interface. This object is derived from the <xref:Microsoft.Xrm.Sdk.IExecutionContext> Interface which provides access to many read-only properties that describe the context of the operation. The `IWorkflowContext` provides similar contextual information specific to the executing workflow that is using your workflow assembly.

Use the following code in your `Execute` function to access the `IWorkflowContext`:

```csharp
protected override void Execute(CodeActivityContext context)
{
 IWorkflowContext workflowContext = context.GetExtension<IWorkflowContext>();

...
```

### Use the Organization Service

When you need to perform data operations using the Organization service you can access this using the [CodeActivityContext.GetExtension<T>](/dotnet/api/system.activities.activitycontext.getextension) method with the <xref:Microsoft.Xrm.Sdk.IOrganizationServiceFactory> interface. From there you can use the <xref:Microsoft.Xrm.Sdk.IOrganizationServiceFactory.CreateOrganizationService(System.Nullable{System.Guid})> method to access an instance of the service proxy that you can use to perform data operations. The <xref:Microsoft.Xrm.Sdk.Workflow.IWorkflowContext>.<xref:Microsoft.Xrm.Sdk.IExecutionContext.InitiatingUserId> can be used to determine the user context to use if you want the operation to be performed in the same context as the calling process.
Use the following code in your `Execute` function to get access to the Organization service:

```csharp
protected override void Execute(CodeActivityContext context)
{
 IWorkflowContext workflowContext = context.GetExtension<IWorkflowContext>();
 IOrganizationServiceFactory serviceFactory = context.GetExtension<IOrganizationServiceFactory>();

 // Use the context service to create an instance of IOrganizationService.             
 IOrganizationService service = serviceFactory.CreateOrganizationService(workflowContext.InitiatingUserId);

...
```

## Register your assembly

You will use the Plug-in Registration Tool (PRT) to register assemblies containing custom workflow activities. This is the same tool you use to register plug-ins. For both plug-ins and custom workflow activities, you must register the assembly which will upload it to the environment. However, you do not register steps for custom workflow activities.

For custom workflow activites you must specify the following properties to control what is displayed in the workflow process designer.

|Field|Description|
|--|--|
|Description|Not visible in the UI of the process designer, but may be useful when generating documentation from data drawn from the PluginType Entity that stores this information.|
|FriendlyName|User friendly name for the plug-in.|
|Name|The name of the menu represented|
|WorkflowActivityGroupName|The name of the submenu added to the main menu in the CDS for Apps process designer.|

![Set descriptive properties](media/create-workflow-activity-set-properties.png)

> [!NOTE]
> These values will not be visible in the unmanaged solution when you test your workflow activity. However, when you export a managed solution that includes this workflow activity these values will be visible in the process designer.

## Debug Workflow Activities

With custom workflow activities deployed to CDS for apps you can capture profiles to replay for local debugging and use the tracing service to write information to an entity. 

The following example shows using the tracing service to write the following message: `Add your message.`

```csharp
protected override void Execute(CodeActivityContext context)
{
//Create the tracing service
ITracingService tracingService = executionContext.GetExtension<ITracingService>();

//Use the tracing service
tracingService.Trace("{0} {1} {2}.","Add","your","message");

...
```

More information:
 - [Debug Workflow Activities](debug-workflow-activites.md)
 - [Use Tracing](../debug-plug-in.md#use-tracing)
 - [View trace logs](../tutorial-write-plug-in.md#view-trace-logs)

## Add to Solution

When you register assemblies using the plug-in registration tool they will be added to the **Default solution**, not to be confused with the **Common Data Service Default Solution**. Because the **Default solution** contains all the unmanaged customizations applied to the environment, before you can distribute your custom workflow activity using a solution you must add it to an unmanaged solution. For example, you could add it to the **Common Data Service Default Solution** or any unmanaged solution you have created.

## Manage changes to custom workflow activities

You will need to maintain the code for your custom workflow activities. Because code changes can include breaking changes, you will need to manage this change. You will use different steps to update or upgrade your custom workflow assemblies.

When you register an assembly containing custom workflow activities the version of the assembly is included. This information is extracted using reflection from the assembly. You can control the version number using the `AssemblyInfo.cs` file in your Visual Studio project.

You will find a section at the bottom that looks like this:


```
// Version information for an assembly consists of the following four values:
//
//      Major Version
//      Minor Version 
//      Build Number
//      Revision
//
// You can specify all the values or you can default the Build and Revision Numbers 
// by using the '*' as shown below:
//[assembly: AssemblyVersion("1.0.0.*")]
[assembly: AssemblyVersion("1.0.0.0")]
[assembly: AssemblyFileVersion("1.0.0.0")]
```

This version information is important because it allows you to apply updates to deployed assemblies or upgrade assemblies when you want to include new capabilities.

### Update a custom workflow activity assembly

When you make changes to fix bugs or re-factor code that do not make significant changes to public classes or method signatures you can update the assembly so that all running processes will automatically start using the new version of the assembly.

#### To update an assembly:

1. Change only the **Build Number** and **Revision values** in your `AssemblyInfo.cs` `AssemblyVersion` attribute. For example, change from `1.0.0.0` to `1.0.10.5`.
1. Use the Plug-in registration tool to Update the assembly. More information: [Update an assembly](../register-plug-in.md#update-an-assembly)

#### Upgrade a custom workflow activity assembly:

If you make changes that include significant changes to public classes or method signatures, such as changing the parameters you would break any currently running processes defined to use the original signatures. In this case you must upgrade the assembly. This will create a new custom workflow activity that exposes options define which version to apply in the process designer. This allows for each process using this activity to be re-configured to adapt to the changes included in the new assembly. After all processes using the original assembly are updated to use the upgraded assembly, you can de-register the older assembly.

#### To upgrade an assembly:

1. Make sure the new assembly has the same `Name`, `PublicKeyToken`, and `Culture` as the existing assembly.
1. Change the **Major Version** and/or **Minor Version** values in your `AssemblyInfo.cs` `AssemblyVersion` attribute. For example, change from `1.0.0.0` to `2.0.0.0`.
1. Use the Plug-in registration tool to Register the assembly as a new assembly. More information: [Register an assembly](../register-plug-in.md#register-an-assembly)
1. For each process using the custom workflow activity, you must deactivate the process and edit the steps which use the custom workflow activity.

    You will find a **Version** selector in the process designer that you can use to choose which version of the assembly should be used.

    ![workflow set version](media/workflow-set-version.png)

When all processes are converted to use the new assembly, you can use the Plug-in Registration tool to Unregister the assembly, so it will no longer be available. More information: [Unregister components](../register-plug-in.md#unregister-components)


### See also

[Tutorial: Create workflow extension](tutorial-create-workflow-extension.md)<br />
[Sample: Create a custom workflow activity](sample-create-custom-workflow-activity.md)<br />
[Sample: Update next birthday using a custom workflow activity](sample-update-next-birthday-using-custom-workflow-activity.md)<br />
[Sample: Calculate a credit score with a custom workflow activity](sample-calculate-credit-score-custom-workflow-activity.md)
