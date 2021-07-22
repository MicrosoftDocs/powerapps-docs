---
title: "Quickstart: Create a plug-in using Power Platform Tools | Microsoft Docs"
description: "Learn how to create and register a Dataverse plug-in using the Power Platform Tools extension for Visual Studio."
ms.custom: ""
ms.date: 07/19/2021
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

To create a plug-in using the Power Platform Tools extension for Visual Studio, start by creating a new Dataverse solution with a plug-in library. Instructions to do this can be found in the topic [Create a Power Platform Tools project](devtools-create-project.md).

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

The Power Platform Explorer view will be displayed. Expand the nodes to see what kinds of environment data you can view. Right-click on nodes to see what options are available.

> [!NOTE]
> The Power Platform Explorer view of the Power Platform Tools extension is capable of more than plug-in and workflow activity registration. Documentation for additional features will be provided in a future documentation release. In the meantime, feel free to explore.  


## Register a plug-in step with Dataverse

Follow these instructions to register a plug-in step (also known as an SDK message processing step). The step identifies what table and event causes your plug-in to execute.

1. In **Power Platform Explorer**, expand your environment node and the **Tables** sub-node.

1. Right-click on the table type that the step is to be registered on, then select **Create Plug-in**.

1. Fill out the **Register New Step** dialog information and choose **Register New Step**. The class name that you specify when filling out the step information will be used to name your new plug-in class. <!--note: link to the topic with info on creating a step -->

A new plug-in class that derives from `PluginBase` is now visible in your plug-in library, and a new step registration has been added to the solution. However, you will need to build and deploy your plug-in library before the plug-in and step are added to the actual environment.

## The generated plug-in class code

The Plug-in Library template provides the `PluginBase` abstract class. Your plug-in must derive from `PluginBase` if it is to work well with the Power Platform Tools extension. Below is the generated derived class when creating a plug-in from **Power Platform Explorer**. You typically would add your code where the TODO comments are. Notice that the standard plug-in `Execute` method has been replaced with `ExecuteCrmPlugin`.

```csharp
using System;
using System.ServiceModel;
using Microsoft.Xrm.Sdk;

namespace PPTools_Sample_Solution.NotifyPlugin
{
    /// <summary>
    /// NotifyAccountCreate Plugin.
    /// </summary>    
    public class NotifyAccountCreate: PluginBase
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="NotifyAccountCreate"/> class.
        /// </summary>
        /// <param name="unsecure">Contains public (unsecured) configuration information.</param>
        /// <param name="secure">Contains non-public (secured) configuration information. 
        /// When using Microsoft Dynamics 365 for Outlook with Offline Access, 
        /// the secure string is not passed to a plug-in that executes while the client is offline.</param>
        public NotifyAccountCreate(string unsecure, string secure)
            : base(typeof(NotifyAccountCreate))
        {
            
           // TODO: Implement your custom configuration handling.
        }


        /// <summary>
        /// Main entry point for he business logic that the plug-in is to execute.
        /// </summary>
        /// <param name="localContext">The <see cref="LocalPluginContext"/> which contains the
        /// <see cref="IPluginExecutionContext"/>,
        /// <see cref="IOrganizationService"/>
        /// and <see cref="ITracingService"/>
        /// </param>
        /// <remarks>
        /// For improved performance, Microsoft Dynamics 365 caches plug-in instances.
        /// The plug-in's Execute method should be written to be stateless as the constructor
        /// is not called for every invocation of the plug-in. Also, multiple system threads
        /// could execute the plug-in at the same time. All per invocation state information
        /// is stored in the context. This means that you should not use global variables in plug-ins.
        /// </remarks>
        protected override void ExecuteCrmPlugin(LocalPluginContext localContext)
        {
            if (localContext == null)
            {
                throw new InvalidPluginExecutionException(nameof(localContext));
            }           
            // Obtain the tracing service
            ITracingService tracingService = localContext.TracingService;

            try
            { 
                // Obtain the execution context from the service provider.  
                IPluginExecutionContext context = (IPluginExecutionContext)localContext.PluginExecutionContext;

                // Obtain the organization service reference for web service calls.  
                IOrganizationService service = localContext.OrganizationService;

                // TODO: Implement your custom Plug-in business logic.

                
            }	
            // Only throw an InvalidPluginExecutionException. Please Refer https://go.microsoft.com/fwlink/?linkid=2153829.
            catch (Exception ex)
            {
                tracingService?.Trace("An error occurred executing Plugin PPTools_Sample_Solution.NotifyPlugin.NotifyAccountCreate : {0}", ex.ToString());
                throw new InvalidPluginExecutionException("An error occurred executing Plugin PPTools_Sample_Solution.NotifyPlugin.NotifyAccountCreate .", ex);
            }	
        }
    }
}
```

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

After deployment completes, select the refresh icon in **Power Platform Explorer**. Expand the Plug-in Assemblies sub-node of your environment node to see your registered assembly. Right-click on the assembly and step in **Power Platform Explorer** to see what operations are supported.

## Next steps

Learn more about plug-in development

> [!div class="nextstepaction"]
> [Next step](../plug-ins.md#next-steps)

### See Also

*Power Platform Tools specific articles* 
[Install Power Platform Tools](devtools-install.md)  
[Create a Power Platform Tools project](devtools-create-project.md)

*General event handler articles*  
[Event framework](../event-framework.md)  
[Use plug-ins to extend business processes](../plug-ins.md)  
[Workflow extensions](../workflow/workflow-extensions.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
