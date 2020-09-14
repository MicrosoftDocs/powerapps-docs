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

During solution import the system must ensure that there is a fallback form for an entity. This requirement is enforced when you create entities or forms. If during import there isn't a fallback form specified for an entity, then the import creates an unmanaged active layer for one of the main forms and the unmanaged customization indicates the form as the fallback form. This ensures that users can view a form when they don’t have access to any of the other entity forms. More information: [Set the fallback form for an entity](../model-driven-apps/control-access-forms.md#set-the-fallback-form-for-an-entity)

### The form doesn't appear in target environment after importing the unmanaged solution

During export of unmanaged solutions, some forms that aren't modified get exported with the attribute `unmodified=1` in the form XML of the customizations.xml file located in the solution package. This attribute is located in the FormXml node in the customization.xml file within the solution package. This attribute ensures that, even though these forms are part of the solution being exported, when the same solution is imported in a new environment the form will be omitted from the import. To avoid this scenario, the form must have active customizations for it to be exported without the unmodified=1 attribute. To verify this, extract the exported solution package and search the customizations.xml file for the FormXml node in question and verify the unmodified attribute.

### *Microsoft.Crm.CrmInvalidOperationException: full formXml is expected to create a form <formid>* message during solution import

This error can occur when the form you are importing doesn’t exist in the target environment and the form is imported for the first time. The solution you are importing has only form changes (diff) in the form XML when it should have the full form XML. A solution should only import a diff form XML when the form is already present in the environment and you’re importing the changes.  To verify, open your solution’s customizations.xml file and search for the FormXml node using the form id that appears in the error message. If the form XML contains an attribute named `solutionaction`, then the form XML is a diff. To resolve this scenario the form XML must be a full form XML (should not contain the solutionaction attribute) and can be obtained from the instance this form was originally created in as unmanaged.

### *Microsoft.Crm.CrmException: You cannot delete this form because it is the only fallback form of type main for the 'Entity' entity. Each entity must have at least one fallback form for each form type* message during solution upgrade or uninstall

This error occurs when a solution upgrade or uninstall attempts to delete the last remaining form for an entity. This behavior is by design. Each entity must be able to display a form for any valid user. Therefore, at least one form must be designated as a fallback form. A fallback form is available to users whose security roles do not have any forms explicitly assigned to them. To workaround this issue, create a temporary form configured as the fallback form for the entity, and then try the upgrade or uninstall again. More information: [Set the fallback form for an entity](../model-driven-apps/control-access-forms.md#set-the-fallback-form-for-an-entity)

### *Solution cannot be deleted due to dependencies from other components in the system* message when uninstalling a solution

This issue can occur when the solution contains components that are referenced by other solutions on top of it in the layer stack. To resolve this issue, either delete the component or remove the dependency from the solution you’re trying to uninstall. More information: [Removing dependencies](/power-platform/alm/removing-dependencies)

### See also

[Update solutions](update-solutions.md) <br />
[Export solutions](export-solutions.md) <br />
[Publish changes](create-solution.md#publish-changes) <br />
[For developers: Create, export, or import an unmanaged solution](/power-platform/alm/solution-api#create-export-or-import-an-unmanaged-solution)
