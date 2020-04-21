---
title: Configure Regional Hospital Emergency Response app | Microsoft Docs
description: Provides provides detailed instructions for hospital IT admins to deploy and configure the sample app for their organization.
author: KumarVivek
manager: annbe
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 04/15/2020
ms.author: kvivek
ms.reviewer: kvivek
searchScope:
  - PowerApps
---
# Use the Regional Emergency Response Portal

## Overview

Hospital staff are challenged to meet an increase in number of patients while managing supply chain during emergency. By using the Regional Emergency Response portal, frontline workers can quickly view and add data for ventilators, staffing, pending discharges, and COVID-19 related patients.

## Portal at a glance

Browse to the Power Apps portal to work with staffing, equipment, supplies, patient and other areas. The following section walks you through what you can access, submit or update as the frontline user of the portal.

> [!div class="mx-imgBorder"]
> ![Portal at glance ](media/portal-user-at-glance.png)

You can use latest mobile devices and web browsers when using Regional Emergency Response portal except Apple iPad.

## Portal components

The Regional Emergency Response sample solution app consists of multiple apps for enhanced user experience.

- **Bed capacity**  
  Collect details regarding bed licenses, capacity, acuteness, staffed and surge data.

- **Staff**  
  Collect status of the RNs by location in that facility.

- **Equipment**  
  Collect equipment details such as ventilators, PAPR belts/chargers/hoods.

- **Supplies**  
  Collect key supplies to track, manage, and forecast inventory more effectively. ​

- **COVID-19 stats**  
  Collect status on how many patients are under investigation for COVID-19 and how many tested positive.

## Getting started with the portal

When you visit the portal, you have an option to log in, or for the first time, redeem an invitation:

> [!div class="mx-imgBorder"]
> ![Getting started](media/portal-user-getting-started.png)

### Redeem invitation

Select **Redeem invitation** if you received an email invitation with an invitation code:

> [!div class="mx-imgBorder"]
> ![Redeem invitation](media/portal-user-redeem-invitation.png)

You can select the checkbox *I have an existing account* if you are aware of your account already being present in the solution.

Select **Register** to start registration process and provide your details to save in your account.

### Sign in

If you already have email address and password available, enter your details and then select **Sign in**. You can save your credentials with **Remember me** check box if the device you use is not shared.

If you forget your password, you can use the **Forgot your password?** option to receive password reset email:

> [!div class="mx-imgBorder"]
> ![Sign in](media/portal-user-forgot-password.png)

After you sign in the portal, you’ll see **Hospital System, Region** and **Facility** selector before you can begin to submit data:

> [!div class="mx-imgBorder"]
> ![Manage your resources](media/portal-user-manage-your-resources.png)

Enter your choices before you proceed to the next step. You can use the search button to lookup records and search for your desired hospital, region or facility:

> [!div class="mx-imgBorder"]
> ![Lookup records](media/portal-user-lookup-records.png)

### Bed capacity

Select **Bed capacity** to update patient information, beds and staffing capacity for the selected location:

> [!div class="mx-imgBorder"]
> ![Bed capacity](media/portal-user-bed-capacity.png)

#### Options and description

| **Option name**                                               | **Description**                                                                       |
|---------------------------------------------------------------|---------------------------------------------------------------------------------------|
| How many licensed beds are currently in use in this facility? | Number of licensed beds currently in use at this facility.                            |
| Number of ICU Beds (AIIR Room) currently in use               | Number of ICU Beds (AIIR Room) currently in use.                                      |
| Number of ICU Beds (non-AIIR Room) currently in use           | Number of ICU Beds (non-AIIR Room) currently in use.                                  |
| Number of Acute Care Beds (AIIR Room) currently in use        | Number of Acute Care Beds (AIIR Room) currently in use.                               |
| Number of Acute Care Beds (non-AIIR Room) currently in use    | Number of Acute Care Beds (non-AIIR Room) currently in use.                           |
| Is your facility staffed to its full license bed capacity?    | Yes/No If the answer is No, you have the option to select all the reasons that apply: |
| Are you able to surge beyond your licensed beds?              | Yes/No If the answer is No, you have the option to select all the reasons that apply: |
| Number of surge beds currently in use                         | Number of surge beds currently in use.                                                |

