---
title: "Create a Custom API with solution files (Common Data Service) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "You can write create custom APis by editing solution files." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 10/26/2020
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "JimDaly" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Create a Custom API with solution files 


[This topic is pre-release documentation and is subject to change.]

> [!NOTE]
> This is an advanced topic that assumes you have already read and understood these topics:
> - [Create and use Custom APIs](custom-api.md)
> - [Create a Custom API in the maker portal](create-custom-api-maker-portal.md)
>
> This topic also involves working with solutions. This topic assumes you have familarity with the following:
> - [Solution concepts](/power-platform/alm/solution-concepts-alm)
> - [Source control with solution files](/power-platform/alm/use-source-control-solution-files)
> - [Solution component file reference (SolutionPackager)](solution-component-file-reference-solutionpackager.md)

While you can create Custom APIs through a designer or with code, you can also define them by working with files within a solution. This may be the preferred option for solution publishers who apply the recommended best practices for Application Lifecycle Management (ALM).

A solution file is a compressed (zip) file that has been exported from a Common Data Service instance. The contents of this file can be extracted and the components checked into a source repository. The contents can be edited and then compressed again. The changes applied to the solution will then be part of the solution and will be created when the solution is imported.

> [!NOTE]
> These processes are typically automated with tools and processes that are beyond the scope of this topic. This topic will focus on the simple scenario of creating a Custom API by manually manipulating the extracted files in a solution to demonstrate how the data in the files can be used to create Custom API.

## Step 1: Create an unmanaged solution

You should not try to compose a solution file manually. Use the tools in [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) to generate a solution file. Use the steps in the following topics to create and export a solution. The solution doesn't need to contain any solution components.

1. [Create a solution](../../maker/common-data-service/create-solution.md)

  For this example, the solution is defined simply like this:
  :::image type="content" source="media/custom-api-solution.png" alt-text="An empty solution":::

1. [Export solutions](../../maker/common-data-service/export-solutions.md)

  For this example, make sure you export an unmanaged solution. Managed solution is the default.
  :::image type="content" source="media/export-empty-unmanaged-solution.png" alt-text="Option to select to export an unmanaged solution":::
  
You can find the exported file in your downloads folder.

## Step 2: Extract the contents of the solution

The solution is a compressed (zip) file. Right-click on the file and choose **Extract All...** from the context menu.

You should see just the following three files in the folder:

- `[Content_Types].xml`
- `customizations.xml`
- `solution.xml`

You will not need to edit any of these files.

## Step 3: Add the definition of the Custom API

1. In the folder with the extracted files, create a new folder named `customapis`.
1. In the **customapis** folder, create a folder with the `UniqueName` of the Custom API you want to create. For this example we will use `sample_CustomAPIExample`.
1. In the **sample_CustomAPIExample** folder, create a file named `customapi.xml`.
1. Edit the customapi.xml to set the properties of the custom API you want to create. For this example, we will use the following:
  ```xml
  <customapi uniquename="sample_CustomAPIExample">
    <allowedcustomprocessingsteptype>0</allowedcustomprocessingsteptype>
    <bindingtype>0</bindingtype>
    <description default="A simple example of a Custom API">
      <label description="A simple example of a Custom API" languagecode="1033" />
    </description>
    <displayname default="Custom API Example">
      <label description="Custom API Example" languagecode="1033" />
    </displayname>
    <iscustomizable>1</iscustomizable>
    <isfunction>0</isfunction>
    <name>sample_CustomAPIExample</name>
  </customapi>
  ```
    
> [!NOTE]
> If you already have a Plug-in Type that you want to associate with this Custom API, you can include a reference to it in this definition by adding the following element within the  `<customapi>` element:
>
>  ```xml
>    <plugintypeid>
>      <plugintypeid>{Add the GUID value of the plug-in type id}</plugintypeid>
>    </plugintypeid>
>  ```
>
>  You can retrieve the Plug-in Type Id using a query like this where you know the name of the plug-in type:
>
>  ```http
>  GET {{webapiurl}}plugintypes?$select=name&$filter=contains(name,'MyPlugin.TypeName')
>  ```
