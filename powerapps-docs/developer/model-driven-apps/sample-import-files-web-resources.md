---
title: "Sample: Import files as web resources(model-driven apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "The sample provides a simplified example of importing files as web resources." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 04/14/2021
ms.reviewer: ""
ms.service: powerapps
ms.topic: "article"
author: "KumarVivek" # GitHub ID
ms.author: "kvivek" # MSFT alias of Microsoft employees only
manager: "shilpas" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Sample: Import files as web resources

When you develop a large number of files to use as Web resources you can save yourself the work of manually adding them through the application. Many Web resources can be developed and tested outside of Model-driven apps and then imported.  
  
This sample provides a simplified example of this process.  
 
Download the sample: [Import files as web resources](https://github.com/Microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23/ImportWebResources). 

[!INCLUDE[cc-terminology](../data-platform/includes/cc-terminology.md)]

## Prerequisites

[!INCLUDE[sdk-prerequisite](../../includes/sdk-prerequisite.md)]
  
## Requirements  

The sample code included in the SDK download package includes the following files required by this sample:  
  
 **ImportJob.xml**  
 This file provides data about the Web Resource records that will be created. For each file it contains the following data:  
  
- **path:** The path to each file from the FilesToImport folder.  
  
- **displayName:** The display name for the Web resource.  
  
- **description:** A description of what each file does.  
  
- **name:** The name that will be used for the Web Resource.  
  
  > [!NOTE]
  > - Each of these names begin with an underscore character. The customization prefix of the solution publisher will be prepended to the name when the Web resource is created. Rather than hard-coding a specific customization prefix, this sample will detect the current customization prefix for a publisher record that may already exist in the organization.  
  >   - Because each of these files was developed outside of Model-driven apps and depend on relative paths to access each other, the names include backslash “/” characters to create a virtual folder structure so the relative links will continue to function within Model-driven apps.  
  
- **type:** Specifies the type of Web Resource to create using the integer values found in [Web Resource Types](web-resources.md#BKMK_WebResourceTypes).
  
  **FilesToImport/ShowData.htm**  
  This HTML Web resource requires each of the other files to display the following table.  

|First Name|Last Name|
|-|-|
|Apurva|Dalia|  
|Ofer|Daliot|  
|Jim|Daly|  
|Ryan|Danner|  
|Mike|Danseglio|  
|Alex|Darrow|  
  
 **FilesToImport/CSS/Styles.css**  
 This file provides the CSS Styles used in ShowData.htm.  
  
 **FilesToImport/Data/Data.xml**  
 This file contains the list of names that is displayed in the table.  
  
 **FilesToImport/Script/Script.js**  
 This file contains a JScript library that contains information about the relative location of the Data.xml file and the Transform.xslt file. It also contains the `showData` function that transforms the data and adds it to the ShowData.htm page.  
  
 **FilesToImport/XSL/Transform.xslt**  
 This file contains the XSL definition of how to transform the data into an HTML table.  
  
## Demonstrates  
  
### Creating Web Resources in the Context of a Solution  

Web Resources are organization-owned records so they can be created using either the<xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*> method or by using the <xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> message and the <xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute*> method. This sample will show how to use the `SolutionUniqueName` optional parameter to associate a Web resource with a specific solution when it is created. This requires using the <xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> message.  
  
### Uploading Files from Disk  
 The WebResource.Content property requires a Base 64 string representing the binary contents of the file. The following sample is the method used to convert the file into the required type.  
  
```C#
//Encodes the Web Resource File
static public string getEncodedFileContents(String pathToFile)
{
    FileStream fs = new FileStream(pathToFile, FileMode.Open, FileAccess.Read);
    byte[] binaryData = new byte[fs.Length];
    long bytesRead = fs.Read(binaryData, 0, (int)fs.Length);
    fs.Close();
    return System.Convert.ToBase64String(binaryData, 0, binaryData.Length);
}
```
  
### Combining Web Resource Record Data with File Data  
 The ImportJob.xml file demonstrates how the data about the files being imported and the data about the Web Resource to create are combined. In particular, in order for relative links between related files to continue to function, the name of the Web resources you create must preserve information about the relative position of the files on disk using simulated directories in the file name. Because of the data in the ImportJob.xml file all these related Web resource files will be created under a common virtual folder.  
  
> [!NOTE]
>  It is not necessary to publish Web resources when they are created. It is necessary to publish them when they are updated.  
  
## Example  
 The following portion of the ImportWebResources.cs file expects the following variables:  
  
- `_customizationPrefix` : The customization prefix of the **SDK Samples** publisher. If this publisher does not exist it will be created with the customization prefix of “sample”.  
  
- `_ImportWebResourcesSolutionUniqueName` : The unique name of the **Import Web Resources Sample Solution** created in this sample. The value is `ImportWebResourcesSample`.  
  
```C#
//Read the descriptive data from the XML file
XDocument xmlDoc = XDocument.Load("../../ImportJob.xml");

//Create a collection of anonymous type references to each of the Web Resources
var webResources = from webResource in xmlDoc.Descendants("webResource")
                   select new
                   {
                       path = webResource.Element("path").Value,
                       displayName = webResource.Element("displayName").Value,
                       description = webResource.Element("description").Value,
                       name = webResource.Element("name").Value,
                       type = webResource.Element("type").Value
                   };

// Loop through the collection creating Web Resources
int counter = 0;
foreach (var webResource in webResources)
{
    //Set the Web Resource properties
    WebResource wr = new WebResource
    {
        Content = getEncodedFileContents(@"../../" + webResource.path),
        DisplayName = webResource.displayName,
        Description = webResource.description,
        Name = _customizationPrefix + webResource.name,
        LogicalName = WebResource.EntityLogicalName,
        WebResourceType = new OptionSetValue(Int32.Parse(webResource.type))
    };

    // Using CreateRequest because we want to add an optional parameter
    CreateRequest cr = new CreateRequest
    {
        Target = wr
    };
    //Set the SolutionUniqueName optional parameter so the Web Resources will be
    // created in the context of a specific solution.
    cr.Parameters.Add("SolutionUniqueName", _ImportWebResourcesSolutionUniqueName);

    CreateResponse cresp = (CreateResponse)_serviceProxy.Execute(cr);
    // Capture the id values for the Web Resources so the sample can delete them.
    _webResourceIds[counter] = cresp.id;
    counter++;
    Console.WriteLine("Created Web Resource: {0}", webResource.displayName);
}
```
  
  It is not necessary to publish Web resources when they are created. It is necessary to publish them when they are updated.  
  
### See also  
 [Web resource table reference](../data-platform/reference/entities/webresource.md)<br/>
 [Web resources](web-resources.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]