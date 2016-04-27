<properties
	pageTitle="Cost Estimator | Microsoft PowerApps"
	description="Step-by-step instructions for opening and running the Cost Estimator app."
	services=""
	suite="powerapps"
	documentationCenter="na"
	authors="linhtranms"
	manager="erikre"
	editor=""
	tags=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="04/11/2016"
   ms.author="litran"/>

# Open and run Cost Estimator #
In **Cost Estimator**, create an appointment for estimating the cost of installing a flooring product in a room of a particular size. Capture details such as address and square footage, and calculate the price based on discounts and tax rates. Filter a list of appointments to show those for which estimates have been created, for which estimates haven't been created, or all appointments.

## Open the app ##

1. Sign in to [powerapps.com](https://web.powerapps.com), and then select **Cost Estimator** in the list of sample apps.

	![Portal Homepage](./media/cost-estimator/portal-homepage.png)

1. Select **Phone** to show the app as it would look on a phone.

	The app is pre-populated with sample data to demonstrate the functionality of the app. It contains data for creating appointments and estimating the cost of installing a specific flooring product in a room of a particular size.

	![Portal Homepage](./media/cost-estimator/cost_estimator_home.png)

## Make and view an appointment ##

1. Select **+** to make an appointment for an estimate.

	![Portal Homepage](./media/cost-estimator/cost_estimator_add.png)

1. Provide details, and then select **Save job**.

	![Portal Homepage](./media/cost-estimator/cost_estimator_new.png)

	The appointment that you created appears in the list of appointments.

	![Portal Homepage](./media/cost-estimator/new_job_added.png)

1. Select an appointment, such as the one you created, to view its details, including a map of the location.

	![Portal Homepage](./media/cost-estimator/job_details.png)

	**Note**: You can delete an appointment by selecting the trash-can icon in the upper-right corner.
	![Portal Homepage](./media/cost-estimator/job_delete.png)

## Create an estimate ##
1. On the details page of an appointment, select **Begin Estimate**.

	![Portal Homepage](./media/cost-estimator/begin_estimate.png)

1. Provide required information about the room, such as its **Name**, **Length**, and **Width**, and then select **Select flooring style**.

	![Portal Homepage](./media/cost-estimator/dimensions.png)

	A list of categories for flooring products appears.

	![Portal Homepage](./media/cost-estimator/select_flooring_type.png)

1. Select **Carpet** > **Caserta Sky Grey**.

	![Portal Homepage](./media/cost-estimator/carpet.png)

1. If you're running the app on a device that has a camera, select **Take photos**.

	![Portal Homepage](./media/cost-estimator/add_photos.png)

1. Take one or more photos, and then select **Done**.

	![Portal Homepage](./media/cost-estimator/take_photos.png)

## Finish and submit an estimate ##

1. Select **Review Estimate**.

	![Portal Homepage](./media/cost-estimator/review_estimate.png)

1. (optional) Specify a **Price adjustment** and a **Tax** rate.

1. Add a signature, and then select **Submit estimate**.

	![Portal Homepage](./media/cost-estimator/submit_estimate.png)

	Your default mail client opens with a message that contains the estimate information.

	![Portal Homepage](./media/cost-estimator/email.png)

	In PowerApps, the screen indicates that an estimate has been sent.

	![Portal Homepage](./media/cost-estimator/done.png)

1. Select **Done** to return to the list of appointments.

	The appointment for the estimate that you just completed appears in green, which indicates that it's closed.

	![Portal Homepage](./media/cost-estimator/estimate_done.png)

1. (optional) Select the filter icon in the upper-left corner, and then filter the list by status (open or closed) or show all appointments.

### Other sample apps with sample data ###

- [Site Inspection](site-inspection.md)
- [Budget Tracker](budget-tracker.md)
- [Service Desk](service-desk.md)  
