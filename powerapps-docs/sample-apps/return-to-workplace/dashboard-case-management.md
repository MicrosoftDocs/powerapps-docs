---
title: Use the Case Management dashboard
description: Provides an overview of case management dashboards.
author: wbakker-11
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 08/25/2020
ms.author: garybird
ms.reviewer: kvivek
---

# Use the Case Management dashboard

This article is for Health and Safety Leads who use the Power BI dashboard to have an awareness of employee well-being and effectively manage and track employee cases across their network of facilities and locations using the Return to the Workplace solution.

## How to view the Case Management dashboard

1. Open Power BI Desktop.

2. In the search bar, search for Return to the Workplace – **Case management**.

    > [!div class="mx-imgBorder"]
    > ![Search for dashboard](media/pbi-dash-command-bar2.png "Search for dashboard")

## Overview page

The overview page is the default page of the dashboard that provides an overall visibility into key metrics and trends related to employee cases. The key metrics include: 

- Total Active Cases: Number of active cases.

- Cases per case manager: Average number of active cases (in open, investigating, and monitoring phase) per case manager.

- Days without New Cases: Number of days for which a new case has not been opened at a facility.

- Average Risk: Average case risk associated with a facility or group of facilities.

- Average Resolution Time: Days needed to resolve cases.

The interactive map displays the active cases by stage and by location. The size of the bubble represents the number of cases. The Case Manager Overview table contains information about number of cases, average risk, and average resolution time (days).

> [!div class="mx-imgBorder"]
> ![System at a Glance](media/pbi-dash-system-at-a-glance3.png "System at a Glance")

## Investigating page

This page provides a detailed view of active cases being investigated with a set of key metrics important for that stage. Key metrics include:

- Cases being investigated: The number of cases being investigated.

- Contacts reached: Number of employees that have been reached out of all employee cases under investigation.

- Time to start investigating: Average time taken from opening a case to starting an investigation.

- Time to reach a contact: Average time taken from opening a case to contacting an employee.

- Cases per case manager: Average number of cases under investigation per case manager.

The interactive map displays the location of cases in investigating stage and can be drilled into by Country, Province, and Facility. The size of the bubble represents the number of cases. 

The Case Manager Overview table contains information about number of cases, case manager, time to start investigating, and time to reach a contact in tabular form.

> [!div class="mx-imgBorder"]
> ![System at a Glance cases](media/pbi-dash-report-covidcases2.png "System at a Glance cases")

## Monitoring page 

This page focuses on active cases that are in monitoring stage. Key metrics include:

- Cases being Monitored: Number of cases being monitored.

- Avg Resolution Time (days): Average time taken for a case from being opened to resolved.

- Cases per Case Manager: Average number of cases in the monitoring phase per case manager.

- Resolved Cases: Total number of cases already resolved.

The interactive map displays the location of cases in the monitoring phase and can be drilled into by Country, Province, and Facility. The size of the bubble represents the number of cases. The Case Manager Overview table contains information about number of cases, case manager, average resolution time, and variance from average in tabular form.

> [!div class="mx-imgBorder"]
> ![System at a Glance fatal COVID cases](media/pbi-dash-report-fatalcovidcases2.png "System at a Glance fatal COVID cases")

## Slicers

Users can filter all the three pages by the case creation date and their groups of facilities and locations, going down to the level of a single facility.

> [!div class="mx-imgBorder"]
> ![System at a Glance reproductive number](media/pbi-dash-report-reproductivenumber2.png "System at a Glance reproductive number")


## Feedback about the solution

To provide feedback about the Return to the Workplace solution, visit <https://aka.ms/rtw-community>.
