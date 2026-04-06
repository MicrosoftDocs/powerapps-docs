---
title: Build and package plug-in code
description: "Learn how to build and package plug-in code for Microsoft Dataverse. Understand assembly constraints, dependent assembly limitations, and NuGet packaging. Get started today."
ms.date: 03/30/2026
ms.topic: how-to
author: MsSQLGirl
ms.author: jukoesma
ms.reviewer: pehecke
ms.subservice: dataverse-developer
search.audienceType:
  - developer
contributors:
  - phecke
  - JimDaly
ms.custom:
  - ai-gen-docs-bap
  - ai-gen-desc
  - ai-seo-date:11/16/2023
  - bap-template
---

# Build and package plug-in code

This article describes the constraints and limitations you need to know when building and packaging plug-in code for Microsoft Dataverse, including assembly constraints, dependent assembly requirements, and NuGet packaging options.
  
## Plug-in assembly constraints

When you build a plug-in project, keep the following output assembly constraints in mind.

### Use .NET Framework 4.6.2

Plug-in and custom workflow activity assembly projects must target .NET Framework 4.6.2.

> [!NOTE]
> Official Microsoft [support](/lifecycle/products/microsoft-net-framework) for .NET Framework 4.6.2 ends on January 12, 2027. Microsoft plans to introduce Dataverse plug-in support for the .NET Framework 4.8 runtime sometime during the fourth quarter of 2026.

### Limit assemblies to 16 MB

Your assembly can include multiple plug-in classes or types and even custom workflow activities, but it can't be larger than 16 MB. As a best practice, consolidate plug-ins and workflow assemblies into a single assembly, as long as the size remains below 16 MB.

### Sign assemblies before registering them

If you don't use the [dependent assemblies](#dependent-assemblies) capability, you must sign assemblies before you register them with Dataverse. To sign the assembly, use the Visual Studio **Signing** tab in your project's properties or the [Sn.exe (Strong Name Tool)](/dotnet/framework/tools/sn-exe-strong-name-tool) command.

### NuGet CoreAssemblies are in the sandbox

