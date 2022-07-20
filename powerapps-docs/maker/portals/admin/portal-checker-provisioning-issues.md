---
title: Provisioning issues
description: Learn about Portal Checker diagnostics results for provisioning issues.
author: neerajnandwana-msft

ms.topic: conceptual
ms.custom: 
ms.date: 07/18/2022
ms.subservice: portals
ms.author: nenandw
ms.reviewer: ndoelman
contributors:
    - neerajnandwana-msft
    - nickdoelman
    - dileepsinghmicrosoft
    - ProfessorKendrick
---

# Provisioning issues

In this article, you'll learn about Portal Checker diagnostics results for portal provisioning issues.

## Profile form isn't available for contact table

The profile page is one of the common pages used in your portal for all profile-related issues. This page shows a form that can be used by users to update their profiles. The form used on this page comes from the **Profile Web Page** main form available in the Contact table. This form is created in your Dataverse environment when the portal is provisioned. This error is displayed when the **Profile** form is either deleted or disabled in your portal. This form is mandatory and deleting or disabling this form can break the whole website, displaying a runtime error on your portal. This is an irreparable state and requires the portal to be reinstalled in the environment.

### See also

[Run Portal Checker](portal-checker.md)


