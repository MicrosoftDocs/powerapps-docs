---
title: "Work with solutions (Common Data Service for Apps) | Microsoft Docs"
description: ""
keywords: ""
ms.date: 08/01/2018
ms.service:
  - "powerapps"
ms.custom:
  - ""
ms.topic: article
ms.assetid: 33c9da5b-27dd-d82d-1eb1-7b3b69b6032b
author: shmcarth # GitHub ID
ms.author: jdaly # MSFT alias of Microsoft employees only
manager: ryjones # MSFT alias of manager or PM counterpart
ms.reviewer: 
---

# Work with solutions

This topic presents specific programming tasks included in [Sample: Work With Solutions](org-service/samples/work-solutions.md) and [Sample: Detect Solution Dependencies](org-service/samples/detect-solution-dependencies.md).  
  
<a name="BKMK_CreatePublisher"></a>

## Create a publisher

 Every solution requires a publisher, represented by the [Publisher Entity](reference/entities/publisher.md). A solution cannot use the `Microsoft Corporation` publisher but it can use the `Default` publisher for the organization or a new publisher  
  
 A publisher requires the following:  
  
- A customization prefix  
  
- A unique name  
  
- A friendly name  
  
  The following sample first defines a publisher and then checks to see whether the publisher already exists based on the unique name. If it already exists, the customization prefix may have been changed, so this sample seeks to capture the current customization prefix. The `PublisherId` is also captured so that the publisher record can be deleted. If the publisher is not found, a new publisher is created using the<xref:Microsoft.Xrm.Sdk.IOrganizationService>. <xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*> method 

  ```csharp
  //Define a new publisher
Publisher _crmSdkPublisher = new Publisher
{
    UniqueName = "sdksamples",
    FriendlyName = "Microsoft CRM SDK Samples",
    SupportingWebsiteUrl = "http://msdn.microsoft.com/en-us/dynamics/crm/default.aspx",
    CustomizationPrefix = "sample",
    EMailAddress = "someone@microsoft.com",
    Description = "This publisher was created with samples from the Microsoft Dynamics CRM SDK"
};

//Does publisher already exist?
QueryExpression querySDKSamplePublisher = new QueryExpression
{
    EntityName = Publisher.EntityLogicalName,
    ColumnSet = new ColumnSet("publisherid", "customizationprefix"),
    Criteria = new FilterExpression()
};

querySDKSamplePublisher.Criteria.AddCondition("uniquename", ConditionOperator.Equal, _crmSdkPublisher.UniqueName);
EntityCollection querySDKSamplePublisherResults = _serviceProxy.RetrieveMultiple(querySDKSamplePublisher);
Publisher SDKSamplePublisherResults = null;

//If it already exists, use it
if (querySDKSamplePublisherResults.Entities.Count > 0)
{
    SDKSamplePublisherResults = (Publisher)querySDKSamplePublisherResults.Entities[0];
    _crmSdkPublisherId = (Guid)SDKSamplePublisherResults.PublisherId;
    _customizationPrefix = SDKSamplePublisherResults.CustomizationPrefix;
}
//If it doesn't exist, create it
if (SDKSamplePublisherResults == null)
{
    _crmSdkPublisherId = _serviceProxy.Create(_crmSdkPublisher);
    Console.WriteLine(String.Format("Created publisher: {0}.", _crmSdkPublisher.FriendlyName));
    _customizationPrefix = _crmSdkPublisher.CustomizationPrefix;
}
  ``` 
  
<a name="BKMK_RetrieveDefaultPublisher"></a>   
## Retrieve the default publisher  
 This sample shows how toretrieve the default publisher. The default publisher has a constant GUID value: `d21aab71-79e7-11dd-8874-00188b01e34f`.  
  
