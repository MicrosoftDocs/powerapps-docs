---
title: "Generate early-bound classes for the SDK for .NET (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn about a command-line code generation tool for use with Microsoft Dataverse. This tool generates early-bound .NET Framework classes that represent the Entity Data Model used by Dataverse." # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 12/22/2022
author: kkanakas
ms.author: kartikka
ms.reviewer: pehecke
ms.topic: "article"
search.audienceType: 
  - developer
contributors:
 - JimDaly
 - phecke
---

# Generate early-bound classes for the SDK for .NET

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

*CrmSvcUtil* is a command-line code generation tool for use with Microsoft Dataverse. The tool generates early-bound .NET Framework classes that represent the Entity Data Model (EDM) used by Dataverse. To generate cross-platform .NET (Core) classes, use the [modelbuilder](/power-platform/developer/cli/reference/modelbuilder) argument of Power Platform CLI.

The code generation tool (CrmSvcUtil.exe) is distributed as part of the [Microsoft.CrmSdk.CoreTools](https://www.nuget.org/packages/Microsoft.CrmSdk.CoreTools) NuGet package. You can download the NuGet package, rename the file's extension .nupkg to .zip, and extract the files. You may also need to unblock the file in the Properties dialog of File Explorer.

> [!NOTE]
> For more information about available tools, including the code generation tool, see [Dataverse development tools](../download-tools-NuGet.md).

## Generate Entity classes

The CrmSvcUtil tool creates a Microsoft Visual C# or Visual Basic .NET output file that contains strongly-typed classes for tables in your environment. This includes custom tables and columns. This output file contains one class derived from <xref:Microsoft.Xrm.Sdk.Entity> for each table, providing early binding and IntelliSense support in Visual Studio to aid you as you write code. The generated classes are partial classes that can be extended with custom business logic in separate files. You can also write extensions for this tool to customize its functionality. For more information, see [Create extensions for the Code Generation Tool](extend-code-generation-tool.md).  

## Generate an OrganizationServiceContext class

The tool can also be used to generate a class derived from the <xref:Microsoft.Xrm.Sdk.Client.OrganizationServiceContext> class that acts as an entity container in the EDM. This service context provides the facilities for tracking changes and managing identities, concurrency, and relationships. This class also exposes a <xref:Microsoft.Xrm.Sdk.Client.OrganizationServiceContext.SaveChanges> method that writes inserts, updates, and deletes table rows in Dataverse. For more information, see [Use OrganizationServiceContext](organizationservicecontext.md).  

## Use generated classes

The classes created by the code generation tool are designed to be built into a class library that can be referenced by projects that use Dataverse. After you have generated the class file(s) using the tool, you should add the file(s) to your Visual Studio project. You must also add references to several assemblies that the generated classes are dependent upon.  

The following lists assemblies that must be referenced in your project when you use the generated code file.  

- `Microsoft.Crm.Sdk.Proxy.dll`  
- `Microsoft.Xrm.Sdk.dll` 

These assemblies are part of the [Microsoft.CrmSdk.CoreAssemblies](https://www.nuget.org/packages/Microsoft.CrmSdk.CoreAssemblies/) or [Microsoft.PowerPlatform.Dataverse.Client](https://www.nuget.org/packages/Microsoft.PowerPlatform.Dataverse.Client) NuGet package. Use one of these NuGet packages to add the required assemblies to your Visual Studio project.

<a name="bkmk_RuntheCodeGenerationUtility"></a>

## Run the code generation tool

The code generation tool takes several parameters that determine the contents of the file that is created. The parameters can be passed in from the command line when you run the tool or in a .NET-connected application configuration file. 

Run the `CrmSvcUtil.exe` application from the folder where it is installed. If you run the tool from another folder location, make sure that a copy of the `Microsoft.Xrm.Sdk.dll` assembly is in that same folder.

The following sample shows the format for running the tool from the command line with Dataverse. To use an interactive environment login, you can simply provide these options:

```ms-dos
CrmSvcUtil.exe /interactivelogin ^
/out:<outputFilename>.cs ^
/namespace:<outputNamespace> ^
/serviceContextName:<serviceContextName> ^
/generateActions
```

When you run the tool with the `interactivelogin` (shortcut `il`) option you will open a dialog and be able to specify your login credentials and the server you want to connect with.

You can also specify the parameters you want to pass directly in the command line or via a batch (.bat) file you can run to generate new classes.

```ms-dos
CrmSvcUtil.exe ^
/url:https://<organizationUrlName>.api.crm.dynamics.com/XRMServices/2011/Organization.svc ^
/out:<outputFilename>.cs ^
/username:<username> ^
/password:<password> ^
/namespace:<outputNamespace> ^
/serviceContextName:<serviceContextName>
```
For example:

```ms-dos
CrmSvcUtil.exe ^
/url:https://myorganization.api.crm.dynamics.com/XRMServices/2011/Organization.svc ^
/out:MyOrganizationSdkTypes.cs ^
/username:you@yourOrg.onmicrosoft.com ^
/password:myp455w0rd ^
/namespace:MyOrg ^
/serviceContextName:MyContext
```


> [!NOTE]
> The examples above uses the carat (`^`) character to break up the list of parameters for readability. You can compose the command parameters with arguments using notepad and then paste it into the command line.

- For the `username` and `password` parameters, type the user name and password that is used to sign in to your Dataverse environment. 
- For the `url` parameter you can look up the correct URL in Power Apps, or in the legacy web application by selecting **Settings**, navigating to **Customizations**, and then choosing **Developer Resources**. The URL is shown under **Organization Service**.  

To view the latest supported command-line parameters, use the following command.

```ms-dos
CrmSvcUtil.exe /?  
```

<a name="bkmk_parameters"></a>

## Parameters

The following table lists the code generation tool parameters at the time when this topic was last updated, and provides a brief description of command parameter use.  
  
|Parameter|Shortcut|Description|
|--|--|--|
|`url`||The URL for the Organization service. Required, unless you use `interactivelogin`|
|`out`|`o`|The file name for the generated code. Required|
|`language`|`l`|The language to generate the code in. This can be either "CS" or "VB". The default value is "CS".|
|`namespace`|`n`|The namespace for the generated code. The default is the global namespace.| 
|`username`|`u`|The user name to use when you connect to the server for authentication.|  
|`password`|`p`|The password to use when you connect to the server for authentication.|
|`domain`|`d`|The domain to authenticate against when you connect to an on-premises server.|
|`servicecontextname`||The name of the generated context class. If no value is supplied, no service context is created.
|`help`|`?`|Show usage information.|
|`nologo`||Suppress the banner at runtime.|
|`generateActions`||Generate request and response classes for custom actions.|
|`interactivelogin`|`il`|When used, a dialog to log into the Dataverse service is displayed. All other connection related parameters specified on the command line are ignored.| 
|`connectionstring`|`connstr`|Contains information, provided as a single string, for connecting to a Dataverse organization. All other connection related parameters specified on the command line are ignored. For more information see [Use connection strings in XRM tooling to connect to Dataverse](../xrm-tooling/use-connection-strings-xrm-tooling-connect.md).|
|`suppressGeneratedCodeAttribute`|`sgca`|Suppresses the GeneratedCodeAttribute on all classes|
|`emitfieldsclasses`|`emitfc`|Generate a Fields class per entity that contains all of the field names at the time of code generation|
|`entitynamesfilter`| |Filters the list of entities retrieved when reading data from Dataverse. Passed in as a semicolon separated list using the form \<entitylogicalname>;\<entitylogicalname>;...|
|`messagenamesfilter`| |Filters the list of messages that are retrieved when reading data from Dataverse. Passed in as a semicolon separated list. Required messages ( Create, Update, Delete, Retrieve, RetrieveMultiple, Associate and DisAssociate) are always included. A * can be used to proceed or trail a message allowing for all messages starting with or ending with a string. The list takes the form \<messagename>;\<messagename>;...|
|`splitfiles`| |Splits the output into files by type, organized by entity, message, and optionsets. when enabled, the `out` property is ignored and `outdirectory` is required instead|
|`outdirectory`|`outdir`|Write entity, message and optionset files to a specified output directory. Valid only with the `splitfiles` option|
|`entitytypesfolder`| |Folder name that will contain entities. THe default folder name is "Entities". Valid only with the `splitfiles` option.|
|`messagestypesfolder`| |Folder name that will contain messages. The default name is "Messages". Valid only with the `splitfiles` option|
|`optionsetstypesfolder`| |Folder name that will contain optionsets. The default name is "OptionSets". Valid only with `splitfiles` option|
|`generateGlobalOptionSets`| |Emit all global optionsets. Note: if an entity contains a reference to a global optionset, it will be emitted even if this switch is not present|
|`legacyMode`| |Disable emitting optionsets and many newer code features to support compatibility with older custom extensions|

<a name="bkmk_sampleconfig"></a>

## Use the configuration File

The CrmSvcUtil.exe.config configuration file must be in the same folder as the CrmSvcUtil.exe tool. The configuration file uses the standard key/value pairs in the `appSettings` section. However, if you enter a value at the command line, that value will be used instead of the one in the configuration file. Any key/value pairs found in the application configuration file that do not match any of the expected parameters are ignored.  

Do not include the `url` and `namespace` parameters in the configuration file. These must be entered from the command line when the CrmSvcUtil.exe tool is being run.  

The following sample shows how to configure the output file and the domain name parameters in the application configuration file using shortcut keys.  

```xml
<appSettings>    
    <add key="o" value="CrmProxy.cs"/>    
    <add key="d" value="mydomain"/>
</appSettings>  
```

<a name="bkmk_enabletrace"></a>

## Enable tracing

 To enable tracing when you run the tool, add the following lines to the configuration file:  

```xml
<system.diagnostics>   
   <trace autoflush="false" indentsize="4">   
      <listeners>   
         <add name="configConsoleListener" type="System.Diagnostics.ConsoleTraceListener">   
            <filter type="System.Diagnostics.EventTypeFilter" initializeData="Error" />   
         </add>   
      </listeners>   
   </trace>   
</system.diagnostics>  
```

For more information on supported tracing options see [Configure tracing for XRM tooling](../xrm-tooling/configure-tracing-xrm-tooling.md).  

## Community tools

**Early Bound Generator** is a tool from the XrmToolbox community. Please see the [Developer tools and resources](../developer-tools.md) topic for more community developed tools.

> [!NOTE]
> The community tools are not a product of Microsoft and does not extend support to the community tools. 
> If you have questions pertaining to the tool, please contact the publisher. More Information: [XrmToolBox](https://www.xrmtoolbox.com). 

### See Also

[Late-bound and early-bound programming](early-bound-programming.md)  
[Sample: Early-bound table operations](samples/early-bound-entity-operations.md)

[Create extensions for the Code Generation Tool](extend-code-generation-tool.md)  
[Developer tools and resources](../developer-tools.md)  
[Dataverse development tools](../download-tools-NuGet.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
