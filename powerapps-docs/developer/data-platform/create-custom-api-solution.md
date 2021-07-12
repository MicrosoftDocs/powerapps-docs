---
title: "Create a Custom API with solution files (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "You can write create custom APis by editing solution files." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 03/13/2021
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

> [!NOTE]
> This is an advanced topic that assumes you have already read and understood these topics:
> - [Create and use Custom APIs](custom-api.md)
> - [Create a Custom API in the maker portal](create-custom-api-maker-portal.md)


While you can create Custom APIs through a designer or with code, you can also define them by working with files within a solution. This may be the preferred option for solution publishers who apply the recommended best practices for Application Lifecycle Management (ALM).

A solution file is a compressed (zip) file that has been exported from a Microsoft Dataverse instance. The contents of this file can be extracted and the components checked into a source repository. The contents can be edited and then compressed again. The changes applied to the solution will then be part of the solution and will be created when the solution is imported.

> [!NOTE]
> These processes are typically automated with tools and processes that are beyond the scope of this topic. This topic will focus on the simple scenario of creating a Custom API by manually manipulating the extracted files in a solution to demonstrate how the data in the files can be used to create Custom API. More information: [Source control with solution files](/power-platform/alm/use-source-control-solution-files)

## Step 1: Create an Unmanaged solution

You should not try to compose a solution file manually. Use the tools in [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) to generate a solution file. Use the steps in the following topics to create and export a solution. The solution doesn't need to contain any solution components.

1. [Create a solution](../../maker/data-platform/create-solution.md)

    For this example, the solution is defined simply like this:

    :::image type="content" source="media/custom-api-solution.png" alt-text="An empty solution.":::

1. [Export solutions](../../maker/data-platform/export-solutions.md)

    For this example, make sure you export an unmanaged solution. Managed solution is the default.

    :::image type="content" source="media/export-empty-unmanaged-solution.png" alt-text="Option to select to export an unmanaged solution.":::
    
You can find the exported file in your downloads folder. It will have a name that depends on the name and version of the solution, in this case: `CustomAPIExample_1_0_0_2.zip`.

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

1. Update the value by 1. In this example, it will be `<Version>1.0.0.2</Version>`.
1. Save the file.

## Step 3: Add the definition of the Custom API

All Custom APIs in a solution are found within a folder named **customapis**. Within that folder each Custom API will be in a folder named after the Custom API `UniqueName` property.
Within the folder, the data representing the Custom API is found within an XML file named `customapi.xml`

1. In the folder with the extracted files, create a new folder named `customapis`.
1. In the **customapis** folder, create a folder with the `UniqueName` of the Custom API you want to create. For this example we will use `sample_CustomAPIExample`.
1. In the **sample_CustomAPIExample** folder you created, create a file named `customapi.xml`.
1. Edit the customapi.xml to set the properties of the custom API you want to create. For this example, we will use the following:
    ```xml
    <customapi uniquename="sample_CustomAPIExample">
      <allowedcustomprocessingsteptype>0</allowedcustomprocessingsteptype>
      <bindingtype>0</bindingtype>
      <boundentitylogicalname />
      <description default="A simple example of a Custom API">
        <label description="A simple example of a Custom API" languagecode="1033" />
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

  See the information in [CustomAPI Table Columns](customapi-table-columns.md) to set the values of the elements.
      
  > [!NOTE]
  > If you already have a Plug-in Type that you want to associate with this Custom API, you can include a reference to it in this definition by adding the following element within the  `<customapi>` element:
  >
  >  ```xml
  >    <plugintypeid>
  >      <plugintypeid>{Add the GUID value of the plug-in type id}</plugintypeid>
  >    </plugintypeid>
  >  ```
  >
  >  You can retrieve the Plug-in Type Id using a Web API query like this where you know the name of the plug-in type:
  >
  >  ```http
  >  GET https://yourorg.crm.dynamics.com/api/data/v9.1/plugintypes?$select=name&$filter=contains(name,'MyPlugin.TypeName')
  >  ```

## Step 4: Add any Custom API Request Parameters

Any definitions of request parameters for the Custom API are included in a folder called `customapirequestparameters`. Within that folder each Custom API Request Parameter will be in a folder named after the Custom API Request Parameter `UniqueName` property.

1. If your Custom API has an request parameters, within the folder for the Custom API you created in the previous step, create a folder named `customapirequestparameters`.
1. For each Custom API Request Parameter, create a new folder using the `UniqueName` property of the Custom API Request Parameter. For this example we will use `StringParameter`.
1. Within the folder, add an xml file named `customapirequestparameter.xml`.
1. Edit the **customapirequestparameter.xml** file to set the properties of the Custom API you want to create. For this example, we will use the following:

  ```xml
  <customapirequestparameter uniquename="StringParameter">
    <description default="The StringParameter request parameter for Custom API Example">
      <label description="The StringParameter request parameter for Custom API Example" languagecode="1033" />
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

