---
title: "Import solutions | MicrosoftDocs"
description: "Learn how to import a solution in Power Apps"
ms.custom: ""
ms.date: 08/02/2021
ms.reviewer: ""
ms.service: powerapps
ms.topic: "article"
author: "Mattp123"
ms.assetid: 56363ea3-ea76-4311-9b7a-b71675e446fb
caps.latest.revision: 57
ms.subservice: dataverse-maker
ms.author: "matp"
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---
# Import solutions

[!INCLUDE[cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

You can manually import solutions using the steps in this article. You must import only those solutions that you've obtained from a trusted source.
 
> [!NOTE]
> - The create privilege is required to import a component. Although, the System Customer security role has create privilege on most components that are commonly imported, by default it doesn't have create privilege on the **Plug-In Assembly** table. The System Administrator security role has this privilege.
> - When you import a managed solution, all component changes will be brought into the environment in a published state. However, when you import an unmanaged solution, the changes are imported in a draft state so you must publish them to make them active. 
> - To implement healthy application lifecycle management (ALM) in your organization, consider using a source control system to store and collaborate on your solutions, and automate the solution import process. More information: [ALM basics](/power-platform/alm/basics-alm) in the Power Platform ALM guide.

When you import an **unmanaged** solution:
- You add all the components of that solution into your environment and can't delete the components by deleting the solution. Deleting the unmanaged solution deletes only the solution container.
- That contains components you have already customized, your customizations will be overwritten by the customizations in the imported unmanaged solution. You can’t undo this.

To import a solution:

1. Sign into [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) and select **Solutions** from the left navigation.  
  
1. On the command bar, select **Import**.  

    > [!div class="mx-imgBorder"]  
    > ![Import solution.](media/solution-import.png "Import solution") 
  
1. On the **Import a solution** page, select **Browse** to locate the compressed (.zip or .cab) file that contains the solution you want to import.

1. Select **Next**.  
  
1. Information about the solution is displayed. By default, in the **Advanced settings** section, if SDK messages and flows exist in the solution, they will be imported. Clear the **Enable SDK messages and flows included in the solution** option if you want them to import in an inactive state. 

1. If your solution contains [connection references](create-connection-reference.md), you’ll be prompted to select the connections you want. If a connection does not already exist, create a new one. Select **Next**.

1. If your solution contains [environment variables](EnvironmentVariables.md), you will be prompted to enter values. You will not see this screen if value(s) are already present in your solution or the target environment. 

1. If missing dependencies are detected in the target environment, a list of the dependencies is presented. In environments where the required package version is available for import in the target environment, a link to resolve the dependency is presented. Selecting the link takes you to the Power Platform admin center where you can install the application update. After the application update is completed, you can start the solution import again.

1. Select **Import**.

Your solution imports in the background and may take a few moments.  
  
 If you have imported any changes that require publishing, you must publish customizations before they are available.
  
 If the import isn’t successful, you will see a notification on the solutions page showing any errors or warnings that were captured. Select **Download Log File** to capture details about what caused the import to fail. The most common cause for an import to fail is that the solution did not contain some required components.  

When you download the log file, you will find an XML file that you can open using Office Excel to view the contents.

> [!NOTE]
> You can view the details of all solution operations including solution import with the [solution history](solution-history.md) feature. To view these operations, select **See history** on the solutions page.
  
## Troubleshooting solution import

### There's an active unmanaged layer created after importing a managed solution

During solution import the system must ensure that there is a fallback form for a table. This requirement is enforced when you create tables or forms. If during import there isn't a fallback form specified for a table, then the import creates an unmanaged active layer for one of the main forms and the unmanaged customization indicates the form as the fallback form. This ensures that users can view a form when they don’t have access to any of the other table forms. More information: [Set the fallback form for a table](../model-driven-apps/control-access-forms.md#set-the-fallback-form-for-a-table)

### The form doesn't appear in target environment after importing the unmanaged solution

During export of unmanaged solutions, some forms that aren't modified get exported with the attribute `unmodified=1` in the form XML of the customizations.xml file located in the solution package. This attribute is located in the FormXml node in the customization.xml file within the solution package. This attribute ensures that, even though these forms are part of the solution being exported, when the same solution is imported in a new environment the form will be omitted from the import. To avoid this scenario, the form must have active customizations for it to be exported without the unmodified=1 attribute. To verify this, extract the exported solution package and search the customizations.xml file for the FormXml node in question and verify the unmodified attribute.

### *Microsoft.Crm.CrmInvalidOperationException: full formXml is expected to create a form <formid>* message during solution import

This error can occur when the form you are importing doesn’t exist in the target environment and the form is imported for the first time. The solution you are importing has only form changes (diff) in the form XML when it should have the full form XML. A solution should only import a diff form XML when the form is already present in the environment and you’re importing the changes.  To verify, open your solution’s customizations.xml file and search for the FormXml node using the form ID that appears in the error message. If the form XML contains an attribute named `solutionaction`, then the form XML is a diff. To resolve this scenario the form XML must be a full form XML (should not contain the `solutionaction` attribute) and can be obtained from the instance this form was originally created in as unmanaged.

### *Microsoft.Crm.CrmException: You cannot delete this form because it is the only fallback form of type main for the 'table' table. Each table must have at least one fallback form for each form type* message during solution upgrade or uninstall

This error occurs when a solution upgrade or uninstall attempts to delete the last remaining form for a table. This behavior is by design. Each table must be able to display a form for any valid user. Therefore, at least one form must be designated as a fallback form. A fallback form is available to users whose security roles do not have any forms explicitly assigned to them. To work around this issue, create a temporary form configured as the fallback form for the table, and then try the upgrade or uninstall again. More information: [Set the fallback form for a table](../model-driven-apps/control-access-forms.md#set-the-fallback-form-for-a-table)

### *Solution cannot be deleted due to dependencies from other components in the system* message when uninstalling a solution

This issue can occur when the solution contains components that are referenced by other solutions on top of it in the layer stack. To resolve this issue, either delete the component or remove the dependency from the solution you’re trying to uninstall. More information: [Removing dependencies](/power-platform/alm/removing-dependencies)

### Newly added components don’t appear in the app after importing an update to the app 

A model-driven app change that uses **All** when selecting a component, such as a view, aren’t reflected after importing an update to the app in the target environment.  This can happen when the following are true:

1. You didn’t initially select **All** in the app designer but selected the components individually. For example, you select two views, and then export the app in a managed solution from your development environment and imported it to your test (target) environment.
2. Then you created another solution with the same app in the development environment. You selected **All** to select all views in the app designer. The solution is then exported as managed from your development environment and imported into your test (target) environment.

To work around this behavior, select each component individually, such as the newly added views described in step 2, rather than select All.

### See also

[Update solutions](update-solutions.md) <br />
[Export solutions](export-solutions.md) <br />
[Publish changes](create-solution.md#publish-changes) <br />
[For developers: Create, export, or import an unmanaged solution](/power-platform/alm/solution-api#create-export-or-import-an-unmanaged-solution)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]