---
title: "SolutionPackager tool (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "SolutionPackager is a tool that can reversibly decompose a Dynamics 365 Customer Engagement compressed solution file into multiple XML files and other files so that these files can be easily managed by a source control system" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "shmcarth" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# SolutionPackager tool

SolutionPackager is a tool that can reversibly decompose a Common Data Service for Apps compressed solution file into multiple XML files and other files so that these files can be easily managed by a source control system. The following sections show you how to run the tool and how to use the tool with managed and unmanaged solutions.  
  
<a name="bkm_where"></a>   

## Where to find the SolutionPackager tool  

 The SolutionPackager tool is distributed as part of the [Microsoft.CrmSdk.CoreTools](https://www.nuget.org/packages/Microsoft.CrmSdk.CoreTools) NuGet package. See [Download tools from NuGet](download-tools-nuget.md) for information about how to download it.
  
<a name="arguments"></a>   

## SolutionPackager command-line arguments  

 SolutionPackager is a command-line tool that can be invoked with the parameters identified in the following table.  
  
|Argument|Description|  
|--------------|-----------------|  
|/action: {Extract&#124;Pack}|Required. The action to perform. The action can be either to extract a solution .zip file to a folder, or to pack a folder into a .zip file.|  
|/zipfile: \<file path>|Required. The path and name of a solution .zip file. When extracting, the file must exist and will be read from. When packing, the file is replaced.|  
|/folder: \<folder path>|Required. The path to a folder. When extracting, this folder is created and populated with component files. When packing, this folder must already exist and contain previously extracted component files.|  
|/packagetype: {Unmanaged&#124;Managed&#124;Both}|Optional. The type of package to process. The default value is Unmanaged. This argument may be omitted in most occasions because the package type can be read from inside the .zip file or component files. When extracting and Both is specified, managed and unmanaged solution .zip files must be present and are processed into a single folder. When packing and Both is specified, managed and unmanaged solution .zip files will be produced from one folder. For more information, see the section on working with managed and unmanaged solutions later in this topic.|  
|/allowWrite:{Yes&#124;No}|Optional. The default value is Yes. This argument is used only during an extraction. When /allowWrite:No is specified, the tool performs all operations but is prevented from writing or deleting any files. The extract operation can be safely assessed without overwriting or deleting any existing files.|  
|/allowDelete:{Yes&#124;No&#124;Prompt}|Optional. The default value is Prompt. This argument is used only during an extraction. When /allowDelete:Yes is specified, any files present in the folder specified by the /folder parameter that are not expected are automatically deleted. When /allowDelete:No is specified, no deletes will occur. When /allowDelete:Prompt is specified, the user is prompted through the console to allow or deny all delete operations. Note that if /allowWrite:No is specified, no deletes will occur even if /allowDelete:Yes is also specified.|  
|/clobber|Optional. This argument is used only during an extraction. When /clobber is specified, files that have the read-only attribute set are overwritten or deleted. When not specified, files with the read-only attribute aren’t overwritten or deleted.|  
|/errorlevel: {Off&#124;Error&#124;Warning&#124;Info&#124;Verbose}|Optional. The default value is Info. This argument indicates the level of logging information to output.|  
|/map: \<file path>|Optional. The path and name of an .xml file containing file mapping directives. When used during an extraction, files typically read from inside the folder specified by the /folder parameter are read from alternate locations as specified in the mapping file. During a pack operation, files that match the directives aren’t written.|  
|/nologo|Optional. Suppress the banner at runtime.|  
|/log: \<file path>|Optional. A path and name to a log file. If the file already exists, new logging information is appended to the file.|  
|@ \<file path>|Optional. A path and name to a file that contains command-line arguments for the tool.|  
|/sourceLoc: \<string>|Optional. This argument generates a template resource file, and is valid only on extract.<br /><br /> Possible values are `auto` or an LCID/ISO code for the language you want to export. When this argument is used, the string resources from the given locale are extracted as a neutral .resx file. If `auto` or just the long or short form of the switch is specified, the base locale or the solution is used. You can use the short form of the command: /src.|  
|/localize|Optional. Extract or merge all string resources into .resx files. You can use the short form of the command: /loc.|  
  
<a name="use_command"></a>   

## Use the /map command argument  

 The following discussion details the use of the /map argument to the SolutionPackager tool.  
  
 Files that are built in an automated build system, such as .xap Silverlight files and plug-in assemblies, are typically not checked into source control. Web resources may already be present in source control in locations that are not directly compatible with the SolutionPackager tool. By including the /map parameter, the SolutionPackager tool can be directed to read and package such files from alternate locations and not from inside the Extract folder as it would typically be done. The /map parameter must specify the name and path to an XML file containing mapping directives that instruct the SolutionPackager to match files by their name and path, and indicate the alternate location to find the matched file. The following information applies to all directives equally.  
  
- Multiple directives may be listed including those that will match identical files. Directives listed early in the file take precedence over those listed later.  
  
- If a file is matched to any directive, it must be found in at least one alternative location. If no matching alternatives are found, the SolutionPackager will issue an error.  
  
- Folder and file paths may be absolute or relative. Relative paths are always evaluated from the folder specified by the /folder parameter.  
  
- Environment variables may be specified by using a %variable% syntax.  
  
- A folder wildcard “**” may be used to mean “in any sub-folder”. It can only be used as the final part of a path, for example: “c:\folderA\\\*\*”.  
  
- File name wildcards may be used only in the forms “*.ext” or “\*.\*”. No other pattern is supported.  
  
  The three types of directives mappings are described here, along with an example that shows you how to use them.  
  
<a name="Folder_mapping"></a>   

### Folder mapping  

 The following provides detailed information on folder mapping.  
  
 Xml Format  
 `<Folder map="folderA" to="folderB" />`  
  
 Description  
 File paths that match “folderA” will be switched to “folderB”.  
  
- The hierarchy of subfolders under each must exactly match.  
  
- Folder wildcards are not supported.  
  
- No file names may be specified.  
  
  Examples  
  ```xml  
  <Folder map="folderA" to="folderB" />  
  <Folder map="folderA\folderB" to="..\..\folderC\" />  
  <Folder map="WebResources\subFolder" to="%base%\WebResources" />  
  ```  
  
<a name="file_mapping"></a>   

### File To file mapping  

 The following provides detailed information on file-to-file mapping.  
  
 Xml Format  
 `<FileToFile map="path\filename.ext" to="path\filename.ext" />`  
  
 Description  
 Any file matching the `map` parameter will be read from the name and path specified in the `to` parameter.  
  
 For the `map` parameter:  
  
- A file name must be specified. The path is optional. If no path is specified, files from any folder may be matched.  
  
- File name wildcards are not supported.  
  
- The folder wildcard is supported.  
  
  For the `to` parameter:  
  
- A file name and path must be specified.  
  
- The file name may differ from the name in the `map` parameter.  
  
- File name wildcards are not supported.  
  
- The folder wildcard is supported.  
  
  Examples  
  ```xml  
  <FileToFile map="assembly.dll" to="c:\path\folder\assembly.dll" />  
  <FileToFile map="PluginAssemblies\**\this.dll" to="..\..\Plugins\**\that.dll" />  
  <FileToFile map="Webresrouces\ardvark.jpg" to="%SRCBASE%\CrmPackage\WebResources\JPG format\aardvark.jpg" />  
  ```  
  
<a name="file_path_mapping"></a>   

### File to path mapping  

 The following provides detailed information on file-to-path mapping.  
  
 Xml Format  
 `<FileToPath map="path\filename.ext" to="path" />`  
  
 Description  
 Any file matching the `map` parameter is read from the path specified in the `to` parameter.  
  
 For the `map` parameter:  
  
- A file name must be specified. The path is optional. If no path is specified, files from any folder may be matched.  
  
- File name wildcards are supported.  
  
- The folder wildcard is supported.  
  
  For the `to` parameter:  
  
- A path must be specified.  
  
- The folder wildcard is supported.  
  
- A file name must not be specified.  
  
  Examples  
  ```xml  
  <FileToPath map="assembly.dll" to="c:\path\folder" />  
  <FileToPath map="PluginAssemblies\**\this.dll" to="..\..\Plugins\bin\**" />  
  <FileToPath map="*.jpg" to="%SRCBASE%\CrmPackage\WebResources\JPG format\" />  
  <FileToPath map="*.*" to="..\..\%ARCH%\%TYPE%\drop" />  
  ```  
  
<a name="Example_mapping"></a>   
### Example mapping  
 The following XML code sample shows a complete mapping file that enables the SolutionPackager tool to read any web resource and the two default generated assemblies from a Developer Toolkit project named CRMDevTookitSample.  
  
```xml  
<?xml version="1.0" encoding="utf-8"?>  
<Mapping>  
       <!-- Match specific named files to an alternate folder -->  
       <FileToFile map="CRMDevTookitSamplePlugins.dll" to="..\..\Plugins\bin\**\CRMDevTookitSample.plugins.dll" />  
       <FileToFile map="CRMDevTookitSampleWorkflow.dll" to="..\..\Workflow\bin\**\CRMDevTookitSample.Workflow.dll" />  
       <!-- Match any file in and under WebResources to an alternate set of sub-folders -->  
       <FileToPath map="WebResources\*.*" to="..\..\CrmPackage\WebResources\**" />  
       <FileToPath map="WebResources\**\*.*" to="..\..\CrmPackage\WebResources\**" />  
</Mapping>  
```  
  
<a name="managed"></a>   

## Managed and unmanaged solutions  

 A CDS for Apps compressed solution (.zip) file can be exported in one of two types as shown here.  
  
 Managed solution  
 A completed solution ready to be imported into an organization. Once imported, components can’t be added or removed, although they can optionally allow further customization. This is recommended when development of the solution is complete.  
  
 Unmanaged solution  
 An open solution with no restrictions on what can be added, removed, or modified. This is recommended during development of a solution.  
  
 The format of a compressed solution file will be different based on its type, either managed or unmanaged. The SolutionPackager can process compressed solution files of either type. However, the tool can’t convert one type to another. The only way to convert solution files to a different type, for example from unmanaged to managed, is by importing the unmanaged solution .zip file into a CDS for Apps server and then exporting the solution as a managed solution.  
  
 The SolutionPackager can process unmanaged and managed solution .zip files as a combined set via the /PackageType:Both parameter. To perform this operation, it is necessary to export your solution twice as each type, naming the .zip files as follows.  
  
|||  
|-|-|  
|Unmanaged .zip file: AnyName.zip|Managed .zip file: AnyName_managed.zip|  
  
 The tool will assume the presence of the managed zip file in the same folder as the unmanaged file and extract both files into a single folder preserving the differences where managed and unmanaged components exist.  
  
 After a solution has been extracted as both unmanaged and managed, it is possible from that single folder to pack both, or each type individually, using the /PackageType parameter to specify which type to create. When specifying both, two .zip files will be produced using the naming convention as above. If the /PackageType parameter is missing when packing from a dual managed and unmanaged folder, the default is to produce a single unmanaged .zip file.  
  
## Troubleshooting  

 If you use Visual Studio 2012 to edit resource files created by the solution packager, you may receive a message when you repack similar to this: `“Failed to determine version id of the resource file <filename>.resx the resource file must be exported from the solutionpackager.exe tool in order to be used as part of the pack process.”` This happens because Visual Studio replaces the resource file’s metadata tags with data tags.  
  
#### Workaround  
  
1. Open the resource file in your favorite text editor and locate and update the following tags:  
  
   ```xml  
   <data name="Source LCID" xml:space="preserve">  
   <data name="Source file" xml:space="preserve">  
   <data name="Source package type" xml:space="preserve">  
   <data name="SolutionPackager Version" mimetype="application/x-microsoft.net.object.binary.base64">  
  
   ```  
  
2. Change the node name from `<data>` to `<metadata>`.  
  
    For example, this string:  
  
   ```xml  
   <data name="Source LCID" xml:space="preserve">  
     <value>1033</value>  
   </data>  
  
   ```  
  
    Changes to:  
  
   ```xml  
   <metadata name="Source LCID" xml:space="preserve">  
     <value>1033</value>  
   </metadata>  
  
   ```  
  
   This allows the solution packager to read and import the resource file. This problem has only been observed when using the Visual Studio Resource editor.  
  
### See also  
 [Solution Tools for Team Development](solution-tools-team-development.md)   
 [Use Source Control with Solution Files](use-source-control-solution-files.md)   
 [Solution Component File Reference](solution-component-file-reference-solutionpackager.md)   
 [Introduction to Solutions](introduction-solutions.md)