See the information in [CustomAPIRequestParameter Table Columns](customapirequestparameter-table-columns.md) to set the values of the elements.

## Step 5: Add any Custom API Response Properties

Any definitions of response properties for the Custom API are included in a folder called `customapiresponseproperties`. Within that folder each Custom API Response Property will be in a folder named after the Custom API Response Property  `UniqueName` property.

1. If your Custom API has an response properties, within the folder for the Custom API you created in [Step 3: Add the definition of the Custom API](#step-3-add-the-definition-of-the-custom-api), create a folder named `customapiresponseproperties`.
1. For each Custom API Response Property, create a new folder using the `UniqueName` property of the Custom API Response Property. For this example we will use `StringProperty`.
1. Within the folder, add an xml file named `customapiresponseproperty.xml`.
1. Edit the **customapiresponseproperty.xml** file to set the properties of the Custom API you want to create. For this example, we will use the following:

  ```xml
  <customapiresponseproperty uniquename="StringProperty">
    <description default="The StringProperty response property for Custom API Example">
      <label description="The StringProperty response property for Custom API Example" languagecode="1033" />
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
1. You can re-name the resulting file to be anything you want. For this example, rename it to match the original exported solution file: `CustomAPIExample_1_0_0_2.zip`.

## Step 7: Import the solution with the definition of your Custom API

1. Return to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) and select **Solutions**.
1. Select **Import** and follow the instructions to select the solution file you created in the previous step.

    :::image type="content" source="media/import-solution-with-customapi.png" alt-text="Import the solution file.":::

    > [!NOTE]
    > If you see a warning saying **This version of the solution package is already installed**, you must not have updated the `Version` element of the solution.xml as described in [Step 2: Extract the contents of the solution and update the version](#step-2-extract-the-contents-of-the-solution-and-update-the-version).

1. You should see a warning saying **This solution package contains an update for a solution that is already installed**. Click **Import** to continue.
1. Wait a few minutes while the solution import completes. 

  > [!NOTE]
  > It is possible you will see an error if another solution is being installed at the same time. More information: [The solution installation or removal failed due to the installation or removal of another solution at the same time](https://support.microsoft.com/help/4343228/the-solution-installation-or-removal-failed-due-to-the-installation-or)

## Step 8: Verify that the Custom API was added to your solution

Open the solution you created and verify that the Custom API and the associated request parameters and response properties are included.

:::image type="content" source="media/customapi-solution-installed-successfully.png" alt-text="Showing that the solution component installed successfully.":::

At this point, you can test your API using the steps describe in [Test your Custom API](create-custom-api-maker-portal.md#test-your-custom-api)


## Providing Localized Labels with the solution

As an alternative to using the process described in [Localized Label values](custom-api.md#localized-label-values), if you are editing the solution files for Custom API entities, you can provide translations directly in these files. For example if you want to provide Japanese localized labels for your Custom API, you can provide them for the `description` and `displayname` properties as shown below

```xml
<customapi uniquename="sample_CustomAPIExample">
  <allowedcustomprocessingsteptype>0</allowedcustomprocessingsteptype>
  <bindingtype>0</bindingtype>
  <description default="A simple example of a Custom API">
    <label description="A simple example of a Custom API" languagecode="1033" />
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

[Create and use Custom APIs](custom-api.md)<br />
[Create a Custom API in the maker portal](create-custom-api-maker-portal.md)<br />
[Create a Custom API with code](create-custom-api-with-code.md)<br />
[Create your own messages](custom-actions.md)<br />


[!INCLUDE[footer-include](../../includes/footer-banner.md)]