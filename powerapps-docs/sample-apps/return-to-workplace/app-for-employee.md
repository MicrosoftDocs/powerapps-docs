---
title: Use the Employee Return to the Workplace app
description: Provides information for employees to track their symptoms and determine whether they're eligible to enter into a facility.
author: wbakker
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 07/20/2020
ms.author: garybird
ms.reviewer: kvivek
---

# Use the Employee Return to the Workplace app

This article provides step-by-step instructions about how to use the Employee Return to the Workplace app. You can check in, answer questions to determine whether you're eligible to enter a facility, and say how you feel about returning to the workplace.

## Prerequisites

- Download [Power Apps Mobile](https://powerapps.microsoft.com/downloads):

  - For Apple devices with iOS, such as iPhone and iPad, use the [App Store](https://aka.ms/powerappsios).

  - For Android devices, use [Google Play](https://aka.ms/powerappsandroid).

- Ensure that your organization has deployed and configured the Employee Return to the Workplace app, as described in [Deploy the solution](deploy.md).

## Getting started with the app

Open the app from your device and sign in with your company's Azure Active Directory account. You can view all apps shared with you by your organization after you sign in. More information: [Power Apps mobile device sign in](https://docs.microsoft.com/powerapps/user/run-app-client#open-power-apps-and-sign-in)

When you successfully sign in and open the **Return to the Workplace** app from your mobile device, you can get a day pass, look up facility status, or answer the employee sentiment question.

> [!div class="mx-imgBorder"]
> ![Welcome screen](media/employee-welcome2.png "Welcome screen")

## See the reopen status of a facility

You can find all available facilities and see the reopen status for them<!--note from editor: Suggested.-->. Select **Look Up Status** to look for facilities and view details such as whether the facility is open and what phase of reopening it's in.

When you select a facility from the facility list, the current status of the facility and associated details are displayed. Select the top arrow<!--note from editor: Can we get an inline graphic for this? I took off the bold formatting because I'm pretty sure "Top Arrow" isn't the name that shows up in a tooltip for the graphic.--> to return to the home screen.

> [!div class="mx-imgBorder"]
> ![List of facilities](media/employee-facility-list2.png "List of facilities")

> [!div class="mx-imgBorder"]
> ![Facility details](media/employee-facility-details2.png "Facility details")

## Check in to a facility

After you complete the steps to select a particular facility that's open to employees returning to work, you can complete a health survey that determines whether you're eligible to check in to that facility. 

If you're eligible, you'll be given a pass to your selected building for that day. 

**To check in to a facility**

1. Select **GET DAY PASS**.

2. Select an available facility from the facility list.

3. Select **Start Health Survey** to complete the check-in process.

   > [!div class="mx-imgBorder"]
   > ![Start survey](media/employee-start-survey2.png "Start survey")

4. Accept the terms and agreements.

    > [!div class="mx-imgBorder"]
    > ![Terms and agreements](media/employee-termandagreement.png "Terms and agreements")

5. Review the **Symptom Check** statements. Select **I Agree**  if you agree with the statements, and **I Disagree** if you don't.

   > [!div class="mx-imgBorder"]
   > ![Symptom check](media/employee-agreement.png "Symptom check")

### Employee pass

If your responses to the symptom check statements show that you're healthy, you'll receive a pass to enter the selected facility. The pass expires in 24 hours. 

> [!div class="mx-imgBorder"]
> ![Employee pass](media/employee-pass.png "Employee pass")

If your responses show you aren't healthy, you won't receive a pass and you'll be given contact information for the company health and safety department to use if you need.<!--note from editor: Edit suggested, if the contact information is always provided. Another note: I think the alt text for the following image could be better, since "negative results" these days means that you don't have COVID-19. How about "Message to stay home" or something similar?-->

> [!div class="mx-imgBorder"]
> ![Negative results](media/employee-pass-negative.png "Negative results")

## Share sentiment

You can say how you're feeling about returning to the workplace. On the home page, select one of the options to answer the question **Do you feel safe returning to work?**<!--Suggested.-->  

> [!div class="mx-imgBorder"]
> ![Share sentiment](media/employee-share-sentiment2.png "Share sentiment")

After you select one of the options, the option will become visible.<!--But it must have been visible for someone to select it in the first place, right? I don't understand what happens here, but maybe it will be clear to the person using the app. I also don't know why there's a percentage in the following screenshot. Can people say that they feel 75% "yes" about returning to work?--> This option will reset itself after you reopen the app.<!--note from editor: The alt text for the following screenshot needs to be different from the previous screenshot, but I'm not sure what to suggest.-->

> [!div class="mx-imgBorder"]
> ![Share sentiment](media/employee-share-sentiment2-2.png "Share sentiment")

<!--
## Issues and feedback

- To report an issue with the Return to the Workplace solution, visit <https://aka.ms/rtw-issues>.

- For feedback about the Return to the Workplace solution, visit <https://aka.ms/rtw-feedback>. 
