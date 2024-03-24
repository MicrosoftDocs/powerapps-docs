---
title: Build and package plug-in code
description: Learn about building plug-in code into assemblies and packages for later registration and upload to the Microsoft Dataverse service.
ms.date: 03/18/2024
ms.reviewer: pehecke
ms.topic: article
author: divkamath
ms.subservice: dataverse-developer
ms.author: dikamath
search.audienceType: 
  - developer
contributors:
  - phecke
  - JimDaly
---

# Build and package plug-in code

This article describes what you need to know about configuring and building an assembly for your plug-in project. We'll also discuss how to create a plug-in package that can contain your plug-in assembly plus any other require dependent assemblies your plug-in needs at run-time.
  
## Building the plug-in assembly

When building a plug-in project, keep the following output assembly constraints in mind.

### Use .NET Framework 4.6.2

Plug-in and custom workflow activity assembly projects must target .NET Framework 4.6.2. While assemblies built using later versions of the .NET Framework should generally work, if the plug-in code uses any features introduced after 4.6.2, a run-time error will occur.

### Optimize assembly development

Your assembly may include multiple plug-in classes (or types) and even custom workflow activities, but can be no larger than 16 MB in size. It's recommended to consolidate plug-ins and workflow assemblies into a single assembly as long as the size remains below 16 MB.

### Signed assemblies are required

Assemblies must be signed before they can be registered with Dataverse only if you aren't using the [dependent assemblies](#dependent-assemblies) capability. You can use the Visual Studio **Signing** tab in your project's properties or the [Sn.exe (Strong Name Tool)](/dotnet/framework/tools/sn-exe-strong-name-tool) command to sign the assembly.

### Dependency on the CoreAssemblies NuGet package

Adding the `Microsoft.CrmSdk.CoreAssemblies` NuGet package to your project includes the required Dataverse assembly references in your project, but it doesn't upload these assemblies along with your plug-in assembly as these assemblies already exist in the server's sandbox run-time where your code executes.

### Where to go next

If you're interested in learning about or using dependent assemblies, continue reading the next section in this article. If not, proceed to [Register a plug-in](register-plug-in.md).

## Dependent assemblies

