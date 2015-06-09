![Microsoft][0]

# PowerApps

### Guide for Private Preview

May 2015

This document outlines the scenarios and capabilities of PowerApps in Private Preview.  Microsoft PowerApps is a fully managed SaaS offering for Business Optimizers which makes designing, creating, acquiring, and sharing mobile apps easy using PowerPoint and Excel-like skills without relying on developer or IT help.

# 1. Welcome to PowerApps

Today's workforce requires experiences that enterprise business applications and LOB systems can't provide. This challenge, along with the growth and maturity of Cloud and SaaS as pillars of modern apps, has given rise to the proliferation of SaaS solutions.

PowerApps help everyone work more productively on mobile devices. It is a fully managed SaaS offering that helps Business Optimizers design, create, acquire, and share mobile apps using only PowerPoint and Excel-like skills, not help from a developer or IT.

![PowerApps tools][1]

PowerApps offers the following tools and services:

- **PowerApps Portal**: In the Portal, you can browse pre-made apps, apps that you've published, and apps that others have shared with you. You can also download an app to run on a local device, share an app with others, and perform other management tasks.
- **PowerApps Player**: In the Player, you can run an app on either Windows or iOS and share an app with others.
- **PowerApps Studio**: In the Studio, you can create or update an app, publish it to the Portal for your own use, and share the app with others.

**Compatibility**

| &nbsp; | PowerApps Portal | PowerApps Player | PowerApps Studio |
| --- | --- | --- | --- |
| A laptop or a desktop computer that's running 32-bit Windows 8.1, 64-bit Windows 8.1, or Windows 10 Technical Preview | Yes | Yes | Yes |
| An iPad or an iPhone that's running iOS 8.2 or later | Yes | Yes | No |
| Any device with a browser | Yes | No | No |

# 2. Setup

**First time registration**

