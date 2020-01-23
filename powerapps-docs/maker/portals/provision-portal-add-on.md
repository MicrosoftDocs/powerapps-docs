---
title: "Provision a portal using the older portal add-on | MicrosoftDocs"
description: "Instructions to provision a portal using the older portal add-on."
author: tapanm-msft
manager: kvivek
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 11/11/2019
ms.author: tapanm
ms.reviewer:
---

# Provision a portal using the older portal add-on

If you have purchased an older portal add-on, and want to provision a portal using the add-on, you must go to the **Dynamics 365 Administration Center** page and provision the portal.

> [!NOTE]
> To provision a portal, you must be assigned either System Administrator or System Customizer role of the Common Data Service environment selected for the portal. You must also have the [required permissions](https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal#required-permissions) to create and register an application in Azure AD. If you don't have the required permissions, contact the Global Administrator to update your permissions or ask the Global Administrator to provision the portal.

To provision a portal:

1. Sign in to [Microsoft 365 admin center](https://admin.microsoft.com).
 
2. In the navigation column on the left, select **Show all**.

3. If you are working with the new admin center, select **All admin centers**. From the list of all admin centers, select **Dynamics 365**.

    > [!div class="mx-imgBorder"]
    > ![Open Dynamics 365 Administration Center from new admin center](media/from-new-admin-center.png "Open Dynamics 365 Administration Center from new admin center") 

4. If you are working with the old admin center, expand **Admin centers** in the left navigation column, and then select **Dynamics 365**.

    > [!div class="mx-imgBorder"]
    > ![Open Dynamics 365 Administration Center from old admin center](media/from-old-admin-center.png "Open Dynamics 365 Administration Center from old admin center") 

5. On the **Dynamics 365 Administration Center** page, select the **Applications** tab.

6. Select the application row titled **Portal Add-On**, and then select **Manage.**

7. In the **General Settings** section, enter a **Name** for your portal. The **Name** will help to identify the portal and can be changed later.

8. The **Type** field represents the type of portal subscription (Trial or Production). This is a system field, so it cannot be changed by the user. The value changes based on whether it is trial subscription or paid subscription.

9. Optionally, in the **Portal development status** drop-down list, select one of the following development statuses for your portal:

    - Prototype
    - Development
    - Test
    - UAT
    - Live

    > [!NOTE]
    > - For existing provisioned portals, this drop-down list is available on the **Portal Details** tab and no status is selected by default.
    > - This drop-down list is available only for the portals of type production.
    > - This field is used by Microsoft to understand the usage pattern of this portal and does not affect any functionality. If you use different names for development lifecycle, please select the one which is closer in purpose. This can be changed at a later point of time once portal is provisioned.

10. In the **Portal URL** field, enter the subdomain name you want for your portal. You can only use alphanumeric characters or hyphens (-); other characters are not permitted.

    > [!NOTE]
    > - To change the URL of a portal after it is provisioned, see [change the base URL of a portal](admin/change-base-url.md).
    > - To link your portal to a custom domain, see [link your portal to a custom domain](admin/add-custom-domain.md).

11. In the **Dynamics 365 Instance** drop-down list, select the instance you want to link the portal to. This requires System Administrator or System Customizer role in the instance you pick to select it.

12. In the **Select Portal Language** drop-down list, select the default language for your portal. The available languages will depend on the languages that are installed in your instance. 
    
    > [!NOTE]
    > Sample data is only provided in one language, so choosing a default language will also decide how the sample data is translated. Arabic and Hebrew are not supported and will not appear in the list.

13. In the **Select Portal Administrator** drop-down list, select the user who will configure, customize, and maintain the portal. All users who have the System Administrator role in the organization will appear as options. 

14. In the **Portal Audience** section, choose the type of audience who will visit the new portal. This will determine what options of portals you will be given. You can choose:

    -   Partner    
        -   Customer Self Service Portal
        -   Custom Portal
        -   Partner Portal
        -   Partner Project Service (Optional, requires solutions installed)
        -   Partner Field Service (Optional, requires solutions installed)
        -   Community Portal

    -   Customer
        -   Customer Self Service Portal
        -   Custom Portal
        -   Community Portal

    -   Employee
        -   Employee Self Service Portal

15. In the **Select portal to be deployed** section, choose what type of portal you want to create. The options you see are based on the audience you selected.

    > [!div class="mx-imgBorder"]
    > ![Configure settings for your portal](media/configure-settings-portal.png "Configure settings for your portal")  

16. Select **Submit**, and accept the Terms of Service.
    > [!div class="mx-imgBorder"]
    > ![Terms of service](media/terms-of-service.png "Terms of service")  

After you accept the Terms of Service, the portal will begin provisioning. Provisioning usually takes 30 minutes but can take a few hours depending on the system load. The *Name* of the portal on the Application tab will change to *Name*-Configuring while it is provisioning. Navigate back to the portal management page to check whether provisioning has succeeded.

After the portal is provisioned, the **Portal Details** page is displayed with the required details.

> [!div class="mx-imgBorder"]
> ![Portal details](media/portal-details-prov.png "Portal details") 


> [!Note]
> When a portal user signs in to the portal for the first time by using an Azure AD credential, a consent page is displayed to all users irrespective of the user or portal type.

The table below summarizes the features associated with each portal option:

| Feature                                | Customer Self-Service Portal | Partner Portal | Employee Self-Service Portal | Community Portal | Custom Portal |
|----------------------------------------|------------------------------|----------------|------------------------------|------------------|---------------|
| World Ready                            | •                            | •              | •                            | •                | •             |
| Multi-Language Support                 | •                            | •              | •                            | •                | •             |
| Portal Administration                  | •                            | •              | •                            | •                | •             |
| Customization and Extensibility        | •                            | •              | •                            | •                | •             |
| Theming                                | •                            | •              | •                            | •                | •             |
| Content Management                     | •                            |                | •                            | •                |               |
| Knowledge Management                   | •                            | •              | •                            | •                |               |
| Support/Case Management                | •                            |                | •                            | •                |               |
| Forums                                 | •                            |                | •                            | •                |               |
| Faceted Search                         | •                            |                | •                            |                  |               |
| Profile Management                     | •                            |                | •                            |                  |               |
| Subscribe to Forum Thread              | •                            |                | •                            |                  |               |
| Comments                               | •                            |                | •                            | •                |               |
| [!INCLUDE[pn-azure-shortest](../../includes/pn-azure-shortest.md)] AD Authentication                |                              |                | •                            |                  |               |
| Ideas                                  |                              |                |                              | •                |               |
| Blogs                                  |                              |                |                              | •                |               |
| Project Service Automation Integration |                              | •              |                              |                  |               |
| Field Service Integration              |                              | •              |                              |                  |               |
| Partner Onboarding                     |                              | •              |                              |                  |               |
| Portal Base                            |  •                           | •              |  •                           | •                | •             |
| Portal Workflows                       |  •                           | •              |  •                           | •                | •             |
| Web Notifications                      |  •                           | •              |  •                           | •                | •             |
| [!INCLUDE[cc-microsoft](../../includes/cc-microsoft.md)] Identity                     |     •                         |  •              |     •                         |   •               | •             |
| Identity Workflows                     | •                            |  •             |     •                         |   •               | •             |
| Web Forms                              |  •                            | •               |    •                          | •                 | •             |
| Feedback                               |   •                           |  •              |  •                            | •                 | •             |
||

## Troubleshoot provisioning

Sometimes the package installation process or URL creation process can error out. In these cases, the processes can be restarted.

If *Name*-Configuring changes to *Name*-Provisioning Failed, you need to restart the provisioning process.

1. Go to the **Applications** page, and select the portal.
2. Select the blue pencil button labeled **Manage**.
3. Choose one of the following options:

   - **Restart Provisioning**: Restarts the installation process with the configuration that was previously defined.

   - **Change Values and Restart Provisioning**: Lets you change some of the values before restarting the provisioning process.

If the package installation has failed, the portal administrator page will open without any issues, but navigating to the actual portal URL will show a message Getting set up. To confirm this:

1. Go to the Solution Management page of the **Dynamics 365 Administration Center** page and check that the package status is **Install Failed**. 

2. If the package status is **Install Failed**, try retrying the installation from the solution page. Also, be sure to check that a system administrator is installing the solution with the default language in Common Data Service set to the language the portal should be installed in.

> [!NOTE]
> Some solutions have prerequisites for their installation, so an installation will fail if the prerequisites are not met. For example, to install the Partner Field Service for a partner portal, the Partner Portal and Field Service solutions must have already been installed. If you attempt to install the Partner Field Service first, the installation will fail and give you an error message.
