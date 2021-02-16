---
title: "Add record-based security by using Entity Permissions for a portal | MicrosoftDocs"
description: "Instructions to add an entity permission and assign web roles to it."
author: sandhangitmsft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 01/06/2021
ms.author: sandhan
ms.reviewer: tapanm
---

# Add record-based security by using entity permissions for portals

[!INCLUDE[cc-data-platform-banner](../../../includes/cc-data-platform-banner.md)]

To apply record-based security in portals to individual records, use entity permissions. You add entity permissions to web roles so you can define roles in your organization that correspond logically to the privileges and concepts of record ownership and access that are introduced by using entity permissions. Remember that a given contact can belong to any number of roles, and a given role can contain any number of entity permissions. [!INCLUDE[proc-more-information](../../../includes/proc-more-information.md)] [Create web roles for portals](create-web-roles.md) 

Although permissions to change and access URLs in a portal site map is granted via Content Authorization, site managers will also want to secure their custom web applications built with entity forms and entity lists. [!INCLUDE[proc-more-information](../../../includes/proc-more-information.md)] [Define entity forms](entity-forms.md) and [Define entity lists](entity-lists.md)  

To secure these features, entity permissions allow for granular rights to be granted for arbitrary entities and for record-level security to be enabled via relationship definitions.

## Add entity permissions to a web role

1.  Open the [Portal Management app](configure-portal.md).

2. Go to **Portals** &gt; **Web Roles** and open the web role you want to add the permissions to. 

3. Under **Related**, select **Entity Permissions**.

4. Select **Add Existing Entity Permission** to add an existing entity permission to a web role. 

4. Browse for an entity permission or select **New Entity Permission** to create a new Entity Permission record.

    ![Add entity permissions to a web role](../media/add-entity-permission-web-role.png "Add entity permissions to a web role")  

When creating a new Entity Permission record, the first step is to determine the entity that will be secured. The next step is to define scope, as discussed in the following section, and&mdash;for any scope other than Global&mdash;the relationships that define that scope. Finally, determine the rights that are being granted to the role via this permission. Rights are cumulative, so if a user is in a role that grants Read, and another that grants Read and Update, the user will have Read and Update rights for any records that overlap between the two roles.

> [!Note]
> Selecting entities like webpage, web files and other configuration entities is invalid and might have other unintended consequences. The portal will assert the security of configuration entities based on content access controls, not entity permissions.

### Global scope

If an Entity Permission record with Read permission is granted to a role that has global scope, any contact in that role will have access to all records of the defined entity. For example, they can see all leads, all accounts, and so on. This permission will be automatically respected by any entity lists, essentially showing all records according to the model-driven app views that have been defined for that list. Further, if a user attempts to access a record via an entity form that they don't have access to, they'll receive a permission error.

### Contact scope

With Contact scope, a signed-in user in the role for which the permission record is defined will have the rights granted by that permission only for records that are related to that user's contact record via a defined relationship.

On an entity list, this scope means that a filter will be added to whatever model-driven app views are surfaced by that list, which only retrieves records directly linked to the current user. (Depending on the scenario, this relationship can be thought of as ownership or management rights.)

Entity forms will only allow the appropriate permission for Read, Create, Write, and so on, if this relationship exists when the record is loaded. [!INCLUDE[proc-more-information](../../../includes/proc-more-information.md)] [Define entity forms](entity-forms.md).  

### Account scope

With Account Scope, a signed-in user in the role for which the permission record is defined will have the rights granted by that permission only for records that are related to that user's parent account record via a defined relationship.

This scope means that the entity list will only show the records of the selected entity that are associated to the user's parent account. For example, if an entity permission allows Read access to Lead entity with the Account scope, the user having this permission can view all the leads of only the parent account of the user.

### Self scope

Self Scope allows you to define the rights a user has to their own Contact (Identity) record. Users can use entity forms or web forms to make changes to their own Contact record linked with their profile. The default Profile Page has a special built-in form that allows any user to change their basic contact info, and opt in or out of marketing lists. If this form is included in your portal (which it is by default), users won't require this permission to use it. However, they'll require this permission to use any custom entity forms or web forms that target their User Contact record.

### Parental scope

In this most complex case, permissions are granted for an entity that is a relationship away from an entity for which an Entity Permission record has already been defined. This permission is actually a child record of the parent entity permission.

