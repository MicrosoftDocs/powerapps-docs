---
title: Use the Return to the Workplace employee app
description: Provides information to track symptoms of the employees and determine if they are eligible to enter into a facility.
author: wbakker
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 07/06/2020
ms.author: garybird
ms.reviewer: kvivek
---

# Use the employee return to the workplace app

This article provides step-by-step instructions to employees on how to use the employee app. Employees can check-in, answer the questions to determine whether they are eligible to enter into a facility, and respond to how they feel about returning to the workplace.

## Prerequisites

To get started with the employee app, you need to download the Power Apps Mobile on your device using the device's app store.

- Download the [Power Apps Mobile](https://powerapps.microsoft.com/downloads)

  - For **Apple** devices with iOS such as iPhone and iPad, use [App store](https://aka.ms/powerappsios)

  - For **Android** devices, use [Google Play](https://aka.ms/powerappsandroid)

- Ensure your organization has deployed and configured the Return to the Workplace employee app as explained in [Deploy the app](https://docs.microsoft.com/powerapps/sample-apps/return-to-the-workplace/deploy).

## Getting started with the app

Open the app from your device and sign in with your company's Azure Active Directory account. You can view all apps shared with you by your organization once
you sign in. More information: [Power Apps mobile device sign in](https://docs.microsoft.com/powerapps/user/run-app-client#open-power-apps-and-sign-in).

When you successfully sign in and launch the **Return to the Workplace** app from your mobile device you have an option to get day pass, look up facility status, or answer the employee sentiment question:

> [!div class="mx-imgBorder"]
> ![Welcome screen](media/employee-welcome2.png "Welcome screen")

## See the reopen status of a facility

You can see the reopen status for a facility, you can find all the available facilities.

Select **Look Up Status** to lookup for facilities and view the details such as whether the facility is open and what phase of reopening it is in.

Select a facility from the facility list and the current status of the facility and associated details are displayed. Select **Top Arrow** to return to the home screen.

> [!div class="mx-imgBorder"]
> ![List of facilities](media/employee-facility-list2.png "List of facilities")

> [!div class="mx-imgBorder"]
> ![Facility details](media/employee-facility-details2.png "Facility details")


## Check in to a facility

Employees can complete the steps required to select a particular facility that is `open` to employees returning to work. Employees can find a facility and then complete a health survey that determines if they are eligible to check in to the facility they have selected. If eligible the employee will be provided with a pass to their selected building for that day. To check in to a facility:

1. Select **Facility**.

2. Select an available facility form the facility list.

3. Select **Start Health Survey** to complete the check-in process. Accept the terms & agreements.

   > [!div class="mx-imgBorder"]
   > ![Start survey](media/employee-start-survey2.png "Start survey")

    > [!div class="mx-imgBorder"]
   > ![Term and agreements](media/employee-termandagreement.png "Term and Agreements")


### Symptom check 

Review the **Symptom Check** statements. Select **I Agree**  if you agree with the statements and **I Disagree** if you don't.

> [!div class="mx-imgBorder"]
> ![Symptom check](media/employee-agreement.png "Symptom check")


### Employee pass

If your responses to the statement show you are healthy, you will receive a pass to enter into the selected facility. The pass expires in 24 hours. 

If your responses show you are not healthy, you will not receive a pass and will be given the contact information for the company health and safety department if needed.

> [!div class="mx-imgBorder"]
> ![Employee pass](media/employee-pass.png)

> [!div class="mx-imgBorder"]
> ![Negative results](media/employee-pass-negative.png "Negative results")

## Share sentiment

Employees can share their opinion on how they are feeling about returning to the workplace.

On the home page you can give your response for the **Do you feel safe returning to work?** by selecting one of the options available.  

> [!div class="mx-imgBorder"]
> ![Share sentiment](media/employee-share-sentiment2.png "Share sentiment")

> [!div class="mx-imgBorder"]
> ![Share sentiment](media/employee-share-sentiment2-2.png "Share sentiment")

## Issues and feedback

- To report an issue with the Return to the Workplace solution, visit <https://aka.ms/rtw-issues>.

- For feedback about the Return to the Workplace solution, visit <https://aka.ms/rtw-feedback>.