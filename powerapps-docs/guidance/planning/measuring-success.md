---
title: Planning a Power Apps project - Measuring success | Microsoft Docs
description: As part of planning a Power Apps project, identify SMART measures to track progress against realizing the business value you think is achievable for your app.
author: TGrounds
ms.service: powerapps
ms.topic: conceptual
ms.custom: guidance
ms.date: 06/16/2020
ms.subservice: guidance
ms.author: thground
ms.reviewer: kathyos

---

# Measuring success against the business value

After you've identified the business value you think is achievable, you
must figure out how to measure progress toward realizing that value. To do this,
identify SMART measures. SMART measures stand for:

- **S**pecific: What, where, and how. A specific goal is distinct and
    contains no ambiguous language.

- **M**easurable: *From* and *To*&mdash;a measurement gives feedback and lets
    you know when the goal has been achieved. Typically, the "from" value is where we
    are today and the "to" value is the target we're aiming for.

- **A**ssignable: This is the "who": the individual or group who will
    achieve the goal. Many times, changes in behavior are triggered by the fact
    that the person knows that something is being measured. The **A** is sometimes
    defined as Achievable, but Assignable acknowledges that the Realistic measure
    has something to do with whether the goal is Achievable.

- **R**ealistic: Is what's being measured even feasible? Realistic goals are
    challenging yet attainable within the given timeframe.

- **T**ime-based: When will the goal be achieved? The timeframe must be
    aggressive yet realistic

When identifying the measure, always ask yourself: will it help realize the
business value that we've identified? Don't spend time measuring activities
that don't help achieve business value.

Some measures will be a dollar amount, but others might just be a number. Those
values can be converted to a dollar amount with a bit of effort. For example, if you know the amount of time that will be saved per person, multiply the amount of time by the loaded
cost of the person doing the process. The result is the dollar amount that was saved.

Another goal-setting methodology you can use is to define objectives and key results
(OKRs). The objective is the big-picture vision you're trying to achieve. The
key result is the way you'll measure progress toward that goal. For example, an
objective might be "Increase retention in the Accounting team," and the key result might be "20&nbsp;percent increase in survey-measured job satisfaction after app launch."

## Return on investment

The calculation of return on investment (ROI) is done by reviewing the cost of building the
solution to ensure that the value is more than that cost.

In many cases, when a business user is solving a problem, it's being done in
their spare time and doesn't necessarily need to be accounted for as a cost.
However, when you need to determine ROI,
it's important to understand the time it will take to build the solution. To
help you estimate that, proceed to the next section, [Creating a project plan](defining-app-project-objective.md).

## Example: Measuring success for the expense reporting solution

To decide on our goals, we looked back at our project objective:

> Expense reporting: Create a process that's efficient for employees and the
> accounting department, allows faster budget tracking, and reduces our
> exposure in audits.

We can consider a couple of meaningful success measures in our
example.

Initially, we considered tracking the number of expense reports that were returned for rework.
However, if the app is built to impose business rules&mdash;like requiring a receipt
for a charge greater than \$75&mdash;the employee submitting the expense report
won't be able to submit it until they provide the receipt, so that measure won't be
very meaningful.

One measure that will be valuable is being able to track the amount of time an
employee takes to complete their expense report; after all, we based our
cost savings on the user's being able to go from 1 hour down to 20 minutes. It might
be worth tracking the actual time the user is in the app to validate
this number and report against it.

Now that Nick and the other managers are responsible for approving the expense
reports, it might be worth tracking how long it takes between the time the expense report is
submitted by the employee to the time Nick and the other managers approve it.
Tracking this, and having managers be aware that it's being tracked, will
help improve this behavior. People tend to focus on what's being measured.

The SMART goals we decided on are:

- For at least 80&nbsp;percent of expense reports, expense report creators spend no more
    than 20 minutes actively working on creating reports.

- For at least 90&nbsp;percent of expense reports, the time between submitting the report
    and having a payment logged in the finance system is less than three business
    days.

- By the end of this year, department managers access a weekly budget report that's up-to-date
    for all expenses within one hour of their approval.

- Within one month of solution availability, 100&nbsp;percent of expense reports use the
    digital system.

- The number of errors found in the semiannual audit is reduced by 50&nbsp;percent.

> [!div class="nextstepaction"]
> [Next step: Creating a project plan](defining-app-project-objective.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]