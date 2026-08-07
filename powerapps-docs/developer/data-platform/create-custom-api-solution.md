---
title: "Create a custom API with solution files"
description: "Learn how to create a custom API by adding definition files to a Dataverse solution project and using Microsoft Power Platform CLI."
ms.date: 08/03/2026
ms.reviewer: jdaly
ms.topic: how-to
author: kewear
ms.author: kewear
ms.subservice: dataverse-developer
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

This article demonstrates how to create a custom API by adding definition files to a Microsoft Dataverse solution project. This approach is useful for solution publishers who store [solution files in source control](/power-platform/alm/use-source-control-solution-files) and apply application lifecycle management (ALM) practices.

Use [Microsoft Power Platform CLI](/power-platform/developer/cli/introduction) to initialize the solution project, build the solution package, and import it into a Dataverse environment. You don't need to create or export an empty solution first.

## Prerequisites

- Install [Microsoft Power Platform CLI](/power-platform/developer/cli/introduction#install-microsoft-power-platform-cli).
- Install a [.NET SDK](https://dotnet.microsoft.com/download) that includes the `dotnet` command.
- Have access to a Dataverse environment where you have privileges to import solutions.

## Step 1: Initialize a solution project

From the folder where you want to create the project, run the following command:

```powershell
pac solution init --publisher-name Samples --publisher-prefix sample --outputDirectory CustomAPIExample
```

The [pac solution init](/power-platform/developer/cli/reference/solution#pac-solution-init) command creates a `CustomAPIExample` folder that contains:

- `CustomAPIExample.cdsproj`: The Dataverse solution project file.
- `src\Other\Solution.xml`: The solution and publisher definition.
- `src\Other\Customizations.xml`: The solution customizations definition.
- `src\Other\Relationships.xml`: The solution relationships definition.

The output directory name becomes the solution unique name. Verify the generated values in `src\Other\Solution.xml` before you continue.

> [!NOTE]
> The publisher name and customization prefix must meet the requirements described for [pac solution init](/power-platform/developer/cli/reference/solution#pac-solution-init). Use values for an existing publisher in the target environment or a new publisher that you want to create.

## Step 2: Add the definition of the custom API

All custom APIs in a solution are found within a folder named **customapis**. Within that folder, each custom API is in a folder named after the custom API `UniqueName` property. The data representing the custom API is in an XML file named `customapi.xml`.

1. In the `CustomAPIExample\src` folder, create a new folder named `customapis`.
1. In the **customapis** folder, create a folder with the `UniqueName` of the custom API you want to create. For this example, we use `sample_CustomAPIExample`.
1. In the **sample_CustomAPIExample** folder you created, create a file named `customapi.xml`.
1. Edit the `customapi.xml` to set the properties of the custom API you want to create. For this example, use the following XML:
   
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

If you already have a plug-in type that you want to associate with this custom API, include a reference to it in this definition by adding the following element within the `<customapi>` element:

```xml
<plugintypeid>
  <plugintypeexportkey>{Add the GUID value of the plug-in type export key}</plugintypeexportkey>
</plugintypeid>
```

or

```xml
<plugintypeid>
  <plugintypeid>{Add the GUID value of the plug-in type ID}</plugintypeid>
</plugintypeid>
```

> [!NOTE]
> Either value will work, but we recommend you use the `plugintypeexportkey`.

To retrieve the [PluginTypeExportKey](reference/entities/plugintype.md#BKMK_PluginTypeExportKey) and [PluginTypeId](reference/entities/plugintype.md#BKMK_PluginTypeId) values, use a Web API query when you know the name of the plug-in type:

```http
GET [Organization Uri]/api/data/v9.2/plugintypes?$select=name,plugintypeid,plugintypeexportkey&$filter=contains(name,'MyPlugin.TypeName')
```

## Step 3: Add any custom API request parameters

Include definitions of request parameters for the custom API in a folder called `customapirequestparameters`. Within that folder, each custom API request parameter is in a folder named after its `UniqueName` property.

1. If your custom API has any request parameters, within the `CustomAPIExample\src\customapis\sample_CustomAPIExample` folder, create a folder named `customapirequestparameters`.
1. For each custom API Request Parameter, create a new folder using the `UniqueName` property of the custom API Request Parameter. For this example, we use `StringParameter`.
1. Within the folder, add an XML file named `customapirequestparameter.xml`.
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

    See [Custom API request parameter table columns](custom-api-tables.md#customapirequestparameter-table-columns) to set the values of the elements.

## Step 4: Add any custom API response properties

You define response properties for the custom API in a folder named `customapiresponseproperties`. Each custom API response property resides in its own folder, which is named after the property's `UniqueName` value.

1. If your custom API includes response properties, create a `customapiresponseproperties` folder inside `CustomAPIExample\src\customapis\sample_CustomAPIExample`.
1. For each custom API Response Property, create a new folder using the `UniqueName` property of the custom API Response Property. For this example, we use `StringProperty`.
1. Add an XML file named `customapiresponseproperty.xml` to the folder.
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

    To set the values of the elements, see [Custom API response property table columns](customapiresponseproperty-table-columns.md).

> [!NOTE]
> While the schema for request parameters and response properties is very similar, note that `isoptional` is not valid for a response property and will cause an error when you try to import the solution.

## Step 5: Review the solution project structure

Your solution project should have this structure:

```text
CustomAPIExample
|   CustomAPIExample.cdsproj
|
\---src
    +---customapis
    |   \---sample_CustomAPIExample
    |       |   customapi.xml
    |       |
    |       +---customapirequestparameters
    |       |   \---StringParameter
    |       |           customapirequestparameter.xml
    |       |
    |       \---customapiresponseproperties
    |           \---StringProperty
    |                   customapiresponseproperty.xml
    |
    \---Other
            Customizations.xml
            Relationships.xml
            Solution.xml
```

## Step 6: Build the solution

From the `CustomAPIExample` project folder, run:

```powershell
dotnet build
```

The build process restores the required packages and creates the unmanaged solution package at `bin\Debug\CustomAPIExample.zip`.

## Step 7: Import the solution

> [!IMPORTANT]
> You need an authenticated PAC CLI session to the Dataverse environment. 

If you already have authentication profiles, use [pac auth list and pac auth select](/power-platform/developer/cli/reference/auth#switch-to-another-authentication-profile) to select the profile for the target environment. 

If you don't have any authentication profiles, [learn to connect to your environment](/power-platform/developer/cli/introduction#connect-to-your-tenant).

1. From the `CustomAPIExample` project folder, import and publish the solution:

   ```powershell
   pac solution import --path .\bin\Debug\CustomAPIExample.zip --publish-changes
   ```

Wait for the import to complete.

> [!NOTE]
> You might see an error if another solution is being installed at the same time. For more information, see [Concurrent solution operation failures](/troubleshoot/power-platform/dataverse/working-with-solutions/concurrent-solution-operation-failures).  The resolution is typically to try again later.

## Step 8: Verify that the custom API was added to your solution

In [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), open the **CustomAPIExample** solution and verify that the custom API and the associated request parameters and response properties are included.

:::image type="content" source="media/customapi-solution-installed-successfully.png" alt-text="Showing that the solution component installed successfully.":::

At this point, you can test your API by using the steps described in [Test your custom API](create-custom-api-maker-portal.md#test-your-custom-api).
At this point, you can test your API by using the steps described in [Test your custom API](create-custom-api-maker-portal.md#test-your-custom-api).
## Update a custom API in a solution

After you ship a solution that contains a custom API, you may want to make some changes to the custom API in your unmanaged solution. You can add new parameters or response properties and make changes to those columns that support being updated, such as the `displayname` and `description`.

Before you build and import an updated solution, set the revision to a value greater than the version that is already installed. For example, run these commands from the solution project folder:

```powershell
pac solution version --revisionversion 2 --solutionPath .\src
dotnet build
pac solution import --path .\bin\Debug\CustomAPIExample.zip --publish-changes
```

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
> - Custom API request parameter properties:
>    - `isoptional`
>    - `logicalentityname`
>    - `type`
>    - `uniquename`
> - Custom API response property properties:
>    - `logicalentityname`
>    - `type`
>    - `uniquename`
>
> For more information, see [CustomAPI tables](custom-api-tables.md).
> For more information, see [CustomAPI tables](custom-api-tables.md).
## Provide localized labels with the solution

Instead of using the process described in [Localized Label values](custom-api.md#localized-label-values), you can provide translations directly in the solution files for custom API entities. For example, if you want to provide Japanese localized labels for your custom API, you can provide them for the `description` and `displayname` properties as shown in the following example:
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

- [Create and use custom APIs](custom-api.md)
- [CustomAPI tables](custom-api-tables.md)
- [Create a custom API using the plug-in registration tool](create-custom-api-prt.md)
- [Create a custom API in Power Apps](create-custom-api-maker-portal.md)
- [Create a custom API with code](create-custom-api-with-code.md)
- [Create your own messages](custom-actions.md)
- [Microsoft Power Platform CLI solution command group](/power-platform/developer/cli/reference/solution)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
