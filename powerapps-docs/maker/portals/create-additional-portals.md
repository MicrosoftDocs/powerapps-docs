---
title: Create additional sites in an environment
description: Instructions to create additional portals in an environment.
author: neerajnandwana-msft

ms.topic: conceptual
ms.custom: 
ms.date: 05/20/2022
ms.subservice: portals
ms.author: nenandw
ms.reviewer: ndoelman
contributors:
    - neerajnandwana-msft
    - nickdoelman
    - ProfessorKendrick
---

# Create additional sites in an environment


[!INCLUDE[cc-pages-banner](../../includes/cc-pages-banner.md)]

The ability to create additional environments is determined by the template chosen for the new site (portal). The following table explains the limits for creating additional portals in an environment.

| Environment type | Template | Limit | Additional information |
| - | - | - | - |
| [Environment with Dataverse](portal-templates.md#environment-with-dataverse) | Dataverse starter portal | 50 portals\* | No limits for language. Each portal can have one or more languages enabled. \*\*\* |
| [Environment with customer engagement apps](portal-templates.md#environment-with-customer-engagement-apps) | Portal from blank | 50 portals\* | No limits for language. Each portal can have one or more languages enabled. \*\*\* |
| [Environment with customer engagement apps](portal-templates.md#environment-with-customer-engagement-apps) | Community, Customer self-service, Employee self-service portals | 50 portals\*\* | No limits for language. Each portal can have one or more languages enabled. \*\*\*
| [Environment with customer engagement apps](portal-templates.md#environment-with-customer-engagement-apps) | Partner portal, [Customer portal for Dynamics 365 Supply Chain Management](/dynamics365/supply-chain/sales-marketing/customer-portal-overview) | one portal for each template | Limit of one portal template, but additional languages for each template can be enabled. \*\*\* |

\* Requires Starter portal package version [9.3.2109.x or later](release-updates.md#starter-portal-package-updates)

\*\* Requires Starter portal package version [9.3.2201.0 or later](release-updates.md#starter-portal-package-updates)

\*\*\* Additional languages can be enabled for individual portals, even if only one portal type per environment is allowed. For more information about enabling additional languages for portals, go to [Enable multiple language support](./configure/enable-multiple-language-support.md).

To enable multiple [Modern Community](/dynamics365/customer-service/community-get-started) portals, see [Create new websites in Community](/dynamics365/customer-service/community-create-websites).

Once you've reached the maximum number of a specific portal type for an environment, you'll see a message displayed indicating that the maximum number of portals has been reached.

## Create new environment

Follow these steps when you create an environment using the option provided in the **Portal from blank** window.

1.  In the **New environment** pane, enter a name for the environment, and then select a region and environment type from the drop-down lists. You can't change the region once the environment is created. When you're done, select **Create environment**.

    > [!div class=mx-imgBorder]
    > ![create new environment.](media/create-new-environment.png "Create new environment")  

2.  Once the environment is created, you'll receive a confirmation message in the dialog box, and you'll be prompted to create a database. Select **Create database** to enable access to Dataverse.

    > [!NOTE]
    > The prompt to create a database might not be displayed automatically. In this case, you must go to the new environment and select the **Portal from blank** tile again.

    > [!div class=mx-imgBorder]
    > ![new environment created.](media/new-environment-created.png "New environment created")  

3.  Select the currency and language for the data stored in the database. You can't change the currency or language once the database is created. When you're done, select **Create my database**. The database is created with the starter portal that enables you to quickly get started with sample content once the portal is provisioned.

    > [!NOTE]
    > The **Include starter portal** option is available only when you create an environment using the option provided in the **Portal from blank** window. This option is not available when you create an environment from Power Platform admin center.

    > [!div class=mx-imgBorder]
    > ![create new database.](media/create-new-database.png "Create new database") 

    It might take several minutes to create the database on Dataverse. Once the database is created, the new environment is selected in the list of environments on the Power Apps home page and the Portal Management app is created. This app isn't the actual portal but a model-driven companion app that allows you to perform advance configuration activities. You can now continue with creating the portal for designing the external-facing website.

    > [!div class=mx-imgBorder]
    > ![portal management app.](media/portal-mgmt-app.png "Portal management app")

4. After creating the environment and database, under **Make your own app**, select **Portal from blank**. 

    > [!NOTE]
    > If the database is created and you are still getting the create database prompt, you must refresh the Power Apps home page before selecting the **Portal from blank** tile.

After you enter the portal name, address, and choose the language, the portal creation begins. For portal creation notification information, see [Portal provisioning notifications](create-portal.md#portal-provisioning-notifications).

### See also

[Available portal templates](portal-templates.md) <br>
[Administer Power Apps portals](/training/paths/administer-portals/) <br>

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
