---
title: "Uninstall or delete a solution (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This doc describes how uninstall and delete actions work for managed and unmanaged solution in Dynamics 365" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "shmcarth" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Uninstall or delete a solution

You delete managed and unmanaged solutions in the same way, but the resulting actions are very different. Deleting a managed solution will uninstall the managed solution.  
  
<a name="BKMK_DeleteSolution"></a>   
## Delete a solution  
 Depending on the type of solution that you want to delete, you’ll see one of the following **Confirm Deletion** messages:  
  
 **Managed solution**  
 “You are deleting a managed solution. The solution and all its components will be deleted. This action cannot be undone. This solution might take several minutes to uninstall. You cannot cancel the uninstallation after it starts. Do you want to continue?”  
  
 **Unmanaged solution**  
 “You are deleting an unmanaged solution. The solution will be deleted but components that are contained in this solution will not be deleted. This action cannot be undone. Do you want to continue?”  
  
 To delete a solution programmatically use the <xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*> method. More information: [Delete a Solution](work-solutions.md#BKMK_DeleteSolution)  
  
<a name="BKMK_UinstallAManagedSolution"></a>   
### Uninstall a managed solution  
 Deleting a managed solution will uninstall the solution. All the solution components defined in it are deleted.  
  
> [!IMPORTANT]
>  When you uninstall a managed solution, the following data is lost: data stored in custom entities that are part of the solution and data stored in custom attributes on system entities that are part of the solution.  
  
<a name="BKMK_DeleteUnmanagedSolution"></a>   
### Delete an unmanaged solution  
 An unmanaged solution is a group of solution components. Deleting the solution deletes a single solution record in the database. Solution components are not affected by the solution being deleted, they remain in the system.  
  
<a name="BKMK_AccessSolutionsGridWithUrl"></a>   
## Access the solutions list with a URL  
 If you need to navigate directly to the solutions list you can use the following URL:  
  
```
<organization root url>/tools/Solution/home_solution.aspx?etn=solution  
```  
  
### See also  
 [Package and Distribute Extensions](/dynamics365/customer-engagement/developer/package-distribute-extensions-use-solutions)   
 [Delete a Solution](work-solutions.md#BKMK_DeleteSolution)   
 [Introduction to Solutions](introduction-solutions.md)   
 [Planning for Solution Development](/dynamics365/customer-engagement/developer/plan-solution-development)   
 [Solution Components and Dependency Tracking](dependency-tracking-solution-components.md)   
 [Create a Managed Solution](create-install-update-managed-solution.md#BKMK_CreateManagedSolution)   
 [Export an unmanaged solution](create-export-import-unmanaged-solution.md#BKMK_UnmanagedSolution)   
 [Import an unmanaged solution](create-export-import-unmanaged-solution.md#BKMK_ImportUnmanagedSolution)   
 [Create a Managed Solution](create-install-update-managed-solution.md#BKMK_CreateManagedSolution)   
 [Create Solutions that Support Multiple Languages](create-solutions-support-multiple-languages.md)   
 [Install a Managed Solution](create-install-update-managed-solution.md#BKMK_InstallManagedSolution)
