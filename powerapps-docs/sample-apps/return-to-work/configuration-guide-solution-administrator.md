---
title: Configuration Guide for Solution Administrator
---

## Version History

| Version | Release Date | Comments                                               |
|---------|--------------|--------------------------------------------------------|
| 0.1     | 19-06-2020   | Initial Draft for Review                               |
| 0.2     | 19-06-2020   | Updates to initial draft                               |
| 0.3     | 26-06-2020   | Updating screenshot and changes to support updated ERD |

# Prerequisites

The following prerequisites apply to this guide:

-   The environment needs to have all the Return to Workplace components in
    place with the Model Driven Apps, Canvas Apps and Power BI Dashboards.

-   For the following steps you need to have the right security roles in place.

    Contact your IT Admin if you are unable to access or use the admin app.

-   The sample data is in the package and needs to be installed on the
    environment.

# Overview

This guide provides business administrators a guide on how they need to
configure the Return to Workplace solution. A business administrator is
responsible for making sure the facility manager can guide their facilities
throughout their phases. This means that the following steps are needed and will
be covered in the document:

-   Plan Reopening Phases

-   Manage Facilities

-   Specify Solution Settings

# Plan Reopening Phases

Plan reopening requires the business administrator to define Reopen Phases to
reopen. Within these phases you define a goal upon which track progress on a
certain metric. These metrics can be sorted via categories to ease use. In the
phases you also define readiness factors which defines the steps required to be
taken in that phase.

In the model-driven app, you select the **Setup** module, which allow you to
configure the plan.

![](media/77d5316901485b262b8eefce12890e13.png)

When planning a reopening you need to step through the following steps:

1.  Define Key Metrics

2.  Setup Readiness Categories

3.  Define Readiness Factors

4.  Setup a Readiness Phase

5.  Set the Goals and Readiness Factors for a Phase

## Define Key Metrics

We have 5 key metrics which are tracked, and they will be provided within the
default set of data. When you have more, you can define your own key metrics. To
create a new key metric, follow the below steps:

1.  Select **Key Metrics** in the left pane and select **New**.

    ![A screenshot of a cell phone Description automatically generated](media/c20214ce90ef7c2fc5abc80990d8dc32.png)

2.  I n the **Key Metrics** page, specify a Name.

    ![](media/a8282fc2535b3537cabb00ef9a41bfe0.png)

| **Field** | **Description**           |
|-----------|---------------------------|
| Name      | A name for the Key Metric |

3.  Select **Save & Close**. The newly created record will be available in the
    **Active Key Metrics** list.

To edit the record, select the newly created record, update the values as
required, and select **Save & Close**.

## Setup Readiness Categories

Categories organize readiness factors. By default, we provide 6 categories, when
you want add a category, follow the below steps:

1.  Select **Categories** in the left pane and select **New**.

    ![A screenshot of a social media post Description automatically generated](media/b6c143054737add03e932bc8318b678e.png)

2.  In the New **Category** screen, specify a Category.

![](media/16a490b932a55eb1e857a694457a225e.png)

| **Field** | **Description**             |
|-----------|-----------------------------|
| Name      | A name for the new Category |

1.  Select **Save & Close**. The newly created record will be available in the
    **Active Categories** list.

To edit the record, select the newly created record, update the values as
required, and select **Save & Close**.

## Define Readiness Factors 

Readiness Factors will be used to check off when you want to move through
phases. By default, numerous readiness factors will be in the solution. When you
want more readiness factors, follow the below steps:

1.  Select Readiness Factors in the left pane and Select New.

![](media/9f5aa4fb744270d7b23c17dd3c9a0d2d.png)

>   A screenshot of a cell phone Description automatically generated

1.  In the New **Readiness Factor** screen specify the appropriate values:

![](media/24ebcf4480a814572f8fd2882ddc6413.png)

| **Field**   | **Description**                                                     |
|-------------|---------------------------------------------------------------------|
| Factor      | Type a name for your Factor                                         |
| Description | A description of your Readiness Factor.                             |
| Category    | Select the appropriate Category to assign to your Readiness Factor. |

1.  Select **Save & Close**. The newly created record will be available in the
    **Active Readiness Factors** list.

>   To edit the record, select the newly created record, update the values as
>   required, and select **Save & Close**.

## Setup a Reopen Phase

In your reopen plan you define a couple of phases through which a facility will
walk. The phases will be in the solution by default. If you want to add or edit
these phases, follow the following steps:

1.  Select **Reopen Phases** in the left pane and select **New**.

    ![A screenshot of a social media post Description automatically generated](media/d5f220cab773b922143d8e281896c774.png)

2.  In the **New Reopen Phase** page, specify the Index, Name, and Description:

    ![](media/efca16c7e05697b120b1c01c9c5538ac.png)

| **Field**     | **Description**                                                                                                                                       |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| Index         | Type a unique index number to establish where in the sequence of the phases that the new phase shall be placed                                        |
| Name          | Type a name for your new Reopen Phase                                                                                                                 |
| Description   | A description of your Readiness Factor.                                                                                                               |
| Process Stage | Select the appropriate Process Stage to assign to your new Reopen Phase. This identifies which stage in the business process flow should be activated |

3.  Select **Save & Close**. The newly created record will be available in the
    **Active Reopen Phases** list.

To edit the record, select the newly created record, update the values as
required, and select **Save & Close**.

