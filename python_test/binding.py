# ./binding.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2015-04-23 12:10:59.504833 by PyXB version 1.2.4 using Python 2.7.6.final.0
# Namespace AbsentNamespace0

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:09ba6b46-e9a1-11e4-8ec4-28cfe906a4b5')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.4'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes
import pyxb.binding.xml_

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.CreateAbsentNamespace()
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """
        Top-level list of one or more IATI activity records.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 34, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element iati-activity uses Python identifier iati_activity
    __iati_activity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'iati-activity'), 'iati_activity', '__AbsentNamespace0_CTD_ANON_iati_activity', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 88, 2), )

    
    iati_activity = property(__iati_activity.value, __iati_activity.set, None, '\n        Top-level element for a single IATI activity report.\n      ')

    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'version'), 'version', '__AbsentNamespace0_CTD_ANON_version', pyxb.binding.datatypes.decimal)
    __version._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 39, 6)
    __version._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 39, 6)
    
    version = property(__version.value, __version.set, None, '\n            A number indicating the IATI specification version in use.\n            "1.01" should be assumed if not specified.  It is required to\n            specify this attribute if the document is using features\n            specific to an IATI specification other than the initial\n            1.01 version.\n          ')

    
    # Attribute generated-datetime uses Python identifier generated_datetime
    __generated_datetime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'generated-datetime'), 'generated_datetime', '__AbsentNamespace0_CTD_ANON_generated_datetime', pyxb.binding.datatypes.dateTime)
    __generated_datetime._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 50, 6)
    __generated_datetime._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 50, 6)
    
    generated_datetime = property(__generated_datetime.value, __generated_datetime.set, None, '\n            A date/time stamp for when this file was generated.  This\n            is not necessarily the last-updated date for the\n            individual activity records in it.  Uses ISO 8601 date\n            format, e.g. "2010-03-12T18:45:00+01:00".  Use of this\n            attribute is highly recommended, to allow recipients to\n            know when a file has been updated.\n          ')

    
    # Attribute linked-data-default uses Python identifier linked_data_default
    __linked_data_default = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'linked-data-default'), 'linked_data_default', '__AbsentNamespace0_CTD_ANON_linked_data_default', pyxb.binding.datatypes.string)
    __linked_data_default._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 62, 6)
    __linked_data_default._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 62, 6)
    
    linked_data_default = property(__linked_data_default.value, __linked_data_default.set, None, '\n            IATI publishers are not obliged to publish their own\n            Linked Data.  However, if a publisher chooses to publish\n            linked data about their IATI activities then allowing them\n            to declare where this data is published would support\n            discovery of it, and any additional information they may\n            choose to publish as Linked Data alongside it.\n            \n            This attribute is URI path upon which an activity\n            identifier can be appended to get a dereferenceable URI\n            for any activity contained within a file.\n            \n            Where a publisher declares using one of these properties\n            that authoritative linked data is accessible for an\n            activity then consuming applications that are generating\n            Linked Data from an IATI XML file should assert an\n            owl:sameAs relationship to the relevant URI.\n          ')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None))
    _HasWildcardElement = True
    _ElementMap.update({
        __iati_activity.name() : __iati_activity
    })
    _AttributeMap.update({
        __version.name() : __version,
        __generated_datetime.name() : __generated_datetime,
        __linked_data_default.name() : __linked_data_default
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """
        Top-level element for a single IATI activity report.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 94, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element activity-website uses Python identifier activity_website
    __activity_website = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'activity-website'), 'activity_website', '__AbsentNamespace0_CTD_ANON__activity_website', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 186, 2), )

    
    activity_website = property(__activity_website.value, __activity_website.set, None, '\n        A direct link to a web site or web page providing more information\n        about the specific aid activity.  Multiple links can be included.\n        Multiple versions of the link may appear for different languages.  \n        Should not be general websites or addresses, and should include the \n        http or https prefix.\n      ')

    
    # Element participating-org uses Python identifier participating_org
    __participating_org = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'participating-org'), 'participating_org', '__AbsentNamespace0_CTD_ANON__participating_org', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 205, 2), )

    
    participating_org = property(__participating_org.value, __participating_org.set, None, '\n        An organisation (including the reporting organisation)\n        involved with the activity.  May be a donor, fund, agency,\n        etc.  Specifying the @ref and @role attributes is\n        strongly recommended.  May contain the organisation name as\n        content.\n\n        For the value of the @type attribute, see\n        http://iatistandard.org/codelists/organisation-type\n      ')

    
    # Element activity-scope uses Python identifier activity_scope
    __activity_scope = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'activity-scope'), 'activity_scope', '__AbsentNamespace0_CTD_ANON__activity_scope', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 239, 2), )

    
    activity_scope = property(__activity_scope.value, __activity_scope.set, None, '\n        What geographical area does the activity encompass?\n        eg. Global, Regional, Multi-National, National, Multiple\n        (sub-national) administrative areas, etc\n      ')

    
    # Element recipient-country uses Python identifier recipient_country
    __recipient_country = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'recipient-country'), 'recipient_country', '__AbsentNamespace0_CTD_ANON__recipient_country', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 249, 2), )

    
    recipient_country = property(__recipient_country.value, __recipient_country.set, None, '\n        A partner country that will benefit from this activity.  This\n        element is primarily for administrative and geopolitical\n        purposes.  If a specific country is not known, the activity\n        report can use the recipient-region element instead. For\n        geographical location, use the location element.\n\n        For the value of the @code attribute, see\n        http://iatistandard.org/codelists/country\n      ')

    
    # Element recipient-region uses Python identifier recipient_region
    __recipient_region = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'recipient-region'), 'recipient_region', '__AbsentNamespace0_CTD_ANON__recipient_region', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 273, 2), )

    
    recipient_region = property(__recipient_region.value, __recipient_region.set, None, '\n        A geopolitical region (above the country level) that will\n        benefit from this activity.  This element is primarily for\n        administrative and geopolitical purposes.  If the specific\n        country/-ies are known, the activity report can use the\n        recipient-country element instead. For geographical location,\n        use the location element.\n\n        For the value of the @code attribute, see\n        http://iatistandard.org/codelists/region\n      ')

    
    # Element collaboration-type uses Python identifier collaboration_type
    __collaboration_type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'collaboration-type'), 'collaboration_type', '__AbsentNamespace0_CTD_ANON__collaboration_type', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 306, 2), )

    
    collaboration_type = property(__collaboration_type.value, __collaboration_type.set, None, '\n        The type of collaboration involved in the project\'s\n        disbursements, e.g. "bilateral" or "multilateral".\n\n        For the value of the @code attribute, see\n        http://iatistandard.org/codelists/collaboration_type\n      ')

    
    # Element default-flow-type uses Python identifier default_flow_type
    __default_flow_type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'default-flow-type'), 'default_flow_type', '__AbsentNamespace0_CTD_ANON__default_flow_type', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 318, 2), )

    
    default_flow_type = property(__default_flow_type.value, __default_flow_type.set, None, '\n        The type of assistance provided, e.g. Official Development\n        Assistance (ODA).  Type types will be defined by IATI.\n\n        For the value of the @code attribute, see\n        http://iatistandard.org/codelists/flow_type\n      ')

    
    # Element default-aid-type uses Python identifier default_aid_type
    __default_aid_type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'default-aid-type'), 'default_aid_type', '__AbsentNamespace0_CTD_ANON__default_aid_type', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 330, 2), )

    
    default_aid_type = property(__default_aid_type.value, __default_aid_type.set, None, "\n        The type of aid being supplied (budget support, debt relief,\n        etc.).  This element specifies a default for all the\n        activity's financial transactions; it can be overridden at the\n        individual transaction level.\n\n        For the value of the @code attribute, see\n        http://iatistandard.org/codelists/aid_type\n      ")

    
    # Element default-finance-type uses Python identifier default_finance_type
    __default_finance_type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'default-finance-type'), 'default_finance_type', '__AbsentNamespace0_CTD_ANON__default_finance_type', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 344, 2), )

    
    default_finance_type = property(__default_finance_type.value, __default_finance_type.set, None, '\n        The type of finance (e.g. debt relief). The types will be\n        defined by IATI.  This the default value for all transactions\n        in the activity report; it can be overridded by individual\n        transactions.\n\n        For the value of the @code attribute, see\n        http://iatistandard.org/codelists/finance_type\n      ')

    
    # Element other-identifier uses Python identifier other_identifier
    __other_identifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'other-identifier'), 'other_identifier', '__AbsentNamespace0_CTD_ANON__other_identifier', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 358, 2), )

    
    other_identifier = property(__other_identifier.value, __other_identifier.set, None, "\n        An alternative, non-IATI identifier for the activity.  This\n        identifier is not guaranteed to be unique or persistent (it\n        depends on the owner organisation's policies, not IATI's).\n\n        If other-identifier is present then either @owner-ref or\n        @owner-name must be present\n      ")

    
    # Element sector uses Python identifier sector
    __sector = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'sector'), 'sector', '__AbsentNamespace0_CTD_ANON__sector', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 391, 2), )

    
    sector = property(__sector.value, __sector.set, None, '\n        Sector code and name.  For the value of the @code attribute,\n        see http://iatistandard.org/codelists/sector\n\n        Either the @code attribute or descriptive text content must be\n        present.\n      ')

    
    # Element activity-date uses Python identifier activity_date
    __activity_date = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'activity-date'), 'activity_date', '__AbsentNamespace0_CTD_ANON__activity_date', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 438, 2), )

    
    activity_date = property(__activity_date.value, __activity_date.set, None, '\n        The planned and actual start and completion dates of the \n        activity. Start dates may reflect either the commencement of \n        funding, planning or physical activity. End dates should, \n        wherever possible, reflect the ending of physical activity. \n        Dates should be in ISO 8601 date YYYY-MM-DD format, e.g. \n        2010-10-01. \n        \n        For the value of the @type attribute, see\n        http://iatistandard.org/codelists/activity_date_type\n\n        The text content may contain a general date text (e.g. 2011Q1)\n        for recording less specific dates such as month, quarter, or\n        year.\n      ')

    
    # Element activity-status uses Python identifier activity_status
    __activity_status = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'activity-status'), 'activity_status', '__AbsentNamespace0_CTD_ANON__activity_status', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 475, 2), )

    
    activity_status = property(__activity_status.value, __activity_status.set, None, '\n        The current status of the project (e.g. "planned"), using a\n        list defined by IATI.  For the value of the @code attribute,\n        see http://iatistandard.org/codelists/activity_status\n      ')

    
    # Element contact-info uses Python identifier contact_info
    __contact_info = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'contact-info'), 'contact_info', '__AbsentNamespace0_CTD_ANON__contact_info', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 485, 2), )

    
    contact_info = property(__contact_info.value, __contact_info.set, None, '\n        Contact information for the activity.  Specify whatever is\n        available.  You may repeat this element for each contact\n        person.\n      ')

    
    # Element default-tied-status uses Python identifier default_tied_status
    __default_tied_status = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'default-tied-status'), 'default_tied_status', '__AbsentNamespace0_CTD_ANON__default_tied_status', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 571, 2), )

    
    default_tied_status = property(__default_tied_status.value, __default_tied_status.set, None, '\n        Specify whether the aid is untied, tied, or partially tied,\n        using a codelist created by IATI.  The content is free text\n        that can optionally provide more detail.  For the value of the\n        @code attribute, see\n        http://iatistandard.org/codelists/tied_status\n      ')

    
    # Element policy-marker uses Python identifier policy_marker
    __policy_marker = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'policy-marker'), 'policy_marker', '__AbsentNamespace0_CTD_ANON__policy_marker', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 583, 2), )

    
    policy_marker = property(__policy_marker.value, __policy_marker.set, None, '\n        A policy or theme addressed by the activity.  A text\n        description of the theme appears in the content, and a formal\n        identifier appears in the @ref attribute.  The @vocabulary\n        attribute can also help to segment the markers into separate\n        vocabularies.  This element can be repeated for each policy\n        marker.  For the value of the @code attribute, see\n        http://iatistandard.org/codelists/policy_marker\n      ')

    
    # Element capital-spend uses Python identifier capital_spend
    __capital_spend = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'capital-spend'), 'capital_spend', '__AbsentNamespace0_CTD_ANON__capital_spend', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 635, 2), )

    
    capital_spend = property(__capital_spend.value, __capital_spend.set, None, '\n        The percentage of the total commitment that is for capital\n        spending\n      ')

    
    # Element transaction uses Python identifier transaction
    __transaction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'transaction'), 'transaction', '__AbsentNamespace0_CTD_ANON__transaction', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 651, 2), )

    
    transaction = property(__transaction.value, __transaction.set, None, '\n        Committed or actual money flowing in or out of an aid\n        activity.The @ref attribute allows uniquely identifying a\n        transaction, to match it up with the corresponding in- or\n        outflow in a different activity.\n      ')

    
    # Element location uses Python identifier location
    __location = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'location'), 'location', '__AbsentNamespace0_CTD_ANON__location', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 824, 2), )

    
    location = property(__location.value, __location.set, None, '\n        The sub-national geographical identification of the target \n        locations of an activity. These can be described by gazetteer \n        reference, coordinates, administrative areas or a textual \n        description.\n      ')

    
    # Element country-budget-items uses Python identifier country_budget_items
    __country_budget_items = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'country-budget-items'), 'country_budget_items', '__AbsentNamespace0_CTD_ANON__country_budget_items', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1203, 2), )

    
    country_budget_items = property(__country_budget_items.value, __country_budget_items.set, None, "\n        Recipient country budget items.\n\n        This item encodes the alignment of activities with both the\n        functional and administrative classifications used in the\n        recipient country's Chart of Accounts. This applies to both\n        on- and off-budget activities.\n      ")

    
    # Element related-activity uses Python identifier related_activity
    __related_activity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'related-activity'), 'related_activity', '__AbsentNamespace0_CTD_ANON__related_activity', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1251, 2), )

    
    related_activity = property(__related_activity.value, __related_activity.set, None, "\n        Another IATI activity related to this one.  The 'type'\n        attribute describes the type of relationship (e.g. parent,\n        sibling).  This does not need to be used to express funding\n        relationships, since those are covered in individual\n        transactions.\n\n        For the value of the @type attribute, see\n        http://iatistandard.org/codelists/related_activity_type\n      ")

    
    # Element legacy-data uses Python identifier legacy_data
    __legacy_data = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'legacy-data'), 'legacy_data', '__AbsentNamespace0_CTD_ANON__legacy_data', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1274, 2), )

    
    legacy_data = property(__legacy_data.value, __legacy_data.set, None, '\n        Hold a single name=value pair of legacy data.  This element is\n        *not* for adding new data types; instead, it holds the\n        original (non-IATI) value or code for an existing data type.\n      ')

    
    # Element result uses Python identifier result
    __result = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'result'), 'result', '__AbsentNamespace0_CTD_ANON__result', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1310, 2), )

    
    result = property(__result.value, __result.set, None, '\n        A measurable result of aid work.\n      ')

    
    # Element conditions uses Python identifier conditions
    __conditions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'conditions'), 'conditions', '__AbsentNamespace0_CTD_ANON__conditions', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1493, 2), )

    
    conditions = property(__conditions.value, __conditions.set, None, '\n        Conditions attached to the activity.\n      ')

    
    # Element budget uses Python identifier budget
    __budget = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'budget'), 'budget', '__AbsentNamespace0_CTD_ANON__budget', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1529, 2), )

    
    budget = property(__budget.value, __budget.set, None, "\n        The value of the aid activity's budget for each financial year\n        as in the original project document.\n      ")

    
    # Element planned-disbursement uses Python identifier planned_disbursement
    __planned_disbursement = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'planned-disbursement'), 'planned_disbursement', '__AbsentNamespace0_CTD_ANON__planned_disbursement', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1571, 2), )

    
    planned_disbursement = property(__planned_disbursement.value, __planned_disbursement.set, None, '\n        The planned disbursement element should only be used to report\n        specific planned cash transfers. These should be reported for\n        a specific date or a meaningfully predictable period. These\n        transactions should be reported in addition to budgets - which\n        are typically annual breakdowns of the total activity\n        commitment.\n      ')

    
    # Element crs-add uses Python identifier crs_add
    __crs_add = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'crs-add'), 'crs_add', '__AbsentNamespace0_CTD_ANON__crs_add', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1624, 2), )

    
    crs_add = property(__crs_add.value, __crs_add.set, None, '\n        Additional items specific to CRS++ reporting.\n      ')

    
    # Element fss uses Python identifier fss
    __fss = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'fss'), 'fss', '__AbsentNamespace0_CTD_ANON__fss', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1795, 2), )

    
    fss = property(__fss.value, __fss.set, None, '\n        This section allows entry of data required for the OECD\n        DAC Forward Spending Survey at an activity level.\n      ')

    
    # Element title uses Python identifier title
    __title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'title'), 'title', '__AbsentNamespace0_CTD_ANON__title', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 27, 2), )

    
    title = property(__title.value, __title.set, None, '\n        A short, human-readable title.  May be repeated for different\n        languages.\n      ')

    
    # Element description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'description'), 'description', '__AbsentNamespace0_CTD_ANON__description', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 36, 2), )

    
    description = property(__description.value, __description.set, None, '\n        A longer, human-readable description.  May be repeated for\n        different languages.\n      ')

    
    # Element iati-identifier uses Python identifier iati_identifier
    __iati_identifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'iati-identifier'), 'iati_identifier', '__AbsentNamespace0_CTD_ANON__iati_identifier', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 61, 2), )

    
    iati_identifier = property(__iati_identifier.value, __iati_identifier.set, None, "\n        The iati-identifier element is used in both Activity files and\n        Organisation files, and has a slightly different meaning depending on\n        where it is being used, and should not be confused.\n\n        When used in an organisation it is a globally unique identifier for\n        that organisation.\n\n        When used in an activity it is a globally unique identifier for that\n        activity.  This should be in the form of the IATI Organisation\n        Identifier (for the reporting organisation) concatenated to that\n        organisation's activity identifier. (NB. Two or more reporting\n        organisations may publish information on the same activity.)\n      ")

    
    # Element reporting-org uses Python identifier reporting_org
    __reporting_org = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'reporting-org'), 'reporting_org', '__AbsentNamespace0_CTD_ANON__reporting_org', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 83, 2), )

    
    reporting_org = property(__reporting_org.value, __reporting_org.set, None, '\n        The organisation issuing the report.\n        May be a primary source (reporting on its own activity as\n        donor, implementing agency, etc) or a secondary source\n        (reporting on the activities of another organisation). \n        \n        Specifying the @ref attribute is mandatory.\n        May contain the organisation name as content.\n        \n        All activities in an activity xml file must contain the same\n        @ref AND this @ref must be the same as the iati-identifier\n        recorded in the registry publisher record of the account under\n        which this file is published.\n      ')

    
    # Element document-link uses Python identifier document_link
    __document_link = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'document-link'), 'document_link', '__AbsentNamespace0_CTD_ANON__document_link', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 119, 2), )

    
    document_link = property(__document_link.value, __document_link.set, None, '\n        A categorized link to an external document.\n      ')

    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__AbsentNamespace0_CTD_ANON__httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang)
    __lang._DeclarationLocation = None
    __lang._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 151, 6)
    
    lang = property(__lang.value, __lang.set, None, None)

    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'version'), 'version', '__AbsentNamespace0_CTD_ANON__version', pyxb.binding.datatypes.decimal)
    __version._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 131, 6)
    __version._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 131, 6)
    
    version = property(__version.value, __version.set, None, '\n            A number indicating the IATI specification version in use.\n            "1.01" should be assumed if not specified.  It is required to\n            specify this attribute if the document is using features\n            specific to an IATI specification other than the initial\n            1.01 version.\n          ')

    
    # Attribute last-updated-datetime uses Python identifier last_updated_datetime
    __last_updated_datetime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'last-updated-datetime'), 'last_updated_datetime', '__AbsentNamespace0_CTD_ANON__last_updated_datetime', pyxb.binding.datatypes.dateTime)
    __last_updated_datetime._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 142, 6)
    __last_updated_datetime._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 142, 6)
    
    last_updated_datetime = property(__last_updated_datetime.value, __last_updated_datetime.set, None, '\n            The last date/time that the data for this specific\n            activity was updated.  This date must change whenever the\n            value of any field changes.\n          ')

    
    # Attribute default-currency uses Python identifier default_currency
    __default_currency = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'default-currency'), 'default_currency', '__AbsentNamespace0_CTD_ANON__default_currency', pyxb.binding.datatypes.string)
    __default_currency._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 152, 6)
    __default_currency._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 152, 6)
    
    default_currency = property(__default_currency.value, __default_currency.set, None, '\n            Default ISO 4217 currency code for all financial values in\n            this activity report.  See\n            http://iatistandard.org/codelists/currency\n          ')

    
    # Attribute hierarchy uses Python identifier hierarchy
    __hierarchy = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'hierarchy'), 'hierarchy', '__AbsentNamespace0_CTD_ANON__hierarchy', pyxb.binding.datatypes.int)
    __hierarchy._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 161, 6)
    __hierarchy._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 161, 6)
    
    hierarchy = property(__hierarchy.value, __hierarchy.set, None, "\n            The hierarchical level within the reporting organisation's\n            subdivision of its units of aid. (eg activity = 1;\n            sub-activity = 2; sub-sub-activity = 3). If hierarchy is\n            not reported then 1 is assumed. If multiple levels are\n            reported then, to avoid double counting, financial\n            transactions should only be reported at the lowest\n            hierarchical level.\n          ")

    
    # Attribute linked-data-uri uses Python identifier linked_data_uri
    __linked_data_uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'linked-data-uri'), 'linked_data_uri', '__AbsentNamespace0_CTD_ANON__linked_data_uri', pyxb.binding.datatypes.string)
    __linked_data_uri._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 174, 6)
    __linked_data_uri._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 174, 6)
    
    linked_data_uri = property(__linked_data_uri.value, __linked_data_uri.set, None, '\n            A Linked Data URI for a given activity (overrides\n            iati-activities/@linked-data-default if set)\n          ')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None))
    _HasWildcardElement = True
    _ElementMap.update({
        __activity_website.name() : __activity_website,
        __participating_org.name() : __participating_org,
        __activity_scope.name() : __activity_scope,
        __recipient_country.name() : __recipient_country,
        __recipient_region.name() : __recipient_region,
        __collaboration_type.name() : __collaboration_type,
        __default_flow_type.name() : __default_flow_type,
        __default_aid_type.name() : __default_aid_type,
        __default_finance_type.name() : __default_finance_type,
        __other_identifier.name() : __other_identifier,
        __sector.name() : __sector,
        __activity_date.name() : __activity_date,
        __activity_status.name() : __activity_status,
        __contact_info.name() : __contact_info,
        __default_tied_status.name() : __default_tied_status,
        __policy_marker.name() : __policy_marker,
        __capital_spend.name() : __capital_spend,
        __transaction.name() : __transaction,
        __location.name() : __location,
        __country_budget_items.name() : __country_budget_items,
        __related_activity.name() : __related_activity,
        __legacy_data.name() : __legacy_data,
        __result.name() : __result,
        __conditions.name() : __conditions,
        __budget.name() : __budget,
        __planned_disbursement.name() : __planned_disbursement,
        __crs_add.name() : __crs_add,
        __fss.name() : __fss,
        __title.name() : __title,
        __description.name() : __description,
        __iati_identifier.name() : __iati_identifier,
        __reporting_org.name() : __reporting_org,
        __document_link.name() : __document_link
    })
    _AttributeMap.update({
        __lang.name() : __lang,
        __version.name() : __version,
        __last_updated_datetime.name() : __last_updated_datetime,
        __default_currency.name() : __default_currency,
        __hierarchy.name() : __hierarchy,
        __linked_data_uri.name() : __linked_data_uri
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """
        A direct link to a web site or web page providing more information
        about the specific aid activity.  Multiple links can be included.
        Multiple versions of the link may appear for different languages.  
        Should not be general websites or addresses, and should include the 
        http or https prefix.
      """
    _TypeDefinition = pyxb.binding.datatypes.anyURI
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 196, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyURI
    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type MIXED
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """
        An organisation (including the reporting organisation)
        involved with the activity.  May be a donor, fund, agency,
        etc.  Specifying the @ref and @role attributes is
        strongly recommended.  May contain the organisation name as
        content.

        For the value of the @type attribute, see
        http://iatistandard.org/codelists/organisation-type
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 218, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__AbsentNamespace0_CTD_ANON_3_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang)
    __lang._DeclarationLocation = None
    __lang._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 246, 4)
    
    lang = property(__lang.value, __lang.set, None, None)

    
    # Attribute role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'role'), 'role', '__AbsentNamespace0_CTD_ANON_3_role', pyxb.binding.datatypes.string, required=True)
    __role._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 225, 6)
    __role._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 225, 6)
    
    role = property(__role.value, __role.set, None, "\n            A code describing the organisation's role in the activity\n            (donor, agency, etc.).\n\n            See http://iatistandard.org/codelists/organisation_role\n          ")

    
    # Attribute ref uses Python identifier ref
    __ref = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'ref'), 'ref', '__AbsentNamespace0_CTD_ANON_3_ref', pyxb.binding.datatypes.string)
    __ref._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 181, 2)
    __ref._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 223, 6)
    
    ref = property(__ref.value, __ref.set, None, '\n        Machine-readable identification string for the business\n        object being described.\n      ')

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'type'), 'type', '__AbsentNamespace0_CTD_ANON_3_type', pyxb.binding.datatypes.string)
    __type._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 190, 2)
    __type._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 224, 6)
    
    type = property(__type.value, __type.set, None, '\n        A machine readable code describing the type of thing being referenced.\n        The value should be available on a related codelist.\n      ')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None))
    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __lang.name() : __lang,
        __role.name() : __role,
        __ref.name() : __ref,
        __type.name() : __type
    })



# Complex type [anonymous] with content type MIXED
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    """
        A partner country that will benefit from this activity.  This
        element is primarily for administrative and geopolitical
        purposes.  If a specific country is not known, the activity
        report can use the recipient-region element instead. For
        geographical location, use the location element.

        For the value of the @code attribute, see
        http://iatistandard.org/codelists/country
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 262, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__AbsentNamespace0_CTD_ANON_4_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang)
    __lang._DeclarationLocation = None
    __lang._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 246, 4)
    
    lang = property(__lang.value, __lang.set, None, None)

    
    # Attribute code uses Python identifier code
    __code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'code'), 'code', '__AbsentNamespace0_CTD_ANON_4_code', pyxb.binding.datatypes.string, required=True)
    __code._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 172, 2)
    __code._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 266, 6)
    
    code = property(__code.value, __code.set, None, '\n        Machine readable code for the entity being described. The value should\n        be available on a related codelist.\n      ')

    
    # Attribute percentage uses Python identifier percentage
    __percentage = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'percentage'), 'percentage', '__AbsentNamespace0_CTD_ANON_4_percentage', pyxb.binding.datatypes.decimal)
    __percentage._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 199, 2)
    __percentage._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 268, 6)
    
    percentage = property(__percentage.value, __percentage.set, None, '\n        The percentage of the budget allocated to this item.  Content\n        must be a positive decimal number between 0 and 100, with no\n        percentage sign. In version 1.03 of the IATI Standard this\n        value became designated as a decimal value and no longer \n        as a positive integer.\n      ')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None))
    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __lang.name() : __lang,
        __code.name() : __code,
        __percentage.name() : __percentage
    })



