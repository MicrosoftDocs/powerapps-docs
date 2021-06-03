---
title: "Export ribbon definitions (model-driven apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn about exporting the ribbon definitions." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 04/14/2021
ms.reviewer: ""
ms.service: powerapps
ms.topic: "article"
author: "nkrb" # GitHub ID
ms.author: "nabuthuk" # MSFT alias of Microsoft employees only
manager: "kvivek" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Export ribbon definitions

To effectively define changes to the default RibbonXml, you must be able to reference the RibbonXml data that defines those ribbons.  
  
## Access the ribbon definitions for your organization  

If the Ribbon for your organization has been modified, you should export the current definitions if you intend to work with the customized ribbon elements. To do this, use the [Export ribbon xml](https://github.com/microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23/ExportRibbonDefinitions) sample.  

[!INCLUDE[cc-terminology](../data-platform/includes/cc-terminology.md)]
  
## Access the default ribbon data  

 The default ribbon definitions for model-driven apps can be downloaded from [Microsoft Downloads: ExportedRibbonXml.zip](https://download.microsoft.com/download/C/2/A/C2A79C47-DD2D-4938-A595-092CAFF32D6B/ExportedRibbonXml.zip). 
  
 The applicationRibbon.xml file contains the definition of the core application ribbons.  
  
 The remaining files contain the definitions used by tables that have ribbon definitions that differ from the table template. Each file is named according to the name of the table: logical table name + Ribbon.xml.  
  
 These files represent the output of two messages using the [Sample: Export ribbon definitions](sample-export-ribbon-definitions.md):  
  
 <xref:Microsoft.Crm.Sdk.Messages.RetrieveApplicationRibbonRequest>  
 This message retrieves the core application ribbons including the table template.  
  
 <xref:Microsoft.Crm.Sdk.Messages.RetrieveEntityRibbonRequest>  
 This message retrieves the ribbon definition used for a specific table.  
  
### Decompress the ribbon data  

 The ribbon data is exported as a compressed file. To decompress the file into XML, you have to use the [System.IO.Packaging.ZipPackage](/dotnet/api/system.io.packaging.zippackage) class. The following example is a helper method used in the SDK sample to decompress the file.  

 ``` C# 
/// <summary>
/// A helper method that decompresses the Ribbon data returned
/// </summary>
/// <param name="data">The compressed ribbon data</param>
/// <returns></returns>
public byte[] unzipRibbon(byte[] data)
{
 System.IO.Packaging.ZipPackage package = null;
 MemoryStream memStream = null;

 memStream = new MemoryStream();
 memStream.Write(data, 0, data.Length);
 package = (ZipPackage)ZipPackage.Open(memStream, FileMode.Open);

 ZipPackagePart part = (ZipPackagePart)package.GetPart(new Uri("/RibbonXml.xml", UriKind.Relative));
 using (Stream strm = part.GetStream())
 {
  long len = strm.Length;
  byte[] buff = new byte[len];
  strm.Read(buff, 0, (int)len);
  return buff;
 }
}

```

### Retrieve the application ribbon data  

 The application ribbon can be retrieved using the <xref:Microsoft.Crm.Sdk.Messages.RetrieveApplicationRibbonRequest> as shown in the following sample.  

 ```C# 
 //Retrieve the Application Ribbon
var appribReq = new RetrieveApplicationRibbonRequest();
var appribResp = (RetrieveApplicationRibbonResponse)service.Execute(appribReq);

System.String applicationRibbonPath = Path.GetFullPath(exportFolder + "\\applicationRibbon.xml");
File.WriteAllBytes(applicationRibbonPath, unzipRibbon(appribResp.CompressedApplicationRibbonXml)); 
```
  
### Retrieve table ribbons  

 To retrieve the ribbon definition for tables, you can just include the name of the table as a parameter to the <xref:Microsoft.Crm.Sdk.Messages.RetrieveEntityRibbonRequest>.  
  
 To retrieve the ribbon definitions for all tables that support the ribbon, you need a list of those system tables that have ribbon definitions that vary from the table ribbon template. The following sample shows an array of all the system tables that have ribbon definitions.  

 ```C# 
 //This array contains all of the system tables that use the ribbon.
public System.String[] entitiesWithRibbons = {"account",
"activitymimeattachment",
"activitypointer",
"appointment",
"bulkoperation",
"calendar",
"campaign",
"campaignactivity",
"campaignresponse",
"competitor",
"connection",
"contact",
"contract",
"contractdetail",
"convertrule",
"convertruleitem",
"customeraddress",
"discount",
"discounttype",
"email",
"emailserverprofile",
"entitlement",
"entitlementchannel",
"entitlementtemplate",
"entitlementtemplatechannel",
"fax",
"goal",
"goalrollupquery",
"importfile",
"incident",
"invoice",
"invoicedetail",
"kbarticle",
"kbarticlecomment",
"lead",
"letter",
"list",
"listmember",
"mailbox",
"metric",
"opportunity",
"opportunityproduct",
"partnerapplication",
"phonecall",
"postfollow",
"pricelevel",
"product",
"productpricelevel",
"queue",
"queueitem",
"quote",
"quotedetail",
"recurringappointmentmaster",
"report",
"rollupfield",
"routingrule",
"routingruleitem",
"salesliterature",
"salesliteratureitem",
"salesorder",
"salesorderdetail",
"service",
"serviceappointment",
"sharepointdocument",
"sharepointdocumentlocation",
"sharepointsite",
"site",
"sla",
"slaitem",
"socialactivity",
"socialprofile",
"systemuser",
"task",
"team",
"teamtemplate",
"territory",
"uom",
"uomschedule",
"userquery"};
 ```
  
The following sample shows how to retrieve the ribbon definitions for a set of tables. 

```csharp
//Retrieve system table Ribbons
var entRibReq = new RetrieveEntityRibbonRequest() { RibbonLocationFilter = RibbonLocationFilters.All };
foreach (System.String entityName in entitiesWithRibbons)
{
 entRibReq.EntityName = entityName;
 var entRibResp = (RetrieveEntityRibbonResponse)service.Execute(entRibReq);

 System.String entityRibbonPath = Path.GetFullPath(exportFolder + "\\" + entityName + "Ribbon.xml");
 File.WriteAllBytes(entityRibbonPath, unzipRibbon(entRibResp.CompressedEntityXml));
 //Write the path where the file has been saved.
 Console.WriteLine(entityRibbonPath);
} 
``` 

Any custom tables also support ribbon customizations. To get a list of custom tables, use the <xref:Microsoft.Xrm.Sdk.Messages.RetrieveAllEntitiesRequest> and retrieve the names of custom tables. The following sample shows how to retrieve ribbon definitions for all custom tables.  

```csharp 
//Check for custom tables
 var raer = new RetrieveAllEntitiesRequest() { EntityFilters = EntityFilters.Entity };
 var resp = (RetrieveAllEntitiesResponse)service.Execute(raer);
 foreach (EntityMetadata em in resp.EntityMetadata)
 {
  if (em.IsCustomEntity == true && em.IsIntersect == false)
  {
   entRibReq.EntityName = em.LogicalName;
   var entRibResp = (RetrieveEntityRibbonResponse)service.Execute(entRibReq);
   System.String entityRibbonPath = Path.GetFullPath(exportFolder + "\\" + em.LogicalName + "Ribbon.xml");
   File.WriteAllBytes(entityRibbonPath, unzipRibbon(entRibResp.CompressedEntityXml));
   //Write the path where the file has been saved.
   Console.WriteLine(entityRibbonPath);
  }
 } 
``` 

## Troubleshoot ribbon issues

If you are experiencing an issue with a ribbon command bar button, use this [troubleshooting guide](/troubleshoot/power-platform/power-apps/ribbon-issues-button-hidden?tabs=delete) to find and solve the problem.

### See also  
 [Customize the ribbon](customize-commands-ribbon.md)   
 [Command bar or ribbon presentation](command-bar-ribbon-presentation.md)   
 [Export, prepare to edit, and import the ribbon](export-prepare-edit-import-ribbon.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]