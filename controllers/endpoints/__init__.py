from fastapi import FastAPI

from . import AnalyticAccount
from . import BankAccounts
from . import Blog
from . import BlogPost
from . import Companies
from . import Contact
from . import DiscussionChannel
from . import EmailCCmanagement
from . import EmailThread
from . import MailBlacklist
from . import MailBlacklistmixin
from . import MailMainAttachmentmanagement
from . import PhoneBlacklist
from . import PhoneBlacklistMixin
from . import Pricelist
from . import Product
from . import ProductVariant
from . import RatingMixin
from . import TwoFactorSetupWizard
from . import APIKeyDescription
from . import AccessGroups
from . import ActionURL
from . import ActionWindow
from . import ActionWindowClose
from . import ActionWindowView
from . import Actions
from . import Activity
from . import ActivityMixin
from . import ActivityPlan
from . import ActivityType
from . import Activityplantemplate
from . import ActivityscheduleplanWizard
from . import AllWebsiteRoute
from . import AnalyticDistributionModel
from . import AnalyticLine
from . import AnalyticMixin
from . import AnalyticPlansApplicabilities
from . import AnalyticPlans
from . import Application
from . import Asset
from . import Attachment
from . import AttributeValue
from . import AuthenticationDevice
from . import AvatarMixin
from . import Bank
from . import BarcodeNomenclature
from . import BarcodeRule
from . import BaseImport
from . import BaseImportMapping
from . import BlogTag
from . import BlogTagCategory
from . import CampaignStage
from . import CannedResponseShortcode
from . import ChangePasswordWizard
from . import ChannelMember
from . import ChatbotMessage
from . import ChatbotScript
from . import ChatbotScriptAnswer
from . import ChatbotScriptStep
from . import Choosethesheetlayouttoprintthelabels
from . import ClientAction
from . import CommunicationBus
from . import CompanyDocumentLayout
from . import CompanyProperty
from . import Config
from . import ConfigInstaller
from . import ConfigSettings
from . import ConfigurationWizards
from . import Copyofashareddashboard
from . import Country
from . import CountryGroup
from . import Countrystate
from . import CoverPropertiesWebsiteMixin
from . import CreateMenuWizard
from . import Crondatausedforwebpushnotification
from . import Currency
from . import CurrencyRate
from . import CustomView
from . import DecimalPrecision
from . import DefaultValues
from . import Demo
from . import DemoFailurewizard
from . import Demofailure
from . import Digest
from . import DigestTips
from . import DocumentFollowers
from . import EmailAliases
from . import EmailAliasesMixin
from . import EmailAliasesMixinlight
from . import EmailDomain
from . import EmailTemplatePreview
from . import EmailTemplates
from . import Emailcompositionwizard
from . import Emailresendwizard
from . import Enableprofilingforsometime
from . import Exports
from . import ExportsLine
from . import FieldhtmlHistory
from . import Fields
from . import FieldsSelection
from . import Filters
from . import FormatErrorSendingaSnailmailLetter
from . import GeneratePaymentLink
from . import GeoProvider
from . import GoogleGmailMixin
from . import GrantPortalAccess
from . import Groupofdashboards
from . import Guest
from . import IAPAccount
from . import IAPAccountInfo
from . import ICEserver
from . import ImageMixin
from . import ImportModule
from . import IncomingMailServer
from . import Industry
from . import InstallLanguage
from . import Invitewizard
from . import LanguageExport
from . import LanguageImport
from . import Languages
from . import LinkSMStomailingsmstrackingmodels
from . import LivechatChannel
from . import LivechatChannelRules
from . import LivechatSupportChannelReport
from . import LivechatSupportOperatorReport
from . import Logging
from . import MailComposerMixin
from . import MailGatewayAllowed
from . import MailRTCsession
from . import MailRenderMixin
from . import MailServer
from . import MailTemplateReset
from . import MailTrackingValue
from . import Menu
from . import MergePartnerLine
from . import MergePartnerWizard
from . import Message
from . import MessageNotifications
from . import MessageReaction
from . import MessageTranslation
from . import Messagesubtypes
from . import Metadataforvoiceattachments
from . import MixintocomputethetimearecordhasspentineachvalueamanyTwoonefieldcantake
from . import ModelAccess
from . import ModelConstraint
from . import ModelData
from . import ModelInheritanceTree
from . import ModelPage
from . import Models
from . import Module
from . import ModuleActivationRequest
from . import ModuleActivationReview
from . import ModuleUninstall
from . import Moduledependency
from . import Moduleexclusion
from . import MultiWebsiteMixin
from . import MultiWebsitePublishedMixin
from . import Onboarding
from . import OnboardingProgressStepTracker
from . import OnboardingProgressTracker
from . import OnboardingStep
from . import OutgoingMails
from . import OutgoingSMS
from . import Page
from . import PaperFormatConfig
from . import PartnerAutocompleteSync
from . import PartnerTags
from . import PartnerTitle
from . import PartnerWebPushDevice
from . import Partnerwithadditionalinformationformailresend
from . import PasswordCheckWizard
from . import PaymentCaptureWizard
from . import PaymentMethod
from . import PaymentProvider
from . import PaymentToken
from . import PaymentTransaction
from . import Paymentprovideronboardingwizard
from . import PortalMixin
from . import PortalSharing
from . import PortalUserConfig
from . import PricelistRule
from . import PrivacyLog
from . import PrivacyLookupWizard
from . import PrivacyLookupWizardLine
from . import ProductAttribute
from . import ProductAttributeCustomValue
from . import ProductCategory
from . import ProductDocument
from . import ProductPackaging
from . import ProductTag
from . import ProductTemplateAttributeExclusion
from . import ProductTemplateAttributeLine
from . import ProductTemplateAttributeValue
from . import ProductUnitofMeasure
from . import ProductUoMCategories
from . import Profilingresults
from . import Rating
from . import RatingParentMixin
from . import RecordRule
from . import RelationModel
from . import Removeemailfromblacklistwizard
from . import Removephonefromblacklist
from . import ReportAction
from . import ReportLayout
from . import ResendNotification
from . import ResetViewArchitectureWizard
from . import ResourceMixin
from . import ResourceTimeOffDetail
from . import ResourceWorkingTime
from . import Resources
from . import RobotstxtEditor
from . import SEOmetadata
from . import SMSResend
from . import SMSTemplatePreview
from . import SMSTemplateReset
from . import SMSTemplates
from . import SavefavoriteGIFfromTenorAPI
from . import ScheduledActions
from . import ScheduledMessages
from . import SendSMSWizard
from . import Sequence
from . import SequenceDateRange
from . import ServerActions
from . import ShowAPIKey
from . import SnailmailLetter
from . import SpreadsheetDashboard
from . import Spreadsheetmixin
from . import Storelinkpreviewdata
from . import SupplierPricelist
from . import SystemParameter
from . import TemplateResetMixin
from . import ThemeAsset
from . import ThemeAttachments
from . import ThemeUIView
from . import Tours
from . import Triggeredactions
from . import UTMCampaign
from . import UTMMedium
from . import UTMMixin
from . import UTMSource
from . import UTMSourceMixin
from . import UTMTag
from . import UpdateModule
from . import Updateaddressofpartner
from . import UpgradeModule
from . import User
from . import UserPresence
from . import UserSettings
from . import UserSettingsVolumes
from . import UserChangePasswordWizard
from . import Userchangeownpasswordwizard
from . import UsersAPIKeys
from . import UsersDeletionRequest
from . import UsersLog
from . import View
from . import VisitedPages
from . import WebEditorConverterSubtest
from . import WebEditorConverterTest
from . import Website
from . import WebsiteConfiguratorFeature
from . import WebsiteMenu
from . import WebsitePublishedMixin
from . import WebsiteSnippetFilter
from . import WebsiteThemeMenu
from . import WebsiteThemePage
from . import WebsiteVisitor
from . import Websiterewrite
from . import WorkDetail