# Complex type [anonymous] with content type MIXED
class CTD_ANON_5 (pyxb.binding.basis.complexTypeDefinition):
    """
        A geopolitical region (above the country level) that will
        benefit from this activity.  This element is primarily for
        administrative and geopolitical purposes.  If the specific
        country/-ies are known, the activity report can use the
        recipient-country element instead. For geographical location,
        use the location element.

        For the value of the @code attribute, see
        http://iatistandard.org/codelists/region
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 287, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__AbsentNamespace0_CTD_ANON_5_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang)
    __lang._DeclarationLocation = None
    __lang._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 246, 4)
    
    lang = property(__lang.value, __lang.set, None, None)

    
    # Attribute vocabulary uses Python identifier vocabulary
    __vocabulary = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'vocabulary'), 'vocabulary', '__AbsentNamespace0_CTD_ANON_5_vocabulary', pyxb.binding.datatypes.string)
    __vocabulary._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 292, 6)
    __vocabulary._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 292, 6)
    
    vocabulary = property(__vocabulary.value, __vocabulary.set, None, "\n            The vocabulary from which the region code is drawn. If it\n            is not present 1 - 'OECD DAC' is assumed.\n          ")

    
    # Attribute code uses Python identifier code
    __code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'code'), 'code', '__AbsentNamespace0_CTD_ANON_5_code', pyxb.binding.datatypes.string)
    __code._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 172, 2)
    __code._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 291, 6)
    
    code = property(__code.value, __code.set, None, '\n        Machine readable code for the entity being described. The value should\n        be available on a related codelist.\n      ')

    
    # Attribute percentage uses Python identifier percentage
    __percentage = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'percentage'), 'percentage', '__AbsentNamespace0_CTD_ANON_5_percentage', pyxb.binding.datatypes.decimal)
    __percentage._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 199, 2)
    __percentage._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 301, 6)
    
    percentage = property(__percentage.value, __percentage.set, None, '\n        The percentage of the budget allocated to this item.  Content\n        must be a positive decimal number between 0 and 100, with no\n        percentage sign. In version 1.03 of the IATI Standard this\n        value became designated as a decimal value and no longer \n        as a positive integer.\n      ')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None))
    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __lang.name() : __lang,
        __vocabulary.name() : __vocabulary,
        __code.name() : __code,
        __percentage.name() : __percentage
    })



# Complex type [anonymous] with content type MIXED
class CTD_ANON_6 (pyxb.binding.basis.complexTypeDefinition):
    """
        An alternative, non-IATI identifier for the activity.  This
        identifier is not guaranteed to be unique or persistent (it
        depends on the owner organisation's policies, not IATI's).

        If other-identifier is present then either @owner-ref or
        @owner-name must be present
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 369, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute owner-ref uses Python identifier owner_ref
    __owner_ref = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'owner-ref'), 'owner_ref', '__AbsentNamespace0_CTD_ANON_6_owner_ref', pyxb.binding.datatypes.string)
    __owner_ref._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 370, 6)
    __owner_ref._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 370, 6)
    
    owner_ref = property(__owner_ref.value, __owner_ref.set, None, '\n            An identifier for the owner of this identifier.\n            For guidance on constructing the value of the @ref\n            attribute, see http://iatistandard.org/org-ref\n          ')

    
    # Attribute owner-name uses Python identifier owner_name
    __owner_name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'owner-name'), 'owner_name', '__AbsentNamespace0_CTD_ANON_6_owner_name', pyxb.binding.datatypes.string)
    __owner_name._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 379, 6)
    __owner_name._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 379, 6)
    
    owner_name = property(__owner_name.value, __owner_name.set, None, '\n            Free text providing a human-readable name for the owner\n            of this identifier.\n          ')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __owner_ref.name() : __owner_ref,
        __owner_name.name() : __owner_name
    })



# Complex type [anonymous] with content type MIXED
class CTD_ANON_7 (pyxb.binding.basis.complexTypeDefinition):
    """
        Sector code and name.  For the value of the @code attribute,
        see http://iatistandard.org/codelists/sector

        Either the @code attribute or descriptive text content must be
        present.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 401, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__AbsentNamespace0_CTD_ANON_7_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang)
    __lang._DeclarationLocation = None
    __lang._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 246, 4)
    
    lang = property(__lang.value, __lang.set, None, None)

    
    # Attribute vocabulary uses Python identifier vocabulary
    __vocabulary = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'vocabulary'), 'vocabulary', '__AbsentNamespace0_CTD_ANON_7_vocabulary', pyxb.binding.datatypes.string)
    __vocabulary._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 417, 6)
    __vocabulary._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 417, 6)
    
    vocabulary = property(__vocabulary.value, __vocabulary.set, None, '\n            The vocabulary (codelist) used for sector\n            classifications. If omitted, assume DAC. "DAC" codes\n            should be used wherever possible. It is also recommended\n            that if a publisher has its own classification system then\n            the vocabulary "RO" (Reporting Organisation\'s own\n            vocabulary" should be used in addition to "DAC". NB that\n            if multiple sector codes are used in multiple vocabularies\n            then each vocabulary\'s percentages should add up to 100%.\n\n            See http://iatistandard.org/codelists/vocabulary\n          ')

    
    # Attribute code uses Python identifier code
    __code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'code'), 'code', '__AbsentNamespace0_CTD_ANON_7_code', pyxb.binding.datatypes.string)
    __code._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 172, 2)
    __code._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 406, 6)
    
    code = property(__code.value, __code.set, None, '\n        Machine readable code for the entity being described. The value should\n        be available on a related codelist.\n      ')

    
    # Attribute percentage uses Python identifier percentage
    __percentage = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'percentage'), 'percentage', '__AbsentNamespace0_CTD_ANON_7_percentage', pyxb.binding.datatypes.decimal)
    __percentage._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 199, 2)
    __percentage._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 433, 6)
    
    percentage = property(__percentage.value, __percentage.set, None, '\n        The percentage of the budget allocated to this item.  Content\n        must be a positive decimal number between 0 and 100, with no\n        percentage sign. In version 1.03 of the IATI Standard this\n        value became designated as a decimal value and no longer \n        as a positive integer.\n      ')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None))
    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __lang.name() : __lang,
        __vocabulary.name() : __vocabulary,
        __code.name() : __code,
        __percentage.name() : __percentage
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_8 (pyxb.binding.basis.complexTypeDefinition):
    """
        The planned and actual start and completion dates of the 
        activity. Start dates may reflect either the commencement of 
        funding, planning or physical activity. End dates should, 
        wherever possible, reflect the ending of physical activity. 
        Dates should be in ISO 8601 date YYYY-MM-DD format, e.g. 
        2010-10-01. 
        
        For the value of the @type attribute, see
        http://iatistandard.org/codelists/activity_date_type

        The text content may contain a general date text (e.g. 2011Q1)
        for recording less specific dates such as month, quarter, or
        year.
      """
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 456, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__AbsentNamespace0_CTD_ANON_8_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang)
    __lang._DeclarationLocation = None
    __lang._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 246, 4)
    
    lang = property(__lang.value, __lang.set, None, None)

    
    # Attribute iso-date uses Python identifier iso_date
    __iso_date = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'iso-date'), 'iso_date', '__AbsentNamespace0_CTD_ANON_8_iso_date', pyxb.binding.datatypes.date)
    __iso_date._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 461, 10)
    __iso_date._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 461, 10)
    
    iso_date = property(__iso_date.value, __iso_date.set, None, '\n                An activity milestone date in ISO 8601 date format,\n                e.g. "2010-12-01".\n              ')

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'type'), 'type', '__AbsentNamespace0_CTD_ANON_8_type', pyxb.binding.datatypes.string, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 190, 2)
    __type._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 459, 10)
    
    type = property(__type.value, __type.set, None, '\n        A machine readable code describing the type of thing being referenced.\n        The value should be available on a related codelist.\n      ')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __lang.name() : __lang,
        __iso_date.name() : __iso_date,
        __type.name() : __type
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_9 (pyxb.binding.basis.complexTypeDefinition):
    """
        Contact information for the activity.  Specify whatever is
        available.  You may repeat this element for each contact
        person.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 493, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element organisation uses Python identifier organisation
    __organisation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'organisation'), 'organisation', '__AbsentNamespace0_CTD_ANON_9_organisation', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 495, 8), )

    
    organisation = property(__organisation.value, __organisation.set, None, '\n              The organisation to contact for more information about the\n              activity.\n              \n              This is required if content-info is included.\n            ')

    
    # Element person-name uses Python identifier person_name
    __person_name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'person-name'), 'person_name', '__AbsentNamespace0_CTD_ANON_9_person_name', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 505, 8), )

    
    person_name = property(__person_name.value, __person_name.set, None, '\n              The name of the contact person at the organisation.\n              \n              If person-name is present then either person-name/text() \n              or job-title/text() must be present\n            ')

    
    # Element job-title uses Python identifier job_title
    __job_title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'job-title'), 'job_title', '__AbsentNamespace0_CTD_ANON_9_job_title', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 515, 8), )

    
    job_title = property(__job_title.value, __job_title.set, None, '\n              The job title of the contact person at the organisation.\n              You may repeat this element for different languages.\n              \n              If person-name is present then either person-name/text() \n              or job-title/text() must be present\n            ')

    
    # Element telephone uses Python identifier telephone
    __telephone = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'telephone'), 'telephone', '__AbsentNamespace0_CTD_ANON_9_telephone', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 526, 8), )

    
    telephone = property(__telephone.value, __telephone.set, None, '\n              The contact telephone number, if available.  May be\n              repeated for multiple numbers.\n            ')

    
    # Element email uses Python identifier email
    __email = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'email'), 'email', '__AbsentNamespace0_CTD_ANON_9_email', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 537, 8), )

    
    email = property(__email.value, __email.set, None, '\n              The contact email address, if available.  May be\n              repeated for multiple addresses.\n            ')

    
    # Element mailing-address uses Python identifier mailing_address
    __mailing_address = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'mailing-address'), 'mailing_address', '__AbsentNamespace0_CTD_ANON_9_mailing_address', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 545, 8), )

    
    mailing_address = property(__mailing_address.value, __mailing_address.set, None, '\n              The contact mailing address, if available.\n            ')

    
    # Element website uses Python identifier website
    __website = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'website'), 'website', '__AbsentNamespace0_CTD_ANON_9_website', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 556, 8), )

    
    website = property(__website.value, __website.set, None, '\n              The contact web address, if available.  May be repeated\n              for multiple sites.\n            ')

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'type'), 'type', '__AbsentNamespace0_CTD_ANON_9_type', pyxb.binding.datatypes.string)
    __type._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 190, 2)
    __type._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 566, 6)
    
    type = property(__type.value, __type.set, None, '\n        A machine readable code describing the type of thing being referenced.\n        The value should be available on a related codelist.\n      ')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None))
    _HasWildcardElement = True
    _ElementMap.update({
        __organisation.name() : __organisation,
        __person_name.name() : __person_name,
        __job_title.name() : __job_title,
        __telephone.name() : __telephone,
        __email.name() : __email,
        __mailing_address.name() : __mailing_address,
        __website.name() : __website
    })
    _AttributeMap.update({
        __type.name() : __type
    })



# Complex type [anonymous] with content type MIXED
class CTD_ANON_10 (pyxb.binding.basis.complexTypeDefinition):
    """
              The contact telephone number, if available.  May be
              repeated for multiple numbers.
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 533, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type MIXED
class CTD_ANON_11 (pyxb.binding.basis.complexTypeDefinition):
    """
              The contact mailing address, if available.
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 551, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__AbsentNamespace0_CTD_ANON_11_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang)
    __lang._DeclarationLocation = None
    __lang._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 246, 4)
    
    lang = property(__lang.value, __lang.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __lang.name() : __lang
    })



# Complex type [anonymous] with content type MIXED
class CTD_ANON_12 (pyxb.binding.basis.complexTypeDefinition):
    """
        A policy or theme addressed by the activity.  A text
        description of the theme appears in the content, and a formal
        identifier appears in the @ref attribute.  The @vocabulary
        attribute can also help to segment the markers into separate
        vocabularies.  This element can be repeated for each policy
        marker.  For the value of the @code attribute, see
        http://iatistandard.org/codelists/policy_marker
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 595, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__AbsentNamespace0_CTD_ANON_12_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang)
    __lang._DeclarationLocation = None
    __lang._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 246, 4)
    
    lang = property(__lang.value, __lang.set, None, None)

    
    # Attribute vocabulary uses Python identifier vocabulary
    __vocabulary = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'vocabulary'), 'vocabulary', '__AbsentNamespace0_CTD_ANON_12_vocabulary', pyxb.binding.datatypes.string)
    __vocabulary._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 609, 6)
    __vocabulary._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 609, 6)
    
    vocabulary = property(__vocabulary.value, __vocabulary.set, None, '\n            Policy vocabulary used. Default is "DAC", but "RO" may also\n            be used for publisher\'s own markers.\n\n            See http://iatistandard.org/codelists/vocabulary\n          ')

    
    # Attribute significance uses Python identifier significance
    __significance = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'significance'), 'significance', '__AbsentNamespace0_CTD_ANON_12_significance', pyxb.binding.datatypes.string)
    __significance._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 619, 6)
    __significance._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 619, 6)
    
    significance = property(__significance.value, __significance.set, None, '\n            The significance of the policy marker for this activity\n            (e.g. principal or significant), from a list defined by\n            IATI.  If a marker is not significant, the policy-marker\n            element will not be present.\n\n            See http://iatistandard.org/codelists/policy_significance\n          ')

    
    # Attribute code uses Python identifier code
    __code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'code'), 'code', '__AbsentNamespace0_CTD_ANON_12_code', pyxb.binding.datatypes.string)
    __code._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 172, 2)
    __code._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 600, 6)
    
    code = property(__code.value, __code.set, None, '\n        Machine readable code for the entity being described. The value should\n        be available on a related codelist.\n      ')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None))
    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __lang.name() : __lang,
        __vocabulary.name() : __vocabulary,
        __significance.name() : __significance,
        __code.name() : __code
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_13 (pyxb.binding.basis.complexTypeDefinition):
    """
        The percentage of the total commitment that is for capital
        spending
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 642, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute percentage uses Python identifier percentage
    __percentage = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'percentage'), 'percentage', '__AbsentNamespace0_CTD_ANON_13_percentage', pyxb.binding.datatypes.decimal, required=True)
    __percentage._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 199, 2)
    __percentage._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 646, 6)
    
    percentage = property(__percentage.value, __percentage.set, None, '\n        The percentage of the budget allocated to this item.  Content\n        must be a positive decimal number between 0 and 100, with no\n        percentage sign. In version 1.03 of the IATI Standard this\n        value became designated as a decimal value and no longer \n        as a positive integer.\n      ')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None))
    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __percentage.name() : __percentage
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_14 (pyxb.binding.basis.complexTypeDefinition):
    """
        Committed or actual money flowing in or out of an aid
        activity.The @ref attribute allows uniquely identifying a
        transaction, to match it up with the corresponding in- or
        outflow in a different activity.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 660, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element value uses Python identifier value_
    __value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'value'), 'value_', '__AbsentNamespace0_CTD_ANON_14_value', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 662, 8), )

    
    value_ = property(__value.value, __value.set, None, '\n              The amount of the contribution (or its value, if in\n              kind).\n            ')

    
    # Element description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'description'), 'description', '__AbsentNamespace0_CTD_ANON_14_description', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 670, 8), )

    
    description = property(__description.value, __description.set, None, '\n              A human-readable description of the transaction.\n            ')

    
    # Element transaction-type uses Python identifier transaction_type
    __transaction_type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'transaction-type'), 'transaction_type', '__AbsentNamespace0_CTD_ANON_14_transaction_type', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 677, 8), )

    
    transaction_type = property(__transaction_type.value, __transaction_type.set, None, '\n              The type of the transaction (e.g. commitment,\n              disbursement, expenditure, etc.).  The @ref attribute\n              contains a code defined by IATI, and the content is an\n              optional free-text description of the type.\n\n              For the value of the @code attribute, see\n              http://iatistandard.org/codelists/transaction_type\n            ')

    
    # Element provider-org uses Python identifier provider_org
    __provider_org = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'provider-org'), 'provider_org', '__AbsentNamespace0_CTD_ANON_14_provider_org', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 690, 8), )

    
    provider_org = property(__provider_org.value, __provider_org.set, None, '\n              The organisation providing the money for the\n              transaction (if omitted, the provider organisation is\n              the reporting organisation).\n            ')

    
    # Element receiver-org uses Python identifier receiver_org
    __receiver_org = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'receiver-org'), 'receiver_org', '__AbsentNamespace0_CTD_ANON_14_receiver_org', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 716, 8), )

    
    receiver_org = property(__receiver_org.value, __receiver_org.set, None, '\n              The organisation receiving the money from the\n              transaction (if omitted, then the receiver\n              organisation is the reporting organisation).\n            ')

    
    # Element transaction-date uses Python identifier transaction_date
    __transaction_date = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'transaction-date'), 'transaction_date', '__AbsentNamespace0_CTD_ANON_14_transaction_date', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 741, 8), )

    
    transaction_date = property(__transaction_date.value, __transaction_date.set, None, '\n              A milestone date for this transaction (such as the\n              decision date, disbursement date, etc.).\n            ')

    
    # Element flow-type uses Python identifier flow_type
    __flow_type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'flow-type'), 'flow_type', '__AbsentNamespace0_CTD_ANON_14_flow_type', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 762, 8), )

    
    flow_type = property(__flow_type.value, __flow_type.set, None, '\n              Optional element to override the top-level\n              default-flow-type element.\n              \n              For the value of the @code attribute, see\n              http://iatistandard.org/codelists/flow_type\n            ')

    
    # Element finance-type uses Python identifier finance_type
    __finance_type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'finance-type'), 'finance_type', '__AbsentNamespace0_CTD_ANON_14_finance_type', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 773, 8), )

    
    finance_type = property(__finance_type.value, __finance_type.set, None, '\n              Optional element to override the top-level\n              default-finance-type element on a\n              transaction-by-transaction basis, if needed.\n\n              For the value of the @code attribute, see\n              http://iatistandard.org/codelists/finance_type\n            ')

    
    # Element aid-type uses Python identifier aid_type
    __aid_type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'aid-type'), 'aid_type', '__AbsentNamespace0_CTD_ANON_14_aid_type', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 785, 8), )

    
    aid_type = property(__aid_type.value, __aid_type.set, None, '\n              Optional element to override the top-level\n              default-aid-type element (debt relief, etc.) on a\n              transaction-by-transaction basis if needed.\n\n              For the value of the @code attribute, see\n              http://iatistandard.org/codelists/aid_type\n            ')

    
    # Element tied-status uses Python identifier tied_status
    __tied_status = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'tied-status'), 'tied_status', '__AbsentNamespace0_CTD_ANON_14_tied_status', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 797, 8), )

    
    tied_status = property(__tied_status.value, __tied_status.set, None, '\n              Optional element to override the top-level\n              default-tied-status element (pooled, etc.) on a\n              transaction-by-transaction basis if needed.\n\n              For the value of the @code attribute, see\n              http://iatistandard.org/codelists/tied_status\n            ')

    
    # Element disbursement-channel uses Python identifier disbursement_channel
    __disbursement_channel = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'disbursement-channel'), 'disbursement_channel', '__AbsentNamespace0_CTD_ANON_14_disbursement_channel', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 809, 8), )

    
    disbursement_channel = property(__disbursement_channel.value, __disbursement_channel.set, None, '\n              The channel through which the funds will flow for this\n              transaction, from an IATI codelist.\n            ')

    
    # Attribute ref uses Python identifier ref
    __ref = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'ref'), 'ref', '__AbsentNamespace0_CTD_ANON_14_ref', pyxb.binding.datatypes.string)
    __ref._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 181, 2)
    __ref._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 819, 6)
    
    ref = property(__ref.value, __ref.set, None, '\n        Machine-readable identification string for the business\n        object being described.\n      ')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None))
    _HasWildcardElement = True
    _ElementMap.update({
        __value.name() : __value,
        __description.name() : __description,
        __transaction_type.name() : __transaction_type,
        __provider_org.name() : __provider_org,
        __receiver_org.name() : __receiver_org,
        __transaction_date.name() : __transaction_date,
        __flow_type.name() : __flow_type,
        __finance_type.name() : __finance_type,
        __aid_type.name() : __aid_type,
        __tied_status.name() : __tied_status,
        __disbursement_channel.name() : __disbursement_channel
    })
    _AttributeMap.update({
        __ref.name() : __ref
    })



# Complex type [anonymous] with content type MIXED
class CTD_ANON_15 (pyxb.binding.basis.complexTypeDefinition):
    """
              The organisation providing the money for the
              transaction (if omitted, the provider organisation is
              the reporting organisation).
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 698, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute provider-activity-id uses Python identifier provider_activity_id
    __provider_activity_id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'provider-activity-id'), 'provider_activity_id', '__AbsentNamespace0_CTD_ANON_15_provider_activity_id', pyxb.binding.datatypes.string)
    __provider_activity_id._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 703, 12)
    __provider_activity_id._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 703, 12)
    
    provider_activity_id = property(__provider_activity_id.value, __provider_activity_id.set, None, '\n                  If the funds are being provided from the budget of \n                  another activity that is reported to IATI, this \n                  should record the unique IATI activity identifier for \n                  that activity.\n                ')

    
    # Attribute ref uses Python identifier ref
    __ref = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'ref'), 'ref', '__AbsentNamespace0_CTD_ANON_15_ref', pyxb.binding.datatypes.string)
    __ref._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 181, 2)
    __ref._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 702, 12)
    
    ref = property(__ref.value, __ref.set, None, '\n        Machine-readable identification string for the business\n        object being described.\n      ')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None))
    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __provider_activity_id.name() : __provider_activity_id,
        __ref.name() : __ref
    })



