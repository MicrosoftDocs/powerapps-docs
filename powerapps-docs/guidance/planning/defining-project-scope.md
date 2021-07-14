---
title: Planning - Defining the Power Apps project scope | Microsoft Docs
description: Your scope directly affects and determines which features to include and not to include when making the app. Learn about scope constraints to consider.
author: taiki-yoshida
ms.service: powerapps
ms.topic: conceptual
ms.custom: guidance
ms.date: 06/16/2020
ms.author: tayoshi
ms.reviewer: kathyos

---

# Defining the project scope

Make sure you scope the project so that you know how much you'll be trying to
achieve from the project. Keep a clear roadmap for what you define as
complete and what's outside the scope of the project (and, possibly, to be done in the next
version). Your scope directly affects and determines which [features to include and not to include](prioritizing-features.md) when making the app.

To define the project scope, you should consider the following constraints:

- **Time**: Set a deadline for when you'd like to accomplish the project
    objectives. With smaller projects, this might be a few weeks,
    whereas larger projects might take several months.

- **People**: How many people do you have available for the project?

- **Budget**: If you need to account for time spent by you and your
    coworkers, or if you need to hire experts, you'll need to establish a
    budget.

- **Feasibility**: You might find you're constrained by available expertise, by
    lack of access to the data you need, or by the amount of change your
    organization has appetite for.

You should also consider what functional pieces you can deliver in usable
chunks. It won't do anybody any good if your app only delivers halfway on several features; plan to
deliver each component in a working form, end to end. Even if it doesn't yet have
every feature you want, deliver something that can be used. Your project plan
should specify what you'll deliver in each phase.

## Example: Expense report project scope

Looking at our business process, we see that it's divided into five main tasks:

1. Creating the expense report

2. Approving the expense report

3. Getting the data into the financial payment system

4. Reviewing weekly budget analytics

5. Auditing

![Business process flowchart with major tasks and task location called out.](media/task-chart.png "Business process flowchart with major tasks and task location called out")

We think we have the expertise to create an expense report app and the approvals
process. The auditing requirements seem to have quite a bit of overlap with what
we need for expense report approvals.

After we deliver the creation of expense reports, we think we'll be ready to
tackle the budget analysis; in fact, as soon as we get the data model set up, we should
be able to have our separate team of Power BI experts start on that project in
parallel.

We're unsure about getting the data directly into the finance system, because it
requires system expertise we don't have access to right now. So that's
currently outside the scope of the project, but we'll most likely add it in a
later phase.

Always coming back to our overall project mission ("Create a process that's
efficient for employees and the accounting department, allows faster budget
tracking, and reduces our exposure in audits"), we think our project scope is
appropriate.

> [!div class="nextstepaction"]
> [Next step: Prioritzing features](prioritizing-features.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]