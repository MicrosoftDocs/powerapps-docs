---
title: Build and package plug-in code
description: Learn about building and packaging plug-in code for Microsoft Dataverse, including assembly constraints and dependent assembly limitations.
ms.date: 11/02/2023
ms.topic: conceptual
author: divkamath
ms.author: dikamath
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

This article describes constraints and limitations you need to know about when you're configuring and building an assembly for your Microsoft Dataverse plug-in.
  
## Plug-in assembly constraints

When you build a plug-in project, keep the following output assembly constraints in mind.

### Use .NET Framework 4.6.2

Plug-in and custom workflow activity assembly projects must target .NET Framework 4.6.2. Assemblies that are built using later versions of the .NET Framework should generally work. However, if the plug-in code uses any features introduced after 4.6.2, a runtime error occurs.

### Limit assemblies to 16 MB

Your assembly can include multiple plug-in classes or types and even custom workflow activities, but it can't be larger than 16 MB. As a best practice, we recommend that you consolidate plug-ins and workflow assemblies into a single assembly, as long as the size remains below 16 MB.

### Sign assemblies before registering them

If you're not using the [dependent assemblies](#dependent-assemblies) capability, assemblies must be signed before you can register them with Dataverse. To sign the assembly, use the Visual Studio **Signing** tab in your project's properties or the [Sn.exe (Strong Name Tool)](/dotnet/framework/tools/sn-exe-strong-name-tool) command.

### NuGet CoreAssemblies are in the sandbox

If you add the `Microsoft.CrmSdk.CoreAssemblies` [NuGet](https://www.nuget.org) package to your project, the required Dataverse assembly references are also added, but the assemblies themselves aren't uploaded with your plug-in assembly. They already exist in the server's sandbox runtime where your code executes.

## Dependent assemblies

> [!IMPORTANT]
> The dependent assembly capability is so important to plug-in development that you should consider using it from the start, even if you don't have an immediate need. Adding support for dependent assemblies to your plug-in project is much more difficult later in the development cycle.
>
> We don't support ILMerge. The dependent assemblies capability offers the same functionality as ILMerge and more.

Use the dependent assembly capability to include other required .NET assemblies or resources, like localized strings, with your plug-in assembly in a single [NuGet](https://www.nuget.org) package that's uploaded to the Dataverse server during registration.

The NuGet package file is stored in the [`PluginPackage`](reference/entities/pluginpackage.md) table. The contents of the package are stored in file storage rather than in the SQL database.

When you upload your NuGet package, any assemblies that contain classes that implement the <xref:Microsoft.Xrm.Sdk.IPlugin> interface are registered in the [`PluginAssembly`](reference/entities/pluginassembly.md) table and associated with the plug-in package. As you develop and maintain your project, you continue to update the `PluginPackage` table row and changes to the related plug-in assemblies are managed on the server.

At runtime, Dataverse copies the contents of the NuGet package from the `PluginPackage` row and extracts it to the sandbox runtime. This way, any dependent assemblies needed for the plug-in are available.

### Signed assemblies aren't required

You aren't required to sign plug-in assemblies used in plug-in packages.

When you register individual plug-in assemblies without the dependent assemblies capability, signing is required because it provides a unique name for the assembly. But with plug-in assemblies in a plug-in package, the assemblies are loaded on the sandbox server using a different mechanism, so signing isn't necessary.

> [!IMPORTANT]
> If you sign your assemblies, be aware that signed assemblies can't use resources that are contained in unsigned assemblies. If you sign your plug-in assemblies or any dependent assembly, all the assemblies that those assemblies depend on must be signed.
>
> If any signed assemblies depend on unsigned assemblies, you get an error like this: "Could not load file or assembly *AssemblyName*, Version=*Version*, Culture=neutral, PublicKeyToken=null or one of its dependencies. A strongly-named assembly is required."

### Dependent assemblies limitations

The following limitations apply when you use plug-in dependent assemblies:

- [Workflow extensions](workflow/workflow-extensions.md), also known as *custom workflow activities*, aren't supported.
- Plug-ins for virtual table data providers aren't supported.
- On-premises environments aren't supported.
- Unmanaged code isn't supported. You can't include references to unmanaged resources.

## Create a plug-in package

You can place your plug-in assembly and any dependent assemblies together in a NuGet package and then register and upload them to the Dataverse server. If your plug-in project doesn't require any dependent assemblies at runtime other than what ships in the `Microsoft.CrmSdk.CoreAssemblies` NuGet package, you don't need to create a package.

Learn how [create and register a plug-in package using PAC CLI](/power-platform/developer/howto/cli-create-package) and how to [create and register a plug-in package using Visual Studio](/power-platform/developer/howto/vs-create-package).

### Don't depend on System.Text.Json

Because the `Microsoft.CrmSdk.CoreAssemblies` NuGet package has a [dependency](https://www.nuget.org/packages/Microsoft.CrmSdk.CoreAssemblies#dependencies-body-tab) on [`System.Text.Json`](xref:System.Text.Json), you're able to refer to `System.Text.Json` types at design time. However, the `System.Text.Json.dll` file in the sandbox runtime might not be the same version that you refer to in your project. If you need to use `System.Text.Json`, you should use the dependent assembly capability and explicitly include it in your NuGet package.

## Next step

- [Register a plug-in](register-plug-in.md)

### See also

- [Use plug-ins to extend business processes](plug-ins.md)

[!INCLUDE [footer-include](../../includes/footer-banner.md)]