If you add the `Microsoft.CrmSdk.CoreAssemblies` [NuGet](https://www.nuget.org) package to your project, the required Dataverse assembly references are added. However, the assemblies themselves aren't uploaded with your plug-in assembly. They already exist in the server's sandbox runtime where your code executes.

## Dependent assemblies

> [!IMPORTANT]
> The dependent assembly capability is so important to plug-in development that you should consider using it from the start, even if you don't have an immediate need. Adding support for dependent assemblies to your plug-in project is much more difficult later in the development cycle.
>
> Microsoft doesn't support ILMerge. The dependent assemblies capability offers the same functionality as ILMerge and more.

Use the dependent assembly capability to include other required .NET assemblies or resources, like localized strings, with your plug-in assembly in a single [NuGet](https://www.nuget.org) package that's uploaded to the Dataverse server during registration.

The NuGet package file is stored in the [`PluginPackage`](reference/entities/pluginpackage.md) table. The contents of the package are stored in file storage rather than in the SQL database.

When you upload your NuGet package, any assemblies that contain classes that implement the <xref:Microsoft.Xrm.Sdk.IPlugin> interface are registered in the [`PluginAssembly`](reference/entities/pluginassembly.md) table and associated with the plug-in package. As you develop and maintain your project, you continue to update the `PluginPackage` table row and changes to the related plug-in assemblies are managed on the server.

At runtime, Dataverse copies the contents of the NuGet package from the `PluginPackage` row and extracts it to the sandbox runtime. This way, any dependent assemblies needed for the plug-in are available.

> [!IMPORTANT]
> You can't change the name and version of the plug-in package (on the server) once created. Attempting to do so by using an API call results in an error.

### Signed assemblies aren't required

You don't need to sign plug-in assemblies used in plug-in packages.

When you register individual plug-in assemblies without the dependent assemblies capability, signing is required because it provides a unique name for the assembly. But with plug-in assemblies in a plug-in package, the assemblies load on the sandbox server by using a different mechanism, so signing isn't necessary.

> [!IMPORTANT]
> If you sign your assemblies, be aware that signed assemblies can't use resources that are contained in unsigned assemblies. If you sign your plug-in assemblies or any dependent assembly, all the assemblies that those assemblies depend on must be signed.
>
> If any signed assemblies depend on unsigned assemblies, you get an error like this: "Could not load file or assembly *AssemblyName*, Version=*Version*, Culture=neutral, PublicKeyToken=null or one of its dependencies. A strongly-named assembly is required."

### Dependent assemblies limitations

The following limitations apply when you use plug-in dependent assemblies:

- [Workflow extensions](workflow/workflow-extensions.md), also known as *custom workflow activities*, aren't supported.
- On-premises environments aren't supported.
- Unmanaged code isn't supported. You can't include references to unmanaged resources.

### Performance considerations when importing or registering a plug-in package

Plug-in packages containing assemblies with a large number (hundreds to thousands) of classes that implement `IPlugin` take a relatively long time to import into Dataverse.

Import times of 15 minutes for a thousand plug-in types have been observed. This duration applies regardless of whether you're importing a solution by using an API call or through the Web UI, or registering the package by using the Plug-in Registration tool.

## Create a plug-in package

You can place your plug-in assembly and any dependent assemblies together in a NuGet package, and then register and upload the package to the Dataverse server. If your plug-in project doesn't require any dependent assemblies at runtime other than what ships in the `Microsoft.CrmSdk.CoreAssemblies` NuGet package, you don't need to create a package.

Learn how to [create and register a plug-in package using PAC CLI](/power-platform/developer/howto/cli-create-package) and how to [create and register a plug-in package using Visual Studio](/power-platform/developer/howto/vs-create-package).

## All projects must use the SDK style

A plug-in package can only contain custom assemblies that are built from a project file in a specific format known as the *SDK style*. If you don't follow this rule, you get an error ("file can't be found") when you try to register the package by using the Plug-in Registration tool.

> [!IMPORTANT]
> All MSBuild projects where you add the resulting compiled assembly to a plug-in package must use the "SDK style" format.

An SDK style project is one where the contents of the project's .csproj file contains the following line of code: `<Project Sdk="Microsoft.NET.Sdk">`.

When you create a plug-in project by using one of the tools, such as the Power Platform CLI `pac plugin init` command, the plug-in project file is in the correct format. Here's an example of such a project file.

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

If you're adding another project to the Visual Studio solution, such as a class library project, create an SDK style project by following these steps:

1. In Visual Studio, add the new project to your solution using a .NET or .NET Standard template. Do not target .NET Framework.
1. Edit the project file by right-clicking on the project name in Solution Explorer and selecting **Edit project file**, or open the project's .csproj file in a separate editor.
1. You should see the line `<Project Sdk="Microsoft.NET.Sdk">` in the project file. Change the TargetFramework property to be `<TargetFramework>net462</TargetFramework>` and save the file.
1. Verify your solution builds, and you're done.

For more information, see [.NET Project SDKs](/dotnet/core/project-sdk/overview#project-files).

### Don't depend on System.Text.Json

Because the `Microsoft.CrmSdk.CoreAssemblies` NuGet package has a [dependency](https://www.nuget.org/packages/Microsoft.CrmSdk.CoreAssemblies#dependencies-body-tab) on [`System.Text.Json`](xref:System.Text.Json), you can refer to `System.Text.Json` types at design time. However, the `System.Text.Json.dll` file in the sandbox runtime might not be the same version that you refer to in your project. If you need to use `System.Text.Json`, use the dependent assembly capability and explicitly include it in your NuGet package.

## Next step

- [Register a plug-in](register-plug-in.md)

### See also

- [Use plug-ins to extend business processes](plug-ins.md)

[!INCLUDE [footer-include](../../includes/footer-banner.md)]
