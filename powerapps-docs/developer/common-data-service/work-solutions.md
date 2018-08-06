---
title: "<Topic Title> (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces"
description: "<Description>" # 115-145 characters including spaces. This abstract displays in the search result."
keywords: ""
ms.date: 08/01/2018
ms.service:
  - "powerapps"
ms.custom:
  - ""
ms.topic: article
ms.assetid: 33c9da5b-27dd-d82d-1eb1-7b3b69b6032b
author: shmcarth" # GitHub ID
ms.author: jdaly" # MSFT alias of Microsoft employees only
manager: ryjones" # MSFT alias of manager or PM counterpart
ms.reviewer: 
---

# Work with solutions

<!-- https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/work-solutions -->

This topic presents specific programming tasks included in [Sample: Work With Solutions](sample-work-solutions.md) and [Sample: Detect Solution Dependencies](sample-detect-solution-dependencies.md).  
  
<a name="BKMK_CreatePublisher"></a>

## Create a publisher

 Every solution requires a publisher, represented by the [Publisher Entity](entities/publisher.md). A solution cannot use the `Microsoft Corporation` publisher but it can use the `Default` publisher for the organization or a new publisher  
  
 A publisher requires the following:  
  
- A customization prefix  
  
- A unique name  
  
- A friendly name  
  
  The following sample first defines a publisher and then checks to see whether the publisher already exists based on the unique name. If it already exists, the customization prefix may have been changed, so this sample seeks to capture the current customization prefix. The `PublisherId` is also captured so that the publisher record can be deleted. If the publisher is not found, a new publisher is created using the<xref:Microsoft.Xrm.Sdk.IOrganizationService>. <xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*> method  
  
  [!code-csharp[Solutions#WorkWithSolutions1](../snippets/csharp/CRMV8/solutions/cs/workwithsolutions1.cs#workwithsolutions1)]  
  
<a name="BKMK_RetrieveDefaultPublisher"></a>   
## Retrieve the default publisher  
 This sample shows how toretrieve the default publisher. The default publisher has a constant GUID value: `d21aab71-79e7-11dd-8874-00188b01e34f`.  
  
 [!code-csharp[Solutions#WorkWithSolutions2](../snippets/csharp/CRMV8/solutions/cs/workwithsolutions2.cs#workwithsolutions2)]  
  
<a name="BKMK_CreateASolution"></a>
 
## Create a solution

 The following sample shows how to create an unmanaged solution using the SDK Samples publisher created in [Create a Publisher](work-solutions.md#BKMK_CreatePublisher).  
  
 A solution requires the following:  
  
- A Publisher  
  
- A Friendly Name  
  
- A Unique Name  
  
- A Version Number  
  
  The variable `_crmSdkPublisherId` is a GUID value representing the `publisherid` value.  
  
  This sample checks whether the Solution already exists in the organization based on the unique name. If the solution does not exist it is created. The `SolutionId` value is captured so the solution can be deleted.  
  
  [!code-csharp[Solutions#WorkWithSolutions3](../snippets/csharp/CRMV8/solutions/cs/workwithsolutions3.cs#workwithsolutions3)]
  
<a name="BKMK_RetrieveASolution"></a>   
## Retrieve a solution  
 To retrieve a specific solution you can use the solution’s `UniqueName`. Each organization will have a default solution with a constant GUID value: `FD140AAF-4DF4-11DD-BD17-0019B9312238`.  
  
 This sample shows how to retrieve data for a solution with the unique name ”samplesolution”. A solution with this name is created in [Create a Solution](work-solutions.md#BKMK_CreateASolution).  
  
 [!code-csharp[Solutions#WorkWithSolutions4](../snippets/csharp/CRMV8/solutions/cs/workwithsolutions4.cs#workwithsolutions4)] 
  
<a name="BKMK_AddANewSolutionComponent"></a>   
## Add a new solution component  
 This sample shows how to create a solution component that is associated with a specific solution. If you don’t associate the solution component to a specific solution when it is created it will only be added to the default solution and you will need to add it to a solution manually or by using the code included in the [Add an Existing Solution Component](work-solutions.md#BKMK_AddExistingSolutionComponent).  
  
 This code creates a new global option set and adds it to the solution with a unique name equal to `_primarySolutionName`.  
  
 [!code-csharp[Solutions#GetSolutionDependencies3](../snippets/csharp/CRMV8/solutions/cs/getsolutiondependencies3.cs#getsolutiondependencies3)]  
  
<a name="BKMK_AddExistingSolutionComponent"></a>   
## Add an existing solution component  
 This sample shows how to add an existing solution component to a solution.  
  
 The following code uses the <xref:Microsoft.Crm.Sdk.Messages.AddSolutionComponentRequest> to add the `Account` entity as a solution component to an unmanaged solution.  
  
 [!code-csharp[Solutions#WorkWithSolutions5](../snippets/csharp/CRMV8/solutions/cs/workwithsolutions5.cs#workwithsolutions5)] 
  
<a name="BKMK_RemoveSolutionComponent"></a>   
## Remove a solution component  
 This sample shows how to remove a solution component from an unmanaged solution. The following code uses the <xref:Microsoft.Crm.Sdk.Messages.RemoveSolutionComponentRequest> to remove an entity solution component from an unmanaged solution. The `solution.UniqueName` references the Solution created in the [Create a Solution](work-solutions.md#BKMK_CreateASolution).  
  
 [!code-csharp[Solutions#WorkWithSolutions6](../snippets/csharp/CRMV8/solutions/cs/workwithsolutions6.cs#workwithsolutions6)]
  
<a name="BKMK_ExportPackageSolution"></a>   
## Export or package a solution  
 This sample shows how to export an unmanaged solution or package a managed solution. The code uses <xref:Microsoft.Crm.Sdk.Messages.ExportSolutionRequest> to export a compressed file representing an unmanaged solution. The option to create a managed solution is set using the <xref:Microsoft.Crm.Sdk.Messages.ExportSolutionRequest.Managed> property. This sample saves a file named samplesolution.zip to the `c:\temp\` folder.  
  
 [!code-csharp[Solutions#WorkWithSolutions7](../snippets/csharp/CRMV8/solutions/cs/workwithsolutions7.cs#workwithsolutions7)]
  
<a name="BKMK_InstallUpgradeSolution"></a>   
## Install or upgrade a solution  
 This sample shows how to install or upgrade a solution using the <xref:Microsoft.Crm.Sdk.Messages.ImportSolutionRequest> message.  
  
 You can use the `ImportJob` entity to capture data about the success of the import.  
  
 The following sample shows how to import a solution without tracking the success.  
  
 [!code-csharp[Solutions#WorkWithSolutions8](../snippets/csharp/CRMV8/solutions/cs/workwithsolutions8.cs#workwithsolutions8)] 
  
### Tracking import success
 When you specify an <xref:Microsoft.Crm.Sdk.Messages.ImportSolutionRequest.ImportJobId> for the `ImportSolutionRequest`, you can use that value to query the `ImportJob` entity about the status of the import.  
  
 The `ImportJobId` can also be used to download an import log file using the <xref:Microsoft.Crm.Sdk.Messages.RetrieveFormattedImportJobResultsRequest> message.  
  
#### Retrieving import job data

 The following sample shows how to retrieve the import job record and the content of the `ImportJob.Data` attribute.  
  
 [!code-csharp[Solutions#WorkWithSolutions9](../snippets/csharp/CRMV8/solutions/cs/workwithsolutions9.cs#workwithsolutions9)]  
  
 The contents of the `Data` property is a string representing an XML file. The following is a sample captured using the code in this sample. This managed solution contained a single global option set called `sample_tempsampleglobaloptionsetname`.  
  
```xml  
<importexportxml start="634224017519682730"  
                 stop="634224017609764033"  
                 progress="80"  
                 processed="true">  
 <solutionManifests>  
  <solutionManifest languagecode="1033"  
                    id="samplesolutionforImport"  
                    LocalizedName="Sample Solution for Import"  
                    processed="true">  
   <UniqueName>samplesolutionforImport</UniqueName>  
   <LocalizedNames>  
    <LocalizedName description="Sample Solution for Import"  
                   languagecode="1033" />  
   </LocalizedNames>  
   <Descriptions>  
    <Description description="This solution was created by the WorkWithSolutions sample code in the Microsoft CRM SDK samples."  
                 languagecode="1033" />  
   </Descriptions>  
   <Version>1.0</Version>  
   <Managed>1</Managed>  
   <Publisher>  
    <UniqueName>sdksamples</UniqueName>  
    <LocalizedNames>  
     <LocalizedName description="Microsoft CRM SDK Samples"  
                    languagecode="1033" />  
    </LocalizedNames>  
    <Descriptions>  
     <Description description="This publisher was created with samples from the Microsoft CRM SDK"  
                  languagecode="1033" />  
    </Descriptions>  
    <EMailAddress>someone@microsoft.com</EMailAddress>  
    <SupportingWebsiteUrl>http://msdn.microsoft.com/en-us/dynamics/crm/default.aspx</SupportingWebsiteUrl>  
    <Addresses>  
     <Address>  
      <City />  
      <Country />  
      <Line1 />  
      <Line2 />  
      <PostalCode />  
      <StateOrProvince />  
      <Telephone1 />  
     </Address>  
    </Addresses>  
   </Publisher>  
   <results />  
   <result result="success"  
           errorcode="0"  
           errortext=""  
           datetime="20:49:12.08"  
           datetimeticks="634224269520845122" />  
  </solutionManifest>  
 </solutionManifests>  
 <upgradeSolutionPackageInformation>  
  <upgradeRequired>0</upgradeRequired>  
  <upgradeValid>1</upgradeValid>  
  <fileVersion>5.0.9669.0</fileVersion>  
  <currentVersion>5.0.9669.0</currentVersion>  
  <fileSku>OnPremise</fileSku>  
  <currentSku>OnPremise</currentSku>  
 </upgradeSolutionPackageInformation>  
 <entities />  
 <nodes />  
 <settings />  
 <dashboards />  
 <securityroles />  
 <workflows />  
 <templates />  
 <optionSets>  
  <optionSet id="sample_tempsampleglobaloptionsetname"  
             LocalizedName="Example Option Set"  
             Description=""  
             processed="true">  
   <result result="success"  
           errorcode="0"  
           errortext=""  
           datetime="20:49:16.10"  
           datetimeticks="634224269561025400" />  
  </optionSet>  
 </optionSets>  
 <ConnectionRoles />  
 <SolutionPluginAssemblies />  
 <SdkMessageProcessingSteps />  
 <ServiceEndpoints />  
 <webResources />  
 <reports />  
 <FieldSecurityProfiles />  
 <languages>  
  <language>  
   <result result="success"  
           errorcode="0"  
           errortext=""  
           datetime="20:49:12.00"  
           datetimeticks="634224269520092986" />  
  </language>  
 </languages>  
 <entitySubhandlers />  
 <publishes>  
  <publish processed="false" />  
 </publishes>  
 <rootComponents>  
  <rootComponent processed="true">  
   <result result="success"  
           errorcode="0"  
           errortext=""  
           datetime="20:49:20.83"  
           datetimeticks="634224269608387238" />  
  </rootComponent>  
 </rootComponents>  
 <dependencies>  
  <dependency processed="true">  
   <result result="success"  
           errorcode="0"  
           errortext=""  
           datetime="20:49:20.97"  
           datetimeticks="634224269609715208" />  
  </dependency>  
 </dependencies>  
</importexportxml>  
```  
  
<a name="BKMK_DeleteSolution"></a>

## Delete a solution

 This sample shows how to delete a solution.The following sample shows how to retrieve a solution using the solution `uniquename` and then extract the `solutionid` from the results. Use the `solutionid` with the<xref:Microsoft.Xrm.Sdk.IOrganizationService>. <xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*> method.  
  
 [!code-csharp[Solutions#WorkWithSolutions10](../snippets/csharp/CRMV8/solutions/cs/workwithsolutions10.cs#workwithsolutions10)] 
  
<a name="BKMK_DetectSolutionDependencies"></a>

## Detect solution dependencies

 This sample shows how to create a report showing the dependencies between solution components.  
  
 This code will:  
  
- Retrieve all the components for a solution.  
  
- Retrieve all the dependencies for each component.  
  
- For each dependency found display a report describing the dependency.  
  
  [!code-csharp[Solutions#GetSolutionDependencies1](../snippets/csharp/CRMV8/solutions/cs/getsolutiondependencies1.cs#getsolutiondependencies1)]
  
  The `DependencyReport` method is in the following code sample.  
  
### Dependency report

 The `DependencyReport` method provides a friendlier message based on information found within the dependency.  
  
> [!NOTE]
>  In this sample the method is only partially implemented. It can display messages only for attribute and option set solution components.  
  
 [!code-csharp[Solutions#GetSolutionDependencies7](../snippets/csharp/CRMV8/solutions/cs/getsolutiondependencies7.cs#getsolutiondependencies7)]
  
  
### Detect whether a solution component may be delete

 Use the <xref:Microsoft.Crm.Sdk.Messages.RetrieveDependenciesForDeleteRequest> message to identify any other solution components which would prevent a given solution component from being deleted. The following code sample looks for any attributes using a known global optionset. Any attribute using the global optionset would prevent the global optionset from being deleted.  
  
 [!code-csharp[Solutions#GetSolutionDependencies8](../snippets/csharp/CRMV8/solutions/cs/getsolutiondependencies8.cs#getsolutiondependencies8)]

### See also

 [Package and Distribute Extensions with Dynamics 365 Solutions](package-distribute-extensions-use-solutions.md)   
 [Introduction to Solutions](introduction-solutions.md)   
 [Plan For Solution Development](/dynamics365/customer-engagement/developer/plan-solution-development)   
 [Dependency Tracking for Solution Components](dependency-tracking-solution-components.md)   
 [Create, Export, or Import an Unmanaged Solution](create-export-import-unmanaged-solution.md)   
 [Create, Install, and Update a Managed Solution](create-install-update-managed-solution.md)   
 [Uninstall or Delete a solution](uninstall-delete-solution.md)   
 [Solution Entities](/dynamics365/customer-engagement/developer/solution-entities)   
 [Sample: Work With Solutions](org-service/samples/work-solutions.md)
 [Sample: Detect Solution Dependencies](/dynamics365/customer-engagement/developer/sample-detect-solution-dependencies)