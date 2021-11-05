---
title: "Quickstart: Create a plug-in using Power Platform Tools | Microsoft Docs"
description: "Learn how to create and register a Dataverse plug-in using the Power Platform Tools extension for Visual Studio."
ms.custom: ""
ms.date: 11/04/2021
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "phecke" # GitHub ID
ms.subservice: dataverse-developer
ms.author: "pehecke" # MSFT alias of Microsoft employees only
manager: "kvivek" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Quickstart: Create a plug-in using Power Platform Tools

To create and deploy a plug-in using the Power Platform Tools extension for Visual Studio, start by creating a new Dataverse solution with a plug-in library. Instructions to do this can be found in the topic [Create a Power Platform Tools project](devtools-create-project.md).

If you already have an existing Dataverse solution set up, then follow these [instructions](devtools-create-project.md#add-a-new-project-to-a-power-platform-solution) to add a Plug-in Library project to the solution using the Power Platform Tools template.

## Prerequisites

- Visual Studio 2019 or later
- Power Platform Tools extension for Visual Studio
- C# language
- .NET Framework 4.6.2 (only for plug-in or custom workflow activity development)
- Power Apps/Dataverse subscription or a trial environment

## Connect to your Dataverse environment

To connect to your Dataverse environment and register custom code assemblies, steps, and more, follow these steps.

1. In the **Tools** menu, select **Connect to Dataverse**.

1. Step #1 is to login. Check the desired options in the dialog and select **Login**.

1. Step #2 is to select an existing Dataverse solution, or the **Default** solution. This is the solution that your plug-in and workflow activity assemblies will be registered with.

1. Choose **Done** when finished.

The Power Platform Explorer view will be displayed or you can open that view from the **View** menu. Expand the nodes to see what kinds of environment data you can view. Right-click on nodes to see what options are available.

> [!NOTE]
> The Power Platform Explorer view of the Power Platform Tools extension is capable of more than plug-in and workflow activity registration. Documentation for additional features will be provided in a future documentation release. In the meantime, feel free to explore.  


## Register a plug-in step with Dataverse

Follow these instructions to register a plug-in step (also known as an SDK message processing step). The step identifies what data table and event causes your plug-in to execute. More information: [Event framework](../event-framework.md), [Register plug-in step](../register-plug-in.md#register-plug-in-step)

1. Select **View** > **Power Platform Explorer**, expand your environment node and the **Tables** sub-node.

1. Right-click on the table type (e.g.; "Account") that the step is to be registered on, then select **Create Plug-in**.

    :::image type="content" source="../media/tools/devtools-create-plugin.png" alt-text="Create a plug-in.":::

    > [!NOTE]
    > You can also create a plug-in by expanding the **Event Catalog**, right-clicking a business event, and choose **Add Plug-in**.

1. Fill out the **Register New Step** dialog information and choose **Register New Step** when done. <p/>The class name that you specify when filling out the step information will be used to name your new plug-in class. The class will be placed in the plug-in project library specified by the **Handler Assembly** dialog field. If there is only one Plug-in Library project in the solution, the **Handler Assembly** field will be inactive.

A new step registration has been added to the solution. However, you will need to build and deploy your plug-in library before the plug-in assembly and step are added to the specified Dataverse environment and solution.

### Add another plug-in class to the library

Let's say that you followed the steps above to create a plug-in class in the plug-in project library and add a step. Now you want to add another plug-in class to that same library. How do you do that? You have two options, both are through context menus of the Power Platform Tools extension.

1. The first method is to do the same as you did above by expanding the **Table** node in the **Power Platform Explorer** view, right-clicking a table type, and then selecting **Create Plug-in**. When registering the step, specify the same plug-in project library in the **Handler Assembly**, and the new class name in the **Class Name** form field.

1. For the second method, let's say that you already built and deployed the plug-in library assembly to the Dataverse environment. In this case, you will see the deployed assembly and step you created after you refresh the explorer view and expand the **Plug-in Assemblies** node. At that point you can simply right-click the target assembly node and select **Add Plug-in**. Doing so will display the step registration form which you can now fill out for your new plug-in class.

Afterwards, build and deploy the plug-in library project to update the target environment and solution.

### Add a plug-in step

You can add a step for an existing registered plug-in that you own. To do so, expand the target plug-in assembly node in the **Power Platform Explorer** view to display the registered plug-in. Right-click that plug-in's node and select **Add Step**. Fill out the **Register New Step** form.

You do not need to build and deploy the plug-in project for the step registration to be available in the target environment and solution.

## The PluginBase abstract class

`PluginBase` is automatically generated from the Plug-in Library template. Your custom plug-in class should derive from this base class. The base class implements common plug-in code that helps to make you more productive sooner. Take a look at the `PluginBase` class code in your plug-in project to see what it does.

## The generated plug-in class code

The Plug-in Library template provides the `PluginBase` abstract class. Your plug-in must derive from `PluginBase` if it is to work well with the Power Platform Tools extension. Below is the generated derived class when creating a plug-in from Power Platform Explorer. You typically would add your code where the TODO comments are. Notice that the standard [IPlugin](xref:Microsoft.Xrm.Sdk.IPlugin) interface `Execute` method has been replaced with `ExecuteCdsPlugin` in the plug-in code.

```csharp
using System;
using System.ServiceModel;
using Microsoft.Xrm.Sdk;

namespace PPTools_Sample_Solution.NotifyPlugin
{    
    public class NotifyAccountCreate: PluginBase
    {
        public NotifyAccountCreate(string unsecure, string secure)
            : base(typeof(NotifyAccountCreate))
        {
           // TODO: Implement your custom configuration handling.
        }

        protected override void ExecuteCdsPlugin(LocalPluginContext localContext)
        {
            if (localContext == null)
            {
                throw new InvalidPluginExecutionException(nameof(localContext));
            }           
            ITracingService tracingService = localContext.TracingService;

            try
            {  
                IPluginExecutionContext context = (IPluginExecutionContext)localContext.PluginExecutionContext;
 
                IOrganizationService service = localContext.OrganizationService;

                // TODO: Implement your custom Plug-in business logic.

            }
            catch (Exception ex)
            {
                tracingService?.Trace("An error occurred executing Plugin PPTools_Sample_Solution.NotifyPlugin.NotifyAccountCreate : {0}", ex.ToString());
                throw new InvalidPluginExecutionException("An error occurred executing Plugin PPTools_Sample_Solution.NotifyPlugin.NotifyAccountCreate .", ex);
            }
        }
    }
}
```

At this point you would add your custom plug-in code where indicated by the TODO code comments. For more information, read some of these related topics: [Pass configuration data to your plug-in](../write-plug-in.md#pass-configuration-data-to-your-plug-in), [Understand the execution context](../understand-the-data-context.md#understand-the-execution-context), and [Tracing and logging](../logging-tracing.md).

> [!IMPORTANT]
> We encourage you to use the Power Platform Tools context menus. When you use the Power Platform Explorer context menus to add plug-ins, classes are generated using the provided information and deployment entries in the CrmPackage project's RegisterFile.crmregister file are maintained. It is this information that is used for deployment of assemblies, plug-ins, and steps.

## Sign the assembly

All plug-in and custom workflow assemblies must be digitally signed before they are uploaded to the Dataverse server. to sign the assembly, follow these steps.

1. Select the plug-in or workflow activity project in **Solution Explorer**.

1. Choose **Project** > \<project name> **Properties** to edit the project's properties.

1. On the **Signing** tab, check **Sign the assembly**, and then specify a strong name key file.


## Deploy the plug-in to the environment solution

After you are done modifying code and are ready to deploy the plug-in assembly and step(s) to you environment, follow these steps.

1. Build the plug-in library.

1. Right-click the plug-in library project in **Solution Explorer**.

1. Select **Deploy** in the context menu.

> [!TIP]
> You can deploy all projects in the Visual Studio solution by right-clicking the CrmPackage project and choosing **Deploy**.

After deployment completes, select the refresh icon in **Power Platform Explorer**. Expand the **Plug-in Assemblies** sub-node of your environment node to see your registered assembly. Right-click on the plug-in assembly and step in **Power Platform Explorer** to see what operations are supported. Selecting **Delete Assembly** will un-register the assembly and its related steps.

## Next steps

Learn more about plug-in development

> [!div class="nextstepaction"]
> [Next step](../plug-ins.md#next-steps)

## Providing tool feedback

You can send tool feedback to Microsoft using the feedback icon in the Power Platform Explorer view.

:::image type="content" source="../media/tools/devtools-feedback-dialog(small).png" alt-text="Provide feedback.":::

### See Also

*Power Platform Tools specific articles*  
[Install Power Platform Tools](devtools-install.md)  
[Create a Power Platform Tools project](devtools-create-project.md)  
[Tutorial: Debug a plug-in](../tutorial-debug-plug-in.md?tabs=pptools)

*General event handler articles*  
[Event framework](../event-framework.md)  
[Use plug-ins to extend business processes](../plug-ins.md)  
[Workflow extensions](../workflow/workflow-extensions.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
