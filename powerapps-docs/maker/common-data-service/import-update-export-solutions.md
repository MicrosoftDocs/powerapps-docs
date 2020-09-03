---
title: "Import solutions | MicrosoftDocs"
description: "Learn how to import a solution in Power Apps"
ms.custom: ""
ms.date: 08/06/2020
ms.reviewer: ""
ms.service: powerapps
ms.topic: "article"
author: "Mattp123"
ms.assetid: 56363ea3-ea76-4311-9b7a-b71675e446fb
caps.latest.revision: 57
ms.author: "matp"
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---
# Import solutions 

You can manually import solutions using the steps in this article. You must import only those solutions that you've obtained from a trusted source. Customizations might include code that can send data to external sources.   
 
> [!NOTE]
> - To import a solution that includes a plug-in assembly, the **Create** privilege on the **Plug-In Assembly** entity is required. By default, the System Administrator security role has this privilege, but the System Customizer security role doesn’t. 
> - When you import a managed solution, all component changes will be brought into the environment in a published state. However, when you import an unmanaged solution, the changes are imported in a draft state so you must publish them to make them active. 
> - To implement healthy application lifecycle management (ALM) in your organization, consider using a source control system to store and collaborate on your solutions, and automate the solution import process. More information: [ALM basics](/power-platform/alm/basics-alm) in the Power Platform ALM guide.

When you import an **unmanaged** solution:
- You add all the components of that solution into your environment and can't delete the components by deleting the solution. Deleting the unmanaged solution deletes only the solution container.
- That contains components you have already customized, your customizations will be overwritten by the customizations in the imported unmanaged solution. You can’t undo this.

To import a solution:

1.  Sign into [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) and select **Solutions** from the left navigation.  
  
2.  On the command bar, select **Import**.  

    > [!div class="mx-imgBorder"]  
    > ![Import solution](media/solution-import.png "Import solution") 
  
3.  On the **Select Solution Package** page, select **Browse** to locate the compressed (.zip or .cab) file that contains the solution you want to import. 
  
4.  Select **Next**.  
  
5.  Information about the solution is displayed. Select **Import**.  
  
6. You may need to wait a few moments while the import completes. View the results and then select **Close**.  
  
 If you have imported any changes that require publishing, you must publish customizations before they are available. 
  
 If the import isn’t successful, you will see a report showing any errors or warnings that were captured. Select **Download Log File** to capture details about what caused the import to fail. The most common cause for an import to fail is that the solution did not contain some required components.  
  
 When you download the log file, you will find an XML file that you can open using Office Excel to view the contents.  
  
> [!NOTE]
> You can’t edit an active routing rule set. Therefore, if you’re importing a solution that includes an active routing rule set into an environment where the rule already exists with the same ID, the import will fail. More information: [Create rules to automatically route cases](https://docs.microsoft.com/dynamics365/customer-engagement/customer-service/create-rules-automatically-route-cases)  
  
## Troubleshooting solution import

### There's an active unmanaged layer created after importing a managed solution

During solution import the system must ensure that there is a fallback form for an entity. This requirement is enforced on the customization settings when you create entities or forms. But, if for some reason, an import is causing a scenario where there's no fallback form for an entity, then the import will create an active unmanaged layer for one of the main forms and the unmanaged customization will configure the form as the fallback. This makes sure that users who don't have access to any of the forms for an entity can view the fallback form. More information: [Set the fallback form for an entity](../model-driven-apps/control-access-forms.md#set-the-fallback-form-for-an-entity)

### Form doesn't appear in target environment after importing unmanaged solution

During export of unmanaged solutions some forms which are not modified get exported with the attribute `unmodified=1` for the form XML in the customizations.xml file located in the solution package. This ensures that, while these forms are part of the solution exported, when the same solution is imported in a new environment these forms are skipped during the import. To avoid this scenario the form needs to have active customizations for it to be exported without the unmodified=1 attribute. You can determine whether the form XML has the unmodified=1 attribute by extracting the exported solution. Then, search customizations.xml for the form  and check for the unmodified attribute.

### *Microsoft.Crm.CrmInvalidOperationException: full formXml is expected to create a form <formid>* message during solution import

This error can occur when the form you are importing doesn't exist in the target environment and the form that you're trying to import doesn't have the full component and metadata. Subsequently, the form XML only contains the changes when the full form XML is required. For example, this error can occur when you add a custom entity to a solution and don't select the **Include all components** option before export (also known as a segmented solution). To verify if the solution is segmented, open the customizations.xml file in the solution and search for the form id displayed in the error message. If the form XML contains an attribute named `solutionaction` the form XML doesn't include all components but only has changes to the form. To resolve this issue, include all components when you add the entity to your solution. More information: [Use segmented solutions](/power-platform/alm/segmented-solutions-alm)

### *Microsoft.Crm.CrmException: You cannot delete this form because it is the only fallback form of type main for the 'Entity' entity. Each entity must have at least one fallback form for each form type* message during solution upgrade or uninstall

The underlying cause of this error is due to trying to delete the last remaining form for an entity during a solution upgrade or uninstall. This behavior is by design. Each entity must be able to display a form for any user, at least one form must be designated as a fallback form. A fallback form is visible to users whose security roles do not have any forms explicitly assigned to them. The solution uninstall or upgrade may  be causing the removal of the fallback form. To workaround this issue, create a temporary form configured as the fallback form for the entity, and then try the upgrade or uninstall again. More information: [Set the fallback form for an entity](../model-driven-apps/control-access-forms.md#set-the-fallback-form-for-an-entity)

### See also

[Update solutions](update-solutions.md) <br />
[Export solutions](export-solutions.md) <br />
[Publish changes](create-solution.md#publish-changes) <br />
[For developers: Create, export, or import an unmanaged solution](/power-platform/alm/solution-api#create-export-or-import-an-unmanaged-solution)
