---
title: Import metadata translation
description: Instructions to import metadata translation.
author: neerajnandwana-msft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 04/21/2021
ms.subservice: portals
ms.author: nenandw
ms.reviewer: tapanm
contributors:
    - neerajnandwana-msft
    - tapanm-msft
---

# Import metadata translation

When you provision a portal, the portal-related solutions are installed on the organization. During the installation of solutions, the solution metadata translations (for example, field name, form name, and view name) are installed only for the languages currently activated in the organization. If you activate a new language in the future, the metadata will not be installed automatically for the newly activated language. To get the metadata translation for the newly activated language, you must import the metadata translation from the Power Apps portals admin center.

## To import metadata translation

> [!TIP]
> To learn about the roles required to perform this task, read [Admin roles required for portal administrative tasks](portal-admin-roles.md).

1.	Open [Power Apps portals admin center](admin-overview.md).

2.	Go to **Portal Actions** > **Get latest metadata translations**. A confirmation window is displayed asking whether to update the portal solutions.

3.	Select **Update**. The portal solutions will be updated with the latest metadata translation.

> [!Note]
> - If the latest version of a portal package is available, it isn't updated. The portal solutions are updated in the same version. To upgrade your portal solutions based on the latest available packages, you need to access the Solution Admin center.
> - If a user has modified any data in Microsoft Dataverse, the existing data will not be overwritten during the update.
> - If the portal solutions are being installed, the solution update cannot be triggered.


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]