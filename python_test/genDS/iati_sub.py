#!/usr/bin/env python

#
# Generated Wed Apr 22 11:22:16 2015 by generateDS.py version 2.15b.
#
# Command line options:
#   ('-o', 'iati.py')
#   ('-s', 'iati_sub.py')
#
# Command line arguments:
#   iati-activities-schema.xsd
#
# Command line:
#   /home/daan/.virtualenvs/datapool/bin/generateDS.py -o "iati.py" -s "iati_sub.py" iati-activities-schema.xsd
#
# Current working directory (os.getcwd()):
#   genDS
#

import sys
from lxml import etree as etree_

import ??? as supermod

def parsexml_(*args, **kwargs):
    if 'parser' not in kwargs:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        kwargs['parser'] = etree_.ETCompatXMLParser()
    doc = etree_.parse(*args, **kwargs)
    return doc

#
# Globals
#

ExternalEncoding = 'utf-8'

#
# Data representation classes
#


class iati_activitiesSub(supermod.iati_activities):
    def __init__(self, generated_datetime=None, version=None, linked_data_default=None, iati_activity=None, anytypeobjs_=None):
        super(iati_activitiesSub, self).__init__(generated_datetime, version, linked_data_default, iati_activity, anytypeobjs_, )
supermod.iati_activities.subclass = iati_activitiesSub
# end class iati_activitiesSub


class iati_activitySub(supermod.iati_activity):
    def __init__(self, lang=None, last_updated_datetime=None, linked_data_uri=None, hierarchy=None, default_currency=None, iati_identifier=None, reporting_org=None, title=None, description=None, participating_org=None, other_identifier=None, activity_status=None, activity_date=None, contact_info=None, activity_scope=None, recipient_country=None, recipient_region=None, location=None, sector=None, country_budget_items=None, policy_marker=None, collaboration_type=None, default_flow_type=None, default_finance_type=None, default_aid_type=None, default_tied_status=None, budget=None, planned_disbursement=None, capital_spend=None, transaction=None, document_link=None, related_activity=None, legacy_data=None, conditions=None, result=None, crs_add=None, fss=None, anytypeobjs_=None):
        super(iati_activitySub, self).__init__(lang, last_updated_datetime, linked_data_uri, hierarchy, default_currency, iati_identifier, reporting_org, title, description, participating_org, other_identifier, activity_status, activity_date, contact_info, activity_scope, recipient_country, recipient_region, location, sector, country_budget_items, policy_marker, collaboration_type, default_flow_type, default_finance_type, default_aid_type, default_tied_status, budget, planned_disbursement, capital_spend, transaction, document_link, related_activity, legacy_data, conditions, result, crs_add, fss, anytypeobjs_, )
supermod.iati_activity.subclass = iati_activitySub
# end class iati_activitySub


class iati_identifierSub(supermod.iati_identifier):
    def __init__(self, valueOf_=None):
        super(iati_identifierSub, self).__init__(valueOf_, )
supermod.iati_identifier.subclass = iati_identifierSub
# end class iati_identifierSub


class participating_orgSub(supermod.participating_org):
    def __init__(self, type_=None, role=None, ref=None, narrative=None, anytypeobjs_=None):
        super(participating_orgSub, self).__init__(type_, role, ref, narrative, anytypeobjs_, )
supermod.participating_org.subclass = participating_orgSub
# end class participating_orgSub


class activity_scopeSub(supermod.activity_scope):
    def __init__(self, code=None, anytypeobjs_=None):
        super(activity_scopeSub, self).__init__(code, anytypeobjs_, )
supermod.activity_scope.subclass = activity_scopeSub
# end class activity_scopeSub


class recipient_countrySub(supermod.recipient_country):
    def __init__(self, percentage=None, code=None, narrative=None, anytypeobjs_=None):
        super(recipient_countrySub, self).__init__(percentage, code, narrative, anytypeobjs_, )
