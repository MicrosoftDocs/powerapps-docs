---
title: "Manage plug-ins in a single solution | MicrosoftDocs"
description: "The definition of a Plug-in assembly should be maintained within a single solution. You may want to have a separate solution that contains only plug-in definitions to help manage the plugin definitions."
services: ''
suite: powerapps
documentationcenter: na
author: JimDaly
manager: sunilg
editor: ''
tags: ''
ms.service: powerapps
ms.devlang: na
ms.topic: article
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 10/25/2021
ms.subservice: dataverse-developer
ms.author: pehecke
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Manage plug-ins in a single solution

**Category**: Maintainability, Design

**Impact potential**: Low

## Symptoms

When importing a solution that contains a plug-in, you may see an error like this:

```text
ImportSolutionException: Plugin Assemblies import: FAILURE. Error: Plugin: Custom.Xrm.Plugins,
Version=1.2.0.0, Culture=neutral, PublicKeyToken=59f189e458044167 of PluginTypeName: 
Microsoft.Crm.Entities.PluginType and PluginTypeNode: caused an exception.: Plugin Types 
import: FAILURE. Error: Plugin: Custom.Xrm.Plugins, Version=1.2.0.0, Culture=neutral, 
PublicKeyToken=59f189e458044167 of PluginTypeName: Microsoft.Crm.Entities.PluginType caused an 
exception.: PluginType [Custom.Xrm.Plugins.CreateContact] not found in PluginAssembly
```

This error occurs when a new Plug-in Type is added to an existing assembly in the solution and that assembly is also included in a different solution.


## Guidance

The definition of a Plug-in assembly should be maintained within a single solution. You may want to have a separate solution that contains only plug-in definitions to help manage the plug-ins.

## Problematic patterns

Below are two examples of the condition for this error may occur. In both examples, there is a Plug-in Assembly representing the BasicPlugin.dll file. Both examples will fail with error: `PluginType [BasicPlugin.CreateAccount] not found in PluginAssembly`.


### Example 1: Upgrade an existing solution

There are two solutions that include BasicPlugin.dll.

In the target (managed) environment, the BasicPlugin.dll assembly has the following solution layering.


|Layer  |Solution  |Solution Version  |BasicPlugin Types  |
|---------|---------|---------|---------|
|1|AnotherSolution|v1.0.0.0|`UpdateLead`|
|2|PluginSolution|v1.0.0.0|`UpdateLead`|

Then, you update the **PluginSolution**, changing the version to v2.0.0.0, and include a new Plugin Type: `CreateAccount`.

This will fail because the top-level solution component plug-in assembly doesn't contain the new `CreateAccount` Plugin Type.

### Example 2: Install a new solution

In the target (managed) environment, the BasicPlugin.dll assembly has the following solution layering.

|Layer  |Solution  |Solution Version  |BasicPlugin Types  |
|---------|---------|---------|---------|
|1|PluginSolution|v1.0.0.0|`UpdateLead`<br />`CreateAccount`|


When you try to install a new solution, **AnotherSolution** v1.0.0.0, which has a BasicPlugin assembly that contains only plug-in type: `UpdateLead`

The error occurs because the BasicPlugin.dll in this new solution doesn't contain the `CreateAccount` PluginType.

### Remedies

The correct solution is to avoid the situation where the same plug-in assembly is included in multiple solutions.

In both examples above, when the Plug-in Assembly is part of two different solutions, you must maintain consistent Plug-in Types in both solutions. If you continue to maintain both Plug-in assemblies in both solutions, you will need to update both solutions each time you add a new Plugin Type to the assembly.


## Additional information

Solutions can contain Plug-ins. Plug-ins consist of PluginAssembly and PluginType records that are associated with each other.

PluginAssembly contains the binary contents of the assembly. PluginType contains a reference to the class in the assembly that implements the IPlugin interface.

As solution components, plug-ins participate in the solution layering system. If the same assembly is included in two solutions installed on top of each other, the type validations will fail if there are mismatched types within the assemblies. 

### See also

[Solution layers](/power-platform/alm/solution-layers-alm)
