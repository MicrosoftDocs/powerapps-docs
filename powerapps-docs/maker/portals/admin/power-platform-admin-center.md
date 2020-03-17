---
title: "Power Apps Portals settings on Power Platform admin center | MicrosoftDocs"
description: "Information about Power Apps Portals settings on Power Platform admin center."
author: tapanm-msft
manager: kvivek
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 03/17/2020
ms.author: nenandw
ms.reviewer: tapanm
---

## Manage Portals

You can manage Portals in the Power Platform admin center.

Portals in this topic refer to Power Apps Portals; such as Starter portal,
Community portal, Employee self-service portal, Customer self-service, and
Partner portal.

You can manage portals from either the tenant level or environment level.

## Tenant-level view of portals

To see a list of all portals for your tenant:

1. Sign in to the [Power Platform admin
    center](https://admin.powerplatform.microsoft.com/).

1. Select **Resources** and then **Portals** from the left-side menu.

    You'll see a list of installed or available for installation Dynamics 365 apps for the signed-in user and their tenant. An admin will see all installed or available for installation apps.

    ![Portals option on Power Portals admin center](..\media\portals-on-ppac.png)

Environment-level view of portals
---------------------------------

Follow these steps to see a list of all portals for your environment.

1.  Sign in to the [Power Platform admin
    center](https://admin.powerplatform.microsoft.com/).

2.  Select **Environments** and then select an environment.

3.  Under **Resources**, select **Portals**.

You'll see a list of Portals installed in the selected environment.

![Environments on Power Platform admin center](..\media\environments-on-ppac.png)

**Type**:

| **Type**            | **Description**                                                                    |
|---------------------|------------------------------------------------------------------------------------|
| Production          | Production portal based on capacity-based license                                  |
| Trial (n days)      | Trial portal based on capacity-based license with n days remaining for suspension. |
| Production (add-on) | Production portal based on add-on license                                          |
| Trial (add-on)      | Trial portal based on add-on license                                               |

**Status**

| **Status**     | **Description**                                                                                                                 |
|----------------|---------------------------------------------------------------------------------------------------------------------------------|
| Configured     | This portal has been configured to an environment.                                                                              |
| Suspended      | This portal has been suspended due to trial period over. This portal will be deleted in 7 days, if not converted to production. |
| Not-configured | This app is ready to be configured to an environment.                                                                           |
