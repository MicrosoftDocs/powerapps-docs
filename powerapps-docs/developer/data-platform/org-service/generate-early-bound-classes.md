---
title: "Generate early-bound classes for the SDK for .NET"
description: "Learn how to use the Power Platform CLI pac modelbuilder build command to generate early-bound classes for use with the Microsoft Dataverse SDK for .NET. This tool generates early-bound .NET classes that represent the Entity Data Model used by Dataverse."
ms.date: 04/22/2025
author: MicroSri
ms.author: sriknair
ms.reviewer: pehecke
ms.topic: article
search.audienceType: 
  - developer
contributors:
 - JimDaly
 - phecke
 - daryllabar
---

# Generate early-bound classes for the SDK for .NET

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

Creating early-bound classes for your .NET projects:

- Improves code readability and maintainability.
- Decreases the risk of errors because they provide compile time type checking.
- Improves developer productivity because developers can discover tables, columns, and choice options using IntelliSense.
- Provides the [OrganizationServiceContext](xref:Microsoft.Xrm.Sdk.Client.OrganizationServiceContext) class so you can write Dataverse queries using LINQ and other capabilities work with data.

Learn more:

- [Late and early-bound programming](early-bound-programming.md)
- [Use OrganizationServiceContext](organizationservicecontext.md)

