---
title: Use the Employee Return to the Workplace app
description: Provides information for employees to track their symptoms and determine whether they're eligible to enter into a facility.
author: wbakker
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 07/21/2020
ms.author: garybird
ms.reviewer: kvivek
---

# Use the Employee Return to the Workplace app

This article provides step-by-step instructions about how to use the Employee Return to the Workplace app. You can check in, answer questions to determine whether you're eligible to enter a facility, and say how you feel about returning to the workplace.

## Prerequisites

- Open PowerApps in a [web browser](https://make.powerapps.com) or Download [Power Apps Mobile](https://powerapps.microsoft.com/downloads):

  - For Apple devices with iOS, such as iPhone and iPad, use the [App Store](https://aka.ms/powerappsios).

  - For Android devices, use [Google Play](https://aka.ms/powerappsandroid).

- Ensure that your organization has deployed and configured the Employee Return to the Workplace app, as described in [Deploy the solution](deploy.md).

## Getting started with the app

Open the app from your device and sign in with your company's Azure Active Directory account. You can view all apps shared with you by your organization after you sign in. More information: [Power Apps mobile device sign in](https://docs.microsoft.com/powerapps/user/run-app-client#open-power-apps-and-sign-in), [Powerapps web browser sign in](https://docs.microsoft.com/en-us/powerapps/user/run-app-browser)

When you successfully sign in and open the **Return to the Workplace** app, you can get a day pass, look up facility status, or answer the employee sentiment question.

> [!div class="mx-imgBorder"]
> ![Welcome screen](media/employee-welcome2.png "Welcome screen")

## See the reopen status of a facility

You can find all available facilities and see the reopen status for them. Select **Look Up Status** to look for facilities and view details such as whether the facility is open and what phase of reopening it's in.

When you select a facility from the facility list, the current status of the facility and associated details are displayed. Select **<** to return to the previous screen.

> [!div class="mx-imgBorder"]
> ![List of facilities](media/employee-facility-list2.png "List of facilities")

> [!div class="mx-imgBorder"]
> ![Facility details](media/employee-facility-details2.png "Facility details")

## Check in to a facility

After you complete the steps to select a particular facility that's open to employees returning to work, you can complete a health survey that determines whether you're eligible to check in to that facility. 

If you're eligible, you'll be given a pass to your selected building for that day. 

**To check in to a facility**

1. Select **GET DAY PASS**.

2. Select an available facility from the facility list or use the saved facility and area shortcut if applicable.

3. Select **Book a Space** to continue with the check-in process.

   > [!div class="mx-imgBorder"]
   > ![Select Facility](media/employee-select-facility.png "Select facility")

4. Select an available area within that facility. Select **Next** to continue with the check-in process.

   > [!div class="mx-imgBorder"]
   > ![Select Area](media/employee-select-area.png "Select area")

5. Select time window for arrival at the facility. Select **Next** to continue with the check-in process.

   > [!div class="mx-imgBorder"]
   > ![Select Time](media/employee-select-time.png "Select time")

6. Accept the terms and agreements.

    > [!div class="mx-imgBorder"]
    > ![Terms and agreements](media/employee-termandagreement.png "Terms and agreements")

7. Review the **Symptom Check** statements. Select **I Agree**  if you agree with the statements, and **I Disagree** if you don't.

   > [!div class="mx-imgBorder"]
   > ![Symptom check](media/employee-agreement.png "Symptom check")

### Employee pass

If your responses to the symptom check statements show that you're healthy, you'll receive a pass to enter the selected facility. The pass is valid until the end of the day. 

> [!div class="mx-imgBorder"]
> ![Employee pass](media/employee-pass.png "Employee pass")

To cancel your pass, select the **Cancel** button. Select **Yes, Cancel** to proceed with cancelling the pass or **No** to keep the pass.

> [!div class="mx-imgBorder"]
> ![Employee cancel pass](media/employee-cancel-pass.png "Employee cancel pass")

If your responses show you aren't healthy, you won't receive a pass and you'll be given contact information for the company health and safety department to use if you need.

> [!div class="mx-imgBorder"]
> ![Not feeling well](media/employee-pass-negative.png "Not feeling well")

## Share sentiment

You can say how you're feeling about returning to the workplace. On the home page, select one of the options to answer the question **Do you feel safe returning to work?**

> [!div class="mx-imgBorder"]
> ![Share sentiment](media/employee-share-sentiment2.png "Share sentiment")

 This option will reset itself after you reopen the app.

> [!div class="mx-imgBorder"]
> ![Share sentiment](media/employee-share-sentiment2-2.png "Share sentiment")

## Feedback about the solution

To provide feedback about the Return to the Workplace solution, visit <https://aka.ms/rtw-community>.