```csharp
// Retrieve the Default Publisher

//The default publisher has a constant GUID value;
Guid DefaultPublisherId = new Guid("{d21aab71-79e7-11dd-8874-00188b01e34f}");

Publisher DefaultPublisher = (Publisher)_serviceProxy.Retrieve(Publisher.EntityLogicalName, DefaultPublisherId, new ColumnSet(new string[] {"friendlyname" }));

EntityReference DefaultPublisherReference = new EntityReference
{
    Id = DefaultPublisher.Id,
    LogicalName = Publisher.EntityLogicalName,
    Name = DefaultPublisher.FriendlyName
};
Console.WriteLine("Retrieved the {0}.", DefaultPublisherReference.Name);
```
  
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
  
  ```csharp
  // Create a Solution
//Define a solution
Solution solution = new Solution
{
    UniqueName = "samplesolution",
    FriendlyName = "Sample Solution",
    PublisherId = new EntityReference(Publisher.EntityLogicalName, _crmSdkPublisherId),
    Description = "This solution was created by the WorkWithSolutions sample code in the Microsoft Dynamics CRM SDK samples.",
    Version = "1.0"
};

//Check whether it already exists
QueryExpression queryCheckForSampleSolution = new QueryExpression
{
    EntityName = Solution.EntityLogicalName,
    ColumnSet = new ColumnSet(),
    Criteria = new FilterExpression()
};
queryCheckForSampleSolution.Criteria.AddCondition("uniquename", ConditionOperator.Equal, solution.UniqueName);

//Create the solution if it does not already exist.
EntityCollection querySampleSolutionResults = _serviceProxy.RetrieveMultiple(queryCheckForSampleSolution);
Solution SampleSolutionResults = null;
if (querySampleSolutionResults.Entities.Count > 0)
{
    SampleSolutionResults = (Solution)querySampleSolutionResults.Entities[0];
    _solutionsSampleSolutionId = (Guid)SampleSolutionResults.SolutionId;
}
if (SampleSolutionResults == null)
{
    _solutionsSampleSolutionId = _serviceProxy.Create(solution);
}
  ```
  
