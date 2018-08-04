---
title: "Register a plug-in (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn how to register a plug-in to apply custom business logic to Common Data Service for Apps." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "brandonsimons" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---

# Register a plug-in


The process of writing, registering, and debugging a plug-in is:

1. Create a .NET Framework Class library project in Visual Studio
1. Add the `Microsoft.CrmSdk.CoreAssemblies` NuGet package to the project
1. Implement the <xref:Microsoft.Xrm.Sdk.IPlugin> interface on classes that will be registered as steps.
1. Add your code to the <xref:Microsoft.Xrm.Sdk.IPlugin.Execute*> method required by the interface
    1. Get references to services you need
    1. Add your business logic
1. Sign & build the assembly
1. Test the assembly
    1. **Register the assembly in a test environment**
    1. Test the behavior of the assembly
    1. Verify expected trace logs are written
    1. Debug the assembly as needed

Content in this topic coverts the steps **in bold** above and supports the following tutorials:

- [Tutorial: Write a plug-in](tutorial-write-plug-in.md)
- [Tutorial: Debug a plug-in](tutorial-debug-plug-in.md)
- [Tutorial: Update a plug-in](tutorial-update-plug-in.md)

## Plugin registration tool

You will use the Plugin Registration Tool (PRT) to register your plug-in assemblies and steps.

PRT is one of the tools available for download from NuGet. Follow the instructions in [Download tools from NuGet](download-tools-nuget.md#download-tools-from-nuget). That topic includes instructions to use a PowerShell script to download the latest tools from NuGet.

After you download the PRT, use the steps found in [Connect using the Plug-in Registration tool](tutorial-write-plug-in.md#connect-using-the-plug-in-registration-tool) to connect to your CDS for Apps environment.

## Register an assembly

With CDS for Apps, registering an assembly is the the process of uploading the assembly to the CDS for Apps database. See the instructions found at [Register your assembly](tutorial-write-plug-in.md#register-your-assembly) in the [Tutorial: Write a plug-in](tutorial-write-plug-in.md)

> [!NOTE]
> You will find options related to the *isolation mode* and *location* for the assembly. These refer to options that apply to on-premise deployments. CDS for Apps is not available for on-premises deployments, so you will always accept the default options of **SandBox** and **Database** for these options.

When an assembly is uploaded it is stored in the `PluginAssembly` entity. Most of the properties are set using reflection of the imported entity. The base64 encoded bytes of the assembly is stored in the `Content` attribute. While viewing the **Properties** of the assembly in the PRT, you can only edit the **Description** attribute value.

To view information about registered assemblies without the PRT, you can use the following Web API query in your browser:

```
[org uri]]/api/data/v9.0/pluginassemblies
?$filter=ishidden/Value eq false
&$select=
createdon,
culture,
customizationlevel,
description,
isolationmode,
major,
minor,
modifiedon,
name,
pluginassemblyid,
publickeytoken,
version
```

Or use following FetchXml to retrieve it.

```xml
<fetch>
  <entity name='pluginassembly' >
    <attribute name='createdon' />
    <attribute name='culture' />
    <attribute name='customizationlevel' />
    <attribute name='description' />
    <attribute name='isolationmode' />
    <attribute name='major' />
    <attribute name='minor' />
    <attribute name='modifiedon' />
    <attribute name='name' />
    <attribute name='pluginassemblyid' />
    <attribute name='publickeytoken' />
    <attribute name='version' />
    <filter type='and' >
      <filter>
        <condition attribute='ishidden' operator='eq' value='false' />
      </filter>
    </filter>
  </entity>
</fetch>
```
More information: [Use FetchXML with FetchExpression](org-service/entity-operations-query-data.md#use-fetchxml-with-fetchexpression)

## Register plug-in step

When an assembly is loaded or updated, any classes that implement <xref:Microsoft.Xrm.Sdk.IPlugin> will be available in the PRT. Use the instructions in [Register a new step](tutorial-write-plug-in.md#register-a-new-step) to create a new step registration.

When you register a step, there are many options available to you which depend on the stage of the event pipeline and the nature of the operation you will register your code to respond to.

### General Configuration Information Fields

|Field|Description|
|--|--|
|**Message**|PRT will auto-complete available messages in the system|
|**Primary Entity**|PRT will auto-complete valid entities that apply to the selected message. If valid entities apply, you should set this when you want to limit the number of times the plug-in is called. You can leave it blank for core entity messages like `Create`, `Update`, `Delete`, `Retrieve`, and `RetrieveMultiple` or any message that can be applied with the message. But then the plug-in will be invoked for all the entities that support this message.|
|**Secondary Entity**|This field remains for backward compatibility for long deprecated messages that accepted two entity parameters, and the potential that a future message may require two entities as parameters.|
|**Filtering Attributes**|For `Create` and `Update` messages that have a **Primary Entity** set, filtering attributes limits the execution of the plug-in to cases where the selected attributes are included. This is a best practice for performance. |
|**Event Handler**|This value will be populated based on the name of the assembly. |
|**Step Name**|The name of the step. A value is pre=populated based on the configuration of the step, but this value can be overridden.|
|**Run in User's Context**|Provides options for applying impersonation for the step. The default value is **Calling User**. If the calling user doesn't have privileges to perform operations in the step, you may need to set this to a user who has these privileges.  |
|**Execution Order**|Multiple steps can be registered for the same event. The number in this field determines the order in which they will be applied from lowest to highest.|
|**Description**|A description for step. This value is prepopulated but can be overwritten.|


### Event Pipeline Stage of execution

|Field|Description|
|--|--|
|**x**||
|**x**||


### Execution Mode

|Field|Description|
|--|--|
|**x**||
|**x**||

### Deployment

|Field|Description|
|--|--|
|**x**||
|**x**||




## Set configuration data

## Update an assembly

## Unregister an assembly