1. Register using your org-id (work email account) at [https://portal.kratosapps.com/](https://portal.kratosapps.com/). If your organization has never registered with PowerApps, you will see the following screen:
	
	![Register using your org-id][2]

2. Click **Accept**. You will land on a page like below. Please copy the information in the table (Tenant ID and your email address) and send an email to [cfang@microsoft.com](mailto:cfang@microsoft.com) to have your organization whitelisted to access PowerApps. Whitelisting will complete in 72 hours.
	
	![Thanks for your interest][3]

**Subsequent registrations**

2. Sign in using your org-id work account from a browser at [the PowerApps homepage](https://www.kratosapps.com/) ([https://www.kratosapps.com/](https://www.kratosapps.com/)). 
	
	![Sign in using your org-id][4]

3. Click on **Try it now** to sign up. 
	
	![Try it now][5]

4. (optional) Add the email addresses of people who might want to try PowerApps. You can skip if you don't want to add more users now.

	**Note:** This option appears only the first time that you sign in.
	
	![Invite cooworkers][6]

5. Navigate to the [downloads page](http://www.kratosapps.com/en-us/downloads/) to acquire the installer or do the following:

	1. To install the Studio and the Player on Windows, click [this link](http://www.kratosapps.com/files/PowerAppsPreviewInstaller.exe), follow the prompts in the wizard that appears, and then wait a few minutes for the installation to finish. When the installation finishes, you can open the Studio and the Player from the Start screen.

		![Installing PowerApps][7]

		> [AZURE.NOTE] The PowerApps installer will replace any previous versions of the Studio or Player

	2. To install the Player on iOS we use Apple's TestFlight. Navigate to [https://www.kratosapps.com/en-us/downloads/](http://www.kratosapps.com/en-us/downloads/) and enter your Apple ID. You should receive an email invitation in 1-2 business days.  

		iOS devices registered with this ID can be used to run the PowerApps Player using TestFlight.
		
		![Microsoft invited you to test PowerApps on iOS][8]

		From the iOS device, click on **Open in TestFlight** and follow the steps to install TestFlight app. Open the TestFlight app and you should see instructions to install the PowerApps Player.

		![Install PowerApps on iOS][9]

# 3. Install & run an app

1. Sign in to the PowerApps homepage, and then click **App Gallery** to show pre-made apps that you can install, run, modify, and publish.

	![PowerApps app Gallery][10]

2. Click **Kudos Phone**, click **Install**, and then wait up to five minutes for the installation to finish.

	When you install an app from the App Gallery, that app become available for you to download and run on a local device on which you've installed the Player.

	![Install Kudos Phone app][11]

3. Click **My Apps** to show the list of apps that you can download and run in the Player.

	You can download and run apps that you created and published and apps that others have created, published, and shared with you.

	![Apps installed by me][12]

4. Under either **Apps installed by me** or **Apps shared with me**, click the ellipsis (…), and then click **Open**
	
	![Open an installed app][13]

5. When your browser prompts you, click **Allow**. 

	![Allow to open an app on your computer][14]

6. If you've never used the Player before, sign in by using the same credentials that you use to sign in to the Portal.

	![Connecting to a service][15]

7. Click Yes to confirm that you want to download the app. 

	![Are you sure you want to download this app][16]

	After the app is downloaded, it runs automatically in the Player.

	To show a list of apps that you've downloaded to the Player, show the navigation bar by swiping down from the top (or right-clicking anywhere), and then click the Back arrow.

# 4. Create and publish an app (Windows only)

In the Studio, you can create your own app from nothing, publish it to the Portal, and share the app with others. To more quickly understand the process, you'll download a sample app, modify it slightly, and then publish and share it.

1. Download the compressed file for the [TravelTranslator](https://gallery.technet.microsoft.com/Siena-Travel-Translator-7681ab27), extract its contents to a location that you can remember, and then open the Studio.

	![PowerApps Studio][17]

2. Click on File > Open, and then click **Browse**.  

	![Open file][18]

3. Browse to the location where you extracted the contents of the compressed file, and then open the TravelTranslator folder.

4. Click TravelTranslator.siena, and then click **Open**.

	![Opened TravelTranslator][19]

	The app opens in the design workspace, where you can create or update an app by adding and configuring UI elements, called controls or visuals. However, not all functions work in the design workspace, so you'll open Preview so that you can briefly explore how TravelTranslator works.

5. Press the Play button on the top right or F5 to open **Preview**, choose a language from the list in the big blue arrow, and then write some text in the top pane of the app.

	In the lower-left pane, your text appears as typed English words. In the lower-right pane, your text is translated into the language that you specified.

	![TravelTranslator demo][20]

6. Press Esc to return to the design workspace. 

**Update and publish an app**

1. Open TravelTranslator, as the previous procedure describes.
2. Click the lower-left pane, click **Fill** on the **Home** tab, and then click a fairly light color.

	The background of the pane changes to the color that you specified.

3. Press Ctrl-S to save your change, click **Sign in** near the upper-right corner of the Studio, and then provide your credentials.

	**Note:** You must sign in to publish an app to the Portal.

	![Connecting to a service][21]

4. Do one of the following:

	1. To convert written text to typed text and then translate it:

		1. Register your application for [a Client ID and Client Secret](http://blogs.msdn.com/b/translation/p/gettingstarted1.aspx) for BingTranslator.

			**Note**: you MUST create a registered application in Azure Data Marketplace to generate the correct Client ID and Secret for the online translation to work

		2. In the Studio, go the **File** menu, click **App Settings** in the left navigation bar, and then click **BingTranslator** under **Service keys** in the right pane.
    
		3. Specify your Client ID and Client Secret, and then click **Apply**.
		
			![All services successfully updated to use unique keys][22]

	2. To just convert written text to typed text:
    
		1. Press File menu go to **Data Sources**, and then click **BingTranslator** under **Existing sources.** 
    
		2. Delete that data source by clicking the trash-can icon, and then press Esc.

5. From the File menu, click **Publish** in the left navigation bar.

	![Publish to PowerApps][23]

6. In the text box, give your updated app a distinct name, select the check box to download and include media files, and then click **Publish**.

	![Publishing in PowerApps][24]

	After a few seconds, a toast notification confirms that the app has finished publishing.

	![App was successfully published to PowerApps][25]

7. (optional) Confirm that the app you published appears under **My Apps** in the Portal, [install your app](), and then test drive it.

	![Your new app was installed][26]

# 5. Update and republish an app (Windows only)

1. Open the app in the Studio:

	- From the Studio, open the app as the previous section describes.
	- From the Player, open the app by performing these steps:

		1. Run the app by clicking it or by clicking the ellipsis (...) and then clicking **Open**.

			![Runn the app][27]

		2. Show the navigation bar (by swiping down from the top or right-clicking anywhere), and then click the Edit icon near the right edge.

			![Show the navigation bar][28]

			The app opens in the Studio.

2. Change the **Fill** of the box that contains translated text. 

	![Change the Fill of the box that contains translated text][29]

3. Publish the app again, as described earlier in this guide, and then wait a couple of minutes for the Player to be updated.

4. In the Player, click the Refresh icon, click the update icon that appears in the app, and then click **Yes** when prompted to update the app.

	![Click the update icon][30]

When the app is updated, it runs automatically.

# 6. Share an app

One of the cool features in PowerApps is the ability to share the apps you create with your co-workers. The ability to share apps enables others to know and use your app and given feedback. Sharing apps sends an email to the users with a link to download the app.

> [AZURE.NOTE] You can share apps from the PowerApps Studio, Portal or the Player

**Sharing from the Player**

Apps can be shared from the Player after they have be downloaded locally. Click the ellipsis (…), and then choose **Share**

![Share an app][31]

From the Share dialog, enter email address, customize the Subject and/or the Message and click **Share**:

![Share dialog][32]

**Share apps from the Portal**

You can share apps that you own from the My Apps view. Click the ellipsis (…), and then choose **Share**

![Share an app that you own][33]

In the Share dialog, enter email addresses, customize the Subject and/or the Message and click **Share**.

![Share dialog][34]

**Share apps from the Studio**

Sharing is available for apps after they are published from the Studio. From the File menu, choose the **Share** option. Enter the email addresses, customize the subject and/or the message, and then click **Share.**

![Share an app from the Studio][35]

A message confirms that the app is shared.

![Shared succeeded][36]

You can edit the permissions assigned to a user from any of the above tools. For example, from the Studio, click the name of a user with whom the app is shared, and then modify the permissions for that user.

![Edit permissions on a shared app][37]

# 7. Use API Apps

You can easily connect an app to popular SaaS and Enterprise platforms by using API Apps. Refer to more details [here](http://azure.microsoft.com/en-us/services/app-service/api/). PowerApps can harness the power of API Apps by exposing the APIs in the Studio.

1. On the **File** menu, click **New Phone App**.

	On the **File** menu, click **Data Sources**, and then click **Show ApiApps**

	![Show apiApps from DataSources][38]

2. If you haven't signed-in using your work account, enter your credentials.

3. In the list of ApiApps, click **Deploy** on the ApiApp that you want to use.

	![Deploy on the ApiApp][39]

	> [AZURE.NOTE] An ApiApp can take up to five minutes to deploy.

	A toast notification confirms that you deployed the ApiApp.

	![Successfully deployed ApiApp][40]

	The ApiApps section shows the status of the API App as deployed.

	![ApiApp Deployed][41]


4. Under **Existing Sources**, click **Geolocation**, click **Add data**, and then press Esc to return to the design workspace.

5. On the **Insert** tab, click **Label**.

	![Insert label][42]

6. Click the label that you just added, and then set its **Text** property to this 

		GeoLocation!Address\_Lookup(Location!Latitude,Location!Longitude)

	![GeoLocation!Address\_Lookup(Location!Latitude,Location!Longitude)][43]

7. If prompted, click **Allow**.

	The label shows the address of your current location.

	![The label shows the address of your current location][44]

# 8. Delete an app

You can delete an app from the Player and uninstall the app from the Portal.

- If you delete an app from the Player, you can download the app again from the Portal and run the app.
- If you uninstall an app from the Portal, you must republish it again from the Studio and download it to the Player before you can run that app. 

To delete an installed app from the Player, click the ellipsis (…), and then click **Delete**.

![Delete an installed App][45]

> [AZURE.NOTE] If the ellipsis (…) doesn't appear in an app, it may not have been downloaded to the Player

To uninstall an app from the Portal, click the ellipsis (…), and then choose **Uninstall**.

![Uninstall from the Portal][46]

Confirm uninstallation of the app by typing or pasting the name of the app in the text box and then clicking **Yes**.

![Confirm uninstallation][47]

# 9. Sending feedback

You can send feedback to the product team from the PowerApps Studio, PowerApps Player or the PowerApps Portal.

In the Portal, click the Support tab, and then enter your feedback and contact information.

![Support tab on the PowerApps Portal][48]

The Studio and the Player have a smiley icon to send feedback. Choose the smiley icon from the top-right navigation bar, and submit a smile or a frown.

> [AZURE.NOTE] You must sign in before you use the feedback option.

![Send a smile or a frown][49]

After clicking the smile or frown icon, you can enter the feedback and submit.

![Feedback submit][50]


# 10. FAQs

- **How can I submit an idea/feature that is not present in the current release of PowerApps?** 

	Thanks for noticing! You can file your feedback using any of the options above or alternatively email your TAP buddy.

- **Who can I reach to get help on the app I am building?** 

	Connect with your assigned PM contact for private preview. If you don't have a contact, you can email Claire Fang ( [cfang@microsoft.com](mailto:cfang@microsoft.com))

- **I ran into a setup error, how should I proceed?** 

	It is recommended you uninstall Project Siena or any previous versions of PowerApps. If the problem persists contact your TAP buddy.

- **I am unable to retrieve my ApiApp. How should I proceed?** 

	Check if you are logged in with your work account in PowerApps Studio and then try again.

- **I am unable to publish**** an app or unable to use an ****ApiApps, how should I proceed?** 

	You may not have registered for PowerApps. Go to www.kratosapps.com, and click on "Try it Now". Once you are done, you can retry in the Studio.

- **I am unable to register with my work email account, what should I do?** 

	We require an org-ID to register with PowerApps. If you have an o365 account, you automatically have an org-ID. If you don't, you can sign up for an Azure trial account at [http://www.azure.com](http://www.azure.com) using your work email account.

	
[0]: ./media/overview-get-started/microsoft.png
[1]: ./media/overview-get-started/power-apps-tools.png
[2]: ./media/overview-get-started/kratosapps-register.png
[3]: ./media/overview-get-started/kratosapps-register-completed.png
[4]: ./media/overview-get-started/kratosapps-sign-in.png
[5]: ./media/overview-get-started/kratosapps-try-now.png
[6]: ./media/overview-get-started/kratosapps-invite-coworkers.png
[7]: ./media/overview-get-started/installing-power-apps.png
[8]: ./media/overview-get-started/ios-test-power-apps.png
[9]: ./media/overview-get-started/ios-installing-power-apps.png
[10]: ./media/overview-get-started/power-apps-portal-gallery.png
[11]: ./media/overview-get-started/install-kudos-phone.png
[12]: ./media/overview-get-started/apps-installed-by-me.png
[13]: ./media/overview-get-started/open-an-installed-app.png
[14]: ./media/overview-get-started/allow-open-app.png
[15]: ./media/overview-get-started/connecting-to-service.png
[16]: ./media/overview-get-started/acept-download.png
[17]: ./media/overview-get-started/power-apps-studio.png
[18]: ./media/overview-get-started/open-file.png
[19]: ./media/overview-get-started/opened-travel-translator.png
[20]: ./media/overview-get-started/travel-translator-demo.png
[21]: ./media/overview-get-started/connecting-to-service-2.png
[22]: ./media/overview-get-started/service-keys.png
[23]: ./media/overview-get-started/publish-to-power-apps.png
[24]: ./media/overview-get-started/publishing-to-power-apps.png
[25]: ./media/overview-get-started/successfully-published.png
[26]: ./media/overview-get-started/new-app-installed.png
[27]: ./media/overview-get-started/run-app.png
[28]: ./media/overview-get-started/show-navigation-bar.png
[29]: ./media/overview-get-started/change-fill-of-box.png
[30]: ./media/overview-get-started/click-update-icon.png
[31]: ./media/overview-get-started/share-app.png
[32]: ./media/overview-get-started/share-dialog.png
[33]: ./media/overview-get-started/share-app-from-portal.png
[34]: ./media/overview-get-started/share-dialog-from-portal.png
[35]: ./media/overview-get-started/share-app-from-studio.png
[36]: ./media/overview-get-started/shared-succedeed.png
[37]: ./media/overview-get-started/edit-permissions-on-shared.png