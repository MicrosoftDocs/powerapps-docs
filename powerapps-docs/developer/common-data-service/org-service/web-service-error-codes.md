---
title: "Web service error codes (Common Data Service) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This topic lists the error codes you might encounter when you debug your code. " # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 05/09/2019
ms.reviewer: ""
ms.service: powerapps
ms.topic: "article"
author: "brandonsimons" # GitHub ID
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

 The following list shows the error codes used in Common Data Service. For more information, see [Handle exceptions in your code](handle-exceptions-code.md).  

> [!div class="mx-tdBreakAll"]
>
> |Error|Message|
> |---|---|
> |**Name**:<br />AccessDenied<br />**Hex**:<br />80048405<br />**Number**:<br />-2147187707|Access is denied.|
> |**Name**:<br />AccessDeniedSharePointRecord<br />**Hex**:<br />80060904<br />**Number**:<br />-2147088124|Access denied on SharePoint record in Dynamics 365.|
> |**Name**:<br />AccessTokenExpired<br />**Hex**:<br />8005F101<br />**Number**:<br />-2147094271|The requested resource requires authentication.|
> |**Name**:<br />AccountDoesNotExist<br />**Hex**:<br />80040502<br />**Number**:<br />-2147220222|Account does not exist.|
> |**Name**:<br />AccountLoopBeingCreated<br />**Hex**:<br />80040507<br />**Number**:<br />-2147220217|Creating this parental association would create a loop in Accounts hierarchy.|
> |**Name**:<br />AccountLoopExists<br />**Hex**:<br />80040506<br />**Number**:<br />-2147220218|Loop exists in the accounts hierarchy.|
> |**Name**:<br />ActionCardDisabledError<br />**Hex**:<br />80071100<br />**Number**:<br />-2147020544|Action Card feature is not enabled.|
> |**Name**:<br />ActionCardInvalidStateCodeException<br />**Hex**:<br />80071103<br />**Number**:<br />-2147020541|Invalid state code passed in expression.|
> |**Name**:<br />ActionStepInvalidPipelineStageid<br />**Hex**:<br />8006040e<br />**Number**:<br />-2147089394|ActionStep references invalid Pipeline Stage Id.|
> |**Name**:<br />ActionStepInvalidProcessAction<br />**Hex**:<br />8006041c<br />**Number**:<br />-2147089380|ActionStep {0} references invalid Process Action {1}.|
> |**Name**:<br />ActionStepInvalidProcessid<br />**Hex**:<br />8006040d<br />**Number**:<br />-2147089395|ActionStep references invalid Process Id.|
> |**Name**:<br />ActionStepInvalidStageid<br />**Hex**:<br />8006040c<br />**Number**:<br />-2147089396|ActionStep references invalid Stage Id.|
> |**Name**:<br />ActionSupportNotEnabled<br />**Hex**:<br />80060382<br />**Number**:<br />-2147089534| Business Processes containing an Action Step cannot be exported because Action Step support is still a Public Preview feature and it is not currently enabled for this organization.|
> |**Name**:<br />ActivePropertyValidationFailed<br />**Hex**:<br />80061001<br />**Number**:<br />-2147086335|You can't create a property instance for an inactive property.|
> |**Name**:<br />ActiveQueueItemAlreadyExists<br />**Hex**:<br />80040526<br />**Number**:<br />-2147220186|An active queue item already exists for the given object. Cannot create more than one active queue item for this object.|
> |**Name**:<br />ActiveSlaCannotEdit<br />**Hex**:<br />8004F871<br />**Number**:<br />-2147157903|You can't edit an active SLA. Deactivate the SLA, and then try editing it.|
> |**Name**:<br />ActiveStageIdDoesNotMatchLastStageInTraversedPath<br />**Hex**:<br />80060455<br />**Number**:<br />-2147089323|Active Stage ID ‘{0}’ does not match last Stage ID in Traversed Path ‘{1}’. Please contact your system administrator.|
> |**Name**:<br />ActiveStageIDIsNull<br />**Hex**:<br />80060449<br />**Number**:<br />-2147089335|Error updating the Business Process: Active Stage ID cannot be empty.|
> |**Name**:<br />ActiveStageIsNotOnLeadEntity<br />**Hex**:<br />80100002<br />**Number**:<br />-2146435070|Active stage is not on 'Lead' entity.|
> |**Name**:<br />ActivityAnalysisOrganizationUpdateError<br />**Hex**:<br />80044275<br />**Number**:<br />-2147204491|Relationship Analytics organization setting can only be enabled if Relationship Analytics solution is installed.|
> |**Name**:<br />ActivityCannotHaveRelatedActivities<br />**Hex**:<br />8004F121<br />**Number**:<br />-2147159775|A custom entity defined as an activity must not have a relationship with Activities.|
> |**Name**:<br />ActivityEntityCannotBeActivityParty<br />**Hex**:<br />80048501<br />**Number**:<br />-2147187455|An activity entity cannot be also an activity party|
> |**Name**:<br />ActivityInvalidObjectTypeCode<br />**Hex**:<br />80043513<br />**Number**:<br />-2147207917|An Invalid type code was specified by the throwing method|
> |**Name**:<br />ActivityInvalidSessionToken<br />**Hex**:<br />80043512<br />**Number**:<br />-2147207918|An Invalid session token was passed into the throwing method|
> |**Name**:<br />ActivityMetadataUpdate<br />**Hex**:<br />8004F126<br />**Number**:<br />-2147159770|The metadata specified for activity is invalid.|
> |**Name**:<br />ActivityMustHaveRelatedNotes<br />**Hex**:<br />8004F123<br />**Number**:<br />-2147159773|A custom entity defined as an activity must have a relationship to Notes by default.|
> |**Name**:<br />ActivityPartyObjectTypeNotAllowed<br />**Hex**:<br />80043506<br />**Number**:<br />-2147207930|Cannot create activity party of specified object type.|
> |**Name**:<br />AdminProfileCannotBeEditedOrDeleted<br />**Hex**:<br />8004F50C<br />**Number**:<br />-2147158772|The System Administrator field security profile cannot be modified or deleted.|
> |**Name**:<br />AdvancedSimilarityAzureSearchUnexpectedError<br />**Hex**:<br />80061696<br />**Number**:<br />-2147084650|An unexpected error occurred executing the search. Try again later.|
> |**Name**:<br />AggregateInnerQuery<br />**Hex**:<br />8004D2B1<br />**Number**:<br />-2147167567|The Inner Query must not be an aggregate query.|
> |**Name**:<br />AggregateQueryRecordLimitExceeded<br />**Hex**:<br />8004E023<br />**Number**:<br />-2147164125|The maximum record limit is exceeded. Reduce the number of records.|
> |**Name**:<br />AlreadyLinkedToAnotherAttribute<br />**Hex**:<br />8004F0FE<br />**Number**:<br />-2147159810|Given linked attribute is alreadly linked to other attribute.|
> |**Name**:<br />AppConfigFeatureNotEnabled<br />**Hex**:<br />80072200<br />**Number**:<br />-2147016192|In-App Customization App Configuration feature is not enabled.|
> |**Name**:<br />ApplicationMetadataConverterFailed<br />**Hex**:<br />8005F231<br />**Number**:<br />-2147093967|Sorry, something went wrong. Please try again, or restart the app.|
> |**Name**:<br />ApplicationMetadatadaCreateFailed<br />**Hex**:<br />8005F233<br />**Number**:<br />-2147093965|Sorry, something went wrong. Please try again, or restart the app.|
> |**Name**:<br />ApplicationMetadatadaNullData<br />**Hex**:<br />8005F232<br />**Number**:<br />-2147093966|Sorry, something went wrong. Please try again, or restart the app.|
> |**Name**:<br />ApplicationMetadatadaUpdateFailed<br />**Hex**:<br />8005F234<br />**Number**:<br />-2147093964|Sorry, something went wrong. Please try again, or restart the app.|
> |**Name**:<br />ApplicationMetadataFailedWithContinue<br />**Hex**:<br />8005F241<br />**Number**:<br />-2147093951|There was a problem with the server configuration changes.  You can continue using the application, but may experience difficulties, including the inability to save changes. Please contact your Dynamics 365 administrator and give them the information available in ‘more information’.|
> |**Name**:<br />ApplicationMetadataGetPreviewMetadataUnknownError<br />**Hex**:<br />8005F230<br />**Number**:<br />-2147093968|Sorry, something went wrong. Please try again, or restart the app.|
> |**Name**:<br />ApplicationMetadataPrepareCustomizationsAppLock<br />**Hex**:<br />8005F237<br />**Number**:<br />-2147093961|We encountered some issues when we tried to prepare your customizations for your users. Users on some clients won't be able to download your customization updates until this issue is resolved.|
> |**Name**:<br />ApplicationMetadataPrepareCustomizationsRetrieverError<br />**Hex**:<br />8005F235<br />**Number**:<br />-2147093963|There was a problem with the server configuration changes.  Users can continue using the application, but may experience difficulties, including the inability to save changes.|
> |**Name**:<br />ApplicationMetadataPrepareCustomizationsTimeout<br />**Hex**:<br />8005F236<br />**Number**:<br />-2147093962|Sorry, but your client customization changes could not be processed.  This may be due to a large number of entities enabled for your users, or the number of languages enabled.  Users will not receive customizations until this issue is resolved.|
> |**Name**:<br />ApplicationMetadataPrepareCustomizationsUnknownError<br />**Hex**:<br />8005F226<br />**Number**:<br />-2147093978|Sorry, something went wrong. Please try again, or restart the app.|
> |**Name**:<br />ApplicationMetadataRetrieveUnknownError<br />**Hex**:<br />8005F229<br />**Number**:<br />-2147093975|Sorry, something went wrong. Please try again, or restart the app.|
> |**Name**:<br />ApplicationMetadataRetrieveUserContextUnknownError<br />**Hex**:<br />8005F227<br />**Number**:<br />-2147093977|Sorry, something went wrong. Please try again, or restart the app.|
> |**Name**:<br />ApplicationMetadataSyncAppLock<br />**Hex**:<br />8005F244<br />**Number**:<br />-2147093948|Sorry, your server is busy so configurations can’t be downloaded right now. Your changes should be available in a few minutes.  Wait a few minutes, and sign in again.|
> |**Name**:<br />ApplicationMetadataSyncAppLockWithContinue<br />**Hex**:<br />8005F245<br />**Number**:<br />-2147093947|Sorry, your server is busy so configuration changes can’t be downloaded right now. Your changes should be available in a few minutes.  In the meantime, you can continue using the app, and you’ll be reminded later to try downloading the changes. Or, you can wait a few minutes, restart the app, and accept the prompt to try again.|
> |**Name**:<br />ApplicationMetadataSyncFailed<br />**Hex**:<br />8005F240<br />**Number**:<br />-2147093952|There was a problem with the server configuration changes.  We are unable to load the application, please contact your Dynamics 365 administrator.|
> |**Name**:<br />ApplicationMetadataSyncTimeout<br />**Hex**:<br />8005F242<br />**Number**:<br />-2147093950|Sorry, but your server configuration changes could not be downloaded.  This may be due to a slow connection, or due to a large number of entities enabled for mobile use.  Please verify your connection and try again.  If this issue continues please contact your Dynamics 365 administrator.|
> |**Name**:<br />ApplicationMetadataSyncTimeoutWithContinue<br />**Hex**:<br />8005F243<br />**Number**:<br />-2147093949|Sorry, but your server configuration changes could not be downloaded.  This may be due to a slow connection, or due to a large number of entities enabled for mobile use.  Please verify your connection and try again. You can continue to use the app with the older configuration, however you may experience problems including errors when saving.  If this issue continues please contact your Dynamics 365 administrator.|
> |**Name**:<br />ApplicationMetadataSyncUnknownError<br />**Hex**:<br />8005F228<br />**Number**:<br />-2147093976|Sorry, something went wrong. Please try again, or restart the app.|
> |**Name**:<br />ApplicationMetadataUserValidationUnknownError<br />**Hex**:<br />8005F225<br />**Number**:<br />-2147093979|Sorry, something went wrong. Please try again, or restart the app.|
> |**Name**:<br />ApplicationNotRegisteredWithDeployment<br />**Hex**:<br />80041d49<br />**Number**:<br />-2147214007|Application needs to be registered and enabled at deployment level before it can be created for this organization|
> |**Name**:<br />ApplicationProfileMustContainEntity<br />**Hex**:<br />80071131<br />**Number**:<br />-2147020495|The application profile must contain at least one entity.|
> |**Name**:<br />ApplicationUserCannotBeUpdated<br />**Hex**:<br />80041d48<br />**Number**:<br />-2147214008|The user representing an OAuth application cannot not be updated|
> |**Name**:<br />AppLockTimeout<br />**Hex**:<br />8004Ed47<br />**Number**:<br />-2147160761|Timeout expired before applock could be acquired.|
> |**Name**:<br />ApplyActiveSLAOnly<br />**Hex**:<br />80055001<br />**Number**:<br />-2147135487|You can only apply active service level agreements (SLAs) to cases.|
> |**Name**:<br />AppModuleComponentEntityMustHaveFormOrView<br />**Hex**:<br />80050115<br />**Number**:<br />-2147155691|The entity “{0}” must have at least one form or view in the app.|
> |**Name**:<br />AppModuleFeatureNotEnabled<br />**Hex**:<br />80050117<br />**Number**:<br />-2147155689|The feature isn’t turned on for this organization.|
> |**Name**:<br />AppModuleMustHaveOnlyValidClientEntity<br />**Hex**:<br />8005012A<br />**Number**:<br />-2147155670|The “{0}” entity isn’t valid for the chosen client, and won’t be shown at runtime.|
> |**Name**:<br />AppModuleNotContainMOCAEnabledEntity<br />**Hex**:<br />80050118<br />**Number**:<br />-2147155688|App Module with MOCA as a supported client should have at least one MOCA enabled entity|
> |**Name**:<br />AppModuleNotReferEntity<br />**Hex**:<br />8005011D<br />**Number**:<br />-2147155683|App Module does not reference at least one entity|
> |**Name**:<br />AppModulesImportError<br />**Hex**:<br />80050123<br />**Number**:<br />-2147155677|An error occurred while importing App Modules|
> |**Name**:<br />AppModuleWithClientExists<br />**Hex**:<br />80050127<br />**Number**:<br />-2147155673|Couldn’t create the app. There’s already an app for this client type.|
> |**Name**:<br />AppointmentDeleted<br />**Hex**:<br />8004E106<br />**Number**:<br />-2147163898|The appointment entity instance is already deleted.|
> |**Name**:<br />AppointmentScheduleNotSet<br />**Hex**:<br />80040275<br />**Number**:<br />-2147220875|Scheduled End and Scheduled Start must be set for Appointments in order to sync with Outlook.|
> |**Name**:<br />ArgumentDirectionMismatch<br />**Hex**:<br />80060388<br />**Number**:<br />-2147089528|Direction mismatch for argument {0}.|
> |**Name**:<br />ArgumentTypeMismatch<br />**Hex**:<br />80060387<br />**Number**:<br />-2147089529|Type mismatch for argument {0}.|
> |**Name**:<br />ArrayMappingFoundForSingletonParameter<br />**Hex**:<br />8004037f<br />**Number**:<br />-2147220609|An array transformation parameter mapping is defined for a single parameter.|
> |**Name**:<br />ArticleIsPublished<br />**Hex**:<br />800404fe<br />**Number**:<br />-2147220226|The article cannot be updated or deleted because it is in published state|
> |**Name**:<br />AssociateProductFailureDifferentUom<br />**Hex**:<br />80061040<br />**Number**:<br />-2147086272|The product can't be added to the bundle. You have to use a product unit that belongs to the unit group of the product.|
> |**Name**:<br />AssociationRoleOrdinalInvalid<br />**Hex**:<br />80048468<br />**Number**:<br />-2147187608|The association role ordinal is not valid - it must be 1 or 2.|
> |**Name**:<br />AsyncCommunicationError<br />**Hex**:<br />80044307<br />**Number**:<br />-2147204345|A communication error occurred while processing the async operation.|
> |**Name**:<br />AsyncNetworkError<br />**Hex**:<br />80044306<br />**Number**:<br />-2147204346|An error occurred while accessing the network.|
> |**Name**:<br />AsyncOperationCannotCancel<br />**Hex**:<br />80044F00<br />**Number**:<br />-2147201280|This system job cannot be canceled.|
> |**Name**:<br />AsyncOperationCannotDeleteUnlessCompleted<br />**Hex**:<br />8004416a<br />**Number**:<br />-2147204758|Cannot delete async operation unless it is in Completed state.|
> |**Name**:<br />AsyncOperationCannotPause<br />**Hex**:<br />80044F01<br />**Number**:<br />-2147201279|This system job cannot be paused.|
> |**Name**:<br />AsyncOperationCannotUpdateNonrecurring<br />**Hex**:<br />80044168<br />**Number**:<br />-2147204760|Cannot update recurrence pattern for a job that is not recurring.|
> |**Name**:<br />AsyncOperationCannotUpdateRecurring<br />**Hex**:<br />80044169<br />**Number**:<br />-2147204759|Cannot update recurrence pattern for a job type that is not supported.|
> |**Name**:<br />AsyncOperationInvalidStateChange<br />**Hex**:<br />80044162<br />**Number**:<br />-2147204766|The target state could not be set because the state transition is not valid.|
> |**Name**:<br />AsyncOperationInvalidStateChangeToComplete<br />**Hex**:<br />80044165<br />**Number**:<br />-2147204763|The target state could not be set to complete because the state transition is not valid.|
> |**Name**:<br />AsyncOperationInvalidStateChangeToReady<br />**Hex**:<br />80044166<br />**Number**:<br />-2147204762|The target state could not be set to ready because the state transition is not valid.|
> |**Name**:<br />AsyncOperationInvalidStateChangeToSuspended<br />**Hex**:<br />80044167<br />**Number**:<br />-2147204761|The target state could not be set to suspended because the state transition is not valid.|
> |**Name**:<br />AsyncOperationInvalidStateChangeUnexpected<br />**Hex**:<br />80044163<br />**Number**:<br />-2147204765|The target state could not be set because the state was changed by another process.|
> |**Name**:<br />AsyncOperationMissingId<br />**Hex**:<br />80044164<br />**Number**:<br />-2147204764|The AsyncOperationId is required to do the update.|
> |**Name**:<br />AsyncOperationPostponed<br />**Hex**:<br />80040328<br />**Number**:<br />-2147220696|This operation has been postponed because it failed for more than {0} times in {1} minutes|
> |**Name**:<br />AsyncOperationPostponedByExceptionCountThrottle<br />**Hex**:<br />80060917<br />**Number**:<br />-2147088105|Currently, we are unable to complete this action. It has been postponed. We will try again later.|
> |**Name**:<br />AsyncOperationSuspendedOrLocked<br />**Hex**:<br />80040339<br />**Number**:<br />-2147220679|>A background job associated with this import is either suspended or locked. In order to delete this import, in the Workplace, click Imports, open the import, click System Jobs, and resume any suspended jobs.|
> |**Name**:<br />AsyncOperationTypeIsNotRecognized<br />**Hex**:<br />80044303<br />**Number**:<br />-2147204349|The operation type of the async operation was not recognized.|
> |**Name**:<br />AsyncOperationTypeThrottled<br />**Hex**:<br />80060916<br />**Number**:<br />-2147088106|The job could not be completed because the server is busy. We will retry the job again soon.|
> |**Name**:<br />AttachmentBlocked<br />**Hex**:<br />80043e09<br />**Number**:<br />-2147205623|The attachment is either not a valid type or is too large. It cannot be uploaded or downloaded.|
> |**Name**:<br />AttachmentInvalidFileName<br />**Hex**:<br />80044a08<br />**Number**:<br />-2147202552|Attachment file name contains invalid characters.|
> |**Name**:<br />AttachmentNotFound<br />**Hex**:<br />80048493<br />**Number**:<br />-2147187565|The reference to the attachment couldn't be found.|
> |**Name**:<br />AttachmentNotRelatedToEmail<br />**Hex**:<br />80050006<br />**Number**:<br />-2147155962|This attachment does not belong to an email.|
> |**Name**:<br />AttributeCannotBeUpdated<br />**Hex**:<br />80060413<br />**Number**:<br />-2147089389|Attribute - {0} cannot be updated for a Business Process Flow|
> |**Name**:<br />AttributeCannotBeUsedInAggregate<br />**Hex**:<br />80060559<br />**Number**:<br />-2147089063|The {0} attribute cannot be used with an aggregation function in a formula.|
> |**Name**:<br />AttributeDeprecated<br />**Hex**:<br />80044335<br />**Number**:<br />-2147204299|"Attribute '{0}' on entity '{1}' is deprecated."|
> |**Name**:<br />AttributeDoesNotSupportLocalizedLabels<br />**Hex**:<br />80044198<br />**Number**:<br />-2147204712|The specified attribute does not support localized labels.|
> |**Name**:<br />AttributeFormulaDefinitionIsEmpty<br />**Hex**:<br />80060439<br />**Number**:<br />-2147089351|The formula is empty.|
> |**Name**:<br />AttributeIsNotCustomAttribute<br />**Hex**:<br />80047009<br />**Number**:<br />-2147192823|The specified attribute is not a custom attribute|
> |**Name**:<br />AttributeIsNotFacetable<br />**Hex**:<br />80060305<br />**Number**:<br />-2147089659|Cannot set user search facets for entity {0} as attribute {1} is not facetable. Kindly remove it from the list to proceed.|
> |**Name**:<br />AttributeNotCreatedForOfficeGraphError<br />**Hex**:<br />80044237<br />**Number**:<br />-2147204553|This attribute cannot be created since support to enable attribute for officegraph is not available.|
> |**Name**:<br />AttributeNotOfTypePicklist<br />**Hex**:<br />8004033c<br />**Number**:<br />-2147220676|This attribute is not mapped to a drop-down list, Boolean, or state/status attribute. However, you have included a ListValueMap element for it.  Fix this inconsistency, and then import this data map again.|
> |**Name**:<br />AttributeNotOfTypeReference<br />**Hex**:<br />80040390<br />**Number**:<br />-2147220592|This attribute is not mapped as a reference attribute. However, you have included a ReferenceMap for it.  Fix this inconsistency, and then import this data map again.|
> |**Name**:<br />AttributeNotSecured<br />**Hex**:<br />8004F508<br />**Number**:<br />-2147158776|One or more fields are not enabled for field level security. Field level security is not enabled until you publish the customizations.|
> |**Name**:<br />AttributeNotUpdatedForOfficeGraphError<br />**Hex**:<br />80044238<br />**Number**:<br />-2147204552|This attribute cannot be updated since support to enable attribute for officegraph is not available.|
> |**Name**:<br />AttributePermissionIsInvalid<br />**Hex**:<br />8004F50E<br />**Number**:<br />-2147158770|Permission '{0}' for field '{1}' with id={2} is invalid.|
> |**Name**:<br />AttributePermissionReadIsMissing<br />**Hex**:<br />8004F504<br />**Number**:<br />-2147158780|The user does not have read permissions to a secured field. The requested operation could not be completed.|
> |**Name**:<br />AttributePermissionUpdateIsMissingDuringShare<br />**Hex**:<br />8004F503<br />**Number**:<br />-2147158781|The user does not have update permissions to a secured field. The requested operation could not be completed.|
> |**Name**:<br />AttributePermissionUpdateIsMissingDuringUpdate<br />**Hex**:<br />8004F507<br />**Number**:<br />-2147158777|The user doesn't have AttributePrivilegeUpdate and not granted shared access for a secured attribute during update operation|
> |**Name**:<br />AttributePrivilegeCreateIsMissing<br />**Hex**:<br />8004F502<br />**Number**:<br />-2147158782|The user does not have create permissions to a secured field. The requested operation could not be completed.|
> |**Name**:<br />AttributePrivilegeInvalidToUnsecure<br />**Hex**:<br />8004F50D<br />**Number**:<br />-2147158771|You must have sufficient permissions for a secured field before you can change its field level security.|
> |**Name**:<br />AttributesExceeded<br />**Hex**:<br />80061501<br />**Number**:<br />-2147085055|Attributes cannot be more than 4|
> |**Name**:<br />AttributeSharingCreateDuplicate<br />**Hex**:<br />8004F50B<br />**Number**:<br />-2147158773|Attribute has already been shared.|
> |**Name**:<br />AttributeSharingCreateShouldSetReadOrAndUpdateAccess<br />**Hex**:<br />8004F509<br />**Number**:<br />-2147158775|You must set read and/or update access when you share a secured attribute. Attribute ID: {0}|
> |**Name**:<br />AttributeSharingUpdateInvalid<br />**Hex**:<br />8004F50A<br />**Number**:<br />-2147158774|Both readAccess and updateAccess are false: call Delete instead of Update.|
> |**Name**:<br />AttributeTypeNotSupportedForCalculatedField<br />**Hex**:<br />80050221<br />**Number**:<br />-2147155423|Calculated/RollUp Field is not supported for MultiSelectPicklist Attribute Type.|
> |**Name**:<br />AttributeTypeNotSupportedForGroupByOrderByQuery<br />**Hex**:<br />80050224<br />**Number**:<br />-2147155420|GroupBy or OrderBy Query is not supported for MultiSelectPickList Attribute Type.|
> |**Name**:<br />AttributeUpdateNotAllowed<br />**Hex**:<br />80060463<br />**Number**:<br />-2147089309|The Business Process Flow update has failed. The update of attribute "{0}" in workflow "{1}" is not allowed.|
> |**Name**:<br />AuthenticateToServerBeforeRequestingProxy<br />**Hex**:<br />8004D228<br />**Number**:<br />-2147167704|Authenticate to serverType: {0} before requesting a proxy.|
> |**Name**:<br />AutoDataCaptureAuthorizationFailureException<br />**Hex**:<br />80091042<br />**Number**:<br />-2146889662|You don’t have the proper Office 365 license to get untracked emails. Please contact your system administrator.|
> |**Name**:<br />AutoDataCaptureDisabledError<br />**Hex**:<br />80091041<br />**Number**:<br />-2146889663|Auto capture feature is not enabled.|
> |**Name**:<br />AutoDataCaptureResponseRetrievalFailureException<br />**Hex**:<br />80091043<br />**Number**:<br />-2146889661|Error while fetching untracked emails from Exchange.|
> |**Name**:<br />AzureApplicationIdNotFound<br />**Hex**:<br />8004F510<br />**Number**:<br />-2147158768|We didn’t find that application ID {0} in your Azure Active Directory (Azure AD) with CorrelationID {1}. Make sure your application is registered in Azure AD.|
> |**Name**:<br />AzureApplicationIdNotFoundInOrgDB<br />**Hex**:<br />8004F512<br />**Number**:<br />-2147158766|Azure applicationid not found. We didn’t find the application ID {0} in your CRM database. Correct the application ID and resubmit the update.|
> |**Name**:<br />AzureOperationResponseTimedOut<br />**Hex**:<br />80061635<br />**Number**:<br />-2147084747|An Azure operation request did not return a response within stated timeout period. Retry the operation or increase timeout provided for the operation.|
> |**Name**:<br />AzureRecommendationModelBuildNotExist<br />**Hex**:<br />80061604<br />**Number**:<br />-2147084796|The Azure recommendation model build corresponding to the used model version doesn’t exist.|
> |**Name**:<br />AzureRecommendationModelNotExist<br />**Hex**:<br />80061603<br />**Number**:<br />-2147084797|The Azure recommendation model doesn’t exist.|
> |**Name**:<br />AzureServiceConnectionCascadeDeleteFailed<br />**Hex**:<br />80061636<br />**Number**:<br />-2147084746|One or more models use the connection. Delete all models using this connection, and try deleting the connection again.|
> |**Name**:<br />AzureServiceConnectionInvalidUri<br />**Hex**:<br />80061630<br />**Number**:<br />-2147084752|Provide a valid service URL.|
> |**Name**:<br />AzureSqlDatabaseResourceLimitExceededError<br />**Hex**:<br />80072323<br />**Number**:<br />-2147015901|The limit of resource for the database has been reached. Please check the exception for more details.|
> |**Name**:<br />AzureSqlDatabaseStorageQuotaExceededError<br />**Hex**:<br />80072325<br />**Number**:<br />-2147015899|The storage limit for the database has been met.|
> |**Name**:<br />AzureSqlMaxConcurrentWorkersLimitExceededError<br />**Hex**:<br />80072324<br />**Number**:<br />-2147015900|Too many concurrent requests detected.|
> |**Name**:<br />AzureWebAppPluginsDisabled<br />**Hex**:<br />80050241<br />**Number**:<br />-2147155391|Azure WebApp based plugins disabled for the organization.|
> |**Name**:<br />BadAuthTicket<br />**Hex**:<br />8004A102<br />**Number**:<br />-2147180286|The ticket specified for authentication is invalid|
> |**Name**:<br />BadRequest<br />**Hex**:<br />8005F100<br />**Number**:<br />-2147094272|The request could not be understood by the server.|
> |**Name**:<br />BaseAttributeNameNotPresentError<br />**Hex**:<br />80044240<br />**Number**:<br />-2147204544|BaseAttribute name should be present in condition xml.|
> |**Name**:<br />BaseCurrencyCannotBeDeactivated<br />**Hex**:<br />80048cf4<br />**Number**:<br />-2147185420|The base currency cannot be deactivated.|
> |**Name**:<br />BaseCurrencyNotDeletable<br />**Hex**:<br />80048cff<br />**Number**:<br />-2147185409|The base currency of an organization cannot be deleted.|
> |**Name**:<br />BaseCurrencyOverflow<br />**Hex**:<br />80048cec<br />**Number**:<br />-2147185428|The exchange rate set for the currency specified in this record has generated a value for {0} that is larger than the maximum allowed for the base currency ({1}).|
> |**Name**:<br />BaseCurrencyUnderflow<br />**Hex**:<br />80048ceb<br />**Number**:<br />-2147185429|The exchange rate set for the currency specified in this record has generated a value for {0} that is smaller than the minimum allowed for the base currency ({1}).|
> |**Name**:<br />BaseMatchingAttributeNotSameError<br />**Hex**:<br />80044245<br />**Number**:<br />-2147204539|Base and Matching attribute should be of same type.|
> |**Name**:<br />BaseUnitDoesNotExist<br />**Hex**:<br />80043b1c<br />**Number**:<br />-2147206372|The base unit does not exist.|
> |**Name**:<br />BaseUnitNotDeletable<br />**Hex**:<br />80043b03<br />**Number**:<br />-2147206397|The base unit of a schedule cannot be deleted.|
> |**Name**:<br />BaseUnitNotNull<br />**Hex**:<br />80043b17<br />**Number**:<br />-2147206377|Do not use a base unit as the value for a primary unit. This value should always be null.|
> |**Name**:<br />BaseUomNameNotSpecified<br />**Hex**:<br />80043810<br />**Number**:<br />-2147207152|baseuomname not specified|
> |**Name**:<br />BDK_E_ADDRESS_VALIDATION_FAILURE<br />**Hex**:<br />8004B540<br />**Number**:<br />-2147175104|{0}  |
> |**Name**:<br />BDK_E_AGREEMENT_ALREADY_SIGNED<br />**Hex**:<br />8004B541<br />**Number**:<br />-2147175103|{0}  |
> |**Name**:<br />BDK_E_AUTHORIZATION_FAILED<br />**Hex**:<br />8004B542<br />**Number**:<br />-2147175102|{0}  |
> |**Name**:<br />BDK_E_AVS_FAILED<br />**Hex**:<br />8004B543<br />**Number**:<br />-2147175101|{0}  |
> |**Name**:<br />BDK_E_BAD_CITYNAME_LENGTH<br />**Hex**:<br />8004B544<br />**Number**:<br />-2147175100|{0}  |
> |**Name**:<br />BDK_E_BAD_STATECODE_LENGTH<br />**Hex**:<br />8004B545<br />**Number**:<br />-2147175099|{0}  |
> |**Name**:<br />BDK_E_BAD_ZIPCODE_LENGTH<br />**Hex**:<br />8004B546<br />**Number**:<br />-2147175098|{0}  |
> |**Name**:<br />BDK_E_BADXML<br />**Hex**:<br />8004B547<br />**Number**:<br />-2147175097|{0}  |
> |**Name**:<br />BDK_E_BANNED_PAYMENT_INSTRUMENT<br />**Hex**:<br />8004B548<br />**Number**:<br />-2147175096|{0}  |
> |**Name**:<br />BDK_E_BANNEDPERSON<br />**Hex**:<br />8004B549<br />**Number**:<br />-2147175095|{0}  |
> |**Name**:<br />BDK_E_CANNOT_EXCEED_MAX_OWNERSHIP<br />**Hex**:<br />8004B54A<br />**Number**:<br />-2147175094|{0}  |
> |**Name**:<br />BDK_E_COUNTRY_CURRENCY_PI_MISMATCH<br />**Hex**:<br />8004B54B<br />**Number**:<br />-2147175093|{0}  |
> |**Name**:<br />BDK_E_CREDIT_CARD_EXPIRED<br />**Hex**:<br />8004B54C<br />**Number**:<br />-2147175092|{0}  |
> |**Name**:<br />BDK_E_DATE_EXPIRED<br />**Hex**:<br />8004B54D<br />**Number**:<br />-2147175091|{0}  |
> |**Name**:<br />BDK_E_ERROR_COUNTRYCODE_MISMATCH<br />**Hex**:<br />8004B54E<br />**Number**:<br />-2147175090|{0}  |
> |**Name**:<br />BDK_E_ERROR_COUNTRYCODE_REQUIRED<br />**Hex**:<br />8004B54F<br />**Number**:<br />-2147175089|{0}  |
> |**Name**:<br />BDK_E_EXTRA_REFERRAL_DATA<br />**Hex**:<br />8004B550<br />**Number**:<br />-2147175088|{0}  |
> |**Name**:<br />BDK_E_GUID_EXISTS<br />**Hex**:<br />8004B551<br />**Number**:<br />-2147175087|{0}  |
> |**Name**:<br />BDK_E_INVALID_ADDRESS_ID<br />**Hex**:<br />8004B552<br />**Number**:<br />-2147175086|{0}  |
> |**Name**:<br />BDK_E_INVALID_BILLABLE_ACCOUNT_ID<br />**Hex**:<br />8004B553<br />**Number**:<br />-2147175085|{0}  The specified Billing account is invalid.  Or, although the objectID is of the correct type, the account it identifies does not exist in the system.|
> |**Name**:<br />BDK_E_INVALID_BUF_SIZE<br />**Hex**:<br />8004B554<br />**Number**:<br />-2147175084|{0}  |
> |**Name**:<br />BDK_E_INVALID_CATEGORY_NAME<br />**Hex**:<br />8004B555<br />**Number**:<br />-2147175083|{0}  |
> |**Name**:<br />BDK_E_INVALID_COUNTRY_CODE<br />**Hex**:<br />8004B556<br />**Number**:<br />-2147175082|{0}  |
> |**Name**:<br />BDK_E_INVALID_CURRENCY<br />**Hex**:<br />8004B557<br />**Number**:<br />-2147175081|{0}  |
> |**Name**:<br />BDK_E_INVALID_CUSTOMER_TYPE<br />**Hex**:<br />8004B558<br />**Number**:<br />-2147175080|{0}  |
> |**Name**:<br />BDK_E_INVALID_DATE<br />**Hex**:<br />8004B559<br />**Number**:<br />-2147175079|{0}  |
> |**Name**:<br />BDK_E_INVALID_EMAIL_ADDRESS<br />**Hex**:<br />8004B55A<br />**Number**:<br />-2147175078|{0}  |
> |**Name**:<br />BDK_E_INVALID_FILTER<br />**Hex**:<br />8004B55B<br />**Number**:<br />-2147175077|{0}  |
> |**Name**:<br />BDK_E_INVALID_GUID<br />**Hex**:<br />8004B55C<br />**Number**:<br />-2147175076|{0}  |
> |**Name**:<br />BDK_E_INVALID_INPUT_TO_TAXWARE_OR_VERAZIP<br />**Hex**:<br />8004B55D<br />**Number**:<br />-2147175075|{0}  |
> |**Name**:<br />BDK_E_INVALID_LOCALE<br />**Hex**:<br />8004B55E<br />**Number**:<br />-2147175074|{0}  |
> |**Name**:<br />BDK_E_INVALID_OBJECT_ID<br />**Hex**:<br />8004B55F<br />**Number**:<br />-2147175073|{0}  The Billing system cannot find the object (e.g. account or subscription or offering).|
> |**Name**:<br />BDK_E_INVALID_OFFERING_GUID<br />**Hex**:<br />8004B560<br />**Number**:<br />-2147175072|{0}  |
> |**Name**:<br />BDK_E_INVALID_PAYMENT_INSTRUMENT_STATUS<br />**Hex**:<br />8004B561<br />**Number**:<br />-2147175071|{0}  |
> |**Name**:<br />BDK_E_INVALID_PAYMENT_METHOD_ID<br />**Hex**:<br />8004B562<br />**Number**:<br />-2147175070|{0}  |
> |**Name**:<br />BDK_E_INVALID_PHONE_TYPE<br />**Hex**:<br />8004B563<br />**Number**:<br />-2147175069|{0}  |
> |**Name**:<br />BDK_E_INVALID_POLICY_ID<br />**Hex**:<br />8004B564<br />**Number**:<br />-2147175068|{0}  |
> |**Name**:<br />BDK_E_INVALID_REFERRALDATA_XML<br />**Hex**:<br />8004B565<br />**Number**:<br />-2147175067|{0}  |
> |**Name**:<br />BDK_E_INVALID_STATE_FOR_COUNTRY<br />**Hex**:<br />8004B566<br />**Number**:<br />-2147175066|{0}  |
> |**Name**:<br />BDK_E_INVALID_SUBSCRIPTION_ID<br />**Hex**:<br />8004B567<br />**Number**:<br />-2147175065|{0}  The subscription id specified is invalid.  Or, although the objectID is of correct type and also points to a valid account in SCS, the subscription it identifies does not exist in SCS.|
> |**Name**:<br />BDK_E_INVALID_TAX_EXEMPT_TYPE<br />**Hex**:<br />8004B568<br />**Number**:<br />-2147175064|{0}  |
> |**Name**:<br />BDK_E_MEG_CONFLICT<br />**Hex**:<br />8004B569<br />**Number**:<br />-2147175063|{0}  |
> |**Name**:<br />BDK_E_MULTIPLE_CITIES_FOUND<br />**Hex**:<br />8004B56A<br />**Number**:<br />-2147175062|{0}  |
> |**Name**:<br />BDK_E_MULTIPLE_COUNTIES_FOUND<br />**Hex**:<br />8004B56B<br />**Number**:<br />-2147175061|{0}  |
> |**Name**:<br />BDK_E_NON_ACTIVE_ACCOUNT<br />**Hex**:<br />8004B56C<br />**Number**:<br />-2147175060|{0}  |
> |**Name**:<br />BDK_E_NOPERMISSION<br />**Hex**:<br />8004B56D<br />**Number**:<br />-2147175059|{0}  The calling partner does not have access to this method or when the requester does not have permission to search against the supplied search PUID.|
> |**Name**:<br />BDK_E_OBJECT_ROLE_LIMIT_EXCEEDED<br />**Hex**:<br />8004B56E<br />**Number**:<br />-2147175058|{0}  |
> |**Name**:<br />BDK_E_OFFERING_ACCOUNT_CURRENCY_MISMATCH<br />**Hex**:<br />8004B56F<br />**Number**:<br />-2147175057|{0}  |
> |**Name**:<br />BDK_E_OFFERING_COUNTRY_ACCOUNT_MISMATCH<br />**Hex**:<br />8004B570<br />**Number**:<br />-2147175056|{0}  |
> |**Name**:<br />BDK_E_OFFERING_NOT_PURCHASEABLE<br />**Hex**:<br />8004B571<br />**Number**:<br />-2147175055|{0}  |
> |**Name**:<br />BDK_E_OFFERING_PAYMENT_INSTRUMENT_MISMATCH<br />**Hex**:<br />8004B572<br />**Number**:<br />-2147175054|{0}  |
> |**Name**:<br />BDK_E_OFFERING_REQUIRES_PI<br />**Hex**:<br />8004B573<br />**Number**:<br />-2147175053|{0}  |
> |**Name**:<br />BDK_E_PARTNERNOTINBILLING<br />**Hex**:<br />8004B574<br />**Number**:<br />-2147175052|{0}  |
> |**Name**:<br />BDK_E_PAYMENT_PROVIDER_CONNECTION_FAILED<br />**Hex**:<br />8004B575<br />**Number**:<br />-2147175051|{0}  |
> |**Name**:<br />BDK_E_POLICY_DEAL_COUNTRY_MISMATCH<br />**Hex**:<br />8004B577<br />**Number**:<br />-2147175049|{0}  |
> |**Name**:<br />BDK_E_PRIMARY_PHONE_REQUIRED<br />**Hex**:<br />8004B576<br />**Number**:<br />-2147175050|{0}  |
> |**Name**:<br />BDK_E_PUID_ROLE_LIMIT_EXCEEDED<br />**Hex**:<br />8004B578<br />**Number**:<br />-2147175048|{0}  |
> |**Name**:<br />BDK_E_RATING_FAILURE<br />**Hex**:<br />8004B579<br />**Number**:<br />-2147175047|{0}  |
> |**Name**:<br />BDK_E_REQUIRED_FIELD_MISSING<br />**Hex**:<br />8004B57A<br />**Number**:<br />-2147175046|{0}  |
> |**Name**:<br />BDK_E_STATE_CITY_INVALID<br />**Hex**:<br />8004B57B<br />**Number**:<br />-2147175045|{0}  |
> |**Name**:<br />BDK_E_STATE_INVALID<br />**Hex**:<br />8004B57C<br />**Number**:<br />-2147175044|{0}  |
> |**Name**:<br />BDK_E_STATE_ZIP_CITY_INVALID<br />**Hex**:<br />8004B57D<br />**Number**:<br />-2147175043|{0}  |
> |**Name**:<br />BDK_E_STATE_ZIP_CITY_INVALID2<br />**Hex**:<br />8004B57E<br />**Number**:<br />-2147175042|{0}  |
> |**Name**:<br />BDK_E_STATE_ZIP_CITY_INVALID3<br />**Hex**:<br />8004B57F<br />**Number**:<br />-2147175041|{0}  |
> |**Name**:<br />BDK_E_STATE_ZIP_CITY_INVALID4<br />**Hex**:<br />8004B580<br />**Number**:<br />-2147175040|{0}  |
> |**Name**:<br />BDK_E_STATE_ZIP_COVERS_MULTIPLE_CITIES<br />**Hex**:<br />8004B581<br />**Number**:<br />-2147175039|{0}  |
> |**Name**:<br />BDK_E_STATE_ZIP_INVALID<br />**Hex**:<br />8004B582<br />**Number**:<br />-2147175038|{0}  |
> |**Name**:<br />BDK_E_TAXID_EXPDATE<br />**Hex**:<br />8004B583<br />**Number**:<br />-2147175037|{0}  |
> |**Name**:<br />BDK_E_TOKEN_BLACKLISTED<br />**Hex**:<br />8004B584<br />**Number**:<br />-2147175036|{0}  |
> |**Name**:<br />BDK_E_TOKEN_EXPIRED<br />**Hex**:<br />8004B585<br />**Number**:<br />-2147175035|{0}  |
> |**Name**:<br />BDK_E_TOKEN_NOT_VALID_FOR_OFFERING<br />**Hex**:<br />8004B586<br />**Number**:<br />-2147175034|{0}  |
> |**Name**:<br />BDK_E_TOKEN_RANGE_BLACKLISTED<br />**Hex**:<br />8004B587<br />**Number**:<br />-2147175033|{0}  |
> |**Name**:<br />BDK_E_TRANS_BALANCE_TO_PI_INVALID<br />**Hex**:<br />8004B588<br />**Number**:<br />-2147175032|{0}  |
> |**Name**:<br />BDK_E_UNKNOWN_SERVER_FAILURE<br />**Hex**:<br />8004B589<br />**Number**:<br />-2147175031|{0}  Unknown server failure.|
> |**Name**:<br />BDK_E_UNSUPPORTED_CHAR_EXIST<br />**Hex**:<br />8004B58A<br />**Number**:<br />-2147175030|{0}  |
> |**Name**:<br />BDK_E_USAGE_COUNT_FOR_TOKEN_EXCEEDED<br />**Hex**:<br />8004B58F<br />**Number**:<br />-2147175025|{0}  Billing token is already spent.|
> |**Name**:<br />BDK_E_VATID_DOESNOTHAVEEXPDATE<br />**Hex**:<br />8004B58B<br />**Number**:<br />-2147175029|{0}  |
> |**Name**:<br />BDK_E_ZIP_CITY_MISSING<br />**Hex**:<br />8004B58C<br />**Number**:<br />-2147175028|{0}  |
> |**Name**:<br />BDK_E_ZIP_INVALID<br />**Hex**:<br />8004B58D<br />**Number**:<br />-2147175027|{0}  Billing zip code error.|
> |**Name**:<br />BDK_E_ZIP_INVALID_FOR_ENTERED_STATE<br />**Hex**:<br />8004B58E<br />**Number**:<br />-2147175026|{0}  Billing zip code error.|
> |**Name**:<br />BidsAuthenticationError<br />**Hex**:<br />8005E003<br />**Number**:<br />-2147098621|An error occured while authenticating with server {0}.|
> |**Name**:<br />BidsAuthenticationFailed<br />**Hex**:<br />8005E006<br />**Number**:<br />-2147098618|Authentication failed when trying to connect to server {0}. The username or password is incorrect.|
> |**Name**:<br />BidsInvalidConnectionString<br />**Hex**:<br />8005E000<br />**Number**:<br />-2147098624|Input connection string is invalid. Usage: ServerUrl[;OrganizationName][;HomeRealmUrl]|
> |**Name**:<br />BidsInvalidUrl<br />**Hex**:<br />8005E001<br />**Number**:<br />-2147098623|Input url {0} is invalid.|
> |**Name**:<br />BidsNoOrganizationsFound<br />**Hex**:<br />8005E004<br />**Number**:<br />-2147098620|No organizations found for the user.|
> |**Name**:<br />BidsOrganizationNotFound<br />**Hex**:<br />8005E005<br />**Number**:<br />-2147098619|Organization {0} cannot be found for the user.|
> |**Name**:<br />BidsServerConnectionFailed<br />**Hex**:<br />8005E002<br />**Number**:<br />-2147098622|Failed to connect to server {0}.|
> |**Name**:<br />BillingNoSettingError<br />**Hex**:<br />8004B531<br />**Number**:<br />-2147175119|No Billing application configuration setting [{0}] was found.|
> |**Name**:<br />BillingPartnerCertificate<br />**Hex**:<br />8004B530<br />**Number**:<br />-2147175120|Could not determine the right Partner certificate to use with Billing.  Issuer: {0}  Subject: {1}  Distinguished matches: [{2}]  Name matches: [{3}]  All valid certificates: [{4}].|
> |**Name**:<br />BillingRetrieveKeyError<br />**Hex**:<br />8004B538<br />**Number**:<br />-2147175112|Could not retrieve Billing session key: "{0}"|
> |**Name**:<br />BillingTestConnectionError<br />**Hex**:<br />8004B532<br />**Number**:<br />-2147175118|Billing is not available: Call to IsServiceAvailable returned 'False'.|
> |**Name**:<br />BillingTestConnectionException<br />**Hex**:<br />8004B533<br />**Number**:<br />-2147175117|Billing TestConnection exception.|
> |**Name**:<br />BillingUnknownErrorCode<br />**Hex**:<br />8004B536<br />**Number**:<br />-2147175114|Billing error code [{0}] was thrown with exception {1}|
> |**Name**:<br />BillingUnknownException<br />**Hex**:<br />8004B537<br />**Number**:<br />-2147175113|Billing error was thrown with exception {0}|
> |**Name**:<br />BillingUnmappedErrorCode<br />**Hex**:<br />8004B535<br />**Number**:<br />-2147175115|Billing error code [{0}] was thrown with exception {1}|
> |**Name**:<br />BillingUserPuidNullError<br />**Hex**:<br />8004B534<br />**Number**:<br />-2147175116|User Puid is required, but is null.|
> |**Name**:<br />BookFirstInstanceFailed<br />**Hex**:<br />8004E10E<br />**Number**:<br />-2147163890|Failed to book first instance.|
> |**Name**:<br />BooleanOptionOutOfRange<br />**Hex**:<br />8004431C<br />**Number**:<br />-2147204324|Boolean attribute options must have a value of either 0 or 1.|
> |**Name**:<br />BothConnectionSidesAreNeeded<br />**Hex**:<br />80048218<br />**Number**:<br />-2147188200|You must provide a name or select a role for both sides of this connection.|
> |**Name**:<br />BPFEntityAlreadyExists<br />**Hex**:<br />80060384<br />**Number**:<br />-2147089532|BPF entity with this name already exists.|
> |**Name**:<br />BpfEntityServiceIsNull<br />**Hex**:<br />80060446<br />**Number**:<br />-2147089338|Error creating or updating Business Process: BpfEntityService cannot be null.|
> |**Name**:<br />BpfFactoryIsNull<br />**Hex**:<br />80060447<br />**Number**:<br />-2147089337|Error creating or updating Business Process: BpfFactory cannot be null.|
> |**Name**:<br />BpfInstanceAlreadyExists<br />**Hex**:<br />80060397<br />**Number**:<br />-2147089513|A business process flow already exists for the target record and could not be created. Please contact your system administrator.|
> |**Name**:<br />BpfVisitorIsNull<br />**Hex**:<br />80060448<br />**Number**:<br />-2147089336|Error creating or updating Business Process: BpfVisitor cannot be null.|
> |**Name**:<br />BulkDeleteChildFailure<br />**Hex**:<br />80048459<br />**Number**:<br />-2147187623|One of the Bulk Delete Child Jobs Failed|
> |**Name**:<br />BulkDeleteRecordDeletionFailure<br />**Hex**:<br />80048435<br />**Number**:<br />-2147187659|The record cannot be deleted.|
> |**Name**:<br />BulkDetectInvalidEmailRecipient<br />**Hex**:<br />80048422<br />**Number**:<br />-2147187678|The e-mail recipient either does not exist or the e-mail address for the e-mail recipient is not valid.|
> |**Name**:<br />BulkMailOperationFailed<br />**Hex**:<br />8004502D<br />**Number**:<br />-2147200979|The bulk e-mail job completed with {0} failures. The failures might be caused by missing e-mail addresses or because you do not have permission to send e-mail. To find records with missing e-mail addresses, use Advanced Find. If you need increased e-mail permissions, contact your system administrator.|
> |**Name**:<br />BulkMailServiceNotAccessible<br />**Hex**:<br />80048304<br />**Number**:<br />-2147187964|The Microsoft Dynamics 365 Bulk E-Mail Service is not running.|
> |**Name**:<br />BundleCannotContainBundle<br />**Hex**:<br />8004F972<br />**Number**:<br />-2147157646|You can't add a bundle to a bundle.|
> |**Name**:<br />BundleCannotContainProductFamily<br />**Hex**:<br />8004F992<br />**Number**:<br />-2147157614|You can't add a product family to a bundle.|
> |**Name**:<br />BundleCannotContainProductKit<br />**Hex**:<br />80061014<br />**Number**:<br />-2147086316|You can't add a kit to a bundle.|
> |**Name**:<br />BundleMaxPropertyLimitExceeded<br />**Hex**:<br />8008100E<br />**Number**:<br />-2146955250|This bundle can't be published because it has too many properties. A bundle in your organization can't have more than {0} properties.|
> |**Name**:<br />BusinessManagementInvalidUserId<br />**Hex**:<br />80041d1f<br />**Number**:<br />-2147214049|The user Id(s) [{0}] is invalid.|
> |**Name**:<br />BusinessManagementLoopBeingCreated<br />**Hex**:<br />80041d21<br />**Number**:<br />-2147214047|Creating this parental association would create a loop in business hierarchy.|
> |**Name**:<br />BusinessManagementLoopExists<br />**Hex**:<br />80041d20<br />**Number**:<br />-2147214048|Loop exists in the business hierarchy.|
> |**Name**:<br />BusinessManagementObjectAlreadyExists<br />**Hex**:<br />8004022a<br />**Number**:<br />-2147220950|An object with the specified name already exists.|
> |**Name**:<br />BusinessNotEnabled<br />**Hex**:<br />8004032c<br />**Number**:<br />-2147220692|The specified business unit is disabled.|
> |**Name**:<br />BusinessProcessFlowDefinitionOutdated<br />**Hex**:<br />80060375<br />**Number**:<br />-2147089547|This action cannot be completed because the Business Process Flow definition is out of sync with the Process Action. Please contact your Dynamics 365 System Administrator to update the Business Process Flow.|
> |**Name**:<br />BusinessProcessFlowMissingEntityErrorMessage<br />**Hex**:<br />80060440<br />**Number**:<br />-2147089344|Failed to import Business Process '{0}' because solution does not include corresponding Business Process entity '{1}'.|
> |**Name**:<br />BusinessProcessFlowStepHasInvalidParent<br />**Hex**:<br />80060405<br />**Number**:<br />-2147089403|{0} parent is not of type {1}|
> |**Name**:<br />BusinessRuleEditorSupportsOnlyIfConditionBranch<br />**Hex**:<br />80060008<br />**Number**:<br />-2147090424|The business rule editor only supports one if condition. Please fix the rule.|
> |**Name**:<br />BusinessUnitCannotBeDisabled<br />**Hex**:<br />80041d59<br />**Number**:<br />-2147213991|Business unit cannot be disabled: no active user with system admin role exists outside of business unit subtree.|
> |**Name**:<br />BusinessUnitDefaultTeamOwnsRecords<br />**Hex**:<br />80041d62<br />**Number**:<br />-2147213982|Business unit default team owns records. Business unit cannot be deleted.|
> |**Name**:<br />BusinessUnitHasChildAndCannotBeDeleted<br />**Hex**:<br />80041d61<br />**Number**:<br />-2147213983|Business unit has a child business unit and cannot be deleted.|
> |**Name**:<br />BusinessUnitIsNotDisabledAndCannotBeDeleted<br />**Hex**:<br />80041d60<br />**Number**:<br />-2147213984|Not disabled business unit cannot be deleted.|
> |**Name**:<br />BusinessUnitQueuesAssociatedWithBU<br />**Hex**:<br />80072526<br />**Number**:<br />-2147015386|There are {0} queues referencing this BusinessUnit with id ={1}, Name = {2}. Please delete the queues before deleting this business unit or assign to a different Business Unit.|
> |**Name**:<br />CalculatedFieldsAssignmentMismatch<br />**Hex**:<br />8006042b<br />**Number**:<br />-2147089365|You can’t set the value {0}, which is of type {1}, to type {2}.|
> |**Name**:<br />CalculatedFieldsCyclicReference<br />**Hex**:<br />80060431<br />**Number**:<br />-2147089359|Field {0} cannot be used in calculated field {1} because it would create a circular reference.|
> |**Name**:<br />CalculatedFieldsDateOnlyBehaviorTypeMismatch<br />**Hex**:<br />8006043a<br />**Number**:<br />-2147089350|You can only use a Date Only type of field.|
> |**Name**:<br />CalculatedFieldsDepthExceeded<br />**Hex**:<br />80060432<br />**Number**:<br />-2147089358|You can’t create or update the {0} field because the {1} field already has a calculated field chain of {2} deep.|
> |**Name**:<br />CalculatedFieldsDivideByZero<br />**Hex**:<br />8006042d<br />**Number**:<br />-2147089363|You cannot divide by {0}, which evaluates to zero.|
> |**Name**:<br />CalculatedFieldsEntitiesExceeded<br />**Hex**:<br />80060433<br />**Number**:<br />-2147089357|Field {0} cannot be created or updated because field {1} contains an additional formula that uses a parent record.|
> |**Name**:<br />CalculatedFieldsFeatureNotEnabled<br />**Hex**:<br />80060422<br />**Number**:<br />-2147089374|Calculated Field feature is not available|
> |**Name**:<br />CalculatedFieldsFunctionMismatch<br />**Hex**:<br />8006042c<br />**Number**:<br />-2147089364|You can't use {0}, which is of type {1}, with the current function.|
> |**Name**:<br />CalculatedFieldsInvalidAttribute<br />**Hex**:<br />80060428<br />**Number**:<br />-2147089368|The {0} field doesn't exist.|
> |**Name**:<br />CalculatedFieldsInvalidAttributes<br />**Hex**:<br />8006042e<br />**Number**:<br />-2147089362|The formula references the following attributes that don't exist: {0}.|
> |**Name**:<br />CalculatedFieldsInvalidEntity<br />**Hex**:<br />80060423<br />**Number**:<br />-2147089373|The formula contains an invalid reference: {0}.|
> |**Name**:<br />CalculatedFieldsInvalidFunction<br />**Hex**:<br />80060427<br />**Number**:<br />-2147089369|The {0} function doesn't exist.|
> |**Name**:<br />CalculatedFieldsInvalidSourceTypeMask<br />**Hex**:<br />80060438<br />**Number**:<br />-2147089352|The formula can't be saved because it contains references to the following fields that have invalid definitions: {0}.|
> |**Name**:<br />CalculatedFieldsInvalidValue<br />**Hex**:<br />8006042f<br />**Number**:<br />-2147089361|The formula references a value that doesn't exist.|
> |**Name**:<br />CalculatedFieldsInvalidValues<br />**Hex**:<br />80060430<br />**Number**:<br />-2147089360|The formula references the following values that don't exist: {0}.|
> |**Name**:<br />CalculatedFieldsInvalidXaml<br />**Hex**:<br />80060424<br />**Number**:<br />-2147089372|The {0} field has an invalid XAML formula definition.|
> |**Name**:<br />CalculatedFieldsNonCalculatedFieldAssignment<br />**Hex**:<br />80060425<br />**Number**:<br />-2147089371|Only calculated fields can have a formula definition.|
> |**Name**:<br />CalculatedFieldsPrimitiveOverflow<br />**Hex**:<br />8006042a<br />**Number**:<br />-2147089366|Cannot convert the value {0} into type {1}.|
> |**Name**:<br />CalculatedFieldsTimeInvBehaviorTypeMismatch<br />**Hex**:<br />8006043b<br />**Number**:<br />-2147089349|You can only use a Time-Zone Independent Date Time type of field.|
> |**Name**:<br />CalculatedFieldsTypeMismatch<br />**Hex**:<br />80060426<br />**Number**:<br />-2147089370|You can't use {0}, which is of type {1}, with the current operator.|
> |**Name**:<br />CalculatedFieldsUserLocBehaviorTypeMismatch<br />**Hex**:<br />8006043c<br />**Number**:<br />-2147089348|You can only use a User Local Date Time type of field.|
> |**Name**:<br />CalculatedFieldUsedInRollupFieldCannotBeComplex<br />**Hex**:<br />80060550<br />**Number**:<br />-2147089072|One or more rollup fields depend on this calculated field. This calculated field can't use a rollup field, another calculated field that is using a rollup field or a field from related entity.|
> |**Name**:<br />CalculateNowOverflowError<br />**Hex**:<br />80060558<br />**Number**:<br />-2147089064|The calculation failed due to an overflow error.|
> |**Name**:<br />CallerCannotChangeOwnDomainName<br />**Hex**:<br />80044161<br />**Number**:<br />-2147204767|The caller cannot change their own domain name|
> |**Name**:<br />CalloutException<br />**Hex**:<br />8004025b<br />**Number**:<br />-2147220901|Callout Exception occurred.|
> |**Name**:<br />CampaignActivityAlreadyPropagated<br />**Hex**:<br />80040326<br />**Number**:<br />-2147220698|This campaign activity has been distributed already. Campaign activities cannot be distributed more than one time.|
> |**Name**:<br />CampaignActivityClosed<br />**Hex**:<br />80040331<br />**Number**:<br />-2147220687|This Campaign Activity is closed or canceled. Campaign activities cannot be distributed after they have been closed or canceled.|
> |**Name**:<br />CampaignNotSpecifiedForCampaignActivity<br />**Hex**:<br />80040309<br />**Number**:<br />-2147220727|RegardingObjectId is a required field.|
> |**Name**:<br />CampaignNotSpecifiedForCampaignResponse<br />**Hex**:<br />8004030a<br />**Number**:<br />-2147220726|RegardingObjectId is a required field.|
> |**Name**:<br />CanAssociateOnlyMobileOfflineEnabledEntityToProfileItem<br />**Hex**:<br />8006099E<br />**Number**:<br />-2147087970|{0} needs to be enabled for mobile offline.|
> |**Name**:<br />CanAssociateOnlyMobileOfflineEnableEntityToProfileItem<br />**Hex**:<br />8006099C<br />**Number**:<br />-2147087972|This entity needs to be enabled for mobile offline.|
> |**Name**:<br />CanAssociateOnlyOneEntityPerProfileItem<br />**Hex**:<br />8006099D<br />**Number**:<br />-2147087971|You can only add one mobile offline profile item record per entity to a mobile offline profile record. |
> |**Name**:<br />CancelActiveChildCaseFirst<br />**Hex**:<br />8003F451<br />**Number**:<br />-2147224495|Cancel active child case before canceling parent case.|
> |**Name**:<br />CannotAcceptEmail<br />**Hex**:<br />8005E20B<br />**Number**:<br />-2147098101|The email that you are trying to deliver cannot be accepted by Microsoft Dynamics 365. Reason Code: {0}.|
> |**Name**:<br />CannotAccessExchangeOptinStatus<br />**Hex**:<br />80071110<br />**Number**:<br />-2147020528|Exchange optin status is not accessible.|
> |**Name**:<br />CannotActivateMailboxForDisabledUserOrQueue<br />**Hex**:<br />8005E230<br />**Number**:<br />-2147098064|Mailbox cannot be activated because the user or queue associated with the mailbox is in disabled state. Mailbox can only be activated for Active User/Queue.|
> |**Name**:<br />CannotActivateRecord<br />**Hex**:<br />80081017<br />**Number**:<br />-2146955241|You can't activate a retired product family or bundle. Also, you can't activate a retired product that is part of a product family.|
> |**Name**:<br />CannotActOnBehalfOfAnotherUser<br />**Hex**:<br />8004A110<br />**Number**:<br />-2147180272|User does not have the privilege to act on behalf another user.|
> |**Name**:<br />CannotActOnBehalfOfExternalParty<br />**Hex**:<br />80061116<br />**Number**:<br />-2147086058|User does not have the privilege to act on behalf of External Party.|
> |**Name**:<br />CannotAddActivityPartyEntityToMobileOfflineProfileItem<br />**Hex**:<br />800609AD<br />**Number**:<br />-2147087955|You can’t add the ActivityParty entity to the mobile offline profile item because it’s added automatically when an activity entity is added to the profile.|
> |**Name**:<br />CannotAddBundleToItself<br />**Hex**:<br />80061031<br />**Number**:<br />-2147086287|You can't add a bundle to itself.|
> |**Name**:<br />CannotAddBundleToPricelist<br />**Hex**:<br />80061007<br />**Number**:<br />-2147086329|You can't add the {0} bundle to the pricelist because the {1} bundle product isn't in the pricelist.|
> |**Name**:<br />CannotAddBusinessDataLocalizedLabelEntityToMobileOfflineProfileItem<br />**Hex**:<br />800609AC<br />**Number**:<br />-2147087956|You can’t add the BusinessDataLocalizedLabel entity to the mobile offline profile item because it’s added automatically when the Product entity is added to the profile.|
> |**Name**:<br />CannotAddDraftFamilyProductBundleToCases<br />**Hex**:<br />8004F984<br />**Number**:<br />-2147157628|You can't add a product family, a draft product, or a draft bundle.|
> |**Name**:<br />CannotAddIntersectEntityToMobileOfflineProfileItem<br />**Hex**:<br />800609AB<br />**Number**:<br />-2147087957|You can’t add the intersect entity to the mobile offline profile item because it’s added automatically when its parent entities are added to the profile.|
> |**Name**:<br />CannotAddKitToItself<br />**Hex**:<br />80061032<br />**Number**:<br />-2147086286|You can't add a kit to itself.|
> |**Name**:<br />CannotAddMembersToDefaultTeam<br />**Hex**:<br />8004830B<br />**Number**:<br />-2147187957|Can't add members to the default business unit team.|
> |**Name**:<br />CannotAddNewBooleanValue<br />**Hex**:<br />8004431D<br />**Number**:<br />-2147204323|You cannot add an option to a Boolean attribute.|
> |**Name**:<br />CannotAddNewStateValue<br />**Hex**:<br />8004431E<br />**Number**:<br />-2147204322|You cannot add state options to a State attribute.|
> |**Name**:<br />CannotAddNonCustomizableComponent<br />**Hex**:<br />8004F015<br />**Number**:<br />-2147160043|The component {0} {1} cannot be added to the solution because it is not customizable|
> |**Name**:<br />CannotAddOrActonBehalfAnotherUserPrivilege<br />**Hex**:<br />8004Ed43<br />**Number**:<br />-2147160765|Act on Behalf of Another User privilege cannot be added or removed.|
> |**Name**:<br />CannotAddParentToAKit<br />**Hex**:<br />80061015<br />**Number**:<br />-2147086315|You can't specify a parent record for a kit.|
> |**Name**:<br />CannotAddPricelistToProductFamily<br />**Hex**:<br />8004F902<br />**Number**:<br />-2147157758|You can't add a product family to a pricelist.|
> |**Name**:<br />CannotAddProduct<br />**Hex**:<br />8004F908<br />**Number**:<br />-2147157752|You can only add Active products.|
> |**Name**:<br />CannotAddProductBundleToKit<br />**Hex**:<br />80061022<br />**Number**:<br />-2147086302|You can't add a bundle to a kit.|
> |**Name**:<br />CannotAddProductFamilyToKit<br />**Hex**:<br />80061023<br />**Number**:<br />-2147086301|You can't add a product family to a kit.|
> |**Name**:<br />CannotAddProductToBundle<br />**Hex**:<br />8004F976<br />**Number**:<br />-2147157642|You cannot add products to this bundle.The limit of {0} has been reached for this bundle.|
> |**Name**:<br />CannotAddProductToKit<br />**Hex**:<br />80061024<br />**Number**:<br />-2147086300|You can't add a product that belongs to a product family to a kit.|
> |**Name**:<br />CannotAddProductToRetiredKit<br />**Hex**:<br />80061026<br />**Number**:<br />-2147086298|You can't add a product to a retired kit.|
> |**Name**:<br />CannotAddQueueItemsToInactiveQueue<br />**Hex**:<br />80040522<br />**Number**:<br />-2147220190|The selected user does not have sufficient permissions to work on items in this queue.|
> |**Name**:<br />CannotAddRetiredProduct<br />**Hex**:<br />80061033<br />**Number**:<br />-2147086285|You can’t create a product relationship with a retired product.|
> |**Name**:<br />CannotAddRetiredProductToKit<br />**Hex**:<br />80061027<br />**Number**:<br />-2147086297|You can't add a retired product to a kit.|
> |**Name**:<br />CannotAddRetiredProductToPricelist<br />**Hex**:<br />80061009<br />**Number**:<br />-2147086327|Retired products can not be added to pricelists.|
> |**Name**:<br />CannotAddSingleQueueEnabledEntityToQueue<br />**Hex**:<br />8004051c<br />**Number**:<br />-2147220196|The entity record cannot be added to the queue as it already exists in other queue.|
> |**Name**:<br />CannotAddSolutionComponentWithoutRoots <br />**Hex**:<br />8004F018<br />**Number**:<br />-2147160040|This item is not a valid solution component. For more information about solution components, see the Microsoft Dynamics 365 SDK documentation.|
> |**Name**:<br />CannotAddUserToMobileOfflineProfile<br />**Hex**:<br />800609A6<br />**Number**:<br />-2147087962|You can’t add this user to this mobile offline profile because the user’s role is either missing or doesn’t have the Dynamics 365 for mobile privilege.|
> |**Name**:<br />CannotAddWorkflowActivationToSolution <br />**Hex**:<br />8004F00C<br />**Number**:<br />-2147160052|Cannot add Workflow Activation to solution |
> |**Name**:<br />CannotAssignAddressBookFilters<br />**Hex**:<br />80048448<br />**Number**:<br />-2147187640|Cannot assign address book filters|
> |**Name**:<br />CannotAssignOfflineFilters<br />**Hex**:<br />800404ff<br />**Number**:<br />-2147220225|Cannot assign offline filters|
> |**Name**:<br />CannotAssignOutlookFilters<br />**Hex**:<br />80040264<br />**Number**:<br />-2147220892|Cannot assign outlook filters|
> |**Name**:<br />CannotAssignRolesOrProfilesToAccessTeam<br />**Hex**:<br />80048331<br />**Number**:<br />-2147187919|Cannot assign roles or profiles to an access team.|
> |**Name**:<br />CannotAssignRolesToSupportUser<br />**Hex**:<br />80041d51<br />**Number**:<br />-2147213999|The support user are read-only, which cannot be assigned with other roles|
> |**Name**:<br />CannotAssignSupportUser<br />**Hex**:<br />80041d44<br />**Number**:<br />-2147214012|The Support User Role cannot be assigned to a user.|
> |**Name**:<br />CannotAssignToAccessTeam<br />**Hex**:<br />80048340<br />**Number**:<br />-2147187904|You cannot assign a record to the access team. You can assign a record to the owner team.|
> |**Name**:<br />CannotAssignToDisabledBusiness<br />**Hex**:<br />8004032d<br />**Number**:<br />-2147220691|The specified business unit cannot be assigned to because it is disabled.|
> |**Name**:<br />CannotAssociateExternalPartyItem<br />**Hex**:<br />80061117<br />**Number**:<br />-2147086057|You can’t associate more than one external party item with an entity record that has been enabled as an external party.|
> |**Name**:<br />CannotAssociateInactiveItemToCampaign<br />**Hex**:<br />80040304<br />**Number**:<br />-2147220732|Cannot associate an inactive item to a Campaign.|
> |**Name**:<br />CannotAssociateInvalidEntityToProfileItem<br />**Hex**:<br />8006099B<br />**Number**:<br />-2147087973|Invalid object type code.|
> |**Name**:<br />CannotAssociateProductFamily<br />**Hex**:<br />8004F999<br />**Number**:<br />-2147157607|You can't create a relationship with a product family.|
> |**Name**:<br />CannotAssociateRetiredBundles<br />**Hex**:<br />80081011<br />**Number**:<br />-2146955247|You can't create a product relationship with a retired bundle.|
> |**Name**:<br />CannotAssociateRetiredProducts<br />**Hex**:<br />8004F974<br />**Number**:<br />-2147157644|You can't create a product relationship with a retired product.|
> |**Name**:<br />CannotBindToSession<br />**Hex**:<br />80040254<br />**Number**:<br />-2147220908|Cannot bind to another session, session already bound.|
> |**Name**:<br />CannotCancelInvoice<br />**Hex**:<br />80100001<br />**Number**:<br />-2146435071|The invoice cannot be cancelled because it is not in active or paid state.|
> |**Name**:<br />CannotChangeAccessModeForInternetMarketingUser<br />**Hex**:<br />80045035<br />**Number**:<br />-2147200971|Internet Marketing User is a system user. You cannot change its access mode.|
> |**Name**:<br />CannotChangeAttributeRequiredLevel<br />**Hex**:<br />8004D293<br />**Number**:<br />-2147167597|An attribute's required level cannot be changed from SystemRequired|
> |**Name**:<br />CannotChangeConvertRuleState<br />**Hex**:<br />800608F4<br />**Number**:<br />-2147088140|Error occured during activating Convert Rule.Please check your privileges on Workflow and kindly try again or Contact your system administrator.|
> |**Name**:<br />CannotChangeDaysSinceRecordLastModified<br />**Hex**:<br />800609A4<br />**Number**:<br />-2147087964|You need to enable this entity for mobile offline before you can set or change the number of days since the record was last modified.|
> |**Name**:<br />CannotChangeInvitationStatusForInternetMarketingUser<br />**Hex**:<br />80045036<br />**Number**:<br />-2147200970|Internet Marketing User is a system user. You cannot change its invitation status.|
> |**Name**:<br />CannotChangeProductRelationship<br />**Hex**:<br />80061013<br />**Number**:<br />-2147086317|You can't add or modify the product relationship of a retired product.|
> |**Name**:<br />CannotChangeSelectedBundleToAnotherValue<br />**Hex**:<br />8004F986<br />**Number**:<br />-2147157626|If a bundle is selected as an existing product, you can't change it to another value.|
> |**Name**:<br />CannotChangeSelectedProductWithBundle<br />**Hex**:<br />8004F987<br />**Number**:<br />-2147157625|If a product is selected as an existing product, you can't change it to a bundle.|
> |**Name**:<br />CannotChangeState<br />**Hex**:<br />8004F863<br />**Number**:<br />-2147157917|Error occured during activating SLA..Please check your privileges on Workflow and kindly try again or Contact your system administrator.|
> |**Name**:<br />CannotChangeStateOfNonpublicView<br />**Hex**:<br />80040279<br />**Number**:<br />-2147220871|Only public views can be deactivated and activated.|
> |**Name**:<br />CannotChangeTeamTypeDueToOwnership<br />**Hex**:<br />80048337<br />**Number**:<br />-2147187913|You cannot modify the type of the team because there are records owned by the team.|
> |**Name**:<br />CannotChangeTeamTypeDueToRoleOrProfile<br />**Hex**:<br />80048336<br />**Number**:<br />-2147187914|You cannot modify the type of the team because there are security roles or field security profiles assigned to the team.|
> |**Name**:<br />CannotClearChannelPropertyGroupFromConvertRule<br />**Hex**:<br />800608ED<br />**Number**:<br />-2147088147|The Channel Property Group is used by one or more steps. Delete the properties from the conditions and steps that use the record before you save or activate the rule.|
> |**Name**:<br />CannotCloneBundleAsProductLimitExceeded<br />**Hex**:<br />8004F985<br />**Number**:<br />-2147157627|You can't create this new bundle because it contains more than the allowed number of {0} products that a bundle can contain.|
> |**Name**:<br />CannotCloneBundleWithRetiredProducts<br />**Hex**:<br />80061034<br />**Number**:<br />-2147086284|You can't clone a bundle that contains retired products.|
> |**Name**:<br />CannotCloneProductKit<br />**Hex**:<br />80061020<br />**Number**:<br />-2147086304|You can't clone a kit.|
> |**Name**:<br />CannotCloseCase<br />**Hex**:<br />8004F456<br />**Number**:<br />-2147158954|This operation can't be completed. One or more child cases can't be closed because of the status transition rules that are defined for cases.|
> |**Name**:<br />CannotConnectToSelf<br />**Hex**:<br />80048217<br />**Number**:<br />-2147188201|Cannot connect a record to itself.|
> |**Name**:<br />CannotConvertBundleToKit<br />**Hex**:<br />80061030<br />**Number**:<br />-2147086288|You can't convert a bundle to a kit.|
> |**Name**:<br />CannotConvertProductAssociatedWithBundleToKit<br />**Hex**:<br />80061018<br />**Number**:<br />-2147086312|You can't convert a product that is a part of a bundle to a kit.|
> |**Name**:<br />CannotConvertProductAssociatedWithFamilyToKit<br />**Hex**:<br />80061016<br />**Number**:<br />-2147086314|You can't convert a product that belongs to a product family to a kit.|
> |**Name**:<br />CannotConvertProductFamilyToKit<br />**Hex**:<br />80061029<br />**Number**:<br />-2147086295|You can't convert a product family to a kit.|
> |**Name**:<br />CannotCopyIncompatibleListType<br />**Hex**:<br />80040306<br />**Number**:<br />-2147220730|Cannot copy lists of different types.|
> |**Name**:<br />CannotCopyStaticList<br />**Hex**:<br />8004F704<br />**Number**:<br />-2147158268|This action is valid only for dynamic list.|
> |**Name**:<br />CannotCreateActivityRelationship<br />**Hex**:<br />80047006<br />**Number**:<br />-2147192826|Relationship with activities cannot be created through this operation|
> |**Name**:<br />CannotCreateAddressBookFilters<br />**Hex**:<br />80048447<br />**Number**:<br />-2147187641|Cannot create address book filters|
> |**Name**:<br />CannotCreateCase<br />**Hex**:<br />80060853<br />**Number**:<br />-2147088301|You can't create this case as the default entitlement for the specified customer has no remaining terms.|
> |**Name**:<br />CannotCreateComponentDefinition<br />**Hex**:<br />80072001<br />**Number**:<br />-2147016703|Creation of a new component definition is not supported|
> |**Name**:<br />CannotCreateExternalPartyWithSameCorrelationKey<br />**Hex**:<br />80061112<br />**Number**:<br />-2147086062|An external party record already exists with the same correlation key value.|
> |**Name**:<br />CannotCreateFromSupportUser<br />**Hex**:<br />80041d46<br />**Number**:<br />-2147214010|Cannot create a role from Support User Role.|
> |**Name**:<br />CannotCreateKitOfTypeFamilyOrBundle<br />**Hex**:<br />80061012<br />**Number**:<br />-2147086318|You can't create a kit of type bundle or product family.|
> |**Name**:<br />CannotCreateOrEnablePositionDueToParentPositionIsDisabled<br />**Hex**:<br />80048344<br />**Number**:<br />-2147187900|A child position cannot be created/enabled under a disabled parent position.|
> |**Name**:<br />CannotCreateOutlookFilters<br />**Hex**:<br />80040263<br />**Number**:<br />-2147220893|Cannot create outlook filters|
> |**Name**:<br />CannotCreatePluginInstance<br />**Hex**:<br />8004A201<br />**Number**:<br />-2147180031|Can not create instance of a plug-in. Verify that plug-in type is not defined as abstract and it has a public constructor supported by Dynamics 365 SDK.|
> |**Name**:<br />CannotCreatePropertyOptionSetItem<br />**Hex**:<br />80081013<br />**Number**:<br />-2146955245|You can only create a property option set item record that refers to a property that has its data type set to Option Set.|
> |**Name**:<br />CannotCreateQueueItemInactiveObject<br />**Hex**:<br />8004051e<br />**Number**:<br />-2147220194|Deactivated object cannot be added to queue.|
> |**Name**:<br />CannotCreateResponseForTemplate<br />**Hex**:<br />80040312<br />**Number**:<br />-2147220718|CampaignResponse can not be created for Template Campaign.|
> |**Name**:<br />CannotCreateSLAForEntity<br />**Hex**:<br />80055005<br />**Number**:<br />-2147135483|You can't create a service level agreement (SLA) for this entity because it’s not enabled for creating SLAs|
> |**Name**:<br />CannotCreateSyncUserIsLicensedField<br />**Hex**:<br />80041d4d<br />**Number**:<br />-2147214003|The property IsLicensed cannot be set for Sync User Creation.|
> |**Name**:<br />CannotCreateSyncUserObjectMissing<br />**Hex**:<br />80041d4b<br />**Number**:<br />-2147214005|This is not a valid Microsoft Online Services ID for this organization.|
> |**Name**:<br />CannotCreateSystemOrDefaultTheme<br />**Hex**:<br />800608D5<br />**Number**:<br />-2147088171|You can’t create system or default themes. System or default theme can only be created out of box.|
> |**Name**:<br />CannotCreateUpdateSourceAttribute<br />**Hex**:<br />80044804<br />**Number**:<br />-2147203068|Source Attribute Not Valid For Create/Update if Metric Type is Count.|
> |**Name**:<br />CannotDeactivateDefaultView<br />**Hex**:<br />8004027a<br />**Number**:<br />-2147220870|Default views cannot be deactivated.|
> |**Name**:<br />CannotDeactivateGuestProfile<br />**Hex**:<br />80061105<br />**Number**:<br />-2147086075|You can't set this guest channel access profile as inactive.|
> |**Name**:<br />CannotDefineMultipleValuesOnOwnerFieldInProfileItemEntityFilter<br />**Hex**:<br />80071129<br />**Number**:<br />-2147020503|You cannot define multiple values on this field.|
> |**Name**:<br />CannotDeleteActiveCaseCreationRule<br />**Hex**:<br />8004F880<br />**Number**:<br />-2147157888|You can't delete an active rule. Deactivate the Record Creation and Update Rule, and then try deleting it.|
> |**Name**:<br />CannotDeleteActiveRecordCreationRuleItem<br />**Hex**:<br />8004F894<br />**Number**:<br />-2147157868|You can’t delete an active record creation rule item. Deactivate the record creation rule, and then try deleting it.|
> |**Name**:<br />CannotDeleteActiveRule<br />**Hex**:<br />8004F850<br />**Number**:<br />-2147157936|You can not delete an active routing rule. Deactivate the rule to delete it.|
> |**Name**:<br />CannotDeleteActiveSla<br />**Hex**:<br />8004F870<br />**Number**:<br />-2147157904|You can't delete an active SLA. Deactivate the SLA, and then try deleting it.|
> |**Name**:<br />CannotDeleteAppModuleAdministration<br />**Hex**:<br />80050130<br />**Number**:<br />-2147155664|This app can’t be deleted.|
> |**Name**:<br />CannotDeleteAppModuleClientType<br />**Hex**:<br />80050129<br />**Number**:<br />-2147155671|This app can’t be deleted.|
> |**Name**:<br />CannotDeleteAsBackgroundOperationInProgress<br />**Hex**:<br />8004032b<br />**Number**:<br />-2147220693|This record is currently being used by Microsoft Dynamics 365 and cannot be deleted. Try again later. If  the problem persists, contact your system administrator.|
> |**Name**:<br />CannotDeleteAsItIsReadOnly<br />**Hex**:<br />80040228<br />**Number**:<br />-2147220952|The object cannot be deleted because it is read-only.|
> |**Name**:<br />CannotDeleteAttributeUsedInWorkflow<br />**Hex**:<br />80045030<br />**Number**:<br />-2147200976|This attribute cannot be deleted because it is used in one or more workflows. Cancel any system jobs for workflows that use this attribute, then delete or modify any workflows that use the attribute, and then try to delete the attribute again.|
> |**Name**:<br />CannotDeleteBaseMoneyCalculationAttribute<br />**Hex**:<br />80048cfe<br />**Number**:<br />-2147185410|The base money calculation Attribute is not valid for deletion|
> |**Name**:<br />CannotDeleteCannedView<br />**Hex**:<br />8004022f<br />**Number**:<br />-2147220945|System-defined views cannot be deleted.|
> |**Name**:<br />CannotDeleteCDSUser<br />**Hex**:<br />80041d5a<br />**Number**:<br />-2147213990|The Common Data Service User Role cannot be deleted.|
> |**Name**:<br />CannotDeleteChannelAccessProfileRule<br />**Hex**:<br />80061108<br />**Number**:<br />-2147086072|You can't delete an active channel access profile rule. Deactivate the rule and then delete it.|
> |**Name**:<br />CannotDeleteChannelProperty<br />**Hex**:<br />800608EB<br />**Number**:<br />-2147088149|You can’t delete a channel property which is being referred in a convert rule.|
> |**Name**:<br />CannotDeleteChildAttribute<br />**Hex**:<br />80047016<br />**Number**:<br />-2147192810|The Child Attribute is not valid for deletion|
> |**Name**:<br />CannotDeleteCustomEntityUsedInWorkflow<br />**Hex**:<br />8004502C<br />**Number**:<br />-2147200980|Cannot delete entity because it is used in a workflow.|
> |**Name**:<br />CannotDeleteDefaultProfile<br />**Hex**:<br />8006099A<br />**Number**:<br />-2147087974|To delete this profile, you first need to set it so that it’s no longer a default mobile offline profile.|
> |**Name**:<br />CannotDeleteDefaultStatusOption<br />**Hex**:<br />80044341<br />**Number**:<br />-2147204287|Default Status options cannot be deleted.|
> |**Name**:<br />CannotDeleteDefaultTeam<br />**Hex**:<br />80048307<br />**Number**:<br />-2147187961|The default business unit team can't be deleted.|
> |**Name**:<br />CannotDeleteDueToAssociation<br />**Hex**:<br />80040227<br />**Number**:<br />-2147220953|The object you tried to delete is associated with another object and cannot be deleted.|
> |**Name**:<br />CannotDeleteDueToBasketEntityAssociation<br />**Hex**:<br />80061612<br />**Number**:<br />-2147084782|You can't delete a Recommendation entity if it has a corresponding Basket entity.|
> |**Name**:<br />CannotDeleteDynamicPropertyInRetiredState<br />**Hex**:<br />8004F892<br />**Number**:<br />-2147157870|You can't delete a property of a retired product.|
> |**Name**:<br />CannotDeleteDynamicPropertyInUse<br />**Hex**:<br />80081003<br />**Number**:<br />-2146955261|Retired Properties being used in transactions can not be deleted.|
> |**Name**:<br />CannotDeleteEnumOptionsFromAttributeType<br />**Hex**:<br />80044323<br />**Number**:<br />-2147204317|You can delete options only from picklist and status attributes.|
> |**Name**:<br />CannotDeleteGuestProfile<br />**Hex**:<br />80061104<br />**Number**:<br />-2147086076|You can't delete this guest channel access profile.|
> |**Name**:<br />CannotDeleteInheritedDynamicProperty<br />**Hex**:<br />80081014<br />**Number**:<br />-2146955244|You can't delete a property that is inherited from a product family.|
> |**Name**:<br />CannotDeleteInUseAttribute<br />**Hex**:<br />80048418<br />**Number**:<br />-2147187688|The selected attribute cannot be deleted because it is referenced by one or more duplicate detection rules that are being published.|
> |**Name**:<br />CannotDeleteInUseComponent<br />**Hex**:<br />8004F01F<br />**Number**:<br />-2147160033|The {0}({1}) component cannot be deleted because it is referenced by {2} other components. For a list of referenced components, use the RetrieveDependenciesForDeleteRequest.|
> |**Name**:<br />CannotDeleteInUseEntity<br />**Hex**:<br />80048420<br />**Number**:<br />-2147187680|The selected entity cannot be deleted because it is referenced by one or more duplicate detection rules that are in process of being published.|
> |**Name**:<br />CannotDeleteInUseOptionSet<br />**Hex**:<br />80048417<br />**Number**:<br />-2147187689|This option set cannot be deleted. The current set of entities that reference this option set are: {0}. These references must be removed before this option set can be deleted|
> |**Name**:<br />CannotDeleteLastEmailAttribute<br />**Hex**:<br />80046FFF<br />**Number**:<br />-2147192833|You cannot delete this field because the record type has been enabled for e-mail.|
> |**Name**:<br />CannotDeleteMetadata<br />**Hex**:<br />8004F032<br />**Number**:<br />-2147160014|The '{2}' operation on the current component(name='{0}', id='{1}') failed during managed property evaluation of condition: '{3}'|
> |**Name**:<br />CannotDeleteMetricWithGoals<br />**Hex**:<br />80044800<br />**Number**:<br />-2147203072|This goal metric is being used by one or more goals and cannot be deleted.|
> |**Name**:<br />CannotDeleteNonLeafNode<br />**Hex**:<br />8004F200<br />**Number**:<br />-2147159552|Only a leaf statement can be deleted. This statement is parenting some other statement.|
> |**Name**:<br />CannotDeleteNotOwnedDynamicProperty<br />**Hex**:<br />80081006<br />**Number**:<br />-2146955258|You cannot delete a dynamic property that is inherited from a product family.|
> |**Name**:<br />CannotDeleteOneNoteTableOfContent<br />**Hex**:<br />800608B7<br />**Number**:<br />-2147088201|You can’t delete this file because it contains links to OneNote notebook sections. To delete notebook contents, open the notebook in OneNote and delete the contents from there. To delete a notebook, open SharePoint and delete the notebook from there.|
> |**Name**:<br />CannotDeleteOnlineRecord<br />**Hex**:<br />8005F248<br />**Number**:<br />-2147093944|You can’t delete this record because it doesn’t exist in the offline mode.|
> |**Name**:<br />CannotDeleteOptionSet<br />**Hex**:<br />80048404<br />**Number**:<br />-2147187708|The selected OptionSet cannot be deleted|
> |**Name**:<br />CannotDeleteOrCancelSystemJobs<br />**Hex**:<br />80044F02<br />**Number**:<br />-2147201278|You can't cancel or delete this system job because it's required by the system. You can only pause, resume, or postpone this job.|
> |**Name**:<br />CannotDeleteOverriddenProperty<br />**Hex**:<br />80081100<br />**Number**:<br />-2146955008|You can't delete this property because it's overridden for one more or child records. Remove the overridden versions of the property, republish the product family hierarchy, and then try deleting the property.|
> |**Name**:<br />CannotDeletePartnerSolutionWithOrganizations<br />**Hex**:<br />8004A10e<br />**Number**:<br />-2147180274|Can not delete partner solution as one or more organizations are associated with it|
> |**Name**:<br />CannotDeletePartnerWithPartnerSolutions<br />**Hex**:<br />8004A10d<br />**Number**:<br />-2147180275|Can not delete partner as one or more solutions are associated with it|
> |**Name**:<br />CannotDeletePrimaryUIAttribute<br />**Hex**:<br />80047002<br />**Number**:<br />-2147192830|The Primary UI Attribute is not valid for deletion|
> |**Name**:<br />CannotDeleteProductFromActiveBundle<br />**Hex**:<br />80061010<br />**Number**:<br />-2147086320|You can't remove products from a bundle that's either active or under revision.|
> |**Name**:<br />CannotDeleteProductStatusCode<br />**Hex**:<br />80081016<br />**Number**:<br />-2146955242|You can't delete a system-generated status reason.|
> |**Name**:<br />CannotDeleteProfileWithExternalPartyItem<br />**Hex**:<br />80061107<br />**Number**:<br />-2147086073|You can't delete this channel access profile because it's associated to an external party item. Remove the association, and then try again.|
> |**Name**:<br />CannotDeleteProfileWithProfileRules<br />**Hex**:<br />80061106<br />**Number**:<br />-2147086074|You can't delete this channel access profile because it's being used by one or more channel access profile rules. Remove this profile from the channel access profile rules, and then try again.|
> |**Name**:<br />CannotDeletePropertyOverriddenByBundleItem<br />**Hex**:<br />80081015<br />**Number**:<br />-2146955243|You can't delete this property because it's overridden in one or more related bundle products. Remove the overridden versions of the property from the related bundle products, publish the bundles that were changed, and then try again.|
> |**Name**:<br />CannotDeleteQueueWithQueueItems<br />**Hex**:<br />80631117<br />**Number**:<br />-2140991209|You can't delete this queue because it has items assigned to it. Assign these items to another user, team, or queue and try again.|
> |**Name**:<br />CannotDeleteQueueWithRouteRules<br />**Hex**:<br />80731118<br />**Number**:<br />-2139942632|You can't delete this queue because one or more routing rule sets use this queue. Remove the queue from the routing rule sets and try again.|
> |**Name**:<br />CannotDeleteRelatedSla<br />**Hex**:<br />8004F859<br />**Number**:<br />-2147157927|The SLA record couldn't be deleted. Please try again or contact your system administrator|
> |**Name**:<br />CannotDeleteRestrictedPublisher<br />**Hex**:<br />8004F006<br />**Number**:<br />-2147160058|Attempting to delete a restricted publisher.|
> |**Name**:<br />CannotDeleteRestrictedSolution<br />**Hex**:<br />8004F005<br />**Number**:<br />-2147160059|Attempting to delete a restricted solution.|
> |**Name**:<br />CannotDeleteSupportUser<br />**Hex**:<br />80041d42<br />**Number**:<br />-2147214014|The Support User Role cannot be deleted.|
> |**Name**:<br />CannotDeleteSysAdmin<br />**Hex**:<br />80041d2e<br />**Number**:<br />-2147214034|The System Administrator Role cannot be deleted.|
> |**Name**:<br />CannotDeleteSystemCustomizer<br />**Hex**:<br />80041d4a<br />**Number**:<br />-2147214006|The System Customizer Role cannot be deleted.|
> |**Name**:<br />CannotDeleteSystemEmailTemplate<br />**Hex**:<br />80048432<br />**Number**:<br />-2147187662|System e-mail templates cannot be deleted.|
> |**Name**:<br />CannotDeleteSystemForm<br />**Hex**:<br />8004F652<br />**Number**:<br />-2147158446|System forms cannot be deleted.|
> |**Name**:<br />CannotDeleteSystemTheme<br />**Hex**:<br />800608DA<br />**Number**:<br />-2147088166|You can't delete system themes.|
> |**Name**:<br />CannotDeleteTeamOwningRecords<br />**Hex**:<br />8004830E<br />**Number**:<br />-2147187954|Can't delete a team which owns records. Reassign the records and try again.|
> |**Name**:<br />CannotDeleteUpdateInUseRule<br />**Hex**:<br />80048428<br />**Number**:<br />-2147187672|The duplicate detection rule is currently in use and cannot be updated or deleted. Please try again later.|
> |**Name**:<br />CannotDeleteUserMailbox<br />**Hex**:<br />8005E200<br />**Number**:<br />-2147098112|The mailbox associated to a user or a queue cannot be deleted.|
> |**Name**:<br />CannotDeleteUserProfile<br />**Hex**:<br />800609A3<br />**Number**:<br />-2147087965|You can’t delete an active mobile offline profile. Remove all users from the profile and try again.|
> |**Name**:<br />CannotDeserializeRequest<br />**Hex**:<br />8004416f<br />**Number**:<br />-2147204753|The SDK request could not be deserialized.|
> |**Name**:<br />CannotDeserializeWorkflowInstance<br />**Hex**:<br />8004501F<br />**Number**:<br />-2147200993|Workflow instance cannot be deserialized. A possible reason for this failure is a workflow referencing a custom activity that has been unregistered.|
> |**Name**:<br />CannotDeserializeXamlWorkflow<br />**Hex**:<br />80045020<br />**Number**:<br />-2147200992|Xaml representing workflow cannot be deserialized into a DynamicActivity.|
> |**Name**:<br />CannotDisableAutoCreateAccessTeams<br />**Hex**:<br />80048338<br />**Number**:<br />-2147187912|You cannot disable the auto create access team setting while there are associated team templates.|
> |**Name**:<br />CannotDisableDuplicateDetection<br />**Hex**:<br />80048462<br />**Number**:<br />-2147187614|Duplicate detection cannot be disabled because a duplicate detection job is currently in progress. Try again later.|
> |**Name**:<br />CannotDisableInternetMarketingUser<br />**Hex**:<br />80045033<br />**Number**:<br />-2147200973|You cannot disable the Internet Marketing Partner user. This user does not consume a user license and is not charged to your organization.|
> |**Name**:<br />CannotDisableMobileOfflineFlagForEntity<br />**Hex**:<br />800609A5<br />**Number**:<br />-2147087963|You cannot disable Mobile Offline flag for this entity as it is being used in Mobile Offline Profiles|
> |**Name**:<br />CannotDisableMobileOfflineFlagForImportEntity<br />**Hex**:<br />80071111<br />**Number**:<br />-2147020527|You can’t disable mobile offline for the {0} entity using solution import. If you don’t want to use this entity in offline mode, uncheck the ‘Enable for Mobile Offline’ flag from the customization screen|
> |**Name**:<br />CannotDisableOrDeletePositionDueToAssociatedUsers<br />**Hex**:<br />80048343<br />**Number**:<br />-2147187901|This position can’t be deleted until all associated users are removed from this position.|
> |**Name**:<br />CannotDisableRelevanceSearchManagedProperty<br />**Hex**:<br />80060303<br />**Number**:<br />-2147089661|The {0} entity is currently syncing to an external search index.  You must remove the entity from the external search index before you can set the "Can Enable Sync to External Search Index" property to False.|
> |**Name**:<br />CannotDisableSysAdmin<br />**Hex**:<br />80041d2f<br />**Number**:<br />-2147214033|A user cannot be disabled if they are the only user that has the System Administrator Role.|
> |**Name**:<br />CannotDisableTenantAdmin<br />**Hex**:<br />80041d65<br />**Number**:<br />-2147213979|Users who are granted the Microsoft Office 365 Global administrator or Service administrator role cannot be disabled in Microsoft Dynamics 365 Online. You must first remove the Microsoft Office 365 role, and then try again.|
> |**Name**:<br />CannotEditActiveRule<br />**Hex**:<br />8004F851<br />**Number**:<br />-2147157935|You can not edit an active routing rule. Deactivate the rule to delete it.|
> |**Name**:<br />CannotEditActiveSla<br />**Hex**:<br />8004F860<br />**Number**:<br />-2147157920|You can't delete active SLA .Please deactivate the SLA to delete or Contact your system administrator.|
> |**Name**:<br />CannotEnableDuplicateDetection<br />**Hex**:<br />80048421<br />**Number**:<br />-2147187679|Duplicate detection cannot be enabled because one or more rules are being published.|
> |**Name**:<br />CannotEnableEntityForRelevanceSearch<br />**Hex**:<br />80060302<br />**Number**:<br />-2147089662|Entity {0} can’t be enabled for relevance search because of the configuration of its managed properties.|
> |**Name**:<br />CannotExceedFilterLimit<br />**Hex**:<br />8004027c<br />**Number**:<br />-2147220868|Cannot exceed synchronization filter limit.|
> |**Name**:<br />CannotExecuteRequestBecauseHttpsIsRequired<br />**Hex**:<br />8004852C<br />**Number**:<br />-2147187412|HTTPS protocol is required for this type of request, please enable HTTPS protocol and try again.|
> |**Name**:<br />CannotFindDomainAccount<br />**Hex**:<br />80044342<br />**Number**:<br />-2147204286|Invalid domain account|
> |**Name**:<br />CannotFindObjectInQueue<br />**Hex**:<br />800404eb<br />**Number**:<br />-2147220245|The object was not found in the given queue|
> |**Name**:<br />CannotFindUserQueue<br />**Hex**:<br />800404ec<br />**Number**:<br />-2147220244|Cannot find user queue|
> |**Name**:<br />CannotFollowInactiveEntity<br />**Hex**:<br />8004F6A3<br />**Number**:<br />-2147158365|Can't follow inactive record. |
> |**Name**:<br />CannotGrantAccessToAddressBookFilters<br />**Hex**:<br />80048446<br />**Number**:<br />-2147187642|Cannot grant access to address book filters|
> |**Name**:<br />CannotGrantAccessToOfflineFilters<br />**Hex**:<br />80040271<br />**Number**:<br />-2147220879|Cannot grant access to offline filters|
> |**Name**:<br />CannotGrantAccessToOutlookFilters<br />**Hex**:<br />80040268<br />**Number**:<br />-2147220888|Cannot grant access to outlook filters|
> |**Name**:<br />CannotHaveDuplicateYomi<br />**Hex**:<br />80047018<br />**Number**:<br />-2147192808|One attribute can be tied to only one yomi at a time|
> |**Name**:<br />CannotHaveMultipleDefaultFilterTemplates<br />**Hex**:<br />8004027d<br />**Number**:<br />-2147220867|Cannot have multiple default synchronization templates for a single entity.|
> |**Name**:<br />CannotImportNullStringsForBaseLanguage<br />**Hex**:<br />80044246<br />**Number**:<br />-2147204538|The base language translation string present in worksheet {0}, row {1}, column {2} is null.|
> |**Name**:<br />CannotInviteDisabledUser<br />**Hex**:<br />8004D212<br />**Number**:<br />-2147167726|An invitation cannot be sent to a disabled user|
> |**Name**:<br />CannotLocateRecordForWorkflowActivity<br />**Hex**:<br />80045031<br />**Number**:<br />-2147200975|A record required by this workflow job could not be found.|
> |**Name**:<br />CannotMakeReadOnlyUser<br />**Hex**:<br />80041d38<br />**Number**:<br />-2147214024|A user cannot be made a read only user if they are the last non read only user that has the System Administrator Role.|
> |**Name**:<br />CannotMakeSelfReadOnlyUser<br />**Hex**:<br />80041d39<br />**Number**:<br />-2147214023|You cannot make yourself a read only user|
> |**Name**:<br />CannotMergeCase<br />**Hex**:<br />8004F457<br />**Number**:<br />-2147158953|The merge couldn't be performed. One or more of the selected cases couldn't be cancelled because of the status transition rules that are defined for cases.|
> |**Name**:<br />CannotModifyAccessToAddressBookFilters<br />**Hex**:<br />80048445<br />**Number**:<br />-2147187643|Cannot modify access for address book filters|
> |**Name**:<br />CannotModifyAccessToOfflineFilters<br />**Hex**:<br />80040272<br />**Number**:<br />-2147220878|Cannot modify access for offline filters|
> |**Name**:<br />CannotModifyAccessToOutlookFilters<br />**Hex**:<br />80040269<br />**Number**:<br />-2147220887|Cannot modify access for outlook filters|
> |**Name**:<br />CannotModifyOldDataFromImport<br />**Hex**:<br />80040376<br />**Number**:<br />-2147220618|The corresponding record in Microsoft Dynamics 365 has more recent data, so this record was ignored.|
> |**Name**:<br />CannotModifyPatchedSolution<br />**Hex**:<br />80048538<br />**Number**:<br />-2147187400|Cannot modify solution because it has the following patches: {0}.|
> |**Name**:<br />CannotModifyReportOutsideSolutionIfManaged<br />**Hex**:<br />8004F038<br />**Number**:<br />-2147160008|Managed solution cannot update reports which are not present in solution package.|
> |**Name**:<br />CannotModifyRollupDependentField<br />**Hex**:<br />80060555<br />**Number**:<br />-2147089067|Rollup field {0} created this field. It can’t be modified directly.|
> |**Name**:<br />CannotModifySpecialUser<br />**Hex**:<br />80041d33<br />**Number**:<br />-2147214029|No modifications to the 'SYSTEM' or 'INTEGRATION' user are permitted.|
> |**Name**:<br />CannotModifySupportUser<br />**Hex**:<br />80041d43<br />**Number**:<br />-2147214013|The Support User Role cannot be modified.|
> |**Name**:<br />CannotModifySysAdmin<br />**Hex**:<br />80041d31<br />**Number**:<br />-2147214031|The System Administrator Role cannot be modified.|
> |**Name**:<br />CannotOverrideOwnedDynamicProperty<br />**Hex**:<br />80081005<br />**Number**:<br />-2146955259|You can't override a property that isn't inherited from a product family.|
> |**Name**:<br />CannotOverrideProperty<br />**Hex**:<br />8004F887<br />**Number**:<br />-2147157881|You can't override this property as another overriden version of this property already exists. Please delete the previously overridden version, and then try again.|
> |**Name**:<br />CannotOverridePropertyFromDifferentHierarchy<br />**Hex**:<br />8004F914<br />**Number**:<br />-2147157740|You can't override a property that belongs to a different product hierarchy.|
> |**Name**:<br />CannotOverwriteActiveComponent<br />**Hex**:<br />8004F016<br />**Number**:<br />-2147160042|A managed solution cannot overwrite the {0} component {1} with Id={2} which has an unmanaged base instance.  The most likely scenario for this error is that an unmanaged solution has installed a new unmanaged {0} component on the target system, and now a managed solution from the same publisher is trying to install that same {0} component as managed.  This will cause an invalid layering of solutions on the target system and is not allowed.|
> |**Name**:<br />CannotOverwriteProperty<br />**Hex**:<br />80061036<br />**Number**:<br />-2147086282|You can't overwrite this property as another overwritten version of this property already exists. Please delete the previously overwritten version, and then try again.|
> |**Name**:<br />CannotPayNonActiveInvoice<br />**Hex**:<br />80100000<br />**Number**:<br />-2146435072|The invoice cannot be paid because it is not in active state.|
> |**Name**:<br />CannotPropagateCamapaignActivityForTemplate<br />**Hex**:<br />80040311<br />**Number**:<br />-2147220719|Cannot execute (distribute) a CampaignActivity for a template Campaign.|
> |**Name**:<br />CannotProvisionPartnerSolution<br />**Hex**:<br />8004A10f<br />**Number**:<br />-2147180273|Can not provision partner solution as it is either already provisioned or going through provisioning.|
> |**Name**:<br />CannotPublishAppModule<br />**Hex**:<br />80050114<br />**Number**:<br />-2147155692|We can’t publish the app because it has validation errors.|
> |**Name**:<br />CannotPublishBundleWithProductStateDraftOrRetire<br />**Hex**:<br />8004F907<br />**Number**:<br />-2147157753|You can't publish this bundle because its associated products are in a draft state, are retired, or are being revised.|
> |**Name**:<br />CannotPublishChildOfNonActiveProductFamily<br />**Hex**:<br />8004F909<br />**Number**:<br />-2147157751|You can't publish this record because it belongs to a product family that isn't published.|
> |**Name**:<br />CannotPublishEmptyRule<br />**Hex**:<br />80048414<br />**Number**:<br />-2147187692|No criteria have been specified. Add criteria, and then publish the duplicate detection rule.|
> |**Name**:<br />CannotPublishInactiveRule<br />**Hex**:<br />80048413<br />**Number**:<br />-2147187693|The selected duplicate detection rule is marked as Inactive. Before publishing, you must activate the rule.|
> |**Name**:<br />CannotPublishKitWithProductStateDraftOrRetire<br />**Hex**:<br />8004F916<br />**Number**:<br />-2147157738|You can't publish this kit because its associated products are in a draft state, are retired, or are being revised.|
> |**Name**:<br />CannotPublishMoreRules<br />**Hex**:<br />80048419<br />**Number**:<br />-2147187687|The selected record type already has the maximum number of published rules. Unpublish or delete existing rules for this record type, and then try again.|
> |**Name**:<br />CannotPublishNestedBundle<br />**Hex**:<br />80061011<br />**Number**:<br />-2147086319|You can't publish a bundle that contains bundles. Remove any bundles from this one, and then try to publish again.|
> |**Name**:<br />CannotQualifyLead<br />**Hex**:<br />80081018<br />**Number**:<br />-2146955240|You can't qualify this lead because you don't have permission to create accounts. Work with your system administrator to create the account and then try again.|
> |**Name**:<br />CannotQueryBaseTableWithAggregates<br />**Hex**:<br />8004F00D<br />**Number**:<br />-2147160051|Invalid query on base table.  Aggregates cannot be included in base table query.|
> |**Name**:<br />CannotRelateObjectTypeToCampaign<br />**Hex**:<br />80040307<br />**Number**:<br />-2147220729|Specified Object Type not supported|
> |**Name**:<br />CannotRelateObjectTypeToCampaignActivity<br />**Hex**:<br />8004030d<br />**Number**:<br />-2147220723|Specified Object Type not supported|
> |**Name**:<br />CannotRemoveComponentFromDefaultSolution<br />**Hex**:<br />8004F000<br />**Number**:<br />-2147160064|A Solution Component cannot be removed from the Default Solution.|
> |**Name**:<br />CannotRemoveComponentFromSolution<br />**Hex**:<br />8004F021<br />**Number**:<br />-2147160031|Cannot find solution component {0} {1} in solution {2}.|
> |**Name**:<br />CannotRemoveComponentFromSystemSolution<br />**Hex**:<br />8004F035<br />**Number**:<br />-2147160011|A Solution Component cannot be removed from the System Solution.|
> |**Name**:<br />CannotRemoveFromSupportUser<br />**Hex**:<br />80041d45<br />**Number**:<br />-2147214011|A user cannot be removed from the Support User Role.|
> |**Name**:<br />CannotRemoveFromSysAdmin<br />**Hex**:<br />80041d30<br />**Number**:<br />-2147214032|A user cannot be removed from the System Administrator Role if they are the only user that has the role.|
> |**Name**:<br />CannotRemoveMembersFromDefaultTeam<br />**Hex**:<br />8004830C<br />**Number**:<br />-2147187956|Can't remove members from the default business unit team.|
> |**Name**:<br />CannotRemoveNonListMember<br />**Hex**:<br />80048458<br />**Number**:<br />-2147187624|Specified Item not a member of the specified List.|
> |**Name**:<br />CannotRemoveProductFromPricelist<br />**Hex**:<br />80061008<br />**Number**:<br />-2147086328|You can't remove this product from the pricelist because one or more bundles refer to it.|
> |**Name**:<br />CannotRemoveSysAdminProfileFromSysAdminUser<br />**Hex**:<br />8004F505<br />**Number**:<br />-2147158779|The Sys Admin Profile cannot be removed from a user with a Sys Admin Role|
> |**Name**:<br />CannotRemoveTenantAdminFromSysAdminRole<br />**Hex**:<br />80041d64<br />**Number**:<br />-2147213980|Users who are granted the Microsoft Office 365 Global administrator or Service administrator role cannot be removed from the Microsoft Dynamics 365 System Administrator security role. You must first remove the Microsoft Office 365 role, and then try again.|
> |**Name**:<br />CannotResetAppointmentsToDraft<br />**Hex**:<br />8004026a<br />**Number**:<br />-2147220886|Appointments cannot be reset to draft.|
> |**Name**:<br />CannotResetSysAdminInvite<br />**Hex**:<br />8004D214<br />**Number**:<br />-2147167724|An invitation cannot be reset for a user if they are the only user that has the System Administrator Role.|
> |**Name**:<br />CannotRetireProduct<br />**Hex**:<br />8004F915<br />**Number**:<br />-2147157739|You can't retire this product because it belongs to active bundles or price lists. Remove it from any bundles or price lists before you retire it.|
> |**Name**:<br />CannotRetireProductFromActiveBundle<br />**Hex**:<br />8004F997<br />**Number**:<br />-2147157609|This product cannot be retired because it is a part of some active bundles or pricelists. Please remove it from all bundles or pricelists before retiring.|
> |**Name**:<br />CannotRevokeAccessToAddressBookFilters<br />**Hex**:<br />80048444<br />**Number**:<br />-2147187644|Cannot revoke access for address book filters|
> |**Name**:<br />CannotRevokeAccessToOfflineFilters<br />**Hex**:<br />80040273<br />**Number**:<br />-2147220877|Cannot revoke access for offline filters|
> |**Name**:<br />CannotRevokeAccessToOutlookFilters<br />**Hex**:<br />80040270<br />**Number**:<br />-2147220880|Cannot revoke access for outlook filters|
> |**Name**:<br />CannotRouteInactiveQueueItem<br />**Hex**:<br />80040527<br />**Number**:<br />-2147220185|You can't route a queue item that has been deactivated.|
> |**Name**:<br />CannotRoutePrivateQueueItemNonmember<br />**Hex**:<br />80631121<br />**Number**:<br />-2140991199|This private queue item can't be assigned To the selected User.|
> |**Name**:<br />CannotRouteToNonQueueMember<br />**Hex**:<br />80731119<br />**Number**:<br />-2139942631|This item cannot be routed to a non-queue member.|
> |**Name**:<br />CannotRouteToQueue<br />**Hex**:<br />800404ea<br />**Number**:<br />-2147220246|Cannot route to Work in progress queue|
> |**Name**:<br />CannotRouteToSameQueue<br />**Hex**:<br />8004051b<br />**Number**:<br />-2147220197|The queue item cannot be routed to the same queue|
> |**Name**:<br />CannotSecureAttribute<br />**Hex**:<br />8004F501<br />**Number**:<br />-2147158783|The field '{0}' is not securable|
> |**Name**:<br />CannotSecureEntityKeyAttribute<br />**Hex**:<br />80060896<br />**Number**:<br />-2147088234|The field {0} is not securable as it is part of entity keys ( {1} ). Please remove the field from all entity keys to make it securable.|
> |**Name**:<br />CannotSelectReadOnlyPublisher<br />**Hex**:<br />8004F034<br />**Number**:<br />-2147160012|Attempting to  select a readonly publisher for solution.|
> |**Name**:<br />CannotSendInviteToDuplicateWindowsLiveId<br />**Hex**:<br />8004D215<br />**Number**:<br />-2147167723|An invitation cannot be sent because there are multiple users with this WLID.|
> |**Name**:<br />CannotSetCaseOnHold<br />**Hex**:<br />80055000<br />**Number**:<br />-2147135488|You do not have the permissions to set this case to an on hold status type. Please contact your system administrator.|
> |**Name**:<br />CannotSetEntitlementTermsDecrementBehavior<br />**Hex**:<br />80060851<br />**Number**:<br />-2147088303|You do not have appropriate privileges to specify whether entitlement terms can be decremented for this case record.|
> |**Name**:<br />CannotSetEntityOnHold<br />**Hex**:<br />80055004<br />**Number**:<br />-2147135484|You don’t have permission to put this record on hold. Contact your system administrator.|
> |**Name**:<br />CannotSetInactiveViewAsDefault<br />**Hex**:<br />8004027b<br />**Number**:<br />-2147220869|Inactive views cannot be set as default view.|
> |**Name**:<br />CannotSetParentDefaultTeam<br />**Hex**:<br />80048308<br />**Number**:<br />-2147187960|The default business unit team parent can't be set.|
> |**Name**:<br />CannotSetProductAsParent<br />**Hex**:<br />8004F998<br />**Number**:<br />-2147157608|You can only select a product family as the parent.|
> |**Name**:<br />CannotSetPublishRetiredProductsToDraft<br />**Hex**:<br />80061035<br />**Number**:<br />-2147086283|You can't set a published or retired product record to the draft state.|
> |**Name**:<br />CannotSetSolutionSystemAttributes<br />**Hex**:<br />8004F008<br />**Number**:<br />-2147160056|System attributes ({0}) cannot be set outside of installation or upgrade.|
> |**Name**:<br />CannotSetWindowsLiveIdForInternetMarketingUser<br />**Hex**:<br />80045034<br />**Number**:<br />-2147200972|You cannot change the Windows Live ID for the Internet Marketing Partner user. This user does not consume a user license and is not charged to your organization.|
> |**Name**:<br />CannotShareSystemManagedTeam<br />**Hex**:<br />80048339<br />**Number**:<br />-2147187911|You can't share or unshare a record with a system-generated access team.|
> |**Name**:<br />CannotShareWithOwner<br />**Hex**:<br />80040214<br />**Number**:<br />-2147220972|An item cannot be shared with the owning user.|
> |**Name**:<br />CannotSpecifyAttendeeForAppointmentPropagation<br />**Hex**:<br />8004031c<br />**Number**:<br />-2147220708|Cannot specify an attendee for appointment distribution.|
> |**Name**:<br />CannotSpecifyBothProductAndProductDesc<br />**Hex**:<br />80043afb<br />**Number**:<br />-2147206405|You cannot set both 'productid' and 'productdescription' for the same record.|
> |**Name**:<br />CannotSpecifyBothUomAndProductDesc<br />**Hex**:<br />80043afa<br />**Number**:<br />-2147206406|You cannot set both 'uomid' and 'productdescription' for the same record.|
> |**Name**:<br />CannotSpecifyCommunicationAttributeOnActivityForPropagation<br />**Hex**:<br />8004031e<br />**Number**:<br />-2147220706|Cannot specify communication attribute on activity for distribution|
> |**Name**:<br />CannotSpecifyOrganizerForAppointmentPropagation<br />**Hex**:<br />8004031a<br />**Number**:<br />-2147220710|Cannot specify an organizer for appointment distribution|
> |**Name**:<br />CannotSpecifyOwnerForActivityPropagation<br />**Hex**:<br />80040327<br />**Number**:<br />-2147220697|Cannot specify owner on activity for distribution|
> |**Name**:<br />CannotSpecifyRecipientForActivityPropagation<br />**Hex**:<br />8004031d<br />**Number**:<br />-2147220707|Cannot specify a recipient for activity distribution.|
> |**Name**:<br />CannotSpecifySenderForActivityPropagation<br />**Hex**:<br />8004031b<br />**Number**:<br />-2147220709|Cannot specify a sender for appointment distribution|
> |**Name**:<br />CannotUndeleteLabel<br />**Hex**:<br />8004F003<br />**Number**:<br />-2147160061|Attempting to undelete a label that is not marked as delete.|
> |**Name**:<br />CannotUninstallReferencedProtectedSolution<br />**Hex**:<br />8004F020<br />**Number**:<br />-2147160032|This solution cannot be uninstalled because the '{0}' with id '{1}'  is required by the '{2}' solution. Uninstall the {2} solution and try again.|
> |**Name**:<br />CannotUninstallWithDependencies<br />**Hex**:<br />8004F01D<br />**Number**:<br />-2147160035|Solution dependencies exist, cannot uninstall.|
> |**Name**:<br />CannotUpdateActiveModernFlow<br />**Hex**:<br />80060466<br />**Number**:<br />-2147089306|Cannot update property "{0}" on a published Modern Flow process.|
> |**Name**:<br />CannotUpdateAppDefaultValueForStateAttribute<br />**Hex**:<br />80044343<br />**Number**:<br />-2147204285|The default value for a status (statecode) attribute cannot be updated.|
> |**Name**:<br />CannotUpdateAppDefaultValueForStatusAttribute<br />**Hex**:<br />80044344<br />**Number**:<br />-2147204284|The default value for a status reason (statuscode) attribute is not used. The default status reason is set in the associated status (statecode) attribute option.|
> |**Name**:<br />CannotUpdateAppModuleClientType<br />**Hex**:<br />80050128<br />**Number**:<br />-2147155672|Can’t change the client type of this app.|
> |**Name**:<br />CannotUpdateAppModuleUniqueName<br />**Hex**:<br />80050119<br />**Number**:<br />-2147155687|You can’t change the unique name .|
> |**Name**:<br />CannotUpdateAzureActiveDirectoryObjectIdField<br />**Hex**:<br />80041d4f<br />**Number**:<br />-2147214001|The property AzureActiveDirectoryObjectId cannot be modified.|
> |**Name**:<br />CannotUpdateBecauseItIsReadOnly<br />**Hex**:<br />8004022e<br />**Number**:<br />-2147220946|The object cannot be updated because it is read-only.|
> |**Name**:<br />CannotUpdateCampaignForCampaignActivity<br />**Hex**:<br />8004030b<br />**Number**:<br />-2147220725|Parent campaign is not updatable.|
> |**Name**:<br />CannotUpdateCampaignForCampaignResponse<br />**Hex**:<br />8004030c<br />**Number**:<br />-2147220724|Parent campaign is not updatable.|
> |**Name**:<br />CannotUpdateDeactivatedQueueItem<br />**Hex**:<br />8004051d<br />**Number**:<br />-2147220195|This item is deactivated. To work with this item, reactivate it and then try again.|
> |**Name**:<br />CannotUpdateDefaultField<br />**Hex**:<br />800608D8<br />**Number**:<br />-2147088168|You can’t update the isdefaultTheme attribute.|
> |**Name**:<br />CannotUpdateDefaultSolution<br />**Hex**:<br />8004F009<br />**Number**:<br />-2147160055|Default solution attribute{0} {1} can only be set on installation or upgrade.  The value{0} cannot be modified.|
> |**Name**:<br />CannotUpdateDelaySendTimeForEmailWhenEmailIsNotInProperState<br />**Hex**:<br />80050020<br />**Number**:<br />-2147155936|We can’t update the delay send time because the email is not a draft or isn’t scheduled to be sent.|
> |**Name**:<br />CannotUpdateDelaySendTimeWhenEEFeatureNotEnabled<br />**Hex**:<br />80050021<br />**Number**:<br />-2147155935|We can’t update the delay send time because Email Engagement isn’t turned on for the organization.|
> |**Name**:<br />CannotUpdateDraftProducts<br />**Hex**:<br />8004F975<br />**Number**:<br />-2147157643|You can Only update draft products.|
> |**Name**:<br />CannotUpdateEmailStatisticForEmailNotFollowed<br />**Hex**:<br />80050002<br />**Number**:<br />-2147155966|We can’t update email statistics because the email isn’t being followed.|
> |**Name**:<br />CannotUpdateEmailStatisticForEmailNotSent<br />**Hex**:<br />80050001<br />**Number**:<br />-2147155967|We can’t update email statistics because the email hasn’t been sent.|
> |**Name**:<br />CannotUpdateEmailStatisticWhenEEFeatureNotEnabled<br />**Hex**:<br />80050018<br />**Number**:<br />-2147155944|We can’t update email statistics because Email Engagement isn’t turned on for the organization.|
> |**Name**:<br />CannotUpdateEntitlement<br />**Hex**:<br />80060852<br />**Number**:<br />-2147088302|You can only set Active entitlement records as default.|
> |**Name**:<br />CannotUpdateEntitySetName<br />**Hex**:<br />8004F663<br />**Number**:<br />-2147158429|EntitySetName cannot be updated for OOB entities|
> |**Name**:<br />CannotUpdateExternalPartyWithSameCorrelationKey<br />**Hex**:<br />80061114<br />**Number**:<br />-2147086060|An external party record already exists with the same correlation key value.|
> |**Name**:<br />CannotUpdateGoalPeriodInfoChildGoal<br />**Hex**:<br />80044901<br />**Number**:<br />-2147202815|You cannot update goal period related attributes on a child goal.|
> |**Name**:<br />CannotUpdateGoalPeriodInfoClosedGoal<br />**Hex**:<br />80044910<br />**Number**:<br />-2147202800|You cannot change the time period of this goal because there are one or more closed subordinate goals.|
> |**Name**:<br />CannotUpdateManagedSolution<br />**Hex**:<br />8004F024<br />**Number**:<br />-2147160028|Cannot update solution '{0}' because it is a managed solution.|
> |**Name**:<br />CannotUpdateMetricOnChildGoal<br />**Hex**:<br />80044900<br />**Number**:<br />-2147202816|You cannot update metric on a child goal.|
> |**Name**:<br />CannotUpdateMetricOnGoalWithChildren<br />**Hex**:<br />80044902<br />**Number**:<br />-2147202814|You cannot update metric on a goal which has associated child goals.|
> |**Name**:<br />CannotUpdateMetricWithGoals<br />**Hex**:<br />80044803<br />**Number**:<br />-2147203069|The changes made to this record cannot be saved because this goal metric is being used by one or more goals.|
> |**Name**:<br />CannotUpdateNameDefaultTeam<br />**Hex**:<br />8004830A<br />**Number**:<br />-2147187958|The default business unit team name can't be updated.|
> |**Name**:<br />CannotUpdateNonCustomizableString<br />**Hex**:<br />80044247<br />**Number**:<br />-2147204537|The translation string present in worksheet {0}, row {1}, column {2} is not customizable.|
> |**Name**:<br />CannotUpdateObjectBecauseItIsInactive<br />**Hex**:<br />80040230<br />**Number**:<br />-2147220944|The object cannot be updated because it is inactive.|
> |**Name**:<br />CannotUpdateOpportunityCurrency<br />**Hex**:<br />80048479<br />**Number**:<br />-2147187591|The currency cannot be changed because this opportunity has Products Quotes, and/ or Orders associated with it.  If you want to change the currency please delete all of the Products/quotes/orders and then change the currency or create a new opportunity with the appropriate currency.|
> |**Name**:<br />CannotUpdateOrgDBOrgSettingWhenOffline<br />**Hex**:<br />80048515<br />**Number**:<br />-2147187435|Organization Settings stored in Organization Database cannot be set when offline.|
> |**Name**:<br />CannotUpdateParentAndDependents<br />**Hex**:<br />8004480c<br />**Number**:<br />-2147203060|Cannot update metric or period attributes when parent is being updated.|
> |**Name**:<br />CannotUpdatePrivateOrWIPQueue<br />**Hex**:<br />800404ee<br />**Number**:<br />-2147220242|The private or WIP Bin queue is not allowed to be updated or deleted|
> |**Name**:<br />CannotUpdateProductCurrency<br />**Hex**:<br />80048cfa<br />**Number**:<br />-2147185414|The currency of the product cannot be updated because there are associated price list items with pricing method percentage.|
> |**Name**:<br />CannotUpdateQuoteCurrency<br />**Hex**:<br />8004480e<br />**Number**:<br />-2147203058|The currency cannot be changed because this quote has Products associated with it. If you want to change the currency please delete all of the Products and then change the currency or create a new quote with the appropriate currency.|
> |**Name**:<br />CannotUpdateReadOnlyPublisher<br />**Hex**:<br />8004F033<br />**Number**:<br />-2147160013|Attempting to update a readonly publisher.|
> |**Name**:<br />CannotUpdateRestrictedPublisher<br />**Hex**:<br />8004F017<br />**Number**:<br />-2147160041|Restricted publisher ({0}) cannot be updated.|
> |**Name**:<br />CannotUpdateRestrictedSolution<br />**Hex**:<br />8004F00A<br />**Number**:<br />-2147160054|Restricted solution ({0}) cannot be updated.|
> |**Name**:<br />CannotUpdateRollupAttributeWithClosedGoals<br />**Hex**:<br />80044801<br />**Number**:<br />-2147203071|The changes made to the roll-up field definition cannot be saved because the related goal metric is being used by one or more closed goals.|
> |**Name**:<br />CannotUpdateRollupFields<br />**Hex**:<br />80044911<br />**Number**:<br />-2147202799|You cannot write on rollup fields if isoverride is not set to true in your create/update request.|
> |**Name**:<br />CannotUpdateSolutionPatch<br />**Hex**:<br />8004F042<br />**Number**:<br />-2147159998|Solution patch with version {0} already exists. Updating patch is not supported.|
> |**Name**:<br />CannotUpdateSupportUser<br />**Hex**:<br />80041d47<br />**Number**:<br />-2147214009|Cannot update the Support User Role.|
> |**Name**:<br />CannotUpdateSyncUserIsLicensedField<br />**Hex**:<br />80041d4c<br />**Number**:<br />-2147214004|The property IsLicensed cannot be modified.|
> |**Name**:<br />CannotUpdateSyncUserIsSyncWithDirectoryField<br />**Hex**:<br />80041d4e<br />**Number**:<br />-2147214002|The property IsSyncUserWithDirectory cannot be modified.|
> |**Name**:<br />CannotUpdateSystemEntityIcons<br />**Hex**:<br />8004F653<br />**Number**:<br />-2147158445|System entity icons cannot be updated.|
> |**Name**:<br />CannotUpdateSystemTheme<br />**Hex**:<br />800608D6<br />**Number**:<br />-2147088170|You can’t modify system themes.|
> |**Name**:<br />CannotUpdateTemplateIdForEmailInNonDraftState<br />**Hex**:<br />80050017<br />**Number**:<br />-2147155945|We can’t update the template because the email has already been sent or is not in a Draft state.|
> |**Name**:<br />CannotUpdateTriggerForPublishedRules<br />**Hex**:<br />80060002<br />**Number**:<br />-2147090430|A trigger cannot be added/deleted/updated for a published rule.|
> |**Name**:<br />CannotUpdateUnpublishedDeleteInstance<br />**Hex**:<br />8004F00F<br />**Number**:<br />-2147160049|The component that you are trying to update has been deleted.|
> |**Name**:<br />CannotUseOpportunitySetStateMessage<br />**Hex**:<br />80100005<br />**Number**:<br />-2146435067|This message can not be used to set the state of opportunity to {0}. In order to set state of opportunity to {1}, use the {1} message instead.|
> |**Name**:<br />CannotUseUserCredentials<br />**Hex**:<br />8005E229<br />**Number**:<br />-2147098071|Email connector cannot use the credentials specified in the mailbox entity. This might be because user has disallowed it. Please use other mode of credential retrieval or allow the use of credential by email connector.|
> |**Name**:<br />CanOnlySetActiveOrDraftProductFamilyAsParent<br />**Hex**:<br />8004F906<br />**Number**:<br />-2147157754|You can only set product families in a draft or active state as parent.|
> |**Name**:<br />CantSaveRecordInOffline<br />**Hex**:<br />8005F214<br />**Number**:<br />-2147093996|You can't save this record while you're offline.|
> |**Name**:<br />CantSetIsGuestProfile<br />**Hex**:<br />8006111A<br />**Number**:<br />-2147086054|You can’t set or change the value of the IsGuestProfile field because it’s for internal use only.|
> |**Name**:<br />CantUpdateOnlineRecord<br />**Hex**:<br />8005F224<br />**Number**:<br />-2147093980|You can’t update this record because it doesn’t exist in the offline mode.|
> |**Name**:<br />CanvasAppsExpectedFileMissing<br />**Hex**:<br />80072356<br />**Number**:<br />-2147015850|The solution specified an expected assets file but that file was missing or invalid.|
> |**Name**:<br />CanvasAppsInvalidSolutionFileContent<br />**Hex**:<br />80072354<br />**Number**:<br />-2147015852|The request to import a canvas app should contain at least one asset file.|
> |**Name**:<br />CanvasAppsNotEnabled<br />**Hex**:<br />80072351<br />**Number**:<br />-2147015855|Creation and editing of Canvas Apps is not enabled.|
> |**Name**:<br />CanvasAppsServiceRequestClientFailure<br />**Hex**:<br />80072352<br />**Number**:<br />-2147015854|The request to the PowerApps service failed with a client failure.|
> |**Name**:<br />CanvasAppsServiceRequestServerFailure<br />**Hex**:<br />80072353<br />**Number**:<br />-2147015853|The request to the PowerApps service failed with a server failure.|
> |**Name**:<br />CanvasAppsUnexpectedCanvasAppId<br />**Hex**:<br />80072355<br />**Number**:<br />-2147015851|The request to the PowerApps service resulted in a new canvasappid when the previously existing value was expected.|
> |**Name**:<br />CanvasAppVersionDoesNotMatchLatestPublishedVersion<br />**Hex**:<br />80072358<br />**Number**:<br />-2147015848|The latest published version of the canvas app does not match the version known by the Dynamics service.|
> |**Name**:<br />CanvasAppVersionMissingOrInvalid<br />**Hex**:<br />80072357<br />**Number**:<br />-2147015849|The app version of the canvas app was not set or was an invalid value.|
> |**Name**:<br />CAPolicyValidationFailedLateBind<br />**Hex**:<br />80072561<br />**Number**:<br />-2147015327|The user is in an admin restricted location.|
> |**Name**:<br />CascadeDeleteNotAllowDelete<br />**Hex**:<br />80048103<br />**Number**:<br />-2147188477|Object is not allowed to be deleted|
> |**Name**:<br />CascadeFailToCreateNativeDAWrapper<br />**Hex**:<br />80048108<br />**Number**:<br />-2147188472|Failed to create unmanaged data access wrapper|
> |**Name**:<br />CascadeInvalidExtraConditionValue<br />**Hex**:<br />80048101<br />**Number**:<br />-2147188479|Invalid Extra-condition value|
> |**Name**:<br />CascadeInvalidLinkType<br />**Hex**:<br />80048102<br />**Number**:<br />-2147188478|Invalid CascadeLink Type|
> |**Name**:<br />CascadeInvalidLinkTypeTransition<br />**Hex**:<br />80044155<br />**Number**:<br />-2147204779|Invalid link type for system entity cascading actions.|
> |**Name**:<br />CascadeMergeInvalidSpecialColumn<br />**Hex**:<br />80048106<br />**Number**:<br />-2147188474|Invalid Column Name for Merge Special Casing|
> |**Name**:<br />CascadeProxyEmptyCallerId<br />**Hex**:<br />8004810b<br />**Number**:<br />-2147188469|Empty Caller Id|
> |**Name**:<br />CascadeProxyInvalidNativeDAPtr<br />**Hex**:<br />80048109<br />**Number**:<br />-2147188471|Invalid pointer of unmanaged data access object|
> |**Name**:<br />CascadeProxyInvalidPrincipalType<br />**Hex**:<br />8004810a<br />**Number**:<br />-2147188470|Invalid security principal type|
> |**Name**:<br />CascadeRemoveLinkOnNonNullable<br />**Hex**:<br />80048104<br />**Number**:<br />-2147188476|CascadeDelete is defined as RemoveLink while the foreign key is not nullable|
> |**Name**:<br />CascadeReparentOnNonUserOwned<br />**Hex**:<br />80048107<br />**Number**:<br />-2147188473|Cannot perform Cascade Reparent on Non-UserOwned entities|
> |**Name**:<br />CaseAlreadyResolved<br />**Hex**:<br />800404cf<br />**Number**:<br />-2147220273|This case has already been resolved. Close and reopen the case record to see the updates.|
> |**Name**:<br />CaseStateChangeInvalid<br />**Hex**:<br />8006074<br />**Number**:<br />134242420|Because of the status transition rules, you can't resolve a case in the current status. Change the case status, and then try resolving it, or contact your system administrator.|
> |**Name**:<br />CategoryDataTypeInvalid<br />**Hex**:<br />8004E01A<br />**Number**:<br />-2147164134|The Data Description for the visualization is invalid. The attribute type for the group by of one of the categories is invalid. Correct the Data Description.|
> |**Name**:<br />CategoryNotSetToBusinessProcessFlow<br />**Hex**:<br />80060404<br />**Number**:<br />-2147089404|Category should be set to BusinessProcessFlow while creating business process flow category|
> |**Name**:<br />CDSOrgNotSupported<br />**Hex**:<br />80044510<br />**Number**:<br />-2147203824|Dynamics 365 for Outlook is not supported for this organization.|
> |**Name**:<br />CertificateNotFound<br />**Hex**:<br />8005E239<br />**Number**:<br />-2147098055|The given certificate cannot be found.|
> |**Name**:<br />ChangeTrackingDisabledForMobileOfflineError<br />**Hex**:<br />800609A1<br />**Number**:<br />-2147087967|You can not disable change tracking for this entity since mobile offline is already enabled.|
> |**Name**:<br />ChangeTrackingNotEnabledForEntity<br />**Hex**:<br />80072491<br />**Number**:<br />-2147015535|Entity {0} isn't enabled for change tracking.|
> |**Name**:<br />ChangeTrackingNotEnabledForRelatedEntities<br />**Hex**:<br />80072492<br />**Number**:<br />-2147015534|Changes cannot be retrieved for intersect entity {0} since both related entities are not enabled for change tracking.|
> |**Name**:<br />ChannelAccessProfileRuleAlreadyInDraftState<br />**Hex**:<br />80061115<br />**Number**:<br />-2147086059|You can't deactivate a draft channel access profile rule.|
> |**Name**:<br />ChannelPropertyGroupAlreadyExistsWithSameSourceType<br />**Hex**:<br />800608EC<br />**Number**:<br />-2147088148|A record for the specified source type already exists. You can't create another one.|
> |**Name**:<br />ChannelPropertyNameInvalid<br />**Hex**:<br />800608F2<br />**Number**:<br />-2147088142|The channel property name is invalid. The name can only contain '_', numerical, and alphabetical characters. Choose a different name, and try again.|
> |**Name**:<br />ChartAreaCategoryMismatch<br />**Hex**:<br />8004E005<br />**Number**:<br />-2147164155|Number of chart areas and number of categories should be same.|
> |**Name**:<br />ChartTypeNotSupportedForComparisonChart<br />**Hex**:<br />8004E018<br />**Number**:<br />-2147164136|This chart type is not supported for comparison charts.|
> |**Name**:<br />ChartTypeNotSupportedForMultipleSeriesChart<br />**Hex**:<br />8004E021<br />**Number**:<br />-2147164127|Series of chart type {0} is not supported for multi-series charts.|
> |**Name**:<br />CheckPrivilegeGroupForUserOnPremiseError<br />**Hex**:<br />80048401<br />**Number**:<br />-2147187711|Please select an account that is a member of the PrivUserGroup security group and try again.|
> |**Name**:<br />CheckPrivilegeGroupForUserOnSplaError<br />**Hex**:<br />80048400<br />**Number**:<br />-2147187712|Please select a Dynamics 365 System Administrator account that belongs to the root business unit and try again.|
> |**Name**:<br />ChildBusinessDoesNotExist<br />**Hex**:<br />80041d22<br />**Number**:<br />-2147214046|The child businesss Id is invalid.|
> |**Name**:<br />ChildUserDoesNotExist<br />**Hex**:<br />80041d26<br />**Number**:<br />-2147214042|The child user Id is invalid.|
> |**Name**:<br />ChildWorkflowNotFound<br />**Hex**:<br />8004502F<br />**Number**:<br />-2147200977|This workflow cannot run because one or more child workflows it uses have not been published or have been deleted. Please check the child workflows and try running this workflow again.|
> |**Name**:<br />ChildWorkflowParameterMismatch<br />**Hex**:<br />80045048<br />**Number**:<br />-2147200952|This workflow cannot run because arguments provided by parent workflow does not match with the specified parameters in linked child workflow. Check the child workflow reference in parent workflow and try running this workflow again.|
> |**Name**:<br />CircularDependency<br />**Hex**:<br />80071157<br />**Number**:<br />-2147020457|The solution operation failed due to a circular dependency with other solutions. Please check the exception for more details: {0}|
> |**Name**:<br />ClientAuthCanceled<br />**Hex**:<br />8004D224<br />**Number**:<br />-2147167708|Authentication was canceled by the user.|
> |**Name**:<br />ClientAuthNoConnectivity<br />**Hex**:<br />8004D226<br />**Number**:<br />-2147167706|There is no connectivity.|
> |**Name**:<br />ClientAuthNoConnectivityOffline<br />**Hex**:<br />8004D225<br />**Number**:<br />-2147167707|There is no connectivity when running in offline mode.|
> |**Name**:<br />ClientAuthOfflineInvalidCallerId<br />**Hex**:<br />8004D227<br />**Number**:<br />-2147167705|Offline SDK calls must be made in the offline user context.|
> |**Name**:<br />ClientAuthSignedOut<br />**Hex**:<br />8004D221<br />**Number**:<br />-2147167711|The user signed out.|
> |**Name**:<br />ClientAuthSyncIssue<br />**Hex**:<br />8004D223<br />**Number**:<br />-2147167709|Synchronization between processes failed.|
> |**Name**:<br />ClientServerDateTimeMismatch<br />**Hex**:<br />80044503<br />**Number**:<br />-2147203837|Your computer's date/time is out of sync with the server by more than 5 minutes.|
> |**Name**:<br />ClientServerEmailAddressMismatch<br />**Hex**:<br />80044504<br />**Number**:<br />-2147203836|The Outlook email address and Dynamics 365 user email address do not match.|
> |**Name**:<br />ClientUpdateAvailable<br />**Hex**:<br />8004D294<br />**Number**:<br />-2147167596|There's an update available for Dynamics 365 for Outlook.|
> |**Name**:<br />ClientVersionTooHigh<br />**Hex**:<br />80044501<br />**Number**:<br />-2147203839|This version of Outlook client isn't compatible with your Dynamics 365 organization (current version {0} is too high).|
> |**Name**:<br />ClientVersionTooLow<br />**Hex**:<br />80044500<br />**Number**:<br />-2147203840|This version of Outlook client isn't compatible with your Dynamics 365 organization (current version {0} is too low).|
> |**Name**:<br />CloneSolutionException<br />**Hex**:<br />80048539<br />**Number**:<br />-2147187399|Operation on clone solution failed.|
> |**Name**:<br />CloneSolutionPatchException<br />**Hex**:<br />80061771<br />**Number**:<br />-2147084431|Patch '{0}' has a matching or higher version ({1}) than that of the patch being installed.|
> |**Name**:<br />CloneTitleTooLong<br />**Hex**:<br />80071112<br />**Number**:<br />-2147020526|A validation error occurred. The length of the Name attribute of the mobileofflineprofile entity exceeded the maximum allowed length of 200.|
> |**Name**:<br />CloseActiveChildCaseFirst<br />**Hex**:<br />8003F452<br />**Number**:<br />-2147224494|Close active child case before closing parent case.|
> |**Name**:<br />ColorStripAttributesExceeded<br />**Hex**:<br />80061500<br />**Number**:<br />-2147085056|Color Strip section cannot have more than 1 attribute|
> |**Name**:<br />ColorStripAttributesInvalid<br />**Hex**:<br />80061502<br />**Number**:<br />-2147085054|Color Strip section can only have attributes of type Two Options, Option Set and Status Reason|
> |**Name**:<br />CombinedManagedPropertyFailure<br />**Hex**:<br />8004F027<br />**Number**:<br />-2147160025|The evaluation of the current component(name={0}, id={1}) in the current operation ({2}) failed during at least one managed property evaluations: {3}|
> |**Name**:<br />CommandNotSupported<br />**Hex**:<br />80154B52<br />**Number**:<br />-2146088110|Command is not supported in offline mode.|
> |**Name**:<br />CommunicationBlocked<br />**Hex**:<br />80044506<br />**Number**:<br />-2147203834|Communication is blocked due to a socket exception.|
> |**Name**:<br />ComponentDefinitionDoesNotExists<br />**Hex**:<br />8004F019<br />**Number**:<br />-2147160039|No component definition exists for the component type {0}.|
> |**Name**:<br />ConcurrencyVersionMismatch<br />**Hex**:<br />80060882<br />**Number**:<br />-2147088254|The version of the existing record doesn't match the RowVersion property provided.|
> |**Name**:<br />ConcurrencyVersionNotProvided<br />**Hex**:<br />80060883<br />**Number**:<br />-2147088253|The RowVersion property must be provided when the value of ConcurrencyBehavior is IfVersionMatches.|
> |**Name**:<br />ConcurrentOperationFailure<br />**Hex**:<br />80071154<br />**Number**:<br />-2147020460|The current {0} operation failed due to another concurrent operation running at the same time. Please try again later.|
> |**Name**:<br />ConditionAttributesNotAnSubsetOfStepAttributes<br />**Hex**:<br />80060436<br />**Number**:<br />-2147089354|Attributes of the condition are not the subset of attributes in the Step, for the Stage : {0}|
> |**Name**:<br />ConditionBranchDoesHaveSetNextStageOnlyChildInXaml<br />**Hex**:<br />80060434<br />**Number**:<br />-2147089356|Branch condition can contain only SetNextStage as a child.|
> |**Name**:<br />ConditionStepCountInXamlExceedsMaxAllowed<br />**Hex**:<br />80060435<br />**Number**:<br />-2147089355|{0} cannot have more than one {1}.|
> |**Name**:<br />ConfigDBCannotDeleteDefaultOrganization<br />**Hex**:<br />8004D23B<br />**Number**:<br />-2147167685|The default {0} organization cannot be deleted from the MSCRM_CONFIG database.|
> |**Name**:<br />ConfigDBCannotDeleteObjectDueState<br />**Hex**:<br />8004D232<br />**Number**:<br />-2147167694|Cannot delete '{0}' with Value = ({1}) in this State = ({2}) from MSCRM_CONFIG database|
> |**Name**:<br />ConfigDBCannotUpdateObjectDueState<br />**Hex**:<br />8004D237<br />**Number**:<br />-2147167689|Cannot update '{0}' with Value = ({1}) in this State = ({2}) from MSCRM_CONFIG database|
> |**Name**:<br />ConfigDBCascadeDeleteNotAllowDelete<br />**Hex**:<br />8004D233<br />**Number**:<br />-2147167693|Cannot delete '{0}' with Value = ({1}) due to child '{2}' references from MSCRM_CONFIG database|
> |**Name**:<br />ConfigDBDuplicateRecord<br />**Hex**:<br />8004D231<br />**Number**:<br />-2147167695|Duplicate '{0}' with Value = ({1}) exists in MSCRM_CONFIG database|
> |**Name**:<br />ConfigDBObjectDoesNotExist<br />**Hex**:<br />8004D230<br />**Number**:<br />-2147167696|'{0}' with Value = ({1}) does not exist in MSCRM_CONFIG database|
> |**Name**:<br />ConfigMissingDescription<br />**Hex**:<br />80044197<br />**Number**:<br />-2147204713|Description must be specified.|
> |**Name**:<br />ConfigNullPrimaryKey<br />**Hex**:<br />80044196<br />**Number**:<br />-2147204714|Primary Key cannot be nullable.|
> |**Name**:<br />ConfigurationPageNotValidForSolution<br />**Hex**:<br />8004701D<br />**Number**:<br />-2147192803|The solution configuration page must exist within the solution it represents.|
> |**Name**:<br />ConfigureClaimsBeforeIfd<br />**Hex**:<br />8004D266<br />**Number**:<br />-2147167642|You must configure claims-based authentication before you can configure an Internet-facing deployment.|
> |**Name**:<br />ConfiguredUserIsDifferentThanSuppliedUser<br />**Hex**:<br />80044508<br />**Number**:<br />-2147203832|Configured user is different than supplied user.|
> |**Name**:<br />ConflictForOverriddenPropertiesEncountered<br />**Hex**:<br />80081010<br />**Number**:<br />-2146955248|This record can't be published. One of the properties that was changed for this record conflicts with its inherited version. Remove the conflicting property, and then try again.|
> |**Name**:<br />ConflictingProvisionTypes<br />**Hex**:<br />8004B02C<br />**Number**:<br />-2147176404|The service component {0} has conflicting provision types.|
> |**Name**:<br />ConnectionCannotBeEnabledOnThisEntity<br />**Hex**:<br />80048214<br />**Number**:<br />-2147188204|Connections cannot be enabled on this {0} entity with id {1}.|
> |**Name**:<br />ConnectionExists<br />**Hex**:<br />80048208<br />**Number**:<br />-2147188216|Connection already exists.|
> |**Name**:<br />ConnectionInvalidStartEndDate<br />**Hex**:<br />80048209<br />**Number**:<br />-2147188215|Start date / end date is invalid.|
> |**Name**:<br />ConnectionNotSupported<br />**Hex**:<br />80048213<br />**Number**:<br />-2147188205|The selected record does not support connections. You cannot add the connection.|
> |**Name**:<br />ConnectionObjectsMissing<br />**Hex**:<br />80048210<br />**Number**:<br />-2147188208|Both objects being connected are missing.|
> |**Name**:<br />ConnectionRoleNotValidForObjectType<br />**Hex**:<br />80048215<br />**Number**:<br />-2147188203|The record type {0} is not defined for use with the connection role {1}.|
> |**Name**:<br />ConnectionTimeOut<br />**Hex**:<br />80071024<br />**Number**:<br />-2147020764|Unable to copy the documents because the network connection timed out.  Please try again later or contact your system administrator.|
> |**Name**:<br />ConnectorNotEnabled<br />**Hex**:<br />80072600<br />**Number**:<br />-2147015168|Creation and editing of Connector is not enabled.|
> |**Name**:<br />ContactDoesNotExist<br />**Hex**:<br />80040503<br />**Number**:<br />-2147220221|Contact does not exist.|
> |**Name**:<br />ContactLoopBeingCreated<br />**Hex**:<br />8004050a<br />**Number**:<br />-2147220214|Creating this parental association would create a loop in Contacts hierarchy.|
> |**Name**:<br />ContactLoopExists<br />**Hex**:<br />80040509<br />**Number**:<br />-2147220215|Loop exists in the contacts hierarchy.|
> |**Name**:<br />ContextIsNull<br />**Hex**:<br />80060445<br />**Number**:<br />-2147089339|Error creating or updating Business Process: context cannot be null.|
> |**Name**:<br />ContractDetailDiscountAmount<br />**Hex**:<br />80044413<br />**Number**:<br />-2147204077|The contract's discount type does not support 'percentage' discounts.|
> |**Name**:<br />ContractDetailDiscountAmountAndPercent<br />**Hex**:<br />80044414<br />**Number**:<br />-2147204076|Both 'amount' and 'percentage' cannot be set.|
> |**Name**:<br />ContractDetailDiscountPercent<br />**Hex**:<br />80044412<br />**Number**:<br />-2147204078|The contract's discount type does not support 'amount' discounts.|
> |**Name**:<br />ContractInvalidAllotmentTypeCode<br />**Hex**:<br />80043205<br />**Number**:<br />-2147208699|The allotment type code is invalid.|
> |**Name**:<br />ContractInvalidBillToAddress<br />**Hex**:<br />8004320f<br />**Number**:<br />-2147208689|The bill-to address of the contract is invalid.|
> |**Name**:<br />ContractInvalidBillToCustomer<br />**Hex**:<br />80043210<br />**Number**:<br />-2147208688|The bill-to customer of the contract is invalid.|
> |**Name**:<br />ContractInvalidContract<br />**Hex**:<br />80043213<br />**Number**:<br />-2147208685|The contract is invalid.|
> |**Name**:<br />ContractInvalidContractTemplate<br />**Hex**:<br />80043211<br />**Number**:<br />-2147208687|The contract template is invalid.|
> |**Name**:<br />ContractInvalidCustomer<br />**Hex**:<br />8004320d<br />**Number**:<br />-2147208691|The customer of the contract is invalid.|
> |**Name**:<br />ContractInvalidDatesForRenew<br />**Hex**:<br />80043218<br />**Number**:<br />-2147208680|The start date / end date of this renewed contract can not overlap with any other invoiced / active contracts with the same contract number.|
> |**Name**:<br />ContractInvalidDiscount<br />**Hex**:<br />80044193<br />**Number**:<br />-2147204717|Discount cannot be greater than total price.|
> |**Name**:<br />ContractInvalidPrice<br />**Hex**:<br />80043215<br />**Number**:<br />-2147208683|The price is invalid.|
> |**Name**:<br />ContractInvalidServiceAddress<br />**Hex**:<br />8004320e<br />**Number**:<br />-2147208690|The service address of the contract is invalid.|
> |**Name**:<br />ContractInvalidStartEndDate<br />**Hex**:<br />80043202<br />**Number**:<br />-2147208702|Start date / end date or billing start date / billing end date is invalid.|
> |**Name**:<br />ContractInvalidState<br />**Hex**:<br />80043203<br />**Number**:<br />-2147208701|The state of the contract is invalid.|
> |**Name**:<br />ContractLineInvalidState<br />**Hex**:<br />80043204<br />**Number**:<br />-2147208700|The state of the contract line item is invalid.|
> |**Name**:<br />ContractNoLineItems<br />**Hex**:<br />8004320c<br />**Number**:<br />-2147208692|There are no contract line items for this contract.|
> |**Name**:<br />ContractTemplateDoesNotExist<br />**Hex**:<br />80043206<br />**Number**:<br />-2147208698|The contract template does not exist.|
> |**Name**:<br />ContractTemplateNoAbbreviation<br />**Hex**:<br />8004320b<br />**Number**:<br />-2147208693|Abbreviation can not be NULL.|
> |**Name**:<br />ControlIdIsNotUnique<br />**Hex**:<br />80060411<br />**Number**:<br />-2147089391|Control id {0} in the Xaml is not unique|
> |**Name**:<br />ControlIdIsNullOrEmpty<br />**Hex**:<br />80072344<br />**Number**:<br />-2147015868|Control id cannot be null or empty|
> |**Name**:<br />ConvertFetchDataSetError<br />**Hex**:<br />8004832e<br />**Number**:<br />-2147187922|An unexpected error occurred while processing the Fetch data set.|
> |**Name**:<br />ConvertReportToCrmError<br />**Hex**:<br />8004832d<br />**Number**:<br />-2147187923|An unexpected error occurred while converting supplied report to Dynamics 365 format.|
> |**Name**:<br />ConvertRuleActivateDeactivateByNonOwner<br />**Hex**:<br />8004F886<br />**Number**:<br />-2147157882|This Convert Rule Set cannot be activated or deactivated by someone who is not its owner.|
> |**Name**:<br />ConvertRuleAlreadyActive<br />**Hex**:<br />80060731<br />**Number**:<br />-2147088591|Selected ConvertRule is already in active state. Please select another record and try again|
> |**Name**:<br />ConvertRuleAlreadyInDraftState <br />**Hex**:<br />80060732<br />**Number**:<br />-2147088590|Selected ConvertRule is already in draft state. Please select another record and try again|
> |**Name**:<br />ConvertRuleInvalidAutoResponseSettings<br />**Hex**:<br />8004F879<br />**Number**:<br />-2147157895|Select an email template for an autoresponse or set the autoresponse option to No.|
> |**Name**:<br />ConvertRulePermissionToPerformAction<br />**Hex**:<br />80060733<br />**Number**:<br />-2147088589|You don't have the required permissions on ConvertRules and processes to perform this action.|
> |**Name**:<br />ConvertRuleQueueIdMissingForEmailSource<br />**Hex**:<br />8004F896<br />**Number**:<br />-2147157866|Queue value required. Provide a value for the queue.|
> |**Name**:<br />ConvertRuleResponseTemplateValidity<br />**Hex**:<br />80060730<br />**Number**:<br />-2147088592|Please select either a global or case template.|
> |**Name**:<br />CopyGenericError<br />**Hex**:<br />80071027<br />**Number**:<br />-2147020761|An error has occurred while copying files. Please try again later. If the problem persists, contact your system administrator.|
> |**Name**:<br />CopyNotAllowedForInternetMarketing<br />**Hex**:<br />80048474<br />**Number**:<br />-2147187596|Duplicating campaigns that have Internet Marketing Campaign Activities is not allowed|
> |**Name**:<br />CorruptedHiddensheetData<br />**Hex**:<br />800609B7<br />**Number**:<br />-2147087945|The hidden sheet data is corrupted.|
> |**Name**:<br />CouldNotDecryptOAuthToken<br />**Hex**:<br />8005F110<br />**Number**:<br />-2147094256|Yammer OAuth token could not be decrypted. Please try to reconfigure Yammer once again.|
> |**Name**:<br />CouldNotFindQueueItemInQueue<br />**Hex**:<br />80040524<br />**Number**:<br />-2147220188|Could not find any queue item associated with the Target in the specified SourceQueueId. Either the SourceQueueId or Target is invalid or the queue item does not exist.|
> |**Name**:<br />CouldNotObtainLockOnResource<br />**Hex**:<br />80044339<br />**Number**:<br />-2147204295|Database resource lock could not be obtained. For more information, see http://docs.microsoft.com/dynamics365/customer-engagement/customize/best-practices-workflow-processes#limit-the-number-of-workflows-that-update-the-same-entity|
> |**Name**:<br />CouldNotReadAccessToken<br />**Hex**:<br />8005F105<br />**Number**:<br />-2147094267|The system was not able to read users Yammer access token although a non-empty code was passed.|
> |**Name**:<br />CouldNotSetLocationTypeToOneNote<br />**Hex**:<br />80060905<br />**Number**:<br />-2147088123|Couldn't set location type of document location to OneNote.|
> |**Name**:<br />CountSpecifiedWithoutOrder<br />**Hex**:<br />8004E01F<br />**Number**:<br />-2147164129|The Data Description for the visualization is invalid as it does not specify an order node for the count attribute.|
> |**Name**:<br />CreatePropertyError<br />**Hex**:<br />8004F889<br />**Number**:<br />-2147157879|An error occurred while saving the {0} property.|
> |**Name**:<br />CreatePropertyInstanceError<br />**Hex**:<br />8004F890<br />**Number**:<br />-2147157872|An error occurred while saving the {0} property instance.|
> |**Name**:<br />CreatePublishedWorkflowDefinitionWorkflowDependency<br />**Hex**:<br />8004500A<br />**Number**:<br />-2147201014|Cannot create a workflow dependency for a published workflow definition.|
> |**Name**:<br />CreateRecurrenceRuleFailed<br />**Hex**:<br />8004E101<br />**Number**:<br />-2147163903|Cannot create the recurrence rule.|
> |**Name**:<br />CreateWorkflowActivationWorkflowDependency<br />**Hex**:<br />80045009<br />**Number**:<br />-2147201015|Cannot create a workflow dependency associated with a workflow activation.|
> |**Name**:<br />CreateWorkflowDependencyForPublishedTemplate<br />**Hex**:<br />80045019<br />**Number**:<br />-2147200999|Cannot create a workflow dependency for a published workflow template.|
> |**Name**:<br />CrmConstraintEvaluationError<br />**Hex**:<br />80040261<br />**Number**:<br />-2147220895|Crm constraint evaluation error occurred.|
> |**Name**:<br />CrmConstraintParsingError<br />**Hex**:<br />80040262<br />**Number**:<br />-2147220894|Crm constraint parsing error occurred.|
> |**Name**:<br />CrmExpressionBodyParsingError<br />**Hex**:<br />8004025e<br />**Number**:<br />-2147220898|Crm expression body parsing error occurred.|
> |**Name**:<br />CrmExpressionEvaluationError<br />**Hex**:<br />80040260<br />**Number**:<br />-2147220896|Crm expression evaluation error occurred.|
> |**Name**:<br />CrmExpressionParametersParsingError<br />**Hex**:<br />8004025f<br />**Number**:<br />-2147220897|Crm expression parameters parsing error occurred.|
> |**Name**:<br />CrmExpressionParsingError<br />**Hex**:<br />8004025d<br />**Number**:<br />-2147220899|Crm expression parsing error occurred.|
> |**Name**:<br />CrmHttpError<br />**Hex**:<br />8006088A<br />**Number**:<br />-2147088246|A failure occurred in Wep Api in Dynamics 365.|
> |**Name**:<br />CrmImpersonationError<br />**Hex**:<br />80040245<br />**Number**:<br />-2147220923|Error occurred in the Crm AutoReimpersonator.|
> |**Name**:<br />CrmLiveAddOnAddLicenseLimitReached<br />**Hex**:<br />8004B056<br />**Number**:<br />-2147176362|Your subscription has the maximum number of user licenses available.  For additional licenses, please contact our sales organization at 1-877-Dynamics 365-CHOICE (276-2464).|
> |**Name**:<br />CrmLiveAddOnAddStorageLimitReached<br />**Hex**:<br />8004B057<br />**Number**:<br />-2147176361|Your storage consumption has reached the maximum storage limit allotted to this environment. Trial environments are allocated with limited resources. If you are not using a trial environment, please contact support.|
> |**Name**:<br />CrmLiveAddOnDataChanged<br />**Hex**:<br />8004B05C<br />**Number**:<br />-2147176356|Due to recent changes you have made to your account, these changes cannot be made at this time.   Close this wizard, and try again later.  If the problem persists, please contact our sales organization at 1-877-Dynamics 365-CHOICE (276-2464).|
> |**Name**:<br />CrmLiveAddOnOrgInNoUpdateMode<br />**Hex**:<br />8004B059<br />**Number**:<br />-2147176359|Your changes cannot be processed at this time. Your organization is currently being updated.  No changes have been made to your account.  Close this wizard, and try again later.  If the problem persists, please contact our sales organization at 1-877-Dynamics 365-CHOICE (276-2464).|
> |**Name**:<br />CrmLiveAddOnRemoveStorageLimitReached<br />**Hex**:<br />8004B058<br />**Number**:<br />-2147176360|Your organization has the minimum amount of storage allowed.  You can remove only storage that has been added to your organization, and  is not being used.|
> |**Name**:<br />CrmLiveAddOnUnexpectedError<br />**Hex**:<br />8004B055<br />**Number**:<br />-2147176363|There was an error contacting the billing system.  Your request cannot be processed at this time.  No changes have been made to your account.  Close this wizard, and try again later.  If the problem persists, please contact our sales organization at 1-877-Dynamics 365-CHOICE (276-2464).|
> |**Name**:<br />CrmLiveCannotFindExternalMessageProvider<br />**Hex**:<br />8004B051<br />**Number**:<br />-2147176367|External Message Provider could not be located for queue item type of: {0}.|
> |**Name**:<br />CrmLiveDnsDomainAlreadyExists<br />**Hex**:<br />8004B048<br />**Number**:<br />-2147176376|Domain already exists in the DNS table.|
> |**Name**:<br />CrmLiveDnsDomainNotFound<br />**Hex**:<br />8004B047<br />**Number**:<br />-2147176377|Domain was not found in the DNS table.|
> |**Name**:<br />CrmLiveDuplicateWindowsLiveId<br />**Hex**:<br />8004B046<br />**Number**:<br />-2147176378|A user with this username already exists.|
> |**Name**:<br />CrmLiveExecuteCustomCodeDisabled<br />**Hex**:<br />8004B063<br />**Number**:<br />-2147176349|Execution of custom code feature for this organization is disabled.|
> |**Name**:<br />CrmLiveGenericError<br />**Hex**:<br />8004B000<br />**Number**:<br />-2147176448|An error has occurred while processing your request.|
> |**Name**:<br />CrmLiveInternalProvisioningError<br />**Hex**:<br />8004B003<br />**Number**:<br />-2147176445|An unexpected error happened in the provisioning system.|
> |**Name**:<br />CrmLiveInvalidEmail<br />**Hex**:<br />8004B05D<br />**Number**:<br />-2147176355|Invalid email address entered.|
> |**Name**:<br />CrmLiveInvalidExternalMessageData<br />**Hex**:<br />8004B052<br />**Number**:<br />-2147176366|External Message Data has some invalid data.  Data: {0} External Message: {1}|
> |**Name**:<br />CrmLiveInvalidInvoicingAccountNumber<br />**Hex**:<br />8004B05B<br />**Number**:<br />-2147176357|This Invoicing Account Number is not valid because it contains an invalid character.|
> |**Name**:<br />CrmLiveInvalidPhone<br />**Hex**:<br />8004B05E<br />**Number**:<br />-2147176354|Invalid phone number entered.|
> |**Name**:<br />CrmLiveInvalidQueueItemSchedule<br />**Hex**:<br />8004B039<br />**Number**:<br />-2147176391|The QueueItem has an invalid schedule of start time {0} and end time {1}.|
> |**Name**:<br />CrmLiveInvalidSetupParameter<br />**Hex**:<br />8004B005<br />**Number**:<br />-2147176443|The parameter to Dynamics 365 Online Setup is incorrect or not specified.|
> |**Name**:<br />CrmLiveInvalidTaxId<br />**Hex**:<br />8004B064<br />**Number**:<br />-2147176348|Invalid TaxId entered.|
> |**Name**:<br />CrmLiveInvalidZipCode<br />**Hex**:<br />8004B05F<br />**Number**:<br />-2147176353|Invalid zip code entered.|
> |**Name**:<br />CrmLiveInvoicingAccountIdMissing<br />**Hex**:<br />8004B045<br />**Number**:<br />-2147176379|Invoicing Account Number (SAP Id) cannot be empty for an invoicing sku.|
> |**Name**:<br />CrmLiveMissingActiveDirectoryGroup<br />**Hex**:<br />8004B002<br />**Number**:<br />-2147176446|The specified Active Directory Group does not exist.|
> |**Name**:<br />CrmLiveMissingServerRolesInScaleGroup<br />**Hex**:<br />8004B007<br />**Number**:<br />-2147176441|The scalegroup is missing some required server roles. 1 Witness Server and 2 Sql Servers are required for Provisioning.|
> |**Name**:<br />CrmLiveMonitoringOrganizationExistsInScaleGroup<br />**Hex**:<br />8004B026<br />**Number**:<br />-2147176410|Only one monitoring organization is allowed in a scalegroup.|
> |**Name**:<br />CrmLiveMultipleWitnessServersInScaleGroup<br />**Hex**:<br />8004B006<br />**Number**:<br />-2147176442|The ScaleGroup has multiple witness servers specified. There should be only 1 witness server in a scale group.|
> |**Name**:<br />CrmLiveOrganizationDeleteFailed<br />**Hex**:<br />8004B02E<br />**Number**:<br />-2147176402|An error has occurred when deleting the organization.|
> |**Name**:<br />CrmLiveOrganizationDetailsNotFound<br />**Hex**:<br />8004B030<br />**Number**:<br />-2147176400|Unable to find organization details.|
> |**Name**:<br />CrmLiveOrganizationDisableFailed<br />**Hex**:<br />8004B054<br />**Number**:<br />-2147176364|Disabling Organization Failed.|
> |**Name**:<br />CrmLiveOrganizationEnableFailed<br />**Hex**:<br />8004B053<br />**Number**:<br />-2147176365|Enabling Organization Failed.|
> |**Name**:<br />CrmLiveOrganizationFriendlyNameTooLong<br />**Hex**:<br />8004B032<br />**Number**:<br />-2147176398|The organization name provided is too long.|
> |**Name**:<br />CrmLiveOrganizationFriendlyNameTooShort<br />**Hex**:<br />8004B031<br />**Number**:<br />-2147176399|The organization name provided is too short.|
> |**Name**:<br />CrmLiveOrganizationProvisioningFailed<br />**Hex**:<br />8004B001<br />**Number**:<br />-2147176447|An error has occurred when provisioning the organization.|
> |**Name**:<br />CrmLiveOrganizationUniqueNameInvalid<br />**Hex**:<br />8004B035<br />**Number**:<br />-2147176395|The unique name provided is not valid.|
> |**Name**:<br />CrmLiveOrganizationUniqueNameReserved<br />**Hex**:<br />8004B036<br />**Number**:<br />-2147176394|The unique name is already reserved.|
> |**Name**:<br />CrmLiveOrganizationUniqueNameTooLong<br />**Hex**:<br />8004B034<br />**Number**:<br />-2147176396|The unique name provided is too long.|
> |**Name**:<br />CrmLiveOrganizationUniqueNameTooShort<br />**Hex**:<br />8004B033<br />**Number**:<br />-2147176397|The unique name provided is too short.|
> |**Name**:<br />CrmLiveOrganizationUpgradeFailed<br />**Hex**:<br />8004B014<br />**Number**:<br />-2147176428|Upgrade Of Crm Organization Failed.|
> |**Name**:<br />CrmLiveQueueItemDoesNotExist<br />**Hex**:<br />8004B004<br />**Number**:<br />-2147176444|The specified queue item does not exist in the queue. It may have been deleted or its ID may not have been specified correctly|
> |**Name**:<br />CrmLiveQueueItemTimeInPast<br />**Hex**:<br />8004B040<br />**Number**:<br />-2147176384|A QueueItem cannot be scheduled to start or end in the past.|
> |**Name**:<br />CrmLiveRegisterCustomCodeDisabled<br />**Hex**:<br />8004B062<br />**Number**:<br />-2147176350|Registration of custom code feature for this organization is disabled.|
> |**Name**:<br />CrmLiveServerCannotHaveWitnessAndDataServerRoles<br />**Hex**:<br />8004B008<br />**Number**:<br />-2147176440|A server cannot have both Witness and Data Server Roles.|
> |**Name**:<br />CrmLiveSupportOrganizationExistsInScaleGroup<br />**Hex**:<br />8004B025<br />**Number**:<br />-2147176411|Only one support organization is allowed in a scalegroup.|
> |**Name**:<br />CrmLiveUnknownCategory<br />**Hex**:<br />8004B05A<br />**Number**:<br />-2147176358|This Category specified is not valid.|
> |**Name**:<br />CrmLiveUnknownSku<br />**Hex**:<br />8004B041<br />**Number**:<br />-2147176383|This Sku specified is not valid.|
> |**Name**:<br />CrmMalformedExpressionError<br />**Hex**:<br />8004025c<br />**Number**:<br />-2147220900|Crm malformed expression error occurred.|
> |**Name**:<br />CrmQueryExpressionNotInitialized<br />**Hex**:<br />8004024d<br />**Number**:<br />-2147220915|The QueryExpression has not been initialized. Please use the constructor that takes in the entity name to create a correctly initialized instance|
> |**Name**:<br />CrmSecurityError<br />**Hex**:<br />80040256<br />**Number**:<br />-2147220906|A failure occurred in CrmSecurity.|
> |**Name**:<br />CrmSQLCharLengthTooLong<br />**Hex**:<br />80073001<br />**Number**:<br />-2147012607|A validation error occurred. A string value provided is too long.|
> |**Name**:<br />CrmSqlGovernorDatabaseRequestDenied<br />**Hex**:<br />8004A001<br />**Number**:<br />-2147180543|The server is busy and the request was not completed. Try again later.|
> |**Name**:<br />CrmSQLNetworkingError<br />**Hex**:<br />80073000<br />**Number**:<br />-2147012608|A networking error caused this operation to fail. Please try again.|
> |**Name**:<br />CrmSQLUniqueIndexOrConstraintViolation<br />**Hex**:<br />80073002<br />**Number**:<br />-2147012606|The operation attempted to insert a duplicate value for an attribute with a unique constraint.|
> |**Name**:<br />CRMUserDoesNotExist<br />**Hex**:<br />80040354<br />**Number**:<br />-2147220652|No Microsoft Dynamics 365 user exists with the specified domain name and user ID|
> |**Name**:<br />CrossEntityRelationshipInvalidOperation<br />**Hex**:<br />80092006<br />**Number**:<br />-2146885626|Invalid cross-entity stage transition. Specified relationship cannot be modified.|
> |**Name**:<br />CurrencyCannotBeNullDueToNonNullMoneyFields<br />**Hex**:<br />80048cfb<br />**Number**:<br />-2147185413|The currency cannot be null.|
> |**Name**:<br />CurrencyFieldMissing<br />**Hex**:<br />8004E026<br />**Number**:<br />-2147164122|Record currency is required to calculate rollup field of type currency. Provide a currency and try again.|
> |**Name**:<br />CurrencyNotEqual<br />**Hex**:<br />80048cea<br />**Number**:<br />-2147185430|The currency of the {0} does not match the currency of the {1}.|
> |**Name**:<br />CurrencyRequiredForDiscountTypeAmount<br />**Hex**:<br />80048cf7<br />**Number**:<br />-2147185417|The currency cannot be null for discount type amount.|
> |**Name**:<br />CustomActionMustBeMarked<br />**Hex**:<br />80060381<br />**Number**:<br />-2147089535|Custom Action must be marked ‘As a Business Process Flow action step’ to use as BPF action step.|
> |**Name**:<br />CustomActivityCannotBeMailMergeEnabled<br />**Hex**:<br />8004F124<br />**Number**:<br />-2147159772|A custom entity defined as an activity already cannot have MailMerge enabled.|
> |**Name**:<br />CustomActivityInvalid<br />**Hex**:<br />8004501D<br />**Number**:<br />-2147200995|Invalid custom activity.|
> |**Name**:<br />CustomActivityMustHaveOfflineAvailability<br />**Hex**:<br />8004F122<br />**Number**:<br />-2147159774|A custom entity defined as an activity must have Offline Availability.|
> |**Name**:<br />CustomControlsDependentPropertyConfiguration<br />**Hex**:<br />80160002<br />**Number**:<br />-2146041854|Property "{0}" can only be configured after property "{1}" has been assigned a value.|
> |**Name**:<br />CustomControlsImportError<br />**Hex**:<br />80160000<br />**Number**:<br />-2146041856|An error occurred while importing Custom Controls. Try importing this solution again.|
> |**Name**:<br />CustomControlsPropertySetConfiguration<br />**Hex**:<br />80160003<br />**Number**:<br />-2146041853|Property "{0}" can only be configured after Corresponding DataSet "{1}" view has been assigned a value.|
> |**Name**:<br />CustomerIsInactive<br />**Hex**:<br />80040517<br />**Number**:<br />-2147220201|An inactive customer cannot be set as the parent of an object.|
> |**Name**:<br />CustomerOpportunityRoleExists<br />**Hex**:<br />80048202<br />**Number**:<br />-2147188222|Customer opportunity role exists.|
> |**Name**:<br />CustomerRelationshipCannotBeDeleted<br />**Hex**:<br />8004847d<br />**Number**:<br />-2147187587|This relationship {1} is required by the {0} attribute and can't be deleted. To delete this relationship, first delete the lookup attribute.|
> |**Name**:<br />CustomerRelationshipExists<br />**Hex**:<br />80048201<br />**Number**:<br />-2147188223|Customer relationship already exists.|
> |**Name**:<br />CustomImageAttributeOnlyAllowedOnCustomEntity<br />**Hex**:<br />80048531<br />**Number**:<br />-2147187407|A custom image attribute can only be added to a custom entity.|
> |**Name**:<br />CustomOperationNotActivated<br />**Hex**:<br />80045052<br />**Number**:<br />-2147200942|Process action associated with this process is not activated.|
> |**Name**:<br />CustomParentingSystemNotSupported<br />**Hex**:<br />80047102<br />**Number**:<br />-2147192574|A custom entity can not have a parental relationship to a system entity|
> |**Name**:<br />CustomPeriodGoalHavingExtraInfo<br />**Hex**:<br />80044904<br />**Number**:<br />-2147202812|For a goal of custom period type, fiscal year and fiscal period attributes must be left blank.|
> |**Name**:<br />CustomPeriodGoalMissingInfo<br />**Hex**:<br />80044907<br />**Number**:<br />-2147202809|For a goal of custom period type, goalstartdate and goalenddate attributes must have data.|
> |**Name**:<br />CustomReflexiveRelationshipNotAllowedForEntity<br />**Hex**:<br />8004432C<br />**Number**:<br />-2147204308|This entity is not valid for a custom reflexive relationship|
> |**Name**:<br />CustomWorkflowActivitiesNotSupported<br />**Hex**:<br />80045051<br />**Number**:<br />-2147200943|Custom Workflow Activities are not enabled.|
> |**Name**:<br />CyclicalRelationship<br />**Hex**:<br />80047004<br />**Number**:<br />-2147192828|The specified relationship will result in a cycle.|
> |**Name**:<br />CyclicDependency<br />**Hex**:<br />80071156<br />**Number**:<br />-2147020458|Cyclic component dependency detected. Please check the exception for more details. Fix the invalid dependencies and try the operation one more time. Detaisl: {0}|
> |**Name**:<br />CyclicReferencesNotSupported<br />**Hex**:<br />8004417F<br />**Number**:<br />-2147204737|The input contains a cyclic reference, which is not supported.|
> |**Name**:<br />DatabaseCallsBlockedFailure<br />**Hex**:<br />80072401<br />**Number**:<br />-2147015679|This invocation may lead to calls do Database which is not allowed.|
> |**Name**:<br />DatacenterNotAvailable<br />**Hex**:<br />8004B065<br />**Number**:<br />-2147176347|This datacenter endpoint is not currently available for this organization.|
> |**Name**:<br />DataColumnsNumberMismatch<br />**Hex**:<br />80040345<br />**Number**:<br />-2147220667|The number of fields differs from the number of column headings.|
> |**Name**:<br />DataEngineQueryThrottling<br />**Hex**:<br />80048544<br />**Number**:<br />-2147187388|This query cannot be executed because it conflicts with throttling optimization.|
> |**Name**:<br />DatafieldNameShouldBeNull<br />**Hex**:<br />8006041b<br />**Number**:<br />-2147089381|ActionStep {0} references invalid DataFieldName {1}.|
> |**Name**:<br />DataMigrationManagerMandatoryUpdatesNotInstalled<br />**Hex**:<br />80044336<br />**Number**:<br />-2147204298|First-time configuration of the Data Migration Manager has been canceled. You will not be able to use the Data Migration Manager until configuration is completed.|
> |**Name**:<br />DataMigrationManagerUnknownProblem<br />**Hex**:<br />80044333<br />**Number**:<br />-2147204301|The Data Migration Manager encountered an unknown problem and cannot continue. To try again, restart the Data Migration Manager.|
> |**Name**:<br />DatasheetNotAvailable<br />**Hex**:<br />800609B5<br />**Number**:<br />-2147087947|The data sheet is not available.|
> |**Name**:<br />DataSourceInitializeFailedErrorCode<br />**Hex**:<br />8005F210<br />**Number**:<br />-2147094000|Try this action again. If the problem continues, check the {0} for solutions or contact your organization's {#Brand_CRM} Administrator. Finally, you can contact {1}.|
> |**Name**:<br />DataSourceOfflineErrorCode<br />**Hex**:<br />8005F211<br />**Number**:<br />-2147093999|This operation failed because you're offline. Reconnect and try again.|
> |**Name**:<br />DataSourceProhibited<br />**Hex**:<br />8004830D<br />**Number**:<br />-2147187955|A non fetch based data source is not permitted on this report|
> |**Name**:<br />DataStoreKeyNotFoundErrorCode<br />**Hex**:<br />8005F21d<br />**Number**:<br />-2147093987|Not in local store with key '{0}'|
> |**Name**:<br />DataSyncNoContent<br />**Hex**:<br />80072512<br />**Number**:<br />-2147015406|No data sync content|
> |**Name**:<br />DataSyncRequestAccepted<br />**Hex**:<br />80072511<br />**Number**:<br />-2147015407|Data sync request accepted|
> |**Name**:<br />DataTableNotAvailable<br />**Hex**:<br />800609B0<br />**Number**:<br />-2147087952|The original data table has been deleted or renamed.|
> |**Name**:<br />DataTypeMismatchForLinkedAttribute<br />**Hex**:<br />8004F0FC<br />**Number**:<br />-2147159812|Data type mismatch found for linked attribute.|
> |**Name**:<br />DateTimeFormatFailed<br />**Hex**:<br />8004025a<br />**Number**:<br />-2147220902|Failed to produce a formatted datetime value.|
> |**Name**:<br />DecimalValueOutOfRange<br />**Hex**:<br />80044330<br />**Number**:<br />-2147204304|A validation error occurred. A decimal value provided is outside of the allowed values for this attribute.|
> |**Name**:<br />DecoupleChildEntity<br />**Hex**:<br />80048206<br />**Number**:<br />-2147188218|Cannot decouple a child entity.|
> |**Name**:<br />DecoupleUserOwnedEntity<br />**Hex**:<br />80048207<br />**Number**:<br />-2147188217|Can only decouple user owned entities.|
> |**Name**:<br />DecreasingDaysWillDeleteOlderData<br />**Hex**:<br />80060992<br />**Number**:<br />-2147087982|Decreasing the number of days will delete mobile offline data older than the number of days specified.|
> |**Name**:<br />DefaultSiteCollectionUrlChanged<br />**Hex**:<br />8004F100<br />**Number**:<br />-2147159808|Default site collection url has been changed this organization after this operation was created.|
> |**Name**:<br />DefaultSiteMapDeleteFailure<br />**Hex**:<br />80048070<br />**Number**:<br />-2147188624|Cannot delete default site map.|
> |**Name**:<br />DelegatedAdminUserCannotBeCreateNorUpdated<br />**Hex**:<br />80041d67<br />**Number**:<br />-2147213977|The delegated admin user cannot be updated|
> |**Name**:<br />DeleteActiveWorkflowTemplateDependency<br />**Hex**:<br />8004501A<br />**Number**:<br />-2147200998|Cannot delete workflow dependency from a published workflow template .|
> |**Name**:<br />DeletePublishedWorkflowDefinitionWorkflowDependency<br />**Hex**:<br />80045006<br />**Number**:<br />-2147201018|Cannot delete a workflow dependency for a published workflow definition.|
> |**Name**:<br />DeleteWorkflowActivation<br />**Hex**:<br />80045004<br />**Number**:<br />-2147201020|Cannot delete a workflow activation.|
> |**Name**:<br />DeleteWorkflowActivationWorkflowDependency<br />**Hex**:<br />80045005<br />**Number**:<br />-2147201019|Cannot delete a workflow dependency associated with a workflow activation.|
> |**Name**:<br />DeleteWorkflowActiveDefinition<br />**Hex**:<br />8004500F<br />**Number**:<br />-2147201009|Cannot delete an active workflow definition.|
> |**Name**:<br />DeleteWorkflowActiveTemplate<br />**Hex**:<br />8004501C<br />**Number**:<br />-2147200996|Cannot delete an active workflow template.|
> |**Name**:<br />DelveActionHubAttributeMissingInResponseException<br />**Hex**:<br />80071002<br />**Number**:<br />-2147020798|Attribute not present in exchange oData response.|
> |**Name**:<br />DelveActionHubAuthorizationFailureException<br />**Hex**:<br />80071007<br />**Number**:<br />-2147020793|You don’t have the proper Office 365 license to view actions. Please contact your system administrator.|
> |**Name**:<br />DelveActionHubDisabledError<br />**Hex**:<br />80071000<br />**Number**:<br />-2147020800|Delve action hub feature is not enabled.|
> |**Name**:<br />DelveActionHubInvalidResponseFormatException<br />**Hex**:<br />80071004<br />**Number**:<br />-2147020796|Invalid response format.|
> |**Name**:<br />DelveActionHubInvalidStateCodeException<br />**Hex**:<br />80071003<br />**Number**:<br />-2147020797|Invalid state code passed in expression.|
> |**Name**:<br />DelveActionHubResponseRetievalFailureException<br />**Hex**:<br />80071005<br />**Number**:<br />-2147020795|Error while fetching actions from Exchange.|
> |**Name**:<br />DelveActionHubS2SSetupFailureException<br />**Hex**:<br />80071008<br />**Number**:<br />-2147020792|Server to Server Authentication with Exchange for Delve Action Hub is not set up.|
> |**Name**:<br />DependencyAlreadyExists<br />**Hex**:<br />8004F01A<br />**Number**:<br />-2147160038|A {0} dependency already exists between {1}({2}) and {3}({4}).  Cannot also create {5} dependency.|
> |**Name**:<br />DependencyTableNotEmpty<br />**Hex**:<br />8004F01B<br />**Number**:<br />-2147160037|The dependency table must be empty for initialization to complete successfully.|
> |**Name**:<br />DependencyTrackingClosed<br />**Hex**:<br />8004F025<br />**Number**:<br />-2147160027|Invalid attempt to process a dependency after the current transaction context has been closed.|
> |**Name**:<br />DeploymentServiceCannotChangeStateForDeploymentService<br />**Hex**:<br />8004D262<br />**Number**:<br />-2147167646|You cannot change the state of this server because it contains the Deployment Service server role.|
> |**Name**:<br />DeploymentServiceCannotDeleteOperationInProgress<br />**Hex**:<br />8004D265<br />**Number**:<br />-2147167643|The Deployment Service cannot delete the specified operation because it is currently in progress.|
> |**Name**:<br />DeploymentServiceNotAllowOperation<br />**Hex**:<br />8004D261<br />**Number**:<br />-2147167647|Deployment Service for {0} does not allow {1} operation.|
> |**Name**:<br />DeploymentServiceNotAllowSetToThisState<br />**Hex**:<br />8004D260<br />**Number**:<br />-2147167648|Deployment Service for {0} allows the state Enabled or Disabled. Cannot set state to {1}.|
> |**Name**:<br />DeploymentServiceOperationIdentifierNotFound<br />**Hex**:<br />8004D264<br />**Number**:<br />-2147167644|The Deployment Service could not find a deferred operation having the specified identifier.|
> |**Name**:<br />DeploymentServiceRequestValidationFailure<br />**Hex**:<br />8004D263<br />**Number**:<br />-2147167645|The Deployment Service cannot process the request because one or more validation checks failed.|
> |**Name**:<br />DeprecatedFormActivation<br />**Hex**:<br />8004F662<br />**Number**:<br />-2147158430|This form has been deprecated in the previous release and cannot be used anymore. Please migrate your changes to a different form. Deprecated forms will be removed from the system in the future.|
> |**Name**:<br />DeprecatedMobileFormsCreation<br />**Hex**:<br />8004F667<br />**Number**:<br />-2147158425|Mobile forms have been deprecated. Cannot create new mobile express forms.|
> |**Name**:<br />DeprecatedMobileFormsEdit<br />**Hex**:<br />8004F668<br />**Number**:<br />-2147158424|Mobile forms have been deprecated. Cannot open mobile forms editor.|
> |**Name**:<br />DeprovisionRIAccessNotAllowed<br />**Hex**:<br />80044274<br />**Number**:<br />-2147204492|Relationship Insights can only be turned off by a system administrator.|
> |**Name**:<br />DesignerAccessDenied<br />**Hex**:<br />80050100<br />**Number**:<br />-2147155712|You do not have enough privileges to perform the requested operation. For more information, contact your administrator.|
> |**Name**:<br />DesignerInvalidParameter<br />**Hex**:<br />80050101<br />**Number**:<br />-2147155711|The {0} provided is incorrect or missing. Please try again with the correct {1}.|
> |**Name**:<br />DestinationFolderNotExists<br />**Hex**:<br />80071022<br />**Number**:<br />-2147020766|Unable to copy the documents. The destination document location no longer exists.|
> |**Name**:<br />DialogNameCannotBeNull<br />**Hex**:<br />80060873<br />**Number**:<br />-2147088269|"DialogName cannot be null for type Dialog|
> |**Name**:<br />DisabledCRMAddinLoadFailure<br />**Hex**:<br />80044202<br />**Number**:<br />-2147204606|An error occurred loading Microsoft Dynamics 365 functionality. Try restarting Outlook. Contact your system administrator if errors persist.|
> |**Name**:<br />DisabledCRMClientVersionHigher<br />**Hex**:<br />80044204<br />**Number**:<br />-2147204604|The Microsoft Dynamics 365 server needs to be upgraded before Microsoft Dynamics 365 client can be used. Contact your system administrator for assistance.|
> |**Name**:<br />DisabledCRMClientVersionLower<br />**Hex**:<br />80044203<br />**Number**:<br />-2147204605|You're running a version of Microsoft Dynamics 365 for Outlook that is not supported for offline mode with this Microsoft Dynamics 365 organization {0}. You'll need to upgrade to a compatible version of Dynamics 365 for Outlook. Make sure your current version of Dynamics 365 for Outlook is supported for upgrading to the compatible version.|
> |**Name**:<br />DisabledCRMGoingOffline<br />**Hex**:<br />80044200<br />**Number**:<br />-2147204608|Microsoft Dynamics 365 functionality is not available while Offline Synchronization is occuring|
> |**Name**:<br />DisabledCRMGoingOnline<br />**Hex**:<br />80044201<br />**Number**:<br />-2147204607|Microsoft Dynamics 365 functionality is not available while Online Synchronization is occuring|
> |**Name**:<br />DisabledCRMOnlineCrmNotAvailable<br />**Hex**:<br />80044206<br />**Number**:<br />-2147204602|Microsoft Dynamics 365 server is not available|
> |**Name**:<br />DisabledCRMPostOfflineUpgrade<br />**Hex**:<br />80044205<br />**Number**:<br />-2147204603|Microsoft Dynamics 365 functionality is not available until the Microsoft Dynamics 365 client is taken back online|
> |**Name**:<br />DisableRIFeatureNotAllowed<br />**Hex**:<br />80044280<br />**Number**:<br />-2147204480|You need system administrator privileges to turn Relationship Insights off for your organization.|
> |**Name**:<br />DiscountAmount<br />**Hex**:<br />80043b20<br />**Number**:<br />-2147206368|The discount type does not support 'percentage' discounts.|
> |**Name**:<br />DiscountAmountAndPercent<br />**Hex**:<br />80043b1f<br />**Number**:<br />-2147206369|Both 'amount' and 'percentage' cannot be set.|
> |**Name**:<br />DiscountPercent<br />**Hex**:<br />80043b21<br />**Number**:<br />-2147206367|The discount type does not support 'amount' discounts.|
> |**Name**:<br />DiscountRangeOverlap<br />**Hex**:<br />80043b02<br />**Number**:<br />-2147206398|The new quantities overlap the range covered by existing quantities.|
> |**Name**:<br />DiscountTypeAndPriceLevelCurrencyNotEqual<br />**Hex**:<br />80048cf8<br />**Number**:<br />-2147185416|The currency of the discount needs to match the currency of the price list for discount type amount.|
> |**Name**:<br />DiskSpaceNotEnough<br />**Hex**:<br />80050124<br />**Number**:<br />-2147155676|There is not enough space in the Temp Folder.|
> |**Name**:<br />DistributeListAssociatedVary<br />**Hex**:<br />80048453<br />**Number**:<br />-2147187629|This campaign activity cannot be distributed. Mail merge activities can be done only on marketing lists that are all the same record type. For this campaign activity, remove marketing lists so that the remaining ones are the same record type, and then try again.|
> |**Name**:<br />DistributeNoListAssociated<br />**Hex**:<br />80048454<br />**Number**:<br />-2147187628|This campaign activity cannot be distributed. No marketing lists are associated with it. Add at least one marketing list and try again.|
> |**Name**:<br />DocumentManagementDisabled<br />**Hex**:<br />8004F0FF<br />**Number**:<br />-2147159809|Document Management has been disabled for this organization.|
> |**Name**:<br />DocumentManagementDisabledForEmail<br />**Hex**:<br />80050010<br />**Number**:<br />-2147155952|Document Management must be enabled on the Email entity in order to follow attachments. Please contact your administrator to enable Document Management.|
> |**Name**:<br />DocumentManagementDisabledOnEntity<br />**Hex**:<br />80060908<br />**Number**:<br />-2147088120|You must enable document management for this Entity in order to enable OneNote integration.|
> |**Name**:<br />DocumentManagementIsDisabled<br />**Hex**:<br />8004F312<br />**Number**:<br />-2147159278|Document Management is not enabled for this Organization.|
> |**Name**:<br />DocumentManagementIsDisabledOnEntity<br />**Hex**:<br />80071011<br />**Number**:<br />-2147020783|You must enable document management for this Entity in order to enable Document Recommendations.|
> |**Name**:<br />DocumentManagementNotEnabledNoPrimaryField<br />**Hex**:<br />8004F313<br />**Number**:<br />-2147159277|Document management could not be enabled because a primary field is not defined for this entity with name {0} and id {1}.|
> |**Name**:<br />DocumentRecommendationsFCBOff<br />**Hex**:<br />80071019<br />**Number**:<br />-2147020775|The document suggestions feature is not enabled.|
> |**Name**:<br />DocumentTemplateFeatureNotEnabled<br />**Hex**:<br />800608C9<br />**Number**:<br />-2147088183|Document template feature is not enabled.|
> |**Name**:<br />DocxExportGeneratingWordFailed<br />**Hex**:<br />800608CD<br />**Number**:<br />-2147088179|An error occurred while generating the Word document. Please try again.|
> |**Name**:<br />DocxValidationFailed<br />**Hex**:<br />800608CE<br />**Number**:<br />-2147088178|The upload failed because the selected file is not consistent with the template layout. Please try again after selecting a file with the template layout.|
> |**Name**:<br />DoNotTrackItem<br />**Hex**:<br />80044228<br />**Number**:<br />-2147204568|Selected item will not be tracked.|
> |**Name**:<br />DownloadAllEntityRecordsChangedOrCreatedWithinTheseDays<br />**Hex**:<br />8006098F<br />**Number**:<br />-2147087985|Download all entity records changed or created within this number of days.|
> |**Name**:<br />DownloadRelatedDataOnlyMustHaveRelationship<br />**Hex**:<br />80071140<br />**Number**:<br />-2147020480|The entity '{0}' in profile '{1}' is configured with the filter download related data only, however there are no relationships specified for this entity in profile item associations. If an entity is set to download related data only you must specify a profile item association to this entity.|
> |**Name**:<br />DraftBundleToProduct<br />**Hex**:<br />8004F994<br />**Number**:<br />-2147157612|You can only add products to a draft bundle.|
> |**Name**:<br />DuplicateAliasFound<br />**Hex**:<br />8004E00B<br />**Number**:<br />-2147164149|Data Description is invalid. Duplicate alias found.|
> |**Name**:<br />DuplicateApplicationUser<br />**Hex**:<br />8004F511<br />**Number**:<br />-2147158767|You are attempting to create an Application ID = {0} that already exists.|
> |**Name**:<br />DuplicateAppModuleUniqueName<br />**Hex**:<br />8005011F<br />**Number**:<br />-2147155681|The name you entered is already in use.|
> |**Name**:<br />DuplicateAttributePhysicalName<br />**Hex**:<br />80060304<br />**Number**:<br />-2147089660|Attribute {0} already exists for entity {1}.|
> |**Name**:<br />DuplicateAttributeSchemaName<br />**Hex**:<br />80047013<br />**Number**:<br />-2147192813|An attribute with the specified name already exists|
> |**Name**:<br />DuplicateChannelPropertyName<br />**Hex**:<br />800608F1<br />**Number**:<br />-2147088143|A channel property with the specified name already exists. You can't create another one.|
> |**Name**:<br />DuplicateCheckNotEnabled<br />**Hex**:<br />80048412<br />**Number**:<br />-2147187694|Duplicate detection is not enabled. To enable duplicate detection, click Settings, click Data Management, and then click Duplicate Detection Settings.|
> |**Name**:<br />DuplicateCheckNotSupportedOnEntity<br />**Hex**:<br />80048410<br />**Number**:<br />-2147187696|Duplicate detection is not supported on this record type.|
> |**Name**:<br />DuplicateComponentInSolutionXml<br />**Hex**:<br />80071153<br />**Number**:<br />-2147020461|Duplicate Component is present in the XML.|
> |**Name**:<br />DuplicateDetectionNotSupportedOnAttributeType<br />**Hex**:<br />80048430<br />**Number**:<br />-2147187664|The rule condition cannot be created or updated because duplicate detection is not supported on the data type of the selected attribute.|
> |**Name**:<br />DuplicateDetectionRulesWereUnpublished<br />**Hex**:<br />8004F039<br />**Number**:<br />-2147160007|The duplicate detection rules for this entity have been unpublished due to possible modifications to the entity.|
> |**Name**:<br />DuplicateDetectionTemplateNotFound<br />**Hex**:<br />80048424<br />**Number**:<br />-2147187676|Microsoft Dynamics 365 could not retrieve the e-mail notification template.|
> |**Name**:<br />DuplicateDisplayCollectionName<br />**Hex**:<br />80047012<br />**Number**:<br />-2147192814|An object with the specified display collection name already exists.|
> |**Name**:<br />DuplicateDisplayName<br />**Hex**:<br />80047011<br />**Number**:<br />-2147192815|An object with the specified display name already exists.|
> |**Name**:<br />DuplicatedJobId<br />**Hex**:<br />80071152<br />**Number**:<br />-2147020462|Parameter ImportJobId must be unique.|
> |**Name**:<br />DuplicatedJobIdDueToConcurrency<br />**Hex**:<br />80071155<br />**Number**:<br />-2147020459|Cannot create the solution job using the supplied JobId ({0}) as it is already in use. This may indicate that another solution operation is progress. Please try again later.|
> |**Name**:<br />DuplicatedPrivilege<br />**Hex**:<br />8004140f<br />**Number**:<br />-2147216369|Privilege {0} is duplicated.|
> |**Name**:<br />DuplicateFileNamesInZip<br />**Hex**:<br />80048484<br />**Number**:<br />-2147187580|Two or more files have the same name. File names must be unique.|
> |**Name**:<br />DuplicateGroupByFound<br />**Hex**:<br />8004E01B<br />**Number**:<br />-2147164133|Data Description is invalid. Same attribute cannot be used as a group by more than once.|
> |**Name**:<br />DuplicateHeaderColumn<br />**Hex**:<br />80040338<br />**Number**:<br />-2147220680|A duplicate column heading exists.|
> |**Name**:<br />DuplicateIsoCurrencyCode<br />**Hex**:<br />80048cf3<br />**Number**:<br />-2147185421|Cannot insert duplicate currency record. Currency with the same currency code already exist in the system.|
> |**Name**:<br />DuplicateLookupFound<br />**Hex**:<br />80040352<br />**Number**:<br />-2147220654|A duplicate lookup reference was found|
> |**Name**:<br />DuplicateMapName<br />**Hex**:<br />80048443<br />**Number**:<br />-2147187645|A data map with the specified name already exists.|
> |**Name**:<br />DuplicateName<br />**Hex**:<br />80047010<br />**Number**:<br />-2147192816|An object with the specified name already exists|
> |**Name**:<br />DuplicateOfflineFilter<br />**Hex**:<br />80048449<br />**Number**:<br />-2147187639|You can create only one local data group for each record type.|
> |**Name**:<br />DuplicateOutlookAppointment<br />**Hex**:<br />80040274<br />**Number**:<br />-2147220876|The Appointment being promoted from Outlook is already tracked in Dynamics 365|
> |**Name**:<br />DuplicatePrimaryNameAttribute<br />**Hex**:<br />8004701E<br />**Number**:<br />-2147192802|The new {2} attribute is set as the primary name attribute for the {1} entity. The {1} entity already has the {0} attribute set as the primary name attribute. An entity can only have one primary name attribute.|
> |**Name**:<br />DuplicatePrivilegeInRolecontrol<br />**Hex**:<br />80061118<br />**Number**:<br />-2147086056|The Channel Access Profile privilege array contains duplicate privilege references.|
> |**Name**:<br />DuplicateProductPriceLevel<br />**Hex**:<br />80043b08<br />**Number**:<br />-2147206392|This product and unit combination has a price for this price list.|
> |**Name**:<br />DuplicateProductRelationship<br />**Hex**:<br />8004F891<br />**Number**:<br />-2147157871|A product relationship with the same product and related product already exists.|
> |**Name**:<br />DuplicateRecord<br />**Hex**:<br />80040237<br />**Number**:<br />-2147220937|Operation failed due to a SQL integrity violation.|
> |**Name**:<br />DuplicateRecordEntityKey<br />**Hex**:<br />80060892<br />**Number**:<br />-2147088238|Entity Key {0} violated. A record with the same value for {1} already exists. A duplicate record cannot be created. Select one or more unique values and try again.|
> |**Name**:<br />DuplicateRecordsFound<br />**Hex**:<br />80040333<br />**Number**:<br />-2147220685|A record was not created or updated because a duplicate of the current record already exists.|
> |**Name**:<br />DuplicateReportVisibility<br />**Hex**:<br />80040495<br />**Number**:<br />-2147220331|A ReportVisibility with the same ReportId and VisibilityCode already exists. Duplicates are not allowed.|
> |**Name**:<br />DuplicateSalesTeamMember<br />**Hex**:<br />80048341<br />**Number**:<br />-2147187903|The user you're trying to add is already a member of the sales team.|
> |**Name**:<br />DuplicateUIStatementRootsFound<br />**Hex**:<br />8004F201<br />**Number**:<br />-2147159551|There can be only one root statement for a given uiscript.|
> |**Name**:<br />DynamicPropertyDefaultValueNeeded<br />**Hex**:<br />80061038<br />**Number**:<br />-2147086280|You must specify a default value because this property is required and is read-only.|
> |**Name**:<br />DynamicPropertyInstanceMissingRequiredColumns<br />**Hex**:<br />8008100A<br />**Number**:<br />-2146955254|The property instance can't be updated. Verify that the following fields are present: dynamicpropertyid, dynamicpropertyoptionsetvalueid, and regardingobjectid.|
> |**Name**:<br />DynamicPropertyInstanceUpdateValuesDifferentRegarding<br />**Hex**:<br />8008100B<br />**Number**:<br />-2146955253|The property instances couldn't be saved because they refer to different product line items.|
> |**Name**:<br />DynamicPropertyInvalidRegardingForUpdate<br />**Hex**:<br />80081004<br />**Number**:<br />-2146955260|You can’t create or change properties for a published or retired product.|
> |**Name**:<br />DynamicPropertyInvalidStateChange<br />**Hex**:<br />80081001<br />**Number**:<br />-2146955263|You can't set an inactive property to an active state.|
> |**Name**:<br />DynamicPropertyInvalidStateForDelete<br />**Hex**:<br />80081002<br />**Number**:<br />-2146955262|You can't delete a property that is in the active state.|
> |**Name**:<br />DynamicPropertyInvalidStateForUpdate<br />**Hex**:<br />80081000<br />**Number**:<br />-2146955264|You can't update a property that isn't in the draft state.|
> |**Name**:<br />DynamicPropertyOptionSetInvalidStateForUpdate<br />**Hex**:<br />8008100C<br />**Number**:<br />-2146955252|You can't modify the property option set item for a property that is not in the draft state.|
> |**Name**:<br />EditorOnlySupportAndOperatorForLogicalConditions<br />**Hex**:<br />80060005<br />**Number**:<br />-2147090427|The rule expression contains logical operator which is not supported. The editor only support And operator for Logical conditions.|
> |**Name**:<br />EditQueryInDynamicExcelNotSupported<br />**Hex**:<br />800609B8<br />**Number**:<br />-2147087944|You can’t edit the query on a dynamic spreadsheet once the Excel file has been exported. If you’d like to make changes, go back to Dynamics 365 and then re-export.|
> |**Name**:<br />EESiteDBFetchFailure<br />**Hex**:<br />80050025<br />**Number**:<br />-2147155931|Unable to fetch data from site DB.|
> |**Name**:<br />EmailAlreadyExistsInDestinationQueue<br />**Hex**:<br />80040523<br />**Number**:<br />-2147220189|You cannot add this e-mail to the selected queue. A queue item for this e-mail already exists in the queue. You can delete the item from the queue, and then try again.|
> |**Name**:<br />EmailDoesNotExist<br />**Hex**:<br />80050007<br />**Number**:<br />-2147155961|Email does not exist for given attachment.|
> |**Name**:<br />EmailEngagementFeatureDisabled<br />**Hex**:<br />80050003<br />**Number**:<br />-2147155965|Please enable Email Engagement feature for current org to follow or unfollow email attachment.|
> |**Name**:<br />EmailEngagementFeatureDisabledForAttachmentTracking<br />**Hex**:<br />80050015<br />**Number**:<br />-2147155947|Please enable Email Engagement feature for this organization to follow email attachments.|
> |**Name**:<br />EmailInteractionsFetchFailure<br />**Hex**:<br />80050022<br />**Number**:<br />-2147155934|Unable to fetch email interactions.|
> |**Name**:<br />EmailMessageSizeExceeded<br />**Hex**:<br />8005E237<br />**Number**:<br />-2147098057|Email Size Exceeds the MaximumMessageSizeLimit specified by the deployment.|
> |**Name**:<br />EmailMonitoringDeProvisionFailed<br />**Hex**:<br />80050014<br />**Number**:<br />-2147155948|Email engagement feature deprovisioning failed|
> |**Name**:<br />EmailMonitoringNotProvisioned<br />**Hex**:<br />80050011<br />**Number**:<br />-2147155951|RI provisioning service failed.|
> |**Name**:<br />EmailMonitoringProvisionFailed<br />**Hex**:<br />80050012<br />**Number**:<br />-2147155950|Email engagement feature provisioning failed|
> |**Name**:<br />EmailNotFollowed<br />**Hex**:<br />80050008<br />**Number**:<br />-2147155960|This attachment cannot be followed as its corresponding email is not followed.|
> |**Name**:<br />EmailOpenActionCardCreationFailure<br />**Hex**:<br />80050024<br />**Number**:<br />-2147155932|We can’t create email open action card.|
> |**Name**:<br />EmailRecipientNotSpecified<br />**Hex**:<br />80040b04<br />**Number**:<br />-2147218684|The e-mail must have at least one recipient before it can be sent|
> |**Name**:<br />EmailReminderActionCardCreationFailure<br />**Hex**:<br />80050023<br />**Number**:<br />-2147155933|We can’t create email reminder action card.|
> |**Name**:<br />EmailRouterFileTooLargeToProcess<br />**Hex**:<br />8005F031<br />**Number**:<br />-2147094479|One or more of the email router configuration files is too large to get processed.|
> |**Name**:<br />EmailServerProfileADBasedAuthenticationProtocolNotAllowed<br />**Hex**:<br />8005E23C<br />**Number**:<br />-2147098052|The authentication protocol cannot be set to Negotiate or NTLM for your organization because these require Active Directory. Use a different authentication protocol or contact your system administrator to enable an Active Directory-based authentication protocol.|
> |**Name**:<br />EmailServerProfileAutoDiscoverNotAllowed<br />**Hex**:<br />8005E204<br />**Number**:<br />-2147098108|Auto discover server URL can location can only be used for an exchange e-mail server type.|
> |**Name**:<br />EmailServerProfileBasicAuthenticationProtocolNotAllowed<br />**Hex**:<br />8005E23D<br />**Number**:<br />-2147098051|The specified authentication protocol cannot be used because the protocol requires sending credentials on a secure channel. Use a different authentication protocol or contact your administrator to enable Basic authentication protocol on a non-secure channel.|
> |**Name**:<br />EmailServerProfileDelegateAccessNotAllowed<br />**Hex**:<br />8005E235<br />**Number**:<br />-2147098059|For an SMTP email server type, auto-granted delegate access cannot be used.|
> |**Name**:<br />EmailServerProfileImpersonationNotAllowed<br />**Hex**:<br />8005E236<br />**Number**:<br />-2147098058|For a Non Exchange email server type, impersonation cannot be used.|
> |**Name**:<br />EmailServerProfileInvalidAuthenticationProtocol<br />**Hex**:<br />8005E23B<br />**Number**:<br />-2147098053|The authentication protocol is invalid for the specified server and connection type. For more information, contact your system administrator.|
> |**Name**:<br />EmailServerProfileInvalidCredentialRetrievalForExchange<br />**Hex**:<br />8005E203<br />**Number**:<br />-2147098109|No credentials (Anonymous) cannot be used a connection type for exchange e-mail server type.|
> |**Name**:<br />EmailServerProfileInvalidCredentialRetrievalForOnline<br />**Hex**:<br />8005E202<br />**Number**:<br />-2147098110|Windows integrated or Anonymous authentication cannot be used as a connection type for Microsoft Dynamics 365 Online.|
> |**Name**:<br />EmailServerProfileInvalidServerLocation<br />**Hex**:<br />8005E20A<br />**Number**:<br />-2147098102|The specified server location {0} is invalid. Correct the server location and try again.|
> |**Name**:<br />EmailServerProfileLocationNotRequired<br />**Hex**:<br />8005E205<br />**Number**:<br />-2147098107|You cannot specify the incoming/outgoing e-mail server location when Autodiscover server location has been set to true.|
> |**Name**:<br />EmailServerProfileNotAssociated<br />**Hex**:<br />8005E222<br />**Number**:<br />-2147098078|Email Server Profile is not associated with the current mailbox. Please associate a valid profile to send/receive mails.|
> |**Name**:<br />EmailServerProfileSslRequiredForOnline<br />**Hex**:<br />8005E201<br />**Number**:<br />-2147098111|You cannot set SSL as false for Microsoft Dynamics 365 Online.|
> |**Name**:<br />EmailServerProfileSslRequiredForOnPremise<br />**Hex**:<br />8005E234<br />**Number**:<br />-2147098060|Usage of SSL while contacting external email servers is mandatory for this Dynamics 365 deployment.|
> |**Name**:<br />EmptyCommandOrEntity<br />**Hex**:<br />80154B51<br />**Number**:<br />-2146088111|Command or entity name cannot be empty.|
> |**Name**:<br />EmptyContent<br />**Hex**:<br />80040365<br />**Number**:<br />-2147220635|The file is empty.|
> |**Name**:<br />EmptyEntityFilterXml<br />**Hex**:<br />80071118<br />**Number**:<br />-2147020520|The FetchXML is missing.|
> |**Name**:<br />EmptyFileForImport<br />**Hex**:<br />80048487<br />**Number**:<br />-2147187577|The selected file contains no data.|
> |**Name**:<br />EmptyFilesInZip<br />**Hex**:<br />80048486<br />**Number**:<br />-2147187578|One or more files in the compressed (.zip) or .cab file don't contain data. Check the files and try again.|
> |**Name**:<br />EmptyHeaderColumn<br />**Hex**:<br />80040337<br />**Number**:<br />-2147220681|The column heading cannot be empty.|
> |**Name**:<br />EmptyHeaderRow<br />**Hex**:<br />80040366<br />**Number**:<br />-2147220634|The first row of the file is empty.|
> |**Name**:<br />EmptyImportFileRow<br />**Hex**:<br />80040347<br />**Number**:<br />-2147220665|Empty row.|
> |**Name**:<br />EmptyRecord<br />**Hex**:<br />80040373<br />**Number**:<br />-2147220621|The record is empty|
> |**Name**:<br />EmptySecretInDataSource<br />**Hex**:<br />80044818<br />**Number**:<br />-2147203048|Data Source secrets are not included in solutions. You'll need to edit your data sources to add secrets back following solution import.|
> |**Name**:<br />EmptySiteMapXml<br />**Hex**:<br />8004F402<br />**Number**:<br />-2147159038|Sitemap xml is empty.|
> |**Name**:<br />EmptyXml<br />**Hex**:<br />80040202<br />**Number**:<br />-2147220990|Empty XML.|
> |**Name**:<br />EnableMobileOfflineDisableChangeTrackingError<br />**Hex**:<br />800609A2<br />**Number**:<br />-2147087966|You must enable change tracking for this entity since mobile offline client is enabled.|
> |**Name**:<br />EnableRIFeatureNotAllowed<br />**Hex**:<br />80044279<br />**Number**:<br />-2147204487|You need system administrator privileges to update Relationship Insights tenant information.|
> |**Name**:<br />EndUserNotificationTypeNotValidForEmail<br />**Hex**:<br />8004D291<br />**Number**:<br />-2147167599|Cannot send Email for EndUserNotification Type: {0}.|
> |**Name**:<br />EntitiesExceedMaxAllowed<br />**Hex**:<br />80060415<br />**Number**:<br />-2147089387|You can't cover more than five entities in a process flow. Remove some entities and try again.|
> |**Name**:<br />EntitiesInViewNotAvailableOffline<br />**Hex**:<br />80071125<br />**Number**:<br />-2147020507|One or more entities referenced are not available offline.|
> |**Name**:<br />EntitiesInViewNotInProfile<br />**Hex**:<br />80071124<br />**Number**:<br />-2147020508|One or more entities in this view are not part of this profile.|
> |**Name**:<br />EntitlementAlreadyInactiveState<br />**Hex**:<br />80060615<br />**Number**:<br />-2147088875|You can't activate an entitlement when it's in the active state.|
> |**Name**:<br />EntitlementAlreadyInCanceledState<br />**Hex**:<br />80044208<br />**Number**:<br />-2147204600|You can't cancel an entitlement when it's in the Canceled state.|
> |**Name**:<br />EntitlementAlreadyInDraftState<br />**Hex**:<br />80060614<br />**Number**:<br />-2147088876|You can't deactivate an entitlement when it's in the draft state.|
> |**Name**:<br />EntitlementBlankTerms<br />**Hex**:<br />80060622<br />**Number**:<br />-2147088862|Total terms can't be blank. Enter a value and try again.|
> |**Name**:<br />EntitlementChannelInvalidState<br />**Hex**:<br />80060603<br />**Number**:<br />-2147088893|An entitlement channel term cannot be created, modified or deleted when the associated entitlement is not in draft state.|
> |**Name**:<br />EntitlementChannelWithoutEntitlementId<br />**Hex**:<br />80060612<br />**Number**:<br />-2147088878|Associate the entitlement channel with an entitlement or entitlement template.|
> |**Name**:<br />EntitlementEditDraft<br />**Hex**:<br />80060613<br />**Number**:<br />-2147088877|You can only edit a draft entitlement.|
> |**Name**:<br />EntitlementInvalidRemainingTerms<br />**Hex**:<br />80060624<br />**Number**:<br />-2147088860|The number of remaining terms can't be greater than the number of total terms.|
> |**Name**:<br />EntitlementInvalidStartEndDate<br />**Hex**:<br />80060600<br />**Number**:<br />-2147088896|Start Date cannot be more than the End Date|
> |**Name**:<br />EntitlementInvalidState<br />**Hex**:<br />80060601<br />**Number**:<br />-2147088895|You cannot delete an entitlement that is in active or waiting state|
> |**Name**:<br />EntitlementInvalidTerms<br />**Hex**:<br />80060604<br />**Number**:<br />-2147088892|Specify a higher value for total terms so the remaining terms won't be a negative value.|
> |**Name**:<br />EntitlementNotActiveInAssociationToCase<br />**Hex**:<br />80060616<br />**Number**:<br />-2147088874|You can't create a case for this entitlement because the entitlement is not in active state.|
> |**Name**:<br />EntitlementTemplateTotalTerms<br />**Hex**:<br />80060620<br />**Number**:<br />-2147088864|If the allocation type is the number of cases, the total terms can't be a decimal value. Specify a whole number.|
> |**Name**:<br />EntitlementTotalTerms<br />**Hex**:<br />80060619<br />**Number**:<br />-2147088871|If the allocation type is the number of cases, the total terms can't be a decimal value. Specify a whole number.|
> |**Name**:<br />EntityCannotBeChildInCustomRelationship<br />**Hex**:<br />8004432D<br />**Number**:<br />-2147204307|This entity is either not valid as a child in a custom parental relationship or is already a child in a parental relationship|
> |**Name**:<br />EntityCannotHaveOwnedByMeFilter<br />**Hex**:<br />80071136<br />**Number**:<br />-2147020490|The entity '{0}' in the profile '{1}' has OwnedByMe set to true. This property is not a valid property for the '{0}' entity.|
> |**Name**:<br />EntityCannotHaveOwnedByMyTeamFilter<br />**Hex**:<br />80071137<br />**Number**:<br />-2147020489|The entity '{0}' in the profile '{1}' has OwnedByMyTeam set to true. This property is not a valid property for the '{0}' entity.|
> |**Name**:<br />EntityCannotParticipateInEntityAssociation<br />**Hex**:<br />80044332<br />**Number**:<br />-2147204302|This entity cannot participate in an entity association|
> |**Name**:<br />EntityDupCheckNotSupportedSystemWide<br />**Hex**:<br />80048431<br />**Number**:<br />-2147187663|Duplicate detection is not enabled for one or more of the selected entities. The duplicate detection job cannot be started.|
> |**Name**:<br />EntityExceedsMaxActiveBusinessProcessFlows<br />**Hex**:<br />80060420<br />**Number**:<br />-2147089376|The {0} entity exceeds the maximum number of active business process flows. The limit is {1}.|
> |**Name**:<br />EntityFilterContainerMustNotBeNullFormatString<br />**Hex**:<br />80071132<br />**Number**:<br />-2147020494|There are no filters specified for the entity '{0}'. You must define at least one filter.|
> |**Name**:<br />EntityGroupNameOrEntityNamesMustBeProvided<br />**Hex**:<br />80060205<br />**Number**:<br />-2147089915|Missing parameter. You must provide EntityGroupName or EntityNames.|
> |**Name**:<br />EntityHasNoStateCode<br />**Hex**:<br />80047015<br />**Number**:<br />-2147192811|Specified entity does not have a statecode.|
> |**Name**:<br />EntityInstanceIsNull<br />**Hex**:<br />80060444<br />**Number**:<br />-2147089340|Error creating or updating Business Process: entity instance cannot be null.|
> |**Name**:<br />EntityInstantiationFailed<br />**Hex**:<br />80040243<br />**Number**:<br />-2147220925|Instantiation of an Entity instance Service failed.|
> |**Name**:<br />EntityIsIntersect<br />**Hex**:<br />8004830F<br />**Number**:<br />-2147187953|The specified entity is intersect entity|
> |**Name**:<br />EntityIsLocked<br />**Hex**:<br />80043b1d<br />**Number**:<br />-2147206371|This entity is already locked.|
> |**Name**:<br />EntityIsNotBusinessProcessFlowEnabled<br />**Hex**:<br />80060421<br />**Number**:<br />-2147089375|The IsBusinessProcessEnabled property of the {0} entity is false.|
> |**Name**:<br />EntityIsNotCustomizable<br />**Hex**:<br />80047008<br />**Number**:<br />-2147192824|The specified entity is not customizable|
> |**Name**:<br />EntityIsNotEnabledForExternalParty<br />**Hex**:<br />8006111B<br />**Number**:<br />-2147086053|You can't create/update an external party item associated to an entity that is not enabled for external party.|
> |**Name**:<br />EntityIsNotEnabledForFollow<br />**Hex**:<br />8004F6A2<br />**Number**:<br />-2147158366|This entity is not enabled to be followed. |
> |**Name**:<br />EntityIsNotEnabledForFollowUser<br />**Hex**:<br />8004F6A1<br />**Number**:<br />-2147158367|This entity is not enabled to be followed. |
> |**Name**:<br />EntityIsUnlocked<br />**Hex**:<br />80043b1e<br />**Number**:<br />-2147206370|This entity is already unlocked.|
> |**Name**:<br />EntityKeyNameExists<br />**Hex**:<br />80060893<br />**Number**:<br />-2147088237|An entity key with the name {0} already exists on entity {1}.|
> |**Name**:<br />EntityKeyNotDefined<br />**Hex**:<br />80060890<br />**Number**:<br />-2147088240|The specified key attributes are not a defined key for the {0} entity|
> |**Name**:<br />EntityKeyWithSelectedAttributesExists<br />**Hex**:<br />80060894<br />**Number**:<br />-2147088236|An entity key with the selected attributes already exists on entity.|
> |**Name**:<br />EntityLimitExceeded<br />**Hex**:<br />80060200<br />**Number**:<br />-2147089920|MultiEntitySearch exceeded Entity Limit defined for the Organization.|
> |**Name**:<br />EntityLoopBeingCreated<br />**Hex**:<br />80040387<br />**Number**:<br />-2147220601|Creating this parental association would create a loop in this entity hierarchy.|
> |**Name**:<br />EntityLoopExists<br />**Hex**:<br />80040386<br />**Number**:<br />-2147220602|Loop exists in this entity hierarchy.|
> |**Name**:<br />EntityMetadataSyncFailed<br />**Hex**:<br />8005F238<br />**Number**:<br />-2147093960|There were problems with the server configurations.  There was a problem with the server configuration changes.  We are unable to load the application, please contact your Dynamics 365 administrator.|
> |**Name**:<br />EntityMetadataSyncFailedWithContinue<br />**Hex**:<br />8005F239<br />**Number**:<br />-2147093959|There were difficulties with the server configuration changes.  You can continue to use the app with the older configuration, however, you may experience problems including errors when saving.  Please contact your Dynamics 365 administrator. |
> |**Name**:<br />EntityNotEnabledForAutoCreatedAccessTeams<br />**Hex**:<br />80048334<br />**Number**:<br />-2147187916|This entity is not enabled for auto created access teams.|
> |**Name**:<br />EntityNotEnabledForCharts<br />**Hex**:<br />8004E00C<br />**Number**:<br />-2147164148|Charts are not enabled on the specified primary entity type code: {0}.|
> |**Name**:<br />EntityNotEnabledForThisDevice<br />**Hex**:<br />8005F200<br />**Number**:<br />-2147094016|Entity not enabled to be viewed in this device|
> |**Name**:<br />EntityNotRule<br />**Hex**:<br />8004E112<br />**Number**:<br />-2147163886|The collection name is not a recurrence rule.|
> |**Name**:<br />EntityReferenceArgumentsNotBound<br />**Hex**:<br />80060395<br />**Number**:<br />-2147089515|Required arguments of type EntityReference must be bound to some entity.|
> |**Name**:<br />EntityRelationshipRoleCustomLabelsMissing<br />**Hex**:<br />80044328<br />**Number**:<br />-2147204312|Custom labels must be provided if an entity relationship role has a display option of UseCustomLabels|
> |**Name**:<br />EntityRelationshipSchemaNameNotUnique<br />**Hex**:<br />8004432B<br />**Number**:<br />-2147204309|A relationship with the specified name already exists. Please specify a unique name.|
> |**Name**:<br />EntityRelationshipSchemaNameRequired<br />**Hex**:<br />8004432A<br />**Number**:<br />-2147204310|Entity relationships require a name|
> |**Name**:<br />EntityTypeNotSupported<br />**Hex**:<br />80100008<br />**Number**:<br />-2146435064|{0} entity does not support this message.|
> |**Name**:<br />EntityTypeSpecifiedForDashboard<br />**Hex**:<br />8004E30B<br />**Number**:<br />-2147163381|An entity type cannot be specified for a dashboard.|
> |**Name**:<br />ErrorConnectingToDiscoveryService<br />**Hex**:<br />8004B066<br />**Number**:<br />-2147176346|Error when trying to connect to customer's discovery service.|
> |**Name**:<br />ErrorConnectingToOrganizationService<br />**Hex**:<br />8004B068<br />**Number**:<br />-2147176344|Error when trying to connect to customer's organization service.|
> |**Name**:<br />ErrorDeleteStatementTextIsReferenced<br />**Hex**:<br />8004F203<br />**Number**:<br />-2147159549|You cannot delete the UI script statement text because it is being referred by one or more ui script statements.|
> |**Name**:<br />ErrorFetchingBaseUrl<br />**Hex**:<br />80044290<br />**Number**:<br />-2147204464|We can't fetch base URL for organization Id {0}. Exception details {1}|
> |**Name**:<br />ErrorFetchingRIProvisionStatus<br />**Hex**:<br />80044291<br />**Number**:<br />-2147204463|We can't fetch RI provisioning status for organization Id {0}. Exception details {1}|
> |**Name**:<br />ErrorGeneratingActionHub<br />**Hex**:<br />80071001<br />**Number**:<br />-2147020799|An error has occurred. Please try again later.|
> |**Name**:<br />ErrorGeneratingInvitation<br />**Hex**:<br />8004B013<br />**Number**:<br />-2147176429|Some Internal error occurred in generating invitation token, Please try again later|
> |**Name**:<br />ErrorImportInvalidForPublishedScript<br />**Hex**:<br />8004F216<br />**Number**:<br />-2147159530|You cannot save data to a published UI script. Unpublish the UI script, and try again.|
> |**Name**:<br />ErrorIncreate<br />**Hex**:<br />80040359<br />**Number**:<br />-2147220647|The Microsoft Dynamics 365 record could not be created|
> |**Name**:<br />ErrorInDelete<br />**Hex**:<br />8004035a<br />**Number**:<br />-2147220646|The Microsoft Dynamics 365 record could not be deleted|
> |**Name**:<br />ErrorInFetchingEmailEngagementProvisioningStatus<br />**Hex**:<br />80050013<br />**Number**:<br />-2147155949|Error in fetching email engagement feature provisioning status.|
> |**Name**:<br />ErrorInFieldWidthIncrease<br />**Hex**:<br />80044351<br />**Number**:<br />-2147204271|An error occurred while increasing the field width.|
> |**Name**:<br />ErrorInImportConfig<br />**Hex**:<br />80040323<br />**Number**:<br />-2147220701|Cannot process with Bulk Import as Import Configuration has some errors.|
> |**Name**:<br />ErrorInParseRow<br />**Hex**:<br />80040346<br />**Number**:<br />-2147220666|The row could not be parsed. This is typically caused by a row that is too long.|
> |**Name**:<br />ErrorInSetState<br />**Hex**:<br />80040357<br />**Number**:<br />-2147220649|The status or status reason of the Microsoft Dynamics 365 record could not be set|
> |**Name**:<br />ErrorInStoringImportFile<br />**Hex**:<br />80048497<br />**Number**:<br />-2147187561|An error occurred while storing the import file in database.|
> |**Name**:<br />ErrorInUnzip<br />**Hex**:<br />80048483<br />**Number**:<br />-2147187581|An error occurred while extracting the uploaded compressed (.zip) or .cab file. Make sure that the file isn't password protected, and try uploading the file again. If this problem persists, contact your system administrator.|
> |**Name**:<br />ErrorInUnzipAlternate<br />**Hex**:<br />80048503<br />**Number**:<br />-2147187453|An error occurred while the uploaded compressed (.zip) file was being extracted. Try to upload the file again. If the problem persists, contact your system administrator.|
> |**Name**:<br />ErrorInUpdate<br />**Hex**:<br />80040358<br />**Number**:<br />-2147220648|The Microsoft Dynamics 365 record could not be updated|
> |**Name**:<br />ErrorInvalidFileNameChars<br />**Hex**:<br />8004F214<br />**Number**:<br />-2147159532|The Microsoft Excel file name cannot contain the following characters: *  \ : > < | ? " /. Rename the file using valid characters, and try again.|
> |**Name**:<br />ErrorInvalidUIScriptImportFile<br />**Hex**:<br />8004F211<br />**Number**:<br />-2147159535|File type is not supported. Select an xml file for import.|
> |**Name**:<br />ErrorMigrationProcessExcessOnServer<br />**Hex**:<br />8005F034<br />**Number**:<br />-2147094476|The server is busy handling other migration processes. Please try after some time.|
> |**Name**:<br />ErrorMimeTypeNullOrEmpty<br />**Hex**:<br />8004F215<br />**Number**:<br />-2147159531|The MimeType property value of the UploadFromBase64DataUIScriptRequest method is null or empty. Specify a valid property value, and try again.|
> |**Name**:<br />ErrorNoActiveRoutingRuleExists<br />**Hex**:<br />8004F874<br />**Number**:<br />-2147157900|Currently there's no active rule to route this case.|
> |**Name**:<br />ErrorNoQueryData<br />**Hex**:<br />8004F220<br />**Number**:<br />-2147159520|An error has occurred. Either the data does not exist or you do not have sufficient privileges to view the data. Contact your system administrator for help.|
> |**Name**:<br />ErrorOnFeatureStatusChange<br />**Hex**:<br />80044289<br />**Number**:<br />-2147204471|We can’t enable/disable the {0} feature for organization Id {1}. Exception details {2}.|
> |**Name**:<br />ErrorOnGetRecord<br />**Hex**:<br />80044286<br />**Number**:<br />-2147204474|There was an error fetching a record for table {0}. Exception details {1}.|
> |**Name**:<br />ErrorOnGetRIProvisionStatus<br />**Hex**:<br />80044282<br />**Number**:<br />-2147204478|We can’t get the Relationship Insights provisioning status for organization ID {0}. Exception details {1}.|
> |**Name**:<br />ErrorOnGetRITenantEndPoint<br />**Hex**:<br />80044283<br />**Number**:<br />-2147204477|We can’t get the Relationship Insights tenant endpoint information for organization ID {0}. Exception details {1}.|
> |**Name**:<br />ErrorOnQryPropertyBagCollection<br />**Hex**:<br />80044287<br />**Number**:<br />-2147204473|The query didn’t return all {0} columns.|
> |**Name**:<br />ErrorOnStartOfRIProvision<br />**Hex**:<br />80044284<br />**Number**:<br />-2147204476|We can’t start provisioning for organization ID {0}. Exception details {1}.|
> |**Name**:<br />ErrorOnTenantVerifyUpdate<br />**Hex**:<br />80044285<br />**Number**:<br />-2147204475|We can’t verify or update tenant information for organization ID {0}. Exception details {1}.|
> |**Name**:<br />ErrorPropertyBagCollectionMissedColumn<br />**Hex**:<br />80044288<br />**Number**:<br />-2147204472|{0} column for table {1} is missing.|
> |**Name**:<br />ErrorReactivatingComponentInstance<br />**Hex**:<br />8004F004<br />**Number**:<br />-2147160060|After undeleting a label, there is no underlying label to reactivate.|
> |**Name**:<br />ErrorScriptCannotDeletePublishedScript<br />**Hex**:<br />8004F209<br />**Number**:<br />-2147159543|You cannot delete a UI script that is published. You must unpublish it first.|
> |**Name**:<br />ErrorScriptCannotUpdatePublishedScript<br />**Hex**:<br />8004F213<br />**Number**:<br />-2147159533|You cannot update a UI script that is published. You must unpublish it first.|
> |**Name**:<br />ErrorScriptFileParse<br />**Hex**:<br />8004F212<br />**Number**:<br />-2147159534|Error occurred while parsing the XML file.|
> |**Name**:<br />ErrorScriptInitialStatementNotInScript<br />**Hex**:<br />8004F207<br />**Number**:<br />-2147159545|The initial statement for this script does not belong to this script.|
> |**Name**:<br />ErrorScriptInitialStatementNotRoot<br />**Hex**:<br />8004F208<br />**Number**:<br />-2147159544|The initial statement should the root statement and cannot have a previous statement set.|
> |**Name**:<br />ErrorScriptLanguageNotInstalled<br />**Hex**:<br />8004F206<br />**Number**:<br />-2147159546|The language specified is not supported in your Dynamics 365 install. Please check with your system administrator on the list of "enabled" languages.|
> |**Name**:<br />ErrorScriptPublishMalformedScript<br />**Hex**:<br />8004F20B<br />**Number**:<br />-2147159541|The selected UI script cannot be published. The UI script contains one or more paths which do not end in an end-script or next-script action node. Correct the paths and try to publish again.|
> |**Name**:<br />ErrorScriptPublishMissingInitialStatement<br />**Hex**:<br />8004F20A<br />**Number**:<br />-2147159542|The selected UI script cannot be published. Provide a value for "First statement number" and try to publish again.|
> |**Name**:<br />ErrorScriptSessionCannotCreateForDraftScript<br />**Hex**:<br />8004F204<br />**Number**:<br />-2147159548|You cannot create a UI script session for a UI script which is not published.|
> |**Name**:<br />ErrorScriptSessionCannotSetStateForDraftScript<br />**Hex**:<br />8004F20D<br />**Number**:<br />-2147159539|You cannot set the state of a UI script session for a UI script which is not published.|
> |**Name**:<br />ErrorScriptSessionCannotUpdateForDraftScript<br />**Hex**:<br />8004F205<br />**Number**:<br />-2147159547|You cannot update a UI script session for a UI script which is not published.|
> |**Name**:<br />ErrorScriptStatementResponseTypeOnlyForPrompt<br />**Hex**:<br />8004F20E<br />**Number**:<br />-2147159538|You cannot associate the response control type for a statement which is not a prompt.|
> |**Name**:<br />ErrorScriptUnpublishActiveScript<br />**Hex**:<br />8004F20C<br />**Number**:<br />-2147159540|This script is in use and has active sessions (status-reason=incomplete). Please terminate the active sessions (i.e. status-reason=cancelled) and try to unpublish again.|
> |**Name**:<br />ErrorsInEmailRouterMigrationFiles<br />**Hex**:<br />8005F032<br />**Number**:<br />-2147094478|Invalid File(s) for Email Router Migration|
> |**Name**:<br />ErrorsInImportFiles<br />**Hex**:<br />8004034a<br />**Number**:<br />-2147220662|Invalid File(s) for Import|
> |**Name**:<br />ErrorsInProfileRuleWorkflowActivation<br />**Hex**:<br />80061119<br />**Number**:<br />-2147086055|You can't activate this profile rule. You don't have the required permissions on the record types that are referenced by this profile rule.|
> |**Name**:<br />ErrorsInSlaWorkflowActivation<br />**Hex**:<br />80048535<br />**Number**:<br />-2147187403|You can't activate this service level agreement (SLA). You don't have the required permissions on the record types that are referenced by this SLA.|
> |**Name**:<br />ErrorsInWorkflowDefinition<br />**Hex**:<br />80048455<br />**Number**:<br />-2147187627|The selected workflow has errors and cannot be published. Please open the workflow, remove the errors and try again.|
> |**Name**:<br />ErrorStatementDeleteOnlyForDraftScript<br />**Hex**:<br />8004F210<br />**Number**:<br />-2147159536|You cannot delete a UI script statement for a UI script which is not draft.|
> |**Name**:<br />ErrorStatementOnlyForDraftScript<br />**Hex**:<br />8004F20F<br />**Number**:<br />-2147159537|You cannot create a UI script statement for a UI script which is not draft.|
> |**Name**:<br />ErrorTemplate<br />**Hex**:<br />80050102<br />**Number**:<br />-2147155710|{0}|
> |**Name**:<br />ErrorUIScriptPromptMissing<br />**Hex**:<br />8004F221<br />**Number**:<br />-2147159519|The dialog that is being activated has no prompt/response.|
> |**Name**:<br />ErrorUpdateStatementTextIsReferenced<br />**Hex**:<br />8004F202<br />**Number**:<br />-2147159550|You cannot update this UI script statement text because it is being referred to by one or more published ui scripts.|
> |**Name**:<br />ErrorUploadingReport<br />**Hex**:<br />80048298<br />**Number**:<br />-2147188072|An error occurred while trying to add the report to Microsoft Dynamics 365. Try adding the report again. If this problem persists, contact your system administrator.|
> |**Name**:<br />EventNotSupportedForBusinessRule<br />**Hex**:<br />80060001<br />**Number**:<br />-2147090431|Event {0} is not supported for client side business rule.|
> |**Name**:<br />EventTypeAndControlNameAreMismatched<br />**Hex**:<br />80060003<br />**Number**:<br />-2147090429|This combination of event type and control name is unexpected|
> |**Name**:<br />EvoStsAuthorizationServerRecordCreationFailureException<br />**Hex**:<br />80071006<br />**Number**:<br />-2147020794|Database operation failed while creating authorization record for Evo STS.|
> |**Name**:<br />ExceedCustomEntityQuota<br />**Hex**:<br />8004b042<br />**Number**:<br />-2147176382|The custom entity limit has been reached.|
> |**Name**:<br />ExceededLimitForAllowedFacetableAttributes<br />**Hex**:<br />80060306<br />**Number**:<br />-2147089658|Cannot set user search facets for entity {0} as the limit for allowed facetable attributes is 4. Kindly remove few attributes to proceed.|
> |**Name**:<br />ExceededNumberOfRecordsCanFollow<br />**Hex**:<br />8004F6A0<br />**Number**:<br />-2147158368|You have exceeded the number of records you can follow. Please unfollow some records to start following again.|
> |**Name**:<br />ExceededRollupFieldsPerEntityQuota<br />**Hex**:<br />80060543<br />**Number**:<br />-2147089085|You can't add a rollup field with name {4} having id {3} for entity with name {2} and id {1}. You’ve reached the maximum number of {0} allowed for this record type.|
> |**Name**:<br />ExceededRollupFieldsPerOrgQuota<br />**Hex**:<br />80060542<br />**Number**:<br />-2147089086|You can't add a rollup field. You’ve reached the maximum number of {0} allowed for your organization.|
> |**Name**:<br />ExcelFileNotFound<br />**Hex**:<br />80060805<br />**Number**:<br />-2147088379|The requested file was not found.|
> |**Name**:<br />ExcelOnlineNotUpdated<br />**Hex**:<br />80060808<br />**Number**:<br />-2147088376|Excel Online file {0} was not updated by the Wopi Server within the timeout specified.|
> |**Name**:<br />ExchangeAutodiscoverError<br />**Hex**:<br />8004503A<br />**Number**:<br />-2147200966|Autodiscover could not find the Exchange Web Services URL for the specified mailbox. Verify that the mailbox address and the credentials provided are correct and that Autodiscover is enabled and has been configured correctly.|
> |**Name**:<br />ExchangeCardAttributeMissingInResponseException<br />**Hex**:<br />80071102<br />**Number**:<br />-2147020542|Attribute not present in exchange oData response.|
> |**Name**:<br />ExchangeCardInvalidResponseFormatException<br />**Hex**:<br />80071104<br />**Number**:<br />-2147020540|Invalid response format.|
> |**Name**:<br />ExchangeCardS2SSetupFailureException<br />**Hex**:<br />80071105<br />**Number**:<br />-2147020539|Server to Server Authentication with Exchange for Action Card is not set up.|
> |**Name**:<br />ExchangeOptinNotEnabled<br />**Hex**:<br />80071106<br />**Number**:<br />-2147020538|Exchange optin is not enabled.|
> |**Name**:<br />ExchangeRateOfBaseCurrencyNotUpdatable<br />**Hex**:<br />80048cf5<br />**Number**:<br />-2147185419|The exchange rate of the base currency cannot be modified.|
> |**Name**:<br />ExecuteNotOnDemandWorkflow<br />**Hex**:<br />80045046<br />**Number**:<br />-2147200954|Workflow must be marked as on-demand or child workflow.|
> |**Name**:<br />ExecuteUnpublishedWorkflow<br />**Hex**:<br />80045047<br />**Number**:<br />-2147200953|Workflow must be in Published state.|
> |**Name**:<br />ExistingExternalReport<br />**Hex**:<br />80040488<br />**Number**:<br />-2147220344|The report could not be published for external use because a report of the same name already exists. Delete that report in SQL Server Reporting Services or rename this report, and try again.|
> |**Name**:<br />ExistingParentalRelationship<br />**Hex**:<br />80048205<br />**Number**:<br />-2147188219|A parental relationship already exists.|
> |**Name**:<br />ExpansionRequestIsOutsideExpansionWindow<br />**Hex**:<br />8004E10C<br />**Number**:<br />-2147163892|The series is already expanded for CutOffWindow.|
> |**Name**:<br />ExpectingAtLeastOneBusinessRuleStep<br />**Hex**:<br />80060011<br />**Number**:<br />-2147090415|There should be a minimum of one Business rule step.|
> |**Name**:<br />ExpiredAuthTicket<br />**Hex**:<br />8004A101<br />**Number**:<br />-2147180287|The ticket specified for authentication is expired|
> |**Name**:<br />ExpiredEntitlementActivate<br />**Hex**:<br />80060617<br />**Number**:<br />-2147088873|You can't activate an expired entitlement.|
> |**Name**:<br />ExpiredKey<br />**Hex**:<br />8004A106<br />**Number**:<br />-2147180282|The key specified to compute a hash value is expired, only active keys are valid.  Expired Key : {0}.|
> |**Name**:<br />ExpiredOAuthToken<br />**Hex**:<br />80041d52<br />**Number**:<br />-2147213998|The OAuth token has expired|
> |**Name**:<br />ExpiredVersionStamp<br />**Hex**:<br />80044352<br />**Number**:<br />-2147204270|Version stamp associated with the client has expired. Please perform a full sync.|
> |**Name**:<br />ExportDefaultAsPackagedError<br />**Hex**:<br />80048048<br />**Number**:<br />-2147188664|The default solution cannot be exported as a package.|
> |**Name**:<br />ExportManagedSolutionError<br />**Hex**:<br />80048036<br />**Number**:<br />-2147188682|An error occurred while exporting a solution. Managed solutions cannot be exported.|
> |**Name**:<br />ExportMissingSolutionError<br />**Hex**:<br />80048037<br />**Number**:<br />-2147188681|An error occurred while exporting a solution. The solution does not exist in this system.|
> |**Name**:<br />ExportSolutionError<br />**Hex**:<br />80048035<br />**Number**:<br />-2147188683|An error occurred while exporting a Solution.|
> |**Name**:<br />ExportToExcelOnlineFeatureNotEnabled<br />**Hex**:<br />80060804<br />**Number**:<br />-2147088380|Export to Excel Online feature is not enabled.|
> |**Name**:<br />ExportToXlsxFeatureNotEnabled<br />**Hex**:<br />800608C1<br />**Number**:<br />-2147088191|Export to excel file feature is not enabled.|
> |**Name**:<br />ExpressionNotSupportedForEditor<br />**Hex**:<br />80060004<br />**Number**:<br />-2147090428|Rule contain an expression that is not supported by the editor.|
> |**Name**:<br />ExternalNameExists<br />**Hex**:<br />80046F8F<br />**Number**:<br />-2147192945|An entity with the specified name already exists for data source - {0}. Please specify a new external name.|
> |**Name**:<br />ExternalSearchAttributeLimitExceeded<br />**Hex**:<br />80060300<br />**Number**:<br />-2147089664|The maximum number of indexed fields has been reached. Update the Relevance Search configuration to reduce the total number of indexed fields {1} below {0}.|
> |**Name**:<br />ExtraPartyInformation<br />**Hex**:<br />80040316<br />**Number**:<br />-2147220714|Extra party information should not be provided for this operation.|
> |**Name**:<br />FailedToDeserializeAsyncOperationData<br />**Hex**:<br />80044304<br />**Number**:<br />-2147204348|Failed to deserialize async operation data.|
> |**Name**:<br />FailedToGetNetworkServiceName<br />**Hex**:<br />80047103<br />**Number**:<br />-2147192573|Failed to obtain the localized name for NetworkService account|
> |**Name**:<br />FailedToLoadAssembly<br />**Hex**:<br />8004024e<br />**Number**:<br />-2147220914|Failed to load assembly|
> |**Name**:<br />FailedToScheduleActivity<br />**Hex**:<br />80047000<br />**Number**:<br />-2147192832|Failed to schedule activity.|
> |**Name**:<br />FailToDeleteConnectorFromExternalPartner<br />**Hex**:<br />80072601<br />**Number**:<br />-2147015167|Fail to delete the target connector from external partner.|
> |**Name**:<br />FallbackCardFormDeactivation<br />**Hex**:<br />8004F664<br />**Number**:<br />-2147158428|This operation can’t be completed. You must have at least one active Card form.|
> |**Name**:<br />FallbackFormDeactivation<br />**Hex**:<br />8004F661<br />**Number**:<br />-2147158431|This operation can’t be completed. You must have at least one active Main form.|
> |**Name**:<br />FallbackFormDeletion<br />**Hex**:<br />8004F654<br />**Number**:<br />-2147158444|You cannot delete this form because it is the only fallback form of type {0} for the {1} entity. Each entity must have at least one fallback form for each form type.|
> |**Name**:<br />FallbackMainInteractionCentricFormDeactivation<br />**Hex**:<br />8004F666<br />**Number**:<br />-2147158426|This operation can’t be completed. You must have at least one active MainInteractionCentric form.|
> |**Name**:<br />FallbackQuickFormDeactivation<br />**Hex**:<br />8004F665<br />**Number**:<br />-2147158427|This operation can’t be completed. You must have at least one active Quick form.|
> |**Name**:<br />FaxNoData<br />**Hex**:<br />80043516<br />**Number**:<br />-2147207914|The fax cannot be sent because there is no data to send. Specify at least one of the following: a cover page, a fax attachment, a fax description.|
> |**Name**:<br />FaxNoSupport<br />**Hex**:<br />80043517<br />**Number**:<br />-2147207913|The fax cannot be sent because this type of attachment is not allowed or does not support virtual printing to a fax device.|
> |**Name**:<br />FaxSendBlocked<br />**Hex**:<br />80043510<br />**Number**:<br />-2147207920|The recipient is marked as "Do Not Fax".|
> |**Name**:<br />FaxServiceNotRunning<br />**Hex**:<br />80043511<br />**Number**:<br />-2147207919|The Microsoft Windows fax service is not running or is not installed.|
> |**Name**:<br />FeatureNotEnabled<br />**Hex**:<br />80061113<br />**Number**:<br />-2147086061|This operation couldn't be completed because this feature isn’t enabled for your organization.|
> |**Name**:<br />FederatedEndpointError<br />**Hex**:<br />80044505<br />**Number**:<br />-2147203835|The username ADFS endpoint is enabled, which is blocking the intended authentication endpoint from being reached.|
> |**Name**:<br />FeedbackFeatureNotEnabled<br />**Hex**:<br />80061770<br />**Number**:<br />-2147084432|Feedback feature is not enabled.|
> |**Name**:<br />FeedbackMinMaxRequired<br />**Hex**:<br />80061772<br />**Number**:<br />-2147084430|The minimum and maximum values are required.|
> |**Name**:<br />FeedbackMinRatingValue<br />**Hex**:<br />80061774<br />**Number**:<br />-2147084428|The submitted minimum rating value {0} must be less than the submitted maximum rating value {1}.|
> |**Name**:<br />FeedbackRatingValue<br />**Hex**:<br />80061773<br />**Number**:<br />-2147084429|The rating must be a value from {0} through {1}.|
> |**Name**:<br />FetchDataSetQueryTimeout<br />**Hex**:<br />8005E00E<br />**Number**:<br />-2147098610|The fetch data set query timed out after {0} seconds. Increase the query timeout, and try again.|
> |**Name**:<br />FieldLevelSecurityNotSupported<br />**Hex**:<br />80044817<br />**Number**:<br />-2147203049|Field level security is not supported for virtual entity.|
> |**Name**:<br />FileInUse<br />**Hex**:<br />80048837<br />**Number**:<br />-2147186633|Could not read the file because another application is using the file.|
> |**Name**:<br />FileNotFound<br />**Hex**:<br />80048440<br />**Number**:<br />-2147187648|The attachment file was not found.|
> |**Name**:<br />FilePickerErrorApplicationInSnapView<br />**Hex**:<br />8005F20D<br />**Number**:<br />-2147094003|Try this action again. If the problem continues, check the {0} for solutions or contact your organization's {#Brand_CRM} Administrator. Finally, you can contact {1}.|
> |**Name**:<br />FilePickerErrorAttachmentTypeBlocked<br />**Hex**:<br />8005F204<br />**Number**:<br />-2147094012|Try this action again. If the problem continues, check the {0} for solutions or contact your organization's {#Brand_CRM} Administrator. Finally, you can contact {1}.|
> |**Name**:<br />FilePickerErrorFileSizeBreached<br />**Hex**:<br />8005F205<br />**Number**:<br />-2147094011|Try this action again. If the problem continues, check the {0} for solutions or contact your organization's {#Brand_CRM} Administrator. Finally, you can contact {1}.|
> |**Name**:<br />FilePickerErrorFileSizeCannotBeZero<br />**Hex**:<br />8005F206<br />**Number**:<br />-2147094010|Try this action again. If the problem continues, check the {0} for solutions or contact your organization's {#Brand_CRM} Administrator. Finally, you can contact {1}.|
> |**Name**:<br />FilePickerErrorUnableToOpenFile<br />**Hex**:<br />8005F207<br />**Number**:<br />-2147094009|Try this action again. If the problem continues, check the {0} for solutions or contact your organization's {#Brand_CRM} Administrator. Finally, you can contact {1}.|
> |**Name**:<br />FileReadError<br />**Hex**:<br />80048437<br />**Number**:<br />-2147187657|There was an error reading the file from the file system. Make sure you have read permission for this file, and then try migrating the file again.|
> |**Name**:<br />FileSizeExceeded<br />**Hex**:<br />80071026<br />**Number**:<br />-2147020762|Unable to copy the documents. The selected file exceeds the maximium size limit of 128 MB.|
> |**Name**:<br />FileStoreFeatureNotEnabled<br />**Hex**:<br />80072520<br />**Number**:<br />-2147015392|Feature not enabled for this organization|
> |**Name**:<br />FileTypeNotSupported<br />**Hex**:<br />800609B4<br />**Number**:<br />-2147087948|The specified file type is not supported as template.|
> |**Name**:<br />FilteredDuetoAntiSpam<br />**Hex**:<br />80040325<br />**Number**:<br />-2147220699|This customer is filtered due to AntiSpam settings.|
> |**Name**:<br />FilteredDuetoInactiveState<br />**Hex**:<br />8004032a<br />**Number**:<br />-2147220694|This customer is filtered due to inactive state.|
> |**Name**:<br />FilteredDuetoMissingEmailAddress<br />**Hex**:<br />8004032e<br />**Number**:<br />-2147220690|This customer is filtered due to missing email address.|
> |**Name**:<br />FinalMergedEntityIsNull<br />**Hex**:<br />80060443<br />**Number**:<br />-2147089341|Error creating or updating Business Process: final merged entity cannot be null.|
> |**Name**:<br />FirstStageIdInTraversedPathDoesNotMatchFirstStageIdInBusinessProcess<br />**Hex**:<br />80060456<br />**Number**:<br />-2147089322|First Stage ID in traversed path ‘{0}’ does not match first Stage ID in Business Process ‘{1}’. Please contact your system administrator.|
> |**Name**:<br />FiscalPeriodGoalMissingInfo<br />**Hex**:<br />80044903<br />**Number**:<br />-2147202813|For a goal of fiscal period type, the fiscal period attribute must be set.|
> |**Name**:<br />FiscalSettingsAlreadyUpdated<br />**Hex**:<br />80043809<br />**Number**:<br />-2147207159|Fiscal settings have already been updated. They can be updated only once.|
> |**Name**:<br />FlowIsNotActive<br />**Hex**:<br />80060469<br />**Number**:<br />-2147089303|Modern Flow must be active to be used on Flow Step.|
> |**Name**:<br />FlowMissingRecord<br />**Hex**:<br />80050262<br />**Number**:<br />-2147155358|You need to select at least one record to trigger this flow.|
> |**Name**:<br />FlowServiceClientError<br />**Hex**:<br />80060467<br />**Number**:<br />-2147089305|Flow client error returned with status code "{0}" and details "{1}".|
> |**Name**:<br />FlowTriggerNotificationDisabled<br />**Hex**:<br />80072342<br />**Number**:<br />-2147015870|Flow trigger notifications are disabled for the organization.|
> |**Name**:<br />FlowTriggerNotificationFailed<br />**Hex**:<br />80072341<br />**Number**:<br />-2147015871|Flow trigger notification call failed during http post. Please check the exception for more details.|
> |**Name**:<br />FolderDoesNotExist<br />**Hex**:<br />80060901<br />**Number**:<br />-2147088127|Folder doesn't exist.|
> |**Name**:<br />Forbidden<br />**Hex**:<br />8005F102<br />**Number**:<br />-2147094270|The server refuses to fulfill the request.|
> |**Name**:<br />FormDoesNotExist<br />**Hex**:<br />80048406<br />**Number**:<br />-2147187706|Form doesn't exist|
> |**Name**:<br />FormTransitionError<br />**Hex**:<br />80040242<br />**Number**:<br />-2147220926|The import has failed because the system cannot transition the entity form {0} from unmanaged to managed. Add at least one full (root) component to the managed solution, and then try to import it again.|
> |**Name**:<br />ForwardMailboxCannotAssociateWithUser<br />**Hex**:<br />8005E207<br />**Number**:<br />-2147098105|A forward mailbox cannot be created for a specific user or a queue.  Please remove the regarding field and try again.|
> |**Name**:<br />ForwardMailboxEmailAddressRequired<br />**Hex**:<br />8005E211<br />**Number**:<br />-2147098095|An e-mail address is a required field in case of forward mailbox.|
> |**Name**:<br />ForwardMailboxUnexpectedIncomingDeliveryMethod<br />**Hex**:<br />8005E212<br />**Number**:<br />-2147098094|Forward mailbox incoming delivery method can only be none or router.|
> |**Name**:<br />ForwardMailboxUnexpectedOutgoingDeliveryMethod<br />**Hex**:<br />8005E213<br />**Number**:<br />-2147098093|Forward mailbox outgoing delivery method can only be none.|
> |**Name**:<br />GenericActiveDirectoryError<br />**Hex**:<br />80041d37<br />**Number**:<br />-2147214025|Active Directory Error.|
> |**Name**:<br />GenericAzureActiveDirectoryError<br />**Hex**:<br />80041d54<br />**Number**:<br />-2147213996|Azure Active Directory Error.|
> |**Name**:<br />GenericImportTranslationsError<br />**Hex**:<br />80060752<br />**Number**:<br />-2147088558|Errors were encountered while processing the translations import file.|
> |**Name**:<br />GenericManagedPropertyFailure<br />**Hex**:<br />8004F026<br />**Number**:<br />-2147160026|The evaluation of the current component(name={0}, id={1}) in the current operation ({2}) failed during managed property evaluation of condition: {3}|
> |**Name**:<br />GenericMetadataSyncFailed<br />**Hex**:<br />8005F246<br />**Number**:<br />-2147093946|Sorry, something went wrong. Please try again, or restart the app.|
> |**Name**:<br />GenericMetadataSyncFailedWithContinue<br />**Hex**:<br />8005F247<br />**Number**:<br />-2147093945|Sorry, something went wrong downloading server configuration changes.  You can continue to use the app with the older configuration, however you may experience problems including errors when saving.  If this issue continues please contact your Dynamics 365 administrator and provide the information available when you choose ‘more information’.|
> |**Name**:<br />GenericTransformationInvocationError<br />**Hex**:<br />8004037b<br />**Number**:<br />-2147220613|The transformation returned invalid data.|
> |**Name**:<br />GetPhotoFromGalleryFailed<br />**Hex**:<br />8005F208<br />**Number**:<br />-2147094008|Try this action again. If the problem continues, check the {0} for solutions or contact your organization's {#Brand_CRM} Administrator. Finally, you can contact {1}.|
> |**Name**:<br />GetTenantIdFailure<br />**Hex**:<br />80071109<br />**Number**:<br />-2147020535|Error occurred while getting TenantId.|
> |**Name**:<br />GoalAttributeAlreadyMapped<br />**Hex**:<br />80044807<br />**Number**:<br />-2147203065|The Metric Detail for Specified Goal Attribute already exists.|
> |**Name**:<br />GoalMissingPeriodTypeInfo<br />**Hex**:<br />80044908<br />**Number**:<br />-2147202808|Goal Period Type needs to be specified when creating a goal. This field cannot be null.|
> |**Name**:<br />GoalPercentageAchievedValueOutOfRange<br />**Hex**:<br />8004F682<br />**Number**:<br />-2147158398|The percentage achieved value has been set to 0 because the calculated value is not in the allowed range.|
> |**Name**:<br />GoOfflineBCPFileSize<br />**Hex**:<br />80044224<br />**Number**:<br />-2147204572|Client was not able to download BCP file. Contact your system administrator for assistance and try going offline again.|
> |**Name**:<br />GoOfflineDbSizeLimit<br />**Hex**:<br />80044222<br />**Number**:<br />-2147204574|You have exceeded the storage limit for your offline database. You must reduce the amount of data to be taken offline by changing your Local Data Groups.|
> |**Name**:<br />GoOfflineEmptyFileForDelete<br />**Hex**:<br />80044230<br />**Number**:<br />-2147204560|Data file for delete is empty.|
> |**Name**:<br />GoOfflineFailedMoveData<br />**Hex**:<br />80044225<br />**Number**:<br />-2147204571|Client was not able to download data. Contact your system administrator for assistance and try going offline again.|
> |**Name**:<br />GoOfflineFailedPrepareMsde<br />**Hex**:<br />80044226<br />**Number**:<br />-2147204570|Prepare MSDE failed. Contact your system administrator for assistance and try going offline again.|
> |**Name**:<br />GoOfflineFailedReloadMetadataCache<br />**Hex**:<br />80044227<br />**Number**:<br />-2147204569|The Microsoft Dynamics 365 for Outlook was unable to go offline. Please try going offline again.|
> |**Name**:<br />GoOfflineFileWasDeleted<br />**Hex**:<br />80044229<br />**Number**:<br />-2147204567|Data file was deleted on server before it was sent to client.|
> |**Name**:<br />GoOfflineGetBCPFileException<br />**Hex**:<br />80044221<br />**Number**:<br />-2147204575|Dynamics 365 server was not able to process your request. Contact your system administrator for assistance and try going offline again.|
> |**Name**:<br />GoOfflineMetadataVersionsMismatch<br />**Hex**:<br />80044220<br />**Number**:<br />-2147204576|Client and Server metadata versions are different due to new customization on the server. Please try going offline again.|
> |**Name**:<br />GoOfflineServerFailedGenerateBCPFile<br />**Hex**:<br />80044223<br />**Number**:<br />-2147204573|Dynamics 365 server was not able to generate BCP file. Contact your system administrator for assistance and try going offline again.|
> |**Name**:<br />GraphApiS2SSetupFailureException<br />**Hex**:<br />80044260<br />**Number**:<br />-2147204512|Server to Server Authentication with Exchange for Office Graph Api  is not set up.|
> |**Name**:<br />GuidNotPresent<br />**Hex**:<br />80040362<br />**Number**:<br />-2147220638|The required globally unique identifier (GUID) in this row is not present|
> |**Name**:<br />HeaderValueDoesNotMatchAttributeDisplayLabel<br />**Hex**:<br />80040370<br />**Number**:<br />-2147220624|The column heading does not match the attribute display label.|
> |**Name**:<br />HiddenPropertyValidationFailed<br />**Hex**:<br />80061000<br />**Number**:<br />-2147086336|You can't create a property instance for a hidden property.|
> |**Name**:<br />HiddensheetNotAvailable<br />**Hex**:<br />800609B6<br />**Number**:<br />-2147087946|The hidden sheet is not available.|
> |**Name**:<br />HierarchicalOperationFailed<br />**Hex**:<br />8008100F<br />**Number**:<br />-2146955249|This operation couldn't be completed on this hierarchy. An error occurred while performing this operation for {0}. You can perform the operation separately on this product to fix the error, and then try the operation again for the complete hierarchy.|
> |**Name**:<br />HierarchyCalculateLimitReached<br />**Hex**:<br />80060547<br />**Number**:<br />-2147089081|Calculations can't be performed online because the master record hierarchy depth limit of {0} has been reached.|
> |**Name**:<br />HipInvalidCertificate<br />**Hex**:<br />8004Ed45<br />**Number**:<br />-2147160763|Invalid Certificate for using HIP.|
> |**Name**:<br />HipNoSettingError<br />**Hex**:<br />8004Ed44<br />**Number**:<br />-2147160764|No Hip application configuration setting [{0}] was found.|
> |**Name**:<br />HonorPauseWithoutSLAKPIError<br />**Hex**:<br />80045000<br />**Number**:<br />-2147201024|SLA can be set to honor pause and resume only if Use SLA KPI is set to Yes.|
> |**Name**:<br />HybridSSSExchangeOnlineS2SCertActsExpired<br />**Hex**:<br />80131500<br />**Number**:<br />-2146233088|Certificate used for S2S authentication of Dynamics 365 Onpremise with Exchange Online has expired|
> |**Name**:<br />HybridSSSExchangeOnlineS2SCertExpired<br />**Hex**:<br />80131509<br />**Number**:<br />-2146233079|Certificate used for S2S authentication of Dynamics 365 Onpremise with Exchange Online has expired|
> |**Name**:<br />ImportArticleTemplateError<br />**Hex**:<br />8004800D<br />**Number**:<br />-2147188723|There was an error in parsing the article templates in Import Xml|
> |**Name**:<br />ImportAttributeNameError<br />**Hex**:<br />80048062<br />**Number**:<br />-2147188638|Invalid name for attribute {0}.  Custom attribute names must start with a valid customization prefix. The prefix for a solution component should match the prefix that is specified for the publisher of the solution.|
> |**Name**:<br />ImportChannelPropertyGroupError<br />**Hex**:<br />800608F3<br />**Number**:<br />-2147088141|An error occurred while importing Channel Property Group.|
> |**Name**:<br />ImportComponentDeletedIgnored<br />**Hex**:<br />8004847c<br />**Number**:<br />-2147187588|You cannot update this component because it does not exist in this Microsoft Dynamics 365 organization.|
> |**Name**:<br />ImportConfigNotSpecified<br />**Hex**:<br />80040322<br />**Number**:<br />-2147220702|Cannot process with Bulk Import as Import Configuration not specified.|
> |**Name**:<br />ImportContractTemplateError<br />**Hex**:<br />8004800B<br />**Number**:<br />-2147188725|There was an error in parsing the contract templates in Import Xml|
> |**Name**:<br />ImportConvertRuleError<br />**Hex**:<br />8004F869<br />**Number**:<br />-2147157911|An error occurred while importing Convert Rules.|
> |**Name**:<br />ImportCustomizationsBadZipFileError<br />**Hex**:<br />80048060<br />**Number**:<br />-2147188640|The solution file is invalid. The compressed file must contain the following files at its root: solution.xml, customizations.xml, and [Content_Types].xml. Customization files exported from previous versions of Microsoft Dynamics 365 are not supported.|
> |**Name**:<br />ImportDashboardDeletedError<br />**Hex**:<br />8004E308<br />**Number**:<br />-2147163384|A dashboard with the same id is marked as deleted in the system. Please first publish the system form entity and import again.|
> |**Name**:<br />ImportDefaultAsPackageError<br />**Hex**:<br />80048049<br />**Number**:<br />-2147188663|The package supplied for the default solution is trying to install it in managed mode. The default solution cannot be managed. In the XML for the default solution, set the Managed value back to "false" and try to import the solution again.|
> |**Name**:<br />ImportDependencySolutionError<br />**Hex**:<br />80048034<br />**Number**:<br />-2147188684|{0} requires solutions that are not currently installed. Import the following solutions before Importing this one. {1} |
> |**Name**:<br />ImportDuplicateEntity<br />**Hex**:<br />8004810c<br />**Number**:<br />-2147188468|This import has failed because a different entity with the identical name, {0}, already exists in the target organization.|
> |**Name**:<br />ImportEmailTemplateError<br />**Hex**:<br />8004800C<br />**Number**:<br />-2147188724|There was an error in parsing the email templates in Import Xml|
> |**Name**:<br />ImportEmailTemplateErrorMissingFile<br />**Hex**:<br />8004802B<br />**Number**:<br />-2147188693|E-mail Template '{0}' import: The attachment '{1}' was not found in the import zip file.|
> |**Name**:<br />ImportEmailTemplatePersonalError<br />**Hex**:<br />80048014<br />**Number**:<br />-2147188716|E-mail Template was not imported. The Template is a personal template on the target system; import cannot overwrite personal templates.|
> |**Name**:<br />ImportEntityCustomResourcesError<br />**Hex**:<br />80048002<br />**Number**:<br />-2147188734|Invalid Custom Resources in the Import File|
> |**Name**:<br />ImportEntityCustomResourcesNewStringError<br />**Hex**:<br />80048003<br />**Number**:<br />-2147188733|Invalid Entity new string in the Custom Resources|
> |**Name**:<br />ImportEntityIconError<br />**Hex**:<br />80048001<br />**Number**:<br />-2147188735|Invalid Icon in the Import File|
> |**Name**:<br />ImportEntityNameMismatchError<br />**Hex**:<br />80048008<br />**Number**:<br />-2147188728|The number of format parameters passed into the input string is incorrect|
> |**Name**:<br />ImportEntitySystemUserLiveMismatchError<br />**Hex**:<br />80048025<br />**Number**:<br />-2147188699|The systemuser entity was imported but customized forms for the entity were not imported. Systemuser entity forms from on-premises or hosted versions of Microsoft Dynamics 365 cannot be imported into Microsoft Dynamics 365 Online.|
> |**Name**:<br />ImportEntitySystemUserOnPremiseMismatchError<br />**Hex**:<br />80048024<br />**Number**:<br />-2147188700|The systemuser entity was imported, but customized forms for the entity were not imported. Systemuser entity forms from Microsoft Dynamics 365 Online cannot be imported into on-premises or hosted versions of Microsoft Dynamics 365.|
> |**Name**:<br />ImportExportDeprecatedError<br />**Hex**:<br />80048045<br />**Number**:<br />-2147188667|This message is no longer available. Please consult the SDK for alternative messages.|
> |**Name**:<br />ImportFieldSecurityProfileAttributesMissingError<br />**Hex**:<br />80048064<br />**Number**:<br />-2147188636|Some field security permissions could not be imported because the following fields are not in the system: {0}.|
> |**Name**:<br />ImportFieldSecurityProfileIsSecuredMissingError<br />**Hex**:<br />80048063<br />**Number**:<br />-2147188637|Some field security permissions could not be imported because the following fields are not securable: {0}.|
> |**Name**:<br />ImportFieldXmlError<br />**Hex**:<br />80048006<br />**Number**:<br />-2147188730|The number of format parameters passed into the input string is incorrect|
> |**Name**:<br />ImportFileFailed<br />**Hex**:<br />80050125<br />**Number**:<br />-2147155675|Import and extraction of the file failed.|
> |**Name**:<br />ImportFileSignatureInvalid<br />**Hex**:<br />80048065<br />**Number**:<br />-2147188635|The import file has an invalid digital signature.|
> |**Name**:<br />ImportFileTooLargeToUpload<br />**Hex**:<br />80040375<br />**Number**:<br />-2147220619|The import file is too large to upload.|
> |**Name**:<br />ImportFormXmlError<br />**Hex**:<br />80048007<br />**Number**:<br />-2147188729|The number of format parameters passed into the input string is incorrect|
> |**Name**:<br />ImportGenericEntitiesError<br />**Hex**:<br />80048020<br />**Number**:<br />-2147188704|An error occurred while importing generic entities.|
> |**Name**:<br />ImportGenericError<br />**Hex**:<br />8004801E<br />**Number**:<br />-2147188706|The import failed. For more information, see the related error messages.|
> |**Name**:<br />ImportHierarchyRuleDeletedError<br />**Hex**:<br />8004F9A1<br />**Number**:<br />-2147157599|A hierarchy rule with the same id is marked as deleted in the system,So first publish the customized entity and import again.|
> |**Name**:<br />ImportHierarchyRuleExistingError<br />**Hex**:<br />8004F9A2<br />**Number**:<br />-2147157598|Cannot reuse existing hierarchy rule.|
> |**Name**:<br />ImportHierarchyRuleOtcMismatchError<br />**Hex**:<br />8004F9A3<br />**Number**:<br />-2147157597|There was an error processing hierarchy rules of the same object type code.(unresolvable system collision)|
> |**Name**:<br />ImportInvalidFileError<br />**Hex**:<br />80048000<br />**Number**:<br />-2147188736|Invalid Import File|
> |**Name**:<br />ImportInvalidXmlError<br />**Hex**:<br />8004802C<br />**Number**:<br />-2147188692|This solution package cannot be imported because it contains invalid XML. You can attempt to repair the file by manually editing the XML contents using the information found in the schema validation errors, or you can contact your solution provider.|
> |**Name**:<br />ImportIsvConfigError<br />**Hex**:<br />8004800E<br />**Number**:<br />-2147188722|There was an error parsing the IsvConfig during Import|
> |**Name**:<br />ImportLanguagesIgnoredError<br />**Hex**:<br />80048026<br />**Number**:<br />-2147188698|Translated labels for the following languages could not be imported because they have not been enabled for this organization: {0}|
> |**Name**:<br />ImportMailMergeTemplateEntityMissingError<br />**Hex**:<br />80048480<br />**Number**:<br />-2147187584|The {0} mail merge template was not imported because the {1} entity associated with this template is not in the target system.|
> |**Name**:<br />ImportMailMergeTemplateError<br />**Hex**:<br />80048456<br />**Number**:<br />-2147187626|There was an error in parsing the mail merge templates in Import Xml|
> |**Name**:<br />ImportMapInUse<br />**Hex**:<br />80048465<br />**Number**:<br />-2147187611|One or more of the selected data maps cannot be deleted because it is currently used in a data import.|
> |**Name**:<br />ImportMappingsInvalidIdSpecified<br />**Hex**:<br />80048427<br />**Number**:<br />-2147187673|The XML file has one or more invalid IDs. The specified ID cannot be used as a unique identifier.|
> |**Name**:<br />ImportMappingsMissingEntityMapError<br />**Hex**:<br />80048010<br />**Number**:<br />-2147188720|This customization file contains a reference to an entity map that does not exist on the target system.|
> |**Name**:<br />ImportMappingsSystemMapError<br />**Hex**:<br />8004800F<br />**Number**:<br />-2147188721|Import cannot create system attribute mappings|
> |**Name**:<br />ImportMissingComponent<br />**Hex**:<br />8004801F<br />**Number**:<br />-2147188705|Cannot add a Root Component {0} of type {1} because it is not in the target system.|
> |**Name**:<br />ImportMissingDependenciesError<br />**Hex**:<br />8004801D<br />**Number**:<br />-2147188707|The following solution cannot be imported: {0}. Some dependencies are missing.|
> |**Name**:<br />ImportMissingRootComponentEntry<br />**Hex**:<br />8004803A<br />**Number**:<br />-2147188678|The import has failed because component {0} of type {1} is not declared in the solution file as a root component. To fix this, import again using the XML file that was generated when you exported the solution.|
> |**Name**:<br />ImportMobileOfflineProfileError<br />**Hex**:<br />8006099F<br />**Number**:<br />-2147087969|An error occurred while importing Mobile Offline Profiles.|
> |**Name**:<br />ImportNewPluginTypesError<br />**Hex**:<br />80048071<br />**Number**:<br />-2147188623|Existing plug-in types have been removed. Please update major or minor verion of plug-in assembly.|
> |**Name**:<br />ImportNonWellFormedFileError<br />**Hex**:<br />80048013<br />**Number**:<br />-2147188717|Invalid customization file. This file is not well formed.|
> |**Name**:<br />ImportNotComplete<br />**Hex**:<br />80048472<br />**Number**:<br />-2147187598|One or more imports are not in completed state. Imported records can only be deleted from completed jobs. Wait until job completes, and then try again.|
> |**Name**:<br />ImportOperationChildFailure<br />**Hex**:<br />80044334<br />**Number**:<br />-2147204300|One or more of the Import Child Jobs Failed|
> |**Name**:<br />ImportOptionSetAttributeError<br />**Hex**:<br />80048039<br />**Number**:<br />-2147188679|Attribute '{0}' was not imported as it references a non-existing global Option Set ('{1}').|
> |**Name**:<br />ImportOptionSetsError<br />**Hex**:<br />80048030<br />**Number**:<br />-2147188688|An error occurred while importing OptionSets.|
> |**Name**:<br />ImportOrgSettingsError<br />**Hex**:<br />80048019<br />**Number**:<br />-2147188711|There was an error parsing the Organization Settings during Import.|
> |**Name**:<br />ImportPluginTypesError<br />**Hex**:<br />80048012<br />**Number**:<br />-2147188718|An error occurred while importing plug-in types.|
> |**Name**:<br />ImportRelationshipRoleMapsError<br />**Hex**:<br />8004800A<br />**Number**:<br />-2147188726|The number of format parameters passed into the input string is incorrect|
> |**Name**:<br />ImportRelationshipRolesError<br />**Hex**:<br />80048009<br />**Number**:<br />-2147188727|The number of format parameters passed into the input string is incorrect|
> |**Name**:<br />ImportRelationshipRolesPrivilegeError<br />**Hex**:<br />8004802F<br />**Number**:<br />-2147188689|{0} cannot be imported. The {1} privilege is required to import this component.|
> |**Name**:<br />ImportReportsError<br />**Hex**:<br />80048032<br />**Number**:<br />-2147188686|An error occurred while importing Reports.|
> |**Name**:<br />ImportRestrictedSolutionError<br />**Hex**:<br />8004F007<br />**Number**:<br />-2147160057|Solution ID provided is restricted and cannot be imported.|
> |**Name**:<br />ImportRibbonsError<br />**Hex**:<br />80048031<br />**Number**:<br />-2147188687|An error occurred while importing Ribbons.|
> |**Name**:<br />ImportRoleError<br />**Hex**:<br />80048017<br />**Number**:<br />-2147188713|Cannot import security role. The role with specified role id is not updatable or role name is not unique.|
> |**Name**:<br />ImportRolePermissionError<br />**Hex**:<br />80048018<br />**Number**:<br />-2147188712|You do not have the necessary privileges to import security roles.|
> |**Name**:<br />ImportRoutingRuleError<br />**Hex**:<br />8004F867<br />**Number**:<br />-2147157913|An error occurred while importing Routing Rule Sets.|
> |**Name**:<br />ImportSavedQueryDeletedError<br />**Hex**:<br />8004801B<br />**Number**:<br />-2147188709|A saved query with the same id is marked as deleted in the system. Please first publish the customized entity and import again.|
> |**Name**:<br />ImportSavedQueryExistingError<br />**Hex**:<br />80048005<br />**Number**:<br />-2147188731|The number of format parameters passed into the input string is incorrect|
> |**Name**:<br />ImportSavedQueryOtcMismatchError<br />**Hex**:<br />80048004<br />**Number**:<br />-2147188732|There was an error processing saved queries of the same object type code (unresolvable system collision)|
> |**Name**:<br />ImportSdkMessagesError<br />**Hex**:<br />80048016<br />**Number**:<br />-2147188714|An error occurred while importing Sdk Messages.|
> |**Name**:<br />ImportSiteMapError<br />**Hex**:<br />80048011<br />**Number**:<br />-2147188719|An error occurred while importing the Site Map.|
> |**Name**:<br />ImportSlaError<br />**Hex**:<br />8004F868<br />**Number**:<br />-2147157912|An error occurred while importing SLAs.|
> |**Name**:<br />ImportSolutionError<br />**Hex**:<br />80048033<br />**Number**:<br />-2147188685|An error occurred while importing a Solution.|
> |**Name**:<br />ImportSolutionIsvConfigWarning<br />**Hex**:<br />80048042<br />**Number**:<br />-2147188670|ISV Config was overwritten.|
> |**Name**:<br />ImportSolutionManagedError<br />**Hex**:<br />80048038<br />**Number**:<br />-2147188680|Solution '{0}' already exists in this system as managed and cannot be upgraded.|
> |**Name**:<br />ImportSolutionManagedToUnmanagedMismatch<br />**Hex**:<br />80048040<br />**Number**:<br />-2147188672|The solution is already installed on this system as an unmanaged solution and the package supplied is attempting to install it in managed mode. Import can only update solutions when the modes match. Uninstall the current solution and try again.|
> |**Name**:<br />ImportSolutionOrganizationSettingsWarning<br />**Hex**:<br />80048044<br />**Number**:<br />-2147188668|Organization settings were overwritten.|
> |**Name**:<br />ImportSolutionPackageInvalidSku<br />**Hex**:<br />8004806B<br />**Number**:<br />-2147188629|The solution package you are importing was generated on Microsoft Dynamics 365 Online, it cannot be imported into on-premises or hosted versions of Microsoft Dynamics 365.|
> |**Name**:<br />ImportSolutionPackageInvalidSolutionPackageVersion<br />**Hex**:<br />80048068<br />**Number**:<br />-2147188632|You can only import solutions with a package version of {0} or earlier into this organization. Also, you can't import any solutions into this organization that were exported from Microsoft Dynamics 365 2011 or earlier.|
> |**Name**:<br />ImportSolutionPackageMinimumVersionNeeded<br />**Hex**:<br />00000001<br />**Number**:<br />1|Deprecated, not removing now as it might cause issues during integrations.|
> |**Name**:<br />ImportSolutionPackageNeedsUpgrade<br />**Hex**:<br />80048067<br />**Number**:<br />-2147188633|The solution package you are importing was generated on a different version of Microsoft Dynamics 365. The system will attempt to transform the package prior to import. Package Version: {0} {1}, System Version: {2} {3}.|
> |**Name**:<br />ImportSolutionPackageNotValid<br />**Hex**:<br />80048066<br />**Number**:<br />-2147188634|The solution package you are importing was generated on a version of Microsoft Dynamics 365 that cannot be imported into this system. Package Version: {0} {1}, System Version: {2} {3}.|
> |**Name**:<br />ImportSolutionPackageRequiresOptInAvailable<br />**Hex**:<br />80048069<br />**Number**:<br />-2147188631|Some components in the solution package you are importing require opt in. Opt in is available, please consult your administrator.|
> |**Name**:<br />ImportSolutionPackageRequiresOptInNotAvailable<br />**Hex**:<br />8004806A<br />**Number**:<br />-2147188630|The solution package you are importing was generated on a SKU of Microsoft Dynamics 365 that supports opt in. It cannot be imported in your system.|
> |**Name**:<br />ImportSolutionSiteMapWarning<br />**Hex**:<br />80048043<br />**Number**:<br />-2147188669|SiteMap was overwritten.|
> |**Name**:<br />ImportSolutionUnmanagedToManagedMismatch<br />**Hex**:<br />80048041<br />**Number**:<br />-2147188671|The solution is already installed on this system as a managed solution and the package supplied is attempting to install it in unmanaged mode. Import can only update solutions when the modes match. Uninstall the current solution and try again.|
> |**Name**:<br />ImportSystemSolutionError<br />**Hex**:<br />80048046<br />**Number**:<br />-2147188666|System solution cannot be imported.|
> |**Name**:<br />ImportTemplateLanguageIgnored<br />**Hex**:<br />8004847a<br />**Number**:<br />-2147187590|You cannot import this template because its language is not enabled in your Microsoft Dynamics 365 organization.|
> |**Name**:<br />ImportTemplatePersonalIgnored<br />**Hex**:<br />8004847b<br />**Number**:<br />-2147187589|You cannot import this template because it is set as "personal" in your Microsoft Dynamics 365 organization.|
> |**Name**:<br />ImportTranslationMissingSolutionError<br />**Hex**:<br />80048047<br />**Number**:<br />-2147188665|An error occurred while importing the translations. The solution associated with the translations does not exist in this system.|
> |**Name**:<br />ImportTranslationsBadZipFileError<br />**Hex**:<br />80048061<br />**Number**:<br />-2147188639|The translation file is invalid. The compressed file must contain the following files at its root: {0}, [Content_Types].xml.|
> |**Name**:<br />ImportVisualizationDeletedError<br />**Hex**:<br />8004E013<br />**Number**:<br />-2147164141|A saved query visualization with id {0} is marked for deletion in the system. Please publish the customized entity first and then import again.|
> |**Name**:<br />ImportVisualizationExistingError<br />**Hex**:<br />8004E014<br />**Number**:<br />-2147164140|A saved query visualization with id {0} already exists in the system, and cannot be resused by a new custom entity.|
> |**Name**:<br />ImportWillExceedCustomEntityQuota<br />**Hex**:<br />8004b043<br />**Number**:<br />-2147176381|This import process is trying to import {0} new custom entities. This would exceed the custom entity limits for this organization.|
> |**Name**:<br />ImportWorkflowAttributeDependencyError<br />**Hex**:<br />80048022<br />**Number**:<br />-2147188702|Cannot import workflow definition. Required attribute dependency is missing.|
> |**Name**:<br />ImportWorkflowEntityDependencyError<br />**Hex**:<br />80048023<br />**Number**:<br />-2147188701|Cannot import workflow definition. Required entity dependency is missing.|
> |**Name**:<br />ImportWorkflowError<br />**Hex**:<br />80048021<br />**Number**:<br />-2147188703|Cannot import workflow definition. The workflow with specified workflow id is not updatable or workflow name is not unique.|
> |**Name**:<br />ImportWorkflowNameConflictError<br />**Hex**:<br />80048027<br />**Number**:<br />-2147188697|Workflow {0} cannot be imported because a workflow with same name and different unique identifier exists in the target system. Change the name of this workflow, and then try again.|
> |**Name**:<br />ImportWorkflowPublishedError<br />**Hex**:<br />80048028<br />**Number**:<br />-2147188696|Workflow {0}({1}) cannot be imported because a workflow with same unique identifier is published on the target system. Unpublish the workflow on the target system before attempting to import this workflow again.|
> |**Name**:<br />ImportWrongPublisherError<br />**Hex**:<br />8004801C<br />**Number**:<br />-2147188708|The following managed solution cannot be imported: {0}. The publisher name cannot be changed from {1} to {2}.|
> |**Name**:<br />ImportXsdValidationError<br />**Hex**:<br />8004801A<br />**Number**:<br />-2147188710|The import file is invalid. XSD validation failed with the following error: '{0}'. The validation failed at: '...{1} <<<<<ERROR LOCATION>>>>> {2}...'."|
> |**Name**:<br />InaccessibleSmtpServer<br />**Hex**:<br />8005E227<br />**Number**:<br />-2147098073|Cannot reach to the smtp server. Please check that the smtp server is accessible.|
> |**Name**:<br />InactiveEmailServerProfile<br />**Hex**:<br />8005E228<br />**Number**:<br />-2147098072|Email server profile is disabled. Cannot process email for disabled profile.|
> |**Name**:<br />InactiveMailbox<br />**Hex**:<br />8005E219<br />**Number**:<br />-2147098087|The mailbox is in inactive state. Send/Receive mails are allowed only for active mailboxes.|
> |**Name**:<br />InactiveMetricSetOnGoal<br />**Hex**:<br />8004F686<br />**Number**:<br />-2147158394|An inactive metric cannot be set on a goal.|
> |**Name**:<br />InactiveRollupQuerySetOnGoal<br />**Hex**:<br />8004F685<br />**Number**:<br />-2147158395|An inactive rollup query cannot be set on a goal.|
> |**Name**:<br />IncidentCannotCancel<br />**Hex**:<br />8004440e<br />**Number**:<br />-2147204082|The incident can not be cancelled because there are open activities for this incident.|
> |**Name**:<br />IncidentContractDoesNotHaveAllotments<br />**Hex**:<br />80044403<br />**Number**:<br />-2147204093|The contract does not have enough allotments. The case can not be created against this contract.|
> |**Name**:<br />IncidentInvalidAllotmentType<br />**Hex**:<br />8004440b<br />**Number**:<br />-2147204085|The allotment type for the contract is invalid.|
> |**Name**:<br />IncidentInvalidContractLineStateForCreate<br />**Hex**:<br />8004440d<br />**Number**:<br />-2147204083|The case can not be created against this contract line item because the contract line item is cancelled or expired.|
> |**Name**:<br />IncidentInvalidContractStateForCreate<br />**Hex**:<br />80044400<br />**Number**:<br />-2147204096|The case can not be created against this contract because of the contract state.|
> |**Name**:<br />IncidentIsAlreadyClosedOrCancelled<br />**Hex**:<br />80044411<br />**Number**:<br />-2147204079|Already Closed or Canceled|
> |**Name**:<br />IncidentMissingActivityRegardingObject<br />**Hex**:<br />80044409<br />**Number**:<br />-2147204087|The incident id is missing.|
> |**Name**:<br />IncidentMissingContractDetail<br />**Hex**:<br />80044401<br />**Number**:<br />-2147204095|The contract detail id is missing.|
> |**Name**:<br />IncidentNullSpentTimeOrBilled<br />**Hex**:<br />8004440c<br />**Number**:<br />-2147204084|The timespent on the Incident is NULL or IncidentResolution Activity's IsBilled is NULL.|
> |**Name**:<br />IncomingDeliveryIsForwardMailbox<br />**Hex**:<br />8005E223<br />**Number**:<br />-2147098077|Cannot poll mails from the mailbox. Its incoming delivery method is Forward mailbox.|
> |**Name**:<br />IncomingServerLocationAndSslSetToNo<br />**Hex**:<br />8005E23E<br />**Number**:<br />-2147098050|The URL specified for Incoming Server Location uses HTTPS but the Use SSL for Incoming Connection option is set to No. Set this option to Yes, and then try again.|
> |**Name**:<br />IncomingServerLocationAndSslSetToYes<br />**Hex**:<br />8005E240<br />**Number**:<br />-2147098048|The URL specified for Incoming Server Location uses HTTP but the Use SSL for Incoming Connection option is set to Yes. Specify a server location that uses HTTPS, and then try again.|
> |**Name**:<br />IncompatibleStepsEncountered<br />**Hex**:<br />8006088B<br />**Number**:<br />-2147088245|You can't enable the EnforceReadOnlyPlugins setting because plug-ins that change data are registered on read-only SDK messages. {0}|
> |**Name**:<br />IncompleteTransformationParameterMappingsFound<br />**Hex**:<br />8004037d<br />**Number**:<br />-2147220611|One or more mandatory transformation parameters do not have mappings defined for them.|
> |**Name**:<br />InconsistentAttributeNameCasing<br />**Hex**:<br />8004F043<br />**Number**:<br />-2147159997|Detected inconsistent attribute name casing, expected: {0}, actual: {1}.|
> |**Name**:<br />InconsistentProductRelationshipState<br />**Hex**:<br />8004F996<br />**Number**:<br />-2147157610|The other row for the product relationship is not available.|
> |**Name**:<br />IncorrectActiveStageEntity<br />**Hex**:<br />80060462<br />**Number**:<br />-2147089310|Active stage is not on '{0}' entity.|
> |**Name**:<br />IncorrectAttributeValueType<br />**Hex**:<br />80044354<br />**Number**:<br />-2147204268|Invalid Attribute Value Type for {0}. Expected: {1}, Found: {2}|
> |**Name**:<br />IncorrectEntitySetName<br />**Hex**:<br />8006089C<br />**Number**:<br />-2147088228|The entity set name {0} must start with a valid customization prefix.|
> |**Name**:<br />IncorrectSingleFileMultipleEntityMap<br />**Hex**:<br />80048502<br />**Number**:<br />-2147187454|There should be two or more Entity Mappings defined when EntitiesPerFile in ImportMap is set to Multiple|
> |**Name**:<br />IncreasingDaysWillResetMobileOfflineData<br />**Hex**:<br />80060991<br />**Number**:<br />-2147087983|Increasing the number of days will cause a reset of mobile offline data and a resynchronization with mobile devices.|
> |**Name**:<br />IndexOutOfRange<br />**Hex**:<br />8005E008<br />**Number**:<br />-2147098616|The index {0} is out of range for {1}. Number of elements present are {2}.|
> |**Name**:<br />IndexSizeConstraintViolated<br />**Hex**:<br />80060895<br />**Number**:<br />-2147088235|Index size exceeded the size limit of {0} bytes. The key is too large. Try removing some columns or making the strings in string columns shorter.|
> |**Name**:<br />InitializeErrorNoReadOnSource<br />**Hex**:<br />8004F800<br />**Number**:<br />-2147158016|The operation could not be completed because you donot have read access on some of the fields in {0} record.|
> |**Name**:<br />InputParameterFieldIncorrect<br />**Hex**:<br />80060378<br />**Number**:<br />-2147089544|Input parameter “{0}” does not match the input parameter field configured. Contact your system administrator to check the configuration metadata if the error persists.|
> |**Name**:<br />InsertOptionValueInvalidType<br />**Hex**:<br />80044320<br />**Number**:<br />-2147204320|You can add option values only to picklist and status attributes.|
> |**Name**:<br />InstanceOutsideEffectiveRange<br />**Hex**:<br />8004E115<br />**Number**:<br />-2147163883|Cannot perform the operation. An instance is outside of series effective expansion range.|
> |**Name**:<br />InsufficientAccessMode<br />**Hex**:<br />80044502<br />**Number**:<br />-2147203838|User does not have read-write access to the Dynamics 365 organization.|
> |**Name**:<br />InsufficientAuthTicket<br />**Hex**:<br />8004A103<br />**Number**:<br />-2147180285|The ticket specified for authentication didn't meet policy|
> |**Name**:<br />InsufficientColumnsInSubQuery<br />**Hex**:<br />8004E022<br />**Number**:<br />-2147164126|One or more columns required by the outer query are not available from the sub-query.|
> |**Name**:<br />InsufficientCreatePrivilege<br />**Hex**:<br />8006110A<br />**Number**:<br />-2147086070|External Party don't have sufficient privilege to create new record with given parameters.|
> |**Name**:<br />InsufficientPrivilegesSupportUser<br />**Hex**:<br />80048345<br />**Number**:<br />-2147187899|Support user does not have permission to perform this operation.|
> |**Name**:<br />InsufficientPrivilegeToQueueOwner<br />**Hex**:<br />80040520<br />**Number**:<br />-2147220192|The owner of this queue does not have sufficient privileges to work with the queue.|
> |**Name**:<br />InsufficientRetrievePrivilege<br />**Hex**:<br />80061109<br />**Number**:<br />-2147086071|External Party don't have sufficient privilege to retrieve record.|
> |**Name**:<br />InsufficientTransformationParameters<br />**Hex**:<br />80048506<br />**Number**:<br />-2147187450|Insufficient parameters to execute transformation mapping.|
> |**Name**:<br />InsufficientUpdatePrivilege<br />**Hex**:<br />8006110B<br />**Number**:<br />-2147086069|External Party don't have sufficient privilege to update record.|
> |**Name**:<br />IntegerValueOutOfRange<br />**Hex**:<br />8004432F<br />**Number**:<br />-2147204305|A validation error occurred. An integer provided is outside of the allowed values for this attribute.|
> |**Name**:<br />IntegratedAuthenticationIsNotAllowed<br />**Hex**:<br />80044301<br />**Number**:<br />-2147204351|Integrated authentication is not allowed.|
> |**Name**:<br />InvalidAbsoluteUrlFormat<br />**Hex**:<br />80048055<br />**Number**:<br />-2147188651|The absolute url contains invalid characters. Please use a different name. Valid absolute url cannot ends with the following strings: .aspx, .ashx, .asmx, .svc|
> |**Name**:<br />InvalidAccessMaskForTeamTemplate<br />**Hex**:<br />80048335<br />**Number**:<br />-2147187915|Invalid access mask is specified for team template.|
> |**Name**:<br />InvalidAccessModeTransition<br />**Hex**:<br />80041d66<br />**Number**:<br />-2147213978|The client access license cannot be changed because the user does not have a Microsoft Dynamics 365 Online license. To change the access mode, you must first add a license for this user in the Microsoft Online Service portal.|
> |**Name**:<br />InvalidAccessRights<br />**Hex**:<br />8004020d<br />**Number**:<br />-2147220979|Invalid access rights.|
> |**Name**:<br />InvalidAccessRightsPassed<br />**Hex**:<br />80048347<br />**Number**:<br />-2147187897|Invalid Access Rights passed.|
> |**Name**:<br />InvalidActivityMimeAttachmentId<br />**Hex**:<br />80050005<br />**Number**:<br />-2147155963|Invalid activityMimeAttachmentId.|
> |**Name**:<br />InvalidActivityOwnershipTypeMask<br />**Hex**:<br />8004F120<br />**Number**:<br />-2147159776|A custom entity defined as an activity must be user or team owned.|
> |**Name**:<br />InvalidActivityPartyAddress<br />**Hex**:<br />80043518<br />**Number**:<br />-2147207912|One or more activity parties have invalid addresses.|
> |**Name**:<br />InvalidActivityType<br />**Hex**:<br />80040321<br />**Number**:<br />-2147220703|An invalid object type was specified for distributing activities.|
> |**Name**:<br />InvalidActivityTypeForCampaignActivityPropagate<br />**Hex**:<br />8004030f<br />**Number**:<br />-2147220721|Must specify a valid CommunicationActivity|
> |**Name**:<br />InvalidActivityTypeForList<br />**Hex**:<br />80040305<br />**Number**:<br />-2147220731|Cannot create activities of the specified list type.|
> |**Name**:<br />InvalidActivityXml<br />**Hex**:<br />80043514<br />**Number**:<br />-2147207916|Invalid Xml in an activity config file.|
> |**Name**:<br />InvalidAllotmentsCalc<br />**Hex**:<br />800404ef<br />**Number**:<br />-2147220241|Allotments: remaining + used != total|
> |**Name**:<br />InvalidAllotmentsOverage<br />**Hex**:<br />8004430B<br />**Number**:<br />-2147204341|Allotment overage is invalid.|
> |**Name**:<br />InvalidAllotmentsRemaining<br />**Hex**:<br />800404f2<br />**Number**:<br />-2147220238|The allotments remaining is invalid|
> |**Name**:<br />InvalidAllotmentsTotal<br />**Hex**:<br />800404f0<br />**Number**:<br />-2147220240|The total allotments is invalid|
> |**Name**:<br />InvalidAllotmentsUsed<br />**Hex**:<br />800404f1<br />**Number**:<br />-2147220239|The allotments used is invalid|
> |**Name**:<br />InvalidAmountFreeResourceLimit<br />**Hex**:<br />8004B060<br />**Number**:<br />-2147176352|The resource type {0} cannot have an amount free value of {1}.|
> |**Name**:<br />InvalidAmountProvided<br />**Hex**:<br />8004B02D<br />**Number**:<br />-2147176403|The service component {0} cannot have a provide {1} of resource type {2}.|
> |**Name**:<br />InvalidAppModuleClientType<br />**Hex**:<br />80050126<br />**Number**:<br />-2147155674|The client type value passed is incorrect and not in the valid range.|
> |**Name**:<br />InvalidAppModuleComponent<br />**Hex**:<br />80050113<br />**Number**:<br />-2147155693|The ID {0} doesn’t exist or isn’t valid for the component type “{1}”.|
> |**Name**:<br />InvalidAppModuleComponentType<br />**Hex**:<br />80050112<br />**Number**:<br />-2147155694|An app can’t reference the component type “{0}”.|
> |**Name**:<br />InvalidAppModuleEventHandlers<br />**Hex**:<br />8005012F<br />**Number**:<br />-2147155665|The event handlers provided for the app are invalid.|
> |**Name**:<br />InvalidAppModuleId<br />**Hex**:<br />80050116<br />**Number**:<br />-2147155690|The app ID is invalid or you don’t have access to the app.|
> |**Name**:<br />InvalidAppModuleSiteMap<br />**Hex**:<br />80050110<br />**Number**:<br />-2147155696|The customized site map for this app module could not be used because it is configured incorrectly. To resolve this issue, navigate to the full experience to repair the customized site map and import it again.|
> |**Name**:<br />InvalidAppModuleSiteMapXml<br />**Hex**:<br />80050109<br />**Number**:<br />-2147155703|The App Module SiteMap is invalid.|
> |**Name**:<br />InvalidAppModuleUniqueName<br />**Hex**:<br />8005011E<br />**Number**:<br />-2147155682|The unique name exceeds the maximum length of 40 characters or contains invalid characters. Only letters and numbers are allowed.|
> |**Name**:<br />InvalidAppModuleUrl<br />**Hex**:<br />8005011A<br />**Number**:<br />-2147155686|The app URL is not unique or the format is invalid.|
> |**Name**:<br />InvalidAppointmentInstance<br />**Hex**:<br />8004E104<br />**Number**:<br />-2147163900|Invalid appointment entity instance.|
> |**Name**:<br />InvalidApproveFromDraftArticle<br />**Hex**:<br />80048dfd<br />**Number**:<br />-2147185155|You are trying to approve an article that has a status of draft. You can only approve an article with the status of unapproved.|
> |**Name**:<br />InvalidApproveFromPublishedArticle<br />**Hex**:<br />80048dfb<br />**Number**:<br />-2147185157|You are trying to approve an article that has a status of published. You can only approve an article with the status of unapproved.|
> |**Name**:<br />InvalidArgument<br />**Hex**:<br />80040203<br />**Number**:<br />-2147220989|Invalid argument.|
> |**Name**:<br />InvalidArticleState<br />**Hex**:<br />800404fb<br />**Number**:<br />-2147220229|The article state is undefined|
> |**Name**:<br />InvalidArticleStateTransition<br />**Hex**:<br />800404fc<br />**Number**:<br />-2147220228|This article state transition is invalid because of the current state of the article|
> |**Name**:<br />InvalidArticleTemplateState<br />**Hex**:<br />800404fd<br />**Number**:<br />-2147220227|The article template state is undefined|
> |**Name**:<br />InvalidAssemblyProcessorArchitecture<br />**Hex**:<br />8004417E<br />**Number**:<br />-2147204738|The given plugin assembly was built with an unsupported target platform and cannot be loaded.|
> |**Name**:<br />InvalidAssemblySourceType<br />**Hex**:<br />8004417D<br />**Number**:<br />-2147204739|The given plugin assembly source type is not supported for isolated plugin assemblies.|
> |**Name**:<br />InvalidAssigneeId<br />**Hex**:<br />80040210<br />**Number**:<br />-2147220976|Invalid assignee id.|
> |**Name**:<br />InvalidAssociatedSavedQuery<br />**Hex**:<br />800609AE<br />**Number**:<br />-2147087954|Selected saved query does not belong to associated entity of the mobile offline profile item.|
> |**Name**:<br />InvalidAttachmentsFolder<br />**Hex**:<br />80048490<br />**Number**:<br />-2147187568|The compressed (.zip) file can't be uploaded because the folder "Attachments" contains one or more subfolders. Remove the subfolders and try again.|
> |**Name**:<br />InvalidAttribute<br />**Hex**:<br />8005E009<br />**Number**:<br />-2147098615|Attribute {0} cannot be found for entity {1}.|
> |**Name**:<br />InvalidAttributeDataType<br />**Hex**:<br />80044815<br />**Number**:<br />-2147203051|Attribute data type: {0} is not valid for this entity.|
> |**Name**:<br />InvalidAttributeFieldType<br />**Hex**:<br />80044816<br />**Number**:<br />-2147203050|Attribute field type: {0} is not valid for virtual entity.|
> |**Name**:<br />InvalidAttributeFound<br />**Hex**:<br />8004E303<br />**Number**:<br />-2147163389|A dashboard Form XML cannot contain attribute: {0}.|
> |**Name**:<br />InvalidAttributeInXaml<br />**Hex**:<br />80060412<br />**Number**:<br />-2147089390|Attribute - {0} in the XAML is invalid|
> |**Name**:<br />InvalidAttributeMap<br />**Hex**:<br />80046203<br />**Number**:<br />-2147196413|InvalidAttributeMap Error Occurred|
> |**Name**:<br />InvalidAttributeMapping<br />**Hex**:<br />80048438<br />**Number**:<br />-2147187656|One or more attribute mappings is invalid.|
> |**Name**:<br />InvalidAttributeQuery<br />**Hex**:<br />80072527<br />**Number**:<br />-2147015385|Attributes must be part of the requested EntityMetadata properties when an AttributeQuery is specified. Expect property = {0} in requested entity properties list.|
> |**Name**:<br />InvalidAuth<br />**Hex**:<br />80048516<br />**Number**:<br />-2147187434|Organization Authentication does not match the current discovery service Role.|
> |**Name**:<br />InvalidAuthTicket<br />**Hex**:<br />8004A100<br />**Number**:<br />-2147180288|The ticket specified for authentication didn't pass validation|
> |**Name**:<br />InvalidBaseAttributeError<br />**Hex**:<br />80044242<br />**Number**:<br />-2147204542|Invalid Base attribute.|
> |**Name**:<br />InvalidBaseUnit<br />**Hex**:<br />80043b0b<br />**Number**:<br />-2147206389|The base unit does not belong to the schedule.|
> |**Name**:<br />InvalidBehavior<br />**Hex**:<br />800608A1<br />**Number**:<br />-2147088223|The Behavior value of this attribute can't be changed.|
> |**Name**:<br />InvalidBehaviorSelection<br />**Hex**:<br />800608A0<br />**Number**:<br />-2147088224|The behavior of this Date and Time field can only be changed to “Date Only".|
> |**Name**:<br />InvalidBrowserToConfigureOrganization<br />**Hex**:<br />8004D255<br />**Number**:<br />-2147167659|Browser not compatible to configure organization|
> |**Name**:<br />InvalidBusinessProcess<br />**Hex**:<br />80060389<br />**Number**:<br />-2147089527|Invalid Business Process.|
> |**Name**:<br />InvalidCaller<br />**Hex**:<br />80040257<br />**Number**:<br />-2147220905|Cannot switch ExecutionContext to system user without setting Caller first.|
> |**Name**:<br />InvalidCascadeLinkType<br />**Hex**:<br />80048204<br />**Number**:<br />-2147188220|The cascade link type is not valid for the cascade action.|
> |**Name**:<br />InvalidCategory<br />**Hex**:<br />8004E009<br />**Number**:<br />-2147164151|Category is invalid. All the measures in the category either do not have same primary group by or are a mix of aggregate and non-aggregate data.|
> |**Name**:<br />InvalidCertificate<br />**Hex**:<br />8005E23A<br />**Number**:<br />-2147098054|The given certificate is invalid.|
> |**Name**:<br />InvalidChangeProcess<br />**Hex**:<br />80092002<br />**Number**:<br />-2146885630|Invalid change process status request. Current process status is {0}, which cannot transition to {1}.|
> |**Name**:<br />InvalidChannelForCampaignActivityPropagate<br />**Hex**:<br />80040310<br />**Number**:<br />-2147220720|Cannot distribute activities for campaign activities of the specified channel type.|
> |**Name**:<br />InvalidChannelOrigin<br />**Hex**:<br />80060602<br />**Number**:<br />-2147088894|An entitlement channel term with the same channel already exists. Specify a different channel and try again.|
> |**Name**:<br />InvalidCharactersInField<br />**Hex**:<br />80040278<br />**Number**:<br />-2147220872|The field '{0}' contains one or more invalid characters.|
> |**Name**:<br />InvalidClassIdInReferencePanelSection<br />**Hex**:<br />80061503<br />**Number**:<br />-2147085053|Reference Panel section can have only sub-grid, quick view form, knowledge base search, i-frame and HTML web resource controls. Found control with invalid classid {0}.|
> |**Name**:<br />InvalidCollectionName<br />**Hex**:<br />8006088E<br />**Number**:<br />-2147088242|An entity with that collection name already exists. Specify a unique name.|
> |**Name**:<br />InvalidColumnMapping<br />**Hex**:<br />80040377<br />**Number**:<br />-2147220617|ColumnMapping is Invalid. Check that the target attribute exists.|
> |**Name**:<br />InvalidColumnNumber<br />**Hex**:<br />80040336<br />**Number**:<br />-2147220682|The column number specified in the data map does not exist.|
> |**Name**:<br />InvalidCommand<br />**Hex**:<br />8005E100<br />**Number**:<br />-2147098368|Invalid command.|
> |**Name**:<br />InvalidComplexControlId<br />**Hex**:<br />8005E103<br />**Number**:<br />-2147098365|The complex control id is invalid.|
> |**Name**:<br />InvalidConnectionString<br />**Hex**:<br />8004023f<br />**Number**:<br />-2147220929|The connection string not found or invalid.|
> |**Name**:<br />InvalidContractDetailId<br />**Hex**:<br />800404f6<br />**Number**:<br />-2147220234|The Contract detail id is invalid|
> |**Name**:<br />InvalidControlClass<br />**Hex**:<br />8004E307<br />**Number**:<br />-2147163385|The dashboard Form XML cannot contain controls elements with class id: {0}.|
> |**Name**:<br />InvalidConversionRule<br />**Hex**:<br />800608F6<br />**Number**:<br />-2147088138|The ConversionRule specified {0} is invalid. Please specify a valid ConversionRule.|
> |**Name**:<br />InvalidCreateOnProtectedComponent<br />**Hex**:<br />8004F011<br />**Number**:<br />-2147160047|You cannot create {0} {1}. Creation cannot be performed when {0} is managed.|
> |**Name**:<br />InvalidCredentialTypeForNonExchangeIncomingConnection<br />**Hex**:<br />8005E214<br />**Number**:<br />-2147098092|For a POP3 email server type, you can only connect using credentials that are specified by a user or queue.|
> |**Name**:<br />InvalidCrmDateTime<br />**Hex**:<br />8004E103<br />**Number**:<br />-2147163901|Invalid CrmDateTime.|
> |**Name**:<br />InvalidCrossEntityOperation<br />**Hex**:<br />80092004<br />**Number**:<br />-2146885628|Invalid cross-entity stage transition. Target entity must be specified.|
> |**Name**:<br />InvalidCrossEntityTargetOperation<br />**Hex**:<br />80092005<br />**Number**:<br />-2146885627|Invalid cross-entity stage transition. Specified target must match {0}.|
> |**Name**:<br />InvalidCurrency<br />**Hex**:<br />80048cfc<br />**Number**:<br />-2147185412|The currency is invalid.|
> |**Name**:<br />InvalidCustomActivityType<br />**Hex**:<br />8004F125<br />**Number**:<br />-2147159771|A custom entity defined as an activity must be of communicaton activity type.|
> |**Name**:<br />InvalidCustomDataDownloadFilters<br />**Hex**:<br />80060996<br />**Number**:<br />-2147087978|You can’t set custom download filters because Record Distribution Criteria isn’t set to Other Data Filters.|
> |**Name**:<br />InvalidCustomer<br />**Hex**:<br />8004022d<br />**Number**:<br />-2147220947|The customer is invalid.|
> |**Name**:<br />InvalidCustomReportingWizardXml<br />**Hex**:<br />80040491<br />**Number**:<br />-2147220335|Invalid wizard xml|
> |**Name**:<br />InvalidDataDescription<br />**Hex**:<br />8004E000<br />**Number**:<br />-2147164160|The data description for the visualization is invalid.|
> |**Name**:<br />InvalidDataDownloadFilterBusinessUnit<br />**Hex**:<br />8005F222<br />**Number**:<br />-2147093982|For an entity owned by the Business Owner, you can only use the following data download filters: All records or Download related data only.|
> |**Name**:<br />InvalidDataDownloadFilterOrganization<br />**Hex**:<br />8005F223<br />**Number**:<br />-2147093981|For an entity owned by the Organization, you can only use the following data download filters: All records or Download related data only.|
> |**Name**:<br />InvalidDataFiltersForBUOwnedEntities<br />**Hex**:<br />80060994<br />**Number**:<br />-2147087980|You can’t set Records Owned By Me or Records Owned By My Team for business unit-owned entities.|
> |**Name**:<br />InvalidDataFiltersForOrgOwnedEntities<br />**Hex**:<br />80060995<br />**Number**:<br />-2147087979|You can’t set the Other Data filter for organization-owned entities.|
> |**Name**:<br />InvalidDataFiltersForUnownedEntities<br />**Hex**:<br />80060993<br />**Number**:<br />-2147087981|You can’t set the All Record or Other Data filters for unowned entities.|
> |**Name**:<br />InvalidDataFormat<br />**Hex**:<br />80040356<br />**Number**:<br />-2147220650|The source data is not in the required format|
> |**Name**:<br />InvalidDataSourceEndPoint<br />**Hex**:<br />80044826<br />**Number**:<br />-2147203034|Invalid URI: A fully qualified URI without a query string must be provided.|
> |**Name**:<br />InvalidDataXml<br />**Hex**:<br />8005E101<br />**Number**:<br />-2147098367|Invalid data xml.|
> |**Name**:<br />InvalidDateAttribute<br />**Hex**:<br />80044805<br />**Number**:<br />-2147203067|Date Attribute specified is not an attribute of Source Entity.|
> |**Name**:<br />InvalidDateTime<br />**Hex**:<br />80040239<br />**Number**:<br />-2147220935|The date-time format is invalid, or value is outside the supported range.|
> |**Name**:<br />InvalidDateTimeFormat<br />**Hex**:<br />800608A2<br />**Number**:<br />-2147088222|You can’t change the format value of this attribute to “Date and Time” when the behavior is “Date Only.”|
> |**Name**:<br />InvalidDaysInFebruary<br />**Hex**:<br />8004E124<br />**Number**:<br />-2147163868|February 29 can occur only when pattern start date is in a leap year.|
> |**Name**:<br />InvalidDeactivateFormType<br />**Hex**:<br />8004F660<br />**Number**:<br />-2147158432|You can’t deactivate {0} forms. Only Main forms can be inactive.|
> |**Name**:<br />InvalidDeleteModification<br />**Hex**:<br />80048203<br />**Number**:<br />-2147188221|A system relationship's delete cascading action cannot be modified.|
> |**Name**:<br />InvalidDeleteOnProtectedComponent<br />**Hex**:<br />8004F013<br />**Number**:<br />-2147160045|You cannot delete {0} {1}. Deletion cannot be performed when {0} is managed.|
> |**Name**:<br />InvalidDeleteProcess<br />**Hex**:<br />80060691<br />**Number**:<br />-2147088751|This process can't be deleted because it is a system-generated process.|
> |**Name**:<br />InvalidDependency<br />**Hex**:<br />8004F036<br />**Number**:<br />-2147160010|The {2} component {1} (Id={0}) does not exist.  Failure trying to associate it with {3} (Id={4}) as a dependency. Missing dependency lookup type = {5}.|
> |**Name**:<br />InvalidDependencyComponent<br />**Hex**:<br />8004F040<br />**Number**:<br />-2147160000|The required component {1} (Id={0}) that was defined for the {2} could not be found in the system.|
> |**Name**:<br />InvalidDependencyEntity<br />**Hex**:<br />8004F041<br />**Number**:<br />-2147159999|The required component {1} (Name={0}) that was defined for the {2} could not be found in the system.|
> |**Name**:<br />InvalidDependencyFetchXml<br />**Hex**:<br />8004F037<br />**Number**:<br />-2147160009|The FetchXml ({2}) is invalid.  Failure while calculating dependencies for {1} (Id={0}).|
> |**Name**:<br />InvalidDeviceToConfigureOrganization<br />**Hex**:<br />8004D254<br />**Number**:<br />-2147167660|Mobile device cannot be used to configured organization|
> |**Name**:<br />InvalidDisplayName<br />**Hex**:<br />8004700c<br />**Number**:<br />-2147192820|The specified display name is not valid|
> |**Name**:<br />InvalidDocumentTemplate<br />**Hex**:<br />800608CB<br />**Number**:<br />-2147088181|Invalid document template.|
> |**Name**:<br />InvalidDomainName<br />**Hex**:<br />80048015<br />**Number**:<br />-2147188715|The domain logon for this user is invalid. Select another domain logon and try again.|
> |**Name**:<br />InvalidDundasPresentationDescription<br />**Hex**:<br />8004E016<br />**Number**:<br />-2147164138|The presentation description is not valid for dundas chart.|
> |**Name**:<br />InvalidElementFound<br />**Hex**:<br />8004E300<br />**Number**:<br />-2147163392|A dashboard Form XML cannot contain element: {0}.|
> |**Name**:<br />InvalidEmail<br />**Hex**:<br />8004B016<br />**Number**:<br />-2147176426|Email generated from the template is not valid|
> |**Name**:<br />InvalidEmailAddressFormat<br />**Hex**:<br />80044192<br />**Number**:<br />-2147204718|Invalid e-mail address. For more information, contact your system administrator.|
> |**Name**:<br />InvalidEmailAddressInMailbox<br />**Hex**:<br />8005E221<br />**Number**:<br />-2147098079|The email address in the mailbox is not correct. Please enter the correct email address to process mails.|
> |**Name**:<br />InvalidEmailServerLocation<br />**Hex**:<br />8005E218<br />**Number**:<br />-2147098088|The server location is either not present or is not valid. Please correct the server location.|
> |**Name**:<br />InvalidEmailTemplate<br />**Hex**:<br />80040313<br />**Number**:<br />-2147220717|Must specify a valid Template Id|
> |**Name**:<br />InvalidEntitlementActivate<br />**Hex**:<br />80060606<br />**Number**:<br />-2147088890|You can't activate an expired, waiting or canceled entitlement.|
> |**Name**:<br />InvalidEntitlementAssociationToCase<br />**Hex**:<br />80060609<br />**Number**:<br />-2147088887|You can't create a case for this entitlement because there are no available terms.|
> |**Name**:<br />InvalidEntitlementCancel<br />**Hex**:<br />80060607<br />**Number**:<br />-2147088889|You can't cancel an entitlement that's in the Draft or Expired state.|
> |**Name**:<br />InvalidEntitlementChannelTerms<br />**Hex**:<br />80060605<br />**Number**:<br />-2147088891|Total terms for a specific case origin on an entitlement channel cannot be more than the total terms of the corresponding entitlement.|
> |**Name**:<br />InvalidEntitlementContacts<br />**Hex**:<br />80044207<br />**Number**:<br />-2147204601|The specified contact isn’t associated with the selected customer.|
> |**Name**:<br />InvalidEntitlementDeactivate<br />**Hex**:<br />80060608<br />**Number**:<br />-2147088888|You can deactivate only entitlements that are active or waiting|
> |**Name**:<br />InvalidEntitlementExpire<br />**Hex**:<br />80060618<br />**Number**:<br />-2147088872|You can't set an entitlement to the Expired state. Active entitlements automatically expire when their end date passes.|
> |**Name**:<br />InvalidEntitlementForSelectedCustomerOrProduct<br />**Hex**:<br />8004F866<br />**Number**:<br />-2147157914|Select an active entitlement that belongs to the specified customer, contact, or product, and then try again.|
> |**Name**:<br />InvalidEntitlementRenew<br />**Hex**:<br />80060610<br />**Number**:<br />-2147088880|You can renew only the entitlements that are expired or canceled.|
> |**Name**:<br />InvalidEntitlementStateAssociateToCase<br />**Hex**:<br />80060611<br />**Number**:<br />-2147088879|You can only associate a case with an active entitlement.|
> |**Name**:<br />InvalidEntitlementTotalTerms<br />**Hex**:<br />800443FF<br />**Number**:<br />-2147204097|Total terms for an entitlement cannot be less than the total terms of any of its corresponding EntitlementChannels.|
> |**Name**:<br />InvalidEntity<br />**Hex**:<br />8005E00C<br />**Number**:<br />-2147098612|Entity {0} cannot be found.|
> |**Name**:<br />InvalidEntityClassException<br />**Hex**:<br />80040249<br />**Number**:<br />-2147220919|Invalid entity class.|
> |**Name**:<br />InvalidEntityForDateAttribute<br />**Hex**:<br />80044812<br />**Number**:<br />-2147203054|Entity For Date Attribute can be either source entity or its parent.|
> |**Name**:<br />InvalidEntityForLinkedAttribute<br />**Hex**:<br />8004F0FD<br />**Number**:<br />-2147159811|Not a valid entity for linked attribute.|
> |**Name**:<br />InvalidEntityForRollup<br />**Hex**:<br />80044813<br />**Number**:<br />-2147203053|The entity {0} is not a valid entity for rollup.|
> |**Name**:<br />InvalidEntityKeyOperation<br />**Hex**:<br />8006088F<br />**Number**:<br />-2147088241|Invalid EntityKey Operation performed : {0}|
> |**Name**:<br />InvalidEntityLogicalName<br />**Hex**:<br />80072493<br />**Number**:<br />-2147015533|Entity name '{0}' is not a valid logical name.|
> |**Name**:<br />InvalidEntityName<br />**Hex**:<br />80048416<br />**Number**:<br />-2147187690|The record type does not match the base record type and the matching record type of the duplicate detection rule.|
> |**Name**:<br />InvalidEntitySetName<br />**Hex**:<br />8006089B<br />**Number**:<br />-2147088229|An entity with the specified entity set name {0} already exists. Specify a unique name.|
> |**Name**:<br />InvalidEntitySpecified<br />**Hex**:<br />800609B1<br />**Number**:<br />-2147087951|The entity is not specified in the template.|
> |**Name**:<br />InvalidExchangeRate<br />**Hex**:<br />80048cfd<br />**Number**:<br />-2147185411|The exchange rate is invalid.|
> |**Name**:<br />InvalidExportProcessFlowNotActivated<br />**Hex**:<br />80060376<br />**Number**:<br />-2147089546|Failed to export Business Process “{0}” because solution does not include corresponding Business Process entity “{1}”. If this is a newly created Business Process in Draft state, activate it once to generate the Business Process entity and include it in the solution. For more information, see http://support.microsoft.com/kb/4337537.|
> |**Name**:<br />InvalidExternalCollectionName<br />**Hex**:<br />80046BA7<br />**Number**:<br />-2147193945|The specified External Collection name is not valid.|
> |**Name**:<br />InvalidExternalName<br />**Hex**:<br />80046BC0<br />**Number**:<br />-2147193920|The specified External name is not valid.|
> |**Name**:<br />InvalidExternalPartyConfiguration<br />**Hex**:<br />8006110F<br />**Number**:<br />-2147086065|Multiple External Party Items are present for request parameters.|
> |**Name**:<br />InvalidExternalPartyOperation<br />**Hex**:<br />80061111<br />**Number**:<br />-2147086063|External Party is not allowed.|
> |**Name**:<br />InvalidExternalPartyParent<br />**Hex**:<br />80061110<br />**Number**:<br />-2147086064|External Party has invalid parent attribute.|
> |**Name**:<br />InvalidFeatureType<br />**Hex**:<br />80044272<br />**Number**:<br />-2147204494|The feature type isn’t valid.|
> |**Name**:<br />InvalidFetchCollection<br />**Hex**:<br />8004E019<br />**Number**:<br />-2147164135|The fetch collection for the visualization is invalid.|
> |**Name**:<br />InvalidFetchXml<br />**Hex**:<br />80040303<br />**Number**:<br />-2147220733|Malformed FetchXml.|
> |**Name**:<br />InvalidFileBadCharacters<br />**Hex**:<br />80040396<br />**Number**:<br />-2147220586|The file could not be uploaded because it contains invalid character(s)|
> |**Name**:<br />InvalidFileType<br />**Hex**:<br />800608CC<br />**Number**:<br />-2147088180|Invalid File Type.|
> |**Name**:<br />InvalidFilterCriteriaForVisualization<br />**Hex**:<br />8004E01E<br />**Number**:<br />-2147164130|The visualization cannot be rendered for the given filter criteria.|
> |**Name**:<br />InvalidFiscalPeriod<br />**Hex**:<br />80044814<br />**Number**:<br />-2147203052|The fiscal period {0} does not fall in the permitted range of fiscal periods as per organization's fiscal settings.|
> |**Name**:<br />InvalidFlowProcessClientData<br />**Hex**:<br />80060468<br />**Number**:<br />-2147089304|Flow clientdata is in invalid format. Details: "{0}".|
> |**Name**:<br />InvalidFormatForControl<br />**Hex**:<br />80060875<br />**Number**:<br />-2147088267|Invalid Precision Parameter specified for control {0}. It Dosent Contain Expected Value|
> |**Name**:<br />InvalidFormatForDataDelimiter<br />**Hex**:<br />80040355<br />**Number**:<br />-2147220651|Mismatched data delimiter: only one delimiter was found.|
> |**Name**:<br />InvalidFormatForUpdateMode<br />**Hex**:<br />8004F601<br />**Number**:<br />-2147158527|The file that you uploaded is invalid and cannot be used for updating records.|
> |**Name**:<br />InvalidFormatParameters<br />**Hex**:<br />80047101<br />**Number**:<br />-2147192575|The number of format parameters passed into the input string is incorrect|
> |**Name**:<br />InvalidFormType<br />**Hex**:<br />8004E306<br />**Number**:<br />-2147163386|The type of the form must be set to {0} in the Form XML.|
> |**Name**:<br />InvalidFormTypeCalledThroughSdk<br />**Hex**:<br />80060874<br />**Number**:<br />-2147088268|"Invalid Formtype used in Create call|
> |**Name**:<br />InvalidForOfficeGraph<br />**Hex**:<br />80044231<br />**Number**:<br />-2147204559|One or both entities are not enabled for officegraph and they cannot be used for officegraph.|
> |**Name**:<br />InvalidGoalAttribute<br />**Hex**:<br />8004480b<br />**Number**:<br />-2147203061|Goal Attribute does not match the specified metric type.|
> |**Name**:<br />InvalidGoalManager<br />**Hex**:<br />8004F684<br />**Number**:<br />-2147158396|The manager of a goal can only be a user and not a team.|
> |**Name**:<br />InvalidGranularityValue<br />**Hex**:<br />8004B038<br />**Number**:<br />-2147176392|The Granularity column value is incorrect. Each rule part must be a name-value pair separated by an equal sign (=). For example: FREQ=Minutes;INTERVAL=15|
> |**Name**:<br />InvalidGroupByAlias<br />**Hex**:<br />8004E00F<br />**Number**:<br />-2147164145|Data Description is invalid. Same group by alias cannot be used for different attributes.|
> |**Name**:<br />InvalidGroupByColumn<br />**Hex**:<br />8004E01D<br />**Number**:<br />-2147164131|Group by not allowed on the attribute.|
> |**Name**:<br />InvalidGuid<br />**Hex**:<br />80040363<br />**Number**:<br />-2147220637|The globally unique identifier (GUID) in this row is invalid|
> |**Name**:<br />InvalidGuidInXaml<br />**Hex**:<br />80060407<br />**Number**:<br />-2147089401|Guid - {0} in the Xaml is not valid|
> |**Name**:<br />InvalidHeaderColumn<br />**Hex**:<br />80040344<br />**Number**:<br />-2147220668|The column heading contains an invalid combination of data delimiters.|
> |**Name**:<br />InvalidHexColorValue<br />**Hex**:<br />800608D0<br />**Number**:<br />-2147088176|Only hexadecimal values are allowed.|
> |**Name**:<br />InvalidHierarchicalRelationship<br />**Hex**:<br />8004701F<br />**Number**:<br />-2147192801|This relationship is not self-referential and therefore cannot be made hierarchical.|
> |**Name**:<br />InvalidHierarchicalRelationshipChange<br />**Hex**:<br />8004701a<br />**Number**:<br />-2147192806|You can’t change this entity’s hierarchy because the {0} hierarchical relationship can’t be customized.|
> |**Name**:<br />InvalidImportFileContent<br />**Hex**:<br />80040374<br />**Number**:<br />-2147220620|The content of the import file is not valid. You must select a text file.|
> |**Name**:<br />InvalidImportFileData<br />**Hex**:<br />80040351<br />**Number**:<br />-2147220655|The data is not in the required format|
> |**Name**:<br />InvalidImportFileParseData<br />**Hex**:<br />80040349<br />**Number**:<br />-2147220663|Field and data delimiters for this file are not specified.|
> |**Name**:<br />InvalidImportJobId<br />**Hex**:<br />80044252<br />**Number**:<br />-2147204526|The requested importjob does not exist.|
> |**Name**:<br />InvalidImportJobTemplateFile<br />**Hex**:<br />80044251<br />**Number**:<br />-2147204527|The ImportJobTemplate.xml file is invalid.|
> |**Name**:<br />InvalidIncomingDeliveryExpectingEmailConnector<br />**Hex**:<br />8005E224<br />**Number**:<br />-2147098076|The incoming delivery method is not email connector. To receive mails its incoming delivery method should be Email Connector.|
> |**Name**:<br />InvalidInstanceEntityName<br />**Hex**:<br />8004E10D<br />**Number**:<br />-2147163891|Invalid instance entity name.|
> |**Name**:<br />InvalidInstanceTypeCode<br />**Hex**:<br />8004E107<br />**Number**:<br />-2147163897|Invalid instance type code.|
> |**Name**:<br />InvalidInteractiveUserQuota<br />**Hex**:<br />8004B049<br />**Number**:<br />-2147176375|You have reached the maximum number of interactive/full users.|
> |**Name**:<br />InvalidIntersectEntity<br />**Hex**:<br />80072540<br />**Number**:<br />-2147015360|Cannot use existing non intersect entity {0} as an intersect entity for defining many to many relationships.|
> |**Name**:<br />InvalidInvitationLiveId<br />**Hex**:<br />8004D20E<br />**Number**:<br />-2147167730|A user with this e-mail address was not found. Sign in to Windows Live ID with the same e-mail address where you received the invitation.  If you do not have a Windows Live ID, please create one using that e-mail address.|
> |**Name**:<br />InvalidInvitationToken<br />**Hex**:<br />8004D20D<br />**Number**:<br />-2147167731|The invitation token {0} is not correctly formatted.|
> |**Name**:<br />InvalidIsFirstRowHeaderForUseSystemMap<br />**Hex**:<br />80040364<br />**Number**:<br />-2147220636|The first row of the file does not contain column headings.|
> |**Name**:<br />InvalidIsoCurrencyCode<br />**Hex**:<br />80048cf2<br />**Number**:<br />-2147185422|Invalid ISO currency code.|
> |**Name**:<br />InvalidKeyQuery<br />**Hex**:<br />80072529<br />**Number**:<br />-2147015383|Keys must be part of the requested EntityMetadata properties when a KeyQuery is specified. Expect property = {0} in requested entity properties list.|
> |**Name**:<br />InvalidKit<br />**Hex**:<br />80043afd<br />**Number**:<br />-2147206403|The product is not a kit.|
> |**Name**:<br />InvalidKitProduct<br />**Hex**:<br />80043afe<br />**Number**:<br />-2147206402|You cannot add a product kit to itself. Select a different product or product kit.|
> |**Name**:<br />InvalidLanguageCode<br />**Hex**:<br />80044195<br />**Number**:<br />-2147204715|The specified language code is not valid for this organization.|
> |**Name**:<br />InvalidLanguageForCreate<br />**Hex**:<br />80060750<br />**Number**:<br />-2147088560|Rows with localizable attributes can only be created when the user interface (UI) language for the current user is set to the organization's base language.|
> |**Name**:<br />InvalidLanguageForProcessConfiguration<br />**Hex**:<br />8005E102<br />**Number**:<br />-2147098366|Process configuration is not available since your language does not match system base language.|
> |**Name**:<br />InvalidLanguageForSolution<br />**Hex**:<br />80047019<br />**Number**:<br />-2147192807|Solution and Publisher Options are not available since your language does not match system base language.|
> |**Name**:<br />InvalidLanguageForUpdate<br />**Hex**:<br />80060751<br />**Number**:<br />-2147088559|Localizable attributes can only be updated via the string property when the user interface (UI) language for the current user is set to the organization's base language. Use SetLocLabels to update the localized values for the following attributes: [{0}].|
> |**Name**:<br />InvalidLicenseCannotReadMpcFile<br />**Hex**:<br />8004D245<br />**Number**:<br />-2147167675|Invalid license. MPC code cannot be read from MPC.txt file with this path {0}.|
> |**Name**:<br />InvalidLicenseKey<br />**Hex**:<br />8004D240<br />**Number**:<br />-2147167680|Invalid license key ({0}).|
> |**Name**:<br />InvalidLicenseMpcCode<br />**Hex**:<br />8004D246<br />**Number**:<br />-2147167674|Invalid license. Invalid MPC code ({0}).|
> |**Name**:<br />InvalidLicensePid<br />**Hex**:<br />8004D242<br />**Number**:<br />-2147167678|Invalid license. Invalid PID (Product Id) ({0}).|
> |**Name**:<br />InvalidLicensePidGenCannotLoad<br />**Hex**:<br />8004D243<br />**Number**:<br />-2147167677|Invalid license. PidGen.dll cannot be loaded from this path {0}|
> |**Name**:<br />InvalidLicensePidGenOtherError<br />**Hex**:<br />8004D244<br />**Number**:<br />-2147167676|Invalid license. Cannot generate PID (Product Id) from License key. PidGen error code ({0}).|
> |**Name**:<br />InvalidLocaleIdForKnowledgeArticle<br />**Hex**:<br />80061400<br />**Number**:<br />-2147085312|Language with Locale ID {0}, does not exist|
> |**Name**:<br />InvalidLogoImageId<br />**Hex**:<br />800608D3<br />**Number**:<br />-2147088173|Invalid logo image web resource id.|
> |**Name**:<br />InvalidLogoImageWebResourceType<br />**Hex**:<br />800608D9<br />**Number**:<br />-2147088167|Invalid WebResource Type for Logo Image.|
> |**Name**:<br />InvalidLookupMapNode<br />**Hex**:<br />80048481<br />**Number**:<br />-2147187583|The lookup entity provided is not valid for the given target attribute.|
> |**Name**:<br />InvalidMailbox<br />**Hex**:<br />8005E217<br />**Number**:<br />-2147098089|Invalid mailboxId passed in. Please check the mailboxid.|
> |**Name**:<br />InvalidManagedPropertyException<br />**Hex**:<br />8004F030<br />**Number**:<br />-2147160016|Managed property {0} does not contain enough information to be created.  Please provide (assembly, class), or (entity, attribute) or set the managed property to custom.|
> |**Name**:<br />InvalidManifestFilePath<br />**Hex**:<br />80048533<br />**Number**:<br />-2147187405|Failed to locate the manifest file in the specified location|
> |**Name**:<br />InvalidMatchingAttributeError<br />**Hex**:<br />80044244<br />**Number**:<br />-2147204540|Invalid Matching attribute.|
> |**Name**:<br />InvalidMaximumResourceLimit<br />**Hex**:<br />8004B02B<br />**Number**:<br />-2147176405|The resource type {0} cannot have a maximum limit of {1}.|
> |**Name**:<br />InvalidMaxLengthForControl <br />**Hex**:<br />80060879<br />**Number**:<br />-2147088263|Invalid MaxLength Parameter specified for control {0}.Maxlength must be in between {1} and {2} .|
> |**Name**:<br />InvalidMaxValueForControl <br />**Hex**:<br />8006087B<br />**Number**:<br />-2147088261|Invalid MaxValue Parameter specified for control {0}.Max Value must be in between {1} and {2} .|
> |**Name**:<br />InvalidMeasureCollection<br />**Hex**:<br />8004E00A<br />**Number**:<br />-2147164150|Measure collection is invalid. Not all the measures in the measure collection have the same group bys.|
> |**Name**:<br />InvalidMetadata<br />**Hex**:<br />8004023a<br />**Number**:<br />-2147220934|Invalid Metadata.|
> |**Name**:<br />InvalidMetadataSqlOperation<br />**Hex**:<br />80072343<br />**Number**:<br />-2147015869|SQL exception has been thrown on current metadata operation. Please check the exception for more details.|
> |**Name**:<br />InvalidMigrationFileContent<br />**Hex**:<br />8005F033<br />**Number**:<br />-2147094477|The content of the import file is not valid. You must select a text file.|
> |**Name**:<br />InvalidMinAndMaxValueForControl <br />**Hex**:<br />8006087C<br />**Number**:<br />-2147088260|Invalid MinValue and MaxValue Parameter specified for control {0}.Min Value must be less than Max Value .|
> |**Name**:<br />InvalidMinimumResourceLimit<br />**Hex**:<br />8004B02A<br />**Number**:<br />-2147176406|The resource type {0} cannot have a minimum limit of {1}.|
> |**Name**:<br />InvalidMinValueForControl <br />**Hex**:<br />8006087A<br />**Number**:<br />-2147088262|Invalid MinValue Parameter specified for control {0}.Min Value must be in between {1} and {2} .|
> |**Name**:<br />InvalidMobileOfflineFiltersFetchXml<br />**Hex**:<br />80071113<br />**Number**:<br />-2147020525|XML Format mismatch. Check for the correctness of XML.|
> |**Name**:<br />InvalidMultipleMapping<br />**Hex**:<br />80048498<br />**Number**:<br />-2147187560|A source field is mapped to more than one Dynamics 365 fields of lookup/picklist type.|
> |**Name**:<br />InvalidMultipleSiteMapReferenceSingleAppModule<br />**Hex**:<br />80050111<br />**Number**:<br />-2147155695|An app can’t have multiple site maps.|
> |**Name**:<br />InvalidNamePrefix<br />**Hex**:<br />80044366<br />**Number**:<br />-2147204250|The schema name {0} for type {2} is invalid or missing.Custom attribute, entity, entitykey, option set and relationship names must start with a valid customization prefix.The prefix for a solution component should match the prefix that is specified for the publisher of the solution.|
> |**Name**:<br />InvalidNetPrice<br />**Hex**:<br />800404f3<br />**Number**:<br />-2147220237|The net price is invalid|
> |**Name**:<br />InvalidNonInteractiveUserQuota<br />**Hex**:<br />8004B050<br />**Number**:<br />-2147176368|You have reached the maximum number of non-interactive users/|
> |**Name**:<br />InvalidNumberGroupFormat<br />**Hex**:<br />80043700<br />**Number**:<br />-2147207424|Invalid input string for numbergroupformat. The input string should contain an array of integers. Every element in the value array should be between one and nine, except for the last element, which can be zero.|
> |**Name**:<br />InvalidNumberOfCardFormSections<br />**Hex**:<br />80061505<br />**Number**:<br />-2147085051|Number of sections in a card form must be 4. Found {0}.|
> |**Name**:<br />InvalidNumberOfPartitions<br />**Hex**:<br />8004E200<br />**Number**:<br />-2147163648|You cannot delete audit data in the partitions that are currently in use, or delete the partitions that are created for storing future audit data.|
> |**Name**:<br />InvalidNumberOfReferencePanelSections<br />**Hex**:<br />80061504<br />**Number**:<br />-2147085052|MainInteractionCentric form can have only 1 reference panel section. Found {0}.|
> |**Name**:<br />InvalidNumberOfSectionsInTab<br />**Hex**:<br />80060872<br />**Number**:<br />-2147088270|A dialog Form XML cannot contain more than one section.|
> |**Name**:<br />InvalidNumberOfTabsInDialog<br />**Hex**:<br />80060871<br />**Number**:<br />-2147088271|A dialog Form XML cannot contain more than one tab.|
> |**Name**:<br />InvalidOAuthToken<br />**Hex**:<br />80041d50<br />**Number**:<br />-2147214000|The OAuth token is invalid|
> |**Name**:<br />InvalidObjectTypes<br />**Hex**:<br />8004021f<br />**Number**:<br />-2147220961|Invalid object type.|
> |**Name**:<br />InvalidOccurrenceNumber<br />**Hex**:<br />8004E125<br />**Number**:<br />-2147163867|The effective end date of the series cannot be earlier than today. Select a valid occurrence number.|
> |**Name**:<br />InvalidOfflineOperation<br />**Hex**:<br />8004410e<br />**Number**:<br />-2147204850|Operation not valid when offline.|
> |**Name**:<br />InvalidOneToManyRelationship<br />**Hex**:<br />80072500<br />**Number**:<br />-2147015424|OneToMany Entity Relationship with EntityRelationshipId '{0}' has null ReferencingEntityRole|
> |**Name**:<br />InvalidOneToManyRelationshipForRelatedEntitiesQuery<br />**Hex**:<br />8004430F<br />**Number**:<br />-2147204337|An invalid OneToManyRelationship has been specified for RelatedEntitiesQuery. Referenced Entity {0} should be the same as primary entity {1}|
> |**Name**:<br />InvalidOperandOnLeftHandSide<br />**Hex**:<br />80072501<br />**Number**:<br />-2147015423|The left side of the '{0}' operator must be a property of the entity.|
> |**Name**:<br />InvalidOperation<br />**Hex**:<br />8004023b<br />**Number**:<br />-2147220933|Invalid Operation performed.|
> |**Name**:<br />InvalidOperationForClosedOrCancelledCampaignActivity<br />**Hex**:<br />80040314<br />**Number**:<br />-2147220716|Can not add items to closed (cancelled) campaignactivity.|
> |**Name**:<br />InvalidOperationForDynamicList<br />**Hex**:<br />8004F701<br />**Number**:<br />-2147158271|This action is not available for a dynamic marketing list.|
> |**Name**:<br />InvalidOperationWhenListIsNotActive<br />**Hex**:<br />8004033a<br />**Number**:<br />-2147220678|List is not active. Cannot perform this operation.|
> |**Name**:<br />InvalidOperationWhenListLocked<br />**Hex**:<br />80040302<br />**Number**:<br />-2147220734|List is Locked. Cannot perform this action.|
> |**Name**:<br />InvalidOperationWhenPartyIsNotActive<br />**Hex**:<br />8004033b<br />**Number**:<br />-2147220677|The party is not active. Cannot perform this operation.|
> |**Name**:<br />InvalidOperatorCode<br />**Hex**:<br />80048415<br />**Number**:<br />-2147187691|The operator is not valid or it is not supported.|
> |**Name**:<br />InvalidOperatorCodeError<br />**Hex**:<br />80044253<br />**Number**:<br />-2147204525|Invalid operator code.|
> |**Name**:<br />InvalidOptionSetIdForControl<br />**Hex**:<br />80060876<br />**Number**:<br />-2147088266|An invalid OptionSetId specified for control {0}.OptionSet Id is an non-empty Guid.|
> |**Name**:<br />InvalidOptionSetNameChange<br />**Hex**:<br />80048409<br />**Number**:<br />-2147187703|Cannot update OptionSet Name {0}, Id: {1} because OptionSet name provided value ({2}) is in use by another existing OptionSet (id: {3})|
> |**Name**:<br />InvalidOptionSetOperation<br />**Hex**:<br />80048403<br />**Number**:<br />-2147187709|Invalid OptionSet|
> |**Name**:<br />InvalidOptionSetSchemaName<br />**Hex**:<br />80044345<br />**Number**:<br />-2147204283|An OptionSet with the specified name already exists. Please specify a unique name.|
> |**Name**:<br />InvalidOrEmptyRelationshipId<br />**Hex**:<br />80071122<br />**Number**:<br />-2147020510|The RelationshipId of Mobile profile item association is invalid or empty.|
> |**Name**:<br />InvalidOrganizationFriendlyName<br />**Hex**:<br />8004D252<br />**Number**:<br />-2147167662|Invalid organization friendly name ({0}). Reason: ({1})|
> |**Name**:<br />InvalidOrganizationId<br />**Hex**:<br />80044248<br />**Number**:<br />-2147204536|The Organization ID present in the translations file does not match the current Organization ID.|
> |**Name**:<br />InvalidOrganizationSettings<br />**Hex**:<br />8006110D<br />**Number**:<br />-2147086067|Organization Settings are not properly configured for External Party.|
> |**Name**:<br />InvalidOrganizationUniqueName<br />**Hex**:<br />8004D251<br />**Number**:<br />-2147167663|Invalid organization unique name ({0}). Reason: ({1})|
> |**Name**:<br />InvalidOrgDBOrgSetting<br />**Hex**:<br />80048514<br />**Number**:<br />-2147187436|Invalid Organization Setting passed in. Please check the datatype and pass in an appropriate value.|
> |**Name**:<br />InvalidOrgOwnedCascadeLinkType<br />**Hex**:<br />80044156<br />**Number**:<br />-2147204778|Cascade User-Owned is not a valid cascade link type for org-owned entity relationships.|
> |**Name**:<br />InvalidOtherDataFilterOptions<br />**Hex**:<br />8006098D<br />**Number**:<br />-2147087987|You should select at least one option from Download My Records, My Team Records or My Business Unit's Records for Other Data Filter|
> |**Name**:<br />InvalidOutgoingDeliveryExpectingEmailConnector<br />**Hex**:<br />8005E226<br />**Number**:<br />-2147098074|The outgoing delivery method is not email connector. To send mails its outgoing delivery method should be Email Connector.|
> |**Name**:<br />InvalidOwnerID<br />**Hex**:<br />80040229<br />**Number**:<br />-2147220951|The owner ID is invalid or missing.|
> |**Name**:<br />InvalidOwnershipTypeMask<br />**Hex**:<br />8004700d<br />**Number**:<br />-2147192819|The specified ownership type mask is not valid for this operation|
> |**Name**:<br />InvalidPageResponse<br />**Hex**:<br />8004E00D<br />**Number**:<br />-2147164147|Invalid Page Response generated.|
> |**Name**:<br />InvalidParent<br />**Hex**:<br />80040205<br />**Number**:<br />-2147220987|The parent object is invalid or missing.|
> |**Name**:<br />InvalidParentId<br />**Hex**:<br />80040206<br />**Number**:<br />-2147220986|The parent id is invalid or missing.|
> |**Name**:<br />InvalidPartnerSolutionCustomizationProvider<br />**Hex**:<br />8004A109<br />**Number**:<br />-2147180279|Invalid partner solution customization provider type|
> |**Name**:<br />InvalidPartyMapping<br />**Hex**:<br />80043515<br />**Number**:<br />-2147207915|Invalid party mapping.|
> |**Name**:<br />InvalidPluginAssemblyContent<br />**Hex**:<br />8004418b<br />**Number**:<br />-2147204725|Plug-in assembly does not contain the required types or assembly content cannot be updated.|
> |**Name**:<br />InvalidPluginAssemblyVersion<br />**Hex**:<br />8004417B<br />**Number**:<br />-2147204741|Plug-in assembly fullnames must be unique (ignoring the version build and revision number).|
> |**Name**:<br />InvalidPluginRegistrationConfiguration<br />**Hex**:<br />80044170<br />**Number**:<br />-2147204752|The plug-in assembly registration configuration is invalid.|
> |**Name**:<br />InvalidPluginStrongNameRequired<br />**Hex**:<br />80081114<br />**Number**:<br />-2146954988|Plug-in assembly is not strong name signed.|
> |**Name**:<br />InvalidPluginTypeImplementation<br />**Hex**:<br />8004418c<br />**Number**:<br />-2147204724|Plug-in type must implement exactly one of the following classes or interfaces: Microsoft.Crm.Sdk.IPlugin, Microsoft.Xrm.Sdk.IPlugin, System.Activities.Activity and System.Workflow.ComponentModel.Activity.|
> |**Name**:<br />InvalidPointer<br />**Hex**:<br />80040218<br />**Number**:<br />-2147220968|The object is disposed.|
> |**Name**:<br />InvalidPrecisionForControl <br />**Hex**:<br />8006087D<br />**Number**:<br />-2147088259|Invalid Precision Parameter specified for control {0}.Precision must be in between {1} and {2} .|
> |**Name**:<br />InvalidPresentationDescription<br />**Hex**:<br />8004E002<br />**Number**:<br />-2147164158|The presentation description is invalid.|
> |**Name**:<br />InvalidPreviewModeOperation<br />**Hex**:<br />8005f219<br />**Number**:<br />-2147093991|You can’t perform this operation in preview mode.|
> |**Name**:<br />InvalidPriceLevelCurrencyForPricingMethod<br />**Hex**:<br />80048cf9<br />**Number**:<br />-2147185415|The currency of the price list needs to match the currency of the product for pricing method percentage.|
> |**Name**:<br />InvalidPricePerUnit<br />**Hex**:<br />80043b10<br />**Number**:<br />-2147206384|The price per unit is invalid.|
> |**Name**:<br />InvalidPrimaryContactBasedOnAccount<br />**Hex**:<br />8004F864<br />**Number**:<br />-2147157916|The specified contact doesn't belong to the account selected as the customer. Specify a contact that belongs to the selected account, and then try again.|
> |**Name**:<br />InvalidPrimaryContactBasedOnContact<br />**Hex**:<br />8004F865<br />**Number**:<br />-2147157915|The specified contact doesn't belong to the contact that was specified in the customer field. Remove the value from the contact field, or select a contact associated to the selected customer, and then try again.|
> |**Name**:<br />InvalidPrimaryFieldForActivity<br />**Hex**:<br />8004F127<br />**Number**:<br />-2147159769|A custom entity defined as an activity cannot have primary attribute other than subject.|
> |**Name**:<br />InvalidPrimaryFieldType<br />**Hex**:<br />8004700e<br />**Number**:<br />-2147192818|Primary UI Attribute has to be of type String|
> |**Name**:<br />InvalidPrimaryKey<br />**Hex**:<br />80040266<br />**Number**:<br />-2147220890|Invalid primary key.|
> |**Name**:<br />InvalidPrincipalId<br />**Hex**:<br />80048348<br />**Number**:<br />-2147187896|Passed Guid is empty.|
> |**Name**:<br />InvalidPrincipalType<br />**Hex**:<br />80048346<br />**Number**:<br />-2147187898|Invalid Principal Type passed.|
> |**Name**:<br />InvalidPriv<br />**Hex**:<br />8004024b<br />**Number**:<br />-2147220917|Invalid privilege type.|
> |**Name**:<br />InvalidPrivilegeDepth<br />**Hex**:<br />8004140b<br />**Number**:<br />-2147216373|Invalid privilege depth.|
> |**Name**:<br />InvalidProcessControlAttribute<br />**Hex**:<br />8005E105<br />**Number**:<br />-2147098363|The process control definition contains an invalid attribute.|
> |**Name**:<br />InvalidProcessControlEntity<br />**Hex**:<br />8005E104<br />**Number**:<br />-2147098364|The process control definition contains an invalid entity or invalid entity order.|
> |**Name**:<br />InvalidProcessIdOperation<br />**Hex**:<br />80092001<br />**Number**:<br />-2146885631|Invalid operation. Process ID cannot be modified.|
> |**Name**:<br />InvalidProcessStateData<br />**Hex**:<br />80045049<br />**Number**:<br />-2147200951|ProcessState is not valid for given ProcessSession instance.|
> |**Name**:<br />InvalidProduct<br />**Hex**:<br />80060623<br />**Number**:<br />-2147088861|You can't add a product family.|
> |**Name**:<br />InvalidPublisherUniqueName<br />**Hex**:<br />8004F01C<br />**Number**:<br />-2147160036|Publisher uniquename is required.|
> |**Name**:<br />InvalidPublishOnProtectedComponent<br />**Hex**:<br />8004F014<br />**Number**:<br />-2147160044|You cannot publish {0} {1}. Publish cannot be performed when {0} is managed.|
> |**Name**:<br />InvalidQuantityDecimalCode<br />**Hex**:<br />80043afc<br />**Number**:<br />-2147206404|The quantity decimal code is invalid.|
> |**Name**:<br />InvalidQuery<br />**Hex**:<br />80044183<br />**Number**:<br />-2147204733|The query specified for this operation is invalid|
> |**Name**:<br />InvalidQueryForVirtualEntity<br />**Hex**:<br />80044822<br />**Number**:<br />-2147203038|The query specified is not supported for virtual entity.|
> |**Name**:<br />InvalidRecurrenceInterval<br />**Hex**:<br />8004D2A1<br />**Number**:<br />-2147167583|To set recurrence, you must specify an interval that is between 1 and 365.|
> |**Name**:<br />InvalidRecurrenceIntervalForRollupJobs<br />**Hex**:<br />8004D2A2<br />**Number**:<br />-2147167582|To set recurrence, you must specify an interval that should be greater than 1 hour.|
> |**Name**:<br />InvalidRecurrencePattern<br />**Hex**:<br />8004E100<br />**Number**:<br />-2147163904|Invalid recurrence pattern.|
> |**Name**:<br />InvalidRecurrenceRule<br />**Hex**:<br />80040246<br />**Number**:<br />-2147220922|Error in RecurrencePatternFactory.|
> |**Name**:<br />InvalidRecurrenceRuleForBulkDeleteAndDuplicateDetection<br />**Hex**:<br />8004D2A0<br />**Number**:<br />-2147167584|Bulk Delete and Duplicate Detection recurrence must be specified as daily.|
> |**Name**:<br />InvalidRegardingObjectTypeCode<br />**Hex**:<br />80040319<br />**Number**:<br />-2147220711|The regarding Object Type Code is not valid for the Bulk Operation.|
> |**Name**:<br />InvalidRegistryKey<br />**Hex**:<br />8004024c<br />**Number**:<br />-2147220916|Invalid registry key specified.|
> |**Name**:<br />InvalidRelationshipDescription<br />**Hex**:<br />80047003<br />**Number**:<br />-2147192829|The specified relationship cannot be created|
> |**Name**:<br />InvalidRelationshipInMOPIAssociation<br />**Hex**:<br />80060999<br />**Number**:<br />-2147087975|This relationship doesn’t exist with the entity selected in the parent profile item.|
> |**Name**:<br />InvalidRelationshipNameForControl<br />**Hex**:<br />80060877<br />**Number**:<br />-2147088265|Relationship Name not specified for control {0}.Relationship Name is an mandatory Field.|
> |**Name**:<br />InvalidRelationshipQuery<br />**Hex**:<br />80072528<br />**Number**:<br />-2147015384|Atleast one of the relationship properties must be part of the requested EntityMetadata properties when a RelationshipQuery is specified.Expect atleast one of property = {0}, {1} or {2} in requested entity properties list.|
> |**Name**:<br />InvalidRelationshipType<br />**Hex**:<br />8004700f<br />**Number**:<br />-2147192817|The specified relationship type is not valid for this operation|
> |**Name**:<br />InvalidRelationshipTypeForAccessory<br />**Hex**:<br />8004F989<br />**Number**:<br />-2147157623|An accessory relationship is always unidirectional and can't be changed.|
> |**Name**:<br />InvalidRelationshipTypeForUpSell<br />**Hex**:<br />8004F988<br />**Number**:<br />-2147157624|An upsell relationship is always unidirectional and can't be changed.|
> |**Name**:<br />InvalidRelativeUrlFormat<br />**Hex**:<br />80048054<br />**Number**:<br />-2147188652|The relative url contains invalid characters. Please use a different name. Valid relative url names cannot ends with the following strings: .aspx, .ashx, .asmx, .svc , cannot begin or end with a dot, cannot contain consecutive dots and cannot contain any of the following characters: ~ " # % & * : < > ? / \ { | }.|
> |**Name**:<br />InvalidRequestBody<br />**Hex**:<br />80072530<br />**Number**:<br />-2147015376|Passed entity object cannot be null or empty.|
> |**Name**:<br />InvalidRequestDataFormat<br />**Hex**:<br />80044271<br />**Number**:<br />-2147204495|The updated configuration includes invalid data.|
> |**Name**:<br />InvalidRequestParameter<br />**Hex**:<br />80044828<br />**Number**:<br />-2147203032|Both name and value should be specified for request parameter.|
> |**Name**:<br />InvalidRequestParameters<br />**Hex**:<br />8006110E<br />**Number**:<br />-2147086066|Request parameters are not valid to server External Party request.|
> |**Name**:<br />InvalidResourceType<br />**Hex**:<br />8004B029<br />**Number**:<br />-2147176407|The requested action is not valid for resource type {0}.|
> |**Name**:<br />InvalidRestore<br />**Hex**:<br />80040258<br />**Number**:<br />-2147220904|RestoreCaller must be called after SwitchToSystemUser.|
> |**Name**:<br />InvalidRole<br />**Hex**:<br />8004B012<br />**Number**:<br />-2147176430|You have not assigned roles to this user|
> |**Name**:<br />InvalidRoleOccurrencesForOneToManyRelationship<br />**Hex**:<br />8006089A<br />**Number**:<br />-2147088230|There can't be more than two entity relationship roles for a one-to-many relationship {0}.|
> |**Name**:<br />InvalidRoleTypeForOneToManyRelationship<br />**Hex**:<br />80060899<br />**Number**:<br />-2147088231|This relationship role type isn't valid for a one-to-many relationship {0}.|
> |**Name**:<br />InvalidRollupQueryAttributeSet<br />**Hex**:<br />8004F683<br />**Number**:<br />-2147158397|A Rollup Query cannot be set for a Rollup Field that is not defined in the Goal Metric.|
> |**Name**:<br />InvalidRollupType<br />**Hex**:<br />80040234<br />**Number**:<br />-2147220940|The rollup type is invalid.|
> |**Name**:<br />InvalidS2SAuthentication<br />**Hex**:<br />8005E245<br />**Number**:<br />-2147098043|You can use server-to-server authentication only for email server profiles created for a Microsoft Dynamics 365 Online organization that was set up through the Microsoft online services environment (Office 365).|
> |**Name**:<br />InvalidSchemaName<br />**Hex**:<br />8004700b<br />**Number**:<br />-2147192821|An entity with the specified name already exists. Please specify a unique name.|
> |**Name**:<br />InvalidSearchEntities<br />**Hex**:<br />80060202<br />**Number**:<br />-2147089918|Search - {0} did not find any valid Entities.|
> |**Name**:<br />InvalidSearchEntity<br />**Hex**:<br />80060201<br />**Number**:<br />-2147089919|Invalid Search Entity - {0}.|
> |**Name**:<br />InvalidSearchName<br />**Hex**:<br />80060204<br />**Number**:<br />-2147089916|Invalid Search Name - {0}.|
> |**Name**:<br />InvalidSeriesId<br />**Hex**:<br />8004E105<br />**Number**:<br />-2147163899|SeriesId is null or invalid.|
> |**Name**:<br />InvalidSeriesIdOriginalStart<br />**Hex**:<br />8004E109<br />**Number**:<br />-2147163895|Invalid seriesid or original start date.|
> |**Name**:<br />InvalidSeriesStatus<br />**Hex**:<br />8004E10F<br />**Number**:<br />-2147163889|Invalid series status.|
> |**Name**:<br />InvalidSharee<br />**Hex**:<br />8004020c<br />**Number**:<br />-2147220980|Invalid share id.|
> |**Name**:<br />InvalidSharePointSiteCollectionUrl<br />**Hex**:<br />80048052<br />**Number**:<br />-2147188654|The URL must conform to the http or https schema.|
> |**Name**:<br />InvalidSimilarityRuleStateError<br />**Hex**:<br />80044254<br />**Number**:<br />-2147204524|Invalid similarity rule state.|
> |**Name**:<br />InvalidSingletonResults<br />**Hex**:<br />8004024f<br />**Number**:<br />-2147220913|Crm Internal Exception: Singleton Retrieve Query should not return more than 1 record.|
> |**Name**:<br />InvalidSiteRelativeUrlFormat<br />**Hex**:<br />80048053<br />**Number**:<br />-2147188653|The relative url contains invalid characters. Please use a different name. Valid relative url names cannot end with the following strings: .aspx, .ashx, .asmx, .svc , cannot begin or end with a dot or /, cannot contain consecutive dots or / and cannot contain any of the following characters: ~ " # % & * : < > ? \ { | }.|
> |**Name**:<br />InvalidSolutionAwarenessDeclaration<br />**Hex**:<br />80072000<br />**Number**:<br />-2147016704|An entity cannot be declared as solution-aware on an update operation. Entity: {0}|
> |**Name**:<br />InvalidSolutionConfigurationPage<br />**Hex**:<br />8004701B<br />**Number**:<br />-2147192805|The specified configuration page for this solution is invalid.|
> |**Name**:<br />InvalidSolutionUniqueName<br />**Hex**:<br />8004F002<br />**Number**:<br />-2147160062|Invalid character specified for solution unique name. Only characters within the ranges \[A-Z\], \[a-z\], \[0-9\] or \_ are allowed. The first character may only be in the ranges \[A-Z\], \[a-z\] or \_.|
> |**Name**:<br />InvalidSolutionVersion<br />**Hex**:<br />8004F01E<br />**Number**:<br />-2147160034|An invalid solution version was specified.|
> |**Name**:<br />InvalidSourceAttributeType<br />**Hex**:<br />80044808<br />**Number**:<br />-2147203064|Source Attribute Type does not match the Amount Data Type specified.|
> |**Name**:<br />InvalidSourceEntityAttribute<br />**Hex**:<br />80044806<br />**Number**:<br />-2147203066|Attribute {0} is not an attribute of Entity {1}.|
> |**Name**:<br />InvalidSourceStateValue<br />**Hex**:<br />80044810<br />**Number**:<br />-2147203056|The source state specified for the entity is invalid.|
> |**Name**:<br />InvalidSourceStatusValue<br />**Hex**:<br />80044811<br />**Number**:<br />-2147203055|The source status specified for the entity is invalid.|
> |**Name**:<br />InvalidSourceType<br />**Hex**:<br />80060437<br />**Number**:<br />-2147089353|SourceType {0} isn't valid for the {1} data type.|
> |**Name**:<br />InvalidSourceTypeCode<br />**Hex**:<br />800608EA<br />**Number**:<br />-2147088150|Please select valid property bag for the selected source type.|
> |**Name**:<br />InvalidStage<br />**Hex**:<br />80060452<br />**Number**:<br />-2147089326|Validation error: invalid stage.|
> |**Name**:<br />InvalidStageTransition<br />**Hex**:<br />80092003<br />**Number**:<br />-2146885629|Invalid stage transition. Transition to stage {0} is not in the process active path.|
> |**Name**:<br />InvalidStageTransitionOnInactiveInstance<br />**Hex**:<br />80060377<br />**Number**:<br />-2147089545|Invalid stage transition. Stage transition is not allowed on inactive processes.|
> |**Name**:<br />InvalidState<br />**Hex**:<br />80040233<br />**Number**:<br />-2147220941|The object is not in a valid state to perform this operation.|
> |**Name**:<br />InvalidStateCodeStatusCode<br />**Hex**:<br />80048408<br />**Number**:<br />-2147187704|State code is invalid or state code is valid but status code is invalid for a specified state code.|
> |**Name**:<br />InvalidStateForPublish<br />**Hex**:<br />8004F90A<br />**Number**:<br />-2147157750|The specified ProductFamily, Product or Bundle can only be published from Draft state or ActiveDraft status|
> |**Name**:<br />InvalidStateTransition<br />**Hex**:<br />8004F00E<br />**Number**:<br />-2147160050|The {0} (Id={1}) entity or component has attempted to transition from an invalid state: {2}.|
> |**Name**:<br />InvalidSubmitFromPublishedArticle<br />**Hex**:<br />80048dfa<br />**Number**:<br />-2147185158|You are trying to submit an article that has a status of published. You can only submit an article with the status of draft.|
> |**Name**:<br />InvalidSubmitFromUnapprovedArticle<br />**Hex**:<br />80048dff<br />**Number**:<br />-2147185153|You are trying to submit an article that has a status of unapproved. You can only submit an article with the status of draft.|
> |**Name**:<br />InvalidSubstituteProduct<br />**Hex**:<br />80043aff<br />**Number**:<br />-2147206401|A product can't have a relationship with itself.|
> |**Name**:<br />InvalidSyncDirectionValueForUpdate<br />**Hex**:<br />80060742<br />**Number**:<br />-2147088574|The sync direction is invalid as per the allowed sync direction for one or more attribute mappings.|
> |**Name**:<br />InvalidTargetEntity<br />**Hex**:<br />80040369<br />**Number**:<br />-2147220631|The specified target record type does not exist.|
> |**Name**:<br />InvalidTargetEntityTypeForControl<br />**Hex**:<br />80060878<br />**Number**:<br />-2147088264|Target Entity Type not specified for control {0}.Target Entity is an mandatory Field.|
> |**Name**:<br />InvalidTargetFrameworkVersion<br />**Hex**:<br />8004420b<br />**Number**:<br />-2147204597|Plug-in assembly targets a version of .NET Framework that is not supported.|
> |**Name**:<br />InvalidTaskFlow<br />**Hex**:<br />80060392<br />**Number**:<br />-2147089518|Task Flow is invalid.|
> |**Name**:<br />InvalidTemplate<br />**Hex**:<br />8004B010<br />**Number**:<br />-2147176432|The Invitation Email template is not valid|
> |**Name**:<br />InvalidTemplateContent<br />**Hex**:<br />800609B2<br />**Number**:<br />-2147087950|The template content is invalid.|
> |**Name**:<br />InvalidTemplateId<br />**Hex**:<br />80050019<br />**Number**:<br />-2147155943|That’s not a valid template.|
> |**Name**:<br />InvalidTenantIDValue<br />**Hex**:<br />8005E25B<br />**Number**:<br />-2147098021|Exchange Online Tenant ID value is not valid.The Field value should be a string in the structure of GUID.|
> |**Name**:<br />InvalidThemeDeleteOperation<br />**Hex**:<br />800608D7<br />**Number**:<br />-2147088169|You can’t delete system or default themes.|
> |**Name**:<br />InvalidThemeId<br />**Hex**:<br />800608D4<br />**Number**:<br />-2147088172|Invalid theme id.|
> |**Name**:<br />InvalidTimeZoneCode<br />**Hex**:<br />800608F7<br />**Number**:<br />-2147088137|Time Zone Code {0} specified is not recognized. Please specify a valid Time Zone Code value.|
> |**Name**:<br />InvalidToken<br />**Hex**:<br />8004B061<br />**Number**:<br />-2147176351|The token is invalid.|
> |**Name**:<br />InvalidTotalDiscount<br />**Hex**:<br />800404f4<br />**Number**:<br />-2147220236|The total discount is invalid|
> |**Name**:<br />InvalidTotalPrice<br />**Hex**:<br />800404f5<br />**Number**:<br />-2147220235|The total price is invalid|
> |**Name**:<br />InvalidTransformationParameter<br />**Hex**:<br />80040389<br />**Number**:<br />-2147220599|A parameter for the transformation is either missing or invalid.|
> |**Name**:<br />InvalidTransformationParameterDataType<br />**Hex**:<br />80040380<br />**Number**:<br />-2147220608|The data type of one or more of the transformation parameters is unsupported.|
> |**Name**:<br />InvalidTransformationParameterEmptyCollection<br />**Hex**:<br />80048511<br />**Number**:<br />-2147187439|The transformation parameter: {0} has an invalid input value length: {1}. The parameter length cannot be an empty collection.|
> |**Name**:<br />InvalidTransformationParameterMapping<br />**Hex**:<br />80040382<br />**Number**:<br />-2147220606|The transformation parameter mapping defined is invalid. Check that the target attribute name exists.|
> |**Name**:<br />InvalidTransformationParameterMappings<br />**Hex**:<br />8004037c<br />**Number**:<br />-2147220612|One or more transformation parameter mappings are invalid or do not match the transformation parameter description.|
> |**Name**:<br />InvalidTransformationParameterOutsideRange<br />**Hex**:<br />80048510<br />**Number**:<br />-2147187440|The transformation parameter: {0} has an invalid input value: {1}. The parameter is out of the permissible range: {2}. |
> |**Name**:<br />InvalidTransformationParameterOutsideRangeGeneric<br />**Hex**:<br />80048512<br />**Number**:<br />-2147187438|One or more input transformation parameter values are outside the permissible range: {0}.|
> |**Name**:<br />InvalidTransformationParametersGeneric<br />**Hex**:<br />80048507<br />**Number**:<br />-2147187449|The transformation parameter: {0} has an invalid input value: {1}. The parameter must be of type: {2}.|
> |**Name**:<br />InvalidTransformationParameterString<br />**Hex**:<br />80048508<br />**Number**:<br />-2147187448|The transformation parameter: {0} has an invalid input value: {1}. The parameter must be a string that is not empty.|
> |**Name**:<br />InvalidTransformationParameterZeroToRange<br />**Hex**:<br />80048509<br />**Number**:<br />-2147187447|The transformation parameter: {0} has an invalid input value: {1}. The parameter value must be greater than 0 and less than the length of the parameter 1.|
> |**Name**:<br />InvalidTransformationType<br />**Hex**:<br />8004037a<br />**Number**:<br />-2147220614|The specified transformation type is not supported.|
> |**Name**:<br />InvalidTranslationsFile<br />**Hex**:<br />80044249<br />**Number**:<br />-2147204535|The translations file is invalid or does not confirm to the required schema.|
> |**Name**:<br />InvalidTraversedPath<br />**Hex**:<br />80092007<br />**Number**:<br />-2146885625|Invalid traversed path.|
> |**Name**:<br />InvalidUniqueName<br />**Hex**:<br />80060386<br />**Number**:<br />-2147089530|Invalid unique name for action.|
> |**Name**:<br />InvalidUnpublishFromDraftArticle<br />**Hex**:<br />80048dfc<br />**Number**:<br />-2147185156|You are trying to unpublish an article that has a status of draft. You can only unpublish an article with the status of published.|
> |**Name**:<br />InvalidUnpublishFromUnapprovedArticle<br />**Hex**:<br />80048dfe<br />**Number**:<br />-2147185154|You are trying to unpublish an article that has a status of unapproved. You can only unpublish an article with the status of publish.|
> |**Name**:<br />InvalidUpdateOnProtectedComponent<br />**Hex**:<br />8004F012<br />**Number**:<br />-2147160046|You cannot update {0} {1}. Updates cannot be performed when {0} is managed.|
> |**Name**:<br />InvalidUrlConsecutiveSlashes<br />**Hex**:<br />80048056<br />**Number**:<br />-2147188650|The Url contains consecutive slashes which is not allowed.|
> |**Name**:<br />InvalidUrlProtocol<br />**Hex**:<br />8004E30F<br />**Number**:<br />-2147163377|The specified URL is invalid.|
> |**Name**:<br />InvalidUserAuth<br />**Hex**:<br />80040204<br />**Number**:<br />-2147220988|User does not have the privilege to perform this action.|
> |**Name**:<br />InvalidUserLicenseCount<br />**Hex**:<br />8004B027<br />**Number**:<br />-2147176409|Cannot purchase {0} user licenses for the Offering {1}.|
> |**Name**:<br />InvalidUserName<br />**Hex**:<br />80048095<br />**Number**:<br />-2147188587|You must enter the user name in the format <name>@<domain>. Correct the format and try again.|
> |**Name**:<br />InvalidUserQuota<br />**Hex**:<br />8004B011<br />**Number**:<br />-2147176431|You have reached the maximum number of user quota|
> |**Name**:<br />InvalidUserToImportExcelOnlineFile<br />**Hex**:<br />80060807<br />**Number**:<br />-2147088377|You don't have permission to import this file. Only the user who exported this data can import this file.|
> |**Name**:<br />InvalidUserToViewExcelOnlineFile<br />**Hex**:<br />80060806<br />**Number**:<br />-2147088378|You don't have permission to view this file. Only the user who exported this data can view this file.|
> |**Name**:<br />InvalidValueForCountryCode<br />**Hex**:<br />8004B022<br />**Number**:<br />-2147176414|Account Country/Region code must not be {0}|
> |**Name**:<br />InvalidValueForCurrency<br />**Hex**:<br />8004B023<br />**Number**:<br />-2147176413|Account currency code must not be {0}|
> |**Name**:<br />InvalidValueForDataDelimiter<br />**Hex**:<br />80040341<br />**Number**:<br />-2147220671|The data delimiter is invalid.|
> |**Name**:<br />InvalidValueForFieldDelimiter<br />**Hex**:<br />80040340<br />**Number**:<br />-2147220672|The field delimiter is invalid.|
> |**Name**:<br />InvalidValueForFileType<br />**Hex**:<br />80040348<br />**Number**:<br />-2147220664|The file type is invalid.|
> |**Name**:<br />InvalidValueForLocale<br />**Hex**:<br />8004B024<br />**Number**:<br />-2147176412|Account locale code must not be {0}|
> |**Name**:<br />InvalidValueProcessEmailAfter<br />**Hex**:<br />8005E244<br />**Number**:<br />-2147098044|The date in the Process Email From field is earlier than what is allowed for your organization. Enter a date that is later than the one specified, and try again.|
> |**Name**:<br />InvalidVersion<br />**Hex**:<br />8004023c<br />**Number**:<br />-2147220932|Unhandled Version mismatch found.|
> |**Name**:<br />InvalidViewReference<br />**Hex**:<br />800609B3<br />**Number**:<br />-2147087949|The view is not specified or is invalid.|
> |**Name**:<br />InvalidWebResourceForVisualization<br />**Hex**:<br />8004E017<br />**Number**:<br />-2147164137|The web resource type {0} is not supported for visualizations.|
> |**Name**:<br />InvalidWebresourceId<br />**Hex**:<br />8005012B<br />**Number**:<br />-2147155669|The webresource ID is invalid.|
> |**Name**:<br />InvalidWebresourceType<br />**Hex**:<br />8005012D<br />**Number**:<br />-2147155667|The web resource provided for the app icon is invalid.|
> |**Name**:<br />InvalidWebToLeadRedirect<br />**Hex**:<br />80048476<br />**Number**:<br />-2147187594|The redirectto is invalid for web2lead redirect.|
> |**Name**:<br />InvalidWelcomePageId<br />**Hex**:<br />8005012C<br />**Number**:<br />-2147155668|The welcome page ID is invalid.|
> |**Name**:<br />InvalidWelcomePageType<br />**Hex**:<br />8005012E<br />**Number**:<br />-2147155666|The web resource provided for the app Welcome page is invalid.|
> |**Name**:<br />InvalidWordDocumentTemplate<br />**Hex**:<br />800608EF<br />**Number**:<br />-2147088145|The document template is not valid.|
> |**Name**:<br />InvalidWordFileType<br />**Hex**:<br />800608EE<br />**Number**:<br />-2147088146|The file type isn't supported.|
> |**Name**:<br />InvalidWordTemplateContent<br />**Hex**:<br />800608FB<br />**Number**:<br />-2147088133|The template content is not valid.|
> |**Name**:<br />InvalidWordXmlFile<br />**Hex**:<br />80048441<br />**Number**:<br />-2147187647|Only Microsoft Word xml format files can be uploaded.|
> |**Name**:<br />InvalidWorkflowOrWorkflowDoesNotExist<br />**Hex**:<br />8006040a<br />**Number**:<br />-2147089398|Invalid workflow or workflow does not exist.|
> |**Name**:<br />InvalidXaml<br />**Hex**:<br />80060417<br />**Number**:<br />-2147089385|XAML for workflow is NULL or Empty|
> |**Name**:<br />InvalidXml<br />**Hex**:<br />80040201<br />**Number**:<br />-2147220991|Invalid XML.|
> |**Name**:<br />InvalidXmlCollectionNameException<br />**Hex**:<br />80040247<br />**Number**:<br />-2147220921|Invalid Xml collection name.|
> |**Name**:<br />InvalidXmlEntityNameException<br />**Hex**:<br />80040248<br />**Number**:<br />-2147220920|Invalid Xml entity name.|
> |**Name**:<br />InvalidXmlForParameters<br />**Hex**:<br />80060410<br />**Number**:<br />-2147089392|Parameters node for ControlStep have invalid XML in it|
> |**Name**:<br />InvalidXmlSSContent<br />**Hex**:<br />80040350<br />**Number**:<br />-2147220656|The data file can’t be imported because it contains invalid entity data or it’s in the wrong format. Make sure that the file contains correct data and that it’s in the XML Spreadsheet 2003 format, and then try uploading again.|
> |**Name**:<br />InvalidXrmSdkReference<br />**Hex**:<br />8004419b<br />**Number**:<br />-2147204709|Plug-in assembly references a version of Microsoft.Xrm.Sdk that is higher than the server version|
> |**Name**:<br />InvalidZipFileForImport<br />**Hex**:<br />80048482<br />**Number**:<br />-2147187582|The selected compressed (.zip) file contains files that can't be imported. A .zip file can contain only .xlsx, .csv, or .xml files.|
> |**Name**:<br />InvalidZipFileFormat<br />**Hex**:<br />80048488<br />**Number**:<br />-2147187576|The file that you're trying to upload isn't a valid file. Check the file and try again.|
> |**Name**:<br />InvitationBillingAdminUnknown<br />**Hex**:<br />8004D213<br />**Number**:<br />-2147167725|You are not a billing administrator for this organization and therefore, you cannot send invitations.  You can either contact your billing administrator and ask him or her to send the invitation, or the billing administrator can visit https://billing.microsoft.com and make you a delegate billing administrator. You can then send invitations.|
> |**Name**:<br />InvitationCannotBeReset<br />**Hex**:<br />8004D210<br />**Number**:<br />-2147167728|The invitation for the user cannot be reset.|
> |**Name**:<br />InvitationIsAccepted<br />**Hex**:<br />8004D208<br />**Number**:<br />-2147167736|{0} -- Invitation has already been accepted -- Token={1} Puid={2} Id={3} Status={4}|
> |**Name**:<br />InvitationIsExpired<br />**Hex**:<br />8004D207<br />**Number**:<br />-2147167737|{0} -- Invitation is expired -- Token={1} Puid={2} Id={3} Status={4}|
> |**Name**:<br />InvitationIsRejected<br />**Hex**:<br />8004D209<br />**Number**:<br />-2147167735|{0} -- Invitation has already been rejected by the new user-- Token={1} Puid={2} Id={3} Status={4}|
> |**Name**:<br />InvitationIsRevoked<br />**Hex**:<br />8004D20A<br />**Number**:<br />-2147167734|{0} -- Invitation has been revoked by the organization -- Token={1} Puid={2} Id={3} Status={4}|
> |**Name**:<br />InvitationNotFound<br />**Hex**:<br />8004D204<br />**Number**:<br />-2147167740|{0} -- Invitation not found or status is not Open -- Token={1} Puid={2} Id={3} Status={4}|
> |**Name**:<br />InvitationOrganizationNotEnabled<br />**Hex**:<br />8004D217<br />**Number**:<br />-2147167721|The organization for the invitation is not enabled.|
> |**Name**:<br />InvitationSendToSelf<br />**Hex**:<br />8004D20F<br />**Number**:<br />-2147167729|The invitation cannot be sent to yourself.|
> |**Name**:<br />InvitationStatusError<br />**Hex**:<br />8004D20C<br />**Number**:<br />-2147167732|"The invitation has status {0}."|
> |**Name**:<br />InvitationWrongUserOrgRelation<br />**Hex**:<br />8004D206<br />**Number**:<br />-2147167738|{0} -- The pre-created userorg relation {1} is wrong.  Authentication {2} is already used by another user|
> |**Name**:<br />InvitedUserAlreadyAdded<br />**Hex**:<br />8004D205<br />**Number**:<br />-2147167739|{0} -- The crm user {1} is already added, but to organization {2} instead of the inviting organization {3}|
> |**Name**:<br />InvitedUserAlreadyExists<br />**Hex**:<br />8004D202<br />**Number**:<br />-2147167742|{0} -- Invited user is already in an organization -- {1}|
> |**Name**:<br />InvitedUserIsOrganization<br />**Hex**:<br />8004D203<br />**Number**:<br />-2147167741|{0} -- The user {1} has authentication {2} and is already related to organization {3} with relation id {4}|
> |**Name**:<br />InvitedUserMultipleTimes<br />**Hex**:<br />8004D20B<br />**Number**:<br />-2147167733|The Dynamics 365 user {0} has been invited multiple times.|
> |**Name**:<br />InvitingOrganizationNotFound<br />**Hex**:<br />8004D200<br />**Number**:<br />-2147167744|{0} -- Inviting organization not found -- {1}|
> |**Name**:<br />InvitingUserNotInOrganization<br />**Hex**:<br />8004D201<br />**Number**:<br />-2147167743|{0} -- Inviting user is not in the inviting organization -- {1}|
> |**Name**:<br />IsKitCannotBeNull<br />**Hex**:<br />80044158<br />**Number**:<br />-2147204776|Attribute iskit cannot be null|
> |**Name**:<br />IsNotLiveToSendInvitation<br />**Hex**:<br />8004B009<br />**Number**:<br />-2147176439|This functionality is not supported, its only available for Online solution.|
> |**Name**:<br />IsvAborted<br />**Hex**:<br />80040265<br />**Number**:<br />-2147220891|ISV code aborted the operation.|
> |**Name**:<br />IsvExtensionsPrivilegeNotPresent<br />**Hex**:<br />80048029<br />**Number**:<br />-2147188695|To import ISV.Config, your user account must be associated with a security role that includes the ISV Extensions privilege.|
> |**Name**:<br />IsvUnExpected<br />**Hex**:<br />80040224<br />**Number**:<br />-2147220956|An unexpected error occurred from ISV code.|
> |**Name**:<br />JobNameIsEmptyOrNull<br />**Hex**:<br />80048457<br />**Number**:<br />-2147187625|Job Name can not be null or empty.|
> |**Name**:<br />KBInvalidCreateAssociation<br />**Hex**:<br />80060861<br />**Number**:<br />-2147088287|This KB article is already linked to the {0}.|
> |**Name**:<br />KnowledgeSearchActiveModelsAlreadyExist<br />**Hex**:<br />80061680<br />**Number**:<br />-2147084672|An active configuration already exists for source entity {0}. Only one active configuration is allowed per source entity.|
> |**Name**:<br />LabelIdDoesNotMatchStepId<br />**Hex**:<br />80060419<br />**Number**:<br />-2147089383|The label ID {0} doesn’t match the step ID {1}.|
> |**Name**:<br />LanguageProvisioningSrsDataConnectorNotInstalled<br />**Hex**:<br />8004F710<br />**Number**:<br />-2147158256|The Microsoft Dynamics 365 Reporting Extensions must be installed before the language can be provisioned for this organization.|
> |**Name**:<br />LeadAlreadyInClosedState<br />**Hex**:<br />80040519<br />**Number**:<br />-2147220199|The lead is already closed.|
> |**Name**:<br />LeadAlreadyInOpenState<br />**Hex**:<br />80040518<br />**Number**:<br />-2147220200|The lead is already in the open state.|
> |**Name**:<br />LegacyXlsxFileNotSupported<br />**Hex**:<br />800608CF<br />**Number**:<br />-2147088177|Legacy .xlsx files cannot be used for Excel Templates.|
> |**Name**:<br />LicenseConfigFileInvalid<br />**Hex**:<br />8004D250<br />**Number**:<br />-2147167664|The provided configuration file {0} has invalid formatting.|
> |**Name**:<br />LicenseNotEnoughToActivate<br />**Hex**:<br />80042f14<br />**Number**:<br />-2147209452|There are not enough licenses available for the number of users being activated.|
> |**Name**:<br />LicenseRegistrationExpired<br />**Hex**:<br />8004415d<br />**Number**:<br />-2147204771|The registration period for Microsoft Dynamics 365 has expired.|
> |**Name**:<br />LicenseTampered<br />**Hex**:<br />8004415f<br />**Number**:<br />-2147204769|The licensing for this installation of Microsoft Dynamics 365 has been tampered with. The system is unusable. Please contact Microsoft Product Support Services.|
> |**Name**:<br />LicenseTrialExpired<br />**Hex**:<br />8004415c<br />**Number**:<br />-2147204772|The trial installation of Microsoft Dynamics 365 has expired.|
> |**Name**:<br />LicenseUpgradePathNotAllowed<br />**Hex**:<br />8004D247<br />**Number**:<br />-2147167673|Cannot upgrade to specified license type.|
> |**Name**:<br />LinkedEntitiesAreNotAllowed<br />**Hex**:<br />80071120<br />**Number**:<br />-2147020512|Linked Entities Are Not Allowed in the filter|
> |**Name**:<br />LiveAdminUnknownCommand<br />**Hex**:<br />8004D239<br />**Number**:<br />-2147167687|Unknown administration command {0}|
> |**Name**:<br />LiveAdminUnknownObject<br />**Hex**:<br />8004D238<br />**Number**:<br />-2147167688|Unknown administration target {0}|
> |**Name**:<br />LivePlatformEmailInvalidBody<br />**Hex**:<br />8004B524<br />**Number**:<br />-2147175132|The "Body" parameter is blank or null|
> |**Name**:<br />LivePlatformEmailInvalidFrom<br />**Hex**:<br />8004B522<br />**Number**:<br />-2147175134|The "From" parameter is blank or null|
> |**Name**:<br />LivePlatformEmailInvalidSubject<br />**Hex**:<br />8004B523<br />**Number**:<br />-2147175133|The "Subject" parameter is blank or null|
> |**Name**:<br />LivePlatformEmailInvalidTo<br />**Hex**:<br />8004B521<br />**Number**:<br />-2147175135|The "To" parameter is blank or null|
> |**Name**:<br />LivePlatformGeneralEmailError<br />**Hex**:<br />8005B520<br />**Number**:<br />-2147109600|An Email Error Occurred|
> |**Name**:<br />LocalDataSourceAbortError<br />**Hex**:<br />80072453<br />**Number**:<br />-2147015597|The browser operation stopped. Please try again.|
> |**Name**:<br />LocalDataSourceDatabaseError<br />**Hex**:<br />80072455<br />**Number**:<br />-2147015595|The browser operation failed due to browser database errors. Please try again. If it doesn’t work, try the same operation again by ensuring that your device remains unlocked until the operation completes.|
> |**Name**:<br />LocalDataSourceError<br />**Hex**:<br />80072451<br />**Number**:<br />-2147015599|The operation failed. Please try again.|
> |**Name**:<br />LocalDataSourceQuotaExceededError<br />**Hex**:<br />80072452<br />**Number**:<br />-2147015598|The operation failed because there was not enough space in the browser storage quota or the browser storage quota was reached, and the user declined to provide more space to the browser database.|
> |**Name**:<br />LocalDataSourceTimeOutError<br />**Hex**:<br />80072454<br />**Number**:<br />-2147015596|The operation timed out. Please try again.|
> |**Name**:<br />LockStatusNotValidForDynamicList<br />**Hex**:<br />8004F703<br />**Number**:<br />-2147158269|Lock Status cannot be specified for a dynamic list.|
> |**Name**:<br />LogoImageNodeDoesNotExist<br />**Hex**:<br />800608D2<br />**Number**:<br />-2147088174|Logo Image node in organization cache theme data doesnot exist.|
> |**Name**:<br />LongParseRow<br />**Hex**:<br />80040372<br />**Number**:<br />-2147220622|The row is too long to import|
> |**Name**:<br />LookupNotFound<br />**Hex**:<br />80040353<br />**Number**:<br />-2147220653|The lookup reference could not be resolved|
> |**Name**:<br />LowerVersionUpgrade<br />**Hex**:<br />80048541<br />**Number**:<br />-2147187391|The import solution must have a higher version than the existing solution it is upgrading.|
> |**Name**:<br />LowQuantityGreaterThanHighQuantity<br />**Hex**:<br />80043b01<br />**Number**:<br />-2147206399|Low quantity should be less than high quantity.|
> |**Name**:<br />LowQuantityLessThanZero<br />**Hex**:<br />80043b00<br />**Number**:<br />-2147206400|Low quantity should be greater than zero.|
> |**Name**:<br />MailApp_AppointmentFeatureNotEnabled<br />**Hex**:<br />80061218<br />**Number**:<br />-2147085800|Access to the app hasn’t been enabled for Appointments for this Microsoft Dynamics 365 organization. Contact your system administrator to enable access for appointments.|
> |**Name**:<br />MailApp_DifferentSecurityZoneError<br />**Hex**:<br />80061210<br />**Number**:<br />-2147085808|Try adding the following URLs to your Trusted Sites:{0} {1} {2}|
> |**Name**:<br />MailApp_EmailAddressMismatch<br />**Hex**:<br />80061211<br />**Number**:<br />-2147085807|It looks like you're trying to access the CRM App for Outlook from an email address that we don't recognize. Either sign out and sign in with the email address you use for Dynamics CRM or have your system administrator update your email Mailbox settings to reflect this email address.|
> |**Name**:<br />MailApp_FeatureControlBitDisabled<br />**Hex**:<br />80061204<br />**Number**:<br />-2147085820|Access to the app hasn’t been enabled for this Dynamics 365 organization. Contact your system administrator to enable access to this app.|
> |**Name**:<br />MailApp_MailboxNotConfiguredWithServerSideSync<br />**Hex**:<br />80061202<br />**Number**:<br />-2147085822|Email account isn't configured with server-side synchronization for incoming email|
> |**Name**:<br />MailApp_MailboxNotConfiguredWithServerSideSyncForACT<br />**Hex**:<br />80061217<br />**Number**:<br />-2147085801|Email account isn’t configured with server-side sync for appointments, contacts, and tasks|
> |**Name**:<br />MailApp_MailboxServerSideSyncConfigurationFailure<br />**Hex**:<br />80061220<br />**Number**:<br />-2147085792|Microsoft Dynamics 365 server-side synchronization failed for incoming emails.|
> |**Name**:<br />MailApp_MailboxServerSideSyncConfigurationFailureForACT<br />**Hex**:<br />80061221<br />**Number**:<br />-2147085791|Microsoft Dynamics 365 server-side synchronization failed for appointments.|
> |**Name**:<br />MailApp_MobileBrowserIsNotSupported<br />**Hex**:<br />80061208<br />**Number**:<br />-2147085816|The mobile browser version of Outlook is currently unsupported. Please try again from the Outlook desktop application.|
> |**Name**:<br />MailApp_PermissionsToReadContactRequired<br />**Hex**:<br />80061219<br />**Number**:<br />-2147085799|Can't check to see if the recipients are in Dynamics 365 because user doesn't have sufficient privileges|
> |**Name**:<br />MailApp_PermissionToUseCrmForOfficeAppsRequired<br />**Hex**:<br />80061205<br />**Number**:<br />-2147085819|User doesn't have permission to access app|
> |**Name**:<br />MailApp_ReadWriteAccessRequired<br />**Hex**:<br />80061203<br />**Number**:<br />-2147085821|User only has administrative access to Dynamics 365|
> |**Name**:<br />MailApp_TrackingIsNotSupported<br />**Hex**:<br />80061207<br />**Number**:<br />-2147085817|This version of Outlook doesn't support tracking new emails.|
> |**Name**:<br />MailApp_UnsupportedBrowser<br />**Hex**:<br />80061201<br />**Number**:<br />-2147085823|Your browser is currently unsupported.|
> |**Name**:<br />MailApp_UnsupportedDevice<br />**Hex**:<br />80061200<br />**Number**:<br />-2147085824|Your device is currently unsupported.|
> |**Name**:<br />MailApp_UserMailboxInactive<br />**Hex**:<br />80061216<br />**Number**:<br />-2147085802|User's mailbox is inactive|
> |**Name**:<br />MailAppLimitedMode<br />**Hex**:<br />80061222<br />**Number**:<br />-2147085790|Generic Error when Server-side sync isn't configured properly and MailApp is only allowed to be loaded in LimitedMode|
> |**Name**:<br />MailboxCannotDeleteEmails<br />**Hex**:<br />8005E233<br />**Number**:<br />-2147098061|The Delete Emails after Processing option cannot be set to Yes for user mailboxes.|
> |**Name**:<br />MailboxCannotModifyEmailAddress<br />**Hex**:<br />8005E208<br />**Number**:<br />-2147098104|E-mail Address of a mailbox cannot be updated when associated with an user/queue.|
> |**Name**:<br />MailboxCredentialNotSpecified<br />**Hex**:<br />8005E209<br />**Number**:<br />-2147098103|Username is not specified|
> |**Name**:<br />MailboxTrackingFolderMappingCannotBeUpdated<br />**Hex**:<br />8006088C<br />**Number**:<br />-2147088244|The mailbox tracking folder mapping cannot be updated.|
> |**Name**:<br />MailboxUnsupportedEmailServerType<br />**Hex**:<br />8005E247<br />**Number**:<br />-2147098041|Server-side synchronization for appointments, contacts, and tasks isn't supported for POP3 or SMTP server types. Select a supported email type or change the synchronization method for appointments, contacts, and tasks to None.|
> |**Name**:<br />ManagedBpfDeletionInvalid<br />**Hex**:<br />80060383<br />**Number**:<br />-2147089533| The business process flow is part of a managed solution and cannot be individually deleted. Uninstall the parent solution to remove the business process flow.|
> |**Name**:<br />ManagedProcessDeletionError<br />**Hex**:<br />80072457<br />**Number**:<br />-2147015593|The process is part of a managed solution and cannot be individually deleted. Uninstall the parent solution to remove the process.|
> |**Name**:<br />ManifestParsingFailure<br />**Hex**:<br />80048534<br />**Number**:<br />-2147187404|Failed to parse the specified manifest file to retrieve OrganizationId|
> |**Name**:<br />ManifestXsdValidationError<br />**Hex**:<br />80160001<br />**Number**:<br />-2146041855|The import manifest file is invalid. XSD validation failed with the following error: '{0}'."|
> |**Name**:<br />ManyToManyVirtualEntityNotSupported<br />**Hex**:<br />80044820<br />**Number**:<br />-2147203040|An N:N relationship between virtual entities is not supported.|
> |**Name**:<br />MappingExistsForTargetAttribute<br />**Hex**:<br />8004033e<br />**Number**:<br />-2147220674|This attribute is mapped more than once. Remove any duplicate mappings, and then import this data map again.|
> |**Name**:<br />MarsConnectorDisableFailure<br />**Hex**:<br />80071108<br />**Number**:<br />-2147020536|Error occurred while disabling Mars connector.|
> |**Name**:<br />MarsConnectorEnableFailure<br />**Hex**:<br />80071107<br />**Number**:<br />-2147020537|Error occurred while enabling Mars connector.|
> |**Name**:<br />MatchingAttributeNameNotNullError<br />**Hex**:<br />80044243<br />**Number**:<br />-2147204541|Matching attribute name should be null single entity rule.|
> |**Name**:<br />MaxActiveSLAError<br />**Hex**:<br />8004F897<br />**Number**:<br />-2147157865|You can’t activate this SLA because you’ve exceeded the maxiumum number of entities that can have active SLAs for your organization.|
> |**Name**:<br />MaxActiveSLAKPIError<br />**Hex**:<br />8004F898<br />**Number**:<br />-2147157864|You can’t activate this SLA because you’ve exceeded the maxiumum number of SLA KPIs that are allowed per entity for your organization.|
> |**Name**:<br />MaxChildCasesLimitExceeded<br />**Hex**:<br />8003F454<br />**Number**:<br />-2147224492|A Parent Case cannot have more than maximum child cases allowed. Contact your administrator for more details|
> |**Name**:<br />MaxConditionsMobileOfflineFilters<br />**Hex**:<br />80071114<br />**Number**:<br />-2147020524|You can only define 3 Mobile offline Org  filter for each entity.|
> |**Name**:<br />MaximumControlsLimitExceeded<br />**Hex**:<br />8004E301<br />**Number**:<br />-2147163391|The dashboard Form XML contains more than the maximum allowed number of control elements: {0}.|
> |**Name**:<br />MaximumCountForUpdateModeExceeded<br />**Hex**:<br />8004F602<br />**Number**:<br />-2147158526|In an update operation, you can import only one file at a time.|
> |**Name**:<br />MaximumNumberHandlersExceeded<br />**Hex**:<br />80048505<br />**Number**:<br />-2147187451|This solution adds form event handlers so the number of event handlers for a form event exceeds the maximum number.|
> |**Name**:<br />MaximumNumberOfAttributesForEntityReached<br />**Hex**:<br />8004841A<br />**Number**:<br />-2147187686|The maximum number of attributes allowed for an entity has already been reached. The attribute cannot be created.|
> |**Name**:<br />MaxLimitForRollupAttribute<br />**Hex**:<br />8004480a<br />**Number**:<br />-2147203062|Only three metric details per metric can be created.|
> |**Name**:<br />MaxMatchCodeLengthExceeded<br />**Hex**:<br />80048429<br />**Number**:<br />-2147187671|The rule condition cannot be created or updated because it would cause the matchcode length to exceed the maximum limit.|
> |**Name**:<br />MaxProductsAllowed<br />**Hex**:<br />80071020<br />**Number**:<br />-2147020768|You cannot create more than {0} products.|
> |**Name**:<br />MaxprofileItemFilterConditionsAllowed<br />**Hex**:<br />80071116<br />**Number**:<br />-2147020522|You can only define 6 Mobile offline entity filter conditions for each entity.|
> |**Name**:<br />MaxUnzipFolderSizeExceeded<br />**Hex**:<br />80048499<br />**Number**:<br />-2147187559|The selected compressed (.zip) file can't be unzipped because it's too large.|
> |**Name**:<br />MeasureDataTypeInvalid<br />**Hex**:<br />8004E010<br />**Number**:<br />-2147164144|The Data Description for the visualization is invalid. The attribute type for one of the non aggregate measures is invalid. Correct the Data Description.|
> |**Name**:<br />MemberHasAlreadyBeenContacted<br />**Hex**:<br />8004140e<br />**Number**:<br />-2147216370|This marketing list member was not contacted, because the member has previously received this communication.|
> |**Name**:<br />MergeActiveQuoteError<br />**Hex**:<br />80045302<br />**Number**:<br />-2147200254|Merge cannot be performed on sub-entity that has active quote.|
> |**Name**:<br />MergeCyclicalParentingError<br />**Hex**:<br />80045300<br />**Number**:<br />-2147200256|Merge could create cyclical parenting.|
> |**Name**:<br />MergeDifferentlyParentedWarning<br />**Hex**:<br />80045316<br />**Number**:<br />-2147200234|Merge warning: sub-entity will be differently parented.|
> |**Name**:<br />MergeEntitiesIdenticalError<br />**Hex**:<br />80045305<br />**Number**:<br />-2147200251|Merge cannot be performed on master and sub-entities that are identical.|
> |**Name**:<br />MergeEntityNotActiveError<br />**Hex**:<br />80045304<br />**Number**:<br />-2147200252|Merge cannot be performed on entity that is inactive.|
> |**Name**:<br />MergeLossOfParentingWarning<br />**Hex**:<br />80045317<br />**Number**:<br />-2147200233|Merge warning: sub-entity might lose parenting|
> |**Name**:<br />MergeSecurityError<br />**Hex**:<br />80045301<br />**Number**:<br />-2147200255|Merge is not allowed: caller does not have the privilege or access.|
> |**Name**:<br />MetadataNoMapping<br />**Hex**:<br />80040e01<br />**Number**:<br />-2147217919|The mapping between specified entities does not exist|
> |**Name**:<br />MetadataNotFound<br />**Hex**:<br />8004024a<br />**Number**:<br />-2147220918|Metadata not found.|
> |**Name**:<br />MetadataNotSerializable<br />**Hex**:<br />80040e03<br />**Number**:<br />-2147217917|The given metadata entity is not serializable|
> |**Name**:<br />MetadataRecordNotDeletable<br />**Hex**:<br />80044250<br />**Number**:<br />-2147204528|The metadata record being deleted cannot be deleted by the end user|
> |**Name**:<br />MetadataSyncRequired<br />**Hex**:<br />80072510<br />**Number**:<br />-2147015408|Metadata sync required|
> |**Name**:<br />MetricEntityOrFieldDeleted<br />**Hex**:<br />8004F687<br />**Number**:<br />-2147158393|The entity or field that is referenced in the goal metric is not valid|
> |**Name**:<br />MetricNameAlreadyExists<br />**Hex**:<br />80044802<br />**Number**:<br />-2147203070|A goal metric with the same name already exists. Specify a different name, and try again.|
> |**Name**:<br />MinMaxValidationFailed<br />**Hex**:<br />80061004<br />**Number**:<br />-2147086332|The value is out of range.|
> |**Name**:<br />MissingBOWFRules<br />**Hex**:<br />80040329<br />**Number**:<br />-2147220695|Bulk Operation related workflow rules are missing.|
> |**Name**:<br />MissingBusinessId<br />**Hex**:<br />8004021a<br />**Number**:<br />-2147220966|The business id is missing or invalid.|
> |**Name**:<br />MissingColumn<br />**Hex**:<br />8004B028<br />**Number**:<br />-2147176408|The property bag is missing an entry for {0}.|
> |**Name**:<br />MissingControlStep<br />**Hex**:<br />80060385<br />**Number**:<br />-2147089531|Required control step is missing.|
> |**Name**:<br />MissingCrmAuthenticationToken<br />**Hex**:<br />80044300<br />**Number**:<br />-2147204352|CrmAuthenticationToken is missing.|
> |**Name**:<br />MissingCrmAuthenticationTokenOrganizationName<br />**Hex**:<br />80044308<br />**Number**:<br />-2147204344|Organization Name must be specified in CrmAuthenticationToken.|
> |**Name**:<br />MissingHierarchicalRelationshipForOperator<br />**Hex**:<br />80047020<br />**Number**:<br />-2147192800|This query uses a hierarchical operator, but the {0} entity doesn't have a hierarchical relationship.|
> |**Name**:<br />MissingOpportunityId<br />**Hex**:<br />80043b15<br />**Number**:<br />-2147206379|The opportunity id is missing or invalid.|
> |**Name**:<br />MissingOrganizationFriendlyName<br />**Hex**:<br />8004B00A<br />**Number**:<br />-2147176438|Cannot install Dynamics 365 without an organization friendly name.|
> |**Name**:<br />MissingOrganizationUniqueName<br />**Hex**:<br />8004B00B<br />**Number**:<br />-2147176437|Cannot install Dynamics 365 without an organization unique name.|
> |**Name**:<br />MissingOrInvalidRedirectId<br />**Hex**:<br />80048473<br />**Number**:<br />-2147187597|The RedirId parameter is missing for the partner redirect.|
> |**Name**:<br />MissingOwner<br />**Hex**:<br />80040215<br />**Number**:<br />-2147220971|Item does not have an owner.|
> |**Name**:<br />MissingParameter<br />**Hex**:<br />8004031f<br />**Number**:<br />-2147220705|A required parameter is missing for the Bulk Operation|
> |**Name**:<br />MissingParameterToMethod<br />**Hex**:<br />8004B021<br />**Number**:<br />-2147176415|Missing parameter {0} to method {1}|
> |**Name**:<br />MissingParameterToStoredProcedure<br />**Hex**:<br />8004C000<br />**Number**:<br />-2147172352|Missing parameter to stored procedure:  {0}|
> |**Name**:<br />MissingPriceLevelId<br />**Hex**:<br />80043b12<br />**Number**:<br />-2147206382|The price level id is missing.|
> |**Name**:<br />MissingProductId<br />**Hex**:<br />80043b11<br />**Number**:<br />-2147206383|The product id is missing.|
> |**Name**:<br />MissingQuantity<br />**Hex**:<br />80081012<br />**Number**:<br />-2146955246|The Quantity is missing.|
> |**Name**:<br />MissingQueryType<br />**Hex**:<br />80040235<br />**Number**:<br />-2147220939|The query type is missing.|
> |**Name**:<br />MissingRecipient<br />**Hex**:<br />8004350d<br />**Number**:<br />-2147207923|The fax must have a recipient before it can be sent.|
> |**Name**:<br />MissingRequiredAttributes<br />**Hex**:<br />80061037<br />**Number**:<br />-2147086281|The property couldn’t be created or updated because the regardingobjectid, datatype, or name attribute is missing.|
> |**Name**:<br />MissingRequiredComponentAttributes<br />**Hex**:<br />80072002<br />**Number**:<br />-2147016702|Required attribute should not be null. Attribute: {0}|
> |**Name**:<br />MissingTeamName<br />**Hex**:<br />80041d0b<br />**Number**:<br />-2147214069|The team name was unexpectedly missing.|
> |**Name**:<br />MissingUomId<br />**Hex**:<br />80043b0d<br />**Number**:<br />-2147206387|The unit id is missing.|
> |**Name**:<br />MissingUomScheduleId<br />**Hex**:<br />80043b0a<br />**Number**:<br />-2147206390|The unit schedule id is missing.|
> |**Name**:<br />MissingUserId<br />**Hex**:<br />8004021b<br />**Number**:<br />-2147220965|The user id or the team id is missing.|
> |**Name**:<br />MissingWebToLeadRedirect<br />**Hex**:<br />80048477<br />**Number**:<br />-2147187593|The redirectto is missing for web2lead redirect.|
> |**Name**:<br />MobileClientLanguageNotSupported<br />**Hex**:<br />8005F201<br />**Number**:<br />-2147094015|The application could not find a supported language on the server. Contact an administrator to enable a supported language|
> |**Name**:<br />MobileClientNotConfiguredForCurrentUser<br />**Hex**:<br />8005F20E<br />**Number**:<br />-2147094002|Try this action again. If the problem continues, check the {0} for solutions or contact your organization's {#Brand_CRM} Administrator. Finally, you can contact {1}.|
> |**Name**:<br />MobileClientVersionNotSupported<br />**Hex**:<br />8005F202<br />**Number**:<br />-2147094014|Mobile Client version is not supported|
> |**Name**:<br />MobileExcelFeatureNotEnabled<br />**Hex**:<br />800608CA<br />**Number**:<br />-2147088182|Mobile export to excel feature is not enabled.|
> |**Name**:<br />MobileOfflineDaysSinceRecordLastModifiedZero<br />**Hex**:<br />80060990<br />**Number**:<br />-2147087984|No records will be available in the mobile offline mode if the value for number of days is 0.|
> |**Name**:<br />MobileOfflineProfileItemNameAlreadyExists<br />**Hex**:<br />800609A8<br />**Number**:<br />-2147087960|A mobile offline profile item with this name already exists for this mobile offline profile. Enter a unique name.|
> |**Name**:<br />MobileOfflineProfileItemNameCanNotBeNullOrEmpty<br />**Hex**:<br />800609AA<br />**Number**:<br />-2147087958|The mobile offline profile item name can’t be null or empty. Enter a name for this profile item.|
> |**Name**:<br />MobileOfflineProfileNameAlreadyExists<br />**Hex**:<br />800609A7<br />**Number**:<br />-2147087961|A mobile offline profile with this name already exists. Enter a unique name.|
> |**Name**:<br />MobileOfflineProfileNameCanNotBeNullOrEmpty<br />**Hex**:<br />800609A9<br />**Number**:<br />-2147087959|The mobile offline profile name can’t be null or empty. Enter a name for this profile.|
> |**Name**:<br />MobileOfflineRuleEnhancementFeatureNotAvailaible<br />**Hex**:<br />80071117<br />**Number**:<br />-2147020521|This feature is not enabled for your organization. Please contact your system administrator for help.|
> |**Name**:<br />MobileServiceError<br />**Hex**:<br />8004B070<br />**Number**:<br />-2147176336|Error communicating with mobile service|
> |**Name**:<br />ModernFlowProcessesNotEnabled<br />**Hex**:<br />80060464<br />**Number**:<br />-2147089308|Creation of Modern Flow processes is not enabled.|
> |**Name**:<br />ModernFlowProcessesOnlyAvailableOnline<br />**Hex**:<br />80060465<br />**Number**:<br />-2147089307|Creation of Modern Flow processes is only available online.|
> |**Name**:<br />MoneySizeExceeded<br />**Hex**:<br />80040317<br />**Number**:<br />-2147220713|Supplied value exceeded the MIN/MAX value of Money Type field.|
> |**Name**:<br />MOPIAssociationNameCannotBeEmptyOrSpace<br />**Hex**:<br />80060997<br />**Number**:<br />-2147087977|The Mobile Offline Profile Item Association name can’t be a space or an empty string.|
> |**Name**:<br />MoveBothToPrimary<br />**Hex**:<br />8004D234<br />**Number**:<br />-2147167692|Move operation would put both instances on the same server:  Database = {0}  Old Primary = {1}  Old Secondary = {2}  New Secondary = {3}|
> |**Name**:<br />MoveBothToSecondary<br />**Hex**:<br />8004D235<br />**Number**:<br />-2147167691|Move operation would put both instances on the same server:  Database = {0}  Old Primary = {1}  Old Secondary = {2}  New Secondary = {3}|
> |**Name**:<br />MoveOrganizationFailedNotDisabled<br />**Hex**:<br />8004D236<br />**Number**:<br />-2147167690|Move operation failed because organization {0} is not disabled|
> |**Name**:<br />MultilevelParentChildRelationshipNotAllowed<br />**Hex**:<br />8003F453<br />**Number**:<br />-2147224493|Associating child cases to the existing child case is not allowed.|
> |**Name**:<br />MultipleChartAreasFound<br />**Hex**:<br />8004E008<br />**Number**:<br />-2147164152|Multiple Chart Areas are not supported.|
> |**Name**:<br />MultipleChildPicklist<br />**Hex**:<br />80040250<br />**Number**:<br />-2147220912|Crm Internal Exception: Picklists with more than one childAttribute are not supported.|
> |**Name**:<br />MultipleFilesFound<br />**Hex**:<br />80048439<br />**Number**:<br />-2147187655|The attachment file name is not unique.|
> |**Name**:<br />MultipleFormElementsFound<br />**Hex**:<br />8004E304<br />**Number**:<br />-2147163388|A dashboard Form XML can contain only one form element.|
> |**Name**:<br />MultipleLabelsInUserDashboard<br />**Hex**:<br />8004E30D<br />**Number**:<br />-2147163379|A user dashboard can have at most one label for a form element.|
> |**Name**:<br />MultipleMeasureCollectionsFound<br />**Hex**:<br />8004E01C<br />**Number**:<br />-2147164132|More than one measure collection is not supported for charts with subcategory i.e. comparison charts|
> |**Name**:<br />MultipleMeasuresFound<br />**Hex**:<br />8004E007<br />**Number**:<br />-2147164153|More than one measure is not supported for charts with subcategory i.e. comparison charts|
> |**Name**:<br />MultipleOrganizationsNotAllowed<br />**Hex**:<br />80041d35<br />**Number**:<br />-2147214027|Only one organization and one root business are allowed.|
> |**Name**:<br />MultipleParentReportsFound<br />**Hex**:<br />80040485<br />**Number**:<br />-2147220347|More than one report link found. Each report can have only one parent.|
> |**Name**:<br />MultipleParentsNotSupported<br />**Hex**:<br />80047007<br />**Number**:<br />-2147192825|An entity can have only one parental relationship|
> |**Name**:<br />MultiplePartnerSecurityRoleWithSameInformation<br />**Hex**:<br />8004A10a<br />**Number**:<br />-2147180278|More than one security role found for partner user|
> |**Name**:<br />MultiplePartnerUserWithSameInformation<br />**Hex**:<br />8004A10b<br />**Number**:<br />-2147180277|More than one partner user found with same information|
> |**Name**:<br />MultipleQueueItemsFound<br />**Hex**:<br />80040525<br />**Number**:<br />-2147220187|This item occurs in more than one queue and cannot be routed from this list. Locate the item in a queue and try to route the item again.|
> |**Name**:<br />MultipleRecordsFoundByEntityKey<br />**Hex**:<br />8006089D<br />**Number**:<br />-2147088227|More than one record exists for entity {0} with entity key involving attributes {1}|
> |**Name**:<br />MultipleRelationshipsNotSupported<br />**Hex**:<br />80048200<br />**Number**:<br />-2147188224|Multiple relationships are not supported|
> |**Name**:<br />MultipleRootBusinessUnit<br />**Hex**:<br />8004A10c<br />**Number**:<br />-2147180276|More than one root business unit found|
> |**Name**:<br />MultipleSitemapsFound<br />**Hex**:<br />80050120<br />**Number**:<br />-2147155680|Found {0} unpublished site maps but expected only 1|
> |**Name**:<br />MultipleSubcategoriesFound<br />**Hex**:<br />8004E006<br />**Number**:<br />-2147164154|The data XML for the visualization cannot contain more than two Group By clauses.|
> |**Name**:<br />MultiValueParameterFound<br />**Hex**:<br />8005E00A<br />**Number**:<br />-2147098614|Fetch xml parameter {0} cannot obtain multiple values. Change report parameter {0} to single value parameter and try again.|
> |**Name**:<br />MustContainAtLeastACharInMention<br />**Hex**:<br />8004F6A4<br />**Number**:<br />-2147158364|The display name must contain atleast one non-whitespace character.|
> |**Name**:<br />NavigationPropertyAlreadyExists<br />**Hex**:<br />80072551<br />**Number**:<br />-2147015343|NavigationPropertyName {0} is not unique within an entity|
> |**Name**:<br />NavigationPropertyNameCannotBeTheSameOnBothSidesOfRel<br />**Hex**:<br />80072550<br />**Number**:<br />-2147015344|Navigation Property Name cannot be the same on both sides of a self-referential relationship. SchemaName - {0}|
> |**Name**:<br />NavPaneNotCustomizable<br />**Hex**:<br />80044329<br />**Number**:<br />-2147204311|The nav pane properties for this relationship are not customizable|
> |**Name**:<br />NavPaneOrderValueNotAllowed<br />**Hex**:<br />80044327<br />**Number**:<br />-2147204313|The provided nav pane order value is not allowed|
> |**Name**:<br />NetworkIssue<br />**Hex**:<br />8005F104<br />**Number**:<br />-2147094268|Request failed due to unknown network issues or GateWay issues or server issues.|
> |**Name**:<br />NewStatusHasInvalidState<br />**Hex**:<br />80044322<br />**Number**:<br />-2147204318|The state value that was provided for this new status option does not exist.|
> |**Name**:<br />NewStatusRequiresAssociatedState<br />**Hex**:<br />80044321<br />**Number**:<br />-2147204319|The new status option must have an associated state value.|
> |**Name**:<br />NoActiveLocation<br />**Hex**:<br />80060900<br />**Number**:<br />-2147088128|No active location found.|
> |**Name**:<br />NoAppModuleComponentReferred<br />**Hex**:<br />8005011B<br />**Number**:<br />-2147155685|No component is referenced|
> |**Name**:<br />NoAttributesForEntityCreate<br />**Hex**:<br />80047014<br />**Number**:<br />-2147192812|No attributes for Create Entity action.|
> |**Name**:<br />NoConditionRuleCreationNotAllowedForSetValueShowError<br />**Hex**:<br />80060013<br />**Number**:<br />-2147090413|The "Show error message" and "Set value" actions can't be used in a business rule that doesn't have a condition.|
> |**Name**:<br />NoConnectionRoleAndObjectTypeCodePairPresent<br />**Hex**:<br />8004F222<br />**Number**:<br />-2147159518|There are no ConnectionRoleId and AssociatedObjectTypeCode pairs present. Entities being connected: ({0},{1}); Entity Records being connected: ({2},{3}); Record1ConnectionRoleName: {4}, Record2ConnectionRoleName: {5}. ConnectionRoleIds : {6}|
> |**Name**:<br />NoConversionRule<br />**Hex**:<br />800608F5<br />**Number**:<br />-2147088139|A ConversionRule is required for the tool to run.|
> |**Name**:<br />NoDataFilterSelectedForOtherDataFilter<br />**Hex**:<br />80071138<br />**Number**:<br />-2147020488|The entity '{0}' in the profile '{1}' contained the Data Download Filter 'Other data filter' however no data filter option was selected. The entity must specify a data filter option.|
> |**Name**:<br />NoDataForVisualization<br />**Hex**:<br />8004E011<br />**Number**:<br />-2147164143|There is no data to create this visualization.|
> |**Name**:<br />NoDefaultValueForOptionSetArgument<br />**Hex**:<br />80060396<br />**Number**:<br />-2147089514|Arguments of type OptionSet must have a default value set.|
> |**Name**:<br />NoDefinedRelationshipsForMOPIAssociation<br />**Hex**:<br />80060998<br />**Number**:<br />-2147087976|The Profile Item Association entity doesn’t have any defined relationships.|
> |**Name**:<br />NoDialNumber<br />**Hex**:<br />8004350f<br />**Number**:<br />-2147207921|There is no fax number specified on the fax or for the recipient.|
> |**Name**:<br />NoEntitiesForBulkDelete<br />**Hex**:<br />80048442<br />**Number**:<br />-2147187646|The Bulk Delete Wizard cannot be opened because there are no valid entities for deletion.|
> |**Name**:<br />NoEntitySpecified<br />**Hex**:<br />800608FA<br />**Number**:<br />-2147088134|At least one Entity is expected by the tool to process.|
> |**Name**:<br />NoFilesSelected<br />**Hex**:<br />80071021<br />**Number**:<br />-2147020767|No documents are selected to copy. Please select a document and try again.|
> |**Name**:<br />NoHeaderColumnFound<br />**Hex**:<br />80040368<br />**Number**:<br />-2147220632|A column heading is missing.|
> |**Name**:<br />NoIncidentMergeHavingSameParent<br />**Hex**:<br />8003F450<br />**Number**:<br />-2147224496|Child cases having different parent case associated can not be merged.|
> |**Name**:<br />NoLabelsAssociatedWithStep<br />**Hex**:<br />80060408<br />**Number**:<br />-2147089400|{0} does not have any labels associated with it|
> |**Name**:<br />NoLanguageProvisioned<br />**Hex**:<br />80044199<br />**Number**:<br />-2147204711|There is no language provisioned for this organization.|
> |**Name**:<br />NoLicenseInConfigDB<br />**Hex**:<br />8004D241<br />**Number**:<br />-2147167679|No license exists in MSCRM_CONFIG database.|
> |**Name**:<br />NoMinimumRequiredPrivilegesForTabletApp<br />**Hex**:<br />8005F20F<br />**Number**:<br />-2147094001|You do not have sufficient permissions on the server to load the application.\nPlease contact your administrator to update your permissions.|
> |**Name**:<br />NoMoreCustomOptionValuesExist<br />**Hex**:<br />8004431F<br />**Number**:<br />-2147204321|All available custom option values have been used.|
> |**Name**:<br />NoncompliantXml<br />**Hex**:<br />80048425<br />**Number**:<br />-2147187675|The input XML does not comply with the XML schema.|
> |**Name**:<br />NonCrmUIInteractiveWorkflowNotSupported<br />**Hex**:<br />80045044<br />**Number**:<br />-2147200956|This interactive workflow cannot be created, updated or published because it was created outside the Microsoft Dynamics 365 Web application.|
> |**Name**:<br />NonCrmUIWorkflowsNotSupported<br />**Hex**:<br />80045040<br />**Number**:<br />-2147200960|This workflow cannot be created, updated or published because it was created outside the Microsoft Dynamics 365 Web application. Your organization does not allow this type of workflow.|
> |**Name**:<br />NonDraftBundleUpdate<br />**Hex**:<br />80061039<br />**Number**:<br />-2147086279|Product Association cannot be updated when bundle is in invalid state.|
> |**Name**:<br />NonInteractiveUserCannotAccessUI<br />**Hex**:<br />80044160<br />**Number**:<br />-2147204768|Non-interactive users cannot access the web user interface. Contact your organization system administrator.|
> |**Name**:<br />NonMappableEntity<br />**Hex**:<br />80046200<br />**Number**:<br />-2147196416|NonMappableEntity Error Occurred|
> |**Name**:<br />NonPrimaryEntityDataDescriptionFound<br />**Hex**:<br />8004E001<br />**Number**:<br />-2147164159|The data description for the visualization is invalid .The data description for the visualization can only have attributes either from the primary entity of the view or the linked entities.|
> |**Name**:<br />NoOutputTransformationParameterMappingFound<br />**Hex**:<br />80040384<br />**Number**:<br />-2147220604|There is no output transformation parameter mapping defined. A transformation mapping must have atleast one output transformation parameter mapping.|
> |**Name**:<br />NoPreviewForCustomWebResource<br />**Hex**:<br />8004E020<br />**Number**:<br />-2147164128|This chart uses a custom Web resource. You cannot preview this chart.|
> |**Name**:<br />NoPrivilegeToApplyManualSLA<br />**Hex**:<br />80055002<br />**Number**:<br />-2147135486|You don't have appropriate permissions to apply Servie Level Agreement (SLA) to this case record.|
> |**Name**:<br />NoPrivilegeToPublishWorkflow<br />**Hex**:<br />80045016<br />**Number**:<br />-2147201002|User does not have sufficient privileges to publish workflows.|
> |**Name**:<br />NoPrivilegeToWorker<br />**Hex**:<br />80040521<br />**Number**:<br />-2147220191|You cannot add items to an inactive queue. Select another queue and try again.|
> |**Name**:<br />NoPublishedDuplicateDetectionRules<br />**Hex**:<br />80048436<br />**Number**:<br />-2147187658|There are no published duplicate detection rules in the system. To run duplicate detection, you must create and publish one or more rules.|
> |**Name**:<br />NoQuickFindFound<br />**Hex**:<br />80060203<br />**Number**:<br />-2147089917|Entity - {0} did not have a valid Quickfind query.|
> |**Name**:<br />NoRollupAttributesDefined<br />**Hex**:<br />8004F681<br />**Number**:<br />-2147158399|For rollup to succeed atleast one rollup attribute needs to be associated with the goal metric|
> |**Name**:<br />NoSettingError<br />**Hex**:<br />8004Ed46<br />**Number**:<br />-2147160762|No configdb configuration setting [{0}] was found.|
> |**Name**:<br />NoSiteMapReferenceInAppModule<br />**Hex**:<br />8005011C<br />**Number**:<br />-2147155684|App Module does not contain Site Map|
> |**Name**:<br />NotAWellFormedXml<br />**Hex**:<br />80048426<br />**Number**:<br />-2147187674|The input XML is not well-formed XML.|
> |**Name**:<br />NotEnoughPrivilegesForXamlWorkflows<br />**Hex**:<br />80045041<br />**Number**:<br />-2147200959|Not enough privileges to complete the operation. Only the deployment administrator can create or update workflows that are created outside the Microsoft Dynamics 365 Web application.|
> |**Name**:<br />NoTestEmailAccessPrivilege<br />**Hex**:<br />8005E232<br />**Number**:<br />-2147098062|There is not sufficient privilege to perform the test access.|
> |**Name**:<br />NotExistArgumentInAction<br />**Hex**:<br />80060393<br />**Number**:<br />-2147089517|Argument {0} does not exist in Action.|
> |**Name**:<br />NotExistBusinessProcess<br />**Hex**:<br />80060391<br />**Number**:<br />-2147089519|Business Process does not exist.|
> |**Name**:<br />NoTimeZoneCodeForConversionRule<br />**Hex**:<br />800608F9<br />**Number**:<br />-2147088135|The TimeZoneCode property is required when the value of the ConversionRule property is SpecificTimeZone.|
> |**Name**:<br />NotImplemented<br />**Hex**:<br />80040219<br />**Number**:<br />-2147220967|The requested functionality is not yet implemented.|
> |**Name**:<br />NotMobileEnabled<br />**Hex**:<br />8005F215<br />**Number**:<br />-2147093995|You can't view this type of record on your tablet. Contact your system administrator.|
> |**Name**:<br />NotMobileWriteEnabled<br />**Hex**:<br />8005F21c<br />**Number**:<br />-2147093988|You can't create this type of record on your device. Contact your system administrator.|
> |**Name**:<br />NotSupported<br />**Hex**:<br />80040315<br />**Number**:<br />-2147220715|This action is not supported.|
> |**Name**:<br />NotVerifiedAdmin<br />**Hex**:<br />8005F106<br />**Number**:<br />-2147094266|You need an enterprise account with Yammer in order to complete this setup. Please sign in with a Yammer administrator account or contact a Yammer administrator for help.|
> |**Name**:<br />NoUserPrivilege<br />**Hex**:<br />80154B50<br />**Number**:<br />-2146088112|You do not have sufficient permissions.|
> |**Name**:<br />NoWritePermission<br />**Hex**:<br />80071023<br />**Number**:<br />-2147020765|You do not have Write permissions to copy the documents.|
> |**Name**:<br />NoYammerNetworksFound<br />**Hex**:<br />8005F108<br />**Number**:<br />-2147094264|You are not authorized for any Yammer network. Please reauthorize the Yammer setup with a Yammer administrator account or contact a Yammer administrator for help.|
> |**Name**:<br />NullArticleTemplateFormatXml<br />**Hex**:<br />800404f8<br />**Number**:<br />-2147220232|The article template formatxml cannot be NULL|
> |**Name**:<br />NullArticleTemplateStructureXml<br />**Hex**:<br />800404f9<br />**Number**:<br />-2147220231|The article template structurexml cannot be NULL|
> |**Name**:<br />NullArticleXml<br />**Hex**:<br />800404f7<br />**Number**:<br />-2147220233|The article xml cannot be NULL|
> |**Name**:<br />NullDashboardName<br />**Hex**:<br />8004E305<br />**Number**:<br />-2147163387|The name of a dashboard cannot be null.|
> |**Name**:<br />NullKBArticleTemplateId<br />**Hex**:<br />800404fa<br />**Number**:<br />-2147220230|The kbarticletemplateid cannot be NULL|
> |**Name**:<br />NullOrEmptyAttributeInXaml<br />**Hex**:<br />80060406<br />**Number**:<br />-2147089402|Attribute - {0} of {1} cannot be null or empty|
> |**Name**:<br />NumberFormatFailed<br />**Hex**:<br />80040259<br />**Number**:<br />-2147220903|Failed to produce a formatted numeric value.|
> |**Name**:<br />OAuthTokenNotFound<br />**Hex**:<br />8005F109<br />**Number**:<br />-2147094263|Yammer OAuth token is not found. You should configure Yammer before accessing any related feature.|
> |**Name**:<br />ObjectAlreadyExists<br />**Hex**:<br />8004E30A<br />**Number**:<br />-2147163382|An object with id {0} already exists. Please change the id and try again.|
> |**Name**:<br />ObjectDoesNotExist<br />**Hex**:<br />80040217<br />**Number**:<br />-2147220969|The specified object was not found.|
> |**Name**:<br />ObjectNotFoundInAD<br />**Hex**:<br />80041d2a<br />**Number**:<br />-2147214038|The object does not exist in active directory.|
> |**Name**:<br />ObjectNotRelatedToCampaign<br />**Hex**:<br />8004030e<br />**Number**:<br />-2147220722|Specified Object not related to the parent Campaign|
> |**Name**:<br />OccurrenceCrossingBoundary<br />**Hex**:<br />8004E120<br />**Number**:<br />-2147163872|Two occurrences cannot overlap.|
> |**Name**:<br />OccurrenceSkipsOverBackward<br />**Hex**:<br />8004E123<br />**Number**:<br />-2147163869|Cannot reschedule an occurrence of the recurring appointment if it skips over an earlier occurrence of the same appointment.|
> |**Name**:<br />OccurrenceSkipsOverForward<br />**Hex**:<br />8004E122<br />**Number**:<br />-2147163870|Cannot reschedule an occurrence of the recurring appointment if it skips over a later occurrence of the same appointment.|
> |**Name**:<br />OccurrenceTimeSpanTooBig<br />**Hex**:<br />8004E121<br />**Number**:<br />-2147163871|Cannot perform the operation. An instance is outside of series effective expansion range.|
> |**Name**:<br />OfferingCategoryAndTokenNull<br />**Hex**:<br />8004B00C<br />**Number**:<br />-2147176436|Offer category and Billing Token are both missing, but at least one is required.|
> |**Name**:<br />OfferingIdNotSupported<br />**Hex**:<br />8004B00D<br />**Number**:<br />-2147176435|This version does not support search for offering id.|
> |**Name**:<br />OfficeGraphDisabledError<br />**Hex**:<br />80044239<br />**Number**:<br />-2147204551|Document Recommendations has been disabled for this organization.|
> |**Name**:<br />OfficeGraphSiteNotConfigured<br />**Hex**:<br />80044257<br />**Number**:<br />-2147204521|No default SharePoint site has been configured.|
> |**Name**:<br />OfficeGroupsExceptionRetrieveSetting<br />**Hex**:<br />800610EB<br />**Number**:<br />-2147086101|Office Groups Exception occured in RetrieveOfficeGroupsSetting: {0}.|
> |**Name**:<br />OfficeGroupsFeatureNotEnabled<br />**Hex**:<br />800610EA<br />**Number**:<br />-2147086102|Office Groups feature is not enabled.|
> |**Name**:<br />OfficeGroupsInvalidSettingType<br />**Hex**:<br />800610EC<br />**Number**:<br />-2147086100|Invalid setting type for Office Groups feature: {0}.|
> |**Name**:<br />OfficeGroupsNoAuthServersFound<br />**Hex**:<br />800610EE<br />**Number**:<br />-2147086098|Office Groups feature could not find any authorization servers.|
> |**Name**:<br />OfficeGroupsNotSupportedCall<br />**Hex**:<br />800610ED<br />**Number**:<br />-2147086099|Office Groups feature attempted an unsupported call.|
> |**Name**:<br />OfflineFilterNestedDateTimeOR<br />**Hex**:<br />80048450<br />**Number**:<br />-2147187632|You cannot use nested date time conditions within an OR clause in a local data group.|
> |**Name**:<br />OfflineFilterParentDownloaded<br />**Hex**:<br />80048451<br />**Number**:<br />-2147187631|You cannot use the Parent Downloaded condition in a local data group.|
> |**Name**:<br />OneDriveForBusinessDisabled<br />**Hex**:<br />80050004<br />**Number**:<br />-2147155964|Following attachments requires OneDrive for Business. Please contact your administrator to enable OneDrive for Business in the organization.|
> |**Name**:<br />OneDriveForBusinessLocationNotFound<br />**Hex**:<br />80050009<br />**Number**:<br />-2147155959|No One Drive for Business active location found.|
> |**Name**:<br />OneNoteCreationFailed<br />**Hex**:<br />80060902<br />**Number**:<br />-2147088126|OneNote creation failed.|
> |**Name**:<br />OneNoteLocationDeactivated<br />**Hex**:<br />80060907<br />**Number**:<br />-2147088121|The location mapping for OneNote is inactive. Contact your administrator to activate the OneNote location record for this Dynamics 365 record.|
> |**Name**:<br />OneNoteLocationNotCreated<br />**Hex**:<br />80060906<br />**Number**:<br />-2147088122|OneNote location not created.|
> |**Name**:<br />OneNoteRenderFailed<br />**Hex**:<br />80060903<br />**Number**:<br />-2147088125|OneNote render failed.|
> |**Name**:<br />OnlyDisabledOrganizationCanBeDeleted<br />**Hex**:<br />8004B02F<br />**Number**:<br />-2147176401|Can not delete enabled organization. Organization must be disabled before it can be deleted.|
> |**Name**:<br />OnlyOneSearchParameterMustBeProvided<br />**Hex**:<br />80060206<br />**Number**:<br />-2147089914|Extra parameter. You only need to provide EntityGroupName or EntityNames, not both.|
> |**Name**:<br />OnlyOwnerCanRevoke<br />**Hex**:<br />80040223<br />**Number**:<br />-2147220957|Only the owner of an object can revoke the owner's access to that object.|
> |**Name**:<br />OnlyOwnerCanSetManagedProperties<br />**Hex**:<br />8004F031<br />**Number**:<br />-2147160015|Cannot import component {0}: {1} because managed property {2} with value {3} is different than the current value {4} and the publisher of the solution that is being imported does not match the publisher of the solution that installed this component.|
> |**Name**:<br />OnlyProductCanBeConvertedToKit<br />**Hex**:<br />80061017<br />**Number**:<br />-2147086313|Only products can be converted to kits.|
> |**Name**:<br />OnlyStepInPredefinedStagesCanBeModified<br />**Hex**:<br />80044184<br />**Number**:<br />-2147204732|Invalid plug-in registration stage. Steps can only be modified in stages BeforeMainOperationOutsideTransaction, BeforeMainOperationInsideTransaction, AfterMainOperationInsideTransaction and AfterMainOperationOutsideTransaction.|
> |**Name**:<br />OnlyStepInServerOnlyCanHaveSecureConfiguration<br />**Hex**:<br />80044185<br />**Number**:<br />-2147204731|Only SdkMessageProcessingStep with ServerOnly supported deployment can have secure configuration.|
> |**Name**:<br />OnlyStepOutsideTransactionCanCreateCrmService<br />**Hex**:<br />80044186<br />**Number**:<br />-2147204730|Only SdkMessageProcessingStep in parent pipeline and in stages outside transaction can create CrmService to prevent deadlock.|
> |**Name**:<br />OnlyWorkflowDefinitionOrTemplateCanBePublished<br />**Hex**:<br />8004500D<br />**Number**:<br />-2147201011|Only workflow definition or draft workflow template can be published.|
> |**Name**:<br />OnlyWorkflowDefinitionOrTemplateCanBeUnpublished<br />**Hex**:<br />8004500E<br />**Number**:<br />-2147201010|Only workflow definition or workflow template can be unpublished.|
> |**Name**:<br />OnPremiseRestoreOrganizationManifestFailed<br />**Hex**:<br />80048532<br />**Number**:<br />-2147187406|Failed to restore Organization's configdb state from manifest|
> |**Name**:<br />OpenCrmDBConnection<br />**Hex**:<br />8004023e<br />**Number**:<br />-2147220930|Db Connection is Open, when it should be Closed.|
> |**Name**:<br />OpenDocumentErrorCodeGeneric<br />**Hex**:<br />8005F20C<br />**Number**:<br />-2147094004|Try this action again. If the problem continues, check the {0} for solutions or contact your organization's {#Brand_CRM} Administrator. Finally, you can contact {1}.|
> |**Name**:<br />OpenDocumentErrorCodeUnableToFindAnActivity<br />**Hex**:<br />8005F20A<br />**Number**:<br />-2147094006|Try this action again. If the problem continues, check the {0} for solutions or contact your organization's {#Brand_CRM} Administrator. Finally, you can contact {1}.|
> |**Name**:<br />OpenDocumentErrorCodeUnableToFindTheDataId<br />**Hex**:<br />8005F20B<br />**Number**:<br />-2147094005|Try this action again. If the problem continues, check the {0} for solutions or contact your organization's {#Brand_CRM} Administrator. Finally, you can contact {1}.|
> |**Name**:<br />OpenMailboxException<br />**Hex**:<br />8005E216<br />**Number**:<br />-2147098090|Exception occurs while opening mailbox for Exchaange mail server.|
> |**Name**:<br />OperationCanBeCalledOnlyOnce<br />**Hex**:<br />80040334<br />**Number**:<br />-2147220684|The specified action can be done only one time.|
> |**Name**:<br />OperationCanceled<br />**Hex**:<br />80060912<br />**Number**:<br />-2147088110|Refresh was canceled by user.|
> |**Name**:<br />OperationFailedTryAgain<br />**Hex**:<br />80154B53<br />**Number**:<br />-2146088109|Operation could not be performed at the moment. Please try again.|
> |**Name**:<br />OperationOrganizationNotFullyDisabled<br />**Hex**:<br />8004D23a<br />**Number**:<br />-2147167686|The {1} operation failed because organization {0} is not fully disabled yet.  Use FORCE to override|
> |**Name**:<br />OperatorCodeNotPresentError<br />**Hex**:<br />80044241<br />**Number**:<br />-2147204543|OperatorCode should be present in condition xml.|
> |**Name**:<br />OperatorsInViewNotSupportedOffline<br />**Hex**:<br />80071127<br />**Number**:<br />-2147020505|One or more operators in this view are not supported offline.|
> |**Name**:<br />OpportunityAlreadyInOpenState<br />**Hex**:<br />8004051a<br />**Number**:<br />-2147220198|The opportunity is already in the open state.|
> |**Name**:<br />OpportunityCannotBeClosed<br />**Hex**:<br />80040516<br />**Number**:<br />-2147220202|The opportunity cannot be closed.|
> |**Name**:<br />OpportunityCurrencyComparisonNotPossible<br />**Hex**:<br />80100004<br />**Number**:<br />-2146435068|Unable to update the opportunity, currency comparison could not be made.|
> |**Name**:<br />OpportunityIsAlreadyClosed<br />**Hex**:<br />80040515<br />**Number**:<br />-2147220203|The opportunity is already closed.|
> |**Name**:<br />OpportunityNotFound<br />**Hex**:<br />80100006<br />**Number**:<br />-2146435066|Unable to get opportunity entity for update.|
> |**Name**:<br />OpportunityPreImageNotFound<br />**Hex**:<br />80100007<br />**Number**:<br />-2146435065|Unable to find pre-image of the opportunity before the update.|
> |**Name**:<br />OptimisticConcurrencyNotEnabled<br />**Hex**:<br />8006088D<br />**Number**:<br />-2147088243|Optimistic concurrency isn't enabled for entity type {0}. The IfVersionMatches value of ConcurrencyBehavior can only be used if optimistic concurrency is enabled.|
> |**Name**:<br />OptionReorderArrayIncorrectLength<br />**Hex**:<br />80044324<br />**Number**:<br />-2147204316|The array of option values that were provided for reordering does not match the number of options for the attribute.|
> |**Name**:<br />OptionSetValidationFailed<br />**Hex**:<br />80061005<br />**Number**:<br />-2147086331|The value is out of range.|
> |**Name**:<br />OptionValuePrefixOutOfRange<br />**Hex**:<br />80048402<br />**Number**:<br />-2147187710|CustomizationOptionValuePrefix must be a number between {0} and {1}|
> |**Name**:<br />OrganizationDisabled<br />**Hex**:<br />8004A104<br />**Number**:<br />-2147180284|The Dynamics 365 organization you are attempting to access is currently disabled.  Please contact your system administrator|
> |**Name**:<br />OrganizationMigrationUnderway<br />**Hex**:<br />8004B044<br />**Number**:<br />-2147176380|Organization migration is already underway.|
> |**Name**:<br />OrganizationNotConfigured<br />**Hex**:<br />8004D253<br />**Number**:<br />-2147167661|Organization is not configured yet|
> |**Name**:<br />OrganizationTakenBySomeoneElse<br />**Hex**:<br />8004B00F<br />**Number**:<br />-2147176433|The organization {0} is already purchased by another customer.|
> |**Name**:<br />OrganizationTakenByYou<br />**Hex**:<br />8004B00E<br />**Number**:<br />-2147176434|The organization {0} is already purchased by you.|
> |**Name**:<br />OrganizationUIDeprecated<br />**Hex**:<br />80044159<br />**Number**:<br />-2147204775|The OrganizationUI entity is deprecated. It has been replaced by the SystemForm entity.|
> |**Name**:<br />OrgDoesNotExistInDiscoveryService<br />**Hex**:<br />8004B067<br />**Number**:<br />-2147176345|Organization not found in customer's discovery service|
> |**Name**:<br />OrgIdNotDetermined<br />**Hex**:<br />80044353<br />**Number**:<br />-2147204269|Error. The current organization ID couldn’t be determined|
> |**Name**:<br />OrgsInaccessible<br />**Hex**:<br />8004D24A<br />**Number**:<br />-2147167670|The client access license (CAL) results were not returned because one or more organizations in the deployment cannot be accessed.|
> |**Name**:<br />OutgoingNotAllowedForForwardMailbox<br />**Hex**:<br />8005E225<br />**Number**:<br />-2147098075|Mailbox is a forward mailbox. A forward mailbox cannot send the mails.|
> |**Name**:<br />OutgoingServerLocationAndSslSetToNo<br />**Hex**:<br />8005E23F<br />**Number**:<br />-2147098049|The URL specified for Outgoing Server Location uses HTTPS but the Use SSL for Outgoing Connection option is set to No. Set this option to Yes, and then try again.|
> |**Name**:<br />OutgoingServerLocationAndSslSetToYes<br />**Hex**:<br />8005E241<br />**Number**:<br />-2147098047|The URL specified for Outgoing Server Location uses HTTP but the Use SSL for Outgoing Connection option is set to Yes. Specify a server location that uses HTTPS, and then try again.|
> |**Name**:<br />OutgoingSettingsUpdateNotAllowed<br />**Hex**:<br />8005E238<br />**Number**:<br />-2147098056|Different outgoing connection settings cannot be specified because the "Use Same Settings for Outgoing Connections" flag is set to True.|
> |**Name**:<br />OutlookClientConfigActionFailed<br />**Hex**:<br />80044509<br />**Number**:<br />-2147203831|Dynamics 365 Outlook client configuration action failed.|
> |**Name**:<br />OutOfScopeSlug<br />**Hex**:<br />80045050<br />**Number**:<br />-2147200944|The data required to display the next dialog page cannot be found. To resolve this issue, contact the dialog owner or the system administrator.|
> |**Name**:<br />OverlappingInstances<br />**Hex**:<br />8004E108<br />**Number**:<br />-2147163896|Two instances of the series cannot overlap.|
> |**Name**:<br />OverRetrievalUpperLimitWithoutPagingCookie<br />**Hex**:<br />8004430A<br />**Number**:<br />-2147204342|Over upper limit of records that can be requested without a paging cookie. A paging cookie is required when retrieving a high page number.|
> |**Name**:<br />OwnerAttributeMissing<br />**Hex**:<br />8006110C<br />**Number**:<br />-2147086068|Owner Attribute is not present in the request.|
> |**Name**:<br />OwnerMappingExistsWithSourceSystemUserName<br />**Hex**:<br />80040343<br />**Number**:<br />-2147220669|The data map already contains this owner mapping.|
> |**Name**:<br />OwnerValueNotMapped<br />**Hex**:<br />80040361<br />**Number**:<br />-2147220639|The owner value is not mapped|
> |**Name**:<br />PageNotFound<br />**Hex**:<br />8005F21A<br />**Number**:<br />-2147093990|Page not found. The record might not exist, or the link might be incorrect.|
> |**Name**:<br />ParentBusinessDoesNotExist<br />**Hex**:<br />80041d23<br />**Number**:<br />-2147214045|The parent business Id is invalid.|
> |**Name**:<br />ParentCaseNotAllowedAsAChildCase<br />**Hex**:<br />8003F455<br />**Number**:<br />-2147224491|You can't add a parent case as a child case|
> |**Name**:<br />ParentChildMetricIdDiffers<br />**Hex**:<br />80044905<br />**Number**:<br />-2147202811|The metricid of child goal should be same as the parent goal.|
> |**Name**:<br />ParentChildPeriodAttributesDiffer<br />**Hex**:<br />80044906<br />**Number**:<br />-2147202810|The period settings of child goal should be same as the parent goal.|
> |**Name**:<br />ParentHierarchyExistProperty<br />**Hex**:<br />8004F888<br />**Number**:<br />-2147157880|A parent should exist for each node in hierarchy except the root node.|
> |**Name**:<br />ParentReadOnly<br />**Hex**:<br />80043b09<br />**Number**:<br />-2147206391|The parent is read only and cannot be edited.|
> |**Name**:<br />ParentRecordAlreadyExists<br />**Hex**:<br />80048478<br />**Number**:<br />-2147187592|This record cannot be added because it already has a parent record.|
> |**Name**:<br />ParentReportDoesNotReferenceChild<br />**Hex**:<br />80040486<br />**Number**:<br />-2147220346|Specified parent report does not reference the current one. Only SQL Reporting Services reports can have parent reports.|
> |**Name**:<br />ParentReportLinksToSameNameChild<br />**Hex**:<br />80040496<br />**Number**:<br />-2147220330|Parent report already links to another report with the same name.|
> |**Name**:<br />ParentReportNotSupported<br />**Hex**:<br />80040487<br />**Number**:<br />-2147220345|Parent report is not supported for the type of report specified. Only SQL Reporting Services reports can have parent reports.|
> |**Name**:<br />ParentUserDoesNotExist<br />**Hex**:<br />80041d27<br />**Number**:<br />-2147214041|The parent user Id is invalid.|
> |**Name**:<br />ParseMustBeCalledBeforeTransform<br />**Hex**:<br />80040371<br />**Number**:<br />-2147220623|Cannot call transform before parse.|
> |**Name**:<br />ParsingMetadataNotFound<br />**Hex**:<br />80040367<br />**Number**:<br />-2147220633|Data required to parse the file, such as the data delimiter, field delimiter, or column headings, was not found.|
> |**Name**:<br />PartialExpansionSettingLoadError<br />**Hex**:<br />8004E102<br />**Number**:<br />-2147163902|Failed to retrieve partial expansion settings from the configuration database.|
> |**Name**:<br />PartialHolidayScheduleCreation<br />**Hex**:<br />8004F873<br />**Number**:<br />-2147157901|Partial holiday schedule can not be created.|
> |**Name**:<br />ParticipatingEntityDoesNotAppearInTraversedPath<br />**Hex**:<br />80060441<br />**Number**:<br />-2147089343|Error displaying Business Process control. Participating entity must be part of traversed path, but entity '{0}' does not appear in path '{1}'. Please contact your system administrator.|
> |**Name**:<br />ParticipatingQueryEntityMismatch<br />**Hex**:<br />80044909<br />**Number**:<br />-2147202807|The entitytype of participating query should be the same as the entity specified in fetchxml.|
> |**Name**:<br />PasswordRequiredForImpersonation<br />**Hex**:<br />8005E24E<br />**Number**:<br />-2147098034|Type in a password and save again|
> |**Name**:<br />PatchMissingBase<br />**Hex**:<br />80048540<br />**Number**:<br />-2147187392|You can't import the patch ({0}) for the solution ({1}) because the solution isn't present. The operation has been canceled.|
> |**Name**:<br />PercentageDiscountCannotHaveCurrency<br />**Hex**:<br />80048cf1<br />**Number**:<br />-2147185423|Currency cannot be set when discount type is percentage.|
> |**Name**:<br />PersonalReportFound<br />**Hex**:<br />8004E309<br />**Number**:<br />-2147163383|A system dashboard cannot contain personal reports.|
> |**Name**:<br />PickListMappingExistsForTargetValue<br />**Hex**:<br />8004033f<br />**Number**:<br />-2147220673|This list value is mapped more than once. Remove any duplicate mappings, and then import this data map again.|
> |**Name**:<br />PickListMappingExistsWithSourceValue<br />**Hex**:<br />80040342<br />**Number**:<br />-2147220670|The data map already contains this list value mapping.|
> |**Name**:<br />PicklistValueNotFound<br />**Hex**:<br />80040393<br />**Number**:<br />-2147220589|The file specifies a list value that does not exist in Microsoft Dynamics 365.|
> |**Name**:<br />PicklistValueNotMapped<br />**Hex**:<br />80040360<br />**Number**:<br />-2147220640|The record could not be processed as the Option set value could not be mapped.|
> |**Name**:<br />PicklistValueNotUnique<br />**Hex**:<br />80044310<br />**Number**:<br />-2147204336|The picklist value already exists.  Picklist values must be unique.|
> |**Name**:<br />PicklistValueOutOfRange<br />**Hex**:<br />8004431A<br />**Number**:<br />-2147204326|The picklist value is out of the range.|
> |**Name**:<br />PingFailureErrorCode<br />**Hex**:<br />8005F212<br />**Number**:<br />-2147093998|The system couldn't reconnect with your {#Brand_CRM} server.|
> |**Name**:<br />PluginAssemblyContentSizeExceeded<br />**Hex**:<br />8004418f<br />**Number**:<br />-2147204721|"The assembly content size '{0} bytes' has exceeded the maximum value allowed for isolated plug-ins '{1} bytes'."|
> |**Name**:<br />PluginAssemblyMustHavePublicKeyToken<br />**Hex**:<br />8004416c<br />**Number**:<br />-2147204756|Public assembly must have public key token.|
> |**Name**:<br />PluginDoesNotImplementCorrectInterface<br />**Hex**:<br />8004A200<br />**Number**:<br />-2147180032|The plug-in specified does not implement the required interface Microsoft.Xrm.Sdk.IPlugin or Microsoft.Crm.Sdk.IPlugin.|
> |**Name**:<br />PluginSecureStoreAdalAcquireToken<br />**Hex**:<br />80091005<br />**Number**:<br />-2146889723|Unable to AcquireToken for resource|
> |**Name**:<br />PluginSecureStoreKeyVaultClient<br />**Hex**:<br />80091000<br />**Number**:<br />-2146889728|Unable to initialize KeyVaultClientProvider under Sandbox WorkerProcess|
> |**Name**:<br />PluginSecureStoreKeyVaultClientDecrypt<br />**Hex**:<br />80091003<br />**Number**:<br />-2146889725|Unable to Decrypt using KeyVault|
> |**Name**:<br />PluginSecureStoreKeyVaultClientEncrypt<br />**Hex**:<br />80091004<br />**Number**:<br />-2146889724|Unable to Encrypt using KeyVault|
> |**Name**:<br />PluginSecureStoreKeyVaultClientGetSecret<br />**Hex**:<br />80091001<br />**Number**:<br />-2146889727|Unable to GetSecret from KeyVault|
> |**Name**:<br />PluginSecureStoreKeyVaultClientSetSecret<br />**Hex**:<br />80091002<br />**Number**:<br />-2146889726|Unable to SetSecret to KeyVault|
> |**Name**:<br />PluginSecureStoreKeyVaultServiceCertFormat<br />**Hex**:<br />8009100D<br />**Number**:<br />-2146889715|Certificate not stored as a Base64String in KeyVault|
> |**Name**:<br />PluginSecureStoreKeyVaultServiceProviderGetData<br />**Hex**:<br />8009100C<br />**Number**:<br />-2146889716|Missing AppId / Secrets in KeyVault|
> |**Name**:<br />PluginSecureStoreLocalConfigStoreGetData<br />**Hex**:<br />8009100A<br />**Number**:<br />-2146889718|Unable to get data from LocalConfigStore|
> |**Name**:<br />PluginSecureStoreLocalConfigStoreSetData<br />**Hex**:<br />8009100B<br />**Number**:<br />-2146889717|Unable to set data to LocalConfigStore|
> |**Name**:<br />PluginSecureStoreNoFullySigned<br />**Hex**:<br />8009100F<br />**Number**:<br />-2146889713|Assembly not fully signed|
> |**Name**:<br />PluginSecureStoreS2SMissing<br />**Hex**:<br />80091008<br />**Number**:<br />-2146889720|S2S Credentials missing|
> |**Name**:<br />PluginSecureStoreTPSAssemblyNotRegistered<br />**Hex**:<br />80091007<br />**Number**:<br />-2146889721|Assembly is not registered in TPS|
> |**Name**:<br />PluginSecureStoreTPSClient<br />**Hex**:<br />80091009<br />**Number**:<br />-2146889719|Unable to create TPS Client|
> |**Name**:<br />PluginSecureStoreTPSKeyVaultUnconfigured<br />**Hex**:<br />80091006<br />**Number**:<br />-2146889722|KeyVaultURI was not configured for an Assembly in TPS|
> |**Name**:<br />PluginTypeMustBeUnique<br />**Hex**:<br />8004417C<br />**Number**:<br />-2147204740|Multiple plug-in types from the same assembly and with the same typename are not allowed.|
> |**Name**:<br />Pop3UnexpectedException<br />**Hex**:<br />8005E215<br />**Number**:<br />-2147098091|Exception occur while polling mails using Pop3 protocol.|
> |**Name**:<br />PowerBICannotBeSystemDashboard<br />**Hex**:<br />800608FC<br />**Number**:<br />-2147088132|A Power BI Dashboard cannot be a System Dashboard.|
> |**Name**:<br />PowerBIDashboardControlLimitation<br />**Hex**:<br />800608FD<br />**Number**:<br />-2147088131|A Power BI Dashboard can only contain one control and that control must be a Power BI control.|
> |**Name**:<br />PresentParentAccountAndParentContact<br />**Hex**:<br />80040508<br />**Number**:<br />-2147220216|You can either specify a contacts parent contact or its account, but not both.|
> |**Name**:<br />PreviousOperationNotComplete<br />**Hex**:<br />80048464<br />**Number**:<br />-2147187612|An operation on which this operation depends did not complete successfully.|
> |**Name**:<br />PriceLevelNameExists<br />**Hex**:<br />80043b0f<br />**Number**:<br />-2147206385|The name already exists.|
> |**Name**:<br />PriceLevelNoName<br />**Hex**:<br />80043b0e<br />**Number**:<br />-2147206386|The name can not be null.|
> |**Name**:<br />PrimaryEntityInvalid<br />**Hex**:<br />8004501E<br />**Number**:<br />-2147200994|Invalid primary entity.|
> |**Name**:<br />PrimaryEntityIsNull<br />**Hex**:<br />80060401<br />**Number**:<br />-2147089407|Primary Entity cannot be NULL while creating business process flow category|
> |**Name**:<br />PrimaryNameAttributeNotFound<br />**Hex**:<br />80044355<br />**Number**:<br />-2147204267|PrimaryName attribute not found for Entity: {0}|
> |**Name**:<br />PrimaryParticipatingEntityIsNotPresent<br />**Hex**:<br />80060453<br />**Number**:<br />-2147089325|Validation error: primary participating entity is not present and is required for every Business Process entity record.|
> |**Name**:<br />PrincipalPrivilegeDenied<br />**Hex**:<br />80040231<br />**Number**:<br />-2147220943|Target user or team does not hold required privileges.|
> |**Name**:<br />PrivilegeCreateIsDisabledForOrganization<br />**Hex**:<br />80040276<br />**Number**:<br />-2147220874|Privilege Create is disabled for organization.|
> |**Name**:<br />PrivilegeDenied<br />**Hex**:<br />80040220<br />**Number**:<br />-2147220960|The user does not hold the necessary privileges.|
> |**Name**:<br />ProcessActionDoesNotExist<br />**Hex**:<br />80045054<br />**Number**:<br />-2147200940|Process Action does not exist.|
> |**Name**:<br />ProcessActionIsNotActive<br />**Hex**:<br />80045053<br />**Number**:<br />-2147200941|Process Action should be active to be used on Action Step.|
> |**Name**:<br />ProcessActionNameIncorrect<br />**Hex**:<br />80060379<br />**Number**:<br />-2147089543|Process Action “{0}” does not match the name configured: “{1}”. Contact your system administrator to check the configuration metadata if the error persists.|
> |**Name**:<br />ProcessActionWithInvalidInputOutputParam<br />**Hex**:<br />80045058<br />**Number**:<br />-2147200936|Process Action contains a parameter that is not supported. Name: {0}, type: {1}, direction: {2}.|
> |**Name**:<br />ProcessActionWithInvalidInputParam<br />**Hex**:<br />80045057<br />**Number**:<br />-2147200937|Process Action contains a field in input parameter that is unsupported on Action Steps. Refer to {0} |
> |**Name**:<br />ProcessActionWithInvalidOutputParam<br />**Hex**:<br />80045056<br />**Number**:<br />-2147200938|Process Action contains a field in output parameter that is unsupported on Action Steps. Refer to {0}.|
> |**Name**:<br />ProcessActionWorkflowNotEnabledForOnDemand<br />**Hex**:<br />80060380<br />**Number**:<br />-2147089536|Process Action or Workflow must be enabled for on-demand execution to be available for action steps.|
> |**Name**:<br />ProcessEmptyBranches<br />**Hex**:<br />80060399<br />**Number**:<br />-2147089511|This process contains empty branches. Define or delete these branches and try again.|
> |**Name**:<br />ProcessIdDoesNotMatchBusinessProcessDefinition<br />**Hex**:<br />80060460<br />**Number**:<br />-2147089312|Validation error: Process ID does not match Business Process definition.|
> |**Name**:<br />ProcessIdIsEmpty<br />**Hex**:<br />80060459<br />**Number**:<br />-2147089319|Validation error: Process ID cannot be empty.|
> |**Name**:<br />ProcessImageFailure<br />**Hex**:<br />80072553<br />**Number**:<br />-2147015341|Error occured when processing image. Reason: {0}|
> |**Name**:<br />ProcessNameContainsInvalidCharacters<br />**Hex**:<br />80060398<br />**Number**:<br />-2147089512|The business process name contains invalid characters.|
> |**Name**:<br />ProcessNameIsNullOrEmpty<br />**Hex**:<br />80060418<br />**Number**:<br />-2147089384|The business process flow name is NULL or empty. |
> |**Name**:<br />ProcessStageIdIsEmpty<br />**Hex**:<br />80060461<br />**Number**:<br />-2147089311|Validation error: Primary Stage ID cannot be empty.|
> |**Name**:<br />ProductCanOnlyBeUpdatedInDraft<br />**Hex**:<br />8004F995<br />**Number**:<br />-2147157611|Product, product family and bundle can only be updated in draft state.|
> |**Name**:<br />ProductCloneFailed<br />**Hex**:<br />80061006<br />**Number**:<br />-2147086330|You can't clone a child record of a retired product family.|
> |**Name**:<br />ProductDoesNotExist<br />**Hex**:<br />80043b24<br />**Number**:<br />-2147206364|The product does not exist.|
> |**Name**:<br />ProductFamilyCanCreateDynamicProperty<br />**Hex**:<br />80081007<br />**Number**:<br />-2146955257|A property can only be created for a product family.|
> |**Name**:<br />ProductFamilyRootParentisLocked<br />**Hex**:<br />8008101F<br />**Number**:<br />-2146955233|The product family root parent record is locked by some other process.|
> |**Name**:<br />ProductFromActiveToActiveState<br />**Hex**:<br />8004F982<br />**Number**:<br />-2147157630|Product is already in Active State.|
> |**Name**:<br />ProductFromActiveToDraftState<br />**Hex**:<br />8004F912<br />**Number**:<br />-2147157742|You can't set a published product to the draft state.|
> |**Name**:<br />ProductFromDraftToDraftState<br />**Hex**:<br />8004F981<br />**Number**:<br />-2147157631|Product is already in Draft State.|
> |**Name**:<br />ProductFromDraftToRetiredState<br />**Hex**:<br />8004F978<br />**Number**:<br />-2147157640|You can't retire a product that's in the draft state.|
> |**Name**:<br />ProductFromDraftToRevisedState<br />**Hex**:<br />8004F913<br />**Number**:<br />-2147157741|You can't revise a draft or a retired product.|
> |**Name**:<br />ProductFromRetiredToActiveState<br />**Hex**:<br />8004F977<br />**Number**:<br />-2147157641|You can't set a retired property to an active state.|
> |**Name**:<br />ProductFromRetiredToDraftState<br />**Hex**:<br />8004F979<br />**Number**:<br />-2147157639|It is not possible to move product from Retired to Draft State.|
> |**Name**:<br />ProductFromRetiredToRetiredState<br />**Hex**:<br />8004F980<br />**Number**:<br />-2147157632|Product is already in Retired State.|
> |**Name**:<br />ProductHasUnretiredChild<br />**Hex**:<br />8004F910<br />**Number**:<br />-2147157744|You can't retire this product family because one or more of its child records aren't retired.|
> |**Name**:<br />ProductInvalidPriceLevelPercentage<br />**Hex**:<br />80043b0c<br />**Number**:<br />-2147206388|The pricing percentage must be greater than or equal to zero and less than 100000.|
> |**Name**:<br />ProductInvalidQuantityDecimal<br />**Hex**:<br />80043b07<br />**Number**:<br />-2147206393|The number of decimal places on the quantity is invalid.|
> |**Name**:<br />ProductInvalidUnit<br />**Hex**:<br />80043b14<br />**Number**:<br />-2147206380|The specified unit is not valid for this product.|
> |**Name**:<br />ProductKitLoopBeingCreated<br />**Hex**:<br />80043b23<br />**Number**:<br />-2147206365|You can’t add a kit to itself.|
> |**Name**:<br />ProductKitLoopExists<br />**Hex**:<br />80043b22<br />**Number**:<br />-2147206366|Loop exists in the kit hierarchy.|
> |**Name**:<br />ProductMaxPropertyLimitExceeded<br />**Hex**:<br />8008100D<br />**Number**:<br />-2146955251|This product can't be published because it has too many properties. A product in your organization can't have more than {0} properties.|
> |**Name**:<br />ProductMissingUomSheduleId<br />**Hex**:<br />80043b13<br />**Number**:<br />-2147206381|The unit schedule id of the product is missing.|
> |**Name**:<br />ProductNoProductNumber<br />**Hex**:<br />80043b05<br />**Number**:<br />-2147206395|The product number can not be null.|
> |**Name**:<br />ProductNoSubstitutedProductNumber<br />**Hex**:<br />8004F990<br />**Number**:<br />-2147157616|The substituted Product number cannot be a NULL.|
> |**Name**:<br />ProductOrBundleCannotBeAsParent<br />**Hex**:<br />8004F973<br />**Number**:<br />-2147157645|Only Product Families can be parents to products.|
> |**Name**:<br />ProductProductNumberExists<br />**Hex**:<br />80043b06<br />**Number**:<br />-2147206394|The specified product ID conflicts with the product ID of an existing record. Specify a different product ID and try again.|
> |**Name**:<br />ProductRecommendationsFeatureNotEnabled<br />**Hex**:<br />80061600<br />**Number**:<br />-2147084800|Product Recommendations feature is not enabled.|
> |**Name**:<br />ProfileContainsCircularReference<br />**Hex**:<br />80071141<br />**Number**:<br />-2147020479|The profile '{0}' has a circular reference which will prevent your data download. Please review the circular reference chain: {1} and remove the profile item association that causes the circular reference.|
> |**Name**:<br />ProfileContainsRelationshipWithoutEntity<br />**Hex**:<br />80071142<br />**Number**:<br />-2147020478|The profile '{0}' has a profile item {1} which contains a profile item association for {2}, however there does not exist a profile item for {2}. Please include the profile item and publish.|
> |**Name**:<br />ProfileCountUserLimitExceeded<br />**Hex**:<br />80071134<br />**Number**:<br />-2147020492|The total number of users ('{0}') in this profile exceeds the allowed limit ('{1}'). Please limit the total number of users to be within the supported limit.|
> |**Name**:<br />ProfileRuleActivateDeactivateByNonOwner<br />**Hex**:<br />80061102<br />**Number**:<br />-2147086078|This Profile Rule cannot be activated or deactivated by someone who is not its owner.|
> |**Name**:<br />ProfileRuleMissingRuleCriteria<br />**Hex**:<br />80061100<br />**Number**:<br />-2147086080|You can't activate this rule until you resolve any missing rule criteria information in the rule items.|
> |**Name**:<br />ProfileRulePublishedByOwner<br />**Hex**:<br />80061103<br />**Number**:<br />-2147086077|Your rule can't be activated until the current active rule is deactivated. The active rule can only be deactivated by the rule owner.|
> |**Name**:<br />ProfileRuleWorkflowAuthorGenericError<br />**Hex**:<br />80061101<br />**Number**:<br />-2147086079|An error occurred while authoring workflow. Please fix workflow definition and try again.|
> |**Name**:<br />ProvisioningNotCompleted<br />**Hex**:<br />80091044<br />**Number**:<br />-2146889660|To enable auto capture, you need to set up Cortana Intelligence Customer Insights in Relationship Insights settings.|
> |**Name**:<br />ProvisionRIAccessNotAllowed<br />**Hex**:<br />80044270<br />**Number**:<br />-2147204496|You need system administrator privileges to turn Relationship Insights on for your organization.|
> |**Name**:<br />PublishArticle_TranslationWithMoreThanOneApprovedVersion<br />**Hex**:<br />80061401<br />**Number**:<br />-2147085311|There is more than one approved version of the {0} language. You can only publish one version of each language.|
> |**Name**:<br />PublishedWorkflowLimitForSkuReached<br />**Hex**:<br />80045015<br />**Number**:<br />-2147201003|This workflow cannot be published because your organization has reached its limit for the number of workflows that can be published at the same time. (There is no limit on the number of draft workflows.) You can publish this workflow by unpublishing a different workflow, or by upgrading your license to a license that supports more workflows.|
> |**Name**:<br />PublishedWorkflowOwnershipChange<br />**Hex**:<br />8004500C<br />**Number**:<br />-2147201012|A published workflow can only be assigned to the caller.|
> |**Name**:<br />PublishWorkflowWhileActingOnBehalfOfAnotherUserError<br />**Hex**:<br />80045032<br />**Number**:<br />-2147200974|Publishing Workflows while acting on behalf of another user is not allowed.|
> |**Name**:<br />PublishWorkflowWhileImpersonatingError<br />**Hex**:<br />80045039<br />**Number**:<br />-2147200967|Publishing Workflows while impersonating another user is not allowed.|
> |**Name**:<br />QuantityReadonly<br />**Hex**:<br />80043b18<br />**Number**:<br />-2147206376|Do not modify the Quantity field when you update the primary unit.|
> |**Name**:<br />QueriesForDifferentEntities<br />**Hex**:<br />8004D2B0<br />**Number**:<br />-2147167568|The Inner and Outer Queries must be for the same entity.|
> |**Name**:<br />QueryBuilderAlias_Does_Not_Exist<br />**Hex**:<br />8004110a<br />**Number**:<br />-2147217142|The specified alias for the given entity in the condition does not exist.|
> |**Name**:<br />QueryBuilderAliasNotAllowedForNonAggregateOrderBy<br />**Hex**:<br />80041132<br />**Number**:<br />-2147217102|An alias cannot be specified for an order clause for a non-aggregate Query. Use an attribute.|
> |**Name**:<br />QueryBuilderAliasRequiredForAggregateOrderBy<br />**Hex**:<br />80041134<br />**Number**:<br />-2147217100|An alias is required for an order clause for an aggregate Query.|
> |**Name**:<br />QueryBuilderAttribute_With_Aggregate<br />**Hex**:<br />80041107<br />**Number**:<br />-2147217145|Attributes can not be returned when aggregate operation is specified.|
> |**Name**:<br />QueryBuilderAttributeCannotBeGroupByAndAggregate<br />**Hex**:<br />80041137<br />**Number**:<br />-2147217097|An attribute can either be an aggregate or a Group By but not both|
> |**Name**:<br />QueryBuilderAttributeNotAllowedForAggregateOrderBy<br />**Hex**:<br />80041131<br />**Number**:<br />-2147217103|An attribute cannot be specified for an order clause for an aggregate Query. Use an alias.|
> |**Name**:<br />QueryBuilderAttributeNotFound<br />**Hex**:<br />8004111e<br />**Number**:<br />-2147217122|A required attribute was not specified.|
> |**Name**:<br />QueryBuilderAttributePairMismatch<br />**Hex**:<br />80041111<br />**Number**:<br />-2147217135|AttributeFrom and AttributeTo must be either both specified or both omitted.|
> |**Name**:<br />QueryBuilderAttributeRequiredForNonAggregateOrderBy<br />**Hex**:<br />80041133<br />**Number**:<br />-2147217101|An attribute is required for an order clause for a non-aggregate Query.|
> |**Name**:<br />QueryBuilderBad_Condition<br />**Hex**:<br />80041106<br />**Number**:<br />-2147217146|Incorrect filter condition or conditions.|
> |**Name**:<br />QueryBuilderByAttributeMismatch<br />**Hex**:<br />8004110f<br />**Number**:<br />-2147217137|QueryByAttribute must specify a non-empty value array with the same number of elements as in the attributes array.|
> |**Name**:<br />QueryBuilderByAttributeNonEmpty<br />**Hex**:<br />80041110<br />**Number**:<br />-2147217136|QueryByAttribute must specify a non-empty attribute array.|
> |**Name**:<br />QueryBuilderColumnSetVersionMissing<br />**Hex**:<br />80041113<br />**Number**:<br />-2147217133|The specified columnset version is invalid.|
> |**Name**:<br />QueryBuilderDeserializeEmptyXml<br />**Hex**:<br />80041124<br />**Number**:<br />-2147217116|Xml String can't be null.|
> |**Name**:<br />QueryBuilderDeserializeInvalidAggregate<br />**Hex**:<br />8004111a<br />**Number**:<br />-2147217126|An error occurred while processing Aggregates in Query|
> |**Name**:<br />QueryBuilderDeserializeInvalidDescending<br />**Hex**:<br />80041119<br />**Number**:<br />-2147217127|The only valid values for descending attribute are 'true', 'false', '1', and '0'.|
> |**Name**:<br />QueryBuilderDeserializeInvalidDistinct<br />**Hex**:<br />80041115<br />**Number**:<br />-2147217131|The only valid values for distinct attribute are 'true', 'false', '1', and '0'.|
> |**Name**:<br />QueryBuilderDeserializeInvalidGetMinActiveRowVersion<br />**Hex**:<br />8004111b<br />**Number**:<br />-2147217125|The only valid values for GetMinActiveRowVersion attribute are 'true', 'false', '1', and '0'.|
> |**Name**:<br />QueryBuilderDeserializeInvalidGroupBy<br />**Hex**:<br />8004112E<br />**Number**:<br />-2147217106|The only valid values for groupby attribute are 'true', 'false', '1', and '0'.|
> |**Name**:<br />QueryBuilderDeserializeInvalidLinkType<br />**Hex**:<br />80041117<br />**Number**:<br />-2147217129|The only valid values for link-type attribute are 'natural', 'inner','in','exists','matchfirstrowusingcrossapply' and 'outer'.|
> |**Name**:<br />QueryBuilderDeserializeInvalidMapping<br />**Hex**:<br />80041116<br />**Number**:<br />-2147217130|The only valid values for mapping are 'logical' or 'internal' which is deprecated.|
> |**Name**:<br />QueryBuilderDeserializeInvalidNode<br />**Hex**:<br />8004111c<br />**Number**:<br />-2147217124|The element node encountered is invalid.|
> |**Name**:<br />QueryBuilderDeserializeInvalidNoLock<br />**Hex**:<br />80041118<br />**Number**:<br />-2147217128|The only valid values for no-lock attribute are 'true', 'false', '1', and '0'.|
> |**Name**:<br />QueryBuilderDeserializeInvalidUseRawOrderBy<br />**Hex**:<br />800410fd<br />**Number**:<br />-2147217155|The only valid values for useraworderby attribute are 'true', 'false', '1', and '0'.|
> |**Name**:<br />QueryBuilderDeserializeInvalidUtcOffset<br />**Hex**:<br />8004111d<br />**Number**:<br />-2147217123|The utc-offset attribute is not supported for deserialization.|
> |**Name**:<br />QueryBuilderDeserializeNoDocElemXml<br />**Hex**:<br />80041125<br />**Number**:<br />-2147217115|Document Element can't be null.|
> |**Name**:<br />QueryBuilderDuplicateAlias<br />**Hex**:<br />80041130<br />**Number**:<br />-2147217104|FetchXML should have unique aliases.|
> |**Name**:<br />QueryBuilderElementNotFound<br />**Hex**:<br />80041123<br />**Number**:<br />-2147217117|A required element was not specified.|
> |**Name**:<br />QueryBuilderEntitiesDontMatch<br />**Hex**:<br />80041128<br />**Number**:<br />-2147217112|The entity name specified in fetchxml does not match the entity name specified in the Entity or Query Expression.|
> |**Name**:<br />QueryBuilderInvalid_Alias<br />**Hex**:<br />80041109<br />**Number**:<br />-2147217143|Invalid alias for aggregate operation.|
> |**Name**:<br />QueryBuilderInvalid_Value<br />**Hex**:<br />80041108<br />**Number**:<br />-2147217144|Invalid value specified for type.|
> |**Name**:<br />QueryBuilderInvalidAggregateAttribute<br />**Hex**:<br />8004112F<br />**Number**:<br />-2147217105|Aggregate {0} is not supported for attribute of type {1}.|
> |**Name**:<br />QueryBuilderInvalidAttributeValue<br />**Hex**:<br />80041139<br />**Number**:<br />-2147217095|The attribute value provided is invalid.|
> |**Name**:<br />QueryBuilderInvalidColumnSetVersion<br />**Hex**:<br />80041112<br />**Number**:<br />-2147217134|The specified columnset version is invalid.|
> |**Name**:<br />QueryBuilderInvalidConditionOperator<br />**Hex**:<br />80041120<br />**Number**:<br />-2147217120|Unsupported condition operator.|
> |**Name**:<br />QueryBuilderInvalidDateGrouping<br />**Hex**:<br />80041135<br />**Number**:<br />-2147217099|An invalid value was specified for dategrouping.|
> |**Name**:<br />QueryBuilderInvalidFilterType<br />**Hex**:<br />80041122<br />**Number**:<br />-2147217118|Unsupported filter type. Valid values are 'and', or 'or'.|
> |**Name**:<br />QueryBuilderInvalidJoinOperator<br />**Hex**:<br />80041121<br />**Number**:<br />-2147217119|Unsupported join operator.|
> |**Name**:<br />QueryBuilderInvalidLogicalOperator<br />**Hex**:<br />800410fe<br />**Number**:<br />-2147217154|Unsupported logical operator: {0}.  Accepted values are ('and', 'or').|
> |**Name**:<br />QueryBuilderInvalidOrderType<br />**Hex**:<br />8004111f<br />**Number**:<br />-2147217121|A valid order type must be set in the order before calling this method.|
> |**Name**:<br />QueryBuilderInvalidPagingCookie<br />**Hex**:<br />8004112A<br />**Number**:<br />-2147217110|Invalid page number in paging cookie.|
> |**Name**:<br />QueryBuilderInvalidUpdate<br />**Hex**:<br />80041100<br />**Number**:<br />-2147217152|An attempt was made to update a non-updateable field.|
> |**Name**:<br />QueryBuilderLinkNodeForOrderNotFound<br />**Hex**:<br />80041126<br />**Number**:<br />-2147217114|Converting from Query to EntityExpression failed. Link Node for order was not found.|
> |**Name**:<br />QueryBuilderMultipleIntersectEntities<br />**Hex**:<br />8004110e<br />**Number**:<br />-2147217138|More than one intersect entity exists between the two entities specified.|
> |**Name**:<br />QueryBuilderNoAlias<br />**Hex**:<br />8004110b<br />**Number**:<br />-2147217141|No alias for the given entity in the condition was found.|
> |**Name**:<br />QueryBuilderNoAttribute<br />**Hex**:<br />80041103<br />**Number**:<br />-2147217149|The specified attribute does not exist on this entity.|
> |**Name**:<br />QueryBuilderNoAttrsDistinctConflict<br />**Hex**:<br />8004112C<br />**Number**:<br />-2147217108|The no-attrs tag cannot be used in conjuction with Distinct set to true.|
> |**Name**:<br />QueryBuilderNoEntity<br />**Hex**:<br />80041102<br />**Number**:<br />-2147217150|The specified entity was not found.|
> |**Name**:<br />QueryBuilderNoEntityKey<br />**Hex**:<br />80041140<br />**Number**:<br />-2147217088|The specified entitykey was not found.|
> |**Name**:<br />QueryBuilderPagingOrderBy<br />**Hex**:<br />80041129<br />**Number**:<br />-2147217111|Order by columns do not match those in paging cookie.|
> |**Name**:<br />QueryBuilderReportView_Does_Not_Exist<br />**Hex**:<br />8004110d<br />**Number**:<br />-2147217139|A report view does not exist for the specified entity.|
> |**Name**:<br />QueryBuilderSerializationInvalidIsQuickFindFilter<br />**Hex**:<br />80041138<br />**Number**:<br />-2147217096|The only valid values for isquickfindfields attribute are 'true', 'false', '1', and '0'.|
> |**Name**:<br />QueryBuilderSerialzeLinkTopCriteria<br />**Hex**:<br />80041114<br />**Number**:<br />-2147217132|Fetch does not support where clause with conditions from linkentity.|
> |**Name**:<br />QueryBuilderUnexpected<br />**Hex**:<br />80041101<br />**Number**:<br />-2147217151|An unexpected error occurred.|
> |**Name**:<br />QueryBuilderValue_GreaterThanZero<br />**Hex**:<br />8004110c<br />**Number**:<br />-2147217140|A value greater than zero must be specified.|
> |**Name**:<br />QueryContainedSecuredAttributeWithoutAccess<br />**Hex**:<br />8004F506<br />**Number**:<br />-2147158778|The Query contained a secured attribute to which the caller does not have access|
> |**Name**:<br />QueryFilterConditionAttributeNotPresentInExpressionEntity<br />**Hex**:<br />80071119<br />**Number**:<br />-2147020519|The query references a field that does not exist in Dynamics 365: "{0}"|
> |**Name**:<br />QueryNotValidForStaticList<br />**Hex**:<br />8004F702<br />**Number**:<br />-2147158270|Query cannot be specified for a static list.|
> |**Name**:<br />QueryParameterNotUnique<br />**Hex**:<br />8005E00B<br />**Number**:<br />-2147098613|Query parameter {0} must be defined only once within the data set.|
> |**Name**:<br />QueueIdNotPresent<br />**Hex**:<br />80040528<br />**Number**:<br />-2147220184|You must enter the target queue. Provide a valid value in the Queue field and try again.|
> |**Name**:<br />QueueItemNotPresent<br />**Hex**:<br />80040529<br />**Number**:<br />-2147220183|You must enter the name of the record that you would like to put in the queue. Provide a valid value in the Queue Item field and try again.|
> |**Name**:<br />QueueMailboxUnexpectedDeliveryMethod<br />**Hex**:<br />8005E210<br />**Number**:<br />-2147098096|Delivery method for mailbox associated with a queue cannot be outlook client.|
> |**Name**:<br />QuickCreateDisabledOnEntity<br />**Hex**:<br />80060911<br />**Number**:<br />-2147088111|The {0} entity doesn't have a quick create form or the number of nested quick create forms has exceeded the maximum number allowed.|
> |**Name**:<br />QuickCreateInvalidEntityName<br />**Hex**:<br />80060910<br />**Number**:<br />-2147088112|The entityLogicalName isn't valid. This value can't be null or empty, and it must represent an entity in the organization.|
> |**Name**:<br />QuickFindQueryRecordLimitExceeded<br />**Hex**:<br />8004E024<br />**Number**:<br />-2147164124|QuickFindQueryRecordLimit exceeded. Cannot perform this operation.|
> |**Name**:<br />QuickFindSavedQueryAlreadyExists<br />**Hex**:<br />8004853A<br />**Number**:<br />-2147187398|"Only one quickfind saved query can exist for an entity. There already exists a quick-find saved query for entity with objecttypecode: {0}"|
> |**Name**:<br />QuickFormNotCustomizableThroughSdk<br />**Hex**:<br />8004F659<br />**Number**:<br />-2147158439|The SDK does not support creating a form of type "Quick". This form type is reserved for internal use only.|
> |**Name**:<br />QuoteAndSalesOrderCurrencyNotEqual<br />**Hex**:<br />80048cee<br />**Number**:<br />-2147185426|The currency of the record does not match the currency of the price list.|
> |**Name**:<br />QuoteReviseExistingActiveQuote<br />**Hex**:<br />80048d00<br />**Number**:<br />-2147185408|Quote cannot be revised as there already exists another quote in Draft/Active state and with same quote number.|
> |**Name**:<br />ReactivateEntityKeyOnlyForFailedJobs<br />**Hex**:<br />80060897<br />**Number**:<br />-2147088233|Reactivate entity key is only supported for failed job|
> |**Name**:<br />ReadIntentIncompatible<br />**Hex**:<br />80060881<br />**Number**:<br />-2147088255|Plugin Execution Intent of current execution context is not compatible with its parent context|
> |**Name**:<br />ReadOnlyCreateValidationFailed<br />**Hex**:<br />80061002<br />**Number**:<br />-2147086334|You can't create and assign a value to a property instance for a read-only property.|
> |**Name**:<br />ReadOnlyUpdateValidationFailed<br />**Hex**:<br />80061003<br />**Number**:<br />-2147086333|You can't update the property instance for a read-only property.|
> |**Name**:<br />ReadOnlyUserNotSupported<br />**Hex**:<br />80041d40<br />**Number**:<br />-2147214016|The read-only access mode is not supported|
> |**Name**:<br />RecalculateNotSupportedOnNonRollupField<br />**Hex**:<br />80060554<br />**Number**:<br />-2147089068|Field {0} of type {1} does not support Recalculate action. Recalculate action can only be invoked for rollup field.|
> |**Name**:<br />RecommendationAzureConnectionCascadeActivateFailed<br />**Hex**:<br />80061633<br />**Number**:<br />-2147084749|One or more recommendation models couldn't be activated. Try activating the existing recommendation models separately from the Azure service connection.|
> |**Name**:<br />RecommendationAzureConnectionFailed<br />**Hex**:<br />80061631<br />**Number**:<br />-2147084751|Failed to connect to the Azure Recommendations service. Check that the service URL and the Azure account key are valid and the service subscription is active.|
> |**Name**:<br />RecommendationModelActivateConnectionMustBeActive<br />**Hex**:<br />80061607<br />**Number**:<br />-2147084793|The Azure Machine Learning recommendation service connection must be activated before the model can be activated. Please activate the recommendation service connection and try again.|
> |**Name**:<br />RecommendationModelActiveVersionInvalidStatus<br />**Hex**:<br />80061602<br />**Number**:<br />-2147084798|The model version used must be successfully built before the model can be activated.|
> |**Name**:<br />RecommendationModelActiveVersionNotSet<br />**Hex**:<br />80061601<br />**Number**:<br />-2147084799|The model version used is empty. To activate the model, specify the model version.|
> |**Name**:<br />RecommendationModelBuildConnectionMustBeActive<br />**Hex**:<br />80061606<br />**Number**:<br />-2147084794|The Azure Machine Learning recommendation service connection must be activated before building a recommendation model. Please activate the recommendation service connection and try again.|
> |**Name**:<br />RecommendationModelExpired<br />**Hex**:<br />80061608<br />**Number**:<br />-2147084792|The recommendation model has expired. Change the Valid Until date and try to activate the model again.|
> |**Name**:<br />RecommendationModelMappingDuplicateRecord<br />**Hex**:<br />80061610<br />**Number**:<br />-2147084784|The recommendation model mapping values for entity, mapping type and version must be unique.|
> |**Name**:<br />RecommendationModelMappingReadOnly<br />**Hex**:<br />80061611<br />**Number**:<br />-2147084783|You can't modify a Recommendation entity if it has a corresponding Basket entity.|
> |**Name**:<br />RecommendationModelVersionActive<br />**Hex**:<br />80061620<br />**Number**:<br />-2147084768|The RecommendationModel Version is selected as the active version on a model and cannot be deleted.|
> |**Name**:<br />RecommendationModelVersionBuildInProgress<br />**Hex**:<br />80061621<br />**Number**:<br />-2147084767|A workflow to build a model is already in progress. You can't start another build workflow until the current workflow has finished.|
> |**Name**:<br />RecommendationModelVersionDuplicateName<br />**Hex**:<br />80061622<br />**Number**:<br />-2147084766|A model version with the same name already exists. Specify a different name.|
> |**Name**:<br />RecommendationsUnavailable<br />**Hex**:<br />80061605<br />**Number**:<br />-2147084795|Azure Machine Learning product recommendations are temporarily unavailable. Only catalog recommendations are available.|
> |**Name**:<br />RecommendedDocumentsRetrievalFailure<br />**Hex**:<br />80071015<br />**Number**:<br />-2147020779|Unable to retrieve document suggestions from the document source.|
> |**Name**:<br />RecommendedDocumentsRetrievalFailureWhenSPSiteNotConfigured<br />**Hex**:<br />80071028<br />**Number**:<br />-2147020760|Unable to retrieve document suggestions from the document source.|
> |**Name**:<br />RecordAndOpportunityCurrencyNotEqual<br />**Hex**:<br />80048cef<br />**Number**:<br />-2147185425|The currency of the record does not match the currency of the price list.|
> |**Name**:<br />RecordAndPricelistCurrencyNotEqual<br />**Hex**:<br />80048cf6<br />**Number**:<br />-2147185418|The currency of the record does not match the currency of the price list.|
> |**Name**:<br />RecordCanOnlyBeRevisedFromActiveState<br />**Hex**:<br />8004F883<br />**Number**:<br />-2147157885|You can only revise an active product.|
> |**Name**:<br />RecordCountExceededForExcelOnlineError<br />**Hex**:<br />80072456<br />**Number**:<br />-2147015594|Expected records count is {0}. Current records count is:{1}|
> |**Name**:<br />RecordNotFoundByEntityKey<br />**Hex**:<br />80060891<br />**Number**:<br />-2147088239|A record with the specified key values does not exist in {0} entity|
> |**Name**:<br />RecordResolutionFailed<br />**Hex**:<br />8004F603<br />**Number**:<br />-2147158525|The record could not be updated because the original record no longer exists in Microsoft Dynamics 365.|
> |**Name**:<br />RecurrenceCalendarTypeNotSupported<br />**Hex**:<br />8004E116<br />**Number**:<br />-2147163882|The calendar type is not supported.|
> |**Name**:<br />RecurrenceEndDateTooBig<br />**Hex**:<br />8004E119<br />**Number**:<br />-2147163879|The recurrence pattern end date is invalid.|
> |**Name**:<br />RecurrenceHasNoOccurrence<br />**Hex**:<br />8004E117<br />**Number**:<br />-2147163881|The recurrence pattern has no occurrences.|
> |**Name**:<br />RecurrenceRuleDeleteFailure<br />**Hex**:<br />8004E111<br />**Number**:<br />-2147163887|Cannot delete a rule that is attached to an existing rule master. Delete the rule by using the parent entity.|
> |**Name**:<br />RecurrenceRuleUpdateFailure<br />**Hex**:<br />8004E110<br />**Number**:<br />-2147163888|Cannot update a rule that is attached to an existing rule master. Update the rule by using the parent entity.|
> |**Name**:<br />RecurrenceStartDateTooSmall<br />**Hex**:<br />8004E118<br />**Number**:<br />-2147163880|The recurrence pattern start date is invalid.|
> |**Name**:<br />RecurringSeriesCompleted<br />**Hex**:<br />8004E10B<br />**Number**:<br />-2147163893|The series has invalid ExpansionStateCode.|
> |**Name**:<br />RecurringSeriesMasterIsLocked<br />**Hex**:<br />8004E113<br />**Number**:<br />-2147163885|The recurring series master record is locked by some other process.|
> |**Name**:<br />RefEntityRelationshipRoleRequired<br />**Hex**:<br />80048470<br />**Number**:<br />-2147187600|The entity relationship role of the referencing entity is required when creating a new one-to-many entity relationship.|
> |**Name**:<br />ReferencedEntityHasLogicalPrimaryNameField<br />**Hex**:<br />8004432E<br />**Number**:<br />-2147204306|This entity has a primary field that is logical and therefore cannot be the referenced entity in a one-to-many relationship|
> |**Name**:<br />ReferencedEntityMustHaveLookupView<br />**Hex**:<br />80044337<br />**Number**:<br />-2147204297|Referenced entities of a relationship must have a lookup view|
> |**Name**:<br />ReferencingEntityCannotBeSolutionAware<br />**Hex**:<br />80044350<br />**Number**:<br />-2147204272|Referencing entities in a relationship cannot be a component in a solution.|
> |**Name**:<br />ReferencingEntityMustHaveAssociationView<br />**Hex**:<br />80044338<br />**Number**:<br />-2147204296|Referencing entities of a relationship must have an association view|
> |**Name**:<br />RefferedSolutionIsDifferent<br />**Hex**:<br />80050122<br />**Number**:<br />-2147155678|Found unpublished row outside of active solution: SiteMapId = {0}, SolutionId = {1}|
> |**Name**:<br />ReflexiveEntityParentOrChildDoesNotExist<br />**Hex**:<br />80040388<br />**Number**:<br />-2147220600|Either the parent or child entity does not exist|
> |**Name**:<br />RefRoleNavPaneDisplayOptionRequired<br />**Hex**:<br />80060898<br />**Number**:<br />-2147088232|The NavPaneDisplayOption attribute is required for the Referencing Role of a one-to-many relationship {0}.|
> |**Name**:<br />RegardingObjectValuesRetrievalFailure<br />**Hex**:<br />80071012<br />**Number**:<br />-2147020782|Failed to retrieve regarding object values.|
> |**Name**:<br />RelatedEntityAlreadyExistsInProfile<br />**Hex**:<br />8005F21e<br />**Number**:<br />-2147093986|The related entity already exists in this profile.|
> |**Name**:<br />RelatedEntityDoesNotExistInProfileItem<br />**Hex**:<br />8006098E<br />**Number**:<br />-2147087986|The related entity {0} of the mobile offline profile item association {1} of the mobile offline profile item {2} doesn’t exist in the profile items of profile {3}.|
> |**Name**:<br />RelatedEntityDoesNotExistsInProfile<br />**Hex**:<br />8005F21f<br />**Number**:<br />-2147093985|The related entity doesn’t exist in the profile items.|
> |**Name**:<br />RelatedEntityGenericError<br />**Hex**:<br />8005F220<br />**Number**:<br />-2147093984|An unexpected error occurred while creating the profile association. Please try again.|
> |**Name**:<br />RelatedRecordsFailure<br />**Hex**:<br />80071013<br />**Number**:<br />-2147020781|Failed to retrieve related records.|
> |**Name**:<br />RelationshipGraphLimitExceeded<br />**Hex**:<br />80071139<br />**Number**:<br />-2147020487|You have specified one or more profile item associations for the entities defined in the profile '{0}'. Please review the profile item associations involving the entity '{1}' which has an association count of {2} and exceeds the supported limit of {3}.|
> |**Name**:<br />RelationshipInsightsFeatureDisableError<br />**Hex**:<br />80044292<br />**Number**:<br />-2147204462|Relationship Insights feature can't be disabled|
> |**Name**:<br />RelationshipInsightsFeatureNotEnabledError<br />**Hex**:<br />80044293<br />**Number**:<br />-2147204461|Relationship Insights feature is not enabled or RI package is not installed|
> |**Name**:<br />RelationshipIntelligenceSDKInvocationError<br />**Hex**:<br />80044276<br />**Number**:<br />-2147204490|You need Dynamics 365 (online) to use the Relationship Insights SDK.|
> |**Name**:<br />RelationshipIsNotCustomRelationship<br />**Hex**:<br />8004700a<br />**Number**:<br />-2147192822|The specified relationship is not a custom relationship|
> |**Name**:<br />RelationshipNameLengthExceedsLimit<br />**Hex**:<br />8004802A<br />**Number**:<br />-2147188694|Identifiers cannot be more than {1} characters long. The name provided: {0} length is greater than maxlength {1} characters.|
> |**Name**:<br />RelationshipNotCreatedForOfficeGraphError<br />**Hex**:<br />80044235<br />**Number**:<br />-2147204555|This relationship cannot be created because neither entity is enabled for officegraph.|
> |**Name**:<br />RelationshipNotUpdatedForOfficeGraphError<br />**Hex**:<br />80044236<br />**Number**:<br />-2147204554|This relationship cannot be updated for officegraph because neither entity is enabled for officegraph.|
> |**Name**:<br />RelationshipRoleMismatch<br />**Hex**:<br />80048467<br />**Number**:<br />-2147187609|The relationship role name {0} does not match either expected entity name of {1} or {2}.|
> |**Name**:<br />RelationshipRoleNodeNumberInvalid<br />**Hex**:<br />80048469<br />**Number**:<br />-2147187607|There must be two entity relationship role nodes when creating a new many-to-many entity relationship.|
> |**Name**:<br />RelatioshipAlreadyExists<br />**Hex**:<br />8005F221<br />**Number**:<br />-2147093983|Selected Relationship for entity already exists in profile. |
> |**Name**:<br />ReportDoesNotExist<br />**Hex**:<br />80040499<br />**Number**:<br />-2147220327|Report does not exist. ReportId:{0}|
> |**Name**:<br />ReportFileTooBig<br />**Hex**:<br />80048297<br />**Number**:<br />-2147188073|The file is too large and cannot be uploaded. Please reduce the size of the file and try again.|
> |**Name**:<br />ReportFileZeroLength<br />**Hex**:<br />80048296<br />**Number**:<br />-2147188074|You have uploaded an empty file.  Please select a new file and try again.|
> |**Name**:<br />ReportImportCategoryOptionNotFound<br />**Hex**:<br />8004F028<br />**Number**:<br />-2147160024|A category option for the reports was not found.|
> |**Name**:<br />ReportingServicesReportExpected<br />**Hex**:<br />80040484<br />**Number**:<br />-2147220348|The report is not a Reporting Services report.|
> |**Name**:<br />ReportLocalProcessingError<br />**Hex**:<br />80048310<br />**Number**:<br />-2147187952|Error occurred while viewing locally processed report. ReportId:{0}|
> |**Name**:<br />ReportLoopBeingCreated<br />**Hex**:<br />80040498<br />**Number**:<br />-2147220328|Creating this parental association would create a loop in Reports hierarchy.|
> |**Name**:<br />ReportLoopExists<br />**Hex**:<br />80040497<br />**Number**:<br />-2147220329|Loop exists in the reports hierarchy.|
> |**Name**:<br />ReportMissingDataSourceCredentialsError<br />**Hex**:<br />80048311<br />**Number**:<br />-2147187951|Credentials have not been supplied for a data source used by the report. ReportId:{0}|
> |**Name**:<br />ReportMissingDataSourceError<br />**Hex**:<br />80048312<br />**Number**:<br />-2147187950|A data source expected by the report has not been supplied. ReportId:{0}|
> |**Name**:<br />ReportMissingEndpointError<br />**Hex**:<br />80048313<br />**Number**:<br />-2147187949|The SOAP endpoint used by the ReportViewer control could not be accessed.|
> |**Name**:<br />ReportMissingParameterError<br />**Hex**:<br />80048314<br />**Number**:<br />-2147187948|A parameter expected by the report has not been supplied. ReportId:{0}|
> |**Name**:<br />ReportMissingReportSourceError<br />**Hex**:<br />80048315<br />**Number**:<br />-2147187947|No source has been specified for the report. ReportId:{0}|
> |**Name**:<br />ReportNotAvailable<br />**Hex**:<br />80048299<br />**Number**:<br />-2147188071|Report not available|
> |**Name**:<br />ReportParentChildNotCustomizable<br />**Hex**:<br />8004832f<br />**Number**:<br />-2147187921|The report could not be updated because either the parent report or the child report is not customizable.|
> |**Name**:<br />ReportRdlSandboxing<br />**Hex**:<br />80048293<br />**Number**:<br />-2147188077|Report upload failed due to RDL Sandboxing limitations on the Report Server.|
> |**Name**:<br />ReportRenderError<br />**Hex**:<br />80040494<br />**Number**:<br />-2147220332|An error occurred during report rendering.|
> |**Name**:<br />ReportSecurityError<br />**Hex**:<br />80048316<br />**Number**:<br />-2147187946|The report contains a security violation. ReportId:{0}|
> |**Name**:<br />ReportServerInvalidUrl<br />**Hex**:<br />80048301<br />**Number**:<br />-2147187967|Cannot contact report server from given URL|
> |**Name**:<br />ReportServerNoPrivilege<br />**Hex**:<br />80048302<br />**Number**:<br />-2147187966|Not enough privilege to configure report server|
> |**Name**:<br />ReportServerSP2HotFixNotApplied<br />**Hex**:<br />80048309<br />**Number**:<br />-2147187959|Report server SP2 Workgroup does not have the hotfix for role creation|
> |**Name**:<br />ReportServerUnknownException<br />**Hex**:<br />80048300<br />**Number**:<br />-2147187968|Unknown exception thrown by report server|
> |**Name**:<br />ReportServerVersionLow<br />**Hex**:<br />80048303<br />**Number**:<br />-2147187965|Report server does not meet the minimal version requirement|
> |**Name**:<br />ReportTypeBlocked<br />**Hex**:<br />80048295<br />**Number**:<br />-2147188075|The report is not a valid type.  It cannot be uploaded or downloaded.|
> |**Name**:<br />ReportUploadDisabled<br />**Hex**:<br />80048294<br />**Number**:<br />-2147188076|Reporting Services reports cannot be uploaded. If you want to create a new report, please use the Report Wizard.|
> |**Name**:<br />ReportViewerError<br />**Hex**:<br />8004832c<br />**Number**:<br />-2147187924|An error occurred during report rendering. ReportId:{0}|
> |**Name**:<br />RequestIsNotAuthenticated<br />**Hex**:<br />80044302<br />**Number**:<br />-2147204350|Request is not authenticated.|
> |**Name**:<br />RequestLengthTooLarge<br />**Hex**:<br />8004418a<br />**Number**:<br />-2147204726|Request message length is too large.|
> |**Name**:<br />RequiredBundleItemCannotBeUpdated<br />**Hex**:<br />80081009<br />**Number**:<br />-2146955255|You can't delete this bundle item because it's a required product in the bundle.|
> |**Name**:<br />RequiredBundleProductCannotBeDeleted<br />**Hex**:<br />80081008<br />**Number**:<br />-2146955256|You can't delete this product record because it's a required product in a bundle.|
> |**Name**:<br />RequiredChildReportHasOtherParent<br />**Hex**:<br />8004F029<br />**Number**:<br />-2147160023|A category option for the reports was not found.|
> |**Name**:<br />RequiredColumnsNotFoundInImportFile<br />**Hex**:<br />80040383<br />**Number**:<br />-2147220605|One or more source columns used in the transformation do not exist in the source file.|
> |**Name**:<br />RequiredFieldMissing<br />**Hex**:<br />80040200<br />**Number**:<br />-2147220992|Required field missing.|
> |**Name**:<br />RequiredProcessStepIsNull<br />**Hex**:<br />8006041a<br />**Number**:<br />-2147089382|To move to the next stage, complete the required steps.|
> |**Name**:<br />RequireValidImportMapForUpdate<br />**Hex**:<br />8004F600<br />**Number**:<br />-2147158528|The update operation cannot be completed because the import map used for the update is invalid.|
> |**Name**:<br />RestrictedSolutionName<br />**Hex**:<br />8004F022<br />**Number**:<br />-2147160030|The solution unique name '{0}' is restricted and can only be used by internal solutions.|
> |**Name**:<br />RestrictInheritedRole<br />**Hex**:<br />80044152<br />**Number**:<br />-2147204782|Inherited roles cannot be modified.|
> |**Name**:<br />RetiredProductToBundle<br />**Hex**:<br />8004F993<br />**Number**:<br />-2147157613|You can't add a retired product to a bundle.|
> |**Name**:<br />RetrieveImagePropertiesFail<br />**Hex**:<br />80072552<br />**Number**:<br />-2147015342|Cannot retrieve properties for provided entity image|
> |**Name**:<br />RetrieveOrganizationInfoUnexpectedError<br />**Hex**:<br />80072301<br />**Number**:<br />-2147015935|Unexpected error during retrieve organization information. The dependent services might not be available at this time. Please retry later.|
> |**Name**:<br />RetrieveRecordOfflineErrorCode<br />**Hex**:<br />8005F213<br />**Number**:<br />-2147093997|This record isn't available while you're offline.  Reconnect and try again.|
> |**Name**:<br />RetrieveUserLicenseUnexpectedError<br />**Hex**:<br />80072300<br />**Number**:<br />-2147015936|Unexpected error during retrieve user license information. The dependent services might not be available at this time. Please retry later.|
> |**Name**:<br />RetryFailed<br />**Hex**:<br />8004F045<br />**Number**:<br />-2147159995|The action was failed after {0} times of retry. InnerException is: {1}.|
> |**Name**:<br />RibbonImportDependencyMissingEntity<br />**Hex**:<br />8004F104<br />**Number**:<br />-2147159804|The ribbon item '{0}' is dependent on entity {1}.|
> |**Name**:<br />RibbonImportDependencyMissingRibbonControl<br />**Hex**:<br />8004F107<br />**Number**:<br />-2147159801|The ribbon item '{0}' is dependent on ribbon control id='{1}'.|
> |**Name**:<br />RibbonImportDependencyMissingRibbonElement<br />**Hex**:<br />8004F105<br />**Number**:<br />-2147159803|The ribbon item '{0}' is dependent on <{1} Id="{2}" />.|
> |**Name**:<br />RibbonImportDependencyMissingWebResource<br />**Hex**:<br />8004F106<br />**Number**:<br />-2147159802|The ribbon item '{0}' is dependent on Web resource id='{1}'.|
> |**Name**:<br />RibbonImportDuplicateElementId<br />**Hex**:<br />8004F10B<br />**Number**:<br />-2147159797|The ribbon element with the Id:{0} cannot be imported because an existing ribbon element with the same Id already exists.|
> |**Name**:<br />RibbonImportEntityNotSupported<br />**Hex**:<br />8004F103<br />**Number**:<br />-2147159805|The solution cannot be imported because the {0} entity contains a Ribbon definition, which is not supported for that entity. Remove the RibbonDiffXml node from the entity definition and try to import again.|
> |**Name**:<br />RibbonImportHidingBasicHomeTab<br />**Hex**:<br />8004F101<br />**Number**:<br />-2147159807|The definition of the ribbon being imported will remove the Microsoft Dynamics 365 home tab. Include a home tab definition, or a ribbon will not be displayed in areas of the application that display the home tab.|
> |**Name**:<br />RibbonImportHidingJewel<br />**Hex**:<br />8004F10A<br />**Number**:<br />-2147159798|Ribbon customizations cannot hide the <Jewel> node. Any ribbon customization that hides this node is ignored during import and will not be exported.|
> |**Name**:<br />RibbonImportInvalidPrivilegeName<br />**Hex**:<br />8004F102<br />**Number**:<br />-2147159806|The RibbonDiffXml in this solution contains a reference to an invalid privilege: {0}. Update the RibbonDiffXml to reference a valid privilege and try importing again.|
> |**Name**:<br />RibbonImportLocationAndIdDoNotMatch<br />**Hex**:<br />8004F109<br />**Number**:<br />-2147159799|CustomAction Id '{0}' cannot override '{1}' because '{2}' does not match the CustomAction Location value.|
> |**Name**:<br />RibbonImportModifyingTopLevelNode<br />**Hex**:<br />8004F108<br />**Number**:<br />-2147159800|Ribbon customizations cannot be made to the following top-level ribbon nodes: <Ribbon>, <ContextualGroups>, and <Tabs>.|
> |**Name**:<br />RibbonImportRibbonDiffIdInvalidLength<br />**Hex**:<br />8004F10C<br />**Number**:<br />-2147159796|We can’t import this ribbon element because the ID length exceeds the maximum length of 128 characters: {0}|
> |**Name**:<br />RINotProvisioned<br />**Hex**:<br />80044281<br />**Number**:<br />-2147204479|Relationship Insights hasn’t been turned on for your organization {0}.|
> |**Name**:<br />RoleAlreadyExists<br />**Hex**:<br />80041403<br />**Number**:<br />-2147216381|A role with the specified name '{0}' already exists on business unit {1} and Solution Id {3}. Role id: {2}|
> |**Name**:<br />RoleNotEnabledForTabletApp<br />**Hex**:<br />8005F203<br />**Number**:<br />-2147094013|You haven't been authorized to use this app.\nCheck with your system administrator to update your settings.|
> |**Name**:<br />RollupAggregateQueryRecordLimitExceeded<br />**Hex**:<br />8004E025<br />**Number**:<br />-2147164123|Calculations can't be performed online because the calculation limit of {0} related records has been reached.|
> |**Name**:<br />RollupCalculationLimitReached<br />**Hex**:<br />80060561<br />**Number**:<br />-2147089055|Calculations can't be performed at this time because the calculation limit has been reached. Please wait and try again.|
> |**Name**:<br />RollupDependentFieldNameAlreadyExists<br />**Hex**:<br />80060556<br />**Number**:<br />-2147089066|Required dependent field {0} for rollup field cannot be created as another field with same name already exists. Please use an alternative name to create the rollup field.|
> |**Name**:<br />RollupFieldAggregateFunctionNotAllowed<br />**Hex**:<br />80060546<br />**Number**:<br />-2147089082|The aggregate function {0} isn’t allowed.|
> |**Name**:<br />RollupFieldAggregateFunctionNotAllowedForRollupFieldDataType<br />**Hex**:<br />80060545<br />**Number**:<br />-2147089083|The aggregate function {0} isn’t allowed when the rollup field is a {1} data type.|
> |**Name**:<br />RollupFieldAndAggregateFieldDataTypeFormatMismatch<br />**Hex**:<br />80060544<br />**Number**:<br />-2147089084|The {0} data type with format {1} isn’t allowed for the aggregated field when the rollup field is a {2} data type with format {3}.|
> |**Name**:<br />RollupFieldDefinitionNotValid<br />**Hex**:<br />80060553<br />**Number**:<br />-2147089069|The calculation failed because the rollup field definition is invalid. Contact your system administrator.|
> |**Name**:<br />RollupFieldDependentFieldCannotDeleted<br />**Hex**:<br />80060541<br />**Number**:<br />-2147089087|Rollup field {0} depends on this field. It can only be deleted by deleting the corresponding rollup field {0}.|
> |**Name**:<br />RollupFieldNoWriteAccess<br />**Hex**:<br />8004E027<br />**Number**:<br />-2147164121|User does not have write permission on {0} record {1} with ID:{2} to calculate rollup field.|
> |**Name**:<br />RollupFieldsAggregateFieldDataTypeNotAllowedSimilarRollupFieldDataType<br />**Hex**:<br />8006053d<br />**Number**:<br />-2147089091|The {0} data type isn’t allowed for the aggregated field when the rollup field is a {1} data type.|
> |**Name**:<br />RollupFieldsAggregateFieldNotBelongToRelatedEntity<br />**Hex**:<br />80060540<br />**Number**:<br />-2147089088|The aggregated field {0} doesn’t belong to the related entity {1}.|
> |**Name**:<br />RollupFieldsAggregateFieldNotBelongToSourceEntity<br />**Hex**:<br />8006053f<br />**Number**:<br />-2147089089|The aggregated field {0} doesn’t belong to the source entity {1}.|
> |**Name**:<br />RollupFieldsAggregateFieldNotPartOfEntity<br />**Hex**:<br />80060537<br />**Number**:<br />-2147089097|Aggregated field {0} does not belong to entity {1}|
> |**Name**:<br />RollupFieldsAggregateFunctionTypeMismatch<br />**Hex**:<br />8006053a<br />**Number**:<br />-2147089094|The {0} data type isn’t allowed for the aggregated field when the aggregate function is {1}.|
> |**Name**:<br />RollupFieldsAggregateNotDefined<br />**Hex**:<br />80060536<br />**Number**:<br />-2147089098|An aggregate function and an aggregated field must be provided for the rollup.|
> |**Name**:<br />RollupFieldsAggregateOnRollupFieldOrComplexCalcFieldNotAllowed<br />**Hex**:<br />8006053c<br />**Number**:<br />-2147089092|The aggregated field must be either a simple field or a basic calculated field.|
> |**Name**:<br />RollupFieldsDataTypeNotValid<br />**Hex**:<br />8006053e<br />**Number**:<br />-2147089090|The {0} data type isn’t valid for the rollup field.|
> |**Name**:<br />RollupFieldsGeneric<br />**Hex**:<br />8006053b<br />**Number**:<br />-2147089093|The rollup field definition isn't valid.|
> |**Name**:<br />RollupFieldSourceFilterFieldNotAllowed<br />**Hex**:<br />80060548<br />**Number**:<br />-2147089080|The source entity filter must use either a simple field or a basic calculated field. It can't use a rollup field, or a calculated field that is using a rollup field.|
> |**Name**:<br />RollupFieldsSourceEntityNotHierarchical<br />**Hex**:<br />80060535<br />**Number**:<br />-2147089099|The source entity {0} hierarchy doesn’t exist.|
> |**Name**:<br />RollupFieldsSourceFilterConditionInvalid<br />**Hex**:<br />80060538<br />**Number**:<br />-2147089096|The source entity {0} filter condition {1} isn’t valid.|
> |**Name**:<br />RollupFieldsTargetEntityNotValid<br />**Hex**:<br />80060552<br />**Number**:<br />-2147089070|Related entity {0} is not allowed for rollups.|
> |**Name**:<br />RollupFieldsTargetFilterConditionInvalid<br />**Hex**:<br />80060539<br />**Number**:<br />-2147089095|The related entity {0} filter condition {1} isn’t valid.|
> |**Name**:<br />RollupFieldsTargetRelationshipNotPartOfOneToNRelationship<br />**Hex**:<br />80060534<br />**Number**:<br />-2147089100|1:N relationship {0} from the source entity {1} to the related entity {2} doesn’t exist.|
> |**Name**:<br />RollupFieldsTargetRelationshipNull<br />**Hex**:<br />80060533<br />**Number**:<br />-2147089101|The related entity is empty. It must be provided when the source entity hierarchy isn’t used for the rollup.|
> |**Name**:<br />RollupFieldsTargetSameAsSourceEntity<br />**Hex**:<br />80060551<br />**Number**:<br />-2147089071|Self referential 1:N relationships are not allowed for the rollup field.|
> |**Name**:<br />RollupFieldsV2FeatureNotEnabled<br />**Hex**:<br />80060565<br />**Number**:<br />-2147089051|The feature is not supported in the current version of the product|
> |**Name**:<br />RollupFieldTargetFilterFieldNotAllowed<br />**Hex**:<br />80060549<br />**Number**:<br />-2147089079|The target entity filter must use either a simple field or a basic calculated field. It can't use a rollup field, or a calculated field that is using a rollup field.|
> |**Name**:<br />RollupFormulaFieldInvalid<br />**Hex**:<br />80060560<br />**Number**:<br />-2147089056|The formula field isn’t valid.|
> |**Name**:<br />RollupInvalidAttributeForFilterCondition<br />**Hex**:<br />80060564<br />**Number**:<br />-2147089052|The {0} attribute is not allowed for filter condition.|
> |**Name**:<br />RollupOrCalcNotAllowedInWorkflowWaitCondition<br />**Hex**:<br />80060557<br />**Number**:<br />-2147089065|The field {0} is either a rollup field or a rollup dependent field or a calculated field. Such fields are not allowed in workflow wait condition.|
> |**Name**:<br />RollupTargetLinkedEntityCanOnlyUsedForActivityPartyEntities<br />**Hex**:<br />80060563<br />**Number**:<br />-2147089053|Target related entity can only be used for {0} entity for rollup over {1} type entities.|
> |**Name**:<br />RollupTargetLinkedEntityOnlySupportedForActivityEntities<br />**Hex**:<br />80060562<br />**Number**:<br />-2147089054|Target related entity is only supported for rollup over {0} type entities.|
> |**Name**:<br />RollupTargetLinkedRelationshipNotValid<br />**Hex**:<br />80060566<br />**Number**:<br />-2147089050|Target Linked Relationship {0} is not valid.|
> |**Name**:<br />RootBusinessUnitCannotBeDisabled<br />**Hex**:<br />80041d63<br />**Number**:<br />-2147213981|Root Business unit cannot be disabled.|
> |**Name**:<br />RouterIsDisabled<br />**Hex**:<br />8005E246<br />**Number**:<br />-2147098042|Microsoft Dynamics 365 has been configured to use server-side synchronization to process email. This error occurs because some clients are still configured to use the legacy Email router. You need to uninstall the Email router client application on any servers it was installed on.|
> |**Name**:<br />RouteTypeUnsupported<br />**Hex**:<br />800404e9<br />**Number**:<br />-2147220247|The route type is unsupported|
> |**Name**:<br />RoutingNotAllowed<br />**Hex**:<br />800404e7<br />**Number**:<br />-2147220249|This object type can not be routed.|
> |**Name**:<br />RoutingRuleActivateDeactivateByNonOwner<br />**Hex**:<br />8004F885<br />**Number**:<br />-2147157883|This Routing Rule Set cannot be activated or deactivated by someone who is not its owner.|
> |**Name**:<br />RoutingRuleMissingRuleCriteria<br />**Hex**:<br />8004F877<br />**Number**:<br />-2147157897|You can't activate this rule until you resolve any missing rule criteria information in the rule items.|
> |**Name**:<br />RoutingRulePublishedByNonOwner<br />**Hex**:<br />8004F878<br />**Number**:<br />-2147157896|The Routing Rule Set cannot be published or unpublished by someone who is not its owner.|
> |**Name**:<br />RoutingRulePublishedByOwner<br />**Hex**:<br />8004F876<br />**Number**:<br />-2147157898|Your rule can't be activated until the current active rule is deactivated. The active rule can only be deactivated by the rule owner.|
> |**Name**:<br />RowGuidIsNotValidName<br />**Hex**:<br />80047001<br />**Number**:<br />-2147192831|rowguid is a reserved name and cannot be used as an identifier|
> |**Name**:<br />RSCancelBatchError<br />**Hex**:<br />8004831c<br />**Number**:<br />-2147187940|Error occurred while canceling the batch operation.|
> |**Name**:<br />RSCreateBatchError<br />**Hex**:<br />80048320<br />**Number**:<br />-2147187936|Error occurred while creating a batch operation.|
> |**Name**:<br />RSDeleteItemError<br />**Hex**:<br />80048317<br />**Number**:<br />-2147187945|Error occurred while deleting an item from the report server.|
> |**Name**:<br />RSExecuteBatchError<br />**Hex**:<br />8004831d<br />**Number**:<br />-2147187939|Error occurred while performing the batch operation.|
> |**Name**:<br />RSFindItemsError<br />**Hex**:<br />80048318<br />**Number**:<br />-2147187944|Error occurred while finding an item on the report server.|
> |**Name**:<br />RSGetDataSourceContentsError<br />**Hex**:<br />8004831a<br />**Number**:<br />-2147187942|Error occurred while getting the data source contents.|
> |**Name**:<br />RSGetItemDataSourcesError<br />**Hex**:<br />80048321<br />**Number**:<br />-2147187935|Error occurred while fetching current data sources.|
> |**Name**:<br />RSGetItemTypeError<br />**Hex**:<br />8004832b<br />**Number**:<br />-2147187925|Error occurred while fetching the report.|
> |**Name**:<br />RSGetReportHistoryLimitError<br />**Hex**:<br />8004831e<br />**Number**:<br />-2147187938|Error occurred while fetching the number of snapshots stored for the report.|
> |**Name**:<br />RSGetReportParametersError<br />**Hex**:<br />80048323<br />**Number**:<br />-2147187933|Error occurred while getting report parameters.|
> |**Name**:<br />RSListExtensionsError<br />**Hex**:<br />8004831b<br />**Number**:<br />-2147187941|Error occurred while fetching the list of data extensions installed on the report server.|
> |**Name**:<br />RSListReportHistoryError<br />**Hex**:<br />8004831f<br />**Number**:<br />-2147187937|Error occurred while fetching the report history snapshots.|
> |**Name**:<br />RSMoveItemError<br />**Hex**:<br />80048330<br />**Number**:<br />-2147187920|Cannot move report item {0} to {1}|
> |**Name**:<br />RSReportParameterTypeMismatchError<br />**Hex**:<br />80048329<br />**Number**:<br />-2147187927|The parameter type of the report is not valid.|
> |**Name**:<br />RSSetDataSourceContentsError<br />**Hex**:<br />80048319<br />**Number**:<br />-2147187943|Error occurred while setting the data source contents.|
> |**Name**:<br />RSSetExecutionOptionsError<br />**Hex**:<br />80048325<br />**Number**:<br />-2147187931|Error occurred while setting execution options.|
> |**Name**:<br />RSSetItemDataSourcesError<br />**Hex**:<br />80048322<br />**Number**:<br />-2147187934|Error occurred while setting the data source.|
> |**Name**:<br />RSSetPropertiesError<br />**Hex**:<br />8004832a<br />**Number**:<br />-2147187926|Error occurred while setting property values for the report.|
> |**Name**:<br />RSSetReportHistoryLimitError<br />**Hex**:<br />80048327<br />**Number**:<br />-2147187929|Error occurred while setting report history snapshot limit.|
> |**Name**:<br />RSSetReportHistoryOptionsError<br />**Hex**:<br />80048326<br />**Number**:<br />-2147187930|Error occurred while setting report history snapshot options.|
> |**Name**:<br />RSSetReportParametersError<br />**Hex**:<br />80048324<br />**Number**:<br />-2147187932|Error occurred while setting report parameters.|
> |**Name**:<br />RSUpdateReportExecutionSnapshotError<br />**Hex**:<br />80048328<br />**Number**:<br />-2147187928|Error occurred while taking snapshot of a report.|
> |**Name**:<br />RuleActivationNotAllowedWithDeletedStages<br />**Hex**:<br />80060014<br />**Number**:<br />-2147090412|You can't activate this rule because it contains a deleted stage or stage category. Fix the rule and try again.|
> |**Name**:<br />RuleAlreadyExistsWithSameQueueAndChannel<br />**Hex**:<br />8004F884<br />**Number**:<br />-2147157884|Record creation rule for the specified channel and queue already exists. You can't create another one.|
> |**Name**:<br />RuleAlreadyInactiveState<br />**Hex**:<br />8004F852<br />**Number**:<br />-2147157934|This routing rule is already in Active state.|
> |**Name**:<br />RuleAlreadyInDraftState<br />**Hex**:<br />8004F853<br />**Number**:<br />-2147157933|You can not deactivate a draft routing rule.|
> |**Name**:<br />RuleAlreadyPublishing<br />**Hex**:<br />80048434<br />**Number**:<br />-2147187660|The selected duplicate detection rule is already being published.|
> |**Name**:<br />RuleCreationNotAllowedForCyclicReferences<br />**Hex**:<br />80060012<br />**Number**:<br />-2147090414|You can't create this rule because it contains a cyclical reference. Fix the rule and try again.|
> |**Name**:<br />RuleNotFound<br />**Hex**:<br />80048433<br />**Number**:<br />-2147187661|No rules were found that match the criteria.|
> |**Name**:<br />RuleNotSupportedForEditor<br />**Hex**:<br />80060007<br />**Number**:<br />-2147090425|The current rule definition cannot be edited in the Business rule editor.|
> |**Name**:<br />RulesInInconsistentStateFound<br />**Hex**:<br />80048423<br />**Number**:<br />-2147187677|One or more rules cannot be unpublished, either because they are in the process of being published, or are in a state where they cannot be unpublished.|
> |**Name**:<br />RuntimeRibbonXmlValidation<br />**Hex**:<br />8004F671<br />**Number**:<br />-2147158415|The most recent customized ribbon for a tab on this page cannot be generated. The out-of-box version of the ribbon is displayed instead.|
> |**Name**:<br />S2SAccessTokenCannotBeAcquired<br />**Hex**:<br />8005E243<br />**Number**:<br />-2147098045|Failed to acquire S2S access token from authorization server.|
> |**Name**:<br />S2SNotConfigured<br />**Hex**:<br />80044259<br />**Number**:<br />-2147204519|Office Graph Integration relies on server-based SharePoint integration. To use this feature, enable server-based integration and have at least one active SharePoint site.|
> |**Name**:<br />SalesOrderAndInvoiceCurrencyNotEqual<br />**Hex**:<br />80048ced<br />**Number**:<br />-2147185427|The currency of the record does not match the currency of the price list.|
> |**Name**:<br />SalesPeopleDuplicateCalendarNotAllowed<br />**Hex**:<br />80043803<br />**Number**:<br />-2147207165|Fiscal calendar already exists for this salesperson/year|
> |**Name**:<br />SalesPeopleEmptyEffectiveDate<br />**Hex**:<br />80043801<br />**Number**:<br />-2147207167|Fiscal calendar effective date cannot be empty|
> |**Name**:<br />SalesPeopleEmptySalesPerson<br />**Hex**:<br />80043800<br />**Number**:<br />-2147207168|Parent salesperson cannot be empty|
> |**Name**:<br />SalesPeopleManagerNotAllowed<br />**Hex**:<br />80043805<br />**Number**:<br />-2147207163|Territory manager cannot belong to other territory|
> |**Name**:<br />SandboxClientPluginTimeout<br />**Hex**:<br />80044171<br />**Number**:<br />-2147204751|The plug-in execution failed because the operation has timed-out at the Sandbox Client.|
> |**Name**:<br />SandboxHostNotAvailable<br />**Hex**:<br />8004418e<br />**Number**:<br />-2147204722|The plug-in execution failed because no Sandbox Hosts are currently available. Please check that you have a Sandbox server configured and that it is running.|
> |**Name**:<br />SandboxHostPluginTimeout<br />**Hex**:<br />80044172<br />**Number**:<br />-2147204750|The plug-in execution failed because the operation has timed-out at the Sandbox Host.|
> |**Name**:<br />SandboxPluginDisabled<br />**Hex**:<br />80081115<br />**Number**:<br />-2146954987|Sandbox Plug-in execution is disabled.|
> |**Name**:<br />SandboxSdkListenerStartFailed<br />**Hex**:<br />80044174<br />**Number**:<br />-2147204748|The plug-in execution failed because the Sandbox Client encountered an error during initialization.|
> |**Name**:<br />SandboxWorkerNotAvailable<br />**Hex**:<br />8004418d<br />**Number**:<br />-2147204723|The plug-in execution failed because no Sandbox Worker processes are currently available. Please try again.|
> |**Name**:<br />SandboxWorkerPluginExecuteTimeout<br />**Hex**:<br />80081111<br />**Number**:<br />-2146954991|Didn’t receive a response from the {0} plug-in within the 2:20-minute limit.|
> |**Name**:<br />SandboxWorkerPluginTimeout<br />**Hex**:<br />80044173<br />**Number**:<br />-2147204749|The plug-in execution failed because the operation has timed-out at the Sandbox Worker.|
> |**Name**:<br />SandboxWorkerThrottleLimit<br />**Hex**:<br />80081116<br />**Number**:<br />-2146954986|Maximum processes allocated for plug-in business logic exceeded. Fatal errors in plug-ins for this environment have occurred {0} times in the last {1} minutes. Each error requires an additional process to recover. Processes for plug-ins are being recycled. All plug-ins for this environment will fail during this period. More information: https://go.microsoft.com/fwlink/?linkid=2038718 |
> |**Name**:<br />SaveAsDraftAppointmentNotAllowed<br />**Hex**:<br />8004026b<br />**Number**:<br />-2147220885|AllowSaveAsDraftAppointment is turned off.|
> |**Name**:<br />SaveDataFileErrorOutOfSpace<br />**Hex**:<br />8005F209<br />**Number**:<br />-2147094007|Try this action again. If the problem continues, check the {0} for solutions or contact your organization's {#Brand_CRM} Administrator. Finally, you can contact {1}.|
> |**Name**:<br />SavedQueryIsNotCustomizable<br />**Hex**:<br />80047017<br />**Number**:<br />-2147192809|The specified view is not customizable|
> |**Name**:<br />SavedQueryValidationError<br />**Hex**:<br />800609A0<br />**Number**:<br />-2147087968|You can’t publish profile {0} because one of its profile items {1} has an entity {2} in the saved query {3}, which isn’t part of this profile.|
> |**Name**:<br />SavePending<br />**Hex**:<br />80060913<br />**Number**:<br />-2147088109|Save operation is already running in the background.|
> |**Name**:<br />SaveRecordBeforeAddingBundle<br />**Hex**:<br />8004F983<br />**Number**:<br />-2147157629|After you select a price list, you must save the record before you can add a bundle with optional products.|
> |**Name**:<br />ScaleGroupDisabled<br />**Hex**:<br />8004A107<br />**Number**:<br />-2147180281|The specified scalegroup is disabled. Access to organizations in this scalegroup are not allowed.|
> |**Name**:<br />SchedulingFailedForBookingValidation<br />**Hex**:<br />80060915<br />**Number**:<br />-2147088107|Book or Reschedule operation failed due to booking validation.|
> |**Name**:<br />SchedulingFailedForInvalidData<br />**Hex**:<br />80060914<br />**Number**:<br />-2147088108|Book or Reschedule operation failed due to invalid data.|
> |**Name**:<br />SchemaNameContainsNonAlphaNumericCharacters<br />**Hex**:<br />80044364<br />**Number**:<br />-2147204252|Identifier {0} for type {2} can only consist of alpha-numeric and underscore characters.|
> |**Name**:<br />SchemaNameisNotUnique<br />**Hex**:<br />80044363<br />**Number**:<br />-2147204253|The schema name {0} for type {1} is not unique. An {0} with same name already exists.|
> |**Name**:<br />SchemaNameLengthExceedsLimit<br />**Hex**:<br />80044367<br />**Number**:<br />-2147204249|Identifiers cannot be more than {1} characters long. The provided schema name {0} length for type {2} is greater than maxlength {1} characters.|
> |**Name**:<br />SchemaNameMatchesExistingIdentifier<br />**Hex**:<br />80044361<br />**Number**:<br />-2147204255|Identifiers cannot match existing object names. An object of type {1} with same name {0} already exists.|
> |**Name**:<br />SchemaNameMatchesReservedSqlKeywords<br />**Hex**:<br />80044362<br />**Number**:<br />-2147204254|Identifiers cannot match reserved SQL keywords. The name provided :{0} for type {1} matches KeyWord:{2}|
> |**Name**:<br />SchemaNameNotStartwithLetter<br />**Hex**:<br />80044365<br />**Number**:<br />-2147204251|Identifers should start with a letter. The schema name {0} for type {2} doesn't start with letter.|
> |**Name**:<br />ScopeNotSetToGlobal<br />**Hex**:<br />80060403<br />**Number**:<br />-2147089405|Scope should be set to Global while creating business process flow category|
> |**Name**:<br />SdkCorrelationTokenDepthTooHigh<br />**Hex**:<br />80044182<br />**Number**:<br />-2147204734|This workflow job was canceled because the workflow that started it included an infinite loop. Correct the workflow logic and try again. For information about workflow logic, see Help.|
> |**Name**:<br />SdkCustomProcessingStepIsNotAllowed<br />**Hex**:<br />80044187<br />**Number**:<br />-2147204729|Custom SdkMessageProcessingStep is not allowed on the specified message and entity.|
> |**Name**:<br />SdkEntityDoesNotSupportMessage<br />**Hex**:<br />80040800<br />**Number**:<br />-2147219456|The method being invoked does not support provided entity type.|
> |**Name**:<br />SdkEntityOfflineQueuePlaybackIsNotAllowed<br />**Hex**:<br />80044188<br />**Number**:<br />-2147204728|Entity '{0}' is not allowed in offline queue playback.|
> |**Name**:<br />SdkInvalidMessagePropertyName<br />**Hex**:<br />8004416b<br />**Number**:<br />-2147204757|Message property name '{0}' is not valid on message {1}.|
> |**Name**:<br />SdkMessageDoesNotSupportImageRegistration<br />**Hex**:<br />80044189<br />**Number**:<br />-2147204727|Message '{0}' does not support image registration.|
> |**Name**:<br />SdkMessageDoesNotSupportPostImageRegistration<br />**Hex**:<br />8004416e<br />**Number**:<br />-2147204754|PreEvent step registration does not support Post Image.|
> |**Name**:<br />SdkMessageInvalidImageTypeRegistration<br />**Hex**:<br />8004416d<br />**Number**:<br />-2147204755|Message {0} does not support this image type.|
> |**Name**:<br />SdkMessageNotImplemented<br />**Hex**:<br />80044824<br />**Number**:<br />-2147203036|Sdk message is not implemented.|
> |**Name**:<br />SdkMessageNotSupportedOnClient<br />**Hex**:<br />80044181<br />**Number**:<br />-2147204735|The message requested is not supported on the client.|
> |**Name**:<br />SdkMessageNotSupportedOnServer<br />**Hex**:<br />80044180<br />**Number**:<br />-2147204736|The message requested is not supported on the server.|
> |**Name**:<br />SdkMessagesDeprecatedError<br />**Hex**:<br />8004F903<br />**Number**:<br />-2147157757|This message is no longer available. Please consult the SDK for alternative messages.|
> |**Name**:<br />SdkNotEnoughPrivilegeToSetCallerOriginToken<br />**Hex**:<br />80044309<br />**Number**:<br />-2147204343|Caller does not have enough privilege to set CallerOriginToken to the specified value.|
> |**Name**:<br />SearchTextLenExceeded<br />**Hex**:<br />800401ff<br />**Number**:<br />-2147220993|Search Text Length Exceeded.|
> |**Name**:<br />SelectedFileNotFound<br />**Hex**:<br />80071025<br />**Number**:<br />-2147020763|Unable to copy the documents. The source file no longer exists.|
> |**Name**:<br />SeriesMeasureCollectionMismatch<br />**Hex**:<br />8004E003<br />**Number**:<br />-2147164157|Number of series for chart area and number of measure collections for category should be same.|
> |**Name**:<br />ServerLocationAndSSLSetToYes<br />**Hex**:<br />8005E255<br />**Number**:<br />-2147098027|The URL specified for Server Location uses HTTP but Secure Sockets Layer(SSL) is required for Exchange Online.|
> |**Name**:<br />ServerLocationIsEmpty<br />**Hex**:<br />8005E250<br />**Number**:<br />-2147098032|Server Location Field cannot be Empty|
> |**Name**:<br />ServiceAccountMailboxesCountIsGreaterThanOne<br />**Hex**:<br />8005E24A<br />**Number**:<br />-2147098038|More no of service account mailboxes is associated to emailserver profile|
> |**Name**:<br />ServiceAccountMailboxesCountIsZero<br />**Hex**:<br />8005E249<br />**Number**:<br />-2147098039|No service account mailbox is associated for the email server profile.|
> |**Name**:<br />ServiceBusEndpointNotConfigured<br />**Hex**:<br />80081112<br />**Number**:<br />-2146954990|Configuration of required credentials must be completed before messages can be sent.|
> |**Name**:<br />ServiceBusExtendedTokenFailed<br />**Hex**:<br />80044178<br />**Number**:<br />-2147204744|Failed to retrieve the additional token for service bus post.|
> |**Name**:<br />ServiceBusIssuerCertificateError<br />**Hex**:<br />80044177<br />**Number**:<br />-2147204745|Service integration issuer certificate error.|
> |**Name**:<br />ServiceBusIssuerNotFound<br />**Hex**:<br />80044176<br />**Number**:<br />-2147204746|Cannot find service integration issuer information.|
> |**Name**:<br />ServiceBusMaxSizeExceeded<br />**Hex**:<br />80050208<br />**Number**:<br />-2147155448|The service bus call failed because the request payload has exceeded maximum allowed size. Please reduce your request size and retry.|
> |**Name**:<br />ServiceBusPostDisabled<br />**Hex**:<br />8004417A<br />**Number**:<br />-2147204742|Service bus post is disabled for the organization.|
> |**Name**:<br />ServiceBusPostFailed<br />**Hex**:<br />80044175<br />**Number**:<br />-2147204747|The service bus post failed.|
> |**Name**:<br />ServiceBusPostPostponed<br />**Hex**:<br />80044179<br />**Number**:<br />-2147204743|Service bus post is being postponed.|
> |**Name**:<br />ServiceEndpointAcsAuthNotSupported<br />**Hex**:<br />80050209<br />**Number**:<br />-2147155447|Service Endpoint with ACS authentication type is no longer supported. Please change your endpoint configuration to use a supported authentication type|
> |**Name**:<br />ServiceInstantiationFailed<br />**Hex**:<br />80040244<br />**Number**:<br />-2147220924|Instantiation of an Entity failed.|
> |**Name**:<br />SessionTokenUnavailable<br />**Hex**:<br />80040253<br />**Number**:<br />-2147220909|Session token is not available unless there is a transaction in place.|
> |**Name**:<br />SetActiveNotSupportedOnNewRecords<br />**Hex**:<br />80060374<br />**Number**:<br />-2147089548|SetActiveProcess is not supported on new records.|
> |**Name**:<br />SharePointAbsoluteAndRelativeUrlEmpty<br />**Hex**:<br />80048149<br />**Number**:<br />-2147188407|Both absolute URL and relative URL cannot be null.|
> |**Name**:<br />SharePointAuthenticationFailure<br />**Hex**:<br />800608B3<br />**Number**:<br />-2147088205|Microsoft Dynamics 365 cannot authenticate this user {0} . Verify that the information for this user is correct, and then try again.|
> |**Name**:<br />SharePointAuthorizationFailure<br />**Hex**:<br />800608B4<br />**Number**:<br />-2147088204|Microsoft Dynamics 365 cannot authorize this user {0} . Verify that the information for this user is correct, and then try again.|
> |**Name**:<br />SharePointCertificateExpired<br />**Hex**:<br />800608B1<br />**Number**:<br />-2147088207|Certificate used for Sharepoint validation has expired|
> |**Name**:<br />SharePointConnectionFailure<br />**Hex**:<br />800608B5<br />**Number**:<br />-2147088203|Microsoft Dynamics 365 cannot connect this user {0} to SharePoint. Verify that the information for this user is correct and exists in SharePoint, and then try again.|
> |**Name**:<br />SharePointCrmDomainValidator<br />**Hex**:<br />8004F302<br />**Number**:<br />-2147159294|The SharePoint and Microsoft Dynamics 365 Servers are on different domains. Please ensure a trust relationship between the two domains.|
> |**Name**:<br />SharePointCrmGridIsInstalledValidator<br />**Hex**:<br />8004F309<br />**Number**:<br />-2147159287|The Microsoft Dynamics 365 Grid component must be installed on the SharePoint server. This component is required for SharePoint integration to work correctly.|
> |**Name**:<br />SharePointErrorAbsoluteUrlClipped<br />**Hex**:<br />8004F314<br />**Number**:<br />-2147159276|The URL exceeds the maximum number of 256 characters. Use shorter names for sites and folders, and try again.|
> |**Name**:<br />SharePointErrorRetrieveAbsoluteUrl<br />**Hex**:<br />8004F310<br />**Number**:<br />-2147159280|An error occurred while retrieving the absolute and site collection url for a SharePoint object.|
> |**Name**:<br />SharePointInvalidEntityForValidation<br />**Hex**:<br />8004F311<br />**Number**:<br />-2147159279|Entity Does not support SharePoint Url Validation.|
> |**Name**:<br />SharePointRealmMismatch<br />**Hex**:<br />800608B2<br />**Number**:<br />-2147088206|Sharepoint realm ID entered does not match with the registered realm at Sharepoint side.|
> |**Name**:<br />SharePointRecordWithDuplicateUrl<br />**Hex**:<br />80048057<br />**Number**:<br />-2147188649|There is already a record with the same Url.|
> |**Name**:<br />SharePointRoleProvisionJobAlreadyExists<br />**Hex**:<br />8004F0FA<br />**Number**:<br />-2147159814|A system job to provision the selected security role is pending. Any changes made to the security role record before this system job starts will be applied to this system job.|
> |**Name**:<br />SharePointS2SIsDisabled<br />**Hex**:<br />80071017<br />**Number**:<br />-2147020777|SharePoint server-based SharePoint integration not enabled.|
> |**Name**:<br />SharePointServerDiscoveryValidator<br />**Hex**:<br />8004F303<br />**Number**:<br />-2147159293|The URL is incorrect or the site is not running.|
> |**Name**:<br />SharePointServerLanguageValidator<br />**Hex**:<br />8004F308<br />**Number**:<br />-2147159288|Microsoft Dynamics 365 and Microsoft Office SharePoint Server must have the same base language.|
> |**Name**:<br />SharePointServerVersionValidator<br />**Hex**:<br />8004F304<br />**Number**:<br />-2147159292|The SharePoint Site Collection must be running a supported version of Microsoft Office SharePoint Server or Microsoft Windows SharePoint Services. Please refer the implementation guide.|
> |**Name**:<br />SharePointSiteCollectionIsAccessibleValidator<br />**Hex**:<br />8004F305<br />**Number**:<br />-2147159291|The URL is incorrect or the site is not running.|
> |**Name**:<br />SharePointSiteCreationFailure<br />**Hex**:<br />8004F0F8<br />**Number**:<br />-2147159816|Failed to create the site {0} in SharePoint.|
> |**Name**:<br />SharePointSiteNotConfigured<br />**Hex**:<br />80071014<br />**Number**:<br />-2147020780|SharePointSite is not configured, it need to be configured.|
> |**Name**:<br />SharePointSiteNotPresentInSharePoint<br />**Hex**:<br />8004F0F3<br />**Number**:<br />-2147159821|Site {0} does not exists in SharePoint.|
> |**Name**:<br />SharePointSitePermissionsValidator<br />**Hex**:<br />8004F307<br />**Number**:<br />-2147159289|The current user does not have the appropriate privileges. You must be a SharePoint site administrator on the SharePoint site.|
> |**Name**:<br />SharePointSiteWideProvisioningJobFailed<br />**Hex**:<br />8004F0FB<br />**Number**:<br />-2147159813|SharePoint provisioning job has failed.|
> |**Name**:<br />SharePointTeamProvisionJobAlreadyExists<br />**Hex**:<br />8004F0F9<br />**Number**:<br />-2147159815|A system job to provision the selected team is pending. Any changes made to the team record before this system job starts will be applied to this system job.|
> |**Name**:<br />SharePointUnableToAclSite<br />**Hex**:<br />8004F0F6<br />**Number**:<br />-2147159818|Unable to ACL site {0} in SharePoint.|
> |**Name**:<br />SharePointUnableToAclSiteWithPrivilege<br />**Hex**:<br />8004F0F5<br />**Number**:<br />-2147159819|Unable to ACL site {0} with privilege {1} in SharePoint.|
> |**Name**:<br />SharePointUnableToAddUserToGroup<br />**Hex**:<br />8004F0F1<br />**Number**:<br />-2147159823|Microsoft Dynamics 365 cannot add this user {0} to the group {1} in SharePoint. Verify that the information for this user and group are correct and that the group exists in SharePoint, and then try again.|
> |**Name**:<br />SharePointUnableToCreateSiteGroup<br />**Hex**:<br />8004F0F7<br />**Number**:<br />-2147159817|Unable to create site group {0} in SharePoint.|
> |**Name**:<br />SharePointUnableToRemoveUserFromGroup<br />**Hex**:<br />8004F0F2<br />**Number**:<br />-2147159822|Unable to remove user {0} from group {1} in SharePoint.|
> |**Name**:<br />SharePointUnableToRetrieveGroup<br />**Hex**:<br />8004F0F4<br />**Number**:<br />-2147159820|Unable to retrieve the group {0} from SharePoint.|
> |**Name**:<br />SharePointUrlHostValidator<br />**Hex**:<br />8004F301<br />**Number**:<br />-2147159295|The URL cannot be resolved into an IP.|
> |**Name**:<br />SharePointUrlIsRootWebValidator<br />**Hex**:<br />8004F306<br />**Number**:<br />-2147159290|The URL is not valid. The URL must be a valid site collection and cannot include a subsite. The URL must be in a valid form, such as http://SharePointServer/sites/CrmSite.|
> |**Name**:<br />SharePointVersionUnsupported<br />**Hex**:<br />800608B6<br />**Number**:<br />-2147088202|Microsoft Dynamics 365 cannot connect to Sharepoint as the Sharepoint Version is unsupported. Install the correct version, and then try again. |
> |**Name**:<br />SimilarityRuleDisabled<br />**Hex**:<br />80071016<br />**Number**:<br />-2147020778|No similarity rule active for this entity.|
> |**Name**:<br />SimilarityRuleFCBOff<br />**Hex**:<br />80071018<br />**Number**:<br />-2147020776|Similarity rules not enabled.|
> |**Name**:<br />SingletonMappingFoundForArrayParameter<br />**Hex**:<br />8004037e<br />**Number**:<br />-2147220610|A single transformation parameter mapping is defined for an array parameter.|
> |**Name**:<br />SiteMapMissing<br />**Hex**:<br />80050016<br />**Number**:<br />-2147155946|You don’t have permissions for these records or something may be wrong with the site map. Contact your system administrator.If you are the administrator, you can go to the solutions page and import a different solution.|
> |**Name**:<br />SiteMapXsdValidationError<br />**Hex**:<br />8004F401<br />**Number**:<br />-2147159039|Sitemap xml failed XSD validation with the following error: '{0}' at line {1} position {2}.|
> |**Name**:<br />SkipValidDateTimeBehavior<br />**Hex**:<br />800608A3<br />**Number**:<br />-2147088221|The behavior value for this field was ignored. A System Customizer will need to configure the behavior value for this field directly.|
> |**Name**:<br />SlaActivateDeactivateByNonOwner<br />**Hex**:<br />8004F872<br />**Number**:<br />-2147157902|This SLA cannot be activated or deactivated by someone who is not its owner.|
> |**Name**:<br />SlaAlreadyInactiveState<br />**Hex**:<br />8004F861<br />**Number**:<br />-2147157919|You can't activate this record because it's already active.|
> |**Name**:<br />SlaAlreadyInDraftState <br />**Hex**:<br />8004F862<br />**Number**:<br />-2147157918|You can't deactivate this record because it's in a draft state.|
> |**Name**:<br />SlaNotEnabledEntity<br />**Hex**:<br />80055003<br />**Number**:<br />-2147135485|SLA is not enabled for this entity.|
> |**Name**:<br />SlaPermissionToPerformAction<br />**Hex**:<br />8004F875<br />**Number**:<br />-2147157899|You don't have the required permissions on SLAs and processes to perform this action.|
> |**Name**:<br />SnapshotReportNotReady<br />**Hex**:<br />80040489<br />**Number**:<br />-2147220343|The selected report is not ready for viewing. The report is still being created or a report snapshot is not available. ReportId:{0}|
> |**Name**:<br />SocialCareDisabledError<br />**Hex**:<br />80060621<br />**Number**:<br />-2147088863|There's a problem communicating with the Dynamics 365 Organization. The organization might be unavailable or the feature is set so that it can't receive social data. Try again later. If the problem persists, contact your Microsoft Dynamics 365 administrator.|
> |**Name**:<br />SolutionConcurrencyFailure<br />**Hex**:<br />80071151<br />**Number**:<br />-2147020463|The solution installation or removal failed due to the installation or removal of another solution at the same time. Please try again later.|
> |**Name**:<br />SolutionConfigurationPageMustBeHtmlWebResource<br />**Hex**:<br />8004701C<br />**Number**:<br />-2147192804|The solution configuration page must exist within the solution it represents.|
> |**Name**:<br />SolutionImportCauseTimeout<br />**Hex**:<br />80048543<br />**Number**:<br />-2147187389|The operation timed out. This may be because a solution is currently being imported into this environment. Please try again after the solution import is completed. Solutions should be imported outside of working hours if possible.|
> |**Name**:<br />SolutionRestrictedAttributes<br />**Hex**:<br />80072003<br />**Number**:<br />-2147016701|Component cannot be created because it already has solution-aware columns. Entity: {0}, Existing Attribute: {1}|
> |**Name**:<br />SolutionUniqueNameViolation<br />**Hex**:<br />8004F023<br />**Number**:<br />-2147160029|The solution unique name '{0}' is already being used and cannot be used again.|
> |**Name**:<br />SolutionUpgradeFailed<br />**Hex**:<br />8004F046<br />**Number**:<br />-2147159994|Solution Upgrade action failed after import as holding. InnerException is: {1}.|
> |**Name**:<br />SolutionUpgradeNotAvailable<br />**Hex**:<br />8004853B<br />**Number**:<br />-2147187397|"The {0} solution doesn’t have an upgrade that is ready to be applied."|
> |**Name**:<br />SolutionUpgradeWrongSolutionSelected<br />**Hex**:<br />8004853C<br />**Number**:<br />-2147187396|"To use this action, you must first select the old solution and then try again."|
> |**Name**:<br />SourceAttributeHeaderTooBig<br />**Hex**:<br />80044340<br />**Number**:<br />-2147204288|Column headers must be 160 or fewer characters. Fix the column headers, and then run Data Migration Manager again.|
> |**Name**:<br />SourceEntityMappedToMultipleTargets<br />**Hex**:<br />8004033d<br />**Number**:<br />-2147220675|This source entity is mapped to more than one Microsoft Dynamics 365 entity. Remove any duplicate mappings, and then import this data map again.|
> |**Name**:<br />SPAccountNameFetchFailure<br />**Hex**:<br />8006072A<br />**Number**:<br />-2147088598|Exception occured while fetching account name from Sharepoint.|
> |**Name**:<br />SPAllFilesErrorScenario<br />**Hex**:<br />80060760<br />**Number**:<br />-2147088544|One or more sites in all files view of SharePointDocument failed.|
> |**Name**:<br />SPBadLockInFileCollectionErrorCode<br />**Hex**:<br />8006070A<br />**Number**:<br />-2147088630|The file in the collection has bad lock |
> |**Name**:<br />SPCertificationError<br />**Hex**:<br />80060767<br />**Number**:<br />-2147088537|S2STokenIssuer certificate not found.|
> |**Name**:<br />SPConnectionFailure<br />**Hex**:<br />80060761<br />**Number**:<br />-2147088543|Failed to connect to SharePointSite.|
> |**Name**:<br />SPCurrentDocumentLocationDisabledErrorCode<br />**Hex**:<br />80060720<br />**Number**:<br />-2147088608|Current document location is disabled by administrator|
> |**Name**:<br />SPCurrentFolderAlreadyExistErrorCode<br />**Hex**:<br />80060721<br />**Number**:<br />-2147088607|Record already present in db|
> |**Name**:<br />SPDataValidationFiledOnFieldAndListErrorCode<br />**Hex**:<br />80060713<br />**Number**:<br />-2147088621|Data validation has failed on the field and the list|
> |**Name**:<br />SPDataValidationFiledOnFieldErrorCode<br />**Hex**:<br />80060711<br />**Number**:<br />-2147088623|Data validation has failed on the field|
> |**Name**:<br />SPDataValidationFiledOnListErrorCode<br />**Hex**:<br />80060712<br />**Number**:<br />-2147088622|Data validation has failed on the list|
> |**Name**:<br />SPDefaultSiteNotPresent<br />**Hex**:<br />80060739<br />**Number**:<br />-2147088583|OneDrive activation needs a default SharePoint site.|
> |**Name**:<br />SPDocumentMappingFailure<br />**Hex**:<br />80060734<br />**Number**:<br />-2147088588|Can't map documents to their location.|
> |**Name**:<br />SPDuplicateValuesFoundErrorCode<br />**Hex**:<br />80060708<br />**Number**:<br />-2147088632|The list item could not be updated because duplicate values were found for one or more field(s) in the list|
> |**Name**:<br />SpecifyIncomingPassword<br />**Hex**:<br />8005E253<br />**Number**:<br />-2147098029|Specify password for Incoming Connection|
> |**Name**:<br />SpecifyInComingPort<br />**Hex**:<br />8005E24F<br />**Number**:<br />-2147098033|Specify Incomming Port and save again|
> |**Name**:<br />SpecifyIncomingServerLocation<br />**Hex**:<br />8005E24B<br />**Number**:<br />-2147098037|Specify the URL of the incoming server location|
> |**Name**:<br />SpecifyIncomingUserName<br />**Hex**:<br />8005E251<br />**Number**:<br />-2147098031|Specify username for Incoming Connection|
> |**Name**:<br />SpecifyOutgoingPassword<br />**Hex**:<br />8005E254<br />**Number**:<br />-2147098028|Specify password for Outgoing Connection|
> |**Name**:<br />SpecifyOutgoingPort<br />**Hex**:<br />8005E256<br />**Number**:<br />-2147098026|Specify Outgoing Port and save again|
> |**Name**:<br />SpecifyOutgoingServerLocation<br />**Hex**:<br />8005E24C<br />**Number**:<br />-2147098036|Specify the URL of the outgoing server location|
> |**Name**:<br />SpecifyOutgoingUserName<br />**Hex**:<br />8005E252<br />**Number**:<br />-2147098030|Specify username for Outgoing Connection|
> |**Name**:<br />SPExclusiveLockOnFileErrorCode<br />**Hex**:<br />80060705<br />**Number**:<br />-2147088635|Exclusive lock on the file|
> |**Name**:<br />SPFileAlreadyCheckedOutErrorCode<br />**Hex**:<br />80060702<br />**Number**:<br />-2147088638|File is already checked out|
> |**Name**:<br />SPFileCheckedOutInvalidArgsErrorCode<br />**Hex**:<br />80060703<br />**Number**:<br />-2147088637|Checkout arguments are not valid|
> |**Name**:<br />SPFileContentNullErrorCode<br />**Hex**:<br />8006070D<br />**Number**:<br />-2147088627|Content of the file creation information must not be null|
> |**Name**:<br />SPFileIsCheckedOutByOtherUser<br />**Hex**:<br />80060728<br />**Number**:<br />-2147088600|File is checked out to a user other than the current user|
> |**Name**:<br />SPFileIsReadOnlyErrorCode<br />**Hex**:<br />8006070F<br />**Number**:<br />-2147088625|Field is read-only|
> |**Name**:<br />SPFileNameModifiedErrorCode<br />**Hex**:<br />80060729<br />**Number**:<br />-2147088599|The folder can't be found. If you changed the automatically generated folder name for this document location directly in SharePoint, you must change the folder name in Dynamics 365 to match the renamed folder. To do this, select Edit Location and type the matching name in Folder Name field.|
> |**Name**:<br />SPFileNotCheckedOutErrorCode<br />**Hex**:<br />80060700<br />**Number**:<br />-2147088640|File is not checked out|
> |**Name**:<br />SPFileNotFoundErrorCode<br />**Hex**:<br />80060706<br />**Number**:<br />-2147088634|File cannot be found|
> |**Name**:<br />SPFileNotLockedErrorCode<br />**Hex**:<br />80060707<br />**Number**:<br />-2147088633|The file in the collection is not locked|
> |**Name**:<br />SPFileSizeMismatchErrorCode<br />**Hex**:<br />8006070E<br />**Number**:<br />-2147088626|There is a mismatch between the size of the document stream written and the size of the input document stream|
> |**Name**:<br />SPFileTooLargeOrInfectedErrorCode<br />**Hex**:<br />80060709<br />**Number**:<br />-2147088631|Virus checking indicates the file is infected with a virus or the file is too large|
> |**Name**:<br />SPFolderCreationFailure<br />**Hex**:<br />8004F0F0<br />**Number**:<br />-2147159824|Cannot Create Folder with this name|
> |**Name**:<br />SPFolderNotFoundErrorCode<br />**Hex**:<br />8006071B<br />**Number**:<br />-2147088613|Folder Not Found|
> |**Name**:<br />SPFolderRenameFailure<br />**Hex**:<br />8006072C<br />**Number**:<br />-2147088596|Exception occurred while Editing Sharepoint Document Proeprties.|
> |**Name**:<br />SPGenericErrorCode<br />**Hex**:<br />80060719<br />**Number**:<br />-2147088615|Error while doing this operation on SharePoint|
> |**Name**:<br />SPIllegalCharactersInFileNameErrorCode<br />**Hex**:<br />8006071F<br />**Number**:<br />-2147088609|Illegal characters in filename|
> |**Name**:<br />SPIllegalFileTypeErrorCode<br />**Hex**:<br />8006071D<br />**Number**:<br />-2147088611|Illegal file type|
> |**Name**:<br />SPInstanceOfRecurringEventErrorCode<br />**Hex**:<br />80060716<br />**Number**:<br />-2147088618|List item is an instance of a recurring event which is not a recurrence exception, the list item is a workflow task whose parent workflow is in the recycle bin, or the parent list is a document library|
> |**Name**:<br />SPIntermittentError<br />**Hex**:<br />80060764<br />**Number**:<br />-2147088540|Intermittent error occured. Please refresh the grid and try again|
> |**Name**:<br />SPInvalidDocumentLocation<br />**Hex**:<br />80060762<br />**Number**:<br />-2147088542|Invalid Sharepoint Document Location type|
> |**Name**:<br />SPInvalidFieldValueErrorCode<br />**Hex**:<br />8006071E<br />**Number**:<br />-2147088610|Invalid Field Value|
> |**Name**:<br />SPInvalidLookupValuesErrorCode<br />**Hex**:<br />8006070B<br />**Number**:<br />-2147088629|List item could not be updated because invalid lookup values were found for one or more field(s) in the list|
> |**Name**:<br />SPInvalidSavedQueryErrorCode<br />**Hex**:<br />80060718<br />**Number**:<br />-2147088616|Error while doing this operation on SharePoint|
> |**Name**:<br />SPInvalidSubSite<br />**Hex**:<br />80060763<br />**Number**:<br />-2147088541|SubSite url is incorrectly formed|
> |**Name**:<br />SPItemNotExistErrorCode<br />**Hex**:<br />80060717<br />**Number**:<br />-2147088617|List item does not exist|
> |**Name**:<br />SPMalFormedRelativeUrl<br />**Hex**:<br />80060766<br />**Number**:<br />-2147088538|Relative URL should not have preceding or trailing spaces.|
> |**Name**:<br />SPModifiedOnServerErrorCode<br />**Hex**:<br />80060710<br />**Number**:<br />-2147088624|List item was modified on the server so changes cannot be committed|
> |**Name**:<br />SPMultipleOdbSitesError<br />**Hex**:<br />8006072D<br />**Number**:<br />-2147088595|More than one site with One Drive enabled is not allowed.|
> |**Name**:<br />SPNoActiveDocumentLocationErrorCode<br />**Hex**:<br />8006071C<br />**Number**:<br />-2147088612|No Active Document Location|
> |**Name**:<br />SPNotAdminError<br />**Hex**:<br />80060765<br />**Number**:<br />-2147088539|Only crm admin who is tenant admin can perform create operation|
> |**Name**:<br />SPNotEnabledError<br />**Hex**:<br />8006073A<br />**Number**:<br />-2147088582|SharePoint integration is not enabled on Entity|
> |**Name**:<br />SPNotEnabledForEntity<br />**Hex**:<br />8006073B<br />**Number**:<br />-2147088581|SharePoint Integration and Microsoft Teams Integration is not enabled on Entity|
> |**Name**:<br />SPNullFileUrlErrorCode<br />**Hex**:<br />8006070C<br />**Number**:<br />-2147088628|URL of the file creation information must not be null and URL of the file creation information must not be invalid|
> |**Name**:<br />SPNullRegardingObjectErrorCode<br />**Hex**:<br />80060723<br />**Number**:<br />-2147088605|Regarding object id is null|
> |**Name**:<br />SPOdbDisabledError<br />**Hex**:<br />8006072E<br />**Number**:<br />-2147088594|Please enable ODB(One Drive for Business) feature to create ODB site.|
> |**Name**:<br />SPOdbDuplicateLocationError<br />**Hex**:<br />80060735<br />**Number**:<br />-2147088587|More than one ODB (OneDrive for Business) location is not allowed.|
> |**Name**:<br />SPOdbUpdateDeleteError<br />**Hex**:<br />8006072F<br />**Number**:<br />-2147088593|You cannot update or delete ODB(One Drive for Business) site.|
> |**Name**:<br />SPOdbUpdateDeleteLocationError<br />**Hex**:<br />80060736<br />**Number**:<br />-2147088586|You cannot update or delete SharePoint Document Location of type ODB (OneDrive for Business).|
> |**Name**:<br />SPOperationNotSupportedErrorCode<br />**Hex**:<br />80060715<br />**Number**:<br />-2147088619|List does not support this operation|
> |**Name**:<br />SPOperatorNotSupportedErrorCode<br />**Hex**:<br />80060724<br />**Number**:<br />-2147088604|{0} does not support the selected operator|
> |**Name**:<br />SPPersonalSiteNotFound<br />**Hex**:<br />8006072B<br />**Number**:<br />-2147088597|Personal Site not found for the user.|
> |**Name**:<br />SPRequiredColCheckInErrorCode<br />**Hex**:<br />80060725<br />**Number**:<br />-2147088603|Exception occurred while doing document check-in as some columns are made required at SharePoint|
> |**Name**:<br />SPSearchOneDriveNotCreated<br />**Hex**:<br />80060737<br />**Number**:<br />-2147088585|OneDrive location is not created yet. Please create the location before searching.|
> |**Name**:<br />SPSharedLockOnFileErrorCode<br />**Hex**:<br />80060704<br />**Number**:<br />-2147088636|Shared lock on the file|
> |**Name**:<br />SPSiteNotFoundErrorCode<br />**Hex**:<br />8006071A<br />**Number**:<br />-2147088614|Site Not Found|
> |**Name**:<br />SPSiteProtocolError<br />**Hex**:<br />80060738<br />**Number**:<br />-2147088584|Protocol error in accessing SharePoint|
> |**Name**:<br />SPThrottlingLimitExceededErrorCode<br />**Hex**:<br />80060714<br />**Number**:<br />-2147088620|Throttling limit is exceeded by the operation|
> |**Name**:<br />SPUnauthorizedAccessErrorCode<br />**Hex**:<br />80060701<br />**Number**:<br />-2147088639|Current user have insufficient privileges|
> |**Name**:<br />SPUploadFailure<br />**Hex**:<br />80060740<br />**Number**:<br />-2147088576|Upload failed on SharePoint due to unknown reasons. Probably the file is too large|
> |**Name**:<br />SqlArithmeticOverflowError<br />**Hex**:<br />80041136<br />**Number**:<br />-2147217098|A SQL arithmetic overflow error occurred|
> |**Name**:<br />SqlEncryption<br />**Hex**:<br />80048518<br />**Number**:<br />-2147187432|There was an error in Data Encryption.|
> |**Name**:<br />SqlEncryptionCannotOpenSymmetricKeyBecauseDatabaseMasterKeyDoesNotExistOrIsNotOpened<br />**Hex**:<br />8004851A<br />**Number**:<br />-2147187430|Cannot open Symmetric Key because Database Master Key does not exist in the database or is not opened.|
> |**Name**:<br />SqlEncryptionCertificateDoesNotExist<br />**Hex**:<br />8004851D<br />**Number**:<br />-2147187427|Certificate with Name='{0}' does not exist in the database.|
> |**Name**:<br />SqlEncryptionChangeEncryptionKeyExceededQuotaForTheInterval<br />**Hex**:<br />80048529<br />**Number**:<br />-2147187415|'Change' encryption key has already been executed {0} times in the last {1} minutes. Please wait a couple of minutes and then try again.|
> |**Name**:<br />SqlEncryptionCreateCertificateError<br />**Hex**:<br />8004851E<br />**Number**:<br />-2147187426|Cannot create Certificate with Name='{0}' because it already exists.|
> |**Name**:<br />SqlEncryptionCreateDatabaseMasterKeyError<br />**Hex**:<br />8004851B<br />**Number**:<br />-2147187429|Cannot create Database Master Key because already exists.|
> |**Name**:<br />SqlEncryptionCreateSymmetricKeyError<br />**Hex**:<br />80048521<br />**Number**:<br />-2147187423|Cannot create Symmetric Key with Name='{0}' because it already exists.|
> |**Name**:<br />SqlEncryptionDatabaseMasterKeyDoesNotExist<br />**Hex**:<br />80048519<br />**Number**:<br />-2147187431|Database Master Key does not exist in the database.|
> |**Name**:<br />SqlEncryptionDeleteCertificateError<br />**Hex**:<br />8004851F<br />**Number**:<br />-2147187425|Cannot delete Certificate with Name='{0}' because it does not exist.|
> |**Name**:<br />SqlEncryptionDeleteDatabaseMasterKeyError<br />**Hex**:<br />8004851C<br />**Number**:<br />-2147187428|Cannot delete Database Master Key because it does not exist.|
> |**Name**:<br />SqlEncryptionDeleteEncryptionKeyError<br />**Hex**:<br />80048526<br />**Number**:<br />-2147187418|Cannot delete the encryption key.|
> |**Name**:<br />SqlEncryptionDeleteSymmetricKeyError<br />**Hex**:<br />80048522<br />**Number**:<br />-2147187422|Cannot delete Symmetric Key with Name='{0}' because it does not exist.|
> |**Name**:<br />SqlEncryptionEncryptionDecryptionTestError<br />**Hex**:<br />80048523<br />**Number**:<br />-2147187421|Error while testing data encryption and decryption.|
> |**Name**:<br />SqlEncryptionEncryptionKeyValidationError<br />**Hex**:<br />80048528<br />**Number**:<br />-2147187416|The new encryption key does not meet the strong encryption key requirements. The key must be between 10 and 100 characters in length, and must have at least one numeral, at least one letter, and one symbol or special character. {0}|
> |**Name**:<br />SqlEncryptionIsActiveCannotRestoreEncryptionKey<br />**Hex**:<br />80048525<br />**Number**:<br />-2147187419|Cannot perform 'activate' encryption key because the encryption key is already set and is working. Use 'change' encryption key instead.|
> |**Name**:<br />SqlEncryptionIsInactiveCannotChangeEncryptionKey<br />**Hex**:<br />80048527<br />**Number**:<br />-2147187417|Cannot perform 'change' encryption key because the encryption key is not already set or is not working. First use 'activate' encryption key instead to set the correct current encryption key and then use 'change' encryption if you want to re-encrypt data using a new encryption key.|
> |**Name**:<br />SqlEncryptionKeyCannotDecryptExistingData<br />**Hex**:<br />80048524<br />**Number**:<br />-2147187420|Cannot decrypt existing encrypted data (Entity='{0}', Attribute='{1}') using the current encryption key. Use 'activate' encryption key to set the correct encryption key.|
> |**Name**:<br />SqlEncryptionRestoreEncryptionKeyCannotDecryptExistingData<br />**Hex**:<br />8004852B<br />**Number**:<br />-2147187413|Cannot perform 'activate' because the encryption key doesn’t match the original encryption key that was used to encrypt the data.|
> |**Name**:<br />SqlEncryptionSetEncryptionKeyIsAlreadyRunningCannotRunItInParallel<br />**Hex**:<br />8004852A<br />**Number**:<br />-2147187414|The system is currently running a request to 'change' or 'activate' the encryption key. Please wait before making another request.|
> |**Name**:<br />SqlEncryptionSymmetricKeyCannotOpenBecauseWrongPassword<br />**Hex**:<br />80048530<br />**Number**:<br />-2147187408|Cannot open encryption Symmetric Key because the password is wrong.|
> |**Name**:<br />SqlEncryptionSymmetricKeyDoesNotExist<br />**Hex**:<br />80048520<br />**Number**:<br />-2147187424|Symmetric Key with Name='{0}' does not exist in the database.|
> |**Name**:<br />SqlEncryptionSymmetricKeyDoesNotExistOrNoPermission<br />**Hex**:<br />8004852F<br />**Number**:<br />-2147187409|Cannot open encryption Symmetric Key because it does not exist in the database or user does not have permission.|
> |**Name**:<br />SqlEncryptionSymmetricKeyPasswordDoesNotExistInConfigDB<br />**Hex**:<br />8004852E<br />**Number**:<br />-2147187410|Encryption Symmetric Key password does not exist in Config DB.|
> |**Name**:<br />SqlEncryptionSymmetricKeySourceDoesNotExistInConfigDB<br />**Hex**:<br />8004852D<br />**Number**:<br />-2147187411|Encryption Symmetric Key Source does not exist in Config DB.|
> |**Name**:<br />SqlErrorInStoredProcedure<br />**Hex**:<br />8004C001<br />**Number**:<br />-2147172351|SQL error {0} occurred in stored procedure {1}|
> |**Name**:<br />SqlMaxRecursionExceeded<br />**Hex**:<br />80044157<br />**Number**:<br />-2147204777|The maximum recursion has reached before statement completion.|
> |**Name**:<br />SrsDataConnectorNotInstalled<br />**Hex**:<br />80040492<br />**Number**:<br />-2147220334|MSCRM Data Connector Not Installed|
> |**Name**:<br />SrsDataConnectorNotInstalledUpload<br />**Hex**:<br />80048292<br />**Number**:<br />-2147188078|This report can’t upload because Dynamics 365 Reporting Extensions, required components for reporting, are not installed on the server that is running Microsoft SQL Server Reporting Services.|
> |**Name**:<br />SSM_MaxPCI_Exceeded<br />**Hex**:<br />80072570<br />**Number**:<br />-2147015312|Please re-login to refresh your session.|
> |**Name**:<br />SSM_RefreshToken_Failed<br />**Hex**:<br />80072571<br />**Number**:<br />-2147015311|Failed to refresh login session.|
> |**Name**:<br />StageEntityIsNull<br />**Hex**:<br />80060451<br />**Number**:<br />-2147089327|Validation error: stage entity cannot be null.|
> |**Name**:<br />StageIdIsEmpty<br />**Hex**:<br />80060454<br />**Number**:<br />-2147089324|Validation error: Stage ID cannot be empty.|
> |**Name**:<br />StageIdIsNotPresentInBusinessProcess<br />**Hex**:<br />80060450<br />**Number**:<br />-2147089328|Validation error: Stage ID ‘{0}’ is not present in Business Process. Please contact your system administrator.|
> |**Name**:<br />StageIdIsNotValid<br />**Hex**:<br />80060458<br />**Number**:<br />-2147089320|Validation error: Stage ID is not valid for Business Process.|
> |**Name**:<br />StateTransitionActivateNewStatus<br />**Hex**:<br />8004F857<br />**Number**:<br />-2147157929|You can't activate this record because of the status transition rules.Contact your system administrator.|
> |**Name**:<br />StateTransitionActiveToCanceled<br />**Hex**:<br />8004F855<br />**Number**:<br />-2147157931|Because of the status transition rules, you can't cancel the case in the current status.Change the case status, and then try canceling it, or contact your system administrator.|
> |**Name**:<br />StateTransitionActiveToResolve<br />**Hex**:<br />8004F854<br />**Number**:<br />-2147157932|Because of the status transition rules, you can't resolve a case in the current status.Change the case status, and then try resolving it, or contact your system administrator.|
> |**Name**:<br />StateTransitionDeactivateNewStatus<br />**Hex**:<br />8004F858<br />**Number**:<br />-2147157928|You can't deactivate this record because of the status transition rules.Contact your system administrator.|
> |**Name**:<br />StateTransitionResolvedOrCanceledToActive<br />**Hex**:<br />8004F856<br />**Number**:<br />-2147157930|Because of the status transition rules, you can't activate the case from the current status.Contact your system administrator.|
> |**Name**:<br />StepAutomaticallyDisabled<br />**Hex**:<br />80045043<br />**Number**:<br />-2147200957|The original sdkmessageprocessingstep has been disabled and replaced.|
> |**Name**:<br />StepCountInXamlExceedsMaxAllowed<br />**Hex**:<br />80060414<br />**Number**:<br />-2147089388|There are {0} {1} in the Xaml. Max allowed is {2}.|
> |**Name**:<br />StepDoesNotHaveAnyChildInXaml<br />**Hex**:<br />80060416<br />**Number**:<br />-2147089386|{0} does not have at least one {1} as its child.|
> |**Name**:<br />StepNotSupportedForClientBusinessRule<br />**Hex**:<br />80060000<br />**Number**:<br />-2147090432|Step {0} is not supported for client side business rule.|
> |**Name**:<br />StepStepDoesNotHaveAnyControlStepAsItsChildren<br />**Hex**:<br />80060409<br />**Number**:<br />-2147089399|StepStep does not have any ControlStep as its children|
> |**Name**:<br />StoredProcedureContext<br />**Hex**:<br />8004C002<br />**Number**:<br />-2147172350|Dynamics 365 error {0} in {1}:{2}|
> |**Name**:<br />StringAttributeIndexError<br />**Hex**:<br />8004D292<br />**Number**:<br />-2147167598|One of the attributes of the selected entity is a part of database index and so it cannot be greater than 900 bytes.|
> |**Name**:<br />StringLengthTooLong<br />**Hex**:<br />80044331<br />**Number**:<br />-2147204303|A validation error occurred. A string value provided is too long.|
> |**Name**:<br />SubcomponentDoesNotExist<br />**Hex**:<br />80048537<br />**Number**:<br />-2147187401|Subcomponent {0} of type {1} is not found in the organization, it can not be added to the SolutionComponents.|
> |**Name**:<br />SubcomponentMissingARoot<br />**Hex**:<br />80048536<br />**Number**:<br />-2147187402|Subcomponent {0} cannot be added to the solution because the root component {1} is missing.|
> |**Name**:<br />SubjectDoesNotExist<br />**Hex**:<br />80043e02<br />**Number**:<br />-2147205630|Subject does not exist.|
> |**Name**:<br />SubjectLoopBeingCreated<br />**Hex**:<br />80043e01<br />**Number**:<br />-2147205631|Creating this parental association would create a loop in Subjects hierarchy.|
> |**Name**:<br />SubjectLoopExists<br />**Hex**:<br />80043e00<br />**Number**:<br />-2147205632|Loop exists in the subjects hierarchy.|
> |**Name**:<br />SubReportDoesNotExist<br />**Hex**:<br />80040493<br />**Number**:<br />-2147220333|Subreport does not exist. ReportId:{0}|
> |**Name**:<br />SubscriptionGone<br />**Hex**:<br />80072513<br />**Number**:<br />-2147015405|Subscription expired|
> |**Name**:<br />SupportLogOnExpired<br />**Hex**:<br />8004A108<br />**Number**:<br />-2147180280|Support login is expired|
> |**Name**:<br />SupportUserCannotBeCreateNorUpdated<br />**Hex**:<br />80041d41<br />**Number**:<br />-2147214015|The support user cannot be updated|
> |**Name**:<br />SyncAttributeMappingCannotBeUpdated<br />**Hex**:<br />80060741<br />**Number**:<br />-2147088575|The sync attribute mapping cannot be updated.|
> |**Name**:<br />SyncToMsdeFailure<br />**Hex**:<br />80048407<br />**Number**:<br />-2147187705|Failed to start or connect to the offline mode MSDE database.|
> |**Name**:<br />SystemAttributeMap<br />**Hex**:<br />80046205<br />**Number**:<br />-2147196411|SystemAttributeMap Error Occurred|
> |**Name**:<br />SystemEntityMap<br />**Hex**:<br />80046202<br />**Number**:<br />-2147196414|SystemEntityMap Error Occurred|
> |**Name**:<br />SystemFormCopyUnmatchedEntity<br />**Hex**:<br />8004F656<br />**Number**:<br />-2147158442|The entity for the Target and the SourceId must match.|
> |**Name**:<br />SystemFormCopyUnmatchedFormType<br />**Hex**:<br />8004F657<br />**Number**:<br />-2147158441|The form type of the SourceId is not valid for the Target entity.|
> |**Name**:<br />SystemFormCreateWithExistingLabel<br />**Hex**:<br />8004F658<br />**Number**:<br />-2147158440|The label '{0}', id: '{1}' already exists. Supply unique labelid values.|
> |**Name**:<br />SystemFormImportMissingRoles<br />**Hex**:<br />8004F655<br />**Number**:<br />-2147158443|The unmanaged solution you are importing has displaycondition XML attributes that refer to security roles that are missing from the target system. Any displaycondition attributes that refer to these security roles will be removed.|
> |**Name**:<br />SystemUserDisabled<br />**Hex**:<br />8004A112<br />**Number**:<br />-2147180270|The system user was disabled therefore the ticket expired.|
> |**Name**:<br />TamperedAuthTicket<br />**Hex**:<br />8004A105<br />**Number**:<br />-2147180283|The ticket specified for authentication has been tampered with or invalidated.|
> |**Name**:<br />TargetAttributeInvalidForIgnore<br />**Hex**:<br />80048500<br />**Number**:<br />-2147187456|Target attribute name should be empty when the processcode is ignore.|
> |**Name**:<br />TargetAttributeInvalidForMap<br />**Hex**:<br />80040394<br />**Number**:<br />-2147220588|This attribute is not valid for mapping.|
> |**Name**:<br />TargetAttributeNotFound<br />**Hex**:<br />80040392<br />**Number**:<br />-2147220590|The file specifies an attribute that does not exist in Microsoft Dynamics 365.|
> |**Name**:<br />TargetEntityInvalidForMap<br />**Hex**:<br />80040395<br />**Number**:<br />-2147220587|The file specifies an entity that is not valid for data migration.|
> |**Name**:<br />TargetEntityNotFound<br />**Hex**:<br />80040391<br />**Number**:<br />-2147220591|The file specifies an entity that does not exist in Microsoft Dynamics 365.|
> |**Name**:<br />TargetEntityNotMapped<br />**Hex**:<br />80048460<br />**Number**:<br />-2147187616|Target Entity Name not defined for source:{0} file.|
> |**Name**:<br />TargetUserInsufficientPrivileges<br />**Hex**:<br />80048342<br />**Number**:<br />-2147187902|The user can't be added to the team because the user doesn't have the "{0}" privilege.|
> |**Name**:<br />TaskFlowEmptyName<br />**Hex**:<br />80061712<br />**Number**:<br />-2147084526|The name field cannot be empty. Please enter a name.|
> |**Name**:<br />TaskFlowEntityAttributeIsNotValid<br />**Hex**:<br />80061717<br />**Number**:<br />-2147084521|Invalid attribute type: {0}.{1}.|
> |**Name**:<br />TaskFlowEntityRelationshipIsNotValid<br />**Hex**:<br />80061716<br />**Number**:<br />-2147084522|Invalid relationship type: {0}.|
> |**Name**:<br />TaskFlowFormXmlNotFound<br />**Hex**:<br />80061713<br />**Number**:<br />-2147084525|Could not find the system form {0} for Task flow {1}.|
> |**Name**:<br />TaskFlowInvalidCharactersInName<br />**Hex**:<br />80061711<br />**Number**:<br />-2147084527|The name field can only contain alphanumeric characters.|
> |**Name**:<br />TaskFlowMaxNumberControls<br />**Hex**:<br />80061719<br />**Number**:<br />-2147084519|The task flow has exceeded the maximum number of controls allowed ({0}). To continue, you need to remove some controls.|
> |**Name**:<br />TaskFlowMaxNumberPages<br />**Hex**:<br />80061718<br />**Number**:<br />-2147084520|The task flow has exceeded the maximum number of pages allowed ({0}). To continue, you need to remove some pages.|
> |**Name**:<br />TaskFlowNameIsNotUnique<br />**Hex**:<br />80061710<br />**Number**:<br />-2147084528|A task flow with the specified name already exists.  Please specify a unique name.|
> |**Name**:<br />TaskFlowNotFound<br />**Hex**:<br />80061720<br />**Number**:<br />-2147084512|A Task Flow which is trying to launch is not available on this device. You may not have permission to access it or it may not be available on your organization. Please contact your system administrator.|
> |**Name**:<br />TaskFlowNotValid<br />**Hex**:<br />8006172F<br />**Number**:<br />-2147084497|Task flow definition is invalid.|
> |**Name**:<br />TaskFlowPageMissingFormXmlTab<br />**Hex**:<br />80061714<br />**Number**:<br />-2147084524|Could not find the pages {0} for Task flow {1} Step {2}.|
> |**Name**:<br />TaskFlowUnsupportedEntities<br />**Hex**:<br />80061715<br />**Number**:<br />-2147084523|The following entities are not enabled for Task flows: {0}.|
> |**Name**:<br />TeamAdministratorMissedPrivilege<br />**Hex**:<br />80041d0a<br />**Number**:<br />-2147214070|The team administrator does not have privilege read team.|
> |**Name**:<br />TeamInWrongBusiness<br />**Hex**:<br />8004140d<br />**Number**:<br />-2147216371|The team with id={0} belongs to a different business unit={1} than the role with roleId={2} and roleBusinessUnit={3}.|
> |**Name**:<br />TeamNameTooLong<br />**Hex**:<br />80048305<br />**Number**:<br />-2147187963|The specified name for the team is too long.|
> |**Name**:<br />TeamNotAssignedRoles<br />**Hex**:<br />80042f0a<br />**Number**:<br />-2147209462|The team has not been assigned any roles.|
> |**Name**:<br />TemplateNotAllowedForInternetMarketing<br />**Hex**:<br />80048475<br />**Number**:<br />-2147187595|Creating Templates with Internet Marketing Campaign Activities is not allowed|
> |**Name**:<br />TemplateTypeNotSupportedForUnsubscribeAcknowledgement<br />**Hex**:<br />80040324<br />**Number**:<br />-2147220700|This template type is not supported for unsubscribe acknowledgement.|
> |**Name**:<br />TenantIDIsEmpty<br />**Hex**:<br />8005E25A<br />**Number**:<br />-2147098022|Exchange Online Tenant ID field cannot be empty.|
> |**Name**:<br />TenantIDValueChanged<br />**Hex**:<br />8005E25C<br />**Number**:<br />-2147098020|The detected tenantId for your exchange is different than the once you saved.|
> |**Name**:<br />TestEmailConfigurationScheduledInProgress<br />**Hex**:<br />8005E248<br />**Number**:<br />-2147098040|Test email configuration scheduled is in progress. Please save after completion of test.|
> |**Name**:<br />TextAnalyticsAPIActiveConfigurationDoesNotExist<br />**Hex**:<br />80061690<br />**Number**:<br />-2147084656|Active configuration does not exist for entity.|
> |**Name**:<br />TextAnalyticsAPIActiveSimilarityConfigurationDoesNotExist<br />**Hex**:<br />80061695<br />**Number**:<br />-2147084651|No active similarity rule exists. The system administrator must set up a similarity rule configuration.|
> |**Name**:<br />TextAnalyticsAPIAllowedOnlyForEnglishLanguage<br />**Hex**:<br />80061691<br />**Number**:<br />-2147084655|Text Analytics feature is available for organizations with base language as English.|
> |**Name**:<br />TextAnalyticsAPIAzureUnableToConnectWithBuild<br />**Hex**:<br />80061692<br />**Number**:<br />-2147084654|Dynamics 365 failed to connect with the Azure text analytics service. Verify that the service URI and account key are valid, and the Azure subscription is active.|
> |**Name**:<br />TextAnalyticsAzureConnectionCascadeActivateFailed<br />**Hex**:<br />80061634<br />**Number**:<br />-2147084748|One or more text analytics models couldn't be activated. Try activating the existing text analytics models separately from the Azure service connection.|
> |**Name**:<br />TextAnalyticsAzureConnectionFailed<br />**Hex**:<br />80061650<br />**Number**:<br />-2147084720|Unable to connect to Text Analytics API.|
> |**Name**:<br />TextAnalyticsAzureSchedulerError<br />**Hex**:<br />80061693<br />**Number**:<br />-2147084653|Dynamics 365 failed to connect with the Azure text analytics service. Please try again and if the problem persists contact your system administrator.|
> |**Name**:<br />TextAnalyticsAzureTestConnectionFailed<br />**Hex**:<br />80061632<br />**Number**:<br />-2147084750|Failed to connect to the Azure Text Analytics service. Check that the service URL and the Azure account key are valid and the service subscription is active.|
> |**Name**:<br />TextAnalyticsAzureUnableToConnectWithBuild<br />**Hex**:<br />80061655<br />**Number**:<br />-2147084715|Dynamics 365 failed to connect with the Azure text analytics service. Verify that the service URI and account key are valid, and the Azure subscription is active.|
> |**Name**:<br />TextAnalyticsFeatureNotEnabled<br />**Hex**:<br />80061652<br />**Number**:<br />-2147084718|The Azure Text Analytics feature isn’t activated. The system administrator must activate this feature and set up the required configuration.|
> |**Name**:<br />TextAnalyticsMappingUsedForActiveConfiguration<br />**Hex**:<br />80061667<br />**Number**:<br />-2147084697|This text analytics entity mapping is used for an active configuration. It can’t be modified or deleted while it is used by an active config.|
> |**Name**:<br />TextAnalyticsMaxLimitForTopicModelReached<br />**Hex**:<br />80061694<br />**Number**:<br />-2147084652|Maximum number of topic models allowed for your organization has been reached.|
> |**Name**:<br />TextAnalyticsModelActivateConnectionMustBeActive<br />**Hex**:<br />80061657<br />**Number**:<br />-2147084713|The Azure Machine Learning Text Analytics service connection must be activated before the model can be activated. Please activate the text analytics service connection and try again.|
> |**Name**:<br />ThemeIdOrUpdateTimestampIsNull<br />**Hex**:<br />800608D1<br />**Number**:<br />-2147088175|Theme Id or Update Timestamp value is not present in theme data.|
> |**Name**:<br />Throttling<br />**Hex**:<br />8005F103<br />**Number**:<br />-2147094269|Too many requests.|
> |**Name**:<br />ThrottlingBurstRequestLimitExceededError<br />**Hex**:<br />80072322<br />**Number**:<br />-2147015902|Number of requests exceeded the limit of {0} over time window of {1} seconds.|
> |**Name**:<br />ThrottlingConcurrencyLimitExceededError<br />**Hex**:<br />80072326<br />**Number**:<br />-2147015898|Number of concurrent requests exceeded the limit of {0}.|
> |**Name**:<br />ThrottlingTimeExceededError<br />**Hex**:<br />80072321<br />**Number**:<br />-2147015903|Combined execution time of incoming requests exceeded limit of {0} milliseconds over time window of {1} seconds. Decrease number of concurrent requests or reduce the duration of requests and try again later.|
> |**Name**:<br />TooManyBytesInInputStream<br />**Hex**:<br />8004F901<br />**Number**:<br />-2147157759|The stream being read from has too many bytes.|
> |**Name**:<br />TooManyCalculatedFieldsInQuery<br />**Hex**:<br />80060429<br />**Number**:<br />-2147089367|Number of calculated fields in query exceeded maximum limit of {0}.|
> |**Name**:<br />TooManyConditionParametersInQuery<br />**Hex**:<br />8004430E<br />**Number**:<br />-2147204338|Number of parameters in a condition exceeded maximum limit.|
> |**Name**:<br />TooManyConditionsInQuery<br />**Hex**:<br />8004430C<br />**Number**:<br />-2147204340|Number of conditions in query exceeded maximum limit.|
> |**Name**:<br />TooManyEntitiesEnabledForAutoCreatedAccessTeams<br />**Hex**:<br />80048332<br />**Number**:<br />-2147187918|Too many entities enabled for auto created access teams.|
> |**Name**:<br />TooManyLinkEntitiesInQuery<br />**Hex**:<br />8004430D<br />**Number**:<br />-2147204339|Number of link entities in query exceeded maximum limit.|
> |**Name**:<br />TooManyMultiSelectConditionParametersInQuery<br />**Hex**:<br />80050223<br />**Number**:<br />-2147155421|Number of multiselect condition parameters in query exceeded maximum limit: {0}.|
> |**Name**:<br />TooManyPicklistValues<br />**Hex**:<br />80048492<br />**Number**:<br />-2147187566|Number of distinct picklist values exceed the limit.|
> |**Name**:<br />TooManyRecipients<br />**Hex**:<br />8004350e<br />**Number**:<br />-2147207922|Sending to multiple recipients is not supported.|
> |**Name**:<br />TooManySelectionsForAttributeType<br />**Hex**:<br />80050222<br />**Number**:<br />-2147155422|Number of selections for MultiSelectPicklist Attribute Type exceeded maximum limit: {0}.|
> |**Name**:<br />TooManyTeamTemplatesForEntityAccessTeams<br />**Hex**:<br />80048333<br />**Number**:<br />-2147187917|Current number of teams: {0} is greater than teams limit: {1} for entity with ObjectTypeCode {2}|
> |**Name**:<br />TopicModelActivateWithInvalidConfiguration<br />**Hex**:<br />80061656<br />**Number**:<br />-2147084714|The configuration used for the build is invalid. Topic determination fields are required for the configuration used for topic analysis.|
> |**Name**:<br />TopicModelConfigurationAssociatedModelAlreadyActive<br />**Hex**:<br />80061670<br />**Number**:<br />-2147084688|Cannot update or delete topic model configuration because it is associated with an active topic model.|
> |**Name**:<br />TopicModelConfigurationUsedEmpty<br />**Hex**:<br />80061653<br />**Number**:<br />-2147084717|Activation requires specifying the build configuration. Specify the configuration used for the build before activation.|
> |**Name**:<br />TopicModelScheduleBuildSettingsEmpty<br />**Hex**:<br />80061651<br />**Number**:<br />-2147084719|Activation requires setting the build schedule. Specify the schedule build settings before activation.|
> |**Name**:<br />TopicModelTestWithoutConfiguration<br />**Hex**:<br />80061654<br />**Number**:<br />-2147084716|Specify the configuration used for the build.|
> |**Name**:<br />TraceMessageConstructionError<br />**Hex**:<br />8004F900<br />**Number**:<br />-2147157760|The trace record has an invalid trace code or an insufficient number of trace parameters.|
> |**Name**:<br />TransactionAborted<br />**Hex**:<br />80040255<br />**Number**:<br />-2147220907|Transaction Aborted.|
> |**Name**:<br />TransactionNotCommited<br />**Hex**:<br />80040252<br />**Number**:<br />-2147220910|Transaction not committed.|
> |**Name**:<br />TransactionNotStarted<br />**Hex**:<br />80040251<br />**Number**:<br />-2147220911|Transaction not started.|
> |**Name**:<br />TransactionNotSupported<br />**Hex**:<br />8005E007<br />**Number**:<br />-2147098617|The operation that you are trying to perform does not support transactions.|
> |**Name**:<br />TransformationResumeNotSupported<br />**Hex**:<br />80048463<br />**Number**:<br />-2147187613|The resume/retry of Transformation job of Import is not supported.|
> |**Name**:<br />TransformMustBeCalledBeforeImport<br />**Hex**:<br />80040335<br />**Number**:<br />-2147220683|Cannot call import before transform.|
> |**Name**:<br />TranslateArticle_OnlyPrimaryArticlesCanBeTranslated<br />**Hex**:<br />80061402<br />**Number**:<br />-2147085310|This article is a translation of the original article. It cannot be translated again. If you want another translation, start with the original article rather than this one.|
> |**Name**:<br />TranslateArticle_TranslationCanNotBeCreatedForTheSameLanguage<br />**Hex**:<br />80061403<br />**Number**:<br />-2147085309|A translation for this language already exists for this version of the article|
> |**Name**:<br />TrendingDocumentsDataRetrievalFailure<br />**Hex**:<br />80044234<br />**Number**:<br />-2147204556|We can't get to the trending documents. Try again later.|
> |**Name**:<br />TrendingDocumentsIntegrationDisabledError<br />**Hex**:<br />80044233<br />**Number**:<br />-2147204557|Trending Documents is disabled for your Microsoft Dynamics 365 account.|
> |**Name**:<br />TrendingDocumentsIntegrationTurnedOffError<br />**Hex**:<br />80044255<br />**Number**:<br />-2147204523|Trending Documents is turned off. Please contact your system administrator to turn this feature on in System Settings.|
> |**Name**:<br />TrendingDocumentsOfflineModeError<br />**Hex**:<br />80044258<br />**Number**:<br />-2147204520|Trending Documents isn't available in offline mode.|
> |**Name**:<br />TrendingDocumentsOnpremiseDeploymentError<br />**Hex**:<br />80044232<br />**Number**:<br />-2147204558|The Trending Documents dashboard component isn't supported by your company's Microsoft Office service.|
> |**Name**:<br />TriggerFlowFailure<br />**Hex**:<br />80050261<br />**Number**:<br />-2147155359|An error has occurred when trying to run this flow.|
> |**Name**:<br />TypeNotSetToDefinition<br />**Hex**:<br />80060402<br />**Number**:<br />-2147089406|Type should be set to Definition while creating business process flow category|
> |**Name**:<br />UIDataGenerationFailed<br />**Hex**:<br />80045037<br />**Number**:<br />-2147200969|There was an error generating the UIData from XAML.|
> |**Name**:<br />UIDataMissingInWorkflow<br />**Hex**:<br />80048471<br />**Number**:<br />-2147187599|The workflow does not contain UIData.|
> |**Name**:<br />UIScriptIdentifierDuplicate<br />**Hex**:<br />8004F217<br />**Number**:<br />-2147159529|A variable or input argument with the same name already exists. Choose a different name, and try again.|
> |**Name**:<br />UIScriptIdentifierInvalid<br />**Hex**:<br />8004F218<br />**Number**:<br />-2147159528|The variable or input argument name is invalid. The name can only contain '_', numerical, and alphabetical characters. Choose a different name, and try again.|
> |**Name**:<br />UIScriptIdentifierInvalidLength<br />**Hex**:<br />8004F219<br />**Number**:<br />-2147159527|The variable or input argument name is too long. Choose a smaller name, and try again.|
> |**Name**:<br />UnableToActivateQuoteNotInDraft<br />**Hex**:<br />80100003<br />**Number**:<br />-2146435069|The quote cannot be activated because it is not in draft state.|
> |**Name**:<br />UnableToLoadCustomActivity<br />**Hex**:<br />8004505A<br />**Number**:<br />-2147200934|Unable to load the custom activity.|
> |**Name**:<br />UnableToLoadPluginAssembly<br />**Hex**:<br />80044191<br />**Number**:<br />-2147204719|Unable to load plug-in assembly.|
> |**Name**:<br />UnableToLoadPluginType<br />**Hex**:<br />80044190<br />**Number**:<br />-2147204720|Unable to load plug-in type.|
> |**Name**:<br />UnableToLoadTransformationAssembly<br />**Hex**:<br />80040378<br />**Number**:<br />-2147220616|Unable to load the transformation assembly.|
> |**Name**:<br />UnableToLoadTransformationType<br />**Hex**:<br />80040379<br />**Number**:<br />-2147220615|Unable to load the transformation type.|
> |**Name**:<br />UnableToLogOnUserFromUserNameAndPassword<br />**Hex**:<br />80044311<br />**Number**:<br />-2147204335|The specified user name and password can not logon.|
> |**Name**:<br />UnableToSendEmail<br />**Hex**:<br />8004B015<br />**Number**:<br />-2147176427|Some Internal error occurred in sending invitation, Please try again later|
> |**Name**:<br />UnapprovedMailbox<br />**Hex**:<br />8005E220<br />**Number**:<br />-2147098080|The mailbox is not in approved state. Send/Receive mails are allowed only for approved mailboxes.|
> |**Name**:<br />UnauthorizedAccess<br />**Hex**:<br />80040277<br />**Number**:<br />-2147220873|Attempted to perform an unauthorized operation.|
> |**Name**:<br />UnExpected<br />**Hex**:<br />80040216<br />**Number**:<br />-2147220970|An unexpected error occurred.|
> |**Name**:<br />UnexpectedErrorInMailMerge<br />**Hex**:<br />80040330<br />**Number**:<br />-2147220688|There was an unexpected error during mail merge.|
> |**Name**:<br />UnexpectedNullReferenceError<br />**Hex**:<br />8004F044<br />**Number**:<br />-2147159996|Unexpected null reference error: {0}.|
> |**Name**:<br />UnexpectedRightOperandCount<br />**Hex**:<br />80060006<br />**Number**:<br />-2147090426|The right operand array in the expression contain unexpected no. of operand.|
> |**Name**:<br />UnitDoesNotExist<br />**Hex**:<br />80043b1b<br />**Number**:<br />-2147206373|The unit does not exist.|
> |**Name**:<br />UnitLoopBeingCreated<br />**Hex**:<br />80043b1a<br />**Number**:<br />-2147206374|Using this base unit would create a loop in the unit hierarchy.|
> |**Name**:<br />UnitLoopExists<br />**Hex**:<br />80043b19<br />**Number**:<br />-2147206375|Loop exists in the unit hierarchy.|
> |**Name**:<br />UnitNoName<br />**Hex**:<br />80043b26<br />**Number**:<br />-2147206362|The unit name cannot be null.|
> |**Name**:<br />UnitNotInSchedule<br />**Hex**:<br />80043b16<br />**Number**:<br />-2147206378|The unit does not exist in the specified unit schedule.|
> |**Name**:<br />UnknownInvalidTransformationParameterGeneric<br />**Hex**:<br />80048513<br />**Number**:<br />-2147187437|One or more input transformation parameter values are invalid: {0}.|
> |**Name**:<br />unManagedchildentityisnotchild<br />**Hex**:<br />800404e6<br />**Number**:<br />-2147220250|The child entity supplied is not a child.|
> |**Name**:<br />unManagedcihldofconditionforoffilefilters<br />**Hex**:<br />800404a9<br />**Number**:<br />-2147220311|Child-of condition is only allowed on offline filters.|
> |**Name**:<br />UnmanagedComponentParentsManagedComponent<br />**Hex**:<br />8004803B<br />**Number**:<br />-2147188677|Found {0} dependency records where unmanaged component is the parent of a managed component. First record (dependentcomponentobjectid = {1}, type = {2}, requiredcomponentobjectid = {3}, type= {4}, solution = {5}).|
> |**Name**:<br />unManagedemptyprocessliteralcondition<br />**Hex**:<br />800404b0<br />**Number**:<br />-2147220304|No data specified for ProcessLiteralCondition.|
> |**Name**:<br />unManagedentityisnotintersect<br />**Hex**:<br />800404aa<br />**Number**:<br />-2147220310|The entity is not an intersect entity.|
> |**Name**:<br />unManagederroraddingfiltertoqueryplan<br />**Hex**:<br />800404ca<br />**Number**:<br />-2147220278|An error occurred adding a filter to the query plan.|
> |**Name**:<br />unManagederrorprocessingfilternodes<br />**Hex**:<br />800404c4<br />**Number**:<br />-2147220284|An unexpected error occurred processing the filter nodes.|
> |**Name**:<br />unManagedfieldnotvalidatedbyplatform<br />**Hex**:<br />800404ae<br />**Number**:<br />-2147220306|A field was not validated by the platform.|
> |**Name**:<br />unManagedfilterindexoutofrange<br />**Hex**:<br />800404ab<br />**Number**:<br />-2147220309|The filter index is out of range.|
> |**Name**:<br />unManagedIdsAccessDenied<br />**Hex**:<br />80048306<br />**Number**:<br />-2147187962|Not enough privilege to access the Microsoft Dynamics 365 object or perform the requested operation.|
> |**Name**:<br />unManagedidsaccounthaschildopportunities<br />**Hex**:<br />80040511<br />**Number**:<br />-2147220207|The Account has child opportunities.|
> |**Name**:<br />unManagedidsactivitydurationdoesnotmatch<br />**Hex**:<br />8004350a<br />**Number**:<br />-2147207926|Activity duration does not match start/end time|
> |**Name**:<br />unManagedidsactivityinvalidduration<br />**Hex**:<br />80043509<br />**Number**:<br />-2147207927|Invalid activity duration|
> |**Name**:<br />unManagedidsactivityinvalidobjecttype<br />**Hex**:<br />80043503<br />**Number**:<br />-2147207933|Activity regarding object type is invalid|
> |**Name**:<br />unManagedidsactivityinvalidpartyobjecttype<br />**Hex**:<br />80043505<br />**Number**:<br />-2147207931|Activity party object type is invalid|
> |**Name**:<br />unManagedidsactivityinvalidregardingobject<br />**Hex**:<br />80043507<br />**Number**:<br />-2147207929|Invalid activity regarding object, it probably does not exist|
> |**Name**:<br />unManagedidsactivityinvalidstate<br />**Hex**:<br />80043500<br />**Number**:<br />-2147207936|Invalid activity state|
> |**Name**:<br />unManagedidsactivityinvalidtimeformat<br />**Hex**:<br />80043508<br />**Number**:<br />-2147207928|Invalid activity time, check format|
> |**Name**:<br />unManagedidsactivityinvalidtype<br />**Hex**:<br />80043501<br />**Number**:<br />-2147207935|Invalid activity type code|
> |**Name**:<br />unManagedidsactivitynotroutable<br />**Hex**:<br />8004350b<br />**Number**:<br />-2147207925|This type of activity is not routable|
> |**Name**:<br />unManagedidsactivityobjectidortypemissing<br />**Hex**:<br />80043502<br />**Number**:<br />-2147207934|Activity regarding object Id or type is missing|
> |**Name**:<br />unManagedidsactivitypartyobjectidortypemissing<br />**Hex**:<br />80043504<br />**Number**:<br />-2147207932|Activity party object Id or type is missing|
> |**Name**:<br />unManagedidsanonymousenabled<br />**Hex**:<br />80040226<br />**Number**:<br />-2147220954|The logged-in user was not found in the Active Directory.|
> |**Name**:<br />unManagedidsarticletemplatecontainsarticles<br />**Hex**:<br />80043e05<br />**Number**:<br />-2147205627|Cannot change article template because there are knowledge base articles using it.|
> |**Name**:<br />unManagedidsarticletemplateisnotactive<br />**Hex**:<br />80043e07<br />**Number**:<br />-2147205625|KB article template is inactive.|
> |**Name**:<br />unManagedidsattachmentcannotcreatetempfile<br />**Hex**:<br />80044a05<br />**Number**:<br />-2147202555|Cannot create temporary attachment file.|
> |**Name**:<br />unManagedidsattachmentcannotgetfilesize<br />**Hex**:<br />80044a01<br />**Number**:<br />-2147202559|Cannot get temporary attachment file size.|
> |**Name**:<br />unManagedidsattachmentcannotopentempfile<br />**Hex**:<br />80044a00<br />**Number**:<br />-2147202560|Cannot open temporary attachment file.|
> |**Name**:<br />unManagedidsattachmentcannotreadtempfile<br />**Hex**:<br />80044a03<br />**Number**:<br />-2147202557|Cannot read temporary attachment file.|
> |**Name**:<br />unManagedidsattachmentcannottruncatetempfile<br />**Hex**:<br />80044a07<br />**Number**:<br />-2147202553|Cannot truncate temporary attachment file.|
> |**Name**:<br />unManagedidsattachmentcannotunmaptempfile<br />**Hex**:<br />80044a06<br />**Number**:<br />-2147202554|Cannot unmap temporary attachment file.|
> |**Name**:<br />unManagedidsattachmentinvalidfilesize<br />**Hex**:<br />80044a02<br />**Number**:<br />-2147202558|Attachment file size is too big.|
> |**Name**:<br />unManagedidsattachmentisempty<br />**Hex**:<br />80044a04<br />**Number**:<br />-2147202556|Attachment is empty.|
> |**Name**:<br />unManagedidsbizmgmtbusinessparentdiffmerchant<br />**Hex**:<br />80041d04<br />**Number**:<br />-2147214076|The business is not in the same merchant as parent business.|
> |**Name**:<br />unManagedidsbizmgmtcallernotinpartnerbusiness<br />**Hex**:<br />80041d14<br />**Number**:<br />-2147214060|The caller is not from partner business.|
> |**Name**:<br />unManagedidsbizmgmtcallernotinprimarybusiness<br />**Hex**:<br />80041d12<br />**Number**:<br />-2147214062|The caller is not from primary business.|
> |**Name**:<br />unManagedidsbizmgmtcannotaddlocaluser<br />**Hex**:<br />80041d32<br />**Number**:<br />-2147214030|A local user cannot be added to the Dynamics 365.|
> |**Name**:<br />unManagedidsbizmgmtcannotdeletebusiness<br />**Hex**:<br />80041d18<br />**Number**:<br />-2147214056|This is a sub-business. Use IBizMerchant::Delete to delete this sub-business.|
> |**Name**:<br />unManagedidsbizmgmtcannotdeleteprovision<br />**Hex**:<br />80041d19<br />**Number**:<br />-2147214055|This is a provisioned root-business. Use IBizProvision::Delete to delete this root-business.|
> |**Name**:<br />unManagedidsbizmgmtcannotdisablebusiness<br />**Hex**:<br />80041d1a<br />**Number**:<br />-2147214054|This business unit cannot be disabled.|
> |**Name**:<br />unManagedidsbizmgmtcannotdisableprovision<br />**Hex**:<br />80041d1b<br />**Number**:<br />-2147214053|This is a provisioned root-business. Use IBizProvision::Disable to disable this root-business.|
> |**Name**:<br />unManagedidsbizmgmtcannotenablebusiness<br />**Hex**:<br />80041d1c<br />**Number**:<br />-2147214052|This is a sub-business. Use IBizMerchant::Enable to enable this sub-business.|
> |**Name**:<br />unManagedidsbizmgmtcannotenableprovision<br />**Hex**:<br />80041d1d<br />**Number**:<br />-2147214051|This is a provisioned root-business. Use IBizProvision::Enable to enable this root-business.|
> |**Name**:<br />unManagedidsbizmgmtcannotmovedefaultuser<br />**Hex**:<br />80041d05<br />**Number**:<br />-2147214075|unManagedidsbizmgmtcannotmovedefaultuser|
> |**Name**:<br />unManagedidsbizmgmtcannotreadaccountcontrol<br />**Hex**:<br />80041d2d<br />**Number**:<br />-2147214035|Insufficient permissions to the specified Active Directory user. Contact your System Administrator.|
> |**Name**:<br />unManagedidsbizmgmtcannotremovepartnershipdefaultuser<br />**Hex**:<br />80041d17<br />**Number**:<br />-2147214057|The default user of a partnership can not be removed.|
> |**Name**:<br />unManagedidsbizmgmtcantchangeorgname<br />**Hex**:<br />80041d36<br />**Number**:<br />-2147214026|The organization name cannot be changed.|
> |**Name**:<br />unManagedidsbizmgmtdefaultusernotinbusiness<br />**Hex**:<br />80041d03<br />**Number**:<br />-2147214077|The default user is not in the business.|
> |**Name**:<br />unManagedidsbizmgmtdefaultusernotinpartnerbusiness<br />**Hex**:<br />80041d15<br />**Number**:<br />-2147214059|The default user is not from partner business.|
> |**Name**:<br />unManagedidsbizmgmtdefaultusernotinprimarybusiness<br />**Hex**:<br />80041d13<br />**Number**:<br />-2147214061|The default user is not from primary business.|
> |**Name**:<br />unManagedidsbizmgmtmissbusinessname<br />**Hex**:<br />80041d00<br />**Number**:<br />-2147214080|The business name was unexpectedly missing.|
> |**Name**:<br />unManagedidsbizmgmtmissparentbusiness<br />**Hex**:<br />80041d02<br />**Number**:<br />-2147214078|The parent business was unexpectedly missing.|
> |**Name**:<br />unManagedidsbizmgmtmisspartnerbusiness<br />**Hex**:<br />80041d0f<br />**Number**:<br />-2147214065|The partnership partner business was unexpectedly missing.|
> |**Name**:<br />unManagedidsbizmgmtmissprimarybusiness<br />**Hex**:<br />80041d0e<br />**Number**:<br />-2147214066|The partnership primary business was unexpectedly missing.|
> |**Name**:<br />unManagedidsbizmgmtmissuserdomainname<br />**Hex**:<br />80041d01<br />**Number**:<br />-2147214079|The user's domain name was unexpectedly missing.|
> |**Name**:<br />unManagedidsbizmgmtnoparentbusiness<br />**Hex**:<br />80041d29<br />**Number**:<br />-2147214039|The specified business does not have a parent business.|
> |**Name**:<br />unManagedidsbizmgmtpartnershipalreadyexists<br />**Hex**:<br />80041d11<br />**Number**:<br />-2147214063|A partnership between specified primary business and partner business already exists.|
> |**Name**:<br />unManagedidsbizmgmtpartnershipnotinpendingstatus<br />**Hex**:<br />80041d16<br />**Number**:<br />-2147214058|The partnership has been accepted or declined.|
> |**Name**:<br />unManagedidsbizmgmtprimarysameaspartner<br />**Hex**:<br />80041d10<br />**Number**:<br />-2147214064|The primary business is the same as partner business.|
> |**Name**:<br />unManagedidsbizmgmtusercannotbeownparent<br />**Hex**:<br />80041d06<br />**Number**:<br />-2147214074|The user can not be its own parent user.|
> |**Name**:<br />unManagedidsbizmgmtuserdoesnothaveparent<br />**Hex**:<br />80041d1e<br />**Number**:<br />-2147214050|This user does not have a parent user.|
> |**Name**:<br />unManagedidsbizmgmtusersettingsnotcreated<br />**Hex**:<br />80041d2b<br />**Number**:<br />-2147214037|The specified user's settings have not yet been created.|
> |**Name**:<br />unManagedidscalendarinvalidcalendar<br />**Hex**:<br />80044d00<br />**Number**:<br />-2147201792|The calendar is invalid.|
> |**Name**:<br />unManagedidscalendarruledoesnotexist<br />**Hex**:<br />80045100<br />**Number**:<br />-2147200768|The calendar rule does not exist.|
> |**Name**:<br />unManagedidsCalloutException<br />**Hex**:<br />80045f05<br />**Number**:<br />-2147197179|Callout code throws exception|
> |**Name**:<br />unManagedidscalloutinvalidconfig<br />**Hex**:<br />80045f03<br />**Number**:<br />-2147197181|Invalid callout configuration|
> |**Name**:<br />unManagedidscalloutinvalidevent<br />**Hex**:<br />80045f04<br />**Number**:<br />-2147197180|Invalid callout event|
> |**Name**:<br />unManagedidscalloutisvabort<br />**Hex**:<br />80045f01<br />**Number**:<br />-2147197183|Callout ISV code aborted the operation|
> |**Name**:<br />unManagedidscalloutisvexception<br />**Hex**:<br />80045f00<br />**Number**:<br />-2147197184|Callout ISV code throws exception|
> |**Name**:<br />unManagedidscalloutisvstop<br />**Hex**:<br />80045f02<br />**Number**:<br />-2147197182|Callout ISV code stopped the operation|
> |**Name**:<br />unManagedidscannotassigntobusiness<br />**Hex**:<br />80040221<br />**Number**:<br />-2147220959|Cannot assign an object to a merchant.|
> |**Name**:<br />unManagedidscannotdeactivatepricelevel<br />**Hex**:<br />80043b04<br />**Number**:<br />-2147206396|The price level cannot be deactivated because it is the default price level of an account, contact or product.|
> |**Name**:<br />unManagedidscannotdefaultprivateview<br />**Hex**:<br />80040238<br />**Number**:<br />-2147220936|Private views cannot be default.|
> |**Name**:<br />unManagedidscannotgrantorrevokeaccesstobusiness<br />**Hex**:<br />8004021e<br />**Number**:<br />-2147220962|Cannot grant or revoke access rights to a merchant.|
> |**Name**:<br />unManagedidscantdisable<br />**Hex**:<br />80044154<br />**Number**:<br />-2147204780|The user cannot be disabled because they have workflow rules running under their context.|
> |**Name**:<br />unManagedidscascadeemptylinkerror<br />**Hex**:<br />80045602<br />**Number**:<br />-2147199486|The relationship link is empty|
> |**Name**:<br />unManagedidscascadeinconsistencyerror<br />**Hex**:<br />80045600<br />**Number**:<br />-2147199488|Cascade map information is inconsistent.|
> |**Name**:<br />unManagedidscascadeundefinedrelationerror<br />**Hex**:<br />80045601<br />**Number**:<br />-2147199487|Relationship type is not supported|
> |**Name**:<br />unManagedidscascadeunexpectederror<br />**Hex**:<br />80045603<br />**Number**:<br />-2147199485|Unexpected error occurred in cascading operation|
> |**Name**:<br />unManagedidscommunicationsbadsender<br />**Hex**:<br />80040b01<br />**Number**:<br />-2147218687|More than one sender specified|
> |**Name**:<br />unManagedidscommunicationsnoparticipationmask<br />**Hex**:<br />80040b06<br />**Number**:<br />-2147218682|Participation type is missing from an activity|
> |**Name**:<br />unManagedidscommunicationsnopartyaddress<br />**Hex**:<br />80040b00<br />**Number**:<br />-2147218688|Object address not found on party or party is marked as non-emailable|
> |**Name**:<br />unManagedidscommunicationsnorecipients<br />**Hex**:<br />80040b05<br />**Number**:<br />-2147218683|At least one system user or queue in the organization must be a recipient|
> |**Name**:<br />unManagedidscommunicationsnosender<br />**Hex**:<br />80040b02<br />**Number**:<br />-2147218686|No email address was specified, and the calling user does not have an email address set|
> |**Name**:<br />unManagedidscommunicationsnosenderaddress<br />**Hex**:<br />80040b08<br />**Number**:<br />-2147218680|The sender does not have an email address on the party record|
> |**Name**:<br />unManagedidscommunicationstemplateinvalidtemplate<br />**Hex**:<br />80040b07<br />**Number**:<br />-2147218681|The template body is invalid|
> |**Name**:<br />unManagedidscontacthaschildopportunities<br />**Hex**:<br />80040512<br />**Number**:<br />-2147220206|The Contact has child opportunities.|
> |**Name**:<br />unManagedidscontractaccountmissing<br />**Hex**:<br />80043201<br />**Number**:<br />-2147208703|Account is required to save a contract.|
> |**Name**:<br />unManagedidscontractdoesnotexist<br />**Hex**:<br />80043207<br />**Number**:<br />-2147208697|The contract does not exist.|
> |**Name**:<br />unManagedidscontractinvalidowner<br />**Hex**:<br />80043212<br />**Number**:<br />-2147208686|The owner of the contract is invalid.|
> |**Name**:<br />unManagedidscontractinvalidstartdateforrenewedcontract<br />**Hex**:<br />80043217<br />**Number**:<br />-2147208681|The start date of the renewed contract can not be earlier than the end date of the originating contract.|
> |**Name**:<br />unManagedidscontractinvalidtotalallotments<br />**Hex**:<br />80043214<br />**Number**:<br />-2147208684|The totalallotments is invalid.|
> |**Name**:<br />unManagedidscontractlineitemdoesnotexist<br />**Hex**:<br />80043208<br />**Number**:<br />-2147208696|The contract line item does not exist.|
> |**Name**:<br />unManagedidscontractopencasesexist<br />**Hex**:<br />8004320a<br />**Number**:<br />-2147208694|There are open cases against this contract line item.|
> |**Name**:<br />unManagedidscontracttemplateabbreviationexists<br />**Hex**:<br />80043216<br />**Number**:<br />-2147208682|The value for abbreviation already exists.|
> |**Name**:<br />unManagedidscontractunexpected<br />**Hex**:<br />80043200<br />**Number**:<br />-2147208704|An unexpected error occurred in Contracts.|
> |**Name**:<br />unManagedidscpbadpassword<br />**Hex**:<br />80042901<br />**Number**:<br />-2147211007|Incorrect password for the specified customer portal user.|
> |**Name**:<br />unManagedidscpdecryptfailed<br />**Hex**:<br />80042903<br />**Number**:<br />-2147211005|Decryption of the password failed.|
> |**Name**:<br />unManagedidscpencryptfailed<br />**Hex**:<br />80042902<br />**Number**:<br />-2147211006|Encryption of the supplied password failed.|
> |**Name**:<br />unManagedidscpuserdoesnotexist<br />**Hex**:<br />80042900<br />**Number**:<br />-2147211008|The customer portal user does not exist, or the password was incorrect.|
> |**Name**:<br />unManagedidscustomentityalreadyinitialized<br />**Hex**:<br />80045901<br />**Number**:<br />-2147198719|Custom entity interface already initialized on this thread.|
> |**Name**:<br />unManagedidscustomentityambiguousrelationship<br />**Hex**:<br />8004590d<br />**Number**:<br />-2147198707|More than one relationship between the requested entities exists.|
> |**Name**:<br />unManagedidscustomentityexistingloop<br />**Hex**:<br />80045907<br />**Number**:<br />-2147198713|There is an existing loop in the database.|
> |**Name**:<br />unManagedidscustomentityinvalidchild<br />**Hex**:<br />80045909<br />**Number**:<br />-2147198711|The supplied child passed in is not a valid entity.|
> |**Name**:<br />unManagedidscustomentityinvalidownership<br />**Hex**:<br />80045903<br />**Number**:<br />-2147198717|Custom entity ownership type mask is improperly set.|
> |**Name**:<br />unManagedidscustomentityinvalidparent<br />**Hex**:<br />8004590a<br />**Number**:<br />-2147198710|The supplied parent passed in is not a valid entity.|
> |**Name**:<br />unManagedidscustomentitynameviolation<br />**Hex**:<br />80045900<br />**Number**:<br />-2147198720|Supplied entity found, but it is not a custom entity.|
> |**Name**:<br />unManagedidscustomentitynorelationship<br />**Hex**:<br />8004590c<br />**Number**:<br />-2147198708|No relationship exists between the requested entities.|
> |**Name**:<br />unManagedidscustomentitynotinitialized<br />**Hex**:<br />80045902<br />**Number**:<br />-2147198718|Custom entity interface was not properly initialized.|
> |**Name**:<br />unManagedidscustomentityparentchildidentical<br />**Hex**:<br />8004590b<br />**Number**:<br />-2147198709|The supplied parent and child entities are identical.|
> |**Name**:<br />unManagedidscustomentitystackoverflow<br />**Hex**:<br />80045905<br />**Number**:<br />-2147198715|Custom entity MD stack overflow.|
> |**Name**:<br />unManagedidscustomentitystackunderflow<br />**Hex**:<br />80045906<br />**Number**:<br />-2147198714|Custom entity MD stack underflow.|
> |**Name**:<br />unManagedidscustomentitytlsfailure<br />**Hex**:<br />80045904<br />**Number**:<br />-2147198716|Custom entity MD TLS not initialized.|
> |**Name**:<br />unManagedidscustomentitywouldcreateloop<br />**Hex**:<br />80045908<br />**Number**:<br />-2147198712|This association would create a loop in the database.|
> |**Name**:<br />unManagedidscustomeraddresstypeinvalid<br />**Hex**:<br />80040514<br />**Number**:<br />-2147220204|Invalid customer address type.|
> |**Name**:<br />unManagedidscustomizationtransformationnotsupported<br />**Hex**:<br />80044700<br />**Number**:<br />-2147203328|Transformation is not supported for this object.|
> |**Name**:<br />unManagedidsdataaccessunexpected<br />**Hex**:<br />80042300<br />**Number**:<br />-2147212544|Unexpected error in data access.  DB Connection may not have been opened successfully.|
> |**Name**:<br />unManagedidsdataoutofrange<br />**Hex**:<br />8004022c<br />**Number**:<br />-2147220948|Data out of range|
> |**Name**:<br />unManagedidsevalaborted<br />**Hex**:<br />80042c03<br />**Number**:<br />-2147210237|Evaluation aborted.|
> |**Name**:<br />unManagedidsevalallaborted<br />**Hex**:<br />80042c02<br />**Number**:<br />-2147210238|Evaluation aborted and stop further processing.|
> |**Name**:<br />unManagedidsevalallcompleted<br />**Hex**:<br />80042c0c<br />**Number**:<br />-2147210228|Evaluation completed and stop further processing.|
> |**Name**:<br />unManagedidsevalassignshouldhave4parameters<br />**Hex**:<br />80042c01<br />**Number**:<br />-2147210239|Assign action should have 4 parameters.|
> |**Name**:<br />unManagedidsevalchangetypeerror<br />**Hex**:<br />80042c0d<br />**Number**:<br />-2147210227|Change type error.|
> |**Name**:<br />unManagedidsevalcompleted<br />**Hex**:<br />80042c04<br />**Number**:<br />-2147210236|Evaluation completed.|
> |**Name**:<br />unManagedidsevalcreateshouldhave2parameters<br />**Hex**:<br />80042c3c<br />**Number**:<br />-2147210180|Create action should have 2 parameters.|
> |**Name**:<br />unManagedidsevalerrorabsparameter<br />**Hex**:<br />80042c2c<br />**Number**:<br />-2147210196|Error occurred when evaluating a WFPM_ABS parameter.|
> |**Name**:<br />unManagedidsevalerroractivityattachment<br />**Hex**:<br />80042c18<br />**Number**:<br />-2147210216|Error in action activity attachment.|
> |**Name**:<br />unManagedidsevalerroraddparameter<br />**Hex**:<br />80042c0f<br />**Number**:<br />-2147210225|Error occurred when evaluating a WFPM_ADD parameter.|
> |**Name**:<br />unManagedidsevalerrorappendtoactivityparty<br />**Hex**:<br />80042c3f<br />**Number**:<br />-2147210177|unManagedidsevalerrorappendtoactivityparty|
> |**Name**:<br />unManagedidsevalerrorassign<br />**Hex**:<br />80042c22<br />**Number**:<br />-2147210206|Error in action assign.|
> |**Name**:<br />unManagedidsevalerrorbeginwithparameter<br />**Hex**:<br />80042c38<br />**Number**:<br />-2147210184|Error occurred when evaluating a WFPM_BEGIN_WITH parameter.|
> |**Name**:<br />unManagedidsevalerrorbetweenparameter<br />**Hex**:<br />80042c33<br />**Number**:<br />-2147210189|Error occurred when evaluating a WFPM_BETWEEN parameter.|
> |**Name**:<br />unManagedidsevalerrorcontainparameter<br />**Hex**:<br />80042c3a<br />**Number**:<br />-2147210182|Error occurred when evaluating a WFPM_CONTAIN parameter.|
> |**Name**:<br />unManagedidsevalerrorcreate<br />**Hex**:<br />80042c3b<br />**Number**:<br />-2147210181|Error in create update.|
> |**Name**:<br />unManagedidsevalerrorcreateactivity<br />**Hex**:<br />80042c17<br />**Number**:<br />-2147210217|Error in action create activity.|
> |**Name**:<br />unManagedidsevalerrorcreateincident<br />**Hex**:<br />80042c1d<br />**Number**:<br />-2147210211|Error in action create incident.|
> |**Name**:<br />unManagedidsevalerrorcreatenote<br />**Hex**:<br />80042c1b<br />**Number**:<br />-2147210213|Error in action create note.|
> |**Name**:<br />unManagedidsevalerrordividedbyzero<br />**Hex**:<br />80042c16<br />**Number**:<br />-2147210218|Divided by zero.|
> |**Name**:<br />unManagedidsevalerrordivisionparameter<br />**Hex**:<br />80042c13<br />**Number**:<br />-2147210221|Error occurred when evaluating a WFPM_DIVISION parameter.|
> |**Name**:<br />unManagedidsevalerrordivisionparameters<br />**Hex**:<br />80042c12<br />**Number**:<br />-2147210222|Division parameter can have only two subparameters.|
> |**Name**:<br />unManagedidsevalerroremailtemplate<br />**Hex**:<br />80042c21<br />**Number**:<br />-2147210207|Error in action email template.|
> |**Name**:<br />unManagedidsevalerrorendwithparameter<br />**Hex**:<br />80042c39<br />**Number**:<br />-2147210183|Error occurred when evaluating a WFPM_END_WITH parameter.|
> |**Name**:<br />unManagedidsevalerroreqparameter<br />**Hex**:<br />80042c31<br />**Number**:<br />-2147210191|Error occurred when evaluating a WFPM_EQ parameter.|
> |**Name**:<br />unManagedidsevalerrorexec<br />**Hex**:<br />80042c27<br />**Number**:<br />-2147210201|Error in action exec.|
> |**Name**:<br />unManagedidsevalerrorformatbooleanparameter<br />**Hex**:<br />80042c45<br />**Number**:<br />-2147210171|Error happens when evaluating WFPM_FORMAT_BOOLEAN parameter.|
> |**Name**:<br />unManagedidsevalerrorformatdatetimeparameter<br />**Hex**:<br />80042c44<br />**Number**:<br />-2147210172|Error happens when evaluating WFPM_FORMAT_DATETIME parameter.|
> |**Name**:<br />unManagedidsevalerrorformatdecimalparameter<br />**Hex**:<br />80042c4a<br />**Number**:<br />-2147210166|Error happens when evaluating WFPM_FORMAT_DECIMAL parameter.|
> |**Name**:<br />unManagedidsevalerrorformatintegerparameter<br />**Hex**:<br />80042c49<br />**Number**:<br />-2147210167|Error happens when evaluating WFPM_FORMAT_INTEGER parameter.|
> |**Name**:<br />unManagedidsevalerrorformatlookupparameter<br />**Hex**:<br />80042c4c<br />**Number**:<br />-2147210164|Error happens when evaluating WFPM_FORMAT_LOOKUP parameter.|
> |**Name**:<br />unManagedidsevalerrorformatpicklistparameter<br />**Hex**:<br />80042c46<br />**Number**:<br />-2147210170|Error happens when evaluating WFPM_FORMAT_PICKLIST parameter.|
> |**Name**:<br />unManagedidsevalerrorformattimezonecodeparameter<br />**Hex**:<br />80042c4b<br />**Number**:<br />-2147210165|unManagedidsevalerrorformattimezonecodeparameter|
> |**Name**:<br />unManagedidsevalerrorgeqparameter<br />**Hex**:<br />80042c2e<br />**Number**:<br />-2147210194|Error occurred when evaluating a WFPM_GEQ parameter.|
> |**Name**:<br />unManagedidsevalerrorgtparameter<br />**Hex**:<br />80042c2d<br />**Number**:<br />-2147210195|Error occurred when evaluating a WFPM_GT parameter.|
> |**Name**:<br />unManagedidsevalerrorhalt<br />**Hex**:<br />80042c28<br />**Number**:<br />-2147210200|Error in action halt.|
> |**Name**:<br />unManagedidsevalerrorhandleactivity<br />**Hex**:<br />80042c19<br />**Number**:<br />-2147210215|Error in action handle activity.|
> |**Name**:<br />unManagedidsevalerrorhandleincident<br />**Hex**:<br />80042c1e<br />**Number**:<br />-2147210210|Error in action handle incident.|
> |**Name**:<br />unManagedidsevalerrorincidentqueue<br />**Hex**:<br />80042c29<br />**Number**:<br />-2147210199|Failed to evaluate INCIDENT_QUEUE.|
> |**Name**:<br />unManagedidsevalerrorinlistparameter<br />**Hex**:<br />80042c42<br />**Number**:<br />-2147210174|unManagedidsevalerrorinlistparameter|
> |**Name**:<br />unManagedidsevalerrorinparameter<br />**Hex**:<br />80042c34<br />**Number**:<br />-2147210188|Error occurred when evaluating a WFPM_IN parameter.|
> |**Name**:<br />unManagedidsevalerrorinvalidparameter<br />**Hex**:<br />80042c2b<br />**Number**:<br />-2147210197|Invalid parameter.|
> |**Name**:<br />unManagedidsevalerrorinvalidrecipient<br />**Hex**:<br />80042c35<br />**Number**:<br />-2147210187|Invalid email recipient.|
> |**Name**:<br />unManagedidsevalerrorisnulllistparameter<br />**Hex**:<br />80042c43<br />**Number**:<br />-2147210173|unManagedidsevalerrorisnulllistparameter|
> |**Name**:<br />unManagedidsevalerrorleqparameter<br />**Hex**:<br />80042c30<br />**Number**:<br />-2147210192|Error occurred when evaluating a WFPM_LEQ parameter.|
> |**Name**:<br />unManagedidsevalerrorltparameter<br />**Hex**:<br />80042c2f<br />**Number**:<br />-2147210193|Error occurred when evaluating a WFPM_LT parameter.|
> |**Name**:<br />unManagedidsevalerrormodulusparameter<br />**Hex**:<br />80042c15<br />**Number**:<br />-2147210219|Error occurred when evaluating a WFPM_MODULUR parameter.|
> |**Name**:<br />unManagedidsevalerrormodulusparameters<br />**Hex**:<br />80042c14<br />**Number**:<br />-2147210220|Modulus parameter can have only two subparameters.|
> |**Name**:<br />unManagedidsevalerrormultiplicationparameter<br />**Hex**:<br />80042c11<br />**Number**:<br />-2147210223|Error occurred when evaluating a WFPM_MULTIPLICATION parameter.|
> |**Name**:<br />unManagedidsevalerrorneqparameter<br />**Hex**:<br />80042c32<br />**Number**:<br />-2147210190|Error occurred when evaluating a WFPM_NEQ parameter.|
> |**Name**:<br />unManagedidsevalerrornoteattachment<br />**Hex**:<br />80042c1c<br />**Number**:<br />-2147210212|Error in action note attachment.|
> |**Name**:<br />unManagedidsevalerrorobjecttype<br />**Hex**:<br />80042c48<br />**Number**:<br />-2147210168|Error happens when evaluating WFPM_GetObjectType parameter.|
> |**Name**:<br />unManagedidsevalerrorposturl<br />**Hex**:<br />80042c26<br />**Number**:<br />-2147210202|Error in action posturl.|
> |**Name**:<br />unManagedidsevalerrorqueueidparameter<br />**Hex**:<br />80042c47<br />**Number**:<br />-2147210169|unManagedidsevalerrorqueueidparameter|
> |**Name**:<br />unManagedidsevalerrorremovefromactivityparty<br />**Hex**:<br />80042c40<br />**Number**:<br />-2147210176|unManagedidsevalerrorremovefromactivityparty|
> |**Name**:<br />unManagedidsevalerrorroute<br />**Hex**:<br />80042c24<br />**Number**:<br />-2147210204|Error in action route.|
> |**Name**:<br />unManagedidsevalerrorsendemail<br />**Hex**:<br />80042c20<br />**Number**:<br />-2147210208|Error in action send email.|
> |**Name**:<br />unManagedidsevalerrorsetactivityparty<br />**Hex**:<br />80042c41<br />**Number**:<br />-2147210175|unManagedidsevalerrorsetactivityparty|
> |**Name**:<br />unManagedidsevalerrorsetstate<br />**Hex**:<br />80042c25<br />**Number**:<br />-2147210203|Error in action set state.|
> |**Name**:<br />unManagedidsevalerrorstrlenparameter<br />**Hex**:<br />80042c37<br />**Number**:<br />-2147210185|Error occurred when evaluating a WFPM_STRLEN parameter.|
> |**Name**:<br />unManagedidsevalerrorsubstrparameter<br />**Hex**:<br />80042c36<br />**Number**:<br />-2147210186|Error occurred when evaluating a WFPM_SUBSTR parameter.|
> |**Name**:<br />unManagedidsevalerrorsubtractionparameter<br />**Hex**:<br />80042c10<br />**Number**:<br />-2147210224|Error occurred when evaluating a WFPM_SUBTRACTION parameter.|
> |**Name**:<br />unManagedidsevalerrorunhandleactivity<br />**Hex**:<br />80042c1a<br />**Number**:<br />-2147210214|Error in action unhandle activity.|
> |**Name**:<br />unManagedidsevalerrorunhandleincident<br />**Hex**:<br />80042c1f<br />**Number**:<br />-2147210209|Error in action unhandle incident.|
> |**Name**:<br />unManagedidsevalerrorupdate<br />**Hex**:<br />80042c23<br />**Number**:<br />-2147210205|Error in action update.|
> |**Name**:<br />unManagedidsevalgenericerror<br />**Hex**:<br />80042c2a<br />**Number**:<br />-2147210198|Evaluation error.|
> |**Name**:<br />unManagedidsevalmetabaseattributenotfound<br />**Hex**:<br />80042c08<br />**Number**:<br />-2147210232|The specified metabase attribute does not exist.|
> |**Name**:<br />unManagedidsevalmetabaseattributenotmatchquery<br />**Hex**:<br />80042c0b<br />**Number**:<br />-2147210229|The specified refattributeid does not the query for a WFPM_SELECT parameter.|
> |**Name**:<br />unManagedidsevalmetabaseentitycompoundkeys<br />**Hex**:<br />80042c07<br />**Number**:<br />-2147210233|The specified metabase object has compound keys. We do not support compound-key entities yet.|
> |**Name**:<br />unManagedidsevalmetabaseentitynotmatchquery<br />**Hex**:<br />80042c0a<br />**Number**:<br />-2147210230|The specified refentityid does not the query for a WFPM_SELECT parameter.|
> |**Name**:<br />unManagedidsevalmissselectquery<br />**Hex**:<br />80042c0e<br />**Number**:<br />-2147210226|Missing the query subparameter in a select parameter.|
> |**Name**:<br />unManagedidsevalobjectnotfound<br />**Hex**:<br />80042c05<br />**Number**:<br />-2147210235|The required object does not exist.|
> |**Name**:<br />unManagedidsevalpropertyisnull<br />**Hex**:<br />80042c09<br />**Number**:<br />-2147210231|The required property of the object was not set.|
> |**Name**:<br />unManagedidsevalpropertynotfound<br />**Hex**:<br />80042c06<br />**Number**:<br />-2147210234|The required property of the object was not found.|
> |**Name**:<br />unManagedidsevaltimererrorcalculatescheduletime<br />**Hex**:<br />80042c3e<br />**Number**:<br />-2147210178|Failed to calculate the schedule time for the timer action.|
> |**Name**:<br />unManagedidsevaltimerinvalidparameternumber<br />**Hex**:<br />80042c3d<br />**Number**:<br />-2147210179|Invalid parameters for Timer action.|
> |**Name**:<br />unManagedidsevalupdateshouldhave3parameters<br />**Hex**:<br />80042c00<br />**Number**:<br />-2147210240|Update action should have 3 parameters.|
> |**Name**:<br />unManagedidsfailureinittoken<br />**Hex**:<br />8004020f<br />**Number**:<br />-2147220977|Failure in obtaining user token.|
> |**Name**:<br />unManagedidsfetchbetweentext<br />**Hex**:<br />80044153<br />**Number**:<br />-2147204781|between, not-between, in, and not-in operators are not allowed on attributes of type text or ntext.|
> |**Name**:<br />unManagedidsfulltextoperationfailed<br />**Hex**:<br />80043e06<br />**Number**:<br />-2147205626|Full text operation failed.|
> |**Name**:<br />unManagedidsincidentassociatedactivitycorrupted<br />**Hex**:<br />80044405<br />**Number**:<br />-2147204091|The activity associated with this case is corrupted.|
> |**Name**:<br />unManagedidsincidentcannotclose<br />**Hex**:<br />8004440a<br />**Number**:<br />-2147204086|The incident can not be closed because there are open activities for this incident.|
> |**Name**:<br />unManagedidsincidentcontractdetaildoesnotmatchcontract<br />**Hex**:<br />80044402<br />**Number**:<br />-2147204094|The contract line item is not in the specified contract.|
> |**Name**:<br />unManagedidsincidentinvalidactivitytypecode<br />**Hex**:<br />80044406<br />**Number**:<br />-2147204090|The activitytypecode is wrong.|
> |**Name**:<br />unManagedidsincidentinvalidstate<br />**Hex**:<br />80044404<br />**Number**:<br />-2147204092|Incident state is invalid.|
> |**Name**:<br />unManagedidsincidentmissingactivityobjecttype<br />**Hex**:<br />80044408<br />**Number**:<br />-2147204088|Missing object type code.|
> |**Name**:<br />unManagedidsincidentnullactivitytypecode<br />**Hex**:<br />80044407<br />**Number**:<br />-2147204089|The activitytypecode can't be NULL.|
> |**Name**:<br />unManagedidsincidentparentaccountandparentcontactnotpresent<br />**Hex**:<br />80044410<br />**Number**:<br />-2147204080|You should specify a parent contact or account.|
> |**Name**:<br />unManagedidsincidentparentaccountandparentcontactpresent<br />**Hex**:<br />8004440f<br />**Number**:<br />-2147204081|You can either specify a parent contact or account, but not both.|
> |**Name**:<br />unManagedidsinvalidassociation<br />**Hex**:<br />80040211<br />**Number**:<br />-2147220975|Invalid association.|
> |**Name**:<br />unManagedidsinvalidbusinessid<br />**Hex**:<br />80040209<br />**Number**:<br />-2147220983|Invalid business id.|
> |**Name**:<br />unManagedidsinvaliditemid<br />**Hex**:<br />8004020b<br />**Number**:<br />-2147220981|Invalid item id.|
> |**Name**:<br />unManagedidsinvalidorgid<br />**Hex**:<br />8004020a<br />**Number**:<br />-2147220982|Invalid organization id.|
> |**Name**:<br />unManagedidsinvalidowninguser<br />**Hex**:<br />80040212<br />**Number**:<br />-2147220974|Item does not have an owning user.|
> |**Name**:<br />unManagedidsinvalidteamid<br />**Hex**:<br />80040208<br />**Number**:<br />-2147220984|Invalid team id.|
> |**Name**:<br />unManagedidsinvaliduserid<br />**Hex**:<br />80040207<br />**Number**:<br />-2147220985|The user id is invalid or missing.|
> |**Name**:<br />unManagedidsinvaliduseridorbusinessidorusersbusinessinvalid<br />**Hex**:<br />8004021d<br />**Number**:<br />-2147220963|One of the following occurred: invalid user id, invalid business id or the user does not belong to the business.|
> |**Name**:<br />unManagedidsinvalidvisibility<br />**Hex**:<br />8004020e<br />**Number**:<br />-2147220978|Invalid visibility.|
> |**Name**:<br />unManagedidsinvalidvisibilitymodificationaccess<br />**Hex**:<br />80040213<br />**Number**:<br />-2147220973|User does not have access to modify the visibility of this item.|
> |**Name**:<br />unManagedidsinvoicecloseapideprecated<br />**Hex**:<br />80043b25<br />**Number**:<br />-2147206363|The Invoice Close API is deprecated. It has been replaced by the Pay and Cancel APIs.|
> |**Name**:<br />unManagedidsjournalinginvalideventtype<br />**Hex**:<br />80040803<br />**Number**:<br />-2147219453|Invalid event type.|
> |**Name**:<br />unManagedidsjournalingmissingaccountid<br />**Hex**:<br />80040806<br />**Number**:<br />-2147219450|Account Id missed.|
> |**Name**:<br />unManagedidsjournalingmissingcontactid<br />**Hex**:<br />80040808<br />**Number**:<br />-2147219448|Contact Id missed.|
> |**Name**:<br />unManagedidsjournalingmissingeventdirection<br />**Hex**:<br />80040802<br />**Number**:<br />-2147219454|Event direction code missed.|
> |**Name**:<br />unManagedidsjournalingmissingeventtype<br />**Hex**:<br />80040804<br />**Number**:<br />-2147219452|Event type missed.|
> |**Name**:<br />unManagedidsjournalingmissingincidentid<br />**Hex**:<br />80040809<br />**Number**:<br />-2147219447|Incident Id missed.|
> |**Name**:<br />unManagedidsjournalingmissingleadid<br />**Hex**:<br />80040805<br />**Number**:<br />-2147219451|Lead Id missed.|
> |**Name**:<br />unManagedidsjournalingmissingopportunityid<br />**Hex**:<br />80040807<br />**Number**:<br />-2147219449|Opportunity Id missed.|
> |**Name**:<br />unManagedidsjournalingunsupportedobjecttype<br />**Hex**:<br />80040801<br />**Number**:<br />-2147219455|Unsupported type of objects passed in operation.|
> |**Name**:<br />unManagedidsleaddoesnotexist<br />**Hex**:<br />80040501<br />**Number**:<br />-2147220223|Lead does not exist.|
> |**Name**:<br />unManagedidsleadnoparent<br />**Hex**:<br />8004050b<br />**Number**:<br />-2147220213|The lead does not have a parent.|
> |**Name**:<br />unManagedidsleadnotassigned<br />**Hex**:<br />8004050c<br />**Number**:<br />-2147220212|The lead has not been assigned.|
> |**Name**:<br />unManagedidsleadnotassignedtocaller<br />**Hex**:<br />80040513<br />**Number**:<br />-2147220205|The lead is not being assigned to the caller for acceptance.|
> |**Name**:<br />unManagedidsleadoneaccount<br />**Hex**:<br />80040510<br />**Number**:<br />-2147220208|A lead can be associated with only one account.|
> |**Name**:<br />unManagedidsleadusercannotreject<br />**Hex**:<br />8004050d<br />**Number**:<br />-2147220211|The user does not have the privilege to reject a lead, so he cannot be assigned the lead for acceptance.|
> |**Name**:<br />unManagedidsmergedifferentbizorgerror<br />**Hex**:<br />80045303<br />**Number**:<br />-2147200253|Merge cannot be performed on entities from different business entity.|
> |**Name**:<br />unManagedidsmetadatanoentity<br />**Hex**:<br />80040e00<br />**Number**:<br />-2147217920|The specified entity does not exist|
> |**Name**:<br />unManagedidsmetadatanorelationship<br />**Hex**:<br />80040e02<br />**Number**:<br />-2147217918|The relationship does not exist|
> |**Name**:<br />unManagedidsnorelationship<br />**Hex**:<br />80040236<br />**Number**:<br />-2147220938|No relationship exists between the objects specified.|
> |**Name**:<br />unManagedidsnotesalreadyattached<br />**Hex**:<br />80041701<br />**Number**:<br />-2147215615|The specified note is already attached to an object.|
> |**Name**:<br />unManagedidsnotesloopbeingcreated<br />**Hex**:<br />80041703<br />**Number**:<br />-2147215613|Creating this parental association would create a loop in the annotation hierarchy.|
> |**Name**:<br />unManagedidsnotesloopexists<br />**Hex**:<br />80041702<br />**Number**:<br />-2147215614|A loop exists in the annotation hierarchy.|
> |**Name**:<br />unManagedidsnotesnoattachment<br />**Hex**:<br />80041704<br />**Number**:<br />-2147215612|The specified note has no attachments.|
> |**Name**:<br />unManagedidsnotesnotedoesnotexist<br />**Hex**:<br />80041700<br />**Number**:<br />-2147215616|The specified note does not exist.|
> |**Name**:<br />unManagedidsopportunitydoesnotexist<br />**Hex**:<br />80040500<br />**Number**:<br />-2147220224|Opportunity does not exist.|
> |**Name**:<br />unManagedidsopportunityinvalidparent<br />**Hex**:<br />80040504<br />**Number**:<br />-2147220220|The parent of an opportunity must be an account or contact.|
> |**Name**:<br />unManagedidsopportunitymissingparent<br />**Hex**:<br />80040505<br />**Number**:<br />-2147220219|The parent of the opportunity is missing.|
> |**Name**:<br />unManagedidsopportunityoneaccount<br />**Hex**:<br />8004050e<br />**Number**:<br />-2147220210|An opportunity can be associated with only one account.|
> |**Name**:<br />unManagedidsopportunityorphan<br />**Hex**:<br />8004050f<br />**Number**:<br />-2147220209|Removing this association will make the opportunity an orphan.|
> |**Name**:<br />unManagedidsoutofmemory<br />**Hex**:<br />80040222<br />**Number**:<br />-2147220958|Out of memory.|
> |**Name**:<br />unManagedidsownernotenabled<br />**Hex**:<br />8004022b<br />**Number**:<br />-2147220949|The specified owner has been disabled.|
> |**Name**:<br />unManagedidspresentuseridandteamid<br />**Hex**:<br />8004021c<br />**Number**:<br />-2147220964|Both the user id and team id are present. Only one should be present.|
> |**Name**:<br />unManagedidspropbagattributealreadyset<br />**Hex**:<br />8004203f<br />**Number**:<br />-2147213249|One of the attributes passed has already been set|
> |**Name**:<br />unManagedidspropbagattributenotnullable<br />**Hex**:<br />8004203e<br />**Number**:<br />-2147213250|One of the attributes passed cannot be NULL|
> |**Name**:<br />unManagedidspropbagcolloutofrange<br />**Hex**:<br />8004201e<br />**Number**:<br />-2147213282|The bag index in the collection was out of range.|
> |**Name**:<br />unManagedidspropbagnointerface<br />**Hex**:<br />80042001<br />**Number**:<br />-2147213311|The property bag interface could not be found.|
> |**Name**:<br />unManagedidspropbagnullproperty<br />**Hex**:<br />80042002<br />**Number**:<br />-2147213310|The specified property was null in the property bag.|
> |**Name**:<br />unManagedidspropbagpropertynotfound<br />**Hex**:<br />80042000<br />**Number**:<br />-2147213312|The specified property was not found in the property bag.|
> |**Name**:<br />unManagedidsqueuemissingbusinessunitid<br />**Hex**:<br />80043e03<br />**Number**:<br />-2147205629|Missing businessunitid.|
> |**Name**:<br />unManagedidsqueueorganizationidnotmatch<br />**Hex**:<br />80043e04<br />**Number**:<br />-2147205628|Callers' organization Id does not match businessunit's organization Id.|
> |**Name**:<br />unManagedidsrcsyncfilternoaccess<br />**Hex**:<br />8004410f<br />**Number**:<br />-2147204849|Cannot go offline: missing access rights on required entity.|
> |**Name**:<br />unManagedidsrcsyncinvalidfiltererror<br />**Hex**:<br />8004410d<br />**Number**:<br />-2147204851|Invalid filter specified.|
> |**Name**:<br />unManagedidsrcsyncinvalidsubscription<br />**Hex**:<br />80044109<br />**Number**:<br />-2147204855|The specified subscription does not exist.|
> |**Name**:<br />unManagedidsrcsyncinvalidsynctime<br />**Hex**:<br />80044100<br />**Number**:<br />-2147204864|The specified sync time is invalid.  Sync times must not be earlier than those returned by the previous sync.  Please reinitialize your subscription.|
> |**Name**:<br />unManagedidsrcsyncmethodnone<br />**Hex**:<br />80044114<br />**Number**:<br />-2147204844|Synchronization tasks can’t be performed on this computer since the synchronization method is set to None.|
> |**Name**:<br />unManagedidsrcsyncmsxmlfailed<br />**Hex**:<br />80044101<br />**Number**:<br />-2147204863|unManagedidsrcsyncmsxmlfailed|
> |**Name**:<br />unManagedidsrcsyncnoclient<br />**Hex**:<br />80044113<br />**Number**:<br />-2147204845|Client does not exist.|
> |**Name**:<br />unManagedidsrcsyncnoprimary<br />**Hex**:<br />80044112<br />**Number**:<br />-2147204846|No primary client exists.|
> |**Name**:<br />unManagedidsrcsyncnotprimary<br />**Hex**:<br />80044111<br />**Number**:<br />-2147204847|Cannot sync: not the primary OutlookSync client.|
> |**Name**:<br />unManagedidsrcsyncsoapconnfailed<br />**Hex**:<br />80044103<br />**Number**:<br />-2147204861|unManagedidsrcsyncsoapconnfailed|
> |**Name**:<br />unManagedidsrcsyncsoapfaulterror<br />**Hex**:<br />80044106<br />**Number**:<br />-2147204858|unManagedidsrcsyncsoapfaulterror|
> |**Name**:<br />unManagedidsrcsyncsoapgenfailed<br />**Hex**:<br />80044102<br />**Number**:<br />-2147204862|unManagedidsrcsyncsoapgenfailed|
> |**Name**:<br />unManagedidsrcsyncsoapparseerror<br />**Hex**:<br />80044108<br />**Number**:<br />-2147204856|unManagedidsrcsyncsoapparseerror|
> |**Name**:<br />unManagedidsrcsyncsoapreaderror<br />**Hex**:<br />80044107<br />**Number**:<br />-2147204857|unManagedidsrcsyncsoapreaderror|
> |**Name**:<br />unManagedidsrcsyncsoapsendfailed<br />**Hex**:<br />80044104<br />**Number**:<br />-2147204860|unManagedidsrcsyncsoapsendfailed|
> |**Name**:<br />unManagedidsrcsyncsoapservererror<br />**Hex**:<br />80044105<br />**Number**:<br />-2147204859|unManagedidsrcsyncsoapservererror|
> |**Name**:<br />unManagedidsrcsyncsqlgenericerror<br />**Hex**:<br />80044110<br />**Number**:<br />-2147204848|unManagedidsrcsyncsqlgenericerror|
> |**Name**:<br />unManagedidsrcsyncsqlpausederror<br />**Hex**:<br />8004410c<br />**Number**:<br />-2147204852|unManagedidsrcsyncsqlpausederror|
> |**Name**:<br />unManagedidsrcsyncsqlstoppederror<br />**Hex**:<br />8004410b<br />**Number**:<br />-2147204853|unManagedidsrcsyncsqlstoppederror|
> |**Name**:<br />unManagedidsrcsyncsubscriptionowner<br />**Hex**:<br />8004410a<br />**Number**:<br />-2147204854|The caller id does not match the subscription owner id.  Only subscription owners may perform subscription operations.|
> |**Name**:<br />unManagedidsrolesdeletenonparentrole<br />**Hex**:<br />8004140c<br />**Number**:<br />-2147216372|Cannot delete a role that is inherited from a parent business.|
> |**Name**:<br />unManagedidsrolesinvalidroledata<br />**Hex**:<br />80041400<br />**Number**:<br />-2147216384|The role data is invalid.|
> |**Name**:<br />unManagedidsrolesinvalidroleid<br />**Hex**:<br />80041401<br />**Number**:<br />-2147216383|Invalid role ID.|
> |**Name**:<br />unManagedidsrolesinvalidrolename<br />**Hex**:<br />8004140a<br />**Number**:<br />-2147216374|The role name is invalid.|
> |**Name**:<br />unManagedidsrolesinvalidtemplateid<br />**Hex**:<br />80041404<br />**Number**:<br />-2147216380|Invalid role template ID.|
> |**Name**:<br />unManagedidsrolesmissbusinessid<br />**Hex**:<br />80041406<br />**Number**:<br />-2147216378|The role's business unit ID was unexpectedly missing.|
> |**Name**:<br />unManagedidsrolesmissprivid<br />**Hex**:<br />80041408<br />**Number**:<br />-2147216376|The privilege ID was unexpectedly missing.|
> |**Name**:<br />unManagedidsrolesmissroleid<br />**Hex**:<br />80041405<br />**Number**:<br />-2147216379|The role ID was unexpectedly missing.|
> |**Name**:<br />unManagedidsrolesmissrolename<br />**Hex**:<br />80041407<br />**Number**:<br />-2147216377|The role name was unexpectedly missing.|
> |**Name**:<br />unManagedidsrolesroledoesnotexist<br />**Hex**:<br />80041402<br />**Number**:<br />-2147216382|The specified role does not exist.|
> |**Name**:<br />unManagedidsrspropbagdbinfoalreadyset<br />**Hex**:<br />8004203d<br />**Number**:<br />-2147213251|The DB info for the recordset property bag has already been set.|
> |**Name**:<br />unManagedidsrspropbagdbinfonotset<br />**Hex**:<br />8004203c<br />**Number**:<br />-2147213252|The DB info for the recordset property bag has not been set.|
> |**Name**:<br />unManagedidssalespeopleduplicatecalendarfound<br />**Hex**:<br />80043802<br />**Number**:<br />-2147207166|Duplicate fiscal calendars found for this salesperson/year|
> |**Name**:<br />unManagedidssalespeopleinvalidfiscalcalendartype<br />**Hex**:<br />80043808<br />**Number**:<br />-2147207160|Invalid fiscal calendar type|
> |**Name**:<br />unManagedidssalespeopleinvalidfiscalperiodindex<br />**Hex**:<br />80043807<br />**Number**:<br />-2147207161|Invalid fiscal period index|
> |**Name**:<br />unManagedidssalespeopleinvalidterritoryobjecttype<br />**Hex**:<br />80043804<br />**Number**:<br />-2147207164|Territories cannot be retrieved by this kind of object|
> |**Name**:<br />unManagedidssqlerror<br />**Hex**:<br />80044150<br />**Number**:<br />-2147204784|Generic SQL error.|
> |**Name**:<br />unManagedidssqltimeouterror<br />**Hex**:<br />80044151<br />**Number**:<br />-2147204783|SQL timeout expired.|
> |**Name**:<br />unManagedidsstatedoesnotexist<br />**Hex**:<br />80043af9<br />**Number**:<br />-2147206407|The state is not valid for this object.|
> |**Name**:<br />unManagedidsusernotenabled<br />**Hex**:<br />80040225<br />**Number**:<br />-2147220955|The specified user is either disabled or is not a member of any business unit.|
> |**Name**:<br />unManagedidsviewisnotsharable<br />**Hex**:<br />80040232<br />**Number**:<br />-2147220942|The view is not sharable.|
> |**Name**:<br />unManagedidsxmlinvalidcollectionname<br />**Hex**:<br />80041a03<br />**Number**:<br />-2147214845|The collection name specified is incorrect|
> |**Name**:<br />unManagedidsxmlinvalidcreate<br />**Hex**:<br />80041a01<br />**Number**:<br />-2147214847|A field that is not valid for create was specified|
> |**Name**:<br />unManagedidsxmlinvalidentityattributes<br />**Hex**:<br />80041a06<br />**Number**:<br />-2147214842|Invalid attributes|
> |**Name**:<br />unManagedidsxmlinvalidentityname<br />**Hex**:<br />80041a00<br />**Number**:<br />-2147214848|The entity name specified is incorrect|
> |**Name**:<br />unManagedidsxmlinvalidfield<br />**Hex**:<br />80041a07<br />**Number**:<br />-2147214841|An invalid value was passed in for a field|
> |**Name**:<br />unManagedidsxmlinvalidread<br />**Hex**:<br />80041a08<br />**Number**:<br />-2147214840|A field that is not valid for read was specified|
> |**Name**:<br />unManagedidsxmlinvalidupdate<br />**Hex**:<br />80041a02<br />**Number**:<br />-2147214846|A field that is not valid for update was specified|
> |**Name**:<br />unManagedidsxmlparseerror<br />**Hex**:<br />80041a04<br />**Number**:<br />-2147214844|A parse error was encountered in the XML|
> |**Name**:<br />unManagedidsxmlunexpected<br />**Hex**:<br />80041a05<br />**Number**:<br />-2147214843|An unexpected error has occurred|
> |**Name**:<br />unManagedinvalddbtimefield<br />**Hex**:<br />800404d9<br />**Number**:<br />-2147220263|The platform cannot handle dbtime fields.|
> |**Name**:<br />unManagedinvalidargumentsforcondition<br />**Hex**:<br />800404b7<br />**Number**:<br />-2147220297|An invalid number of arguments was supplied to a condition.|
> |**Name**:<br />unManagedinvalidbinaryfield<br />**Hex**:<br />800404dc<br />**Number**:<br />-2147220260|The platform cannot handle binary fields.|
> |**Name**:<br />unManagedinvalidbusinessunitid<br />**Hex**:<br />800404a7<br />**Number**:<br />-2147220313|The businessunitid is missing or invalid.|
> |**Name**:<br />unManagedinvalidcharacterdataforaggregate<br />**Hex**:<br />800404de<br />**Number**:<br />-2147220258|Character data is not valid when clearing an aggregate.|
> |**Name**:<br />unManagedinvalidcountvalue<br />**Hex**:<br />800404c1<br />**Number**:<br />-2147220287|The count value is invalid or missing.|
> |**Name**:<br />unManagedinvaliddbdatefield<br />**Hex**:<br />800404da<br />**Number**:<br />-2147220262|The platform cannot handle dbdate fields.|
> |**Name**:<br />unManagedinvaliddynamicparameteraccessor<br />**Hex**:<br />800404d5<br />**Number**:<br />-2147220267|SetParam failed processing the DynamicParameterAccessor parameter.|
> |**Name**:<br />unManagedinvalidequalityoperand<br />**Hex**:<br />800404ac<br />**Number**:<br />-2147220308|Only QB_LITERAL is supported for equality operand.|
> |**Name**:<br />unManagedinvalidescapedxml<br />**Hex**:<br />800404a1<br />**Number**:<br />-2147220319|Escaped xml size not as expected.|
> |**Name**:<br />unManagedinvalidfieldtype<br />**Hex**:<br />800404d8<br />**Number**:<br />-2147220264|The platform cannot handle the specified field type.|
> |**Name**:<br />unManagedinvalidlinkobjects<br />**Hex**:<br />800404ba<br />**Number**:<br />-2147220294|Invalid link entity, link to attribute, or link from attribute.|
> |**Name**:<br />unManagedinvalidoperator<br />**Hex**:<br />800404c7<br />**Number**:<br />-2147220281|The operator provided is not valid.|
> |**Name**:<br />unManagedinvalidorganizationid<br />**Hex**:<br />800404be<br />**Number**:<br />-2147220290|The organizationid is missing or invalid.|
> |**Name**:<br />unManagedinvalidowningbusinessunit<br />**Hex**:<br />800404a8<br />**Number**:<br />-2147220312|The owningbusinessunit is missing or invalid.|
> |**Name**:<br />unManagedinvalidowningbusinessunitorbusinessunitid<br />**Hex**:<br />800404bc<br />**Number**:<br />-2147220292|The owningbusinessunit or businessunitid is missing or invalid.|
> |**Name**:<br />unManagedinvalidowninguser<br />**Hex**:<br />800404bd<br />**Number**:<br />-2147220291|The owninguser is mising or invalid.|
> |**Name**:<br />unManagedinvalidpagevalue<br />**Hex**:<br />800404c2<br />**Number**:<br />-2147220286|The page value is invalid or missing.|
> |**Name**:<br />unManagedinvalidparametertypeforparameterizedquery<br />**Hex**:<br />800404d6<br />**Number**:<br />-2147220266|A parameterized query is not supported for the supplied parameter type.|
> |**Name**:<br />unManagedinvalidprincipal<br />**Hex**:<br />8004049e<br />**Number**:<br />-2147220322|The principal id is missing or invalid.|
> |**Name**:<br />unManagedinvalidprivilegeedepth<br />**Hex**:<br />800404bb<br />**Number**:<br />-2147220293|Invalid privilege depth for user.|
> |**Name**:<br />unManagedinvalidprivilegeid<br />**Hex**:<br />800404ce<br />**Number**:<br />-2147220274|The privilege id is invalid or missing.|
> |**Name**:<br />unManagedinvalidprivilegeusergroup<br />**Hex**:<br />800404cd<br />**Number**:<br />-2147220275|The privilege user group id is invalid or missing.|
> |**Name**:<br />unManagedinvalidprocesschildofcondition<br />**Hex**:<br />800404b4<br />**Number**:<br />-2147220300|ProcessChildOfCondition was called with non-child-of condition.|
> |**Name**:<br />unManagedinvalidprocessliternalcondition<br />**Hex**:<br />800404b1<br />**Number**:<br />-2147220303|ProcessLiteralCondition is only valid for use with Rollup queries.|
> |**Name**:<br />unManagedinvalidsecurityprincipal<br />**Hex**:<br />800404d2<br />**Number**:<br />-2147220270|The security principal is invalid or missing.|
> |**Name**:<br />unManagedinvalidstreamfield<br />**Hex**:<br />800404d7<br />**Number**:<br />-2147220265|The platform cannot handle stream fields.|
> |**Name**:<br />unManagedinvalidtlsmananger<br />**Hex**:<br />800404a2<br />**Number**:<br />-2147220318|Failed to retrieve TLS Manager.|
> |**Name**:<br />unManagedinvalidtrxcountforcommit<br />**Hex**:<br />800404e2<br />**Number**:<br />-2147220254|The transaction count was expected to be 1 in order to commit.|
> |**Name**:<br />unManagedinvalidtrxcountforrollback<br />**Hex**:<br />800404e1<br />**Number**:<br />-2147220255|The transaction count was expected to be 1 in order to rollback.|
> |**Name**:<br />unManagedinvalidvaluettagoutsideconditiontag<br />**Hex**:<br />800404bf<br />**Number**:<br />-2147220289|A invalid value tag was found outside of it's condition tag.|
> |**Name**:<br />unManagedinvalidversionvalue<br />**Hex**:<br />800404c0<br />**Number**:<br />-2147220288|The version value is invalid or missing.|
> |**Name**:<br />unManagedinvaludidispatchfield<br />**Hex**:<br />800404db<br />**Number**:<br />-2147220261|The platform cannot handle idispatch fields.|
> |**Name**:<br />unManagedmissingaddressentity<br />**Hex**:<br />800404cb<br />**Number**:<br />-2147220277|The address entity could not be found.|
> |**Name**:<br />unManagedmissingattributefortag<br />**Hex**:<br />800404c5<br />**Number**:<br />-2147220283|An expected attribute was not found for the tag specified.|
> |**Name**:<br />unManagedmissingdataaccess<br />**Hex**:<br />800404df<br />**Number**:<br />-2147220257|The data access could not be retrieved from the ExecutionContext.|
> |**Name**:<br />unManagedmissingfilterattribute<br />**Hex**:<br />800404ad<br />**Number**:<br />-2147220307|Missing filter attribute.|
> |**Name**:<br />unManagedmissinglinkentity<br />**Hex**:<br />800404b2<br />**Number**:<br />-2147220302|Unexpected error locating link entity.|
> |**Name**:<br />unManagedMissingObjectType<br />**Hex**:<br />80042003<br />**Number**:<br />-2147213309|Object type must be specified for one of the attributes.|
> |**Name**:<br />unManagedmissingparentattributeonentity<br />**Hex**:<br />800404b5<br />**Number**:<br />-2147220299|The parent attribute was not found on the expected entity.|
> |**Name**:<br />unManagedmissingparententity<br />**Hex**:<br />800404e5<br />**Number**:<br />-2147220251|The parent entity could not be located.|
> |**Name**:<br />unManagedmissingpreviousownertype<br />**Hex**:<br />800404d0<br />**Number**:<br />-2147220272|Unable to determine the previous owner's type.|
> |**Name**:<br />unManagedmissingreferencesfromrelationship<br />**Hex**:<br />800404c9<br />**Number**:<br />-2147220279|Unable to access a relationship in an entity's ReferencesFrom collection.|
> |**Name**:<br />unManagedmissingreferencingattribute<br />**Hex**:<br />800404c8<br />**Number**:<br />-2147220280|The relationship's ReferencingAttribute is missing or invalid.|
> |**Name**:<br />unManagedmorethanonesortattribute<br />**Hex**:<br />800404a6<br />**Number**:<br />-2147220314|More than one sort attributes were defined.|
> |**Name**:<br />unManagedObjectTypeUnexpected<br />**Hex**:<br />80042004<br />**Number**:<br />-2147213308|Object type was specified for one of the attributes that does not allow it.|
> |**Name**:<br />unManagedparentattributenotfound<br />**Hex**:<br />800404a4<br />**Number**:<br />-2147220316|The parent attribute was not found for the child attribute.|
> |**Name**:<br />unManagedpartylistattributenotsupported<br />**Hex**:<br />800404b8<br />**Number**:<br />-2147220296|Attributes of type partylist are not supported.|
> |**Name**:<br />unManagedpendingtrxexists<br />**Hex**:<br />800404e3<br />**Number**:<br />-2147220253|A pending transaction already exists.|
> |**Name**:<br />unManagedproxycreationfailed<br />**Hex**:<br />8004049f<br />**Number**:<br />-2147220321|Cannot create an instance of managed proxy.|
> |**Name**:<br />unManagedtrxinterophandlerset<br />**Hex**:<br />800404dd<br />**Number**:<br />-2147220259|The TrxInteropHandler has already been set.|
> |**Name**:<br />unManagedunablegetexecutioncontext<br />**Hex**:<br />800404e4<br />**Number**:<br />-2147220252|Failed to retrieve execution context (TLS).|
> |**Name**:<br />unManagedunablegetsessiontoken<br />**Hex**:<br />800404d3<br />**Number**:<br />-2147220269|Unable to retrieve the session token.|
> |**Name**:<br />unManagedunablegetsessiontokennotrx<br />**Hex**:<br />800404d4<br />**Number**:<br />-2147220268|Unable to retrieve the session token as there are no pending transactions.|
> |**Name**:<br />unManagedunableswitchusercontext<br />**Hex**:<br />800404e0<br />**Number**:<br />-2147220256|Cannot set to a different user context.|
> |**Name**:<br />unManagedunabletoaccessqueryplan<br />**Hex**:<br />800404a5<br />**Number**:<br />-2147220315|Unable to access the query plan.|
> |**Name**:<br />unManagedunabletoaccessqueryplanfilter<br />**Hex**:<br />800404c6<br />**Number**:<br />-2147220282|Unable to access a filter in the query plan.|
> |**Name**:<br />unManagedunabletolocateconditionfilter<br />**Hex**:<br />800404c3<br />**Number**:<br />-2147220285|Unexpected error locating the filter for the condition.|
> |**Name**:<br />unManagedunabletoretrieveprivileges<br />**Hex**:<br />800404a0<br />**Number**:<br />-2147220320|Failed to retrieve privileges.|
> |**Name**:<br />unManagedunexpectedpropertytype<br />**Hex**:<br />800404cc<br />**Number**:<br />-2147220276|Unexpected type for the property.|
> |**Name**:<br />unManagedunexpectedrimarykey<br />**Hex**:<br />800404b3<br />**Number**:<br />-2147220301|Primary key attribute was not as expected.|
> |**Name**:<br />unManagedunknownaggregateoperation<br />**Hex**:<br />800404b6<br />**Number**:<br />-2147220298|An unknown aggregate operation was supplied.|
> |**Name**:<br />unManagedunusablevariantdata<br />**Hex**:<br />800404af<br />**Number**:<br />-2147220305|Variant supplied contains data in an unusable format.|
> |**Name**:<br />UnmappedTransformationOutputDataFound<br />**Hex**:<br />80040381<br />**Number**:<br />-2147220607|One or more outputs returned by the transformation is not mapped to target fields.|
> |**Name**:<br />UnpopulatedPrimaryKey<br />**Hex**:<br />8004023d<br />**Number**:<br />-2147220931|Primary Key must be populated for calls to platform on rich client in offline mode.|
> |**Name**:<br />UnrelatedConnectionRoles<br />**Hex**:<br />80048216<br />**Number**:<br />-2147188202|The connection roles are not related.|
> |**Name**:<br />UnrestrictedIFrameInUserDashboard<br />**Hex**:<br />8004E30C<br />**Number**:<br />-2147163380|A user dashboard Form XML cannot have Security = false.|
> |**Name**:<br />UnspecifiedActivityXmlForCampaignActivityPropagate<br />**Hex**:<br />80040318<br />**Number**:<br />-2147220712|Must specify an Activity Xml for CampaignActivity Execute/Distribute|
> |**Name**:<br />UnsupportedActionType<br />**Hex**:<br />80060390<br />**Number**:<br />-2147089520|Missing Control Step.|
> |**Name**:<br />UnsupportedArgumentsMarkedRequired<br />**Hex**:<br />80060394<br />**Number**:<br />-2147089516|Unsupported arguments should not be marked as required.|
> |**Name**:<br />UnsupportedAttributeForEditor<br />**Hex**:<br />80060010<br />**Number**:<br />-2147090416|The rule contain an attribute which is not supported.|
> |**Name**:<br />UnsupportedAttributeInInProfileItemEntityFilters<br />**Hex**:<br />80071123<br />**Number**:<br />-2147020509|Attribute {0} is not supported in the filter query option.|
> |**Name**:<br />UnsupportedAttributeOrOperatorMobileOfflineFilters<br />**Hex**:<br />80071115<br />**Number**:<br />-2147020523|Attribute or Operator “{0}” is not supported for Mobile Offline Org Filter.|
> |**Name**:<br />UnsupportedAttributeType<br />**Hex**:<br />8005E00D<br />**Number**:<br />-2147098611|Attribute type {0} is not supported. Remove attribute {1} from the query and try again.|
> |**Name**:<br />UnsupportedComponentOperation<br />**Hex**:<br />8004F010<br />**Number**:<br />-2147160048|{0} is not recognized as a supported operation.|
> |**Name**:<br />UnsupportedCudOperationForDynamicProperties<br />**Hex**:<br />80061019<br />**Number**:<br />-2147086311|You can't create a property for a kit.|
> |**Name**:<br />UnsupportedDashboardInEditor<br />**Hex**:<br />8004E30E<br />**Number**:<br />-2147163378|The dashboard could not be opened.|
> |**Name**:<br />UnsupportedEmailServer<br />**Hex**:<br />8005E242<br />**Number**:<br />-2147098046|The email server isn't supported.|
> |**Name**:<br />UnsupportedImportComponent<br />**Hex**:<br />80061302<br />**Number**:<br />-2147085566|Sorry, your import failed because the {0} component isn’t supported for import and export.|
> |**Name**:<br />UnsupportedListMemberType<br />**Hex**:<br />80040301<br />**Number**:<br />-2147220735|Unsupported list member type.|
> |**Name**:<br />UnsupportedOperatorForAttributeInProfileItemEntityFilters<br />**Hex**:<br />80071121<br />**Number**:<br />-2147020511|Operator {0} is not supported with attribute {1} in the filter query option.|
> |**Name**:<br />UnsupportedParameter<br />**Hex**:<br />80040320<br />**Number**:<br />-2147220704|A parameter specified is not supported by the Bulk Operation|
> |**Name**:<br />UnsupportedProcessCode<br />**Hex**:<br />80040385<br />**Number**:<br />-2147220603|The process code is not supported on this entity.|
> |**Name**:<br />UnsupportedSdkMessageForBundles<br />**Hex**:<br />80061025<br />**Number**:<br />-2147086299|This message isn't supported for products of type bundle.|
> |**Name**:<br />UnsupportedStepForBusinessRuleEditor<br />**Hex**:<br />80060009<br />**Number**:<br />-2147090423|The rule contain a step which is not supported by the editor.|
> |**Name**:<br />UnsupportedZipFileForImport<br />**Hex**:<br />80048495<br />**Number**:<br />-2147187563|The compressed (.zip) or .cab file couldn't be uploaded because the file is corrupted or doesn't contain valid importable files.|
> |**Name**:<br />UnzipProcessCountLimitReached<br />**Hex**:<br />80048494<br />**Number**:<br />-2147187564|Cannot start a new process to unzip.|
> |**Name**:<br />UnzipTimeout<br />**Hex**:<br />80048496<br />**Number**:<br />-2147187562|Timeout happened in unzipping the zip file uploaded for import.|
> |**Name**:<br />UpdateAttributeMap<br />**Hex**:<br />80046204<br />**Number**:<br />-2147196412|UpdateAttributeMap Error Occurred|
> |**Name**:<br />UpdateEntityMap<br />**Hex**:<br />80046201<br />**Number**:<br />-2147196415|UpdateEntityMap Error Occurred|
> |**Name**:<br />UpdateNonCustomReportFromTemplate<br />**Hex**:<br />80040490<br />**Number**:<br />-2147220336|Cannot update a report from a template if the report was not created from a template|
> |**Name**:<br />UpdatePublishedWorkflowDefinition<br />**Hex**:<br />80045002<br />**Number**:<br />-2147201022|Cannot update a published workflow definition.|
> |**Name**:<br />UpdatePublishedWorkflowDefinitionWorkflowDependency<br />**Hex**:<br />80045008<br />**Number**:<br />-2147201016|Cannot update a workflow dependency for a published workflow definition.|
> |**Name**:<br />UpdatePublishedWorkflowTemplate<br />**Hex**:<br />8004501B<br />**Number**:<br />-2147200997|Cannot update a published workflow template.|
> |**Name**:<br />UpdateRecurrenceRuleFailed<br />**Hex**:<br />8004E114<br />**Number**:<br />-2147163884|Failed to update the recurrence rule. A corresponding recurrence rule cannot be found.|
> |**Name**:<br />UpdateRIOrganizationDataAccessNotAllowed<br />**Hex**:<br />80044273<br />**Number**:<br />-2147204493|This feature configuration can only be updated by a system administrator.|
> |**Name**:<br />UpdateWorkflowActivation<br />**Hex**:<br />80045003<br />**Number**:<br />-2147201021|Cannot update a workflow activation.|
> |**Name**:<br />UpdateWorkflowActivationWorkflowDependency<br />**Hex**:<br />80045007<br />**Number**:<br />-2147201017|Cannot update a workflow dependency associated with a workflow activation.|
> |**Name**:<br />UserAlreadyExists<br />**Hex**:<br />80041d2c<br />**Number**:<br />-2147214036|The specified Active Directory user already exists as a Dynamics 365 user.|
> |**Name**:<br />UserCancelledMailMerge<br />**Hex**:<br />8004032f<br />**Number**:<br />-2147220689|The mail merge operation was cancelled by the user.|
> |**Name**:<br />UserCannotEnableWithoutLicense<br />**Hex**:<br />8004D24C<br />**Number**:<br />-2147167668|Cannot enable an unlicensed user|
> |**Name**:<br />UserDataNotFound<br />**Hex**:<br />8004D211<br />**Number**:<br />-2147167727|The user data could not be found.|
> |**Name**:<br />UserDoesNotHaveAccessToTheTenant<br />**Hex**:<br />80044507<br />**Number**:<br />-2147203833|User does not have access to the tenant.|
> |**Name**:<br />UserDoesNotHaveAdminOnlyModePermissions<br />**Hex**:<br />8004A113<br />**Number**:<br />-2147180269|User does not have required privileges (or role membership) to access the org when it is in Admin Only mode.|
> |**Name**:<br />UserDoesNotHavePrivilegesToRunTheTool<br />**Hex**:<br />800608F8<br />**Number**:<br />-2147088136|You must be a system administrator to execute this request.|
> |**Name**:<br />UserDoesNotHaveSendAsAllowed<br />**Hex**:<br />8004480d<br />**Number**:<br />-2147203059|User does not have send-as privilege|
> |**Name**:<br />UserDoesNotHaveSendAsForQueue<br />**Hex**:<br />8004480f<br />**Number**:<br />-2147203057|You do not have sufficient privileges to send e-mail as the selected queue. Contact your system administrator for assistance.|
> |**Name**:<br />UserIdOrQueueNotSet<br />**Hex**:<br />800404e8<br />**Number**:<br />-2147220248|Primary User Id or Destination Queue Type code not set|
> |**Name**:<br />UserInviteDisabled<br />**Hex**:<br />8004D216<br />**Number**:<br />-2147167722|Invitation cannot be sent because user invitations are disabled.|
> |**Name**:<br />UserInWrongBusiness<br />**Hex**:<br />80041409<br />**Number**:<br />-2147216375|The user with id={0} belongs to a different business unit={1} than the role with roleId={2} and rolebusinessUnit={3}.|
> |**Name**:<br />UserIsNotSystemAdminInOrganization<br />**Hex**:<br />8004B069<br />**Number**:<br />-2147176343|Current user is not a system admin in customer's organization|
> |**Name**:<br />UserLoopBeingCreated<br />**Hex**:<br />80041d25<br />**Number**:<br />-2147214043|You cannot set the selected user as the manager for this user because the selected user is either already the manager or is in the user's immediate management hierarchy.  Either select another user to be the manager or do not update the record.|
> |**Name**:<br />UserLoopExists<br />**Hex**:<br />80041d24<br />**Number**:<br />-2147214044|A manager for this user cannot be set because an existing relationship in the management hierarchy is causing a circular relationship.  This is usually caused by a manual edit of the Microsoft Dynamics 365 database. To fix this, the hierarchy in the database must be changed to remove the circular relationship.|
> |**Name**:<br />UserNameRequiredForImpersonation<br />**Hex**:<br />8005E24D<br />**Number**:<br />-2147098035|Type in a user name and save again|
> |**Name**:<br />UserNeverLoggedIntoYammer<br />**Hex**:<br />8005F111<br />**Number**:<br />-2147094255|To follow other users, you must be logged in to Yammer. Log in to your Yammer account, and try again.|
> |**Name**:<br />UserNotAssignedLicense<br />**Hex**:<br />8004D24B<br />**Number**:<br />-2147167669|The user has not been assigned any License|
> |**Name**:<br />UserNotAssignedRoles<br />**Hex**:<br />80042f09<br />**Number**:<br />-2147209463|The user has not been assigned any roles.|
> |**Name**:<br />UserNotInParentHierarchy<br />**Hex**:<br />80041d07<br />**Number**:<br />-2147214073|The user is not in parent user's business hierarchy.|
> |**Name**:<br />UserNotMemberOfOrg<br />**Hex**:<br />80072560<br />**Number**:<br />-2147015328|The user is not a member of the organization.|
> |**Name**:<br />UserSettingsInvalidAdvancedFindStartupMode<br />**Hex**:<br />80041d34<br />**Number**:<br />-2147214028|Invalid advanced find startup mode.|
> |**Name**:<br />UserSettingsInvalidSearchExperienceValue<br />**Hex**:<br />80041d53<br />**Number**:<br />-2147213997|Invalid search experience value.|
> |**Name**:<br />UserSettingsOverMaxPagingLimit<br />**Hex**:<br />80044305<br />**Number**:<br />-2147204347|Paging limit over maximum configured value.|
> |**Name**:<br />UserTimeConvertException<br />**Hex**:<br />80040241<br />**Number**:<br />-2147220927|Failed to convert user time zone information.|
> |**Name**:<br />UserTimeZoneException<br />**Hex**:<br />80040240<br />**Number**:<br />-2147220928|Failed to retrieve user time zone information.|
> |**Name**:<br />UserViewsOrVisualizationsFound<br />**Hex**:<br />8004E302<br />**Number**:<br />-2147163390|A system dashboard cannot contain user views and visualizations.|
> |**Name**:<br />ValidateNotSupported<br />**Hex**:<br />8004E10A<br />**Number**:<br />-2147163894|Validate method is not supported for recurring appointment master.|
> |**Name**:<br />ValidationContextIsNull<br />**Hex**:<br />80060442<br />**Number**:<br />-2147089342|Error creating or updating Business Process: validation context cannot be null.|
> |**Name**:<br />ValidationFailedForDynamicProperty<br />**Hex**:<br />80061021<br />**Number**:<br />-2147086303|An error occurred while saving the {0} property.|
> |**Name**:<br />ValidDateTimeBehaviorExportAsWarning<br />**Hex**:<br />800608A5<br />**Number**:<br />-2147088219|The {0} field will be a User Local Date and Time since the Date Only and Time Zone Independent behaviors won't work in earlier versions of Dynamics 365.|
> |**Name**:<br />ValidDateTimeBehaviorWarning<br />**Hex**:<br />800608A4<br />**Number**:<br />-2147088220|The behavior of this field was changed. You should review all the dependencies of this field, such as business rules, workflows, and calculated or rollup fields, to ensure that issues won't occur. Attribute: {0}|
> |**Name**:<br />ValidOnlyForDynamicsOnline<br />**Hex**:<br />80072302<br />**Number**:<br />-2147015934|This API is only valid for Dynamics 365 online.|
> |**Name**:<br />ValueMissingInOptionOrderArray<br />**Hex**:<br />80044325<br />**Number**:<br />-2147204315|The options array is missing a value.|
> |**Name**:<br />ValueParsingError<br />**Hex**:<br />8004B037<br />**Number**:<br />-2147176393|Error parsing parameter {0} of type {1} with value {2}|
> |**Name**:<br />VersionedRowNotFoundInTempDB<br />**Hex**:<br />80048542<br />**Number**:<br />-2147187390|Required versioned row was not found in TempDB; the TempDB is likely out of space; try again at a later time.|
> |**Name**:<br />VersionMismatch<br />**Hex**:<br />8004B020<br />**Number**:<br />-2147176416|Unsupported version - This is {0} version {1}, but version {2} was requested.|
> |**Name**:<br />VeryLargeFileInZipImport<br />**Hex**:<br />80048491<br />**Number**:<br />-2147187567|One of the files in the compressed (.zip) or .cab file that you're trying to import exceeds the size limit.|
> |**Name**:<br />ViewConditionTypeNotSupportedOffline<br />**Hex**:<br />80071130<br />**Number**:<br />-2147020496|The condition {0} is not supported.|
> |**Name**:<br />ViewForDuplicateDetectionNotDefined<br />**Hex**:<br />80048838<br />**Number**:<br />-2147186632|Required view for viewing duplicates of an entity not defined.|
> |**Name**:<br />ViewNotAvailableForMobileOffline<br />**Hex**:<br />8005F21b<br />**Number**:<br />-2147093989|Currently view is not available Offline. Please try switching view or contact administrator|
> |**Name**:<br />ViewNotAvailableOnMobile<br />**Hex**:<br />80071126<br />**Number**:<br />-2147020506|This view is not available on mobile.|
> |**Name**:<br />ViewNotSupportedInCalendarModeOffline<br />**Hex**:<br />80071128<br />**Number**:<br />-2147020504|This view is supported only in grid mode offline. It is not supported in calendar mode offline.|
> |**Name**:<br />VirtualEntitiesNotSupported<br />**Hex**:<br />80073020<br />**Number**:<br />-2147012576|Virtual entities are not supported.|
> |**Name**:<br />VirtualEntityFailure<br />**Hex**:<br />80050263<br />**Number**:<br />-2147155357|Virtual Entity Operation Failed.|
> |**Name**:<br />VirtualEntityFCBOFF<br />**Hex**:<br />80081113<br />**Number**:<br />-2146954989|Feature Bit for VirtualEntity not enabled.|
> |**Name**:<br />VirtualEntityNotSupportedInMobileOffline<br />**Hex**:<br />80044821<br />**Number**:<br />-2147203039|The entity {0} is a virtual entity that’s not available in mobile offline.|
> |**Name**:<br />VisualizationModuleNotFound<br />**Hex**:<br />8004E012<br />**Number**:<br />-2147164142|No visualization module found with the given name.|
> |**Name**:<br />VisualizationOtcNotFoundError<br />**Hex**:<br />8004E015<br />**Number**:<br />-2147164139|Object type code is not specified for the visualization.|
> |**Name**:<br />VisualizationRenderingError<br />**Hex**:<br />8004E00E<br />**Number**:<br />-2147164146|An error occurred while the chart was rendering|
> |**Name**:<br />WebhooksHttpRequestTimedOut<br />**Hex**:<br />80050202<br />**Number**:<br />-2147155454|The webhook call failed because the Http request timed out at client side. Please check your webhook request handler.|
> |**Name**:<br />WebhooksInvalidHttpHeaders<br />**Hex**:<br />80050203<br />**Number**:<br />-2147155453|The webhook call failed because of invalid http headers in authValue. Check if the authValue format, header names and values are valid for your Service Endpoint entity.|
> |**Name**:<br />WebhooksInvalidHttpQueryParams<br />**Hex**:<br />80050204<br />**Number**:<br />-2147155452|The webhook call failed because of invalid http query params in authValue. Check if the authValue format, query parameter names and values are valid for your Service Endpoint entity.|
> |**Name**:<br />WebhooksMaxSizeExceeded<br />**Hex**:<br />80050207<br />**Number**:<br />-2147155449|The webhook call failed because the http request payload has exceeded maximum allowed size. Please reduce your request size and retry.|
> |**Name**:<br />WebhooksNonSuccessHttpResponse<br />**Hex**:<br />80050201<br />**Number**:<br />-2147155455|The webhook call failed because the http request received non-success httpStatus code. Please check your webhook request handler.|
> |**Name**:<br />WebhooksPostDisabled<br />**Hex**:<br />80050206<br />**Number**:<br />-2147155450|The Webhook post is disabled for the organization.|
> |**Name**:<br />WebhooksPostRequestFailed<br />**Hex**:<br />80050205<br />**Number**:<br />-2147155451|The webhook call failed during http post. Please check the exception for more details.|
> |**Name**:<br />WebResourceContentSizeExceeded<br />**Hex**:<br />8004F114<br />**Number**:<br />-2147159788|Webresource content size is too big.|
> |**Name**:<br />WebResourceDuplicateName<br />**Hex**:<br />8004F115<br />**Number**:<br />-2147159787|A webresource with the same name already exists. Use a different name.|
> |**Name**:<br />WebResourceEmptyName<br />**Hex**:<br />8004F116<br />**Number**:<br />-2147159786|Webresource name cannot be null or empty.|
> |**Name**:<br />WebResourceEmptySilverlightVersion<br />**Hex**:<br />8004F112<br />**Number**:<br />-2147159790|Silverlight version cannot be empty for silverlight web resources.|
> |**Name**:<br />WebResourceImportError<br />**Hex**:<br />8004F11B<br />**Number**:<br />-2147159781|An error occurred while importing a Web resource. Try importing this solution again. For further assistance, contact Microsoft Dynamics 365 technical support.|
> |**Name**:<br />WebResourceImportMissingFile<br />**Hex**:<br />8004F11A<br />**Number**:<br />-2147159782|The file for this Web resource does not exist in the solution file.|
> |**Name**:<br />WebResourceInvalidSilverlightVersion<br />**Hex**:<br />8004F113<br />**Number**:<br />-2147159789|Silverlight version can only be of the format xx.xx[.xx.xx].|
> |**Name**:<br />WebResourceInvalidType<br />**Hex**:<br />8004F111<br />**Number**:<br />-2147159791|Invalid web resource type specified.|
> |**Name**:<br />WebResourceNameInvalidCharacters<br />**Hex**:<br />8004F117<br />**Number**:<br />-2147159785|Web resource names may only include letters, numbers, periods, and nonconsecutive forward slash characters.|
> |**Name**:<br />WebResourceNameInvalidFileExtension<br />**Hex**:<br />8004F119<br />**Number**:<br />-2147159783|A Web resource cannot have the following file extensions: .aspx, .ascx, .asmx or .ashx.|
> |**Name**:<br />WebResourceNameInvalidPrefix<br />**Hex**:<br />8004F118<br />**Number**:<br />-2147159784|Webresource name does not contain a valid prefix.|
> |**Name**:<br />WopiApplicationUrl<br />**Hex**:<br />80060802<br />**Number**:<br />-2147088382|Error in retrieving information from WOPI application url.|
> |**Name**:<br />WopiDiscoveryFailed<br />**Hex**:<br />80060800<br />**Number**:<br />-2147088384|Request for retrieving the WOPI discovery XML failed.|
> |**Name**:<br />WopiMaxFileSizeExceeded<br />**Hex**:<br />80060803<br />**Number**:<br />-2147088381|{0} file exceeded size limit of {1}.|
> |**Name**:<br />WordTemplateFeatureNotEnabled<br />**Hex**:<br />800608DB<br />**Number**:<br />-2147088165|Word document template feature is not enabled.|
> |**Name**:<br />WorkflowActivityNotSupported<br />**Hex**:<br />80045045<br />**Number**:<br />-2147200955|This workflow cannot be created, updated or published because it's referring unsupported workflow step.|
> |**Name**:<br />WorkflowAutomaticallyDeactivated<br />**Hex**:<br />80045042<br />**Number**:<br />-2147200958|The original workflow definition has been deactivated and replaced.|
> |**Name**:<br />WorkflowCompileFailure<br />**Hex**:<br />80045001<br />**Number**:<br />-2147201023|An error has occurred during compilation of the workflow.|
> |**Name**:<br />WorkflowConditionIncorrectBinaryOperatorFormation<br />**Hex**:<br />80045011<br />**Number**:<br />-2147201007|Incorrect formation of binary operator.|
> |**Name**:<br />WorkflowConditionIncorrectUnaryOperatorFormation<br />**Hex**:<br />80045010<br />**Number**:<br />-2147201008|Incorrect formation of unary operator.|
> |**Name**:<br />WorkflowConditionOperatorNotSupported<br />**Hex**:<br />80045012<br />**Number**:<br />-2147201006|Condition operator not supported for specified type.|
> |**Name**:<br />WorkflowConditionTypeNotSupport<br />**Hex**:<br />80045013<br />**Number**:<br />-2147201005|Invalid type specified on condition.|
> |**Name**:<br />WorkflowDoesNotExist<br />**Hex**:<br />8006040b<br />**Number**:<br />-2147089397|Workflow does not exist.|
> |**Name**:<br />WorkflowExpressionOperatorNotSupported<br />**Hex**:<br />8004502E<br />**Number**:<br />-2147200978|Expression operator not supported for specified type.|
> |**Name**:<br />WorkflowIdIsNull<br />**Hex**:<br />80060400<br />**Number**:<br />-2147089408|Workflow Id cannot be NULL while creating business process flow category|
> |**Name**:<br />WorkflowIsNotActive<br />**Hex**:<br />80045055<br />**Number**:<br />-2147200939|Workflow must be active to be used on Action Step.|
> |**Name**:<br />WorkflowIsNotOnDemand<br />**Hex**:<br />80045059<br />**Number**:<br />-2147200935|Workflow must be marked as On Demand.|
> |**Name**:<br />WorkflowPublishedByNonOwner<br />**Hex**:<br />8004500B<br />**Number**:<br />-2147201013|The workflow cannot be published or unpublished by someone who is not its owner.|
> |**Name**:<br />WorkflowPublishNoActivationParameters<br />**Hex**:<br />80045018<br />**Number**:<br />-2147201000|Automatic workflow cannot be published if no activation parameters have been specified.|
> |**Name**:<br />WorkflowReferencesInvalidActivity<br />**Hex**:<br />80045038<br />**Number**:<br />-2147200968|The workflow definition contains a step that references and invalid custom activity. Remove the invalid references and try again.|
> |**Name**:<br />WorkflowSystemPaused<br />**Hex**:<br />80045017<br />**Number**:<br />-2147201001|Workflow should be paused by system.|
> |**Name**:<br />WorkflowValidationFailure<br />**Hex**:<br />80045014<br />**Number**:<br />-2147201004|Validation failed on the specified workflow.|
> |**Name**:<br />WrongNumberOfBooleanOptions<br />**Hex**:<br />8004431B<br />**Number**:<br />-2147204325|Boolean attributes must have exactly two option values.|
> |**Name**:<br />XamlNotFound<br />**Hex**:<br />80154B4F<br />**Number**:<br />-2146088113|This feature is not available in offline mode.|
> |**Name**:<br />XlsxExportGeneratingExcelFailed<br />**Hex**:<br />800608C7<br />**Number**:<br />-2147088185|Failed to generate excel.|
> |**Name**:<br />XlsxImportColumnHeadersInvalid<br />**Hex**:<br />800608C6<br />**Number**:<br />-2147088186|Invalid columns.|
> |**Name**:<br />XlsxImportExcelFailed<br />**Hex**:<br />800608C8<br />**Number**:<br />-2147088184|Failed to import data.|
> |**Name**:<br />XlsxImportHiddenColumnAbsent<br />**Hex**:<br />800608C4<br />**Number**:<br />-2147088188|Required columns missing.|
> |**Name**:<br />XlsxImportInvalidColumnCount<br />**Hex**:<br />800608C5<br />**Number**:<br />-2147088187|Column mismatch.|
> |**Name**:<br />XlsxImportInvalidExcelDocument<br />**Hex**:<br />800608C2<br />**Number**:<br />-2147088190|Invalid file to import.|
> |**Name**:<br />XlsxImportInvalidFileData<br />**Hex**:<br />800608C3<br />**Number**:<br />-2147088189|Invalid format in import file.|
> |**Name**:<br />YammerAuthTimedOut<br />**Hex**:<br />8005F107<br />**Number**:<br />-2147094265|You have waited too long to complete the Yammer authorization. Please try again.|
> |**Name**:<br />YValuesPerPointMeasureMismatch<br />**Hex**:<br />8004E004<br />**Number**:<br />-2147164156|Number of YValuesPerPoint for series and number of measures for measure collection for category should be same.|
> |**Name**:<br />ZeroEmailReceived<br />**Hex**:<br />8005E231<br />**Number**:<br />-2147098063|There were no email available in the mailbox or could not be retrieved.|
> |**Name**:<br />ZipFileHasMixOfCsvAndXmlFiles<br />**Hex**:<br />80048485<br />**Number**:<br />-2147187579|The compressed (.zip) file that you're trying to upload contains more than one type of file. The file can contain either Excel (.xlsx) files, comma-delimited (.csv) files or XML Spreadsheet 2003 (.xml) files, but not a combination of file types.|
> |**Name**:<br />ZipInsideZip<br />**Hex**:<br />80048489<br />**Number**:<br />-2147187575|The compressed (.zip) file that you are trying to upload contains another .zip file within it.|

### See also

[Handle exceptions in your code](handle-exceptions-code.md)