---
title: Understanding job roles and personas for your app project | Microsoft Docs
description: As part of the planning phase of a Power Apps project, document who is doing the work, when, and where.
author: TGrounds
ms.service: powerapps
ms.topic: conceptual
ms.custom: guidance
ms.date: 06/16/2020
ms.subservice: guidance
ms.author: thground
ms.reviewer: kathyos

---

# Who is doing the work, when, and where?
For this step, you need to understand who is doing the work. What is their role?

It might be easiest to start with the names of people, but you'll want to understand
what their role is when they're doing the task. For example:

- *Any employee* submitting an expense report

- *Report submitter's manager* approving the report (the relationship to the submitter
    is the key)

- *Accounting specialist* reviewing the report (membership in a specific team
    is the key)

- *CFO* reviewing aggregated financials (the specific title is the key)

A single person might at times play each of these roles, but the key is to
understand *the role they're playing when they do the task*. Understanding roles
will help you design the app screens, and configure access and security. (We'll get to those in the designing phase.)

In IT terms, each person or group of people who perform the same function are
referred to as a *job role*, and a description of their relevant characteristics
is identified in a *persona* (which often has a name attached to it for easy
reference).

After you identify the "who," consider:

- What device is used? Where is the primary location of the work? Is it in the
    office? Client site? Factory? (We'll discuss this more in the next
    sections.)

- What other systems are used regularly? (Knowing this will be useful in the
    designing phase. For example, a manager who "lives" in Microsoft Teams might want to get
    approval requests there versus email.)

- What would this person gain by using the app or cooperating to work with
    this new process?

The last point is very important, because there might be objections or hesitation from
the people involved in the process before or after the steps handled by your app. That could result in your app's not being used due to the lack of
cooperation.

> [!TIP]
> It's essential to know who will be affected by a change to a business process. Identify who will be using the app and who will be affected by this
change, even if they don't use the app.

> [!TIP]
> When going through this analysis for the information you might not know,
the best thing to do is to talk with the person and get their perspective. You
can certainly make an assumption about how they do the work, but it's amazing
what you can learn in a quick conversation&mdash;not just how they do it today, but
how they'd prefer to do it in the future.

## How often are they doing the work?

Also write down how often the task is done. Daily, weekly, occasionally,
seasonally?

An app that's used daily has different design considerations than one that's only
used occasionally. (For example, the former might need to be streamlined
and the latter might need to include more explanatory text.)

## Where are they doing the work?

As you consider each person who contributes to solving the problem, think about
how they do their work:

- Is this something they do at their desk?

- Are they working at a specific location in the field?

- Do they move from location to location in the field?

It's good to understand how each of the users works so that the solution you
create works for them.

- Will this be a mobile app?

- Will it be a desktop app?

- Should there be both mobile and desktop versions?

### Connectivity considerations

As each worker performs their part of the process, can they get online?

Are they in the field where there isn't any connectivity? Can the user work with
the automated solution to capture the data in real time and have the data sync up
when they do establish connectivity?

What do the other participants in the process need to know (if anything) while
the person performing this step is offline?

Understanding this helps determine whether you need processes that capture data
locally so that the user can be "disconnected" while they do their part of the
process, and then sync the results when they reconnect.

### Device considerations

As you understand how each contributor to solving the problem works, it's also
important to know what devices they're working on. If a worker is in the field
and only works on their phone or a tablet, that's good to know as you get
into defining how screens look and function. If all the contributors are on a
desktop or laptop, you can take different design approaches. You can build desktop and
mobile solutions that work together.

## Example: Personas for the expense reporting process

These are the types of roles, work styles, and preferences we found when we
looked into our expense reporting process.

:::row:::
    :::column:::
       ![Illustration of Lee in Sales.](media/lee-small.png "Illustration of Lee in Sales")

       **Lee – Salesperson**

       -   Almost always on the move

       -   Prefers to work with a tablet when meeting with customers

       -   Doesn't always have internet connectivity, so must be able to work offline

       -   Prefers to capture his expenses and receipts as soon as possible after they happen
    :::column-end:::
    :::column:::
       ![Illustration of Nick the Sales Manager.](media/nick-small.png "Illustration of Nick the Sales Manager")

        **Nick – Sales Manager**

        - Almost always on the move

      -   Needs just a touchscreen

      -   Requires offline support for remote locations

      -   Responsible for approving the expense reports of all his direct reports
    :::column-end:::
:::row-end:::

:::row:::
    :::column:::
       ![Illustration of Shawna in Customer Support.](media/shawna-small.png "Illustration of Shawna in Customer Support")

        **Shawna – Customer Support**

        -  Mainly uses a desktop
        
        -  Usually incurs expenses for team morale, and must identify the employees included
    :::column-end:::
    :::column:::
       ![Illustration of Rebecca the Auditor.](media/rebecca-small.png "Illustration of Rebecca the Auditor")
       
       **Rebecca – Auditor**

       -   Needs to interact with all employees in all locations

        -  Has occasional travel expenses

        -  Mainly uses a desktop, but prefers to use her mobile phone

        -  Usually has access to the internet

        -  Responsible for ensuring overall employee compliance with reporting
       procedures
    :::column-end:::
:::row-end:::

:::row:::
    :::column:::
        ![Illustration of Abhay in Accounting.](media/abhay-small.png "Illustration of Abhay in Accounting")

        **Abhay - Accountant**

        -   Must be able to review all expense reports and receipts

        -   Responsible for ensuring compliance for every expense report

        -   Handles a large volume of work; needs to be able to process information quickly

        -   Must be able to report on how expenses are balancing up to the budget

    :::column-end:::
    :::column:::
        ![Illustration of Charlotte the CFO.](media/charlotte-small.png "Illustration of Charlotte the CFO")

        **Charlotte - CFO**

        -   Must keep an eye on the overall expense budget and help section managers
        stay within budget

        -   Travels to various offices, has external meetings and conferences, and
        must capture her own expenses

        -   Works from the office, remotely, and from home using various devices&mdash;desktop,
        tablet, and her phone

        -   Isn't always connected to the internet
    :::column-end:::
:::row-end:::

When we looked specifically at step 1 in our process (actually creating the
expense report), here's what we documented.

**Task 1: Create an expense report**

<table>
<colgroup>
<col width="30%">
<col width="70%">
</colgroup>
<tbody>
<tr><td><b>Who does this?</b></td><td>All employees</td></tr>
<tr><td><b>Where does the work happen?</b></td><td>At the office, at client sites, or on the road</td></tr>
<tr><td><b>When does the work happen?</b></td><td>Ad hoc. Some employees are doing this at least weekly. Others might do it once or twice a year.</td></tr>
<tr><td><b>Online or offline?</b></td><td>This is currently done on paper, but the team wants to do it digitally. Data entry can be done offline when no connectivity is available. Salespeople don't want to have to be online to start recording their receipts and expenses. (For instance, they might prefer to do this on the plane ride home.)</td></tr>
<tr><td><b>Devices?</b></td><td>Phone, tablet, laptop, or desktop</td></tr>
</tbody>
</table>

> [!div class="nextstepaction"]
> [Next step: What activities are being done?](what-activities.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]