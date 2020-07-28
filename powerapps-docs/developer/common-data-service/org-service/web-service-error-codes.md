---
title: "Web service error codes (Common Data Service) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This topic lists the error codes you might encounter when you debug your code. " # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 07/28/2020
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "JimDaly" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Web service error codes

This topic lists the error codes you might encounter when you debug your code.

<a name="BKMK_CRMErrors"></a>   

## Common Data Service Errors 

 The following list shows the error codes used in Common Data Service. For more information about handling errors, see [Handle exceptions in your code](handle-exceptions-code.md).  

> [!div class="mx-tdBreakAll"]
>
> |Error name|Values|Message|
> |---|---|---|
> |AADError|0x80072559, -2147015335|Error from AAD|
> |AadGroupTeamsCanOnlyAssignInheritableRoles|0x80048350, -2147187888|Cannot assign security role with "Team Privileges only" Inheritance to AAD Group or Office Group teams. (TeamId = {0})|
> |AccessDenied|0x80048405, -2147187707|Access is denied.|
> |AccessDeniedSharePointRecord|0x80060904, -2147088124|Access denied on SharePoint record in Dynamics 365.|
> |AccessTokenExpired|0x8005F101, -2147094271|The requested resource requires authentication.|
> |AccountDoesNotExist|0x80040502, -2147220222|Account does not exist.|
> |AccountLoopBeingCreated|0x80040507, -2147220217|Creating this parental association would create a loop in Accounts hierarchy.|
> |AccountLoopExists|0x80040506, -2147220218|Loop exists in the accounts hierarchy.|
> |ActionCardDisabledError|0x80071100, -2147020544|Action Card feature is not enabled.|
> |ActionCardInvalidStateCodeException|0x80071103, -2147020541|Invalid state code passed in expression.|
> |ActionStepInvalidPipelineStageid|0x8006040e, -2147089394|ActionStep references invalid Pipeline Stage Id.|
> |ActionStepInvalidProcessAction|0x8006041c, -2147089380|ActionStep {0} references invalid Process Action {1}.|
> |ActionStepInvalidProcessid|0x8006040d, -2147089395|ActionStep references invalid Process Id.|
> |ActionStepInvalidStageid|0x8006040c, -2147089396|ActionStep references invalid Stage Id.|
> |ActionSupportNotEnabled|0x80060382, -2147089534| Business Processes containing an Action Step cannot be exported because Action Step support is still a Public Preview feature and it is not currently enabled for this organization.|
> |ActivePropertyValidationFailed|0x80061001, -2147086335|You can't create a property instance for an inactive property.|
> |ActiveQueueItemAlreadyExists|0x80040526, -2147220186|An active queue item already exists for the given object. Cannot create more than one active queue item for this object.|
> |ActiveSlaCannotEdit|0x8004F871, -2147157903|You can't edit an active SLA. Deactivate the SLA, and then try editing it.|
> |ActiveStageIdDoesNotMatchLastStageInTraversedPath|0x80060455, -2147089323|Active Stage ID ‘{0}’ does not match last Stage ID in Traversed Path ‘{1}’. Please contact your system administrator.|
> |ActiveStageIDIsNull|0x80060449, -2147089335|Error updating the Business Process: Active Stage ID cannot be empty.|
> |ActiveStageIsNotOnLeadEntity|0x80100002, -2146435070|Active stage is not on 'Lead' entity.|
> |ActivityAnalysisOrganizationUpdateError|0x80044275, -2147204491|Relationship Analytics organization setting can only be enabled if Relationship Analytics solution is installed.|
> |ActivityCannotHaveRelatedActivities|0x8004F121, -2147159775|A custom entity defined as an activity must not have a relationship with Activities.|
> |ActivityEntityCannotBeActivityParty|0x80048501, -2147187455|An activity entity cannot be also an activity party|
> |ActivityInvalidObjectTypeCode|0x80043513, -2147207917|An Invalid type code was specified by the throwing method|
> |ActivityInvalidSessionToken|0x80043512, -2147207918|An Invalid session token was passed into the throwing method|
> |ActivityMetadataUpdate|0x8004F126, -2147159770|The metadata specified for activity is invalid.|
> |ActivityMustHaveRelatedNotes|0x8004F123, -2147159773|A custom entity defined as an activity must have a relationship to Notes by default.|
> |ActivityNotSupported|0x80090415, -2146892779|Activity is not supported in your organization. Unable to process Entity {0} with IsActivity={1} and IsActivityParty={2}.|
> |ActivityPartyObjectTypeNotAllowed|0x80043506, -2147207930|Cannot create activity party of specified object type.|
> |AdlsServiceConfigurationInvalidData|0x80090200, -2146893312|Configuration data for CDS ADLS service client is invalid. Setting: {0}, value :{1}.|
> |AdlsServiceConfigurationMissingData|0x80090201, -2146893311|Configuration data missing for CDS ADLS service. Setting: {0}.|
> |AdminProfileCannotBeEditedOrDeleted|0x8004F50C, -2147158772|The System Administrator field security profile cannot be modified or deleted.|
> |ADResourceNotFound|0x80041d68, -2147213976|The Azure AD Group was not found in your Azure Active Directory. Please validate the Group ID and try again.|
> |AdvancedSimilarityAzureSearchUnexpectedError|0x80061696, -2147084650|An unexpected error occurred executing the search. Try again later.|
> |AggregateInnerQuery|0x8004D2B1, -2147167567|The Inner Query must not be an aggregate query.|
> |AggregateQueryRecordLimitExceeded|0x8004E023, -2147164125|The maximum record limit is exceeded. Reduce the number of records.|
> |AlreadyLinkedToAnotherAttribute|0x8004F0FE, -2147159810|Given linked attribute is alreadly linked to other attribute.|
> |AppConfigFeatureNotEnabled|0x80072200, -2147016192|In-App Customization App Configuration feature is not enabled.|
> |AppEntityLimitExceeded|0x80048547, -2147187385|This operation failed since it exceeded the maximum entity limit of {0} total entities for the app {1} set by its owning publisher {2}.|
> |AppEntityLimitExceededInSiteMap|0x80048552, -2147187374|You cannot save or publish the sitemap. The publisher ({0}) of the app ({1}) allows only up to {2} additional entities to be added.|
> |ApplicationMetadataConverterFailed|0x8005F231, -2147093967|Sorry, something went wrong. Please try again, or restart the app.|
> |ApplicationMetadatadaCreateFailed|0x8005F233, -2147093965|Sorry, something went wrong. Please try again, or restart the app.|
> |ApplicationMetadatadaNullData|0x8005F232, -2147093966|Sorry, something went wrong. Please try again, or restart the app.|
> |ApplicationMetadatadaUpdateFailed|0x8005F234, -2147093964|Sorry, something went wrong. Please try again, or restart the app.|
> |ApplicationMetadataFailedWithContinue|0x8005F241, -2147093951|There was a problem with the server configuration changes.  You can continue using the application, but may experience difficulties, including the inability to save changes. Please contact your Dynamics 365 administrator and give them the information available in ‘more information’.|
> |ApplicationMetadataGetPreviewMetadataUnknownError|0x8005F230, -2147093968|Sorry, something went wrong. Please try again, or restart the app.|
> |ApplicationMetadataPrepareCustomizationsAppLock|0x8005F237, -2147093961|We encountered some issues when we tried to prepare your customizations for your users. Users on some clients won't be able to download your customization updates until this issue is resolved.|
> |ApplicationMetadataPrepareCustomizationsRetrieverError|0x8005F235, -2147093963|There was a problem with the server configuration changes.  Users can continue using the application, but may experience difficulties, including the inability to save changes.|
> |ApplicationMetadataPrepareCustomizationsTimeout|0x8005F236, -2147093962|Sorry, but your client customization changes could not be processed.  This may be due to a large number of entities enabled for your users, or the number of languages enabled.  Users will not receive customizations until this issue is resolved.|
> |ApplicationMetadataPrepareCustomizationsUnknownError|0x8005F226, -2147093978|Sorry, something went wrong. Please try again, or restart the app.|
> |ApplicationMetadataRetrieveUnknownError|0x8005F229, -2147093975|Sorry, something went wrong. Please try again, or restart the app.|
> |ApplicationMetadataRetrieveUserContextUnknownError|0x8005F227, -2147093977|Sorry, something went wrong. Please try again, or restart the app.|
> |ApplicationMetadataSyncAppLock|0x8005F244, -2147093948|Sorry, your server is busy so configurations can’t be downloaded right now. Your changes should be available in a few minutes.  Wait a few minutes, and sign in again.|
> |ApplicationMetadataSyncAppLockWithContinue|0x8005F245, -2147093947|Sorry, your server is busy so configuration changes can’t be downloaded right now. Your changes should be available in a few minutes.  In the meantime, you can continue using the app, and you’ll be reminded later to try downloading the changes. Or, you can wait a few minutes, restart the app, and accept the prompt to try again.|
> |ApplicationMetadataSyncFailed|0x8005F240, -2147093952|There was a problem with the server configuration changes.  We are unable to load the application, please contact your Dynamics 365 administrator.|
> |ApplicationMetadataSyncTimeout|0x8005F242, -2147093950|Sorry, but your server configuration changes could not be downloaded.  This may be due to a slow connection, or due to a large number of entities enabled for mobile use.  Please verify your connection and try again.  If this issue continues please contact your Dynamics 365 administrator.|
> |ApplicationMetadataSyncTimeoutWithContinue|0x8005F243, -2147093949|Sorry, but your server configuration changes could not be downloaded.  This may be due to a slow connection, or due to a large number of entities enabled for mobile use.  Please verify your connection and try again. You can continue to use the app with the older configuration, however you may experience problems including errors when saving.  If this issue continues please contact your Dynamics 365 administrator.|
> |ApplicationMetadataSyncUnknownError|0x8005F228, -2147093976|Sorry, something went wrong. Please try again, or restart the app.|
> |ApplicationMetadataUserValidationUnknownError|0x8005F225, -2147093979|Sorry, something went wrong. Please try again, or restart the app.|
> |ApplicationNotRegisteredWithDeployment|0x80041d49, -2147214007|Application needs to be registered and enabled at deployment level before it can be created for this organization|
> |ApplicationProfileMustContainEntity|0x80071131, -2147020495|The application profile must contain at least one entity.|
> |ApplicationUserCannotBeUpdated|0x80041d48, -2147214008|The user representing an OAuth application cannot not be updated|
> |ApplicationUserCannotChangeAccessMode|0x80040d40, -2147218112|An application user's access mode cannot be changed.|
> |AppLockTimeout|0x8004Ed47, -2147160761|Timeout expired before applock could be acquired.|
> |ApplyActiveSLAOnly|0x80055001, -2147135487|You can only apply active service level agreements (SLAs) to cases.|
> |AppModuleCannotHaveMorethanOneUnifiedApps|0x80050107, -2147155705|'{0}' app cannot be associated to more than one unified app. Please save the app and try again.|
> |AppModuleCannotHaveMorethanOneUnifiedAppsDuringImport|0x80050105, -2147155707|'{0}' app cannot be associated to more than one unified app. Please save this app in the designer and try again.|
> |AppModuleComponentEntityMustHaveFormOrView|0x80050115, -2147155691|The entity “{0}” must have at least one form or view in the app.|
> |AppModuleFeatureNotEnabled|0x80050117, -2147155689|The feature isn’t turned on for this organization.|
> |AppModuleMustHaveOnlyValidClientEntity|0x8005012A, -2147155670|The “{0}” entity isn’t valid for the chosen client, and won’t be shown at runtime.|
> |AppModuleNotContainMOCAEnabledEntity|0x80050118, -2147155688|App Module with MOCA as a supported client should have at least one MOCA enabled entity|
> |AppModuleNotReferEntity|0x8005011D, -2147155683|App Module does not reference at least one entity|
> |AppModulesImportError|0x80050123, -2147155677|An error occurred while importing App Modules|
> |AppModuleWithClientExists|0x80050127, -2147155673|Couldn’t create the app. There’s already an app for this client type.|
> |AppointmentDeleted|0x8004E106, -2147163898|The appointment entity instance is already deleted.|
> |AppointmentScheduleNotSet|0x80040275, -2147220875|Scheduled End and Scheduled Start must be set for Appointments in order to sync with Outlook.|
> |ArgumentDirectionMismatch|0x80060388, -2147089528|Direction mismatch for argument {0}.|
> |ArgumentTypeMismatch|0x80060387, -2147089529|Type mismatch for argument {0}.|
> |ArrayMappingFoundForSingletonParameter|0x8004037f, -2147220609|An array transformation parameter mapping is defined for a single parameter.|
> |ArticleIsPublished|0x800404fe, -2147220226|The article cannot be updated or deleted because it is in published state|
> |AssociateProductFailureDifferentUom|0x80061040, -2147086272|The product can't be added to the bundle. You have to use a product unit that belongs to the unit group of the product.|
> |AssociationRoleOrdinalInvalid|0x80048468, -2147187608|The association role ordinal is not valid - it must be 1 or 2.|
> |AsyncAssignOperationOngoing|0x80048555, -2147187371|This entity is currently being assigned as part of an asynchronous cascade assign job. Please wait for the asynchronous job to complete before attempting to assign this entity again. (EntityId: {0}, EntityName: {1}, AsyncJobName: {2}, AsyncJobId: {3}, AsyncAssignOperationId: {4})|
> |AsyncCommunicationError|0x80044307, -2147204345|A communication error occurred while processing the async operation.|
> |AsyncDeleteOperationOngoing|0x80048549, -2147187383|This entity is currently being deleted as part of an asynchronous cascade delete job. Please wait for the asynchronous job to complete before attempting to delete this entity again. (EntityId: {0}, EntityName: {1}, AsyncJobName: {2}, AsyncJobId: {3}, AsyncDeleteOperationId: {4})|
> |AsyncNetworkError|0x80044306, -2147204346|An error occurred while accessing the network.|
> |AsyncOperationCannotCancel|0x80044F00, -2147201280|This system job cannot be canceled.|
> |AsyncOperationCannotDeleteUnlessCompleted|0x8004416a, -2147204758|Cannot delete async operation unless it is in Completed state.|
> |AsyncOperationCannotPause|0x80044F01, -2147201279|This system job cannot be paused.|
> |AsyncOperationCannotUpdateNonrecurring|0x80044168, -2147204760|Cannot update recurrence pattern for a job that is not recurring.|
> |AsyncOperationCannotUpdateRecurring|0x80044169, -2147204759|Cannot update recurrence pattern for a job type that is not supported.|
> |AsyncOperationInvalidStateChange|0x80044162, -2147204766|The target state could not be set because the state transition is not valid.|
> |AsyncOperationInvalidStateChangeToComplete|0x80044165, -2147204763|The target state could not be set to complete because the state transition is not valid.|
> |AsyncOperationInvalidStateChangeToReady|0x80044166, -2147204762|The target state could not be set to ready because the state transition is not valid.|
> |AsyncOperationInvalidStateChangeToSuspended|0x80044167, -2147204761|The target state could not be set to suspended because the state transition is not valid.|
> |AsyncOperationInvalidStateChangeUnexpected|0x80044163, -2147204765|The target state could not be set because the state was changed by another process.|
> |AsyncOperationMissingId|0x80044164, -2147204764|The AsyncOperationId is required to do the update.|
> |AsyncOperationPostponed|0x80040328, -2147220696|This operation has been postponed because it failed for more than {0} times in {1} minutes|
> |AsyncOperationPostponedByExceptionCountThrottle|0x80060917, -2147088105|Currently, we are unable to complete this action. It has been postponed. We will try again later.|
> |AsyncOperationSuspendedOrLocked|0x80040339, -2147220679|>A background job associated with this import is either suspended or locked. In order to delete this import, in the Workplace, click Imports, open the import, click System Jobs, and resume any suspended jobs.|
> |AsyncOperationTypeIsNotRecognized|0x80044303, -2147204349|The operation type of the async operation was not recognized.|
> |AsyncOperationTypeThrottled|0x80060916, -2147088106|The job could not be completed because the server is busy. We will retry the job again soon.|
> |AttachmentBlocked|0x80043e09, -2147205623|The attachment is either not a valid type or is too large. It cannot be uploaded or downloaded.|
> |AttachmentInvalidFileName|0x80044a08, -2147202552|Attachment file name contains invalid characters.|
> |AttachmentNotFound|0x80048493, -2147187565|The reference to the attachment couldn't be found.|
> |AttachmentNotRelatedToEmail|0x80050006, -2147155962|This attachment does not belong to an email.|
> |AttributeCannotBeUpdated|0x80060413, -2147089389|Attribute - {0} cannot be updated for a Business Process Flow|
> |AttributeCannotBeUsedInAggregate|0x80060559, -2147089063|The {0} attribute cannot be used with an aggregation function in a formula.|
> |AttributeCreateUnsupportedTable|0x80090419, -2146892775|"Can't add an attribute to entity '{0}', it's not supported."|
> |AttributeDataTypeNotSupported|0x80090410, -2146892784|Attribute {0} of Entity {1} cannot be processed because the attribute data type {2} is not supported in your organization.|
> |AttributeDeprecated|0x80044335, -2147204299|"Attribute '{0}' on entity '{1}' is deprecated."|
> |AttributeDoesNotSupportLocalizedLabels|0x80044198, -2147204712|The specified attribute does not support localized labels.|
> |AttributeFormulaDefinitionIsEmpty|0x80060439, -2147089351|The formula is empty.|
> |AttributeIsNotCustomAttribute|0x80047009, -2147192823|The specified attribute is not a custom attribute|
> |AttributeIsNotFacetable|0x80060305, -2147089659|Cannot set user search facets for entity {0} as attribute {1} is not facetable. Kindly remove it from the list to proceed.|
> |AttributeMapHasAnUnmanagedBaseInstance|0x8004F223, -2147159517|An AttributeMap, with Id: {0}, between attribute {1} and {2} of entity {3} and {4}, has an unmanaged base instance and therefore cannot be updated by a managed solution.|
> |AttributeMapIsManagedException|0x8004F224, -2147159516|Cannot delete managed attribute map with Id: {0} between attribute {1} and {2} of entity {3} and {4}.|
> |AttributeNameConflictWithNavigationPropertyName|0x80048834, -2147186636|Attribute name {0} conflict with NavigationProerty name on entity. Please use unique name for attribute.|
> |AttributeNotCreatedForOfficeGraphError|0x80044237, -2147204553|This attribute cannot be created since support to enable attribute for officegraph is not available.|
> |AttributeNotOfTypePicklist|0x8004033c, -2147220676|This attribute is not mapped to a drop-down list, Boolean, or state/status attribute. However, you have included a ListValueMap element for it.  Fix this inconsistency, and then import this data map again.|
> |AttributeNotOfTypeReference|0x80040390, -2147220592|This attribute is not mapped as a reference attribute. However, you have included a ReferenceMap for it.  Fix this inconsistency, and then import this data map again.|
> |AttributeNotSecured|0x8004F508, -2147158776|One or more fields are not enabled for field level security. Field level security is not enabled until you publish the customizations.|
> |AttributeNotUpdatedForOfficeGraphError|0x80044238, -2147204552|This attribute cannot be updated since support to enable attribute for officegraph is not available.|
> |AttributePermissionIsInvalid|0x8004F50E, -2147158770|Permission '{0}' for field '{1}' with id={2} is invalid.|
> |AttributePermissionReadIsMissing|0x8004F504, -2147158780|The user does not have read permissions to a secured field. The requested operation could not be completed.|
> |AttributePermissionUpdateIsMissingDuringShare|0x8004F503, -2147158781|The user does not have update permissions to a secured field. The requested operation could not be completed.|
> |AttributePermissionUpdateIsMissingDuringUpdate|0x8004F507, -2147158777|The user doesn't have AttributePrivilegeUpdate and not granted shared access for a secured attribute during update operation|
> |AttributePrivilegeCreateIsMissing|0x8004F502, -2147158782|The user does not have create permissions to a secured field. The requested operation could not be completed.|
> |AttributePrivilegeInvalidToUnsecure|0x8004F50D, -2147158771|You must have sufficient permissions for a secured field before you can change its field level security.|
> |AttributesExceeded|0x80061501, -2147085055|Attributes cannot be more than 4|
> |AttributeSharingCreateDuplicate|0x8004F50B, -2147158773|Attribute has already been shared.|
> |AttributeSharingCreateShouldSetReadOrAndUpdateAccess|0x8004F509, -2147158775|You must set read and/or update access when you share a secured attribute. Attribute ID: {0}|
> |AttributeSharingUpdateInvalid|0x8004F50A, -2147158774|Both readAccess and updateAccess are false: call Delete instead of Update.|
> |AttributeTypeNotSupportedForCalculatedField|0x80050221, -2147155423|Calculated/RollUp Field is not supported for MultiSelectPicklist Attribute Type.|
> |AttributeTypeNotSupportedForGroupByOrderByQuery|0x80050224, -2147155420|GroupBy or OrderBy Query is not supported for MultiSelectPickList Attribute Type.|
> |AttributeUpdateNotAllowed|0x80060463, -2147089309|The Business Process Flow update has failed. The update of attribute "{0}" in workflow "{1}" is not allowed.|
> |AuthenticateToServerBeforeRequestingProxy|0x8004D228, -2147167704|Authenticate to serverType: {0} before requesting a proxy.|
> |AutoDataCaptureAuthorizationFailureException|0x80091042, -2146889662|You don’t have the proper Office 365 license to get untracked emails. Please contact your system administrator.|
> |AutoDataCaptureDisabledError|0x80091041, -2146889663|Auto capture feature is not enabled.|
> |AutoDataCaptureResponseRetrievalFailureException|0x80091043, -2146889661|Error while fetching untracked emails from Exchange.|
> |AutoNumberAttributeSequenceMissing|0x80060885, -2147088251|SQL Sequence missing for Auto Number attribute {0} of entity {1}. Will attempt to re-create the SQL Sequence now.|
> |AzureApplicationIdNotFound|0x8004F510, -2147158768|We didn’t find that application ID {0} in your Azure Active Directory (Azure AD) with CorrelationID {1}. Make sure your application is registered in Azure AD.|
> |AzureApplicationIdNotFoundInOrgDB|0x8004F512, -2147158766|Azure applicationid not found. We didn’t find the application ID {0} in your CRM database. Correct the application ID and resubmit the update.|
> |AzureOperationResponseTimedOut|0x80061635, -2147084747|An Azure operation request did not return a response within stated timeout period. Retry the operation or increase timeout provided for the operation.|
> |AzureRecommendationModelBuildNotExist|0x80061604, -2147084796|The Azure recommendation model build corresponding to the used model version doesn’t exist.|
> |AzureRecommendationModelNotExist|0x80061603, -2147084797|The Azure recommendation model doesn’t exist.|
> |AzureServiceConnectionCascadeDeleteFailed|0x80061636, -2147084746|One or more models use the connection. Delete all models using this connection, and try deleting the connection again.|
> |AzureServiceConnectionInvalidUri|0x80061630, -2147084752|Provide a valid service URL.|
> |AzureSqlDatabaseResourceLimitExceededError|0x80072323, -2147015901|The limit of resource for the database has been reached. Please check the exception for more details.|
> |AzureSqlDatabaseStorageQuotaExceededError|0x80072325, -2147015899|The storage limit for the database has been met.|
> |AzureSqlMaxConcurrentWorkersLimitExceededError|0x80072324, -2147015900|Too many concurrent requests detected.|
> |AzureWebAppPluginsDisabled|0x80050241, -2147155391|Azure WebApp based plugins disabled for the organization.|
> |BadAuthTicket|0x8004A102, -2147180286|The ticket specified for authentication is invalid|
> |BadRequest|0x8005F100, -2147094272|The request could not be understood by the server.|
> |BaseAttributeNameNotPresentError|0x80044240, -2147204544|BaseAttribute name should be present in condition xml.|
> |BaseCurrencyCannotBeDeactivated|0x80048cf4, -2147185420|The base currency cannot be deactivated.|
> |BaseCurrencyNotDeletable|0x80048cff, -2147185409|The base currency of an organization cannot be deleted.|
> |BaseCurrencyOverflow|0x80048cec, -2147185428|The exchange rate set for the currency specified in this record has generated a value for {0} that is larger than the maximum allowed for the base currency ({1}).|
> |BaseCurrencyUnderflow|0x80048ceb, -2147185429|The exchange rate set for the currency specified in this record has generated a value for {0} that is smaller than the minimum allowed for the base currency ({1}).|
> |BaseMatchingAttributeNotSameError|0x80044245, -2147204539|Base and Matching attribute should be of same type.|
> |BaseUnitDoesNotExist|0x80043b1c, -2147206372|The base unit does not exist.|
> |BaseUnitNotDeletable|0x80043b03, -2147206397|The base unit of a schedule cannot be deleted.|
> |BaseUnitNotNull|0x80043b17, -2147206377|Do not use a base unit as the value for a primary unit. This value should always be null.|
> |BaseUomNameNotSpecified|0x80043810, -2147207152|baseuomname not specified|
> |BDK_E_ADDRESS_VALIDATION_FAILURE|0x8004B540, -2147175104|{0}  |
> |BDK_E_AGREEMENT_ALREADY_SIGNED|0x8004B541, -2147175103|{0}  |
> |BDK_E_AUTHORIZATION_FAILED|0x8004B542, -2147175102|{0}  |
> |BDK_E_AVS_FAILED|0x8004B543, -2147175101|{0}  |
> |BDK_E_BAD_CITYNAME_LENGTH|0x8004B544, -2147175100|{0}  |
> |BDK_E_BAD_STATECODE_LENGTH|0x8004B545, -2147175099|{0}  |
> |BDK_E_BAD_ZIPCODE_LENGTH|0x8004B546, -2147175098|{0}  |
> |BDK_E_BADXML|0x8004B547, -2147175097|{0}  |
> |BDK_E_BANNED_PAYMENT_INSTRUMENT|0x8004B548, -2147175096|{0}  |
> |BDK_E_BANNEDPERSON|0x8004B549, -2147175095|{0}  |
> |BDK_E_CANNOT_EXCEED_MAX_OWNERSHIP|0x8004B54A, -2147175094|{0}  |
> |BDK_E_COUNTRY_CURRENCY_PI_MISMATCH|0x8004B54B, -2147175093|{0}  |
> |BDK_E_CREDIT_CARD_EXPIRED|0x8004B54C, -2147175092|{0}  |
> |BDK_E_DATE_EXPIRED|0x8004B54D, -2147175091|{0}  |
> |BDK_E_ERROR_COUNTRYCODE_MISMATCH|0x8004B54E, -2147175090|{0}  |
> |BDK_E_ERROR_COUNTRYCODE_REQUIRED|0x8004B54F, -2147175089|{0}  |
> |BDK_E_EXTRA_REFERRAL_DATA|0x8004B550, -2147175088|{0}  |
> |BDK_E_GUID_EXISTS|0x8004B551, -2147175087|{0}  |
> |BDK_E_INVALID_ADDRESS_ID|0x8004B552, -2147175086|{0}  |
> |BDK_E_INVALID_BILLABLE_ACCOUNT_ID|0x8004B553, -2147175085|{0}  The specified Billing account is invalid.  Or, although the objectID is of the correct type, the account it identifies does not exist in the system.|
> |BDK_E_INVALID_BUF_SIZE|0x8004B554, -2147175084|{0}  |
> |BDK_E_INVALID_CATEGORY_NAME|0x8004B555, -2147175083|{0}  |
> |BDK_E_INVALID_COUNTRY_CODE|0x8004B556, -2147175082|{0}  |
> |BDK_E_INVALID_CURRENCY|0x8004B557, -2147175081|{0}  |
> |BDK_E_INVALID_CUSTOMER_TYPE|0x8004B558, -2147175080|{0}  |
> |BDK_E_INVALID_DATE|0x8004B559, -2147175079|{0}  |
> |BDK_E_INVALID_EMAIL_ADDRESS|0x8004B55A, -2147175078|{0}  |
> |BDK_E_INVALID_FILTER|0x8004B55B, -2147175077|{0}  |
> |BDK_E_INVALID_GUID|0x8004B55C, -2147175076|{0}  |
> |BDK_E_INVALID_INPUT_TO_TAXWARE_OR_VERAZIP|0x8004B55D, -2147175075|{0}  |
> |BDK_E_INVALID_LOCALE|0x8004B55E, -2147175074|{0}  |
> |BDK_E_INVALID_OBJECT_ID|0x8004B55F, -2147175073|{0}  The Billing system cannot find the object (e.g. account or subscription or offering).|
> |BDK_E_INVALID_OFFERING_GUID|0x8004B560, -2147175072|{0}  |
> |BDK_E_INVALID_PAYMENT_INSTRUMENT_STATUS|0x8004B561, -2147175071|{0}  |
> |BDK_E_INVALID_PAYMENT_METHOD_ID|0x8004B562, -2147175070|{0}  |
> |BDK_E_INVALID_PHONE_TYPE|0x8004B563, -2147175069|{0}  |
> |BDK_E_INVALID_POLICY_ID|0x8004B564, -2147175068|{0}  |
> |BDK_E_INVALID_REFERRALDATA_XML|0x8004B565, -2147175067|{0}  |
> |BDK_E_INVALID_STATE_FOR_COUNTRY|0x8004B566, -2147175066|{0}  |
> |BDK_E_INVALID_SUBSCRIPTION_ID|0x8004B567, -2147175065|{0}  The subscription id specified is invalid.  Or, although the objectID is of correct type and also points to a valid account in SCS, the subscription it identifies does not exist in SCS.|
> |BDK_E_INVALID_TAX_EXEMPT_TYPE|0x8004B568, -2147175064|{0}  |
> |BDK_E_MEG_CONFLICT|0x8004B569, -2147175063|{0}  |
> |BDK_E_MULTIPLE_CITIES_FOUND|0x8004B56A, -2147175062|{0}  |
> |BDK_E_MULTIPLE_COUNTIES_FOUND|0x8004B56B, -2147175061|{0}  |
> |BDK_E_NON_ACTIVE_ACCOUNT|0x8004B56C, -2147175060|{0}  |
> |BDK_E_NOPERMISSION|0x8004B56D, -2147175059|{0}  The calling partner does not have access to this method or when the requester does not have permission to search against the supplied search PUID.|
> |BDK_E_OBJECT_ROLE_LIMIT_EXCEEDED|0x8004B56E, -2147175058|{0}  |
> |BDK_E_OFFERING_ACCOUNT_CURRENCY_MISMATCH|0x8004B56F, -2147175057|{0}  |
> |BDK_E_OFFERING_COUNTRY_ACCOUNT_MISMATCH|0x8004B570, -2147175056|{0}  |
> |BDK_E_OFFERING_NOT_PURCHASEABLE|0x8004B571, -2147175055|{0}  |
> |BDK_E_OFFERING_PAYMENT_INSTRUMENT_MISMATCH|0x8004B572, -2147175054|{0}  |
> |BDK_E_OFFERING_REQUIRES_PI|0x8004B573, -2147175053|{0}  |
> |BDK_E_PARTNERNOTINBILLING|0x8004B574, -2147175052|{0}  |
> |BDK_E_PAYMENT_PROVIDER_CONNECTION_FAILED|0x8004B575, -2147175051|{0}  |
> |BDK_E_POLICY_DEAL_COUNTRY_MISMATCH|0x8004B577, -2147175049|{0}  |
> |BDK_E_PRIMARY_PHONE_REQUIRED|0x8004B576, -2147175050|{0}  |
> |BDK_E_PUID_ROLE_LIMIT_EXCEEDED|0x8004B578, -2147175048|{0}  |
> |BDK_E_RATING_FAILURE|0x8004B579, -2147175047|{0}  |
> |BDK_E_REQUIRED_FIELD_MISSING|0x8004B57A, -2147175046|{0}  |
> |BDK_E_STATE_CITY_INVALID|0x8004B57B, -2147175045|{0}  |
> |BDK_E_STATE_INVALID|0x8004B57C, -2147175044|{0}  |
> |BDK_E_STATE_ZIP_CITY_INVALID|0x8004B57D, -2147175043|{0}  |
> |BDK_E_STATE_ZIP_CITY_INVALID2|0x8004B57E, -2147175042|{0}  |
> |BDK_E_STATE_ZIP_CITY_INVALID3|0x8004B57F, -2147175041|{0}  |
> |BDK_E_STATE_ZIP_CITY_INVALID4|0x8004B580, -2147175040|{0}  |
> |BDK_E_STATE_ZIP_COVERS_MULTIPLE_CITIES|0x8004B581, -2147175039|{0}  |
> |BDK_E_STATE_ZIP_INVALID|0x8004B582, -2147175038|{0}  |
> |BDK_E_TAXID_EXPDATE|0x8004B583, -2147175037|{0}  |
> |BDK_E_TOKEN_BLACKLISTED|0x8004B584, -2147175036|{0}  |
> |BDK_E_TOKEN_EXPIRED|0x8004B585, -2147175035|{0}  |
> |BDK_E_TOKEN_NOT_VALID_FOR_OFFERING|0x8004B586, -2147175034|{0}  |
> |BDK_E_TOKEN_RANGE_BLACKLISTED|0x8004B587, -2147175033|{0}  |
> |BDK_E_TRANS_BALANCE_TO_PI_INVALID|0x8004B588, -2147175032|{0}  |
> |BDK_E_UNKNOWN_SERVER_FAILURE|0x8004B589, -2147175031|{0}  Unknown server failure.|
> |BDK_E_UNSUPPORTED_CHAR_EXIST|0x8004B58A, -2147175030|{0}  |
> |BDK_E_USAGE_COUNT_FOR_TOKEN_EXCEEDED|0x8004B58F, -2147175025|{0}  Billing token is already spent.|
> |BDK_E_VATID_DOESNOTHAVEEXPDATE|0x8004B58B, -2147175029|{0}  |
> |BDK_E_ZIP_CITY_MISSING|0x8004B58C, -2147175028|{0}  |
> |BDK_E_ZIP_INVALID|0x8004B58D, -2147175027|{0}  Billing zip code error.|
> |BDK_E_ZIP_INVALID_FOR_ENTERED_STATE|0x8004B58E, -2147175026|{0}  Billing zip code error.|
> |BidsAuthenticationError|0x8005E003, -2147098621|An error occured while authenticating with server {0}.|
> |BidsAuthenticationFailed|0x8005E006, -2147098618|Authentication failed when trying to connect to server {0}. The username or password is incorrect.|
> |BidsInvalidConnectionString|0x8005E000, -2147098624|Input connection string is invalid. Usage: ServerUrl[;OrganizationName][;HomeRealmUrl]|
> |BidsInvalidUrl|0x8005E001, -2147098623|Input url {0} is invalid.|
> |BidsNoOrganizationsFound|0x8005E004, -2147098620|No organizations found for the user.|
> |BidsOrganizationNotFound|0x8005E005, -2147098619|Organization {0} cannot be found for the user.|
> |BidsServerConnectionFailed|0x8005E002, -2147098622|Failed to connect to server {0}.|
> |BillingNoSettingError|0x8004B531, -2147175119|No Billing application configuration setting [{0}] was found.|
> |BillingPartnerCertificate|0x8004B530, -2147175120|Could not determine the right Partner certificate to use with Billing.  Issuer: {0}  Subject: {1}  Distinguished matches: [{2}]  Name matches: [{3}]  All valid certificates: [{4}].|
> |BillingRetrieveKeyError|0x8004B538, -2147175112|Could not retrieve Billing session key: "{0}"|
> |BillingTestConnectionError|0x8004B532, -2147175118|Billing is not available: Call to IsServiceAvailable returned 'False'.|
> |BillingTestConnectionException|0x8004B533, -2147175117|Billing TestConnection exception.|
> |BillingUnknownErrorCode|0x8004B536, -2147175114|Billing error code [{0}] was thrown with exception {1}|
> |BillingUnknownException|0x8004B537, -2147175113|Billing error was thrown with exception {0}|
> |BillingUnmappedErrorCode|0x8004B535, -2147175115|Billing error code [{0}] was thrown with exception {1}|
> |BillingUserPuidNullError|0x8004B534, -2147175116|User Puid is required, but is null.|
> |BindAttributeNotSpecifiedForLookup|0x80160043, -2146041789|BindAttribute for lookup property {0} is not provided. More Details:{1}|
> |BindAttributeValuesAreDifferentAcrossControlConfigurations|0x80160044, -2146041788|Bind Attribute for lookup property {0} should be same for all form factor control configurations Please check the configuration: {1}. More Details:{2}|
> |BookFirstInstanceFailed|0x8004E10E, -2147163890|Failed to book first instance.|
> |BooleanOptionOutOfRange|0x8004431C, -2147204324|Boolean attribute options must have a value of either 0 or 1.|
> |BothConnectionSidesAreNeeded|0x80048218, -2147188200|You must provide a name or select a role for both sides of this connection.|
> |BoundPropertyShoulNotHaveStaticValue|0x80160031, -2146041807|Property {0} is configured with a static value, but must be bound to an attribute. More Details:{1}|
> |BoundPropertyTypeMismatch|0x80160041, -2146041791|The type declared for property {0} (type {1}) on the control manifest does not match the type(s){2} of property '{3}' bound to it. More Details:{4}|
> |BPFEntityAlreadyExists|0x80060384, -2147089532|BPF entity with this name already exists.|
> |BpfEntityServiceIsNull|0x80060446, -2147089338|Error creating or updating Business Process: BpfEntityService cannot be null.|
> |BpfFactoryIsNull|0x80060447, -2147089337|Error creating or updating Business Process: BpfFactory cannot be null.|
> |BpfInstanceAlreadyExists|0x80060397, -2147089513|A business process flow already exists for the target record and could not be created. Please contact your system administrator.|
> |BpfVisitorIsNull|0x80060448, -2147089336|Error creating or updating Business Process: BpfVisitor cannot be null.|
> |BulkDeleteChildFailure|0x80048459, -2147187623|One of the Bulk Delete Child Jobs Failed|
> |BulkDeleteRecordDeletionFailure|0x80048435, -2147187659|The record cannot be deleted.|
> |BulkDetectInvalidEmailRecipient|0x80048422, -2147187678|The e-mail recipient either does not exist or the e-mail address for the e-mail recipient is not valid.|
> |BulkDuplicateDetectionJobSendEmailFailed|0x8009000F, -2146893809|Bulk Duplicate Detection successfully completed. Please review the results and perform a manual merge. We were unable to send a notification to your specified email address. If this persists, please validate the email address you provided and review any active plugins.|
> |BulkMailOperationFailed|0x8004502D, -2147200979|The bulk e-mail job completed with {0} failures. The failures might be caused by missing e-mail addresses or because you do not have permission to send e-mail. To find records with missing e-mail addresses, use Advanced Find. If you need increased e-mail permissions, contact your system administrator.|
> |BulkMailServiceNotAccessible|0x80048304, -2147187964|The Microsoft Dynamics 365 Bulk E-Mail Service is not running.|
> |BundleCannotContainBundle|0x8004F972, -2147157646|You can't add a bundle to a bundle.|
> |BundleCannotContainProductFamily|0x8004F992, -2147157614|You can't add a product family to a bundle.|
> |BundleCannotContainProductKit|0x80061014, -2147086316|You can't add a kit to a bundle.|
> |BundleMaxPropertyLimitExceeded|0x8008100E, -2146955250|This bundle can't be published because it has too many properties. A bundle in your organization can't have more than {0} properties.|
> |BusinessManagementInvalidUserId|0x80041d1f, -2147214049|The user Id(s) [{0}] is invalid.|
> |BusinessManagementLoopBeingCreated|0x80041d21, -2147214047|Creating this parental association would create a loop in business hierarchy.|
> |BusinessManagementLoopExists|0x80041d20, -2147214048|Loop exists in the business hierarchy.|
> |BusinessManagementObjectAlreadyExists|0x8004022a, -2147220950|An object with the specified name already exists.|
> |BusinessNotEnabled|0x8004032c, -2147220692|The specified business unit : '{0}' is disabled.|
> |BusinessProcessFlowDefinitionOutdated|0x80060375, -2147089547|This action cannot be completed because the Business Process Flow definition is out of sync with the Process Action. Please contact your Dynamics 365 System Administrator to update the Business Process Flow.|
> |BusinessProcessFlowMissingEntityErrorMessage|0x80060440, -2147089344|Failed to import Business Process '{0}' because solution does not include corresponding Business Process entity '{1}'.|
> |BusinessProcessFlowStepHasInvalidParent|0x80060405, -2147089403|{0} parent is not of type {1}|
> |BusinessRuleEditorSupportsOnlyIfConditionBranch|0x80060008, -2147090424|The business rule editor only supports one if condition. Please fix the rule.|
> |BusinessUnitCannotBeDisabled|0x80041d59, -2147213991|Business unit cannot be disabled: no active user with system admin role exists outside of business unit subtree.|
> |BusinessUnitDefaultTeamOwnsRecords|0x80041d62, -2147213982|Business unit default team owns records. Business unit (Id = {0}) cannot be deleted. Reassign the records owned by default team and try again.|
> |BusinessUnitHasChildAndCannotBeDeleted|0x80041d61, -2147213983|Business unit has a child business unit and cannot be deleted.|
> |BusinessUnitIsNotDisabledAndCannotBeDeleted|0x80041d60, -2147213984|Not disabled business unit cannot be deleted.|
> |BusinessUnitQueuesAssociatedWithBU|0x80072526, -2147015386|There are {0} queues referencing this BusinessUnit with id ={1}, Name = {2}. Please delete the queues before deleting this business unit or assign to a different Business Unit.|
> |CalculatedFieldsAssignmentMismatch|0x8006042b, -2147089365|You can’t set the value {0}, which is of type {1}, to type {2}.|
> |CalculatedFieldsCyclicReference|0x80060431, -2147089359|Field {0} cannot be used in calculated field {1} because it would create a circular reference.|
> |CalculatedFieldsDateOnlyBehaviorTypeMismatch|0x8006043a, -2147089350|You can only use a Date Only type of field.|
> |CalculatedFieldsDepthExceeded|0x80060432, -2147089358|You can’t create or update the {0} field because the {1} field already has a calculated field chain of {2} deep.|
> |CalculatedFieldsDivideByZero|0x8006042d, -2147089363|You cannot divide by {0}, which evaluates to zero.|
> |CalculatedFieldsEntitiesExceeded|0x80060433, -2147089357|Field {0} cannot be created or updated because field {1} contains an additional formula that uses a parent record.|
> |CalculatedFieldsFeatureNotEnabled|0x80060422, -2147089374|Calculated Field feature is not available|
> |CalculatedFieldsFunctionMismatch|0x8006042c, -2147089364|You can't use {0}, which is of type {1}, with the current function.|
> |CalculatedFieldsInvalidAttribute|0x80060428, -2147089368|The {0} field doesn't exist.|
> |CalculatedFieldsInvalidAttributes|0x8006042e, -2147089362|The formula references the following attributes that don't exist: {0}.|
> |CalculatedFieldsInvalidEntity|0x80060423, -2147089373|The formula contains an invalid reference: {0}.|
> |CalculatedFieldsInvalidFunction|0x80060427, -2147089369|The {0} function doesn't exist.|
> |CalculatedFieldsInvalidSourceTypeMask|0x80060438, -2147089352|The formula can't be saved because it contains references to the following fields that have invalid definitions: {0}.|
> |CalculatedFieldsInvalidValue|0x8006042f, -2147089361|The formula references a value that doesn't exist.|
> |CalculatedFieldsInvalidValues|0x80060430, -2147089360|The formula references the following values that don't exist: {0}.|
> |CalculatedFieldsInvalidXaml|0x80060424, -2147089372|The {0} field has an invalid XAML formula definition.|
> |CalculatedFieldsNonCalculatedFieldAssignment|0x80060425, -2147089371|Only calculated fields can have a formula definition.|
> |CalculatedFieldsPrimitiveOverflow|0x8006042a, -2147089366|Cannot convert the value {0} into type {1}.|
> |CalculatedFieldsTimeInvBehaviorTypeMismatch|0x8006043b, -2147089349|You can only use a Time-Zone Independent Date Time type of field.|
> |CalculatedFieldsTypeMismatch|0x80060426, -2147089370|You can't use {0}, which is of type {1}, with the current operator.|
> |CalculatedFieldsUserLocBehaviorTypeMismatch|0x8006043c, -2147089348|You can only use a User Local Date Time type of field.|
> |CalculatedFieldUsedInRollupFieldCannotBeComplex|0x80060550, -2147089072|One or more rollup fields depend on this calculated field. This calculated field can't use a rollup field, another calculated field that is using a rollup field or a field from related entity.|
> |CalculateNowOverflowError|0x80060558, -2147089064|The calculation failed due to an overflow error.|
> |CallerCannotChangeOwnDomainName|0x80044161, -2147204767|The caller cannot change their own domain name|
> |CalloutException|0x8004025b, -2147220901|Callout Exception occurred.|
> |CampaignActivityAlreadyPropagated|0x80040326, -2147220698|This campaign activity has been distributed already. Campaign activities cannot be distributed more than one time.|
> |CampaignActivityClosed|0x80040331, -2147220687|This Campaign Activity is closed or canceled. Campaign activities cannot be distributed after they have been closed or canceled.|
> |CampaignNotSpecifiedForCampaignActivity|0x80040309, -2147220727|RegardingObjectId is a required field.|
> |CampaignNotSpecifiedForCampaignResponse|0x8004030a, -2147220726|RegardingObjectId is a required field.|
> |CanAssociateOnlyMobileOfflineEnabledEntityToProfileItem|0x8006099E, -2147087970|{0} needs to be enabled for mobile offline.|
> |CanAssociateOnlyMobileOfflineEnableEntityToProfileItem|0x8006099C, -2147087972|This entity needs to be enabled for mobile offline.|
> |CanAssociateOnlyOneEntityPerProfileItem|0x8006099D, -2147087971|You can only add one mobile offline profile item record per entity to a mobile offline profile record. |
> |CancelActiveChildCaseFirst|0x8003F451, -2147224495|Cancel active child case before canceling parent case.|
> |CannotAcceptEmail|0x8005E20B, -2147098101|The email that you are trying to deliver cannot be accepted by Microsoft Dynamics 365. Reason Code: {0}.|
> |CannotAccessExchangeOptinStatus|0x80071110, -2147020528|Exchange optin status is not accessible.|
> |CannotActivateDeactivateOnAnyEntityRoutingRuleFCBOff|0x8004F849, -2147157943|Unable to activate or deactivate routing rule set record for entities (except case entity) as the feature control bit for entity records routing is disabled.|
> |CannotActivateMailboxForDisabledUserOrQueue|0x8005E230, -2147098064|Mailbox cannot be activated because the user or queue associated with the mailbox is in disabled state. Mailbox can only be activated for Active User/Queue.|
> |CannotActivateRecord|0x80081017, -2146955241|You can't activate a retired product family or bundle. Also, you can't activate a retired product that is part of a product family.|
> |CannotActivateRecordWithProperties|0x800422FF, -2147212545|You can't activate a retired product that has properties.|
> |CannotActOnBehalfOfAnotherUser|0x8004A110, -2147180272|User does not have the privilege to act on behalf another user.|
> |CannotActOnBehalfOfExternalParty|0x80061116, -2147086058|User does not have the privilege to act on behalf of External Party.|
> |CannotAddActivityPartyEntityToMobileOfflineProfileItem|0x800609AD, -2147087955|You can’t add the ActivityParty entity to the mobile offline profile item because it’s added automatically when an activity entity is added to the profile.|
> |CannotAddBundleToItself|0x80061031, -2147086287|You can't add a bundle to itself.|
> |CannotAddBundleToPricelist|0x80061007, -2147086329|You can't add the {0} bundle to the pricelist because the {1} bundle product isn't in the pricelist.|
> |CannotAddBusinessDataLocalizedLabelEntityToMobileOfflineProfileItem|0x800609AC, -2147087956|You can’t add the BusinessDataLocalizedLabel entity to the mobile offline profile item because it’s added automatically when the Product entity is added to the profile.|
> |CannotAddCanvasAppElementOfTypeToAppModule|0x80050131, -2147155663|Canvas app {0} with type “{1}” cannot be added to the app as a new element.|
> |CannotAddDraftFamilyProductBundleToCases|0x8004F984, -2147157628|You can't add a product family, a draft product, or a draft bundle.|
> |CannotAddIntersectEntityToMobileOfflineProfileItem|0x800609AB, -2147087957|You can’t add the intersect entity to the mobile offline profile item because it’s added automatically when its parent entities are added to the profile.|
> |CannotAddKitToItself|0x80061032, -2147086286|You can't add a kit to itself.|
> |CannotAddMembersToDefaultTeam|0x8004830B, -2147187957|Can't add members to the default business unit team (TeamId = {0}).|
> |CannotAddNewBooleanValue|0x8004431D, -2147204323|You cannot add an option to a Boolean attribute.|
> |CannotAddNewStateValue|0x8004431E, -2147204322|You cannot add state options to a State attribute.|
> |CannotAddNonCustomizableComponent|0x8004F015, -2147160043|The component {0} {1} cannot be added to the solution because it is not customizable|
> |CannotAddOrActonBehalfAnotherUserPrivilege|0x8004Ed43, -2147160765|Act on Behalf of Another User privilege cannot be added or removed.|
> |CannotAddParentToAKit|0x80061015, -2147086315|You can't specify a parent record for a kit.|
> |CannotAddPricelistToProductFamily|0x8004F902, -2147157758|You can't add a product family to a pricelist.|
> |CannotAddProduct|0x8004F908, -2147157752|You can only add Active products.|
> |CannotAddProductBundleToKit|0x80061022, -2147086302|You can't add a bundle to a kit.|
> |CannotAddProductFamilyToKit|0x80061023, -2147086301|You can't add a product family to a kit.|
> |CannotAddProductToBundle|0x8004F976, -2147157642|You cannot add products to this bundle.The limit of {0} has been reached for this bundle.|
> |CannotAddProductToKit|0x80061024, -2147086300|You can't add a product that belongs to a product family to a kit.|
> |CannotAddProductToRetiredKit|0x80061026, -2147086298|You can't add a product to a retired kit.|
> |CannotAddQueueItemsToInactiveQueue|0x80040522, -2147220190|The selected user does not have sufficient permissions to work on items in this queue.|
> |CannotAddRetiredProduct|0x80061033, -2147086285|You can’t create a product relationship with a retired product.|
> |CannotAddRetiredProductToKit|0x80061027, -2147086297|You can't add a retired product to a kit.|
> |CannotAddRetiredProductToPricelist|0x80061009, -2147086327|Retired products can not be added to pricelists.|
> |CannotAddSingleQueueEnabledEntityToQueue|0x8004051c, -2147220196|The entity record cannot be added to the queue as it already exists in other queue.|
> |CannotAddSolutionComponentWithoutRoots|0x8004F018, -2147160040|This item is not a valid solution component. For more information about solution components, see the Microsoft Dynamics 365 SDK documentation.|
> |CannotAddUserToMobileOfflineProfile|0x800609A6, -2147087962|You can’t add this user to this mobile offline profile because the user’s role is either missing or doesn’t have the Dynamics 365 for mobile privilege.|
> |CannotAddWorkflowActivationToSolution|0x8004F00C, -2147160052|Cannot add Workflow Activation to solution.|
> |CannotAssignAddressBookFilters|0x80048448, -2147187640|Cannot assign address book filters|
> |CannotAssignOfflineFilters|0x800404ff, -2147220225|Cannot assign offline filters|
> |CannotAssignOutlookFilters|0x80040264, -2147220892|Cannot assign outlook filters|
> |CannotAssignRolesOrProfilesToAccessTeam|0x80048331, -2147187919|Cannot assign roles or profiles to an access team (TeamId = {0}).|
> |CannotAssignRolesToSupportUser|0x80041d51, -2147213999|The support user are read-only, which cannot be assigned with other roles|
> |CannotAssignSupportUser|0x80041d44, -2147214012|The Support User Role cannot be assigned to a user.|
> |CannotAssignToAccessTeam|0x80048340, -2147187904|You cannot assign a record to the access team. You can assign a record to the owner team.|
> |CannotAssignToDisabledBusiness|0x8004032d, -2147220691|The specified business unit cannot be assigned to because it is disabled.|
> |CannotAssociateExternalPartyItem|0x80061117, -2147086057|You can’t associate more than one external party item with an entity record that has been enabled as an external party.|
> |CannotAssociateInactiveItemToCampaign|0x80040304, -2147220732|Cannot associate an inactive item to a Campaign.|
> |CannotAssociateInvalidEntityToProfileItem|0x8006099B, -2147087973|Invalid object type code.|
> |CannotAssociateProductFamily|0x8004F999, -2147157607|You can't create a relationship with a product family.|
> |CannotAssociateRetiredBundles|0x80081011, -2146955247|You can't create a product relationship with a retired bundle.|
> |CannotAssociateRetiredProducts|0x8004F974, -2147157644|You can't create a product relationship with a retired product.|
> |CannotBindToSession|0x80040254, -2147220908|Cannot bind to another session, session already bound.|
> |CannotCancelInvoice|0x80100001, -2146435071|The invoice cannot be cancelled because it is not in active or paid state.|
> |CannotChangeAccessMode|0x80040d38, -2147218120|A user cannot change their access mode if they are the only user with Full Access mode.|
> |CannotChangeAccessModeForInternetMarketingUser|0x80045035, -2147200971|Internet Marketing User is a system user. You cannot change its access mode.|
> |CannotChangeAttributeRequiredLevel|0x8004D293, -2147167597|An attribute's required level cannot be changed from SystemRequired|
> |CannotChangeConnectorDisplayName|0x80072607, -2147015161|The connector display name attribute cannot be changed.|
> |CannotChangeConvertRuleState|0x800608F4, -2147088140|Error occured during activating Convert Rule.Please check your privileges on Workflow and kindly try again or Contact your system administrator.|
> |CannotChangeDaysSinceRecordLastModified|0x800609A4, -2147087964|You need to enable this entity for mobile offline before you can set or change the number of days since the record was last modified.|
> |CannotChangeInvitationStatusForInternetMarketingUser|0x80045036, -2147200970|Internet Marketing User is a system user. You cannot change its invitation status.|
> |CannotChangeProductRelationship|0x80061013, -2147086317|You can't add or modify the product relationship of a retired product.|
> |CannotChangeSelectedBundleToAnotherValue|0x8004F986, -2147157626|If a bundle is selected as an existing product, you can't change it to another value.|
> |CannotChangeSelectedProductWithBundle|0x8004F987, -2147157625|If a product is selected as an existing product, you can't change it to a bundle.|
> |CannotChangeState|0x8004F863, -2147157917|Error occured during activating SLA.Please check your privileges on Workflow and kindly try again or Contact your system administrator.|
> |CannotChangeStateOfNonpublicView|0x80040279, -2147220871|Only public views can be deactivated and activated.|
> |CannotChangeTeamTypeDueToOwnership|0x80048337, -2147187913|You cannot modify the type of the team because there are records owned by the team.|
> |CannotChangeTeamTypeDueToRoleOrProfile|0x80048336, -2147187914|You cannot modify the type of the team because there are security roles or field security profiles assigned to the team.|
> |CannotClearChannelPropertyGroupFromConvertRule|0x800608ED, -2147088147|The Channel Property Group is used by one or more steps. Delete the properties from the conditions and steps that use the record before you save or activate the rule.|
> |CannotCloneBundleAsProductLimitExceeded|0x8004F985, -2147157627|You can't create this new bundle because it contains more than the allowed number of {0} products that a bundle can contain.|
> |CannotCloneBundleWithRetiredProducts|0x80061034, -2147086284|You can't clone a bundle that contains retired products.|
> |CannotCloneProductKit|0x80061020, -2147086304|You can't clone a kit.|
> |CannotCloseCase|0x8004F456, -2147158954|This operation can't be completed. One or more child cases can't be closed because of the status transition rules that are defined for cases.|
> |CannotCompleteLockRequest|0x8004026c, -2147220884|Cannot complete Request due to timeout taking {0} lock.|
> |CannotConnectToSelf|0x80048217, -2147188201|Cannot connect a record to itself.|
> |CannotConvertBundleToKit|0x80061030, -2147086288|You can't convert a bundle to a kit.|
> |CannotConvertProductAssociatedWithBundleToKit|0x80061018, -2147086312|You can't convert a product that is a part of a bundle to a kit.|
> |CannotConvertProductAssociatedWithFamilyToKit|0x80061016, -2147086314|You can't convert a product that belongs to a product family to a kit.|
> |CannotConvertProductFamilyToKit|0x80061029, -2147086295|You can't convert a product family to a kit.|
> |CannotCopyIncompatibleListType|0x80040306, -2147220730|Cannot copy lists of different types.|
> |CannotCopyStaticList|0x8004F704, -2147158268|This action is valid only for dynamic list.|
> |CannotCreateActivityRelationship|0x80047006, -2147192826|Relationship with activities cannot be created through this operation|
> |CannotCreateAddressBookFilters|0x80048447, -2147187641|Cannot create address book filters|
> |CannotCreateCase|0x80060853, -2147088301|You can't create this case as the default entitlement for the specified customer has no remaining terms.|
> |CannotCreateComponentDefinition|0x80072001, -2147016703|Creation of a new component definition is not supported|
> |CannotCreateExternalPartyWithSameCorrelationKey|0x80061112, -2147086062|An external party record already exists with the same correlation key value.|
> |CannotCreateFromSupportUser|0x80041d46, -2147214010|Cannot create a role from Support User Role.|
> |CannotCreateKitOfTypeFamilyOrBundle|0x80061012, -2147086318|You can't create a kit of type bundle or product family.|
> |CannotCreateOrEnablePositionDueToParentPositionIsDisabled|0x80048344, -2147187900|A child position cannot be created/enabled under a disabled parent position.|
> |CannotCreateOutlookFilters|0x80040263, -2147220893|Cannot create outlook filters|
> |CannotCreatePluginInstance|0x8004A201, -2147180031|Can not create instance of a plug-in. Verify that plug-in type is not defined as abstract and it has a public constructor supported by Dynamics 365 SDK.|
> |CannotCreatePropertyOptionSetItem|0x80081013, -2146955245|You can only create a property option set item record that refers to a property that has its data type set to Option Set.|
> |CannotCreateQueueItemInactiveObject|0x8004051e, -2147220194|Deactivated object cannot be added to queue.|
> |CannotCreateResponseForTemplate|0x80040312, -2147220718|CampaignResponse can not be created for Template Campaign.|
> |CannotCreateRuleOnAnyEntityRoutingRuleFCBOff|0x8004F848, -2147157944|Unable to create routing rule set record for entities (except case entity) as the feature control bit for entity records routing is disabled.|
> |CannotCreateSelfReferencingParentChild|0x8007200C, -2147016692|Parent-Child relationship {0} cannot be self-referenced.|
> |CannotCreateSelfReferentialPolymorphicLookup|0x80090423, -2146892765|Relationship for polymorphic lookup cannot be self referential. The entity '{0}' cannot be the referencing and referenced entity.|
> |CannotCreateSLAForEntity|0x80055005, -2147135483|You can't create a service level agreement (SLA) for this entity because it’s not enabled for creating SLAs|
> |CannotCreateSyncUserIsLicensedField|0x80041d4d, -2147214003|The property IsLicensed cannot be set for Sync User Creation.|
> |CannotCreateSyncUserObjectMissing|0x80041d4b, -2147214005|This is not a valid Microsoft Online Services ID for this organization.|
> |CannotCreateSystemOrDefaultTheme|0x800608D5, -2147088171|You can’t create system or default themes. System or default theme can only be created out of box.|
> |CannotCreateUpdateSourceAttribute|0x80044804, -2147203068|Source Attribute Not Valid For Create/Update if Metric Type is Count.|
> |CannotDeactivateDefaultView|0x8004027a, -2147220870|Default views cannot be deactivated.|
> |CannotDeactivateGuestProfile|0x80061105, -2147086075|You can't set this guest channel access profile as inactive.|
> |CannotDefineMultipleValuesOnOwnerFieldInProfileItemEntityFilter|0x80071129, -2147020503|You cannot define multiple values on this field.|
> |CannotDeleteActiveCaseCreationRule|0x8004F880, -2147157888|You can't delete an active rule. Deactivate the Record Creation and Update Rule, and then try deleting it.|
> |CannotDeleteActiveRecordCreationRuleItem|0x8004F894, -2147157868|You can’t delete an active record creation rule item. Deactivate the record creation rule, and then try deleting it.|
> |CannotDeleteActiveRule|0x8004F850, -2147157936|You can not delete an active routing rule. Deactivate the rule to delete it.|
> |CannotDeleteActiveSla|0x8004F870, -2147157904|You can't delete an active SLA. Deactivate the SLA, and then try deleting it.|
> |CannotDeleteAppModuleAdministration|0x80050130, -2147155664|This app can’t be deleted.|
> |CannotDeleteAppModuleClientType|0x80050129, -2147155671|This app can’t be deleted.|
> |CannotDeleteAsBackgroundOperationInProgress|0x8004032b, -2147220693|This record is currently being used by Microsoft Dynamics 365 and cannot be deleted. Try again later. If  the problem persists, contact your system administrator.|
> |CannotDeleteAsItIsReadOnly|0x80040228, -2147220952|The object cannot be deleted because it is read-only.|
> |CannotDeleteAttributeUsedInWorkflow|0x80045030, -2147200976|This attribute cannot be deleted because it is used in one or more workflows. Cancel any system jobs for workflows that use this attribute, then delete or modify any workflows that use the attribute, and then try to delete the attribute again.|
> |CannotDeleteBaseMoneyCalculationAttribute|0x80048cfe, -2147185410|The base money calculation Attribute is not valid for deletion|
> |CannotDeleteCannedView|0x8004022f, -2147220945|System-defined views cannot be deleted.|
> |CannotDeleteCDSUser|0x80041d5a, -2147213990|The Common Data Service User Role cannot be deleted.|
> |CannotDeleteChannelAccessProfileRule|0x80061108, -2147086072|You can't delete an active channel access profile rule. Deactivate the rule and then delete it.|
> |CannotDeleteChannelProperty|0x800608EB, -2147088149|You can’t delete a channel property which is being referred in a convert rule.|
> |CannotDeleteChildAttribute|0x80047016, -2147192810|The Child Attribute is not valid for deletion|
> |CannotDeleteCustomEntityUsedInWorkflow|0x8004502C, -2147200980|Cannot delete entity because it is used in a workflow.|
> |CannotDeleteDefaultProfile|0x8006099A, -2147087974|To delete this profile, you first need to set it so that it’s no longer a default mobile offline profile.|
> |CannotDeleteDefaultStatusOption|0x80044341, -2147204287|Default Status options cannot be deleted.|
> |CannotDeleteDefaultTeam|0x80048307, -2147187961|The default business unit team can't be deleted (TeamId = {0}).|
> |CannotDeleteDueToAssociation|0x80040227, -2147220953|The object you tried to delete is associated with another object and cannot be deleted.|
> |CannotDeleteDueToBasketEntityAssociation|0x80061612, -2147084782|You can't delete a Recommendation entity if it has a corresponding Basket entity.|
> |CannotDeleteDynamicPropertyInRetiredState|0x8004F892, -2147157870|You can't delete a property of a retired product.|
> |CannotDeleteDynamicPropertyInUse|0x80081003, -2146955261|Retired Properties being used in transactions can not be deleted.|
> |CannotDeleteEnumOptionsFromAttributeType|0x80044323, -2147204317|You can delete options only from picklist and status attributes.|
> |CannotDeleteGuestProfile|0x80061104, -2147086076|You can't delete this guest channel access profile.|
> |CannotDeleteInheritedDynamicProperty|0x80081014, -2146955244|You can't delete a property that is inherited from a product family.|
> |CannotDeleteInUseAttribute|0x80048418, -2147187688|The selected attribute cannot be deleted because it is referenced by one or more duplicate detection rules that are being published.|
> |CannotDeleteInUseComponent|0x8004F01F, -2147160033|The {0}({1}) component cannot be deleted because it is referenced by {2} other components. For a list of referenced components, use the RetrieveDependenciesForDeleteRequest.|
> |CannotDeleteInUseEntity|0x80048420, -2147187680|The selected entity cannot be deleted because it is referenced by one or more duplicate detection rules that are in process of being published.|
> |CannotDeleteInUseOptionSet|0x80048417, -2147187689|This option set cannot be deleted. The current set of entities that reference this option set are: {0}. These references must be removed before this option set can be deleted|
> |CannotDeleteLastEmailAttribute|0x80046FFF, -2147192833|You cannot delete this field because the record type has been enabled for e-mail.|
> |CannotDeleteMetadata|0x8004F032, -2147160014|The '{2}' operation on the current component(name='{0}', id='{1}') failed during managed property evaluation of condition: '{3}'|
> |CannotDeleteMetricWithGoals|0x80044800, -2147203072|This goal metric is being used by one or more goals and cannot be deleted.|
> |CannotDeleteNonLeafNode|0x8004F200, -2147159552|Only a leaf statement can be deleted. This statement is parenting some other statement.|
> |CannotDeleteNotOwnedDynamicProperty|0x80081006, -2146955258|You cannot delete a dynamic property that is inherited from a product family.|
> |CannotDeleteOneNoteTableOfContent|0x800608B7, -2147088201|You can’t delete this file because it contains links to OneNote notebook sections. To delete notebook contents, open the notebook in OneNote and delete the contents from there. To delete a notebook, open SharePoint and delete the notebook from there.|
> |CannotDeleteOnlineRecord|0x8005F248, -2147093944|You can’t delete this record because it doesn’t exist in the offline mode.|
> |CannotDeleteOptionSet|0x80048404, -2147187708|The selected OptionSet cannot be deleted|
> |CannotDeleteOrCancelSystemJobs|0x80044F02, -2147201278|You can't cancel or delete this system job because it's required by the system. You can only pause, resume, or postpone this job.|
> |CannotDeleteOverriddenProperty|0x80081100, -2146955008|You can't delete this property because it's overridden for one more or child records. Remove the overridden versions of the property, republish the product family hierarchy, and then try deleting the property.|
> |CannotDeletePartnerSolutionWithOrganizations|0x8004A10e, -2147180274|Can not delete partner solution as one or more organizations are associated with it|
> |CannotDeletePartnerWithPartnerSolutions|0x8004A10d, -2147180275|Can not delete partner as one or more solutions are associated with it|
> |CannotDeletePrimaryUIAttribute|0x80047002, -2147192830|The Primary UI Attribute is not valid for deletion|
> |CannotDeleteProductFromActiveBundle|0x80061010, -2147086320|You can't remove products from a bundle that's either active or under revision.|
> |CannotDeleteProductStatusCode|0x80081016, -2146955242|You can't delete a system-generated status reason.|
> |CannotDeleteProfileWithExternalPartyItem|0x80061107, -2147086073|You can't delete this channel access profile because it's associated to an external party item. Remove the association, and then try again.|
> |CannotDeleteProfileWithProfileRules|0x80061106, -2147086074|You can't delete this channel access profile because it's being used by one or more channel access profile rules. Remove this profile from the channel access profile rules, and then try again.|
> |CannotDeletePropertyOverriddenByBundleItem|0x80081015, -2146955243|You can't delete this property because it's overridden in one or more related bundle products. Remove the overridden versions of the property from the related bundle products, publish the bundles that were changed, and then try again.|
> |CannotDeleteQueueWithQueueItems|0x80631117, -2140991209|You can't delete this queue because it has items assigned to it. Assign these items to another user, team, or queue and try again.|
> |CannotDeleteQueueWithRouteRules|0x80731118, -2139942632|You can't delete this queue because one or more routing rule sets use this queue. Remove the queue from the routing rule sets and try again.|
> |CannotDeleteRelatedSla|0x8004F859, -2147157927|The SLA record couldn't be deleted. Please try again or contact your system administrator|
> |CannotDeleteRestrictedPublisher|0x8004F006, -2147160058|Attempting to delete a restricted publisher.|
> |CannotDeleteRestrictedSolution|0x8004F005, -2147160059|Attempting to delete a restricted solution.|
> |CannotDeleteSupportUser|0x80041d42, -2147214014|The Support User Role cannot be deleted.|
> |CannotDeleteSysAdmin|0x80041d2e, -2147214034|The System Administrator Role cannot be deleted.|
> |CannotDeleteSystemCustomizer|0x80041d4a, -2147214006|The System Customizer Role cannot be deleted.|
> |CannotDeleteSystemEmailTemplate|0x80048432, -2147187662|System e-mail templates cannot be deleted.|
> |CannotDeleteSystemForm|0x8004F652, -2147158446|System forms cannot be deleted.|
> |CannotDeleteSystemTheme|0x800608DA, -2147088166|You can't delete system themes.|
> |CannotDeleteTeamOwningRecords|0x8004830E, -2147187954|Can't delete a team which owns records. Reassign the records and try again (TeamId = {0}).|
> |CannotDeleteUpdateInUseRule|0x80048428, -2147187672|The duplicate detection rule is currently in use and cannot be updated or deleted. Please try again later.|
> |CannotDeleteUserMailbox|0x8005E200, -2147098112|The mailbox associated to a user or a queue cannot be deleted.|
> |CannotDeleteUserProfile|0x800609A3, -2147087965|You can’t delete an active mobile offline profile. Remove all users from the profile and try again.|
> |CannotDeserializeRequest|0x8004416f, -2147204753|The SDK request could not be deserialized.|
> |CannotDeserializeWorkflowInstance|0x8004501F, -2147200993|Workflow instance cannot be deserialized. A possible reason for this failure is a workflow referencing a custom activity that has been unregistered.|
> |CannotDeserializeXamlWorkflow|0x80045020, -2147200992|Xaml representing workflow cannot be deserialized into a DynamicActivity.|
> |CannotDisableAutoCreateAccessTeams|0x80048338, -2147187912|You cannot disable the auto create access team setting while there are associated team templates.|
> |CannotDisableDuplicateDetection|0x80048462, -2147187614|Duplicate detection cannot be disabled because a duplicate detection job is currently in progress. Try again later.|
> |CannotDisableInternetMarketingUser|0x80045033, -2147200973|You cannot disable the Internet Marketing Partner user. This user does not consume a user license and is not charged to your organization.|
> |CannotDisableMobileOfflineFlagForEntity|0x800609A5, -2147087963|You cannot disable Mobile Offline flag for this entity as it is being used in Mobile Offline Profiles|
> |CannotDisableMobileOfflineFlagForImportEntity|0x80071111, -2147020527|You can’t disable mobile offline for the {0} entity using solution import. If you don’t want to use this entity in offline mode, uncheck the ‘Enable for Mobile Offline’ flag from the customization screen|
> |CannotDisableOrDeletePositionDueToAssociatedUsers|0x80048343, -2147187901|This position can’t be deleted until all associated users are removed from this position.|
> |CannotDisableRelevanceSearchManagedProperty|0x80060303, -2147089661|The {0} entity is currently syncing to an external search index.  You must remove the entity from the external search index before you can set the "Can Enable Sync to External Search Index" property to False.|
> |CannotDisableSysAdmin|0x80041d2f, -2147214033|A user cannot be disabled if they are the only user that has the System Administrator Role.|
> |CannotDisableTenantAdmin|0x80041d65, -2147213979|Users who are granted the Microsoft Office 365 Global administrator or Service administrator role cannot be disabled in Microsoft Dynamics 365 Online. You must first remove the Microsoft Office 365 role, and then try again.|
> |CannotEditActiveRule|0x8004F851, -2147157935|You can not edit an active routing rule. Deactivate the rule to delete it.|
> |CannotEditActiveSla|0x8004F860, -2147157920|You can't delete active SLA .Please deactivate the SLA to delete or Contact your system administrator.|
> |CannotEnableDuplicateDetection|0x80048421, -2147187679|Duplicate detection cannot be enabled because one or more rules are being published.|
> |CannotEnableEntityForRelevanceSearch|0x80060302, -2147089662|Entity {0} can’t be enabled for relevance search because of the configuration of its managed properties.|
> |CannotExceedFilterLimit|0x8004027c, -2147220868|Cannot exceed synchronization filter limit.|
> |CannotExecuteRequestBecauseHttpsIsRequired|0x8004852C, -2147187412|HTTPS protocol is required for this type of request, please enable HTTPS protocol and try again.|
> |CannotExportRuleOnAnyEntityRoutingRuleFCBOff|0x8004F847, -2147157945|Unable to export routing rule set record for entities (except case entity) as the feature control bit for entity records routing is disabled.|
> |CannotFindDomainAccount|0x80044342, -2147204286|Invalid domain account|
> |CannotFindLayerToMerge|0x8004F060, -2147159968|Cannot find a suitable layer to merge Component: [{0}] with Id: [{1}]. Cannot continue with the operation. Check the layers of the component.|
> |CannotFindObjectInQueue|0x800404eb, -2147220245|The object was not found in the given queue|
> |CannotFindUserQueue|0x800404ec, -2147220244|Cannot find user queue|
> |CannotFollowInactiveEntity|0x8004F6A3, -2147158365|Can't follow inactive record. |
> |CannotGrantAccessToAddressBookFilters|0x80048446, -2147187642|Cannot grant access to address book filters|
> |CannotGrantAccessToOfflineFilters|0x80040271, -2147220879|Cannot grant access to offline filters|
> |CannotGrantAccessToOutlookFilters|0x80040268, -2147220888|Cannot grant access to outlook filters|
> |CannotHaveDuplicateYomi|0x80047018, -2147192808|One attribute can be tied to only one yomi at a time|
> |CannotHaveMultipleDefaultFilterTemplates|0x8004027d, -2147220867|Cannot have multiple default synchronization templates for a single entity.|
> |CannotImportNullStringsForBaseLanguage|0x80044246, -2147204538|The base language translation string present in worksheet {0}, row {1}, column {2} is null.|
> |CannotImportRuleOnAnyEntityRoutingRuleFCBOff|0x8004F845, -2147157947|Unable to import routing rule set record for entities (except case entity) as the feature control bit for entity records routing is disabled.|
> |CannotImportRuleOnFieldMetadataUnavailable|0x8004F846, -2147157946|Unable to import routing rule set record for entities (except case entity) as the metadata for msdyn_entitylogicalname field is unavailable.|
> |CannotInviteDisabledUser|0x8004D212, -2147167726|An invitation cannot be sent to a disabled user|
> |CannotLocateRecordForWorkflowActivity|0x80045031, -2147200975|A record required by this workflow job could not be found.|
> |CannotMakeReadOnlyUser|0x80041d38, -2147214024|A user cannot be made a read only user if they are the last non read only user that has the System Administrator Role.|
> |CannotMakeSelfReadOnlyUser|0x80041d39, -2147214023|You cannot make yourself a read only user|
> |CannotMergeCase|0x8004F457, -2147158953|The merge couldn't be performed. One or more of the selected cases couldn't be cancelled because of the status transition rules that are defined for cases.|
> |CannotModifyAccessToAddressBookFilters|0x80048445, -2147187643|Cannot modify access for address book filters|
> |CannotModifyAccessToOfflineFilters|0x80040272, -2147220878|Cannot modify access for offline filters|
> |CannotModifyAccessToOutlookFilters|0x80040269, -2147220887|Cannot modify access for outlook filters|
> |CannotModifyOldDataFromImport|0x80040376, -2147220618|The corresponding record in Microsoft Dynamics 365 has more recent data, so this record was ignored.|
> |CannotModifyPatchedSolution|0x80048538, -2147187400|Cannot modify solution because it has the following patches: {0}.|
> |CannotModifyReportOutsideSolutionIfManaged|0x8004F038, -2147160008|Managed solution cannot update reports which are not present in solution package.|
> |CannotModifyRollupDependentField|0x80060555, -2147089067|Rollup field {0} created this field. It can’t be modified directly.|
> |CannotModifySpecialUser|0x80041d33, -2147214029|No modifications to the 'SYSTEM' or 'INTEGRATION' user are permitted.|
> |CannotModifySupportUser|0x80041d43, -2147214013|The Support User Role cannot be modified.|
> |CannotModifySysAdmin|0x80041d31, -2147214031|The System Administrator Role cannot be modified.|
> |CannotOverrideOwnedDynamicProperty|0x80081005, -2146955259|You can't override a property that isn't inherited from a product family.|
> |CannotOverrideProperty|0x8004F887, -2147157881|You can't override this property as another overriden version of this property already exists. Please delete the previously overridden version, and then try again.|
> |CannotOverridePropertyFromDifferentHierarchy|0x8004F914, -2147157740|You can't override a property that belongs to a different product hierarchy.|
> |CannotOverwriteActiveComponent|0x8004F016, -2147160042|A managed solution cannot overwrite the {0} component {1} with Id={2} which has an unmanaged base instance.  The most likely scenario for this error is that an unmanaged solution has installed a new unmanaged {0} component on the target system, and now a managed solution from the same publisher is trying to install that same {0} component as managed.  This will cause an invalid layering of solutions on the target system and is not allowed.|
> |CannotOverwriteProperty|0x80061036, -2147086282|You can't overwrite this property as another overwritten version of this property already exists. Please delete the previously overwritten version, and then try again.|
> |CannotParseFieldFromSQL|0x80090102, -2146893566|The field with column name '{0}' on the table with name '{1}' cannot be parsed from SQL to type {2}.|
> |CannotPayNonActiveInvoice|0x80100000, -2146435072|The invoice cannot be paid because it is not in active state.|
> |CannotPropagateCamapaignActivityForTemplate|0x80040311, -2147220719|Cannot execute (distribute) a CampaignActivity for a template Campaign.|
> |CannotProvisionPartnerSolution|0x8004A10f, -2147180273|Can not provision partner solution as it is either already provisioned or going through provisioning.|
> |CannotPublishAppModule|0x80050114, -2147155692|We can’t publish the app because it has validation errors.|
> |CannotPublishBundleWithProductStateDraftOrRetire|0x8004F907, -2147157753|You can't publish this bundle because its associated products are in a draft state, are retired, or are being revised.|
> |CannotPublishChildOfNonActiveProductFamily|0x8004F909, -2147157751|You can't publish this record because it belongs to a product family that isn't published.|
> |CannotPublishEmptyRule|0x80048414, -2147187692|No criteria have been specified. Add criteria, and then publish the duplicate detection rule.|
> |CannotPublishInactiveRule|0x80048413, -2147187693|The selected duplicate detection rule is marked as Inactive. Before publishing, you must activate the rule.|
> |CannotPublishKitWithProductStateDraftOrRetire|0x8004F916, -2147157738|You can't publish this kit because its associated products are in a draft state, are retired, or are being revised.|
> |CannotPublishMoreRules|0x80048419, -2147187687|The selected record type already has the maximum number of published rules. Unpublish or delete existing rules for this record type, and then try again.|
> |CannotPublishNestedBundle|0x80061011, -2147086319|You can't publish a bundle that contains bundles. Remove any bundles from this one, and then try to publish again.|
> |CannotQualifyLead|0x80081018, -2146955240|You can't qualify this lead because you don't have permission to create accounts. Work with your system administrator to create the account and then try again.|
> |CannotQueryBaseTableWithAggregates|0x8004F00D, -2147160051|Invalid query on base table.  Aggregates cannot be included in base table query.|
> |CannotRelateObjectTypeToCampaign|0x80040307, -2147220729|Specified Object Type not supported|
> |CannotRelateObjectTypeToCampaignActivity|0x8004030d, -2147220723|Specified Object Type not supported|
> |CannotRemoveComponentFromDefaultSolution|0x8004F000, -2147160064|A Solution Component cannot be removed from the Default Solution.|
> |CannotRemoveComponentFromSolution|0x8004F021, -2147160031|Cannot find solution component {0} {1} in solution {2}.|
> |CannotRemoveComponentFromSystemSolution|0x8004F035, -2147160011|A Solution Component cannot be removed from the System Solution.|
> |CannotRemoveFromSupportUser|0x80041d45, -2147214011|A user cannot be removed from the Support User Role.|
> |CannotRemoveFromSysAdmin|0x80041d30, -2147214032|A user cannot be removed from the System Administrator Role if they are the only user that has the role.|
> |CannotRemoveMembersFromDefaultTeam|0x8004830C, -2147187956|Can't remove members from the default business unit team (TeamId = {0}).|
> |CannotRemoveNonListMember|0x80048458, -2147187624|Specified Item not a member of the specified List.|
> |CannotRemoveProductFromPricelist|0x80061008, -2147086328|You can't remove this product from the pricelist because one or more bundles refer to it.|
> |CannotRemoveSysAdminProfileFromSysAdminUser|0x8004F505, -2147158779|The Sys Admin Profile cannot be removed from a user with a Sys Admin Role|
> |CannotRemoveTenantAdminFromSysAdminRole|0x80041d64, -2147213980|Users who are granted the Microsoft Office 365 Global administrator or Service administrator role cannot be removed from the Microsoft Dynamics 365 System Administrator security role. You must first remove the Microsoft Office 365 role, and then try again.|
> |CannotResetAppointmentsToDraft|0x8004026a, -2147220886|Appointments cannot be reset to draft.|
> |CannotResetSysAdminInvite|0x8004D214, -2147167724|An invitation cannot be reset for a user if they are the only user that has the System Administrator Role.|
> |CannotRetireProduct|0x8004F915, -2147157739|You can't retire this product because it belongs to active bundles. Remove it from active bundles before you retire it.|
> |CannotRetireProductFromActiveBundle|0x8004F997, -2147157609|This product cannot be retired because it is a part of some active bundles or pricelists. Please remove it from all bundles or pricelists before retiring.|
> |CannotRevokeAccessToAddressBookFilters|0x80048444, -2147187644|Cannot revoke access for address book filters|
> |CannotRevokeAccessToOfflineFilters|0x80040273, -2147220877|Cannot revoke access for offline filters|
> |CannotRevokeAccessToOutlookFilters|0x80040270, -2147220880|Cannot revoke access for outlook filters|
> |CannotRouteInactiveQueueItem|0x80040527, -2147220185|You can't route a queue item that has been deactivated.|
> |CannotRoutePrivateQueueItemNonmember|0x80631121, -2140991199|This private queue item can't be assigned To the selected User.|
> |CannotRouteToNonQueueMember|0x80731119, -2139942631|This item cannot be routed to a non-queue member.|
> |CannotRouteToQueue|0x800404ea, -2147220246|Cannot route to Work in progress queue|
> |CannotRouteToSameQueue|0x8004051b, -2147220197|The queue item cannot be routed to the same queue|
> |CannotSecureAttribute|0x8004F501, -2147158783|The field '{0}' is not securable|
> |CannotSecureEntityKeyAttribute|0x80060896, -2147088234|The field {0} is not securable as it is part of entity keys ( {1} ). Please remove the field from all entity keys to make it securable.|
> |CannotSelectReadOnlyPublisher|0x8004F034, -2147160012|Attempting to  select a readonly publisher for solution.|
> |CannotSendInviteToDuplicateWindowsLiveId|0x8004D215, -2147167723|An invitation cannot be sent because there are multiple users with this WLID.|
> |CannotSetCaseOnHold|0x80055000, -2147135488|You do not have the permissions to set this case to an on hold status type. Please contact your system administrator.|
> |CannotSetEntitlementTermsDecrementBehavior|0x80060851, -2147088303|You do not have appropriate privileges to specify whether entitlement terms can be decremented for this case record.|
> |CannotSetEntityOnHold|0x80055004, -2147135484|You don’t have permission to put this record on hold. Contact your system administrator.|
> |CannotSetInactiveViewAsDefault|0x8004027b, -2147220869|Inactive views cannot be set as default view.|
> |CannotSetParentDefaultTeam|0x80048308, -2147187960|The default business unit team parent can't be set (TeamId = {0}).|
> |CannotSetProductAsParent|0x8004F998, -2147157608|You can only select a product family as the parent.|
> |CannotSetPublishRetiredProductsToDraft|0x80061035, -2147086283|You can't set a published or retired product record to the draft state.|
> |CannotSetSolutionSystemAttributes|0x8004F008, -2147160056|System attributes ({0}) cannot be set outside of installation or upgrade.|
> |CannotSetWindowsLiveIdForInternetMarketingUser|0x80045034, -2147200972|You cannot change the Windows Live ID for the Internet Marketing Partner user. This user does not consume a user license and is not charged to your organization.|
> |CannotShareSystemManagedTeam|0x80048339, -2147187911|You can't share or unshare a record with a system-generated access team.|
> |CannotShareWithOwner|0x80040214, -2147220972|An item cannot be shared with the owning user.|
> |CannotSpecifyAttendeeForAppointmentPropagation|0x8004031c, -2147220708|Cannot specify an attendee for appointment distribution.|
> |CannotSpecifyBothProductAndProductDesc|0x80043afb, -2147206405|You cannot set both 'productid' and 'productdescription' for the same record.|
> |CannotSpecifyBothUomAndProductDesc|0x80043afa, -2147206406|You cannot set both 'uomid' and 'productdescription' for the same record.|
> |CannotSpecifyCommunicationAttributeOnActivityForPropagation|0x8004031e, -2147220706|Cannot specify communication attribute on activity for distribution|
> |CannotSpecifyOrganizerForAppointmentPropagation|0x8004031a, -2147220710|Cannot specify an organizer for appointment distribution|
> |CannotSpecifyOwnerForActivityPropagation|0x80040327, -2147220697|Cannot specify owner on activity for distribution|
> |CannotSpecifyRecipientForActivityPropagation|0x8004031d, -2147220707|Cannot specify a recipient for activity distribution.|
> |CannotSpecifySenderForActivityPropagation|0x8004031b, -2147220709|Cannot specify a sender for appointment distribution|
> |CannotUndeleteLabel|0x8004F003, -2147160061|Attempting to undelete a label that is not marked as delete.|
> |CannotUninstallReferencedProtectedSolution|0x8004F020, -2147160032|This solution cannot be uninstalled because the '{0}' with id '{1}'  is required by the '{2}' solution. Uninstall the {2} solution and try again.|
> |CannotUninstallWithDependencies|0x8004F01D, -2147160035|Solution dependencies exist, cannot uninstall.|
> |CannotUpdateActiveModernFlow|0x80060466, -2147089306|Cannot update property "{0}" on a published Modern Flow process.|
> |CannotUpdateAppDefaultValueForStateAttribute|0x80044343, -2147204285|The default value for a status (statecode) attribute cannot be updated.|
> |CannotUpdateAppDefaultValueForStatusAttribute|0x80044344, -2147204284|The default value for a status reason (statuscode) attribute is not used. The default status reason is set in the associated status (statecode) attribute option.|
> |CannotUpdateAppModuleClientType|0x80050128, -2147155672|Can’t change the client type of this app.|
> |CannotUpdateAppModuleUniqueName|0x80050119, -2147155687|You can’t change the unique name .|
> |CannotUpdateAzureActiveDirectoryObjectIdField|0x80041d4f, -2147214001|The property AzureActiveDirectoryObjectId cannot be modified.|
> |CannotUpdateBecauseItIsReadOnly|0x8004022e, -2147220946|The object cannot be updated because it is read-only.|
> |CannotUpdateCampaignForCampaignActivity|0x8004030b, -2147220725|Parent campaign is not updatable.|
> |CannotUpdateCampaignForCampaignResponse|0x8004030c, -2147220724|Parent campaign is not updatable.|
> |CannotUpdateDeactivatedQueueItem|0x8004051d, -2147220195|This item is deactivated. To work with this item, reactivate it and then try again.|
> |CannotUpdateDefaultField|0x800608D8, -2147088168|You can’t update the isdefaultTheme attribute.|
> |CannotUpdateDefaultSolution|0x8004F009, -2147160055|Default solution attribute{0} {1} can only be set on installation or upgrade.  The value{0} cannot be modified.|
> |CannotUpdateDelaySendTimeForEmailWhenEmailIsNotInProperState|0x80050020, -2147155936|We can’t update the delay send time because the email is not a draft or isn’t scheduled to be sent.|
> |CannotUpdateDelaySendTimeWhenEEFeatureNotEnabled|0x80050021, -2147155935|We can’t update the delay send time because Email Engagement isn’t turned on for the organization.|
> |CannotUpdateDraftProducts|0x8004F975, -2147157643|You can Only update draft products.|
> |CannotUpdateEmailStatisticForEmailNotFollowed|0x80050002, -2147155966|We can’t update email statistics because the email isn’t being followed.|
> |CannotUpdateEmailStatisticForEmailNotSent|0x80050001, -2147155967|We can’t update email statistics because the email hasn’t been sent.|
> |CannotUpdateEmailStatisticWhenEEFeatureNotEnabled|0x80050018, -2147155944|We can’t update email statistics because Email Engagement isn’t turned on for the organization.|
> |CannotUpdateEntitlement|0x80060852, -2147088302|You can only set Active entitlement records as default.|
> |CannotUpdateEntitySetName|0x8004F663, -2147158429|EntitySetName cannot be updated for OOB entities|
> |CannotUpdateExternalPartyWithSameCorrelationKey|0x80061114, -2147086060|An external party record already exists with the same correlation key value.|
> |CannotUpdateGoalPeriodInfoChildGoal|0x80044901, -2147202815|You cannot update goal period related attributes on a child goal.|
> |CannotUpdateGoalPeriodInfoClosedGoal|0x80044910, -2147202800|You cannot change the time period of this goal because there are one or more closed subordinate goals.|
> |CannotUpdateLogicalAttribute|0x80048461, -2147187615|Cannot update logical attribute {0} |
> |CannotUpdateManagedSolution|0x8004F024, -2147160028|Cannot update solution '{0}' because it is a managed solution.|
> |CannotUpdateMetricOnChildGoal|0x80044900, -2147202816|You cannot update metric on a child goal.|
> |CannotUpdateMetricOnGoalWithChildren|0x80044902, -2147202814|You cannot update metric on a goal which has associated child goals.|
> |CannotUpdateMetricWithGoals|0x80044803, -2147203069|The changes made to this record cannot be saved because this goal metric is being used by one or more goals.|
> |CannotUpdateNameDefaultTeam|0x8004830A, -2147187958|The default business unit team name can't be updated (TeamId = {0}).|
> |CannotUpdateNonCustomizableString|0x80044247, -2147204537|The translation string present in worksheet {0}, row {1}, column {2} is not customizable.|
> |CannotUpdateObjectBecauseItIsInactive|0x80040230, -2147220944|The object cannot be updated because it is inactive.|
> |CannotUpdateOpportunityCurrency|0x80048479, -2147187591|The currency cannot be changed because this opportunity has Products Quotes, and/ or Orders associated with it.  If you want to change the currency please delete all of the Products/quotes/orders and then change the currency or create a new opportunity with the appropriate currency.|
> |CannotUpdateOrgDBOrgSettingWhenOffline|0x80048515, -2147187435|Organization Settings stored in Organization Database cannot be set when offline.|
> |CannotUpdateParentAndDependents|0x8004480c, -2147203060|Cannot update metric or period attributes when parent is being updated.|
> |CannotUpdatePrivateOrWIPQueue|0x800404ee, -2147220242|The private or WIP Bin queue is not allowed to be updated or deleted|
> |CannotUpdateProductCurrency|0x80048cfa, -2147185414|The currency of the product cannot be updated because there are associated price list items with pricing method percentage.|
> |CannotUpdateQuoteCurrency|0x8004480e, -2147203058|The currency cannot be changed because this quote has Products associated with it. If you want to change the currency please delete all of the Products and then change the currency or create a new quote with the appropriate currency.|
> |CannotUpdateReadOnlyPublisher|0x8004F033, -2147160013|Attempting to update a readonly publisher.|
> |CanNotUpdateRequiredBundleItem|0x80100009, -2146435063|You can't update this bundle item because it's a required product in the bundle.|
> |CannotUpdateRestrictedPublisher|0x8004F017, -2147160041|Restricted publisher ({0}) cannot be updated.|
> |CannotUpdateRestrictedSolution|0x8004F00A, -2147160054|Restricted solution ({0}) cannot be updated.|
> |CannotUpdateRollupAttributeWithClosedGoals|0x80044801, -2147203071|The changes made to the roll-up field definition cannot be saved because the related goal metric is being used by one or more closed goals.|
> |CannotUpdateRollupFields|0x80044911, -2147202799|You cannot write on rollup fields if isoverride is not set to true in your create/update request.|
> |CannotUpdateSolutionPatch|0x8004F042, -2147159998|Solution patch with version {0} already exists. Updating patch is not supported.|
> |CannotUpdateSupportUser|0x80041d47, -2147214009|Cannot update the Support User Role.|
> |CannotUpdateSyncUserIsLicensedField|0x80041d4c, -2147214004|The property IsLicensed cannot be modified.|
> |CannotUpdateSyncUserIsSyncWithDirectoryField|0x80041d4e, -2147214002|The property IsSyncUserWithDirectory cannot be modified.|
> |CannotUpdateSystemEntityIcons|0x8004F653, -2147158445|System entity icons cannot be updated.|
> |CannotUpdateSystemTheme|0x800608D6, -2147088170|You can’t modify system themes.|
> |CannotUpdateTemplateIdForEmailInNonDraftState|0x80050017, -2147155945|We can’t update the template because the email has already been sent or is not in a Draft state.|
> |CannotUpdateTriggerForPublishedRules|0x80060002, -2147090430|A trigger cannot be added/deleted/updated for a published rule.|
> |CannotUpdateUnpublishedDeleteInstance|0x8004F00F, -2147160049|The component that you are trying to update has been deleted.|
> |CannotUseOpportunitySetStateMessage|0x80100005, -2146435067|This message can not be used to set the state of opportunity to {0}. In order to set state of opportunity to {1}, use the {1} message instead.|
> |CannotUseUserCredentials|0x8005E229, -2147098071|Email connector cannot use the credentials specified in the mailbox entity. This might be because user has disallowed it. Please use other mode of credential retrieval or allow the use of credential by email connector.|
> |CanOnlySetActiveOrDraftProductFamilyAsParent|0x8004F906, -2147157754|You can only set product families in a draft or active state as parent.|
> |CantSaveRecordInOffline|0x8005F214, -2147093996|You can't save this record while you're offline.|
> |CantSetIsGuestProfile|0x8006111A, -2147086054|You can’t set or change the value of the IsGuestProfile field because it’s for internal use only.|
> |CantUpdateOnlineRecord|0x8005F224, -2147093980|You can’t update this record because it doesn’t exist in the offline mode.|
> |CanvasAppsExpectedFileMissing|0x80072356, -2147015850|The solution specified an expected assets file but that file was missing or invalid.|
> |CanvasAppsInvalidSolutionFileContent|0x80072354, -2147015852|The request to import a canvas app should contain at least one asset file.|
> |CanvasAppsNotEnabled|0x80072351, -2147015855|Creation and editing of Canvas Apps is not enabled.|
> |CanvasAppsServiceRequestClientFailure|0x80072352, -2147015854|The request to the PowerApps service failed with a client failure.|
> |CanvasAppsServiceRequestServerFailure|0x80072353, -2147015853|The request to the PowerApps service failed with a server failure.|
> |CanvasAppsUnexpectedCanvasAppId|0x80072355, -2147015851|The request to the PowerApps service resulted in a new canvasappid when the previously existing value was expected.|
> |CanvasAppVersionDoesNotMatchLatestPublishedVersion|0x80072358, -2147015848|The latest published version of the canvas app does not match the version known by the Dynamics service.|
> |CanvasAppVersionMissingOrInvalid|0x80072357, -2147015849|The app version of the canvas app was not set or was an invalid value.|
> |CapabilityLimited|0x80048557, -2147187369|"The Capability {0} has reached {1} (Limit {2}). Please upgrade to CDS FULL|
> |CapabilityNotAvailable|0x80048556, -2147187370|"The Capability {0} is not available. Please upgrade to CDS FULL|
> |CAPolicyValidationFailedLateBind|0x80072561, -2147015327|The user is in an admin restricted location.|
> |CascadeBehaviorNotSupportedInPolymorphicLookup|0x80090426, -2146892762|The cascade behavior '{0}' is not supported. The cascade behaviors supported for polymorphic lookup are CascadeAssign=Nocascade, CascadeDelete=RemoveLink, CascadeMerge=Nocascade, CascadeReparent=Nocascade, CascadeShare=Nocascade, CascadeUnshare=Nocascade and CascadeRollupView=Nocascade. EntityId '{1}', AttributeId '{2}'|
> |CascadeDeleteNotAllowDelete|0x80048103, -2147188477|Object is not allowed to be deleted|
> |CascadeFailToCreateNativeDAWrapper|0x80048108, -2147188472|Failed to create unmanaged data access wrapper|
> |CascadeInvalidExtraConditionValue|0x80048101, -2147188479|Invalid Extra-condition value|
> |CascadeInvalidLinkType|0x80048102, -2147188478|Invalid CascadeLink Type|
> |CascadeInvalidLinkTypeTransition|0x80044155, -2147204779|Invalid link type for system entity cascading actions.|
> |CascadeMergeInvalidSpecialColumn|0x80048106, -2147188474|Invalid Column Name for Merge Special Casing|
> |CascadeOperationConcurrentRequested|0x80048105, -2147188475|More than one concurrent {0} requests detected for an Entity {1} and ObjectTypeCode {2}.|
> |CascadeProxyEmptyCallerId|0x8004810b, -2147188469|Empty Caller Id|
> |CascadeProxyInvalidNativeDAPtr|0x80048109, -2147188471|Invalid pointer of unmanaged data access object|
> |CascadeProxyInvalidPrincipalType|0x8004810a, -2147188470|Invalid security principal type|
> |CascadeRemoveLinkOnNonNullable|0x80048104, -2147188476|CascadeDelete is defined as RemoveLink while the foreign key is not nullable|
> |CascadeReparentOnNonUserOwned|0x80048107, -2147188473|Cannot perform Cascade Reparent on Non-UserOwned entities|
> |CaseAlreadyResolved|0x800404cf, -2147220273|This case has already been resolved. Close and reopen the case record to see the updates.|
> |CaseStateChangeInvalid|0x8006074, 134242420|Because of the status transition rules, you can't resolve a case in the current status. Change the case status, and then try resolving it, or contact your system administrator.|
> |CategoryDataTypeInvalid|0x8004E01A, -2147164134|The Data Description for the visualization is invalid. The attribute type for the group by of one of the categories is invalid. Correct the Data Description.|
> |CategoryNotSetToBusinessProcessFlow|0x80060404, -2147089404|Category should be set to BusinessProcessFlow while creating business process flow category|
> |CDSOrgNotSupported|0x80044510, -2147203824|Dynamics 365 for Outlook is not supported for this organization.|
> |CertificateNotFound|0x8005E239, -2147098055|The given certificate cannot be found.|
> |ChangeTrackingDisabledForMobileOfflineError|0x800609A1, -2147087967|You can not disable change tracking for this entity since mobile offline is already enabled.|
> |ChangeTrackingNotEnabledForEntity|0x80072491, -2147015535|Entity {0} isn't enabled for change tracking.|
> |ChangeTrackingNotEnabledForRelatedEntities|0x80072492, -2147015534|Changes cannot be retrieved for intersect entity {0} since both related entities are not enabled for change tracking.|
> |ChannelAccessProfileRuleAlreadyInDraftState|0x80061115, -2147086059|You can't deactivate a draft channel access profile rule.|
> |ChannelPropertyGroupAlreadyExistsWithSameSourceType|0x800608EC, -2147088148|A record for the specified source type already exists. You can't create another one.|
> |ChannelPropertyNameInvalid|0x800608F2, -2147088142|The channel property name is invalid. The name can only contain '_', numerical, and alphabetical characters. Choose a different name, and try again.|
> |ChartAreaCategoryMismatch|0x8004E005, -2147164155|Number of chart areas and number of categories should be same.|
> |ChartTypeNotSupportedForComparisonChart|0x8004E018, -2147164136|This chart type is not supported for comparison charts.|
> |ChartTypeNotSupportedForMultipleSeriesChart|0x8004E021, -2147164127|Series of chart type {0} is not supported for multi-series charts.|
> |CheckPrivilegeGroupForUserOnPremiseError|0x80048401, -2147187711|Please select an account that is a member of the PrivUserGroup security group and try again.|
> |CheckPrivilegeGroupForUserOnSplaError|0x80048400, -2147187712|Please select a Dynamics 365 System Administrator account that belongs to the root business unit and try again.|
> |ChildBusinessDoesNotExist|0x80041d22, -2147214046|The child businesss Id is invalid.|
> |ChildUserDoesNotExist|0x80041d26, -2147214042|The child user Id is invalid.|
> |ChildWorkflowNotFound|0x8004502F, -2147200977|This workflow cannot run because one or more child workflows it uses have not been published or have been deleted. Please check the child workflows and try running this workflow again.|
> |ChildWorkflowParameterMismatch|0x80045048, -2147200952|This workflow cannot run because arguments provided by parent workflow does not match with the specified parameters in linked child workflow. Check the child workflow reference in parent workflow and try running this workflow again.|
> |ChunkSizeExceeded|0x80090008, -2146893816|Invalid file chunk size: {0} MB. Maximum chunk size supported: {1} MB.|
> |CircularDependency|0x80071157, -2147020457|The solution operation failed due to a circular dependency with other solutions. Please check the exception for more details: {0}|
> |ClientAuthCanceled|0x8004D224, -2147167708|Authentication was canceled by the user.|
> |ClientAuthNoConnectivity|0x8004D226, -2147167706|There is no connectivity.|
> |ClientAuthNoConnectivityOffline|0x8004D225, -2147167707|There is no connectivity when running in offline mode.|
> |ClientAuthOfflineInvalidCallerId|0x8004D227, -2147167705|Offline SDK calls must be made in the offline user context.|
> |ClientAuthSignedOut|0x8004D221, -2147167711|The user signed out.|
> |ClientAuthSyncIssue|0x8004D223, -2147167709|Synchronization between processes failed.|
> |ClientServerDateTimeMismatch|0x80044503, -2147203837|Your computer's date/time is out of sync with the server by more than 5 minutes.|
> |ClientServerEmailAddressMismatch|0x80044504, -2147203836|The Outlook email address and Dynamics 365 user email address do not match.|
> |ClientUpdateAvailable|0x8004D294, -2147167596|There's an update available for Dynamics 365 for Outlook.|
> |ClientVersionTooHigh|0x80044501, -2147203839|This version of Outlook client isn't compatible with your Dynamics 365 organization (current version {0} is too high).|
> |ClientVersionTooLow|0x80044500, -2147203840|This version of Outlook client isn't compatible with your Dynamics 365 organization (current version {0} is too low).|
> |CloneSolutionException|0x80048539, -2147187399|Operation on clone solution failed.|
> |CloneSolutionPatchException|0x80061771, -2147084431|Patch '{0}' has a matching or higher version ({1}) than that of the patch being installed.|
> |CloneTitleTooLong|0x80071112, -2147020526|A validation error occurred. The length of the Name attribute of the mobileofflineprofile entity exceeded the maximum allowed length of 200.|
> |CloseActiveChildCaseFirst|0x8003F452, -2147224494|Close active child case before closing parent case.|
> |ColorStripAttributesExceeded|0x80061500, -2147085056|Color Strip section cannot have more than 1 attribute|
> |ColorStripAttributesInvalid|0x80061502, -2147085054|Color Strip section can only have attributes of type Two Options, Option Set and Status Reason|
> |ColumnNameNotFound|0x80090101, -2146893567|The column with name '{0}' cannot be found on the table with name '{1}'.|
> |CombinedManagedPropertyFailure|0x8004F027, -2147160025|The evaluation of the current component(name={0}, id={1}) in the current operation ({2}) failed during at least one managed property evaluations: {3}|
> |CommandNotSupported|0x80154B52, -2146088110|Command is not supported in offline mode.|
> |CommitFileFailure|0x80072556, -2147015338|Error occured when commiting file. (chunkList size: {0}, uploadToken: {1}, fileName:{2}, mimeType:{3})|
> |CommunicationBlocked|0x80044506, -2147203834|Communication is blocked due to a socket exception.|
> |ComponentDefinitionDoesNotExists|0x8004F019, -2147160039|No component definition exists for the component type {0}.|
> |ComponentDisabledForMigration|0x80072014, -2147016684|Component with name {0} is not enabled for import on this organization.|
> |ComponentNotConfiguredForSoftDelete|0x80072038, -2147016648|Component {0} does not support soft deletion|
> |ConcurrencyVersionMismatch|0x80060882, -2147088254|The version of the existing record doesn't match the RowVersion property provided.|
> |ConcurrencyVersionNotProvided|0x80060883, -2147088253|The RowVersion property must be provided when the value of ConcurrencyBehavior is IfVersionMatches.|
> |ConcurrentOperationFailure|0x80071154, -2147020460|The current {0} operation failed due to another concurrent operation running at the same time. Please try again later.|
> |ConditionAttributesNotAnSubsetOfStepAttributes|0x80060436, -2147089354|Attributes of the condition are not the subset of attributes in the Step, for the Stage : {0}|
> |ConditionBranchDoesHaveSetNextStageOnlyChildInXaml|0x80060434, -2147089356|Branch condition can contain only SetNextStage as a child.|
> |ConditionStepCountInXamlExceedsMaxAllowed|0x80060435, -2147089355|{0} cannot have more than one {1}.|
> |ConfigDBCannotDeleteDefaultOrganization|0x8004D23B, -2147167685|The default {0} organization cannot be deleted from the MSCRM_CONFIG database.|
> |ConfigDBCannotDeleteObjectDueState|0x8004D232, -2147167694|Cannot delete '{0}' with Value = ({1}) in this State = ({2}) from MSCRM_CONFIG database|
> |ConfigDBCannotUpdateObjectDueState|0x8004D237, -2147167689|Cannot update '{0}' with Value = ({1}) in this State = ({2}) from MSCRM_CONFIG database|
> |ConfigDBCascadeDeleteNotAllowDelete|0x8004D233, -2147167693|Cannot delete '{0}' with Value = ({1}) due to child '{2}' references from MSCRM_CONFIG database|
> |ConfigDBDuplicateRecord|0x8004D231, -2147167695|Duplicate '{0}' with Value = ({1}) exists in MSCRM_CONFIG database|
> |ConfigDBObjectDoesNotExist|0x8004D230, -2147167696|'{0}' with Value = ({1}) does not exist in MSCRM_CONFIG database|
> |ConfigMissingDescription|0x80044197, -2147204713|Description must be specified.|
> |ConfigNullPrimaryKey|0x80044196, -2147204714|Primary Key cannot be nullable.|
> |ConfigurationPageNotValidForSolution|0x8004701D, -2147192803|The solution configuration page must exist within the solution it represents.|
> |ConfigureClaimsBeforeIfd|0x8004D266, -2147167642|You must configure claims-based authentication before you can configure an Internet-facing deployment.|
> |ConfiguredUserIsDifferentThanSuppliedUser|0x80044508, -2147203832|Configured user is different than supplied user.|
> |ConflictForOverriddenPropertiesEncountered|0x80081010, -2146955248|This record can't be published. One of the properties that was changed for this record conflicts with its inherited version. Remove the conflicting property, and then try again.|
> |ConflictingProvisionTypes|0x8004B02C, -2147176404|The service component {0} has conflicting provision types.|
> |ConnectionCannotBeEnabledOnThisEntity|0x80048214, -2147188204|Connections cannot be enabled on this {0} entity with id {1}.|
> |ConnectionExists|0x80048208, -2147188216|Connection already exists.|
> |ConnectionInvalidStartEndDate|0x80048209, -2147188215|Start date / end date is invalid.|
> |ConnectionNotSupported|0x80048213, -2147188205|The selected record does not support connections. You cannot add the connection.|
> |ConnectionObjectsMissing|0x80048210, -2147188208|Both objects being connected are missing.|
> |ConnectionRoleNotValidForObjectType|0x80048215, -2147188203|The record of type {0} (Object type code {1}) is not defined for use with connection role {2} with id {3}.|
> |ConnectionTimeOut|0x80071024, -2147020764|Unable to copy the documents because the network connection timed out.  Please try again later or contact your system administrator.|
> |ConnectorLogicalNameAlreadyExists|0x80072606, -2147015162|The connector logical name '{0}' already exists in the org.|
> |ConnectorNotEnabled|0x80072600, -2147015168|Creation and editing of Connector is not enabled.|
> |ContactDoesNotExist|0x80040503, -2147220221|Contact does not exist.|
> |ContactLoopBeingCreated|0x8004050a, -2147220214|Creating this parental association would create a loop in Contacts hierarchy.|
> |ContactLoopExists|0x80040509, -2147220215|Loop exists in the contacts hierarchy.|
> |ContextIsNull|0x80060445, -2147089339|Error creating or updating Business Process: context cannot be null.|
> |ContractDetailDiscountAmount|0x80044413, -2147204077|The contract's discount type does not support 'percentage' discounts.|
> |ContractDetailDiscountAmountAndPercent|0x80044414, -2147204076|Both 'amount' and 'percentage' cannot be set.|
> |ContractDetailDiscountPercent|0x80044412, -2147204078|The contract's discount type does not support 'amount' discounts.|
> |ContractInvalidAllotmentTypeCode|0x80043205, -2147208699|The allotment type code is invalid.|
> |ContractInvalidBillToAddress|0x8004320f, -2147208689|The bill-to address of the contract is invalid.|
> |ContractInvalidBillToCustomer|0x80043210, -2147208688|The bill-to customer of the contract is invalid.|
> |ContractInvalidContract|0x80043213, -2147208685|The contract is invalid.|
> |ContractInvalidContractTemplate|0x80043211, -2147208687|The contract template is invalid.|
> |ContractInvalidCustomer|0x8004320d, -2147208691|The customer of the contract is invalid.|
> |ContractInvalidDatesForRenew|0x80043218, -2147208680|The start date / end date of this renewed contract can not overlap with any other invoiced / active contracts with the same contract number.|
> |ContractInvalidDiscount|0x80044193, -2147204717|Discount cannot be greater than total price.|
> |ContractInvalidPrice|0x80043215, -2147208683|The price is invalid.|
> |ContractInvalidServiceAddress|0x8004320e, -2147208690|The service address of the contract is invalid.|
> |ContractInvalidStartEndDate|0x80043202, -2147208702|Start date / end date or billing start date / billing end date is invalid.|
> |ContractInvalidState|0x80043203, -2147208701|The state of the contract is invalid.|
> |ContractLineInvalidState|0x80043204, -2147208700|The state of the contract line item is invalid.|
> |ContractNoLineItems|0x8004320c, -2147208692|There are no contract line items for this contract.|
> |ContractTemplateDoesNotExist|0x80043206, -2147208698|The contract template does not exist.|
> |ContractTemplateNoAbbreviation|0x8004320b, -2147208693|Abbreviation can not be NULL.|
> |ControlDescriptionSchemaValidation|0x80160018, -2146041832|Control Description failed schema validationSpecifically look at {0}. More Details:{1}|
> |ControlIdIsNotUnique|0x80060411, -2147089391|Control id {0} in the Xaml is not unique|
> |ControlIdIsNullOrEmpty|0x80072344, -2147015868|Control id cannot be null or empty|
> |ControlReferenceValidationUnhandledError|0x80160005, -2146041851|Unhandled error during control configuration validation. More Details:{0}|
> |ConvertFetchDataSetError|0x8004832e, -2147187922|An unexpected error occurred while processing the Fetch data set.|
> |ConvertReportToCrmError|0x8004832d, -2147187923|An unexpected error occurred while converting supplied report to Dynamics 365 format.|
> |ConvertRuleActivateDeactivateByNonOwner|0x8004F886, -2147157882|This Convert Rule Set cannot be activated or deactivated by someone who is not its owner.|
> |ConvertRuleAlreadyActive|0x80060731, -2147088591|Selected ConvertRule is already in active state. Please select another record and try again|
> |ConvertRuleAlreadyInDraftState|0x80060732, -2147088590|Selected ConvertRule is already in draft state. Please select another record and try again|
> |ConvertRuleInvalidAutoResponseSettings|0x8004F879, -2147157895|Select an email template for an autoresponse or set the autoresponse option to No.|
> |ConvertRulePermissionToPerformAction|0x80060733, -2147088589|You don't have the required permissions on ConvertRules and processes to perform this action.|
> |ConvertRuleQueueIdMissingForEmailSource|0x8004F896, -2147157866|Queue value required. Provide a value for the queue.|
> |ConvertRuleResponseTemplateValidity|0x80060730, -2147088592|Please select either a global or case template.|
> |CopyGenericError|0x80071027, -2147020761|An error has occurred while copying files. Please try again later. If the problem persists, contact your system administrator.|
> |CopyNotAllowedForInternetMarketing|0x80048474, -2147187596|Duplicating campaigns that have Internet Marketing Campaign Activities is not allowed|
> |CorruptedHiddensheetData|0x800609B7, -2147087945|The hidden sheet data is corrupted.|
> |CouldNotDecryptOAuthToken|0x8005F110, -2147094256|Yammer OAuth token could not be decrypted. Please try to reconfigure Yammer once again.|
> |CouldNotFindQueueItemInQueue|0x80040524, -2147220188|Could not find any queue item associated with the Target in the specified SourceQueueId. Either the SourceQueueId or Target is invalid or the queue item does not exist.|
> |CouldNotObtainLockOnResource|0x80044339, -2147204295|Database resource lock could not be obtained. For more information, see http://docs.microsoft.com/dynamics365/customer-engagement/customize/best-practices-workflow-processes#limit-the-number-of-workflows-that-update-the-same-entity|
> |CouldNotReadAccessToken|0x8005F105, -2147094267|The system was not able to read users Yammer access token although a non-empty code was passed.|
> |CouldNotSetLocationTypeToOneNote|0x80060905, -2147088123|Couldn't set location type of document location to OneNote.|
> |CountSpecifiedWithoutOrder|0x8004E01F, -2147164129|The Data Description for the visualization is invalid as it does not specify an order node for the count attribute.|
> |CreatePolymorphicLookupAttributeApiIsNotActive|0x80090425, -2146892763|CreatePolymorphicLookupAttribute API is not active. Entity name '{0}', attribute name '{1}'.|
> |CreatePropertyError|0x8004F889, -2147157879|An error occurred while saving the {0} property.|
> |CreatePropertyInstanceError|0x8004F890, -2147157872|An error occurred while saving the {0} property instance.|
> |CreatePublishedWorkflowDefinitionWorkflowDependency|0x8004500A, -2147201014|Cannot create a workflow dependency for a published workflow definition.|
> |CreateRecurrenceRuleFailed|0x8004E101, -2147163903|Cannot create the recurrence rule.|
> |CreateWorkflowActivationWorkflowDependency|0x80045009, -2147201015|Cannot create a workflow dependency associated with a workflow activation.|
> |CreateWorkflowDependencyForPublishedTemplate|0x80045019, -2147200999|Cannot create a workflow dependency for a published workflow template.|
> |CrmConstraintEvaluationError|0x80040261, -2147220895|Crm constraint evaluation error occurred.|
> |CrmConstraintParsingError|0x80040262, -2147220894|Crm constraint parsing error occurred.|
> |CrmExpressionBodyParsingError|0x8004025e, -2147220898|Crm expression body parsing error occurred.|
> |CrmExpressionEvaluationError|0x80040260, -2147220896|Crm expression evaluation error occurred.|
> |CrmExpressionParametersParsingError|0x8004025f, -2147220897|Crm expression parameters parsing error occurred.|
> |CrmExpressionParsingError|0x8004025d, -2147220899|Crm expression parsing error occurred.|
> |CRMGlobalMetadataVersionMismatch|0x80072494, -2147015532|Mismatch in CRM global metadata version when retrieving data for entity: '{0}'. Global metadata version before retrieving data: '{1}'. Global metadata version after retrieving data: '{2}'|
> |CrmHttpError|0x8006088A, -2147088246|A failure occurred in Wep Api in Dynamics 365.|
> |CrmImpersonationError|0x80040245, -2147220923|Error occurred in the Crm AutoReimpersonator.|
> |CrmLicensingError|0x80050300, -2147155200|A failure occurred during licensing check.|
> |CrmLicensingNoServicePlan|0x80050301, -2147155199|This application requires an appropriate license. This user with userId={0} does not have appropriate license(s) to access this application uniqueName={1} with Id={2} from publisher={3}. An appropriate license is required with one of these service plans : {5}. For more information, please refer https://go.microsoft.com/fwlink/p/?linkid=2122607 |
> |CrmLicensingNoUserPass|0x80050302, -2147155198|This application requires an appropriate license. This user with userId={0} does not have an appropriate license to access this application uniqueName={1} with Id={2} from publisher={3}. An appropriate license is required or the organization instance needs to have sufficient per app licenses assigned, for accessing custom applications. For more information, please refer https://go.microsoft.com/fwlink/p/?linkid=2122607 |
> |CrmLiveAddOnAddLicenseLimitReached|0x8004B056, -2147176362|Your subscription has the maximum number of user licenses available.  For additional licenses, please contact our sales organization at 1-877-Dynamics 365-CHOICE (276-2464).|
> |CrmLiveAddOnAddStorageLimitReached|0x8004B057, -2147176361|Your storage consumption has reached the maximum storage limit allotted to this environment. Trial environments are allocated with limited resources. If you are not using a trial environment, please contact support.|
> |CrmLiveAddOnDataChanged|0x8004B05C, -2147176356|Due to recent changes you have made to your account, these changes cannot be made at this time.   Close this wizard, and try again later.  If the problem persists, please contact our sales organization at 1-877-Dynamics 365-CHOICE (276-2464).|
> |CrmLiveAddOnOrgInNoUpdateMode|0x8004B059, -2147176359|Your changes cannot be processed at this time. Your organization is currently being updated.  No changes have been made to your account.  Close this wizard, and try again later.  If the problem persists, please contact our sales organization at 1-877-Dynamics 365-CHOICE (276-2464).|
> |CrmLiveAddOnRemoveStorageLimitReached|0x8004B058, -2147176360|Your organization has the minimum amount of storage allowed.  You can remove only storage that has been added to your organization, and  is not being used.|
> |CrmLiveAddOnUnexpectedError|0x8004B055, -2147176363|There was an error contacting the billing system.  Your request cannot be processed at this time.  No changes have been made to your account.  Close this wizard, and try again later.  If the problem persists, please contact our sales organization at 1-877-Dynamics 365-CHOICE (276-2464).|
> |CrmLiveCannotFindExternalMessageProvider|0x8004B051, -2147176367|External Message Provider could not be located for queue item type of: {0}.|
> |CrmLiveDnsDomainAlreadyExists|0x8004B048, -2147176376|Domain already exists in the DNS table.|
> |CrmLiveDnsDomainNotFound|0x8004B047, -2147176377|Domain was not found in the DNS table.|
> |CrmLiveDuplicateWindowsLiveId|0x8004B046, -2147176378|A user with this username already exists.|
> |CrmLiveExecuteCustomCodeDisabled|0x8004B063, -2147176349|Execution of custom code feature for this organization is disabled.|
> |CrmLiveGenericError|0x8004B000, -2147176448|An error has occurred while processing your request.|
> |CrmLiveInternalProvisioningError|0x8004B003, -2147176445|An unexpected error happened in the provisioning system.|
> |CrmLiveInvalidEmail|0x8004B05D, -2147176355|Invalid email address entered.|
> |CrmLiveInvalidExternalMessageData|0x8004B052, -2147176366|External Message Data has some invalid data.  Data: {0} External Message: {1}|
> |CrmLiveInvalidInvoicingAccountNumber|0x8004B05B, -2147176357|This Invoicing Account Number is not valid because it contains an invalid character.|
> |CrmLiveInvalidPhone|0x8004B05E, -2147176354|Invalid phone number entered.|
> |CrmLiveInvalidQueueItemSchedule|0x8004B039, -2147176391|The QueueItem has an invalid schedule of start time {0} and end time {1}.|
> |CrmLiveInvalidSetupParameter|0x8004B005, -2147176443|The parameter to Dynamics 365 Online Setup is incorrect or not specified.|
> |CrmLiveInvalidTaxId|0x8004B064, -2147176348|Invalid TaxId entered.|
> |CrmLiveInvalidZipCode|0x8004B05F, -2147176353|Invalid zip code entered.|
> |CrmLiveInvoicingAccountIdMissing|0x8004B045, -2147176379|Invoicing Account Number (SAP Id) cannot be empty for an invoicing sku.|
> |CrmLiveMissingActiveDirectoryGroup|0x8004B002, -2147176446|The specified Active Directory Group does not exist.|
> |CrmLiveMissingServerRolesInScaleGroup|0x8004B007, -2147176441|The scalegroup is missing some required server roles. 1 Witness Server and 2 Sql Servers are required for Provisioning.|
> |CrmLiveMonitoringOrganizationExistsInScaleGroup|0x8004B026, -2147176410|Only one monitoring organization is allowed in a scalegroup.|
> |CrmLiveMultipleWitnessServersInScaleGroup|0x8004B006, -2147176442|The ScaleGroup has multiple witness servers specified. There should be only 1 witness server in a scale group.|
> |CrmLiveOrganizationDeleteFailed|0x8004B02E, -2147176402|An error has occurred when deleting the organization.|
> |CrmLiveOrganizationDetailsNotFound|0x8004B030, -2147176400|Unable to find organization details.|
> |CrmLiveOrganizationDisableFailed|0x8004B054, -2147176364|Disabling Organization Failed.|
> |CrmLiveOrganizationEnableFailed|0x8004B053, -2147176365|Enabling Organization Failed.|
> |CrmLiveOrganizationFriendlyNameTooLong|0x8004B032, -2147176398|The organization name provided is too long.|
> |CrmLiveOrganizationFriendlyNameTooShort|0x8004B031, -2147176399|The organization name provided is too short.|
> |CrmLiveOrganizationProvisioningFailed|0x8004B001, -2147176447|An error has occurred when provisioning the organization.|
> |CrmLiveOrganizationUniqueNameInvalid|0x8004B035, -2147176395|The unique name provided is not valid.|
> |CrmLiveOrganizationUniqueNameReserved|0x8004B036, -2147176394|The unique name is already reserved.|
> |CrmLiveOrganizationUniqueNameTooLong|0x8004B034, -2147176396|The unique name provided is too long.|
> |CrmLiveOrganizationUniqueNameTooShort|0x8004B033, -2147176397|The unique name provided is too short.|
> |CrmLiveOrganizationUpgradeFailed|0x8004B014, -2147176428|Upgrade Of Crm Organization Failed.|
> |CrmLiveQueueItemDoesNotExist|0x8004B004, -2147176444|The specified queue item does not exist in the queue. It may have been deleted or its ID may not have been specified correctly|
> |CrmLiveQueueItemTimeInPast|0x8004B040, -2147176384|A QueueItem cannot be scheduled to start or end in the past.|
> |CrmLiveRegisterCustomCodeDisabled|0x8004B062, -2147176350|Registration of custom code feature for this organization is disabled.|
> |CrmLiveServerCannotHaveWitnessAndDataServerRoles|0x8004B008, -2147176440|A server cannot have both Witness and Data Server Roles.|
> |CrmLiveSupportOrganizationExistsInScaleGroup|0x8004B025, -2147176411|Only one support organization is allowed in a scalegroup.|
> |CrmLiveUnknownCategory|0x8004B05A, -2147176358|This Category specified is not valid.|
> |CrmLiveUnknownSku|0x8004B041, -2147176383|This Sku specified is not valid.|
> |CrmMalformedExpressionError|0x8004025c, -2147220900|Crm malformed expression error occurred.|
> |CrmQueryExpressionNotInitialized|0x8004024d, -2147220915|The QueryExpression has not been initialized. Please use the constructor that takes in the entity name to create a correctly initialized instance|
> |CrmSecurityError|0x80040256, -2147220906|A failure occurred in CrmSecurity.|
> |CrmSQLCharLengthTooLong|0x80073001, -2147012607|A validation error occurred. A string value provided is too long.|
> |CrmSqlGovernorDatabaseRequestDenied|0x8004A001, -2147180543|The server is busy and the request was not completed. Try again later.|
> |CrmSQLNetworkingError|0x80073000, -2147012608|A networking error caused this operation to fail. Please try again.|
> |CrmSQLUniqueIndexOrConstraintViolation|0x80073002, -2147012606|The operation attempted to insert a duplicate value for an attribute with a unique constraint.|
> |CRMUserDoesNotExist|0x80040354, -2147220652|No Microsoft Dynamics 365 user exists with the specified domain name and user ID|
> |CrossEntityRelationshipInvalidOperation|0x80092006, -2146885626|Invalid cross-entity stage transition. Specified relationship cannot be modified.|
> |CurrencyCannotBeNullDueToNonNullMoneyFields|0x80048cfb, -2147185413|The currency cannot be null.|
> |CurrencyFieldMissing|0x8004E026, -2147164122|Record currency is required to calculate rollup field of type currency. Provide a currency and try again.|
> |CurrencyNotEqual|0x80048cea, -2147185430|The currency of the {0} does not match the currency of the {1}.|
> |CurrencyRequiredForDiscountTypeAmount|0x80048cf7, -2147185417|The currency cannot be null for discount type amount.|
> |CurrentFormEntityIsNull|0x80060371, -2147089551|Current Form Entity cannot be NULL|
> |CustomActionMustBeMarked|0x80060381, -2147089535|Custom Action must be marked ‘As a Business Process Flow action step’ to use as BPF action step.|
> |CustomActivityCannotBeMailMergeEnabled|0x8004F124, -2147159772|A custom entity defined as an activity already cannot have MailMerge enabled.|
> |CustomActivityInvalid|0x8004501D, -2147200995|Invalid custom activity.|
> |CustomActivityMustHaveOfflineAvailability|0x8004F122, -2147159774|A custom entity defined as an activity must have Offline Availability.|
> |CustomControlDescriptionMissingForControl|0x80160019, -2146041831|There needs to be a one-to-one mapping between the control and its description No matching ControlDescription found for the custom control {0}. More Details:{1}|
> |CustomControlNotAllowedInFooter|0x80160004, -2146041852|Custom controls are not allowed in footer. More Details:{0}|
> |CustomControlsDependentPropertyConfiguration|0x80160002, -2146041854|Property "{0}" can only be configured after property "{1}" has been assigned a value.|
> |CustomControlsImportError|0x80160000, -2146041856|An error occurred while importing Custom Controls. Try importing this solution again.|
> |CustomControlsPropertySetConfiguration|0x80160003, -2146041853|Property "{0}" can only be configured after Corresponding DataSet "{1}" view has been assigned a value.|
> |CustomControlWithIdNotFound|0x80160008, -2146041848|Custom control with Id {0} does not exist. More Details:{1}|
> |CustomControlWithNameNotFound|0x80160007, -2146041849|Custom control with name {0} does not exist. More Details:{1}|
> |CustomDataTypeCreateRestricted|0x80090118, -2146893544|Creation of data type '{0}' is not enabled in current publisher context.|
> |CustomDataTypeMemberCreateRestricted|0x80090119, -2146893543|Creation of data type member '{0}' is not enabled in current publisher context.|
> |CustomerIsInactive|0x80040517, -2147220201|An inactive customer cannot be set as the parent of an object.|
> |CustomerOpportunityRoleExists|0x80048202, -2147188222|Customer opportunity role exists.|
> |CustomerRelationshipCannotBeDeleted|0x8004847d, -2147187587|This relationship {1} is required by the {0} attribute and can't be deleted. To delete this relationship, first delete the lookup attribute.|
> |CustomerRelationshipExists|0x80048201, -2147188223|Customer relationship already exists. CustomerRelationshipId: {0}, CustomerId: {1}, CustomerIdType: {2}, PartnerId: {3}, PartnerIdType: {4}, CustomerRoleId: {5}, PartnerRoleId: {6}, UniqueDscId: {7}|
> |CustomImageAttributeOnlyAllowedOnCustomEntity|0x80048531, -2147187407|A custom image attribute can only be added to a custom entity.|
> |CustomizationFileMissing|0x8004F066, -2147159962|Please provide a valide CustomizationFile or a valid StageSolutionUploadId to download the CustomizationFile.|
> |CustomizationLockEx_BlockedUnknown|0x8004F062, -2147159966|Cannot start the requested operation because there is another [{0}] running at this moment. Use Solution History for more details.|
> |CustomizationLockEx_BlockingUnknown|0x8004F067, -2147159961|Cannot start the requested operation [{0}] because there is a customization running at this moment. Use Solution History for more details.|
> |CustomizationLockEx_BothKnownDifferent|0x8004F064, -2147159964|Cannot start the requested operation [{0}] because there is another [{1}] running at this moment. Use Solution History for more details.|
> |CustomizationLockEx_BothKnownSame|0x8004F063, -2147159965|Cannot start another [{0}] because there is a previous [{1}] running at this moment. Use Solution History for more details.|
> |CustomizationLockEx_BothUnknown|0x8004F061, -2147159967|Cannot start the requested operation because there is a customization running at this moment. Use Solution History for more details.|
> |CustomOperationNotActivated|0x80045052, -2147200942|Process action associated with this process is not activated.|
> |CustomParentingSystemNotSupported|0x80047102, -2147192574|A custom entity can not have a parental relationship to a system entity|
> |CustomPeriodGoalHavingExtraInfo|0x80044904, -2147202812|For a goal of custom period type, fiscal year and fiscal period attributes must be left blank.|
> |CustomPeriodGoalMissingInfo|0x80044907, -2147202809|For a goal of custom period type, goalstartdate and goalenddate attributes must have data.|
> |CustomReflexiveRelationshipNotAllowedForEntity|0x8004432C, -2147204308|This entity is not valid for a custom reflexive relationship|
> |CustomTypeAttributeCreateRestricted|0x80090117, -2146893545|Use of data type {0} for attribute '{1}' of entity with id = '{2}' is not enabled in current publisher context.|
> |CustomWorkflowActivitiesNotSupported|0x80045051, -2147200943|Custom Workflow Activities are not enabled.|
> |CyclicalRelationship|0x80047004, -2147192828|The specified relationship will result in a cycle.|
> |CyclicDependency|0x80071156, -2147020458|Cyclic component dependency detected. Please check the exception for more details. Fix the invalid dependencies and try the operation one more time. Detaisl: {0}|
> |CyclicReferencesNotSupported|0x8004417F, -2147204737|The input contains a cyclic reference, which is not supported.|
> |DatabaseCallsBlockedFailure|0x80072401, -2147015679|This invocation may lead to calls to Database which is not allowed.|
> |DatacenterNotAvailable|0x8004B065, -2147176347|This datacenter endpoint is not currently available for this organization.|
> |DataColumnsNumberMismatch|0x80040345, -2147220667|The number of fields differs from the number of column headings.|
> |DataEngineQueryThrottling|0x80048544, -2147187388|This query cannot be executed because it conflicts with throttling optimization.|
> |DataFieldNameIsMissing|0x80160021, -2146041823|Required attribute \datafieldname\ is missing for control. More Details:{0}|
> |DatafieldNameShouldBeNull|0x8006041b, -2147089381|ActionStep {0} references invalid DataFieldName {1}.|
> |DataFieldSpecifiedIsNotALookup|0x80160022, -2146041822|The datafieldname attribute {0} is not of type lookup. More Details:{1}|
> |DataMigrationManagerMandatoryUpdatesNotInstalled|0x80044336, -2147204298|First-time configuration of the Data Migration Manager has been canceled. You will not be able to use the Data Migration Manager until configuration is completed.|
> |DataMigrationManagerUnknownProblem|0x80044333, -2147204301|The Data Migration Manager encountered an unknown problem and cannot continue. To try again, restart the Data Migration Manager.|
> |DatasetControlSchemaInvalid|0x80160016, -2146041834|The dataset '{0}' should contain ViewId, IsUserView, or both nodes {1}. More Details:{2}|
> |DatasetWithNameNotFound|0x80160036, -2146041802|Dataset with name '{0}' not found Dataset Configuration for reference: {1}. More Details:{2}|
> |DatasheetNotAvailable|0x800609B5, -2147087947|The data sheet is not available.|
> |DataSourceInitializeFailedErrorCode|0x8005F210, -2147094000|Try this action again. If the problem continues, check the {0} for solutions or contact your organization's {#Brand_CRM} Administrator. Finally, you can contact {1}.|
> |DataSourceOfflineErrorCode|0x8005F211, -2147093999|This operation failed because you're offline. Reconnect and try again.|
> |DataSourceProhibited|0x8004830D, -2147187955|A non fetch based data source is not permitted on this report|
> |DataStoreKeyNotFoundErrorCode|0x8005F21d, -2147093987|Not in local store with key '{0}'|
> |DataSyncBadRequest|0x80072514, -2147015404|The request could not be understood by the server|
> |DataSyncNoContent|0x80072512, -2147015406|No data sync content|
> |DataSyncRequestAccepted|0x80072511, -2147015407|Data sync request accepted|
> |DataTableNotAvailable|0x800609B0, -2147087952|The original data table has been deleted or renamed.|
> |DataTypeMismatchForLinkedAttribute|0x8004F0FC, -2147159812|Data type mismatch found for linked attribute.|
> |DataTypeNotFound|0x80090100, -2146893568|The data type with {0} = '{1}' cannot be found.|
> |DataTypeValidationError|0x80090106, -2146893562|The data type with Id = '{0}', Name = '{1}', and DisplayName = '{2}' has failed validation. Please review the following value '{3}' for parameter '{4}'.|
> |DateTimeFormatFailed|0x8004025a, -2147220902|Failed to produce a formatted datetime value.|
> |DBConnectionOrTransactionInitializationFailed|0x80048551, -2147187375|Initialization of the database connection or transaction failed. This operation should be retried later. Initialization exception message: {0}|
> |DBUpgradeCauseTimeout|0x80048553, -2147187373|The operation timed out because the database is currently being upgraded. Please try again after the database upgrade is complete.|
> |DecimalValueOutOfRange|0x80044330, -2147204304|A validation error occurred. A decimal value provided is outside of the allowed values for this attribute.|
> |DecoupleChildEntity|0x80048206, -2147188218|Cannot decouple a child entity.|
> |DecoupleUserOwnedEntity|0x80048207, -2147188217|Can only decouple user owned entities.|
> |DecreasingDaysWillDeleteOlderData|0x80060992, -2147087982|Decreasing the number of days will delete mobile offline data older than the number of days specified.|
> |DefaultSiteCollectionUrlChanged|0x8004F100, -2147159808|Default site collection url has been changed this organization after this operation was created.|
> |DefaultSiteMapDeleteFailure|0x80048070, -2147188624|Cannot delete default site map.|
> |DelegatedAdminUserCannotBeCreateNorUpdated|0x80041d67, -2147213977|The delegated admin user cannot be updated|
> |DeleteActiveWorkflowTemplateDependency|0x8004501A, -2147200998|Cannot delete workflow dependency from a published workflow template .|
> |DeletePublishedWorkflowDefinitionWorkflowDependency|0x80045006, -2147201018|Cannot delete a workflow dependency for a published workflow definition.|
> |DeleteWorkflowActivation|0x80045004, -2147201020|Cannot delete a workflow activation.|
> |DeleteWorkflowActivationWorkflowDependency|0x80045005, -2147201019|Cannot delete a workflow dependency associated with a workflow activation.|
> |DeleteWorkflowActiveDefinition|0x8004500F, -2147201009|Cannot delete an active workflow definition.|
> |DeleteWorkflowActiveTemplate|0x8004501C, -2147200996|Cannot delete an active workflow template.|
> |DelveActionHubAttributeMissingInResponseException|0x80071002, -2147020798|Attribute not present in exchange oData response.|
> |DelveActionHubAuthorizationFailureException|0x80071007, -2147020793|You don’t have the proper Office 365 license to view actions. Please contact your system administrator.|
> |DelveActionHubDisabledError|0x80071000, -2147020800|Delve action hub feature is not enabled.|
> |DelveActionHubInvalidResponseFormatException|0x80071004, -2147020796|Invalid response format.|
> |DelveActionHubInvalidStateCodeException|0x80071003, -2147020797|Invalid state code passed in expression.|
> |DelveActionHubResponseRetievalFailureException|0x80071005, -2147020795|Error while fetching actions from Exchange.|
> |DelveActionHubS2SSetupFailureException|0x80071008, -2147020792|Server to Server Authentication with Exchange for Delve Action Hub is not set up.|
> |DependencyAlreadyExists|0x8004F01A, -2147160038|A {0} dependency already exists between {1}({2}) and {3}({4}).  Cannot also create {5} dependency.|
> |DependencyTableNotEmpty|0x8004F01B, -2147160037|The dependency table must be empty for initialization to complete successfully.|
> |DependencyTrackingClosed|0x8004F025, -2147160027|Invalid attempt to process a dependency after the current transaction context has been closed.|
> |DeploymentServiceCannotChangeStateForDeploymentService|0x8004D262, -2147167646|You cannot change the state of this server because it contains the Deployment Service server role.|
> |DeploymentServiceCannotDeleteOperationInProgress|0x8004D265, -2147167643|The Deployment Service cannot delete the specified operation because it is currently in progress.|
> |DeploymentServiceNotAllowOperation|0x8004D261, -2147167647|Deployment Service for {0} does not allow {1} operation.|
> |DeploymentServiceNotAllowSetToThisState|0x8004D260, -2147167648|Deployment Service for {0} allows the state Enabled or Disabled. Cannot set state to {1}.|
> |DeploymentServiceOperationIdentifierNotFound|0x8004D264, -2147167644|The Deployment Service could not find a deferred operation having the specified identifier.|
> |DeploymentServiceRequestValidationFailure|0x8004D263, -2147167645|The Deployment Service cannot process the request because one or more validation checks failed.|
> |DeprecatedFormActivation|0x8004F662, -2147158430|This form has been deprecated in the previous release and cannot be used anymore. Please migrate your changes to a different form. Deprecated forms will be removed from the system in the future.|
> |DeprecatedMobileFormsCreation|0x8004F667, -2147158425|Mobile forms have been deprecated. Cannot create new mobile express forms.|
> |DeprecatedMobileFormsEdit|0x8004F668, -2147158424|Mobile forms have been deprecated. Cannot open mobile forms editor.|
> |DeprovisionRIAccessNotAllowed|0x80044274, -2147204492|Relationship Insights can only be turned off by a system administrator.|
> |DesignerAccessDenied|0x80050100, -2147155712|You do not have enough privileges to perform the requested operation. For more information, contact your administrator.|
> |DesignerInvalidParameter|0x80050101, -2147155711|The {0} provided is incorrect or missing. Please try again with the correct {1}.|
> |DestinationFolderNotExists|0x80071022, -2147020766|Unable to copy the documents. The destination document location no longer exists.|
> |DialogNameCannotBeNull|0x80060873, -2147088269|"DialogName cannot be null for type Dialog|
> |DisabledCRMAddinLoadFailure|0x80044202, -2147204606|An error occurred loading Microsoft Dynamics 365 functionality. Try restarting Outlook. Contact your system administrator if errors persist.|
> |DisabledCRMClientVersionHigher|0x80044204, -2147204604|The Microsoft Dynamics 365 server needs to be upgraded before Microsoft Dynamics 365 client can be used. Contact your system administrator for assistance.|
> |DisabledCRMClientVersionLower|0x80044203, -2147204605|You're running a version of Microsoft Dynamics 365 for Outlook that is not supported for offline mode with this Microsoft Dynamics 365 organization {0}. You'll need to upgrade to a compatible version of Dynamics 365 for Outlook. Make sure your current version of Dynamics 365 for Outlook is supported for upgrading to the compatible version.|
> |DisabledCRMGoingOffline|0x80044200, -2147204608|Microsoft Dynamics 365 functionality is not available while Offline Synchronization is occuring|
> |DisabledCRMGoingOnline|0x80044201, -2147204607|Microsoft Dynamics 365 functionality is not available while Online Synchronization is occuring|
> |DisabledCRMOnlineCrmNotAvailable|0x80044206, -2147204602|Microsoft Dynamics 365 server is not available|
> |DisabledCRMPostOfflineUpgrade|0x80044205, -2147204603|Microsoft Dynamics 365 functionality is not available until the Microsoft Dynamics 365 client is taken back online|
> |DisableRIFeatureNotAllowed|0x80044280, -2147204480|You need system administrator privileges to turn Relationship Insights off for your organization.|
> |DiscountAmount|0x80043b20, -2147206368|The discount type does not support 'percentage' discounts.|
> |DiscountAmountAndPercent|0x80043b1f, -2147206369|Both 'amount' and 'percentage' cannot be set.|
> |DiscountPercent|0x80043b21, -2147206367|The discount type does not support 'amount' discounts.|
> |DiscountRangeOverlap|0x80043b02, -2147206398|The new quantities overlap the range covered by existing quantities.|
> |DiscountTypeAndPriceLevelCurrencyNotEqual|0x80048cf8, -2147185416|The currency of the discount needs to match the currency of the price list for discount type amount.|
> |DiskSpaceNotEnough|0x80050124, -2147155676|There is not enough space in the Temp Folder.|
> |DistinctWithImageAttributeError|0x80072531, -2147015375|Distinct is not allowed when image attributes are selected.|
> |DistributeListAssociatedVary|0x80048453, -2147187629|This campaign activity cannot be distributed. Mail merge activities can be done only on marketing lists that are all the same record type. For this campaign activity, remove marketing lists so that the remaining ones are the same record type, and then try again.|
> |DistributeNoListAssociated|0x80048454, -2147187628|This campaign activity cannot be distributed. No marketing lists are associated with it. Add at least one marketing list and try again.|
> |DocumentManagementDisabled|0x8004F0FF, -2147159809|Document Management has been disabled for this organization.|
> |DocumentManagementDisabledForEmail|0x80050010, -2147155952|Document Management must be enabled on the Email entity in order to follow attachments. Please contact your administrator to enable Document Management.|
> |DocumentManagementDisabledOnEntity|0x80060908, -2147088120|You must enable document management for this Entity in order to enable OneNote integration.|
> |DocumentManagementIsDisabled|0x8004F312, -2147159278|Document Management is not enabled for this Organization.|
> |DocumentManagementIsDisabledOnEntity|0x80071011, -2147020783|You must enable document management for this Entity in order to enable Document Recommendations.|
> |DocumentManagementNotEnabledNoPrimaryField|0x8004F313, -2147159277|Document management could not be enabled because a primary field is not defined for this entity with name {0} and id {1}.|
> |DocumentRecommendationsFCBOff|0x80071019, -2147020775|The document suggestions feature is not enabled.|
> |DocumentTemplateFeatureNotEnabled|0x800608C9, -2147088183|Document template feature is not enabled.|
> |DocxExportGeneratingWordFailed|0x800608CD, -2147088179|An error occurred while generating the Word document. Please try again.|
> |DocxValidationFailed|0x800608CE, -2147088178|The upload failed because the selected file is not consistent with the template layout. Please try again after selecting a file with the template layout.|
> |DoNotTrackItem|0x80044228, -2147204568|Selected item will not be tracked.|
> |DownloadAllEntityRecordsChangedOrCreatedWithinTheseDays|0x8006098F, -2147087985|Download all entity records changed or created within this number of days.|
> |DownloadRelatedDataOnlyMustHaveRelationship|0x80071140, -2147020480|The entity '{0}' in profile '{1}' is configured with the filter download related data only, however there are no relationships specified for this entity in profile item associations. If an entity is set to download related data only you must specify a profile item association to this entity.|
> |DraftBundleToProduct|0x8004F994, -2147157612|You can only add products to a draft bundle.|
> |DSSThrottlingConcurrencyLimitExceededError|0x80072327, -2147015897|Too many concurrent requests detected.|
> |DuplicateAliasFound|0x8004E00B, -2147164149|Data Description is invalid. Duplicate alias found.|
> |DuplicateApplicationUser|0x8004F511, -2147158767|You are attempting to create an Application ID = {0} that already exists.|
> |DuplicateAppModuleUniqueName|0x8005011F, -2147155681|The name you entered is already in use.|
> |DuplicateAttributePhysicalName|0x80060304, -2147089660|Attribute {0} already exists for entity {1}.|
> |DuplicateAttributeSchemaName|0x80047013, -2147192813|{0}|
> |DuplicateChannelPropertyName|0x800608F1, -2147088143|A channel property with the specified name already exists. You can't create another one.|
> |DuplicateCheckNotEnabled|0x80048412, -2147187694|Duplicate detection is not enabled. To enable duplicate detection, click Settings, click Data Management, and then click Duplicate Detection Settings.|
> |DuplicateCheckNotSupportedOnEntity|0x80048410, -2147187696|Duplicate detection is not supported on this record type.|
> |DuplicateComponentInSolutionXml|0x80071153, -2147020461|Duplicate Component is present in the XML.|
> |DuplicateDatasetConfigurationFound|0x80160037, -2146041801|Dataset with name'{0}' has a duplicate configuration Dataset Configuration for reference: {1}. More Details:{2}|
> |DuplicateDetectionNotSupportedOnAttributeType|0x80048430, -2147187664|The rule condition cannot be created or updated because duplicate detection is not supported on the data type of the selected attribute.|
> |DuplicateDetectionRulesWereUnpublished|0x8004F039, -2147160007|The duplicate detection rules for this entity have been unpublished due to possible modifications to the entity.|
> |DuplicateDetectionTemplateNotFound|0x80048424, -2147187676|Microsoft Dynamics 365 could not retrieve the e-mail notification template.|
> |DuplicateDisplayCollectionName|0x80047012, -2147192814|An object with the specified display collection name already exists.|
> |DuplicateDisplayName|0x80047011, -2147192815|An object with the specified display name already exists.|
> |DuplicatedJobId|0x80071152, -2147020462|Parameter ImportJobId must be unique.|
> |DuplicatedJobIdDueToConcurrency|0x80071155, -2147020459|Cannot create the solution job using the supplied JobId ({0}) as it is already in use. This may indicate that another solution operation is progress. Please try again later.|
> |DuplicatedPrivilege|0x8004140f, -2147216369|Privilege {0} is duplicated.|
> |DuplicateFileNamesInZip|0x80048484, -2147187580|Two or more files have the same name. File names must be unique.|
> |DuplicateGroupByFound|0x8004E01B, -2147164133|Data Description is invalid. Same attribute cannot be used as a group by more than once.|
> |DuplicateHeaderColumn|0x80040338, -2147220680|A duplicate column heading exists.|
> |DuplicateIsoCurrencyCode|0x80048cf3, -2147185421|Cannot insert duplicate currency record. Currency with the same currency code already exist in the system.|
> |DuplicateLookupFound|0x80040352, -2147220654|A duplicate lookup reference was found|
> |DuplicateMapName|0x80048443, -2147187645|A data map with the specified name already exists.|
> |DuplicateName|0x80047010, -2147192816|An object with the specified name already exists|
> |DuplicateNonFormFactorControlNodes|0x80160020, -2146041824|There are duplicate custom control nodes found for control {0}. More Details:{1}|
> |DuplicateOfflineFilter|0x80048449, -2147187639|You can create only one local data group for each record type.|
> |DuplicateOutlookAppointment|0x80040274, -2147220876|The Appointment being promoted from Outlook is already tracked in Dynamics 365|
> |DuplicateParameterIsFoundOnDefaultDeclaration|0x80160034, -2146041804|Property:{0} is declared more than once on default declaration. More Details:{1}|
> |DuplicateParameterIsFoundOnFormFactor|0x80160033, -2146041805|Property:{0} is declared more than once on form factor '{1}'. More Details:{2}|
> |DuplicatePrimaryNameAttribute|0x8004701E, -2147192802|The new {2} attribute is set as the primary name attribute for the {1} entity. The {1} entity already has the {0} attribute set as the primary name attribute. An entity can only have one primary name attribute.|
> |DuplicatePrivilegeInRolecontrol|0x80061118, -2147086056|The Channel Access Profile privilege array contains duplicate privilege references.|
> |DuplicateProductPriceLevel|0x80043b08, -2147206392|This product and unit combination has a price for this price list.|
> |DuplicateProductRelationship|0x8004F891, -2147157871|A product relationship with the same product and related product already exists.|
> |DuplicateRecord|0x80040237, -2147220937|Operation failed due to a SQL integrity violation.|
> |DuplicateRecordEntityKey|0x80060892, -2147088238|Entity Key {0} violated. A record with the same value for {1} already exists. A duplicate record cannot be created. Select one or more unique values and try again.|
> |DuplicateRecordsFound|0x80040333, -2147220685|A record was not created or updated because a duplicate of the current record already exists.|
> |DuplicateReportVisibility|0x80040495, -2147220331|A ReportVisibility with the same ReportId and VisibilityCode already exists. Duplicates are not allowed.|
> |DuplicateSalesTeamMember|0x80048341, -2147187903|The user you're trying to add is already a member of the sales team.|
> |DuplicateUIStatementRootsFound|0x8004F201, -2147159551|There can be only one root statement for a given uiscript.|
> |DynamicPropertyDefaultValueNeeded|0x80061038, -2147086280|You must specify a default value because this property is required and is read-only.|
> |DynamicPropertyInstanceMissingRequiredColumns|0x8008100A, -2146955254|The property instance can't be updated. Verify that the following fields are present: dynamicpropertyid, dynamicpropertyoptionsetvalueid, and regardingobjectid.|
> |DynamicPropertyInstanceUpdateValuesDifferentRegarding|0x8008100B, -2146955253|The property instances couldn't be saved because they refer to different product line items.|
> |DynamicPropertyInvalidRegardingForUpdate|0x80081004, -2146955260|You can’t create or change properties for a published or retired product.|
> |DynamicPropertyInvalidStateChange|0x80081001, -2146955263|You can't set an inactive property to an active state.|
> |DynamicPropertyInvalidStateForDelete|0x80081002, -2146955262|You can't delete a property that is in the active state.|
> |DynamicPropertyInvalidStateForUpdate|0x80081000, -2146955264|You can't update a property that isn't in the draft state.|
> |DynamicPropertyOptionSetInvalidStateForUpdate|0x8008100C, -2146955252|You can't modify the property option set item for a property that is not in the draft state.|
> |EditorOnlySupportAndOperatorForLogicalConditions|0x80060005, -2147090427|The rule expression contains logical operator which is not supported. The editor only support And operator for Logical conditions.|
> |EditQueryInDynamicExcelNotSupported|0x800609B8, -2147087944|You can’t edit the query on a dynamic spreadsheet once the Excel file has been exported. If you’d like to make changes, go back to Dynamics 365 and then re-export.|
> |EESiteDBFetchFailure|0x80050025, -2147155931|Unable to fetch data from site DB.|
> |EmailAlreadyExistsInDestinationQueue|0x80040523, -2147220189|You cannot add this e-mail to the selected queue. A queue item for this e-mail already exists in the queue. You can delete the item from the queue, and then try again.|
> |EmailDoesNotExist|0x80050007, -2147155961|Email does not exist for given attachment.|
> |EmailEngagementFeatureDisabled|0x80050003, -2147155965|Please enable Email Engagement feature for current org to follow or unfollow email attachment.|
> |EmailEngagementFeatureDisabledForAttachmentTracking|0x80050015, -2147155947|Please enable Email Engagement feature for this organization to follow email attachments.|
> |EmailInteractionsFetchFailure|0x80050022, -2147155934|Unable to fetch email interactions.|
> |EmailMessageSizeExceeded|0x8005E237, -2147098057|Email Size Exceeds the MaximumMessageSizeLimit specified by the deployment.|
> |EmailMonitoringDeProvisionFailed|0x80050014, -2147155948|Email engagement feature deprovisioning failed|
> |EmailMonitoringNotProvisioned|0x80050011, -2147155951|RI provisioning service failed.|
> |EmailMonitoringProvisionFailed|0x80050012, -2147155950|Email engagement feature provisioning failed|
> |EmailNotFollowed|0x80050008, -2147155960|This attachment cannot be followed as its corresponding email is not followed.|
> |EmailOpenActionCardCreationFailure|0x80050024, -2147155932|We can’t create email open action card.|
> |EmailRecipientNotSpecified|0x80040b04, -2147218684|The e-mail must have at least one recipient before it can be sent|
> |EmailReminderActionCardCreationFailure|0x80050023, -2147155933|We can’t create email reminder action card.|
> |EmailRouterFileTooLargeToProcess|0x8005F031, -2147094479|One or more of the email router configuration files is too large to get processed.|
> |EmailServerProfileADBasedAuthenticationProtocolNotAllowed|0x8005E23C, -2147098052|The authentication protocol cannot be set to Negotiate or NTLM for your organization because these require Active Directory. Use a different authentication protocol or contact your system administrator to enable an Active Directory-based authentication protocol.|
> |EmailServerProfileAutoDiscoverNotAllowed|0x8005E204, -2147098108|Auto discover server URL can location can only be used for an exchange e-mail server type.|
> |EmailServerProfileBasicAuthenticationProtocolNotAllowed|0x8005E23D, -2147098051|The specified authentication protocol cannot be used because the protocol requires sending credentials on a secure channel. Use a different authentication protocol or contact your administrator to enable Basic authentication protocol on a non-secure channel.|
> |EmailServerProfileDelegateAccessNotAllowed|0x8005E235, -2147098059|For an SMTP email server type, auto-granted delegate access cannot be used.|
> |EmailServerProfileImpersonationNotAllowed|0x8005E236, -2147098058|For a Non Exchange email server type, impersonation cannot be used.|
> |EmailServerProfileInvalidAuthenticationProtocol|0x8005E23B, -2147098053|The authentication protocol is invalid for the specified server and connection type. For more information, contact your system administrator.|
> |EmailServerProfileInvalidCredentialRetrievalForExchange|0x8005E203, -2147098109|No credentials (Anonymous) cannot be used a connection type for exchange e-mail server type.|
> |EmailServerProfileInvalidCredentialRetrievalForOnline|0x8005E202, -2147098110|Windows integrated or Anonymous authentication cannot be used as a connection type for Microsoft Dynamics 365 Online.|
> |EmailServerProfileInvalidServerLocation|0x8005E20A, -2147098102|The specified server location {0} is invalid. Correct the server location and try again.|
> |EmailServerProfileLocationNotRequired|0x8005E205, -2147098107|You cannot specify the incoming/outgoing e-mail server location when Autodiscover server location has been set to true.|
> |EmailServerProfileNotAssociated|0x8005E222, -2147098078|Email Server Profile is not associated with the current mailbox. Please associate a valid profile to send/receive mails.|
> |EmailServerProfileSslRequiredForOnline|0x8005E201, -2147098111|You cannot set SSL as false for Microsoft Dynamics 365 Online.|
> |EmailServerProfileSslRequiredForOnPremise|0x8005E234, -2147098060|Usage of SSL while contacting external email servers is mandatory for this Dynamics 365 deployment.|
> |EmptyCommandOrEntity|0x80154B51, -2146088111|Command or entity name cannot be empty.|
> |EmptyContent|0x80040365, -2147220635|The file is empty.|
> |EmptyEntityFilterXml|0x80071118, -2147020520|The FetchXML is missing.|
> |EmptyFileForImport|0x80048487, -2147187577|The selected file contains no data.|
> |EmptyFilesInZip|0x80048486, -2147187578|One or more files in the compressed (.zip) or .cab file don't contain data. Check the files and try again.|
> |EmptyHeaderColumn|0x80040337, -2147220681|The column heading cannot be empty.|
> |EmptyHeaderRow|0x80040366, -2147220634|The first row of the file is empty.|
> |EmptyImportFileRow|0x80040347, -2147220665|Empty row.|
> |EmptyRecord|0x80040373, -2147220621|The record is empty|
> |EmptySecretInDataSource|0x80044818, -2147203048|Data Source secrets are not included in solutions. You'll need to edit your data sources to add secrets back following solution import.|
> |EmptySiteMapXml|0x8004F402, -2147159038|Sitemap xml is empty.|
> |EmptyXml|0x80040202, -2147220990|Empty XML.|
> |EnableMobileOfflineDisableChangeTrackingError|0x800609A2, -2147087966|You must enable change tracking for this entity since mobile offline client is enabled.|
> |EnableRIFeatureNotAllowed|0x80044279, -2147204487|You need system administrator privileges to update Relationship Insights tenant information.|
> |EndUserNotificationTypeNotValidForEmail|0x8004D291, -2147167599|Cannot send Email for EndUserNotification Type: {0}.|
> |EntitiesExceedMaxAllowed|0x80060415, -2147089387|You can't cover more than five entities in a process flow. Remove some entities and try again.|
> |EntitiesInViewNotAvailableOffline|0x80071125, -2147020507|One or more entities referenced are not available offline.|
> |EntitiesInViewNotInProfile|0x80071124, -2147020508|One or more entities in this view are not part of this profile.|
> |EntitlementAlreadyInactiveState|0x80060615, -2147088875|You can't activate an entitlement when it's in the active state.|
> |EntitlementAlreadyInCanceledState|0x80044208, -2147204600|You can't cancel an entitlement when it's in the Canceled state.|
> |EntitlementAlreadyInDraftState|0x80060614, -2147088876|You can't deactivate an entitlement when it's in the draft state.|
> |EntitlementBlankTerms|0x80060622, -2147088862|Total terms can't be blank. Enter a value and try again.|
> |EntitlementChannelInvalidState|0x80060603, -2147088893|An entitlement channel term cannot be created, modified or deleted when the associated entitlement is not in draft state.|
> |EntitlementChannelWithoutEntitlementId|0x80060612, -2147088878|Associate the entitlement channel with an entitlement or entitlement template.|
> |EntitlementEditDraft|0x80060613, -2147088877|You can only edit a draft entitlement.|
> |EntitlementInvalidRemainingTerms|0x80060624, -2147088860|The number of remaining terms can't be greater than the number of total terms.|
> |EntitlementInvalidStartEndDate|0x80060600, -2147088896|Start Date cannot be more than the End Date|
> |EntitlementInvalidState|0x80060601, -2147088895|You cannot delete an entitlement that is in active or waiting state|
> |EntitlementInvalidTerms|0x80060604, -2147088892|Specify a higher value for total terms so the remaining terms won't be a negative value.|
> |EntitlementNotActiveInAssociationToCase|0x80060616, -2147088874|You can't create a case for this entitlement because the entitlement is not in active state.|
> |EntitlementTemplateTotalTerms|0x80060620, -2147088864|If the allocation type is the number of cases, the total terms can't be a decimal value. Specify a whole number.|
> |EntitlementTotalTerms|0x80060619, -2147088871|If the allocation type is the number of cases, the total terms can't be a decimal value. Specify a whole number.|
> |EntityCannotBeChildInCustomRelationship|0x8004432D, -2147204307|This entity is either not valid as a child in a custom parental relationship or is already a child in a parental relationship|
> |EntityCannotHaveOwnedByMeFilter|0x80071136, -2147020490|The entity '{0}' in the profile '{1}' has OwnedByMe set to true. This property is not a valid property for the '{0}' entity.|
> |EntityCannotHaveOwnedByMyTeamFilter|0x80071137, -2147020489|The entity '{0}' in the profile '{1}' has OwnedByMyTeam set to true. This property is not a valid property for the '{0}' entity.|
> |EntityCannotParticipateInEntityAssociation|0x80044332, -2147204302|This entity cannot participate in an entity association|
> |EntityCannotParticipateInEntityAssociationTaskOrPhonecall|0x80044368, -2147204248|Entity {0} cannot be in an entity association with entity {1}. It should be between {1} and knowledgebaserecord.|
> |EntityCanOnlyBeReferencedOnceInPolymorphicLookup|0x80090424, -2146892764|The entity '{0}' cannot be referenced more than once in a polymorphic lookup. Referencing entity '{1}', attribute '{2}'.|
> |EntityCustomizationLockException|0x80090412, -2146892782|"Cannot start the requested operation because there is an entity customization running at this moment."|
> |EntityDupCheckNotSupportedSystemWide|0x80048431, -2147187663|Duplicate detection is not enabled for one or more of the selected entities. The duplicate detection job cannot be started.|
> |EntityExceedsMaxActiveBusinessProcessFlows|0x80060420, -2147089376|The {0} entity exceeds the maximum number of active business process flows. The limit is {1}.|
> |EntityFilterContainerMustNotBeNullFormatString|0x80071132, -2147020494|There are no filters specified for the entity '{0}'. You must define at least one filter.|
> |EntityGroupNameOrEntityNamesMustBeProvided|0x80060205, -2147089915|Missing parameter. You must provide EntityGroupName or EntityNames.|
> |EntityHasNoStateCode|0x80047015, -2147192811|Specified entity does not have a statecode.|
> |EntityInstanceIsNull|0x80060444, -2147089340|Error creating or updating Business Process: entity instance cannot be null.|
> |EntityInstantiationFailed|0x80040243, -2147220925|Instantiation of an Entity instance Service failed.|
> |EntityIsIntersect|0x8004830F, -2147187953|The specified entity is intersect entity|
> |EntityIsLocked|0x80043b1d, -2147206371|This entity is already locked.|
> |EntityIsNotBusinessProcessFlowEnabled|0x80060421, -2147089375|The IsBusinessProcessEnabled property of the {0} entity is false.|
> |EntityIsNotCustomizable|0x80047008, -2147192824|The specified entity is not customizable|
> |EntityIsNotEnabledForExternalParty|0x8006111B, -2147086053|You can't create/update an external party item associated to an entity that is not enabled for external party.|
> |EntityIsNotEnabledForFollow|0x8004F6A2, -2147158366|This entity is not enabled to be followed. |
> |EntityIsNotEnabledForFollowUser|0x8004F6A1, -2147158367|This entity is not enabled to be followed. |
> |EntityIsUnlocked|0x80043b1e, -2147206370|This entity is already unlocked.|
> |EntityKeyAttributeNotValidForCreate|0x80090110, -2146893552|Attribute of an entity key must be valid for create. Atribute Name = '{0}' Id = '{1}'|
> |EntityKeyAttributeNotValidForCreateAndUpdate|0x80090112, -2146893550|Attribute of an entity key must be valid for create and update. Atribute Name = '{0}' Id = '{1}'|
> |EntityKeyAttributeNotValidForUpdate|0x80090111, -2146893551|Attribute of an entity key must be valid for update. Atribute Name = '{0}' Id = '{1}'|
> |EntityKeyNameExists|0x80060893, -2147088237|An entity key with the name {0} already exists on entity {1}.|
> |EntityKeyNotDefined|0x80060890, -2147088240|The specified key attributes are not a defined key for the {0} entity|
> |EntityKeyNotSupportedForSolutionAwareComponents|0x8006089F, -2147088225|Entity keys are not supported for entity {0} because the entity is a solution aware component|
> |EntityKeyWithSelectedAttributesExists|0x80060894, -2147088236|An entity key with the selected attributes already exists on entity.|
> |EntityLimitExceeded|0x80060200, -2147089920|MultiEntitySearch exceeded Entity Limit defined for the Organization.|
> |EntityLoopBeingCreated|0x80040387, -2147220601|Creating this parental association would create a loop in this entity hierarchy.|
> |EntityLoopExists|0x80040386, -2147220602|Loop exists in this entity hierarchy.|
> |EntityMetadataSyncFailed|0x8005F238, -2147093960|There were problems with the server configurations.  There was a problem with the server configuration changes.  We are unable to load the application, please contact your Dynamics 365 administrator.|
> |EntityMetadataSyncFailedWithContinue|0x8005F239, -2147093959|There were difficulties with the server configuration changes.  You can continue to use the app with the older configuration, however, you may experience problems including errors when saving.  Please contact your Dynamics 365 administrator. |
> |EntityNotEnabledForAutoCreatedAccessTeams|0x80048334, -2147187916|This entity is not enabled for auto created access teams.|
> |EntityNotEnabledForCharts|0x8004E00C, -2147164148|Charts are not enabled on the specified primary entity type code: {0}.|
> |EntityNotEnabledForThisDevice|0x8005F200, -2147094016|Entity not enabled to be viewed in this device|
> |EntityNotRule|0x8004E112, -2147163886|The collection name is not a recurrence rule.|
> |EntityProperyProcessingNotSupported|0x80090400, -2146892800|Entity {0} cannot be processed because it includes property {1} which has a dependency on an unsupported entity {2} in your organization.|
> |EntityReferenceArgumentsNotBound|0x80060395, -2147089515|Required arguments of type EntityReference must be bound to some entity.|
> |EntityReferenceLinkNull|0x80048466, -2147187610|EntityRefererence link cannot be null|
> |EntityRelationshipRoleCustomLabelsMissing|0x80044328, -2147204312|Custom labels must be provided if an entity relationship role has a display option of UseCustomLabels|
> |EntityRelationshipSchemaNameNotUnique|0x8004432B, -2147204309|A relationship with the specified name already exists. Please specify a unique name.|
> |EntityRelationshipSchemaNameRequired|0x8004432A, -2147204310|Entity relationships require a name|
> |EntityTypeNotSupported|0x80100008, -2146435064|{0} entity does not support this message.|
> |EntityTypeSpecifiedForDashboard|0x8004E30B, -2147163381|An entity type cannot be specified for a dashboard.|
> |ERMissingReferencingEntityNode|0x80090416, -2146892778|Unable to process EntityRelationship {0} because it does not contain ReferencingEntity node.|
> |ErrorConnectingToDiscoveryService|0x8004B066, -2147176346|Error when trying to connect to customer's discovery service.|
> |ErrorConnectingToOrganizationService|0x8004B068, -2147176344|Error when trying to connect to customer's organization service.|
> |ErrorDeleteStatementTextIsReferenced|0x8004F203, -2147159549|You cannot delete the UI script statement text because it is being referred by one or more ui script statements.|
> |ErrorFetchingBaseUrl|0x80044290, -2147204464|We can't fetch base URL for organization Id {0}. Exception details {1}|
> |ErrorFetchingRIProvisionStatus|0x80044291, -2147204463|We can't fetch RI provisioning status for organization Id {0}. Exception details {1}|
> |ErrorGeneratingActionHub|0x80071001, -2147020799|An error has occurred. Please try again later.|
> |ErrorGeneratingInvitation|0x8004B013, -2147176429|Some Internal error occurred in generating invitation token, Please try again later|
> |ErrorImportInvalidForPublishedScript|0x8004F216, -2147159530|You cannot save data to a published UI script. Unpublish the UI script, and try again.|
> |ErrorIncreate|0x80040359, -2147220647|The Microsoft Dynamics 365 record could not be created|
> |ErrorInDelete|0x8004035a, -2147220646|The Microsoft Dynamics 365 record could not be deleted|
> |ErrorInFetchingEmailEngagementProvisioningStatus|0x80050013, -2147155949|Error in fetching email engagement feature provisioning status.|
> |ErrorInFieldWidthIncrease|0x80044351, -2147204271|An error occurred while increasing the field width.|
> |ErrorInImportConfig|0x80040323, -2147220701|Cannot process with Bulk Import as Import Configuration has some errors.|
> |ErrorInParseRow|0x80040346, -2147220666|The row could not be parsed. This is typically caused by a row that is too long.|
> |ErrorInSetState|0x80040357, -2147220649|The status or status reason of the Microsoft Dynamics 365 record could not be set|
> |ErrorInStoringImportFile|0x80048497, -2147187561|An error occurred while storing the import file in database.|
> |ErrorInUnzip|0x80048483, -2147187581|An error occurred while extracting the uploaded compressed (.zip) or .cab file. Make sure that the file isn't password protected, and try uploading the file again. If this problem persists, contact your system administrator.|
> |ErrorInUnzipAlternate|0x80048503, -2147187453|An error occurred while the uploaded compressed (.zip) file was being extracted. Try to upload the file again. If the problem persists, contact your system administrator.|
> |ErrorInUpdate|0x80040358, -2147220648|The Microsoft Dynamics 365 record could not be updated|
> |ErrorInvalidFileNameChars|0x8004F214, -2147159532|The Microsoft Excel file name cannot contain the following characters: *  \ : > < | ? " /. Rename the file using valid characters, and try again.|
> |ErrorInvalidUIScriptImportFile|0x8004F211, -2147159535|File type is not supported. Select an xml file for import.|
> |ErrorMigrationProcessExcessOnServer|0x8005F034, -2147094476|The server is busy handling other migration processes. Please try after some time.|
> |ErrorMimeTypeNullOrEmpty|0x8004F215, -2147159531|The MimeType property value of the UploadFromBase64DataUIScriptRequest method is null or empty. Specify a valid property value, and try again.|
> |ErrorNoActiveRoutingRuleExists|0x8004F874, -2147157900|Currently there's no active rule to route this case.|
> |ErrorNoQueryData|0x8004F220, -2147159520|An error has occurred. Either the data does not exist or you do not have sufficient privileges to view the data. Contact your system administrator for help.|
> |ErrorOnFeatureStatusChange|0x80044289, -2147204471|We can’t enable/disable the {0} feature for organization Id {1}. Exception details {2}.|
> |ErrorOnGetRecord|0x80044286, -2147204474|There was an error fetching a record for table {0}. Exception details {1}.|
> |ErrorOnGetRIProvisionStatus|0x80044282, -2147204478|We can’t get the Relationship Insights provisioning status for organization ID {0}. Exception details {1}.|
> |ErrorOnGetRITenantEndPoint|0x80044283, -2147204477|We can’t get the Relationship Insights tenant endpoint information for organization ID {0}. Exception details {1}.|
> |ErrorOnQryPropertyBagCollection|0x80044287, -2147204473|The query didn’t return all {0} columns.|
> |ErrorOnStartOfRIProvision|0x80044284, -2147204476|We can’t start provisioning for organization ID {0}. Exception details {1}.|
> |ErrorOnTenantVerifyUpdate|0x80044285, -2147204475|We can’t verify or update tenant information for organization ID {0}. Exception details {1}.|
> |ErrorPropertyBagCollectionMissedColumn|0x80044288, -2147204472|{0} column for table {1} is missing.|
> |ErrorReactivatingComponentInstance|0x8004F004, -2147160060|After undeleting a label, there is no underlying label to reactivate.|
> |ErrorScriptCannotDeletePublishedScript|0x8004F209, -2147159543|You cannot delete a UI script that is published. You must unpublish it first.|
> |ErrorScriptCannotUpdatePublishedScript|0x8004F213, -2147159533|You cannot update a UI script that is published. You must unpublish it first.|
> |ErrorScriptFileParse|0x8004F212, -2147159534|Error occurred while parsing the XML file.|
> |ErrorScriptInitialStatementNotInScript|0x8004F207, -2147159545|The initial statement for this script does not belong to this script.|
> |ErrorScriptInitialStatementNotRoot|0x8004F208, -2147159544|The initial statement should the root statement and cannot have a previous statement set.|
> |ErrorScriptLanguageNotInstalled|0x8004F206, -2147159546|The language specified is not supported in your Dynamics 365 install. Please check with your system administrator on the list of "enabled" languages.|
> |ErrorScriptPublishMalformedScript|0x8004F20B, -2147159541|The selected UI script cannot be published. The UI script contains one or more paths which do not end in an end-script or next-script action node. Correct the paths and try to publish again.|
> |ErrorScriptPublishMissingInitialStatement|0x8004F20A, -2147159542|The selected UI script cannot be published. Provide a value for "First statement number" and try to publish again.|
> |ErrorScriptSessionCannotCreateForDraftScript|0x8004F204, -2147159548|You cannot create a UI script session for a UI script which is not published.|
> |ErrorScriptSessionCannotSetStateForDraftScript|0x8004F20D, -2147159539|You cannot set the state of a UI script session for a UI script which is not published.|
> |ErrorScriptSessionCannotUpdateForDraftScript|0x8004F205, -2147159547|You cannot update a UI script session for a UI script which is not published.|
> |ErrorScriptStatementResponseTypeOnlyForPrompt|0x8004F20E, -2147159538|You cannot associate the response control type for a statement which is not a prompt.|
> |ErrorScriptUnpublishActiveScript|0x8004F20C, -2147159540|This script is in use and has active sessions (status-reason=incomplete). Please terminate the active sessions (i.e. status-reason=cancelled) and try to unpublish again.|
> |ErrorsInEmailRouterMigrationFiles|0x8005F032, -2147094478|Invalid File(s) for Email Router Migration|
> |ErrorsInImportFiles|0x8004034a, -2147220662|Invalid File(s) for Import|
> |ErrorsInProfileRuleWorkflowActivation|0x80061119, -2147086055|You can't activate this profile rule. You don't have the required permissions on the record types that are referenced by this profile rule.|
> |ErrorsInSlaWorkflowActivation|0x80048535, -2147187403|You can't activate this service level agreement (SLA). You don't have the required permissions on the record types that are referenced by this SLA.|
> |ErrorsInWorkflowDefinition|0x80048455, -2147187627|The selected workflow has errors and cannot be published. Please open the workflow, remove the errors and try again.|
> |ErrorStatementDeleteOnlyForDraftScript|0x8004F210, -2147159536|You cannot delete a UI script statement for a UI script which is not draft.|
> |ErrorStatementOnlyForDraftScript|0x8004F20F, -2147159537|You cannot create a UI script statement for a UI script which is not draft.|
> |ErrorTemplate|0x80050102, -2147155710|{0}|
> |ErrorUIScriptPromptMissing|0x8004F221, -2147159519|The dialog that is being activated has no prompt/response.|
> |ErrorUpdateStatementTextIsReferenced|0x8004F202, -2147159550|You cannot update this UI script statement text because it is being referred to by one or more published ui scripts.|
> |ErrorUploadingReport|0x80048298, -2147188072|An error occurred while trying to add the report to Microsoft Dynamics 365. Try adding the report again. If this problem persists, contact your system administrator.|
> |EventNotSupportedForBusinessRule|0x80060001, -2147090431|Event {0} is not supported for client side business rule.|
> |EventTypeAndControlNameAreMismatched|0x80060003, -2147090429|This combination of event type and control name is unexpected|
> |EveryEntityKeyAttributesMustBeMapped|0x80090403, -2146892797|Every attribute of entitykey '{0}' of referenced entity '{1}' must be mapped to an attribute of the same type on the referencing entity '{2}' of relationship '{3}'.|
> |EvoStsAuthorizationServerRecordCreationFailureException|0x80071006, -2147020794|Database operation failed while creating authorization record for Evo STS.|
> |ExceedCustomEntityQuota|0x8004b042, -2147176382|The custom entity limit has been reached.|
> |ExceededLimitForAllowedFacetableAttributes|0x80060306, -2147089658|Cannot set user search facets for entity {0} as the limit for allowed facetable attributes is 4. Kindly remove few attributes to proceed.|
> |ExceededNumberOfRecordsCanFollow|0x8004F6A0, -2147158368|You have exceeded the number of records you can follow. Please unfollow some records to start following again.|
> |ExceededRollupFieldsPerEntityQuota|0x80060543, -2147089085|You can't add a rollup field with name {4} having id {3} for entity with name {2} and id {1}. You’ve reached the maximum number of {0} allowed for this record type.|
> |ExceededRollupFieldsPerOrgQuota|0x80060542, -2147089086|You can't add a rollup field. You’ve reached the maximum number of {0} allowed for your organization.|
> |ExcelFileNotFound|0x80060805, -2147088379|The requested file was not found.|
> |ExcelOnlineNotUpdated|0x80060808, -2147088376|Excel Online file {0} was not updated by the Wopi Server within the timeout specified.|
> |ExchangeAutodiscoverError|0x8004503A, -2147200966|Autodiscover could not find the Exchange Web Services URL for the specified mailbox. Verify that the mailbox address and the credentials provided are correct and that Autodiscover is enabled and has been configured correctly.|
> |ExchangeCardAttributeMissingInResponseException|0x80071102, -2147020542|Attribute not present in exchange oData response.|
> |ExchangeCardInvalidResponseFormatException|0x80071104, -2147020540|Invalid response format.|
> |ExchangeCardS2SSetupFailureException|0x80071105, -2147020539|Server to Server Authentication with Exchange for Action Card is not set up.|
> |ExchangeOptinNotEnabled|0x80071106, -2147020538|Exchange optin is not enabled.|
> |ExchangeRateOfBaseCurrencyNotUpdatable|0x80048cf5, -2147185419|The exchange rate of the base currency cannot be modified.|
> |ExecuteNotOnDemandWorkflow|0x80045046, -2147200954|Workflow must be marked as on-demand or child workflow.|
> |ExecuteUnpublishedWorkflow|0x80045047, -2147200953|Workflow must be in Published state.|
> |ExistingExternalReport|0x80040488, -2147220344|The report could not be published for external use because a report of the same name already exists. Delete that report in SQL Server Reporting Services or rename this report, and try again.|
> |ExistingParentalRelationship|0x80048205, -2147188219|A parental relationship already exists.|
> |ExpansionRequestIsOutsideExpansionWindow|0x8004E10C, -2147163892|The series is already expanded for CutOffWindow.|
> |ExpectingAtLeastOneBusinessRuleStep|0x80060011, -2147090415|There should be a minimum of one Business rule step.|
> |ExpiredAuthTicket|0x8004A101, -2147180287|The ticket specified for authentication is expired|
> |ExpiredEntitlementActivate|0x80060617, -2147088873|You can't activate an expired entitlement.|
> |ExpiredKey|0x8004A106, -2147180282|The key specified to compute a hash value is expired, only active keys are valid.  Expired Key : {0}.|
> |ExpiredOAuthToken|0x80041d52, -2147213998|The OAuth token has expired|
> |ExpiredVersionStamp|0x80044352, -2147204270|Version stamp associated with the client has expired. Please perform a full sync.|
> |ExportAttributeMapException|0x80044415, -2147204075|Failed to export AttributeMap from attribute {0} to {1} in EntityMap from entity {2} to {3} during solution export. AttributeMapId = {4}, EntityMapId = {5}|
> |ExportDefaultAsPackagedError|0x80048048, -2147188664|The default solution cannot be exported as a package.|
> |ExportDefaultSolutionError|0x80071158, -2147020456|Exporting the default solution is not supported. To export components, add them to a custom solution.|
> |ExportEntityMapException|0x80044416, -2147204074|Failed to export EntityMap from entity {0} to {1} during solution export. EntityMapId = {2}|
> |ExportKeyAttributeInvalidExceedsDepth|0x80072011, -2147016687|Export key attribute {0} for component {1} is invalid. Attributes defined for export EntityKey must not exceed lookup depth of 3|
> |ExportKeyAttributeInvalidLocalizable|0x80072010, -2147016688|Export key attribute {0} for component {1} is invalid. Attributes defined for export EntityKey must not be localizable|
> |ExportKeyAttributeInvalidNotInvalidForUpdate|0x8007200F, -2147016689|Export key attribute {0} for component {1} is invalid. Attributes defined for export EntityKey must be invalid for update|
> |ExportKeyAttributeInvalidNotSystemRequired|0x800608AF, -2147088209|Export key attribute {0} for component {1} is invalid. Attributes defined for export EntityKey must be system required|
> |ExportKeyAttributeInvalidPrefix|0x800608AD, -2147088211|Export key attribute {0} for component {1} must start with a valid customization prefix.|
> |ExportKeyAttributeInvalidPrimaryKey|0x800608AE, -2147088210|Export key attribute {0} for component {1} is invalid. Attributes defined for export EntityKey must not be the primary key|
> |ExportKeyAttributeInvalidReferencesNonSolutionAware|0x80072012, -2147016686|Export key attribute {0} for component {1} is invalid. Attributes defined for export EntityKey must not have a lookup to non-solution aware components|
> |ExportKeyAttributeNotBeginWithLetterOrNonAlphaNumericCharacters|0x800608AB, -2147088213|Export key attribute {0} for component {1} must begin with a letter and only consist of alpha-numeric and _.{}! characters.|
> |ExportKeyAttributeValuesIncorrectNumber|0x800608AC, -2147088212|Incorrect number of export key attribute values for export key {0} for entity {1}.|
> |ExportKeyInvalidCreate|0x80072013, -2147016685|It is invalid to create component {0} with the same export key value(s) as an existing component. Please change the key. The current value(s) are {1}|
> |ExportKeyNotSupported|0x800608A8, -2147088216|Export keys are not supported for entity {0} because export keys are unsupported|
> |ExportKeyNotSupportedForMaxAttributes|0x800608AA, -2147088214|Export key cannot be created for entity {0} because the key exceeds {1} attributes|
> |ExportKeyNotSupportedForNonCustomizableComponents|0x800608A7, -2147088217|Export keys are not supported for entity {0} because the entity is not customizable|
> |ExportKeyNotSupportedForNonSolutionAwareComponents|0x800608A6, -2147088218|Export keys are not supported for entity {0} because the entity is not a solution aware component|
> |ExportManagedSolutionError|0x80048036, -2147188682|An error occurred while exporting a solution. Managed solutions cannot be exported.|
> |ExportMissingSolutionError|0x80048037, -2147188681|An error occurred while exporting a solution. The solution does not exist in this system.|
> |ExportSolutionError|0x80048035, -2147188683|An error occurred while exporting a Solution.|
> |ExportToExcelOnlineFeatureNotEnabled|0x80060804, -2147088380|Export to Excel Online feature is not enabled.|
> |ExportToXlsxFeatureNotEnabled|0x800608C1, -2147088191|Export to excel file feature is not enabled.|
> |ExpressionNotSupportedForEditor|0x80060004, -2147090428|Rule contain an expression that is not supported by the editor.|
> |ExternalNameExists|0x80046F8F, -2147192945|An entity with the specified name already exists for data source - {0}. Please specify a new external name.|
> |ExternalSearchAttributeLimitExceeded|0x80060300, -2147089664|The maximum number of indexed fields has been reached. Update the Relevance Search configuration to reduce the total number of indexed fields {1} below {0}.|
> |ExtraPartyInformation|0x80040316, -2147220714|Extra party information should not be provided for this operation.|
> |FailedToAddSLADependency|0x80055007, -2147135481|Failed to add SLA dependency on ApplicableFrom attribute because attribute is not found in applicable entity metadata. Please contact your system administrator.|
> |FailedToAquireLock|0x80048411, -2147187695|PluginSqlLockManager failed to acquire lock|
> |FailedToDeserializeAsyncOperationData|0x80044304, -2147204348|Failed to deserialize async operation data.|
> |FailedToFindDependentConnectorsForModernFlow|0x80060475, -2147089291|Failed to find any of dependent custom connectors of current Modern Flow.|
> |FailedToGetNetworkServiceName|0x80047103, -2147192573|Failed to obtain the localized name for NetworkService account|
> |FailedToGetSlaPauseStates|0x80055012, -2147135470|Pause states do not exist in XML format in the DB. Try again or reach out to Dynamics 365 customer support.|
> |FailedToLoadAssembly|0x8004024e, -2147220914|Failed to load assembly|
> |FailedToRetrieveEntityCount|0x80055009, -2147135479|Failed to retrieve Entity Count with Active SLA. Please contact your system administrator.|
> |FailedToRetrieveSLAkpiCount|0x80055008, -2147135480|Failed to retrieve SLA KPI Count. Try again or reach out to Dynamics 365 customer support.|
> |FailedToScheduleActivity|0x80047000, -2147192832|Failed to schedule activity.|
> |FailToDeleteConnectorFromExternalPartner|0x80072601, -2147015167|Fail to delete the target connector from external partner.|
> |FallbackCardFormDeactivation|0x8004F664, -2147158428|This operation can’t be completed. You must have at least one active Card form.|
> |FallbackFormDeactivation|0x8004F661, -2147158431|This operation can’t be completed. You must have at least one active Main form.|
> |FallbackFormDeletion|0x8004F654, -2147158444|You cannot delete this form because it is the only fallback form of type {0} for the {1} entity. Each entity must have at least one fallback form for each form type.|
> |FallbackMainInteractionCentricFormDeactivation|0x8004F666, -2147158426|This operation can’t be completed. You must have at least one active MainInteractionCentric form.|
> |FallbackQuickFormDeactivation|0x8004F665, -2147158427|This operation can’t be completed. You must have at least one active Quick form.|
> |FaxNoData|0x80043516, -2147207914|The fax cannot be sent because there is no data to send. Specify at least one of the following: a cover page, a fax attachment, a fax description.|
> |FaxNoSupport|0x80043517, -2147207913|The fax cannot be sent because this type of attachment is not allowed or does not support virtual printing to a fax device.|
> |FaxSendBlocked|0x80043510, -2147207920|The recipient is marked as "Do Not Fax".|
> |FaxServiceNotRunning|0x80043511, -2147207919|The Microsoft Windows fax service is not running or is not installed.|
> |FeatureNotEnabled|0x80061113, -2147086061|This operation couldn't be completed because this feature isn’t enabled for your organization.|
> |FederatedEndpointError|0x80044505, -2147203835|The username ADFS endpoint is enabled, which is blocking the intended authentication endpoint from being reached.|
> |FeedbackFeatureNotEnabled|0x80061770, -2147084432|Feedback feature is not enabled.|
> |FeedbackMinMaxRequired|0x80061772, -2147084430|The minimum and maximum values are required.|
> |FeedbackMinRatingValue|0x80061774, -2147084428|The submitted minimum rating value {0} must be less than the submitted maximum rating value {1}.|
> |FeedbackRatingValue|0x80061773, -2147084429|The rating must be a value from {0} through {1}.|
> |FetchDataSetQueryTimeout|0x8005E00E, -2147098610|The fetch data set query timed out after {0} seconds. Increase the query timeout, and try again.|
> |FieldLevelControlUsedInGlobalContext|0x80160015, -2146041835|The control '{0}' has a property that binds to a field which is not allowed in this context. More Details:{1}|
> |FieldLevelSecurityNotSupported|0x80044817, -2147203049|Field level security is not supported for virtual entity.|
> |FileContentIsNull|0x80090004, -2146893820|File content can not be null.|
> |FileInUse|0x80048837, -2147186633|Could not read the file because another application is using the file.|
> |FileNotFound|0x80048440, -2147187648|The attachment file was not found.|
> |FilePickerErrorApplicationInSnapView|0x8005F20D, -2147094003|Try this action again. If the problem continues, check the {0} for solutions or contact your organization's {#Brand_CRM} Administrator. Finally, you can contact {1}.|
> |FilePickerErrorAttachmentTypeBlocked|0x8005F204, -2147094012|Try this action again. If the problem continues, check the {0} for solutions or contact your organization's {#Brand_CRM} Administrator. Finally, you can contact {1}.|
> |FilePickerErrorFileSizeBreached|0x8005F205, -2147094011|Try this action again. If the problem continues, check the {0} for solutions or contact your organization's {#Brand_CRM} Administrator. Finally, you can contact {1}.|
> |FilePickerErrorFileSizeCannotBeZero|0x8005F206, -2147094010|Try this action again. If the problem continues, check the {0} for solutions or contact your organization's {#Brand_CRM} Administrator. Finally, you can contact {1}.|
> |FilePickerErrorUnableToOpenFile|0x8005F207, -2147094009|Try this action again. If the problem continues, check the {0} for solutions or contact your organization's {#Brand_CRM} Administrator. Finally, you can contact {1}.|
> |FileReadError|0x80048437, -2147187657|There was an error reading the file from the file system. Make sure you have read permission for this file, and then try migrating the file again.|
> |FileSizeExceeded|0x80071026, -2147020762|Unable to copy the documents. The selected file exceeds the maximium size limit of 128 MB.|
> |FileSizeExceededForNonChunkedRequest|0x80090001, -2146893823|Maximum file size supported for {0} is [{1}] MB. File of [{2} MB] size may only be {0}ed using staged chunk {0}.|
> |FileStoreFeatureNotEnabled|0x80072520, -2147015392|Feature not enabled for this organization|
> |FileTypeNotSupported|0x800609B4, -2147087948|The specified file type is not supported as template.|
> |FilteredDuetoAntiSpam|0x80040325, -2147220699|This customer is filtered due to AntiSpam settings.|
> |FilteredDuetoInactiveState|0x8004032a, -2147220694|This customer is filtered due to inactive state.|
> |FilteredDuetoMissingEmailAddress|0x8004032e, -2147220690|This customer is filtered due to missing email address.|
> |FinalMergedEntityIsNull|0x80060443, -2147089341|Error creating or updating Business Process: final merged entity cannot be null.|
> |FinanceAndOperationsVirtualEntityInvalidDataSource|0x80090300, -2146893056|Unable to establish connection using data source: '{0}'. Failed to sync entity metadata. Ensure the data source is configured properly.|
> |FinanceAndOperationsVirtualEntityInvalidEntities|0x80090301, -2146893055|Unable to sync metadata for entities: '{0}'. Ensure the entities are available in data source: '{1}'.|
> |FinanceAndOperationsVirtualEntitySyncError|0x80090302, -2146893054|Failed to sync entity metadata for entity '{0}'. Exception details: {1}.|
> |FirstStageIdInTraversedPathDoesNotMatchFirstStageIdInBusinessProcess|0x80060456, -2147089322|First Stage ID in traversed path ‘{0}’ does not match first Stage ID in Business Process ‘{1}’. Please contact your system administrator.|
> |FiscalPeriodGoalMissingInfo|0x80044903, -2147202813|For a goal of fiscal period type, the fiscal period attribute must be set.|
> |FiscalSettingsAlreadyUpdated|0x80043809, -2147207159|Fiscal settings have already been updated. They can be updated only once.|
> |FlowIsNotActive|0x80060469, -2147089303|Modern Flow must be active to be used on Flow Step.|
> |FlowMissingRecord|0x80050262, -2147155358|You need to select at least one record to trigger this flow.|
> |FlowServiceClientError|0x80060467, -2147089305|Flow client error returned with status code "{0}" and details "{1}".|
> |FlowTriggerNotificationDisabled|0x80072342, -2147015870|Flow trigger notifications are disabled for the organization.|
> |FlowTriggerNotificationFailed|0x80072341, -2147015871|Flow trigger notification call failed during http post. Please check the exception for more details.|
> |FolderDoesNotExist|0x80060901, -2147088127|Folder doesn't exist.|
> |Forbidden|0x8005F102, -2147094270|The server refuses to fulfill the request.|
> |FormDoesNotExist|0x80048406, -2147187706|Form doesn't exist|
> |FormFactorDeclaredMoreThanOnceInForm|0x80160010, -2146041840|Form factor {0} declaration is declared more than once for control with uniqueid {1}. More Details:{2}|
> |FormFactorDeclaredMoreThanOnceInNonFormContext|0x80160013, -2146041837|Form factor {0} declaration is declared more than once. More Details:{1}|
> |FormFactorMissingInForm|0x80160009, -2146041847|Custom control declaration for form factor(s) {0} is missing for control with uniqueid {1}. More Details:{2}|
> |FormFactorMissingInNonFormContext|0x80160012, -2146041838|Custom control declaration for form factor(s) {0} is missing. More Details:{1}|
> |FormTransitionError|0x80040242, -2147220926|The import has failed because the system cannot transition the entity form {0} from unmanaged to managed. Add at least one full (root) component to the managed solution, and then try to import it again.|
> |ForwardMailboxCannotAssociateWithUser|0x8005E207, -2147098105|A forward mailbox cannot be created for a specific user or a queue.  Please remove the regarding field and try again.|
> |ForwardMailboxEmailAddressRequired|0x8005E211, -2147098095|An e-mail address is a required field in case of forward mailbox.|
> |ForwardMailboxUnexpectedIncomingDeliveryMethod|0x8005E212, -2147098094|Forward mailbox incoming delivery method can only be none or router.|
> |ForwardMailboxUnexpectedOutgoingDeliveryMethod|0x8005E213, -2147098093|Forward mailbox outgoing delivery method can only be none.|
> |GenericActiveDirectoryError|0x80041d37, -2147214025|Active Directory Error.|
> |GenericAzureActiveDirectoryError|0x80041d54, -2147213996|Azure Active Directory Error.|
> |GenericImportTranslationsError|0x80060752, -2147088558|Errors were encountered while processing the translations import file.|
> |GenericManagedPropertyFailure|0x8004F026, -2147160026|The evaluation of the current component(name={0}, id={1}) in the current operation ({2}) failed during managed property evaluation of condition: {3}|
> |GenericMetadataSyncFailed|0x8005F246, -2147093946|Sorry, something went wrong. Please try again, or restart the app.|
> |GenericMetadataSyncFailedWithContinue|0x8005F247, -2147093945|Sorry, something went wrong downloading server configuration changes.  You can continue to use the app with the older configuration, however you may experience problems including errors when saving.  If this issue continues please contact your Dynamics 365 administrator and provide the information available when you choose ‘more information’.|
> |GenericTransformationInvocationError|0x8004037b, -2147220613|The transformation returned invalid data.|
> |GetOnPolymorphicAttributeError|0x80072532, -2147015374|Cannot query for {0} on {1}|
> |GetPhotoFromGalleryFailed|0x8005F208, -2147094008|Try this action again. If the problem continues, check the {0} for solutions or contact your organization's {#Brand_CRM} Administrator. Finally, you can contact {1}.|
> |GetTenantIdFailure|0x80071109, -2147020535|Error occurred while getting TenantId.|
> |GoalAttributeAlreadyMapped|0x80044807, -2147203065|The Metric Detail for Specified Goal Attribute already exists.|
> |GoalMissingPeriodTypeInfo|0x80044908, -2147202808|Goal Period Type needs to be specified when creating a goal. This field cannot be null.|
> |GoalPercentageAchievedValueOutOfRange|0x8004F682, -2147158398|The percentage achieved value has been set to 0 because the calculated value is not in the allowed range.|
> |GoOfflineBCPFileSize|0x80044224, -2147204572|Client was not able to download BCP file. Contact your system administrator for assistance and try going offline again.|
> |GoOfflineDbSizeLimit|0x80044222, -2147204574|You have exceeded the storage limit for your offline database. You must reduce the amount of data to be taken offline by changing your Local Data Groups.|
> |GoOfflineEmptyFileForDelete|0x80044230, -2147204560|Data file for delete is empty.|
> |GoOfflineFailedMoveData|0x80044225, -2147204571|Client was not able to download data. Contact your system administrator for assistance and try going offline again.|
> |GoOfflineFailedPrepareMsde|0x80044226, -2147204570|Prepare MSDE failed. Contact your system administrator for assistance and try going offline again.|
> |GoOfflineFailedReloadMetadataCache|0x80044227, -2147204569|The Microsoft Dynamics 365 for Outlook was unable to go offline. Please try going offline again.|
> |GoOfflineFeatureNotEnabled|0x8004422a, -2147204566|Offline capability is not supported with Microsoft Dynamics 365 for Outlook.|
> |GoOfflineFileWasDeleted|0x80044229, -2147204567|Data file was deleted on server before it was sent to client.|
> |GoOfflineGetBCPFileException|0x80044221, -2147204575|Dynamics 365 server was not able to process your request. Contact your system administrator for assistance and try going offline again.|
> |GoOfflineMetadataVersionsMismatch|0x80044220, -2147204576|Client and Server metadata versions are different due to new customization on the server. Please try going offline again.|
> |GoOfflineServerFailedGenerateBCPFile|0x80044223, -2147204573|Dynamics 365 server was not able to generate BCP file. Contact your system administrator for assistance and try going offline again.|
> |GraphApiS2SSetupFailureException|0x80044260, -2147204512|Server to Server Authentication with Exchange for Office Graph Api  is not set up.|
> |GridNotValidForTargetEntity|0x80160049, -2146041783|Grid control (id={0}) not valid for target entity {1}. More Details:{2}|
> |GuidNotPresent|0x80040362, -2147220638|The required globally unique identifier (GUID) in this row is not present|
> |HeaderValueDoesNotMatchAttributeDisplayLabel|0x80040370, -2147220624|The column heading does not match the attribute display label.|
> |HiddenPropertyValidationFailed|0x80061000, -2147086336|You can't create a property instance for a hidden property.|
> |HiddensheetNotAvailable|0x800609B6, -2147087946|The hidden sheet is not available.|
> |HierarchicalOperationFailed|0x8008100F, -2146955249|This operation couldn't be completed on this hierarchy. An error occurred while performing this operation for {0}. You can perform the operation separately on this product to fix the error, and then try the operation again for the complete hierarchy.|
> |HierarchyCalculateLimitReached|0x80060547, -2147089081|Calculations can't be performed online because the master record hierarchy depth limit of {0} has been reached.|
> |HipInvalidCertificate|0x8004Ed45, -2147160763|Invalid Certificate for using HIP.|
> |HipNoSettingError|0x8004Ed44, -2147160764|No Hip application configuration setting [{0}] was found.|
> |HonorPauseWithoutSLAKPIError|0x80045000, -2147201024|SLA can be set to honor pause and resume only if Use SLA KPI is set to Yes.|
> |HybridSSSExchangeOnlineS2SCertActsExpired|0x80131500, -2146233088|Certificate used for S2S authentication of Dynamics 365 Onpremise with Exchange Online has expired|
> |HybridSSSExchangeOnlineS2SCertExpired|0x80131509, -2146233079|Certificate used for S2S authentication of Dynamics 365 Onpremise with Exchange Online has expired|
> |ImageAttributeNotSupportedFullImage|0x8009000D, -2146893811|Image attribute {0} of entity {1} does not support storing full image.|
> |ImageInvalidMaxSizeInKB|0x8009000E, -2146893810|Invalid MaxSizeInKB for image attribute {0} of entity {1}. Valid size should be between [{2} - {3}] KB|
> |ImportArticleTemplateError|0x8004800D, -2147188723|There was an error in parsing the article templates in Import Xml|
> |ImportAttributeNameError|0x80048062, -2147188638|Invalid name for attribute {0}.  Custom attribute names must start with a valid customization prefix. The prefix for a solution component should match the prefix that is specified for the publisher of the solution.|
> |ImportChannelPropertyGroupError|0x800608F3, -2147088141|An error occurred while importing Channel Property Group.|
> |ImportComponentDeletedIgnored|0x8004847c, -2147187588|You cannot update this component because it does not exist in this Microsoft Dynamics 365 organization.|
> |ImportConfigNotSpecified|0x80040322, -2147220702|Cannot process with Bulk Import as Import Configuration not specified.|
> |ImportContractTemplateError|0x8004800B, -2147188725|There was an error in parsing the contract templates in Import Xml|
> |ImportConvertRuleError|0x8004F869, -2147157911|An error occurred while importing Convert Rules.|
> |ImportCustomizationsBadZipFileError|0x80048060, -2147188640|The solution file is invalid. The compressed file must contain the following files at its root: solution.xml, customizations.xml, and [Content_Types].xml. Customization files exported from previous versions of Microsoft Dynamics 365 are not supported.|
> |ImportDashboardDeletedError|0x8004E308, -2147163384|A dashboard with the same id is marked as deleted in the system. Please first publish the system form entity and import again.|
> |ImportDefaultAsPackageError|0x80048049, -2147188663|The package supplied for the default solution is trying to install it in managed mode. The default solution cannot be managed. In the XML for the default solution, set the Managed value back to "false" and try to import the solution again.|
> |ImportDependencySolutionError|0x80048034, -2147188684|{0} requires solutions that are not currently installed. Import the following solutions before Importing this one. {1} |
> |ImportDuplicateEntity|0x8004810c, -2147188468|This import has failed because a different entity with the identical name, {0}, already exists in the target organization.|
> |ImportEmailTemplateError|0x8004800C, -2147188724|There was an error in parsing the email templates in Import Xml|
> |ImportEmailTemplateErrorMissingFile|0x8004802B, -2147188693|E-mail Template '{0}' import: The attachment '{1}' was not found in the import zip file.|
> |ImportEmailTemplatePersonalError|0x80048014, -2147188716|E-mail Template was not imported. The Template is a personal template on the target system; import cannot overwrite personal templates.|
> |ImportEntityCustomResourcesError|0x80048002, -2147188734|Invalid Custom Resources in the Import File|
> |ImportEntityCustomResourcesNewStringError|0x80048003, -2147188733|Invalid Entity new string in the Custom Resources|
> |ImportEntityIconError|0x80048001, -2147188735|Invalid Icon in the Import File|
> |ImportEntityNameMismatchError|0x80048008, -2147188728|The number of format parameters passed into the input string is incorrect|
> |ImportEntitySystemUserLiveMismatchError|0x80048025, -2147188699|The systemuser entity was imported but customized forms for the entity were not imported. Systemuser entity forms from on-premises or hosted versions of Microsoft Dynamics 365 cannot be imported into Microsoft Dynamics 365 Online.|
> |ImportEntitySystemUserOnPremiseMismatchError|0x80048024, -2147188700|The systemuser entity was imported, but customized forms for the entity were not imported. Systemuser entity forms from Microsoft Dynamics 365 Online cannot be imported into on-premises or hosted versions of Microsoft Dynamics 365.|
> |ImportExportDeprecatedError|0x80048045, -2147188667|This message is no longer available. Please consult the SDK for alternative messages.|
> |ImportFieldSecurityProfileAttributesMissingError|0x80048064, -2147188636|Some field security permissions could not be imported because the following fields are not in the system: {0}.|
> |ImportFieldSecurityProfileError|0x80048072, -2147188622|An error occurred while importing Field Security Profile.|
> |ImportFieldSecurityProfileIsSecuredMissingError|0x80048063, -2147188637|Some field security permissions could not be imported because the following fields are not securable: {0}.|
> |ImportFieldXmlError|0x80048006, -2147188730|The number of format parameters passed into the input string is incorrect|
> |ImportFileFailed|0x80050125, -2147155675|Import and extraction of the file failed.|
> |ImportFileSignatureInvalid|0x80048065, -2147188635|The import file has an invalid digital signature.|
> |ImportFileTooLargeToUpload|0x80040375, -2147220619|The import file is too large to upload.|
> |ImportFileUnprocessed|0x80072035, -2147016651|Unprocessed files found: {0}|
> |ImportFormXmlError|0x80048007, -2147188729|The number of format parameters passed into the input string is incorrect|
> |ImportGenericEntitiesError|0x80048020, -2147188704|An error occurred while importing generic entities.|
> |ImportGenericError|0x8004801E, -2147188706|The import failed. For more information, see the related error messages.|
> |ImportHierarchyRuleDeletedError|0x8004F9A1, -2147157599|A hierarchy rule with the same id is marked as deleted in the system,So first publish the customized entity and import again.|
> |ImportHierarchyRuleExistingError|0x8004F9A2, -2147157598|Cannot reuse existing hierarchy rule.|
> |ImportHierarchyRuleOtcMismatchError|0x8004F9A3, -2147157597|There was an error processing hierarchy rules of the same object type code.(unresolvable system collision)|
> |ImportInvalidFileError|0x80048000, -2147188736|Invalid Import File|
> |ImportInvalidXmlError|0x8004802C, -2147188692|This solution package cannot be imported because it contains invalid XML. You can attempt to repair the file by manually editing the XML contents using the information found in the schema validation errors, or you can contact your solution provider.|
> |ImportIsvConfigError|0x8004800E, -2147188722|There was an error parsing the IsvConfig during Import|
> |ImportLanguagesIgnoredError|0x80048026, -2147188698|Translated labels for the following languages could not be imported because they have not been enabled for this organization: {0}|
> |ImportMailMergeTemplateEntityMissingError|0x80048480, -2147187584|The {0} mail merge template was not imported because the {1} entity associated with this template is not in the target system.|
> |ImportMailMergeTemplateError|0x80048456, -2147187626|There was an error in parsing the mail merge templates in Import Xml|
> |ImportMapInUse|0x80048465, -2147187611|One or more of the selected data maps cannot be deleted because it is currently used in a data import.|
> |ImportMappingsInvalidIdSpecified|0x80048427, -2147187673|The XML file has one or more invalid IDs. The specified ID cannot be used as a unique identifier.|
> |ImportMappingsMissingEntityMapError|0x80048010, -2147188720|This customization file contains a reference to an entity map that does not exist on the target system.|
> |ImportMappingsSystemMapError|0x8004800F, -2147188721|Import cannot create system attribute mappings|
> |ImportMissingComponent|0x8004801F, -2147188705|Cannot add a Root Component {0} of type {1} because it is not in the target system.|
> |ImportMissingDependenciesError|0x8004801D, -2147188707|The following solution cannot be imported: {0}. Some dependencies are missing.|
> |ImportMissingRootComponentEntry|0x8004803A, -2147188678|The import has failed because component {0} of type {1} is not declared in the solution file as a root component. To fix this, import again using the XML file that was generated when you exported the solution.|
> |ImportMobileOfflineProfileError|0x8006099F, -2147087969|An error occurred while importing Mobile Offline Profiles.|
> |ImportNewPluginTypesError|0x80048071, -2147188623|Existing plug-in types have been removed. Please update major or minor verion of plug-in assembly.|
> |ImportNonWellFormedFileError|0x80048013, -2147188717|Invalid customization file. This file is not well formed.|
> |ImportNotComplete|0x80048472, -2147187598|One or more imports are not in completed state. Imported records can only be deleted from completed jobs. Wait until job completes, and then try again.|
> |ImportOperationChildFailure|0x80044334, -2147204300|One or more of the Import Child Jobs Failed|
> |ImportOptionSetAttributeError|0x80048039, -2147188679|Attribute '{0}' was not imported as it references a non-existing global Option Set ('{1}').|
> |ImportOptionSetsError|0x80048030, -2147188688|An error occurred while importing OptionSets.|
> |ImportOrgSettingsError|0x80048019, -2147188711|There was an error parsing the Organization Settings during Import.|
> |ImportPluginTypesError|0x80048012, -2147188718|An error occurred while importing plug-in types.|
> |ImportRelationshipRoleMapsError|0x8004800A, -2147188726|The number of format parameters passed into the input string is incorrect|
> |ImportRelationshipRolesError|0x80048009, -2147188727|The number of format parameters passed into the input string is incorrect|
> |ImportRelationshipRolesPrivilegeError|0x8004802F, -2147188689|{0} cannot be imported. The {1} privilege is required to import this component.|
> |ImportReportsError|0x80048032, -2147188686|An error occurred while importing Reports.|
> |ImportRestrictedSolutionError|0x8004F007, -2147160057|Solution ID provided is restricted and cannot be imported.|
> |ImportRibbonsError|0x80048031, -2147188687|An error occurred while importing Ribbons.|
> |ImportRoleError|0x80048017, -2147188713|Cannot import security role. The role with specified role id is not updatable or role name is not unique.|
> |ImportRolePermissionError|0x80048018, -2147188712|You do not have the necessary privileges to import security roles.|
> |ImportRoutingRuleError|0x8004F867, -2147157913|An error occurred while importing Routing Rule Sets.|
> |ImportSavedQueryDeletedError|0x8004801B, -2147188709|A saved query with the same id is marked as deleted in the system. Please first publish the customized entity and import again.|
> |ImportSavedQueryExistingError|0x80048005, -2147188731|The number of format parameters passed into the input string is incorrect|
> |ImportSavedQueryOtcMismatchError|0x80048004, -2147188732|There was an error processing saved queries of the same object type code (unresolvable system collision)|
> |ImportSdkMessagesError|0x80048016, -2147188714|An error occurred while importing Sdk Messages.|
> |ImportServiceEndpointError|0x80048073, -2147188621|An error occurred while importing Service Endpoints.|
> |ImportSiteMapError|0x80048011, -2147188719|An error occurred while importing the Site Map.|
> |ImportSlaError|0x8004F868, -2147157912|An error occurred while importing SLAs.|
> |ImportSolutionError|0x80048033, -2147188685|An error occurred while importing a Solution.|
> |ImportSolutionIsvConfigWarning|0x80048042, -2147188670|ISV Config was overwritten.|
> |ImportSolutionManagedError|0x80048038, -2147188680|Solution '{0}' already exists in this system as managed and cannot be upgraded.|
> |ImportSolutionManagedToUnmanagedMismatch|0x80048040, -2147188672|The solution is already installed on this system as an unmanaged solution and the package supplied is attempting to install it in managed mode. Import can only update solutions when the modes match. Uninstall the current solution and try again.|
> |ImportSolutionOrganizationSettingsWarning|0x80048044, -2147188668|Organization settings were overwritten.|
> |ImportSolutionPackageInvalidSku|0x8004806B, -2147188629|The solution package you are importing was generated on Microsoft Dynamics 365 Online, it cannot be imported into on-premises or hosted versions of Microsoft Dynamics 365.|
> |ImportSolutionPackageInvalidSolutionPackageVersion|0x80048068, -2147188632|You can only import solutions with a package version of {0} or earlier into this organization. Also, you can't import any solutions into this organization that were exported from Microsoft Dynamics 365 2011 or earlier.|
> |ImportSolutionPackageMinimumVersionNeeded|0x00000001, 1|Deprecated, not removing now as it might cause issues during integrations.|
> |ImportSolutionPackageNeedsUpgrade|0x80048067, -2147188633|The solution package you are importing was generated on a different version of Microsoft Dynamics 365. The system will attempt to transform the package prior to import. Package Version: {0} {1}, System Version: {2} {3}.|
> |ImportSolutionPackageNotValid|0x80048066, -2147188634|The solution package you are importing was generated on a version of Microsoft Dynamics 365 that cannot be imported into this system. Package Version: {0} {1}, System Version: {2} {3}.|
> |ImportSolutionPackageRequiresOptInAvailable|0x80048069, -2147188631|Some components in the solution package you are importing require opt in. Opt in is available, please consult your administrator.|
> |ImportSolutionPackageRequiresOptInNotAvailable|0x8004806A, -2147188630|The solution package you are importing was generated on a SKU of Microsoft Dynamics 365 that supports opt in. It cannot be imported in your system.|
> |ImportSolutionPackageUpgradeError|0x80048074, -2147188620|An error occurred while importing Solution Package Upgrade.|
> |ImportSolutionSiteMapWarning|0x80048043, -2147188669|SiteMap was overwritten.|
> |ImportSolutionUnmanagedToManagedMismatch|0x80048041, -2147188671|The solution is already installed on this system as a managed solution and the package supplied is attempting to install it in unmanaged mode. Import can only update solutions when the modes match. Uninstall the current solution and try again.|
> |ImportSystemSolutionError|0x80048046, -2147188666|System solution cannot be imported.|
> |ImportTemplateLanguageIgnored|0x8004847a, -2147187590|You cannot import this template because its language is not enabled in your Microsoft Dynamics 365 organization.|
> |ImportTemplatePersonalIgnored|0x8004847b, -2147187589|You cannot import this template because it is set as "personal" in your Microsoft Dynamics 365 organization.|
> |ImportTranslationMissingSolutionError|0x80048047, -2147188665|An error occurred while importing the translations. The solution associated with the translations does not exist in this system.|
> |ImportTranslationsBadZipFileError|0x80048061, -2147188639|The translation file is invalid. The compressed file must contain the following files at its root: {0}, [Content_Types].xml.|
> |ImportVisualizationDeletedError|0x8004E013, -2147164141|A saved query visualization with id {0} is marked for deletion in the system. Please publish the customized entity first and then import again.|
> |ImportVisualizationExistingError|0x8004E014, -2147164140|A saved query visualization with id {0} already exists in the system, and cannot be resused by a new custom entity.|
> |ImportWillExceedCustomEntityQuota|0x8004b043, -2147176381|This import process is trying to import {0} new custom entities. This would exceed the custom entity limits for this organization.|
> |ImportWorkflowAttributeDependencyError|0x80048022, -2147188702|Cannot import workflow definition. Required attribute dependency is missing.|
> |ImportWorkflowEntityDependencyError|0x80048023, -2147188701|Cannot import workflow definition. Required entity dependency is missing.|
> |ImportWorkflowError|0x80048021, -2147188703|Cannot import workflow definition. The workflow with specified workflow id is not updatable or workflow name is not unique.|
> |ImportWorkflowNameConflictError|0x80048027, -2147188697|Workflow {0} cannot be imported because a workflow with same name and different unique identifier exists in the target system. Change the name of this workflow, and then try again.|
> |ImportWorkflowPublishedError|0x80048028, -2147188696|Workflow {0}({1}) cannot be imported because a workflow with same unique identifier is published on the target system. Unpublish the workflow on the target system before attempting to import this workflow again.|
> |ImportWrongPublisherError|0x8004801C, -2147188708|The following managed solution cannot be imported: {0}. The publisher name cannot be changed from {1} to {2}.|
> |ImportXsdValidationError|0x8004801A, -2147188710|The import file is invalid. XSD validation failed with the following error: '{0}'. The validation failed at: '...{1} <<<<<ERROR LOCATION>>>>> {2}...'."|
> |InaccessibleSmtpServer|0x8005E227, -2147098073|Cannot reach to the smtp server. Please check that the smtp server is accessible.|
> |InactiveEmailServerProfile|0x8005E228, -2147098072|Email server profile is disabled. Cannot process email for disabled profile.|
> |InactiveMailbox|0x8005E219, -2147098087|The mailbox is in inactive state. Send/Receive mails are allowed only for active mailboxes.|
> |InactiveMetricSetOnGoal|0x8004F686, -2147158394|An inactive metric cannot be set on a goal.|
> |InactiveRollupQuerySetOnGoal|0x8004F685, -2147158395|An inactive rollup query cannot be set on a goal.|
> |IncidentCannotCancel|0x8004440e, -2147204082|The incident can not be cancelled because there are open activities for this incident.|
> |IncidentContractDoesNotHaveAllotments|0x80044403, -2147204093|The contract does not have enough allotments. The case can not be created against this contract.|
> |IncidentInvalidAllotmentType|0x8004440b, -2147204085|The allotment type for the contract is invalid.|
> |IncidentInvalidContractLineStateForCreate|0x8004440d, -2147204083|The case can not be created against this contract line item because the contract line item is cancelled or expired.|
> |IncidentInvalidContractStateForCreate|0x80044400, -2147204096|The case can not be created against this contract because of the contract state.|
> |IncidentIsAlreadyClosedOrCancelled|0x80044411, -2147204079|Already Closed or Canceled|
> |IncidentMissingActivityRegardingObject|0x80044409, -2147204087|The incident id is missing.|
> |IncidentMissingContractDetail|0x80044401, -2147204095|The contract detail id is missing.|
> |IncidentNullSpentTimeOrBilled|0x8004440c, -2147204084|The timespent on the Incident is NULL or IncidentResolution Activity's IsBilled is NULL.|
> |IncomingDeliveryIsForwardMailbox|0x8005E223, -2147098077|Cannot poll mails from the mailbox. Its incoming delivery method is Forward mailbox.|
> |IncomingServerLocationAndSslSetToNo|0x8005E23E, -2147098050|The URL specified for Incoming Server Location uses HTTPS but the Use SSL for Incoming Connection option is set to No. Set this option to Yes, and then try again.|
> |IncomingServerLocationAndSslSetToYes|0x8005E240, -2147098048|The URL specified for Incoming Server Location uses HTTP but the Use SSL for Incoming Connection option is set to Yes. Specify a server location that uses HTTPS, and then try again.|
> |IncompatibleStepsEncountered|0x8006088B, -2147088245|You can't enable the EnforceReadOnlyPlugins setting because plug-ins that change data are registered on read-only SDK messages. {0}|
> |IncompatibleValueTypeInLookup|0x80160039, -2146041799|Parameter {0} is incompatible for lookup property {1}. More Details:{2}|
> |IncompleteTransformationParameterMappingsFound|0x8004037d, -2147220611|One or more mandatory transformation parameters do not have mappings defined for them.|
> |InconsistentAttributeNameCasing|0x8004F043, -2147159997|Detected inconsistent attribute name casing, expected: {0}, actual: {1}.|
> |InconsistentConfiguration|0x80072009, -2147016695|More than one configuration found for {0} with id {1}.|
> |InconsistentProductRelationshipState|0x8004F996, -2147157610|The other row for the product relationship is not available.|
> |IncorrectActiveStageEntity|0x80060462, -2147089310|Active stage is not on '{0}' entity.|
> |IncorrectAttributeValueType|0x80044354, -2147204268|Invalid Attribute Value Type for {0}. Expected: {1}, Found: {2}|
> |IncorrectEntitySetName|0x8006089C, -2147088228|The entity set name {0} must start with a valid customization prefix.|
> |IncorrectFileFormat|0x80072037, -2147016649|The file {0} cannot be imported.|
> |IncorrectSingleFileMultipleEntityMap|0x80048502, -2147187454|There should be two or more Entity Mappings defined when EntitiesPerFile in ImportMap is set to Multiple|
> |IncreasingDaysWillResetMobileOfflineData|0x80060991, -2147087983|Increasing the number of days will cause a reset of mobile offline data and a resynchronization with mobile devices.|
> |IndexOutOfRange|0x8005E008, -2147098616|The index {0} is out of range for {1}. Number of elements present are {2}.|
> |IndexSizeConstraintViolated|0x80060895, -2147088235|Index size exceeded the size limit of {0} bytes. The key is too large. Try removing some columns or making the strings in string columns shorter.|
> |InitializeErrorNoReadOnSource|0x8004F800, -2147158016|The operation could not be completed because you donot have read access on some of the fields in {0} record.|
> |InitializeFileRequestFailure|0x80072555, -2147015339|Error occured during initialize file request. (RecordId: {0}, EntityName: {1}) Details:{2}|
> |InputParameterFieldIncorrect|0x80060378, -2147089544|Input parameter “{0}” does not match the input parameter field configured. Contact your system administrator to check the configuration metadata if the error persists.|
> |InsertOptionValueInvalidType|0x80044320, -2147204320|You can add option values only to picklist and status attributes.|
> |InstanceOutsideEffectiveRange|0x8004E115, -2147163883|Cannot perform the operation. An instance is outside of series effective expansion range.|
> |InsufficientAccessMode|0x80044502, -2147203838|User does not have read-write access to the Dynamics 365 organization.|
> |InsufficientAuthTicket|0x8004A103, -2147180285|The ticket specified for authentication didn't meet policy|
> |InsufficientColumnsInSubQuery|0x8004E022, -2147164126|One or more columns required by the outer query are not available from the sub-query.|
> |InsufficientCreatePrivilege|0x8006110A, -2147086070|External Party don't have sufficient privilege to create new record with given parameters.|
> |InsufficientPrivilegesSupportUser|0x80048345, -2147187899|Support user does not have permission to perform this operation.|
> |InsufficientPrivilegeToQueueOwner|0x80040520, -2147220192|The owner of this queue does not have sufficient privileges to work with the queue.|
> |InsufficientRetrievePrivilege|0x80061109, -2147086071|External Party don't have sufficient privilege to retrieve record.|
> |InsufficientTransformationParameters|0x80048506, -2147187450|Insufficient parameters to execute transformation mapping.|
> |InsufficientUpdatePrivilege|0x8006110B, -2147086069|External Party don't have sufficient privilege to update record.|
> |IntegerValueOutOfRange|0x8004432F, -2147204305|A validation error occurred. An integer provided is outside of the allowed values for this attribute.|
> |IntegratedAuthenticationIsNotAllowed|0x80044301, -2147204351|Integrated authentication is not allowed.|
> |InvalidAbsoluteUrlFormat|0x80048055, -2147188651|The absolute url contains invalid characters. Please use a different name. Valid absolute url cannot ends with the following strings: .aspx, .ashx, .asmx, .svc|
> |InvalidAccessMaskForTeamTemplate|0x80048335, -2147187915|Invalid access mask is specified for team template.|
> |InvalidAccessModeTransition|0x80041d66, -2147213978|The client access license cannot be changed because the user does not have a Microsoft Dynamics 365 Online license. To change the access mode, you must first add a license for this user in the Microsoft Online Service portal.|
> |InvalidAccessRights|0x8004020d, -2147220979|Invalid access rights.|
> |InvalidAccessRightsPassed|0x80048347, -2147187897|Invalid Access Rights passed.|
> |InvalidActivityMimeAttachmentId|0x80050005, -2147155963|Invalid activityMimeAttachmentId.|
> |InvalidActivityOwnershipTypeMask|0x8004F120, -2147159776|A custom entity defined as an activity must be user or team owned.|
> |InvalidActivityPartyAddress|0x80043518, -2147207912|One or more activity parties have invalid addresses.|
> |InvalidActivityType|0x80040321, -2147220703|An invalid object type was specified for distributing activities.|
> |InvalidActivityTypeForCampaignActivityPropagate|0x8004030f, -2147220721|Must specify a valid CommunicationActivity|
> |InvalidActivityTypeForList|0x80040305, -2147220731|Cannot create activities of the specified list type.|
> |InvalidActivityXml|0x80043514, -2147207916|Invalid Xml in an activity config file.|
> |InvalidAllotmentsCalc|0x800404ef, -2147220241|Allotments: remaining + used != total|
> |InvalidAllotmentsOverage|0x8004430B, -2147204341|Allotment overage is invalid.|
> |InvalidAllotmentsRemaining|0x800404f2, -2147220238|The allotments remaining is invalid|
> |InvalidAllotmentsTotal|0x800404f0, -2147220240|The total allotments is invalid|
> |InvalidAllotmentsUsed|0x800404f1, -2147220239|The allotments used is invalid|
> |InvalidAmountFreeResourceLimit|0x8004B060, -2147176352|The resource type {0} cannot have an amount free value of {1}.|
> |InvalidAmountProvided|0x8004B02D, -2147176403|The service component {0} cannot have a provide {1} of resource type {2}.|
> |InvalidApplicationUserUpdate|0x80072562, -2147015326|Invalid Application User Update|
> |InvalidAppModuleClientType|0x80050126, -2147155674|The client type value passed is incorrect and not in the valid range.|
> |InvalidAppModuleComponent|0x80050113, -2147155693|The ID {0} doesn’t exist or isn’t valid for the component type “{1}”.|
> |InvalidAppModuleComponentEntity|0x80050108, -2147155704|App Module Import Failed because entity with Unique Name {0} doesn't exist in system. Remove this entity from App Module Components or bring this entity as part of your solution.|
> |InvalidAppModuleComponentType|0x80050112, -2147155694|An app can’t reference the component type “{0}”.|
> |InvalidAppModuleEventHandlers|0x8005012F, -2147155665|The event handlers provided for the app are invalid.|
> |InvalidAppModuleId|0x80050116, -2147155690|The app ID is invalid or you don’t have access to the app.|
> |InvalidAppModuleOptimizedFor|0x8005013A, -2147155654|The optimized for value(s) provided for the app are invalid.|
> |InvalidAppModuleSiteMap|0x80050110, -2147155696|The customized site map for this app module could not be used because it is configured incorrectly. To resolve this issue, navigate to the full experience to repair the customized site map and import it again.|
> |InvalidAppModuleSiteMapXml|0x80050109, -2147155703|The App Module SiteMap is invalid.|
> |InvalidAppModuleUniqueName|0x8005011E, -2147155682|The unique name exceeds the maximum length of 40 characters or contains invalid characters. Only letters and numbers are allowed.|
> |InvalidAppModuleUrl|0x8005011A, -2147155686|The app URL is not unique or the format is invalid.|
> |InvalidAppointmentInstance|0x8004E104, -2147163900|Invalid appointment entity instance.|
> |InvalidApproveFromDraftArticle|0x80048dfd, -2147185155|You are trying to approve an article that has a status of draft. You can only approve an article with the status of unapproved.|
> |InvalidApproveFromPublishedArticle|0x80048dfb, -2147185157|You are trying to approve an article that has a status of published. You can only approve an article with the status of unapproved.|
> |InvalidArgument|0x80040203, -2147220989|Invalid argument.|
> |InvalidArticleState|0x800404fb, -2147220229|The article state is undefined|
> |InvalidArticleStateTransition|0x800404fc, -2147220228|This article state transition is invalid because of the current state of the article|
> |InvalidArticleTemplateState|0x800404fd, -2147220227|The article template state is undefined|
> |InvalidAssemblyProcessorArchitecture|0x8004417E, -2147204738|The given plugin assembly was built with an unsupported target platform and cannot be loaded.|
> |InvalidAssemblySourceType|0x8004417D, -2147204739|The given plugin assembly source type is not supported for isolated plugin assemblies.|
> |InvalidAssigneeId|0x80040210, -2147220976|Invalid assignee id.|
> |InvalidAssociatedSavedQuery|0x800609AE, -2147087954|Selected saved query does not belong to associated entity of the mobile offline profile item.|
> |InvalidAttachmentsFolder|0x80048490, -2147187568|The compressed (.zip) file can't be uploaded because the folder "Attachments" contains one or more subfolders. Remove the subfolders and try again.|
> |InvalidAttribute|0x8005E009, -2147098615|Attribute {0} cannot be found for entity {1}.|
> |InvalidAttributeCopyTarget|0x80048545, -2147187387|A target attribute must be unset or have the same value as the source attribute when copying.|
> |InvalidAttributeDataType|0x80044815, -2147203051|Attribute data type: {0} is not valid for this entity.|
> |InvalidAttributeFieldType|0x80044816, -2147203050|Attribute field type: {0} is not valid for virtual entity.|
> |InvalidAttributeFound|0x8004E303, -2147163389|A Form XML of type {1} with id {2} cannot contain attribute: {0}.|
> |InvalidAttributeInXaml|0x80060412, -2147089390|Attribute - {0} in the XAML is invalid|
> |InvalidAttributeMap|0x80046203, -2147196413|InvalidAttributeMap Error Occurred|
> |InvalidAttributeMapping|0x80048438, -2147187656|One or more attribute mappings is invalid.|
> |InvalidAttributeQuery|0x80072527, -2147015385|Attributes must be part of the requested EntityMetadata properties when an AttributeQuery is specified. Expect property = {0} in requested entity properties list.|
> |InvalidAuth|0x80048516, -2147187434|Organization Authentication does not match the current discovery service Role.|
> |InvalidAuthTicket|0x8004A100, -2147180288|The ticket specified for authentication didn't pass validation|
> |InvalidBaseAttributeError|0x80044242, -2147204542|Invalid Base attribute.|
> |InvalidBaseUnit|0x80043b0b, -2147206389|The base unit does not belong to the schedule.|
> |InvalidBehavior|0x800608A1, -2147088223|The Behavior value of this attribute can't be changed.|
> |InvalidBehaviorSelection|0x800608A0, -2147088224|The behavior of this Date and Time field can only be changed to “Date Only".|
> |InvalidBlockList|0x80090006, -2146893818|Commit file operation failed. Either the specified block list is invalid or some chunk(s) are missing to upload.|
> |InvalidBrowserToConfigureOrganization|0x8004D255, -2147167659|Browser not compatible to configure organization|
> |InvalidBusinessProcess|0x80060389, -2147089527|Invalid Business Process.|
> |InvalidCaller|0x80040257, -2147220905|Cannot switch ExecutionContext to system user without setting Caller first.|
> |InvalidCascadeLinkType|0x80048204, -2147188220|The cascade link type is not valid for the cascade action.|
> |InvalidCategory|0x8004E009, -2147164151|Category is invalid. All the measures in the category either do not have same primary group by or are a mix of aggregate and non-aggregate data.|
> |InvalidCertificate|0x8005E23A, -2147098054|The given certificate is invalid.|
> |InvalidChangeProcess|0x80092002, -2146885630|Invalid change process status request. Current process status is {0}, which cannot transition to {1}.|
> |InvalidChannelForCampaignActivityPropagate|0x80040310, -2147220720|Cannot distribute activities for campaign activities of the specified channel type.|
> |InvalidChannelOrigin|0x80060602, -2147088894|An entitlement channel term with the same channel already exists. Specify a different channel and try again.|
> |InvalidCharactersInField|0x80040278, -2147220872|The field '{0}' contains one or more invalid characters.|
> |InvalidCharInConnectorName|0x80072604, -2147015164|Connector name must be alphanumeric, '-', or '_' and start with alphanumeric.|
> |InvalidClassIdInReferencePanelSection|0x80061503, -2147085053|Reference Panel section can have only sub-grid, quick view form, knowledge base search, i-frame and HTML web resource controls. Found control with invalid classid {0}.|
> |InvalidCollectionName|0x8006088E, -2147088242|An entity with that collection name already exists. Specify a unique name.|
> |InvalidColumnMapping|0x80040377, -2147220617|ColumnMapping is Invalid. Check that the target attribute exists.|
> |InvalidColumnNumber|0x80040336, -2147220682|The column number specified in the data map does not exist.|
> |InvalidCommand|0x8005E100, -2147098368|Invalid command.|
> |InvalidComplexControlId|0x8005E103, -2147098365|The complex control id is invalid.|
> |InvalidComplexTypeNamespace|0x80090113, -2146893549|The namespace '{0}' is invalid namespace for complex object.|
> |InvalidComponentType|0x80072004, -2147016700|Component type {0} cannot be found|
> |InvalidConnectionString|0x8004023f, -2147220929|The connection string not found or invalid.|
> |InvalidContentRangeForFileUpload|0x80090005, -2146893819|Content range is either not valid or size of the payload [{0}] doesn't match with the chunk size provided.|
> |InvalidContractDetailId|0x800404f6, -2147220234|The Contract detail id is invalid|
> |InvalidControlClass|0x8004E307, -2147163385|The Form XML of type {1} with id {2} cannot contain controls elements with class id: {0}.|
> |InvalidControlDescriptionRootNode|0x80160006, -2146041850|Invalid XmlNode passed as input parameter The expected XmlNode is ControlDescription {0}. More Details:{1}|
> |InvalidConversionRule|0x800608F6, -2147088138|The ConversionRule specified {0} is invalid. Please specify a valid ConversionRule.|
> |InvalidCreateOnProtectedComponent|0x8004F011, -2147160047|You cannot create {0} {1}. Creation cannot be performed when {0} is managed.|
> |InvalidCredentialTypeForNonExchangeIncomingConnection|0x8005E214, -2147098092|For a POP3 email server type, you can only connect using credentials that are specified by a user or queue.|
> |InvalidCrmDateTime|0x8004E103, -2147163901|Invalid CrmDateTime.|
> |InvalidCrossEntityOperation|0x80092004, -2146885628|Invalid cross-entity stage transition. Target entity must be specified.|
> |InvalidCrossEntityTargetOperation|0x80092005, -2146885627|Invalid cross-entity stage transition. Specified target must match {0}.|
> |InvalidCurrency|0x80048cfc, -2147185412|The currency is invalid.|
> |InvalidCustomActivityType|0x8004F125, -2147159771|A custom entity defined as an activity must be of communicaton activity type.|
> |InvalidCustomAttributeValue|0x80090115, -2146893547|The attribute '{0}' of entity '{1}' has invalid value for custom attribute.|
> |InvalidCustomDataDownloadFilters|0x80060996, -2147087978|You can’t set custom download filters because Record Distribution Criteria isn’t set to Other Data Filters.|
> |InvalidCustomer|0x8004022d, -2147220947|The customer is invalid.|
> |InvalidCustomerLookupXml|0x80048051, -2147188655|Customer lookup Xml is invalid. One or more relationships is/are missing.|
> |InvalidCustomReportingWizardXml|0x80040491, -2147220335|Invalid wizard xml|
> |InvalidDataDescription|0x8004E000, -2147164160|The data description for the visualization is invalid.|
> |InvalidDataDownloadFilterBusinessUnit|0x8005F222, -2147093982|For an entity owned by the Business Owner, you can only use the following data download filters: All records or Download related data only.|
> |InvalidDataDownloadFilterOrganization|0x8005F223, -2147093981|For an entity owned by the Organization, you can only use the following data download filters: All records or Download related data only.|
> |InvalidDataFiltersForBUOwnedEntities|0x80060994, -2147087980|You can’t set Records Owned By Me or Records Owned By My Team for business unit-owned entities.|
> |InvalidDataFiltersForOrgOwnedEntities|0x80060995, -2147087979|You can’t set the Other Data filter for organization-owned entities.|
> |InvalidDataFiltersForUnownedEntities|0x80060993, -2147087981|You can’t set the All Record or Other Data filters for unowned entities.|
> |InvalidDataFormat|0x80040356, -2147220650|The source data is not in the required format|
> |InvalidDataSourceEndPoint|0x80044826, -2147203034|Invalid URI: A fully qualified URI without a query string must be provided.|
> |InvalidDataTypeForCustomAttribute|0x80090411, -2146892783|"Cannot create custom attribute '{0}' of Entity '{1}' because the type '{2}' is not valid for custom attribute."|
> |InvalidDataTypeMemberOperation|0x80090105, -2146893563|Unable to perform operation {0} on data type member with Id = '{1}', MemberName = '{2}', DisplayName = '{3}', and ParentTypeId = '{4}'.|
> |InvalidDataTypeMembersInitialization|0x80090107, -2146893561|The data type members for data type with Id = '{0}', Name = '{1}', and DisplayName = '{2}' have already been initialized.|
> |InvalidDataTypeOperation|0x80090104, -2146893564|Unable to perform operation {0} on data type with Id = '{1}', Name = '{2}', and DisplayName = '{3}'.|
> |InvalidDataXml|0x8005E101, -2147098367|Invalid data xml.|
> |InvalidDateAttribute|0x80044805, -2147203067|Date Attribute specified is not an attribute of Source Entity.|
> |InvalidDateTime|0x80040239, -2147220935|The date-time format is invalid, or value is outside the supported range.|
> |InvalidDateTimeFormat|0x800608A2, -2147088222|You can’t change the format value of this attribute to “Date and Time” when the behavior is “Date Only.”|
> |InvalidDaysInFebruary|0x8004E124, -2147163868|February 29 can occur only when pattern start date is in a leap year.|
> |InvalidDeactivateFormType|0x8004F660, -2147158432|You can’t deactivate {0} forms. Only Main forms can be inactive.|
> |InvalidDeleteModification|0x80048203, -2147188221|A system relationship's delete cascading action cannot be modified.|
> |InvalidDeleteOnProtectedComponent|0x8004F013, -2147160045|You cannot delete {0} {1}. Deletion cannot be performed when {0} is managed.|
> |InvalidDeleteProcess|0x80060691, -2147088751|This process can't be deleted because it is a system-generated process.|
> |InvalidDependency|0x8004F036, -2147160010|The {2} component {1} (Id={0}) does not exist.  Failure trying to associate it with {3} (Id={4}) as a dependency. Missing dependency lookup type = {5}.|
> |InvalidDependencyComponent|0x8004F040, -2147160000|The required component {1} (Id={0}) that was defined for the {2} could not be found in the system.|
> |InvalidDependencyEntity|0x8004F041, -2147159999|The required component {1} (Name={0}) that was defined for the {2} could not be found in the system.|
> |InvalidDependencyFetchXml|0x8004F037, -2147160009|The FetchXml ({2}) is invalid.  Failure while calculating dependencies for {1} (Id={0}).|
> |InvalidDeviceToConfigureOrganization|0x8004D254, -2147167660|Mobile device cannot be used to configured organization|
> |InvalidDisplayName|0x8004700c, -2147192820|The specified display name is not valid|
> |InvalidDocumentTemplate|0x800608CB, -2147088181|Invalid document template.|
> |InvalidDomainName|0x80048015, -2147188715|The domain logon for this user is invalid. Select another domain logon and try again.|
> |InvalidDundasPresentationDescription|0x8004E016, -2147164138|The presentation description is not valid for dundas chart.|
> |InvalidElementFound|0x8004E300, -2147163392|Form XML of type {1} with id {2} cannot contain element: {0}.|
> |InvalidEmail|0x8004B016, -2147176426|Email generated from the template is not valid|
> |InvalidEmailAddressFormat|0x80044192, -2147204718|Invalid e-mail address. For more information, contact your system administrator.|
> |InvalidEmailAddressFormatWithEntityTypeAndId|0x80040b0b, -2147218677|Invalid e-mail address for recipient of type '{0}' with ID '{1}'|
> |InvalidEmailAddressInMailbox|0x8005E221, -2147098079|The email address in the mailbox is not correct. Please enter the correct email address to process mails.|
> |InvalidEmailServerLocation|0x8005E218, -2147098088|The server location is either not present or is not valid. Please correct the server location.|
> |InvalidEmailTemplate|0x80040313, -2147220717|Must specify a valid Template Id|
> |InvalidEntitlementActivate|0x80060606, -2147088890|You can't activate an expired, waiting or canceled entitlement.|
> |InvalidEntitlementAssociationToCase|0x80060609, -2147088887|You can't create a case for this entitlement because there are no available terms.|
> |InvalidEntitlementCancel|0x80060607, -2147088889|You can't cancel an entitlement that's in the Draft or Expired state.|
> |InvalidEntitlementChannelTerms|0x80060605, -2147088891|Total terms for a specific case origin on an entitlement channel cannot be more than the total terms of the corresponding entitlement.|
> |InvalidEntitlementContacts|0x80044207, -2147204601|The specified contact isn’t associated with the selected customer.|
> |InvalidEntitlementDeactivate|0x80060608, -2147088888|You can deactivate only entitlements that are active or waiting|
> |InvalidEntitlementExpire|0x80060618, -2147088872|You can't set an entitlement to the Expired state. Active entitlements automatically expire when their end date passes.|
> |InvalidEntitlementForSelectedCustomerOrProduct|0x8004F866, -2147157914|Select an active entitlement that belongs to the specified customer, contact, or product, and then try again.|
> |InvalidEntitlementRenew|0x80060610, -2147088880|You can renew only the entitlements that are expired or canceled.|
> |InvalidEntitlementStateAssociateToCase|0x80060611, -2147088879|You can only associate a case with an active entitlement.|
> |InvalidEntitlementTotalTerms|0x800443FF, -2147204097|Total terms for an entitlement cannot be less than the total terms of any of its corresponding EntitlementChannels.|
> |InvalidEntity|0x8005E00C, -2147098612|Entity {0} cannot be found.|
> |InvalidEntityClassException|0x80040249, -2147220919|Invalid entity class.|
> |InvalidEntityForDateAttribute|0x80044812, -2147203054|Entity For Date Attribute can be either source entity or its parent.|
> |InvalidEntityForLinkedAttribute|0x8004F0FD, -2147159811|Not a valid entity for linked attribute.|
> |InvalidEntityForRollup|0x80044813, -2147203053|The entity {0} is not a valid entity for rollup.|
> |InvalidEntityKeyOperation|0x8006088F, -2147088241|Invalid EntityKey Operation performed : {0}|
> |InvalidEntityLogicalName|0x80072493, -2147015533|Entity name '{0}' is not a valid logical name.|
> |InvalidEntityName|0x80048416, -2147187690|The record type does not match the base record type and the matching record type of the duplicate detection rule.|
> |InvalidEntitySetName|0x8006089B, -2147088229|An entity with the specified entity set name {0} already exists. Specify a unique name.|
> |InvalidEntitySpecified|0x800609B1, -2147087951|The entity is not specified in the template.|
> |InvalidExchangeRate|0x80048cfd, -2147185411|The exchange rate is invalid.|
> |InvalidExportProcessFlowNotActivated|0x80060376, -2147089546|Failed to export Business Process “{0}” because solution does not include corresponding Business Process entity “{1}”. If this is a newly created Business Process in Draft state, activate it once to generate the Business Process entity and include it in the solution. For more information, see http://support.microsoft.com/kb/4337537.|
> |InvalidExternalCollectionName|0x80046BA7, -2147193945|The specified External Collection name is not valid.|
> |InvalidExternalName|0x80046BC0, -2147193920|The specified External name is not valid.|
> |InvalidExternalPartyConfiguration|0x8006110F, -2147086065|Multiple External Party Items are present for request parameters.|
> |InvalidExternalPartyOperation|0x80061111, -2147086063|External Party is not allowed.|
> |InvalidExternalPartyParent|0x80061110, -2147086064|External Party has invalid parent attribute.|
> |InvalidFeatureType|0x80044272, -2147204494|The feature type isn’t valid.|
> |InvalidFetchCollection|0x8004E019, -2147164135|The fetch collection for the visualization is invalid.|
> |InvalidFetchXml|0x80040303, -2147220733|Malformed FetchXml.|
> |InvalidFileAttributeName|0x80090007, -2146893817|Invalid File Attribute Name: [{0}].|
> |InvalidFileBadCharacters|0x80040396, -2147220586|The file could not be uploaded because it contains invalid character(s)|
> |InvalidFileRangeRequested|0x80090000, -2146893824|Chunk range used in this call is either not valid or it is bigger than allowed {0} MB.|
> |InvalidFileType|0x800608CC, -2147088180|Invalid File Type.|
> |InvalidFilterCriteriaForVisualization|0x8004E01E, -2147164130|The visualization cannot be rendered for the given filter criteria.|
> |InvalidFiscalPeriod|0x80044814, -2147203052|The fiscal period {0} does not fall in the permitted range of fiscal periods as per organization's fiscal settings.|
> |InvalidFlowProcessClientData|0x80060468, -2147089304|Flow clientdata is in invalid format. Details: "{0}".|
> |InvalidFormatForControl|0x80060875, -2147088267|Invalid Precision Parameter specified for control {0}. It Dosent Contain Expected Value|
> |InvalidFormatForDataDelimiter|0x80040355, -2147220651|Mismatched data delimiter: only one delimiter was found.|
> |InvalidFormatForUpdateMode|0x8004F601, -2147158527|The file that you uploaded is invalid and cannot be used for updating records.|
> |InvalidFormatParameters|0x80047101, -2147192575|The number of format parameters passed into the input string is incorrect|
> |InvalidFormType|0x8004E306, -2147163386|The type of the form must be set to {0} in the Form XML.|
> |InvalidFormTypeCalledThroughSdk|0x80060874, -2147088268|"Invalid Formtype used in Create call|
> |InvalidForOfficeGraph|0x80044231, -2147204559|One or both entities are not enabled for officegraph and they cannot be used for officegraph.|
> |InvalidGoalAttribute|0x8004480b, -2147203061|Goal Attribute does not match the specified metric type.|
> |InvalidGoalManager|0x8004F684, -2147158396|The manager of a goal can only be a user and not a team.|
> |InvalidGranularityValue|0x8004B038, -2147176392|The Granularity column value is incorrect. Each rule part must be a name-value pair separated by an equal sign (=). For example: FREQ=Minutes;INTERVAL=15|
> |InvalidGroupByAlias|0x8004E00F, -2147164145|Data Description is invalid. Same group by alias cannot be used for different attributes.|
> |InvalidGroupByColumn|0x8004E01D, -2147164131|Group by not allowed on the attribute.|
> |InvalidGuid|0x80040363, -2147220637|The globally unique identifier (GUID) in this row is invalid|
> |InvalidGuidInXaml|0x80060407, -2147089401|Guid - {0} in the Xaml is not valid|
> |InvalidHeaderColumn|0x80040344, -2147220668|The column heading contains an invalid combination of data delimiters.|
> |InvalidHexColorValue|0x800608D0, -2147088176|Only hexadecimal values are allowed.|
> |InvalidHierarchicalRelationship|0x8004701F, -2147192801|This relationship is not self-referential and therefore cannot be made hierarchical.|
> |InvalidHierarchicalRelationshipChange|0x8004701a, -2147192806|You can’t change this entity’s hierarchy because the {0} hierarchical relationship can’t be customized.|
> |InvalidIconFileFormatForConnector|0x80072603, -2147015165|Invalid icon file format. Supported formats are PNG and JPG.|
> |InvalidImportFileContent|0x80040374, -2147220620|The content of the import file is not valid. You must select a text file.|
> |InvalidImportFileData|0x80040351, -2147220655|The data is not in the required format|
> |InvalidImportFileParseData|0x80040349, -2147220663|Field and data delimiters for this file are not specified.|
> |InvalidImportJobId|0x80044252, -2147204526|The requested importjob does not exist.|
> |InvalidImportJobTemplateFile|0x80044251, -2147204527|The ImportJobTemplate.xml file is invalid.|
> |InvalidIncomingDeliveryExpectingEmailConnector|0x8005E224, -2147098076|The incoming delivery method is not email connector. To receive mails its incoming delivery method should be Email Connector.|
> |InvalidInputArgumentForModernFlowExecute|0x80060480, -2147089280|Cannot execute Modern Flow '{0}' because '{1}' is not a supported input argument.|
> |InvalidInstanceEntityName|0x8004E10D, -2147163891|Invalid instance entity name.|
> |InvalidInstanceTypeCode|0x8004E107, -2147163897|Invalid instance type code.|
> |InvalidInteractiveUserQuota|0x8004B049, -2147176375|You have reached the maximum number of interactive/full users.|
> |InvalidIntersectEntity|0x80072540, -2147015360|Cannot use existing non intersect entity {0} as an intersect entity for defining many to many relationships.|
> |InvalidInvitationLiveId|0x8004D20E, -2147167730|A user with this e-mail address was not found. Sign in to Windows Live ID with the same e-mail address where you received the invitation.  If you do not have a Windows Live ID, please create one using that e-mail address.|
> |InvalidInvitationToken|0x8004D20D, -2147167731|The invitation token {0} is not correctly formatted.|
> |InvalidIsFirstRowHeaderForUseSystemMap|0x80040364, -2147220636|The first row of the file does not contain column headings.|
> |InvalidIsoCurrencyCode|0x80048cf2, -2147185422|Invalid ISO currency code.|
> |InvalidKeyQuery|0x80072529, -2147015383|Keys must be part of the requested EntityMetadata properties when a KeyQuery is specified. Expect property = {0} in requested entity properties list.|
> |InvalidKit|0x80043afd, -2147206403|The product is not a kit.|
> |InvalidKitProduct|0x80043afe, -2147206402|You cannot add a product kit to itself. Select a different product or product kit.|
> |InvalidLanguageCode|0x80044195, -2147204715|The specified language code is not valid for this organization.|
> |InvalidLanguageForCreate|0x80060750, -2147088560|Rows with localizable attributes can only be created when the user interface (UI) language for the current user is set to the organization's base language.|
> |InvalidLanguageForProcessConfiguration|0x8005E102, -2147098366|Process configuration is not available since your language does not match system base language.|
> |InvalidLanguageForSolution|0x80047019, -2147192807|Solution and Publisher Options are not available since your language does not match system base language.|
> |InvalidLanguageForUpdate|0x80060751, -2147088559|Localizable attributes can only be updated via the string property when the user interface (UI) language for the current user is set to the organization's base language. Use SetLocLabels to update the localized values for the following attributes: [{0}].|
> |InvalidLicenseCannotReadMpcFile|0x8004D245, -2147167675|Invalid license. MPC code cannot be read from MPC.txt file with this path {0}.|
> |InvalidLicenseKey|0x8004D240, -2147167680|Invalid license key ({0}).|
> |InvalidLicenseMpcCode|0x8004D246, -2147167674|Invalid license. Invalid MPC code ({0}).|
> |InvalidLicensePid|0x8004D242, -2147167678|Invalid license. Invalid PID (Product Id) ({0}).|
> |InvalidLicensePidGenCannotLoad|0x8004D243, -2147167677|Invalid license. PidGen.dll cannot be loaded from this path {0}|
> |InvalidLicensePidGenOtherError|0x8004D244, -2147167676|Invalid license. Cannot generate PID (Product Id) from License key. PidGen error code ({0}).|
> |InvalidLocaleIdForKnowledgeArticle|0x80061400, -2147085312|Language with Locale ID {0}, does not exist|
> |InvalidLogoImageId|0x800608D3, -2147088173|Invalid logo image web resource id.|
> |InvalidLogoImageWebResourceType|0x800608D9, -2147088167|Invalid WebResource Type for Logo Image.|
> |InvalidLookupMapNode|0x80048481, -2147187583|The lookup entity provided is not valid for the given target attribute.|
> |InvalidMailbox|0x8005E217, -2147098089|Invalid mailboxId passed in. Please check the mailboxid.|
> |InvalidManagedPropertyException|0x8004F030, -2147160016|Managed property {0} does not contain enough information to be created.  Please provide (assembly, class), or (entity, attribute) or set the managed property to custom.|
> |InvalidManifestFilePath|0x80048533, -2147187405|Failed to locate the manifest file in the specified location|
> |InvalidMatchingAttributeError|0x80044244, -2147204540|Invalid Matching attribute.|
> |InvalidMaximumResourceLimit|0x8004B02B, -2147176405|The resource type {0} cannot have a maximum limit of {1}.|
> |InvalidMaxLengthForControl|0x80060879, -2147088263|Invalid MaxLength Parameter specified for control {0}.Maxlength must be in between {1} and {2}.|
> |InvalidMaxSizeInKB|0x80090009, -2146893815|Invalid size for file type attribute. Valid size should be between [0-{0}] KB|
> |InvalidMaxValueForControl|0x8006087B, -2147088261|Invalid MaxValue Parameter specified for control {0}.Max Value must be in between {1} and {2}.|
> |InvalidMeasureCollection|0x8004E00A, -2147164150|Measure collection is invalid. Not all the measures in the measure collection have the same group bys.|
> |InvalidMetadata|0x8004023a, -2147220934|Invalid Metadata.|
> |InvalidMetadataSqlOperation|0x80072343, -2147015869|SQL exception has been thrown on current metadata operation. Please check the exception for more details.|
> |InvalidMigrationFileContent|0x8005F033, -2147094477|The content of the import file is not valid. You must select a text file.|
> |InvalidMinAndMaxValueForControl|0x8006087C, -2147088260|Invalid MinValue and MaxValue Parameter specified for control {0}.Min Value must be less than Max Value.|
> |InvalidMinimumResourceLimit|0x8004B02A, -2147176406|The resource type {0} cannot have a minimum limit of {1}.|
> |InvalidMinValueForControl|0x8006087A, -2147088262|Invalid MinValue Parameter specified for control {0}.Min Value must be in between {1} and {2}.|
> |InvalidMobileOfflineFiltersFetchXml|0x80071113, -2147020525|XML Format mismatch. Check for the correctness of XML.|
> |InvalidMultipleMapping|0x80048498, -2147187560|A source field is mapped to more than one Dynamics 365 fields of lookup/picklist type.|
> |InvalidMultipleSiteMapReferenceSingleAppModule|0x80050111, -2147155695|An app can’t have multiple site maps.|
> |InvalidNamePrefix|0x80044366, -2147204250|The schema name {0} for type {2} is invalid or missing.Custom attribute, entity, entitykey, option set and relationship names must start with a valid customization prefix.The prefix for a solution component should match the prefix that is specified for the publisher of the solution.|
> |InvalidNetPrice|0x800404f3, -2147220237|The net price is invalid|
> |InvalidNonInteractiveUserQuota|0x8004B050, -2147176368|You have reached the maximum number of non-interactive users/|
> |InvalidNumberGroupFormat|0x80043700, -2147207424|Invalid input string for numbergroupformat. The input string should contain an array of integers. Every element in the value array should be between one and nine, except for the last element, which can be zero.|
> |InvalidNumberOfCardFormSections|0x80061505, -2147085051|Number of sections in a card form must be 4. Found {0}.|
> |InvalidNumberOfParametersForFileUpload|0x80090002, -2146893822|Invalid number of parameters [{0}] provided in request URL.|
> |InvalidNumberOfPartitions|0x8004E200, -2147163648|You cannot delete audit data in the partitions that are currently in use, or delete the partitions that are created for storing future audit data.|
> |InvalidNumberOfReferencePanelSections|0x80061504, -2147085052|MainInteractionCentric form can have only 1 reference panel section. Found {0}.|
> |InvalidNumberOfSectionsInTab|0x80060872, -2147088270|A dialog Form XML cannot contain more than one section.|
> |InvalidNumberOfTabsInDialog|0x80060871, -2147088271|A dialog Form XML cannot contain more than one tab.|
> |InvalidOAuthToken|0x80041d50, -2147214000|The OAuth token is invalid|
> |InvalidObjectTypeCode|0x80072005, -2147016699|Object type code {0} cannot be found. Is Metadata: {1}|
> |InvalidObjectTypes|0x8004021f, -2147220961|Invalid object type.|
> |InvalidOccurrenceNumber|0x8004E125, -2147163867|The effective end date of the series cannot be earlier than today. Select a valid occurrence number.|
> |InvalidOfflineOperation|0x8004410e, -2147204850|Operation not valid when offline.|
> |InvalidOneToManyRelationship|0x80072500, -2147015424|OneToMany Entity Relationship with EntityRelationshipId '{0}' has null ReferencingEntityRole|
> |InvalidOneToManyRelationshipForRelatedEntitiesQuery|0x8004430F, -2147204337|An invalid OneToManyRelationship has been specified for RelatedEntitiesQuery. Referenced Entity {0} should be the same as primary entity {1}|
> |InvalidOperandOnLeftHandSide|0x80072501, -2147015423|The left side of the '{0}' operator must be a property of the entity.|
> |InvalidOperation|0x8004023b, -2147220933|Invalid Operation performed.|
> |InvalidOperationForClosedOrCancelledCampaignActivity|0x80040314, -2147220716|Can not add items to closed (cancelled) campaignactivity.|
> |InvalidOperationForDynamicList|0x8004F701, -2147158271|This action is not available for a dynamic marketing list.|
> |InvalidOperationWhenBusinessRuleIsActive|0x80060015, -2147090411|Invalid  operation - You cannot activate or deactivate this business rule|
> |InvalidOperationWhenListIsNotActive|0x8004033a, -2147220678|List is not active. Cannot perform this operation.|
> |InvalidOperationWhenListLocked|0x80040302, -2147220734|List is Locked. Cannot perform this action.|
> |InvalidOperationWhenPartyIsNotActive|0x8004033b, -2147220677|The party is not active. Cannot perform this operation.|
> |InvalidOperatorCode|0x80048415, -2147187691|The operator is not valid or it is not supported.|
> |InvalidOperatorCodeError|0x80044253, -2147204525|Invalid operator code.|
> |InvalidOptionSetIdForControl|0x80060876, -2147088266|An invalid OptionSetId specified for control {0}.OptionSet Id is an non-empty Guid.|
> |InvalidOptionSetNameChange|0x80048409, -2147187703|Cannot update OptionSet Name {0}, Id: {1} because OptionSet name provided value ({2}) is in use by another existing OptionSet (id: {3})|
> |InvalidOptionSetOperation|0x80048403, -2147187709|Invalid OptionSet|
> |InvalidOptionSetSchemaName|0x80044345, -2147204283|An OptionSet with the specified name already exists. Please specify a unique name.|
> |InvalidOrEmptyRelationshipId|0x80071122, -2147020510|The RelationshipId of Mobile profile item association is invalid or empty.|
> |InvalidOrganizationFriendlyName|0x8004D252, -2147167662|Invalid organization friendly name ({0}). Reason: ({1})|
> |InvalidOrganizationId|0x80044248, -2147204536|The Organization ID present in the translations file does not match the current Organization ID.|
> |InvalidOrganizationSettings|0x8006110D, -2147086067|Organization Settings are not properly configured for External Party.|
> |InvalidOrganizationUniqueName|0x8004D251, -2147167663|Invalid organization unique name ({0}). Reason: ({1})|
> |InvalidOrgDBOrgSetting|0x80048514, -2147187436|Invalid Organization Setting passed in: {0}. Please check the datatype and pass in an appropriate value.|
> |InvalidOrgOwnedCascadeLinkType|0x80044156, -2147204778|Cascade User-Owned is not a valid cascade link type for org-owned entity relationships.|
> |InvalidOtherDataFilterOptions|0x8006098D, -2147087987|You should select at least one option from Download My Records, My Team Records or My Business Unit's Records for Other Data Filter|
> |InvalidOutgoingDeliveryExpectingEmailConnector|0x8005E226, -2147098074|The outgoing delivery method is not email connector. To send mails its outgoing delivery method should be Email Connector.|
> |InvalidOwnerID|0x80040229, -2147220951|The owner ID is invalid or missing.|
> |InvalidOwnershipTypeMask|0x8004700d, -2147192819|The specified ownership type mask is not valid for this operation|
> |InvalidPageResponse|0x8004E00D, -2147164147|Invalid Page Response generated.|
> |InvalidParameterForFileOperation|0x80090003, -2146893821|Invalid parameter [{0}] provided in request URL.|
> |InvalidParent|0x80040205, -2147220987|The parent object is invalid or missing.|
> |InvalidParentChildCascadeBehavior|0x8007200D, -2147016691|Parent-Child relationship {0} requires parental cascade behavior.|
> |InvalidParentChildRelationshipUpdate|0x8007200B, -2147016693|You cannot update relationship of type ParentChild.|
> |InvalidParentDraftState|0x80042302, -2147212542|For a record in the Draft status, only an Under Revision, Draft, or Active record can be selected as its parent.|
> |InvalidParentId|0x80040206, -2147220986|The parent id is invalid or missing.|
> |InvalidParentURState|0x80042303, -2147212541|For a record in the Under Revision status, only an Under Revision or Active record can be selected as its parent.|
> |InvalidPartnerSolutionCustomizationProvider|0x8004A109, -2147180279|Invalid partner solution customization provider type|
> |InvalidPartyMapping|0x80043515, -2147207915|Invalid party mapping.|
> |InvalidPicklistUpdate|0x80090417, -2146892777|"Can't update '{0}' of optionset '{1}', For 'Picklist' and 'Status' options, only ParentValues can be updated."|
> |InvalidPluginAssemblyContent|0x8004418b, -2147204725|Plug-in assembly does not contain the required types or assembly content cannot be updated.|
> |InvalidPluginAssemblyVersion|0x8004417B, -2147204741|Plug-in assembly fullnames must be unique (ignoring the version build and revision number).|
> |InvalidPluginRegistrationConfiguration|0x80044170, -2147204752|The plug-in assembly registration configuration is invalid.|
> |InvalidPluginStrongNameRequired|0x80081114, -2146954988|Plug-in assembly is not strong name signed.|
> |InvalidPluginTypeImplementation|0x8004418c, -2147204724|Plug-in type must implement exactly one of the following classes or interfaces: Microsoft.Crm.Sdk.IPlugin, Microsoft.Xrm.Sdk.IPlugin, System.Activities.Activity and System.Workflow.ComponentModel.Activity.|
> |InvalidPointer|0x80040218, -2147220968|The object is disposed.|
> |InvalidPostponeUntilTimeForModernFlowExecute|0x80060478, -2147089288|Cannot execute Modern Flow '{0}' because '{1}' is not in a supported DateTimeOffset format.|
> |InvalidPrecisionForControl|0x8006087D, -2147088259|Invalid Precision Parameter specified for control {0}.Precision must be in between {1} and {2}.|
> |InvalidPrefixInConnectorName|0x80072605, -2147015163|Connector name must start with a alphanumeric prefix with length between 2~8 and followed by  '_' and alphanumeric name.|
> |InvalidPresentationDescription|0x8004E002, -2147164158|The presentation description is invalid.|
> |InvalidPreviewModeOperation|0x8005f219, -2147093991|You can’t perform this operation in preview mode.|
> |InvalidPriceLevelCurrencyForPricingMethod|0x80048cf9, -2147185415|The currency of the price list needs to match the currency of the product for pricing method percentage.|
> |InvalidPricePerUnit|0x80043b10, -2147206384|The price per unit is invalid.|
> |InvalidPrimaryContactBasedOnAccount|0x8004F864, -2147157916|The specified contact doesn't belong to the account selected as the customer. Specify a contact that belongs to the selected account, and then try again.|
> |InvalidPrimaryContactBasedOnContact|0x8004F865, -2147157915|The specified contact doesn't belong to the contact that was specified in the customer field. Remove the value from the contact field, or select a contact associated to the selected customer, and then try again.|
> |InvalidPrimaryFieldForActivity|0x8004F127, -2147159769|A custom entity defined as an activity cannot have primary attribute other than subject.|
> |InvalidPrimaryFieldType|0x8004700e, -2147192818|Primary UI Attribute has to be of type String|
> |InvalidPrimaryKey|0x80040266, -2147220890|Invalid primary key.|
> |InvalidPrincipalId|0x80048348, -2147187896|Passed Guid is empty.|
> |InvalidPrincipalType|0x80048346, -2147187898|Invalid Principal Type passed.|
> |InvalidPriv|0x8004024b, -2147220917|Invalid privilege type.|
> |InvalidPrivilegeDepth|0x8004140b, -2147216373|Invalid privilege depth.|
> |InvalidProcessControlAttribute|0x8005E105, -2147098363|The process control definition contains an invalid attribute.|
> |InvalidProcessControlEntity|0x8005E104, -2147098364|The process control definition contains an invalid entity or invalid entity order.|
> |InvalidProcessIdOperation|0x80092001, -2146885631|Invalid operation. Process ID cannot be modified.|
> |InvalidProcessStateData|0x80045049, -2147200951|ProcessState is not valid for given ProcessSession instance.|
> |InvalidProduct|0x80060623, -2147088861|You can't add a product family.|
> |InvalidPublisherUniqueName|0x8004F01C, -2147160036|Publisher uniquename is required.|
> |InvalidPublishOnProtectedComponent|0x8004F014, -2147160044|You cannot publish {0} {1}. Publish cannot be performed when {0} is managed.|
> |InvalidQuantityDecimalCode|0x80043afc, -2147206404|The quantity decimal code is invalid.|
> |InvalidQuery|0x80044183, -2147204733|The query specified for this operation is invalid|
> |InvalidQueryForVirtualEntity|0x80044822, -2147203038|The query specified is not supported for virtual entity.|
> |InvalidRecurrenceInterval|0x8004D2A1, -2147167583|To set recurrence, you must specify an interval that is between 1 and 365.|
> |InvalidRecurrenceIntervalForRollupJobs|0x8004D2A2, -2147167582|To set recurrence, you must specify an interval that should be greater than 1 hour.|
> |InvalidRecurrencePattern|0x8004E100, -2147163904|Invalid recurrence pattern.|
> |InvalidRecurrenceRule|0x80040246, -2147220922|Error in RecurrencePatternFactory.|
> |InvalidRecurrenceRuleForBulkDeleteAndDuplicateDetection|0x8004D2A0, -2147167584|Bulk Delete and Duplicate Detection recurrence must be specified as daily.|
> |InvalidReferencesFound|0x80072032, -2147016654|Invalid references found: {0}|
> |InvalidRegardingObjectTypeCode|0x80040319, -2147220711|The regarding Object Type Code is not valid for the Bulk Operation.|
> |InvalidRegistryKey|0x8004024c, -2147220916|Invalid registry key specified.|
> |InvalidRelationshipAttributeId|0x80090409, -2146892791|Relationship attribute with id '{0}' of relationship with id '{1}' does not exist.|
> |InvalidRelationshipDescription|0x80047003, -2147192829|The specified relationship cannot be created|
> |InvalidRelationshipInMOPIAssociation|0x80060999, -2147087975|This relationship doesn’t exist with the entity selected in the parent profile item.|
> |InvalidRelationshipNameForControl|0x80060877, -2147088265|Relationship Name not specified for control {0}.Relationship Name is an mandatory Field.|
> |InvalidRelationshipQuery|0x80072528, -2147015384|Atleast one of the relationship properties must be part of the requested EntityMetadata properties when a RelationshipQuery is specified.Expect atleast one of property = {0}, {1} or {2} in requested entity properties list.|
> |InvalidRelationshipType|0x8004700f, -2147192817|The specified relationship type is not valid for this operation|
> |InvalidRelationshipTypeForAccessory|0x8004F989, -2147157623|An accessory relationship is always unidirectional and can't be changed.|
> |InvalidRelationshipTypeForUpSell|0x8004F988, -2147157624|An upsell relationship is always unidirectional and can't be changed.|
> |InvalidRelativeUrlFormat|0x80048054, -2147188652|The relative url contains invalid characters. Please use a different name. Valid relative url names cannot ends with the following strings: .aspx, .ashx, .asmx, .svc , cannot begin or end with a dot, cannot contain consecutive dots and cannot contain any of the following characters: ~ " # % & * : < > ? / \ { | }.|
> |InvalidRequestBody|0x80072530, -2147015376|Passed entity object cannot be null or empty.|
> |InvalidRequestDataFormat|0x80044271, -2147204495|The updated configuration includes invalid data.|
> |InvalidRequestParameter|0x80044828, -2147203032|Both name and value should be specified for request parameter.|
> |InvalidRequestParameters|0x8006110E, -2147086066|Request parameters are not valid to server External Party request.|
> |InvalidResourceType|0x8004B029, -2147176407|The requested action is not valid for resource type {0}.|
> |InvalidRestore|0x80040258, -2147220904|RestoreCaller must be called after SwitchToSystemUser.|
> |InvalidRoboticProcessAutomationFlowProcessClientData|0x80060473, -2147089293|Clientdata is in invalid format. Details: "{0}".|
> |InvalidRole|0x8004B012, -2147176430|You have not assigned roles to this user|
> |InvalidRoleOccurrencesForOneToManyRelationship|0x8006089A, -2147088230|There can't be more than two entity relationship roles for a one-to-many relationship {0}.|
> |InvalidRoleTypeForOneToManyRelationship|0x80060899, -2147088231|This relationship role type isn't valid for a one-to-many relationship {0}.|
> |InvalidRollupQueryAttributeSet|0x8004F683, -2147158397|A Rollup Query cannot be set for a Rollup Field that is not defined in the Goal Metric.|
> |InvalidRollupType|0x80040234, -2147220940|The rollup type is invalid.|
> |InvalidS2SAuthentication|0x8005E245, -2147098043|You can use server-to-server authentication only for email server profiles created for a Microsoft Dynamics 365 Online organization that was set up through the Microsoft online services environment (Office 365).|
> |InvalidSchemaName|0x8004700b, -2147192821|An entity with the specified name already exists. Please specify a unique name.|
> |InvalidSearchEntities|0x80060202, -2147089918|Search - {0} did not find any valid Entities.|
> |InvalidSearchEntity|0x80060201, -2147089919|Invalid Search Entity - {0}.|
> |InvalidSearchName|0x80060204, -2147089916|Invalid Search Name - {0}.|
> |InvalidSeriesId|0x8004E105, -2147163899|SeriesId is null or invalid.|
> |InvalidSeriesIdOriginalStart|0x8004E109, -2147163895|Invalid seriesid or original start date.|
> |InvalidSeriesStatus|0x8004E10F, -2147163889|Invalid series status.|
> |InvalidSharee|0x8004020c, -2147220980|Invalid share id.|
> |InvalidSharePointSiteCollectionUrl|0x80048052, -2147188654|The URL must conform to the http or https schema.|
> |InvalidSimilarityRuleStateError|0x80044254, -2147204524|Invalid similarity rule state.|
> |InvalidSingletonResults|0x8004024f, -2147220913|Crm Internal Exception: Singleton Retrieve Query should not return more than 1 record.|
> |InvalidSiteRelativeUrlFormat|0x80048053, -2147188653|The relative url contains invalid characters. Please use a different name. Valid relative url names cannot end with the following strings: .aspx, .ashx, .asmx, .svc , cannot begin or end with a dot or /, cannot contain consecutive dots or / and cannot contain any of the following characters: ~ " # % & * : < > ? \ { | }.|
> |InvalidSolutionAwarenessDeclaration|0x80072000, -2147016704|An entity cannot be declared as solution-aware on an update operation. Entity: {0}|
> |InvalidSolutionComponentKey|0x8007200E, -2147016690|The attribute {0} from key {1} and entity {2} should be exportable to be an export key.|
> |InvalidSolutionConfigurationPage|0x8004701B, -2147192805|The specified configuration page for this solution is invalid.|
> |InvalidSolutionDependencies|0x80072006, -2147016698|All components present in this solution have dependencies. This is not allowed as uninstall of this solution would be unactionable.|
> |InvalidSolutionUniqueName|0x8004F002, -2147160062|Invalid character specified for solution unique name. Only characters within the ranges [A-Z], [a-z], [0-9] or _ are allowed. The first character may only be in the ranges [A-Z], [a-z] or _.|
> |InvalidSolutionVersion|0x8004F01E, -2147160034|An invalid solution version was specified.|
> |InvalidSourceAttributeType|0x80044808, -2147203064|Source Attribute Type does not match the Amount Data Type specified.|
> |InvalidSourceEntityAttribute|0x80044806, -2147203066|Attribute {0} is not an attribute of Entity {1}.|
> |InvalidSourceStateValue|0x80044810, -2147203056|The source state specified for the entity is invalid.|
> |InvalidSourceStatusValue|0x80044811, -2147203055|The source status specified for the entity is invalid.|
> |InvalidSourceType|0x80060437, -2147089353|SourceType {0} isn't valid for the {1} data type.|
> |InvalidSourceTypeCode|0x800608EA, -2147088150|Please select valid property bag for the selected source type.|
> |InvalidStage|0x80060452, -2147089326|Validation error: invalid stage.|
> |InvalidStageTransition|0x80092003, -2146885629|Invalid stage transition. Transition to stage {0} is not in the process active path.|
> |InvalidStageTransitionOnInactiveInstance|0x80060377, -2147089545|Invalid stage transition. Stage transition is not allowed on inactive processes.|
> |InvalidState|0x80040233, -2147220941|The object is not in a valid state to perform this operation.|
> |InvalidStateCodeStatusCode|0x80048408, -2147187704|State code is invalid or state code is valid but status code is invalid for a specified state code.|
> |InvalidStateForPublish|0x8004F90A, -2147157750|The specified ProductFamily, Product or Bundle can only be published from Draft state or ActiveDraft status|
> |InvalidStatePicklistUpdate|0x80090418, -2146892776|"Can't update '{0}' of optionset '{1}', For State Options you can update only DisplayName, Description and DefaultStatusCode."|
> |InvalidStateTransition|0x8004F00E, -2147160050|The {0} (Id={1}) entity or component has attempted to transition from an invalid state: {2}.|
> |InvalidSubmitFromPublishedArticle|0x80048dfa, -2147185158|You are trying to submit an article that has a status of published. You can only submit an article with the status of draft.|
> |InvalidSubmitFromUnapprovedArticle|0x80048dff, -2147185153|You are trying to submit an article that has a status of unapproved. You can only submit an article with the status of draft.|
> |InvalidSubstituteProduct|0x80043aff, -2147206401|A product can't have a relationship with itself.|
> |InvalidSyncDirectionValueForUpdate|0x80060742, -2147088574|The sync direction is invalid as per the allowed sync direction for one or more attribute mappings.|
> |InvalidSyncToken|0x80072515, -2147015403|Invalid Sync Token|
> |InvalidTargetEntity|0x80040369, -2147220631|The specified target record type does not exist.|
> |InvalidTargetEntityTypeForControl|0x80060878, -2147088264|Target Entity Type not specified for control {0}.Target Entity is an mandatory Field.|
> |InvalidTargetFrameworkVersion|0x8004420b, -2147204597|Plug-in assembly targets a version of .NET Framework that is not supported.|
> |InvalidTaskFlow|0x80060392, -2147089518|Task Flow is invalid.|
> |InvalidTemplate|0x8004B010, -2147176432|The Invitation Email template is not valid|
> |InvalidTemplateContent|0x800609B2, -2147087950|The template content is invalid.|
> |InvalidTemplateId|0x80050019, -2147155943|That’s not a valid template.|
> |InvalidTenantIDValue|0x8005E25B, -2147098021|Exchange Online Tenant ID value is not valid.The Field value should be a string in the structure of GUID.|
> |InvalidThemeDeleteOperation|0x800608D7, -2147088169|You can’t delete system or default themes.|
> |InvalidThemeId|0x800608D4, -2147088172|Invalid theme id.|
> |InvalidTimeZoneCode|0x800608F7, -2147088137|Time Zone Code {0} specified is not recognized. Please specify a valid Time Zone Code value.|
> |InvalidToDeleteFileAttachmentBulkDelete|0x8009000A, -2146893814|File Attachment bulk delete jobs cannot be deleted.|
> |InvalidToken|0x8004B061, -2147176351|The token is invalid.|
> |InvalidTotalDiscount|0x800404f4, -2147220236|The total discount is invalid|
> |InvalidTotalPrice|0x800404f5, -2147220235|The total price is invalid|
> |InvalidTransformationParameter|0x80040389, -2147220599|A parameter for the transformation is either missing or invalid.|
> |InvalidTransformationParameterDataType|0x80040380, -2147220608|The data type of one or more of the transformation parameters is unsupported.|
> |InvalidTransformationParameterEmptyCollection|0x80048511, -2147187439|The transformation parameter: {0} has an invalid input value length: {1}. The parameter length cannot be an empty collection.|
> |InvalidTransformationParameterMapping|0x80040382, -2147220606|The transformation parameter mapping defined is invalid. Check that the target attribute name exists.|
> |InvalidTransformationParameterMappings|0x8004037c, -2147220612|One or more transformation parameter mappings are invalid or do not match the transformation parameter description.|
> |InvalidTransformationParameterOutsideRange|0x80048510, -2147187440|The transformation parameter: {0} has an invalid input value: {1}. The parameter is out of the permissible range: {2}. |
> |InvalidTransformationParameterOutsideRangeGeneric|0x80048512, -2147187438|One or more input transformation parameter values are outside the permissible range: {0}.|
> |InvalidTransformationParametersGeneric|0x80048507, -2147187449|The transformation parameter: {0} has an invalid input value: {1}. The parameter must be of type: {2}.|
> |InvalidTransformationParameterString|0x80048508, -2147187448|The transformation parameter: {0} has an invalid input value: {1}. The parameter must be a string that is not empty.|
> |InvalidTransformationParameterZeroToRange|0x80048509, -2147187447|The transformation parameter: {0} has an invalid input value: {1}. The parameter value must be greater than 0 and less than the length of the parameter 1.|
> |InvalidTransformationType|0x8004037a, -2147220614|The specified transformation type is not supported.|
> |InvalidTranslationsFile|0x80044249, -2147204535|The translations file is invalid or does not confirm to the required schema.|
> |InvalidTraversedPath|0x80092007, -2146885625|Invalid traversed path.|
> |InvalidTypeConversion|0x80090103, -2146893565|Unable to cast {0} with value '{1}' to type {2}.|
> |InvalidUniqueName|0x80060386, -2147089530|Invalid unique name for action.|
> |InvalidUnpublishFromDraftArticle|0x80048dfc, -2147185156|You are trying to unpublish an article that has a status of draft. You can only unpublish an article with the status of published.|
> |InvalidUnpublishFromUnapprovedArticle|0x80048dfe, -2147185154|You are trying to unpublish an article that has a status of unapproved. You can only unpublish an article with the status of publish.|
> |InvalidUpdateOnProtectedComponent|0x8004F012, -2147160046|You cannot update {0} {1}. Updates cannot be performed when {0} is managed.|
> |InvalidUrlConsecutiveSlashes|0x80048056, -2147188650|The Url contains consecutive slashes which is not allowed.|
> |InvalidUrlProtocol|0x8004E30F, -2147163377|The specified URL is invalid.|
> |InvalidUserAuth|0x80040204, -2147220988|User does not have the privilege to perform this action.|
> |InvalidUserLicenseCount|0x8004B027, -2147176409|Cannot purchase {0} user licenses for the Offering {1}.|
> |InvalidUserName|0x80048095, -2147188587|You must enter the user name in the format <name>@<domain>. Correct the format and try again.|
> |InvalidUserQuota|0x8004B011, -2147176431|You have reached the maximum number of user quota|
> |InvalidUserToImportExcelOnlineFile|0x80060807, -2147088377|You don't have permission to import this file. Only the user who exported this data can import this file.|
> |InvalidUserToViewExcelOnlineFile|0x80060806, -2147088378|You don't have permission to view this file. Only the user who exported this data can view this file.|
> |InvalidValueForCountryCode|0x8004B022, -2147176414|Account Country/Region code must not be {0}|
> |InvalidValueForCurrency|0x8004B023, -2147176413|Account currency code must not be {0}|
> |InvalidValueForDataDelimiter|0x80040341, -2147220671|The data delimiter is invalid.|
> |InvalidValueForFieldDelimiter|0x80040340, -2147220672|The field delimiter is invalid.|
> |InvalidValueForFileType|0x80040348, -2147220664|The file type is invalid.|
> |InvalidValueForLocale|0x8004B024, -2147176412|Account locale code must not be {0}|
> |InvalidValueProcessEmailAfter|0x8005E244, -2147098044|The date in the Process Email From field is earlier than what is allowed for your organization. Enter a date that is later than the one specified, and try again.|
> |InvalidVersion|0x8004023c, -2147220932|Unhandled Version mismatch found.|
> |InvalidViewReference|0x800609B3, -2147087949|The view is not specified or is invalid.|
> |InvalidWebResourceForVisualization|0x8004E017, -2147164137|The web resource type {0} is not supported for visualizations.|
> |InvalidWebresourceId|0x8005012B, -2147155669|The webresource ID is invalid.|
> |InvalidWebresourceType|0x8005012D, -2147155667|The web resource provided for the app icon is invalid.|
> |InvalidWebToLeadRedirect|0x80048476, -2147187594|The redirectto is invalid for web2lead redirect.|
> |InvalidWelcomePageId|0x8005012C, -2147155668|The welcome page ID is invalid.|
> |InvalidWelcomePageType|0x8005012E, -2147155666|The web resource provided for the app Welcome page is invalid.|
> |InvalidWordDocumentTemplate|0x800608EF, -2147088145|The document template is not valid.|
> |InvalidWordFileType|0x800608EE, -2147088146|The file type isn't supported.|
> |InvalidWordTemplateContent|0x800608FB, -2147088133|The template content is not valid.|
> |InvalidWordXmlFile|0x80048441, -2147187647|Only Microsoft Word xml format files can be uploaded.|
> |InvalidWorkflowOrWorkflowDoesNotExist|0x8006040a, -2147089398|Invalid workflow or workflow does not exist.|
> |InvalidXaml|0x80060417, -2147089385|XAML for workflow is NULL or Empty|
> |InvalidXml|0x80040201, -2147220991|Invalid XML.|
> |InvalidXmlCollectionNameException|0x80040247, -2147220921|Invalid Xml collection name.|
> |InvalidXmlEntityNameException|0x80040248, -2147220920|Invalid Xml entity name.|
> |InvalidXmlForParameters|0x80060410, -2147089392|Parameters node for ControlStep have invalid XML in it|
> |InvalidXmlSSContent|0x80040350, -2147220656|The data file can’t be imported because it contains invalid entity data or it’s in the wrong format. Make sure that the file contains correct data and that it’s in the XML Spreadsheet 2003 format, and then try uploading again.|
> |InvalidXrmSdkReference|0x8004419b, -2147204709|Plug-in assembly references a version of Microsoft.Xrm.Sdk that is higher than the server version|
> |InvalidZipFileForImport|0x80048482, -2147187582|The selected compressed (.zip) file contains files that can't be imported. A .zip file can contain only .xlsx, .csv, or .xml files.|
> |InvalidZipFileFormat|0x80048488, -2147187576|The file that you're trying to upload isn't a valid file. Check the file and try again.|
> |InvitationBillingAdminUnknown|0x8004D213, -2147167725|You are not a billing administrator for this organization and therefore, you cannot send invitations.  You can either contact your billing administrator and ask him or her to send the invitation, or the billing administrator can visit https://billing.microsoft.com and make you a delegate billing administrator. You can then send invitations.|
> |InvitationCannotBeReset|0x8004D210, -2147167728|The invitation for the user cannot be reset.|
> |InvitationIsAccepted|0x8004D208, -2147167736|{0} -- Invitation has already been accepted -- Token={1} Puid={2} Id={3} Status={4}|
> |InvitationIsExpired|0x8004D207, -2147167737|{0} -- Invitation is expired -- Token={1} Puid={2} Id={3} Status={4}|
> |InvitationIsRejected|0x8004D209, -2147167735|{0} -- Invitation has already been rejected by the new user-- Token={1} Puid={2} Id={3} Status={4}|
> |InvitationIsRevoked|0x8004D20A, -2147167734|{0} -- Invitation has been revoked by the organization -- Token={1} Puid={2} Id={3} Status={4}|
> |InvitationNotFound|0x8004D204, -2147167740|{0} -- Invitation not found or status is not Open -- Token={1} Puid={2} Id={3} Status={4}|
> |InvitationOrganizationNotEnabled|0x8004D217, -2147167721|The organization for the invitation is not enabled.|
> |InvitationSendToSelf|0x8004D20F, -2147167729|The invitation cannot be sent to yourself.|
> |InvitationStatusError|0x8004D20C, -2147167732|"The invitation has status {0}."|
> |InvitationWrongUserOrgRelation|0x8004D206, -2147167738|{0} -- The pre-created userorg relation {1} is wrong.  Authentication {2} is already used by another user|
> |InvitedUserAlreadyAdded|0x8004D205, -2147167739|{0} -- The crm user {1} is already added, but to organization {2} instead of the inviting organization {3}|
> |InvitedUserAlreadyExists|0x8004D202, -2147167742|{0} -- Invited user is already in an organization -- {1}|
> |InvitedUserIsOrganization|0x8004D203, -2147167741|{0} -- The user {1} has authentication {2} and is already related to organization {3} with relation id {4}|
> |InvitedUserMultipleTimes|0x8004D20B, -2147167733|The Dynamics 365 user {0} has been invited multiple times.|
> |InvitingOrganizationNotFound|0x8004D200, -2147167744|{0} -- Inviting organization not found -- {1}|
> |InvitingUserNotInOrganization|0x8004D201, -2147167743|{0} -- Inviting user is not in the inviting organization -- {1}|
> |IsKitCannotBeNull|0x80044158, -2147204776|Attribute iskit cannot be null|
> |IsNotLiveToSendInvitation|0x8004B009, -2147176439|This functionality is not supported, its only available for Online solution.|
> |IsvAborted|0x80040265, -2147220891|ISV code aborted the operation.|
> |IsvAbortedForbidden|0x80048d06, -2147185402|ISV code aborted the operation.|
> |IsvAbortedNotFound|0x80048d02, -2147185406|ISV code aborted the operation.|
> |IsvAbortedRequestTimeout|0x80048d07, -2147185401|ISV code aborted the operation.|
> |IsvAbortedServiceUnavailable|0x80048d03, -2147185405|ISV code aborted the operation.|
> |IsvAbortedTooManyRequests|0x80048d04, -2147185404|ISV code aborted the operation.|
> |IsvAbortedUnauthorized|0x80048d05, -2147185403|ISV code aborted the operation.|
> |IsvExtensionsPrivilegeNotPresent|0x80048029, -2147188695|To import ISV.Config, your user account must be associated with a security role that includes the ISV Extensions privilege.|
> |IsvTransactionCount|0x8009000C, -2146893812|ISV code reduced the open transaction count. Custom plug-ins should not catch exceptions from OrganizationService calls and continue processing.|
> |IsvUnExpected|0x80040224, -2147220956|An unexpected error occurred from ISV code.|
> |JobNameIsEmptyOrNull|0x80048457, -2147187625|Job Name can not be null or empty.|
> |KBInvalidCreateAssociation|0x80060861, -2147088287|This KB article is already linked to the {0}.|
> |KeyAlreadyExists|0x80090109, -2146893559|The Key = '{0}' already exists in the dictionary. Cannot add duplicate key.|
> |KnowledgeSearchActiveModelsAlreadyExist|0x80061680, -2147084672|An active configuration already exists for source entity {0}. Only one active configuration is allowed per source entity.|
> |LabelIdDoesNotMatchStepId|0x80060419, -2147089383|The label ID {0} doesn’t match the step ID {1}.|
> |LanguageProvisioningSrsDataConnectorNotInstalled|0x8004F710, -2147158256|The Microsoft Dynamics 365 Reporting Extensions must be installed before the language can be provisioned for this organization.|
> |LastPolymorphicRelationshipCannotBeDeleted|0x80090420, -2146892768|The relationship '{0}' is required by the '{1}' polymorphic lookup attribute and can't be deleted. The relationship will be removed when the polymorphic lookup attribute is deleted.|
> |LayerDesiredOrderFCBIsOff|0x8004F057, -2147159977|The LayerDesiredOrder parameter is present in the import request but the feature flag that allows it to be used is not enabled.|
> |LayerDesiredOrderHintDiffFormOnBase|0x8004F055, -2147159979|The LayerDesiredOrder parameter contains a value that will cause form [{0}] to become the base, but the Form in the incoming solution is not a full Form. This error indicates unexpected order on the layers for this Form.|
> |LayerDesiredOrderHintTypeNotAvailable|0x8004F054, -2147159980|The LayerDesiredOrder parameter contains a type attribute [{0}] that is not available for use. The only type currently suported is 'below'.|
> |LayerDesiredOrderInvalidLayerState|0x8004F051, -2147159983|There was a match for a solution in the LayerDesiredOrder parameter but it is not possible to honor it, due to unexpected layers for the component [{0}], id [{1}]. The layer state is: [{2}].|
> |LayerDesiredOrderInvalidXML|0x8004F049, -2147159991|The LayerDesiredOrder parameter contains an invalid XML schema.|
> |LayerDesiredOrderInvalidXMLDetail|0x8004F050, -2147159984|The LayerDesiredOrder parameter contains an invalid XML schema. Check the property [{0}].|
> |LayerDesiredOrderNotAllowedOnPatch|0x8004F052, -2147159982|The LayerDesiredOrder parameter cannot be used when importing a Patch. The parameter can only be used while importing a solution.|
> |LayerDesiredOrderNotSamePublisher|0x8004F048, -2147159992|The solution [{0}] was used in the LayerDesiredOrder parameter, but its publisher [{1}] does not match the publisher of the solution being installed: [{2}]. This parameter can be used only by solutions from the same publisher.|
> |LayerDesiredOrderNotWhitelist|0x8004F065, -2147159963|The LayerDesiredOrder parameter is present in the import request of [{0}], but this solution is not allowed to use it. Solutions must be whitelisted to use this feature.|
> |LayerDesiredOrderPendingUpgrade|0x8004F047, -2147159993|The solution [{0}] used in LayerDesiredOrder parameter has a pending upgrade. Please complete its upgrade before retrying this operation.|
> |LayerDesiredOrderPublisherNotAllowed|0x8004F056, -2147159978|The publisher [{0}] is not allowed to use the LayerDesiredOrder parameter.|
> |LayerDesiredOrderRestrictedSolution|0x8004F058, -2147159976|The LayerDesiredOrder parameter cannot be used on [{0}].|
> |LeadAlreadyInClosedState|0x80040519, -2147220199|The lead is already closed.|
> |LeadAlreadyInOpenState|0x80040518, -2147220200|The lead is already in the open state.|
> |LegacyWorkflowExpressionMethodNotYetSupportedForAutomaticConversion|0x80060483, -2147089277|Async Workflow '{0}' cannot be converted because expression method '{1}' is currently not supported for automatic conversion.|
> |LegacyWorkflowExpressionNotYetSupportedForAutomaticConversion|0x80060486, -2147089274|Async Workflow '{0}' cannot be converted because expressions of type '{1}' are currently not supported for automatic conversion.|
> |LegacyWorkflowExpressionOperatorNotYetSupportedForAutomaticConversion|0x80060482, -2147089278|Async Workflow '{0}' cannot be converted because because expression operator '{1}' is currently not supported for automatic conversion.|
> |LegacyWorkflowExpressionParameterTypeNotYetSupportedForAutomaticConversion|0x80060484, -2147089276|Async Workflow '{0}' cannot be converted because expression parameters of type '{1}' are currently not supported for automatic conversion.|
> |LegacyWorkflowStepNotYetSupportedForAutomaticConversion|0x80060481, -2147089279|Async Workflow '{0}' cannot be converted because step type '{1}' is currently not supported for automatic conversion.|
> |LegacyWorkflowWithNoTriggersNotYetSupportedForAutomaticConversion|0x80060485, -2147089275|Async Workflow '{0}' cannot be converted because converting workflows with no trigger conditions is not yet supported.|
> |LegacyXlsxFileNotSupported|0x800608CF, -2147088177|Legacy .xlsx files cannot be used for Excel Templates.|
> |LicenseConfigFileInvalid|0x8004D250, -2147167664|The provided configuration file {0} has invalid formatting.|
> |LicenseNotEnoughToActivate|0x80042f14, -2147209452|There are not enough licenses available for the number of users being activated.|
> |LicenseRegistrationExpired|0x8004415d, -2147204771|The registration period for Microsoft Dynamics 365 has expired.|
> |LicenseTampered|0x8004415f, -2147204769|The licensing for this installation of Microsoft Dynamics 365 has been tampered with. The system is unusable. Please contact Microsoft Product Support Services.|
> |LicenseTrialExpired|0x8004415c, -2147204772|The trial installation of Microsoft Dynamics 365 has expired.|
> |LicenseUpgradePathNotAllowed|0x8004D247, -2147167673|Cannot upgrade to specified license type.|
> |LinkedEntitiesAreNotAllowed|0x80071120, -2147020512|Linked Entities Are Not Allowed in the filter|
> |LiveAdminUnknownCommand|0x8004D239, -2147167687|Unknown administration command {0}|
> |LiveAdminUnknownObject|0x8004D238, -2147167688|Unknown administration target {0}|
> |LivePlatformEmailInvalidBody|0x8004B524, -2147175132|The "Body" parameter is blank or null|
> |LivePlatformEmailInvalidFrom|0x8004B522, -2147175134|The "From" parameter is blank or null|
> |LivePlatformEmailInvalidSubject|0x8004B523, -2147175133|The "Subject" parameter is blank or null|
> |LivePlatformEmailInvalidTo|0x8004B521, -2147175135|The "To" parameter is blank or null|
> |LivePlatformGeneralEmailError|0x8005B520, -2147109600|An Email Error Occurred|
> |LocalDataSourceAbortError|0x80072453, -2147015597|The browser operation stopped. Please try again.|
> |LocalDataSourceDatabaseError|0x80072455, -2147015595|The browser operation failed due to browser database errors. Please try again. If it doesn’t work, try the same operation again by ensuring that your device remains unlocked until the operation completes.|
> |LocalDataSourceError|0x80072451, -2147015599|The operation failed. Please try again.|
> |LocalDataSourceQuotaExceededError|0x80072452, -2147015598|The operation failed because there was not enough space in the browser storage quota or the browser storage quota was reached, and the user declined to provide more space to the browser database.|
> |LocalDataSourceTimeOutError|0x80072454, -2147015596|The operation timed out. Please try again.|
> |LockStatusNotValidForDynamicList|0x8004F703, -2147158269|Lock Status cannot be specified for a dynamic list.|
> |LogoImageNodeDoesNotExist|0x800608D2, -2147088174|Logo Image node in organization cache theme data doesnot exist.|
> |LongParseRow|0x80040372, -2147220622|The row is too long to import|
> |LookupNotFound|0x80040353, -2147220653|The lookup reference could not be resolved|
> |LowerVersionUpgrade|0x80048541, -2147187391|The import solution must have a higher version than the existing solution it is upgrading.|
> |LowQuantityGreaterThanHighQuantity|0x80043b01, -2147206399|Low quantity should be less than high quantity.|
> |LowQuantityLessThanZero|0x80043b00, -2147206400|Low quantity should be greater than zero.|
> |MailApp_AppModuleDashboardFormInactive|0x80061227, -2147085785|App for Outlook Dashboard form is inactive.|
> |MailApp_AppModuleDashboardFormMissing|0x80061223, -2147085789|App for Outlook Dashboard form is missing.|
> |MailApp_AppModuleDashboardFormRoleNotAssigned|0x80061228, -2147085784|User does not have access to the App for Outlook Dashboard.|
> |MailApp_AppModulePermission|0x80070004, -2147024892|Сurrent user role does not have required permissions to access App for Outlook|
> |MailApp_AppModuleSitemapDashboardMissing|0x80061224, -2147085788|App for Outlook Dashboard is missing in Site Map.|
> |MailApp_AppModuleSitemapDashboardNotDefault|0x80061225, -2147085787|App for Outlook Dashboard is not set as default in Site Map.|
> |MailApp_AppModuleSitemapMissing|0x80061226, -2147085786|App for Outlook AppModule Site Map is missing|
> |MailApp_AppointmentFeatureNotEnabled|0x80061218, -2147085800|Access to the app hasn’t been enabled for Appointments for this Microsoft Dynamics 365 organization. Contact your system administrator to enable access for appointments.|
> |MailApp_DifferentSecurityZoneError|0x80061210, -2147085808|Try adding the following URLs to your Trusted Sites:{0} {1} {2}|
> |MailApp_EmailAddressMismatch|0x80061211, -2147085807|It looks like you're trying to access the CRM App for Outlook from an email address that we don't recognize. Either sign out and sign in with the email address you use for Dynamics CRM or have your system administrator update your email Mailbox settings to reflect this email address.|
> |MailApp_FeatureControlBitDisabled|0x80061204, -2147085820|Access to the app hasn’t been enabled for this Dynamics 365 organization. Contact your system administrator to enable access to this app.|
> |MailApp_MailboxNotConfiguredWithServerSideSync|0x80061202, -2147085822|Email account isn't configured with server-side synchronization for incoming email|
> |MailApp_MailboxNotConfiguredWithServerSideSyncForACT|0x80061217, -2147085801|Email account isn’t configured with server-side sync for appointments, contacts, and tasks|
> |MailApp_MailboxServerSideSyncConfigurationFailure|0x80061220, -2147085792|Microsoft Dynamics 365 server-side synchronization failed for incoming emails.|
> |MailApp_MailboxServerSideSyncConfigurationFailureForACT|0x80061221, -2147085791|Microsoft Dynamics 365 server-side synchronization failed for appointments.|
> |MailApp_MobileBrowserIsNotSupported|0x80061208, -2147085816|The mobile browser version of Outlook is currently unsupported. Please try again from the Outlook desktop application.|
> |MailApp_PermissionsToReadContactRequired|0x80061219, -2147085799|Can't check to see if the recipients are in Dynamics 365 because user doesn't have sufficient privileges|
> |MailApp_PermissionToUseCrmForOfficeAppsRequired|0x80061205, -2147085819|User doesn't have permission to access app|
> |MailApp_ReadWriteAccessRequired|0x80061203, -2147085821|User only has administrative access to Dynamics 365|
> |MailApp_TrackingIsNotSupported|0x80061207, -2147085817|This version of Outlook doesn't support tracking new emails.|
> |MailApp_UnsupportedBrowser|0x80061201, -2147085823|Your browser is currently unsupported.|
> |MailApp_UnsupportedDevice|0x80061200, -2147085824|Your device is currently unsupported.|
> |MailApp_UserMailboxInactive|0x80061216, -2147085802|User's mailbox is inactive|
> |MailAppLimitedMode|0x80061222, -2147085790|Generic Error when Server-side sync isn't configured properly and MailApp is only allowed to be loaded in LimitedMode|
> |MailboxCannotDeleteEmails|0x8005E233, -2147098061|The Delete Emails after Processing option cannot be set to Yes for user mailboxes.|
> |MailboxCannotModifyEmailAddress|0x8005E208, -2147098104|E-mail Address of a mailbox cannot be updated when associated with an user/queue.|
> |MailboxCredentialNotSpecified|0x8005E209, -2147098103|Username is not specified|
> |MailboxTrackingFolderMappingCannotBeUpdated|0x8006088C, -2147088244|The mailbox tracking folder mapping cannot be updated.|
> |MailboxUnsupportedEmailServerType|0x8005E247, -2147098041|Server-side synchronization for appointments, contacts, and tasks isn't supported for POP3 or SMTP server types. Select a supported email type or change the synchronization method for appointments, contacts, and tasks to None.|
> |ManagedBpfDeletionInvalid|0x80060383, -2147089533| The business process flow is part of a managed solution and cannot be individually deleted. Uninstall the parent solution to remove the business process flow.|
> |ManagedProcessDeletionError|0x80072457, -2147015593|The process is part of a managed solution and cannot be individually deleted. Uninstall the parent solution to remove the process.|
> |ManifestParsingFailure|0x80048534, -2147187404|Failed to parse the specified manifest file to retrieve OrganizationId|
> |ManifestXsdValidationError|0x80160001, -2146041855|The import manifest file is invalid. XSD validation failed with the following error: '{0}'."|
> |ManyToManyVirtualEntityNotSupported|0x80044820, -2147203040|An N:N relationship between virtual entities is not supported.|
> |MappingExistsForTargetAttribute|0x8004033e, -2147220674|This attribute is mapped more than once. Remove any duplicate mappings, and then import this data map again.|
> |MarsConnectorDisableFailure|0x80071108, -2147020536|Error occurred while disabling Mars connector.|
> |MarsConnectorEnableFailure|0x80071107, -2147020537|Error occurred while enabling Mars connector.|
> |MatchingAttributeNameNotNullError|0x80044243, -2147204541|Matching attribute name should be null single entity rule.|
> |MaxActiveSLAError|0x8004F897, -2147157865|You can’t activate this SLA because you’ve exceeded the maxiumum number of entities that can have active SLAs for your organization.|
> |MaxActiveSLAKPIError|0x8004F898, -2147157864|You can’t activate this SLA because you’ve exceeded the maxiumum number of SLA KPIs that are allowed per entity for your organization.|
> |MaxChildCasesLimitExceeded|0x8003F454, -2147224492|A Parent Case cannot have more than maximum child cases allowed. Contact your administrator for more details|
> |MaxConditionsMobileOfflineFilters|0x80071114, -2147020524|You can only define 3 Mobile offline Org  filter for each entity.|
> |MaxIconSizeExceededForConnector|0x80072602, -2147015166|Connector icon file too large, size cannot exceed 1 MB.|
> |MaximumControlsLimitExceeded|0x8004E301, -2147163391|The dashboard Form XML contains more than the maximum allowed number of control elements: {0}.|
> |MaximumCountForUpdateModeExceeded|0x8004F602, -2147158526|In an update operation, you can import only one file at a time.|
> |MaximumNumberHandlersExceeded|0x80048505, -2147187451|This solution adds form event handlers so the number of event handlers for a form event exceeds the maximum number.|
> |MaximumNumberOfAttributesForEntityReached|0x8004841A, -2147187686|The maximum number of attributes allowed for an entity has already been reached. The attribute cannot be created.|
> |MaxLimitForRollupAttribute|0x8004480a, -2147203062|Only three metric details per metric can be created.|
> |MaxMatchCodeLengthExceeded|0x80048429, -2147187671|The rule condition cannot be created or updated because it would cause the matchcode length to exceed the maximum limit.|
> |MaxProductsAllowed|0x80071020, -2147020768|You cannot create more than {0} products.|
> |MaxprofileItemFilterConditionsAllowed|0x80071116, -2147020522|You can only define 6 Mobile offline entity filter conditions for each entity.|
> |MaxUnzipFolderSizeExceeded|0x80048499, -2147187559|The selected compressed (.zip) file can't be unzipped because it's too large.|
> |MeasureDataTypeInvalid|0x8004E010, -2147164144|The Data Description for the visualization is invalid. The attribute type for one of the non aggregate measures is invalid. Correct the Data Description.|
> |MemberHasAlreadyBeenContacted|0x8004140e, -2147216370|This marketing list member was not contacted, because the member has previously received this communication.|
> |MergeActiveQuoteError|0x80045302, -2147200254|Merge cannot be performed on sub-entity that has active quote.|
> |MergeCyclicalParentingError|0x80045300, -2147200256|Merge could create cyclical parenting.|
> |MergeDifferentlyParentedWarning|0x80045316, -2147200234|Merge warning: sub-entity will be differently parented.|
> |MergeEntitiesIdenticalError|0x80045305, -2147200251|Merge cannot be performed on master and sub-entities that are identical.|
> |MergeEntityNotActiveError|0x80045304, -2147200252|Merge cannot be performed on entity that is inactive.|
> |MergeLossOfParentingWarning|0x80045317, -2147200233|Merge warning: sub-entity might lose parenting|
> |MergeSecurityError|0x80045301, -2147200255|Merge is not allowed: caller does not have the privilege or access.|
> |MetadataNoMapping|0x80040e01, -2147217919|The mapping between specified entities does not exist|
> |MetadataNotFound|0x8004024a, -2147220918|Metadata not found.|
> |MetadataNotSerializable|0x80040e03, -2147217917|The given metadata entity is not serializable|
> |MetadataRecordNotDeletable|0x80044250, -2147204528|The metadata record being deleted cannot be deleted by the end user|
> |MetadataSyncRequired|0x80072510, -2147015408|Metadata sync required|
> |MetricEntityOrFieldDeleted|0x8004F687, -2147158393|The entity or field that is referenced in the goal metric is not valid|
> |MetricNameAlreadyExists|0x80044802, -2147203070|A goal metric with the same name already exists. Specify a different name, and try again.|
> |MinMaxValidationFailed|0x80061004, -2147086332|The value is out of range.|
> |MissingBOWFRules|0x80040329, -2147220695|Bulk Operation related workflow rules are missing.|
> |MissingBusinessId|0x8004021a, -2147220966|The business id is missing or invalid.|
> |MissingColumn|0x8004B028, -2147176408|The property bag is missing an entry for {0}.|
> |MissingControlStep|0x80060385, -2147089531|Required control step is missing.|
> |MissingCrmAuthenticationToken|0x80044300, -2147204352|CrmAuthenticationToken is missing.|
> |MissingCrmAuthenticationTokenOrganizationName|0x80044308, -2147204344|Organization Name must be specified in CrmAuthenticationToken.|
> |MissingDependencyFound|0x80072039, -2147016647|Missing dependencies found.|
> |MissingDependentConnectorsForModernFlow|0x80060474, -2147089292|There are missing custom connectors for current flow, Expected count: {0} with name: {1}, actual count: {2}|
> |MissingHierarchicalRelationshipForOperator|0x80047020, -2147192800|This query uses a hierarchical operator, but the {0} entity doesn't have a hierarchical relationship.|
> |MissingKeyValue|0x80072034, -2147016652|Entity {0} does not contain key value for attribute {1}.|
> |MissingOpportunityId|0x80043b15, -2147206379|The opportunity id is missing or invalid.|
> |MissingOrganizationFriendlyName|0x8004B00A, -2147176438|Cannot install Dynamics 365 without an organization friendly name.|
> |MissingOrganizationUniqueName|0x8004B00B, -2147176437|Cannot install Dynamics 365 without an organization unique name.|
> |MissingOrInvalidRedirectId|0x80048473, -2147187597|The RedirId parameter is missing for the partner redirect.|
> |MissingOwner|0x80040215, -2147220971|Item does not have an owner.|
> |MissingParameter|0x8004031f, -2147220705|A required parameter is missing for the Bulk Operation|
> |MissingParameterToMethod|0x8004B021, -2147176415|Missing parameter {0} to method {1}|
> |MissingParameterToStoredProcedure|0x8004C000, -2147172352|Missing parameter to stored procedure:  {0}|
> |MissingPriceLevelId|0x80043b12, -2147206382|The price level id is missing.|
> |MissingPrimaryKey|0x80072033, -2147016653|The Entity {0} is missing primary key {1}.|
> |MissingProductId|0x80043b11, -2147206383|The product id is missing.|
> |MissingQuantity|0x80081012, -2146955246|The Quantity is missing.|
> |MissingQueryType|0x80040235, -2147220939|The query type is missing.|
> |MissingRecipient|0x8004350d, -2147207923|The fax must have a recipient before it can be sent.|
> |MissingRelationshipInSolution|0x80048548, -2147187384|The following attributes {0} of entity {1} are missing their associated relationship definition in customizations xml of {2} solution. Please include the associated relationship components and retry solution import.|
> |MissingRequiredAttributes|0x80061037, -2147086281|The property couldn’t be created or updated because the regardingobjectid, datatype, or name attribute is missing.|
> |MissingRequiredComponentAttributes|0x80072002, -2147016702|Required attribute should not be null. Attribute: {0}|
> |MissingTeamName|0x80041d0b, -2147214069|The team name was unexpectedly missing.|
> |MissingTransactionCurrencyId|0x80048546, -2147187386|TransactionCurrencyId needs to be supplied to format the money field (Id: {0}, Name: {1}, Value: {2}, Entity: {3}).|
> |MissingUomId|0x80043b0d, -2147206387|The unit id is missing.|
> |MissingUomScheduleId|0x80043b0a, -2147206390|The unit schedule id is missing.|
> |MissingUserId|0x8004021b, -2147220965|The user id or the team id is missing.|
> |MissingWebToLeadRedirect|0x80048477, -2147187593|The redirectto is missing for web2lead redirect.|
> |MobileClientLanguageNotSupported|0x8005F201, -2147094015|The application could not find a supported language on the server. Contact an administrator to enable a supported language|
> |MobileClientNotConfiguredForCurrentUser|0x8005F20E, -2147094002|Try this action again. If the problem continues, check the {0} for solutions or contact your organization's {#Brand_CRM} Administrator. Finally, you can contact {1}.|
> |MobileClientVersionNotSupported|0x8005F202, -2147094014|Mobile Client version is not supported|
> |MobileExcelFeatureNotEnabled|0x800608CA, -2147088182|Mobile export to excel feature is not enabled.|
> |MobileOfflineDaysSinceRecordLastModifiedZero|0x80060990, -2147087984|No records will be available in the mobile offline mode if the value for number of days is 0.|
> |MobileOfflineProfileItemNameAlreadyExists|0x800609A8, -2147087960|A mobile offline profile item with this name already exists for this mobile offline profile. Enter a unique name.|
> |MobileOfflineProfileItemNameCanNotBeNullOrEmpty|0x800609AA, -2147087958|The mobile offline profile item name can’t be null or empty. Enter a name for this profile item.|
> |MobileOfflineProfileNameAlreadyExists|0x800609A7, -2147087961|A mobile offline profile with this name already exists. Enter a unique name.|
> |MobileOfflineProfileNameCanNotBeNullOrEmpty|0x800609A9, -2147087959|The mobile offline profile name can’t be null or empty. Enter a name for this profile.|
> |MobileOfflineRuleEnhancementFeatureNotAvailaible|0x80071117, -2147020521|This feature is not enabled for your organization. Please contact your system administrator for help.|
> |MobileServiceError|0x8004B070, -2147176336|Error communicating with mobile service|
> |ModernFlowMustBeMarkedAsOnDemandForExecuteWorkflow|0x80060479, -2147089287|Cannot execute Modern Flow '{0}' because it is not marked as on-demand.|
> |ModernFlowProcessesNotEnabled|0x80060464, -2147089308|Creation of Modern Flow processes is not enabled.|
> |ModernFlowProcessesOnlyAvailableOnline|0x80060465, -2147089307|Creation of Modern Flow processes is only available online.|
> |MoneySizeExceeded|0x80040317, -2147220713|Supplied value exceeded the MIN/MAX value of Money Type field.|
> |MOPIAssociationNameCannotBeEmptyOrSpace|0x80060997, -2147087977|The Mobile Offline Profile Item Association name can’t be a space or an empty string.|
> |MoveBothToPrimary|0x8004D234, -2147167692|Move operation would put both instances on the same server:  Database = {0}  Old Primary = {1}  Old Secondary = {2}  New Secondary = {3}|
> |MoveBothToSecondary|0x8004D235, -2147167691|Move operation would put both instances on the same server:  Database = {0}  Old Primary = {1}  Old Secondary = {2}  New Secondary = {3}|
> |MoveOrganizationFailedNotDisabled|0x8004D236, -2147167690|Move operation failed because organization {0} is not disabled|
> |MultiCurrencyPluginDisabled|0x80048d01, -2147185407|Unable to fetch ExchangeRate details, MultiCurrency plugin may be Disabled. Please enable the plugin and retry.|
> |MultilevelParentChildRelationshipNotAllowed|0x8003F453, -2147224493|Associating child cases to the existing child case is not allowed.|
> |MultipleChartAreasFound|0x8004E008, -2147164152|Multiple Chart Areas are not supported.|
> |MultipleChildPicklist|0x80040250, -2147220912|Crm Internal Exception: Picklists with more than one childAttribute are not supported.|
> |MultipleExportKeyNotSupported|0x800608A9, -2147088215|Export key cannot be created for entity {0} because the entity already has an export key defined|
> |MultipleFilesFound|0x80048439, -2147187655|The attachment file name is not unique.|
> |MultipleFormElementsFound|0x8004E304, -2147163388|A Form XML of type {1} with id {2} can contain only one {0} element.|
> |MultipleImportFilesFound|0x80072036, -2147016650|Multiple files for attribute {0} were found for entity {1}.|
> |MultipleInstancesOnEntity|0x80060373, -2147089549|Multiple instances of process '{0}' exist for '{1}':'{2}'. Use business process flow APIs to perform process related actions.|
> |MultipleLabelsInUserDashboard|0x8004E30D, -2147163379|A user dashboard can have at most one label for a form element.|
> |MultipleMeasureCollectionsFound|0x8004E01C, -2147164132|More than one measure collection is not supported for charts with subcategory i.e. comparison charts|
> |MultipleMeasuresFound|0x8004E007, -2147164153|More than one measure is not supported for charts with subcategory i.e. comparison charts|
> |MultipleOrganizationsNotAllowed|0x80041d35, -2147214027|Only one organization and one root business are allowed.|
> |MultipleParentEntitiesFoundByEntity|0x8006089E, -2147088226|More than one parent exists for {0} An entity can have only one parent entity.|
> |MultipleParentReportsFound|0x80040485, -2147220347|More than one report link found. Each report can have only one parent.|
> |MultipleParentsNotSupported|0x80047007, -2147192825|An entity can have only one parental relationship|
> |MultiplePartnerSecurityRoleWithSameInformation|0x8004A10a, -2147180278|More than one security role found for partner user|
> |MultiplePartnerUserWithSameInformation|0x8004A10b, -2147180277|More than one partner user found with same information|
> |MultipleQueueItemsFound|0x80040525, -2147220187|This item occurs in more than one queue and cannot be routed from this list. Locate the item in a queue and try to route the item again.|
> |MultipleRecordsFoundByEntityKey|0x8006089D, -2147088227|More than one record exists for entity {0} with entity key involving attributes {1}|
> |MultipleRelationshipsNotSupported|0x80048200, -2147188224|Multiple relationships are not supported|
> |MultipleRootBusinessUnit|0x8004A10c, -2147180276|More than one root business unit found|
> |MultipleSitemapsFound|0x80050120, -2147155680|Found {0} unpublished site maps but expected only 1|
> |MultipleSubcategoriesFound|0x8004E006, -2147164154|The data XML for the visualization cannot contain more than two Group By clauses.|
> |MultiPredicateRelationshipEntityKeyDoesNotExist|0x80090408, -2146892792|Entity Key '{0}' of referenced entity '{1}' of relationship '{2}' does not exist.|
> |MultiPredicatesNotSupportedForRelationshipType|0x80090405, -2146892795|Multiple predicates is not supported for relationship '{0}' of type '{1}'.|
> |MultiValueParameterFound|0x8005E00A, -2147098614|Fetch xml parameter {0} cannot obtain multiple values. Change report parameter {0} to single value parameter and try again.|
> |MustContainAtLeastACharInMention|0x8004F6A4, -2147158364|The display name must contain atleast one non-whitespace character.|
> |NavigationPropertyAlreadyExists|0x80072551, -2147015343|NavigationPropertyName {0} is not unique within an entity|
> |NavigationPropertyNameCannotBeTheSameOnBothSidesOfRel|0x80072550, -2147015344|Navigation Property Name cannot be the same on both sides of a self-referential relationship. SchemaName - {0}|
> |NavigationPropertyNameMissingForRelationship|0x80048839, -2147186631|NavigationPropertyName is missing for relationship {0} which is not expected. Please populate same using sdk or webapi.|
> |NavigationPropertyNameNodeMissing|0x80048452, -2147187630|NavigationPropertyName node is missing for entity relationship {0}.|
> |NavigationPropertyNameValueMissing|0x80048836, -2147186634|NavigationPropertyName value is missing for entity relationship {0}.|
> |NavPaneNotCustomizable|0x80044329, -2147204311|The nav pane properties for this relationship are not customizable|
> |NavPaneOrderValueNotAllowed|0x80044327, -2147204313|The provided nav pane order value is not allowed|
> |NegativeAutoNumberSeed|0x80060886, -2147088250|Cannot set Auto Number seed for attribute {0} of entity {1} with value {2} as it is less than 0.|
> |NestedAlternateKeysLimitExceededInRequest|0x80090116, -2146893546|Nested alternate keys are not supported for more than {0} levels.|
> |NetworkIssue|0x8005F104, -2147094268|Request failed due to unknown network issues or GateWay issues or server issues.|
> |NewStatusHasInvalidState|0x80044322, -2147204318|The state value that was provided for this new status option does not exist.|
> |NewStatusRequiresAssociatedState|0x80044321, -2147204319|The new status option must have an associated state value.|
> |NoActiveLocation|0x80060900, -2147088128|No active location found.|
> |NoAddressFoundForRecipient|0x80040b0a, -2147218678|Could not find email address for recipient of type '{0}' with ID '{1}'|
> |NoAppModuleComponentReferred|0x8005011B, -2147155685|No component is referenced|
> |NoAttributesForEntityCreate|0x80047014, -2147192812|No attributes for Create Entity action.|
> |NoConditionRuleCreationNotAllowedForSetValueShowError|0x80060013, -2147090413|The "Show error message" and "Set value" actions can't be used in a business rule that doesn't have a condition.|
> |NoConnectionRoleAndObjectTypeCodePairPresent|0x8004F222, -2147159518|There are no ConnectionRoleId and AssociatedObjectTypeCode pairs present. Entities being connected: ({0},{1}); Entity Records being connected: ({2},{3}); Record1ConnectionRoleName: {4}, Record2ConnectionRoleName: {5}. ConnectionRoleIds: {6};|
> |NoConversionRule|0x800608F5, -2147088139|A ConversionRule is required for the tool to run.|
> |NoDataFilterSelectedForOtherDataFilter|0x80071138, -2147020488|The entity '{0}' in the profile '{1}' contained the Data Download Filter 'Other data filter' however no data filter option was selected. The entity must specify a data filter option.|
> |NoDataForVisualization|0x8004E011, -2147164143|There is no data to create this visualization.|
> |NoDefaultValueForOptionSetArgument|0x80060396, -2147089514|Arguments of type OptionSet must have a default value set.|
> |NoDefinedRelationshipsForMOPIAssociation|0x80060998, -2147087976|The Profile Item Association entity doesn’t have any defined relationships.|
> |NoDialNumber|0x8004350f, -2147207921|There is no fax number specified on the fax or for the recipient.|
> |NoEntitiesForBulkDelete|0x80048442, -2147187646|The Bulk Delete Wizard cannot be opened because there are no valid entities for deletion.|
> |NoEntitySpecified|0x800608FA, -2147088134|At least one Entity is expected by the tool to process.|
> |NoFilesSelected|0x80071021, -2147020767|No documents are selected to copy. Please select a document and try again.|
> |NoHeaderColumnFound|0x80040368, -2147220632|A column heading is missing.|
> |NoIncidentMergeHavingSameParent|0x8003F450, -2147224496|Child cases having different parent case associated can not be merged.|
> |NoLabelsAssociatedWithStep|0x80060408, -2147089400|{0} does not have any labels associated with it|
> |NoLanguageProvisioned|0x80044199, -2147204711|There is no language provisioned for this organization.|
> |NoLicenseInConfigDB|0x8004D241, -2147167679|No license exists in MSCRM_CONFIG database.|
> |NoMinimumRequiredPrivilegesForTabletApp|0x8005F20F, -2147094001|You do not have sufficient permissions on the server to load the application.\nPlease contact your administrator to update your permissions.|
> |NoMoreCustomOptionValuesExist|0x8004431F, -2147204321|All available custom option values have been used.|
> |NonAutoNumberAttributeSpecified|0x80060884, -2147088252|Attribute {0} of entity {1} is not an Auto Number attribute. Please confirm the inputs for Attribute and Entity correctly map to an Auto Number attribute.|
> |NoncompliantXml|0x80048425, -2147187675|The input XML does not comply with the XML schema.|
> |NonCrmUIInteractiveWorkflowNotSupported|0x80045044, -2147200956|This interactive workflow cannot be created, updated or published because it was created outside the Microsoft Dynamics 365 Web application.|
> |NonCrmUIWorkflowsNotSupported|0x80045040, -2147200960|This workflow cannot be created, updated or published because it was created outside the Microsoft Dynamics 365 Web application. Your organization does not allow this type of workflow.|
> |NonDraftBundleUpdate|0x80061039, -2147086279|Product Association cannot be updated when bundle is in invalid state.|
> |NonInteractiveUserCannotAccessUI|0x80044160, -2147204768|Non-interactive users cannot access the web user interface. Contact your organization system administrator.|
> |NonMappableEntity|0x80046200, -2147196416|NonMappableEntity Error Occurred|
> |NonPrimaryEntityDataDescriptionFound|0x8004E001, -2147164159|The data description for the visualization is invalid .The data description for the visualization can only have attributes either from the primary entity of the view or the linked entities.|
> |NoOutputTransformationParameterMappingFound|0x80040384, -2147220604|There is no output transformation parameter mapping defined. A transformation mapping must have atleast one output transformation parameter mapping.|
> |NoPreviewForCustomWebResource|0x8004E020, -2147164128|This chart uses a custom Web resource. You cannot preview this chart.|
> |NoPrivilegeToApplyManualSLA|0x80055002, -2147135486|You don't have appropriate permissions to apply Servie Level Agreement (SLA) to this case record.|
> |NoPrivilegeToPublishWorkflow|0x80045016, -2147201002|User does not have sufficient privileges to publish workflows.|
> |NoPrivilegeToWorker|0x80040521, -2147220191|You cannot add items to an inactive queue. Select another queue and try again.|
> |NoPublishedDuplicateDetectionRules|0x80048436, -2147187658|There are no published duplicate detection rules in the system. To run duplicate detection, you must create and publish one or more rules.|
> |NoQuickFindFound|0x80060203, -2147089917|Entity - {0} did not have a valid Quickfind query.|
> |NoRollupAttributesDefined|0x8004F681, -2147158399|For rollup to succeed atleast one rollup attribute needs to be associated with the goal metric|
> |NoSettingError|0x8004Ed46, -2147160762|No configdb configuration setting [{0}] was found.|
> |NoSiteMapReferenceInAppModule|0x8005011C, -2147155684|App Module {0} does not contain Site Map. App Module must have 1 sitemap as part of App Module Components.|
> |NotAQuickForm|0x80160024, -2146041820|Form with Id {0} is not a quick form. More Details:{1}|
> |NotAWellFormedXml|0x80048426, -2147187674|The input XML is not well-formed XML.|
> |NotBuiltInControlId|0x80160050, -2146041776|The given identifier {0} is not a valid built-in control id. More Details:{1}|
> |NotEnoughPrivilegesForXamlWorkflows|0x80045041, -2147200959|Not enough privileges to complete the operation. Only the deployment administrator can create or update workflows that are created outside the Microsoft Dynamics 365 Web application.|
> |NoTestEmailAccessPrivilege|0x8005E232, -2147098062|There is not sufficient privilege to perform the test access.|
> |NotExistArgumentInAction|0x80060393, -2147089517|Argument {0} does not exist in Action.|
> |NotExistBusinessProcess|0x80060391, -2147089519|Business Process does not exist.|
> |NoTimeZoneCodeForConversionRule|0x800608F9, -2147088135|The TimeZoneCode property is required when the value of the ConversionRule property is SpecificTimeZone.|
> |NotImplemented|0x80040219, -2147220967|The requested functionality is not yet implemented.|
> |NotMobileEnabled|0x8005F215, -2147093995|You can't view this type of record on your tablet. Contact your system administrator.|
> |NotMobileWriteEnabled|0x8005F21c, -2147093988|You can't create this type of record on your device. Contact your system administrator.|
> |NotSupported|0x80040315, -2147220715|This action is not supported.|
> |NotVerifiedAdmin|0x8005F106, -2147094266|You need an enterprise account with Yammer in order to complete this setup. Please sign in with a Yammer administrator account or contact a Yammer administrator for help.|
> |NoUserPrivilege|0x80154B50, -2146088112|You do not have sufficient permissions.|
> |NoValidModernFlowTriggerForExecute|0x80060476, -2147089290|Modern Flow '{0}' is not valid for ExecuteWorkflow.  Please select a Flow that triggers whenever a Common Data Service entity is created, updated, or deleted.|
> |NoWritePermission|0x80071023, -2147020765|You do not have Write permissions to copy the documents.|
> |NoYammerNetworksFound|0x8005F108, -2147094264|You are not authorized for any Yammer network. Please reauthorize the Yammer setup with a Yammer administrator account or contact a Yammer administrator for help.|
> |NullArticleTemplateFormatXml|0x800404f8, -2147220232|The article template formatxml cannot be NULL|
> |NullArticleTemplateStructureXml|0x800404f9, -2147220231|The article template structurexml cannot be NULL|
> |NullArticleXml|0x800404f7, -2147220233|The article xml cannot be NULL|
> |NullAutoNumberParameterSpecfied|0x80060887, -2147088249|Auto Number attribute or Entity parameters cannot be null or empty string.|
> |NullDashboardName|0x8004E305, -2147163387|The name of a dashboard cannot be null.|
> |NullKBArticleTemplateId|0x800404fa, -2147220230|The kbarticletemplateid cannot be NULL|
> |NullOrEmptyAttributeInXaml|0x80060406, -2147089402|Attribute - {0} of {1} cannot be null or empty|
> |NumberFormatFailed|0x80040259, -2147220903|Failed to produce a formatted numeric value.|
> |O365RoleUnsupportedForEmailApproval|0x8009000B, -2146893813|Email address can only be approved by an Office 365 Global Administrator or by an Exchange Administrator. For more information, contact your system administrator.|
> |OAuthTokenNotFound|0x8005F109, -2147094263|Yammer OAuth token is not found. You should configure Yammer before accessing any related feature.|
> |ObjectAlreadyExists|0x8004E30A, -2147163382|An object with id {0} already exists. Please change the id and try again.|
> |ObjectDoesNotExist|0x80040217, -2147220969|The specified object was not found.|
> |ObjectNotFoundInAD|0x80041d2a, -2147214038|The object does not exist in active directory.|
> |ObjectNotRelatedToCampaign|0x8004030e, -2147220722|Specified Object not related to the parent Campaign|
> |OccurrenceCrossingBoundary|0x8004E120, -2147163872|Two occurrences cannot overlap.|
> |OccurrenceSkipsOverBackward|0x8004E123, -2147163869|Cannot reschedule an occurrence of the recurring appointment if it skips over an earlier occurrence of the same appointment.|
> |OccurrenceSkipsOverForward|0x8004E122, -2147163870|Cannot reschedule an occurrence of the recurring appointment if it skips over a later occurrence of the same appointment.|
> |OccurrenceTimeSpanTooBig|0x8004E121, -2147163871|Cannot perform the operation. An instance is outside of series effective expansion range.|
> |OfferingCategoryAndTokenNull|0x8004B00C, -2147176436|Offer category and Billing Token are both missing, but at least one is required.|
> |OfferingIdNotSupported|0x8004B00D, -2147176435|This version does not support search for offering id.|
> |OfficeGraphDisabledError|0x80044239, -2147204551|Document Recommendations has been disabled for this organization.|
> |OfficeGraphSiteNotConfigured|0x80044257, -2147204521|No default SharePoint site has been configured.|
> |OfficeGroupsExceptionRetrieveSetting|0x800610EB, -2147086101|Office Groups Exception occured in RetrieveOfficeGroupsSetting: {0}.|
> |OfficeGroupsFeatureNotEnabled|0x800610EA, -2147086102|Office Groups feature is not enabled.|
> |OfficeGroupsInvalidSettingType|0x800610EC, -2147086100|Invalid setting type for Office Groups feature: {0}.|
> |OfficeGroupsNoAuthServersFound|0x800610EE, -2147086098|Office Groups feature could not find any authorization servers.|
> |OfficeGroupsNotSupportedCall|0x800610ED, -2147086099|Office Groups feature attempted an unsupported call.|
> |OfflineFilterNestedDateTimeOR|0x80048450, -2147187632|You cannot use nested date time conditions within an OR clause in a local data group.|
> |OfflineFilterParentDownloaded|0x80048451, -2147187631|You cannot use the Parent Downloaded condition in a local data group.|
> |OneDriveForBusinessDisabled|0x80050004, -2147155964|Following attachments requires OneDrive for Business. Please contact your administrator to enable OneDrive for Business in the organization.|
> |OneDriveForBusinessLocationNotFound|0x80050009, -2147155959|No One Drive for Business active location found.|
> |OneNoteCreationFailed|0x80060902, -2147088126|OneNote creation failed.|
> |OneNoteLocationDeactivated|0x80060907, -2147088121|The location mapping for OneNote is inactive. Contact your administrator to activate the OneNote location record for this Dynamics 365 record.|
> |OneNoteLocationNotCreated|0x80060906, -2147088122|OneNote location not created.|
> |OneNoteRenderFailed|0x80060903, -2147088125|OneNote render failed.|
> |OnlyDisabledOrganizationCanBeDeleted|0x8004B02F, -2147176401|Can not delete enabled organization. Organization must be disabled before it can be deleted.|
> |OnlyOneSearchParameterMustBeProvided|0x80060206, -2147089914|Extra parameter. You only need to provide EntityGroupName or EntityNames, not both.|
> |OnlyOwnerCanRevoke|0x80040223, -2147220957|Only the owner of an object can revoke the owner's access to that object.|
> |OnlyOwnerCanSetManagedProperties|0x8004F031, -2147160015|Cannot import component {0}: {1} because managed property {2} with value {3} is different than the current value {4} and the publisher of the solution that is being imported does not match the publisher of the solution that installed this component.|
> |OnlyOwnerTeamsCanHaveQueues|0x80048349, -2147187895|Cannot assign queues to teams that are not owner team.|
> |OnlyProductCanBeConvertedToKit|0x80061017, -2147086313|Only products can be converted to kits.|
> |OnlyStepInPredefinedStagesCanBeModified|0x80044184, -2147204732|Invalid plug-in registration stage. Steps can only be modified in stages BeforeMainOperationOutsideTransaction, BeforeMainOperationInsideTransaction, AfterMainOperationInsideTransaction and AfterMainOperationOutsideTransaction.|
> |OnlyStepInServerOnlyCanHaveSecureConfiguration|0x80044185, -2147204731|Only SdkMessageProcessingStep with ServerOnly supported deployment can have secure configuration.|
> |OnlyStepOutsideTransactionCanCreateCrmService|0x80044186, -2147204730|Only SdkMessageProcessingStep in parent pipeline and in stages outside transaction can create CrmService to prevent deadlock.|
> |OnlyWorkflowDefinitionOrTemplateCanBePublished|0x8004500D, -2147201011|Only workflow definition or draft workflow template can be published.|
> |OnlyWorkflowDefinitionOrTemplateCanBeUnpublished|0x8004500E, -2147201010|Only workflow definition or workflow template can be unpublished.|
> |OnPremiseRestoreOrganizationManifestFailed|0x80048532, -2147187406|Failed to restore Organization's configdb state from manifest|
> |OpenCrmDBConnection|0x8004023e, -2147220930|Db Connection is Open, when it should be Closed.|
> |OpenDocumentErrorCodeGeneric|0x8005F20C, -2147094004|Try this action again. If the problem continues, check the {0} for solutions or contact your organization's {#Brand_CRM} Administrator. Finally, you can contact {1}.|
> |OpenDocumentErrorCodeUnableToFindAnActivity|0x8005F20A, -2147094006|Try this action again. If the problem continues, check the {0} for solutions or contact your organization's {#Brand_CRM} Administrator. Finally, you can contact {1}.|
> |OpenDocumentErrorCodeUnableToFindTheDataId|0x8005F20B, -2147094005|Try this action again. If the problem continues, check the {0} for solutions or contact your organization's {#Brand_CRM} Administrator. Finally, you can contact {1}.|
> |OpenMailboxException|0x8005E216, -2147098090|Exception occurs while opening mailbox for Exchange mail server.|
> |OperationCanBeCalledOnlyOnce|0x80040334, -2147220684|The specified action can be done only one time.|
> |OperationCanceled|0x80060912, -2147088110|Refresh was canceled by user.|
> |OperationFailedTryAgain|0x80154B53, -2146088109|Operation could not be performed at the moment. Please try again.|
> |OperationOrganizationNotFullyDisabled|0x8004D23a, -2147167686|The {1} operation failed because organization {0} is not fully disabled yet.  Use FORCE to override|
> |OperationReservedForSolutionAwareEntities|0x80072008, -2147016696|This operation is reserved for solution-aware entities only.|
> |OperatorCodeNotPresentError|0x80044241, -2147204543|OperatorCode should be present in condition xml.|
> |OperatorsInViewNotSupportedOffline|0x80071127, -2147020505|One or more operators in this view are not supported offline.|
> |OpportunityAlreadyInOpenState|0x8004051a, -2147220198|The opportunity is already in the open state.|
> |OpportunityCannotBeClosed|0x80040516, -2147220202|The opportunity cannot be closed.|
> |OpportunityCurrencyComparisonNotPossible|0x80100004, -2146435068|Unable to update the opportunity, currency comparison could not be made.|
> |OpportunityIsAlreadyClosed|0x80040515, -2147220203|The opportunity is already closed.|
> |OpportunityNotFound|0x80100006, -2146435066|Unable to get opportunity entity for update.|
> |OpportunityPreImageNotFound|0x80100007, -2146435065|Unable to find pre-image of the opportunity before the update.|
> |OptimisticConcurrencyNotEnabled|0x8006088D, -2147088243|Optimistic concurrency isn't enabled for entity type {0}. The IfVersionMatches value of ConcurrencyBehavior can only be used if optimistic concurrency is enabled.|
> |OptionReorderArrayIncorrectLength|0x80044324, -2147204316|The array of option values that were provided for reordering does not match the number of options for the attribute.|
> |OptionSetValidationFailed|0x80061005, -2147086331|The value is out of range.|
> |OptionValuePrefixOutOfRange|0x80048402, -2147187710|CustomizationOptionValuePrefix must be a number between {0} and {1}|
> |OrganizationDisabled|0x8004A104, -2147180284|The Dynamics 365 organization you are attempting to access is currently disabled.  Please contact your system administrator|
> |OrganizationMigrationUnderway|0x8004B044, -2147176380|Organization migration is already underway.|
> |OrganizationNotConfigured|0x8004D253, -2147167661|Organization is not configured yet|
> |OrganizationTakenBySomeoneElse|0x8004B00F, -2147176433|The organization {0} is already purchased by another customer.|
> |OrganizationTakenByYou|0x8004B00E, -2147176434|The organization {0} is already purchased by you.|
> |OrganizationUIDeprecated|0x80044159, -2147204775|The OrganizationUI entity is deprecated. It has been replaced by the SystemForm entity.|
> |OrgDoesNotExistInDiscoveryService|0x8004B067, -2147176345|Organization not found in customer's discovery service|
> |OrgIdNotDetermined|0x80044353, -2147204269|Error. The current organization ID couldn’t be determined|
> |OrgsInaccessible|0x8004D24A, -2147167670|The client access license (CAL) results were not returned because one or more organizations in the deployment cannot be accessed.|
> |OutgoingNotAllowedForForwardMailbox|0x8005E225, -2147098075|Mailbox is a forward mailbox. A forward mailbox cannot send the mails.|
> |OutgoingServerLocationAndSslSetToNo|0x8005E23F, -2147098049|The URL specified for Outgoing Server Location uses HTTPS but the Use SSL for Outgoing Connection option is set to No. Set this option to Yes, and then try again.|
> |OutgoingServerLocationAndSslSetToYes|0x8005E241, -2147098047|The URL specified for Outgoing Server Location uses HTTP but the Use SSL for Outgoing Connection option is set to Yes. Specify a server location that uses HTTPS, and then try again.|
> |OutgoingSettingsUpdateNotAllowed|0x8005E238, -2147098056|Different outgoing connection settings cannot be specified because the "Use Same Settings for Outgoing Connections" flag is set to True.|
> |OutlookClientConfigActionFailed|0x80044509, -2147203831|Dynamics 365 Outlook client configuration action failed.|
> |OutOfScopeSlug|0x80045050, -2147200944|The data required to display the next dialog page cannot be found. To resolve this issue, contact the dialog owner or the system administrator.|
> |OverlappingInstances|0x8004E108, -2147163896|Two instances of the series cannot overlap.|
> |OverRetrievalUpperLimitWithoutPagingCookie|0x8004430A, -2147204342|Over upper limit of records that can be requested without a paging cookie. A paging cookie is required when retrieving a high page number.|
> |OwnerAttributeMissing|0x8006110C, -2147086068|Owner Attribute is not present in the request.|
> |OwnerMappingExistsWithSourceSystemUserName|0x80040343, -2147220669|The data map already contains this owner mapping.|
> |OwnerValueNotMapped|0x80040361, -2147220639|The owner value is not mapped|
> |PageNotFound|0x8005F21A, -2147093990|Page not found. The record might not exist, or the link might be incorrect.|
> |ParentBusinessDoesNotExist|0x80041d23, -2147214045|The parent business Id is invalid.|
> |ParentCaseNotAllowedAsAChildCase|0x8003F455, -2147224491|You can't add a parent case as a child case|
> |ParentChildMetricIdDiffers|0x80044905, -2147202811|The metricid of child goal should be same as the parent goal.|
> |ParentChildPeriodAttributesDiffer|0x80044906, -2147202810|The period settings of child goal should be same as the parent goal.|
> |ParentHierarchyExistProperty|0x8004F888, -2147157880|A parent should exist for each node in hierarchy except the root node.|
> |ParentReadOnly|0x80043b09, -2147206391|The parent is read only and cannot be edited.|
> |ParentRecordAlreadyExists|0x80048478, -2147187592|This record cannot be added because it already has a parent record.|
> |ParentReportDoesNotReferenceChild|0x80040486, -2147220346|Specified parent report does not reference the current one. Only SQL Reporting Services reports can have parent reports.|
> |ParentReportLinksToSameNameChild|0x80040496, -2147220330|Parent report already links to another report with the same name.|
> |ParentReportNotSupported|0x80040487, -2147220345|Parent report is not supported for the type of report specified. Only SQL Reporting Services reports can have parent reports.|
> |ParentUserDoesNotExist|0x80041d27, -2147214041|The parent user Id is invalid.|
> |ParseMustBeCalledBeforeTransform|0x80040371, -2147220623|Cannot call transform before parse.|
> |ParsingMetadataNotFound|0x80040367, -2147220633|Data required to parse the file, such as the data delimiter, field delimiter, or column headings, was not found.|
> |PartialExpansionSettingLoadError|0x8004E102, -2147163902|Failed to retrieve partial expansion settings from the configuration database.|
> |PartialHolidayScheduleCreation|0x8004F873, -2147157901|Partial holiday schedule can not be created.|
> |ParticipatingEntityDoesNotAppearInTraversedPath|0x80060441, -2147089343|Record for entity '{0}' is not in the traversed path '{1}'. Please contact your system administrator.|
> |ParticipatingQueryEntityMismatch|0x80044909, -2147202807|The entitytype of participating query should be the same as the entity specified in fetchxml.|
> |PasswordRequiredForImpersonation|0x8005E24E, -2147098034|Type in a password and save again|
> |PatchMissingBase|0x80048540, -2147187392|You can't import the patch ({0}) for the solution ({1}) because the solution isn't present. The operation has been canceled.|
> |PercentageDiscountCannotHaveCurrency|0x80048cf1, -2147185423|Currency cannot be set when discount type is percentage.|
> |PersonalReportFound|0x8004E309, -2147163383|A system dashboard cannot contain personal reports.|
> |PickListMappingExistsForTargetValue|0x8004033f, -2147220673|This list value is mapped more than once. Remove any duplicate mappings, and then import this data map again.|
> |PickListMappingExistsWithSourceValue|0x80040342, -2147220670|The data map already contains this list value mapping.|
> |PicklistValueNotFound|0x80040393, -2147220589|The file specifies a list value that does not exist in Microsoft Dynamics 365.|
> |PicklistValueNotMapped|0x80040360, -2147220640|The record could not be processed as the Option set value could not be mapped.|
> |PicklistValueNotUnique|0x80044310, -2147204336|The picklist value already exists.  Picklist values must be unique.|
> |PicklistValueOutOfRange|0x8004431A, -2147204326|The picklist value is out of the range.|
> |PingFailureErrorCode|0x8005F212, -2147093998|The system couldn't reconnect with your {#Brand_CRM} server.|
> |PluginAssemblyContentSizeExceeded|0x8004418f, -2147204721|"The assembly content size '{0} bytes' has exceeded the maximum value allowed for isolated plug-ins '{1} bytes'."|
> |PluginAssemblyMustHavePublicKeyToken|0x8004416c, -2147204756|Public assembly must have public key token.|
> |PluginDoesNotImplementCorrectInterface|0x8004A200, -2147180032|The plug-in specified does not implement the required interface Microsoft.Xrm.Sdk.IPlugin or Microsoft.Crm.Sdk.IPlugin.|
> |PluginSecureStoreAdalAcquireToken|0x80091005, -2146889723|Unable to AcquireToken for resource|
> |PluginSecureStoreKeyVaultClient|0x80091000, -2146889728|Unable to initialize KeyVaultClientProvider under Sandbox WorkerProcess|
> |PluginSecureStoreKeyVaultClientDecrypt|0x80091003, -2146889725|Unable to Decrypt using KeyVault|
> |PluginSecureStoreKeyVaultClientDeleteSecret|0x80091010, -2146889712|Unable to DeleteSecret to KeyVault|
> |PluginSecureStoreKeyVaultClientEncrypt|0x80091004, -2146889724|Unable to Encrypt using KeyVault|
> |PluginSecureStoreKeyVaultClientGetSecret|0x80091001, -2146889727|Unable to GetSecret from KeyVault|
> |PluginSecureStoreKeyVaultClientSetSecret|0x80091002, -2146889726|Unable to SetSecret to KeyVault|
> |PluginSecureStoreKeyVaultServiceCertFormat|0x8009100D, -2146889715|Certificate not stored as a Base64String in KeyVault|
> |PluginSecureStoreKeyVaultServiceProviderGetData|0x8009100C, -2146889716|Missing AppId / Secrets in KeyVault|
> |PluginSecureStoreLocalConfigStoreGetData|0x8009100A, -2146889718|Unable to get data from LocalConfigStore|
> |PluginSecureStoreLocalConfigStoreSetData|0x8009100B, -2146889717|Unable to set data to LocalConfigStore|
> |PluginSecureStoreNoFullySigned|0x8009100F, -2146889713|Assembly not fully signed|
> |PluginSecureStoreS2SMissing|0x80091008, -2146889720|S2S Credentials missing|
> |PluginSecureStoreTPSAssemblyNotRegistered|0x80091007, -2146889721|Assembly is not registered in TPS|
> |PluginSecureStoreTPSClient|0x80091009, -2146889719|Unable to create TPS Client|
> |PluginSecureStoreTPSKeyVaultUnconfigured|0x80091006, -2146889722|KeyVaultURI was not configured for an Assembly in TPS|
> |PluginTypeMustBeUnique|0x8004417C, -2147204740|Multiple plug-in types from the same assembly and with the same typename are not allowed.|
> |PolymorphicLookupNotSupportedInSolutionAwareEntity|0x80090428, -2146892760|The entity '{0}' is solution aware and cannot include the polymorphic lookup.|
> |PolymorphicLookupStyleCannotBeUpdated|0x80090427, -2146892761|The polymorphic lookup style cannot be updated. Entity '{0}', AttributeId '{1}'.|
> |Pop3UnexpectedException|0x8005E215, -2147098091|Exception occur while polling mails using Pop3 protocol.|
> |PowerBICannotBeSystemDashboard|0x800608FC, -2147088132|A Power BI Dashboard cannot be a System Dashboard.|
> |PowerBIDashboardControlLimitation|0x800608FD, -2147088131|A Power BI Dashboard can only contain one control and that control must be a Power BI control.|
> |PresentParentAccountAndParentContact|0x80040508, -2147220216|You can either specify a contacts parent contact or its account, but not both.|
> |PreviousOperationNotComplete|0x80048464, -2147187612|An operation on which this operation depends did not complete successfully.|
> |PriceLevelNameExists|0x80043b0f, -2147206385|The name already exists.|
> |PriceLevelNoName|0x80043b0e, -2147206386|The name can not be null.|
> |PriceListIsMandatory|0x80100010, -2146435056|PriceList is mandatory for creating entity.|
> |PrimaryEntityInvalid|0x8004501E, -2147200994|Invalid primary entity.|
> |PrimaryEntityIsNull|0x80060401, -2147089407|Primary Entity cannot be NULL while creating business process flow category|
> |PrimaryNameAttributeNotFound|0x80044355, -2147204267|PrimaryName attribute not found for Entity: {0}|
> |PrimaryParticipatingEntityIsNotPresent|0x80060453, -2147089325|Validation error: primary participating entity is not present and is required for every Business Process entity record.|
> |PrincipalPrivilegeDenied|0x80040231, -2147220943|Target user or team does not hold required privileges.|
> |PrivilegeCreateIsDisabledForOrganization|0x80040276, -2147220874|Privilege Create is disabled for organization.|
> |PrivilegeDenied|0x80040220, -2147220960|The user does not hold the necessary privileges.|
> |ProcessActionDoesNotExist|0x80045054, -2147200940|Process Action does not exist.|
> |ProcessActionIsNotActive|0x80045053, -2147200941|Process Action should be active to be used on Action Step.|
> |ProcessActionNameIncorrect|0x80060379, -2147089543|Process Action “{0}” does not match the name configured: “{1}”. Contact your system administrator to check the configuration metadata if the error persists.|
> |ProcessActionWithInvalidInputOutputParam|0x80045058, -2147200936|Process Action contains a parameter that is not supported. Name: {0}, type: {1}, direction: {2}.|
> |ProcessActionWithInvalidInputParam|0x80045057, -2147200937|Process Action contains a field in input parameter that is unsupported on Action Steps. Refer to {0} |
> |ProcessActionWithInvalidOutputParam|0x80045056, -2147200938|Process Action contains a field in output parameter that is unsupported on Action Steps. Refer to {0}.|
> |ProcessActionWorkflowNotEnabledForOnDemand|0x80060380, -2147089536|Process Action or Workflow must be enabled for on-demand execution to be available for action steps.|
> |ProcessControlDoesNotExistOnForm|0x80060372, -2147089550|Process Control does not exist on form|
> |ProcessEmptyBranches|0x80060399, -2147089511|This process contains empty branches. Define or delete these branches and try again.|
> |ProcessFileFailure|0x80072554, -2147015340|Error occured when processing file. Reason: {0}|
> |ProcessIdDoesNotMatchBusinessProcessDefinition|0x80060460, -2147089312|Validation error: Process ID does not match Business Process definition.|
> |ProcessIdIsEmpty|0x80060459, -2147089319|Validation error: Process ID cannot be empty.|
> |ProcessImageFailure|0x80072553, -2147015341|Error occured when processing image. Reason: {0}|
> |ProcessInstanceNotFound|0x80060370, -2147089552|Supplied process instance {0} does not match any existing instance on this entity {1}|
> |ProcessNameContainsInvalidCharacters|0x80060398, -2147089512|The business process name contains invalid characters.|
> |ProcessNameIsNullOrEmpty|0x80060418, -2147089384|The business process flow name is NULL or empty. |
> |ProcessStageIdIsEmpty|0x80060461, -2147089311|Validation error: Primary Stage ID cannot be empty.|
> |ProductCanOnlyBeUpdatedInDraft|0x8004F995, -2147157611|Product, product family and bundle can only be updated in draft state.|
> |ProductCloneFailed|0x80061006, -2147086330|You can't clone a child record of a retired product family.|
> |ProductDoesNotExist|0x80043b24, -2147206364|The product does not exist.|
> |ProductFamilyCanCreateDynamicProperty|0x80081007, -2146955257|A property can only be created for a product family.|
> |ProductFamilyRootParentisLocked|0x8008101F, -2146955233|The product family root parent record is locked by some other process.|
> |ProductFromActiveToActiveState|0x8004F982, -2147157630|Product is already in Active State.|
> |ProductFromActiveToDraftState|0x8004F912, -2147157742|You can't set a published product to the draft state.|
> |ProductFromDraftToDraftState|0x8004F981, -2147157631|Product is already in Draft State.|
> |ProductFromDraftToRetiredState|0x8004F978, -2147157640|You can't retire this product because {0} is in draft state. A product should be in Active/ Under Revision state for retiring.|
> |ProductFromDraftToRevisedState|0x8004F913, -2147157741|You can't revise a draft or a retired product.|
> |ProductFromRetiredToActiveState|0x8004F977, -2147157641|You can't set a retired property to an active state.|
> |ProductFromRetiredToDraftState|0x8004F979, -2147157639|It is not possible to move product from Retired to Draft State.|
> |ProductFromRetiredToRetiredState|0x8004F980, -2147157632|Product is already in Retired State.|
> |ProductHasUnretiredChild|0x8004F910, -2147157744|You can't retire this product family because one or more of its child records aren't retired.|
> |ProductInvalidPriceLevelPercentage|0x80043b0c, -2147206388|The pricing percentage must be greater than or equal to zero and less than 100000.|
> |ProductInvalidQuantityDecimal|0x80043b07, -2147206393|The number of decimal places on the quantity is invalid.|
> |ProductInvalidUnit|0x80043b14, -2147206380|The specified unit is not valid for this product.|
> |ProductKitLoopBeingCreated|0x80043b23, -2147206365|You can’t add a kit to itself.|
> |ProductKitLoopExists|0x80043b22, -2147206366|Loop exists in the kit hierarchy.|
> |ProductMaxPropertyLimitExceeded|0x8008100D, -2146955251|This product can't be published because it has too many properties. A product in your organization can't have more than {0} properties.|
> |ProductMissingUomSheduleId|0x80043b13, -2147206381|The unit schedule id of the product is missing.|
> |ProductNoProductNumber|0x80043b05, -2147206395|The product number can not be null.|
> |ProductNoSubstitutedProductNumber|0x8004F990, -2147157616|The substituted Product number cannot be a NULL.|
> |ProductOrBundleCannotBeAsParent|0x8004F973, -2147157645|Only Product Families can be parents to products.|
> |ProductProductNumberExists|0x80043b06, -2147206394|The specified product ID conflicts with the product ID of an existing record. Specify a different product ID and try again.|
> |ProductRecommendationsFeatureNotEnabled|0x80061600, -2147084800|Product Recommendations feature is not enabled.|
> |ProfileContainsCircularReference|0x80071141, -2147020479|The profile '{0}' has a circular reference which will prevent your data download. Please review the circular reference chain: {1} and remove the profile item association that causes the circular reference.|
> |ProfileContainsRelationshipWithoutEntity|0x80071142, -2147020478|The profile '{0}' has a profile item {1} which contains a profile item association for {2}, however there does not exist a profile item for {2}. Please include the profile item and publish.|
> |ProfileCountUserLimitExceeded|0x80071134, -2147020492|The total number of users ('{0}') in this profile exceeds the allowed limit ('{1}'). Please limit the total number of users to be within the supported limit.|
> |ProfileRuleActivateDeactivateByNonOwner|0x80061102, -2147086078|This Profile Rule cannot be activated or deactivated by someone who is not its owner.|
> |ProfileRuleMissingRuleCriteria|0x80061100, -2147086080|You can't activate this rule until you resolve any missing rule criteria information in the rule items.|
> |ProfileRulePublishedByOwner|0x80061103, -2147086077|Your rule can't be activated until the current active rule is deactivated. The active rule can only be deactivated by the rule owner.|
> |ProfileRuleWorkflowAuthorGenericError|0x80061101, -2147086079|An error occurred while authoring workflow. Please fix workflow definition and try again.|
> |PropertyBoundToNonExistingAttribute|0x80160045, -2146041787|Property {0} is bound to a non-existent attribute {1} in entity {2}. More Details:{3}|
> |PropertyBoundToNonExistingAttributeInPrimaryAndRelatedEntitiesAndNotExistingAsFormParameter|0x80160051, -2146041775|Property {0} is bound to a non-existent attribute {1} in current entity {2} or in related entity {3} and also not present as part of formParameters. More Details:{4}|
> |PropertyBoundToNonExistingEntity|0x80160046, -2146041786|Property {0} is bound to an attribute in non-existent entity. More Details:{1}|
> |PropertyIsRequiredButNoValueDefined|0x80160026, -2146041818|Property {0} is required, but has no defined value. More Details:{1}|
> |PropertyNotDeclaredInManifest|0x80160038, -2146041800|Property {0} is not declared in the control manifest. More Details:{1}|
> |PropertyTypeCouldNotBeDeterminedFromAsSameTypeProperty|0x80160035, -2146041803|Cannot determine the type of property '{0}', because it is the same type as undetermined property '{1}'. More Details:{2}|
> |ProvisioningNotCompleted|0x80091044, -2146889660|To enable auto capture, you need to set up Cortana Intelligence Customer Insights in Relationship Insights settings.|
> |ProvisionRIAccessNotAllowed|0x80044270, -2147204496|You need system administrator privileges to turn Relationship Insights on for your organization.|
> |PSqlEndpointDisabled|0x80041205, -2147216891|TDS protocol endpoint is disabled for this organization. For more information, please visit http://aka.ms/EnableSQLForCDS|
> |PSqlErrorWhenGettingSecret|0x80041204, -2147216892|Unable to get the Secret from the KeyVault. Try again later and if the problem persists, contact your system administrator.|
> |PSqlExceededMaxResultSize|0x80041208, -2147216888|Return records size cannot exceed {0}. Make sure to filter result set to tailor it to your report.|
> |PSqlInvalidDatabaseName|0x80041210, -2147216880|Invalid database name “{0}”.|
> |PSqlInvalidObjectName|0x80041202, -2147216894|Invalid object name in SQL statement.|
> |PSqlInvalidServerName|0x80041209, -2147216887|Invalid server name “{0}”.|
> |PSqlParseError|0x80041201, -2147216895|Invalid SQL statement.|
> |PSqlQueryError|0x80041206, -2147216890|Invalid SQL query.|
> |PSqlTableInvalidForReports|0x80041203, -2147216893|Table is not available for reports.|
> |PSqlUnsupportedDataType|0x80041207, -2147216889|Unsupported data type {0} for column {1}. Please remove the column from the query and retry.|
> |PSqlUnsupportedStatement|0x80041200, -2147216896|Unsupported SQL statement.|
> |PublishArticle_TranslationWithMoreThanOneApprovedVersion|0x80061401, -2147085311|There is more than one approved version of the {0} language. You can only publish one version of each language.|
> |PublishedWorkflowLimitForSkuReached|0x80045015, -2147201003|This workflow cannot be published because your organization has reached its limit for the number of workflows that can be published at the same time. (There is no limit on the number of draft workflows.) You can publish this workflow by unpublishing a different workflow, or by upgrading your license to a license that supports more workflows.|
> |PublishedWorkflowOwnershipChange|0x8004500C, -2147201012|A published workflow can only be assigned to the caller.|
> |PublishWorkflowWhileActingOnBehalfOfAnotherUserError|0x80045032, -2147200974|Publishing Workflows while acting on behalf of another user is not allowed.|
> |PublishWorkflowWhileImpersonatingError|0x80045039, -2147200967|Publishing Workflows while impersonating another user is not allowed.|
> |QuantityReadonly|0x80043b18, -2147206376|Do not modify the Quantity field when you update the primary unit.|
> |QueriesForDifferentEntities|0x8004D2B0, -2147167568|The Inner and Outer Queries must be for the same entity.|
> |QueryBuilderAlias_Does_Not_Exist|0x8004110a, -2147217142|The specified alias for the given entity in the condition does not exist.|
> |QueryBuilderAliasNotAllowedForNonAggregateOrderBy|0x80041132, -2147217102|An alias cannot be specified for an order clause for a non-aggregate Query. Use an attribute.|
> |QueryBuilderAliasRequiredForAggregateOrderBy|0x80041134, -2147217100|An alias is required for an order clause for an aggregate Query.|
> |QueryBuilderAttribute_With_Aggregate|0x80041107, -2147217145|Attributes can not be returned when aggregate operation is specified.|
> |QueryBuilderAttributeCannotBeGroupByAndAggregate|0x80041137, -2147217097|An attribute can either be an aggregate or a Group By but not both|
> |QueryBuilderAttributeNotAllowedForAggregateOrderBy|0x80041131, -2147217103|An attribute cannot be specified for an order clause for an aggregate Query. Use an alias.|
> |QueryBuilderAttributeNotFound|0x8004111e, -2147217122|A required attribute was not specified.|
> |QueryBuilderAttributePairMismatch|0x80041111, -2147217135|AttributeFrom and AttributeTo must be either both specified or both omitted.|
> |QueryBuilderAttributeRequiredForNonAggregateOrderBy|0x80041133, -2147217101|An attribute is required for an order clause for a non-aggregate Query.|
> |QueryBuilderBad_Condition|0x80041106, -2147217146|Incorrect filter condition or conditions.|
> |QueryBuilderByAttributeMismatch|0x8004110f, -2147217137|QueryByAttribute must specify a non-empty value array with the same number of elements as in the attributes array.|
> |QueryBuilderByAttributeNonEmpty|0x80041110, -2147217136|QueryByAttribute must specify a non-empty attribute array.|
> |QueryBuilderColumnSetVersionMissing|0x80041113, -2147217133|The specified columnset version is invalid.|
> |QueryBuilderDeserializeEmptyXml|0x80041124, -2147217116|Xml String can't be null.|
> |QueryBuilderDeserializeInvalidAggregate|0x8004111a, -2147217126|An error occurred while processing Aggregates in Query|
> |QueryBuilderDeserializeInvalidDescending|0x80041119, -2147217127|The only valid values for descending attribute are 'true', 'false', '1', and '0'.|
> |QueryBuilderDeserializeInvalidDistinct|0x80041115, -2147217131|The only valid values for distinct attribute are 'true', 'false', '1', and '0'.|
> |QueryBuilderDeserializeInvalidGetMinActiveRowVersion|0x8004111b, -2147217125|The only valid values for GetMinActiveRowVersion attribute are 'true', 'false', '1', and '0'.|
> |QueryBuilderDeserializeInvalidGroupBy|0x8004112E, -2147217106|The only valid values for groupby attribute are 'true', 'false', '1', and '0'.|
> |QueryBuilderDeserializeInvalidLinkType|0x80041117, -2147217129|The only valid values for link-type attribute are 'natural', 'inner','in','exists','matchfirstrowusingcrossapply' and 'outer'.|
> |QueryBuilderDeserializeInvalidMapping|0x80041116, -2147217130|The only valid values for mapping are 'logical' or 'internal' which is deprecated.|
> |QueryBuilderDeserializeInvalidNode|0x8004111c, -2147217124|The element node encountered is invalid.|
> |QueryBuilderDeserializeInvalidNoLock|0x80041118, -2147217128|The only valid values for no-lock attribute are 'true', 'false', '1', and '0'.|
> |QueryBuilderDeserializeInvalidUseRawOrderBy|0x800410fd, -2147217155|The only valid values for useraworderby attribute are 'true', 'false', '1', and '0'.|
> |QueryBuilderDeserializeInvalidUtcOffset|0x8004111d, -2147217123|The utc-offset attribute is not supported for deserialization.|
> |QueryBuilderDeserializeNoDocElemXml|0x80041125, -2147217115|Document Element can't be null.|
> |QueryBuilderDuplicateAlias|0x80041130, -2147217104|FetchXML should have unique aliases.|
> |QueryBuilderElementNotFound|0x80041123, -2147217117|A required element was not specified.|
> |QueryBuilderEntitiesDontMatch|0x80041128, -2147217112|The entity name specified in fetchxml does not match the entity name specified in the Entity or Query Expression.|
> |QueryBuilderInvalid_Alias|0x80041109, -2147217143|Invalid alias for aggregate operation.|
> |QueryBuilderInvalid_Value|0x80041108, -2147217144|Invalid value specified for type.|
> |QueryBuilderInvalidAggregateAttribute|0x8004112F, -2147217105|Aggregate {0} is not supported for attribute of type {1}.|
> |QueryBuilderInvalidAttributeValue|0x80041139, -2147217095|The attribute value provided is invalid.|
> |QueryBuilderInvalidColumnSetVersion|0x80041112, -2147217134|The specified columnset version is invalid.|
> |QueryBuilderInvalidConditionOperator|0x80041120, -2147217120|Unsupported condition operator.|
> |QueryBuilderInvalidDateGrouping|0x80041135, -2147217099|An invalid value was specified for dategrouping.|
> |QueryBuilderInvalidFilterType|0x80041122, -2147217118|Unsupported filter type. Valid values are 'and', or 'or'.|
> |QueryBuilderInvalidJoinOperator|0x80041121, -2147217119|Unsupported join operator.|
> |QueryBuilderInvalidLogicalOperator|0x800410fe, -2147217154|Unsupported logical operator: {0}.  Accepted values are ('and', 'or').|
> |QueryBuilderInvalidOrderType|0x8004111f, -2147217121|A valid order type must be set in the order before calling this method.|
> |QueryBuilderInvalidPagingCookie|0x8004112A, -2147217110|Invalid page number in paging cookie.|
> |QueryBuilderInvalidUpdate|0x80041100, -2147217152|An attempt was made to update a non-updateable field.|
> |QueryBuilderLinkNodeForOrderNotFound|0x80041126, -2147217114|Converting from Query to EntityExpression failed. Link Node for order was not found.|
> |QueryBuilderMultipleIntersectEntities|0x8004110e, -2147217138|More than one intersect entity exists between the two entities specified.|
> |QueryBuilderNoAlias|0x8004110b, -2147217141|No alias for the given entity in the condition was found.|
> |QueryBuilderNoAttribute|0x80041103, -2147217149|The specified attribute does not exist on this entity.|
> |QueryBuilderNoAttrsDistinctConflict|0x8004112C, -2147217108|The no-attrs tag cannot be used in conjuction with Distinct set to true.|
> |QueryBuilderNoEntity|0x80041102, -2147217150|The specified entity was not found.|
> |QueryBuilderNoEntityKey|0x80041140, -2147217088|The specified entitykey was not found.|
> |QueryBuilderPagingOrderBy|0x80041129, -2147217111|Order by columns do not match those in paging cookie.|
> |QueryBuilderReportView_Does_Not_Exist|0x8004110d, -2147217139|A report view does not exist for the specified entity.|
> |QueryBuilderSerializationInvalidIsQuickFindFilter|0x80041138, -2147217096|The only valid values for isquickfindfields attribute are 'true', 'false', '1', and '0'.|
> |QueryBuilderSerialzeLinkTopCriteria|0x80041114, -2147217132|Fetch does not support where clause with conditions from linkentity.|
> |QueryBuilderUnexpected|0x80041101, -2147217151|An unexpected error occurred.|
> |QueryBuilderValue_GreaterThanZero|0x8004110c, -2147217140|A value greater than zero must be specified.|
> |QueryContainedSecuredAttributeWithoutAccess|0x8004F506, -2147158778|The Query contained a secured attribute to which the caller does not have access|
> |QueryFilterConditionAttributeNotPresentInExpressionEntity|0x80071119, -2147020519|The query references a field that does not exist in Dynamics 365: "{0}"|
> |QueryNotValidForStaticList|0x8004F702, -2147158270|Query cannot be specified for a static list.|
> |QueryParameterNotUnique|0x8005E00B, -2147098613|Query parameter {0} must be defined only once within the data set.|
> |QueueIdNotPresent|0x80040528, -2147220184|You must enter the target queue. Provide a valid value in the Queue field and try again.|
> |QueueItemNotPresent|0x80040529, -2147220183|You must enter the name of the record that you would like to put in the queue. Provide a valid value in the Queue Item field and try again.|
> |QueueMailboxUnexpectedDeliveryMethod|0x8005E210, -2147098096|Delivery method for mailbox associated with a queue cannot be outlook client.|
> |QuickCreateDisabledOnEntity|0x80060911, -2147088111|The {0} entity doesn't have a quick create form or the number of nested quick create forms has exceeded the maximum number allowed.|
> |QuickCreateInvalidEntityName|0x80060910, -2147088112|The entityLogicalName isn't valid. This value can't be null or empty, and it must represent an entity in the organization.|
> |QuickFindQueryRecordLimitExceeded|0x8004E024, -2147164124|The number of records for this search exceeds the Quick Search record limit. Please refine your query and try again.|
> |QuickFindSavedQueryAlreadyExists|0x8004853A, -2147187398|"Only one quickfind saved query can exist for an entity. There already exists a quick-find saved query for entity with objecttypecode: {0}"|
> |QuickFormIsNotAssociatedWithEntity|0x80160025, -2146041819|Quick Form with Id {0} is for entity {1} when it was expected to be for entity {2} - {3}. More Details:{4}|
> |QuickFormNotCustomizableThroughSdk|0x8004F659, -2147158439|The SDK does not support creating a form of type "Quick". This form type is reserved for internal use only.|
> |QuickFormsParameterIsMissing|0x80160023, -2146041821|Required parameter QuickForms is not found. More Details:{0}|
> |QuoteAndSalesOrderCurrencyNotEqual|0x80048cee, -2147185426|The currency of the record does not match the currency of the price list.|
> |QuoteReviseExistingActiveQuote|0x80048d00, -2147185408|Quote cannot be revised as there already exists another quote in Draft/Active state and with same quote number.|
> |ReactivateEntityKeyOnlyForFailedJobs|0x80060897, -2147088233|Reactivate entity key is only supported for failed job|
> |ReadIntentIncompatible|0x80060881, -2147088255|Plugin Execution Intent of current execution context is not compatible with its parent context|
> |ReadOnlyCreateValidationFailed|0x80061002, -2147086334|You can't create and assign a value to a property instance for a read-only property.|
> |ReadOnlyUpdateValidationFailed|0x80061003, -2147086333|You can't update the property instance for a read-only property.|
> |ReadOnlyUserNotSupported|0x80041d40, -2147214016|The read-only access mode is not supported|
> |RecalculateNotSupportedOnNonRollupField|0x80060554, -2147089068|Field {0} of type {1} does not support Recalculate action. Recalculate action can only be invoked for rollup field.|
> |RecipientMarkedDoNotEmail|0x80040b09, -2147218679|Recipient of type '{0}' with ID '{1}' is marked as non-emailable|
> |RecommendationAzureConnectionCascadeActivateFailed|0x80061633, -2147084749|One or more recommendation models couldn't be activated. Try activating the existing recommendation models separately from the Azure service connection.|
> |RecommendationAzureConnectionFailed|0x80061631, -2147084751|Failed to connect to the Azure Recommendations service. Check that the service URL and the Azure account key are valid and the service subscription is active.|
> |RecommendationModelActivateConnectionMustBeActive|0x80061607, -2147084793|The Azure Machine Learning recommendation service connection must be activated before the model can be activated. Please activate the recommendation service connection and try again.|
> |RecommendationModelActiveVersionInvalidStatus|0x80061602, -2147084798|The model version used must be successfully built before the model can be activated.|
> |RecommendationModelActiveVersionNotSet|0x80061601, -2147084799|The model version used is empty. To activate the model, specify the model version.|
> |RecommendationModelBuildConnectionMustBeActive|0x80061606, -2147084794|The Azure Machine Learning recommendation service connection must be activated before building a recommendation model. Please activate the recommendation service connection and try again.|
> |RecommendationModelExpired|0x80061608, -2147084792|The recommendation model has expired. Change the Valid Until date and try to activate the model again.|
> |RecommendationModelMappingDuplicateRecord|0x80061610, -2147084784|The recommendation model mapping values for entity, mapping type and version must be unique.|
> |RecommendationModelMappingReadOnly|0x80061611, -2147084783|You can't modify a Recommendation entity if it has a corresponding Basket entity.|
> |RecommendationModelVersionActive|0x80061620, -2147084768|The RecommendationModel Version is selected as the active version on a model and cannot be deleted.|
> |RecommendationModelVersionBuildInProgress|0x80061621, -2147084767|A workflow to build a model is already in progress. You can't start another build workflow until the current workflow has finished.|
> |RecommendationModelVersionDuplicateName|0x80061622, -2147084766|A model version with the same name already exists. Specify a different name.|
> |RecommendationsUnavailable|0x80061605, -2147084795|Azure Machine Learning product recommendations are temporarily unavailable. Only catalog recommendations are available.|
> |RecommendedDocumentsRetrievalFailure|0x80071015, -2147020779|Unable to retrieve document suggestions from the document source.|
> |RecommendedDocumentsRetrievalFailureWhenSPSiteNotConfigured|0x80071028, -2147020760|Unable to retrieve document suggestions from the document source.|
> |RecordAndOpportunityCurrencyNotEqual|0x80048cef, -2147185425|The currency of the record does not match the currency of the price list.|
> |RecordAndPricelistCurrencyNotEqual|0x80048cf6, -2147185418|The currency of the record does not match the currency of the price list.|
> |RecordCanOnlyBeRevisedFromActiveState|0x8004F883, -2147157885|You can only revise an active product.|
> |RecordCountExceededForExcelOnlineError|0x80072456, -2147015594|Expected records count is {0}. Current records count is:{1}|
> |RecordNotFoundByEntityKey|0x80060891, -2147088239|A record with the specified key values does not exist in {0} entity|
> |RecordResolutionFailed|0x8004F603, -2147158525|The record could not be updated because the original record no longer exists in Microsoft Dynamics 365.|
> |RecurrenceCalendarTypeNotSupported|0x8004E116, -2147163882|The calendar type is not supported.|
> |RecurrenceEndDateTooBig|0x8004E119, -2147163879|The recurrence pattern end date is invalid.|
> |RecurrenceHasNoOccurrence|0x8004E117, -2147163881|The recurrence pattern has no occurrences.|
> |RecurrenceRuleDeleteFailure|0x8004E111, -2147163887|Cannot delete a rule that is attached to an existing rule master. Delete the rule by using the parent entity.|
> |RecurrenceRuleUpdateFailure|0x8004E110, -2147163888|Cannot update a rule that is attached to an existing rule master. Update the rule by using the parent entity.|
> |RecurrenceStartDateTooSmall|0x8004E118, -2147163880|The recurrence pattern start date is invalid.|
> |RecurringSeriesCompleted|0x8004E10B, -2147163893|The series has invalid ExpansionStateCode.|
> |RecurringSeriesMasterIsLocked|0x8004E113, -2147163885|The recurring series master record is locked by some other process.|
> |RefEntityRelationshipRoleRequired|0x80048470, -2147187600|The entity relationship role of the referencing entity is required when creating a new one-to-many entity relationship.|
> |ReferencedEntityHasLogicalPrimaryNameField|0x8004432E, -2147204306|This entity has a primary field that is logical and therefore cannot be the referenced entity in a one-to-many relationship|
> |ReferencedEntityMustHaveLookupView|0x80044337, -2147204297|Referenced entities of a relationship must have a lookup view|
> |ReferencedRelationshipAttributeMustBePartOfEntityKey|0x80090401, -2146892799|Referenced relationship attribute '{0}' of referenced entity '{1}' of relationship '{2}' must be part of the entity key '{3}'.|
> |ReferencingEntityCannotBeDifferent|0x80090422, -2146892766|Relationships on the OneToManyRelationships property must use the same entity. The referencing entity '{0}' and '{1}' should be the same entities.|
> |ReferencingEntityCannotBeSolutionAware|0x80044350, -2147204272|Referencing entities in a relationship cannot be a component in a solution.|
> |ReferencingEntityMustHaveAssociationView|0x80044338, -2147204296|Referencing entities of a relationship must have an association view|
> |RefferedSolutionIsDifferent|0x80050122, -2147155678|Found unpublished row outside of active solution: SiteMapId = {0}, SolutionId = {1}|
> |ReflexiveEntityParentOrChildDoesNotExist|0x80040388, -2147220600|Either the parent or child entity does not exist|
> |RefRoleNavPaneDisplayOptionRequired|0x80060898, -2147088232|The NavPaneDisplayOption attribute is required for the Referencing Role of a one-to-many relationship {0}.|
> |RegardingObjectValuesRetrievalFailure|0x80071012, -2147020782|Failed to retrieve regarding object values.|
> |RelatedEntityAlreadyExistsInProfile|0x8005F21e, -2147093986|The related entity already exists in this profile.|
> |RelatedEntityDoesNotExistInProfileItem|0x8006098E, -2147087986|The related entity {0} of the mobile offline profile item association {1} of the mobile offline profile item {2} doesn’t exist in the profile items of profile {3}.|
> |RelatedEntityDoesNotExistsInProfile|0x8005F21f, -2147093985|The related entity doesn’t exist in the profile items.|
> |RelatedEntityGenericError|0x8005F220, -2147093984|An unexpected error occurred while creating the profile association. Please try again.|
> |RelatedRecordsFailure|0x80071013, -2147020781|Failed to retrieve related records.|
> |RelationshipAttributeDoesNotExist|0x80090402, -2146892798|Relationship attribute '{0}' of relationship '{1}' does not exist in entity '{2}'.|
> |RelationshipAttributeEntityDoesNotExist|0x80090407, -2146892793|Relationship attribute entity '{0}' of relationship '{1}' does not exist.|
> |RelationshipAttributeMappingMustBeProvided|0x80090406, -2146892794|Relationship attribute mappings must be provided for multiple predicates relationship '{0}'.|
> |RelationshipAttributeMissing|0x80090414, -2146892780|Relationship Attribute not found for Multi Predicate relationship with id {0} and EntityKey {1}.|
> |RelationshipAttributeTypesMustMatch|0x80090404, -2146892796|Type '{0}' of referenced attribute '{1}' and type '{2}' of referencing attribute '{3}' of relationship '{4}' must match.|
> |RelationshipGraphLimitExceeded|0x80071139, -2147020487|You have specified one or more profile item associations for the entities defined in the profile '{0}'. Please review the profile item associations involving the entity '{1}' which has an association count of {2} and exceeds the supported limit of {3}.|
> |RelationshipGraphLimitExceededForIntersectEntity|0x80071135, -2147020491|You have specified one or more profile item associations for the entities defined in the profile '{0}' and related to the intersect entity '{1}'. Please review the profile item associations involving the entities '{2}' and '{3}' which have a total association count of {4} and exceeds the supported limit of {5}.|
> |RelationshipInsightsFeatureDisableError|0x80044292, -2147204462|Relationship Insights feature can't be disabled|
> |RelationshipInsightsFeatureNotEnabledError|0x80044293, -2147204461|Relationship Insights feature is not enabled or RI package is not installed|
> |RelationshipIntelligenceSDKInvocationError|0x80044276, -2147204490|You need Dynamics 365 (online) to use the Relationship Insights SDK.|
> |RelationshipIsNotCustomRelationship|0x8004700a, -2147192822|The specified relationship is not a custom relationship|
> |RelationshipNameLengthExceedsLimit|0x8004802A, -2147188694|Identifiers cannot be more than {1} characters long. The name provided: {0} length is greater than maxlength {1} characters.|
> |RelationshipNotCreatedForOfficeGraphError|0x80044235, -2147204555|This relationship cannot be created because neither entity is enabled for officegraph.|
> |RelationshipNotFound|0x80090413, -2146892781|Could not find relationship with id {0}.|
> |RelationshipNotUpdatedForOfficeGraphError|0x80044236, -2147204554|This relationship cannot be updated for officegraph because neither entity is enabled for officegraph.|
> |RelationshipRoleMismatch|0x80048467, -2147187609|The relationship role name {0} does not match either expected entity name of {1} or {2}.|
> |RelationshipRoleNodeNumberInvalid|0x80048469, -2147187607|There must be two entity relationship role nodes when creating a new many-to-many entity relationship.|
> |RelationshipSchemaNameConflictWithFieldNameOnReferencedEntity|0x80048835, -2147186635|RelationshipName {0} conflict with attribute name on entity {1} (entityid={2}). Please use unique name for relationship.|
> |RelationshipsMissingFromCreatePolymorphicLookupAttribute|0x80090421, -2146892767|The OneToManyRelationships property must contain at least one relationship. Lookup attribute name '{0}', Relationships count '{1}'.|
> |RelatioshipAlreadyExists|0x8005F221, -2147093983|Selected Relationship for entity already exists in profile. |
> |RemoveActiveCustomizationsNotSupported|0x8004F059, -2147159975|RemoveActiveCustomizations is not supported for components of type {0}.|
> |RemoveActiveCustomizationsNotSupportOnAttributeType|0x8004F053, -2147159981|RemoveActiveCustomizations is not supported for Attribute of Type: {0}.|
> |ReportDoesNotExist|0x80040499, -2147220327|Report does not exist. ReportId:{0}|
> |ReportFileTooBig|0x80048297, -2147188073|The file is too large and cannot be uploaded. Please reduce the size of the file and try again.|
> |ReportFileZeroLength|0x80048296, -2147188074|You have uploaded an empty file.  Please select a new file and try again.|
> |ReportImportCategoryOptionNotFound|0x8004F028, -2147160024|A category option for the reports was not found.|
> |ReportingServicesReportExpected|0x80040484, -2147220348|The report is not a Reporting Services report.|
> |ReportLocalProcessingError|0x80048310, -2147187952|Error occurred while viewing locally processed report. ReportId:{0}|
> |ReportLoopBeingCreated|0x80040498, -2147220328|Creating this parental association would create a loop in Reports hierarchy.|
> |ReportLoopExists|0x80040497, -2147220329|Loop exists in the reports hierarchy.|
> |ReportMissingDataSourceCredentialsError|0x80048311, -2147187951|Credentials have not been supplied for a data source used by the report. ReportId:{0}|
> |ReportMissingDataSourceError|0x80048312, -2147187950|A data source expected by the report has not been supplied. ReportId:{0}|
> |ReportMissingEndpointError|0x80048313, -2147187949|The SOAP endpoint used by the ReportViewer control could not be accessed.|
> |ReportMissingParameterError|0x80048314, -2147187948|A parameter expected by the report has not been supplied. ReportId:{0}|
> |ReportMissingReportSourceError|0x80048315, -2147187947|No source has been specified for the report. ReportId:{0}|
> |ReportNotAvailable|0x80048299, -2147188071|Report not available|
> |ReportParentChildNotCustomizable|0x8004832f, -2147187921|The report could not be updated because either the parent report or the child report is not customizable.|
> |ReportRdlSandboxing|0x80048293, -2147188077|Report upload failed due to RDL Sandboxing limitations on the Report Server.|
> |ReportRenderError|0x80040494, -2147220332|An error occurred during report rendering.|
> |ReportSecurityError|0x80048316, -2147187946|The report contains a security violation. ReportId:{0}|
> |ReportServerInvalidUrl|0x80048301, -2147187967|Cannot contact report server from given URL|
> |ReportServerNoPrivilege|0x80048302, -2147187966|Not enough privilege to configure report server|
> |ReportServerSP2HotFixNotApplied|0x80048309, -2147187959|Report server SP2 Workgroup does not have the hotfix for role creation|
> |ReportServerUnknownException|0x80048300, -2147187968|Unknown exception thrown by report server|
> |ReportServerVersionLow|0x80048303, -2147187965|Report server does not meet the minimal version requirement|
> |ReportTypeBlocked|0x80048295, -2147188075|The report is not a valid type.  It cannot be uploaded or downloaded.|
> |ReportUploadDisabled|0x80048294, -2147188076|Reporting Services reports cannot be uploaded. If you want to create a new report, please use the Report Wizard.|
> |ReportViewerError|0x8004832c, -2147187924|An error occurred during report rendering. ReportId:{0}|
> |RequestIsNotAuthenticated|0x80044302, -2147204350|Request is not authenticated.|
> |RequestLengthTooLarge|0x8004418a, -2147204726|Request message length is too large.|
> |RequiredBundleItemCannotBeUpdated|0x80081009, -2146955255|You can't delete this bundle item because it's a required product in the bundle.|
> |RequiredBundleProductCannotBeDeleted|0x80081008, -2146955256|You can't delete this product record because it's a required product in a bundle.|
> |RequiredChildReportHasOtherParent|0x8004F029, -2147160023|A category option for the reports was not found.|
> |RequiredColumnsNotFoundInImportFile|0x80040383, -2147220605|One or more source columns used in the transformation do not exist in the source file.|
> |RequiredFieldMissing|0x80040200, -2147220992|Required field missing.|
> |RequiredProcessFlowStepIsNotComplete|0x8006041d, -2147089379|You cannot move to the next stage or complete the process until the required Flow Step or Approval Step on the current stage is completed.|
> |RequiredProcessFlowStepIsNotStarted|0x8006041e, -2147089378|To move to the next stage or complete the process, click the required Flow Step or Approval Step on the current stage. You cannot move stages or complete the process until the required Flow Step or Approval Step on the current stage is completed.|
> |RequiredProcessStepIsNull|0x8006041a, -2147089382|To move to the next stage, complete the required steps.|
> |RequiredPropertyDeclarationIsMissing|0x80160032, -2146041806|Property {0} is required, but the declaration is missing. More Details:{1}|
> |RequireValidImportMapForUpdate|0x8004F600, -2147158528|The update operation cannot be completed because the import map used for the update is invalid.|
> |RestrictCustomPluginForVE|0x80072533, -2147015373|Custom plugin's are not allowed for Virtual Entity. |
> |RestrictedSolutionName|0x8004F022, -2147160030|The solution unique name '{0}' is restricted and can only be used by internal solutions.|
> |RestrictInheritedRole|0x80044152, -2147204782|Inherited roles cannot be modified.|
> |RestrictVEInBatch|0x80072535, -2147015371|Write operation for Virtual Entity is not allowed in Batch request. |
> |RestrictVEPluginOnNestedPipelineAtRunTime|0x80072534, -2147015372|Custom plugin execution is not allowed in nested pipeline for Virtual Entity. |
> |RetiredProductToBundle|0x8004F993, -2147157613|You can't add a retired product to a bundle.|
> |RetrieveImagePropertiesFail|0x80072552, -2147015342|Cannot retrieve properties for provided entity image|
> |RetrieveOrganizationInfoUnexpectedError|0x80072301, -2147015935|Unexpected error during retrieve organization information. The dependent services might not be available at this time. Please retry later.|
> |RetrieveRecordOfflineErrorCode|0x8005F213, -2147093997|This record isn't available while you're offline.  Reconnect and try again.|
> |RetrieveUserLicenseUnexpectedError|0x80072300, -2147015936|Unexpected error during retrieve user license information. The dependent services might not be available at this time. Please retry later.|
> |RetryFailed|0x8004F045, -2147159995|The action was failed after {0} times of retry. InnerException is: {1}.|
> |RibbonImportDependencyMissingEntity|0x8004F104, -2147159804|The ribbon item '{0}' is dependent on entity {1}.|
> |RibbonImportDependencyMissingRibbonControl|0x8004F107, -2147159801|The ribbon item '{0}' is dependent on ribbon control id='{1}'.|
> |RibbonImportDependencyMissingRibbonElement|0x8004F105, -2147159803|The ribbon item '{0}' is dependent on <{1} Id="{2}" />.|
> |RibbonImportDependencyMissingWebResource|0x8004F106, -2147159802|The ribbon item '{0}' is dependent on Web resource id='{1}'.|
> |RibbonImportDuplicateElementId|0x8004F10B, -2147159797|The ribbon element with the Id:{0} cannot be imported because an existing ribbon element with the same Id already exists.|
> |RibbonImportEntityNotSupported|0x8004F103, -2147159805|The solution cannot be imported because the {0} entity contains a Ribbon definition, which is not supported for that entity. Remove the RibbonDiffXml node from the entity definition and try to import again.|
> |RibbonImportHidingBasicHomeTab|0x8004F101, -2147159807|The definition of the ribbon being imported will remove the Microsoft Dynamics 365 home tab. Include a home tab definition, or a ribbon will not be displayed in areas of the application that display the home tab.|
> |RibbonImportHidingJewel|0x8004F10A, -2147159798|Ribbon customizations cannot hide the <Jewel> node. Any ribbon customization that hides this node is ignored during import and will not be exported.|
> |RibbonImportInvalidPrivilegeName|0x8004F102, -2147159806|The RibbonDiffXml in this solution contains a reference to an invalid privilege: {0}. Update the RibbonDiffXml to reference a valid privilege and try importing again.|
> |RibbonImportLocationAndIdDoNotMatch|0x8004F109, -2147159799|CustomAction Id '{0}' cannot override '{1}' because '{2}' does not match the CustomAction Location value.|
> |RibbonImportModifyingTopLevelNode|0x8004F108, -2147159800|Ribbon customizations cannot be made to the following top-level ribbon nodes: <Ribbon>, <ContextualGroups>, and <Tabs>.|
> |RibbonImportRibbonDiffIdInvalidLength|0x8004F10C, -2147159796|We can’t import this ribbon element because the ID length exceeds the maximum length of 128 characters: {0}|
> |RINotProvisioned|0x80044281, -2147204479|Relationship Insights hasn’t been turned on for your organization {0}.|
> |RoboticProcessAutomationFlowProcessesNotEnabled|0x80060471, -2147089295|Creation of Reserved processes is not enabled.|
> |RoboticProcessAutomationFlowProcessesOnlyAvailableOnline|0x80060472, -2147089294|Creation of Reserved processes is only available online.|
> |RoleAlreadyExists|0x80041403, -2147216381|A role with the specified name '{0}' already exists on business unit {1} and Solution Id {3}. Role id: {2}|
> |RoleNotEnabledForTabletApp|0x8005F203, -2147094013|You haven't been authorized to use this app.\nCheck with your system administrator to update your settings.|
> |RollupAggregateQueryRecordLimitExceeded|0x8004E025, -2147164123|Calculations can't be performed online because the calculation limit of {0} related records has been reached.|
> |RollupCalculationLimitReached|0x80060561, -2147089055|Calculations can't be performed at this time because the calculation limit has been reached. Please wait and try again.|
> |RollupDependentFieldNameAlreadyExists|0x80060556, -2147089066|Required dependent field {0} for rollup field cannot be created as another field with same name already exists. Please use an alternative name to create the rollup field.|
> |RollupFieldAggregateFunctionNotAllowed|0x80060546, -2147089082|The aggregate function {0} isn’t allowed.|
> |RollupFieldAggregateFunctionNotAllowedForRollupFieldDataType|0x80060545, -2147089083|The aggregate function {0} isn’t allowed when the rollup field is a {1} data type.|
> |RollupFieldAndAggregateFieldDataTypeFormatMismatch|0x80060544, -2147089084|The {0} data type with format {1} isn’t allowed for the aggregated field when the rollup field is a {2} data type with format {3}.|
> |RollupFieldDefinitionNotValid|0x80060553, -2147089069|The calculation failed because the rollup field definition is invalid. Contact your system administrator.|
> |RollupFieldDependentFieldCannotDeleted|0x80060541, -2147089087|Rollup field {0} depends on this field. It can only be deleted by deleting the corresponding rollup field {0}.|
> |RollupFieldNoWriteAccess|0x8004E027, -2147164121|User does not have write permission on {0} record {1} with ID:{2} to calculate rollup field.|
> |RollupFieldsAggregateFieldDataTypeNotAllowedSimilarRollupFieldDataType|0x8006053d, -2147089091|The {0} data type isn’t allowed for the aggregated field when the rollup field is a {1} data type.|
> |RollupFieldsAggregateFieldNotBelongToRelatedEntity|0x80060540, -2147089088|The aggregated field {0} doesn’t belong to the related entity {1}.|
> |RollupFieldsAggregateFieldNotBelongToSourceEntity|0x8006053f, -2147089089|The aggregated field {0} doesn’t belong to the source entity {1}.|
> |RollupFieldsAggregateFieldNotPartOfEntity|0x80060537, -2147089097|Aggregated field {0} does not belong to entity {1}|
> |RollupFieldsAggregateFunctionTypeMismatch|0x8006053a, -2147089094|The {0} data type isn’t allowed for the aggregated field when the aggregate function is {1}.|
> |RollupFieldsAggregateNotDefined|0x80060536, -2147089098|An aggregate function and an aggregated field must be provided for the rollup.|
> |RollupFieldsAggregateOnRollupFieldOrComplexCalcFieldNotAllowed|0x8006053c, -2147089092|The aggregated field must be either a simple field or a basic calculated field.|
> |RollupFieldsDataTypeNotValid|0x8006053e, -2147089090|The {0} data type isn’t valid for the rollup field.|
> |RollupFieldsGeneric|0x8006053b, -2147089093|The rollup field definition isn't valid.|
> |RollupFieldSourceFilterFieldNotAllowed|0x80060548, -2147089080|The source entity filter must use either a simple field or a basic calculated field. It can't use a rollup field, or a calculated field that is using a rollup field.|
> |RollupFieldsSourceEntityNotHierarchical|0x80060535, -2147089099|The source entity {0} hierarchy doesn’t exist.|
> |RollupFieldsSourceFilterConditionInvalid|0x80060538, -2147089096|The source entity {0} filter condition {1} isn’t valid.|
> |RollupFieldsTargetEntityNotValid|0x80060552, -2147089070|Related entity {0} is not allowed for rollups.|
> |RollupFieldsTargetFilterConditionInvalid|0x80060539, -2147089095|The related entity {0} filter condition {1} isn’t valid.|
> |RollupFieldsTargetRelationshipNotPartOfOneToNRelationship|0x80060534, -2147089100|1:N relationship {0} from the source entity {1} to the related entity {2} doesn’t exist.|
> |RollupFieldsTargetRelationshipNull|0x80060533, -2147089101|The related entity is empty. It must be provided when the source entity hierarchy isn’t used for the rollup.|
> |RollupFieldsTargetSameAsSourceEntity|0x80060551, -2147089071|Self referential 1:N relationships are not allowed for the rollup field.|
> |RollupFieldsV2FeatureNotEnabled|0x80060565, -2147089051|The feature is not supported in the current version of the product|
> |RollupFieldTargetFilterFieldNotAllowed|0x80060549, -2147089079|The target entity filter must use either a simple field or a basic calculated field. It can't use a rollup field, or a calculated field that is using a rollup field.|
> |RollupFormulaFieldInvalid|0x80060560, -2147089056|The formula field isn’t valid.|
> |RollupInvalidAttributeForFilterCondition|0x80060564, -2147089052|The {0} attribute is not allowed for filter condition.|
> |RollupOrCalcNotAllowedInWorkflowWaitCondition|0x80060557, -2147089065|The field {0} is either a rollup field or a rollup dependent field or a calculated field. Such fields are not allowed in workflow wait condition.|
> |RollupTargetLinkedEntityCanOnlyUsedForActivityPartyEntities|0x80060563, -2147089053|Target related entity can only be used for {0} entity for rollup over {1} type entities.|
> |RollupTargetLinkedEntityOnlySupportedForActivityEntities|0x80060562, -2147089054|Target related entity is only supported for rollup over {0} type entities.|
> |RollupTargetLinkedRelationshipNotValid|0x80060566, -2147089050|Target Linked Relationship {0} is not valid.|
> |RootBusinessUnitCannotBeDisabled|0x80041d63, -2147213981|Root Business unit cannot be disabled.|
> |RouterIsDisabled|0x8005E246, -2147098042|Microsoft Dynamics 365 has been configured to use server-side synchronization to process email. This error occurs because some clients are still configured to use the legacy Email router. You need to uninstall the Email router client application on any servers it was installed on.|
> |RouteTypeUnsupported|0x800404e9, -2147220247|The route type is unsupported|
> |RoutingNotAllowed|0x800404e7, -2147220249|This object type can not be routed.|
> |RoutingRuleActivateDeactivateByNonOwner|0x8004F885, -2147157883|This Routing Rule Set cannot be activated or deactivated by someone who is not its owner.|
> |RoutingRuleMissingRuleCriteria|0x8004F877, -2147157897|You can't activate this rule until you resolve any missing rule criteria information in the rule items.|
> |RoutingRulePublishedByNonOwner|0x8004F878, -2147157896|The Routing Rule Set cannot be published or unpublished by someone who is not its owner.|
> |RoutingRulePublishedByOwner|0x8004F876, -2147157898|Your rule can't be activated until the current active rule is deactivated. The active rule can only be deactivated by the rule owner.|
> |RowGuidIsNotValidName|0x80047001, -2147192831|rowguid is a reserved name and cannot be used as an identifier|
> |RSCancelBatchError|0x8004831c, -2147187940|Error occurred while canceling the batch operation.|
> |RSCreateBatchError|0x80048320, -2147187936|Error occurred while creating a batch operation.|
> |RSDeleteItemError|0x80048317, -2147187945|Error occurred while deleting an item from the report server.|
> |RSExecuteBatchError|0x8004831d, -2147187939|Error occurred while performing the batch operation.|
> |RSFindItemsError|0x80048318, -2147187944|Error occurred while finding an item on the report server.|
> |RSGetDataSourceContentsError|0x8004831a, -2147187942|Error occurred while getting the data source contents.|
> |RSGetItemDataSourcesError|0x80048321, -2147187935|Error occurred while fetching current data sources.|
> |RSGetItemTypeError|0x8004832b, -2147187925|Error occurred while fetching the report.|
> |RSGetReportHistoryLimitError|0x8004831e, -2147187938|Error occurred while fetching the number of snapshots stored for the report.|
> |RSGetReportParametersError|0x80048323, -2147187933|Error occurred while getting report parameters.|
> |RSListExtensionsError|0x8004831b, -2147187941|Error occurred while fetching the list of data extensions installed on the report server.|
> |RSListReportHistoryError|0x8004831f, -2147187937|Error occurred while fetching the report history snapshots.|
> |RSMoveItemError|0x80048330, -2147187920|Cannot move report item {0} to {1}|
> |RSReportParameterTypeMismatchError|0x80048329, -2147187927|The parameter type of the report is not valid.|
> |RSSetDataSourceContentsError|0x80048319, -2147187943|Error occurred while setting the data source contents.|
> |RSSetExecutionOptionsError|0x80048325, -2147187931|Error occurred while setting execution options.|
> |RSSetItemDataSourcesError|0x80048322, -2147187934|Error occurred while setting the data source.|
> |RSSetPropertiesError|0x8004832a, -2147187926|Error occurred while setting property values for the report.|
> |RSSetReportHistoryLimitError|0x80048327, -2147187929|Error occurred while setting report history snapshot limit.|
> |RSSetReportHistoryOptionsError|0x80048326, -2147187930|Error occurred while setting report history snapshot options.|
> |RSSetReportParametersError|0x80048324, -2147187932|Error occurred while setting report parameters.|
> |RSUpdateReportExecutionSnapshotError|0x80048328, -2147187928|Error occurred while taking snapshot of a report.|
> |RuleActivationNotAllowedWithDeletedStages|0x80060014, -2147090412|You can't activate this rule because it contains a deleted stage or stage category. Fix the rule and try again.|
> |RuleAlreadyExistsWithSameQueueAndChannel|0x8004F884, -2147157884|Record creation rule for the specified channel and queue already exists. You can't create another one.|
> |RuleAlreadyInactiveState|0x8004F852, -2147157934|This routing rule is already in Active state.|
> |RuleAlreadyInDraftState|0x8004F853, -2147157933|You can not deactivate a draft routing rule.|
> |RuleAlreadyPublishing|0x80048434, -2147187660|The selected duplicate detection rule is already being published.|
> |RuleCreationNotAllowedForCyclicReferences|0x80060012, -2147090414|You can't create this rule because it contains a cyclical reference. Fix the rule and try again.|
> |RuleNotFound|0x80048433, -2147187661|No rules were found that match the criteria.|
> |RuleNotSupportedForEditor|0x80060007, -2147090425|The current rule definition cannot be edited in the Business rule editor.|
> |RulesInInconsistentStateFound|0x80048423, -2147187677|One or more rules cannot be unpublished, either because they are in the process of being published, or are in a state where they cannot be unpublished.|
> |RuntimeRibbonXmlValidation|0x8004F671, -2147158415|The most recent customized ribbon for a tab on this page cannot be generated. The out-of-box version of the ribbon is displayed instead.|
> |S2SAccessTokenCannotBeAcquired|0x8005E243, -2147098045|Failed to acquire S2S access token from authorization server.|
> |S2SNotConfigured|0x80044259, -2147204519|Office Graph Integration relies on server-based SharePoint integration. To use this feature, enable server-based integration and have at least one active SharePoint site.|
> |SalesOrderAndInvoiceCurrencyNotEqual|0x80048ced, -2147185427|The currency of the record does not match the currency of the price list.|
> |SalesPeopleDuplicateCalendarNotAllowed|0x80043803, -2147207165|Fiscal calendar already exists for this salesperson/year|
> |SalesPeopleEmptyEffectiveDate|0x80043801, -2147207167|Fiscal calendar effective date cannot be empty|
> |SalesPeopleEmptySalesPerson|0x80043800, -2147207168|Parent salesperson cannot be empty|
> |SalesPeopleManagerNotAllowed|0x80043805, -2147207163|Territory manager cannot belong to other territory|
> |SameSolutionCircularDependenciesIdentified|0x80072007, -2147016697|Circular dependencies were identified for this solution.|
> |SampleDataIsNotUninstalled|0x80048840, -2147186624|InitialSolutionSampleDataState is not Uninstalled. :{0} |
> |SandboxClientPluginTimeout|0x80044171, -2147204751|The plug-in execution failed because the operation has timed-out at the Sandbox Client.|
> |SandboxHostNotAvailable|0x8004418e, -2147204722|The plug-in execution failed because no Sandbox Hosts are currently available. Please check that you have a Sandbox server configured and that it is running.|
> |SandboxHostPluginTimeout|0x80044172, -2147204750|The plug-in execution failed because the operation has timed-out at the Sandbox Host.|
> |SandboxPluginDisabled|0x80081115, -2146954987|Sandbox Plug-in execution is disabled.|
> |SandboxSdkListenerStartFailed|0x80044174, -2147204748|The plug-in execution failed because the Sandbox Client encountered an error during initialization.|
> |SandboxWorkerNotAvailable|0x8004418d, -2147204723|The plug-in execution failed because no Sandbox Worker processes are currently available. Please try again.|
> |SandboxWorkerPluginExecuteTimeout|0x80081111, -2146954991|Didn’t receive a response from the {0} plug-in within the 2:20-minute limit.|
> |SandboxWorkerPluginTimeout|0x80044173, -2147204749|The plug-in execution failed because the operation has timed-out at the Sandbox Worker.|
> |SandboxWorkerThrottleLimit|0x80081116, -2146954986|Maximum processes allocated for plug-in business logic exceeded. Fatal errors in plug-ins for this environment have occurred {0} times in the last {1} minutes. Each error requires an additional process to recover. Processes for plug-ins are being recycled. All plug-ins for this environment will fail during this period. More information: https://go.microsoft.com/fwlink/?linkid=2038718 |
> |SaveAsDraftAppointmentNotAllowed|0x8004026b, -2147220885|AllowSaveAsDraftAppointment is turned off.|
> |SaveDataFileErrorOutOfSpace|0x8005F209, -2147094007|Try this action again. If the problem continues, check the {0} for solutions or contact your organization's {#Brand_CRM} Administrator. Finally, you can contact {1}.|
> |SavedQueryIsNotCustomizable|0x80047017, -2147192809|The specified view is not customizable|
> |SavedQueryValidationError|0x800609A0, -2147087968|You can’t publish profile {0} because one of its profile items {1} has an entity {2} in the saved query {3}, which isn’t part of this profile.|
> |SavePending|0x80060913, -2147088109|Save operation is already running in the background.|
> |SaveRecordBeforeAddingBundle|0x8004F983, -2147157629|After you select a price list, you must save the record before you can add a bundle with optional products.|
> |ScaleGroupDisabled|0x8004A107, -2147180281|The specified scalegroup is disabled. Access to organizations in this scalegroup are not allowed.|
> |SchedulingFailedForBookingValidation|0x80060915, -2147088107|Book or Reschedule operation failed due to booking validation.|
> |SchedulingFailedForInvalidData|0x80060914, -2147088108|Book or Reschedule operation failed due to invalid data.|
> |SchemaNameContainsNonAlphaNumericCharacters|0x80044364, -2147204252|Identifier {0} for type {2} can only consist of alpha-numeric and underscore characters.|
> |SchemaNameisNotUnique|0x80044363, -2147204253|The schema name {0} for type {1} is not unique. An {0} with same name already exists.|
> |SchemaNameLengthExceedsLimit|0x80044367, -2147204249|Identifiers cannot be more than {1} characters long. The provided schema name {0} length for type {2} is greater than maxlength {1} characters.|
> |SchemaNameMatchesExistingIdentifier|0x80044361, -2147204255|Identifiers cannot match existing object names. An object of type {1} with same name {0} already exists.|
> |SchemaNameMatchesReservedSqlKeywords|0x80044362, -2147204254|Identifiers cannot match reserved SQL keywords. The name provided :{0} for type {1} matches KeyWord:{2}|
> |SchemaNameNotStartwithLetter|0x80044365, -2147204251|Identifers should start with a letter. The schema name {0} for type {2} doesn't start with letter.|
> |ScopeNotSetToGlobal|0x80060403, -2147089405|Scope should be set to Global while creating business process flow category|
> |SdkCorrelationTokenDepthTooHigh|0x80044182, -2147204734|This workflow job was canceled because the workflow that started it included an infinite loop. Correct the workflow logic and try again. For information about workflow logic, see Help.|
> |SdkCustomProcessingStepIsNotAllowed|0x80044187, -2147204729|Custom SdkMessageProcessingStep is not allowed on the specified message and entity.|
> |SdkEntityDoesNotSupportMessage|0x80040800, -2147219456|The method being invoked does not support provided entity type.|
> |SdkEntityOfflineQueuePlaybackIsNotAllowed|0x80044188, -2147204728|Entity '{0}' is not allowed in offline queue playback.|
> |SdkInvalidMessagePropertyName|0x8004416b, -2147204757|Message property name '{0}' is not valid on message {1}.|
> |SdkMessageDoesNotSupportImageRegistration|0x80044189, -2147204727|Message '{0}' does not support image registration.|
> |SdkMessageDoesNotSupportPostImageRegistration|0x8004416e, -2147204754|PreEvent step registration does not support Post Image.|
> |SdkMessageInvalidImageTypeRegistration|0x8004416d, -2147204755|Message {0} does not support this image type.|
> |SdkMessageNotImplemented|0x80044824, -2147203036|Sdk message is not implemented.|
> |SdkMessageNotSupportedOnClient|0x80044181, -2147204735|The message requested is not supported on the client.|
> |SdkMessageNotSupportedOnServer|0x80044180, -2147204736|The message requested is not supported on the server.|
> |SdkMessagesDeprecatedError|0x8004F903, -2147157757|This message is no longer available. Please consult the SDK for alternative messages.|
> |SdkNotEnoughPrivilegeToSetCallerOriginToken|0x80044309, -2147204343|Caller does not have enough privilege to set CallerOriginToken to the specified value.|
> |SearchTextLenExceeded|0x800401ff, -2147220993|Search Text Length Exceeded.|
> |SelectedFileNotFound|0x80071025, -2147020763|Unable to copy the documents. The source file no longer exists.|
> |SeriesMeasureCollectionMismatch|0x8004E003, -2147164157|Number of series for chart area and number of measure collections for category should be same.|
> |ServerLocationAndSSLSetToYes|0x8005E255, -2147098027|The URL specified for Server Location uses HTTP but Secure Sockets Layer(SSL) is required for Exchange Online.|
> |ServerLocationIsEmpty|0x8005E250, -2147098032|Server Location Field cannot be Empty|
> |ServiceAccountMailboxesCountIsGreaterThanOne|0x8005E24A, -2147098038|More no of service account mailboxes is associated to emailserver profile|
> |ServiceAccountMailboxesCountIsZero|0x8005E249, -2147098039|No service account mailbox is associated for the email server profile.|
> |ServiceBusEndpointNotConfigured|0x80081112, -2146954990|Configuration of required credentials must be completed before messages can be sent.|
> |ServiceBusExtendedTokenFailed|0x80044178, -2147204744|Failed to retrieve the additional token for service bus post.|
> |ServiceBusIssuerCertificateError|0x80044177, -2147204745|Service integration issuer certificate error.|
> |ServiceBusIssuerNotFound|0x80044176, -2147204746|Cannot find service integration issuer information.|
> |ServiceBusMaxSizeExceeded|0x80050208, -2147155448|The service bus call failed because the request payload has exceeded maximum allowed size. Please reduce your request size and retry.|
> |ServiceBusPostDisabled|0x8004417A, -2147204742|Service bus post is disabled for the organization.|
> |ServiceBusPostFailed|0x80044175, -2147204747|The service bus post failed.|
> |ServiceBusPostPostponed|0x80044179, -2147204743|Service bus post is being postponed.|
> |ServiceEndpointAcsAuthNotSupported|0x80050209, -2147155447|Service Endpoint with ACS authentication type is no longer supported. Please change your endpoint configuration to use a supported authentication type|
> |ServiceInstantiationFailed|0x80040244, -2147220924|Instantiation of an Entity failed.|
> |SessionTokenUnavailable|0x80040253, -2147220909|Session token is not available unless there is a transaction in place.|
> |SetActiveNotSupportedOnNewRecords|0x80060374, -2147089548|SetActiveProcess is not supported on new records.|
> |SharePointAbsoluteAndRelativeUrlEmpty|0x80048149, -2147188407|Both absolute URL and relative URL cannot be null.|
> |SharePointAuthenticationFailure|0x800608B3, -2147088205|Microsoft Dynamics 365 cannot authenticate this user {0} . Verify that the information for this user is correct, and then try again.|
> |SharePointAuthorizationFailure|0x800608B4, -2147088204|Microsoft Dynamics 365 cannot authorize this user {0} . Verify that the information for this user is correct, and then try again.|
> |SharePointCertificateExpired|0x800608B1, -2147088207|Certificate used for Sharepoint validation has expired|
> |SharePointConnectionFailure|0x800608B5, -2147088203|Microsoft Dynamics 365 cannot connect this user {0} to SharePoint. Verify that the information for this user is correct and exists in SharePoint, and then try again.|
> |SharePointCrmDomainValidator|0x8004F302, -2147159294|The SharePoint and Microsoft Dynamics 365 Servers are on different domains. Please ensure a trust relationship between the two domains.|
> |SharePointCrmGridIsInstalledValidator|0x8004F309, -2147159287|The Microsoft Dynamics 365 Grid component must be installed on the SharePoint server. This component is required for SharePoint integration to work correctly.|
> |SharePointErrorAbsoluteUrlClipped|0x8004F314, -2147159276|The URL exceeds the maximum number of 256 characters. Use shorter names for sites and folders, and try again.|
> |SharePointErrorRetrieveAbsoluteUrl|0x8004F310, -2147159280|An error occurred while retrieving the absolute and site collection url for a SharePoint object.|
> |SharePointInvalidEntityForValidation|0x8004F311, -2147159279|Entity Does not support SharePoint Url Validation.|
> |SharePointRealmMismatch|0x800608B2, -2147088206|Sharepoint realm ID entered does not match with the registered realm at Sharepoint side.|
> |SharePointRecordWithDuplicateUrl|0x80048057, -2147188649|There is already a record with the same Url.|
> |SharePointRoleProvisionJobAlreadyExists|0x8004F0FA, -2147159814|A system job to provision the selected security role is pending. Any changes made to the security role record before this system job starts will be applied to this system job.|
> |SharePointS2SIsDisabled|0x80071017, -2147020777|SharePoint server-based SharePoint integration not enabled.|
> |SharePointServerDiscoveryValidator|0x8004F303, -2147159293|The URL is incorrect or the site is not running.|
> |SharePointServerLanguageValidator|0x8004F308, -2147159288|Microsoft Dynamics 365 and Microsoft Office SharePoint Server must have the same base language.|
> |SharePointServerVersionValidator|0x8004F304, -2147159292|The SharePoint Site Collection must be running a supported version of Microsoft Office SharePoint Server or Microsoft Windows SharePoint Services. Please refer the implementation guide.|
> |SharePointSiteCollectionIsAccessibleValidator|0x8004F305, -2147159291|The URL is incorrect or the site is not running.|
> |SharePointSiteCreationFailure|0x8004F0F8, -2147159816|Failed to create the site {0} in SharePoint.|
> |SharePointSiteNotConfigured|0x80071014, -2147020780|SharePointSite is not configured, it need to be configured.|
> |SharePointSiteNotPresentInSharePoint|0x8004F0F3, -2147159821|Site {0} does not exists in SharePoint.|
> |SharePointSitePermissionsValidator|0x8004F307, -2147159289|The current user does not have the appropriate privileges. You must be a SharePoint site administrator on the SharePoint site.|
> |SharePointSiteWideProvisioningJobFailed|0x8004F0FB, -2147159813|SharePoint provisioning job has failed.|
> |SharePointTeamProvisionJobAlreadyExists|0x8004F0F9, -2147159815|A system job to provision the selected team is pending. Any changes made to the team record before this system job starts will be applied to this system job.|
> |SharePointUnableToAclSite|0x8004F0F6, -2147159818|Unable to ACL site {0} in SharePoint.|
> |SharePointUnableToAclSiteWithPrivilege|0x8004F0F5, -2147159819|Unable to ACL site {0} with privilege {1} in SharePoint.|
> |SharePointUnableToAddUserToGroup|0x8004F0F1, -2147159823|Microsoft Dynamics 365 cannot add this user {0} to the group {1} in SharePoint. Verify that the information for this user and group are correct and that the group exists in SharePoint, and then try again.|
> |SharePointUnableToCreateSiteGroup|0x8004F0F7, -2147159817|Unable to create site group {0} in SharePoint.|
> |SharePointUnableToRemoveUserFromGroup|0x8004F0F2, -2147159822|Unable to remove user {0} from group {1} in SharePoint.|
> |SharePointUnableToRetrieveGroup|0x8004F0F4, -2147159820|Unable to retrieve the group {0} from SharePoint.|
> |SharePointUrlHostValidator|0x8004F301, -2147159295|The URL cannot be resolved into an IP.|
> |SharePointUrlIsRootWebValidator|0x8004F306, -2147159290|The URL is not valid. The URL must be a valid site collection and cannot include a subsite. The URL must be in a valid form, such as http://SharePointServer/sites/CrmSite.|
> |SharePointVersionUnsupported|0x800608B6, -2147088202|Microsoft Dynamics 365 cannot connect to Sharepoint as the Sharepoint Version is unsupported. Install the correct version, and then try again. |
> |SimilarityRuleDisabled|0x80071016, -2147020778|No similarity rule active for this entity.|
> |SimilarityRuleFCBOff|0x80071018, -2147020776|Similarity rules not enabled.|
> |SimplePropertyCannotHaveChildNodes|0x80160040, -2146041792|Simple property {0} cannot have child nodes. More Details:{1}|
> |SingletonMappingFoundForArrayParameter|0x8004037e, -2147220610|A single transformation parameter mapping is defined for an array parameter.|
> |SiteMapMissing|0x80050016, -2147155946|You don’t have permissions for these records or something may be wrong with the site map. Contact your system administrator.If you are the administrator, you can go to the solutions page and import a different solution.|
> |SiteMapSettingsAreaMissing|0x80090010, -2146893808|Settings area with id = "Settings" is missing from default sitemap, add a settings area or update to "Settings" from sitemap designer and try again.|
> |SiteMapXsdValidationError|0x8004F401, -2147159039|Sitemap xml failed XSD validation with the following error: '{0}' at line {1} position {2}.|
> |SkipValidDateTimeBehavior|0x800608A3, -2147088221|The behavior value for this field was ignored. A System Customizer will need to configure the behavior value for this field directly.|
> |SlaActivateDeactivateByNonOwner|0x8004F872, -2147157902|This SLA cannot be activated or deactivated by someone who is not its owner.|
> |SlaAlreadyInactiveState|0x8004F861, -2147157919|You can't activate this record because it's already active.|
> |SlaAlreadyInDraftState|0x8004F862, -2147157918|You can't deactivate this record because it's in a draft state.|
> |SlaItemDeleteOperationError|0x80055011, -2147135471|SLAItem delete operation encountered some errors. {0}, see log for more detail. Please contact your system administrator.|
> |SlaNotEnabledEntity|0x80055003, -2147135485|SLA is not enabled for this entity.|
> |SlaPermissionToPerformAction|0x8004F875, -2147157899|You don't have the required permissions on SLAs and processes to perform this action.|
> |SlaServiceActivateWorkflowError|0x80055010, -2147135472|Error while activating workflow. Please correct the workflow and try again or reach out to Dynamics 365 customer support.|
> |SnapshotReportNotReady|0x80040489, -2147220343|The selected report is not ready for viewing. The report is still being created or a report snapshot is not available. ReportId:{0}|
> |SocialCareDisabledError|0x80060621, -2147088863|There's a problem communicating with the Dynamics 365 Organization. The organization might be unavailable or the feature is set so that it can't receive social data. Try again later. If the problem persists, contact your Microsoft Dynamics 365 administrator.|
> |SolutionComponentDefinitionNotAvailable|0x8007200A, -2147016694|Cannot create component definition for solution-aware entity {0}.|
> |SolutionConcurrencyFailure|0x80071151, -2147020463|The solution installation or removal failed due to the installation or removal of another solution at the same time. Please try again later.|
> |SolutionConfigurationPageMustBeHtmlWebResource|0x8004701C, -2147192804|The solution configuration page must exist within the solution it represents.|
> |SolutionImportCauseTimeout|0x80048543, -2147187389|The operation timed out. This may be because a solution is currently being imported into this environment. Please try again after the solution import is completed. Solutions should be imported outside of working hours if possible.|
> |SolutionRestrictedAttributes|0x80072003, -2147016701|Component cannot be created because it already has solution-aware columns. Entity: {0}, Existing Attribute: {1}|
> |SolutionUniqueNameViolation|0x8004F023, -2147160029|The solution unique name '{0}' is already being used and cannot be used again.|
> |SolutionUpgradeFailed|0x8004F046, -2147159994|Solution Upgrade action failed after import as holding. InnerException is: {1}.|
> |SolutionUpgradeNotAvailable|0x8004853B, -2147187397|"The {0} solution doesn’t have an upgrade that is ready to be applied."|
> |SolutionUpgradeOfApiManagedSolutionError|0x8004803C, -2147188676|The import has failed because an ApiManaged solution cannot be updated.|
> |SolutionUpgradeWrongSolutionSelected|0x8004853C, -2147187396|"To use this action, you must first select the old solution and then try again."|
> |SourceAttributeHeaderTooBig|0x80044340, -2147204288|Column headers must be 160 or fewer characters. Fix the column headers, and then run Data Migration Manager again.|
> |SourceEntityMappedToMultipleTargets|0x8004033d, -2147220675|This source entity is mapped to more than one Microsoft Dynamics 365 entity. Remove any duplicate mappings, and then import this data map again.|
> |SPAccountNameFetchFailure|0x8006072A, -2147088598|Exception occured while fetching account name from Sharepoint.|
> |SPAllFilesErrorScenario|0x80060760, -2147088544|One or more sites in all files view of SharePointDocument failed.|
> |SPBadLockInFileCollectionErrorCode|0x8006070A, -2147088630|The file in the collection has bad lock |
> |SPCertificationError|0x80060767, -2147088537|S2STokenIssuer certificate not found.|
> |SPConnectionFailure|0x80060761, -2147088543|Failed to connect to SharePointSite.|
> |SPCurrentDocumentLocationDisabledErrorCode|0x80060720, -2147088608|Current document location is disabled by administrator|
> |SPCurrentFolderAlreadyExistErrorCode|0x80060721, -2147088607|Record already present in db|
> |SPDataValidationFiledOnFieldAndListErrorCode|0x80060713, -2147088621|Data validation has failed on the field and the list|
> |SPDataValidationFiledOnFieldErrorCode|0x80060711, -2147088623|Data validation has failed on the field|
> |SPDataValidationFiledOnListErrorCode|0x80060712, -2147088622|Data validation has failed on the list|
> |SPDefaultSiteNotPresent|0x80060739, -2147088583|OneDrive activation needs a default SharePoint site.|
> |SPDocumentLibraryMissingErrorCode|0x8006073C, -2147088580|Document library {0} has been renamed or deleted from SharePoint site {1}. Rerun the document management wizard and try again|
> |SPDocumentMappingFailure|0x80060734, -2147088588|Can't map documents to their location.|
> |SPDuplicateValuesFoundErrorCode|0x80060708, -2147088632|The list item could not be updated because duplicate values were found for one or more field(s) in the list|
> |SpecifyIncomingPassword|0x8005E253, -2147098029|Specify password for Incoming Connection|
> |SpecifyInComingPort|0x8005E24F, -2147098033|Specify Incomming Port and save again|
> |SpecifyIncomingServerLocation|0x8005E24B, -2147098037|Specify the URL of the incoming server location|
> |SpecifyIncomingUserName|0x8005E251, -2147098031|Specify username for Incoming Connection|
> |SpecifyOutgoingPassword|0x8005E254, -2147098028|Specify password for Outgoing Connection|
> |SpecifyOutgoingPort|0x8005E256, -2147098026|Specify Outgoing Port and save again|
> |SpecifyOutgoingServerLocation|0x8005E24C, -2147098036|Specify the URL of the outgoing server location|
> |SpecifyOutgoingUserName|0x8005E252, -2147098030|Specify username for Outgoing Connection|
> |SPExclusiveLockOnFileErrorCode|0x80060705, -2147088635|Exclusive lock on the file|
> |SPFileAlreadyCheckedOutErrorCode|0x80060702, -2147088638|File is already checked out|
> |SPFileCheckedOutInvalidArgsErrorCode|0x80060703, -2147088637|Checkout arguments are not valid|
> |SPFileContentNullErrorCode|0x8006070D, -2147088627|Content of the file creation information must not be null|
> |SPFileIsCheckedOutByOtherUser|0x80060728, -2147088600|File is checked out to a user other than the current user|
> |SPFileIsReadOnlyErrorCode|0x8006070F, -2147088625|Field is read-only|
> |SPFileNameModifiedErrorCode|0x80060729, -2147088599|The folder can't be found. If you changed the automatically generated folder name for this document location directly in SharePoint, you must change the folder name in Dynamics 365 to match the renamed folder. To do this, select Edit Location and type the matching name in Folder Name field.|
> |SPFileNotCheckedOutErrorCode|0x80060700, -2147088640|File is not checked out|
> |SPFileNotFoundErrorCode|0x80060706, -2147088634|File cannot be found|
> |SPFileNotLockedErrorCode|0x80060707, -2147088633|The file in the collection is not locked|
> |SPFileSizeMismatchErrorCode|0x8006070E, -2147088626|There is a mismatch between the size of the document stream written and the size of the input document stream|
> |SPFileTooLargeOrInfectedErrorCode|0x80060709, -2147088631|Virus checking indicates the file is infected with a virus or the file is too large|
> |SPFolderCreationFailure|0x8004F0F0, -2147159824|Cannot Create Folder with this name|
> |SPFolderMissingErrorCode|0x8006073D, -2147088579|Folder {0} has been renamed or deleted from SharePoint. It was expected inside {1} path. Restore the folder on SharePoint and try again|
> |SPFolderNotFoundErrorCode|0x8006071B, -2147088613|Folder Not Found|
> |SPFolderRenameFailure|0x8006072C, -2147088596|Exception occurred while Editing Sharepoint Document Proeprties.|
> |SPGenericErrorCode|0x80060719, -2147088615|Error while doing this operation on SharePoint|
> |SPIllegalCharactersInFileNameErrorCode|0x8006071F, -2147088609|Illegal characters in filename|
> |SPIllegalFileTypeErrorCode|0x8006071D, -2147088611|Illegal file type|
> |SPInstanceOfRecurringEventErrorCode|0x80060716, -2147088618|List item is an instance of a recurring event which is not a recurrence exception, the list item is a workflow task whose parent workflow is in the recycle bin, or the parent list is a document library|
> |SPIntermittentError|0x80060764, -2147088540|Intermittent error occured. Please refresh the grid and try again|
> |SPInvalidDocumentLocation|0x80060762, -2147088542|Invalid Sharepoint Document Location type|
> |SPInvalidFieldValueErrorCode|0x8006071E, -2147088610|Invalid Field Value|
> |SPInvalidLookupValuesErrorCode|0x8006070B, -2147088629|List item could not be updated because invalid lookup values were found for one or more field(s) in the list|
> |SPInvalidSavedQueryErrorCode|0x80060718, -2147088616|Error while doing this operation on SharePoint|
> |SPInvalidSubSite|0x80060763, -2147088541|SubSite url is incorrectly formed|
> |SPItemNotExistErrorCode|0x80060717, -2147088617|List item does not exist|
> |SPMalFormedRelativeUrl|0x80060766, -2147088538|Relative URL should not have preceding or trailing spaces.|
> |SPModifiedOnServerErrorCode|0x80060710, -2147088624|List item was modified on the server so changes cannot be committed|
> |SPMultipleOdbSitesError|0x8006072D, -2147088595|More than one site with One Drive enabled is not allowed.|
> |SPNoActiveDocumentLocationErrorCode|0x8006071C, -2147088612|No Active Document Location|
> |SPNotAdminError|0x80060765, -2147088539|Only crm admin who is tenant admin can perform create operation|
> |SPNotEnabledError|0x8006073A, -2147088582|SharePoint integration is not enabled on Entity|
> |SPNotEnabledForEntity|0x8006073B, -2147088581|SharePoint Integration and Microsoft Teams Integration is not enabled on Entity|
> |SPNullFileUrlErrorCode|0x8006070C, -2147088628|URL of the file creation information must not be null and URL of the file creation information must not be invalid|
> |SPNullRegardingObjectErrorCode|0x80060723, -2147088605|Regarding object id is null|
> |SPOdbDisabledError|0x8006072E, -2147088594|Please enable ODB(One Drive for Business) feature to create ODB site.|
> |SPOdbDuplicateLocationError|0x80060735, -2147088587|More than one ODB (OneDrive for Business) location is not allowed.|
> |SPOdbUpdateDeleteError|0x8006072F, -2147088593|You cannot update or delete ODB(One Drive for Business) site.|
> |SPOdbUpdateDeleteLocationError|0x80060736, -2147088586|You cannot update or delete SharePoint Document Location of type ODB (OneDrive for Business).|
> |SPOperationNotSupportedErrorCode|0x80060715, -2147088619|List does not support this operation|
> |SPOperatorNotSupportedErrorCode|0x80060724, -2147088604|{0} does not support the selected operator|
> |SPPersonalSiteNotFound|0x8006072B, -2147088597|Personal Site not found for the user.|
> |SPRequiredColCheckInErrorCode|0x80060725, -2147088603|Exception occurred while doing document check-in as some columns are made required at SharePoint|
> |SPSearchOneDriveNotCreated|0x80060737, -2147088585|OneDrive location is not created yet. Please create the location before searching.|
> |SPSharedLockOnFileErrorCode|0x80060704, -2147088636|Shared lock on the file|
> |SPSiteNotFoundErrorCode|0x8006071A, -2147088614|Site Not Found|
> |SPSiteProtocolError|0x80060738, -2147088584|Protocol error in accessing SharePoint|
> |SPSiteUrlNullOrEmpty|0x80060768, -2147088536|Siteurl cannot be null or empty. Please ensure valid SharePoint site is configured or contact your administrator.|
> |SPThrottlingLimitExceededErrorCode|0x80060714, -2147088620|Throttling limit is exceeded by the operation|
> |SPUnauthorizedAccessErrorCode|0x80060701, -2147088639|Current user have insufficient privileges|
> |SPUploadFailure|0x80060740, -2147088576|Upload failed on SharePoint due to unknown reasons. Probably the file is too large|
> |SqlArithmeticOverflowError|0x80041136, -2147217098|A SQL arithmetic overflow error occurred|
> |SqlEncryption|0x80048518, -2147187432|There was an error in Data Encryption.|
> |SqlEncryptionCannotOpenSymmetricKeyBecauseDatabaseMasterKeyDoesNotExistOrIsNotOpened|0x8004851A, -2147187430|Cannot open Symmetric Key because Database Master Key does not exist in the database or is not opened.|
> |SqlEncryptionCertificateDoesNotExist|0x8004851D, -2147187427|Certificate with Name='{0}' does not exist in the database.|
> |SqlEncryptionChangeEncryptionKeyExceededQuotaForTheInterval|0x80048529, -2147187415|'Change' encryption key has already been executed {0} times in the last {1} minutes. Please wait a couple of minutes and then try again.|
> |SqlEncryptionCreateCertificateError|0x8004851E, -2147187426|Cannot create Certificate with Name='{0}' because it already exists.|
> |SqlEncryptionCreateDatabaseMasterKeyError|0x8004851B, -2147187429|Cannot create Database Master Key because already exists.|
> |SqlEncryptionCreateSymmetricKeyError|0x80048521, -2147187423|Cannot create Symmetric Key with Name='{0}' because it already exists.|
> |SqlEncryptionDatabaseMasterKeyDoesNotExist|0x80048519, -2147187431|Database Master Key does not exist in the database.|
> |SqlEncryptionDeleteCertificateError|0x8004851F, -2147187425|Cannot delete Certificate with Name='{0}' because it does not exist.|
> |SqlEncryptionDeleteDatabaseMasterKeyError|0x8004851C, -2147187428|Cannot delete Database Master Key because it does not exist.|
> |SqlEncryptionDeleteEncryptionKeyError|0x80048526, -2147187418|Cannot delete the encryption key.|
> |SqlEncryptionDeleteSymmetricKeyError|0x80048522, -2147187422|Cannot delete Symmetric Key with Name='{0}' because it does not exist.|
> |SqlEncryptionEncryptionDecryptionTestError|0x80048523, -2147187421|Error while testing data encryption and decryption.|
> |SqlEncryptionEncryptionKeyValidationError|0x80048528, -2147187416|The new encryption key does not meet the strong encryption key requirements. The key must be between 10 and 100 characters in length, and must have at least one numeral, at least one letter, and one symbol or special character. {0}|
> |SqlEncryptionIsActiveCannotRestoreEncryptionKey|0x80048525, -2147187419|Cannot perform 'activate' encryption key because the encryption key is already set and is working. Use 'change' encryption key instead.|
> |SqlEncryptionIsInactiveCannotChangeEncryptionKey|0x80048527, -2147187417|Cannot perform 'change' encryption key because the encryption key is not already set or is not working. First use 'activate' encryption key instead to set the correct current encryption key and then use 'change' encryption if you want to re-encrypt data using a new encryption key.|
> |SqlEncryptionKeyCannotDecryptExistingData|0x80048524, -2147187420|Cannot decrypt existing encrypted data (Entity='{0}', Attribute='{1}') using the current encryption key. Use 'activate' encryption key to set the correct encryption key.|
> |SqlEncryptionRestoreEncryptionKeyCannotDecryptExistingData|0x8004852B, -2147187413|Cannot perform 'activate' because the encryption key doesn’t match the original encryption key that was used to encrypt the data.|
> |SqlEncryptionSetEncryptionKeyIsAlreadyRunningCannotRunItInParallel|0x8004852A, -2147187414|The system is currently running a request to 'change' or 'activate' the encryption key. Please wait before making another request.|
> |SqlEncryptionSymmetricKeyCannotOpenBecauseWrongPassword|0x80048530, -2147187408|Cannot open encryption Symmetric Key because the password is wrong.|
> |SqlEncryptionSymmetricKeyDoesNotExist|0x80048520, -2147187424|Symmetric Key with Name='{0}' does not exist in the database.|
> |SqlEncryptionSymmetricKeyDoesNotExistOrNoPermission|0x8004852F, -2147187409|Cannot open encryption Symmetric Key because it does not exist in the database or user does not have permission.|
> |SqlEncryptionSymmetricKeyPasswordDoesNotExistInConfigDB|0x8004852E, -2147187410|Encryption Symmetric Key password does not exist in Config DB.|
> |SqlEncryptionSymmetricKeySourceDoesNotExistInConfigDB|0x8004852D, -2147187411|Encryption Symmetric Key Source does not exist in Config DB.|
> |SqlErrorInStoredProcedure|0x8004C001, -2147172351|SQL error {0} occurred in stored procedure {1}|
> |SqlMaxRecursionExceeded|0x80044157, -2147204777|The maximum recursion has reached before statement completion.|
> |SrsDataConnectorNotInstalled|0x80040492, -2147220334|MSCRM Data Connector Not Installed|
> |SrsDataConnectorNotInstalledUpload|0x80048292, -2147188078|This report can’t upload because Dynamics 365 Reporting Extensions, required components for reporting, are not installed on the server that is running Microsoft SQL Server Reporting Services.|
> |SSM_MaxPCI_Exceeded|0x80072570, -2147015312|Please re-login to refresh your session.|
> |SSM_RefreshToken_Failed|0x80072571, -2147015311|Failed to refresh login session.|
> |StageEntityIsNull|0x80060451, -2147089327|Validation error: stage entity cannot be null.|
> |StageIdIsEmpty|0x80060454, -2147089324|Validation error: Stage ID cannot be empty.|
> |StageIdIsNotPresentInBusinessProcess|0x80060450, -2147089328|Validation error: Stage ID ‘{0}’ is not present in Business Process. Please contact your system administrator.|
> |StageIdIsNotValid|0x80060458, -2147089320|Validation error: Stage ID is not valid for Business Process.|
> |StandAloneBpfNotActivated|0x80060470, -2147089296|Stand Alone BPF must be activated on Flows page.|
> |StandardSlaTypeNotApplicable|0x80055006, -2147135482|Standard SLA Type is only supported for incident entity. Current entity object type code is {0}. Please pass appropriate SLA Type or entity|
> |StateTransitionActivateNewStatus|0x8004F857, -2147157929|You can't activate this record because of the status transition rules.Contact your system administrator.|
> |StateTransitionActiveToCanceled|0x8004F855, -2147157931|Because of the status transition rules, you can't cancel the case in the current status.Change the case status, and then try canceling it, or contact your system administrator.|
> |StateTransitionActiveToResolve|0x8004F854, -2147157932|Because of the status transition rules, you can't resolve a case in the current status.Change the case status, and then try resolving it, or contact your system administrator.|
> |StateTransitionDeactivateNewStatus|0x8004F858, -2147157928|You can't deactivate this record because of the status transition rules.Contact your system administrator.|
> |StateTransitionResolvedOrCanceledToActive|0x8004F856, -2147157930|Because of the status transition rules, you can't activate the case from the current status.Contact your system administrator.|
> |StaticPropertyCannotBeDeclared|0x80160030, -2146041808|Property {0} is configured as a static value and cannot be declared as {1}. More Details:{2}|
> |StaticPropertyTypeIsMissing|0x80160027, -2146041817|The type of static property {0} is missing Give a type appropriate for the static value given. More Details:{1}|
> |StaticPropertyTypeMismatch|0x80160042, -2146041790|The type declared for property {0} (type {1}) on the control manifest does not match the type(s){2} of value provided to it. More Details:{3}|
> |StaticPropertyValueHasTypeMismatch|0x80160028, -2146041816|The static value configured for property {0} cannot be parsed to type {1}. More Details:{2}|
> |StepAutomaticallyDisabled|0x80045043, -2147200957|The original sdkmessageprocessingstep has been disabled and replaced.|
> |StepCountInXamlExceedsMaxAllowed|0x80060414, -2147089388|There are {0} {1} in the Xaml. Max allowed is {2}.|
> |StepDoesNotHaveAnyChildInXaml|0x80060416, -2147089386|{0} does not have at least one {1} as its child.|
> |StepNotSupportedForClientBusinessRule|0x80060000, -2147090432|Step {0} is not supported for client side business rule.|
> |StepStepDoesNotHaveAnyControlStepAsItsChildren|0x80060409, -2147089399|StepStep does not have any ControlStep as its children|
> |StoredProcedureContext|0x8004C002, -2147172350|Dynamics 365 error {0} in {1}:{2}|
> |StoreLocationNotSupported|0x80090108, -2146893560|An invalid store location was provided for the data type with Id = '{0}', Name = '{1}', and DisplayName = '{2}'. The store location '{3}' is not supported. Please provide a valid store location and try again.|
> |StringAttributeIndexError|0x8004D292, -2147167598|One of the attributes of the selected entity is a part of database index and so it cannot be greater than 900 bytes.|
> |StringLengthTooLong|0x80044331, -2147204303|A validation error occurred. A string value provided is too long.|
> |SubcomponentDoesNotExist|0x80048537, -2147187401|Subcomponent {0} of type {1} is not found in the organization, it can not be added to the SolutionComponents.|
> |SubcomponentMissingARoot|0x80048536, -2147187402|Subcomponent {0} cannot be added to the solution because the root component {1} is missing.|
> |SubjectDoesNotExist|0x80043e02, -2147205630|Subject does not exist.|
> |SubjectLoopBeingCreated|0x80043e01, -2147205631|Creating this parental association would create a loop in Subjects hierarchy.|
> |SubjectLoopExists|0x80043e00, -2147205632|Loop exists in the subjects hierarchy.|
> |SubReportDoesNotExist|0x80040493, -2147220333|Subreport does not exist. ReportId:{0}|
> |SubscriptionGone|0x80072513, -2147015405|Subscription expired|
> |SupportLogOnExpired|0x8004A108, -2147180280|Support login is expired|
> |SupportUserCannotBeCreateNorUpdated|0x80041d41, -2147214015|The support user cannot be updated|
> |SyncAttributeMappingCannotBeUpdated|0x80060741, -2147088575|The sync attribute mapping cannot be updated.|
> |SyncToMsdeFailure|0x80048407, -2147187705|Failed to start or connect to the offline mode MSDE database.|
> |SystemAttributeMap|0x80046205, -2147196411|Cannot create or delete system attribute map having id {0} from {1} to {2} belonging to an entity map with id {3} from {4} to {5}.|
> |SystemEntityMap|0x80046202, -2147196414|SystemEntityMap Error Occurred|
> |SystemFormCopyUnmatchedEntity|0x8004F656, -2147158442|The entity for the Target and the SourceId must match.|
> |SystemFormCopyUnmatchedFormType|0x8004F657, -2147158441|The form type of the SourceId is not valid for the Target entity.|
> |SystemFormCreateWithExistingLabel|0x8004F658, -2147158440|The label '{0}', id: '{1}' already exists. Supply unique labelid values.|
> |SystemFormImportMissingRoles|0x8004F655, -2147158443|The unmanaged solution you are importing has displaycondition XML attributes that refer to security roles that are missing from the target system. Any displaycondition attributes that refer to these security roles will be removed.|
> |SystemUserDisabled|0x8004A112, -2147180270|The system user was disabled therefore the ticket expired.|
> |TamperedAuthTicket|0x8004A105, -2147180283|The ticket specified for authentication has been tampered with or invalidated.|
> |TargetAttributeInvalidForIgnore|0x80048500, -2147187456|Target attribute name should be empty when the processcode is ignore.|
> |TargetAttributeInvalidForMap|0x80040394, -2147220588|This attribute is not valid for mapping.|
> |TargetAttributeNotFound|0x80040392, -2147220590|The file specifies an attribute that does not exist in Microsoft Dynamics 365.|
> |TargetEntityInvalidForMap|0x80040395, -2147220587|The file specifies an entity that is not valid for data migration.|
> |TargetEntityNotFound|0x80040391, -2147220591|The file specifies an entity that does not exist in Microsoft Dynamics 365.|
> |TargetEntityNotMapped|0x80048460, -2147187616|Target Entity Name not defined for source:{0} file.|
> |TargetUserInsufficientPrivileges|0x80048342, -2147187902|The user can't be added to the team because the user doesn't have the "{0}" privilege.|
> |TaskFlowEmptyName|0x80061712, -2147084526|The name field cannot be empty. Please enter a name.|
> |TaskFlowEntityAttributeIsNotValid|0x80061717, -2147084521|Invalid attribute type: {0}.{1}.|
> |TaskFlowEntityRelationshipIsNotValid|0x80061716, -2147084522|Invalid relationship type: {0}.|
> |TaskFlowFormXmlNotFound|0x80061713, -2147084525|Could not find the system form {0} for Task flow {1}.|
> |TaskFlowInvalidCharactersInName|0x80061711, -2147084527|The name field can only contain alphanumeric characters.|
> |TaskFlowMaxNumberControls|0x80061719, -2147084519|The task flow has exceeded the maximum number of controls allowed ({0}). To continue, you need to remove some controls.|
> |TaskFlowMaxNumberPages|0x80061718, -2147084520|The task flow has exceeded the maximum number of pages allowed ({0}). To continue, you need to remove some pages.|
> |TaskFlowNameIsNotUnique|0x80061710, -2147084528|A task flow with the specified name already exists.  Please specify a unique name.|
> |TaskFlowNotFound|0x80061720, -2147084512|A Task Flow which is trying to launch is not available on this device. You may not have permission to access it or it may not be available on your organization. Please contact your system administrator.|
> |TaskFlowNotValid|0x8006172F, -2147084497|Task flow definition is invalid.|
> |TaskFlowPageMissingFormXmlTab|0x80061714, -2147084524|Could not find the pages {0} for Task flow {1} Step {2}.|
> |TaskFlowUnsupportedEntities|0x80061715, -2147084523|The following entities are not enabled for Task flows: {0}.|
> |TDSClientUnsupported|0x80041211, -2147216879|TDS protocol endpoint is not supported for this application.|
> |TeamAdministratorMissedPrivilege|0x80041d0a, -2147214070|The team administrator does not have privilege read team.|
> |TeamInWrongBusiness|0x8004140d, -2147216371|Cannot associate security role because the security role's Business Unit is not the same as the team's Business Unit. Details: userid={0}, userBU={1}, roleId={2}, roleBU={3}|
> |TeamNameTooLong|0x80048305, -2147187963|The specified name for the team is too long.|
> |TeamNotAssignedRoles|0x80042f0a, -2147209462|The team has not been assigned any roles.|
> |TemplateNotAllowedForInternetMarketing|0x80048475, -2147187595|Creating Templates with Internet Marketing Campaign Activities is not allowed|
> |TemplateTypeNotSupportedForUnsubscribeAcknowledgement|0x80040324, -2147220700|This template type is not supported for unsubscribe acknowledgement.|
> |TenantIDIsEmpty|0x8005E25A, -2147098022|Exchange Online Tenant ID field cannot be empty.|
> |TenantIDValueChanged|0x8005E25C, -2147098020|The detected tenantId for your exchange is different than the once you saved.|
> |TestAndEnableInAdministrationModeNotAllowed|0x8005E257, -2147098025|Test and enable is not allowed if the organization is in administration mode.|
> |TestEmailConfigurationScheduledInProgress|0x8005E248, -2147098040|Test email configuration scheduled is in progress. Please save after completion of test.|
> |TextAnalyticsAPIActiveConfigurationDoesNotExist|0x80061690, -2147084656|Active configuration does not exist for entity.|
> |TextAnalyticsAPIActiveSimilarityConfigurationDoesNotExist|0x80061695, -2147084651|No active similarity rule exists. The system administrator must set up a similarity rule configuration.|
> |TextAnalyticsAPIAllowedOnlyForEnglishLanguage|0x80061691, -2147084655|Text Analytics feature is available for organizations with base language as English.|
> |TextAnalyticsAPIAzureUnableToConnectWithBuild|0x80061692, -2147084654|Dynamics 365 failed to connect with the Azure text analytics service. Verify that the service URI and account key are valid, and the Azure subscription is active.|
> |TextAnalyticsAzureConnectionCascadeActivateFailed|0x80061634, -2147084748|One or more text analytics models couldn't be activated. Try activating the existing text analytics models separately from the Azure service connection.|
> |TextAnalyticsAzureConnectionFailed|0x80061650, -2147084720|Unable to connect to Text Analytics API.|
> |TextAnalyticsAzureSchedulerError|0x80061693, -2147084653|Dynamics 365 failed to connect with the Azure text analytics service. Please try again and if the problem persists contact your system administrator.|
> |TextAnalyticsAzureTestConnectionFailed|0x80061632, -2147084750|Failed to connect to the Azure Text Analytics service. Check that the service URL and the Azure account key are valid and the service subscription is active.|
> |TextAnalyticsAzureUnableToConnectWithBuild|0x80061655, -2147084715|Dynamics 365 failed to connect with the Azure text analytics service. Verify that the service URI and account key are valid, and the Azure subscription is active.|
> |TextAnalyticsFeatureNotEnabled|0x80061652, -2147084718|The Azure Text Analytics feature isn’t activated. The system administrator must activate this feature and set up the required configuration.|
> |TextAnalyticsMappingUsedForActiveConfiguration|0x80061667, -2147084697|This text analytics entity mapping is used for an active configuration. It can’t be modified or deleted while it is used by an active config.|
> |TextAnalyticsMaxLimitForTopicModelReached|0x80061694, -2147084652|Maximum number of topic models allowed for your organization has been reached.|
> |TextAnalyticsModelActivateConnectionMustBeActive|0x80061657, -2147084713|The Azure Machine Learning Text Analytics service connection must be activated before the model can be activated. Please activate the text analytics service connection and try again.|
> |ThemeIdOrUpdateTimestampIsNull|0x800608D1, -2147088175|Theme Id or Update Timestamp value is not present in theme data.|
> |Throttling|0x8005F103, -2147094269|Too many requests.|
> |ThrottlingBurstRequestLimitExceededError|0x80072322, -2147015902|Number of requests exceeded the limit of {0} over time window of {1} seconds.|
> |ThrottlingConcurrencyLimitExceededError|0x80072326, -2147015898|Number of concurrent requests exceeded the limit of {0}.|
> |ThrottlingTimeExceededError|0x80072321, -2147015903|Combined execution time of incoming requests exceeded limit of {0} milliseconds over time window of {1} seconds. Decrease number of concurrent requests or reduce the duration of requests and try again later.|
> |TooManyBytesInInputStream|0x8004F901, -2147157759|The stream being read from has too many bytes.|
> |TooManyCalculatedFieldsInQuery|0x80060429, -2147089367|Number of calculated fields in query exceeded maximum limit of {0}.|
> |TooManyConditionParametersInQuery|0x8004430E, -2147204338|Number of parameters in a condition exceeded maximum limit.|
> |TooManyConditionsInQuery|0x8004430C, -2147204340|Number of conditions in query exceeded maximum limit.|
> |TooManyEntitiesEnabledForAutoCreatedAccessTeams|0x80048332, -2147187918|Too many entities enabled for auto created access teams.|
> |TooManyLinkEntitiesInQuery|0x8004430D, -2147204339|Number of link entities in query exceeded maximum limit.|
> |TooManyModernFlowTriggersForExecute|0x80060477, -2147089289|Cannot execute Modern Flow '{0}' because more than one callback is registered.|
> |TooManyMultiSelectConditionParametersInQuery|0x80050223, -2147155421|Number of multiselect condition parameters in query exceeded maximum limit: {0}.|
> |TooManyPicklistValues|0x80048492, -2147187566|Number of distinct picklist values exceed the limit.|
> |TooManyRecipients|0x8004350e, -2147207922|Sending to multiple recipients is not supported.|
> |TooManySelectionsForAttributeType|0x80050222, -2147155422|Number of selections for MultiSelectPicklist Attribute Type exceeded maximum limit: {0}.|
> |TooManyTeamTemplatesForEntityAccessTeams|0x80048333, -2147187917|Current number of teams: {0} is greater than teams limit: {1} for entity with ObjectTypeCode {2}|
> |TopicModelActivateWithInvalidConfiguration|0x80061656, -2147084714|The configuration used for the build is invalid. Topic determination fields are required for the configuration used for topic analysis.|
> |TopicModelConfigurationAssociatedModelAlreadyActive|0x80061670, -2147084688|Cannot update or delete topic model configuration because it is associated with an active topic model.|
> |TopicModelConfigurationUsedEmpty|0x80061653, -2147084717|Activation requires specifying the build configuration. Specify the configuration used for the build before activation.|
> |TopicModelScheduleBuildSettingsEmpty|0x80061651, -2147084719|Activation requires setting the build schedule. Specify the schedule build settings before activation.|
> |TopicModelTestWithoutConfiguration|0x80061654, -2147084716|Specify the configuration used for the build.|
> |TraceMessageConstructionError|0x8004F900, -2147157760|The trace record has an invalid trace code or an insufficient number of trace parameters.|
> |TransactionAborted|0x80040255, -2147220907|Transaction Aborted.|
> |TransactionAbortedByIsvException|0x80048550, -2147187376|Transaction Aborted by ISV code exception in pre-commit stage. See inner exception for detailed information.|
> |TransactionNotCommited|0x80040252, -2147220910|Transaction not committed.|
> |TransactionNotStarted|0x80040251, -2147220911|Transaction not started.|
> |TransactionNotSupported|0x8005E007, -2147098617|The operation that you are trying to perform does not support transactions.|
> |TransformationResumeNotSupported|0x80048463, -2147187613|The resume/retry of Transformation job of Import is not supported.|
> |TransformMustBeCalledBeforeImport|0x80040335, -2147220683|Cannot call import before transform.|
> |TranslateArticle_OnlyPrimaryArticlesCanBeTranslated|0x80061402, -2147085310|This article is a translation of the original article. It cannot be translated again. If you want another translation, start with the original article rather than this one.|
> |TranslateArticle_TranslationCanNotBeCreatedForTheSameLanguage|0x80061403, -2147085309|A translation for this language already exists for this version of the article|
> |TrendingDocumentsDataRetrievalFailure|0x80044234, -2147204556|We can't get to the trending documents. Try again later.|
> |TrendingDocumentsIntegrationDisabledError|0x80044233, -2147204557|Trending Documents is disabled for your Microsoft Dynamics 365 account.|
> |TrendingDocumentsIntegrationTurnedOffError|0x80044255, -2147204523|Trending Documents is turned off. Please contact your system administrator to turn this feature on in System Settings.|
> |TrendingDocumentsOfflineModeError|0x80044258, -2147204520|Trending Documents isn't available in offline mode.|
> |TrendingDocumentsOnpremiseDeploymentError|0x80044232, -2147204558|The Trending Documents dashboard component isn't supported by your company's Microsoft Office service.|
> |TriggerFlowFailure|0x80050261, -2147155359|An error has occurred when trying to run this flow.|
> |TypeAttributeIsNotSupportedForStaticProperty|0x80160029, -2146041815|The type {0} is not supported for property {0}. More Details:{2}|
> |TypeNotSetToDefinition|0x80060402, -2147089406|Type should be set to Definition while creating business process flow category|
> |UIDataGenerationFailed|0x80045037, -2147200969|There was an error generating the UIData from XAML.|
> |UIDataMissingInWorkflow|0x80048471, -2147187599|The workflow does not contain UIData.|
> |UIScriptIdentifierDuplicate|0x8004F217, -2147159529|A variable or input argument with the same name already exists. Choose a different name, and try again.|
> |UIScriptIdentifierInvalid|0x8004F218, -2147159528|The variable or input argument name is invalid. The name can only contain '_', numerical, and alphabetical characters. Choose a different name, and try again.|
> |UIScriptIdentifierInvalidLength|0x8004F219, -2147159527|The variable or input argument name is too long. Choose a smaller name, and try again.|
> |UnableToActivateQuoteNotInDraft|0x80100003, -2146435069|The quote cannot be activated because it is not in draft state.|
> |UnableToLoadCustomActivity|0x8004505A, -2147200934|Unable to load the custom activity.|
> |UnableToLoadPluginAssembly|0x80044191, -2147204719|Unable to load plug-in assembly.|
> |UnableToLoadPluginType|0x80044190, -2147204720|Unable to load plug-in type.|
> |UnableToLoadTransformationAssembly|0x80040378, -2147220616|Unable to load the transformation assembly.|
> |UnableToLoadTransformationType|0x80040379, -2147220615|Unable to load the transformation type.|
> |UnableToLogOnUserFromUserNameAndPassword|0x80044311, -2147204335|The specified user name and password can not logon.|
> |UnableToRetrieveAttributeValueFromEntity|0x80040530, -2147220176|Unable to retrieve attribute '{0}' for entity '{1}'. Please provide a valid attribute name.|
> |UnableToSendEmail|0x8004B015, -2147176427|Some Internal error occurred in sending invitation, Please try again later|
> |UnapprovedMailbox|0x8005E220, -2147098080|The mailbox is not in approved state. Send/Receive mails are allowed only for approved mailboxes.|
> |UnauthorizedAccess|0x80040277, -2147220873|Attempted to perform an unauthorized operation.|
> |UnExpected|0x80040216, -2147220970|An unexpected error occurred.|
> |UnexpectedErrorInMailMerge|0x80040330, -2147220688|There was an unexpected error during mail merge.|
> |UnexpectedNullReferenceError|0x8004F044, -2147159996|Unexpected null reference error: {0}.|
> |UnexpectedRightOperandCount|0x80060006, -2147090426|The right operand array in the expression contain unexpected no. of operand.|
> |UnitDoesNotExist|0x80043b1b, -2147206373|The unit does not exist.|
> |UnitLoopBeingCreated|0x80043b1a, -2147206374|Using this base unit would create a loop in the unit hierarchy.|
> |UnitLoopExists|0x80043b19, -2147206375|Loop exists in the unit hierarchy.|
> |UnitNoName|0x80043b26, -2147206362|The unit name cannot be null.|
> |UnitNotInSchedule|0x80043b16, -2147206378|The unit does not exist in the specified unit schedule.|
> |UnknownInvalidTransformationParameterGeneric|0x80048513, -2147187437|One or more input transformation parameter values are invalid: {0}.|
> |unManagedchildentityisnotchild|0x800404e6, -2147220250|The child entity supplied is not a child.|
> |unManagedcihldofconditionforoffilefilters|0x800404a9, -2147220311|Child-of condition is only allowed on offline filters.|
> |UnmanagedComponentParentsManagedComponent|0x8004803B, -2147188677|Found {0} dependency records where unmanaged component is the parent of a managed component. First record (dependentcomponentobjectid = {1}, type = {2}, requiredcomponentobjectid = {3}, type= {4}, solution = {5}).|
> |unManagedemptyprocessliteralcondition|0x800404b0, -2147220304|No data specified for ProcessLiteralCondition.|
> |unManagedentityisnotintersect|0x800404aa, -2147220310|The entity is not an intersect entity.|
> |unManagederroraddingfiltertoqueryplan|0x800404ca, -2147220278|An error occurred adding a filter to the query plan.|
> |unManagederrorprocessingfilternodes|0x800404c4, -2147220284|An unexpected error occurred processing the filter nodes.|
> |unManagedfieldnotvalidatedbyplatform|0x800404ae, -2147220306|A field was not validated by the platform.|
> |unManagedfilterindexoutofrange|0x800404ab, -2147220309|The filter index is out of range.|
> |unManagedIdsAccessDenied|0x80048306, -2147187962|Not enough privilege to access the Microsoft Dynamics 365 object or perform the requested operation.|
> |unManagedidsaccounthaschildopportunities|0x80040511, -2147220207|The Account has child opportunities.|
> |unManagedidsactivitydurationdoesnotmatch|0x8004350a, -2147207926|Activity duration does not match start/end time|
> |unManagedidsactivityinvalidduration|0x80043509, -2147207927|Invalid activity duration|
> |unManagedidsactivityinvalidobjecttype|0x80043503, -2147207933|Activity regarding object type is invalid|
> |unManagedidsactivityinvalidpartyobjecttype|0x80043505, -2147207931|Activity party object type is invalid|
> |unManagedidsactivityinvalidregardingobject|0x80043507, -2147207929|Invalid activity regarding object, it probably does not exist|
> |unManagedidsactivityinvalidstate|0x80043500, -2147207936|Invalid activity state|
> |unManagedidsactivityinvalidtimeformat|0x80043508, -2147207928|Invalid activity time, check format|
> |unManagedidsactivityinvalidtype|0x80043501, -2147207935|Invalid activity type code|
> |unManagedidsactivitynotroutable|0x8004350b, -2147207925|This type of activity is not routable|
> |unManagedidsactivityobjectidortypemissing|0x80043502, -2147207934|Activity regarding object Id or type is missing|
> |unManagedidsactivitypartyobjectidortypemissing|0x80043504, -2147207932|Activity party object Id or type is missing|
> |unManagedidsanonymousenabled|0x80040226, -2147220954|The logged-in user was not found in the Active Directory.|
> |unManagedidsarticletemplatecontainsarticles|0x80043e05, -2147205627|Cannot change article template because there are knowledge base articles using it.|
> |unManagedidsarticletemplateisnotactive|0x80043e07, -2147205625|KB article template is inactive.|
> |unManagedidsattachmentcannotcreatetempfile|0x80044a05, -2147202555|Cannot create temporary attachment file.|
> |unManagedidsattachmentcannotgetfilesize|0x80044a01, -2147202559|Cannot get temporary attachment file size.|
> |unManagedidsattachmentcannotopentempfile|0x80044a00, -2147202560|Cannot open temporary attachment file.|
> |unManagedidsattachmentcannotreadtempfile|0x80044a03, -2147202557|Cannot read temporary attachment file.|
> |unManagedidsattachmentcannottruncatetempfile|0x80044a07, -2147202553|Cannot truncate temporary attachment file.|
> |unManagedidsattachmentcannotunmaptempfile|0x80044a06, -2147202554|Cannot unmap temporary attachment file.|
> |unManagedidsattachmentinvalidfilesize|0x80044a02, -2147202558|Attachment file size is too big.|
> |unManagedidsattachmentisempty|0x80044a04, -2147202556|Attachment is empty.|
> |unManagedidsbizmgmtbusinessparentdiffmerchant|0x80041d04, -2147214076|The business is not in the same merchant as parent business.|
> |unManagedidsbizmgmtcallernotinpartnerbusiness|0x80041d14, -2147214060|The caller is not from partner business.|
> |unManagedidsbizmgmtcallernotinprimarybusiness|0x80041d12, -2147214062|The caller is not from primary business.|
> |unManagedidsbizmgmtcannotaddlocaluser|0x80041d32, -2147214030|A local user cannot be added to the Dynamics 365.|
> |unManagedidsbizmgmtcannotdeletebusiness|0x80041d18, -2147214056|This is a sub-business. Use IBizMerchant::Delete to delete this sub-business.|
> |unManagedidsbizmgmtcannotdeleteprovision|0x80041d19, -2147214055|This is a provisioned root-business. Use IBizProvision::Delete to delete this root-business.|
> |unManagedidsbizmgmtcannotdisablebusiness|0x80041d1a, -2147214054|This business unit cannot be disabled.|
> |unManagedidsbizmgmtcannotdisableprovision|0x80041d1b, -2147214053|This is a provisioned root-business. Use IBizProvision::Disable to disable this root-business.|
> |unManagedidsbizmgmtcannotenablebusiness|0x80041d1c, -2147214052|This is a sub-business. Use IBizMerchant::Enable to enable this sub-business.|
> |unManagedidsbizmgmtcannotenableprovision|0x80041d1d, -2147214051|This is a provisioned root-business. Use IBizProvision::Enable to enable this root-business.|
> |unManagedidsbizmgmtcannotmovedefaultuser|0x80041d05, -2147214075|unManagedidsbizmgmtcannotmovedefaultuser|
> |unManagedidsbizmgmtcannotreadaccountcontrol|0x80041d2d, -2147214035|Insufficient permissions to the specified Active Directory user. Contact your System Administrator.|
> |unManagedidsbizmgmtcannotremovepartnershipdefaultuser|0x80041d17, -2147214057|The default user of a partnership can not be removed.|
> |unManagedidsbizmgmtcantchangeorgname|0x80041d36, -2147214026|The organization name cannot be changed.|
> |unManagedidsbizmgmtdefaultusernotinbusiness|0x80041d03, -2147214077|The default user is not in the business.|
> |unManagedidsbizmgmtdefaultusernotinpartnerbusiness|0x80041d15, -2147214059|The default user is not from partner business.|
> |unManagedidsbizmgmtdefaultusernotinprimarybusiness|0x80041d13, -2147214061|The default user is not from primary business.|
> |unManagedidsbizmgmtmissbusinessname|0x80041d00, -2147214080|The business name was unexpectedly missing.|
> |unManagedidsbizmgmtmissparentbusiness|0x80041d02, -2147214078|The parent business was unexpectedly missing.|
> |unManagedidsbizmgmtmisspartnerbusiness|0x80041d0f, -2147214065|The partnership partner business was unexpectedly missing.|
> |unManagedidsbizmgmtmissprimarybusiness|0x80041d0e, -2147214066|The partnership primary business was unexpectedly missing.|
> |unManagedidsbizmgmtmissuserdomainname|0x80041d01, -2147214079|The user's domain name was unexpectedly missing.|
> |unManagedidsbizmgmtnoparentbusiness|0x80041d29, -2147214039|The specified business does not have a parent business.|
> |unManagedidsbizmgmtpartnershipalreadyexists|0x80041d11, -2147214063|A partnership between specified primary business and partner business already exists.|
> |unManagedidsbizmgmtpartnershipnotinpendingstatus|0x80041d16, -2147214058|The partnership has been accepted or declined.|
> |unManagedidsbizmgmtprimarysameaspartner|0x80041d10, -2147214064|The primary business is the same as partner business.|
> |unManagedidsbizmgmtusercannotbeownparent|0x80041d06, -2147214074|The user can not be its own parent user.|
> |unManagedidsbizmgmtuserdoesnothaveparent|0x80041d1e, -2147214050|This user does not have a parent user.|
> |unManagedidsbizmgmtusersettingsnotcreated|0x80041d2b, -2147214037|The specified user's settings have not yet been created.|
> |unManagedidscalendarinvalidcalendar|0x80044d00, -2147201792|The calendar is invalid.|
> |unManagedidscalendarruledoesnotexist|0x80045100, -2147200768|The calendar rule does not exist.|
> |unManagedidsCalloutException|0x80045f05, -2147197179|Callout code throws exception|
> |unManagedidscalloutinvalidconfig|0x80045f03, -2147197181|Invalid callout configuration|
> |unManagedidscalloutinvalidevent|0x80045f04, -2147197180|Invalid callout event|
> |unManagedidscalloutisvabort|0x80045f01, -2147197183|Callout ISV code aborted the operation|
> |unManagedidscalloutisvexception|0x80045f00, -2147197184|Callout ISV code throws exception|
> |unManagedidscalloutisvstop|0x80045f02, -2147197182|Callout ISV code stopped the operation|
> |unManagedidscannotassigntobusiness|0x80040221, -2147220959|Cannot assign an object to a merchant.|
> |unManagedidscannotdeactivatepricelevel|0x80043b04, -2147206396|The price level cannot be deactivated because it is the default price level of an account, contact or product.|
> |unManagedidscannotdefaultprivateview|0x80040238, -2147220936|Private views cannot be default.|
> |unManagedidscannotgrantorrevokeaccesstobusiness|0x8004021e, -2147220962|Cannot grant or revoke access rights to a merchant.|
> |unManagedidscantdisable|0x80044154, -2147204780|The user cannot be disabled because they have workflow rules running under their context.|
> |unManagedidscascadeemptylinkerror|0x80045602, -2147199486|The relationship link is empty|
> |unManagedidscascadeinconsistencyerror|0x80045600, -2147199488|Cascade map information is inconsistent.|
> |unManagedidscascadeundefinedrelationerror|0x80045601, -2147199487|Relationship type is not supported|
> |unManagedidscascadeunexpectederror|0x80045603, -2147199485|Unexpected error occurred in cascading operation|
> |unManagedidscommunicationsbadsender|0x80040b01, -2147218687|More than one sender specified|
> |unManagedidscommunicationsnoparticipationmask|0x80040b06, -2147218682|Participation type is missing from an activity|
> |unManagedidscommunicationsnopartyaddress|0x80040b00, -2147218688|Object address not found on party or party is marked as non-emailable|
> |unManagedidscommunicationsnorecipients|0x80040b05, -2147218683|At least one system user or queue in the organization must be a recipient|
> |unManagedidscommunicationsnosender|0x80040b02, -2147218686|No email address was specified, and the calling user does not have an email address set|
> |unManagedidscommunicationsnosenderaddress|0x80040b08, -2147218680|The sender does not have an email address on the party record|
> |unManagedidscommunicationstemplateinvalidtemplate|0x80040b07, -2147218681|The template body is invalid|
> |unManagedidscontacthaschildopportunities|0x80040512, -2147220206|The Contact has child opportunities.|
> |unManagedidscontractaccountmissing|0x80043201, -2147208703|Account is required to save a contract.|
> |unManagedidscontractdoesnotexist|0x80043207, -2147208697|The contract does not exist.|
> |unManagedidscontractinvalidowner|0x80043212, -2147208686|The owner of the contract is invalid.|
> |unManagedidscontractinvalidstartdateforrenewedcontract|0x80043217, -2147208681|The start date of the renewed contract can not be earlier than the end date of the originating contract.|
> |unManagedidscontractinvalidtotalallotments|0x80043214, -2147208684|The totalallotments is invalid.|
> |unManagedidscontractlineitemdoesnotexist|0x80043208, -2147208696|The contract line item does not exist.|
> |unManagedidscontractopencasesexist|0x8004320a, -2147208694|There are open cases against this contract line item.|
> |unManagedidscontracttemplateabbreviationexists|0x80043216, -2147208682|The value for abbreviation already exists.|
> |unManagedidscontractunexpected|0x80043200, -2147208704|An unexpected error occurred in Contracts.|
> |unManagedidscpbadpassword|0x80042901, -2147211007|Incorrect password for the specified customer portal user.|
> |unManagedidscpdecryptfailed|0x80042903, -2147211005|Decryption of the password failed.|
> |unManagedidscpencryptfailed|0x80042902, -2147211006|Encryption of the supplied password failed.|
> |unManagedidscpuserdoesnotexist|0x80042900, -2147211008|The customer portal user does not exist, or the password was incorrect.|
> |unManagedidscustomentityalreadyinitialized|0x80045901, -2147198719|Custom entity interface already initialized on this thread.|
> |unManagedidscustomentityambiguousrelationship|0x8004590d, -2147198707|More than one relationship between the requested entities exists.|
> |unManagedidscustomentityexistingloop|0x80045907, -2147198713|There is an existing loop in the database.|
> |unManagedidscustomentityinvalidchild|0x80045909, -2147198711|The supplied child passed in is not a valid entity.|
> |unManagedidscustomentityinvalidownership|0x80045903, -2147198717|Custom entity ownership type mask is improperly set.|
> |unManagedidscustomentityinvalidparent|0x8004590a, -2147198710|The supplied parent passed in is not a valid entity.|
> |unManagedidscustomentitynameviolation|0x80045900, -2147198720|Supplied entity found, but it is not a custom entity.|
> |unManagedidscustomentitynorelationship|0x8004590c, -2147198708|No relationship exists between the requested entities.|
> |unManagedidscustomentitynotinitialized|0x80045902, -2147198718|Custom entity interface was not properly initialized.|
> |unManagedidscustomentityparentchildidentical|0x8004590b, -2147198709|The supplied parent and child entities are identical.|
> |unManagedidscustomentitystackoverflow|0x80045905, -2147198715|Custom entity MD stack overflow.|
> |unManagedidscustomentitystackunderflow|0x80045906, -2147198714|Custom entity MD stack underflow.|
> |unManagedidscustomentitytlsfailure|0x80045904, -2147198716|Custom entity MD TLS not initialized.|
> |unManagedidscustomentitywouldcreateloop|0x80045908, -2147198712|This association would create a loop in the database.|
> |unManagedidscustomeraddresstypeinvalid|0x80040514, -2147220204|Invalid customer address type.|
> |unManagedidscustomizationtransformationnotsupported|0x80044700, -2147203328|Transformation is not supported for this object.|
> |unManagedidsdataaccessunexpected|0x80042300, -2147212544|Unexpected error in data access.  DB Connection may not have been opened successfully.|
> |unManagedidsdataoutofrange|0x8004022c, -2147220948|Data out of range|
> |unManagedidsevalaborted|0x80042c03, -2147210237|Evaluation aborted.|
> |unManagedidsevalallaborted|0x80042c02, -2147210238|Evaluation aborted and stop further processing.|
> |unManagedidsevalallcompleted|0x80042c0c, -2147210228|Evaluation completed and stop further processing.|
> |unManagedidsevalassignshouldhave4parameters|0x80042c01, -2147210239|Assign action should have 4 parameters.|
> |unManagedidsevalchangetypeerror|0x80042c0d, -2147210227|Change type error.|
> |unManagedidsevalcompleted|0x80042c04, -2147210236|Evaluation completed.|
> |unManagedidsevalcreateshouldhave2parameters|0x80042c3c, -2147210180|Create action should have 2 parameters.|
> |unManagedidsevalerrorabsparameter|0x80042c2c, -2147210196|Error occurred when evaluating a WFPM_ABS parameter.|
> |unManagedidsevalerroractivityattachment|0x80042c18, -2147210216|Error in action activity attachment.|
> |unManagedidsevalerroraddparameter|0x80042c0f, -2147210225|Error occurred when evaluating a WFPM_ADD parameter.|
> |unManagedidsevalerrorappendtoactivityparty|0x80042c3f, -2147210177|unManagedidsevalerrorappendtoactivityparty|
> |unManagedidsevalerrorassign|0x80042c22, -2147210206|Error in action assign.|
> |unManagedidsevalerrorbeginwithparameter|0x80042c38, -2147210184|Error occurred when evaluating a WFPM_BEGIN_WITH parameter.|
> |unManagedidsevalerrorbetweenparameter|0x80042c33, -2147210189|Error occurred when evaluating a WFPM_BETWEEN parameter.|
> |unManagedidsevalerrorcontainparameter|0x80042c3a, -2147210182|Error occurred when evaluating a WFPM_CONTAIN parameter.|
> |unManagedidsevalerrorcreate|0x80042c3b, -2147210181|Error in create update.|
> |unManagedidsevalerrorcreateactivity|0x80042c17, -2147210217|Error in action create activity.|
> |unManagedidsevalerrorcreateincident|0x80042c1d, -2147210211|Error in action create incident.|
> |unManagedidsevalerrorcreatenote|0x80042c1b, -2147210213|Error in action create note.|
> |unManagedidsevalerrordividedbyzero|0x80042c16, -2147210218|Divided by zero.|
> |unManagedidsevalerrordivisionparameter|0x80042c13, -2147210221|Error occurred when evaluating a WFPM_DIVISION parameter.|
> |unManagedidsevalerrordivisionparameters|0x80042c12, -2147210222|Division parameter can have only two subparameters.|
> |unManagedidsevalerroremailtemplate|0x80042c21, -2147210207|Error in action email template.|
> |unManagedidsevalerrorendwithparameter|0x80042c39, -2147210183|Error occurred when evaluating a WFPM_END_WITH parameter.|
> |unManagedidsevalerroreqparameter|0x80042c31, -2147210191|Error occurred when evaluating a WFPM_EQ parameter.|
> |unManagedidsevalerrorexec|0x80042c27, -2147210201|Error in action exec.|
> |unManagedidsevalerrorformatbooleanparameter|0x80042c45, -2147210171|Error happens when evaluating WFPM_FORMAT_BOOLEAN parameter.|
> |unManagedidsevalerrorformatdatetimeparameter|0x80042c44, -2147210172|Error happens when evaluating WFPM_FORMAT_DATETIME parameter.|
> |unManagedidsevalerrorformatdecimalparameter|0x80042c4a, -2147210166|Error happens when evaluating WFPM_FORMAT_DECIMAL parameter.|
> |unManagedidsevalerrorformatintegerparameter|0x80042c49, -2147210167|Error happens when evaluating WFPM_FORMAT_INTEGER parameter.|
> |unManagedidsevalerrorformatlookupparameter|0x80042c4c, -2147210164|Error happens when evaluating WFPM_FORMAT_LOOKUP parameter.|
> |unManagedidsevalerrorformatpicklistparameter|0x80042c46, -2147210170|Error happens when evaluating WFPM_FORMAT_PICKLIST parameter.|
> |unManagedidsevalerrorformattimezonecodeparameter|0x80042c4b, -2147210165|unManagedidsevalerrorformattimezonecodeparameter|
> |unManagedidsevalerrorgeqparameter|0x80042c2e, -2147210194|Error occurred when evaluating a WFPM_GEQ parameter.|
> |unManagedidsevalerrorgtparameter|0x80042c2d, -2147210195|Error occurred when evaluating a WFPM_GT parameter.|
> |unManagedidsevalerrorhalt|0x80042c28, -2147210200|Error in action halt.|
> |unManagedidsevalerrorhandleactivity|0x80042c19, -2147210215|Error in action handle activity.|
> |unManagedidsevalerrorhandleincident|0x80042c1e, -2147210210|Error in action handle incident.|
> |unManagedidsevalerrorincidentqueue|0x80042c29, -2147210199|Failed to evaluate INCIDENT_QUEUE.|
> |unManagedidsevalerrorinlistparameter|0x80042c42, -2147210174|unManagedidsevalerrorinlistparameter|
> |unManagedidsevalerrorinparameter|0x80042c34, -2147210188|Error occurred when evaluating a WFPM_IN parameter.|
> |unManagedidsevalerrorinvalidparameter|0x80042c2b, -2147210197|Invalid parameter.|
> |unManagedidsevalerrorinvalidrecipient|0x80042c35, -2147210187|Invalid email recipient.|
> |unManagedidsevalerrorisnulllistparameter|0x80042c43, -2147210173|unManagedidsevalerrorisnulllistparameter|
> |unManagedidsevalerrorleqparameter|0x80042c30, -2147210192|Error occurred when evaluating a WFPM_LEQ parameter.|
> |unManagedidsevalerrorltparameter|0x80042c2f, -2147210193|Error occurred when evaluating a WFPM_LT parameter.|
> |unManagedidsevalerrormodulusparameter|0x80042c15, -2147210219|Error occurred when evaluating a WFPM_MODULUR parameter.|
> |unManagedidsevalerrormodulusparameters|0x80042c14, -2147210220|Modulus parameter can have only two subparameters.|
> |unManagedidsevalerrormultiplicationparameter|0x80042c11, -2147210223|Error occurred when evaluating a WFPM_MULTIPLICATION parameter.|
> |unManagedidsevalerrorneqparameter|0x80042c32, -2147210190|Error occurred when evaluating a WFPM_NEQ parameter.|
> |unManagedidsevalerrornoteattachment|0x80042c1c, -2147210212|Error in action note attachment.|
> |unManagedidsevalerrorobjecttype|0x80042c48, -2147210168|Error happens when evaluating WFPM_GetObjectType parameter.|
> |unManagedidsevalerrorposturl|0x80042c26, -2147210202|Error in action posturl.|
> |unManagedidsevalerrorqueueidparameter|0x80042c47, -2147210169|unManagedidsevalerrorqueueidparameter|
> |unManagedidsevalerrorremovefromactivityparty|0x80042c40, -2147210176|unManagedidsevalerrorremovefromactivityparty|
> |unManagedidsevalerrorroute|0x80042c24, -2147210204|Error in action route.|
> |unManagedidsevalerrorsendemail|0x80042c20, -2147210208|Error in action send email.|
> |unManagedidsevalerrorsetactivityparty|0x80042c41, -2147210175|unManagedidsevalerrorsetactivityparty|
> |unManagedidsevalerrorsetstate|0x80042c25, -2147210203|Error in action set state.|
> |unManagedidsevalerrorstrlenparameter|0x80042c37, -2147210185|Error occurred when evaluating a WFPM_STRLEN parameter.|
> |unManagedidsevalerrorsubstrparameter|0x80042c36, -2147210186|Error occurred when evaluating a WFPM_SUBSTR parameter.|
> |unManagedidsevalerrorsubtractionparameter|0x80042c10, -2147210224|Error occurred when evaluating a WFPM_SUBTRACTION parameter.|
> |unManagedidsevalerrorunhandleactivity|0x80042c1a, -2147210214|Error in action unhandle activity.|
> |unManagedidsevalerrorunhandleincident|0x80042c1f, -2147210209|Error in action unhandle incident.|
> |unManagedidsevalerrorupdate|0x80042c23, -2147210205|Error in action update.|
> |unManagedidsevalgenericerror|0x80042c2a, -2147210198|Evaluation error.|
> |unManagedidsevalmetabaseattributenotfound|0x80042c08, -2147210232|The specified metabase attribute does not exist.|
> |unManagedidsevalmetabaseattributenotmatchquery|0x80042c0b, -2147210229|The specified refattributeid does not the query for a WFPM_SELECT parameter.|
> |unManagedidsevalmetabaseentitycompoundkeys|0x80042c07, -2147210233|The specified metabase object has compound keys. We do not support compound-key entities yet.|
> |unManagedidsevalmetabaseentitynotmatchquery|0x80042c0a, -2147210230|The specified refentityid does not the query for a WFPM_SELECT parameter.|
> |unManagedidsevalmissselectquery|0x80042c0e, -2147210226|Missing the query subparameter in a select parameter.|
> |unManagedidsevalobjectnotfound|0x80042c05, -2147210235|The required object does not exist.|
> |unManagedidsevalpropertyisnull|0x80042c09, -2147210231|The required property of the object was not set.|
> |unManagedidsevalpropertynotfound|0x80042c06, -2147210234|The required property of the object was not found.|
> |unManagedidsevaltimererrorcalculatescheduletime|0x80042c3e, -2147210178|Failed to calculate the schedule time for the timer action.|
> |unManagedidsevaltimerinvalidparameternumber|0x80042c3d, -2147210179|Invalid parameters for Timer action.|
> |unManagedidsevalupdateshouldhave3parameters|0x80042c00, -2147210240|Update action should have 3 parameters.|
> |unManagedidsfailureinittoken|0x8004020f, -2147220977|Failure in obtaining user token.|
> |unManagedidsfetchbetweentext|0x80044153, -2147204781|between, not-between, in, and not-in operators are not allowed on attributes of type text or ntext.|
> |unManagedidsfulltextoperationfailed|0x80043e06, -2147205626|Full text operation failed.|
> |unManagedidsincidentassociatedactivitycorrupted|0x80044405, -2147204091|The activity associated with this case is corrupted.|
> |unManagedidsincidentcannotclose|0x8004440a, -2147204086|The incident can not be closed because there are open activities for this incident.|
> |unManagedidsincidentcontractdetaildoesnotmatchcontract|0x80044402, -2147204094|The contract line item is not in the specified contract.|
> |unManagedidsincidentinvalidactivitytypecode|0x80044406, -2147204090|The activitytypecode is wrong.|
> |unManagedidsincidentinvalidstate|0x80044404, -2147204092|Incident state is invalid.|
> |unManagedidsincidentmissingactivityobjecttype|0x80044408, -2147204088|Missing object type code.|
> |unManagedidsincidentnullactivitytypecode|0x80044407, -2147204089|The activitytypecode can't be NULL.|
> |unManagedidsincidentparentaccountandparentcontactnotpresent|0x80044410, -2147204080|You should specify a parent contact or account.|
> |unManagedidsincidentparentaccountandparentcontactpresent|0x8004440f, -2147204081|You can either specify a parent contact or account, but not both.|
> |unManagedidsinvalidassociation|0x80040211, -2147220975|Invalid association.|
> |unManagedidsinvalidbusinessid|0x80040209, -2147220983|Invalid business id.|
> |unManagedidsinvaliditemid|0x8004020b, -2147220981|Invalid item id.|
> |unManagedidsinvalidorgid|0x8004020a, -2147220982|Invalid organization id.|
> |unManagedidsinvalidowninguser|0x80040212, -2147220974|Item does not have an owning user.|
> |unManagedidsinvalidteamid|0x80040208, -2147220984|Invalid team id.|
> |unManagedidsinvaliduserid|0x80040207, -2147220985|The user id is invalid or missing.|
> |unManagedidsinvaliduseridorbusinessidorusersbusinessinvalid|0x8004021d, -2147220963|One of the following occurred: invalid user id, invalid business id or the user does not belong to the business.|
> |unManagedidsinvalidvisibility|0x8004020e, -2147220978|Invalid visibility.|
> |unManagedidsinvalidvisibilitymodificationaccess|0x80040213, -2147220973|User does not have access to modify the visibility of this item.|
> |unManagedidsinvoicecloseapideprecated|0x80043b25, -2147206363|The Invoice Close API is deprecated. It has been replaced by the Pay and Cancel APIs.|
> |unManagedidsjournalinginvalideventtype|0x80040803, -2147219453|Invalid event type.|
> |unManagedidsjournalingmissingaccountid|0x80040806, -2147219450|Account Id missed.|
> |unManagedidsjournalingmissingcontactid|0x80040808, -2147219448|Contact Id missed.|
> |unManagedidsjournalingmissingeventdirection|0x80040802, -2147219454|Event direction code missed.|
> |unManagedidsjournalingmissingeventtype|0x80040804, -2147219452|Event type missed.|
> |unManagedidsjournalingmissingincidentid|0x80040809, -2147219447|Incident Id missed.|
> |unManagedidsjournalingmissingleadid|0x80040805, -2147219451|Lead Id missed.|
> |unManagedidsjournalingmissingopportunityid|0x80040807, -2147219449|Opportunity Id missed.|
> |unManagedidsjournalingunsupportedobjecttype|0x80040801, -2147219455|Unsupported type of objects passed in operation.|
> |unManagedidsleaddoesnotexist|0x80040501, -2147220223|Lead does not exist.|
> |unManagedidsleadnoparent|0x8004050b, -2147220213|The lead does not have a parent.|
> |unManagedidsleadnotassigned|0x8004050c, -2147220212|The lead has not been assigned.|
> |unManagedidsleadnotassignedtocaller|0x80040513, -2147220205|The lead is not being assigned to the caller for acceptance.|
> |unManagedidsleadoneaccount|0x80040510, -2147220208|A lead can be associated with only one account.|
> |unManagedidsleadusercannotreject|0x8004050d, -2147220211|The user does not have the privilege to reject a lead, so he cannot be assigned the lead for acceptance.|
> |unManagedidsmergedifferentbizorgerror|0x80045303, -2147200253|Merge cannot be performed on entities from different business entity.|
> |unManagedidsmetadatanoentity|0x80040e00, -2147217920|The specified entity does not exist|
> |unManagedidsmetadatanorelationship|0x80040e02, -2147217918|The relationship does not exist|
> |unManagedidsnorelationship|0x80040236, -2147220938|No relationship exists between the objects specified.|
> |unManagedidsnotesalreadyattached|0x80041701, -2147215615|The specified note is already attached to an object.|
> |unManagedidsnotesloopbeingcreated|0x80041703, -2147215613|Creating this parental association would create a loop in the annotation hierarchy.|
> |unManagedidsnotesloopexists|0x80041702, -2147215614|A loop exists in the annotation hierarchy.|
> |unManagedidsnotesnoattachment|0x80041704, -2147215612|The specified note has no attachments.|
> |unManagedidsnotesnotedoesnotexist|0x80041700, -2147215616|The specified note does not exist.|
> |unManagedidsopportunitydoesnotexist|0x80040500, -2147220224|Opportunity does not exist.|
> |unManagedidsopportunityinvalidparent|0x80040504, -2147220220|The parent of an opportunity must be an account or contact.|
> |unManagedidsopportunitymissingparent|0x80040505, -2147220219|The parent of the opportunity is missing.|
> |unManagedidsopportunityoneaccount|0x8004050e, -2147220210|An opportunity can be associated with only one account.|
> |unManagedidsopportunityorphan|0x8004050f, -2147220209|Removing this association will make the opportunity an orphan.|
> |unManagedidsoutofmemory|0x80040222, -2147220958|Out of memory.|
> |unManagedidsownernotenabled|0x8004022b, -2147220949|The specified owner has been disabled.|
> |unManagedidspresentuseridandteamid|0x8004021c, -2147220964|Both the user id and team id are present. Only one should be present.|
> |unManagedidspropbagattributealreadyset|0x8004203f, -2147213249|One of the attributes passed has already been set|
> |unManagedidspropbagattributenotnullable|0x8004203e, -2147213250|One of the attributes passed cannot be NULL|
> |unManagedidspropbagcolloutofrange|0x8004201e, -2147213282|The bag index in the collection was out of range.|
> |unManagedidspropbagnointerface|0x80042001, -2147213311|The property bag interface could not be found.|
> |unManagedidspropbagnullproperty|0x80042002, -2147213310|The specified property was null in the property bag.|
> |unManagedidspropbagpropertynotfound|0x80042000, -2147213312|The specified property was not found in the property bag.|
> |unManagedidsqueuemissingbusinessunitid|0x80043e03, -2147205629|Missing businessunitid.|
> |unManagedidsqueueorganizationidnotmatch|0x80043e04, -2147205628|Callers' organization Id does not match businessunit's organization Id.|
> |unManagedidsrcsyncfilternoaccess|0x8004410f, -2147204849|Cannot go offline: missing access rights on required entity.|
> |unManagedidsrcsyncinvalidfiltererror|0x8004410d, -2147204851|Invalid filter specified.|
> |unManagedidsrcsyncinvalidsubscription|0x80044109, -2147204855|The specified subscription does not exist.|
> |unManagedidsrcsyncinvalidsynctime|0x80044100, -2147204864|The specified sync time is invalid.  Sync times must not be earlier than those returned by the previous sync.  Please reinitialize your subscription.|
> |unManagedidsrcsyncmethodnone|0x80044114, -2147204844|Synchronization tasks can’t be performed on this computer since the synchronization method is set to None.|
> |unManagedidsrcsyncmsxmlfailed|0x80044101, -2147204863|unManagedidsrcsyncmsxmlfailed|
> |unManagedidsrcsyncnoclient|0x80044113, -2147204845|Client does not exist.|
> |unManagedidsrcsyncnoprimary|0x80044112, -2147204846|No primary client exists.|
> |unManagedidsrcsyncnotprimary|0x80044111, -2147204847|Cannot sync: not the primary OutlookSync client.|
> |unManagedidsrcsyncsoapconnfailed|0x80044103, -2147204861|unManagedidsrcsyncsoapconnfailed|
> |unManagedidsrcsyncsoapfaulterror|0x80044106, -2147204858|unManagedidsrcsyncsoapfaulterror|
> |unManagedidsrcsyncsoapgenfailed|0x80044102, -2147204862|unManagedidsrcsyncsoapgenfailed|
> |unManagedidsrcsyncsoapparseerror|0x80044108, -2147204856|unManagedidsrcsyncsoapparseerror|
> |unManagedidsrcsyncsoapreaderror|0x80044107, -2147204857|unManagedidsrcsyncsoapreaderror|
> |unManagedidsrcsyncsoapsendfailed|0x80044104, -2147204860|unManagedidsrcsyncsoapsendfailed|
> |unManagedidsrcsyncsoapservererror|0x80044105, -2147204859|unManagedidsrcsyncsoapservererror|
> |unManagedidsrcsyncsqlgenericerror|0x80044110, -2147204848|unManagedidsrcsyncsqlgenericerror|
> |unManagedidsrcsyncsqlpausederror|0x8004410c, -2147204852|unManagedidsrcsyncsqlpausederror|
> |unManagedidsrcsyncsqlstoppederror|0x8004410b, -2147204853|unManagedidsrcsyncsqlstoppederror|
> |unManagedidsrcsyncsubscriptionowner|0x8004410a, -2147204854|The caller id does not match the subscription owner id.  Only subscription owners may perform subscription operations.|
> |unManagedidsrolesdeletenonparentrole|0x8004140c, -2147216372|Cannot delete a role that is inherited from a parent business.|
> |unManagedidsrolesinvalidroledata|0x80041400, -2147216384|The role data is invalid.|
> |unManagedidsrolesinvalidroleid|0x80041401, -2147216383|Invalid role ID.|
> |unManagedidsrolesinvalidrolename|0x8004140a, -2147216374|The role name is invalid.|
> |unManagedidsrolesinvalidtemplateid|0x80041404, -2147216380|Invalid role template ID.|
> |unManagedidsrolesmissbusinessid|0x80041406, -2147216378|The role's business unit ID was unexpectedly missing.|
> |unManagedidsrolesmissprivid|0x80041408, -2147216376|The privilege ID was unexpectedly missing.|
> |unManagedidsrolesmissroleid|0x80041405, -2147216379|The role ID was unexpectedly missing.|
> |unManagedidsrolesmissrolename|0x80041407, -2147216377|The role name was unexpectedly missing.|
> |unManagedidsrolesroledoesnotexist|0x80041402, -2147216382|The specified role does not exist.|
> |unManagedidsrspropbagdbinfoalreadyset|0x8004203d, -2147213251|The DB info for the recordset property bag has already been set.|
> |unManagedidsrspropbagdbinfonotset|0x8004203c, -2147213252|The DB info for the recordset property bag has not been set.|
> |unManagedidssalespeopleduplicatecalendarfound|0x80043802, -2147207166|Duplicate fiscal calendars found for this salesperson/year|
> |unManagedidssalespeopleinvalidfiscalcalendartype|0x80043808, -2147207160|Invalid fiscal calendar type|
> |unManagedidssalespeopleinvalidfiscalperiodindex|0x80043807, -2147207161|Invalid fiscal period index|
> |unManagedidssalespeopleinvalidterritoryobjecttype|0x80043804, -2147207164|Territories cannot be retrieved by this kind of object|
> |unManagedidssqlerror|0x80044150, -2147204784|Generic SQL error.|
> |unManagedidssqltimeouterror|0x80044151, -2147204783|SQL timeout expired.|
> |unManagedidsstatedoesnotexist|0x80043af9, -2147206407|The state is not valid for this object.|
> |unManagedidsusernotenabled|0x80040225, -2147220955|The specified user is either disabled or is not a member of any business unit.|
> |unManagedidsviewisnotsharable|0x80040232, -2147220942|The view is not sharable.|
> |unManagedidsxmlinvalidcollectionname|0x80041a03, -2147214845|The collection name specified is incorrect|
> |unManagedidsxmlinvalidcreate|0x80041a01, -2147214847|A field that is not valid for create was specified|
> |unManagedidsxmlinvalidentityattributes|0x80041a06, -2147214842|Invalid attributes|
> |unManagedidsxmlinvalidentityname|0x80041a00, -2147214848|The entity name specified is incorrect|
> |unManagedidsxmlinvalidfield|0x80041a07, -2147214841|An invalid value was passed in for a field|
> |unManagedidsxmlinvalidread|0x80041a08, -2147214840|A field that is not valid for read was specified|
> |unManagedidsxmlinvalidupdate|0x80041a02, -2147214846|A field that is not valid for update was specified|
> |unManagedidsxmlparseerror|0x80041a04, -2147214844|A parse error was encountered in the XML|
> |unManagedidsxmlunexpected|0x80041a05, -2147214843|An unexpected error has occurred|
> |unManagedinvalddbtimefield|0x800404d9, -2147220263|The platform cannot handle dbtime fields.|
> |unManagedinvalidargumentsforcondition|0x800404b7, -2147220297|An invalid number of arguments was supplied to a condition.|
> |unManagedinvalidbinaryfield|0x800404dc, -2147220260|The platform cannot handle binary fields.|
> |unManagedinvalidbusinessunitid|0x800404a7, -2147220313|The businessunitid is missing or invalid.|
> |unManagedinvalidcharacterdataforaggregate|0x800404de, -2147220258|Character data is not valid when clearing an aggregate.|
> |unManagedinvalidcountvalue|0x800404c1, -2147220287|The count value is invalid or missing.|
> |unManagedinvaliddbdatefield|0x800404da, -2147220262|The platform cannot handle dbdate fields.|
> |unManagedinvaliddynamicparameteraccessor|0x800404d5, -2147220267|SetParam failed processing the DynamicParameterAccessor parameter.|
> |unManagedinvalidequalityoperand|0x800404ac, -2147220308|Only QB_LITERAL is supported for equality operand.|
> |unManagedinvalidescapedxml|0x800404a1, -2147220319|Escaped xml size not as expected.|
> |unManagedinvalidfieldtype|0x800404d8, -2147220264|The platform cannot handle the specified field type.|
> |unManagedinvalidlinkobjects|0x800404ba, -2147220294|Invalid link entity, link to attribute, or link from attribute.|
> |unManagedinvalidoperator|0x800404c7, -2147220281|The operator provided is not valid.|
> |unManagedinvalidorganizationid|0x800404be, -2147220290|The organizationid is missing or invalid.|
> |unManagedinvalidowningbusinessunit|0x800404a8, -2147220312|The owningbusinessunit is missing or invalid.|
> |unManagedinvalidowningbusinessunitorbusinessunitid|0x800404bc, -2147220292|The owningbusinessunit or businessunitid is missing or invalid.|
> |unManagedinvalidowninguser|0x800404bd, -2147220291|The owninguser is mising or invalid.|
> |unManagedinvalidpagevalue|0x800404c2, -2147220286|The page value is invalid or missing.|
> |unManagedinvalidparametertypeforparameterizedquery|0x800404d6, -2147220266|A parameterized query is not supported for the supplied parameter type.|
> |unManagedinvalidprincipal|0x8004049e, -2147220322|The principal id is missing or invalid.|
> |unManagedinvalidprivilegeedepth|0x800404bb, -2147220293|Invalid privilege depth for user.|
> |unManagedinvalidprivilegeid|0x800404ce, -2147220274|The privilege id is invalid or missing.|
> |unManagedinvalidprivilegeusergroup|0x800404cd, -2147220275|The privilege user group id is invalid or missing.|
> |unManagedinvalidprocesschildofcondition|0x800404b4, -2147220300|ProcessChildOfCondition was called with non-child-of condition.|
> |unManagedinvalidprocessliternalcondition|0x800404b1, -2147220303|ProcessLiteralCondition is only valid for use with Rollup queries.|
> |unManagedinvalidsecurityprincipal|0x800404d2, -2147220270|The security principal is invalid or missing.|
> |unManagedinvalidstreamfield|0x800404d7, -2147220265|The platform cannot handle stream fields.|
> |unManagedinvalidtlsmananger|0x800404a2, -2147220318|Failed to retrieve TLS Manager.|
> |unManagedinvalidtrxcountforcommit|0x800404e2, -2147220254|The transaction count was expected to be 1 in order to commit.|
> |unManagedinvalidtrxcountforrollback|0x800404e1, -2147220255|The transaction count was expected to be 1 in order to rollback.|
> |unManagedinvalidvaluettagoutsideconditiontag|0x800404bf, -2147220289|A invalid value tag was found outside of it's condition tag.|
> |unManagedinvalidversionvalue|0x800404c0, -2147220288|The version value is invalid or missing.|
> |unManagedinvaludidispatchfield|0x800404db, -2147220261|The platform cannot handle idispatch fields.|
> |unManagedmissingaddressentity|0x800404cb, -2147220277|The address entity could not be found.|
> |unManagedmissingattributefortag|0x800404c5, -2147220283|An expected attribute was not found for the tag specified.|
> |unManagedmissingdataaccess|0x800404df, -2147220257|The data access could not be retrieved from the ExecutionContext.|
> |unManagedmissingfilterattribute|0x800404ad, -2147220307|Missing filter attribute.|
> |unManagedmissinglinkentity|0x800404b2, -2147220302|Unexpected error locating link entity.|
> |unManagedMissingObjectType|0x80042003, -2147213309|Object type must be specified for one of the attributes.|
> |unManagedmissingparentattributeonentity|0x800404b5, -2147220299|The parent attribute was not found on the expected entity.|
> |unManagedmissingparententity|0x800404e5, -2147220251|The parent entity could not be located.|
> |unManagedmissingpreviousownertype|0x800404d0, -2147220272|Unable to determine the previous owner's type.|
> |unManagedmissingreferencesfromrelationship|0x800404c9, -2147220279|Unable to access a relationship in an entity's ReferencesFrom collection.|
> |unManagedmissingreferencingattribute|0x800404c8, -2147220280|The relationship's ReferencingAttribute is missing or invalid.|
> |unManagedmorethanonesortattribute|0x800404a6, -2147220314|More than one sort attributes were defined.|
> |unManagedObjectTypeUnexpected|0x80042004, -2147213308|Object type was specified for one of the attributes that does not allow it.|
> |unManagedparentattributenotfound|0x800404a4, -2147220316|The parent attribute was not found for the child attribute.|
> |unManagedpartylistattributenotsupported|0x800404b8, -2147220296|Attributes of type partylist are not supported.|
> |unManagedpendingtrxexists|0x800404e3, -2147220253|A pending transaction already exists.|
> |unManagedproxycreationfailed|0x8004049f, -2147220321|Cannot create an instance of managed proxy.|
> |unManagedtrxinterophandlerset|0x800404dd, -2147220259|The TrxInteropHandler has already been set.|
> |unManagedunablegetexecutioncontext|0x800404e4, -2147220252|Failed to retrieve execution context (TLS).|
> |unManagedunablegetsessiontoken|0x800404d3, -2147220269|Unable to retrieve the session token.|
> |unManagedunablegetsessiontokennotrx|0x800404d4, -2147220268|Unable to retrieve the session token as there are no pending transactions.|
> |unManagedunableswitchusercontext|0x800404e0, -2147220256|Cannot set to a different user context.|
> |unManagedunabletoaccessqueryplan|0x800404a5, -2147220315|Unable to access the query plan.|
> |unManagedunabletoaccessqueryplanfilter|0x800404c6, -2147220282|Unable to access a filter in the query plan.|
> |unManagedunabletolocateconditionfilter|0x800404c3, -2147220285|Unexpected error locating the filter for the condition.|
> |unManagedunabletoretrieveprivileges|0x800404a0, -2147220320|Failed to retrieve privileges.|
> |unManagedunexpectedpropertytype|0x800404cc, -2147220276|Unexpected type for the property.|
> |unManagedunexpectedrimarykey|0x800404b3, -2147220301|Primary key attribute was not as expected.|
> |unManagedunknownaggregateoperation|0x800404b6, -2147220298|An unknown aggregate operation was supplied.|
> |unManagedunusablevariantdata|0x800404af, -2147220305|Variant supplied contains data in an unusable format.|
> |UnmappedTransformationOutputDataFound|0x80040381, -2147220607|One or more outputs returned by the transformation is not mapped to target fields.|
> |UnpopulatedPrimaryKey|0x8004023d, -2147220931|Primary Key must be populated for calls to platform on rich client in offline mode.|
> |UnrelatedConnectionRoles|0x80048216, -2147188202|The connection roles are not related.|
> |UnrestrictedIFrameInUserDashboard|0x8004E30C, -2147163380|A user dashboard Form XML cannot have Security = false.|
> |UnspecifiedActivityXmlForCampaignActivityPropagate|0x80040318, -2147220712|Must specify an Activity Xml for CampaignActivity Execute/Distribute|
> |UnsupportedActionType|0x80060390, -2147089520|Missing Control Step.|
> |UnsupportedArgumentsMarkedRequired|0x80060394, -2147089516|Unsupported arguments should not be marked as required.|
> |UnsupportedAttributeForEditor|0x80060010, -2147090416|The rule contain an attribute which is not supported.|
> |UnsupportedAttributeInInProfileItemEntityFilters|0x80071123, -2147020509|Attribute {0} is not supported in the filter query option.|
> |UnsupportedAttributeOrOperatorMobileOfflineFilters|0x80071115, -2147020523|Attribute or Operator “{0}” is not supported for Mobile Offline Org Filter.|
> |UnsupportedAttributeType|0x8005E00D, -2147098611|Attribute type {0} is not supported. Remove attribute {1} from the query and try again.|
> |UnsupportedComponentOperation|0x8004F010, -2147160048|{0} is not recognized as a supported operation.|
> |UnsupportedCudOperationForDynamicProperties|0x80061019, -2147086311|You can't create a property for a kit.|
> |UnsupportedDashboardInEditor|0x8004E30E, -2147163378|The dashboard could not be opened.|
> |UnsupportedEmailServer|0x8005E242, -2147098046|The email server isn't supported.|
> |UnsupportedFormFactorsUsedInForm|0x80160011, -2146041839|Unsupported Form factor {0} used for control with uniqueid {1}. More Details:{2}|
> |UnsupportedFormFactorsUsedInNonFormContext|0x80160014, -2146041836|Unsupported form factor(s) {0} used. More Details:{1}|
> |UnsupportedImportComponent|0x80061302, -2147085566|Sorry, your import failed because the {0} component isn’t supported for import and export.|
> |UnsupportedListMemberType|0x80040301, -2147220735|Unsupported list member type.|
> |UnsupportedOperatorForAttributeInProfileItemEntityFilters|0x80071121, -2147020511|Operator {0} is not supported with attribute {1} in the filter query option.|
> |UnsupportedParameter|0x80040320, -2147220704|A parameter specified is not supported by the Bulk Operation|
> |UnsupportedProcessCode|0x80040385, -2147220603|The process code is not supported on this entity.|
> |UnsupportedRelationshipInMOPIAssociation|0x800609AF, -2147087953|This relationship either no longer exists or is unsupported offline since one of the entities is not offline enabled. Please remove this assocation.|
> |UnsupportedSdkMessageForBundles|0x80061025, -2147086299|This message isn't supported for products of type bundle.|
> |UnsupportedStepForBusinessRuleEditor|0x80060009, -2147090423|The rule contain a step which is not supported by the editor.|
> |UnsupportedTypeMemberOfCusomDataType|0x80090114, -2146893548|The property name = '{0}' with custom type entity name = '{1}' is not supported as member of custom data type.|
> |UnsupportedZipFileForImport|0x80048495, -2147187563|The compressed (.zip) or .cab file couldn't be uploaded because the file is corrupted or doesn't contain valid importable files.|
> |UnzipProcessCountLimitReached|0x80048494, -2147187564|Cannot start a new process to unzip.|
> |UnzipTimeout|0x80048496, -2147187562|Timeout happened in unzipping the zip file uploaded for import.|
> |UpdateAttributeMap|0x80046204, -2147196412|UpdateAttributeMap Error Occurred|
> |UpdateEntityMap|0x80046201, -2147196415|UpdateEntityMap Error Occurred|
> |UpdateNonCustomReportFromTemplate|0x80040490, -2147220336|Cannot update a report from a template if the report was not created from a template|
> |UpdatePublishedWorkflowDefinition|0x80045002, -2147201022|Cannot update a published workflow definition.|
> |UpdatePublishedWorkflowDefinitionWorkflowDependency|0x80045008, -2147201016|Cannot update a workflow dependency for a published workflow definition.|
> |UpdatePublishedWorkflowTemplate|0x8004501B, -2147200997|Cannot update a published workflow template.|
> |UpdateRecurrenceRuleFailed|0x8004E114, -2147163884|Failed to update the recurrence rule. A corresponding recurrence rule cannot be found.|
> |UpdateRIOrganizationDataAccessNotAllowed|0x80044273, -2147204493|This feature configuration can only be updated by a system administrator.|
> |UpdateWorkflowActivation|0x80045003, -2147201021|Cannot update a workflow activation.|
> |UpdateWorkflowActivationWorkflowDependency|0x80045007, -2147201017|Cannot update a workflow dependency associated with a workflow activation.|
> |UserAlreadyExists|0x80041d2c, -2147214036|The specified Active Directory user already exists as a Dynamics 365 user.|
> |UserCancelledMailMerge|0x8004032f, -2147220689|The mail merge operation was cancelled by the user.|
> |UserCannotEnableWithoutLicense|0x8004D24C, -2147167668|Cannot enable an unlicensed user|
> |UserDataNotFound|0x8004D211, -2147167727|The user data could not be found.|
> |UserDoesNotHaveAccessToTheTenant|0x80044507, -2147203833|User does not have access to the tenant.|
> |UserDoesNotHaveAdminOnlyModePermissions|0x8004A113, -2147180269|User does not have required privileges (or role membership) to access the org when it is in Admin Only mode.|
> |UserDoesNotHavePrivilegesToRunTheTool|0x800608F8, -2147088136|You must be a system administrator to execute this request.|
> |UserDoesNotHaveSendAsAllowed|0x8004480d, -2147203059|User does not have send-as privilege|
> |UserDoesNotHaveSendAsForQueue|0x8004480f, -2147203057|You do not have sufficient privileges to send e-mail as the selected queue. Contact your system administrator for assistance.|
> |UserIdOrQueueNotSet|0x800404e8, -2147220248|Primary User Id or Destination Queue Type code not set|
> |UserInviteDisabled|0x8004D216, -2147167722|Invitation cannot be sent because user invitations are disabled.|
> |UserInWrongBusiness|0x80041409, -2147216375|Cannot associate security role because the security role's Business Unit is not the same as the user's Business Unit. Details: userid={0}, userBU={1}, roleId={2}, roleBU={3}|
> |UserIsNotSystemAdminInOrganization|0x8004B069, -2147176343|Current user is not a system admin in customer's organization|
> |UserLoopBeingCreated|0x80041d25, -2147214043|You cannot set the selected user as the manager for this user because the selected user is either already the manager or is in the user's immediate management hierarchy.  Either select another user to be the manager or do not update the record.|
> |UserLoopExists|0x80041d24, -2147214044|A manager for this user cannot be set because an existing relationship in the management hierarchy is causing a circular relationship.  This is usually caused by a manual edit of the Microsoft Dynamics 365 database. To fix this, the hierarchy in the database must be changed to remove the circular relationship.|
> |UserNameRequiredForImpersonation|0x8005E24D, -2147098035|Type in a user name and save again|
> |UserNeverLoggedIntoYammer|0x8005F111, -2147094255|To follow other users, you must be logged in to Yammer. Log in to your Yammer account, and try again.|
> |UserNotAssignedLicense|0x8004D24B, -2147167669|The user has not been assigned any License|
> |UserNotAssignedRoles|0x80042f09, -2147209463|The user (Id = {0}) has not been assigned any roles.|
> |UserNotInParentHierarchy|0x80041d07, -2147214073|The user is not in parent user's business hierarchy.|
> |UserNotMemberOfOrg|0x80072560, -2147015328|The user is not a member of the organization.|
> |UserSettingsInvalidAdvancedFindStartupMode|0x80041d34, -2147214028|Invalid advanced find startup mode.|
> |UserSettingsInvalidSearchExperienceValue|0x80041d53, -2147213997|Invalid search experience value.|
> |UserSettingsOverMaxPagingLimit|0x80044305, -2147204347|Paging limit over maximum configured value.|
> |UserTimeConvertException|0x80040241, -2147220927|Failed to convert user time zone information.|
> |UserTimeZoneException|0x80040240, -2147220928|Failed to retrieve user time zone information.|
> |UserViewsOrVisualizationsFound|0x8004E302, -2147163390|A system dashboard cannot contain user views and visualizations.|
> |ValidateNotSupported|0x8004E10A, -2147163894|Validate method is not supported for recurring appointment master.|
> |ValidationContextIsNull|0x80060442, -2147089342|Error creating or updating Business Process: validation context cannot be null.|
> |ValidationFailedForDynamicProperty|0x80061021, -2147086303|An error occurred while saving the {0} property.|
> |ValidDateTimeBehaviorExportAsWarning|0x800608A5, -2147088219|The {0} field will be a User Local Date and Time since the Date Only and Time Zone Independent behaviors won't work in earlier versions of Dynamics 365.|
> |ValidDateTimeBehaviorWarning|0x800608A4, -2147088220|The behavior of this field was changed. You should review all the dependencies of this field, such as business rules, workflows, and calculated or rollup fields, to ensure that issues won't occur. Attribute: {0}|
> |ValidOnlyForDynamicsOnline|0x80072302, -2147015934|This API is only valid for Dynamics 365 online.|
> |ValueMissingInOptionOrderArray|0x80044325, -2147204315|The options array is missing a value.|
> |ValueParsingError|0x8004B037, -2147176393|Error parsing parameter {0} of type {1} with value {2}|
> |VersionedRowNotFoundInTempDB|0x80048542, -2147187390|Required versioned row was not found in TempDB; the TempDB is likely out of space; try again at a later time.|
> |VersionMismatch|0x8004B020, -2147176416|Unsupported version - This is {0} version {1}, but version {2} was requested.|
> |VeryLargeFileInZipImport|0x80048491, -2147187567|One of the files in the compressed (.zip) or .cab file that you're trying to import exceeds the size limit.|
> |ViewConditionTypeNotSupportedOffline|0x80071130, -2147020496|The condition {0} is not supported.|
> |ViewForDuplicateDetectionNotDefined|0x80048838, -2147186632|Required view for viewing duplicates of an entity not defined.|
> |ViewIdEmptyOrNull|0x80160047, -2146041785|View Id is null or empty. More Details:{0}|
> |ViewNotAvailableForMobileOffline|0x8005F21b, -2147093989|Currently view is not available Offline. Please try switching view or contact administrator|
> |ViewNotAvailableOnMobile|0x80071126, -2147020506|This view is not available on mobile.|
> |ViewNotSupportedInCalendarModeOffline|0x80071128, -2147020504|This view is supported only in grid mode offline. It is not supported in calendar mode offline.|
> |ViewReferencedInDatasetNotFound|0x80160017, -2146041833|The view {0} specified in the dataset {1} is not found. More Details:{2}|
> |VirtualEntitiesNotSupported|0x80073020, -2147012576|Virtual entities are not supported.|
> |VirtualEntityFailure|0x80050263, -2147155357|Virtual Entity Operation Failed.|
> |VirtualEntityFCBOFF|0x80081113, -2146954989|Feature Bit for VirtualEntity not enabled.|
> |VirtualEntityNotSupportedInMobileOffline|0x80044821, -2147203039|The entity {0} is a virtual entity that’s not available in mobile offline.|
> |VisuaizationIdEmptyOrNull|0x80160048, -2146041784|Visualization Id is null or empty. More Details:{0}|
> |VisualizationModuleNotFound|0x8004E012, -2147164142|No visualization module found with the given name.|
> |VisualizationOtcNotFoundError|0x8004E015, -2147164139|Object type code is not specified for the visualization.|
> |VisualizationRenderingError|0x8004E00E, -2147164146|An error occurred while the chart was rendering|
> |WebhooksHttpRequestTimedOut|0x80050202, -2147155454|The webhook call failed because the Http request timed out at client side. Please check your webhook request handler.|
> |WebhooksInvalidHttpHeaders|0x80050203, -2147155453|The webhook call failed because of invalid http headers in authValue. Check if the authValue format, header names and values are valid for your Service Endpoint entity.|
> |WebhooksInvalidHttpQueryParams|0x80050204, -2147155452|The webhook call failed because of invalid http query params in authValue. Check if the authValue format, query parameter names and values are valid for your Service Endpoint entity.|
> |WebhooksMaxSizeExceeded|0x80050207, -2147155449|The webhook call failed because the http request payload has exceeded maximum allowed size. Please reduce your request size and retry.|
> |WebhooksNonSuccessHttpResponse|0x80050201, -2147155455|The webhook call failed because the http request received non-success httpStatus code. Please check your webhook request handler.|
> |WebhooksPostDisabled|0x80050206, -2147155450|The Webhook post is disabled for the organization.|
> |WebhooksPostRequestFailed|0x80050205, -2147155451|The webhook call failed during http post. Please check the exception for more details.|
> |WebResourceContentSizeExceeded|0x8004F114, -2147159788|Webresource content size is too big.|
> |WebResourceDuplicateName|0x8004F115, -2147159787|A webresource with the same name already exists. Use a different name.|
> |WebResourceEmptyName|0x8004F116, -2147159786|Webresource name cannot be null or empty.|
> |WebResourceEmptySilverlightVersion|0x8004F112, -2147159790|Silverlight version cannot be empty for silverlight web resources.|
> |WebResourceImportError|0x8004F11B, -2147159781|An error occurred while importing a Web resource. Try importing this solution again. For further assistance, contact Microsoft Dynamics 365 technical support.|
> |WebResourceImportMissingFile|0x8004F11A, -2147159782|The file for this Web resource does not exist in the solution file.|
> |WebResourceInvalidSilverlightVersion|0x8004F113, -2147159789|Silverlight version can only be of the format xx.xx[.xx.xx].|
> |WebResourceInvalidType|0x8004F111, -2147159791|Invalid web resource type specified.|
> |WebResourceNameInvalidCharacters|0x8004F117, -2147159785|Web resource names may only include letters, numbers, periods, and nonconsecutive forward slash characters.|
> |WebResourceNameInvalidFileExtension|0x8004F119, -2147159783|A Web resource cannot have the following file extensions: .aspx, .ascx, .asmx or .ashx.|
> |WebResourceNameInvalidPrefix|0x8004F118, -2147159784|Webresource name does not contain a valid prefix.|
> |WebResourcePreventingFormSave|0x80060369, -2147089559|Unable to save form data due to web resource registered onSave invoking preventDefault.|
> |WopiApplicationUrl|0x80060802, -2147088382|Error in retrieving information from WOPI application url.|
> |WopiDiscoveryFailed|0x80060800, -2147088384|Request for retrieving the WOPI discovery XML failed.|
> |WopiMaxFileSizeExceeded|0x80060803, -2147088381|{0} file exceeded size limit of {1}.|
> |WordTemplateFeatureNotEnabled|0x800608DB, -2147088165|Word document template feature is not enabled.|
> |WorkerProcessCrashFailure|0x80072031, -2147016655|The status for this operation is unavailable, please try again.|
> |WorkflowActivityNotSupported|0x80045045, -2147200955|This workflow cannot be created, updated or published because it's referring unsupported workflow step.|
> |WorkflowAutomaticallyDeactivated|0x80045042, -2147200958|The original workflow definition has been deactivated and replaced.|
> |WorkflowCompileFailure|0x80045001, -2147201023|An error has occurred during compilation of the workflow.|
> |WorkflowConditionIncorrectBinaryOperatorFormation|0x80045011, -2147201007|Incorrect formation of binary operator.|
> |WorkflowConditionIncorrectUnaryOperatorFormation|0x80045010, -2147201008|Incorrect formation of unary operator.|
> |WorkflowConditionOperatorNotSupported|0x80045012, -2147201006|Condition operator not supported for specified type.|
> |WorkflowConditionTypeNotSupport|0x80045013, -2147201005|Invalid type specified on condition.|
> |WorkflowDoesNotExist|0x8006040b, -2147089397|Workflow does not exist.|
> |WorkflowExpressionOperatorNotSupported|0x8004502E, -2147200978|Expression operator not supported for specified type.|
> |WorkflowIdIsNull|0x80060400, -2147089408|Workflow Id cannot be NULL while creating business process flow category|
> |WorkflowIsNotActive|0x80045055, -2147200939|Workflow must be active to be used on Action Step.|
> |WorkflowIsNotOnDemand|0x80045059, -2147200935|Workflow must be marked as On Demand.|
> |WorkflowPublishedByNonOwner|0x8004500B, -2147201013|The workflow cannot be published or unpublished by someone who is not its owner.|
> |WorkflowPublishNoActivationParameters|0x80045018, -2147201000|Automatic workflow cannot be published if no activation parameters have been specified.|
> |WorkflowReferencesInvalidActivity|0x80045038, -2147200968|The workflow definition contains a step that references and invalid custom activity. Remove the invalid references and try again.|
> |WorkflowSystemPaused|0x80045017, -2147201001|Workflow should be paused by system.|
> |WorkflowValidationFailure|0x80045014, -2147201004|Validation failed on the specified workflow.|
> |WrongNumberOfBooleanOptions|0x8004431B, -2147204325|Boolean attributes must have exactly two option values.|
> |XamlNotFound|0x80154B4F, -2146088113|This feature is not available in offline mode.|
> |XlsxExportGeneratingExcelFailed|0x800608C7, -2147088185|Failed to generate excel.|
> |XlsxImportColumnHeadersInvalid|0x800608C6, -2147088186|Invalid columns.|
> |XlsxImportExcelFailed|0x800608C8, -2147088184|Failed to import data.|
> |XlsxImportHiddenColumnAbsent|0x800608C4, -2147088188|Required columns missing.|
> |XlsxImportInvalidColumnCount|0x800608C5, -2147088187|Column mismatch.|
> |XlsxImportInvalidExcelDocument|0x800608C2, -2147088190|Invalid file to import.|
> |XlsxImportInvalidFileData|0x800608C3, -2147088189|Invalid format in import file.|
> |YammerAuthTimedOut|0x8005F107, -2147094265|You have waited too long to complete the Yammer authorization. Please try again.|
> |YValuesPerPointMeasureMismatch|0x8004E004, -2147164156|Number of YValuesPerPoint for series and number of measures for measure collection for category should be same.|
> |ZeroEmailReceived|0x8005E231, -2147098063|There were no email available in the mailbox or could not be retrieved.|
> |ZipFileHasMixOfCsvAndXmlFiles|0x80048485, -2147187579|The compressed (.zip) file that you're trying to upload contains more than one type of file. The file can contain either Excel (.xlsx) files, comma-delimited (.csv) files or XML Spreadsheet 2003 (.xml) files, but not a combination of file types.|
> |ZipInsideZip|0x80048489, -2147187575|The compressed (.zip) file that you are trying to upload contains another .zip file within it.|

### See also

[Handle exceptions in your code](handle-exceptions-code.md)