# Complex type [anonymous] with content type MIXED
class CTD_ANON_16 (pyxb.binding.basis.complexTypeDefinition):
    """
              The organisation receiving the money from the
              transaction (if omitted, then the receiver
              organisation is the reporting organisation).
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 724, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute receiver-activity-id uses Python identifier receiver_activity_id
    __receiver_activity_id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'receiver-activity-id'), 'receiver_activity_id', '__AbsentNamespace0_CTD_ANON_16_receiver_activity_id', pyxb.binding.datatypes.string)
    __receiver_activity_id._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 729, 12)
    __receiver_activity_id._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 729, 12)
    
    receiver_activity_id = property(__receiver_activity_id.value, __receiver_activity_id.set, None, '\n                  If the funds are being provided to another activity \n                  that is reported to IATI, this should record the \n                  unique IATI activity identifier for that activity.\n                ')

    
    # Attribute ref uses Python identifier ref
    __ref = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'ref'), 'ref', '__AbsentNamespace0_CTD_ANON_16_ref', pyxb.binding.datatypes.string)
    __ref._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 181, 2)
    __ref._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 728, 12)
    
    ref = property(__ref.value, __ref.set, None, '\n        Machine-readable identification string for the business\n        object being described.\n      ')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None))
    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __receiver_activity_id.name() : __receiver_activity_id,
        __ref.name() : __ref
    })



# Complex type [anonymous] with content type MIXED
class CTD_ANON_17 (pyxb.binding.basis.complexTypeDefinition):
    """
              A milestone date for this transaction (such as the
              decision date, disbursement date, etc.).
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 748, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute iso-date uses Python identifier iso_date
    __iso_date = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'iso-date'), 'iso_date', '__AbsentNamespace0_CTD_ANON_17_iso_date', pyxb.binding.datatypes.date, required=True)
    __iso_date._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 752, 12)
    __iso_date._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 752, 12)
    
    iso_date = property(__iso_date.value, __iso_date.set, None, '\n                  The ISO 8601 version of the transaction date.\n                ')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None))
    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __iso_date.name() : __iso_date
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_18 (pyxb.binding.basis.complexTypeDefinition):
    """
        The sub-national geographical identification of the target 
        locations of an activity. These can be described by gazetteer 
        reference, coordinates, administrative areas or a textual 
        description.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 833, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element location-id uses Python identifier location_id
    __location_id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'location-id'), 'location_id', '__AbsentNamespace0_CTD_ANON_18_location_id', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 835, 8), )

    
    location_id = property(__location_id.value, __location_id.set, None, '\n               A unique code describing the location according to a \n               recognised gazetteer or administrative boundary \n               repository. Administrative areas should only be reported\n               here if the location being defined is the administrative\n               area itself. For describing the administrative area/s \n               within which a more specific location falls the \n               location/administrative element should be used. \n            ')

    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_CTD_ANON_18_name', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 870, 8), )

    
    name = property(__name.value, __name.set, None, '\n              The human-readable name for the location.  May be\n              repeated in different languages.\n            ')

    
    # Element description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'description'), 'description', '__AbsentNamespace0_CTD_ANON_18_description', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 878, 8), )

    
    description = property(__description.value, __description.set, None, '\n              A description that qualifies the location, not the \n              activity.\n            ')

    
    # Element activity-description uses Python identifier activity_description
    __activity_description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'activity-description'), 'activity_description', '__AbsentNamespace0_CTD_ANON_18_activity_description', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 886, 8), )

    
    activity_description = property(__activity_description.value, __activity_description.set, None, '\n              A description that qualifies the activity taking place at \n              the location. This should not duplicate information \n              provided in the main activity description, and should \n              typically be used to distinguish between activities at \n              multiple locations within a single iati-activity record.\n            ')

    
    # Element administrative uses Python identifier administrative
    __administrative = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'administrative'), 'administrative', '__AbsentNamespace0_CTD_ANON_18_administrative', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 897, 8), )

    
    administrative = property(__administrative.value, __administrative.set, None, '\n              Coded identification of national and sub-national \n              divisions according to recognised administrative \n              boundary repositories. Multiple levels may be reported.\n            ')

    
    # Element point uses Python identifier point
    __point = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'point'), 'point', '__AbsentNamespace0_CTD_ANON_18_point', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 975, 8), )

    
    point = property(__point.value, __point.set, None, '\n              The point element is based on a subset of the GML 3.3 Point\n              element.\n            ')

    
    # Element exactness uses Python identifier exactness
    __exactness = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'exactness'), 'exactness', '__AbsentNamespace0_CTD_ANON_18_exactness', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1008, 8), )

    
    exactness = property(__exactness.value, __exactness.set, None, '\n               Defines whether the location represents the most \n               distinct point reasonably possible for this type of \n               activity or is an approximation due to lack of more \n               detailed information. \n            ')

    
    # Element location-reach uses Python identifier location_reach
    __location_reach = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'location-reach'), 'location_reach', '__AbsentNamespace0_CTD_ANON_18_location_reach', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1032, 8), )

    
    location_reach = property(__location_reach.value, __location_reach.set, None, '\n               Does this location describe where the activity \n               takes place or where the intended beneficiaries reside?\n            ')

    
    # Element location-class uses Python identifier location_class
    __location_class = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'location-class'), 'location_class', '__AbsentNamespace0_CTD_ANON_18_location_class', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1041, 8), )

    
    location_class = property(__location_class.value, __location_class.set, None, '\n               Whether the location refers to a structure, a populated \n               place (e.g. city or village), an administrative \n               division, or another topological feature \n               (e.g. river, nature reserve).\n            ')

    
    # Element feature-designation uses Python identifier feature_designation
    __feature_designation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'feature-designation'), 'feature_designation', '__AbsentNamespace0_CTD_ANON_18_feature_designation', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1065, 8), )

    
    feature_designation = property(__feature_designation.value, __feature_designation.set, None, '\n               A more refined coded classification of the type of \n               feature referred to by this location.\n            ')

    
    # Element coordinates uses Python identifier coordinates
    __coordinates = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'coordinates'), 'coordinates', '__AbsentNamespace0_CTD_ANON_18_coordinates', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1089, 8), )

    
    coordinates = property(__coordinates.value, __coordinates.set, None, '\n              Deprecated since 1.04\n\n              Geodetic coordinates for the location (latitude, longitude).\n            ')

    
    # Element gazetteer-entry uses Python identifier gazetteer_entry
    __gazetteer_entry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'gazetteer-entry'), 'gazetteer_entry', '__AbsentNamespace0_CTD_ANON_18_gazetteer_entry', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1137, 8), )

    
    gazetteer_entry = property(__gazetteer_entry.value, __gazetteer_entry.set, None, "\n              Deprecated since 1.04\n\n              Identifier for this location's entry in a geographical\n              gazetteer, such as GEOnet.  The entry identifier is the\n              element content.\n            ")

    
    # Element location-type uses Python identifier location_type
    __location_type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'location-type'), 'location_type', '__AbsentNamespace0_CTD_ANON_18_location_type', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1165, 8), )

    
    location_type = property(__location_type.value, __location_type.set, None, '\n              Deprecated since 1.04\n\n              The type of location (e.g. "PCL" for a political entity) \n              from the feature designation codes maintained by the \n              US National Geospatial-Intelligence Agency\n\n              See http://iatistandard.org/codelists/location_type\n            ')

    
    # Attribute ref uses Python identifier ref
    __ref = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'ref'), 'ref', '__AbsentNamespace0_CTD_ANON_18_ref', pyxb.binding.datatypes.string)
    __ref._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 181, 2)
    __ref._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1180, 6)
    
    ref = property(__ref.value, __ref.set, None, '\n        Machine-readable identification string for the business\n        object being described.\n      ')

    
    # Attribute percentage uses Python identifier percentage
    __percentage = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'percentage'), 'percentage', '__AbsentNamespace0_CTD_ANON_18_percentage', pyxb.binding.datatypes.decimal)
    __percentage._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 199, 2)
    __percentage._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1188, 6)
    
    percentage = property(__percentage.value, __percentage.set, None, '\n        The percentage of the budget allocated to this item.  Content\n        must be a positive decimal number between 0 and 100, with no\n        percentage sign. In version 1.03 of the IATI Standard this\n        value became designated as a decimal value and no longer \n        as a positive integer.\n      ')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None))
    _HasWildcardElement = True
    _ElementMap.update({
        __location_id.name() : __location_id,
        __name.name() : __name,
        __description.name() : __description,
        __activity_description.name() : __activity_description,
        __administrative.name() : __administrative,
        __point.name() : __point,
        __exactness.name() : __exactness,
        __location_reach.name() : __location_reach,
        __location_class.name() : __location_class,
        __feature_designation.name() : __feature_designation,
        __coordinates.name() : __coordinates,
        __gazetteer_entry.name() : __gazetteer_entry,
        __location_type.name() : __location_type
    })
    _AttributeMap.update({
        __ref.name() : __ref,
        __percentage.name() : __percentage
    })



# Complex type [anonymous] with content type MIXED
class CTD_ANON_19 (pyxb.binding.basis.complexTypeDefinition):
    """
               A unique code describing the location according to a 
               recognised gazetteer or administrative boundary 
               repository. Administrative areas should only be reported
               here if the location being defined is the administrative
               area itself. For describing the administrative area/s 
               within which a more specific location falls the 
               location/administrative element should be used. 
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 847, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute vocabulary uses Python identifier vocabulary
    __vocabulary = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'vocabulary'), 'vocabulary', '__AbsentNamespace0_CTD_ANON_19_vocabulary', pyxb.binding.datatypes.string)
    __vocabulary._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 859, 12)
    __vocabulary._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 859, 12)
    
    vocabulary = property(__vocabulary.value, __vocabulary.set, None, '\n                  A code for a recognised gazetteer or administrative \n                  boundary respository.\n                ')

    
    # Attribute code uses Python identifier code
    __code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'code'), 'code', '__AbsentNamespace0_CTD_ANON_19_code', pyxb.binding.datatypes.string)
    __code._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 172, 2)
    __code._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 851, 12)
    
    code = property(__code.value, __code.set, None, '\n        Machine readable code for the entity being described. The value should\n        be available on a related codelist.\n      ')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None))
    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __vocabulary.name() : __vocabulary,
        __code.name() : __code
    })



# Complex type [anonymous] with content type MIXED
class CTD_ANON_20 (pyxb.binding.basis.complexTypeDefinition):
    """
              Coded identification of national and sub-national 
              divisions according to recognised administrative 
              boundary repositories. Multiple levels may be reported.
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 905, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute vocabulary uses Python identifier vocabulary
    __vocabulary = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'vocabulary'), 'vocabulary', '__AbsentNamespace0_CTD_ANON_20_vocabulary', pyxb.binding.datatypes.string)
    __vocabulary._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 917, 12)
    __vocabulary._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 917, 12)
    
    vocabulary = property(__vocabulary.value, __vocabulary.set, None, '\n                  The code for a recognised administrative boundary.\n                  repository\n                ')

    
    # Attribute level uses Python identifier level
    __level = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'level'), 'level', '__AbsentNamespace0_CTD_ANON_20_level', pyxb.binding.datatypes.nonNegativeInteger)
    __level._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 925, 12)
    __level._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 925, 12)
    
    level = property(__level.value, __level.set, None, '\n                   An integer indicating the hierarchical level being \n                   reported. Level 0 is the national boundary, level 1 \n                   is the first-level administrative sub-division, etc.\n                ')

    
    # Attribute country uses Python identifier country
    __country = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'country'), 'country', '__AbsentNamespace0_CTD_ANON_20_country', pyxb.binding.datatypes.string)
    __country._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 934, 12)
    __country._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 934, 12)
    
    country = property(__country.value, __country.set, None, '\n                  Deprecated since 1.04\n\n                  The ISO 3166-1 alpha2 code for the country\n                  (e.g. "GB" for the United Kingdom).\n\n                  For the @code attribute, see\n                  http://iatistandard.org/codelists/country\n                ')

    
    # Attribute adm1 uses Python identifier adm1
    __adm1 = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'adm1'), 'adm1', '__AbsentNamespace0_CTD_ANON_20_adm1', pyxb.binding.datatypes.string)
    __adm1._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 947, 12)
    __adm1._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 947, 12)
    
    adm1 = property(__adm1.value, __adm1.set, None, '\n                  Deprecated since 1.04\n\n                  The UNSALB level-one administrative code for a\n                  subdivision of a country.\n\n                  See http://iatistandard.org/codelists/admin1\n                ')

    
    # Attribute adm2 uses Python identifier adm2
    __adm2 = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'adm2'), 'adm2', '__AbsentNamespace0_CTD_ANON_20_adm2', pyxb.binding.datatypes.string)
    __adm2._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 959, 12)
    __adm2._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 959, 12)
    
    adm2 = property(__adm2.value, __adm2.set, None, '\n                  Deprecated since 1.04\n\n                  The UNSALB level-two administrative code for a\n                  subdivision of a country.\n\n                  See http://iatistandard.org/codelists/admin2\n                ')

    
    # Attribute code uses Python identifier code
    __code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'code'), 'code', '__AbsentNamespace0_CTD_ANON_20_code', pyxb.binding.datatypes.string)
    __code._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 172, 2)
    __code._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 909, 12)
    
    code = property(__code.value, __code.set, None, '\n        Machine readable code for the entity being described. The value should\n        be available on a related codelist.\n      ')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None))
    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __vocabulary.name() : __vocabulary,
        __level.name() : __level,
        __country.name() : __country,
        __adm1.name() : __adm1,
        __adm2.name() : __adm2,
        __code.name() : __code
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_21 (pyxb.binding.basis.complexTypeDefinition):
    """
              The point element is based on a subset of the GML 3.3 Point
              element.
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 982, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element pos uses Python identifier pos
    __pos = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'pos'), 'pos', '__AbsentNamespace0_CTD_ANON_21_pos', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 984, 14), )

    
    pos = property(__pos.value, __pos.set, None, '\n                    The latitude and longitude coordinates in the \n                    format "lat lng"\n                  ')

    
    # Attribute srsName uses Python identifier srsName
    __srsName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'srsName'), 'srsName', '__AbsentNamespace0_CTD_ANON_21_srsName', pyxb.binding.datatypes.string, required=True)
    __srsName._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 994, 12)
    __srsName._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 994, 12)
    
    srsName = property(__srsName.value, __srsName.set, None, '\n                  The name of the spatial reference system used by the \n                  coordinates. \n\n                  Always: http://www.opengis.net/def/crs/EPSG/0/4326\n                ')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None))
    _HasWildcardElement = True
    _ElementMap.update({
        __pos.name() : __pos
    })
    _AttributeMap.update({
        __srsName.name() : __srsName
    })



# Complex type [anonymous] with content type MIXED
class CTD_ANON_22 (pyxb.binding.basis.complexTypeDefinition):
    """
               Defines whether the location represents the most 
               distinct point reasonably possible for this type of 
               activity or is an approximation due to lack of more 
               detailed information. 
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1017, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute code uses Python identifier code
    __code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'code'), 'code', '__AbsentNamespace0_CTD_ANON_22_code', pyxb.binding.datatypes.string)
    __code._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 172, 2)
    __code._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1021, 12)
    
    code = property(__code.value, __code.set, None, '\n        Machine readable code for the entity being described. The value should\n        be available on a related codelist.\n      ')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None))
    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __code.name() : __code
    })



# Complex type [anonymous] with content type MIXED
class CTD_ANON_23 (pyxb.binding.basis.complexTypeDefinition):
    """
               Whether the location refers to a structure, a populated 
               place (e.g. city or village), an administrative 
               division, or another topological feature 
               (e.g. river, nature reserve).
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1050, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute code uses Python identifier code
    __code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'code'), 'code', '__AbsentNamespace0_CTD_ANON_23_code', pyxb.binding.datatypes.string)
    __code._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 172, 2)
    __code._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1054, 12)
    
    code = property(__code.value, __code.set, None, '\n        Machine readable code for the entity being described. The value should\n        be available on a related codelist.\n      ')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None))
    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __code.name() : __code
    })



# Complex type [anonymous] with content type MIXED
class CTD_ANON_24 (pyxb.binding.basis.complexTypeDefinition):
    """
               A more refined coded classification of the type of 
               feature referred to by this location.
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1072, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute code uses Python identifier code
    __code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'code'), 'code', '__AbsentNamespace0_CTD_ANON_24_code', pyxb.binding.datatypes.string)
    __code._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 172, 2)
    __code._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1076, 12)
    
    code = property(__code.value, __code.set, None, '\n        Machine readable code for the entity being described. The value should\n        be available on a related codelist.\n      ')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None))
    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __code.name() : __code
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_25 (pyxb.binding.basis.complexTypeDefinition):
    """
              Deprecated since 1.04

              Geodetic coordinates for the location (latitude, longitude).
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1097, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute latitude uses Python identifier latitude
    __latitude = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'latitude'), 'latitude', '__AbsentNamespace0_CTD_ANON_25_latitude', pyxb.binding.datatypes.decimal, required=True)
    __latitude._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1101, 12)
    __latitude._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1101, 12)
    
    latitude = property(__latitude.value, __latitude.set, None, '\n                  Deprecated since 1.04\n\n                  The decimal latitude (north is positive), e.g. "45.5"\n                  for 45.5 degrees north (45 degrees 30 minutes).\n                ')

    
    # Attribute longitude uses Python identifier longitude
    __longitude = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'longitude'), 'longitude', '__AbsentNamespace0_CTD_ANON_25_longitude', pyxb.binding.datatypes.decimal, required=True)
    __longitude._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1111, 12)
    __longitude._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1111, 12)
    
    longitude = property(__longitude.value, __longitude.set, None, '\n                  Deprecated since 1.04\n\n                  The decimal longitude (east is positive), e.g. "-75.5"\n                  for 75.5 degrees west (74 degrees 30 minutes).\n                ')

    
    # Attribute precision uses Python identifier precision
    __precision = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'precision'), 'precision', '__AbsentNamespace0_CTD_ANON_25_precision', pyxb.binding.datatypes.string)
    __precision._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1121, 12)
    __precision._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1121, 12)
    
    precision = property(__precision.value, __precision.set, None, '\n                  Deprecated since 1.04\n\n                  An IATI-defined subset of UCPD precision codes for\n                  the location (e.g. "2" for within 25 km of the\n                  specified latitude/longitude).\n\n                  See http://iatistandard.org/codelists/geographical_precision\n                ')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None))
    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __latitude.name() : __latitude,
        __longitude.name() : __longitude,
        __precision.name() : __precision
    })



# Complex type [anonymous] with content type MIXED
class CTD_ANON_26 (pyxb.binding.basis.complexTypeDefinition):
    """
              Deprecated since 1.04

              Identifier for this location's entry in a geographical
              gazetteer, such as GEOnet.  The entry identifier is the
              element content.
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1147, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute gazetteer-ref uses Python identifier gazetteer_ref
    __gazetteer_ref = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'gazetteer-ref'), 'gazetteer_ref', '__AbsentNamespace0_CTD_ANON_26_gazetteer_ref', pyxb.binding.datatypes.string, required=True)
    __gazetteer_ref._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1151, 12)
    __gazetteer_ref._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1151, 12)
    
    gazetteer_ref = property(__gazetteer_ref.value, __gazetteer_ref.set, None, '\n                  Deprecated since 1.04\n\n                  Reference to the gazetteer containing the entry.\n\n                  See http://iatistandard.org/codelists/gazetteer_agency\n                ')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None))
    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __gazetteer_ref.name() : __gazetteer_ref
    })



# Complex type [anonymous] with content type MIXED
class CTD_ANON_27 (pyxb.binding.basis.complexTypeDefinition):
    """
        Recipient country budget items.

        This item encodes the alignment of activities with both the
        functional and administrative classifications used in the
        recipient country's Chart of Accounts. This applies to both
        on- and off-budget activities.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1214, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element budget-item uses Python identifier budget_item
    __budget_item = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'budget-item'), 'budget_item', '__AbsentNamespace0_CTD_ANON_27_budget_item', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1216, 8), )

    
    budget_item = property(__budget_item.value, __budget_item.set, None, '\n              Identifier for a single item in the recipient-country\n              budget. If more than one identifier is reported the\n              percentage share must be reported and all percentages\n              should add up to 100 percent.\n            ')

    
    # Attribute vocabulary uses Python identifier vocabulary
    __vocabulary = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'vocabulary'), 'vocabulary', '__AbsentNamespace0_CTD_ANON_27_vocabulary', pyxb.binding.datatypes.string, required=True)
    __vocabulary._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1237, 6)
    __vocabulary._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1237, 6)
    
    vocabulary = property(__vocabulary.value, __vocabulary.set, None, '\n            A code for the common functional classification or country\n            system (This allows for common codes, country-specific, or\n            any other classification agreed between countries and\n            donors).\n          ')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None))
    _HasWildcardElement = True
    _ElementMap.update({
        __budget_item.name() : __budget_item
    })
    _AttributeMap.update({
        __vocabulary.name() : __vocabulary
    })



# Complex type [anonymous] with content type MIXED
class CTD_ANON_28 (pyxb.binding.basis.complexTypeDefinition):
    """
              Identifier for a single item in the recipient-country
              budget. If more than one identifier is reported the
              percentage share must be reported and all percentages
              should add up to 100 percent.
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1225, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'description'), 'description', '__AbsentNamespace0_CTD_ANON_28_description', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 36, 2), )

    
    description = property(__description.value, __description.set, None, '\n        A longer, human-readable description.  May be repeated for\n        different languages.\n      ')

    
    # Attribute code uses Python identifier code
    __code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'code'), 'code', '__AbsentNamespace0_CTD_ANON_28_code', pyxb.binding.datatypes.string, required=True)
    __code._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 172, 2)
    __code._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1230, 12)
    
    code = property(__code.value, __code.set, None, '\n        Machine readable code for the entity being described. The value should\n        be available on a related codelist.\n      ')

    
    # Attribute percentage uses Python identifier percentage
    __percentage = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'percentage'), 'percentage', '__AbsentNamespace0_CTD_ANON_28_percentage', pyxb.binding.datatypes.decimal)
    __percentage._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 199, 2)
    __percentage._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1231, 12)
    
    percentage = property(__percentage.value, __percentage.set, None, '\n        The percentage of the budget allocated to this item.  Content\n        must be a positive decimal number between 0 and 100, with no\n        percentage sign. In version 1.03 of the IATI Standard this\n        value became designated as a decimal value and no longer \n        as a positive integer.\n      ')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None))
    _HasWildcardElement = True
    _ElementMap.update({
        __description.name() : __description
    })
    _AttributeMap.update({
        __code.name() : __code,
        __percentage.name() : __percentage
    })



# Complex type [anonymous] with content type MIXED
class CTD_ANON_29 (pyxb.binding.basis.complexTypeDefinition):
    """
        Another IATI activity related to this one.  The 'type'
        attribute describes the type of relationship (e.g. parent,
        sibling).  This does not need to be used to express funding
        relationships, since those are covered in individual
        transactions.

        For the value of the @type attribute, see
        http://iatistandard.org/codelists/related_activity_type
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1264, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__AbsentNamespace0_CTD_ANON_29_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang)
    __lang._DeclarationLocation = None
    __lang._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 246, 4)
    
    lang = property(__lang.value, __lang.set, None, None)

    
    # Attribute ref uses Python identifier ref
    __ref = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'ref'), 'ref', '__AbsentNamespace0_CTD_ANON_29_ref', pyxb.binding.datatypes.string, required=True)
    __ref._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 181, 2)
    __ref._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1269, 6)
    
    ref = property(__ref.value, __ref.set, None, '\n        Machine-readable identification string for the business\n        object being described.\n      ')

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'type'), 'type', '__AbsentNamespace0_CTD_ANON_29_type', pyxb.binding.datatypes.string, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 190, 2)
    __type._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1270, 6)
    
    type = property(__type.value, __type.set, None, '\n        A machine readable code describing the type of thing being referenced.\n        The value should be available on a related codelist.\n      ')

    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __lang.name() : __lang,
        __ref.name() : __ref,
        __type.name() : __type
    })



