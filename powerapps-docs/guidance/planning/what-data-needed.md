---
title: Is there data or information that they start with or need access to | Microsoft Docs
description: Is there data or information that they start with or need access to
author: TGround
ms.service: powerapps
ms.topic: conceptual
ms.custom: guidance
ms.date: 06/02/2020
ms.author: thground
ms.reviewer: kvivek
searchScope:  
  - PowerApps
---

# Is there data or information that they start with or need access to?

What data, if any, does this person have presented to them as they begin these
activities?

Where did this data come from?

-   Does this data come from a previous step?

-   Did this data come from an existing system? Does the user need to be signed
    in to access the data?

-   Is there data being pulled from an external system, such as market or
    weather data?

> Example:
>
> To fill out their expense reports, employees start with their name,
employee ID, manager’s name, and the date; they gather their receipts; and they
need access to the list of expense types and the rules for each.

## Data privacy/permission considerations


Thinking about the user executing these steps of the process:

-   What existing data do they need access to?

-   Do they need access to data that other users should not have access to?

-   Can they do tasks that other users shouldn’t be able to do?

Understanding what data users should be able to access helps to define what, if
any, security, and privacy controls need to be in the solution.

Understanding the user also helps determine how much data the user can see. If
the user is a manager, will they be able to see all work items of all workers?
And if the user is a worker, should they only see their own work items?

> Example:
> 
> Data privacy is different depending on the role of the person using the
app:
> - Originator of the expense report – they should be able to see only their own
    expense reports
> - Managers (Nick) – Nick should only be able to see the expense reports of his
    direct reports
> - Audit (Abhay) – Abhay should have the authority to review ALL of the expense
    reports

## Data refresh considerations

How often does the incoming data change? How often should it be refreshed? Is
this data real-time coming from a device or a system, or does this data change
infrequently? How often should the app be updated with new data?

> Example: 
>
> The data coming from Active Directory isn’t changed very often,
however, it does change on occasion as people move from role to role within the
organization as well as the reporting structure – so for this app it is
appropriate to look up the information at the time the user creates the expense
report. There is no need to go check the information again.