supermod.recipient_country.subclass = recipient_countrySub
# end class recipient_countrySub


class recipient_regionSub(supermod.recipient_region):
    def __init__(self, percentage=None, code=None, vocabulary=None, narrative=None, anytypeobjs_=None):
        super(recipient_regionSub, self).__init__(percentage, code, vocabulary, narrative, anytypeobjs_, )
supermod.recipient_region.subclass = recipient_regionSub
# end class recipient_regionSub


class collaboration_typeSub(supermod.collaboration_type):
    def __init__(self, code=None, anytypeobjs_=None):
        super(collaboration_typeSub, self).__init__(code, anytypeobjs_, )
supermod.collaboration_type.subclass = collaboration_typeSub
# end class collaboration_typeSub


class default_flow_typeSub(supermod.default_flow_type):
    def __init__(self, code=None, anytypeobjs_=None):
        super(default_flow_typeSub, self).__init__(code, anytypeobjs_, )
supermod.default_flow_type.subclass = default_flow_typeSub
# end class default_flow_typeSub


class default_aid_typeSub(supermod.default_aid_type):
    def __init__(self, code=None, anytypeobjs_=None):
        super(default_aid_typeSub, self).__init__(code, anytypeobjs_, )
supermod.default_aid_type.subclass = default_aid_typeSub
# end class default_aid_typeSub


class default_finance_typeSub(supermod.default_finance_type):
    def __init__(self, code=None, anytypeobjs_=None):
        super(default_finance_typeSub, self).__init__(code, anytypeobjs_, )
supermod.default_finance_type.subclass = default_finance_typeSub
# end class default_finance_typeSub


class other_identifierSub(supermod.other_identifier):
    def __init__(self, type_=None, ref=None, owner_org=None, anytypeobjs_=None):
        super(other_identifierSub, self).__init__(type_, ref, owner_org, anytypeobjs_, )
supermod.other_identifier.subclass = other_identifierSub
# end class other_identifierSub


class sectorSub(supermod.sector):
    def __init__(self, percentage=None, code=None, vocabulary=None, narrative=None, anytypeobjs_=None):
        super(sectorSub, self).__init__(percentage, code, vocabulary, narrative, anytypeobjs_, )
supermod.sector.subclass = sectorSub
# end class sectorSub


class activity_dateSub(supermod.activity_date):
    def __init__(self, iso_date=None, type_=None, narrative=None, anytypeobjs_=None):
        super(activity_dateSub, self).__init__(iso_date, type_, narrative, anytypeobjs_, )
supermod.activity_date.subclass = activity_dateSub
# end class activity_dateSub


class activity_statusSub(supermod.activity_status):
    def __init__(self, code=None, anytypeobjs_=None):
        super(activity_statusSub, self).__init__(code, anytypeobjs_, )
supermod.activity_status.subclass = activity_statusSub
# end class activity_statusSub


class contact_infoSub(supermod.contact_info):
    def __init__(self, type_=None, organisation=None, department=None, person_name=None, job_title=None, telephone=None, email=None, website=None, mailing_address=None, anytypeobjs_=None):
        super(contact_infoSub, self).__init__(type_, organisation, department, person_name, job_title, telephone, email, website, mailing_address, anytypeobjs_, )
supermod.contact_info.subclass = contact_infoSub
# end class contact_infoSub


class default_tied_statusSub(supermod.default_tied_status):
    def __init__(self, code=None, anytypeobjs_=None):
        super(default_tied_statusSub, self).__init__(code, anytypeobjs_, )
supermod.default_tied_status.subclass = default_tied_statusSub
# end class default_tied_statusSub


class policy_markerSub(supermod.policy_marker):
    def __init__(self, code=None, vocabulary=None, significance=None, narrative=None, anytypeobjs_=None):
        super(policy_markerSub, self).__init__(code, vocabulary, significance, narrative, anytypeobjs_, )
supermod.policy_marker.subclass = policy_markerSub
# end class policy_markerSub