# Complex type [anonymous] with content type MIXED
class CTD_ANON_30 (pyxb.binding.basis.complexTypeDefinition):
    """
        Hold a single name=value pair of legacy data.  This element is
        *not* for adding new data types; instead, it holds the
        original (non-IATI) value or code for an existing data type.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1282, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_CTD_ANON_30_name', pyxb.binding.datatypes.string, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1286, 6)
    __name._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1286, 6)
    
    name = property(__name.value, __name.set, None, '\n            The original field name.\n          ')

    
    # Attribute value uses Python identifier value_
    __value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'value'), 'value_', '__AbsentNamespace0_CTD_ANON_30_value', pyxb.binding.datatypes.string, required=True)
    __value._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1293, 6)
    __value._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1293, 6)
    
    value_ = property(__value.value, __value.set, None, '\n            The original field value.\n          ')

    
    # Attribute iati-equivalent uses Python identifier iati_equivalent
    __iati_equivalent = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'iati-equivalent'), 'iati_equivalent', '__AbsentNamespace0_CTD_ANON_30_iati_equivalent', pyxb.binding.datatypes.NMTOKEN)
    __iati_equivalent._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1300, 6)
    __iati_equivalent._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1300, 6)
    
    iati_equivalent = property(__iati_equivalent.value, __iati_equivalent.set, None, '\n            The name of the equivalent IATI element (if available).\n          ')

    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __name.name() : __name,
        __value.name() : __value,
        __iati_equivalent.name() : __iati_equivalent
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_31 (pyxb.binding.basis.complexTypeDefinition):
    """
        A measurable result of aid work.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1316, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element indicator uses Python identifier indicator
    __indicator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'indicator'), 'indicator', '__AbsentNamespace0_CTD_ANON_31_indicator', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1320, 8), )

    
    indicator = property(__indicator.value, __indicator.set, None, '\n              The indicator(s) that meet the results. There can be\n              multiple indicators for each result.\n            ')

    
    # Element title uses Python identifier title
    __title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'title'), 'title', '__AbsentNamespace0_CTD_ANON_31_title', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 27, 2), )

    
    title = property(__title.value, __title.set, None, '\n        A short, human-readable title.  May be repeated for different\n        languages.\n      ')

    
    # Element description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'description'), 'description', '__AbsentNamespace0_CTD_ANON_31_description', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 36, 2), )

    
    description = property(__description.value, __description.set, None, '\n        A longer, human-readable description.  May be repeated for\n        different languages.\n      ')

    
    # Attribute aggregation-status uses Python identifier aggregation_status
    __aggregation_status = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'aggregation-status'), 'aggregation_status', '__AbsentNamespace0_CTD_ANON_31_aggregation_status', pyxb.binding.datatypes.boolean)
    __aggregation_status._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1453, 6)
    __aggregation_status._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1453, 6)
    
    aggregation_status = property(__aggregation_status.value, __aggregation_status.set, None, '\n            Boolean flag indicating whether the data in the result set\n            are suitable for aggregation.\n          ')

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'type'), 'type', '__AbsentNamespace0_CTD_ANON_31_type', pyxb.binding.datatypes.string, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 190, 2)
    __type._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1452, 6)
    
    type = property(__type.value, __type.set, None, '\n        A machine readable code describing the type of thing being referenced.\n        The value should be available on a related codelist.\n      ')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None))
    _HasWildcardElement = True
    _ElementMap.update({
        __indicator.name() : __indicator,
        __title.name() : __title,
        __description.name() : __description
    })
    _AttributeMap.update({
        __aggregation_status.name() : __aggregation_status,
        __type.name() : __type
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_32 (pyxb.binding.basis.complexTypeDefinition):
    """
              The indicator(s) that meet the results. There can be
              multiple indicators for each result.
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1327, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element baseline uses Python identifier baseline
    __baseline = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'baseline'), 'baseline', '__AbsentNamespace0_CTD_ANON_32_baseline', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1331, 14), )

    
    baseline = property(__baseline.value, __baseline.set, None, '\n                    The baseline value for the indicator\n                  ')

    
    # Element period uses Python identifier period
    __period = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'period'), 'period', '__AbsentNamespace0_CTD_ANON_32_period', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1359, 14), )

    
    period = property(__period.value, __period.set, None, '\n                    The period covered for the results\n                    reported. Multiple periods can be reported for a\n                    single indicator.\n                  ')

    
    # Element title uses Python identifier title
    __title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'title'), 'title', '__AbsentNamespace0_CTD_ANON_32_title', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 27, 2), )

    
    title = property(__title.value, __title.set, None, '\n        A short, human-readable title.  May be repeated for different\n        languages.\n      ')

    
    # Element description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'description'), 'description', '__AbsentNamespace0_CTD_ANON_32_description', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 36, 2), )

    
    description = property(__description.value, __description.set, None, '\n        A longer, human-readable description.  May be repeated for\n        different languages.\n      ')

    
    # Attribute measure uses Python identifier measure
    __measure = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'measure'), 'measure', '__AbsentNamespace0_CTD_ANON_32_measure', pyxb.binding.datatypes.string, required=True)
    __measure._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1430, 12)
    __measure._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1430, 12)
    
    measure = property(__measure.value, __measure.set, None, '\n                  The type of measurement for the indicator value\n                ')

    
    # Attribute ascending uses Python identifier ascending
    __ascending = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ascending'), 'ascending', '__AbsentNamespace0_CTD_ANON_32_ascending', pyxb.binding.datatypes.boolean)
    __ascending._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1437, 12)
    __ascending._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1437, 12)
    
    ascending = property(__ascending.value, __ascending.set, None, '\n                  True if the indicator improves from small to large\n                  (e.g. clinics built); false if it improves from\n                  large to small (e.g. cases of a disease). Defaults\n                  to true if omitted.\n                ')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None))
    _HasWildcardElement = True
    _ElementMap.update({
        __baseline.name() : __baseline,
        __period.name() : __period,
        __title.name() : __title,
        __description.name() : __description
    })
    _AttributeMap.update({
        __measure.name() : __measure,
        __ascending.name() : __ascending
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_33 (pyxb.binding.basis.complexTypeDefinition):
    """
                    The baseline value for the indicator
                  """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1337, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element comment uses Python identifier comment
    __comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'comment'), 'comment', '__AbsentNamespace0_CTD_ANON_33_comment', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 53, 2), )

    
    comment = property(__comment.value, __comment.set, None, '\n        A human-readable comment associated with a piece of aid information.\n      ')

    
    # Attribute year uses Python identifier year
    __year = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'year'), 'year', '__AbsentNamespace0_CTD_ANON_33_year', pyxb.binding.datatypes.positiveInteger, required=True)
    __year._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1342, 18)
    __year._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1342, 18)
    
    year = property(__year.value, __year.set, None, '\n                        The year the baseline value was taken\n                      ')

    
    # Attribute value uses Python identifier value_
    __value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'value'), 'value_', '__AbsentNamespace0_CTD_ANON_33_value', pyxb.binding.datatypes.string, required=True)
    __value._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1349, 18)
    __value._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1349, 18)
    
    value_ = property(__value.value, __value.set, None, '\n                        The baseline value.\n                      ')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None))
    _HasWildcardElement = True
    _ElementMap.update({
        __comment.name() : __comment
    })
    _AttributeMap.update({
        __year.name() : __year,
        __value.name() : __value
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_34 (pyxb.binding.basis.complexTypeDefinition):
    """
                    The period covered for the results
                    reported. Multiple periods can be reported for a
                    single indicator.
                  """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1367, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element period-start uses Python identifier period_start
    __period_start = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'period-start'), 'period_start', '__AbsentNamespace0_CTD_ANON_34_period_start', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1369, 20), )

    
    period_start = property(__period_start.value, __period_start.set, None, '\n                          The start of the reporting period\n                        ')

    
    # Element period-end uses Python identifier period_end
    __period_end = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'period-end'), 'period_end', '__AbsentNamespace0_CTD_ANON_34_period_end', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1376, 20), )

    
    period_end = property(__period_end.value, __period_end.set, None, '\n                          The end of the reporting period\n                        ')

    
    # Element target uses Python identifier target
    __target = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'target'), 'target', '__AbsentNamespace0_CTD_ANON_34_target', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1383, 20), )

    
    target = property(__target.value, __target.set, None, '\n                          The target milestone for this period\n                        ')

    
    # Element actual uses Python identifier actual
    __actual = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'actual'), 'actual', '__AbsentNamespace0_CTD_ANON_34_actual', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1403, 20), )

    
    actual = property(__actual.value, __actual.set, None, '\n                          A record of the achieved result for this period.\n                        ')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None))
    _HasWildcardElement = True
    _ElementMap.update({
        __period_start.name() : __period_start,
        __period_end.name() : __period_end,
        __target.name() : __target,
        __actual.name() : __actual
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_35 (pyxb.binding.basis.complexTypeDefinition):
    """
                          The target milestone for this period
                        """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1389, 22)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element comment uses Python identifier comment
    __comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'comment'), 'comment', '__AbsentNamespace0_CTD_ANON_35_comment', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 53, 2), )

    
    comment = property(__comment.value, __comment.set, None, '\n        A human-readable comment associated with a piece of aid information.\n      ')

    
    # Attribute value uses Python identifier value_
    __value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'value'), 'value_', '__AbsentNamespace0_CTD_ANON_35_value', pyxb.binding.datatypes.string, required=True)
    __value._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1394, 24)
    __value._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1394, 24)
    
    value_ = property(__value.value, __value.set, None, '\n                              The target value.\n                            ')

    _HasWildcardElement = True
    _ElementMap.update({
        __comment.name() : __comment
    })
    _AttributeMap.update({
        __value.name() : __value
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_36 (pyxb.binding.basis.complexTypeDefinition):
    """
                          A record of the achieved result for this period.
                        """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1409, 22)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element comment uses Python identifier comment
    __comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'comment'), 'comment', '__AbsentNamespace0_CTD_ANON_36_comment', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 53, 2), )

    
    comment = property(__comment.value, __comment.set, None, '\n        A human-readable comment associated with a piece of aid information.\n      ')

    
    # Attribute value uses Python identifier value_
    __value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'value'), 'value_', '__AbsentNamespace0_CTD_ANON_36_value', pyxb.binding.datatypes.string, required=True)
    __value._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1414, 24)
    __value._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1414, 24)
    
    value_ = property(__value.value, __value.set, None, '\n                              The actual measure.\n                            ')

    _HasWildcardElement = True
    _ElementMap.update({
        __comment.name() : __comment
    })
    _AttributeMap.update({
        __value.name() : __value
    })



# Complex type indicatorOutcomeType with content type MIXED
class indicatorOutcomeType (pyxb.binding.basis.complexTypeDefinition):
    """
        Content type for a baseline or actual/planned outcome for an
        indicator.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'indicatorOutcomeType')
    _XSDLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1465, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__AbsentNamespace0_indicatorOutcomeType_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang)
    __lang._DeclarationLocation = None
    __lang._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 246, 4)
    
    lang = property(__lang.value, __lang.set, None, None)

    
    # Attribute year uses Python identifier year
    __year = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'year'), 'year', '__AbsentNamespace0_indicatorOutcomeType_year', pyxb.binding.datatypes.string)
    __year._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1475, 4)
    __year._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1475, 4)
    
    year = property(__year.value, __year.set, None, '\n          The year of the baseline or outcome.\n        ')

    
    # Attribute value uses Python identifier value_
    __value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'value'), 'value_', '__AbsentNamespace0_indicatorOutcomeType_value', pyxb.binding.datatypes.string)
    __value._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1482, 4)
    __value._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1482, 4)
    
    value_ = property(__value.value, __value.set, None, '\n          The value of the baseline or outcome.\n        ')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None))
    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __lang.name() : __lang,
        __year.name() : __year,
        __value.name() : __value
    })
Namespace.addCategoryObject('typeBinding', 'indicatorOutcomeType', indicatorOutcomeType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_37 (pyxb.binding.basis.complexTypeDefinition):
    """
        Conditions attached to the activity.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1499, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element condition uses Python identifier condition
    __condition = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'condition'), 'condition', '__AbsentNamespace0_CTD_ANON_37_condition', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1501, 8), )

    
    condition = property(__condition.value, __condition.set, None, '\n              Description of one condition attached to the activity.\n            ')

    
    # Attribute attached uses Python identifier attached
    __attached = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'attached'), 'attached', '__AbsentNamespace0_CTD_ANON_37_attached', pyxb.binding.datatypes.boolean, required=True)
    __attached._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1517, 6)
    __attached._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1517, 6)
    
    attached = property(__attached.value, __attached.set, None, '\n            A yes/no (1/0) value stating whether there are conditions\n            attached to the activity.\n          ')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None))
    _HasWildcardElement = True
    _ElementMap.update({
        __condition.name() : __condition
    })
    _AttributeMap.update({
        __attached.name() : __attached
    })



# Complex type [anonymous] with content type MIXED
class CTD_ANON_38 (pyxb.binding.basis.complexTypeDefinition):
    """
              Description of one condition attached to the activity.
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1507, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__AbsentNamespace0_CTD_ANON_38_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang)
    __lang._DeclarationLocation = None
    __lang._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 246, 4)
    
    lang = property(__lang.value, __lang.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'type'), 'type', '__AbsentNamespace0_CTD_ANON_38_type', pyxb.binding.datatypes.string, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 190, 2)
    __type._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1511, 12)
    
    type = property(__type.value, __type.set, None, '\n        A machine readable code describing the type of thing being referenced.\n        The value should be available on a related codelist.\n      ')

    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __lang.name() : __lang,
        __type.name() : __type
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_39 (pyxb.binding.basis.complexTypeDefinition):
    """
        The value of the aid activity's budget for each financial year
        as in the original project document.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1536, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element period-start uses Python identifier period_start
    __period_start = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'period-start'), 'period_start', '__AbsentNamespace0_CTD_ANON_39_period_start', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1538, 8), )

    
    period_start = property(__period_start.value, __period_start.set, None, '\n              The starting date for the budget period, in ISO 8601\n              format (e.g. 2010-04-01 for 1 April 2010).  This element\n              must be present.\n            ')

    
    # Element period-end uses Python identifier period_end
    __period_end = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'period-end'), 'period_end', '__AbsentNamespace0_CTD_ANON_39_period_end', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1547, 8), )

    
    period_end = property(__period_end.value, __period_end.set, None, '\n              The ending date for the budget period, in ISO 8601\n              format (e.g. 2011-03-31 for 31 March 2011).  This\n              element must be present.\n            ')

    
    # Element value uses Python identifier value_
    __value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'value'), 'value_', '__AbsentNamespace0_CTD_ANON_39_value', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1556, 8), )

    
    value_ = property(__value.value, __value.set, None, "\n              The total value of the organisation's aid budget for\n              this period.  This element is required.\n            ")

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'type'), 'type', '__AbsentNamespace0_CTD_ANON_39_type', pyxb.binding.datatypes.string)
    __type._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 190, 2)
    __type._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1566, 6)
    
    type = property(__type.value, __type.set, None, '\n        A machine readable code describing the type of thing being referenced.\n        The value should be available on a related codelist.\n      ')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None))
    _HasWildcardElement = True
    _ElementMap.update({
        __period_start.name() : __period_start,
        __period_end.name() : __period_end,
        __value.name() : __value
    })
    _AttributeMap.update({
        __type.name() : __type
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_40 (pyxb.binding.basis.complexTypeDefinition):
    """
        The planned disbursement element should only be used to report
        specific planned cash transfers. These should be reported for
        a specific date or a meaningfully predictable period. These
        transactions should be reported in addition to budgets - which
        are typically annual breakdowns of the total activity
        commitment.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1582, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element period-start uses Python identifier period_start
    __period_start = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'period-start'), 'period_start', '__AbsentNamespace0_CTD_ANON_40_period_start', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1584, 8), )

    
    period_start = property(__period_start.value, __period_start.set, None, '\n              The starting date for the disbursement period, in ISO 8601\n              format (e.g. 2010-04-01 for 1 April 2010).  This element\n              must be present.\n            ')

    
    # Element period-end uses Python identifier period_end
    __period_end = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'period-end'), 'period_end', '__AbsentNamespace0_CTD_ANON_40_period_end', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1593, 8), )

    
    period_end = property(__period_end.value, __period_end.set, None, '\n              The ending date for the disbursement period, in ISO 8601\n              format (e.g. 2011-03-31 for 31 March 2011).  This\n              element must be present.\n            ')

    
    # Element value uses Python identifier value_
    __value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'value'), 'value_', '__AbsentNamespace0_CTD_ANON_40_value', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1602, 8), )

    
    value_ = property(__value.value, __value.set, None, '\n              The amount to be disbursed in the specified currency.\n            ')

    
    # Attribute updated uses Python identifier updated
    __updated = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'updated'), 'updated', '__AbsentNamespace0_CTD_ANON_40_updated', pyxb.binding.datatypes.date)
    __updated._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1611, 6)
    __updated._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1611, 6)
    
    updated = property(__updated.value, __updated.set, None, '\n            The date on which this line of information was last\n            updated. Previous updates for the same period should also\n            be reported.\n          ')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None))
    _HasWildcardElement = True
    _ElementMap.update({
        __period_start.name() : __period_start,
        __period_end.name() : __period_end,
        __value.name() : __value
    })
    _AttributeMap.update({
        __updated.name() : __updated
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_41 (pyxb.binding.basis.complexTypeDefinition):
    """
        Additional items specific to CRS++ reporting.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1630, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element aidtype-flag uses Python identifier aidtype_flag
    __aidtype_flag = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'aidtype-flag'), 'aidtype_flag', '__AbsentNamespace0_CTD_ANON_41_aidtype_flag', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1632, 8), )

    
    aidtype_flag = property(__aidtype_flag.value, __aidtype_flag.set, None, '\n              This covers the four CRS++ fields titled: \n              "Free standing technical cooperation"; \n              "Programme-based approach"; \n              "Investment project"; \n              "Associated financing"\n            ')

    
    # Element loan-terms uses Python identifier loan_terms
    __loan_terms = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'loan-terms'), 'loan_terms', '__AbsentNamespace0_CTD_ANON_41_loan_terms', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1657, 8), )

    
    loan_terms = property(__loan_terms.value, __loan_terms.set, None, '\n              Loan repayment terms and interest rates\n            ')

    
    # Element loan-status uses Python identifier loan_status
    __loan_status = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'loan-status'), 'loan_status', '__AbsentNamespace0_CTD_ANON_41_loan_status', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1736, 8), )

    
    loan_status = property(__loan_status.value, __loan_status.set, None, '\n              The status of loan and interest repayments for the most\n              recently reported financial year\n            ')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None))
    _HasWildcardElement = True
    _ElementMap.update({
        __aidtype_flag.name() : __aidtype_flag,
        __loan_terms.name() : __loan_terms,
        __loan_status.name() : __loan_status
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type MIXED
class CTD_ANON_42 (pyxb.binding.basis.complexTypeDefinition):
    """
              This covers the four CRS++ fields titled: 
              "Free standing technical cooperation"; 
              "Programme-based approach"; 
              "Investment project"; 
              "Associated financing"
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1642, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute significance uses Python identifier significance
    __significance = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'significance'), 'significance', '__AbsentNamespace0_CTD_ANON_42_significance', pyxb.binding.datatypes.boolean, required=True)
    __significance._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1647, 12)
    __significance._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1647, 12)
    
    significance = property(__significance.value, __significance.set, None, "\n                  Does this flag apply? If 'false' do not report the flag\n                ")

    
    # Attribute code uses Python identifier code
    __code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'code'), 'code', '__AbsentNamespace0_CTD_ANON_42_code', pyxb.binding.datatypes.string, required=True)
    __code._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 172, 2)
    __code._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1646, 12)
    
    code = property(__code.value, __code.set, None, '\n        Machine readable code for the entity being described. The value should\n        be available on a related codelist.\n      ')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None))
    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __significance.name() : __significance,
        __code.name() : __code
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_43 (pyxb.binding.basis.complexTypeDefinition):
    """
              Loan repayment terms and interest rates
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1663, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element repayment-type uses Python identifier repayment_type
    __repayment_type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'repayment-type'), 'repayment_type', '__AbsentNamespace0_CTD_ANON_43_repayment_type', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1665, 14), )

    
    repayment_type = property(__repayment_type.value, __repayment_type.set, None, '\n                    Type of Repayment. 1 = equal principal payments\n                    (EPP); 2 = annuity; 3 = lump sum; 5 = other,\n                    Codes are listed at\n                    http://iatistandard.org/codelists/crs-repayment-type\n                  ')

    
    # Element repayment-plan uses Python identifier repayment_plan
    __repayment_plan = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'repayment-plan'), 'repayment_plan', '__AbsentNamespace0_CTD_ANON_43_repayment_plan', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1675, 14), )

    
    repayment_plan = property(__repayment_plan.value, __repayment_plan.set, None, '\n                    Number of repayments per annum. 1 = annual; 2 =\n                    semi-annual; 4 = quarterly; 12 = monthly. Codes\n                    are listed at\n                    http://iatistandard.org/codelists/repayment-nopa.\n                  ')

    
    # Element commitment-date uses Python identifier commitment_date
    __commitment_date = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'commitment-date'), 'commitment_date', '__AbsentNamespace0_CTD_ANON_43_commitment_date', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1685, 14), )

    
    commitment_date = property(__commitment_date.value, __commitment_date.set, None, '\n                    Commitment date.The date must be in ISO 8601\n                    format (YYYY-MM-DD).\n                  ')

    
    # Element repayment-first-date uses Python identifier repayment_first_date
    __repayment_first_date = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'repayment-first-date'), 'repayment_first_date', '__AbsentNamespace0_CTD_ANON_43_repayment_first_date', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1693, 14), )

    
    repayment_first_date = property(__repayment_first_date.value, __repayment_first_date.set, None, '\n                    First Repayment Date. The date must be in ISO\n                    8601 format (YYYY-MM-DD).\n                  ')

    
    # Element repayment-final-date uses Python identifier repayment_final_date
    __repayment_final_date = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'repayment-final-date'), 'repayment_final_date', '__AbsentNamespace0_CTD_ANON_43_repayment_final_date', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1701, 14), )

    
    repayment_final_date = property(__repayment_final_date.value, __repayment_final_date.set, None, '\n                    Final Repayment Date. The date must be in ISO\n                    8601 format (YYYY-MM-DD).\n                  ')

    
    # Attribute rate-1 uses Python identifier rate_1
    __rate_1 = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'rate-1'), 'rate_1', '__AbsentNamespace0_CTD_ANON_43_rate_1', pyxb.binding.datatypes.decimal)
    __rate_1._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1711, 12)
    __rate_1._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1711, 12)
    
    rate_1 = property(__rate_1.value, __rate_1.set, None, '\n                  Interest Rate. If an ODA loan with variable\n                  interest rate, report the variable rate here and\n                  the reference fixed rate as rate-2\n\n                  Enter the rate without the percentage sign.\n                ')

    
    # Attribute rate-2 uses Python identifier rate_2
    __rate_2 = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'rate-2'), 'rate_2', '__AbsentNamespace0_CTD_ANON_43_rate_2', pyxb.binding.datatypes.decimal)
    __rate_2._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1722, 12)
    __rate_2._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1722, 12)
    
    rate_2 = property(__rate_2.value, __rate_2.set, None, '\n                  Second Interest Rate.  If an ODA loan with\n                  variable interest rate, report the variable rate\n                  as rate-1 and the reference fixed rate here\n\n                  Enter the rate without the percentage sign.\n                ')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None))
    _HasWildcardElement = True
    _ElementMap.update({
        __repayment_type.name() : __repayment_type,
        __repayment_plan.name() : __repayment_plan,
        __commitment_date.name() : __commitment_date,
        __repayment_first_date.name() : __repayment_first_date,
        __repayment_final_date.name() : __repayment_final_date
    })
    _AttributeMap.update({
        __rate_1.name() : __rate_1,
        __rate_2.name() : __rate_2
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_44 (pyxb.binding.basis.complexTypeDefinition):
    """
              The status of loan and interest repayments for the most
              recently reported financial year
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1743, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element interest-received uses Python identifier interest_received
    __interest_received = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'interest-received'), 'interest_received', '__AbsentNamespace0_CTD_ANON_44_interest_received', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1745, 14), )

    
    interest_received = property(__interest_received.value, __interest_received.set, None, '\n                    Interest received during the reporting year\n                  ')

    
    # Element principal-outstanding uses Python identifier principal_outstanding
    __principal_outstanding = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'principal-outstanding'), 'principal_outstanding', '__AbsentNamespace0_CTD_ANON_44_principal_outstanding', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1752, 14), )

    
    principal_outstanding = property(__principal_outstanding.value, __principal_outstanding.set, None, '\n                    The amount of principal owed on the loan at the\n                    end of the reporting year.\n                  ')

    
    # Element principal-arrears uses Python identifier principal_arrears
    __principal_arrears = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'principal-arrears'), 'principal_arrears', '__AbsentNamespace0_CTD_ANON_44_principal_arrears', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1760, 14), )

    
    principal_arrears = property(__principal_arrears.value, __principal_arrears.set, None, '\n                    Arrears of principal at the end of the\n                    year. Included in principal-outstanding\n                  ')

    
    # Element interest-arrears uses Python identifier interest_arrears
    __interest_arrears = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'interest-arrears'), 'interest_arrears', '__AbsentNamespace0_CTD_ANON_44_interest_arrears', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1768, 14), )

    
    interest_arrears = property(__interest_arrears.value, __interest_arrears.set, None, '\n                    Arrears of interest at the end of the year\n                  ')

    
    # Attribute year uses Python identifier year
    __year = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'year'), 'year', '__AbsentNamespace0_CTD_ANON_44_year', pyxb.binding.datatypes.decimal, required=True)
    __year._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1777, 12)
    __year._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1777, 12)
    
    year = property(__year.value, __year.set, None, '\n                  CRS Reporting Year (CRS++ Column 1)\n                ')

    
    # Attribute currency uses Python identifier currency
    __currency = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'currency'), 'currency', '__AbsentNamespace0_CTD_ANON_44_currency', pyxb.binding.datatypes.string)
    __currency._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 211, 2)
    __currency._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1784, 12)
    
    currency = property(__currency.value, __currency.set, None, '\n        A three letter ISO 4217 code for the original currency of the \n        amount.\n        This is required for all currency amounts unless the\n        iati-activity/@default-currency (or iati-organisation/@default-currency\n        for an organisation file) attribute is specified.\n\n        Currency codes are listed at\n        http://iatistandard.org/codelists/currency\n      ')

    
    # Attribute value-date uses Python identifier value_date
    __value_date = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'value-date'), 'value_date', '__AbsentNamespace0_CTD_ANON_44_value_date', pyxb.binding.datatypes.date, required=True)
    __value_date._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 226, 2)
    __value_date._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1785, 12)
    
    value_date = property(__value_date.value, __value_date.set, None, '\n        The date that this value was set (to allow historical\n        currency conversion).  The date must be in ISO 8601\n        format (YYYY-MM-DD).\n      ')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None))
    _HasWildcardElement = True
    _ElementMap.update({
        __interest_received.name() : __interest_received,
        __principal_outstanding.name() : __principal_outstanding,
        __principal_arrears.name() : __principal_arrears,
        __interest_arrears.name() : __interest_arrears
    })
    _AttributeMap.update({
        __year.name() : __year,
        __currency.name() : __currency,
        __value_date.name() : __value_date
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_45 (pyxb.binding.basis.complexTypeDefinition):
    """
        This section allows entry of data required for the OECD
        DAC Forward Spending Survey at an activity level.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1802, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element forecast uses Python identifier forecast
    __forecast = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'forecast'), 'forecast', '__AbsentNamespace0_CTD_ANON_45_forecast', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1804, 8), )

    
    forecast = property(__forecast.value, __forecast.set, None, '\n              A container to hold separate forecasts for each of\n              the years specified\n            ')

    
    # Attribute extraction-date uses Python identifier extraction_date
    __extraction_date = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'extraction-date'), 'extraction_date', '__AbsentNamespace0_CTD_ANON_45_extraction_date', pyxb.binding.datatypes.date, required=True)
    __extraction_date._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1830, 6)
    __extraction_date._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1830, 6)
    
    extraction_date = property(__extraction_date.value, __extraction_date.set, None, "\n            The exact date when the information was collected or\n            extracted from donors' aid management systems.\n          ")

    
    # Attribute priority uses Python identifier priority
    __priority = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'priority'), 'priority', '__AbsentNamespace0_CTD_ANON_45_priority', pyxb.binding.datatypes.boolean)
    __priority._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1838, 6)
    __priority._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1838, 6)
    
    priority = property(__priority.value, __priority.set, None, '\n            True if the partner country is a priority partner country.\n          ')

    
    # Attribute phaseout-year uses Python identifier phaseout_year
    __phaseout_year = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'phaseout-year'), 'phaseout_year', '__AbsentNamespace0_CTD_ANON_45_phaseout_year', pyxb.binding.datatypes.decimal)
    __phaseout_year._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1845, 6)
    __phaseout_year._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1845, 6)
    
    phaseout_year = property(__phaseout_year.value, __phaseout_year.set, None, '\n            If there are plans to phase out operations from the\n            partner country, this column shows the projected\n            year of last disbursements.\n          ')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None))
    _HasWildcardElement = True
    _ElementMap.update({
        __forecast.name() : __forecast
    })
    _AttributeMap.update({
        __extraction_date.name() : __extraction_date,
        __priority.name() : __priority,
        __phaseout_year.name() : __phaseout_year
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_46 (pyxb.binding.basis.complexTypeDefinition):
    """
              A container to hold separate forecasts for each of
              the years specified
            """
    _TypeDefinition = pyxb.binding.datatypes.decimal
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1811, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.decimal
    
    # Attribute year uses Python identifier year
    __year = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'year'), 'year', '__AbsentNamespace0_CTD_ANON_46_year', pyxb.binding.datatypes.decimal, required=True)
    __year._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1814, 16)
    __year._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1814, 16)
    
    year = property(__year.value, __year.set, None, '\n                      The calendar year that the forward spend covers\n                    ')

    
    # Attribute currency uses Python identifier currency
    __currency = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'currency'), 'currency', '__AbsentNamespace0_CTD_ANON_46_currency', pyxb.binding.datatypes.string)
    __currency._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 211, 2)
    __currency._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1821, 16)
    
    currency = property(__currency.value, __currency.set, None, '\n        A three letter ISO 4217 code for the original currency of the \n        amount.\n        This is required for all currency amounts unless the\n        iati-activity/@default-currency (or iati-organisation/@default-currency\n        for an organisation file) attribute is specified.\n\n        Currency codes are listed at\n        http://iatistandard.org/codelists/currency\n      ')

    
    # Attribute value-date uses Python identifier value_date
    __value_date = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'value-date'), 'value_date', '__AbsentNamespace0_CTD_ANON_46_value_date', pyxb.binding.datatypes.date)
    __value_date._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 226, 2)
    __value_date._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1822, 16)
    
    value_date = property(__value_date.value, __value_date.set, None, '\n        The date that this value was set (to allow historical\n        currency conversion).  The date must be in ISO 8601\n        format (YYYY-MM-DD).\n      ')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __year.name() : __year,
        __currency.name() : __currency,
        __value_date.name() : __value_date
    })



# Complex type [anonymous] with content type MIXED
class CTD_ANON_47 (pyxb.binding.basis.complexTypeDefinition):
    """
        A longer, human-readable description.  May be repeated for
        different languages.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 43, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__AbsentNamespace0_CTD_ANON_47_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang)
    __lang._DeclarationLocation = None
    __lang._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 246, 4)
    
    lang = property(__lang.value, __lang.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'type'), 'type', '__AbsentNamespace0_CTD_ANON_47_type', pyxb.binding.datatypes.string)
    __type._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 190, 2)
    __type._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 48, 6)
    
    type = property(__type.value, __type.set, None, '\n        A machine readable code describing the type of thing being referenced.\n        The value should be available on a related codelist.\n      ')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None))
    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __lang.name() : __lang,
        __type.name() : __type
    })



