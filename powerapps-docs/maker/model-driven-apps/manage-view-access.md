---
title: "Manage access to public system views"
description: "Learn how to managed access with security roles to public system views for model-driven apps in Microsoft Power Apps"
ms.custom: ""
ms.date: 06/23/2025
ms.reviewer: "matp"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "how-to"
applies_to: 
  - "powerapps"
author: "Mattp123"
ms.subservice: mda-maker
ms.author: "paulliew"
ai-usage: ai-assisted
search.audienceType: 
  - admin
  - maker
---
# Manage access to public system views 

Admins can manage views that users can access in model-driven apps with security roles. When a user plays a model-driven app, the user only has access to the system views that apply to the security roles that they're assigned to.

System views are special views that model-driven apps depend on, which exist for system tables or are automatically created when you create custom tables. These views have specific purposes and some additional capabilities. By default, all system views are for **everyone**. When a Power Platform admin manages a view with a security role, only the users who are assigned with the selected security role are able to see the view in the view selector. The other system views aren't filtered from the view selector dropdown list. Users can still access all the views when they navigate to the **Manage and share views** option.

After a Power Platform admin turns on the manage table list views feature, users can set their own default view from the list of views that the admin manages and their own personal views from the Manage and share views option in a model-driven app.

:::image type="content" source="media/manage-share-views.png" alt-text="Manage and share views feature in a model-driven app":::

Data access continues to be secured with security role privileges, which means only records that a user has access to are displayed by the views. Having access to a particular view doesn’t mean you also have access to the data that's available in the view.

> [!NOTE]
> This feature filters views that appear in the table list view selector. All system and associated views continue to display in subgrids and associated grids that have a view selector.

## Prerequisites

- System administrator security role membership in the Microsoft Dataverse environment.
- Turning on auditing is recommended, but not required.

## System views in a Dataverse environment

System views are predefined views that exist for all system tables. These views can include Public, Quick Find, Advanced Find, Associated, or Lookup. When an admin or maker creates a view from Power Apps (make.powerapps.com), the view becomes a public view. You can manage public views with security roles.

### Commonly used public view examples

You can manage the table list of views with your business users based on the users’ security role assignment. Admins select the applicable system views and manage these views with security roles. When the user navigates to a table list form, they can access the system views that were managed with the security roles that are assigned to them. The selected system views with security role aren't visible to users who don't have the security role assigned.

Examples of public views:

| Table   | Public view                                      |
|---------|--------------------------------------------------|
| Account | My Active Accounts                               |
| Account | Accounts: No Campaign Activities in Last 3 months|
| Lead    | My Open Leads                                    |
| Lead    | All Leads                                        |
| Case    | All Cases                                        |
| Case    | Cases I follow                                   |
| Case    | My Cases                                         |
| Case    | My Resolved cases                                |
| Contact | All Contacts                                     |
| Contact | Contact I follow                                 |
| Contact | Inactive contacts                                |

## Turn on manage table list views

1. Make sure you enable the table list views feature in your environment. More information: [Prerequisites](#prerequisites)
1. You manage public views with security roles. If you need to create new security roles, go to [Security roles and privileges](/power-platform/admin/security-roles-privileges) for more information about security roles.
1. Create a solution and add the tables and their corresponding views that you manage.
1. Export the solution.
1. Import the solution into your production environment. Inform your users that their system views are now filtered based on their security role assignment.

## Manage public views with security roles

All system views can be managed with security roles. Once they’re managed, users with the assigned security roles only view these views in the view selector.

> [!NOTE]
> System views are denoted as **Public** view type in Power Apps (make.powerapps.com). Only public views can be managed. Default public views can’t be assigned security roles for access.

### Manage system views with security roles

1. Sign in to [Power Apps](https://make.powerapps.com).
1. On the left navigation pane, select **Solutions**, and then open the solution that has the table with the view you want to manage. If the item isn’t in the side panel pane, select …More and then select the item you want.
1. Open a table, such as the account table, and then select the **Views** area.
1. Select the nondefault public view that you want, and then on the command bar, select **View settings**.
1. Select the **Specific security roles** option.
1. Select the security roles that you want to assign to the public view.
1. When you're done selecting the security roles, select **Save and Publish**.
   :::image type="content" source="media/select-security-roles-public-view.png" alt-text="Select security roles for public view access":::

> [!NOTE]
> When you make changes to the 'EnableRoleBasedSystemViews' and **View settings**:
>
> 1. Setting the OrganizationSettingsEditor tool `EnableRoleBasedSystemViews' property to **true** is effective immediately.
> 2. Setting a view with security roles is effective immediately after you select **Save and publish**.
> 3. Changing a view setting from 'Specify security role' to 'Everyone' can take up to 24 hours to be effective or until the user signs out and back in.
>
> If you select multiple views and go to the view settings, only the first selected Views can be updated. You're required to select individual view to update the view settings. 

## Manage business unit system views with security roles

You can create **business unit** system views by applying a filter in the view. Follow the same steps for [Manage system views with security roles](#manage-system-views-with-security-roles) to set the **Specify security roles** option to the business unit view. Then, filter the view using **Owning Business Unit** equals the business unit you want.
:::image type="content" source="media/filter-view-owning-business-unit.png" alt-text="Filter view by owning business unit to secure":::
The users who are assigned with the security role of the business unit are able to access the view in their view selector. All other users can't access the business unit view.

> [!NOTE]
> The security roles as listed under the **View settings** are shown from the parent business unit. Business unit level security roles are inherited from the parent business unit. When these security roles are selected, the system automatically applies the security role filtering based on the view's business unit.

### Related articles

[Create or edit a model-driven app view in Power Apps](create-edit-views.md)
