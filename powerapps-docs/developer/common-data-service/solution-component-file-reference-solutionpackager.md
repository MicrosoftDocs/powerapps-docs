---
title: "Solution component file reference (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This topic describes the folder structure and file naming scheme used by the SolutionPackager tool. The tool is used to decompose (unpack) Dynamics 365 solution files into XML files that can be managed by a source code control system." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 10/31/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "shmcarth" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Solution component file reference (SolutionPackager)

This topic describes the folder structure and file naming scheme used by the SolutionPackager tool. The tool is used to decompose (unpack) Common Data Service for Apps solution files into XML files that can be managed by a source code control system. The tool can also compile (pack) these individual XML files into a solution file that can be imported into CDS for Apps. For more information about the SolutionPackager tool, see [SolutionPackager tool](compress-extract-solution-file-solutionpackager.md).  
  
 The following sections describe the files that will be created for each solution component type, and which of these files are less suited to inclusion in source control. The folders indicated in the sections are all relative to the folder specified in the `/folder` parameter of the **SolutionPackager** command.  
  
<a name="entity_bm"></a>   
## Entity  
 Differs in managed solutions: Yes  
  
### Notes  
  
1.  Each entity has a distinct folder.  
  
2.  Each Form, View & Visualization gets their own file in the respective sub-folder.  
  
3.  The Form file names will vary by Managed or Unmanaged Solution types.  
  
4.  Direct editing of RibbonDiff.xml to customize entity specific ribbons is supported.  
  
5.  Manual editing of the XML files under the FormXml and SavedQueries folders is supported but optional.  
  
### Files  
 \Entities\\<Entity Schema Name\>\  
  
 Entity.xml  
RibbonDiff.xml  
  
 FormXml\Main\  
  
 {guid 1}.xml  
{guid 1_managed}.xml  
{guid n}.xml  
{guid n_managed}.xml  
  
 FormXml\Mobile\  
  
 {guid 1}.xml  
{guid 1_managed}.xml  
{guid n}.xml  
{guid n_managed}.xml  
  
 SavedQueries\  
  
 {guid 1}.xml  
{guid n}.xml  
  
 Visualizations\  
  
 {guid 1}.xml  
{guid n}.xml  
  
<a name="optionset_bm"></a>   
## Option set  
 Differs in managed solutions: No  
  
### Notes  
 Each option set is stored in a distinct file.  
  
### Files  
 \OptionSets\  
  
 \<schema name 1>.xml  
\<schema name n>.xml  
  
<a name="relationship_bm"></a>   
## Entity relationship  
 Differs in managed solutions: Yes  
  
### Notes  
  
1.  Each entity has a distinct file that contains all relationships where for:  
  
    1.  N:N it is the first listed entity  
  
    2.  1:N it is the referenced entity  
  
### Files  
 \Other\Relationships\  
  
 \<Entity schema name 1>.xml  
\<Entity schema name n>.xml  
  
<a name="ribbon_bm"></a>   
## Ribbon customization  
 Differs in managed solutions: No  
  
### Notes  
  
1.  All entity specific ribbon XML can be found in the respective folder for that entity. All other ribbon XML will be in this file.  
  
2.  Direct editing of RibbonCustomizations.xml to customize the global ribbon is supported.  
  
### Files  
 \Other\RibbonCustomizations.xml  
  
<a name="sitemap_bm"></a>   
## Site map  
 Differs in managed solutions: Yes  
  
### Notes  
 Sitemap XML format is different for unmanaged & managed solutions. Expect the file to be named as shown here. When extracting both package types, both files are present.  
  
### Files  
 \Other\  
  
 SiteMap.xml  
SiteMap_managed.xml  
  
<a name="resource_bm"></a>   
## Web resources  
 Differs in managed solutions: No  
  
### Notes  
  
1.  The raw web resource is stored as a distinct file. The forward slash (/) characters are used to create folders.  
  
2.  The web resource metadata is stored with a similar file name ending in .data.xml.  
  
3.  It is recommended that the name of a web resource contain the natural file name extension.  
  
4.  Adding the raw files to source control may cause duplication.  
  
### Files  
 \WebResources\  
  
 \<name 1>  
\<name 1>.data.xml  
\<name n>  
\<name n>.data.xml  
  
<a name="role_bm"></a>   
## Role  
 Differs in managed solutions: No  
  
### Notes  
 Each role is stored in a distinct file.  
  
### Files  
 \Roles\  
  
 \<schema name>.xml  
  
<a name="connectionrole_bm"></a>   
## Connection role  
 Differs in managed solutions: No  
  
### Notes  
 All Connection Roles are stored jointly in one file.  
  
### Files  
 \Other\ConnectionRoles.xml  
  
<a name="dashboard_bm"></a>   
## Dashboard  
 Differs in managed solutions: No  
  
### Notes  
 Each dashboard is stored in a distinct file.  
  
### Files  
 \Dashboards\  
  
 {guid 1}.xml  
{guid n}.xml  
  
<a name="workflow_bm"></a>   
## Workflow  
 Differs in managed solutions: No  
  
### Notes  
  
1.  The XAML for each workflow is stored in a distinct file.  
  
2.  Metadata for each workflow resides in a similarly named file ending in .data.xml.  
  
### Files  
 \Workflows\  
  
 \<XamlFileName 1>.xaml  
\<XamlFileName 1>.xaml.data.xml  
\<XamlFileName n>.xaml  
\<XamlFileName n>.xaml.data.xml  
  
