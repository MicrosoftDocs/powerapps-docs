---
title: Use the Employee Return to the Workplace app
description: Provides information for employees to track their symptoms and determine whether they're eligible to enter into a facility.
author: wbakker
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 08/25/2020
ms.author: garybird
ms.reviewer: kvivek
---

# Use the Employee Return to the Workplace app

This article provides step-by-step instructions about how to use the Employee Return to the Workplace app. You can check in, answer questions to determine whether you're eligible to enter a facility, and say how you feel about returning to the workplace.

## Prerequisites

- Open [Power Apps](https://make.powerapps.com) in a web browser or download [Power Apps Mobile](https://powerapps.microsoft.com/downloads):

  - For Apple devices with iOS, such as iPhone and iPad, use the [App Store](https://aka.ms/powerappsios).

  - For Android devices, use [Google Play](https://aka.ms/powerappsandroid).

- Ensure that your organization has deployed and configured the Employee Return to the Workplace app, as described in [Deploy the solution](deploy.md).

## Getting started with the app

Open the app from your device and sign in with your company's Azure Active Directory account. You can view all apps shared with you by your organization after you sign in. More information: [Power Apps mobile device sign in](https://docs.microsoft.com/powerapps/user/run-app-client#open-power-apps-and-sign-in), [Power Apps web browser sign in](https://docs.microsoft.com/powerapps/user/run-app-browser)

When you successfully sign in and open the **Return to the Workplace** app, you can get a day pass, look up facility status, or answer the employee sentiment question.

> [!div class="mx-imgBorder"]
> ![Welcome screen](media/employee-welcome2.png "Welcome screen")

## See the reopen status of a facility

You can find all available facilities and see the reopen status for them. Select **Look Up Status** to look for facilities and view details such as whether the facility is open and what phase of reopening it's in.

> [!div class="mx-imgBorder"]
> ![List of facilities](media/employee-facility-list2.png "List of facilities")

When you select a facility from the facility list, the current status of the facility and associated details are displayed. You can also book a space directly from the look up screen. When a facility isn't available, then the **BOOK A SPACE** button is disabled. Select **< Back** to return to the previous screen.

> [!div class="mx-imgBorder"]
> ![Facility details](media/employee-facility-details2.png "Facility details")

## Check in to a facility

After you complete the steps to select a particular facility that's open to employees returning to work, you can complete a health survey that determines whether you're eligible to check in to that facility. 

If you're eligible, you'll be given a pass to your selected building for that day. 

**To check in to a facility**

1. Select **GET DAY PASS**.

2. Select an available facility from the facility list or use the saved facility and area shortcut if applicable. In **Recent** you will find the facilities you most recently used. For saved facilities and recent facilities, it indicates if the facility is available based on their phase and the earlier bookings. When a facility is unavailable, it will be greyed out and unavailable for booking.

3. Select **BOOK A SPACE** to continue with the check-in process.

   > [!div class="mx-imgBorder"]
   > ![Select Facility](media/employee-select-facility.png "Select facility")

4. Select an available area within that facility. Select **See All Available** option to show the available areas. Select **Save as default for future check ins** to save the area to reuse on future check ins. Select **NEXT** to continue with the check-in process.

   > [!div class="mx-imgBorder"]
   > ![Select Area](media/employee-select-area.png "Select area")
   
> [!NOTE]
> When a facility doesn't have any areas, this screen will be skipped for an user. The pass will then only be for that facility.

5. Select time window for arrival at the facility. Select **NEXT** to continue with the check-in process.

   > [!div class="mx-imgBorder"]
   > ![Select Time](media/employee-select-time.png "Select time")

> [!NOTE]
> On a facility you can indicate a time window in which people can check in, it is possible to select 30 minutes, 1 hour or none. When the time window is not filled or none, this screen will be skipped.

6. Accept the terms and agreements.

    > [!div class="mx-imgBorder"]
    > ![Terms and agreements](media/employee-termandagreement.png "Terms and agreements")

7. Review the list of symptom check statements. Select **I AGREE**  if you agree with the statements, and **CANCEL** if you don't.

   > [!div class="mx-imgBorder"]
   > ![Symptom check](media/employee-agreement.png "Symptom check")

### Employee pass

If your responses to the symptom check statements show that you're healthy, you'll receive a pass to enter the selected facility. The pass is valid until the end of the day. When you create a pass for a facility were you already created a pass for earlier that day, the pass earlier that day will be cancelled automatically. 

> [!NOTE]
> In the solution settings an administrator can disable the use of QR codes. This applies to both Employee and Guest passes.

If the administrator enabled QR codes in the solution settings, a QR code will be displayed on the pass (default). If you click the QR code, it will expand for easy scanning.

> [!div class="mx-imgBorder"]
> ![Employee pass](media/employee-pass.png "Employee pass")

To cancel your pass, select the **CANCEL PASS** button. Select **YES, CANCEL** to proceed with canceling the pass or **NO** to keep the pass.

> [!div class="mx-imgBorder"]
> ![Employee cancel pass](media/employee-cancel-pass.png "Employee cancel pass")

If your responses show you aren't healthy, you'll not receive a pass and provided with contact information for the company health and safety department if you need.

> [!div class="mx-imgBorder"]
> ![Not feeling well](media/employee-pass-negative.png "Not feeling well")

> [!NOTE]
> Current negative attestations are also stored, in the solution settings you can turn this feature off if you are not allowed to store them.

## Create guest pass

After an employee created a pass, guest registration becomes available. If the employee does not have a pass, then the option is greyed out. An employee can create multiple guest passes.

> [!NOTE]
> In the solution settings an administrator can disable the use of guest registrations. This will remove the option from the screen.

To create a guest pass, follow these steps:

1. Create a pass for yourself as described above
2. Select **Register a guest**
3. If a user entered a guest before, it will show up to five recent names. Select one of the recent guests or enter new guest details. First name, last name and email address are required fields. Click **Next**
4. This screen shows configured information and privacy discloses and the health requirements and instructions for guests. Both fields can be expanded with the **+**-sign. Click **Next** to continue.
5. This screen shows the guest pass.

Guest passes are available from the home screen under the **Pass** button on top of the screen. They are showed next to the employee pass. This screen can also be used to share guest passes.

### Email Guest Pass

When a guest pass is created, you can share this with the guest by mail by clicking on **Share Pass**. This will send the guest an email with the host name, the facility, date and hour of the reservation and QR code. 

> [!div class="mx-imgBorder"]
> ![Share sentiment](media/employee-share-pass-email.png "Share pass guest")

## Share sentiment

You can say how you're feeling about returning to the workplace. On the home page, select one of the options to answer the question **Do you feel safe returning to work?**

> [!div class="mx-imgBorder"]
> ![Share sentiment](media/employee-share-sentiment2.png "Share sentiment")

 This option will reset itself after you reopen the app.

> [!div class="mx-imgBorder"]
> ![Share sentiment reset](media/employee-share-sentiment2-2.png "Share sentiment reset")

> [!NOTE]
> In the solution settings you can turn this feature off if you don't want to use this.

## Facility access not available

It can happen that a case manager indicates that facility access is no longer available for you. You will see a banner appearing, which indicates the **Facility access is not available**. When clicking the banner, a message is shown with further instructions. 

> [!div class="mx-imgBorder"]
> ![Facility access is not available](media/facility-access-not-available.png "Facility access is not available")

## Feedback about the solution

To provide feedback about the Return to the Workplace solution, visit <https://aka.ms/rtw-community>.
