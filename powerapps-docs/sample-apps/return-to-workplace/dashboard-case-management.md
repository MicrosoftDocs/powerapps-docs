---
title: Use the Location Readiness dashboard
description: Provides an overview of insights through dashboards.
author: wbakker-11
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 07/21/2020
ms.author: garybird
ms.reviewer: kvivek
---

# Use the Case Management Dashboard

This article is for Health and Safety Leads who use the Power BI dashboard to have an awareness of employee well-being and effectively manage and track employee cases across their network of facilities and locations using the Return to the Workplace solution.


##  How to view the Case Management Dashboard

1. Open Power BI Desktop.

2. In the search bar, search for Return to the Workplace – **Case management.**

    > [!div class="mx-imgBorder"]
    > ![Search for dashboard](media/pbi-dash-command-bar2.png "Search for dashboard")


## Overview Page

The **Overview Page** is the default or the top-level page that provides an overall view. It provides visibility into key metrics and trends related to employee cases. The key metrics include: 

- Total Active Cases 

- Cases per Case Manager: Average number of active cases (in open, investigating and monitoring phase) per case manager

- Days without new Cases: Number of days for which a new case has not been opened at a facility 

- Average Risk: Average case risk associated with a facility or group of facilities

- Average Resolution time – days needed to 


> [!div class="mx-imgBorder"]
> ![System at a Glance](media/pbi-dash-system-at-a-glance3.png "System at a Glance")


## Investigating Page

The page provides information on Active Cases in Investigation stage such as the number of cases being investigating, time it takes to start investigation and reach a contact, trends behind them, breaking them down by the Case Manager.

> [!div class="mx-imgBorder"]
> ![System at a Glance cases](media/pbi-dash-report-covidcases2.png "System at a Glance cases")


## Monitoring Page 

This page focuses on active Cases in Monitoring Stage. It shows:

- Cases being Monitored.

- Average resolution time: average time taken for a case from being opened to resolved.

- Cases per case manager: average number of cases in Monitoring phase per Case manager.

- Resolved Cases: Total number of cases already resolved.


> [!div class="mx-imgBorder"]
> ![System at a Glance fatal COVID cases](media/pbi-dash-report-fatalcovidcases2.png "System at a Glance fatal COVID cases")


## Slicers

Users can filter al three pages by the case creation date and their Groups of Facilities and Locations, going down to the level of a single Facility.

> [!div class="mx-imgBorder"]
> ![System at a Glance reproductive number](media/pbi-dash-report-reproductivenumber2.png "System at a Glance reproductive number")



### Data sources

The dashboard consists of data from the model-driven app and the canvas app, but also consists of external data. The following data sources are used:

1. WHO (cases/deaths): <https://covid19.who.int/>  
© World Health Organization 2020, All rights reserved.  
WHO supports open access to the published output of its activities as a fundamental part of its mission and a public benefit to be encouraged wherever possible. Permission from WHO isn't required for the use of the WHO Coronavirus disease (COVID-19) dashboard material or data available for download. It's important to note that:

   - WHO publications can't be used to promote or endorse products, services, or any specific organization.
   - The WHO logo can't be used without written authorization from WHO.
   - WHO provides no warranty of any kind, either expressed or implied. In no event shall WHO be liable for damage arising from the use of WHO publications.

   For further information, visit [WHO Copyright, Licensing, and Permissions](https://www.who.int/about/who-we-are/publishing-policies/copyright).

2. USAFACTS (cases/deaths US only): <https://usafacts.org/visualizations/coronavirus-covid-19-spread-map/>  

   © 2020 USAFacts. All rights reserved.  USAFacts data is available under a Creative Commons license. Learn more at <https://usafacts.org/faq/> 

3. Bing COVID Tracker (cases/deaths for China (mainland), Taiwan, Hong Kong SAR, and Macao SAR: <https://github.com/microsoft/Bing-COVID-19-Data>

    Bing COVID-19 Data.  This data is available strictly for educational and academic purposes, such as medical research, government agencies, and academic institutions, under terms and conditions available at <https://github.com/microsoft/Bing-COVID-19-Data/blob/master/LICENSE.txt>. Data used or cited in publications should include an attribution to 'Bing COVID-19 Tracker' with a link to www.bing.com/covid.

4. Reproductive factor estimates: <https://epiforecasts.io/covid/posts/global/> 

    This dataset is from EpiForecasts and the CMMID COVID-10 working group at <https://epiforecasts.io/covid/posts/global> and is licensed under Creative Commons Attribution CC BY 4.0.

## Feedback about the solution

To provide feedback about the Return to the Workplace solution, visit <https://aka.ms/rtw-community>.