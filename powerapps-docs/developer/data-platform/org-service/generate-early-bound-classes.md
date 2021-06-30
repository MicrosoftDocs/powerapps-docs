---
title: "Generate early-bound classes for the Organization service (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn about a command-line code generation tool for use with Microsoft Dataverse. This tool generates early-bound .NET Framework classes that represent the Entity Data Model used by Dataverse." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 06/10/2021
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

# Generate early-bound classes for the Organization service

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

*CrmSvcUtil* is a command-line code generation tool for use with Microsoft Dataverse. The tool generates early-bound .NET Framework classes that represent the Entity Data Model (EDM) used by Dataverse. The code generation tool (CrmSvcUtil.exe) is distributed as part of the [Microsoft.CrmSdk.CoreTools](https://www.nuget.org/packages/Microsoft.CrmSdk.CoreTools) NuGet package.

> [!NOTE]
> For information about downloading the code generation tool, see [Download tools from NuGet](../download-tools-NuGet.md).

## Generate Entity classes

The CrmSvcUtil tool creates a Microsoft Visual C# or Visual Basic .NET  output file that contains strongly-typed classes for tables in your organization. This includes custom tables and columns. This output file contains one class derived from <xref:Microsoft.Xrm.Sdk.Entity> for each table, providing early binding and IntelliSense support in Visual Studio to aid you as you write code. The generated classes are partial classes that can be extended with custom business logic in separate files. You can also create extensions to this tool. For more information, see [Create extensions for the Code Generation Tool](extend-code-generation-tool.md).  

## Generate an OrganizationServiceContext class

The tool can also be used to generate a class derived from the <xref:Microsoft.Xrm.Sdk.Client.OrganizationServiceContext> class that acts as an entity container in the EDM. This service context provides the facilities for tracking changes and managing identities, concurrency, and relationships. This class also exposes a <xref:Microsoft.Xrm.Sdk.Client.OrganizationServiceContext.SaveChanges> method that writes inserts, updates, and deletes table rows in Dataverse. For more information, see [Use OrganizationServiceContext](organizationservicecontext.md).  

## Use generated classes

The classes created by the code generation tool are designed to be built into a class library that can be referenced by projects that use Dataverse. After you have generated the class file using the tool, you should add the file to your Visual Studio project. You must also add references to several assemblies that the generated classes are dependent upon.  

The following lists assemblies that must be referenced in your project when you use the generated code file.  

- `Microsoft.Crm.Sdk.Proxy.dll`  
- `Microsoft.Xrm.Sdk.dll` 

These assemblies are part of the [Microsoft.CrmSdk.CoreAssemblies](https://www.nuget.org/packages/Microsoft.CrmSdk.CoreAssemblies/) NuGet package. Use this NuGet packages to add these assemblies to your Visual Studio project.

<a name="bkmk_RuntheCodeGenerationUtility"></a>

## Run the code generation tool

The code generation tool takes several parameters that determine the contents of the file that is created. The parameters can be passed in from the command line when you run the tool or in a .NET-connected application configuration file. 

Run the `CrmSvcUtil.exe` tool from the `Tools\CoreTools` folder created when you downloaded the tools using the script described in [Download tools from NuGet](../download-tools-NuGet.md). If you run the tool from another folder location, make sure that a copy of the `Microsoft.Xrm.Sdk.dll` assembly is in that same folder.  

The following sample shows the format for running the tool from the command line with Dataverse. To use the interactive login, you can simply provide these options:

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

- For the `username` and `password` parameters, type the user name and password that is used to sign in to Dataverse. 
- For the `url` parameter, you can look up the correct URL in the web application by selecting **Settings**, navigating to **Customizations**, and then choosing **Developer Resources**. The URL is shown under **Organization Service**.  

To list the supported command-line parameters, use the following command.

```ms-dos
CrmSvcUtil.exe /?  
```

<a name="bkmk_parameters"></a>

## Parameters

The following table lists the code generation tool parameters and a gives a brief description of their use.  
  
|Parameter|Shortcut|Description|Required|
|--|--|--|--|
|`deviceid`|`di`|No longer needed|False|
|`devicepassword`|`dp`|No longer needed|False|
|`domain`|`d`|The domain to authenticate against when you connect to an on-premises server.|False|
|`url`||The URL for the Organization service.|True unless you use `interactivelogin`|
|`out`|`o`|The file name for the generated code.|True|
|`language`|`l`|The language to generate the code in. This can be either “CS” or “VB”. The default value is “CS”.|False|
|`namespace`|`n`|The namespace for the generated code. The default is the global namespace.|False|  
|`username`|`u`|The user name to use when you connect to the server for authentication.|False|  
|`password`|`p`|The password to use when you connect to the server for authentication.|False|  
|`servicecontextname`||The name of the generated organization service context class. If no value is supplied, no service context is created.|False|
|`help`|`?`|Show usage information.|False|
|`nologo`||Suppress the banner at runtime.|False|
|`generateActions`||Generate request and response classes for custom actions.|False|
|`interactivelogin`|`il`|When used, a dialog to log into the Dataverse service is displayed. All other connection related parameters specified on the command line are ignored.|False|  
|`connectionstring`|`connstr`|Contains information, provided as a single string, for connecting to a Dataverse organization. All other connection related parameters specified on the command line are ignored. For more information see [Use connection strings in XRM tooling to connect to Dataverse](../xrm-tooling/use-connection-strings-xrm-tooling-connect.md).|False|


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

**Early Bound Generator** is a tool that XrmToolbox community. Please see the [Developer tools and resources](../developer-tools.md) topic for more community developed tools.

> [!NOTE]
> The community tools are not a product of Microsoft and does not extend support to the community tools. 
> If you have questions pertaining to the tool, please contact the publisher. More Information: [XrmToolBox](https://www.xrmtoolbox.com). 

### See Also

[Late-bound and early-bound programming using the Organization service](early-bound-programming.md)  
[Sample: Early-bound table operations](samples/early-bound-entity-operations.md)

[Create extensions for the Code Generation Tool](extend-code-generation-tool.md)  
[Developer tools and resources](../developer-tools.md)  
[Download tools from NuGet](../download-tools-NuGet.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]