class capital_spendSub(supermod.capital_spend):
    def __init__(self, percentage=None, anytypeobjs_=None):
        super(capital_spendSub, self).__init__(percentage, anytypeobjs_, )
supermod.capital_spend.subclass = capital_spendSub
# end class capital_spendSub


class transactionSub(supermod.transaction):
    def __init__(self, ref=None, transaction_type=None, transaction_date=None, value=None, description=None, provider_org=None, receiver_org=None, disbursement_channel=None, sector=None, recipient_country=None, recipient_region=None, flow_type=None, finance_type=None, aid_type=None, tied_status=None, anytypeobjs_=None):
        super(transactionSub, self).__init__(ref, transaction_type, transaction_date, value, description, provider_org, receiver_org, disbursement_channel, sector, recipient_country, recipient_region, flow_type, finance_type, aid_type, tied_status, anytypeobjs_, )
supermod.transaction.subclass = transactionSub
# end class transactionSub


class locationSub(supermod.location):
    def __init__(self, ref=None, location_reach=None, location_id=None, name=None, description=None, activity_description=None, administrative=None, point=None, exactness=None, location_class=None, feature_designation=None, anytypeobjs_=None):
        super(locationSub, self).__init__(ref, location_reach, location_id, name, description, activity_description, administrative, point, exactness, location_class, feature_designation, anytypeobjs_, )
supermod.location.subclass = locationSub
# end class locationSub


class country_budget_itemsSub(supermod.country_budget_items):
    def __init__(self, vocabulary=None, budget_item=None, anytypeobjs_=None):
        super(country_budget_itemsSub, self).__init__(vocabulary, budget_item, anytypeobjs_, )
supermod.country_budget_items.subclass = country_budget_itemsSub
# end class country_budget_itemsSub


class related_activitySub(supermod.related_activity):
    def __init__(self, type_=None, ref=None, anytypeobjs_=None):
        super(related_activitySub, self).__init__(type_, ref, anytypeobjs_, )
supermod.related_activity.subclass = related_activitySub
# end class related_activitySub


class legacy_dataSub(supermod.legacy_data):
    def __init__(self, name=None, value=None, iati_equivalent=None, anytypeobjs_=None):
        super(legacy_dataSub, self).__init__(name, value, iati_equivalent, anytypeobjs_, )
supermod.legacy_data.subclass = legacy_dataSub
# end class legacy_dataSub


class resultSub(supermod.result):
    def __init__(self, type_=None, aggregation_status=None, title=None, description=None, indicator=None, anytypeobjs_=None):
        super(resultSub, self).__init__(type_, aggregation_status, title, description, indicator, anytypeobjs_, )
supermod.result.subclass = resultSub
# end class resultSub


class conditionsSub(supermod.conditions):
    def __init__(self, attached=None, condition=None, anytypeobjs_=None):
        super(conditionsSub, self).__init__(attached, condition, anytypeobjs_, )
supermod.conditions.subclass = conditionsSub
# end class conditionsSub


class budgetSub(supermod.budget):
    def __init__(self, type_=None, period_start=None, period_end=None, value=None, anytypeobjs_=None):
        super(budgetSub, self).__init__(type_, period_start, period_end, value, anytypeobjs_, )
supermod.budget.subclass = budgetSub
# end class budgetSub


class planned_disbursementSub(supermod.planned_disbursement):
    def __init__(self, type_=None, period_start=None, period_end=None, value=None, anytypeobjs_=None):
        super(planned_disbursementSub, self).__init__(type_, period_start, period_end, value, anytypeobjs_, )
supermod.planned_disbursement.subclass = planned_disbursementSub
# end class planned_disbursementSub


class crs_addSub(supermod.crs_add):
    def __init__(self, other_flags=None, loan_terms=None, loan_status=None, anytypeobjs_=None):
        super(crs_addSub, self).__init__(other_flags, loan_terms, loan_status, anytypeobjs_, )
supermod.crs_add.subclass = crs_addSub
# end class crs_addSub


