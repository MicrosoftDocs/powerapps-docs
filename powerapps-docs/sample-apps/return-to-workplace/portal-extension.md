---
title: Portal extention to the Return to the Workplace solution for Microsoft Power Platform | Microsoft Docs
description: Provides an overview of the portal extention for Return to the Workplace solution.
author: wbakker
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 11/03/2020
ms.author: garybird
ms.reviewer: kvivek
---

# Portal extention

A seperate offering extends the Return to the Workplace solution with a portal. Allowing people external to your organization to perform attestations.


## Prerequisites


## Installation


## Getting started with the portal

The portal provides guests with the ability to attest to the health policies. If a user is not signed in, the portal displays the configured methods for signing in, creating an account or redeeming an invitation.

In case a guest has been invited to make use of the portal, the proces is as follows:

1. A guest is invited to use the portal.
2. The guest received an e-mail with the invite.
3. The guest uses the link in the e-mail to redeem the invite and create a login.

While logged in to the portal, the guest can do the following things:

- Create a pass.
- View existing passes.
- View resources
- Update their profile

The first two options are directly available from the homescreen. The second two are available from the top left hamburger menu. Next to those, the hamburger menu provides a link **home** to the home screen and a link **sign out** to sign out.

### Creating a pass

1. The guest is logged in to the portal and can select **create a pass** from the main screen.
2. The guest selects the facility
3. The guest takes the daily health check
4. A pass is created for the guest for that day

### View existing passes

If a pass has been created for a guest it will be shown here. If no pass exists, the button will be disabled on the home screen and in the hamburger menu. The pass is displayed with all information, a QR code and a cancel button. If the guest does not have a pass, the link to this page is disabled.

> [!NOTE]
> An administrator can disable the use of QR codes in the solution settings. This applies to both employee and guest passes.

### View resources

The resources page displays general information of your organisation to the user of the portal.

> [!NOTE]
> An administrator can configure this information in the solution settings, therefor the actual information displayed depends on the default facility and the facility group associated to that facility.

### Update profile

On the profile page, guests can perform basic operations. They can update their personal information, change their password or change their login method.

> [!NOTE]
> The options presented to **Manage external authorization** depend on the authentication methods configured by the system administrator.

## Inviting users to the portal

This section descibes the way guest can start interacting with the portal

### Sending invites to contacts

In the facility management app and the workplace care management app, the facility manager or the health and safety leader can invite contacts to the portal.

Follow these steps:

1. Open the **Facility management app**
2. Open the **Solution Setup** area
3. Open the **Employees** section
4. Search for or select the contact you would like to invite
5. Verify that the e-mail adress is correct
6. Set the field **Requires portal access** to **yes**
7. **Save** the record.

In the background, and invite will be created and an e-mail will be send to the email adress of the contact. The email contains a personal link that allows the contact to redeem the invite and create an login that will be linked to the contact.

In the Workplace care management app, step 1 and 2 must be skipped. The **Employees** section is directly available from the side menu.

## Extend the portal

The portal can be highly customized. See below resources for more information.

Details about the data model specific to the portal solution have been added to the [Extend the Return to the Workplace solution](extend.md) page.

To learn more about working, administrating or extending Power Apps portals, go to:

- [Power Apps portals documentation](https://docs.microsoft.com/en-us/powerapps/maker/portals/)