<a name="BKMK_RetrieveASolution"></a>   
## Retrieve a solution  
 To retrieve a specific solution you can use the solution’s `UniqueName`. Each organization will have a default solution with a constant GUID value: `FD140AAF-4DF4-11DD-BD17-0019B9312238`.  
  
 This sample shows how to retrieve data for a solution with the unique name ”samplesolution”. A solution with this name is created in [Create a Solution](work-solutions.md#BKMK_CreateASolution).  
  
 ```csharp
 // Retrieve a solution
String solutionUniqueName = "samplesolution";
QueryExpression querySampleSolution = new QueryExpression
{
    EntityName = Solution.EntityLogicalName,
    ColumnSet = new ColumnSet(new string[] { "publisherid", "installedon", "version", "versionnumber", "friendlyname" }),
    Criteria = new FilterExpression()
};

querySampleSolution.Criteria.AddCondition("uniquename", ConditionOperator.Equal, solutionUniqueName);
Solution SampleSolution = (Solution)_serviceProxy.RetrieveMultiple(querySampleSolution).Entities[0];
 ``` 
  
<a name="BKMK_AddANewSolutionComponent"></a>   
## Add a new solution component  
 This sample shows how to create a solution component that is associated with a specific solution. If you don’t associate the solution component to a specific solution when it is created it will only be added to the default solution and you will need to add it to a solution manually or by using the code included in the [Add an Existing Solution Component](work-solutions.md#BKMK_AddExistingSolutionComponent).  
  
 This code creates a new global option set and adds it to the solution with a unique name equal to `_primarySolutionName`.  
  
 ```csharp
 OptionSetMetadata optionSetMetadata = new OptionSetMetadata()
{
    Name = _globalOptionSetName,
    DisplayName = new Label("Example Option Set", _languageCode),
    IsGlobal = true,
    OptionSetType = OptionSetType.Picklist,
    Options =
{
    new OptionMetadata(new Label("Option 1", _languageCode), 1),
    new OptionMetadata(new Label("Option 2", _languageCode), 2)
}
};
CreateOptionSetRequest createOptionSetRequest = new CreateOptionSetRequest
{
    OptionSet = optionSetMetadata                
};

createOptionSetRequest.SolutionUniqueName = _primarySolutionName;
_serviceProxy.Execute(createOptionSetRequest);
 ```  
  
<a name="BKMK_AddExistingSolutionComponent"></a>   
## Add an existing solution component  
 This sample shows how to add an existing solution component to a solution.  
  
 The following code uses the <xref:Microsoft.Crm.Sdk.Messages.AddSolutionComponentRequest> to add the `Account` entity as a solution component to an unmanaged solution.  
  
 ```csharp
 // Add an existing Solution Component
//Add the Account entity to the solution
RetrieveEntityRequest retrieveForAddAccountRequest = new RetrieveEntityRequest()
{
    LogicalName = Account.EntityLogicalName
};
RetrieveEntityResponse retrieveForAddAccountResponse = (RetrieveEntityResponse)_serviceProxy.Execute(retrieveForAddAccountRequest);
AddSolutionComponentRequest addReq = new AddSolutionComponentRequest()
{
    ComponentType = (int)componenttype.Entity,
    ComponentId = (Guid)retrieveForAddAccountResponse.EntityMetadata.MetadataId,
    SolutionUniqueName = solution.UniqueName
};
_serviceProxy.Execute(addReq);
``` 
  
<a name="BKMK_RemoveSolutionComponent"></a>   
## Remove a solution component  
 This sample shows how to remove a solution component from an unmanaged solution. The following code uses the <xref:Microsoft.Crm.Sdk.Messages.RemoveSolutionComponentRequest> to remove an entity solution component from an unmanaged solution. The `solution.UniqueName` references the Solution created in the [Create a Solution](work-solutions.md#BKMK_CreateASolution).  
  
 ```csharp
 // Remove a Solution Component
//Remove the Account entity from the solution
RetrieveEntityRequest retrieveForRemoveAccountRequest = new RetrieveEntityRequest()
{
    LogicalName = Account.EntityLogicalName
};
RetrieveEntityResponse retrieveForRemoveAccountResponse = (RetrieveEntityResponse)_serviceProxy.Execute(retrieveForRemoveAccountRequest);

RemoveSolutionComponentRequest removeReq = new RemoveSolutionComponentRequest()
{
    ComponentId = (Guid)retrieveForRemoveAccountResponse.EntityMetadata.MetadataId,
    ComponentType = (int)componenttype.Entity,
    SolutionUniqueName = solution.UniqueName
};
_serviceProxy.Execute(removeReq);
```
  
<a name="BKMK_ExportPackageSolution"></a>   
## Export or package a solution  
 This sample shows how to export an unmanaged solution or package a managed solution. The code uses <xref:Microsoft.Crm.Sdk.Messages.ExportSolutionRequest> to export a compressed file representing an unmanaged solution. The option to create a managed solution is set using the <xref:Microsoft.Crm.Sdk.Messages.ExportSolutionRequest.Managed> property. This sample saves a file named samplesolution.zip to the `c:\temp\` folder.  
  
```csharp
// Export or package a solution
//Export an a solution

ExportSolutionRequest exportSolutionRequest = new ExportSolutionRequest();
exportSolutionRequest.Managed = false;
exportSolutionRequest.SolutionName = solution.UniqueName;

ExportSolutionResponse exportSolutionResponse = (ExportSolutionResponse)_serviceProxy.Execute(exportSolutionRequest);

byte[] exportXml = exportSolutionResponse.ExportSolutionFile;
string filename = solution.UniqueName + ".zip";
File.WriteAllBytes(outputDir + filename, exportXml);

Console.WriteLine("Solution exported to {0}.", outputDir + filename);
``` 

<a name="BKMK_InstallUpgradeSolution"></a>   
## Install or upgrade a solution  
 This sample shows how to install or upgrade a solution using the <xref:Microsoft.Crm.Sdk.Messages.ImportSolutionRequest> message.  
  
 You can use the `ImportJob` entity to capture data about the success of the import.  
  
 The following sample shows how to import a solution without tracking the success.  
  
 ```csharp
 // Install or Upgrade a Solution                  

byte[] fileBytes = File.ReadAllBytes(ManagedSolutionLocation);

ImportSolutionRequest impSolReq = new ImportSolutionRequest()
{
    CustomizationFile = fileBytes
};

_serviceProxy.Execute(impSolReq);

Console.WriteLine("Imported Solution from {0}", ManagedSolutionLocation);
 ```  
  
### Tracking import success
 When you specify an <xref:Microsoft.Crm.Sdk.Messages.ImportSolutionRequest.ImportJobId> for the `ImportSolutionRequest`, you can use that value to query the `ImportJob` entity about the status of the import.  
  
 The `ImportJobId` can also be used to download an import log file using the <xref:Microsoft.Crm.Sdk.Messages.RetrieveFormattedImportJobResultsRequest> message.  
  
#### Retrieving import job data

 The following sample shows how to retrieve the import job record and the content of the `ImportJob.Data` attribute.  
  
```csharp
// Monitor import success
byte[] fileBytesWithMonitoring = File.ReadAllBytes(ManagedSolutionLocation);

ImportSolutionRequest impSolReqWithMonitoring = new ImportSolutionRequest()
{
    CustomizationFile = fileBytes,
    ImportJobId = Guid.NewGuid()
};

_serviceProxy.Execute(impSolReqWithMonitoring);
Console.WriteLine("Imported Solution with Monitoring from {0}", ManagedSolutionLocation);

ImportJob job = (ImportJob)_serviceProxy.Retrieve(ImportJob.EntityLogicalName, impSolReqWithMonitoring.ImportJobId, new ColumnSet(new System.String[] { "data", "solutionname" }));


System.Xml.XmlDocument doc = new System.Xml.XmlDocument();
doc.LoadXml(job.Data);

String ImportedSolutionName = doc.SelectSingleNode("//solutionManifest/UniqueName").InnerText;
String SolutionImportResult = doc.SelectSingleNode("//solutionManifest/result/@result").Value;

Console.WriteLine("Report from the ImportJob data");
Console.WriteLine("Solution Unique name: {0}", ImportedSolutionName);
Console.WriteLine("Solution Import Result: {0}", SolutionImportResult);
Console.WriteLine("");

// This code displays the results for Global Option sets installed as part of a solution.

System.Xml.XmlNodeList optionSets = doc.SelectNodes("//optionSets/optionSet");
foreach (System.Xml.XmlNode node in optionSets)
{
    string OptionSetName = node.Attributes["LocalizedName"].Value;
    string result = node.FirstChild.Attributes["result"].Value;

    if (result == "success")
    {
        Console.WriteLine("{0} result: {1}",OptionSetName, result);
    }
    else
    {
        string errorCode = node.FirstChild.Attributes["errorcode"].Value;
        string errorText = node.FirstChild.Attributes["errortext"].Value;

        Console.WriteLine("{0} result: {1} Code: {2} Description: {3}",OptionSetName, result, errorCode, errorText);
    }
}
```   
  
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
  
```csharp
// Delete a solution

QueryExpression queryImportedSolution = new QueryExpression
{
    EntityName = Solution.EntityLogicalName,
    ColumnSet = new ColumnSet(new string[] { "solutionid", "friendlyname" }),
    Criteria = new FilterExpression()
};


queryImportedSolution.Criteria.AddCondition("uniquename", ConditionOperator.Equal, ImportedSolutionName);

Solution ImportedSolution = (Solution)_serviceProxy.RetrieveMultiple(queryImportedSolution).Entities[0];

_serviceProxy.Delete(Solution.EntityLogicalName, (Guid)ImportedSolution.SolutionId);

Console.WriteLine("Deleted the {0} solution.", ImportedSolution.FriendlyName);
```  
  
<a name="BKMK_DetectSolutionDependencies"></a>

## Detect solution dependencies

 This sample shows how to create a report showing the dependencies between solution components.  
  
 This code will:  
  
- Retrieve all the components for a solution.  
  
- Retrieve all the dependencies for each component.  
  
- For each dependency found display a report describing the dependency.  
  
```csharp
// Grab all Solution Components for a solution.
QueryByAttribute componentQuery = new QueryByAttribute
{
    EntityName = SolutionComponent.EntityLogicalName,
    ColumnSet = new ColumnSet("componenttype", "objectid", "solutioncomponentid", "solutionid"),
    Attributes = { "solutionid" },

    // In your code, this value would probably come from another query.
    Values = { _primarySolutionId }
};

IEnumerable<SolutionComponent> allComponents =
    _serviceProxy.RetrieveMultiple(componentQuery).Entities.Cast<SolutionComponent>();

foreach (SolutionComponent component in allComponents)
{
    // For each solution component, retrieve all dependencies for the component.
    RetrieveDependentComponentsRequest dependentComponentsRequest =
        new RetrieveDependentComponentsRequest
        {
            ComponentType = component.ComponentType.Value,
            ObjectId = component.ObjectId.Value
        };
    RetrieveDependentComponentsResponse dependentComponentsResponse =
        (RetrieveDependentComponentsResponse)_serviceProxy.Execute(dependentComponentsRequest);

    // If there are no dependent components, we can ignore this component.
    if (dependentComponentsResponse.EntityCollection.Entities.Any() == false)
        continue;

    // If there are dependencies upon this solution component, and the solution
    // itself is managed, then you will be unable to delete the solution.
    Console.WriteLine("Found {0} dependencies for Component {1} of type {2}",
        dependentComponentsResponse.EntityCollection.Entities.Count,
        component.ObjectId.Value,
        component.ComponentType.Value
        );
    //A more complete report requires more code
    foreach (Dependency d in dependentComponentsResponse.EntityCollection.Entities)
    {
        DependencyReport(d);
    }
}
``` 
  
  The `DependencyReport` method is in the following code sample.  
  
### Dependency report

 The `DependencyReport` method provides a friendlier message based on information found within the dependency.  
  
> [!NOTE]
>  In this sample the method is only partially implemented. It can display messages only for attribute and option set solution components.  
  
```csharp
/// <summary>
   /// Shows how to get a more friendly message based on information within the dependency
   /// <param name="dependency">A Dependency returned from the RetrieveDependentComponents message</param>
   /// </summary> 
public void DependencyReport(Dependency dependency)
   {
 //These strings represent parameters for the message.
    String dependentComponentName = "";
    String dependentComponentTypeName = "";
    String dependentComponentSolutionName = "";
    String requiredComponentName = "";
    String requiredComponentTypeName = "";
    String requiredComponentSolutionName = "";

 //The ComponentType global Option Set contains options for each possible component.
    RetrieveOptionSetRequest componentTypeRequest = new RetrieveOptionSetRequest
    {
     Name = "componenttype"
    };

    RetrieveOptionSetResponse componentTypeResponse = (RetrieveOptionSetResponse)_serviceProxy.Execute(componentTypeRequest);
    OptionSetMetadata componentTypeOptionSet = (OptionSetMetadata)componentTypeResponse.OptionSetMetadata;
 // Match the Component type with the option value and get the label value of the option.
    foreach (OptionMetadata opt in componentTypeOptionSet.Options)
    {
     if (dependency.DependentComponentType.Value == opt.Value)
     {
      dependentComponentTypeName = opt.Label.UserLocalizedLabel.Label;
     }
     if (dependency.RequiredComponentType.Value == opt.Value)
     {
      requiredComponentTypeName = opt.Label.UserLocalizedLabel.Label;
     }
    }
 //The name or display name of the compoent is retrieved in different ways depending on the component type
    dependentComponentName = getComponentName(dependency.DependentComponentType.Value, (Guid)dependency.DependentComponentObjectId);
    requiredComponentName = getComponentName(dependency.RequiredComponentType.Value, (Guid)dependency.RequiredComponentObjectId);

 // Retrieve the friendly name for the dependent solution.
    Solution dependentSolution = (Solution)_serviceProxy.Retrieve
     (
      Solution.EntityLogicalName,
      (Guid)dependency.DependentComponentBaseSolutionId,
      new ColumnSet("friendlyname")
     );
    dependentComponentSolutionName = dependentSolution.FriendlyName;
    
 // Retrieve the friendly name for the required solution.
    Solution requiredSolution = (Solution)_serviceProxy.Retrieve
      (
       Solution.EntityLogicalName,
       (Guid)dependency.RequiredComponentBaseSolutionId,
       new ColumnSet("friendlyname")
      );
    requiredComponentSolutionName = requiredSolution.FriendlyName;

 //Display the message
     Console.WriteLine("The {0} {1} in the {2} depends on the {3} {4} in the {5} solution.",
     dependentComponentName,
     dependentComponentTypeName,
     dependentComponentSolutionName,
     requiredComponentName,
     requiredComponentTypeName,
     requiredComponentSolutionName);
   }
```
  
### Detect whether a solution component may be delete

 Use the <xref:Microsoft.Crm.Sdk.Messages.RetrieveDependenciesForDeleteRequest> message to identify any other solution components which would prevent a given solution component from being deleted. The following code sample looks for any attributes using a known global optionset. Any attribute using the global optionset would prevent the global optionset from being deleted.  
  
```csharp
// Use the RetrieveOptionSetRequest message to retrieve  
// a global option set by it's name.
RetrieveOptionSetRequest retrieveOptionSetRequest =
    new RetrieveOptionSetRequest
    {
     Name = _globalOptionSetName
    };

// Execute the request.
RetrieveOptionSetResponse retrieveOptionSetResponse =
    (RetrieveOptionSetResponse)_serviceProxy.Execute(
    retrieveOptionSetRequest);
_globalOptionSetId = retrieveOptionSetResponse.OptionSetMetadata.MetadataId;
if (_globalOptionSetId != null)
{ 
 //Use the global OptionSet MetadataId with the appropriate componenttype
 // to call RetrieveDependenciesForDeleteRequest
 RetrieveDependenciesForDeleteRequest retrieveDependenciesForDeleteRequest = new RetrieveDependenciesForDeleteRequest 
{ 
 ComponentType = (int)componenttype.OptionSet,
 ObjectId = (Guid)_globalOptionSetId
};

 RetrieveDependenciesForDeleteResponse retrieveDependenciesForDeleteResponse =
  (RetrieveDependenciesForDeleteResponse)_serviceProxy.Execute(retrieveDependenciesForDeleteRequest);
 Console.WriteLine("");
 foreach (Dependency d in retrieveDependenciesForDeleteResponse.EntityCollection.Entities)
 {

  if (d.DependentComponentType.Value == 2)//Just testing for Attributes
  {
   String attributeLabel = "";
   RetrieveAttributeRequest retrieveAttributeRequest = new RetrieveAttributeRequest
   {
    MetadataId = (Guid)d.DependentComponentObjectId
   };
   RetrieveAttributeResponse retrieveAttributeResponse = (RetrieveAttributeResponse)_serviceProxy.Execute(retrieveAttributeRequest);

   AttributeMetadata attmet = retrieveAttributeResponse.AttributeMetadata;

   attributeLabel = attmet.DisplayName.UserLocalizedLabel.Label;
  
    Console.WriteLine("An {0} named {1} will prevent deleting the {2} global option set.", 
   (componenttype)d.DependentComponentType.Value, 
   attributeLabel, 
   _globalOptionSetName);
  }
 }                 
}
``` 

### See also

 [Package and Distribute Extensions with Dynamics 365 Solutions](/dynamics365/customer-engagement/developer/package-distribute-extensions-use-solutions)   
 [Introduction to Solutions](introduction-solutions.md)   
 [Plan For Solution Development](/dynamics365/customer-engagement/developer/plan-solution-development)   
 [Dependency Tracking for Solution Components](dependency-tracking-solution-components.md)   
 [Create, Export, or Import an Unmanaged Solution](create-export-import-unmanaged-solution.md)   
 [Create, Install, and Update a Managed Solution](create-install-update-managed-solution.md)   
 [Uninstall or Delete a solution](uninstall-delete-solution.md)   
 [Solution Entities](/dynamics365/customer-engagement/developer/solution-entities)   
 [Sample: Work With Solutions](org-service/samples/work-solutions.md)
 [Sample: Detect Solution Dependencies](/dynamics365/customer-engagement/developer/sample-detect-solution-dependencies)