Use the [Power Platform CLI pac modelbuilder build command](/power-platform/developer/cli/reference/modelbuilder#pac-modelbuilder-build) to generate early-bound code classes. You can also use the `CrmSvcUtil.exe` code generation tool, but for Dataverse we recommend using the `pac modelbuilder build` command. [Learn how to use the CrmSvcUtil.exe to generate early-bound classes for the SDK for .NET](/dynamics365/customerengagement/on-premises/developer/org-service/create-early-bound-entity-classes-code-generation-tool)

Like many Power Platform CLI commands, `pac modelbuilder build` has many parameters you can use to control the outcome. In this article, we recommend that you start by using the  `--settingsTemplateFile` parameter for most use cases. Use this parameter to refer to a JSON file where all the other available settings can be controlled. This way, you don't need to compose a long list of parameters, and the configuration appropriate for your project can be updated to allow regeneration of the classes when you need them.

Of course, you can still use the build command with parameters if you prefer. See [Using parameters](#using-parameters).

## Get started

Before you begin:

1. [Install Power Platform CLI](/power-platform/developer/cli/introduction#install-microsoft-power-platform-cli).
1. Connect to your environment using [Power Platform CLI pac auth commands](/power-platform/developer/cli/reference/auth).

Use the following steps to get started:

1. In your .NET project, add a NuGet package reference to either:

   - For a client application: [Microsoft.PowerPlatform.Dataverse.Client](https://www.nuget.org/packages/Microsoft.PowerPlatform.Dataverse.Client)
   - For a Dataverse plug-in project:  [Microsoft.CrmSdk.CoreAssemblies](https://www.nuget.org/packages/Microsoft.CrmSdk.CoreAssemblies)

1. Create a folder called `model`.
1. In the `model` folder, add a `builderSettings.json` file with the following settings:

   ```json
   {
   "emitentityetc-comment": "Generate a constants structure that contains all of the field names by entity at the time of code generation.",
   "emitEntityETC": false,
   "emitfieldsclasses-comment": "Generate a constants structure that contains all of the field names by entity at the time of code generation.",
   "emitFieldsClasses": false,
   "emitvirtualattributes-comment": "When set, includes the Virtual Attributes of entities in the generated code.",
   "emitVirtualAttributes": false,
   "entitynamesfilter-comment": "Filters the list of entities are retrieved when reading data from Dataverse.",
   "entityNamesFilter": [
      "account",
      "contact"
   ],
   "entitytypesfolder-comment": "Folder name that contains entities.",
   "entityTypesFolder": "Entities",
   "generateGlobalOptionSets-comment": "Emit all Global OptionSets. Note: If an entity contains a reference to a global optionset, it is emitted even if this switch is not present.",
   "generateGlobalOptionSets": false,
   "generatesdkmessages-comment": "When set, emits Sdk message classes as part of code generation",
   "generateSdkMessages": true,
   "language-comment": "The language to use for the generated proxy code. This value can be either 'CS' or 'VB'. The default language is 'CS'.",
   "language": "CS",
   "logLevel-comment": "Log level. The default value is 'Off'.",
   "logLevel": "Off",
   "messagenamesfilter-comment": "Filters the list of messages that are retrieved when reading data from Dataverse.",
   "messageNamesFilter": [
      "searchautocomplete",
      "searchquery",
      "sample_*"
   ],
   "messagestypesfolder-comment": "Folder name that contains messages.",
   "messagesTypesFolder": "Messages",
   "namespace-comment": "The namespace for the generated code.",
   "namespace": "ExampleProject",
   "optionsetstypesfolder-comment": "Folder name that contains option sets.",
   "optionSetsTypesFolder": "OptionSets",
   "serviceContextName-comment": "The name for the generated service context. If a value is passed in, it's used for the Service Context. If not, no Service Context is generated.",
   "serviceContextName": "OrgContext",
   "suppressGeneratedCodeAttribute-comment": "When set, this suppress all generated objects being tagged with the code generation engine and version",
   "suppressGeneratedCodeAttribute": true,
   "suppressINotifyPattern-comment": "When enabled, doesn't write the INotify wrappers for properties and classes.",
   "suppressINotifyPattern": true
   }
   ```

   > [!NOTE]
   > This file is a modified version of the file you can generate using `pac modelbuilder build` with the [`--writesettingsTemplateFile` parameter](/power-platform/developer/cli/reference/modelbuilder#--writesettingstemplatefile--wstf). Learn how to generate the file without comments in [Using parameters](#using-parameters).

1. Use the following command to generate early bound classes for the connected environment using the settings defined in `builderSettings.json` where `C:\projects\exampleproject\` represents the path to your project and `model` is the folder you created.

   ```powershell
   PS C:\projects\exampleproject\model> pac modelbuilder build -o . -stf .\builderSettings.json
   ```

   This command uses these parameters:

   - `-o` shortcut for the required [`--outdirectory` parameter](/power-platform/developer/cli/reference/modelbuilder#--outdirectory--o) with a value of `.`, to indicate the current directory.
   - `-stf` shortcut for the [`--settingsTemplateFile` parameter](/power-platform/developer/cli/reference/modelbuilder#--settingstemplatefile--stf) with a value of `.\builderSettings.json`, to indicate the `builderSettings.json` current directory.

   You could also use this command from the `exampleproject` directory:

   ```powershell
   PS C:\projects\exampleproject>pac modelbuilder build -o model -stf model\builderSettings.json
   ```

### Understand what files are written

With either command, the following output is what you should expect:

```powershell
Connected to... Your Organization
Connected as you@yourorganization.onmicrosoft.com
Begin reading metadata from MetadataProviderService
      Begin Reading Metadata from Server
      Read 2 Entities - 00:00:00.732
      Read 0 Global OptionSets - 00:00:00.000
      Read 12 SDK Messages - 00:00:00.889
      Completed Reading Metadata from Server - 00:00:01.694
Completed reading metadata from MetadataProviderService - 00:00:01.697
Begin Writing Code Files
      Processing 2 Entities
      Wrote 2 Entities - 00:00:00.0625873
      Processing 12 Messages
      Wrote 3 Message(s). Skipped 9 Message(s) - 00:00:00.0091589
      Processing 0 Global OptionSets
      Wrote 0 Global OptionSets - 00:00:00.0000045
      Code written to C:\projects\exampleproject\model\Entities\account.cs.
      Code written to C:\projects\exampleproject\model\Entities\contact.cs.
      Code written to C:\projects\exampleproject\model\Messages\searchquery.cs.
      Code written to C:\projects\exampleproject\model\Messages\searchautocomplete.cs.
      Code written to C:\projects\exampleproject\model\OrgContext.cs.
      Code written to C:\projects\exampleproject\model\EntityOptionSetEnum.cs.
Completed Writing Code Files - 00:00:00.116
Generation Complete - 00:00:01.815
PS C:\projects\exampleproject\model>
```

When you inspect the output, notice that it only generates classes for the tables specified by `entityNamesFilter` and only the messages specified in the `messageNamesFilter`. You should specify which tables (entities) and messages you use in your project. Otherwise, classes for all tables and messages are generated.

For `messageNamesFilter`, you can use `*` as a wildcard character in these values. This filter is useful when messages in your solution share a common customization prefix.

`pac modelbuilder build` writes the files into folders with names you can control in the settings file:

- Entity classes are written to the folder specified by the `entityTypesFolder` setting.
- Message classes are written to the folder specified by the `messagesTypesFolder` setting.
- The [OrganizationServiceContext](xref:Microsoft.Xrm.Sdk.Client.OrganizationServiceContext) class is written to a file with the name specified by the `serviceContextName` setting.
- All the classes are part of the namespace you set in the `namespace` setting.

> [!NOTE]
> If you're generating message classes, you should always include a name for the `serviceContextName` setting. See [Include `serviceContextName` when generating message classes](#include-servicecontextname-when-generating-message-classes)

This is how the files and folders appear in Visual Studio:

:::image type="content" source="../media/pac-modelbuilder-build-output-example-visual-studio.png" alt-text="Example output from pac modelbuilder build command in Visual Studio Explorer":::

With these files written to your project, you're now ready to use early-bound classes.

If you want to change them, delete the files in the `model` folder other than `builderSettings.json`, change the settings in `builderSettings.json`, and generate them again.

## Using parameters

It isn't required to use the `builderSettings.json` settings file and the `--settingsTemplateFile` parameter with `pac modelbuilder build`. You can invoke the command using parameters directly. You can find reference documentation and examples in the [pac modelbuilder build reference documentation](/power-platform/developer/cli/reference/modelbuilder#pac-modelbuilder-build).

If you're using the `builderSettings.json` settings file and the `--settingsTemplateFile` parameter, you can use the parameters in the command line to override the settings.

Here's an example showing how to generate files with the same settings as the example in the [Get started section](#get-started) using parameters:

```powershell
PS C:\>pac modelbuilder build `
   --outdirectory C:\projects\exampleproject\model `
   --entitynamesfilter 'account;contact' `
   --generatesdkmessages `
   --messagenamesfilter 'searchautocomplete;searchquery;sample_*' `
   --namespace ExampleProject `
   --serviceContextName OrgContext `
   --suppressGeneratedCodeAttribute `
   --suppressINotifyPattern `
   --writesettingsTemplateFile
```

This example doesn't include all the settings because it uses the default options. If you use the [`--writesettingsTemplateFile` parameter](/power-platform/developer/cli/reference/modelbuilder#--writesettingstemplatefile--wstf) to generate a `builderSettings.json` file, it doesn't include the comments in the example in the [Get started section](#get-started) of this article. The example using parameters writes the following `builderSettings.json` file in the `model` folder:

```json
{
  "suppressINotifyPattern": true,
  "suppressGeneratedCodeAttribute": true,
  "language": "CS",
  "namespace": "ExampleProject",
  "serviceContextName": "OrgContext",
  "generateSdkMessages": true,
  "generateGlobalOptionSets": false,
  "emitFieldsClasses": false,
  "entityTypesFolder": "Entities",
  "messagesTypesFolder": "Messages",
  "optionSetsTypesFolder": "OptionSets",
  "entityNamesFilter": [
    "account",
    "contact"
  ],
  "messageNamesFilter": [
    "searchautocomplete",
    "searchquery",
    "sample_*"
  ],
  "emitEntityETC": false,
  "emitVirtualAttributes": false
}
```

## Include `serviceContextName` when generating message classes

If you're generating message classes, you should always include a name for the `serviceContextName` parameter so that an [OrganizationServiceContext](xref:Microsoft.Xrm.Sdk.Client.OrganizationServiceContext) class is generated with your code.
This class includes an important property to enable use of generated message classes. If you don't include an `OrganizationServiceContext`, you'll get the following error when you try to use the generated message classes.

```
The formatter threw an exception while trying to deserialize the message: 
There was an error while trying to deserialize parameter http://schemas.microsoft.com/xrm/2011/Contracts/Services:request. 
The InnerException message was 'Error in line 1 position 700. Element 'http://schemas.microsoft.com/xrm/2011/Contracts/Services:request' contains data from a type that maps to the name 'http://schemas.microsoft.com/xrm/2011/new/:<your generated class name>'. 
The deserializer has no knowledge of any type that maps to this name. 
Consider changing the implementation of the ResolveName method on your DataContractResolver to return a non-null value for name '<your generated class name>' and namespace 'http://schemas.microsoft.com/xrm/2011/new/'.'.  
Please see InnerException for more details.
```

## Community tools

The [Early Bound Generator V2](https://www.xrmtoolbox.com/plugins/DLaB.Xrm.EarlyBoundGeneratorV2/) is an XrmToolBox plug-in created by the community to provide a user interface that generates the correct `builderSettings.json` file, and calls `pac modelbuilder build` command for the user. Since the UI is only used to generate the `builderSettings.json` and call the `pac modelbuilder build` command, it can still be ran via the command line in a pipeline without a dependency on the XrmToolBox. It also provides configuration options that the `pac modelbuilder` doesn't. For example, the ability to explicitly control class/properties casing and language specific transliteration of characters. Early Bound Generator V2 can do this using the extensibility features of the `pac modelbuilder`.

> [!NOTE]
> Microsoft doesn't extend support to community developed tools.
> If you have questions pertaining to the tool, contact the publisher. More Information: [XrmToolBox](https://www.xrmtoolbox.com).

## For Dynamics 365 Customer Engagement on-premises

The Power Platform CLI isn't available for Dynamics 365 Customer Engagement on-premises. You need to use the `CrmSvcUtil.exe` code generation tool to generate early bound classes. [Learn how to use the CrmSvcUtil.exe to generate early-bound classes for the SDK for .NET](/dynamics365/customerengagement/on-premises/developer/org-service/create-early-bound-entity-classes-code-generation-tool)

### Related articles

[Late-bound and early-bound programming](early-bound-programming.md)  
[Sample: Early-bound table operations](samples/early-bound-entity-operations.md)  
[Developer tools and resources](../developer-tools.md)  
[Dataverse development tools](../download-tools-NuGet.md)  
[Learn how to use the CrmSvcUtil.exe to generate early-bound classes for the SDK for .NET](/dynamics365/customerengagement/on-premises/developer/org-service/create-early-bound-entity-classes-code-generation-tool)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
