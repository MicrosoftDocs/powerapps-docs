---
title: "Import metadata translation | MicrosoftDocs"
description: "Instructions to import metadata translation."
author: tapanm-msft
manager: kumarvivek
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 10/21/2019
ms.author: tapanm
ms.reviewer:
---

# Import metadata translation

When you provision a portal, the portal-related solutions are installed on the organization. During the installation of solutions, the solution metadata translations (for example, field name, form name, and view name) are installed only for the languages currently activated in the organization. If you activate a new language in the future, the metadata will not be installed automatically for the newly activated language. To get the metadata translation for the newly activated language, you must import the metadata translation from the Power Apps Portals admin center.

## To import metadata translation

1.	Open [Power Apps Portals admin center](admin-overview.md).

2.	Go to **Portal Actions** > **Get latest metadata translations**. A confirmation window is displayed asking whether to update the portal solutions.

3.	Select **Update**. The portal solutions will be updated with the latest metadata translation.

> [!Note]
> - If the latest version of a portal package is available, it isn't updated. The portal solutions are updated in the same version. To upgrade your portal solutions based on the latest available packages, you need to access the Solution Admin center.
> - If a user has modified any data in Common Data Service, the existing data will not be overwritten during the update.
> - If the portal solutions are being installed, the solution update cannot be triggered.