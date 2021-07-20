---
title: "Create a plug-in using the Developer Toolkit | Microsoft Docs"
description: "Learn how to create and register a Dataverse plug-in using the Power Platform Tools for Visual Studio extension."
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

# Create a plug-in using the Developer Toolkit

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

Like any Visual Studio solution, you begin by creating a new project. In the New Project dialog box under Visual C#, select the Dynamics CRM group to view the available project templates.

## Available project templates for Power Platform development

The following table introduces the available project templates.

| Project template | Description |
| --- | --- |
| New Visual Studio Solution Template | Solution template for creating a new instance of a  Visual Studio Solution |

Project template for creating a new Microsoft Dynamics CRM 2013 Plug-in class library (.dll).
Project template for creating a new Microsoft Dynamics CRM 2013 Workflow class library (.dll).
Project for creating a Microsoft Dynamics CRM 2013 Package project.
Project template for creating CRM Workflows using the Visual Studio Workflow Designer.

The New Visual Studio Solution Template for Dynamics CRM 2013 project creates the following types of solution components:

1. Plug-in Library
1. Workflow Library
1. Web Resources (part of the CrmPackage project)

The New Visual Studio Solution Template is a good starting point for any new solution. You can add and remove new projects to and from the solution. You should not remove the CrmPackage project.

The Plug-in Library and Workflow Library project templates are typically used for more advanced scenarios where you may want to add multiple assemblies to a project or if you are only interested in developing that specific component. Before you can deploy a solution that contains only a project of these types, you must add a Package (CrmPackage) project to the solution.

> [!NOTE]
> A Microsoft Dynamics CRM solution can contain only a single CrmPackage project.

## Managing projects

Use the following procedures to manage your Visual Studio solution.

### Add a new project to the solution

Right-click the solution and select Add and then New Project.

Select one of the following from the installed templates under Visual C#:

Dynamics CRM > Plug-in Library

Dynamics CRM > Workflow Library

### Add an existing project to the solution

1. Right-click the solution and select Add and then Existing Project.

1. Navigate to the .csprog file that represents the project you want to add.

1. In the CrmPackage project, right-click the References and select Add Reference.

1. In the Projects tab of the Add Reference dialog box, select the projects and then click Add to add them to the list of selected projects and components.

1. Click OK to add the projects and close the Add Reference dialog box.

### Remove a project from the solution

Right-click the project in **Solution Explorer** and select **Remove**. The project will automatically be removed from the CrmPackage references.

### See also

***Developer Toolkit specific articles***  
[Install Power Platform Tools](devtools-install.md)  
[Create a plug-in using Power Platform Tools](devtools-create-plugin.md)

***General event handler articles***  
[Event framework](../event-framework.md)  
[Use plug-ins to extend business processes](../plug-ins.md)  
[Workflow extensions](../workflow/workflow-extensions.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
