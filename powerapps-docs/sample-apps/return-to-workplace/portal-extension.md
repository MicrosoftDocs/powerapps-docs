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

# Return to the Workplace Guest Portal

A separate offering extends the Return to the Workplace solution with a portal. This portal allows people outside your organization to get a pass by completing a health attestation. The portal has been designed to provide a mobile experience for users but will scale to tablet and desktop screens as well. This enables users to access the portal from a device of their choosing.

> [!div class="mx-imgBorder"]
> ![Portal welcome page](media/portals-welcome-screen.png "Portal welcome screen")

> [!div class="mx-imgBorder"]
> ![Portal Attestation](media/portals-home-welcome.png "Portal Home")


## Configuration

There are solution settings that can be changed to alter the portals behavior: 

- Allow self registration
- Allow unauthenticated users to self-screen
- Allow authenticated users to add guests or create passes for guests/dependents.

Please see [Configure the solution](configure.md#set-solution-settings) for more details.

## Getting started with the portal

The portal provides two ways for end users to self-screen.

1) Unauthenticated. This mode allows users to complete a guest attestation that has been sent to them through email. Users can also create new guest attestations in order to get a pass for a facility. This mode is most relevant for infrequent visitors as it allows users to get a pass without creating an account.

2) Authenticated. Guests can be invited to the portal and are prompted to create an account. There they can create passes for themselves as well as their guests or dependents. This mode is most relevant to frequenst visitors, suppliers/vendors or schools, where a guardian creates a pass for a dependent.

These two modes are explained in greater detail below.

### Unauthenticated access to the portal

When you open the portal the **Get Started** screen is displayed. Click on the **Get Started** button to continue.

In the unauthenticated mode the users are directed to the **terms and conditions** page. User must accept the terms and conditions by checking the box and selecting the **Accept** button. 

On the next screen, the user provides contact details. After this a facility can be selected.

At this point the visitor can self-screen and attest to the company policies.

At the end of this process, a pass is shown and can be e-mailed if needed.


### Authenticated access to the portal

The portal provides guests with the ability to attest to company health policies. If a user is not signed in, they are given the options to sign in, register an account, or redeem an invitation.

 > [!NOTE]
 > Please see [Overview of authentication in Power Apps portals](https://docs.microsoft.com/powerapps/maker/portals/configure/configure-portal-authentication) for more information

In the case where a guest has been invited to make use of the portal and has an invitation code, the process is as follows:

1. Guests are invited to use the portal through email.
2. They use the link in the e-mail to redeem the invitation and create a login.
3. The guest selects Accept on the Daily Health Check.
4. The guest selects Agree on the Health Terms and Agreements.
5. They can now View their pass. 

While logged in to the portal, the guest can do the following things:

- Create a pass
- View existing passes
- View resources
- Update their profile

The first two options are directly available from the homescreen. The second two are available in the hamburger menu located on the top left or the navigation bar on devices with larger screens. Next to those, the hamburger menu provides a link **home** to the home screen and a link **sign out** to sign out.

#### Home

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


#### Creating a pass

1. The guest is logged in to the portal and selects **create a pass** from the home screen.
2. Select the person to create the pass for. This can be either the user or a guest/dependent..
3. The guest selects the facility.

> [!div class="mx-imgBorder"]
> ![Portal Attestation](media/portals-facility.png "Portal facility")

4. The guest accepts the disclaimer.

> [!div class="mx-imgBorder"]
> ![Portal Attestation](media/portals-disclaimer.png "Portal disclaimer")

5. The guest attests to not having symptoms.

> [!div class="mx-imgBorder"]
> ![Portal Attestation](media/portals-attestation.png "Portal attestation")

6. A pass is created for the guest/dependent for that day.

> [!div class="mx-imgBorder"]
> ![Portal Attestation](media/portals-own-pass.png "Portal Pass")

> [!NOTE]
> An administrator can disable the storing of negative attestations in the solution settings. This will stop a negative attestation from being created and wont save the record.

#### View existing passes

If a pass has been created for a guest or one of their dependents, they will be shown here. If no pass exists, the button will be disabled on the home screen and in the hamburger menu. 

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

When **Cancel Pass** is selected, the portal asks for confirmation. When a pass is cancelled it will no longer show up in the view pass screen and the attestation will be deactivated. The record will still exist in the system.

> [!div class="mx-imgBorder"]
> ![Portal Attestation](media/portals-cancel-pass.png "Portal Pass")

> [!NOTE]
> An administrator can disable the use of QR codes in the solution settings. This applies to both employee and guest passes.

#### View resources

The resources page displays general information from your organisation to the portal user.

> [!NOTE]
> An administrator can configure this information in the solution settings, therefore the information displayed depends on the default facility and facility group associated with that facility.

#### Update profile

On the profile page, guests can perform basic operations. They can update their personal information, change their password or change their login method.

> [!div class="mx-imgBorder"]
> ![Portal Attestation](media/portals-profile.png "Portal Profile")

> [!NOTE]
> The options presented to **Manage external authorization** depend on the authentication methods configured by the system administrator.

## Inviting users to the portal

This section descibes the way guests can start interacting with the portal

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

In the background, and invite will be created and an e-mail will be sent to the email address of the contact. The email contains a personal link that allows the contact to redeem the invitation and create a login that will be linked to the contact.

In the Workplace care management app, steps 1 and 2 must be skipped. The **Employees** section is directly available from the side menu.

## Creating Dependents for Guests

In case there is the need to create a pass for a dependent, go to **Home** and select **Register Guest or Dependent**. Contact details must first be filled in for all dependents:

Mandatory fields: 

1. First Name 
2. Last Name
3. Email 

Non-mandatory fields:

4. Phone Number
5. Organization 

> [!div class="mx-imgBorder"]
> ![Portal Register Guest or dependent](media/portals-register-dependent.png "Portal Register Guest or dependent")


After creating dependents, a user will be able to see them listed by clicking the **Create Pass** option. This is where a user selects who to create the pass for.

> [!div class="mx-imgBorder"]
> ![Portal Register Guest or dependent](media/portals-select-dependent.png "Portal Register Guest or dependent")

To find dependents in the Facility Safety Management App, go to **Soluttion Setup** and click on **Employees**. On the **My Active Contacts** view, open a record and find dependents on the Guest section. All of the dependents can be found on the **Active Guests** view.


## Extend the portal

The portal is highly customizable. For more information, check out the resources below.

Details about the data model specific to the portal solution have been added to the [Extend the Return to the Workplace solution](extend.md) page.

To learn more about working, administrating or extending Power Apps portals, go to:

- [Power Apps portals documentation](https://docs.microsoft.com/powerapps/maker/portals/)
