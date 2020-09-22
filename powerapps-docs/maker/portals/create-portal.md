---
title: Create a portal in Power Apps | Microsoft Docs
description: Instructions to create a portal in Power Apps.
author: neerajnandwana-msft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 09/22/2020
ms.author: nenandw
ms.reviewer: tapanm
---

# Create a Common Data Service starter portal

With the capability to build a portal in Power Apps, you can create a website for external and internal users enabling them to interact with data stored in Common Data Service.

Some of the benefits of creating a Power Apps portal:

- Because the data is stored in Common Data Service, you don't need to create a connection from Power Apps as you do with data sources such as SharePoint, customer engagement apps (such as Dynamics 365 Sales and Dynamics 365 Customer Service), or Salesforce. You need only to specify the entities that you want to show or manage in the portal.

- You can design the portal through the WYSIWYG Power Apps portals Studio by adding and configuring components on the webpages.

You can create a portal either in a new environment or in your existing environment.

If you choose to create your portal in a new environment using the **Create new environment** link, the required portal pre-requisites such as entities, data, and a starter portal template are installed when the environment is created. In this method, the portal is provisioned in a few minutes.

If you choose to create your portal in an existing environment without portal pre-requisites, the pre-requisites are installed first and then the portal is created. In this method, the portal provisioning can take some time and you’ll be notified when the portal is provisioned.

Based on the selected environment in Power Apps, you can create a Common Data Service starter portal or a portal in an environment containing customer engagement apps (such as Dynamics 365 Sales and Dynamics 365 Customer Service).