The dependent assembly capability can be used to include other required .NET assemblies or resources (for example, localized strings) with your plug-in assembly in a single [NuGet](https://www.nuget.org) package that is uploaded to the Dataverse server during the registration process.

> [!IMPORTANT]
> The dependent assembly capability is so important to plug-in development that you should consider using it from the start even if you do not have an immediate need to do so. Adding support for dependent assemblies to your plug-in project is much more difficult later on in the development cycle.
>
> We do not supported use of ILMerge. This dependent assemblies feature provides a solution we can support with the same functionality as ILMerge and more.

This NuGet package file is stored in the [PluginPackage](reference/entities/pluginpackage.md) table. The contents of the NuGet package is stored in file storage rather than the SQL database.

When you upload your NuGet package, any assemblies containing classes that implement the <xref:Microsoft.Xrm.Sdk.IPlugin> interface are registered in the [PluginAssembly](reference/entities/pluginassembly.md) table and associated with the plug-in package. As you develop and maintain your project, you continue to update the `PluginPackage` table row and changes to the related plug-in assemblies are managed on the server.

At runtime, Dataverse copies the contents of the NuGet package from the `PluginPackage` row and extracts it to the sandbox runtime. This way, any dependent assemblies needed for the plug-in are available.

> [!IMPORTANT]
> The name and version of the plug-in package cannot be changed once created. Attempting to do so using an API call results in an error.

### Signed assemblies are not required

You aren't required to sign plug-in assemblies used in plug-in packages.

When you register individual plug-in assemblies without the dependent assemblies capability, signing is required because it provides a unique name for the assembly. But with plug-in assemblies within a plug-in package, the assemblies are loaded on the sandbox server using a different mechanism, so signing isn't necessary.

> [!IMPORTANT]
> If you sign your assemblies, be aware that signed assemblies cannot use resources contained in unsigned assemblies. If you sign your plug-in assemblies or any dependent assembly, all the assemblies that those assemblies depend on must be signed.
>
> If any signed assemblies depend on unsigned assemblies, you will get an error similar to the following: Could not load file or assembly \<AssemblyName>, Version=\<Version>, Culture=neutral, PublicKeyToken=null or one of its dependencies. A strongly-named assembly is required.

### Dependent assemblies limitations

The following limitations apply when using plug-in dependent assemblies.

- [Workflow extensions](workflow/workflow-extensions.md), also known as *custom workflow activities* aren't supported when using the dependent assemblies capability.
- On-premises environments aren't supported.
- Un-managed code isn't supported. You can't include references to un-managed resources.

## Creating a plug-in package

Your plug-in assembly plus any required dependent assemblies can be placed together in a NuGet package and then registered and uploaded to the Dataverse server. You don't need to create a package if your plug-in project doesn't require any dependent assemblies at run-time, other than what ships in the Microsoft.CrmSdk.CoreAssemblies NuGet package.

<!-- Add correct links when available -->
Instructions for creating a plug-in package using an interactive tool can be found in these separate how-to's: [Create and register a plug-in package using PAC CLI](/power-platform/developer/howto/cli-create-package), [Create and register a plug-in package using Visual Studio](/power-platform/developer/howto/vs-create-package).

## All projects must be in the SDK style

A plug-in package must only contain custom assemblies that are built from a project file in a specific format known as the *SDK style*. Failure to follow this rule results in an error ("file can not be found") when attempting to register the package using the Plug-in Registration tool.

> [!IMPORTANT]
> All MSBuild projects, where the resulting compiled assembly is to be added to a plug-in package, must be in the "SDK style" format.

An SDK style project is one where the contents of the project's .csproj file contains the following line of code: `<Project Sdk="Microsoft.NET.Sdk">`.

When you create a plug-in project using one of our tools, for example the Power Platform CLI `pac plugin init` command, the plug-in project file is in the correct format. Here's an example of such a project file.

```makefile
<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <TargetFramework>net462</TargetFramework>
    <PowerAppsTargetsPath>$(MSBuildExtensionsPath)\Microsoft\VisualStudio\v$(VisualStudioVersion)\PowerApps</PowerAppsTargetsPath>
    <AssemblyVersion>1.0.0.0</AssemblyVersion>
    <FileVersion>1.0.0.0</FileVersion>
    <ProjectTypeGuids>{4C25E9B5-9FA6-436c-8E19-B395D2A65FAF};{FAE04EC0-301F-11D3-BF4B-00C04F79EFBC}</ProjectTypeGuids>
  </PropertyGroup>
  ...
</Project>
```

If you're adding another project to the Visual Studio solution, say a class library project, you can create an SDK style project by following these steps.

1. In Visual Studio, add the new project to your solution using a .NET or .NET Standard template. Do not target .NET Framework.
1. Edit the project file by right-clicking on the project name in Solution Explorer and select **Edit project file**, or simply open the project's .csproj file in a separate editor.
1. You should see the line `<Project Sdk="Microsoft.NET.Sdk">` in the project file. Change the TargetFramework property to be `<TargetFramework>net462</TargetFramework>` and save the file.
1. Verify your solution builds, and you're done.

More information: [.NET Project SDKs](/dotnet/core/project-sdk/overview#project-files)

### Don't depend on System.Text.Json

Because the Microsoft.CrmSdk.CoreAssemblies NuGet package has a [dependency](https://www.nuget.org/packages/Microsoft.CrmSdk.CoreAssemblies#dependencies-body-tab) on System.Text.Json, you're able to refer to [System.Text.Json](xref:System.Text.Json) types at design time. However, the System.Text.Json.dll file in the sandbox run-time can't be guaranteed to be the same version that you reference in your project. If you need to use `System.Text.Json`, you should use the dependent assembly feature and explicitly include it in your NuGet package.

### See also

[Use plug-ins to extend business processes](plug-ins.md)  

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