# Complex type [anonymous] with content type MIXED
class CTD_ANON_48 (pyxb.binding.basis.complexTypeDefinition):
    """
        The iati-identifier element is used in both Activity files and
        Organisation files, and has a slightly different meaning depending on
        where it is being used, and should not be confused.

        When used in an organisation it is a globally unique identifier for
        that organisation.

        When used in an activity it is a globally unique identifier for that
        activity.  This should be in the form of the IATI Organisation
        Identifier (for the reporting organisation) concatenated to that
        organisation's activity identifier. (NB. Two or more reporting
        organisations may publish information on the same activity.)
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 78, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type MIXED
class CTD_ANON_49 (pyxb.binding.basis.complexTypeDefinition):
    """
        The organisation issuing the report.
        May be a primary source (reporting on its own activity as
        donor, implementing agency, etc) or a secondary source
        (reporting on the activities of another organisation). 
        
        Specifying the @ref attribute is mandatory.
        May contain the organisation name as content.
        
        All activities in an activity xml file must contain the same
        @ref AND this @ref must be the same as the iati-identifier
        recorded in the registry publisher record of the account under
        which this file is published.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 100, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__AbsentNamespace0_CTD_ANON_49_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang)
    __lang._DeclarationLocation = None
    __lang._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 246, 4)
    
    lang = property(__lang.value, __lang.set, None, None)

    
    # Attribute secondary-reporter uses Python identifier secondary_reporter
    __secondary_reporter = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'secondary-reporter'), 'secondary_reporter', '__AbsentNamespace0_CTD_ANON_49_secondary_reporter', pyxb.binding.datatypes.boolean)
    __secondary_reporter._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 106, 6)
    __secondary_reporter._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 106, 6)
    
    secondary_reporter = property(__secondary_reporter.value, __secondary_reporter.set, None, '\n             If an activity is being published by a secondary publisher\n             you may indicate this here. Use 1 for true, 0 for false.\n          ')

    
    # Attribute ref uses Python identifier ref
    __ref = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'ref'), 'ref', '__AbsentNamespace0_CTD_ANON_49_ref', pyxb.binding.datatypes.string, required=True)
    __ref._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 181, 2)
    __ref._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 104, 6)
    
    ref = property(__ref.value, __ref.set, None, '\n        Machine-readable identification string for the business\n        object being described.\n      ')

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'type'), 'type', '__AbsentNamespace0_CTD_ANON_49_type', pyxb.binding.datatypes.string)
    __type._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 190, 2)
    __type._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 105, 6)
    
    type = property(__type.value, __type.set, None, '\n        A machine readable code describing the type of thing being referenced.\n        The value should be available on a related codelist.\n      ')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None))
    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __lang.name() : __lang,
        __secondary_reporter.name() : __secondary_reporter,
        __ref.name() : __ref,
        __type.name() : __type
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_50 (pyxb.binding.basis.complexTypeDefinition):
    """
        A categorized link to an external document.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 125, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element title uses Python identifier title
    __title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'title'), 'title', '__AbsentNamespace0_CTD_ANON_50_title', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 27, 2), )

    
    title = property(__title.value, __title.set, None, '\n        A short, human-readable title.  May be repeated for different\n        languages.\n      ')

    
    # Element category uses Python identifier category
    __category = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'category'), 'category', '__AbsentNamespace0_CTD_ANON_50_category', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 128, 8), )

    
    category = property(__category.value, __category.set, None, '\n              IATI Document Category Code\n\n              For the value of the @code attribute, see\n              http://iatistandard.org/codelists/document_category\n            ')

    
    # Element language uses Python identifier language
    __language = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'language'), 'language', '__AbsentNamespace0_CTD_ANON_50_language', True, pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 138, 8), )

    
    language = property(__language.value, __language.set, None, '\n                The ISO 639 language code for the target document, e.g. "en".\n           ')

    
    # Attribute url uses Python identifier url
    __url = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'url'), 'url', '__AbsentNamespace0_CTD_ANON_50_url', pyxb.binding.datatypes.anyURI, required=True)
    __url._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 147, 6)
    __url._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 147, 6)
    
    url = property(__url.value, __url.set, None, '\n            The target URL of the external document, e.g. "http://www.example.org/doc.odt".\n          ')

    
    # Attribute format uses Python identifier format
    __format = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'format'), 'format', '__AbsentNamespace0_CTD_ANON_50_format', pyxb.binding.datatypes.string)
    __format._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 154, 6)
    __format._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 154, 6)
    
    format = property(__format.value, __format.set, None, '\n            The MIME type of the external document,\n            e.g. "application/pdf".  A list of MIME types\n            appears at http://iatistandard.org/codelists/file_format\n          ')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None))
    _HasWildcardElement = True
    _ElementMap.update({
        __title.name() : __title,
        __category.name() : __category,
        __language.name() : __language
    })
    _AttributeMap.update({
        __url.name() : __url,
        __format.name() : __format
    })



# Complex type plainType with content type MIXED
class plainType (pyxb.binding.basis.complexTypeDefinition):
    """
        Plain text content with no special attributes (e.g. xml:lang),
        though extended attributes are still allowed.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'plainType')
    _XSDLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 249, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'plainType', plainType)


# Complex type textType with content type MIXED
class textType (pyxb.binding.basis.complexTypeDefinition):
    """
        Data type for an element that may contain human-readable text
        in different languages.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'textType')
    _XSDLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 259, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__AbsentNamespace0_textType_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang)
    __lang._DeclarationLocation = None
    __lang._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 246, 4)
    
    lang = property(__lang.value, __lang.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None))
    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __lang.name() : __lang
    })
Namespace.addCategoryObject('typeBinding', 'textType', textType)


# Complex type codeType with content type MIXED
class codeType (pyxb.binding.basis.complexTypeDefinition):
    """
        Data type for an element that refers to an object that can
        have a code as well as human-readable text in different
        languages (e.g. a country or status).
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'codeType')
    _XSDLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 273, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__AbsentNamespace0_codeType_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang)
    __lang._DeclarationLocation = None
    __lang._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 246, 4)
    
    lang = property(__lang.value, __lang.set, None, None)

    
    # Attribute code uses Python identifier code
    __code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'code'), 'code', '__AbsentNamespace0_codeType_code', pyxb.binding.datatypes.string)
    __code._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 172, 2)
    __code._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 285, 4)
    
    code = property(__code.value, __code.set, None, '\n        Machine readable code for the entity being described. The value should\n        be available on a related codelist.\n      ')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None))
    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __lang.name() : __lang,
        __code.name() : __code
    })
Namespace.addCategoryObject('typeBinding', 'codeType', codeType)


# Complex type codeReqType with content type MIXED
class codeReqType (pyxb.binding.basis.complexTypeDefinition):
    """
        Data type for an element that refers to an object that must
        have a code.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'codeReqType')
    _XSDLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 289, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__AbsentNamespace0_codeReqType_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang)
    __lang._DeclarationLocation = None
    __lang._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 246, 4)
    
    lang = property(__lang.value, __lang.set, None, None)

    
    # Attribute code uses Python identifier code
    __code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'code'), 'code', '__AbsentNamespace0_codeReqType_code', pyxb.binding.datatypes.string, required=True)
    __code._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 172, 2)
    __code._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 300, 4)
    
    code = property(__code.value, __code.set, None, '\n        Machine readable code for the entity being described. The value should\n        be available on a related codelist.\n      ')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None))
    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __lang.name() : __lang,
        __code.name() : __code
    })
Namespace.addCategoryObject('typeBinding', 'codeReqType', codeReqType)


# Complex type refType with content type MIXED
class refType (pyxb.binding.basis.complexTypeDefinition):
    """
        Data type for an element that refers to a business object that
        can have unique identifier as well as human-readable text in
        different languages (e.g. an organisation).
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'refType')
    _XSDLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 304, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__AbsentNamespace0_refType_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang)
    __lang._DeclarationLocation = None
    __lang._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 246, 4)
    
    lang = property(__lang.value, __lang.set, None, None)

    
    # Attribute ref uses Python identifier ref
    __ref = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'ref'), 'ref', '__AbsentNamespace0_refType_ref', pyxb.binding.datatypes.string)
    __ref._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 181, 2)
    __ref._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 316, 4)
    
    ref = property(__ref.value, __ref.set, None, '\n        Machine-readable identification string for the business\n        object being described.\n      ')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None))
    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __lang.name() : __lang,
        __ref.name() : __ref
    })
Namespace.addCategoryObject('typeBinding', 'refType', refType)


# Complex type refReqType with content type MIXED
class refReqType (pyxb.binding.basis.complexTypeDefinition):
    """
        Data type for an element that refers to a business object that
        can have unique identifier as well as human-readable text in
        different languages (e.g. an organisation), where the identifier
        reference is required.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'refReqType')
    _XSDLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 320, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__AbsentNamespace0_refReqType_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang)
    __lang._DeclarationLocation = None
    __lang._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 246, 4)
    
    lang = property(__lang.value, __lang.set, None, None)

    
    # Attribute ref uses Python identifier ref
    __ref = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'ref'), 'ref', '__AbsentNamespace0_refReqType_ref', pyxb.binding.datatypes.string, required=True)
    __ref._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 181, 2)
    __ref._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 333, 4)
    
    ref = property(__ref.value, __ref.set, None, '\n        Machine-readable identification string for the business\n        object being described.\n      ')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None))
    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __lang.name() : __lang,
        __ref.name() : __ref
    })
Namespace.addCategoryObject('typeBinding', 'refReqType', refReqType)


# Complex type currencyType with content type SIMPLE
class currencyType (pyxb.binding.basis.complexTypeDefinition):
    """
        Data type for an element containing a currency value.
      """
    _TypeDefinition = pyxb.binding.datatypes.decimal
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'currencyType')
    _XSDLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 337, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.decimal
    
    # Attribute currency uses Python identifier currency
    __currency = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'currency'), 'currency', '__AbsentNamespace0_currencyType_currency', pyxb.binding.datatypes.string)
    __currency._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 211, 2)
    __currency._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 345, 8)
    
    currency = property(__currency.value, __currency.set, None, '\n        A three letter ISO 4217 code for the original currency of the \n        amount.\n        This is required for all currency amounts unless the\n        iati-activity/@default-currency (or iati-organisation/@default-currency\n        for an organisation file) attribute is specified.\n\n        Currency codes are listed at\n        http://iatistandard.org/codelists/currency\n      ')

    
    # Attribute value-date uses Python identifier value_date
    __value_date = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'value-date'), 'value_date', '__AbsentNamespace0_currencyType_value_date', pyxb.binding.datatypes.date, required=True)
    __value_date._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 226, 2)
    __value_date._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 346, 8)
    
    value_date = property(__value_date.value, __value_date.set, None, '\n        The date that this value was set (to allow historical\n        currency conversion).  The date must be in ISO 8601\n        format (YYYY-MM-DD).\n      ')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __currency.name() : __currency,
        __value_date.name() : __value_date
    })
Namespace.addCategoryObject('typeBinding', 'currencyType', currencyType)


# Complex type dateType with content type MIXED
class dateType (pyxb.binding.basis.complexTypeDefinition):
    """
        A date.  The ISO 8601 date goes into the @iso-date attribute.
        The content may be free-form text.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'dateType')
    _XSDLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 352, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute iso-date uses Python identifier iso_date
    __iso_date = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'iso-date'), 'iso_date', '__AbsentNamespace0_dateType_iso_date', pyxb.binding.datatypes.date)
    __iso_date._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 362, 4)
    __iso_date._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 362, 4)
    
    iso_date = property(__iso_date.value, __iso_date.set, None, '\n          The ISO 8601 date.\n        ')

    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __iso_date.name() : __iso_date
    })
Namespace.addCategoryObject('typeBinding', 'dateType', dateType)


