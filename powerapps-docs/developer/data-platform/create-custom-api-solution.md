---
title: "Create a custom API with solution files"
description: "You can write create custom APIs by editing solution files." 
ms.date: 07/14/2023
ms.reviewer: jdaly
ms.topic: article
author: divkamath
ms.subservice: dataverse-developer
ms.author: dikamath
search.audienceType: 
  - developer
contributors:
  - PHecke
  - JimDaly
---
# Create a custom API with solution files

> [!NOTE]
> This is an advanced topic that assumes you have already read and understood these topics:
> - [Create and use custom APIs](custom-api.md)
> - [Create a custom API using the plug-in registration tool](create-custom-api-prt.md)


While you can create custom APIs through a designer or with code, you can also define them by working with files within a solution. Using files within a solution may be the preferred option for solution publishers who apply the recommended best practices for Application Lifecycle Management (ALM).

A solution file is a compressed (zip) file that has been exported from a Microsoft Dataverse instance. The contents of this file can be extracted and the components checked into a source repository. The contents can be edited and then compressed again. The changes applied to the solution are part of the solution and are created when the solution is imported.

> [!NOTE]
> These processes are typically automated with tools and processes that are beyond the scope of this topic. This topic will focus on the simple scenario of creating a custom API by manually manipulating the extracted files in a solution to demonstrate how the data in the files can be used to create custom API. More information: [Source control with solution files](/power-platform/alm/use-source-control-solution-files)

## Step 1: Create an Unmanaged solution

You shouldn't try to compose a solution file manually. Use the tools in [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) to generate a solution file. Use the steps in the following articles to create and export a solution. The solution doesn't need to contain any solution components.

1. [Create a solution](../../maker/data-platform/create-solution.md)

    For this example, the solution is defined simply like this:

    :::image type="content" source="media/custom-api-solution.png" alt-text="An empty solution.":::

1. [Export solutions](../../maker/data-platform/export-solutions.md)

    For this example, make sure you export an unmanaged solution. Managed solution is the default.

    :::image type="content" source="media/export-empty-unmanaged-solution.png" alt-text="Option to select to export an unmanaged solution.":::
    
You can find the exported file in your downloads folder. It has a name that depends on the name and version of the solution, in this case: `CustomAPIExample_1_0_0_2.zip`.

## Step 2: Extract the contents of the solution and update the version

The solution is a compressed (zip) file.

1. Right-click on the file and choose **Extract All...** from the context menu.

    You should see just the following three files in the folder:

    - `[Content_Types].xml`
    - `customizations.xml`
    - `solution.xml`

1. Open the solution.xml file and locate the `Version` element.

    ```xml
    <ImportExportXml version="9.1.0.23474" SolutionPackageVersion="9.1" languagecode="1033" generatedBy="CrmLive" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
      <SolutionManifest>
        <UniqueName>CustomAPIExample</UniqueName>
        <LocalizedNames>
          <LocalizedName description="Custom API Example" languagecode="1033" />
        </LocalizedNames>
        <Descriptions />
        <Version>1.0.0.1</Version>
    ```

1. Update the value by 1. In this example, it's `<Version>1.0.0.2</Version>`.
1. Save the file.

## Step 3: Add the definition of the custom API

All custom APIs in a solution are found within a folder named **customapis**. Within that folder each custom API will be in a folder named after the custom API `UniqueName` property.
Within the folder, the data representing the custom API is found within an XML file named `customapi.xml`

