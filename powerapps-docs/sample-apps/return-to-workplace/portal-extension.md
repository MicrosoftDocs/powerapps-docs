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

# Return to the Workplace Guest Portals

A seperate offering extends the Return to the Workplace solution with a portal. Allowing people external to your organization to get a pass by performing attestations. The portal has been designed to provide a mobile experience for the end user, but it will scale to tablet or desktop screen sizes also. This enables end users to use the portal from their own device.

> [!div class="mx-imgBorder"]
> ![Portal welcome page](media/portals-welcome-screen.png "Portal welcome screen")

> [!div class="mx-imgBorder"]
> ![Portal Attestation](media/portals-home-welcome.png "Portal Home")

## Prerequisites


## Installation


## Getting started with the portal

**Get Started** screen is displayed and click on Get Started button to continue.

Before starting on the portal and as a first time guest, it will ask you to accept the **Terms and Conditions**. Click on the check box and the **Accept** button will enable. 

The portal provides guests with the ability to attest to the health policies. If a user is not signed in, the portal displays the configured methods for signing in, creating an account or redeeming an invitation.

In case a guest has been invited to make use of the portal, the proces is as follows:

1. A guest is invited to use the portal.
2. The guest received an e-mail with the invite.
3. The guest uses the link in the e-mail to redeem the invite and create a login.
4. Accept on the Daily Health Check
5. Agree with the Health and Agreements
6. View the Pass. 

While logged in to the portal, the guest can do the following things:

- Create a pass.
- View existing passes.
- View resources
- Update their profile

The first two options are directly available from the homescreen. The second two are available from the top left hamburger menu. Next to those, the hamburger menu provides a link **home** to the home screen and a link **sign out** to sign out.

### Home

On the home screen you have several options:

- Hamburger menu thats displays
    - Home
    - Resources 
    - Profiles 
    - Sign Out option

> [!div class="mx-imgBorder"]
> ![Portal Attestation](media/portals-hamburguer-menu.png "Portal Hamburguer Menu")

- Create Pass 
- View Pass 
- Register Guest or Dependent

> [!div class="mx-imgBorder"]
> ![Portal Attestation](media/portals-home-welcome.png "Portal Home")


### Creating a pass

1. The guest is logged in to the portal and selects **create a pass** from the home screen.
2. The guest selects the facility.

> [!div class="mx-imgBorder"]
> ![Portal Attestation](media/portals-facility.png "Portal facility")

3. The guest accepts the disclaimer.

> [!div class="mx-imgBorder"]
> ![Portal Attestation](media/portals-disclaimer.png "Portal disclaimer")

4. The guest attests not having symptoms.

> [!div class="mx-imgBorder"]
> ![Portal Attestation](media/portals-attestation.png "Portal attestation")

5. A pass is created for the guest for that day.


> [!NOTE]
> An administrator can disable the store of negative attestations in the solution settings. This will stop a negative attestation of being created and wont save the record.

### View existing passes

If a pass has been created for a guest it will be shown here. If no pass exists, the button will be disabled on the home screen and in the hamburger menu. 

> [!div class="mx-imgBorder"]
> ![Portal Attestation](media/portals-view-pass.png "Portal View Pass")

The pass will display:

1. Name of the guest
2. Pass Date
3. Employee Contact
4. Facility
5. Parent Organizacion 
6. QR code
7. Cancel button

> [!div class="mx-imgBorder"]
> ![Portal Attestation](media/portals-pass.png "Portal Pass")

When a pass is cancel, the portal asks you if you are sure. If you cancel the pass, this wont show up in the view pass anymore and the attestation will deactivate but still will be recorded. 

> [!div class="mx-imgBorder"]
> ![Portal Attestation](media/portals-cancel-pass.png "Portal Pass")

> [!NOTE]
> An administrator can disable the use of QR codes in the solution settings. This applies to both employee and guest passes.

### View resources

The resources page displays general information of your organisation to the user of the portal.

> [!NOTE]
> An administrator can configure this information in the solution settings, therefor the actual information displayed depends on the default facility and the facility group associated to that facility.

### Update profile

On the profile page, guests can perform basic operations. They can update their personal information, change their password or change their login method.

> [!div class="mx-imgBorder"]
> ![Portal Attestation](media/portals-profile.png "Portal Profile")

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

## Creating Dependents for Guests

In case there is the need to create a pass for dependents, go to **Home** and select **Register Gest or Dependent**. For each of the dependents first you need to fill the contact details:

Mandatory fields: 

1. First Name 
2. Last Name
3. Email 

Not mandatory fields:

4. Phone Number
5. Organization 

> [!div class="mx-imgBorder"]
> ![Portal Register Guest or dependent](media/portals-register-dependent.png "Portal Register Guest or dependent")


After creating dependents you would be able to see them when clicking **Create Pass** option to select who to create a pass for.

> [!div class="mx-imgBorder"]
> ![Portal Register Guest or dependent](media/portals-select-dependent.png "Portal Register Guest or dependent")

To find dependents in the Facility Safety Management App, go to **Soluttion Setup** and click on **Employees**. On **My Active Contacts** view, open a record and find dependents on the Guest section. Also, find all of the dependents on the **Active Guests** view.


## Extend the portal

The portal can be highly customized. See below resources for more information.

Details about the data model specific to the portal solution have been added to the [Extend the Return to the Workplace solution](extend.md) page.

To learn more about working, administrating or extending Power Apps portals, go to:

- [Power Apps portals documentation](https://docs.microsoft.com/powerapps/maker/portals/)
