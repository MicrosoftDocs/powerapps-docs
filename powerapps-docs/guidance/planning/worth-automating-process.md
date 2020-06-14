---
title: Is it worth automating this process? | Microsoft Docs
description: As part of the planning phase of a Power Apps project, consider the effort it will take to build the solution and decide whether it's justified by business value.
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

# Is it worth automating this process?

Now it's time to consider the effort it will take to build the solution and
decide whether it's justified. This involves weighing business value against the cost of automating the process. *Business value* is the ongoing benefit that the business receives from the
project.

## The cost of doing nothing

To figure out whether it's worth automating the process, you first must understand
the cost of *not* solving the problem.

As a byproduct of defining the business value that you hope to achieve from the Microsoft
Power Platform solution, you should get a better understanding of what it's
costing your organization to solve the problem in the current manner. In other
words, measure the cost of doing nothing.

If the business value you'll receive by automating the process is less than
the cost of doing nothing, you must ask yourself whether this is the right
business problem to focus on.

However, if the business value you receive by solving the business problem is
greater than the cost of doing nothing&mdash;plus your development time and the
monthly cost of any [software license](https://docs.microsoft.com/power-platform/admin/pricing-billing-skus)&mdash;it makes sense to automate the
process.

Before we decide to automate this business process, we'll answer the question
"what does it cost me to *not* automate the process."

## Example: The cost of the current expense process

The first thing we need to understand is, what is it costing the organization to
continue to do the expense report process manually? Here's what we discovered
when we talked to our colleagues:

- We found that it takes them roughly an hour
    each week to pull together all their receipts and fill out the manual
    expense report. Abhay indicated that there are about 140 expense reports
    per week. We also learned that the fully loaded cost of each team member is
    roughly \$90/hr.

    >   (140 expense reports &times; 1 hour/week) &times; \$90 = \$12,600/week
    >
    >   52 weeks &times; \$12,600 = \$655,200 a year

- Nick isn't reviewing or approving the expense reports; that's all falling
    to Abhay and his team to complete. Because he's not regularly monitoring the
    team's expenses, Nick is missing an important opportunity to sanity-check the
    expenses, watch for fraud, and optimize his team's spending habits.

- Abhay shared with us that his team spends roughly 15 minutes per expense
    report, receives on average 140 reports a week, and sends back 25&nbsp;percent of those
    due to missing information.

    >   Initial review:<br> 140 expense reports &times; 15-minute review = 35 hours
    >
    >   Initial review: 35 hours &times; \$90 = \$3,150 a week = \$163,800/year
    >
    >   Rework review: 35 expense reports &times; 15-minute review = 8.75 hours
    >
    >   Rework review: 8.75 hours &times; \$90/hr = \$787.50/week = \$40,950/year
    >
    >   Total weekly cost: \$3,937.50
    >
    >   Total annual cost: \$204,750

- After the expense report is verified to be accurate, it takes roughly 7
    minutes per expense report to look up the general ledger codes for each
    expense category and write them on each expense line of the report.

    >   140 expense reports &times; 7 minutes of coding = 16.5 hours/week =
        \$1,485/week = \$77,220/year

- It takes roughly 10 minutes per expense report to create a payment journal
    in the financial system to process for payment and appear on the financial
    report for Charlotte.

    >   140 expense reports &times; 10 minutes = 23.8 hours/week = \$2,142/week =
        \$111,384/year

- Charlotte would like to review the budget each week, but isn't able to get
    her report until Thursday, after Abhay has completed his review and
    gotten back the reports that had missing information. (Although this
    isn't a monetary cost, it does have an impact on the business.)

The entire process is costing the company:

> \$655,200 + \$204,750 + \$77,220 + \$111,384 = \$1,048,554

![Business process flowchart showing the employee cost for each task and the total cost of the process](media/cost-of-process.png "Business process flowchart showing the employee cost for each task and the total cost of the process")