1. In the folder with the extracted files, create a new folder named `customapis`.
1. In the **customapis** folder, create a folder with the `UniqueName` of the custom API you want to create. For this example, we use `sample_CustomAPIExample`.
1. In the **sample_CustomAPIExample** folder you created, create a file named `customapi.xml`.
1. Edit the `customapi.xml` to set the properties of the custom API you want to create. For this example, we use the following xml:
   
    ```xml
    <customapi uniquename="sample_CustomAPIExample">
      <allowedcustomprocessingsteptype>0</allowedcustomprocessingsteptype>
      <bindingtype>0</bindingtype>
      <boundentitylogicalname />
      <description default="A simple example of a custom API">
        <label description="A simple example of a custom API" languagecode="1033" />
      </description>
      <displayname default="Custom API Example">
        <label description="Custom API Example" languagecode="1033" />
      </displayname>
      <iscustomizable>0</iscustomizable>
      <executeprivilegename />
      <isfunction>0</isfunction>
      <isprivate>0</isprivate>
      <name>sample_CustomAPIExample</name>
      <plugintypeid />
    </customapi>
    ```

  See the information in [Custom API table columns](custom-api-tables.md#custom-api-table-columns) to set the values of the elements.

### Set a relation to a plug-in type (optional)

If you already have a Plug-in Type that you want to associate with this custom API, you can include a reference to it in this definition by adding the following element within the `<customapi>` element:

```xml
<plugintypeid>
   <plugintypeexportkey>{Add the GUID value of the plug-in type export key}</plugintypeexportkey>
</plugintypeid>
  ```

OR

  ```xml
<plugintypeid>
   <plugintypeid>{Add the GUID value of the plug-in type id}</plugintypeid>
</plugintypeid>
  ```

> [!NOTE]
> Either value will work, but we recommend you use the `plugintypeexportkey`.

You can retrieve the [PluginTypeExportKey](reference/entities/plugintype.md#BKMK_PluginTypeExportKey) and [PluginTypeId](reference/entities/plugintype.md#BKMK_PluginTypeId) values using a Web API query like this where you know the name of the plug-in type:

```http
GET [Organization Uri]/api/data/v9.2/plugintypes?$select=name,plugintypeid,plugintypeexportkey&$filter=contains(name,'MyPlugin.TypeName')
```

## Step 4: Add any custom API Request Parameters

Any definitions of request parameters for the custom API are included in a folder called `customapirequestparameters`. Within that folder each custom API Request Parameter will be in a folder named after the custom API Request Parameter `UniqueName` property.

1. If your custom API has any request parameters, within the folder for the custom API you created in the previous step, create a folder named `customapirequestparameters`.
1. For each custom API Request Parameter, create a new folder using the `UniqueName` property of the custom API Request Parameter. For this example, we use `StringParameter`.
1. Within the folder, add an xml file named `customapirequestparameter.xml`.
1. Edit the **customapirequestparameter.xml** file to set the properties of the custom API you want to create. For this example, we use the following:

  ```xml
  <customapirequestparameter uniquename="StringParameter">
    <description default="The StringParameter request parameter for custom API Example">
      <label description="The StringParameter request parameter for custom API Example" languagecode="1033" />
    </description>
    <displayname default="Custom API Example String Parameter">
      <label description="Custom API Example String Parameter" languagecode="1033" />
    </displayname>
    <iscustomizable>0</iscustomizable>
    <isoptional>0</isoptional>
    <logicalentityname />
    <name>sample_CustomAPIExample.StringParameter</name>
    <type>10</type>
  </customapirequestparameter>
  ```

See the information in [CustomAPIRequestParameter Table Columns](custom-api-tables.md#customapirequestparameter-table-columns) to set the values of the elements.

## Step 5: Add any custom API Response Properties

Any definitions of response properties for the custom API are included in a folder called `customapiresponseproperties`. Within that folder each custom API Response Property will be in a folder named after the custom API Response Property  `UniqueName` property.

1. If your custom API has any response properties, within the folder for the custom API you created in [Step 3: Add the definition of the custom API](#step-3-add-the-definition-of-the-custom-api), create a folder named `customapiresponseproperties`.
1. For each custom API Response Property, create a new folder using the `UniqueName` property of the custom API Response Property. For this example, we use `StringProperty`.
1. Within the folder, add an xml file named `customapiresponseproperty.xml`.
1. Edit the **customapiresponseproperty.xml** file to set the properties of the custom API you want to create. For this example, we use the following:

  ```xml
  <customapiresponseproperty uniquename="StringProperty">
    <description default="The StringProperty response property for custom API Example">
      <label description="The StringProperty response property for custom API Example" languagecode="1033" />
    </description>
    <displayname default="Custom API Example String Property">
      <label description="Custom API Example String Property" languagecode="1033" />
    </displayname>
    <iscustomizable>0</iscustomizable>
    <logicalentityname />
    <name>sample_CustomAPIExample.StringProperty</name>
    <type>10</type>
  </customapiresponseproperty>
  ```

See the information in [CustomAPIResponseProperty Table Columns](customapiresponseproperty-table-columns.md) to set the values of the elements.

> [!NOTE]
> While the schema for request parameters and response properties is very similar, note that `isoptional` is not valid for a response property and will cause an error when you try to import the solution.

## Step 6: Compress the files to create a new solution file

1. Return to the folder where you extracted the original solution file in [Step 2: Extract the contents of the solution and update the version](#step-2-extract-the-contents-of-the-solution-and-update-the-version)
1. Select all the extracted files and the **customapis** folder you created.

    :::image type="content" source="media/selected-solution-files.png" alt-text="The selected solution files.":::

1. Right-click the selected files and choose **Send to** > **Compressed (zipped folder)**.
1. You can rename the resulting file to be anything you want. For this example, rename it to match the original exported solution file: `CustomAPIExample_1_0_0_2.zip`.

## Step 7: Import the solution with the definition of your custom API

1. Return to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) and select **Solutions**.
1. Select **Import** and follow the instructions to select the solution file you created in the previous step.

    :::image type="content" source="media/import-solution-with-customapi.png" alt-text="Import the solution file.":::

    > [!NOTE]
    > If you see a warning saying **This version of the solution package is already installed**, you must not have updated the `Version` element of the solution.xml as described in [Step 2: Extract the contents of the solution and update the version](#step-2-extract-the-contents-of-the-solution-and-update-the-version).

1. You should see a warning saying **This solution package contains an update for a solution that is already installed**. Select **Import** to continue.
1. Wait a few minutes while the solution import completes. 

  > [!NOTE]
  > It is possible you will see an error if another solution is being installed at the same time. More information: [The solution installation or removal failed due to the installation or removal of another solution at the same time](https://support.microsoft.com/help/4343228/the-solution-installation-or-removal-failed-due-to-the-installation-or)

## Step 8: Verify that the custom API was added to your solution

Open the solution you created and verify that the custom API and the associated request parameters and response properties are included.

:::image type="content" source="media/customapi-solution-installed-successfully.png" alt-text="Showing that the solution component installed successfully.":::

At this point, you can test your API using the steps describe in [Test your custom API](create-custom-api-maker-portal.md#test-your-custom-api)

## Update a custom API in a solution

After you ship a solution that contains a custom API, you may want to make some changes to the custom API in your unmanaged solution. You can add new parameters or response properties and make changes to those columns that support being updated, such as the `displayname` and `description`.

> [!IMPORTANT]
> You cannot introduce a change to a custom API in a solution that modifies any of the properties that cannot be changed after they are saved. When you install a newer version of a solution that contains a definition of a custom API, it will attempt to update the custom API, custom API Request Parameters, and custom API Response properties. A solution update is the same as trying to update the custom API using any other method.
>
> The following are properties in the solution files that cannot be changed after a custom API is created:
> - Custom API properties:
>    - `allowedcustomprocessingsteptype`
>    - `bindingtype`
>    - `boundentitylogicalname`
>    - `isfunction`
>    - `uniquename`
>    - `workflowsdkstepenabled`
> - Custom API RequestParameter properties:
>    - `isoptional`
>    - `logicalentityname`
>    - `type`
>    - `uniquename`
> - Custom API Response Property properties:
>    - `logicalentityname`
>    - `type`
>    - `uniquename`
>
>  More information: [CustomAPI tables](custom-api-tables.md)



## Providing Localized Labels with the solution

As an alternative to using the process described in [Localized Label values](custom-api.md#localized-label-values), if you're editing the solution files for custom API entities, you can provide translations directly in these files. For example if you want to provide Japanese localized labels for your custom API, you can provide them for the `description` and `displayname` properties as shown below:

```xml
<customapi uniquename="sample_CustomAPIExample">
  <allowedcustomprocessingsteptype>0</allowedcustomprocessingsteptype>
  <bindingtype>0</bindingtype>
  <description default="A simple example of a custom API">
    <label description="A simple example of a custom API" languagecode="1033" />
    <label description="カスタムAPIの簡単な例" languagecode="1041" />
  </description>
  <displayname default="Custom API Example">
    <label description="Custom API Example" languagecode="1033" />
    <label description="カスタムAPIの例" languagecode="1041" />
  </displayname>
  <iscustomizable>0</iscustomizable>
  <isfunction>0</isfunction>
  <name>sample_CustomAPIExample</name>
</customapi>
```

### See also

[Create and use custom APIs](custom-api.md)   
[CustomAPI tables](custom-api-tables.md)   
[Create a custom API using the plug-in registration tool](create-custom-api-prt.md)   
[Create a custom API in Power Apps](create-custom-api-maker-portal.md)   
[Create a custom API with code](create-custom-api-with-code.md)   
[Create your own messages](custom-actions.md)   


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
