---
title: "Source control with solution files (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "The SolutionPackager tool can be used with any source control system. After a solution .zip file has been extracted to a folder, simply add and submit the files to your source control system. These files can then be synchronized on another computer where they can be packed into a new identical solution .zip file." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "shmcarth" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Source control with solution files

The SolutionPackager tool can be used with any source control system. After a solution .zip file has been extracted to a folder, simply add and submit the files to your source control system. These files can then be synchronized on another computer where they can be packed into a new identical solution .zip file.  
  
 An important aspect when using extracted component files in source control is that adding all the files into source control may cause unnecessary duplication. See the [Solution Component File Reference](solution-component-file-reference-solutionpackager.md) to see which files are generated for each component type and which files are recommended for use in source control.  
  
 As further customizations and changes are necessary for the solution, developers should edit or customize components through existing means, export again to create a .zip file, and extract the compressed solution file into the same folder.  
  
> [!IMPORTANT]
>  Except for the sections described in [When to edit the customizations file](/model-driven-apps/when-edit-customization-file.md), manual editing of extracted component files and .zip files is not supported.  
  
 When the SolutionPackager tool extracts the component files it will not overwrite existing component files of the same name if the file contents are identical. In addition, the tool honors the read-only attribute on component files producing a warning in the console window that particular files were not written. This enables the user to check out, from source control, the minimal set of files that are changing. The `/clobber` parameter can be used to override and cause read-only files to be written or deleted. The `/allowWrite` parameter can be used to assess what impact an extract operation has without actually causing any files to be written or deleted. Use of the `/allowWrite` parameter with verbose logging is effective.  
  
 After the extract operation is completed with the minimal set of files checked out from source control, a developer may submit the changed files back into source control, as is done with any other type of source file.  
  
<a name="team_dev"></a>   
## Team development  
 When there are multiple developers working on the same solution component a conflict might arise where changes from two developers result in changes to a single file. This occurrence is minimized by decomposing each individually editable component or subcomponent into a distinct file. Consider the following example.  
  
1. Developer A and B are both working on the same solution.  
  
2. On independent computers, they both get the latest sources of the solution from source control, pack, and import an unmanaged solution .zip file into independent CDS for Apps organizations.  
  
3. Developer A customizes the “Active Contacts” system view and the main form for the Contact entity.  
  
4. Developer B customizes the main form for the Account entity and changes the “Contact Lookup View”.  
  
5. Both developers export an unmanaged solution .zip file and extract.  
  
   1.  Developer A will need to check out one file for the Contact main form, and one file for the “Active Contacts” view.  
  
   2.  Developer B will need to check out one file for the Account main form, and one file for the “Contact Lookup View”.  
  
6. Both developers may submit, in any order, as their respective changes touched separate files.  
  
7. After both submissions are complete, they can repeat step #2 and then continue to make further changes in their independent organizations. They each have both sets of changes, with no overwrites of their own work.  
  
   The previous example works only when there are changes to separate files. It is inevitable that independent customizations require changes within a single file. Based on the example shown above, consider that developer B customized the “Active Contacts” view while developer A was also customizing it. In this new example, the order of events becomes important. The correct process to reconcile this predicament, written out in full, is as follows.  
  
8. Developer A and B are both working on the same solution.  
  
9. On independent computers, they both get the latest sources of the solution from source control, pack, and import an unmanaged solution .zip file into independent organizations.  
  
10. Developer A customizes the “Active Contacts” system view and the main form for the Contact entity.  
  
11. Developer B customizes the main form for the Account entity and changes the “Active Contacts”.  
  
12. Both developers export an unmanaged solution . zip file and extract.  
  
    1.  Developer A will need to check out one file for the Contact main form, and one file for the “Active Contacts” view.  
  
    2.  Developer B will need to check out one file for the Account main form, and one file for the “Active Contacts” view.  
  
13. Developer A is ready first.  
  
    1.  Before he submits to source control he must get latest sources to ensure no prior check-ins conflict with his changes.  
  
    2.  There are no conflicts so he is able to submit.  
  
14. Developer B is ready next following developer A.  
  
    1.  Before he submits he must get the latest sources to ensure no prior check-ins conflict with his changes.  
  
    2.  There is a conflict because the file for “Active Contacts” has been modified since he last retrieved the latest sources.  
  
    3.  Developer B must reconcile the conflict. It is possible the capabilities of the source control system in use may aide this process; otherwise the following choices are all viable.  
  
        1.  Developer B, through source control history, if available, can see that the developer A made the prior change. Through direct communication they can discuss each change. Then developer B only has to update his organization with the agreed resolution. He then exports, extracts, and overwrites the conflicting file and submits.  
  
        2.  Allow source control to overwrite his local file. Developer B packs the solution and imports it into his organization, then assesses the state of the view and re-customizes it as necessary. Next, he may export, extract, and overwrite the conflicting file.  
  
        3.  If the prior change can be deemed unnecessary, developer B allows his copy of the file to overwrite the version in source control and submits.  
  
    Whether working on a shared organization or independent organizations, team development of CDS for Apps solutions requires those actively working on a common solution to be aware of the work of others. The SolutionPackager tool does not fully remove this need but it does enable easy merging of non-conflicting changes at the source control level, and it proactively highlights the concise components where conflicts have arisen.  
  
    The next sections are the generic processes to effectively use the SolutionPackager tool in source control when developing with teams. These work equally with independent organizations or shared development organizations, though with shared organizations the export and extract will naturally include all changes present within the solution, not just those made by the developer performing the export. Similarly, when importing a solution .zip file the natural behavior to overwrite all components will occur.  
  
<a name="create_sol"></a>   
## Create a solution  
 The following procedure identifies the typical steps used when first creating a solution.  
  
1. In a clean organization, create a solution on CDS for Apps server, and then add or create components as necessary.  
  
2. When you are ready to check in, do the following.  
  
   1.  Export the unmanaged solution.  
  
   2.  Using the SolutionPackager tool, extract the solution into component files.  
  
   3.  From those extracted component files, add the necessary files to source control.  
  
   4.  Submit these changes to source control.  
  
<a name="modify_sol"></a>   
## Modify a solution  
 The following procedure identifies the typical steps used when modifying an existing solution.  
  
1. Synchronize or get the latest solution component file sources.  
  
2. Using the SolutionPackager tool, pack component files into an unmanaged solution .zip file.  
  
3. Import the unmanaged solution file into an organization.  
  
4. Customize and edit the solution as necessary.  
  
5. When you are ready to check the changes into source control, do the following.  
  
   1.  Export the unmanaged solution.  
  
   2.  Using the SolutionPackager tool, extract the exported solution into component files.  
  
   3.  Synchronize or get the latest sources from source control.  
  
   4.  Reconcile if any conflicts exist.  
  
   5.  Submit the changes to source control.  
  
   Steps 2 and 3 must be done before further customizations occur in the development organization. Within step 5, step b must be completed before step c.  
  
### See also  
 [Solution Tools for Team Development](solution-tools-team-development.md)   
 [Solution Component File Reference (SolutionPackager)](solution-component-file-reference-solutionpackager.md)   
 [Use the SolutionPackager Tool to Compress and Extract a Solution File](compress-extract-solution-file-solutionpackager.md)