class fssSub(supermod.fss):
    def __init__(self, priority=None, phaseout_year=None, extraction_date=None, forecast=None, anytypeobjs_=None):
        super(fssSub, self).__init__(priority, phaseout_year, extraction_date, forecast, anytypeobjs_, )
supermod.fss.subclass = fssSub
# end class fssSub


class document_linkSub(supermod.document_link):
    def __init__(self, url=None, format=None, title=None, category=None, language=None, anytypeobjs_=None):
        super(document_linkSub, self).__init__(url, format, title, category, language, anytypeobjs_, )
supermod.document_link.subclass = document_linkSub
# end class document_linkSub


class currencyTypeSub(supermod.currencyType):
    def __init__(self, currency=None, value_date=None, valueOf_=None):
        super(currencyTypeSub, self).__init__(currency, value_date, valueOf_, )
supermod.currencyType.subclass = currencyTypeSub
# end class currencyTypeSub


class narrativeSub(supermod.narrative):
    def __init__(self, lang=None, valueOf_=None):
        super(narrativeSub, self).__init__(lang, valueOf_, )
supermod.narrative.subclass = narrativeSub
# end class narrativeSub


class descriptionSub(supermod.description):
    def __init__(self, narrative=None, anytypeobjs_=None):
        super(descriptionSub, self).__init__(narrative, anytypeobjs_, )
supermod.description.subclass = descriptionSub
# end class descriptionSub


class reporting_orgSub(supermod.reporting_org):
    def __init__(self, type_=None, secondary_reporter=None, ref=None, narrative=None, anytypeobjs_=None):
        super(reporting_orgSub, self).__init__(type_, secondary_reporter, ref, narrative, anytypeobjs_, )
supermod.reporting_org.subclass = reporting_orgSub
# end class reporting_orgSub


class textTypeSub(supermod.textType):
    def __init__(self, narrative=None, anytypeobjs_=None):
        super(textTypeSub, self).__init__(narrative, anytypeobjs_, )
supermod.textType.subclass = textTypeSub
# end class textTypeSub


class textRequiredTypeSub(supermod.textRequiredType):
    def __init__(self, narrative=None, anytypeobjs_=None):
        super(textRequiredTypeSub, self).__init__(narrative, anytypeobjs_, )
supermod.textRequiredType.subclass = textRequiredTypeSub
# end class textRequiredTypeSub


class descriptionTypeSub(supermod.descriptionType):
    def __init__(self, type_=None, narrative=None, anytypeobjs_=None):
        super(descriptionTypeSub, self).__init__(type_, narrative, anytypeobjs_, )
supermod.descriptionType.subclass = descriptionTypeSub
# end class descriptionTypeSub


class owner_orgTypeSub(supermod.owner_orgType):
    def __init__(self, ref=None, narrative=None, anytypeobjs_=None):
        super(owner_orgTypeSub, self).__init__(ref, narrative, anytypeobjs_, )
supermod.owner_orgType.subclass = owner_orgTypeSub
# end class owner_orgTypeSub


class telephoneTypeSub(supermod.telephoneType):
    def __init__(self, valueOf_=None):
        super(telephoneTypeSub, self).__init__(valueOf_, )
supermod.telephoneType.subclass = telephoneTypeSub
# end class telephoneTypeSub


class emailTypeSub(supermod.emailType):
    def __init__(self, valueOf_=None):
        super(emailTypeSub, self).__init__(valueOf_, )
supermod.emailType.subclass = emailTypeSub
# end class emailTypeSub


class websiteTypeSub(supermod.websiteType):
    def __init__(self, valueOf_=None):
        super(websiteTypeSub, self).__init__(valueOf_, )
supermod.websiteType.subclass = websiteTypeSub
# end class websiteTypeSub


class transaction_typeTypeSub(supermod.transaction_typeType):
    def __init__(self, code=None, anytypeobjs_=None):
        super(transaction_typeTypeSub, self).__init__(code, anytypeobjs_, )