app = FastAPI()

app.include_router(AnalyticAccount.router)
app.include_router(BankAccounts.router)
app.include_router(Blog.router)
app.include_router(BlogPost.router)
app.include_router(Companies.router)
app.include_router(Contact.router)
app.include_router(DiscussionChannel.router)
app.include_router(EmailCCmanagement.router)
app.include_router(EmailThread.router)
app.include_router(MailBlacklist.router)
app.include_router(MailBlacklistmixin.router)
app.include_router(MailMainAttachmentmanagement.router)
app.include_router(PhoneBlacklist.router)
app.include_router(PhoneBlacklistMixin.router)
app.include_router(Pricelist.router)
app.include_router(Product.router)
app.include_router(ProductVariant.router)
app.include_router(RatingMixin.router)
app.include_router(TwoFactorSetupWizard.router)
app.include_router(APIKeyDescription.router)
app.include_router(AccessGroups.router)
app.include_router(ActionURL.router)
app.include_router(ActionWindow.router)
app.include_router(ActionWindowClose.router)
app.include_router(ActionWindowView.router)
app.include_router(Actions.router)
app.include_router(Activity.router)
app.include_router(ActivityMixin.router)
app.include_router(ActivityPlan.router)
app.include_router(ActivityType.router)
app.include_router(Activityplantemplate.router)
app.include_router(ActivityscheduleplanWizard.router)
app.include_router(AllWebsiteRoute.router)
app.include_router(AnalyticDistributionModel.router)
app.include_router(AnalyticLine.router)
app.include_router(AnalyticMixin.router)
app.include_router(AnalyticPlansApplicabilities.router)
app.include_router(AnalyticPlans.router)
app.include_router(Application.router)
app.include_router(Asset.router)
app.include_router(Attachment.router)
app.include_router(AttributeValue.router)
app.include_router(AuthenticationDevice.router)
app.include_router(AvatarMixin.router)
app.include_router(Bank.router)
app.include_router(BarcodeNomenclature.router)
app.include_router(BarcodeRule.router)
app.include_router(BaseImport.router)
app.include_router(BaseImportMapping.router)
app.include_router(BlogTag.router)
app.include_router(BlogTagCategory.router)
app.include_router(CampaignStage.router)
app.include_router(CannedResponseShortcode.router)
app.include_router(ChangePasswordWizard.router)
app.include_router(ChannelMember.router)
app.include_router(ChatbotMessage.router)
app.include_router(ChatbotScript.router)
app.include_router(ChatbotScriptAnswer.router)
app.include_router(ChatbotScriptStep.router)
app.include_router(Choosethesheetlayouttoprintthelabels.router)
app.include_router(ClientAction.router)
app.include_router(CommunicationBus.router)
app.include_router(CompanyDocumentLayout.router)
app.include_router(CompanyProperty.router)
app.include_router(Config.router)
app.include_router(ConfigInstaller.router)
app.include_router(ConfigSettings.router)
app.include_router(ConfigurationWizards.router)
app.include_router(Copyofashareddashboard.router)
app.include_router(Country.router)
app.include_router(CountryGroup.router)
app.include_router(Countrystate.router)
app.include_router(CoverPropertiesWebsiteMixin.router)
app.include_router(CreateMenuWizard.router)
app.include_router(Crondatausedforwebpushnotification.router)
app.include_router(Currency.router)
app.include_router(CurrencyRate.router)
app.include_router(CustomView.router)
app.include_router(DecimalPrecision.router)
app.include_router(DefaultValues.router)
app.include_router(Demo.router)
app.include_router(DemoFailurewizard.router)
app.include_router(Demofailure.router)
app.include_router(Digest.router)
app.include_router(DigestTips.router)
app.include_router(DocumentFollowers.router)
app.include_router(EmailAliases.router)
app.include_router(EmailAliasesMixin.router)
app.include_router(EmailAliasesMixinlight.router)
app.include_router(EmailDomain.router)
app.include_router(EmailTemplatePreview.router)
app.include_router(EmailTemplates.router)
app.include_router(Emailcompositionwizard.router)
app.include_router(Emailresendwizard.router)
app.include_router(Enableprofilingforsometime.router)
app.include_router(Exports.router)
app.include_router(ExportsLine.router)
app.include_router(FieldhtmlHistory.router)
app.include_router(Fields.router)
app.include_router(FieldsSelection.router)
app.include_router(Filters.router)
app.include_router(FormatErrorSendingaSnailmailLetter.router)
app.include_router(GeneratePaymentLink.router)
app.include_router(GeoProvider.router)
app.include_router(GoogleGmailMixin.router)
app.include_router(GrantPortalAccess.router)
app.include_router(Groupofdashboards.router)
app.include_router(Guest.router)
app.include_router(IAPAccount.router)
app.include_router(IAPAccountInfo.router)
app.include_router(ICEserver.router)
app.include_router(ImageMixin.router)
app.include_router(ImportModule.router)
app.include_router(IncomingMailServer.router)
app.include_router(Industry.router)
app.include_router(InstallLanguage.router)
app.include_router(Invitewizard.router)
app.include_router(LanguageExport.router)
app.include_router(LanguageImport.router)
app.include_router(Languages.router)
app.include_router(LinkSMStomailingsmstrackingmodels.router)
app.include_router(LivechatChannel.router)
app.include_router(LivechatChannelRules.router)
app.include_router(LivechatSupportChannelReport.router)
app.include_router(LivechatSupportOperatorReport.router)
app.include_router(Logging.router)
app.include_router(MailComposerMixin.router)
app.include_router(MailGatewayAllowed.router)
app.include_router(MailRTCsession.router)
app.include_router(MailRenderMixin.router)
app.include_router(MailServer.router)
app.include_router(MailTemplateReset.router)
app.include_router(MailTrackingValue.router)
app.include_router(Menu.router)
app.include_router(MergePartnerLine.router)
app.include_router(MergePartnerWizard.router)
app.include_router(Message.router)
app.include_router(MessageNotifications.router)
app.include_router(MessageReaction.router)
app.include_router(MessageTranslation.router)
app.include_router(Messagesubtypes.router)
app.include_router(Metadataforvoiceattachments.router)
app.include_router(MixintocomputethetimearecordhasspentineachvalueamanyTwoonefieldcantake.router)
app.include_router(ModelAccess.router)
app.include_router(ModelConstraint.router)
app.include_router(ModelData.router)
app.include_router(ModelInheritanceTree.router)
app.include_router(ModelPage.router)
app.include_router(Models.router)
app.include_router(Module.router)
app.include_router(ModuleActivationRequest.router)
app.include_router(ModuleActivationReview.router)
app.include_router(ModuleUninstall.router)
app.include_router(Moduledependency.router)
app.include_router(Moduleexclusion.router)
app.include_router(MultiWebsiteMixin.router)
app.include_router(MultiWebsitePublishedMixin.router)
app.include_router(Onboarding.router)
app.include_router(OnboardingProgressStepTracker.router)
app.include_router(OnboardingProgressTracker.router)
app.include_router(OnboardingStep.router)
app.include_router(OutgoingMails.router)
app.include_router(OutgoingSMS.router)
app.include_router(Page.router)
app.include_router(PaperFormatConfig.router)
app.include_router(PartnerAutocompleteSync.router)
app.include_router(PartnerTags.router)
app.include_router(PartnerTitle.router)
app.include_router(PartnerWebPushDevice.router)
app.include_router(Partnerwithadditionalinformationformailresend.router)
app.include_router(PasswordCheckWizard.router)
app.include_router(PaymentCaptureWizard.router)
app.include_router(PaymentMethod.router)
app.include_router(PaymentProvider.router)
app.include_router(PaymentToken.router)
app.include_router(PaymentTransaction.router)
app.include_router(Paymentprovideronboardingwizard.router)
app.include_router(PortalMixin.router)
app.include_router(PortalSharing.router)
app.include_router(PortalUserConfig.router)
app.include_router(PricelistRule.router)
app.include_router(PrivacyLog.router)
app.include_router(PrivacyLookupWizard.router)
app.include_router(PrivacyLookupWizardLine.router)
app.include_router(ProductAttribute.router)
app.include_router(ProductAttributeCustomValue.router)
app.include_router(ProductCategory.router)
app.include_router(ProductDocument.router)
app.include_router(ProductPackaging.router)
app.include_router(ProductTag.router)
app.include_router(ProductTemplateAttributeExclusion.router)
app.include_router(ProductTemplateAttributeLine.router)
app.include_router(ProductTemplateAttributeValue.router)
app.include_router(ProductUnitofMeasure.router)
app.include_router(ProductUoMCategories.router)
app.include_router(Profilingresults.router)
app.include_router(Rating.router)
app.include_router(RatingParentMixin.router)
app.include_router(RecordRule.router)
app.include_router(RelationModel.router)
app.include_router(Removeemailfromblacklistwizard.router)
app.include_router(Removephonefromblacklist.router)
app.include_router(ReportAction.router)
app.include_router(ReportLayout.router)
app.include_router(ResendNotification.router)
app.include_router(ResetViewArchitectureWizard.router)
app.include_router(ResourceMixin.router)
app.include_router(ResourceTimeOffDetail.router)
app.include_router(ResourceWorkingTime.router)
app.include_router(Resources.router)
app.include_router(RobotstxtEditor.router)
app.include_router(SEOmetadata.router)
app.include_router(SMSResend.router)
app.include_router(SMSTemplatePreview.router)
app.include_router(SMSTemplateReset.router)
app.include_router(SMSTemplates.router)
app.include_router(SavefavoriteGIFfromTenorAPI.router)
app.include_router(ScheduledActions.router)
app.include_router(ScheduledMessages.router)
app.include_router(SendSMSWizard.router)
app.include_router(Sequence.router)
app.include_router(SequenceDateRange.router)
app.include_router(ServerActions.router)
app.include_router(ShowAPIKey.router)
app.include_router(SnailmailLetter.router)
app.include_router(SpreadsheetDashboard.router)
app.include_router(Spreadsheetmixin.router)
app.include_router(Storelinkpreviewdata.router)
app.include_router(SupplierPricelist.router)
app.include_router(SystemParameter.router)
app.include_router(TemplateResetMixin.router)
app.include_router(ThemeAsset.router)
app.include_router(ThemeAttachments.router)
app.include_router(ThemeUIView.router)
app.include_router(Tours.router)
app.include_router(Triggeredactions.router)
app.include_router(UTMCampaign.router)
app.include_router(UTMMedium.router)
app.include_router(UTMMixin.router)
app.include_router(UTMSource.router)
app.include_router(UTMSourceMixin.router)
app.include_router(UTMTag.router)
app.include_router(UpdateModule.router)
app.include_router(Updateaddressofpartner.router)
app.include_router(UpgradeModule.router)
app.include_router(User.router)
app.include_router(UserPresence.router)
app.include_router(UserSettings.router)
app.include_router(UserSettingsVolumes.router)
app.include_router(UserChangePasswordWizard.router)
app.include_router(Userchangeownpasswordwizard.router)
app.include_router(UsersAPIKeys.router)
app.include_router(UsersDeletionRequest.router)
app.include_router(UsersLog.router)
app.include_router(View.router)
app.include_router(VisitedPages.router)
app.include_router(WebEditorConverterSubtest.router)
app.include_router(WebEditorConverterTest.router)
app.include_router(Website.router)
app.include_router(WebsiteConfiguratorFeature.router)
app.include_router(WebsiteMenu.router)
app.include_router(WebsitePublishedMixin.router)
app.include_router(WebsiteSnippetFilter.router)
app.include_router(WebsiteThemeMenu.router)
app.include_router(WebsiteThemePage.router)
app.include_router(WebsiteVisitor.router)
app.include_router(Websiterewrite.router)
app.include_router(WorkDetail.router)