The Parent Permission record defines a permission and scope for an entity (probably Global or Contact scope, although Parent is also possible). That entity might be related to a Contact (if there's Contact scope) or globally defined. With that permission in place, a child permission is created that defines a relationship from another entity to the entity defined in the parent relationship.

Users in a web role who have access to records defined by parent entity permissions will also have rights as defined by the child permission record to records related to the parent record.

### Attributes and relationships

The following table explains the entity permission attributes.



| Name                     | Description                                                                                                                                                                                                                                                                                                               |
|--------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Name                     | The descriptive name of the record. This field is required.                                                                                                                                                                                                                                                               |
| Entity Name              | The logical name of the entity that is to be secured or that will define the contact relationship or parent relationship to secure a related entity on a child permission. This field is required.                                                                                                                        |
| Scope (mandatory)                   | <ul><li>**Global**: Grant privileges to the entity record without any requirement for an owner (contact).</li><li>**Contact**: Grant privileges to the entity record that has a direct relationship to an owner (contact).</li><li>**Account**: Grant privileges to the entity record that has a relationship to an account, which serves as the owner assuming the account is the parent customer of the contact.</li><li>**Parent**: Grant privileges to the entity record through the chain of its parent permissions' relationships.</li></ul>|
| Relationship for Scope | Depends on the selected Scope. <ul> <li> **Contact Relationship**: Required only if Scope = Contact. <br> The schema name of the relationship between the contact and the entity specified by the Entity Name field. </li> <li> **Account Relationship**: Required only if Scope = Account. <br> The schema name of the relationship between the account and the entity specified by the Entity Name field. </li> <li> **Parent Relationship**: Required only if a parent entity permission is assigned. <br> The schema name of the relationship between the entity specified by the Entity Name field and the entity specified by the Entity Name field on its Parent Entity Permission record. <ul> <li> **Parent Entity Permission**:  Required only if Scope = Parent. </li> </li> </ul>  </ul> <br> **Note**: Available relationships will be empty if the Contact, or the Account has no existing relationships with the selected entity. To create entity relationships, see [Entity relationships overview](../../data-platform/create-edit-entity-relationships.md).
| Read                     | Privilege that controls whether the user can read a record.                                                                                                                                                                                                                                                               |
| Write                    | Privilege that controls whether the user can update a record.                                                                                                                                                                                                                                                             |
| Create                   | Privilege that controls whether the user can create a new record. The right to create a record for an entity type doesn't apply to an individual record, but instead to a class of entities.                                                                                                                             |
| Delete                   | Privilege that controls whether the user can delete a record.                                                                                                                                                                                                                                                             |
| Append                   | Privilege that controls whether the user can attach another record to the specified record. The Append and Append To access rights work in combination. Every time that a user attaches one record to another, the user must have both rights. For example, when you attach a note to a case, you must have the Append access right on the note and the Append To access right on the case for the operation to work.  |
| Append To                | Privilege that controls whether the user can append the record in question to another record. The Append and Append To access rights work in combination. For more information, see the description for Append.|
| | |

## Global permissions for tasks related to leads

In one scenario, we might want to use an entity list and entity forms to surface all leads on the portal to anyone in a custom Lead Manager web role. On the Lead Edit Form, which is launched whenever a lead row is selected on the list, a subgrid will display related Task records. These records should be accessible to anyone in the Lead Manager role. As the first step, we'll give Global permissions to leads to anyone in our Lead Manager Role.

This role has a related Entity Permission for the Lead entity, with a Global scope.

Users in this role can access all leads via entity lists or forms on the portal.

![Grant global permissions to a lead](../media/grant-global-permission-leads.png "Grant global permissions to a lead")  

We'll now add a Child permission to the Global Lead permission. With the Parent Permission record open, go to the **Child Entity Permissions** subgrid, select **New Entity Permission** to add a new record.

![Add child permissions to the Global Lead permission](media\assign-entity-permissions\global-lead-child-permissions-new.png "Add child permissions to the Global Lead permission")  

Select the entity as Tasks and the scope as Parental. You can then select the parent relationship (**Lead\_Tasks**). This permission implies that a contact that is in a web role with the parent permission will then have global permission to all tasks that are related to leads.

In order for your list to respect these permissions:

- Entity Permissions must be enabled on the list.
    
    ![Enable Entity Permissions on the list](media\assign-entity-permissions\enable-entity-permissions.png "Enable Entity Permissions on the list") 

- There must be actions that will actually allow users to do the actions for which their permissions have been granted. 

    ![Actions for which permissions have been granted](media\assign-entity-permissions\form-actions.png "Actions for which permissions have been granted") 

- Permissions must also be enabled on the [entity form](entity-forms.md) record.

    ![Enabled permissions on the entity form record](media\assign-entity-permissions\lead-entity-form.png "Enabled permissions on the entity form record")
 
- The form must be surfacing a page that has a subgrid on it for the entity that you want to enable with child permissions, in this case Tasks.

    ![Subgrid with the entity - Tasks](media\assign-entity-permissions\subgrid-on-form.png "Subgrid with the entity - Tasks")

Also, if you want to enable Read or Create permissions for tasks, you'll need to configure those entity forms too, and edit the forms to remove the Regarding lookup field.  

This action then grants permissions for all tasks that are related to leads. If tasks are being surfaced on an entity list, a filter is added to the list so that only tasks that are related to a lead will appear in the list. In our example, they're being surfaced with a subgrid on an entity form.

![Task example](../media/tasks-example.png "Task example")  

## Contact-scoped permissions for tasks

Another example would be if you wanted to allow access to tasks for which a contact is related to the parent lead for that task. This scenario is nearly identical to the previous section, except in this case the parent permission has a scope of Contact, instead of Global. A relationship must be specified on the parent relationship between the Lead entity and the Contact entity.

After these permissions are in place, users in the Lead Manager role can access leads that are related to them directly as specified by the contact-scope permission, and access tasks related to those same leads as specified by the child permission record.

### See also

[Create web roles for portals](create-web-roles.md)  
[Control webpage access for portals](webpage-access-control.md)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]