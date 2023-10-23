---
title: Create additional sites in an environment
description: Instructions to create additional portals in an environment.
author: neerajnandwana-msft
ms.topic: conceptual
ms.custom: 
ms.date: 09/06/2023
ms.subservice: portals
ms.author: nenandw
ms.reviewer: ndoelman
contributors:
    - neerajnandwana-msft
    - nickdoelman
    - ProfessorKendrick
    - sampatn
---

# Create additional sites in an environment

[!INCLUDE[cc-pages-banner](../../includes/cc-pages-banner.md)]

The template you choose for the new site determines your ability to create additional sites. The following table explains the limits for creating additional portals in an environment.

| Environment type | Template | Limit | Additional information |
| - | - | - | - |
| [Environment with Dataverse](/power-pages/templates/) | Starter layout templates, Solution templates | 50 sites\* | No limits for language. Each portal can have one or more languages enabled. \*\*\* |
| [Environment with Dataverse](/power-pages/templates/blank)| Blank page templates | 50 sites\* | No limits for language. Each portal can have one or more languages enabled. \*\*\* |
| [Environment with Dynamics 365 apps](/power-pages/templates/dynamics-365-apps/overview) | Community, Customer self-service, Employee self-service portals | 50 sites\*\* | No limits for language. Each site can have one or more languages enabled. \*\*\*
| [Environment with Dynamics 365 apps](/power-pages/templates/dynamics-365-apps/overview) | Partner portal, [Modern Community](/dynamics365/customer-service/community-get-started), Field Service customer, Order Returns, [Customer portal for Dynamics 365 Supply Chain Management](/dynamics365/supply-chain/sales-marketing/customer-portal-overview) | one site for each template | Limit of one site template, but additional languages for each template can be enabled. \*\*\* |

\* Requires Starter portal package version [9.3.2109.x or later](release-updates.md#starter-portal-package-updates)

\*\* Requires Starter portal package version [9.3.2201.0 or later](release-updates.md#starter-portal-package-updates)

\*\*\* Additional languages can be enabled for individual sites, even if only one site type per environment is allowed. For more information about enabling additional languages for sites, go to [Enable multiple language support](./configure/enable-multiple-language-support.md).

To enable multiple [Modern Community](/dynamics365/customer-service/community-get-started) sites, see [Create new websites in Community](/dynamics365/customer-service/community-create-websites).

Once you've reached the maximum number of a specific site type for an environment, you'll see a message displayed indicating that the maximum number of sites has been reached.

To create a new environment, see [Create new environment](/power-platform/admin/create-environment)

### See also

[Administer Power Apps portals](/training/paths/administer-portals/) <br />

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
