---
title: "Control access to model-driven app forms in PowerApps | MicrosoftDocs"
description: "Learn how to control acces to main forms"
ms.custom: ""
ms.date: 06/27/2018
ms.reviewer: ""
ms.service: "crm-online"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "powerapps"
author: "Mattp123"
ms.assetid: 15d123e0-b604-45dd-ab34-0b37787a04bb
caps.latest.revision: 33
ms.author: "matp"
manager: "kvivek"
tags: 
---
# Control access to model-driven app forms

 There are two ways you can control access to main forms:  
  
- **Make a main form inactive**  
  
     You can set an active or inactive state to main forms. This feature was included primarily to manage new forms included when Dynamics 365 customer engagement organizations upgrade but you can use it to prevent users from being able to use any main form.   
  
- **Assign security roles to the main form**  
  
     Use this to make a main form available to specific groups.  
  
 Different people in your organization may interact with the same data in different ways. Managers may depend on being able to quickly scan information in a record and service people may require a form that streamlines data entry. You can accommodate different requirements by assigning forms to the security roles that different groups of people belong to.  
  
 For step-by-step procedures, see [Assign security roles to forms](https://docs.microsoft.com/dynamics365/customer-engagement/admin/assign-security-roles-form).  
  
 When you have more than one main or mobile form defined for an entity, you can select which forms users will be able to use based on their security roles. Because each entity must be able to display a form for any user, at least one form must be designated as a ”fallback” form – a form visible to users whose security roles do not have any forms explicitly assigned to them.  
  
> [!NOTE]
>  Quick Create and Quick View forms cannot be assigned to security roles.  
  
 Within the form editor or from the forms grid you can assign security roles to a form. However, if there is only one form for the entity, you will not be able to clear the **Enabled for fallback** option in the **Assign Security Roles** dialog box. In this case, even though you have assigned security roles to the form, anyone associated with a security role you did not include will still be able to view the form because it is enabled for fallback.  
  
 After you create a second main or mobile form for the entity, you will be able to clear the **Enabled for fallback** option for one of them. The system will always make sure that at least one form is enabled for fallback.  
  
 When you have more than one main form, you can specify a form order that will control which of the forms a person is allowed to see will be the one they see by default. If there is more than one form they can use, they can change forms and the form they choose will be their default form until they choose a different one. This preference is stored in their browser. If they use a different computer or browser they will see the original default form.  
  
## Strategies to manage the fallback form  
 Strategies to manage the fallback form include the following:  
  
<a name="BKMK_DoNotUseMultipleForms"></a>   
### All users view the same form  
 If you do not require multiple forms for an entity you do not need a fallback form.  
  
<a name="BKMK_Contingecyform"></a>   
### Create a contingency form  
 If you are using role-based forms because you want to restrict the information people might view or edit, consider creating a form that has a minimum of information displayed. Then, in the **Assign Security Roles** dialog box, select **Display only to these selected security roles**, but do not select any roles except System Administrator, and select **Enabled for fallback**. The result is that this form will never be seen by anyone except the System Administrator and anyone whose security roles have not been associated with a specific form. You could include a HTML web resource in the form with information about why little information is visible in the form and a link to information about how to request being added to a security role that is associated with a from or to include a new security role for a form.  
  
> [!NOTE]
>  You can’t include a web resource in a form header or footer.  
  
<a name="BKMK_CreateGenericForm"></a>   
## Create a generic form  
 If you use role-based forms to provide a customized experience based on a user’s role, you can set your least specialized form as the fallback form and configure it to display for everyone. Then, create customized forms for specific security roles and configure those forms to only display for security roles that require them. Do not enable these forms for fallback. Finally, in the **Forms** list use the **Form Order** dialog to specify which forms to display ranking them from most exclusive to least exclusive. Your fallback form will be at the bottom of the list. This strategy will cause people seeing the form that has been customized for their role as the default form, yet they can still use the form selector to select the most common form if they want. Whatever form they select will remain their default form until they select a different form.  
  
<a name="BKMK_UseFormScripting"></a>   
## Use form scripting  

 Finally, in the web application it is possible, but not recommended, for a developer to use scripts in the form Onload event to use the [Xrm.Page.ui.formSelector.items collection](http://go.microsoft.com/fwlink/p/?LinkID=513300) to query available forms and use the navigate method to direct users to a specific form. Remember that the [navigate method](http://go.microsoft.com/fwlink/p/?LinkID=513301) will cause the form to load again (and the Onload event to occur again). Your logic in the event handler should always check some condition before you use the navigate method to avoid an endless loop or unnecessarily restrict users options to navigate between forms.  
  
 This approach will not work for Dynamics 365 for tablets because multiple forms are not available for selection.  

### Next steps  

[Assign security roles to forms](https://docs.microsoft.com/dynamics365/customer-engagement/admin/assign-security-roles-form)