supermod.transaction_typeType.subclass = transaction_typeTypeSub
# end class transaction_typeTypeSub


class transaction_dateTypeSub(supermod.transaction_dateType):
    def __init__(self, iso_date=None, anytypeobjs_=None):
        super(transaction_dateTypeSub, self).__init__(iso_date, anytypeobjs_, )
supermod.transaction_dateType.subclass = transaction_dateTypeSub
# end class transaction_dateTypeSub


class provider_orgTypeSub(supermod.provider_orgType):
    def __init__(self, provider_activity_id=None, ref=None, narrative=None, anytypeobjs_=None):
        super(provider_orgTypeSub, self).__init__(provider_activity_id, ref, narrative, anytypeobjs_, )
supermod.provider_orgType.subclass = provider_orgTypeSub
# end class provider_orgTypeSub


class receiver_orgTypeSub(supermod.receiver_orgType):
    def __init__(self, receiver_activity_id=None, ref=None, narrative=None, anytypeobjs_=None):
        super(receiver_orgTypeSub, self).__init__(receiver_activity_id, ref, narrative, anytypeobjs_, )
supermod.receiver_orgType.subclass = receiver_orgTypeSub
# end class receiver_orgTypeSub


class disbursement_channelTypeSub(supermod.disbursement_channelType):
    def __init__(self, code=None, anytypeobjs_=None):
        super(disbursement_channelTypeSub, self).__init__(code, anytypeobjs_, )
supermod.disbursement_channelType.subclass = disbursement_channelTypeSub
# end class disbursement_channelTypeSub


class sectorTypeSub(supermod.sectorType):
    def __init__(self, code=None, vocabulary=None, narrative=None, anytypeobjs_=None):
        super(sectorTypeSub, self).__init__(code, vocabulary, narrative, anytypeobjs_, )
supermod.sectorType.subclass = sectorTypeSub
# end class sectorTypeSub


class recipient_countryTypeSub(supermod.recipient_countryType):
    def __init__(self, code=None, narrative=None, anytypeobjs_=None):
        super(recipient_countryTypeSub, self).__init__(code, narrative, anytypeobjs_, )
supermod.recipient_countryType.subclass = recipient_countryTypeSub
# end class recipient_countryTypeSub


class recipient_regionTypeSub(supermod.recipient_regionType):
    def __init__(self, code=None, vocabulary=None, narrative=None, anytypeobjs_=None):
        super(recipient_regionTypeSub, self).__init__(code, vocabulary, narrative, anytypeobjs_, )
supermod.recipient_regionType.subclass = recipient_regionTypeSub
# end class recipient_regionTypeSub


class flow_typeTypeSub(supermod.flow_typeType):
    def __init__(self, code=None, anytypeobjs_=None):
        super(flow_typeTypeSub, self).__init__(code, anytypeobjs_, )
supermod.flow_typeType.subclass = flow_typeTypeSub
# end class flow_typeTypeSub


class finance_typeTypeSub(supermod.finance_typeType):
    def __init__(self, code=None, anytypeobjs_=None):
        super(finance_typeTypeSub, self).__init__(code, anytypeobjs_, )
supermod.finance_typeType.subclass = finance_typeTypeSub
# end class finance_typeTypeSub


class aid_typeTypeSub(supermod.aid_typeType):
    def __init__(self, code=None, anytypeobjs_=None):
        super(aid_typeTypeSub, self).__init__(code, anytypeobjs_, )
supermod.aid_typeType.subclass = aid_typeTypeSub
# end class aid_typeTypeSub


class tied_statusTypeSub(supermod.tied_statusType):
    def __init__(self, code=None, anytypeobjs_=None):
        super(tied_statusTypeSub, self).__init__(code, anytypeobjs_, )
supermod.tied_statusType.subclass = tied_statusTypeSub
# end class tied_statusTypeSub


