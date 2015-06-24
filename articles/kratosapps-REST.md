<properties
	pageTitle="Access data using REST APIs in KratosApps Studio"
	description="Display data from Coursera, DropBox, Visual Studio Online, or your own REST API service in KratosApps."
	services="kratosapps"
	authors="AFTOwen"
 />

# Access data using a REST API in KratosApps #

Display data in KratosApps Studio by using REST API calls to retrieve information from another app. For example, display data from Coursera, DropBox, Visual Studio Online, or your own REST API service.

Apps that you build in KratosApps Studio access the data from a service using a WADL file. This WADL file is simply an XML file that tells your app how to access the REST based web service and the data that's returned. WADL files are created with a specific format based on the [WADL standard](http://www.w3.org/Submission/wadl/). Use basic or OAuth authentication, and pass parameters to the REST API calls from your app to customize the data that's returned. Specify these parameters when you design your app, or take them from the values of other fields in your app.

**Note:** If you're not sure how to use REST API calls, find a developer who can help you create a WADL file, [load it](#load-a-wadl-file-and-access-the-data), and then finish creating your app.

## Create a WADL file ##

Create a WADL file in any combination of these ways:

- Generate a WADL file by using [a tool](#generate-a-wadl-file).
- Copy and update [a sample WADL file](#modify-a-sample-wadl-file) to suit your needs.
- Add [one or more sections](#add-sections-manually) manually.

###Generate a WADL file###

This [WADL generator tool](https://gallery.technet.microsoft.com/WADL-Generator-for-Siena-7792b022) isn't supported but, in most situations, can generate a file for you much more quickly than creating it manually. You can start with a generated file and then modify it as necessary.

If the REST API service that you want to access uses OAuth to authenticate users, you'll often need to create an app for that service first. This step gives you the client ID that you need. You'll also need to provide a callback URL to the tool. This URL is just a placeholder because you're not authenticating from a web app, so simply provide a valid URL. This URL isn't used, but the WADL generator tool must be able to load the page.

1. Start the WADL generator, and create a WADL file that's named based on your service.

1. Add any functions that you want to use from your service.

	When you load the WADL file into KratosApps Studio, these functions will appear with the same names.

	For some REST services that use OAuth 2.0 authentication, you will get an error when you try out the function that you have added. In this case, paste a sample response into the tool that would be returned by this call to the REST API. Then save the function.

1. Export the generated WADL file, and save it as an .xml file to use from KratosApps Studio. 

	Don't forget to save a WADL generation file when you close the tool. That way, you can use the tool to add more functions in the future to your WADL file.

Look at a [sample WADL file](#sample-wadl-files) to review its structure.

[Load a WADL file and access the data](#load-a-wadl-file-and-access-the-data) in KratosApps Studio to confirm whether it behaves as you expect.

###Modify a sample WADL file###

You can create your own .xml file by copying the XML from a sample file for [Coursera](#sample-file-for-coursera) or [Dropbox](#sample-file-for-dropbox).

####Sample file for Coursera####

This WADL file is very basic, simply accessing course information from Coursera without any authentication.

	<?xml version="1.0" encoding="utf-16"?>
	<application xmlns:siena="http://schemas.microsoft.com/MicrosoftProjectSiena/WADL/2014/11" 
						xmlns:xs="http://www.w3.org/2001/XMLSchema" 
						xmlns:sienatool="http://www.todo.com" 
						siena:serviceId="CourseraREST" 
						xmlns="http://wadl.dev.java.net/2009/02">
	  <grammars>
		<siena:jsonTypes targetNamespace="http://www.todo.com" xmlns:wadl="http://wadl.dev.java.net/2009/02">
		  <siena:object name="GetCourses_Root">
			<siena:property name="elements" typeRef="GetCourses_elements_Array" />
			<siena:property name="linked" typeRef="GetCourses_linked_Object" />
		  </siena:object>
		  <siena:object name="GetCourses_elements_Object">
			<siena:property name="id" type="number" />
			<siena:property name="shortName" type="string" />
			<siena:property name="name" type="string" />
			<siena:property name="links" typeRef="GetCourses_links_Object" />
		  </siena:object>
		  <siena:object name="GetCourses_links_Object" />
		  <siena:array name="GetCourses_elements_Array" typeRef="GetCourses_elements_Object" />
		  <siena:object name="GetCourses_linked_Object" />
		</siena:jsonTypes>
	  </grammars>
	  <siena:authenticationProviders />
	  <siena:template />
	  <resources base="https://api.coursera.org">
		<resource path="api/catalog.v1/courses">
		  <method name="Get" id="GetCourses" siena:requiresAuthentication="false">
			<request />
			<response siena:resultForm="single">
			  <representation mediaType="application/json">
				<param name="GetCourses_Name" type="sienatool:GetCourses_Root" style="Plain" path="" />
			  </representation>
			</response>
		  </method>
		</resource>
	  </resources>
	</application>

####Sample file for Dropbox####

This file uses OAuth 2.0 authentication and contains two functions:

- GetFileAndFolderInfo gets the file and folder information from Dropbox for a specific folder
- DisplayImage gets the URL to display an image stored on Dropbox.

When you add items in KratosApps Studio that use these functions, you can specify the folder and the location for the image. These strings can be the text from another field in your app. That field could be data from a call to a REST API too.

	<?xml version="1.0" encoding="utf-16"?>
	<application xmlns:siena="http://schemas.microsoft.com/MicrosoftProjectSiena/WADL/2014/11" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:sienatool="http://www.todo.com" siena:serviceId="Dropbox" xmlns="http://wadl.dev.java.net/2009/02">
	  <grammars>
		<siena:jsonTypes targetNamespace="http://www.todo.com" xmlns:wadl="http://wadl.dev.java.net/2009/02">
		  <siena:object name="GetFileAndFolderInfo_Root">
			<siena:property name="read_only" type="boolean" />
			<siena:property name="hash" type="string" />
			<siena:property name="revision" type="number" />
			<siena:property name="bytes" type="number" />
			<siena:property name="thumb_exists" type="boolean" />
			<siena:property name="rev" type="string" />
			<siena:property name="modified" type="string" />
			<siena:property name="size" type="string" />
			<siena:property name="path" type="string" />
			<siena:property name="is_dir" type="boolean" />
			<siena:property name="modifier" type="string" />
			<siena:property name="root" type="string" />
			<siena:property name="contents" typeRef="GetFileAndFolderInfo_contents_Array" />
			<siena:property name="icon" type="string" />
		  </siena:object>
		  <siena:object name="GetFileAndFolderInfo_contents_Object">
			<siena:property name="rev" type="string" />
			<siena:property name="thumb_exists" type="boolean" />
			<siena:property name="path" type="string" />
			<siena:property name="is_dir" type="boolean" />
			<siena:property name="client_mtime" type="string" />
			<siena:property name="icon" type="string" />
			<siena:property name="read_only" type="boolean" />
			<siena:property name="modifier" type="string" />
			<siena:property name="bytes" type="number" />
			<siena:property name="modified" type="string" />
			<siena:property name="size" type="string" />
			<siena:property name="root" type="string" />
			<siena:property name="mime_type" type="string" />
			<siena:property name="revision" type="number" />
		  </siena:object>
		  <siena:array name="GetFileAndFolderInfo_contents_Array" typeRef="GetFileAndFolderInfo_contents_Object" />
		</siena:jsonTypes>
		<siena:jsonTypes targetNamespace="http://www.todo.com" xmlns:wadl="http://wadl.dev.java.net/2009/02">
		  <siena:object name="DisplayImage_Root">
			<siena:property name="url" type="string" dtype="hyperlink" />
			<siena:property name="expires" type="string" />
		  </siena:object>
		</siena:jsonTypes>
	  </grammars>
	  <resources base="https://api.dropbox.com" siena:authenticationProviderHref="#Dropbox_Auth">
		<resource path="1/metadata/auto/photos">
		  <method name="Get" id="GetFileAndFolderInfo" siena:requiresAuthentication="true">
			<request>
			  <param name="list" style="Query" required="true" siena:sampleDefault="true" />
			</request>
			<response siena:resultForm="single">
			  <representation mediaType="application/json">
				<param name="GetFileAndFolderInfo_Name" type="sienatool:GetFileAndFolderInfo_Root" style="plain" path="" />
			  </representation>
			</response>
		  </method>
		</resource>
	  </resources>
	  <resources base="https://api.dropbox.com" siena:authenticationProviderHref="#Dropbox_Auth">
		<resource path="1/media/auto/">
		  <method name="Get" id="DisplayImage" siena:requiresAuthentication="true">
			<request>
			  <param name="path" style="Query" required="true" siena:sampleDefault="/Photos/i-b858zMh-M.jpg" />
			</request>
			<response siena:resultForm="single">
			  <representation mediaType="application/json">
				<param name="DisplayImage_Name" type="sienatool:DisplayImage_Root" style="plain" path="" />
			  </representation>
			</response>
		  </method>
		</resource>
	  </resources>
	  <siena:authenticationProviders>
		<siena:oauth2 id="Dropbox_Auth">
		  <siena:grantType>
			<siena:implicit>
			  <siena:endpoints>
				<siena:authorization url="https://www.dropbox.com/1/oauth2/authorize" />
				<siena:callback url="https://fabrikam-prime-oauth.azurewebsites.net/" />
			  </siena:endpoints>
			  <siena:credentials clientId="[templated]" />
			</siena:implicit>
		  </siena:grantType>
		  <siena:resourceAuthorization placement="Query" />
		</siena:oauth2>
	  </siena:authenticationProviders>
	  <siena:template>
		<siena:variable name="Dropbox__ClientID">
		  <siena:doc title="Client ID/API Key" />
		  <siena:modifyAuth tag="credentials" href="#Dropbox_Auth" attribute="clientId" />
		</siena:variable>
		<siena:variable name="Dropbox__URI">
		  <siena:doc title="Redirect URI" />
		  <siena:modifyAuth tag="callback" href="#Dropbox_Auth" attribute="url" />
		</siena:variable>
	  </siena:template>
	</application>

###Add sections manually###

Each WADL file needs the following elements:

- &lt;application&gt; - the root element.
- &lt;grammars&gt; - defines formats of the returned data. 
- &lt;resources&gt; - contains the REST API call and any parameters for each method that you call. 
- &lt;siena:authenticationProviders&gt; - empty unless you need authentication to access the REST API.
- &lt;siena:template&gt; - provides the details for the authentication if it is required; otherwise, it's empty.

Some elements differ from or extend the [WADL standard](http://www.w3.org/Submission/wadl/) in ways that are specific to KratosApps Studio. These [differences and extensions](#differences-and-extensions) are described later in this topic. 

**&lt;application&gt;**

Add this root element to your XML file, but replace &lt;name-of-your-service&gt; with whatever your service is called. KratosApps Studio shows this name when you load your WADL file.

	<application xmlns:siena="http://schemas.microsoft.com/MicrosoftProjectSiena/WADL/2014/11" 
                                     xmlns:xs="http://www.w3.org/2001/XMLSchema"  
                                     siena:serviceId="<name-of-your-service>" 
                                     xmlns="http://wadl.dev.java.net/2009/02">
             <!-- Add the other elements here -->
	</application



###Differences and extensions###

## Load a WADL file and access the data ##