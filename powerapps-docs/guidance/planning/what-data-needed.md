---
title: Data needs for each step of a business process | Microsoft Docs
description: As part of the planning phase of a Power Apps project, document the data required for each step of the business process you want to automate.
author: TGrounds
ms.service: powerapps
ms.topic: conceptual
ms.custom: guidance
ms.date: 06/16/2020
ms.subservice: guidance
ms.author: thground
ms.reviewer: kathyos

---

# Is there data or information that they start with or need access to?

What data, if any, has been presented to this person as they begin these
activities? Where did this data come from? Ask yourself:

- Did this data come from a previous step?

- Did this data come from an existing system? Does the user need to be signed
    in to access the data?

- Is data being pulled from an external system, such as market or
    weather data?

> Example:
>
> To fill out their expense reports, employees start with their name,
employee ID, manager's name, and the date; they gather their receipts; and they
need access to the list of expense types and the rules for each.

## Data privacy and permission considerations

Think about the user executing these steps of the process, and ask:

- What existing data do they need access to?

- Do they need access to data that other users shouldn't have access to?

- Can they do tasks that other users shouldn't be able to do?

Understanding what data users should be able to access helps to define what security and privacy controls need to be included the solution.

Understanding the user also helps determine how much data the user can see. If
the user is a manager, will they be able to see all the work items of all workers?
And if the user is a worker, should they only see their own work items?

> Example:
> 
> Data privacy is different depending on the role of the person using the
app:
> - The originator of the expense report: they should be able to see only their own
    expense reports.
> - Managers (Nick): Nick should only be able to see the expense reports of his
    direct reports.
> - Accountant (Abhay): Abhay should have the authority to review *all* the expense
    reports.

## Data refresh considerations

How often does the incoming data change? How often should it be refreshed? Is
this data coming from a device or a system in real time, or does this data change
infrequently? How often should the app be updated with new data?

> Example:
>
> The data coming from Azure Active Directory doesn't change very often;
however, it does change on occasion as people move from role to role within the
organization and in the reporting structure. So, for this app, it's
appropriate to look up the information at the time the user creates the expense
report. There's no need to check the information again.

> [!div class="nextstepaction"]
> [Next step: What data is created?](create-edit-data.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]