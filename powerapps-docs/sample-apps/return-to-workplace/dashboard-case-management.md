---
title: Use the Workplace Care Management dashboard
description: Provides an overview of the Workplace Care Management dashboards.
author: wbakker-11
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 10/05/2020
ms.author: garybird
ms.reviewer: kvivek
---

# Use the Workplace Care Management dashboard

This article is for health and safety leads who use the Power BI dashboard to gain awareness of employee well-being, and effectively manage and track employee cases across their network of facilities and locations, by using the Return to the Workplace solution.

## How to view the Workplace Care Management dashboard

1. Open Power BI Desktop.


<!-- editor question: The image shows "case management". Which is correct, care or case? -->


2. In the search bar, search for Return to Workplace – **Care management**.

    > [!div class="mx-imgBorder"]
    > ![Search for dashboard](media/pbi-dash-command-bar2.png "Search for dashboard")

## Overview page

The Overview page is the default page of the dashboard that provides overall visibility into key metrics and trends related to employee cases. The key metrics include:

- Total active cases: Number of active cases.

- Days without new cases: Number of days since a new case hasn't been opened at a facility.

- Average risk: Average case risk associated with a facility or group of facilities.

- Average resolution time: Days needed to resolve cases.

- Cases per case manager: Average number of active cases (in open, investigating, and monitoring phases) per case manager.

The interactive map displays the active cases by stage and location. The size of the bubble represents the number of cases. The case manager overview table contains information about the number of cases, average risk, and average resolution time in days.

> [!div class="mx-imgBorder"]
> ![System at a glance](media/pbi-dash-system-at-a-glance3.png "System at a glance")

## Investigating page

The Investigating page provides a detailed view of active cases being investigated with a set of key metrics important for that stage. Key metrics include:

- Cases being investigated: The number of cases being investigated.

- Contacts reached: Number of employees that have been reached out of all employee cases under investigation.

- Time to start investigating: Average time taken from opening a case to starting an investigation.

- Time to reach a contact: Average time taken from opening a case to contacting an employee.

- Cases per case manager: Average number of cases under investigation per case manager.



<!-- editor question: Can we say "country or region"? What about "state" in addition to province? -->

The interactive map displays the location of cases in the investigating stage. You can drill into the data by country, province, and facility. The size of the bubble represents the number of cases. 

The case manager overview table contains information about case manager, number of cases, time to start investigating, and time to reach a contact.

> [!div class="mx-imgBorder"]
> ![System at a glance - cases](media/pbi-dash-report-covidcases2.png "System at a glance - cases")

## Monitoring page 

The Monitoring page focuses on active cases that are in the monitoring stage. Key metrics include:

- Cases being monitored: Number of cases being monitored.

- Cases per case manager: Average number of cases in the monitoring phase per case manager.

- Resolved cases: Total number of cases already resolved.



<!-- editor note: I don't see "Avg resolution time" in the screenshot (maybe you have to scroll?). Also, can we add region and state, similar to previous question? -->

- Avg resolution time (days): Average time taken for a case from being opened to resolved.

The interactive map displays the location of cases in the monitoring phase. You can drill into the data by country, province, and facility. The size of the bubble represents the number of cases. The case manager overview table contains information about case manager, number of cases, average resolution time, and variance from average.

> [!div class="mx-imgBorder"]
> ![System at a glance - COVID cases](media/pbi-dash-report-fatalcovidcases2.png "System at a glance - COVID cases")

## Clusters page

The Clusters page helps health and safety leads view cases as clusters and assess whether there is an outbreak in a facility. The tab focuses on case contacts and links between active cases, identifying the root cause of the outbreak. It also provides a set of metrics and trends related to case contacts. These metrics include:

- Case contacts per case: Average number of case contacts per active case.

- % contacts evaluated: Percentage of case contacts whose evaluation is complete.

- Average evaluation time: For evaluated case contacts, time taken to evaluate or process a case contact in days.

- Average linked cases per case: The number of case contacts with an active case of their own per active case. 

- % evaluated within 24 hr: Percentage of case contacts that were evaluated or processed within 24 hours of identification.

> [!div class="mx-imgBorder"]
> ![Cluster nav map](media/pbi-dash-report-clusternavmap.png "Cluster nav map")

Users can switch from a map to the table visual, where key metrics are displayed by facility. 

> [!div class="mx-imgBorder"]
> ![Cluster nav table](media/pbi-dash-report-clusternavtable.png "Cluster nav table")

Map displays active cases by facility. To view a cluster, select a facility on the map. 


<!-- editor question: Is that a fake address in the New York map? -->


> [!div class="mx-imgBorder"]
> ![Cluster nav map facility selected](media/pbi-dash-report-clusternavmap-facility.png "Cluster nav map facility selected")

The clusters view provides information about case contacts and linked cases, and also relationships between active cases for the selected facility and date range. Relationships are visualized in the form of a network, where cases are represented as a circle, colored based on their stage. The thickness of the line displays the exposure score, which measures how close and frequent exposure has been between two cases.

> [!div class="mx-imgBorder"]
> ![Cluster network](media/pbi-dash-report-clusternetwork.png "Cluster network")

You also can switch from a map view to a table view to see key metrics by case. 

> [!div class="mx-imgBorder"]
> ![Cluster table](media/pbi-dash-report-clustertable.png "Cluster table")

The following sets of metrics related to the selected facility are also displayed:

- Total number of cases linked to a facility.

- Total number of case contacts.

- Number of standalone cases: Cases that are not linked to other cases in a facility.

- Number of cases that are part of a cluster.


## Slicers

Slicers help you quickly "slice and dice" the data, focusing only on data points you're interested in. You can filter all three pages by the case creation date and their groups of facilities and locations, down to the level of a single facility. 

> [!div class="mx-imgBorder"]
> ![System at a glance - reproductive number](media/pbi-dash-report-reproductivenumber2.png "System at a glance - reproductive number")

## Give feedback about the solution

To provide feedback about the Return to the Workplace solution, go to the [Return to the workplace community page](https://aka.ms/rtw-community).