# Complex type dateReqType with content type MIXED
class dateReqType (pyxb.binding.basis.complexTypeDefinition):
    """
        A date.  The ISO 8601 date goes into the @iso-date attribute.
        The content may be free-form text.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'dateReqType')
    _XSDLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 371, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute iso-date uses Python identifier iso_date
    __iso_date = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'iso-date'), 'iso_date', '__AbsentNamespace0_dateReqType_iso_date', pyxb.binding.datatypes.date, required=True)
    __iso_date._DeclarationLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 381, 4)
    __iso_date._UseLocation = pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 381, 4)
    
    iso_date = property(__iso_date.value, __iso_date.set, None, '\n          The ISO 8601 date.\n        ')

    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __iso_date.name() : __iso_date
    })
Namespace.addCategoryObject('typeBinding', 'dateReqType', dateReqType)


iati_activities = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'iati-activities'), CTD_ANON, documentation='\n        Top-level list of one or more IATI activity records.\n      ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 28, 2))
Namespace.addCategoryObject('elementBinding', iati_activities.name().localName(), iati_activities)

iati_activity = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'iati-activity'), CTD_ANON_, documentation='\n        Top-level element for a single IATI activity report.\n      ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 88, 2))
Namespace.addCategoryObject('elementBinding', iati_activity.name().localName(), iati_activity)

activity_website = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'activity-website'), CTD_ANON_2, documentation='\n        A direct link to a web site or web page providing more information\n        about the specific aid activity.  Multiple links can be included.\n        Multiple versions of the link may appear for different languages.  \n        Should not be general websites or addresses, and should include the \n        http or https prefix.\n      ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 186, 2))
Namespace.addCategoryObject('elementBinding', activity_website.name().localName(), activity_website)

participating_org = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'participating-org'), CTD_ANON_3, documentation='\n        An organisation (including the reporting organisation)\n        involved with the activity.  May be a donor, fund, agency,\n        etc.  Specifying the @ref and @role attributes is\n        strongly recommended.  May contain the organisation name as\n        content.\n\n        For the value of the @type attribute, see\n        http://iatistandard.org/codelists/organisation-type\n      ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 205, 2))
Namespace.addCategoryObject('elementBinding', participating_org.name().localName(), participating_org)

activity_scope = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'activity-scope'), codeType, documentation='\n        What geographical area does the activity encompass?\n        eg. Global, Regional, Multi-National, National, Multiple\n        (sub-national) administrative areas, etc\n      ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 239, 2))
Namespace.addCategoryObject('elementBinding', activity_scope.name().localName(), activity_scope)

recipient_country = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'recipient-country'), CTD_ANON_4, documentation='\n        A partner country that will benefit from this activity.  This\n        element is primarily for administrative and geopolitical\n        purposes.  If a specific country is not known, the activity\n        report can use the recipient-region element instead. For\n        geographical location, use the location element.\n\n        For the value of the @code attribute, see\n        http://iatistandard.org/codelists/country\n      ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 249, 2))
Namespace.addCategoryObject('elementBinding', recipient_country.name().localName(), recipient_country)

recipient_region = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'recipient-region'), CTD_ANON_5, documentation='\n        A geopolitical region (above the country level) that will\n        benefit from this activity.  This element is primarily for\n        administrative and geopolitical purposes.  If the specific\n        country/-ies are known, the activity report can use the\n        recipient-country element instead. For geographical location,\n        use the location element.\n\n        For the value of the @code attribute, see\n        http://iatistandard.org/codelists/region\n      ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 273, 2))
Namespace.addCategoryObject('elementBinding', recipient_region.name().localName(), recipient_region)

collaboration_type = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'collaboration-type'), codeReqType, documentation='\n        The type of collaboration involved in the project\'s\n        disbursements, e.g. "bilateral" or "multilateral".\n\n        For the value of the @code attribute, see\n        http://iatistandard.org/codelists/collaboration_type\n      ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 306, 2))
Namespace.addCategoryObject('elementBinding', collaboration_type.name().localName(), collaboration_type)

default_flow_type = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'default-flow-type'), codeReqType, documentation='\n        The type of assistance provided, e.g. Official Development\n        Assistance (ODA).  Type types will be defined by IATI.\n\n        For the value of the @code attribute, see\n        http://iatistandard.org/codelists/flow_type\n      ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 318, 2))
Namespace.addCategoryObject('elementBinding', default_flow_type.name().localName(), default_flow_type)

default_aid_type = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'default-aid-type'), codeReqType, documentation="\n        The type of aid being supplied (budget support, debt relief,\n        etc.).  This element specifies a default for all the\n        activity's financial transactions; it can be overridden at the\n        individual transaction level.\n\n        For the value of the @code attribute, see\n        http://iatistandard.org/codelists/aid_type\n      ", location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 330, 2))
Namespace.addCategoryObject('elementBinding', default_aid_type.name().localName(), default_aid_type)

default_finance_type = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'default-finance-type'), codeReqType, documentation='\n        The type of finance (e.g. debt relief). The types will be\n        defined by IATI.  This the default value for all transactions\n        in the activity report; it can be overridded by individual\n        transactions.\n\n        For the value of the @code attribute, see\n        http://iatistandard.org/codelists/finance_type\n      ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 344, 2))
Namespace.addCategoryObject('elementBinding', default_finance_type.name().localName(), default_finance_type)

other_identifier = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'other-identifier'), CTD_ANON_6, documentation="\n        An alternative, non-IATI identifier for the activity.  This\n        identifier is not guaranteed to be unique or persistent (it\n        depends on the owner organisation's policies, not IATI's).\n\n        If other-identifier is present then either @owner-ref or\n        @owner-name must be present\n      ", location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 358, 2))
Namespace.addCategoryObject('elementBinding', other_identifier.name().localName(), other_identifier)

sector = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sector'), CTD_ANON_7, documentation='\n        Sector code and name.  For the value of the @code attribute,\n        see http://iatistandard.org/codelists/sector\n\n        Either the @code attribute or descriptive text content must be\n        present.\n      ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 391, 2))
Namespace.addCategoryObject('elementBinding', sector.name().localName(), sector)

activity_date = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'activity-date'), CTD_ANON_8, documentation='\n        The planned and actual start and completion dates of the \n        activity. Start dates may reflect either the commencement of \n        funding, planning or physical activity. End dates should, \n        wherever possible, reflect the ending of physical activity. \n        Dates should be in ISO 8601 date YYYY-MM-DD format, e.g. \n        2010-10-01. \n        \n        For the value of the @type attribute, see\n        http://iatistandard.org/codelists/activity_date_type\n\n        The text content may contain a general date text (e.g. 2011Q1)\n        for recording less specific dates such as month, quarter, or\n        year.\n      ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 438, 2))
Namespace.addCategoryObject('elementBinding', activity_date.name().localName(), activity_date)

activity_status = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'activity-status'), codeType, documentation='\n        The current status of the project (e.g. "planned"), using a\n        list defined by IATI.  For the value of the @code attribute,\n        see http://iatistandard.org/codelists/activity_status\n      ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 475, 2))
Namespace.addCategoryObject('elementBinding', activity_status.name().localName(), activity_status)

contact_info = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'contact-info'), CTD_ANON_9, documentation='\n        Contact information for the activity.  Specify whatever is\n        available.  You may repeat this element for each contact\n        person.\n      ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 485, 2))
Namespace.addCategoryObject('elementBinding', contact_info.name().localName(), contact_info)

default_tied_status = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'default-tied-status'), codeReqType, documentation='\n        Specify whether the aid is untied, tied, or partially tied,\n        using a codelist created by IATI.  The content is free text\n        that can optionally provide more detail.  For the value of the\n        @code attribute, see\n        http://iatistandard.org/codelists/tied_status\n      ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 571, 2))
Namespace.addCategoryObject('elementBinding', default_tied_status.name().localName(), default_tied_status)

policy_marker = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'policy-marker'), CTD_ANON_12, documentation='\n        A policy or theme addressed by the activity.  A text\n        description of the theme appears in the content, and a formal\n        identifier appears in the @ref attribute.  The @vocabulary\n        attribute can also help to segment the markers into separate\n        vocabularies.  This element can be repeated for each policy\n        marker.  For the value of the @code attribute, see\n        http://iatistandard.org/codelists/policy_marker\n      ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 583, 2))
Namespace.addCategoryObject('elementBinding', policy_marker.name().localName(), policy_marker)

capital_spend = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'capital-spend'), CTD_ANON_13, documentation='\n        The percentage of the total commitment that is for capital\n        spending\n      ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 635, 2))
Namespace.addCategoryObject('elementBinding', capital_spend.name().localName(), capital_spend)

transaction = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'transaction'), CTD_ANON_14, documentation='\n        Committed or actual money flowing in or out of an aid\n        activity.The @ref attribute allows uniquely identifying a\n        transaction, to match it up with the corresponding in- or\n        outflow in a different activity.\n      ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 651, 2))
Namespace.addCategoryObject('elementBinding', transaction.name().localName(), transaction)

location = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'location'), CTD_ANON_18, documentation='\n        The sub-national geographical identification of the target \n        locations of an activity. These can be described by gazetteer \n        reference, coordinates, administrative areas or a textual \n        description.\n      ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 824, 2))
Namespace.addCategoryObject('elementBinding', location.name().localName(), location)

country_budget_items = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'country-budget-items'), CTD_ANON_27, documentation="\n        Recipient country budget items.\n\n        This item encodes the alignment of activities with both the\n        functional and administrative classifications used in the\n        recipient country's Chart of Accounts. This applies to both\n        on- and off-budget activities.\n      ", location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1203, 2))
Namespace.addCategoryObject('elementBinding', country_budget_items.name().localName(), country_budget_items)

related_activity = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'related-activity'), CTD_ANON_29, documentation="\n        Another IATI activity related to this one.  The 'type'\n        attribute describes the type of relationship (e.g. parent,\n        sibling).  This does not need to be used to express funding\n        relationships, since those are covered in individual\n        transactions.\n\n        For the value of the @type attribute, see\n        http://iatistandard.org/codelists/related_activity_type\n      ", location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1251, 2))
Namespace.addCategoryObject('elementBinding', related_activity.name().localName(), related_activity)

legacy_data = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'legacy-data'), CTD_ANON_30, documentation='\n        Hold a single name=value pair of legacy data.  This element is\n        *not* for adding new data types; instead, it holds the\n        original (non-IATI) value or code for an existing data type.\n      ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1274, 2))
Namespace.addCategoryObject('elementBinding', legacy_data.name().localName(), legacy_data)

result = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'result'), CTD_ANON_31, documentation='\n        A measurable result of aid work.\n      ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1310, 2))
Namespace.addCategoryObject('elementBinding', result.name().localName(), result)

conditions = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'conditions'), CTD_ANON_37, documentation='\n        Conditions attached to the activity.\n      ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1493, 2))
Namespace.addCategoryObject('elementBinding', conditions.name().localName(), conditions)

budget = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'budget'), CTD_ANON_39, documentation="\n        The value of the aid activity's budget for each financial year\n        as in the original project document.\n      ", location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1529, 2))
Namespace.addCategoryObject('elementBinding', budget.name().localName(), budget)

planned_disbursement = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'planned-disbursement'), CTD_ANON_40, documentation='\n        The planned disbursement element should only be used to report\n        specific planned cash transfers. These should be reported for\n        a specific date or a meaningfully predictable period. These\n        transactions should be reported in addition to budgets - which\n        are typically annual breakdowns of the total activity\n        commitment.\n      ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1571, 2))
Namespace.addCategoryObject('elementBinding', planned_disbursement.name().localName(), planned_disbursement)

crs_add = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'crs-add'), CTD_ANON_41, documentation='\n        Additional items specific to CRS++ reporting.\n      ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1624, 2))
Namespace.addCategoryObject('elementBinding', crs_add.name().localName(), crs_add)

fss = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'fss'), CTD_ANON_45, documentation='\n        This section allows entry of data required for the OECD\n        DAC Forward Spending Survey at an activity level.\n      ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1795, 2))
Namespace.addCategoryObject('elementBinding', fss.name().localName(), fss)

title = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'title'), textType, documentation='\n        A short, human-readable title.  May be repeated for different\n        languages.\n      ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 27, 2))
Namespace.addCategoryObject('elementBinding', title.name().localName(), title)

description = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'description'), CTD_ANON_47, documentation='\n        A longer, human-readable description.  May be repeated for\n        different languages.\n      ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 36, 2))
Namespace.addCategoryObject('elementBinding', description.name().localName(), description)

comment = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'comment'), textType, documentation='\n        A human-readable comment associated with a piece of aid information.\n      ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 53, 2))
Namespace.addCategoryObject('elementBinding', comment.name().localName(), comment)

iati_identifier = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'iati-identifier'), CTD_ANON_48, documentation="\n        The iati-identifier element is used in both Activity files and\n        Organisation files, and has a slightly different meaning depending on\n        where it is being used, and should not be confused.\n\n        When used in an organisation it is a globally unique identifier for\n        that organisation.\n\n        When used in an activity it is a globally unique identifier for that\n        activity.  This should be in the form of the IATI Organisation\n        Identifier (for the reporting organisation) concatenated to that\n        organisation's activity identifier. (NB. Two or more reporting\n        organisations may publish information on the same activity.)\n      ", location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 61, 2))
Namespace.addCategoryObject('elementBinding', iati_identifier.name().localName(), iati_identifier)

reporting_org = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'reporting-org'), CTD_ANON_49, documentation='\n        The organisation issuing the report.\n        May be a primary source (reporting on its own activity as\n        donor, implementing agency, etc) or a secondary source\n        (reporting on the activities of another organisation). \n        \n        Specifying the @ref attribute is mandatory.\n        May contain the organisation name as content.\n        \n        All activities in an activity xml file must contain the same\n        @ref AND this @ref must be the same as the iati-identifier\n        recorded in the registry publisher record of the account under\n        which this file is published.\n      ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 83, 2))
Namespace.addCategoryObject('elementBinding', reporting_org.name().localName(), reporting_org)

document_link = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'document-link'), CTD_ANON_50, documentation='\n        A categorized link to an external document.\n      ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 119, 2))
Namespace.addCategoryObject('elementBinding', document_link.name().localName(), document_link)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'iati-activity'), CTD_ANON_, scope=CTD_ANON, documentation='\n        Top-level element for a single IATI activity report.\n      ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 88, 2)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 35, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'iati-activity')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 36, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None)), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 37, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'activity-website'), CTD_ANON_2, scope=CTD_ANON_, documentation='\n        A direct link to a web site or web page providing more information\n        about the specific aid activity.  Multiple links can be included.\n        Multiple versions of the link may appear for different languages.  \n        Should not be general websites or addresses, and should include the \n        http or https prefix.\n      ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 186, 2)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'participating-org'), CTD_ANON_3, scope=CTD_ANON_, documentation='\n        An organisation (including the reporting organisation)\n        involved with the activity.  May be a donor, fund, agency,\n        etc.  Specifying the @ref and @role attributes is\n        strongly recommended.  May contain the organisation name as\n        content.\n\n        For the value of the @type attribute, see\n        http://iatistandard.org/codelists/organisation-type\n      ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 205, 2)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'activity-scope'), codeType, scope=CTD_ANON_, documentation='\n        What geographical area does the activity encompass?\n        eg. Global, Regional, Multi-National, National, Multiple\n        (sub-national) administrative areas, etc\n      ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 239, 2)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'recipient-country'), CTD_ANON_4, scope=CTD_ANON_, documentation='\n        A partner country that will benefit from this activity.  This\n        element is primarily for administrative and geopolitical\n        purposes.  If a specific country is not known, the activity\n        report can use the recipient-region element instead. For\n        geographical location, use the location element.\n\n        For the value of the @code attribute, see\n        http://iatistandard.org/codelists/country\n      ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 249, 2)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'recipient-region'), CTD_ANON_5, scope=CTD_ANON_, documentation='\n        A geopolitical region (above the country level) that will\n        benefit from this activity.  This element is primarily for\n        administrative and geopolitical purposes.  If the specific\n        country/-ies are known, the activity report can use the\n        recipient-country element instead. For geographical location,\n        use the location element.\n\n        For the value of the @code attribute, see\n        http://iatistandard.org/codelists/region\n      ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 273, 2)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'collaboration-type'), codeReqType, scope=CTD_ANON_, documentation='\n        The type of collaboration involved in the project\'s\n        disbursements, e.g. "bilateral" or "multilateral".\n\n        For the value of the @code attribute, see\n        http://iatistandard.org/codelists/collaboration_type\n      ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 306, 2)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'default-flow-type'), codeReqType, scope=CTD_ANON_, documentation='\n        The type of assistance provided, e.g. Official Development\n        Assistance (ODA).  Type types will be defined by IATI.\n\n        For the value of the @code attribute, see\n        http://iatistandard.org/codelists/flow_type\n      ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 318, 2)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'default-aid-type'), codeReqType, scope=CTD_ANON_, documentation="\n        The type of aid being supplied (budget support, debt relief,\n        etc.).  This element specifies a default for all the\n        activity's financial transactions; it can be overridden at the\n        individual transaction level.\n\n        For the value of the @code attribute, see\n        http://iatistandard.org/codelists/aid_type\n      ", location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 330, 2)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'default-finance-type'), codeReqType, scope=CTD_ANON_, documentation='\n        The type of finance (e.g. debt relief). The types will be\n        defined by IATI.  This the default value for all transactions\n        in the activity report; it can be overridded by individual\n        transactions.\n\n        For the value of the @code attribute, see\n        http://iatistandard.org/codelists/finance_type\n      ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 344, 2)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'other-identifier'), CTD_ANON_6, scope=CTD_ANON_, documentation="\n        An alternative, non-IATI identifier for the activity.  This\n        identifier is not guaranteed to be unique or persistent (it\n        depends on the owner organisation's policies, not IATI's).\n\n        If other-identifier is present then either @owner-ref or\n        @owner-name must be present\n      ", location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 358, 2)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sector'), CTD_ANON_7, scope=CTD_ANON_, documentation='\n        Sector code and name.  For the value of the @code attribute,\n        see http://iatistandard.org/codelists/sector\n\n        Either the @code attribute or descriptive text content must be\n        present.\n      ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 391, 2)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'activity-date'), CTD_ANON_8, scope=CTD_ANON_, documentation='\n        The planned and actual start and completion dates of the \n        activity. Start dates may reflect either the commencement of \n        funding, planning or physical activity. End dates should, \n        wherever possible, reflect the ending of physical activity. \n        Dates should be in ISO 8601 date YYYY-MM-DD format, e.g. \n        2010-10-01. \n        \n        For the value of the @type attribute, see\n        http://iatistandard.org/codelists/activity_date_type\n\n        The text content may contain a general date text (e.g. 2011Q1)\n        for recording less specific dates such as month, quarter, or\n        year.\n      ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 438, 2)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'activity-status'), codeType, scope=CTD_ANON_, documentation='\n        The current status of the project (e.g. "planned"), using a\n        list defined by IATI.  For the value of the @code attribute,\n        see http://iatistandard.org/codelists/activity_status\n      ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 475, 2)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'contact-info'), CTD_ANON_9, scope=CTD_ANON_, documentation='\n        Contact information for the activity.  Specify whatever is\n        available.  You may repeat this element for each contact\n        person.\n      ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 485, 2)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'default-tied-status'), codeReqType, scope=CTD_ANON_, documentation='\n        Specify whether the aid is untied, tied, or partially tied,\n        using a codelist created by IATI.  The content is free text\n        that can optionally provide more detail.  For the value of the\n        @code attribute, see\n        http://iatistandard.org/codelists/tied_status\n      ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 571, 2)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'policy-marker'), CTD_ANON_12, scope=CTD_ANON_, documentation='\n        A policy or theme addressed by the activity.  A text\n        description of the theme appears in the content, and a formal\n        identifier appears in the @ref attribute.  The @vocabulary\n        attribute can also help to segment the markers into separate\n        vocabularies.  This element can be repeated for each policy\n        marker.  For the value of the @code attribute, see\n        http://iatistandard.org/codelists/policy_marker\n      ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 583, 2)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'capital-spend'), CTD_ANON_13, scope=CTD_ANON_, documentation='\n        The percentage of the total commitment that is for capital\n        spending\n      ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 635, 2)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'transaction'), CTD_ANON_14, scope=CTD_ANON_, documentation='\n        Committed or actual money flowing in or out of an aid\n        activity.The @ref attribute allows uniquely identifying a\n        transaction, to match it up with the corresponding in- or\n        outflow in a different activity.\n      ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 651, 2)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'location'), CTD_ANON_18, scope=CTD_ANON_, documentation='\n        The sub-national geographical identification of the target \n        locations of an activity. These can be described by gazetteer \n        reference, coordinates, administrative areas or a textual \n        description.\n      ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 824, 2)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'country-budget-items'), CTD_ANON_27, scope=CTD_ANON_, documentation="\n        Recipient country budget items.\n\n        This item encodes the alignment of activities with both the\n        functional and administrative classifications used in the\n        recipient country's Chart of Accounts. This applies to both\n        on- and off-budget activities.\n      ", location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1203, 2)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'related-activity'), CTD_ANON_29, scope=CTD_ANON_, documentation="\n        Another IATI activity related to this one.  The 'type'\n        attribute describes the type of relationship (e.g. parent,\n        sibling).  This does not need to be used to express funding\n        relationships, since those are covered in individual\n        transactions.\n\n        For the value of the @type attribute, see\n        http://iatistandard.org/codelists/related_activity_type\n      ", location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1251, 2)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'legacy-data'), CTD_ANON_30, scope=CTD_ANON_, documentation='\n        Hold a single name=value pair of legacy data.  This element is\n        *not* for adding new data types; instead, it holds the\n        original (non-IATI) value or code for an existing data type.\n      ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1274, 2)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'result'), CTD_ANON_31, scope=CTD_ANON_, documentation='\n        A measurable result of aid work.\n      ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1310, 2)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'conditions'), CTD_ANON_37, scope=CTD_ANON_, documentation='\n        Conditions attached to the activity.\n      ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1493, 2)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'budget'), CTD_ANON_39, scope=CTD_ANON_, documentation="\n        The value of the aid activity's budget for each financial year\n        as in the original project document.\n      ", location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1529, 2)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'planned-disbursement'), CTD_ANON_40, scope=CTD_ANON_, documentation='\n        The planned disbursement element should only be used to report\n        specific planned cash transfers. These should be reported for\n        a specific date or a meaningfully predictable period. These\n        transactions should be reported in addition to budgets - which\n        are typically annual breakdowns of the total activity\n        commitment.\n      ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1571, 2)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'crs-add'), CTD_ANON_41, scope=CTD_ANON_, documentation='\n        Additional items specific to CRS++ reporting.\n      ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1624, 2)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'fss'), CTD_ANON_45, scope=CTD_ANON_, documentation='\n        This section allows entry of data required for the OECD\n        DAC Forward Spending Survey at an activity level.\n      ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1795, 2)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'title'), textType, scope=CTD_ANON_, documentation='\n        A short, human-readable title.  May be repeated for different\n        languages.\n      ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 27, 2)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'description'), CTD_ANON_47, scope=CTD_ANON_, documentation='\n        A longer, human-readable description.  May be repeated for\n        different languages.\n      ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 36, 2)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'iati-identifier'), CTD_ANON_48, scope=CTD_ANON_, documentation="\n        The iati-identifier element is used in both Activity files and\n        Organisation files, and has a slightly different meaning depending on\n        where it is being used, and should not be confused.\n\n        When used in an organisation it is a globally unique identifier for\n        that organisation.\n\n        When used in an activity it is a globally unique identifier for that\n        activity.  This should be in the form of the IATI Organisation\n        Identifier (for the reporting organisation) concatenated to that\n        organisation's activity identifier. (NB. Two or more reporting\n        organisations may publish information on the same activity.)\n      ", location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 61, 2)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'reporting-org'), CTD_ANON_49, scope=CTD_ANON_, documentation='\n        The organisation issuing the report.\n        May be a primary source (reporting on its own activity as\n        donor, implementing agency, etc) or a secondary source\n        (reporting on the activities of another organisation). \n        \n        Specifying the @ref attribute is mandatory.\n        May contain the organisation name as content.\n        \n        All activities in an activity xml file must contain the same\n        @ref AND this @ref must be the same as the iati-identifier\n        recorded in the registry publisher record of the account under\n        which this file is published.\n      ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 83, 2)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'document-link'), CTD_ANON_50, scope=CTD_ANON_, documentation='\n        A categorized link to an external document.\n      ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 119, 2)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'reporting-org')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 96, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'iati-identifier')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 97, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'other-identifier')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 98, 8))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'title')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 99, 8))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'description')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 100, 8))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'activity-status')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 101, 8))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'activity-date')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 102, 8))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'contact-info')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 103, 8))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'participating-org')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 104, 8))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'activity-scope')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 105, 8))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'recipient-country')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 106, 8))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'recipient-region')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 107, 8))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'location')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 108, 8))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'sector')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 109, 8))
    st_13 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'country-budget-items')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 110, 8))
    st_14 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'policy-marker')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 111, 8))
    st_15 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'collaboration-type')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 112, 8))
    st_16 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'default-flow-type')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 113, 8))
    st_17 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'default-finance-type')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 114, 8))
    st_18 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'default-aid-type')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 115, 8))
    st_19 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_19)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'default-tied-status')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 116, 8))
    st_20 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_20)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'budget')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 117, 8))
    st_21 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_21)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'planned-disbursement')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 118, 8))
    st_22 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_22)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'capital-spend')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 119, 8))
    st_23 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_23)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'transaction')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 120, 8))
    st_24 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_24)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'document-link')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 121, 8))
    st_25 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_25)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'activity-website')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 122, 8))
    st_26 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_26)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'related-activity')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 123, 8))
    st_27 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_27)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'conditions')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 124, 8))
    st_28 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_28)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'result')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 125, 8))
    st_29 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_29)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'legacy-data')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 126, 8))
    st_30 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_30)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'crs-add')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 127, 8))
    st_31 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_31)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'fss')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 128, 8))
    st_32 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_32)
    final_update = set()
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None)), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 129, 8))
    st_33 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_33)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    transitions.append(fac.Transition(st_20, [
         ]))
    transitions.append(fac.Transition(st_21, [
         ]))
    transitions.append(fac.Transition(st_22, [
         ]))
    transitions.append(fac.Transition(st_23, [
         ]))
    transitions.append(fac.Transition(st_24, [
         ]))
    transitions.append(fac.Transition(st_25, [
         ]))
    transitions.append(fac.Transition(st_26, [
         ]))
    transitions.append(fac.Transition(st_27, [
         ]))
    transitions.append(fac.Transition(st_28, [
         ]))
    transitions.append(fac.Transition(st_29, [
         ]))
    transitions.append(fac.Transition(st_30, [
         ]))
    transitions.append(fac.Transition(st_31, [
         ]))
    transitions.append(fac.Transition(st_32, [
         ]))
    transitions.append(fac.Transition(st_33, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    transitions.append(fac.Transition(st_20, [
         ]))
    transitions.append(fac.Transition(st_21, [
         ]))
    transitions.append(fac.Transition(st_22, [
         ]))
    transitions.append(fac.Transition(st_23, [
         ]))
    transitions.append(fac.Transition(st_24, [
         ]))
    transitions.append(fac.Transition(st_25, [
         ]))
    transitions.append(fac.Transition(st_26, [
         ]))
    transitions.append(fac.Transition(st_27, [
         ]))
    transitions.append(fac.Transition(st_28, [
         ]))
    transitions.append(fac.Transition(st_29, [
         ]))
    transitions.append(fac.Transition(st_30, [
         ]))
    transitions.append(fac.Transition(st_31, [
         ]))
    transitions.append(fac.Transition(st_32, [
         ]))
    transitions.append(fac.Transition(st_33, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    transitions.append(fac.Transition(st_20, [
         ]))
    transitions.append(fac.Transition(st_21, [
         ]))
    transitions.append(fac.Transition(st_22, [
         ]))
    transitions.append(fac.Transition(st_23, [
         ]))
    transitions.append(fac.Transition(st_24, [
         ]))
    transitions.append(fac.Transition(st_25, [
         ]))
    transitions.append(fac.Transition(st_26, [
         ]))
    transitions.append(fac.Transition(st_27, [
         ]))
    transitions.append(fac.Transition(st_28, [
         ]))
    transitions.append(fac.Transition(st_29, [
         ]))
    transitions.append(fac.Transition(st_30, [
         ]))
    transitions.append(fac.Transition(st_31, [
         ]))
    transitions.append(fac.Transition(st_32, [
         ]))
    transitions.append(fac.Transition(st_33, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    transitions.append(fac.Transition(st_20, [
         ]))
    transitions.append(fac.Transition(st_21, [
         ]))
    transitions.append(fac.Transition(st_22, [
         ]))
    transitions.append(fac.Transition(st_23, [
         ]))
    transitions.append(fac.Transition(st_24, [
         ]))
    transitions.append(fac.Transition(st_25, [
         ]))
    transitions.append(fac.Transition(st_26, [
         ]))
    transitions.append(fac.Transition(st_27, [
         ]))
    transitions.append(fac.Transition(st_28, [
         ]))
    transitions.append(fac.Transition(st_29, [
         ]))
    transitions.append(fac.Transition(st_30, [
         ]))
    transitions.append(fac.Transition(st_31, [
         ]))
    transitions.append(fac.Transition(st_32, [
         ]))
    transitions.append(fac.Transition(st_33, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    transitions.append(fac.Transition(st_20, [
         ]))
    transitions.append(fac.Transition(st_21, [
         ]))
    transitions.append(fac.Transition(st_22, [
         ]))
    transitions.append(fac.Transition(st_23, [
         ]))
    transitions.append(fac.Transition(st_24, [
         ]))
    transitions.append(fac.Transition(st_25, [
         ]))
    transitions.append(fac.Transition(st_26, [
         ]))
    transitions.append(fac.Transition(st_27, [
         ]))
    transitions.append(fac.Transition(st_28, [
         ]))
    transitions.append(fac.Transition(st_29, [
         ]))
    transitions.append(fac.Transition(st_30, [
         ]))
    transitions.append(fac.Transition(st_31, [
         ]))
    transitions.append(fac.Transition(st_32, [
         ]))
    transitions.append(fac.Transition(st_33, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    transitions.append(fac.Transition(st_20, [
         ]))
    transitions.append(fac.Transition(st_21, [
         ]))
    transitions.append(fac.Transition(st_22, [
         ]))
    transitions.append(fac.Transition(st_23, [
         ]))
    transitions.append(fac.Transition(st_24, [
         ]))
    transitions.append(fac.Transition(st_25, [
         ]))
    transitions.append(fac.Transition(st_26, [
         ]))
    transitions.append(fac.Transition(st_27, [
         ]))
    transitions.append(fac.Transition(st_28, [
         ]))
    transitions.append(fac.Transition(st_29, [
         ]))
    transitions.append(fac.Transition(st_30, [
         ]))
    transitions.append(fac.Transition(st_31, [
         ]))
    transitions.append(fac.Transition(st_32, [
         ]))
    transitions.append(fac.Transition(st_33, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    transitions.append(fac.Transition(st_20, [
         ]))
    transitions.append(fac.Transition(st_21, [
         ]))
    transitions.append(fac.Transition(st_22, [
         ]))
    transitions.append(fac.Transition(st_23, [
         ]))
    transitions.append(fac.Transition(st_24, [
         ]))
    transitions.append(fac.Transition(st_25, [
         ]))
    transitions.append(fac.Transition(st_26, [
         ]))
    transitions.append(fac.Transition(st_27, [
         ]))
    transitions.append(fac.Transition(st_28, [
         ]))
    transitions.append(fac.Transition(st_29, [
         ]))
    transitions.append(fac.Transition(st_30, [
         ]))
    transitions.append(fac.Transition(st_31, [
         ]))
    transitions.append(fac.Transition(st_32, [
         ]))
    transitions.append(fac.Transition(st_33, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    transitions.append(fac.Transition(st_20, [
         ]))
    transitions.append(fac.Transition(st_21, [
         ]))
    transitions.append(fac.Transition(st_22, [
         ]))
    transitions.append(fac.Transition(st_23, [
         ]))
    transitions.append(fac.Transition(st_24, [
         ]))
    transitions.append(fac.Transition(st_25, [
         ]))
    transitions.append(fac.Transition(st_26, [
         ]))
    transitions.append(fac.Transition(st_27, [
         ]))
    transitions.append(fac.Transition(st_28, [
         ]))
    transitions.append(fac.Transition(st_29, [
         ]))
    transitions.append(fac.Transition(st_30, [
         ]))
    transitions.append(fac.Transition(st_31, [
         ]))
    transitions.append(fac.Transition(st_32, [
         ]))
    transitions.append(fac.Transition(st_33, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    transitions.append(fac.Transition(st_20, [
         ]))
    transitions.append(fac.Transition(st_21, [
         ]))
    transitions.append(fac.Transition(st_22, [
         ]))
    transitions.append(fac.Transition(st_23, [
         ]))
    transitions.append(fac.Transition(st_24, [
         ]))
    transitions.append(fac.Transition(st_25, [
         ]))
    transitions.append(fac.Transition(st_26, [
         ]))
    transitions.append(fac.Transition(st_27, [
         ]))
    transitions.append(fac.Transition(st_28, [
         ]))
    transitions.append(fac.Transition(st_29, [
         ]))
    transitions.append(fac.Transition(st_30, [
         ]))
    transitions.append(fac.Transition(st_31, [
         ]))
    transitions.append(fac.Transition(st_32, [
         ]))
    transitions.append(fac.Transition(st_33, [
         ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    transitions.append(fac.Transition(st_20, [
         ]))
    transitions.append(fac.Transition(st_21, [
         ]))
    transitions.append(fac.Transition(st_22, [
         ]))
    transitions.append(fac.Transition(st_23, [
         ]))
    transitions.append(fac.Transition(st_24, [
         ]))
    transitions.append(fac.Transition(st_25, [
         ]))
    transitions.append(fac.Transition(st_26, [
         ]))
    transitions.append(fac.Transition(st_27, [
         ]))
    transitions.append(fac.Transition(st_28, [
         ]))
    transitions.append(fac.Transition(st_29, [
         ]))
    transitions.append(fac.Transition(st_30, [
         ]))
    transitions.append(fac.Transition(st_31, [
         ]))
    transitions.append(fac.Transition(st_32, [
         ]))
    transitions.append(fac.Transition(st_33, [
         ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    transitions.append(fac.Transition(st_20, [
         ]))
    transitions.append(fac.Transition(st_21, [
         ]))
    transitions.append(fac.Transition(st_22, [
         ]))
    transitions.append(fac.Transition(st_23, [
         ]))
    transitions.append(fac.Transition(st_24, [
         ]))
    transitions.append(fac.Transition(st_25, [
         ]))
    transitions.append(fac.Transition(st_26, [
         ]))
    transitions.append(fac.Transition(st_27, [
         ]))
    transitions.append(fac.Transition(st_28, [
         ]))
    transitions.append(fac.Transition(st_29, [
         ]))
    transitions.append(fac.Transition(st_30, [
         ]))
    transitions.append(fac.Transition(st_31, [
         ]))
    transitions.append(fac.Transition(st_32, [
         ]))
    transitions.append(fac.Transition(st_33, [
         ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    transitions.append(fac.Transition(st_20, [
         ]))
    transitions.append(fac.Transition(st_21, [
         ]))
    transitions.append(fac.Transition(st_22, [
         ]))
    transitions.append(fac.Transition(st_23, [
         ]))
    transitions.append(fac.Transition(st_24, [
         ]))
    transitions.append(fac.Transition(st_25, [
         ]))
    transitions.append(fac.Transition(st_26, [
         ]))
    transitions.append(fac.Transition(st_27, [
         ]))
    transitions.append(fac.Transition(st_28, [
         ]))
    transitions.append(fac.Transition(st_29, [
         ]))
    transitions.append(fac.Transition(st_30, [
         ]))
    transitions.append(fac.Transition(st_31, [
         ]))
    transitions.append(fac.Transition(st_32, [
         ]))
    transitions.append(fac.Transition(st_33, [
         ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    transitions.append(fac.Transition(st_20, [
         ]))
    transitions.append(fac.Transition(st_21, [
         ]))
    transitions.append(fac.Transition(st_22, [
         ]))
    transitions.append(fac.Transition(st_23, [
         ]))
    transitions.append(fac.Transition(st_24, [
         ]))
    transitions.append(fac.Transition(st_25, [
         ]))
    transitions.append(fac.Transition(st_26, [
         ]))
    transitions.append(fac.Transition(st_27, [
         ]))
    transitions.append(fac.Transition(st_28, [
         ]))
    transitions.append(fac.Transition(st_29, [
         ]))
    transitions.append(fac.Transition(st_30, [
         ]))
    transitions.append(fac.Transition(st_31, [
         ]))
    transitions.append(fac.Transition(st_32, [
         ]))
    transitions.append(fac.Transition(st_33, [
         ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    transitions.append(fac.Transition(st_20, [
         ]))
    transitions.append(fac.Transition(st_21, [
         ]))
    transitions.append(fac.Transition(st_22, [
         ]))
    transitions.append(fac.Transition(st_23, [
         ]))
    transitions.append(fac.Transition(st_24, [
         ]))
    transitions.append(fac.Transition(st_25, [
         ]))
    transitions.append(fac.Transition(st_26, [
         ]))
    transitions.append(fac.Transition(st_27, [
         ]))
    transitions.append(fac.Transition(st_28, [
         ]))
    transitions.append(fac.Transition(st_29, [
         ]))
    transitions.append(fac.Transition(st_30, [
         ]))
    transitions.append(fac.Transition(st_31, [
         ]))
    transitions.append(fac.Transition(st_32, [
         ]))
    transitions.append(fac.Transition(st_33, [
         ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    transitions.append(fac.Transition(st_20, [
         ]))
    transitions.append(fac.Transition(st_21, [
         ]))
    transitions.append(fac.Transition(st_22, [
         ]))
    transitions.append(fac.Transition(st_23, [
         ]))
    transitions.append(fac.Transition(st_24, [
         ]))
    transitions.append(fac.Transition(st_25, [
         ]))
    transitions.append(fac.Transition(st_26, [
         ]))
    transitions.append(fac.Transition(st_27, [
         ]))
    transitions.append(fac.Transition(st_28, [
         ]))
    transitions.append(fac.Transition(st_29, [
         ]))
    transitions.append(fac.Transition(st_30, [
         ]))
    transitions.append(fac.Transition(st_31, [
         ]))
    transitions.append(fac.Transition(st_32, [
         ]))
    transitions.append(fac.Transition(st_33, [
         ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    transitions.append(fac.Transition(st_20, [
         ]))
    transitions.append(fac.Transition(st_21, [
         ]))
    transitions.append(fac.Transition(st_22, [
         ]))
    transitions.append(fac.Transition(st_23, [
         ]))
    transitions.append(fac.Transition(st_24, [
         ]))
    transitions.append(fac.Transition(st_25, [
         ]))
    transitions.append(fac.Transition(st_26, [
         ]))
    transitions.append(fac.Transition(st_27, [
         ]))
    transitions.append(fac.Transition(st_28, [
         ]))
    transitions.append(fac.Transition(st_29, [
         ]))
    transitions.append(fac.Transition(st_30, [
         ]))
    transitions.append(fac.Transition(st_31, [
         ]))
    transitions.append(fac.Transition(st_32, [
         ]))
    transitions.append(fac.Transition(st_33, [
         ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    transitions.append(fac.Transition(st_20, [
         ]))
    transitions.append(fac.Transition(st_21, [
         ]))
    transitions.append(fac.Transition(st_22, [
         ]))
    transitions.append(fac.Transition(st_23, [
         ]))
    transitions.append(fac.Transition(st_24, [
         ]))
    transitions.append(fac.Transition(st_25, [
         ]))
    transitions.append(fac.Transition(st_26, [
         ]))
    transitions.append(fac.Transition(st_27, [
         ]))
    transitions.append(fac.Transition(st_28, [
         ]))
    transitions.append(fac.Transition(st_29, [
         ]))
    transitions.append(fac.Transition(st_30, [
         ]))
    transitions.append(fac.Transition(st_31, [
         ]))
    transitions.append(fac.Transition(st_32, [
         ]))
    transitions.append(fac.Transition(st_33, [
         ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    transitions.append(fac.Transition(st_20, [
         ]))
    transitions.append(fac.Transition(st_21, [
         ]))
    transitions.append(fac.Transition(st_22, [
         ]))
    transitions.append(fac.Transition(st_23, [
         ]))
    transitions.append(fac.Transition(st_24, [
         ]))
    transitions.append(fac.Transition(st_25, [
         ]))
    transitions.append(fac.Transition(st_26, [
         ]))
    transitions.append(fac.Transition(st_27, [
         ]))
    transitions.append(fac.Transition(st_28, [
         ]))
    transitions.append(fac.Transition(st_29, [
         ]))
    transitions.append(fac.Transition(st_30, [
         ]))
    transitions.append(fac.Transition(st_31, [
         ]))
    transitions.append(fac.Transition(st_32, [
         ]))
    transitions.append(fac.Transition(st_33, [
         ]))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    transitions.append(fac.Transition(st_20, [
         ]))
    transitions.append(fac.Transition(st_21, [
         ]))
    transitions.append(fac.Transition(st_22, [
         ]))
    transitions.append(fac.Transition(st_23, [
         ]))
    transitions.append(fac.Transition(st_24, [
         ]))
    transitions.append(fac.Transition(st_25, [
         ]))
    transitions.append(fac.Transition(st_26, [
         ]))
    transitions.append(fac.Transition(st_27, [
         ]))
    transitions.append(fac.Transition(st_28, [
         ]))
    transitions.append(fac.Transition(st_29, [
         ]))
    transitions.append(fac.Transition(st_30, [
         ]))
    transitions.append(fac.Transition(st_31, [
         ]))
    transitions.append(fac.Transition(st_32, [
         ]))
    transitions.append(fac.Transition(st_33, [
         ]))
    st_18._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    transitions.append(fac.Transition(st_20, [
         ]))
    transitions.append(fac.Transition(st_21, [
         ]))
    transitions.append(fac.Transition(st_22, [
         ]))
    transitions.append(fac.Transition(st_23, [
         ]))
    transitions.append(fac.Transition(st_24, [
         ]))
    transitions.append(fac.Transition(st_25, [
         ]))
    transitions.append(fac.Transition(st_26, [
         ]))
    transitions.append(fac.Transition(st_27, [
         ]))
    transitions.append(fac.Transition(st_28, [
         ]))
    transitions.append(fac.Transition(st_29, [
         ]))
    transitions.append(fac.Transition(st_30, [
         ]))
    transitions.append(fac.Transition(st_31, [
         ]))
    transitions.append(fac.Transition(st_32, [
         ]))
    transitions.append(fac.Transition(st_33, [
         ]))
    st_19._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    transitions.append(fac.Transition(st_20, [
         ]))
    transitions.append(fac.Transition(st_21, [
         ]))
    transitions.append(fac.Transition(st_22, [
         ]))
    transitions.append(fac.Transition(st_23, [
         ]))
    transitions.append(fac.Transition(st_24, [
         ]))
    transitions.append(fac.Transition(st_25, [
         ]))
    transitions.append(fac.Transition(st_26, [
         ]))
    transitions.append(fac.Transition(st_27, [
         ]))
    transitions.append(fac.Transition(st_28, [
         ]))
    transitions.append(fac.Transition(st_29, [
         ]))
    transitions.append(fac.Transition(st_30, [
         ]))
    transitions.append(fac.Transition(st_31, [
         ]))
    transitions.append(fac.Transition(st_32, [
         ]))
    transitions.append(fac.Transition(st_33, [
         ]))
    st_20._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    transitions.append(fac.Transition(st_20, [
         ]))
    transitions.append(fac.Transition(st_21, [
         ]))
    transitions.append(fac.Transition(st_22, [
         ]))
    transitions.append(fac.Transition(st_23, [
         ]))
    transitions.append(fac.Transition(st_24, [
         ]))
    transitions.append(fac.Transition(st_25, [
         ]))
    transitions.append(fac.Transition(st_26, [
         ]))
    transitions.append(fac.Transition(st_27, [
         ]))
    transitions.append(fac.Transition(st_28, [
         ]))
    transitions.append(fac.Transition(st_29, [
         ]))
    transitions.append(fac.Transition(st_30, [
         ]))
    transitions.append(fac.Transition(st_31, [
         ]))
    transitions.append(fac.Transition(st_32, [
         ]))
    transitions.append(fac.Transition(st_33, [
         ]))
    st_21._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    transitions.append(fac.Transition(st_20, [
         ]))
    transitions.append(fac.Transition(st_21, [
         ]))
    transitions.append(fac.Transition(st_22, [
         ]))
    transitions.append(fac.Transition(st_23, [
         ]))
    transitions.append(fac.Transition(st_24, [
         ]))
    transitions.append(fac.Transition(st_25, [
         ]))
    transitions.append(fac.Transition(st_26, [
         ]))
    transitions.append(fac.Transition(st_27, [
         ]))
    transitions.append(fac.Transition(st_28, [
         ]))
    transitions.append(fac.Transition(st_29, [
         ]))
    transitions.append(fac.Transition(st_30, [
         ]))
    transitions.append(fac.Transition(st_31, [
         ]))
    transitions.append(fac.Transition(st_32, [
         ]))
    transitions.append(fac.Transition(st_33, [
         ]))
    st_22._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    transitions.append(fac.Transition(st_20, [
         ]))
    transitions.append(fac.Transition(st_21, [
         ]))
    transitions.append(fac.Transition(st_22, [
         ]))
    transitions.append(fac.Transition(st_23, [
         ]))
    transitions.append(fac.Transition(st_24, [
         ]))
    transitions.append(fac.Transition(st_25, [
         ]))
    transitions.append(fac.Transition(st_26, [
         ]))
    transitions.append(fac.Transition(st_27, [
         ]))
    transitions.append(fac.Transition(st_28, [
         ]))
    transitions.append(fac.Transition(st_29, [
         ]))
    transitions.append(fac.Transition(st_30, [
         ]))
    transitions.append(fac.Transition(st_31, [
         ]))
    transitions.append(fac.Transition(st_32, [
         ]))
    transitions.append(fac.Transition(st_33, [
         ]))
    st_23._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    transitions.append(fac.Transition(st_20, [
         ]))
    transitions.append(fac.Transition(st_21, [
         ]))
    transitions.append(fac.Transition(st_22, [
         ]))
    transitions.append(fac.Transition(st_23, [
         ]))
    transitions.append(fac.Transition(st_24, [
         ]))
    transitions.append(fac.Transition(st_25, [
         ]))
    transitions.append(fac.Transition(st_26, [
         ]))
    transitions.append(fac.Transition(st_27, [
         ]))
    transitions.append(fac.Transition(st_28, [
         ]))
    transitions.append(fac.Transition(st_29, [
         ]))
    transitions.append(fac.Transition(st_30, [
         ]))
    transitions.append(fac.Transition(st_31, [
         ]))
    transitions.append(fac.Transition(st_32, [
         ]))
    transitions.append(fac.Transition(st_33, [
         ]))
    st_24._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    transitions.append(fac.Transition(st_20, [
         ]))
    transitions.append(fac.Transition(st_21, [
         ]))
    transitions.append(fac.Transition(st_22, [
         ]))
    transitions.append(fac.Transition(st_23, [
         ]))
    transitions.append(fac.Transition(st_24, [
         ]))
    transitions.append(fac.Transition(st_25, [
         ]))
    transitions.append(fac.Transition(st_26, [
         ]))
    transitions.append(fac.Transition(st_27, [
         ]))
    transitions.append(fac.Transition(st_28, [
         ]))
    transitions.append(fac.Transition(st_29, [
         ]))
    transitions.append(fac.Transition(st_30, [
         ]))
    transitions.append(fac.Transition(st_31, [
         ]))
    transitions.append(fac.Transition(st_32, [
         ]))
    transitions.append(fac.Transition(st_33, [
         ]))
    st_25._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    transitions.append(fac.Transition(st_20, [
         ]))
    transitions.append(fac.Transition(st_21, [
         ]))
    transitions.append(fac.Transition(st_22, [
         ]))
    transitions.append(fac.Transition(st_23, [
         ]))
    transitions.append(fac.Transition(st_24, [
         ]))
    transitions.append(fac.Transition(st_25, [
         ]))
    transitions.append(fac.Transition(st_26, [
         ]))
    transitions.append(fac.Transition(st_27, [
         ]))
    transitions.append(fac.Transition(st_28, [
         ]))
    transitions.append(fac.Transition(st_29, [
         ]))
    transitions.append(fac.Transition(st_30, [
         ]))
    transitions.append(fac.Transition(st_31, [
         ]))
    transitions.append(fac.Transition(st_32, [
         ]))
    transitions.append(fac.Transition(st_33, [
         ]))
    st_26._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    transitions.append(fac.Transition(st_20, [
         ]))
    transitions.append(fac.Transition(st_21, [
         ]))
    transitions.append(fac.Transition(st_22, [
         ]))
    transitions.append(fac.Transition(st_23, [
         ]))
    transitions.append(fac.Transition(st_24, [
         ]))
    transitions.append(fac.Transition(st_25, [
         ]))
    transitions.append(fac.Transition(st_26, [
         ]))
    transitions.append(fac.Transition(st_27, [
         ]))
    transitions.append(fac.Transition(st_28, [
         ]))
    transitions.append(fac.Transition(st_29, [
         ]))
    transitions.append(fac.Transition(st_30, [
         ]))
    transitions.append(fac.Transition(st_31, [
         ]))
    transitions.append(fac.Transition(st_32, [
         ]))
    transitions.append(fac.Transition(st_33, [
         ]))
    st_27._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    transitions.append(fac.Transition(st_20, [
         ]))
    transitions.append(fac.Transition(st_21, [
         ]))
    transitions.append(fac.Transition(st_22, [
         ]))
    transitions.append(fac.Transition(st_23, [
         ]))
    transitions.append(fac.Transition(st_24, [
         ]))
    transitions.append(fac.Transition(st_25, [
         ]))
    transitions.append(fac.Transition(st_26, [
         ]))
    transitions.append(fac.Transition(st_27, [
         ]))
    transitions.append(fac.Transition(st_28, [
         ]))
    transitions.append(fac.Transition(st_29, [
         ]))
    transitions.append(fac.Transition(st_30, [
         ]))
    transitions.append(fac.Transition(st_31, [
         ]))
    transitions.append(fac.Transition(st_32, [
         ]))
    transitions.append(fac.Transition(st_33, [
         ]))
    st_28._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    transitions.append(fac.Transition(st_20, [
         ]))
    transitions.append(fac.Transition(st_21, [
         ]))
    transitions.append(fac.Transition(st_22, [
         ]))
    transitions.append(fac.Transition(st_23, [
         ]))
    transitions.append(fac.Transition(st_24, [
         ]))
    transitions.append(fac.Transition(st_25, [
         ]))
    transitions.append(fac.Transition(st_26, [
         ]))
    transitions.append(fac.Transition(st_27, [
         ]))
    transitions.append(fac.Transition(st_28, [
         ]))
    transitions.append(fac.Transition(st_29, [
         ]))
    transitions.append(fac.Transition(st_30, [
         ]))
    transitions.append(fac.Transition(st_31, [
         ]))
    transitions.append(fac.Transition(st_32, [
         ]))
    transitions.append(fac.Transition(st_33, [
         ]))
    st_29._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    transitions.append(fac.Transition(st_20, [
         ]))
    transitions.append(fac.Transition(st_21, [
         ]))
    transitions.append(fac.Transition(st_22, [
         ]))
    transitions.append(fac.Transition(st_23, [
         ]))
    transitions.append(fac.Transition(st_24, [
         ]))
    transitions.append(fac.Transition(st_25, [
         ]))
    transitions.append(fac.Transition(st_26, [
         ]))
    transitions.append(fac.Transition(st_27, [
         ]))
    transitions.append(fac.Transition(st_28, [
         ]))
    transitions.append(fac.Transition(st_29, [
         ]))
    transitions.append(fac.Transition(st_30, [
         ]))
    transitions.append(fac.Transition(st_31, [
         ]))
    transitions.append(fac.Transition(st_32, [
         ]))
    transitions.append(fac.Transition(st_33, [
         ]))
    st_30._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    transitions.append(fac.Transition(st_20, [
         ]))
    transitions.append(fac.Transition(st_21, [
         ]))
    transitions.append(fac.Transition(st_22, [
         ]))
    transitions.append(fac.Transition(st_23, [
         ]))
    transitions.append(fac.Transition(st_24, [
         ]))
    transitions.append(fac.Transition(st_25, [
         ]))
    transitions.append(fac.Transition(st_26, [
         ]))
    transitions.append(fac.Transition(st_27, [
         ]))
    transitions.append(fac.Transition(st_28, [
         ]))
    transitions.append(fac.Transition(st_29, [
         ]))
    transitions.append(fac.Transition(st_30, [
         ]))
    transitions.append(fac.Transition(st_31, [
         ]))
    transitions.append(fac.Transition(st_32, [
         ]))
    transitions.append(fac.Transition(st_33, [
         ]))
    st_31._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    transitions.append(fac.Transition(st_20, [
         ]))
    transitions.append(fac.Transition(st_21, [
         ]))
    transitions.append(fac.Transition(st_22, [
         ]))
    transitions.append(fac.Transition(st_23, [
         ]))
    transitions.append(fac.Transition(st_24, [
         ]))
    transitions.append(fac.Transition(st_25, [
         ]))
    transitions.append(fac.Transition(st_26, [
         ]))
    transitions.append(fac.Transition(st_27, [
         ]))
    transitions.append(fac.Transition(st_28, [
         ]))
    transitions.append(fac.Transition(st_29, [
         ]))
    transitions.append(fac.Transition(st_30, [
         ]))
    transitions.append(fac.Transition(st_31, [
         ]))
    transitions.append(fac.Transition(st_32, [
         ]))
    transitions.append(fac.Transition(st_33, [
         ]))
    st_32._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    transitions.append(fac.Transition(st_20, [
         ]))
    transitions.append(fac.Transition(st_21, [
         ]))
    transitions.append(fac.Transition(st_22, [
         ]))
    transitions.append(fac.Transition(st_23, [
         ]))
    transitions.append(fac.Transition(st_24, [
         ]))
    transitions.append(fac.Transition(st_25, [
         ]))
    transitions.append(fac.Transition(st_26, [
         ]))
    transitions.append(fac.Transition(st_27, [
         ]))
    transitions.append(fac.Transition(st_28, [
         ]))
    transitions.append(fac.Transition(st_29, [
         ]))
    transitions.append(fac.Transition(st_30, [
         ]))
    transitions.append(fac.Transition(st_31, [
         ]))
    transitions.append(fac.Transition(st_32, [
         ]))
    transitions.append(fac.Transition(st_33, [
         ]))
    st_33._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_()




def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 220, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None)), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 220, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_3._Automaton = _BuildAutomaton_2()




def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 264, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None)), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 264, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_4._Automaton = _BuildAutomaton_3()




def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 289, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None)), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 289, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_5._Automaton = _BuildAutomaton_4()




def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_6._Automaton = _BuildAutomaton_5()




def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 403, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None)), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 403, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_7._Automaton = _BuildAutomaton_6()




CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'organisation'), textType, scope=CTD_ANON_9, documentation='\n              The organisation to contact for more information about the\n              activity.\n              \n              This is required if content-info is included.\n            ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 495, 8)))

CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'person-name'), textType, scope=CTD_ANON_9, documentation='\n              The name of the contact person at the organisation.\n              \n              If person-name is present then either person-name/text() \n              or job-title/text() must be present\n            ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 505, 8)))

CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'job-title'), textType, scope=CTD_ANON_9, documentation='\n              The job title of the contact person at the organisation.\n              You may repeat this element for different languages.\n              \n              If person-name is present then either person-name/text() \n              or job-title/text() must be present\n            ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 515, 8)))

CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'telephone'), CTD_ANON_10, scope=CTD_ANON_9, documentation='\n              The contact telephone number, if available.  May be\n              repeated for multiple numbers.\n            ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 526, 8)))

CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'email'), plainType, scope=CTD_ANON_9, documentation='\n              The contact email address, if available.  May be\n              repeated for multiple addresses.\n            ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 537, 8)))

CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'mailing-address'), CTD_ANON_11, scope=CTD_ANON_9, documentation='\n              The contact mailing address, if available.\n            ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 545, 8)))

CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'website'), pyxb.binding.datatypes.anyURI, scope=CTD_ANON_9, documentation='\n              The contact web address, if available.  May be repeated\n              for multiple sites.\n            ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 556, 8)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 494, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(None, 'organisation')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 495, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(None, 'person-name')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 505, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(None, 'job-title')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 515, 8))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(None, 'telephone')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 526, 8))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(None, 'email')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 537, 8))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(None, 'mailing-address')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 545, 8))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(None, 'website')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 556, 8))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None)), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 564, 8))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_9._Automaton = _BuildAutomaton_7()




def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_10._Automaton = _BuildAutomaton_8()




def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_11._Automaton = _BuildAutomaton_9()




def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 597, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None)), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 597, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_12._Automaton = _BuildAutomaton_10()




def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 644, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None)), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 644, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_13._Automaton = _BuildAutomaton_11()




CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'value'), currencyType, scope=CTD_ANON_14, documentation='\n              The amount of the contribution (or its value, if in\n              kind).\n            ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 662, 8)))

CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'description'), textType, scope=CTD_ANON_14, documentation='\n              A human-readable description of the transaction.\n            ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 670, 8)))

CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'transaction-type'), codeReqType, scope=CTD_ANON_14, documentation='\n              The type of the transaction (e.g. commitment,\n              disbursement, expenditure, etc.).  The @ref attribute\n              contains a code defined by IATI, and the content is an\n              optional free-text description of the type.\n\n              For the value of the @code attribute, see\n              http://iatistandard.org/codelists/transaction_type\n            ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 677, 8)))

CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'provider-org'), CTD_ANON_15, scope=CTD_ANON_14, documentation='\n              The organisation providing the money for the\n              transaction (if omitted, the provider organisation is\n              the reporting organisation).\n            ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 690, 8)))

CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'receiver-org'), CTD_ANON_16, scope=CTD_ANON_14, documentation='\n              The organisation receiving the money from the\n              transaction (if omitted, then the receiver\n              organisation is the reporting organisation).\n            ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 716, 8)))

CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'transaction-date'), CTD_ANON_17, scope=CTD_ANON_14, documentation='\n              A milestone date for this transaction (such as the\n              decision date, disbursement date, etc.).\n            ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 741, 8)))

CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'flow-type'), codeReqType, scope=CTD_ANON_14, documentation='\n              Optional element to override the top-level\n              default-flow-type element.\n              \n              For the value of the @code attribute, see\n              http://iatistandard.org/codelists/flow_type\n            ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 762, 8)))

CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'finance-type'), codeReqType, scope=CTD_ANON_14, documentation='\n              Optional element to override the top-level\n              default-finance-type element on a\n              transaction-by-transaction basis, if needed.\n\n              For the value of the @code attribute, see\n              http://iatistandard.org/codelists/finance_type\n            ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 773, 8)))

CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'aid-type'), codeReqType, scope=CTD_ANON_14, documentation='\n              Optional element to override the top-level\n              default-aid-type element (debt relief, etc.) on a\n              transaction-by-transaction basis if needed.\n\n              For the value of the @code attribute, see\n              http://iatistandard.org/codelists/aid_type\n            ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 785, 8)))

CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'tied-status'), codeReqType, scope=CTD_ANON_14, documentation='\n              Optional element to override the top-level\n              default-tied-status element (pooled, etc.) on a\n              transaction-by-transaction basis if needed.\n\n              For the value of the @code attribute, see\n              http://iatistandard.org/codelists/tied_status\n            ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 797, 8)))

CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'disbursement-channel'), codeReqType, scope=CTD_ANON_14, documentation='\n              The channel through which the funds will flow for this\n              transaction, from an IATI codelist.\n            ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 809, 8)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(None, 'value')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 662, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 670, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(None, 'transaction-type')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 677, 8))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(None, 'provider-org')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 690, 8))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(None, 'receiver-org')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 716, 8))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(None, 'transaction-date')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 741, 8))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(None, 'flow-type')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 762, 8))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(None, 'finance-type')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 773, 8))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(None, 'aid-type')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 785, 8))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(None, 'tied-status')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 797, 8))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(None, 'disbursement-channel')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 809, 8))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None)), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 817, 8))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    st_11._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_14._Automaton = _BuildAutomaton_12()




def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 700, 14))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None)), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 700, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_15._Automaton = _BuildAutomaton_13()




def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 726, 14))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None)), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 726, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_16._Automaton = _BuildAutomaton_14()




def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 750, 14))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None)), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 750, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_17._Automaton = _BuildAutomaton_15()




CTD_ANON_18._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'location-id'), CTD_ANON_19, scope=CTD_ANON_18, documentation='\n               A unique code describing the location according to a \n               recognised gazetteer or administrative boundary \n               repository. Administrative areas should only be reported\n               here if the location being defined is the administrative\n               area itself. For describing the administrative area/s \n               within which a more specific location falls the \n               location/administrative element should be used. \n            ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 835, 8)))

CTD_ANON_18._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), textType, scope=CTD_ANON_18, documentation='\n              The human-readable name for the location.  May be\n              repeated in different languages.\n            ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 870, 8)))

CTD_ANON_18._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'description'), textType, scope=CTD_ANON_18, documentation='\n              A description that qualifies the location, not the \n              activity.\n            ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 878, 8)))

CTD_ANON_18._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'activity-description'), textType, scope=CTD_ANON_18, documentation='\n              A description that qualifies the activity taking place at \n              the location. This should not duplicate information \n              provided in the main activity description, and should \n              typically be used to distinguish between activities at \n              multiple locations within a single iati-activity record.\n            ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 886, 8)))

CTD_ANON_18._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'administrative'), CTD_ANON_20, scope=CTD_ANON_18, documentation='\n              Coded identification of national and sub-national \n              divisions according to recognised administrative \n              boundary repositories. Multiple levels may be reported.\n            ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 897, 8)))

CTD_ANON_18._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'point'), CTD_ANON_21, scope=CTD_ANON_18, documentation='\n              The point element is based on a subset of the GML 3.3 Point\n              element.\n            ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 975, 8)))

CTD_ANON_18._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'exactness'), CTD_ANON_22, scope=CTD_ANON_18, documentation='\n               Defines whether the location represents the most \n               distinct point reasonably possible for this type of \n               activity or is an approximation due to lack of more \n               detailed information. \n            ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1008, 8)))

CTD_ANON_18._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'location-reach'), codeType, scope=CTD_ANON_18, documentation='\n               Does this location describe where the activity \n               takes place or where the intended beneficiaries reside?\n            ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1032, 8)))

CTD_ANON_18._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'location-class'), CTD_ANON_23, scope=CTD_ANON_18, documentation='\n               Whether the location refers to a structure, a populated \n               place (e.g. city or village), an administrative \n               division, or another topological feature \n               (e.g. river, nature reserve).\n            ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1041, 8)))

CTD_ANON_18._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'feature-designation'), CTD_ANON_24, scope=CTD_ANON_18, documentation='\n               A more refined coded classification of the type of \n               feature referred to by this location.\n            ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1065, 8)))

CTD_ANON_18._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'coordinates'), CTD_ANON_25, scope=CTD_ANON_18, documentation='\n              Deprecated since 1.04\n\n              Geodetic coordinates for the location (latitude, longitude).\n            ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1089, 8)))

CTD_ANON_18._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'gazetteer-entry'), CTD_ANON_26, scope=CTD_ANON_18, documentation="\n              Deprecated since 1.04\n\n              Identifier for this location's entry in a geographical\n              gazetteer, such as GEOnet.  The entry identifier is the\n              element content.\n            ", location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1137, 8)))

CTD_ANON_18._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'location-type'), codeReqType, scope=CTD_ANON_18, documentation='\n              Deprecated since 1.04\n\n              The type of location (e.g. "PCL" for a political entity) \n              from the feature designation codes maintained by the \n              US National Geospatial-Intelligence Agency\n\n              See http://iatistandard.org/codelists/location_type\n            ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1165, 8)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 834, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(None, 'location-id')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 835, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 870, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 878, 8))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(None, 'activity-description')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 886, 8))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(None, 'administrative')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 897, 8))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(None, 'point')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 975, 8))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(None, 'exactness')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1008, 8))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(None, 'location-reach')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1032, 8))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(None, 'location-class')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1041, 8))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(None, 'feature-designation')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1065, 8))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(None, 'coordinates')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1089, 8))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(None, 'gazetteer-entry')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1137, 8))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(None, 'location-type')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1165, 8))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None)), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1178, 8))
    st_13 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_13._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_18._Automaton = _BuildAutomaton_16()




def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 849, 14))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None)), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 849, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_19._Automaton = _BuildAutomaton_17()




def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 906, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None)), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 907, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_20._Automaton = _BuildAutomaton_18()




CTD_ANON_21._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'pos'), pyxb.binding.datatypes.string, scope=CTD_ANON_21, documentation='\n                    The latitude and longitude coordinates in the \n                    format "lat lng"\n                  ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 984, 14)))

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_21._UseForTag(pyxb.namespace.ExpandedName(None, 'pos')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 984, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None)), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 992, 14))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_21._Automaton = _BuildAutomaton_19()




def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1019, 14))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None)), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1019, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_22._Automaton = _BuildAutomaton_20()




def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1052, 14))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None)), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1052, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_23._Automaton = _BuildAutomaton_21()




def _BuildAutomaton_22 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1074, 14))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None)), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1074, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_24._Automaton = _BuildAutomaton_22()




def _BuildAutomaton_23 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1098, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None)), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1099, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_25._Automaton = _BuildAutomaton_23()




def _BuildAutomaton_24 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_24
    del _BuildAutomaton_24
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1148, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None)), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1149, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_26._Automaton = _BuildAutomaton_24()




CTD_ANON_27._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'budget-item'), CTD_ANON_28, scope=CTD_ANON_27, documentation='\n              Identifier for a single item in the recipient-country\n              budget. If more than one identifier is reported the\n              percentage share must be reported and all percentages\n              should add up to 100 percent.\n            ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1216, 8)))

def _BuildAutomaton_25 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_25
    del _BuildAutomaton_25
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1215, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1235, 8))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_27._UseForTag(pyxb.namespace.ExpandedName(None, 'budget-item')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1216, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None)), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1235, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_27._Automaton = _BuildAutomaton_25()




CTD_ANON_28._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'description'), CTD_ANON_47, scope=CTD_ANON_28, documentation='\n        A longer, human-readable description.  May be repeated for\n        different languages.\n      ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 36, 2)))

def _BuildAutomaton_26 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_26
    del _BuildAutomaton_26
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1226, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1228, 14))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_28._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'description')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1227, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None)), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1228, 14))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_28._Automaton = _BuildAutomaton_26()




def _BuildAutomaton_27 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_27
    del _BuildAutomaton_27
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1266, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None)), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1266, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_29._Automaton = _BuildAutomaton_27()




def _BuildAutomaton_28 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_28
    del _BuildAutomaton_28
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1284, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None)), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1284, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_30._Automaton = _BuildAutomaton_28()




CTD_ANON_31._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'indicator'), CTD_ANON_32, scope=CTD_ANON_31, documentation='\n              The indicator(s) that meet the results. There can be\n              multiple indicators for each result.\n            ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1320, 8)))

CTD_ANON_31._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'title'), textType, scope=CTD_ANON_31, documentation='\n        A short, human-readable title.  May be repeated for different\n        languages.\n      ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 27, 2)))

CTD_ANON_31._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'description'), CTD_ANON_47, scope=CTD_ANON_31, documentation='\n        A longer, human-readable description.  May be repeated for\n        different languages.\n      ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 36, 2)))

def _BuildAutomaton_29 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_29
    del _BuildAutomaton_29
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1317, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_31._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'title')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1318, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_31._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'description')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1319, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_31._UseForTag(pyxb.namespace.ExpandedName(None, 'indicator')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1320, 8))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None)), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1450, 8))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_31._Automaton = _BuildAutomaton_29()




CTD_ANON_32._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'baseline'), CTD_ANON_33, scope=CTD_ANON_32, documentation='\n                    The baseline value for the indicator\n                  ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1331, 14)))

CTD_ANON_32._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'period'), CTD_ANON_34, scope=CTD_ANON_32, documentation='\n                    The period covered for the results\n                    reported. Multiple periods can be reported for a\n                    single indicator.\n                  ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1359, 14)))

CTD_ANON_32._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'title'), textType, scope=CTD_ANON_32, documentation='\n        A short, human-readable title.  May be repeated for different\n        languages.\n      ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 27, 2)))

CTD_ANON_32._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'description'), CTD_ANON_47, scope=CTD_ANON_32, documentation='\n        A longer, human-readable description.  May be repeated for\n        different languages.\n      ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 36, 2)))

def _BuildAutomaton_30 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_30
    del _BuildAutomaton_30
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1328, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_32._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'title')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1329, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_32._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'description')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1330, 14))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_32._UseForTag(pyxb.namespace.ExpandedName(None, 'baseline')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1331, 14))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_32._UseForTag(pyxb.namespace.ExpandedName(None, 'period')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1359, 14))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None)), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1428, 14))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_32._Automaton = _BuildAutomaton_30()




CTD_ANON_33._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'comment'), textType, scope=CTD_ANON_33, documentation='\n        A human-readable comment associated with a piece of aid information.\n      ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 53, 2)))

def _BuildAutomaton_31 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_31
    del _BuildAutomaton_31
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1338, 18))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_33._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'comment')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1339, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None)), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1340, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_33._Automaton = _BuildAutomaton_31()




CTD_ANON_34._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'period-start'), dateType, scope=CTD_ANON_34, documentation='\n                          The start of the reporting period\n                        ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1369, 20)))

CTD_ANON_34._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'period-end'), dateType, scope=CTD_ANON_34, documentation='\n                          The end of the reporting period\n                        ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1376, 20)))

CTD_ANON_34._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'target'), CTD_ANON_35, scope=CTD_ANON_34, documentation='\n                          The target milestone for this period\n                        ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1383, 20)))

CTD_ANON_34._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'actual'), CTD_ANON_36, scope=CTD_ANON_34, documentation='\n                          A record of the achieved result for this period.\n                        ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1403, 20)))

def _BuildAutomaton_32 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_32
    del _BuildAutomaton_32
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1368, 18))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_34._UseForTag(pyxb.namespace.ExpandedName(None, 'period-start')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1369, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_34._UseForTag(pyxb.namespace.ExpandedName(None, 'period-end')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1376, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_34._UseForTag(pyxb.namespace.ExpandedName(None, 'target')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1383, 20))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_34._UseForTag(pyxb.namespace.ExpandedName(None, 'actual')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1403, 20))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None)), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1423, 20))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_34._Automaton = _BuildAutomaton_32()




CTD_ANON_35._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'comment'), textType, scope=CTD_ANON_35, documentation='\n        A human-readable comment associated with a piece of aid information.\n      ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 53, 2)))

def _BuildAutomaton_33 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_33
    del _BuildAutomaton_33
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1390, 24))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_35._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'comment')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1391, 26))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None)), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1392, 26))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_35._Automaton = _BuildAutomaton_33()




CTD_ANON_36._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'comment'), textType, scope=CTD_ANON_36, documentation='\n        A human-readable comment associated with a piece of aid information.\n      ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 53, 2)))

def _BuildAutomaton_34 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_34
    del _BuildAutomaton_34
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1410, 24))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_36._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'comment')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1411, 26))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None)), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1412, 26))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_36._Automaton = _BuildAutomaton_34()




def _BuildAutomaton_35 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_35
    del _BuildAutomaton_35
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1473, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None)), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1473, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
indicatorOutcomeType._Automaton = _BuildAutomaton_35()




CTD_ANON_37._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'condition'), CTD_ANON_38, scope=CTD_ANON_37, documentation='\n              Description of one condition attached to the activity.\n            ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1501, 8)))

def _BuildAutomaton_36 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_36
    del _BuildAutomaton_36
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1500, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_37._UseForTag(pyxb.namespace.ExpandedName(None, 'condition')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1501, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None)), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1515, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_37._Automaton = _BuildAutomaton_36()




def _BuildAutomaton_37 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_37
    del _BuildAutomaton_37
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1509, 14))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None)), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1509, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_38._Automaton = _BuildAutomaton_37()




CTD_ANON_39._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'period-start'), dateType, scope=CTD_ANON_39, documentation='\n              The starting date for the budget period, in ISO 8601\n              format (e.g. 2010-04-01 for 1 April 2010).  This element\n              must be present.\n            ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1538, 8)))

CTD_ANON_39._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'period-end'), dateType, scope=CTD_ANON_39, documentation='\n              The ending date for the budget period, in ISO 8601\n              format (e.g. 2011-03-31 for 31 March 2011).  This\n              element must be present.\n            ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1547, 8)))

CTD_ANON_39._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'value'), currencyType, scope=CTD_ANON_39, documentation="\n              The total value of the organisation's aid budget for\n              this period.  This element is required.\n            ", location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1556, 8)))

def _BuildAutomaton_38 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_38
    del _BuildAutomaton_38
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1537, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_39._UseForTag(pyxb.namespace.ExpandedName(None, 'period-start')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1538, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_39._UseForTag(pyxb.namespace.ExpandedName(None, 'period-end')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1547, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_39._UseForTag(pyxb.namespace.ExpandedName(None, 'value')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1556, 8))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None)), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1564, 8))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_39._Automaton = _BuildAutomaton_38()




CTD_ANON_40._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'period-start'), dateType, scope=CTD_ANON_40, documentation='\n              The starting date for the disbursement period, in ISO 8601\n              format (e.g. 2010-04-01 for 1 April 2010).  This element\n              must be present.\n            ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1584, 8)))

CTD_ANON_40._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'period-end'), dateType, scope=CTD_ANON_40, documentation='\n              The ending date for the disbursement period, in ISO 8601\n              format (e.g. 2011-03-31 for 31 March 2011).  This\n              element must be present.\n            ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1593, 8)))

CTD_ANON_40._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'value'), currencyType, scope=CTD_ANON_40, documentation='\n              The amount to be disbursed in the specified currency.\n            ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1602, 8)))

def _BuildAutomaton_39 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_39
    del _BuildAutomaton_39
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1583, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_40._UseForTag(pyxb.namespace.ExpandedName(None, 'period-start')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1584, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_40._UseForTag(pyxb.namespace.ExpandedName(None, 'period-end')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1593, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_40._UseForTag(pyxb.namespace.ExpandedName(None, 'value')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1602, 8))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None)), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1609, 8))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_40._Automaton = _BuildAutomaton_39()




CTD_ANON_41._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'aidtype-flag'), CTD_ANON_42, scope=CTD_ANON_41, documentation='\n              This covers the four CRS++ fields titled: \n              "Free standing technical cooperation"; \n              "Programme-based approach"; \n              "Investment project"; \n              "Associated financing"\n            ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1632, 8)))

CTD_ANON_41._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'loan-terms'), CTD_ANON_43, scope=CTD_ANON_41, documentation='\n              Loan repayment terms and interest rates\n            ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1657, 8)))

CTD_ANON_41._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'loan-status'), CTD_ANON_44, scope=CTD_ANON_41, documentation='\n              The status of loan and interest repayments for the most\n              recently reported financial year\n            ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1736, 8)))

def _BuildAutomaton_40 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_40
    del _BuildAutomaton_40
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1631, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_41._UseForTag(pyxb.namespace.ExpandedName(None, 'aidtype-flag')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1632, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_41._UseForTag(pyxb.namespace.ExpandedName(None, 'loan-terms')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1657, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_41._UseForTag(pyxb.namespace.ExpandedName(None, 'loan-status')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1736, 8))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None)), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1789, 8))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_41._Automaton = _BuildAutomaton_40()




def _BuildAutomaton_41 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_41
    del _BuildAutomaton_41
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1644, 14))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None)), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1644, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_42._Automaton = _BuildAutomaton_41()




CTD_ANON_43._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'repayment-type'), codeType, scope=CTD_ANON_43, documentation='\n                    Type of Repayment. 1 = equal principal payments\n                    (EPP); 2 = annuity; 3 = lump sum; 5 = other,\n                    Codes are listed at\n                    http://iatistandard.org/codelists/crs-repayment-type\n                  ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1665, 14)))

CTD_ANON_43._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'repayment-plan'), codeType, scope=CTD_ANON_43, documentation='\n                    Number of repayments per annum. 1 = annual; 2 =\n                    semi-annual; 4 = quarterly; 12 = monthly. Codes\n                    are listed at\n                    http://iatistandard.org/codelists/repayment-nopa.\n                  ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1675, 14)))

CTD_ANON_43._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'commitment-date'), dateType, scope=CTD_ANON_43, documentation='\n                    Commitment date.The date must be in ISO 8601\n                    format (YYYY-MM-DD).\n                  ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1685, 14)))

CTD_ANON_43._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'repayment-first-date'), dateType, scope=CTD_ANON_43, documentation='\n                    First Repayment Date. The date must be in ISO\n                    8601 format (YYYY-MM-DD).\n                  ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1693, 14)))

CTD_ANON_43._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'repayment-final-date'), dateType, scope=CTD_ANON_43, documentation='\n                    Final Repayment Date. The date must be in ISO\n                    8601 format (YYYY-MM-DD).\n                  ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1701, 14)))

def _BuildAutomaton_42 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_42
    del _BuildAutomaton_42
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1664, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_43._UseForTag(pyxb.namespace.ExpandedName(None, 'repayment-type')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1665, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_43._UseForTag(pyxb.namespace.ExpandedName(None, 'repayment-plan')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1675, 14))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_43._UseForTag(pyxb.namespace.ExpandedName(None, 'commitment-date')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1685, 14))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_43._UseForTag(pyxb.namespace.ExpandedName(None, 'repayment-first-date')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1693, 14))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_43._UseForTag(pyxb.namespace.ExpandedName(None, 'repayment-final-date')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1701, 14))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None)), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1709, 14))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_43._Automaton = _BuildAutomaton_42()




CTD_ANON_44._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'interest-received'), pyxb.binding.datatypes.decimal, scope=CTD_ANON_44, documentation='\n                    Interest received during the reporting year\n                  ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1745, 14)))

CTD_ANON_44._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'principal-outstanding'), pyxb.binding.datatypes.decimal, scope=CTD_ANON_44, documentation='\n                    The amount of principal owed on the loan at the\n                    end of the reporting year.\n                  ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1752, 14)))

CTD_ANON_44._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'principal-arrears'), pyxb.binding.datatypes.decimal, scope=CTD_ANON_44, documentation='\n                    Arrears of principal at the end of the\n                    year. Included in principal-outstanding\n                  ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1760, 14)))

CTD_ANON_44._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'interest-arrears'), pyxb.binding.datatypes.decimal, scope=CTD_ANON_44, documentation='\n                    Arrears of interest at the end of the year\n                  ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1768, 14)))

def _BuildAutomaton_43 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_43
    del _BuildAutomaton_43
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1744, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_44._UseForTag(pyxb.namespace.ExpandedName(None, 'interest-received')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1745, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_44._UseForTag(pyxb.namespace.ExpandedName(None, 'principal-outstanding')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1752, 14))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_44._UseForTag(pyxb.namespace.ExpandedName(None, 'principal-arrears')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1760, 14))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_44._UseForTag(pyxb.namespace.ExpandedName(None, 'interest-arrears')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1768, 14))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None)), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1775, 14))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_44._Automaton = _BuildAutomaton_43()




CTD_ANON_45._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'forecast'), CTD_ANON_46, scope=CTD_ANON_45, documentation='\n              A container to hold separate forecasts for each of\n              the years specified\n            ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1804, 8)))

def _BuildAutomaton_44 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_44
    del _BuildAutomaton_44
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1803, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_45._UseForTag(pyxb.namespace.ExpandedName(None, 'forecast')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1804, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None)), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-activities-schema.xsd', 1828, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_45._Automaton = _BuildAutomaton_44()




def _BuildAutomaton_45 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_45
    del _BuildAutomaton_45
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 45, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None)), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 45, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_47._Automaton = _BuildAutomaton_45()




def _BuildAutomaton_46 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_46
    del _BuildAutomaton_46
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_48._Automaton = _BuildAutomaton_46()




def _BuildAutomaton_47 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_47
    del _BuildAutomaton_47
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 102, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None)), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 102, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_49._Automaton = _BuildAutomaton_47()




CTD_ANON_50._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'title'), textType, scope=CTD_ANON_50, documentation='\n        A short, human-readable title.  May be repeated for different\n        languages.\n      ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 27, 2)))

CTD_ANON_50._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'category'), codeReqType, scope=CTD_ANON_50, documentation='\n              IATI Document Category Code\n\n              For the value of the @code attribute, see\n              http://iatistandard.org/codelists/document_category\n            ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 128, 8)))

CTD_ANON_50._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'language'), codeType, scope=CTD_ANON_50, documentation='\n                The ISO 639 language code for the target document, e.g. "en".\n           ', location=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 138, 8)))

def _BuildAutomaton_48 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_48
    del _BuildAutomaton_48
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_50._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'title')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 127, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_50._UseForTag(pyxb.namespace.ExpandedName(None, 'category')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 128, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_50._UseForTag(pyxb.namespace.ExpandedName(None, 'language')), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 138, 8))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None)), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 145, 8))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_50._Automaton = _BuildAutomaton_48()




def _BuildAutomaton_49 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_49
    del _BuildAutomaton_49
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)
plainType._Automaton = _BuildAutomaton_49()




def _BuildAutomaton_50 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_50
    del _BuildAutomaton_50
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 267, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None)), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 267, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
textType._Automaton = _BuildAutomaton_50()




def _BuildAutomaton_51 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_51
    del _BuildAutomaton_51
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 282, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None)), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 282, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
codeType._Automaton = _BuildAutomaton_51()




def _BuildAutomaton_52 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_52
    del _BuildAutomaton_52
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 297, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None)), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 297, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
codeReqType._Automaton = _BuildAutomaton_52()




def _BuildAutomaton_53 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_53
    del _BuildAutomaton_53
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 313, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None)), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 313, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
refType._Automaton = _BuildAutomaton_53()




def _BuildAutomaton_54 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_54
    del _BuildAutomaton_54
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 330, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None)), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 330, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
refReqType._Automaton = _BuildAutomaton_54()




def _BuildAutomaton_55 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_55
    del _BuildAutomaton_55
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 360, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None)), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 360, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
dateType._Automaton = _BuildAutomaton_55()




def _BuildAutomaton_56 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_56
    del _BuildAutomaton_56
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 379, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None)), pyxb.utils.utility.Location('/home/daan/zimmerman/datapool/python_test/iati-common.xsd', 379, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
dateReqType._Automaton = _BuildAutomaton_56()

