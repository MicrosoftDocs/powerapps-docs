---
title: "Use editable grids in model-driven apps | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Editable grid is a new custom control in Dynamics 365 Customer Engagement that provides rich inline editing capabilities on web and mobile clients (Dynamics 365 for phones and Dynamics 365 for tablets) including the ability to group, sort, and filter data within the same grid so that you do not have to switch records or views." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "JimDaly" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "shilpas" # MSFT alias of manager or PM counterpart
---
# Use editable grids

<!-- https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/customize-dev/use-editable-grids-dynamics-365 -->

Editable grid is a custom control that provides rich inline editing capabilities on web and mobile clients (Dynamics 365 for phones and Dynamics 365 for tablets) including the ability to group, sort, and filter data within the same grid so that you do not have to switch records or views. The editable grid control is supported in the main grid and subgrids on a form in the web client and in dashboards and on form grids on the mobile clients. Although the editable grid control provides editing capability, it honors the read-only grid metadata and field-level security settings. Editable grids also support business rules and form scripting so you can apply custom business logic according to your organization's requirements.  

> [!NOTE] 
> If you are using legacy forms (versions prior to Dynamics CRM 2016) and enable an editable grid on a subgrid, the editable subgrid will not be rendered. System administrators can turn off legacy forms in system settings, if needed. 