## Set the Goals and Readiness Factors for a Phase

1.  Select **Reopen Phases** in the left pane and select the Reopen Phase for
    which you need to add a new goal (example below – “**Initial Return**”)

![](media/ca6543abbe4e992b16c2c78860c9491c.png)

1.  In the section “Key Metrics” select **+ New Goal.**

    ![A screenshot of a social media post Description automatically generated](media/23c6e70b07639de243577355d5164d5b.png)

2.  In the **Goals** page, specify the appropriate values:

![](media/c6f2e7cc86d46c064c2cf1417e88c069.png)

| **Field**    | **Description**                                |
|--------------|------------------------------------------------|
| Reopen Phase | Type a name for your Reopen Phase              |
| Key Metric   | Select a Key Metric for the goal.              |
| Type         | Select an appropriate goal type from the list: |
| Value        | Enter a numerical target value for the goal    |

-   Lower

-   Higher

-   Equal or Lower

-   Equal or Higher

1.  Select **Save & Close**. The newly created record will be available in the
    **Key Metrics** list.

To edit the record, select the newly created record, update the values as
required, and select **Save & Close**.

1.  To set Readiness Factors for your new Reopen phase select the **Readiness
    Factors** tab

![](media/b40ab14811ebed5267621bad0d8a0369.png)

1.  Select the button **Add Existing Readiness Factor**

![](media/69da9d109bbbeae76207ecd7e0dec3fd.png)

>   A screenshot of a cell phone Description automatically generated

1.  Select your desired Readiness Factor(s) to link to your new Reopen Phase.
    You can select multiple factors from the list prior to pressing the **Add**
    button.

![](media/cac7e1f784398d565a13fc62869f439f.png)

1.  Select the **Add** button to complete the selection process to link your
    selected **Readiness Factors** to your new **Reopen Phase**

![](media/c49264bf5cade8d3aac412355883d53f.png)

# Manage Facilities

Facilities are an important part of the Return to Workplace solution. Various
facility types are available like a building or conference center define the
types of facilities which are stored. The Business Admin has the responsibility
to manage Facility Types which shall include creating new and updating existing.
The facilities creation that is responsibility of the Facility Manager can be
supported by Business Admins through an import record process where needed.

When managing facilities, you will step through the following steps:

1.  Define Facility Types

2.  Import Facilities

## Define Facility Types

Facility types are defined as the types of facilities we support in the
solution. By default, two are provided as an example, you can define more by
following the following steps:

1.  Select **Facility Types** in the left pane and select **New**.

![](media/33cfe610f9bf9050dac90133eb04dc10.png)

>   A screenshot of a cell phone Description automatically generated

1.  In the New **Facility Type** screen, specify the appropriate values:

![](media/af1cb99b2734de0251863c5e4ec566fa.png)

| **Field**   | **Description**                     |
|-------------|-------------------------------------|
| Type        | A name for your type of Facility    |
| Description | A description of your Facility Type |

1.  Select **Save & Close**. The newly created record will be available in the
    **Active Facility Types** list.

To edit the record, select the newly created record, update the values as
required, and select **Save & Close**.

## Import Facilities 

The Facility sample data file is available in the deployment package (.zip).
When you extract the .zip file, the sample data files are available under the
**SampleData** folder.

**How to load Facility data from data files**

To load sample Facility data from the Excel file to the Facility entity:

1.  In the left navigation pane select **Facilities** (in the area of Facility
    Management)

2.  Select **Import from Excel** to select the Facilities data file

![](media/f623d079aa6bbc33443265ab38d9dcea.png)

>   A screenshot of a social media post Description automatically generated

1.  Browse to the **SampleData** folder and select the **Facilities.xlsx** file.
    Change this file according to your own needs and proceed with the wizard
    steps to import the data.

2.  After the sample data is imported, you will see the imported records in the
    entity:

![](media/7545d1af9f2e5dda47ae3642928c5943.png)

# Specify Solution Settings

The overall solution requires certain configurations to make sure that the user
has the correct guidance. Via solution settings, settings like contact emails or
attestations are configured. Via themes, it is possible to tailor the experience
of an employee according to the company branding.

When setting up the solution, you step through the following steps:

1.  Set Solution Settings

2.  Define Theming

## Set Solution Settings

Via Solution Settings you can tailor the experience for employees to match the
company guidelines and culture.

1.  Select **Settings** in the left pane and select **New**.

![](media/f7aec2cd9aca0f38f7ba6a60fbc8669e.png)

1.  In the New Setting screen, specify the appropriate values

![](media/3ea26c7508a4628c0346b27fb6044a9d.png)

Disclaimer: the following isn’t implemented yet; this will come in new releases.

## Define Theming

Theming allows you to change the experience of the employee.

1.  Select **Settings** and then **Customizations**.

![](media/e7a1660fd13d334c33563ba91aaf4e77.png)

1.  Under Customizations select **Themes**.

![](media/8a8b301ea23b309614018d79b50f71ce.png)

1.  From the list select the default theme.

![](media/9516b6b752bacadaaec4280dd687ec70.png)

1.  You can select the different colors from the theme.

![](media/911da9fe409af6e29bd2a9456469235e.png)

*Disclaimer*

*Customer bears the sole risk and responsibility for any use of this app.*

*Sample data included in this app are for illustration only and are fictitious.
No real association is intended or inferred.*
