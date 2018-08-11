---
title: "Create, install, and update a managed solution (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "<Description>" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "shmcarth" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Create, install, and update a managed solution

You create a managed solution by exporting an unmanaged solution as a managed solution. The organizations that use your managed solution will install it and any updates that you create for it.  
  
 More information: [Use solutions for your customizations](/dynamics365/customer-engagement/customize/use-solutions-for-your-customizations).  
  
<a name="BKMK_CreateManagedSolution"></a>   

## Create a managed solution  
 Before you can create a managed solution you must first create an unmanaged solution. For more information about how to create an unmanaged solution, see [Create an unmanaged solution](create-export-import-unmanaged-solution.md#BKMK_CreateUnmanagedSolution).  
  
 You create a managed solution by selecting the **Managed** option in the **Package Type** dialog box when exporting the solution.  
  
 A managed solution only includes any customizable solution components that have been customized. Not only does this prevent unintentionally changing existing solution components on the system where the solution is installed, it also keeps the size of the managed solution smaller.  
  
 Before the final step of creating a managed solution, you must decide whether there are any customization capabilities that you do not want to allow people who install your managed solution to perform. Each solution component contains a set of managed properties that control which customization capabilities you want to allow. The default settings allow all customization capabilities. More information: [Using Managed Properties](use-managed-properties.md)  
  
 You can create a managed solution programmatically by using the <xref:Microsoft.Crm.Sdk.Messages.ExportSolutionRequest> message. More information: [Export or Package a Solution](work-solutions.md#BKMK_ExportPackageSolution)  
  
> [!IMPORTANT]
>  You should not import a managed solution back into the organization you used to create it.  
  
<a name="BKMK_InstallManagedSolution"></a>   

## Install a managed solution  
 You install a managed solution in the same way you import an unmanaged solution. The difference is in how the solution has been packaged.  
  
> [!IMPORTANT]
>  Installing a solution or publishing customizations can interfere with normal system operation. We recommend that you schedule solution imports when it’s least disruptive to users.  
  
 If the solution did not import successfully, you can click **Download Log** in the dialog box to download a report that will provide information about errors that occurred that prevented successful import of the managed solution. This file is an XML document configured to be opened by using Ofice Excel.  
  
 You can import or update a managed solution programmatically by using the <xref:Microsoft.Crm.Sdk.Messages.ImportSolutionRequest> message. When using this message, you can request a reference to an `ImportJob`  entity record that will include details about the success of the import. More information: [Install or Upgrade a Solution](work-solutions.md#BKMK_InstallUpgradeSolution)  
  
 The <xref:Microsoft.Crm.Sdk.Messages.ImportSolutionRequest> can be called using the <xref:Microsoft.Xrm.Sdk.Messages.ExecuteAsyncRequest>. More information: [Execute messages in the background (asynchronously)](/dynamics365/customer-engagement/developer/org-service/use-messages-request-response-classes-execute-method#bkmk_executeasync)  
  
 There are limits to the size of a solution you can install. More information: [Maximum size of solution to import](create-export-import-unmanaged-solution.md#BKMK_MaxSizeOfSolution)  
  
<a name="BKMK_UpdateManagedSolution"></a>   

### Update a managed solution  
 When you install a managed solution that already exists in the organization, the import solution dialog will provide the following options:  
  
 **Maintain customizations (recommended)**  
 This option maintains any unmanaged customizations performed on components, but also implies that some of the updates included in this solution will not take effect.  
  
 **Overwrite customizations**  
 This option overwrites any unmanaged customizations previously performed on components included in this solution. All updates included in this solution will take effect.  
  
> [!NOTE]
>  You may want to direct people who install your managed solution to use the **Overwrite customizations** option when investigating issues where the customizations conflict with the behavior of your solutions. They should always export their unmanaged solutions first so that they can re-apply them if they need to.  
  
### See also  
 [Package and Distribute Extensions with Dynamics 365 Solutions](/dynamics365/customer-engagement/developer/package-distribute-extensions-use-solutions)   
 [Introduction to Solutions](introduction-solutions.md)   
 [Planning for Solution Development](/dynamics365/customer-engagement/developer/plan-solution-development)   
 [Solution Components and Dependency Tracking](dependency-tracking-solution-components.md)   
 [Create, Export, or Import an Unmanaged Solution](create-export-import-unmanaged-solution.md)   
 [Uninstall or Delete a solution](uninstall-delete-solution.md)   
 [Customization Solutions File Schema](/dynamics365/customer-engagement/developer/customize-dev/customization-solutions-file-schema)