class location_reachTypeSub(supermod.location_reachType):
    def __init__(self, code=None, anytypeobjs_=None):
        super(location_reachTypeSub, self).__init__(code, anytypeobjs_, )
supermod.location_reachType.subclass = location_reachTypeSub
# end class location_reachTypeSub


class location_idTypeSub(supermod.location_idType):
    def __init__(self, code=None, vocabulary=None, anytypeobjs_=None):
        super(location_idTypeSub, self).__init__(code, vocabulary, anytypeobjs_, )
supermod.location_idType.subclass = location_idTypeSub
# end class location_idTypeSub


class administrativeTypeSub(supermod.administrativeType):
    def __init__(self, code=None, vocabulary=None, level=None, anytypeobjs_=None):
        super(administrativeTypeSub, self).__init__(code, vocabulary, level, anytypeobjs_, )
supermod.administrativeType.subclass = administrativeTypeSub
# end class administrativeTypeSub


class pointTypeSub(supermod.pointType):
    def __init__(self, srsName=None, pos=None, anytypeobjs_=None):
        super(pointTypeSub, self).__init__(srsName, pos, anytypeobjs_, )
supermod.pointType.subclass = pointTypeSub
# end class pointTypeSub


class exactnessTypeSub(supermod.exactnessType):
    def __init__(self, code=None, anytypeobjs_=None):
        super(exactnessTypeSub, self).__init__(code, anytypeobjs_, )
supermod.exactnessType.subclass = exactnessTypeSub
# end class exactnessTypeSub


class location_classTypeSub(supermod.location_classType):
    def __init__(self, code=None, anytypeobjs_=None):
        super(location_classTypeSub, self).__init__(code, anytypeobjs_, )
supermod.location_classType.subclass = location_classTypeSub
# end class location_classTypeSub


class feature_designationTypeSub(supermod.feature_designationType):
    def __init__(self, code=None, anytypeobjs_=None):
        super(feature_designationTypeSub, self).__init__(code, anytypeobjs_, )
supermod.feature_designationType.subclass = feature_designationTypeSub
# end class feature_designationTypeSub


class budget_itemTypeSub(supermod.budget_itemType):
    def __init__(self, percentage=None, code=None, description=None, anytypeobjs_=None):
        super(budget_itemTypeSub, self).__init__(percentage, code, description, anytypeobjs_, )
supermod.budget_itemType.subclass = budget_itemTypeSub
# end class budget_itemTypeSub


class indicatorTypeSub(supermod.indicatorType):
    def __init__(self, ascending=None, measure=None, title=None, description=None, baseline=None, period=None, anytypeobjs_=None):
        super(indicatorTypeSub, self).__init__(ascending, measure, title, description, baseline, period, anytypeobjs_, )
supermod.indicatorType.subclass = indicatorTypeSub
# end class indicatorTypeSub


class baselineTypeSub(supermod.baselineType):
    def __init__(self, value=None, year=None, comment=None, anytypeobjs_=None):
        super(baselineTypeSub, self).__init__(value, year, comment, anytypeobjs_, )
supermod.baselineType.subclass = baselineTypeSub
# end class baselineTypeSub


class periodTypeSub(supermod.periodType):
    def __init__(self, period_start=None, period_end=None, target=None, actual=None, anytypeobjs_=None):
        super(periodTypeSub, self).__init__(period_start, period_end, target, actual, anytypeobjs_, )
supermod.periodType.subclass = periodTypeSub
# end class periodTypeSub


class period_startTypeSub(supermod.period_startType):
    def __init__(self, iso_date=None, anytypeobjs_=None):
        super(period_startTypeSub, self).__init__(iso_date, anytypeobjs_, )
supermod.period_startType.subclass = period_startTypeSub
# end class period_startTypeSub


class period_endTypeSub(supermod.period_endType):
    def __init__(self, iso_date=None, anytypeobjs_=None):
        super(period_endTypeSub, self).__init__(iso_date, anytypeobjs_, )