<a name="emailtemplate_bm"></a>   
## Email template  
 Differs in managed solutions: No  
  
### Notes  
  
1.  All email template metadata is stored in a single file.  
  
2.  Each email template uses four distinct files per language.  
  
### Files  
 \Templates\  
  
 EmailTemplates.xml  
  
 EmailDocuments\  
  
 \<LCID 1>\\{guid 1}\  
  
 Body.xsl  
Presentation.xml  
Subject.xsl  
Subjectpresentation.xml  
  
 \<LCID 1>\\{guid n}\  
  
 Body.xsl  
Presentation.xml  
Subject.xsl  
Subjectpresentation.xml  
  
 \<LCID n>\\{guid 1}\  
  
 Body.xsl  
Presentation.xml  
Subject.xsl  
Subjectpresentation.xml  
  
 \<LCID n>\\{guid n}\  
  
 Body.xsl  
Presentation.xml  
Subject.xsl  
Subjectpresentation.xml  
  
<a name="contracttemplate_bm"></a>   
## Contract template  
 Differs in managed solutions: No  
  
### Notes  
 All Contract template metadata is stored in a single file.  
  
### Files  
 \Templates\ContractTemplates.xml  
  
<a name="kbarticle_bm"></a>   
## Kb article template  
 Differs in managed solutions: No  
  
### Notes  
  
1.  All contract template metadata is stored in a single file.  
  
2.  Each contract template uses two distinct files per language.  
  
### Files  
 \Templates\  
  
 KBArticleTemplates.xml  
  
 KBArticleTemplates\  
  
 \<LCID 1>\\{guid 1}\  
  
 formatxml.xsl  
Structurexml.xml  
  
 \<LCID 1>\\{guid n}\  
  
 formatxml.xsl  
Structurexml.xml  
  
 \<LCID n>\\{guid 1}\  
  
 formatxml.xsl  
Structurexml.xml  
  
 \<LCID n>\\{guid n}\  
  
 formatxml.xsl  
Structurexml.xml  
  
<a name="mailmerge_bm"></a>   
## Mail merge template  
 Differs in managed solutions: No  
  
### Notes  
  
1.  All mail merge template metadata is stored in a single file.  
  
2.  Each mail merge template uses two distinct files per language.  
  
3.  Documents that are shared across multiple templates will be stored in a single distinct file.  
  
### Files  
 \Templates\  
  
 MailMergeTemplates.xml  
  
 MailMergeDocuments\  
  
 \<LCID 1>\\{guid 1}\\<document name 1>.xml  
\<LCID 1>\\{guid n}\\<document name n\>.xml  
\<LCID n>\\{guid 1}\\<document name 1>.xml  
\<LCID n>\\{guid n}\\<document name n\>.xml  
  
<a name="pluginassembly_bm"></a>   
## PluginAssembly  
 Differs in managed solutions: No  
  
### Notes  
  
1.  Each plug-in assembly will have a distinct file for the raw assembly bytes.  
  
2.  Plug-in assembly metadata is stored in a similar named file ending in .data.xml.  
  
3.  Including the raw assembly in source control is not recommended.  
  
### Files  
 \PluginAssemblies\  
  
 \<Assembly Name 1>-{guid 1}\  
  
 \<Assembly Name 1>.dll  
\<Assembly Name 1>.dll.data.xml  
  
 \<Assembly Name n>-{guid n}\  
  
 \<Assembly Name n>.dll  
\<Assembly Name n>.dll.data.xml  
  
<a name="step_bm"></a>   
## SdkMessageProcessingStep  
 Differs in managed solutions: No  
  
### Notes  
 Each SDK message processing step is stored in a distinct file.  
  
### Files  
 \SdkMessageProcessingSteps\  
  
 {guid 1}.xml  
{guid n}.xml  
  
<a name="serviceendpoint_bm"></a>   
## ServiceEndpoint  
 Differs in managed solutions: No  
  
### Notes  
 All service end point metadata is jointly stored in one file.  
  
### Files  
 \PluginAssemblies\ServiceEndpoints.xml  
  
<a name="reports_bm"></a>   
## Reports  
 Differs in managed solutions: No  
  
### Notes  
  
1.  Reports are stored in a distinct sub-folder per language.  
  
2.  Each report has a distinct file within that folder.  
  
3.  Metadata for each report is stored within a similar named file ending in .data.xml.  
  
### Files  
 \Reports\  
  
 ReportSignatureIdMappings.xml  
  
 ReportLinks.xml  
  
 \<LCID 1>\\{guid 1}\  
  
 \<Report Name 1>.rdl  
\<Report Name 1>.rdl.data.xml  
  
 \<LCID 1>\\{guid n}\  
  
 \<Report Name n>.rdl  
\<Report Name n>.rdl.data.xml  
  
 \<LCID n>\\{guid 1}\  
  
 \<Report Name 1>.rdl  
\<Report Name 1>.rdl.data.xml  
  
 \<LCID n>\\{guid n}\  
  
 \<Report Name n>.rdl  
\<Report Name n>.rdl.data.xml  
  
<a name="entitymap_bm"></a>   
## EntityMap  
 Differs in managed solutions: No  
  
### Notes  
 All entity maps are stored in a single file.  
  
### Files  
 \Other\EntityMaps.xml  
  
### See also  
 [Use the SolutionPackager Tool to Compress and Extract a Solution File](compress-extract-solution-file-solutionpackager.md)   
