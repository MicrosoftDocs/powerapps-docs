---
title: Who is doing the work, when, and where | Microsoft Docs
description: Who is doing the work, when, and where
author: TGrounds
ms.service: powerapps
ms.topic: conceptual
ms.custom: guidance
ms.date: 06/02/2020
ms.author: thground
ms.reviewer: kathyos
searchScope:  
  - PowerApps
---

Who is doing the work, when, and where?
=======================================
<!---Editor team: Two things I was unable to achieve: Make the people images smaller; and widen the first column in the table at the bottom of the article -->
For this specific step, understand who is doing the work. What is their role?

It may be easiest to start with the named people, but you’ll want to understand
what their role is when they are doing the task.

For example

-   “Any employee” submitting an expense report

-   “Report submitter’s manager” approving the report (relationship to submitter
    is the key)

-   “Accounting specialist” reviewing the report (membership in a specific team
    is the key)

-   “CFO” reviewing aggregated financials (specific title is the key)

A single person may at times play each of these roles, but the key is to
understand *the role they’re playing when they do the task*. Understanding roles
will help you design the app screens as well as configure access and security. (We’ll get to those in the Design phase.)

In IT terms, each person or group of people that perform the same function are
referred to as a “Job Role” and a description of their relevant characteristics
is identified in a “Persona” (that often has a name attached to it for easy
reference).

After you identify the “who”, consider:

-   What device is used? Where is the primary location of the work? Is it in the
    office? Client site? Factory? (We’ll discuss this more in the next
    sections.)

-   What other systems are used regularly? (Knowing this will be useful in the
    Design phase. For example, a manager who lives in Teams may want to get
    approval requests there vs email.)

-   What would this person gain by using the app or cooperating to work with
    this new process?

The last point is very important because there may be objections or hesitations from
the people involved in the steps before or after the ones handled by your app. That could result in not being able to use the app due to the lack of
cooperation.

> [!TIP]
> Knowing who will be impacted by a change to the business process is
essential. Identify who will be using the app and who will be impacted by this
change even if they are not using the app.

> [!TIP]
> When going through this analysis, for the information you may not know,
the best thing to do is to talk with the person and get their perspective. You
can certainly make an assumption about how they do the work, but it’s amazing
what you can learn in a quick conversation – not just how they do it today, but
how they would prefer to do it in the future.

How often are they doing the work?
----------------------------------

Also write down how often the task is done. (Daily, weekly, occasionally,
seasonally?)

An app that is used daily has different design considerations than one that is
used occasionally. (For example, the former might need to be streamlined
and the latter might need to have more explanatory text.)

Where are they doing the work?
------------------------------

As you consider each person who contributes to solving the problem, think about
how they do their work

-   Is this something they do at their desk?

-   Are they working at a specific location in the field?

-   Do they move from location to location in the field?

It’s good to understand how each of the users works so that the solution that is
created works for them.

-   Will this be a mobile application?

-   Will it be a desktop application?

-   Should there be both mobile and desktop?

### Connectivity considerations

As each worker performs their part of the process, can they get online?

Are they in the field where there isn’t any connectivity? Can the user work with
the automated solution to capture the data real-time and have the data sync up
when they do establish connectivity?

What do the other participants in the process need to know, if anything, while
the person performing this step is offline?

Understanding this helps determine if you need processes that capture data
locally so that the user can be ‘disconnected’ while they do their part of the
process and then sync the results when they reconnect.

### Device considerations

As you understand how each contributor to solving the problem works, it is also
important to know what devices they are working on. If a worker is in the field
and only works on their phone or a tablet, then that is good to know as you get
into defining how screens look and function. If all the contributors are on a
desktop or laptop, then different design approaches can be taken. Desktop and
mobile solutions can be built that work together.

Example: Personas for expense reporting process
-----------------------------------------------

These are the types of roles, work styles, and preferences we found when we
looked into our expense reporting process:


:::row:::
    :::column:::
       ![Illustration of Lee in Sales](media/lee.png)

       **Lee – Salesperson**

       -   Almost always on the move

       -   Prefers to work with a tablet when meeting with customers

       -   Does not always have internet connectivity so must be able to work offline

       -   Prefers to capture his expenses and receipts as soon after they happen as
       possible
    :::column-end:::
    :::column:::
       ![Illustration of Nick the Sales Manager](media/nick.png)

        **Nick – Sales Manager**

        -   Almost always on the move

      -   Needs just touch screen

      -   Requires offline support for remote locations

      -   Responsible for approving the expense reports of all of his direct reports
    :::column-end:::
:::row-end:::

:::row:::
    :::column:::
       ![Illustration of Shawna in Customer Support](media/shawna.png)

        **Shawna – Customer Support**

        -   Mainly uses desktop
        
        - Usual expenses are for team morale and must identify
        employees included
    :::column-end:::
    :::column:::
       ![Illustration of Rebecca the Auditor](media/rebecca.png)
       
       **Rebecca – Auditor**

       -   Needs to interact with all employees in all locations

        -   Occasional travel expenses

        -   Mainly uses desktop but prefers to use her mobile phone

        -   Usually has access to the Internet

        -   Responsible for ensuring overall employee compliance with reporting
       procedures
    :::column-end:::
:::row-end:::

:::row:::
    :::column:::
        ![Illustration of Abhay in Accounting](media/abhay.png)

        **Abhay - Accountant**

        -   Must be able to review all expense reports and receipts

        -   Responsible for ensuring compliance for every expense report

        -   Large volume of work; needs to be able to process information quickly

        -   Must be able to report on how expenses are balancing up to the budget

    :::column-end:::
    :::column:::
        ![Illustration of Charlotte the CFO](media/charlotte.png)

        **Charlotte - CFO**

        -   Must keep an eye on the overall expense budget and help section managers
        stay within budget

        -   Travels to the various offices and has external meetings and conferences and
        must capture her own expenses

        -   Works from the office, remotely and from home from various devices, desktop,
        tablet, and her phone

        -   Is not always connected to the internet
    :::column-end:::
:::row-end:::


When we looked specifically at step 1 in our process (actually creating the
expense report), here’s what we documented:

**Task 1: Create expense report**

| **Who does this?**                         | All employees                                                                                                                                                                                                                                              |
|--------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Where does the work happen?** | At the office, at client sites, and on the road (and in the air)                                                                                                                                                                                                              |
| **When does the work happen?**  | Ad hoc. Some employees are doing this at least weekly. Others may do this once or twice a year.                                                                                                                                                                               |
| **Online or offline?**          | This is currently done on paper but the team wants to do digitally. Data entry may be done offline when no connectivity available. Salespeople don’t want to have to be online to start recording their receipts and expenses. (For instance may do this on plane ride home.) |
| **Devices**                     | Phone, tablet, laptop, or desktop                                                                                                                                                                                                                                             |