supermod.period_endType.subclass = period_endTypeSub
# end class period_endTypeSub


class targetTypeSub(supermod.targetType):
    def __init__(self, value=None, comment=None, anytypeobjs_=None):
        super(targetTypeSub, self).__init__(value, comment, anytypeobjs_, )
supermod.targetType.subclass = targetTypeSub
# end class targetTypeSub


class actualTypeSub(supermod.actualType):
    def __init__(self, value=None, comment=None, anytypeobjs_=None):
        super(actualTypeSub, self).__init__(value, comment, anytypeobjs_, )
supermod.actualType.subclass = actualTypeSub
# end class actualTypeSub


class conditionTypeSub(supermod.conditionType):
    def __init__(self, type_=None, narrative=None, anytypeobjs_=None):
        super(conditionTypeSub, self).__init__(type_, narrative, anytypeobjs_, )
supermod.conditionType.subclass = conditionTypeSub
# end class conditionTypeSub


class period_startType1Sub(supermod.period_startType1):
    def __init__(self, iso_date=None, anytypeobjs_=None):
        super(period_startType1Sub, self).__init__(iso_date, anytypeobjs_, )
supermod.period_startType1.subclass = period_startType1Sub
# end class period_startType1Sub


class period_endType2Sub(supermod.period_endType2):
    def __init__(self, iso_date=None, anytypeobjs_=None):
        super(period_endType2Sub, self).__init__(iso_date, anytypeobjs_, )
supermod.period_endType2.subclass = period_endType2Sub
# end class period_endType2Sub


class period_startType3Sub(supermod.period_startType3):
    def __init__(self, iso_date=None, anytypeobjs_=None):
        super(period_startType3Sub, self).__init__(iso_date, anytypeobjs_, )
supermod.period_startType3.subclass = period_startType3Sub
# end class period_startType3Sub


class period_endType4Sub(supermod.period_endType4):
    def __init__(self, iso_date=None, anytypeobjs_=None):
        super(period_endType4Sub, self).__init__(iso_date, anytypeobjs_, )
supermod.period_endType4.subclass = period_endType4Sub
# end class period_endType4Sub


class other_flagsTypeSub(supermod.other_flagsType):
    def __init__(self, code=None, significance=None, anytypeobjs_=None):
        super(other_flagsTypeSub, self).__init__(code, significance, anytypeobjs_, )
supermod.other_flagsType.subclass = other_flagsTypeSub
# end class other_flagsTypeSub


class loan_termsTypeSub(supermod.loan_termsType):
    def __init__(self, rate_2=None, rate_1=None, repayment_type=None, repayment_plan=None, commitment_date=None, repayment_first_date=None, repayment_final_date=None, anytypeobjs_=None):
        super(loan_termsTypeSub, self).__init__(rate_2, rate_1, repayment_type, repayment_plan, commitment_date, repayment_first_date, repayment_final_date, anytypeobjs_, )
supermod.loan_termsType.subclass = loan_termsTypeSub
# end class loan_termsTypeSub


class repayment_typeTypeSub(supermod.repayment_typeType):
    def __init__(self, code=None, anytypeobjs_=None):
        super(repayment_typeTypeSub, self).__init__(code, anytypeobjs_, )
supermod.repayment_typeType.subclass = repayment_typeTypeSub
# end class repayment_typeTypeSub


class repayment_planTypeSub(supermod.repayment_planType):
    def __init__(self, code=None, anytypeobjs_=None):
        super(repayment_planTypeSub, self).__init__(code, anytypeobjs_, )
supermod.repayment_planType.subclass = repayment_planTypeSub
# end class repayment_planTypeSub


class commitment_dateTypeSub(supermod.commitment_dateType):
    def __init__(self, iso_date=None, anytypeobjs_=None):
        super(commitment_dateTypeSub, self).__init__(iso_date, anytypeobjs_, )
supermod.commitment_dateType.subclass = commitment_dateTypeSub
# end class commitment_dateTypeSub