> [!NOTE]
> - There can be only one portal of each type and for a language created in an environment. For more information, go to [creating additional portals](#create-additional-portals-in-an-environment).
> - When you create a portal, a few solutions are installed and sample data is imported.

More information on working with environments: [Working with environments and Microsoft Power Apps](https://docs.microsoft.com/powerapps/maker/canvas-apps/working-with-environments)

More information on available portal templates: [Portal templates](portal-templates.md)

To create a portal:

1.  Sign in to [Power Apps](https://make.powerapps.com).  

2.  Under **Make your own app**, select **Portal from blank**.

3.	If the selected environment doesn't contain portal pre-requisites, a message is displayed in the **Portal from blank** window suggesting you select another environment or create a new one.

    ![create new environment message](media/create-portal-message.png "Create new environment message")

4.	If you choose to continue with the current environment, enter the required information in the window as mentioned in the following steps. If you choose to create a new environment, see [Create new environment](#create-new-environment).

5.  In the **Portal from blank** window, enter a name for the portal and address for the website, and select a language from the drop-down list. When you're done, select **Create**.

    > [!TIP]
    > To create a portal using a different language, you must first [enable the language in the environment](https://docs.microsoft.com/power-platform/admin/enable-languages#enable-the-language) so that it becomes available in the language drop-down list.

    > [!div class=mx-imgBorder]
    > ![create new portal](media/create-new-portal.png "Create new portal")  

After you select **Create**, the portal will begin provisioning and the provisioning status is displayed through [notifications](#portal-provisioning-notifications).

If you've created your portal in the environment that doesn't have portal pre-requisites installed, the provisioning status is also displayed in the grid:

> [!div class=mx-imgBorder]
> ![Grid notification](media/provision-progress-notif.png "Grid notification")

After the portal is provisioned successfully, the status is updated and the portal is displayed in the grid:

> [!div class=mx-imgBorder]
> ![Portal provisioned](media/recent-apps.png "Portal provisioned")

To edit the portal in Power Apps portals Studio, see [Edit a portal](manage-existing-portals.md#edit).

> [!NOTE]
> - If you don't have sufficient privileges to provision a portal, an error is displayed. You must have the System Administrator role in Common Data Service to create a portal. You must also have the **Access Mode** set to **Read-Write** under **Client Access License (CAL) Information** in the user record.
> - If you have purchased an older portal add-on, and want to provision a portal using the add-on, you must go to the **Dynamics 365 Administration Center** page. More information: [Provision a portal using the older portal add-on](provision-portal-add-on.md)
> - If you have provisioned a portal using the older portal add-on, you can still customize and manage it from [make.powerapps.com](https://make.powerapps.com).
> - Provisioning portals from [make.powerapps.com](https://make.powerapps.com) does not consume the older portal add-ons. Also, these portals are not listed under the **Applications** tab on the **Dynamics 365 Administration Center** page.
> - A Common Data Service starter portal cannot be created from the **Dynamics 365 Administration Center** page.
> - Power Apps portals is not available in the France region.

### Create additional portals in an environment

An environment can have one portal of each type and for each language. Environments with Common Data Service have [starter portal template](portal-templates.md#environment-with-common-data-service) available. If you already have a starter portal for such an environment, you can't create another starter portal for the same language. Similarly, environments with customer engagement apps (Dynamics 365 Sales, Dynamics 365 Customer Service, Dynamics 365 Field Service, Dynamics 365 Marketing, or Dynamics 365 Project Service Automation) have several [portal templates](portal-templates.md#environment-with-customer-engagement-apps) available. If you have a portal from one of the templates already created in a language, you can't create a new portal with the same template type and language. New portal must have either a different portal type, or a different language.

For example, consider a scenario where you have a Common Data Service environment without the Dynamics 365 Apps. In this environment, you have a portal with *English* language created with the template type of *Starter portal*. You want to create a new portal in this environment.

In this scenario, the following table explains which additional portal template and language combination is allowed when creating additional portals:

| Template type and language of existing portal  | Template type and language of the new portal that you want to create | Allowed |
| - | - | - |
| *Starter portal* in English | *Starter portal* in English | &cross; |
| *Starter portal* in English | *Starter portal* in French | &check; |

Similarly, the following table explains the allowed template type and language combination for a portal that can be created if you have a Common Data Service environment with Dynamics 365 Apps. In this example, you have a portal with the template *Portal from blank* created in *English* language. You want to create a new portal in this environment.

| Template type and language of existing portal | Template type and language of the new portal that you want to create | Allowed |
| - | - | - |
| *Portal from blank* in English | *Portal from blank* in English | &cross; |
| *Portal from blank* in English | *Community portal* in English | &check; |
| *Portal from blank* in English | *Portal from blank* in French | &check; |

When an environment already has a portal of the available template type created, and if the environment doesn't have any additional languages enabled, you'll see this error message: *You have reached the maximum limit of 1 portal(s) on this environment. Please choose another environment or create new environment.*

![Error when creating additional portal](media/create-additional-portal-error.png "Error when creating additional portal")

For more information about enabling languages in an environment, go to [Enable language for an environment](https://docs.microsoft.com/power-platform/admin/enable-languages#enable-the-language).

## Create new environment

Follow these steps when you create an environment using the option provided in the **Portal from blank** window.

1.  In the **New environment** pane, enter a name for the environment, and then select a region and environment type from the drop-down lists. You can't change the region once the environment is created. When you're done, select **Create environment**.

    > [!div class=mx-imgBorder]
    > ![create new environment](media/create-new-environment.png "Create new environment")  

2.  Once the environment is created, you'll receive a confirmation message in the dialog box, and you'll be prompted to create a database. Select **Create database** to enable access to Common Data Service.

    > [!NOTE]
    > The prompt to create a database might not be displayed automatically. In this case, you must go to the new environment and select the **Portal from blank** tile again.

    > [!div class=mx-imgBorder]
    > ![new environment created](media/new-environment-created.png "New environment created")  

3.  Select the currency and language for the data stored in the database. You can't change the currency or language once the database is created. When you're done, select **Create my database**. The database is created with the starter portal that enables you to quickly get started with sample content once the portal is provisioned.

    > [!NOTE]
    > The **Include starter portal** option is available only when you create an environment using the option provided in the **Portal from blank** window. This option is not available when you create an environment from Power Platform admin center.

    > [!div class=mx-imgBorder]
    > ![create new database](media/create-new-database.png "Create new database") 

    It might take several minutes to create the database on Common Data Service. Once the database is created, the new environment is selected in the list of environments on the Power Apps home page and the Portal Management app is created. This app isn't the actual portal but a model-driven companion app that allows you to perform advance configuration activities. You can now continue with creating the portal for designing the external-facing website.

    > [!div class=mx-imgBorder]
    > ![portal management app](media/portal-mgmt-app.png "Portal management app")

4. After creating the environment and database, under **Make your own app**, select **Portal from blank**. 

    > [!NOTE]
    > If the database is created and you are still getting the create database prompt, you must refresh the Power Apps home page before selecting the **Portal from blank** tile.


## Portal provisioning notifications

After you select **Create**, the portal will begin provisioning and the provisioning status is displayed through notifications.

**Notification as a toast**

The following notification is displayed when you select **Create** to provision the portal.

> [!div class=mx-imgBorder]
> ![Toast notification](media/toast-notif.png "Toast notification") 

**Notifications in the Notifications pane**

Once the provisioning request is successfully placed, the following notifications are displayed in the **Notification** pane.

Notification shown for provisioning in progress.

> [!div class=mx-imgBorder]
> ![Pane notification](media/pane-notif.png "Pane notification")

Notification shown for provisioning successfully completed.

> [!div class=mx-imgBorder]
> ![Provisioning success notification](media/provision-complete-notif.png "Provisioning success notification") 

If the portal provisioning fails, the notifications are displayed similarly.
  
**Notifications via emails**

Once the provisioning request is successfully placed, a confirmation email notification is sent to the user creating the portal. Also, an email is sent to the user after the portal provisioning is completed.

## Disable portal creation in a tenant

As a global administrator, if you want to disable portal creation in a tenant by non-administrators, you can do it by enabling the `disablePortalsCreationByNonAdminUsers` tenant level setting through PowerShell. To run PowerShell cmdlets, you must first install the required modules. For information on installing the required PowerShell modules, see [Installation](https://docs.microsoft.com/power-platform/admin/powerapps-powershell#installation).

After installing the modules, run the following command in a PowerShell window (run PowerShell as an administrator).

```
Set-TenantSettings -RequestBody @{ "disablePortalsCreationByNonAdminUsers" = $true }
```

Administrators are the users having one of the following Azure roles:

- Global Administrator
- Dynamics 365 admin
- Power Platform admin

Users not having any of the above mentioned Azure roles are considered as non-administrators.

When the portal creation is disabled in a tenant, non-administrators will see an error as follows:

> [!div class=mx-imgBorder]
> ![Portal creation blocked error](media/portal-create-blocked-error.png "Portal creation blocked error")

### See also

- [Microsoft Learn: Administer Power Apps portals](https://docs.microsoft.com/learn/paths/administer-portals/)
- [Microsoft Learn: Access Common Data Service in Power Apps portals](https://docs.microsoft.com/learn/modules/portals-access-common-data-service/)