<a name="Enable"></a>   
## Enable editable grids  
 You can enable editable grids at the entity level to use in the main grid, or at the form level to replace read-only subgrids (associated grids) with an editable grid.  
  
 You can enable the editable grid control for an entity using the customization tool in Model-driven Apps (**Settings** > **Customizations**  > **Customize the System** > **Entities** > *[Entity_Name]* > **Controls** tab.  
  
 To enable editable grid for a grid in a form, open the form editor, double-click the read-only grid that you want to replace with the editable grid, and then add/enable editable grid in the **Controls** tab.  
  
 You can revert to the non-editable grid at any time for main grid and associated grids, if required. Also, at runtime, users can toggle between editable grids and read-only grids.  
  
 More information: [Make Model-driven Apps grids (lists) editable using the Editable Grid custom control](../../maker/model-driven-apps/make-grids-lists-editable-custom-control.md)  
  
<a name="FormScripting"></a>   
## Form scripting support  
 The editable grids support client-side events and methods that can be used to write custom client extensions according to your business need. More information: [Grids and subgrids in Model-driven Apps (Client API reference)](clientapi/reference/grids.md)
  
<a name="EntitiesSupported"></a>   
## Entities and views supported by editable grid  
 Not all entities and views support the use of editable grid.  
  
 On the web client, an entity will support editable grid if all of the following conditions are true:  
  
- The entity is customizable (IsCustomizable = true)  
  
- The entity is either refreshed (IsAIRUpdated = true) or a custom entity (IsCustomEntity = true)  
  
- The entity is not a child entity (IsChildEntity = false)  
  
  On the mobile client, an entity will support editable grid if the entity can be displayed in the mobile client's site map.  
  
  For information about the entities that support editable grids, see **Supported out-of-the-box entities** section in [Make Model-driven Apps grids (lists) editable using the Editable Grid custom control](../../maker/model-driven-apps/make-grids-lists-editable-custom-control.md) 
   
  Editable grids do not support roll up associated views (**Rollup type** = `Related`).  
  
  Use the following sample code to generate an XML file that you can open in Excel as an XML table to view the entity-support information for editable controls. Excel will figure out the schema automatically, and display the information under the following columns:  
  
- `LogicalName`: Logical name of entity.  
  
- `DisplayName`: Display name of entity.  
  
- `CanEnableEditableGridWeb`: Displays status  (True or False) whether editable grid is supported for the entity  on the web client.  
  
- `CanEnableEditableGridMobile`: Displays status (True or False) whether editable grid is supported for the entity on mobile clients. (Dynamics 365 for phones and Dynamics 365 for tablets).  
  
```csharp  
using System;  
using System.Linq;  
using System.Xml.Linq;  
using System.ServiceModel;  
using System.ServiceModel.Description;  
using System.Collections.Generic;  
using System.Xml.Serialization;  
using System.Xml;  
using System.IO;  
  
// These namespaces are found in the Microsoft.Xrm.Sdk.dll assembly  
// found in the SDK\bin folder.  
using Microsoft.Xrm.Sdk;  
using Microsoft.Xrm.Sdk.Query;  
using Microsoft.Xrm.Sdk.Metadata;  
using Microsoft.Xrm.Sdk.Client;  
using Microsoft.Xrm.Sdk.Messages;  
  
// This namespace is found in Microsoft.Crm.Sdk.Proxy.dll assembly  
// found in the SDK\bin folder.  
using Microsoft.Crm.Sdk.Messages;  
  
namespace Microsoft.Crm.Sdk.Samples  
{  
    /// <summary>  
    /// This sample generates an XML table to display the entity-support information for   
    ///  editable controls.  
    /// </summary>  
    public class DumpEditableGridEntityInfo  
    {  
        #region Class Level Members  
  
        /// <summary>  
        /// Stores the organization service proxy.  
        /// </summary>  
        OrganizationServiceProxy _serviceProxy;  
  
        // Create storage for new attributes being created  
        public List<AttributeMetadata> addedAttributes;  
  
        // Specify which language code to use in the sample. If you are using a language  
        // other than US English, you will need to modify this value accordingly.  
        // See http://msdn.microsoft.com/en-us/library/0h88fahh.aspx  
        public const int _languageCode = 1033;  
  
        // Define the IDs/variables needed for this sample.  
        public int _insertedStatusValue;  
  
        #endregion Class Level Members  
  
        #region How To Sample Code  
        /// <summary>  
        /// </summary>  
        /// <param name="serverConfig">Contains server connection information.</param>  
        /// <param name="promptForDelete">When True, the user will be prompted to delete all  
        /// created entities.</param>  
        public void Run(ServerConnection.Configuration serverConfig, bool promptForDelete)  
        {  
            try  
            {  
  
                // Connect to the Organization service.   
                // The using statement assures that the service proxy will be properly disposed.  
                using (_serviceProxy = new OrganizationServiceProxy(serverConfig.OrganizationUri, serverConfig.HomeRealmUri, serverConfig.Credentials, serverConfig.DeviceCredentials))  
                {  
                    // This statement is required to enable early-bound type support.  
                    _serviceProxy.EnableProxyTypes();  
  
                    //<snippetDumpEditableGridEntityInfo1>  
                    RetrieveAllEntitiesRequest request = new RetrieveAllEntitiesRequest()  
                    {  
                        EntityFilters = EntityFilters.Entity,  
                        RetrieveAsIfPublished = true  
                    };  
  
                    // Retrieve the MetaData.  
                    RetrieveAllEntitiesResponse response = (RetrieveAllEntitiesResponse)_serviceProxy.Execute(request);  
  
                    // Create an instance of StreamWriter to write text to a file.  
                    // The using statement also closes the StreamWriter.  
                    // To view this file, right click the file and choose open with Excel.   
                    // Excel will figure out the schema and display the information in columns.  
  
                    String filename = String.Concat("EditableGridEntityInfo.xml");  
                    using (StreamWriter sw = new StreamWriter(filename))  
                    {  
                        // Create Xml Writer.  
                        XmlTextWriter metadataWriter = new XmlTextWriter(sw);  
  
                        // Start Xml File.  
                        metadataWriter.WriteStartDocument();  
  
                        // Metadata Xml Node.  
                        metadataWriter.WriteStartElement("Metadata");  
  
                        foreach (EntityMetadata currentEntity in response.EntityMetadata)  
                        {  
                            // Start Entity Node  
                            metadataWriter.WriteStartElement("Entity");  
  
                            bool canBeDisplayedInSitemap = currentEntity.IsCustomizable.Value;  
  
                            if (canBeDisplayedInSitemap)  
                            {  
                                metadataWriter.WriteElementString("LogicalName", currentEntity.LogicalName);  
                                metadataWriter.WriteElementString("DisplayName", currentEntity.DisplayName.UserLocalizedLabel?.Label);  
                                metadataWriter.WriteElementString("CanEnableEditableGridWeb", (!(bool)currentEntity.IsChildEntity && ((bool)currentEntity.IsAIRUpdated || (bool)currentEntity.IsCustomEntity)).ToString());  
                                metadataWriter.WriteElementString("CanEnableEditableGridMobile", (currentEntity.IsVisibleInMobileClient.Value || currentEntity.IsVisibleInMobileClient.CanBeChanged).ToString());  
                            }  
  
                            // Write the Entity's Information.  
  
                            //End Entity Node  
                            metadataWriter.WriteEndElement();  
                        }  
  
                        // End Metadata Xml Node  
                        metadataWriter.WriteEndElement();  
                        metadataWriter.WriteEndDocument();  
  
                        // Close xml writer.  
                        metadataWriter.Close();  
                        Console.WriteLine("Dumped information in the EditableGridEntityInfo.xml file");  
                    }  
                }  
            }  
  
            // Catch any service fault exceptions that Microsoft Dynamics CRM throws.  
            catch (FaultException<Microsoft.Xrm.Sdk.OrganizationServiceFault>)  
            {  
                // You can handle an exception here or pass it back to the calling method.  
                throw;  
            }  
        }  
        #endregion How To Sample Code  
  
        #region Main  
        /// <summary>  
        /// Standard Main() method used by most SDK samples.  
        /// </summary>  
        /// <param name="args"></param>  
        static public void Main(string[] args)  
        {  
            try  
            {  
                // Obtain the target organization's Web address and client logon   
                // credentials from the user.  
                ServerConnection serverConnect = new ServerConnection();  
                ServerConnection.Configuration config = serverConnect.GetServerConfiguration();  
                DumpEditableGridEntityInfo app = new DumpEditableGridEntityInfo();  
                app.Run(config, false);                  
            }  
            catch (FaultException<Microsoft.Xrm.Sdk.OrganizationServiceFault> ex)  
            {  
                Console.WriteLine("The application terminated with an error.");  
                Console.WriteLine("Timestamp: {0}", ex.Detail.Timestamp);  
                Console.WriteLine("Code: {0}", ex.Detail.ErrorCode);  
                Console.WriteLine("Message: {0}", ex.Detail.Message);  
                Console.WriteLine("Plugin Trace: {0}", ex.Detail.TraceText);  
                Console.WriteLine("Inner Fault: {0}",  
                    null == ex.Detail.InnerFault ? "No Inner Fault" : "Has Inner Fault");  
            }  
            catch (System.TimeoutException ex)  
            {  
                Console.WriteLine("The application terminated with an error.");  
                Console.WriteLine("Message: {0}", ex.Message);  
                Console.WriteLine("Stack Trace: {0}", ex.StackTrace);  
                Console.WriteLine("Inner Fault: {0}",  
                    null == ex.InnerException.Message ? "No Inner Fault" : ex.InnerException.Message);  
            }  
            catch (System.Exception ex)  
            {  
                Console.WriteLine("The application terminated with an error.");  
                Console.WriteLine(ex.Message);  
  
                // Display the details of the inner exception.  
                if (ex.InnerException != null)  
                {  
                    Console.WriteLine(ex.InnerException.Message);  
  
                    FaultException<Microsoft.Xrm.Sdk.OrganizationServiceFault> fe  
                        = ex.InnerException  
                        as FaultException<Microsoft.Xrm.Sdk.OrganizationServiceFault>;  
                    if (fe != null)  
                    {  
                        Console.WriteLine("Timestamp: {0}", fe.Detail.Timestamp);  
                        Console.WriteLine("Code: {0}", fe.Detail.ErrorCode);  
                        Console.WriteLine("Message: {0}", fe.Detail.Message);  
                        Console.WriteLine("Plugin Trace: {0}", fe.Detail.TraceText);  
                        Console.WriteLine("Inner Fault: {0}",  
                            null == fe.Detail.InnerFault ? "No Inner Fault" : "Has Inner Fault");  
                    }  
                }  
            }  
            // Additional exceptions to catch: SecurityTokenValidationException, ExpiredSecurityTokenException,  
            // SecurityAccessDeniedException, MessageSecurityException, and SecurityNegotiationException.  
  
            finally  
            {  
  
                Console.WriteLine("Press <Enter> to exit.");  
                Console.ReadLine();  
            }  
  
        }  
        #endregion Main  
  
    }  
}  
```  
  
### See also  
 [Grids and subgrids in Model-driven Apps (Client API reference)](clientapi/reference/grids.md)   
 [Make Model-driven Apps grids (lists) editable using the Editable Grid custom control](../../maker/model-driven-apps/make-grids-lists-editable-custom-control.md)
