---
title: "Create a custom workflow activity (PowerApps Common Data Service for Apps)| MicrosoftDocs"
description: "The topic describes how to create a custom workflow activity and register it for use in CDS for Apps (online) Customer Engagement."
ms.custom: ""
ms.date: 06/16/2018
ms.reviewer: ""
ms.service: "crm-online"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
    - "Dynamics 365 (online)"
ms.assetid: ab72830b-e6a6-4f49-a6a8-1d69c4a1d308
caps.latest.revision: 56
author: "JimDaly"
ms.author: "jdaly"
manager: "amyla"
---
# Create a custom workflow activity

This topic describes how to create a custom workflow activity and register it for use in Common Data Service for Apps. 
  
<a name="Requirements"></a>

## Required software and assemblies

To develop Windows Workflow Foundation 4 custom activities for CDS for Apps, you must develop them on Microsoft .NET Framework 4.5.2. The assembilies are available as Nuget packages and you can download from the NuGet profile [crmsdk](https://www.nuget.org/profiles/crmsdk).
  
<a name="UseCodeActivity"></a>

## Use the CodeActivity workflow base class

 To create a custom workflow activity, create a class that inherits from the [CodeActivity](/dotnet/api/system.activities.codeactivity) workflow base class. This class is available in the [System.Activities](/dotnet/api/system.activities) namespace. Activities that inherit from the `CodeActivity` class can override the `Execute` method to produce custom functionality.  
  
1.  Start Visual Studio.  
2.  On the **File** menu, click **New**, and then click **Project**.  
3.  In the **New Project** dialog box, select **Workflow** under **Visual C#** in the **Installed Templates** pane, and then select **Activity Library**.  
4.  Specify a name and location for the solution, and then click **OK**.  
5.  Navigate to the **Project** menu and select **Properties**. On the **Application** tab, specify **.NET Framework 4.5.2** as the target framework.  
6.  Add references to the `Microsoft.Xrm.Sdk.dll` and `Microsoft.Xrm.Workflow.dll` assemblies.  
7.  Delete the Activity1.xaml file in the project.  
8.  Add a class file (.cs) to the project. In Solution Explorer, right-click the project, select **Add**, and then click **Class**. In the **Add New Item** dialog box, type a name for the class, and then click **Add**.  
9. Open the class file, and add the following using directives:  
  
    ```csharp  
    using System.Activities;
    using Microsoft.Xrm.Sdk;
    using Microsoft.Xrm.Sdk.Workflow;  
    ```  
  
10. Make the class inherit from the `CodeActivity` class and give it a public access modifier as shown here:  
  
    ```csharp  
    public class SampleCustomActivity : CodeActivity  
    ```  
  
11. Add functionality to the class by adding an [Execute](https://msdn.microsoft.com/library/system.activities.codeactivity.execute.aspx) method:  
  
    ```csharp  
    protected override void Execute(CodeActivityContext context){    //Activity code}  
    ```  
  
     For more information, see [Adding Metadata to the Custom Workflow Activity](add-metadata-custom-workflow-activity.md).  
  
12. Specify input and output parameters. For more information, see [Adding Metadata to the Custom Workflow Activity](add-metadata-custom-workflow-activity.md).  
  
13. In the project properties, under the **Signing** tab, select **Sign the assembly** and provide a key file name. Custom workflow activity (and plug-in) assemblies must be signed.  
  
14. Compile the project to create an assembly (.dll).  
  
 To view a code sample that demonstrates how to create a custom workflow activity, see [Sample: Create a Custom Workflow Activity](sample-create-custom-workflow-activity.md).  
  
> [!IMPORTANT]
>  For improved performance, CDS for Apps caches custom workflow activity instances. The custom workflow activity’s [Execute](/dotnet/api/system.activities.codeactivity.execute) method should be written to be stateless because the constructor is not called for every invocation of the custom workflow activity. Also, multiple system threads could execute the custom workflow activity at the same time. All per invocation state information is stored in the context, so it is not recommended to use global variables or member variables to pass data from one invocation to the next.  
  
<a name="NameandGroupName"></a>

## Specify the name and group name for a custom workflow activity

When you register a custom workflow activity assembly, specify the name and group name. The name property specifies the name of the workflow activity. The group name property specifies the name of the submenu added to the main menu in the CDS for Apps process designer. These properties link the custom workflow activity with the CDS for Apps process designer, so that the custom activity name will appear in the user interface.  
  
To specify the name and group name for a custom workflow activity, use the `PluginType.Name` and `PluginType.WorkflowActivityGroupName` attributes when you register the custom workflow activity assembly. For more information about registering custom workflow activities, see [Registering the Workflow Assembly](register-use-custom-workflow-activity-assembly.md). If the `PluginType.Name` and `PluginType.WorkflowActivityGroupName` attributes are set to **null**, the custom activity is hidden from the CDS for Apps workflow designer and is only accessible from XAML workflows.  
  
<!-- TODO:
If you are using the Plug-in Registration tool to register the custom workflow activity assembly, you can specify appropriate values in the **Name** and **WorkflowActivityGroupName** boxes, under the **Editable** region. For more information about using the Plug-in Registration tool, see [Walkthrough: Register a plug-in using the plug-in registration tool](../walkthrough-register-plugin-using-plugin-registration-tool.md).   -->
  
 <!-- TODO: 
![Specify the Group Name and Name while registering](../media/process-name-workflow-activity.png "Specify the Group Name and Name while registering")   -->
  
After this custom workflow activity is registered, you can use it from the CDS for Apps process designer for workflows or dialogs. For more information, see [Register and Use a Custom Workflow Activity Assembly](register-use-custom-workflow-activity-assembly.md).  
  
### See also

[Custom workflow activities (workflow assemblies)](../custom-workflow-activities-workflow-assemblies.md)<br />
[Adding Metadata to the Custom Workflow Activity](add-metadata-custom-workflow-activity.md)<br />
[Using the IOrganization Web Service within a Custom Workflow Activity](use-iorganization-web-service-custom-workflow-activity.md)<br />
[Sample: Create a Custom Workflow Activity](sample-create-custom-workflow-activity.md)<br />
<!-- TODO:
[Sample: Azure aware custom workflow activity](../sample-azure-aware-custom-workflow-activity.md) -->