class repayment_first_dateTypeSub(supermod.repayment_first_dateType):
    def __init__(self, iso_date=None, anytypeobjs_=None):
        super(repayment_first_dateTypeSub, self).__init__(iso_date, anytypeobjs_, )
supermod.repayment_first_dateType.subclass = repayment_first_dateTypeSub
# end class repayment_first_dateTypeSub


class repayment_final_dateTypeSub(supermod.repayment_final_dateType):
    def __init__(self, iso_date=None, anytypeobjs_=None):
        super(repayment_final_dateTypeSub, self).__init__(iso_date, anytypeobjs_, )
supermod.repayment_final_dateType.subclass = repayment_final_dateTypeSub
# end class repayment_final_dateTypeSub


class loan_statusTypeSub(supermod.loan_statusType):
    def __init__(self, currency=None, value_date=None, year=None, interest_received=None, principal_outstanding=None, principal_arrears=None, interest_arrears=None, anytypeobjs_=None):
        super(loan_statusTypeSub, self).__init__(currency, value_date, year, interest_received, principal_outstanding, principal_arrears, interest_arrears, anytypeobjs_, )
supermod.loan_statusType.subclass = loan_statusTypeSub
# end class loan_statusTypeSub


class forecastTypeSub(supermod.forecastType):
    def __init__(self, currency=None, value_date=None, year=None, valueOf_=None):
        super(forecastTypeSub, self).__init__(currency, value_date, year, valueOf_, )
supermod.forecastType.subclass = forecastTypeSub
# end class forecastTypeSub


class categoryTypeSub(supermod.categoryType):
    def __init__(self, code=None, anytypeobjs_=None):
        super(categoryTypeSub, self).__init__(code, anytypeobjs_, )
supermod.categoryType.subclass = categoryTypeSub
# end class categoryTypeSub


class languageTypeSub(supermod.languageType):
    def __init__(self, code=None, anytypeobjs_=None):
        super(languageTypeSub, self).__init__(code, anytypeobjs_, )
supermod.languageType.subclass = languageTypeSub
# end class languageTypeSub


def get_root_tag(node):
    tag = supermod.Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = None
    rootClass = supermod.GDSClassesMapping.get(tag)
    if rootClass is None and hasattr(supermod, tag):
        rootClass = getattr(supermod, tag)
    return tag, rootClass


def parse(inFilename, silence=False):
    doc = parsexml_(inFilename)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'iati_activities'
        rootClass = supermod.iati_activities
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='',
            pretty_print=True)
    return rootObj


def parseEtree(inFilename, silence=False):
    doc = parsexml_(inFilename)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'iati_activities'
        rootClass = supermod.iati_activities
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    mapping = {}
    rootElement = rootObj.to_etree(None, name_=rootTag, mapping_=mapping)
    reverse_mapping = rootObj.gds_reverse_node_mapping(mapping)
    if not silence:
        content = etree_.tostring(
            rootElement, pretty_print=True,
            xml_declaration=True, encoding="utf-8")
        sys.stdout.write(content)
        sys.stdout.write('\n')
    return rootObj, rootElement, mapping, reverse_mapping


def parseString(inString, silence=False):
    from StringIO import StringIO
    doc = parsexml_(StringIO(inString))
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'iati_activities'
        rootClass = supermod.iati_activities
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='')
    return rootObj


def parseLiteral(inFilename, silence=False):
    doc = parsexml_(inFilename)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'iati_activities'
        rootClass = supermod.iati_activities
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('#from ??? import *\n\n')
        sys.stdout.write('import ??? as model_\n\n')
        sys.stdout.write('rootObj = model_.rootClass(\n')
        rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
        sys.stdout.write(')\n')
    return rootObj


USAGE_TEXT = """
Usage: python ???.py <infilename>
"""


def usage():
    print(USAGE_TEXT)
    sys.exit(1)


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        usage()
    infilename = args[0]
    parse(infilename)


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()