- Staff

- Space

- PPE

- Equipment

- Low Patient Volume

- Staff

- Space

- PPE

- Equipment

- Low Patient Volume

### Staff

Submit staff specific details such as absenteeism, and registered nurse related details such as requested, assigned, unassigned and partners with **Staff**
form:

> [!div class="mx-imgBorder"]
> ![Staff details](media/portal-user-staff-details.png)

#### Options and description

| **Option name**                               | **Description**                                                                |
|-----------------------------------------------|--------------------------------------------------------------------------------|
| Percentage of essential care personnel absent | Absenteeism of essential care personnel in percentage format.                  |
| **Registered nurses on duty**                 |                                                                                |
| *Partners*                                    | Number of Registered Nurse partners present at the selected location.          |
| *Requested*                                   | Number of Registered Nurses requested for the selected location.               |
| *Assigned*                                    | Number of Registered Nurses assigned to the selected location.                 |
| *Unassigned*                                  | Number of Registered Nurses not assigned to any task at the selected location. |

### Equipment

Submit the equipment details such as ventilators, PAPR belts/chargers/hoods:

> [!div class="mx-imgBorder"]
> ![Equipment details](media/portal-user-equipment-details.png)

#### Options and description

| **Option name** | **Description**                 |
|-----------------|---------------------------------|
| Ventilators     | Number of ventilators in use.   |
| NIPPV           | Number of NIPPV devices in use. |
| PAPR belts      | Number of PAPR belts in use.    |
| PAPR chargers   | Number of PAPR chargers in use. |
| PAPR hoods      | Number of PAPR hoods in use.    |

### Supplies

Submit the supplies inventory in stock and used in last 24 hours:

> [!div class="mx-imgBorder"]
> ![Supplies details](media/portal-user-supplies-details.png)

#### Options and description

The supplies app items list may be different depending on your organization requirements. Refer to your organization resources for descriptions of supply
names.

> [!NOTE]
> The supply inventory item values must be in number format. The supply number is for **individual component**. For example, N-95 masks are counted by each individual mask instead of counting the number of boxes containing masks.

### COVID-19 stats

Submit COVID-19 specific details using the **COVID-19 stats** form:

> [!div class="mx-imgBorder"]
> ![Stats](media/portal-user-stats.png)

#### Options and description

| **Option name**                                                   | **Description**                                                    |
|-------------------------------------------------------------------|--------------------------------------------------------------------|
| Number of patients under investigation (PUIs)                     | Number of patients under investigation.                            |
| Number of patients with confirmed COVID-19                        | Number of patients with confirmed COVID-19.                        |
| Number of intubated patients                                      | Number of patients intubated.                                      |
| Number of patients with COVID-19 discharged in the prior 24 hours | Number of patients with COVID-19 discharged in the prior 24 hours. |

## Other portal options

Explain any other options, including end of shift/sign out, feedback, switch facility or any new.

### Submit form

After you submit any form, you’ll receive an acknowledgement for the submission and have an option to either go to the home page, or submit another record for the selected component:

> [!div class="mx-imgBorder"]
> ![Submit form](media/portal-user-submit-form.png)

### Sign out

You can sign out from the app using the profile icon on the upper-right side of the screen.  

> [!div class="mx-imgBorder"]
> ![Sign Out](media/portal-user-signout.png)

> [!NOTE]
> Sign-out may not be available if your IT administrator has disabled device sharing.

### Switch facility

Switch facility anytime by selecting the facility name on the top-right side of the screen.

> [!div class="mx-imgBorder"]
> ![Switch facility](media/portal-user-switch-facility.png)

If you use a mobile device, use the top right button and then select the name of the facility to switch:

> [!div class="mx-imgBorder"]
> ![Switch facility mobile](media/portal-user-switch-facility-mobile.png)

### Navigation

From any page, you can always go back to the home page by selecting the state department on top left of the screen:

> [!div class="mx-imgBorder"]
> ![Navigation](media/portal-user-navigation.png)

You can also go back to the previous page, such as to **Bed Capacity** in the
following example with link to **Bed Capacity:**

> [!div class="mx-imgBorder"]
> ![Navigation](media/portal-user-bed-capacity-navigation.png)

