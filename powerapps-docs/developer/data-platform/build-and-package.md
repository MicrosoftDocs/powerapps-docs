---
title: Build and package plug-in code
description: Learn about building plug-in code into assemblies and packages for later registration and upload to the Microsoft Dataverse service.
ms.date: 10/02/2023
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

Best practice information: [Optimize assembly development](/dynamics365/customer-engagement/guidance/server/optimize-assembly-development)

### Signed assemblies are required

Assemblies must be signed before they can be registered with Dataverse only if you are not using the [dependent assemblies](#dependent-assemblies) capability. You can use the Visual Studio **Signing** tab in your project's properties or the [Sn.exe (Strong Name Tool)](/dotnet/framework/tools/sn-exe-strong-name-tool) command to sign the assembly.

### Dependency on the CoreAssemblies NuGet package

Adding the `Microsoft.CrmSdk.CoreAssemblies` NuGet package to your project includes the required Dataverse assembly references in your project, but it doesn't upload these assemblies along with your plug-in assembly as these assemblies already exist in the server's sandbox run-time where your code will execute.

### Where to go next

If you are interested in learning about or using dependent assemblies, continue reading the next section in this article. If not, proceed to [Register a plug-in](register-plug-in.md).

## Dependent assemblies

The dependent assembly capability can be used to include other required .NET assemblies or resources (for example, localized strings) with your plug-in assembly in a single [NuGet](https://www.nuget.org) package that is uploaded to the Dataverse server during the registration process.

> [!IMPORTANT]
> The dependent assembly capability is so important to plug-in development that you should consider using it from the start even if you do not have an immediate need to do so. Adding support for dependent assemblies to your plug-in project is much more difficult later on in the development cycle.

This NuGet package file is stored in the [PluginPackage](reference/entities/pluginpackage.md) table. The contents of the NuGet package is stored in file storage rather than the SQL database.

When you upload your NuGet package, any assemblies containing classes that implement the <xref:Microsoft.Xrm.Sdk.IPlugin> interface are registered in the [PluginAssembly](reference/entities/pluginassembly.md) table and associated with the plug-in package. As you develop and maintain your project, you continue to update the `PluginPackage` table row and changes to the related plug-in assemblies are managed on the server.

At runtime, Dataverse copies the contents of the NuGet package from the `PluginPackage` row and extracts it to the sandbox runtime. This way, any dependent assemblies needed for the plug-in are available.

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
- Plug-ins for virtual table data providers aren't supported.
- On-premises environments aren't supported.
- Un-managed code isn't supported. You can't include references to unmanaged resources.

## Creating a plug-in package

Your plug-in assembly plus any required dependent assemblies can be placed together in a NuGet package and then registered and uploaded to the Dataverse server. You do not need to create a package if your plug-in project does not require any dependent assemblies at run-time, other than what ships in the Microsoft.CrmSdk.CoreAssemblies NuGet package.

<!-- Add correct links when available -->
Instructions for creating a plug-in package using an interactive tool can be found in these separate how-to's: [Create and register a plug-in package using PAC CLI](/power-platform/developer/howto/cli-create-package), [Create and register a plug-in package using Visual Studio](/power-platform/developer/howto/vs-create-package).

### Don't depend on System.Text.Json

Because the Microsoft.CrmSdk.CoreAssemblies NuGet package has a [dependency](https://www.nuget.org/packages/Microsoft.CrmSdk.CoreAssemblies#dependencies-body-tab) on System.Text.Json, you're able to refer to [System.Text.Json](xref:System.Text.Json) types at design time. However, the System.Text.Json.dll file in the sandbox run-time can't be guaranteed to be the same version that you reference in your project. If you need to use `System.Text.Json`, you should use the dependent assembly feature and explicitly include it in your NuGet package.

### See also

[Use plug-ins to extend business processes](plug-ins.md)  

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
